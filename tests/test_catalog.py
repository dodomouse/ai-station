import contextlib
from datetime import datetime, timedelta, timezone
import importlib.util
import io
import json
from pathlib import Path
import shutil
import tempfile
import unittest


ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("catalog", ROOT / "scripts/catalog.py")
catalog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(catalog)
NOW = datetime(2026, 11, 15, tzinfo=timezone.utc)


class CatalogTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        for name in ("config", "templates"):
            shutil.copytree(ROOT / name, self.root / name)
        (self.root / "tools").mkdir()
        (self.root / "data/github").mkdir(parents=True)

    def save(self, path, data):
        path.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")

    def fixture(self):
        directory = catalog.new_entry(self.root, "sample", "example/sample")
        data = catalog.read_json(directory / "tool.json")
        data.update(name="Sample", repo_node_id="R_example", category="productivity", platforms=["linux"],
                    summary={"zh-CN": "同步本地文件", "en": "Synchronize local files"},
                    aliases={"zh-CN": ["文件同步助手"], "en": ["File helper"]},
                    use_cases={"zh-CN": ["备份文件"], "en": ["Back up files"]})
        data["editorial"] = {"status": "reviewed", "reviewed_at": {k: catalog.iso(NOW) for k in catalog.LOCALES}, "verification_level": "docs"}
        data["license_review"] = {"spdx": "MIT", "osi_approved": True, "license_sha256": "a" * 64,
                                  "source_url": "https://github.com/example/sample/blob/main/LICENSE", "reviewed_at": catalog.iso(NOW)}
        data["activity_evidence"] = [{"type": "commit", "occurred_at": "2026-08-15T00:00:00Z", "reviewed_at": catalog.iso(NOW),
                                      "url": "https://github.com/example/sample/commit/abc", "reason": {"zh-CN": "修复同步错误", "en": "Fixes synchronization"}, "qualifies": True}]
        data["sources"] = [{"url": "https://github.com/example/sample", "accessed_at": catalog.iso(NOW), "supports": {"zh-CN": "功能说明", "en": "Feature description"}}]
        self.save(directory / "tool.json", data)
        for locale in catalog.LOCALES:
            (directory / f"README.{locale}.md").write_text("# Sample\n\nDocumented file synchronization.\n", encoding="utf-8")
        snapshot = {"schema_version": 1, "repo_node_id": "R_example", "full_name": "example/sample", "stargazers_count": 1000,
                    "archived": False, "disabled": False, "visibility": "public", "license_spdx": "MIT", "license_sha256": "a" * 64, "last_success_at": catalog.iso(NOW)}
        self.save(self.root / "data/github/sample.json", snapshot)
        return directory, data, snapshot

    def state(self):
        policy, _, entries = catalog.load(self.root)
        return catalog.eligibility(entries[0], policy, NOW)

    def test_empty_catalog_builds_and_searches(self):
        self.assertEqual(catalog.build(self.root, NOW), 0)
        self.assertIn("暂无", (self.root / "indexes/README.md").read_text())
        self.assertIn("No entries", (self.root / "indexes/README.en.md").read_text())
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            self.assertEqual(catalog.main(["--root", str(self.root), "search", "--lang", "en", "--json"]), 0)
        self.assertEqual(json.loads(output.getvalue())["results"], [])

    def test_new_creates_two_languages_and_no_eligible_entry(self):
        path = catalog.new_entry(self.root, "demo", "example/demo")
        self.assertTrue((path / "README.zh-CN.md").exists())
        self.assertTrue((path / "README.en.md").exists())
        self.assertEqual(self.state()["status"], "unknown")

    def test_new_refuses_duplicate_and_traversal(self):
        catalog.new_entry(self.root, "demo", "example/demo")
        for identifier, repository in [("demo", "example/other"), ("other", "EXAMPLE/DEMO"), ("../outside", "example/outside")]:
            with self.subTest(identifier=identifier), self.assertRaises(catalog.CatalogError):
                catalog.new_entry(self.root, identifier, repository)

    def test_star_boundary(self):
        _, _, snapshot = self.fixture()
        self.assertEqual(self.state()["status"], "eligible")
        snapshot["stargazers_count"] = 999
        self.save(self.root / "data/github/sample.json", snapshot)
        self.assertEqual(self.state(), {"status": "ineligible", "reasons": ["below_star_threshold"]})

    def test_calendar_month_clamping_and_timezones(self):
        self.assertEqual(catalog.months_before(datetime(2024, 5, 31, 12, tzinfo=timezone.utc), 3).isoformat(), "2024-02-29T12:00:00+00:00")
        self.assertEqual(catalog.months_before(datetime(2025, 5, 31, tzinfo=timezone.utc), 3).day, 28)
        self.assertEqual(catalog.timestamp("2026-11-15T08:00:00+08:00"), NOW)
        with self.assertRaises(catalog.CatalogError):
            catalog.timestamp("2026-11-15")

    def test_activity_boundary_and_unqualified_changes(self):
        directory, data, _ = self.fixture()
        for date, qualifies, expected in [("2026-08-15T00:00:00Z", True, "eligible"),
                                           ("2026-08-14T23:59:59Z", True, "needs_review"),
                                           ("2026-11-14T00:00:00Z", False, "needs_review")]:
            with self.subTest(date=date, qualifies=qualifies):
                data["activity_evidence"][0].update(occurred_at=date, qualifies=qualifies)
                self.save(directory / "tool.json", data)
                self.assertEqual(self.state()["status"], expected)

    def test_snapshot_age_and_future_snapshot(self):
        _, _, snapshot = self.fixture()
        for delta, expected in [(timedelta(days=7), "eligible"), (timedelta(days=7, seconds=1), "unknown"), (timedelta(seconds=-1), "unknown")]:
            with self.subTest(delta=delta):
                snapshot["last_success_at"] = catalog.iso(NOW - delta)
                self.save(self.root / "data/github/sample.json", snapshot)
                self.assertEqual(self.state()["status"], expected)

    def test_archived_disabled_and_private(self):
        _, _, base = self.fixture()
        for key, value in [("archived", True), ("disabled", True), ("visibility", "private")]:
            with self.subTest(key=key):
                self.save(self.root / "data/github/sample.json", {**base, key: value})
                self.assertEqual(self.state()["status"], "ineligible")

    def test_identity_and_license_changes_require_review(self):
        _, _, base = self.fixture()
        for key, value in [("repo_node_id", "R_new"), ("full_name", "new/sample"), ("license_spdx", "Apache-2.0"), ("license_sha256", "b" * 64), ("license_spdx", None)]:
            with self.subTest(key=key):
                self.save(self.root / "data/github/sample.json", {**base, key: value})
                self.assertEqual(self.state()["status"], "unknown")

    def test_missing_snapshot_and_null_count_remain_unknown(self):
        _, _, snapshot = self.fixture()
        snapshot["stargazers_count"] = None
        path = self.root / "data/github/sample.json"
        self.save(path, snapshot)
        self.assertEqual(self.state()["status"], "unknown")
        path.unlink()
        self.assertEqual(self.state()["status"], "unknown")

    def test_reviewed_entry_requires_both_languages(self):
        directory, data, _ = self.fixture()
        data["summary"]["en"] = ""
        self.save(directory / "tool.json", data)
        with self.assertRaises(catalog.CatalogError):
            catalog.load(self.root)

    def test_missing_translation_document_is_invalid_even_for_draft(self):
        path = catalog.new_entry(self.root, "demo", "example/demo")
        (path / "README.en.md").unlink()
        with self.assertRaises(catalog.CatalogError):
            catalog.load(self.root)

    def test_placeholders_cannot_be_reviewed(self):
        directory, _, _ = self.fixture()
        (directory / "README.en.md").write_text("{{Describe the tool.}}")
        with self.assertRaises(catalog.CatalogError):
            catalog.load(self.root)

    def test_bad_references_and_duplicate_repository_identity(self):
        directory, data, _ = self.fixture()
        data["alternatives"] = ["missing"]
        self.save(directory / "tool.json", data)
        with self.assertRaises(catalog.CatalogError):
            catalog.load(self.root)
        data["alternatives"] = []
        self.save(directory / "tool.json", data)
        other = catalog.new_entry(self.root, "other", "example/other")
        second = catalog.read_json(other / "tool.json")
        second["repo_node_id"] = data["repo_node_id"]
        self.save(other / "tool.json", second)
        with self.assertRaises(catalog.CatalogError):
            catalog.load(self.root)

    def test_orphan_snapshot_is_invalid(self):
        self.save(self.root / "data/github/orphan.json", {})
        with self.assertRaises(catalog.CatalogError):
            catalog.load(self.root)

    def test_duplicate_json_keys_are_rejected(self):
        path = self.root / "duplicate.json"
        path.write_text('{"id": "first", "id": "second"}')
        with self.assertRaises(catalog.CatalogError):
            catalog.read_json(path)

    def test_invalid_version_and_license_hash_are_rejected(self):
        directory, data, snapshot = self.fixture()
        data["schema_version"] = True
        self.save(directory / "tool.json", data)
        with self.assertRaises(catalog.CatalogError):
            catalog.load(self.root)
        data["schema_version"] = 1
        data["license_review"]["license_sha256"] = "not-a-sha256"
        self.save(directory / "tool.json", data)
        with self.assertRaises(catalog.CatalogError):
            catalog.load(self.root)

    def test_bilingual_search_and_filters(self):
        self.fixture()
        policy, taxonomy, entries = catalog.load(self.root)
        for query in ("备份", "FILE HELPER", "local files", "文件同步助手"):
            with self.subTest(query=query):
                self.assertEqual(len(catalog.search(entries, policy, taxonomy, NOW, query)), 1)
        self.assertEqual(catalog.search(entries, policy, taxonomy, NOW, "missing"), [])
        self.assertEqual(catalog.search(entries, policy, taxonomy, NOW, platform="windows"), [])
        self.assertEqual(catalog.search(entries, policy, taxonomy, NOW, category="ai"), [])

    def test_drafts_are_opt_in(self):
        directory = catalog.new_entry(self.root, "demo", "example/demo")
        policy, taxonomy, entries = catalog.load(self.root)
        self.assertEqual(catalog.search(entries, policy, taxonomy, NOW, "demo"), [])
        self.assertEqual(len(catalog.search(entries, policy, taxonomy, NOW, "demo", True)), 1)

    def test_build_is_reproducible_and_invalid_input_preserves_output(self):
        directory, data, _ = self.fixture()
        catalog.build(self.root, NOW)
        paths = [self.root / "dist/catalog.json", self.root / "indexes/README.md", self.root / "indexes/README.en.md"]
        before = {path: path.read_bytes() for path in paths}
        catalog.build(self.root, NOW)
        self.assertEqual(before, {path: path.read_bytes() for path in paths})
        self.assertIn("同步本地文件", paths[1].read_text())
        self.assertIn("Synchronize local files", paths[2].read_text())
        data["category"] = "invalid"
        self.save(directory / "tool.json", data)
        with self.assertRaises(catalog.CatalogError):
            catalog.build(self.root, NOW)
        self.assertEqual(before, {path: path.read_bytes() for path in paths})

    def test_cli_reports_validation_errors_without_traceback(self):
        self.fixture()
        stream = io.StringIO()
        with contextlib.redirect_stderr(stream):
            result = catalog.main(["--root", str(self.root), "search", "--category", "missing"])
        self.assertEqual(result, 1)
        self.assertIn("Unknown category", stream.getvalue())


if __name__ == "__main__":
    unittest.main()
