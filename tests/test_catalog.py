"""Exercise failure modes with small, isolated Markdown catalogs."""

import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("check_catalog", REPO / "scripts/check_catalog.py")
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)


class CatalogChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "docs").mkdir()
        self.data = {
            "evaluated_at": "2026-11-16T00:00:00Z",
            "eligibility": {"status": "eligible", "reasons": []},
            "metadata": {
                "id": "example", "name": "Example", "repository": "owner/example",
                "repo_node_id": "R_example", "category": "ai",
                "summary": {"zh-CN": "示例", "en": "Example"},
                "license_review": {"spdx": "MIT", "osi_approved": True,
                    "source_url": "https://github.com/owner/example/blob/" + "a" * 40 + "/LICENSE",
                    "license_sha256": "b" * 64},
                "activity_evidence": [{"qualifies": True,
                    "url": "https://github.com/owner/example/commit/" + "c" * 40,
                    "occurred_at": "2026-11-15T00:00:00Z", "reviewed_at": "2026-11-16T00:00:00Z",
                    "reason": {"zh-CN": "修复输入解析错误。", "en": "Fixes input parsing."}}],
            },
            "snapshot": {"full_name": "owner/example", "repo_node_id": "R_example", "stargazers_count": 8,
                "archived": False, "disabled": False, "visibility": "public", "last_success_at": "2026-11-16T00:00:00Z"},
        }
        self.write_entry()
        for name in ("README.md", "README.en.md"):
            (self.root / name).write_text('''# Catalog
![Included](https://img.shields.io/badge/included-1-blue)
![Candidates](https://img.shields.io/badge/candidates-0-blue)
![Categories](https://img.shields.io/badge/categories-1-blue)
| [AI tools](#included-ai) | Models | [1](#included-ai) | 0 |
<a id="included"></a>
## Included (1)
<a id="included-ai"></a>
<details>
<summary>AI tools · 1 projects</summary>
| [Example](docs/example.md#english) | Purpose | AI tools | 8 |
</details>
<a id="candidates"></a>
## Candidates (0)
''', encoding="utf-8")
        self.change("README.md", "docs/example.md#english", "docs/example.md#中文")

    def write_entry(self, data=None, name="example"):
        data = data or self.data
        (self.root / "docs" / (name + ".md")).write_text('''# Example
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 8 |
| 评估时间 / Evaluated at | 2026-11-16T00:00:00Z |
## 中文
示例。
## English
Example. [Evidence](#review-evidence)
## Review evidence
<details>
<summary>Evidence</summary>

```json
''' + json.dumps(data, ensure_ascii=False, indent=2) + '\n```\n</details>\n', encoding="utf-8")

    def change(self, path, old, new):
        file = self.root / path
        text = file.read_text(encoding="utf-8")
        self.assertIn(old, text)
        file.write_text(text.replace(old, new), encoding="utf-8")

    def assert_error(self, fragment):
        self.assertTrue(any(fragment in e for e in CHECK.check_catalog(self.root)), fragment)

    def test_valid_fixture_and_read_only(self):
        before = {p: p.read_bytes() for p in self.root.rglob("*.md")}
        self.assertEqual([], CHECK.check_catalog(self.root))
        self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob("*.md")})

    def test_broken_path_and_anchor(self):
        self.change("README.md", "docs/example.md#中文", "docs/missing.md#english")
        self.assert_error("broken local link")
        self.change("README.md", "docs/missing.md#english", "docs/example.md#missing")
        self.assert_error("missing local anchor")

    def test_counts_stars_and_status_drift(self):
        self.change("README.md", "included-1-blue", "included-2-blue")
        self.assert_error("badge count")
        self.change("README.md", "AI tools | 8", "AI tools | 9")
        self.assert_error("index Stars")
        self.change("docs/example.md", "已收录 / Included", "候选 / Candidate")
        self.assert_error("status header")
        self.change("README.en.md", 'id="included-ai"', 'id="candidate-ai"')
        self.assert_error("index status/category")

    def test_duplicate_repository(self):
        other = copy.deepcopy(self.data)
        other["metadata"]["id"] = "other"
        self.write_entry(other, "other")
        self.assert_error("duplicate repo")

    def test_unpinned_license_and_content_scope(self):
        license_review = self.data["metadata"]["license_review"]
        license_review["source_url"] = "https://github.com/owner/example/blob/main/LICENSE"
        license_review["spdx"] = "MIT AND CC-BY-SA-4.0"
        self.write_entry()
        self.assert_error("license source_url must pin")
        self.assert_error("OSI flag cannot cover content")

    def test_missing_license_needs_candidate_action(self):
        self.data["metadata"]["license_review"]["source_url"] = None
        self.write_entry()
        self.assert_error("license source_url must pin")
        self.data["eligibility"] = {"status": "unknown", "reasons": ["license_needs_review"],
            "pending_actions": {"zh-CN": ["核对许可"], "en": ["Review license"]}}
        self.write_entry()
        self.assertFalse(any("license source_url must pin" in e for e in CHECK.check_catalog(self.root)))

    def test_generic_activity_and_missing_activity(self):
        self.data["metadata"]["activity_evidence"][0]["reason"]["zh-CN"] = "已核对正式发行 v1 的发布状态与时间。"
        self.write_entry()
        self.assert_error("substantive changes")
        self.data["metadata"]["activity_evidence"] = []
        self.write_entry()
        self.assert_error("requires qualifying activity")

    def test_missing_and_wrong_type_fields_do_not_crash(self):
        for key, replacement in (("metadata", []), ("snapshot", "wrong"), ("eligibility", None)):
            with self.subTest(key=key):
                data = copy.deepcopy(self.data)
                data[key] = replacement
                self.write_entry(data)
                self.assert_error(key + " must be dict")

    def test_reject_boolean_stars_and_duplicate_json_keys(self):
        self.data["snapshot"]["stargazers_count"] = True
        self.write_entry()
        self.assert_error("stargazers_count must be int")
        self.change("docs/example.md", '"status": "eligible",', '"status": "eligible", "status": "unknown",')
        self.assert_error("duplicate JSON key")

    def test_current_threshold_rejected_but_history_allowed(self):
        self.data["eligibility_history"] = [{"status": "ineligible", "reasons": ["below_star_threshold"]}]
        self.write_entry()
        self.assertEqual([], CHECK.check_catalog(self.root))
        self.data["eligibility"]["reasons"] = ["below_star_threshold"]
        self.write_entry()
        self.assert_error("cannot be a current eligibility reason")

    def test_evidence_fold_required(self):
        self.change("docs/example.md", "<details>", "")
        self.assert_error("details block")

    def test_component_license_and_implementation_evidence(self):
        component = copy.deepcopy(self.data["metadata"]["license_review"])
        component.update(scope="illustrations", spdx="CC-BY-SA-4.0")
        self.data["metadata"]["license_review"]["components"] = [component]
        self.data["metadata"]["activity_evidence"][0]["implementation_evidence"] = {"sha": "a" * 40,
            "url": "https://github.com/owner/example/commit/" + "b" * 40, "reviewed_files": []}
        self.write_entry()
        self.assert_error("component OSI flag")
        self.assert_error("matching repository commit SHA")
        self.assert_error("requires reviewed files")

    def test_navigation_and_language_target(self):
        self.change("README.en.md", "docs/example.md#english", "docs/example.md#中文")
        self.assert_error("entry link must target english")
        self.change("README.md", "| [1](#included-ai) | 0 |", "| [2](#included-ai) | 0 |")
        self.assert_error("navigation count")
        self.change("README.md", "| [AI tools](#included-ai) |", "| AI tools |")
        self.assert_error("navigation must contain category")

    def test_candidate_reason_drift(self):
        self.data["eligibility"] = {"status": "unknown", "reasons": ["license_needs_review"]}
        self.write_entry()
        self.change("docs/example.md", "## 中文", "候选原因：待复核。\nCandidate reason: Review needed.\n## 中文")
        self.assert_error("candidate reason differs")

    def test_short_index_row_returns_error(self):
        self.change("README.md", " | Purpose | AI tools | 8 |", " |")
        self.assert_error("index row requires at least four columns")

    def test_license_repository_binding_and_snapshot_digest(self):
        license_review = self.data["metadata"]["license_review"]
        license_review["source_url"] = license_review["source_url"].replace("owner/example", "unrelated/repository")
        license_review["evidence_status"] = "hash_matched"
        self.data["snapshot"]["license_sha256"] = "d" * 64
        self.write_entry()
        self.assert_error("license source repository differs")
        self.assert_error("hash-matched license evidence differs")

    def test_timestamp_validation_and_snapshot_window(self):
        for value, expected in (("not-a-date", "ISO timestamp"),
                ("2026-11-16T00:00:00", "ISO timestamp"),
                ("2026-11-08T23:59:59Z", "no more than 7 days"),
                ("2026-11-17T00:00:00Z", "no more than 7 days")):
            with self.subTest(value=value):
                self.data["snapshot"]["last_success_at"] = value
                self.write_entry()
                self.assert_error(expected)
        self.data["snapshot"]["last_success_at"] = "2026-11-09T00:00:00Z"
        self.write_entry()
        self.assertEqual([], CHECK.check_catalog(self.root))

    def test_activity_calendar_window_and_later_review(self):
        activity = self.data["metadata"]["activity_evidence"][0]
        for value in ("2020-01-01T00:00:00Z", "2026-11-17T00:00:00Z"):
            with self.subTest(value=value):
                activity["occurred_at"] = value
                self.write_entry()
                self.assert_error("three-calendar-month evaluation window")
        activity["occurred_at"] = "2026-08-16T00:00:00Z"
        activity["reviewed_at"] = "2026-11-17T00:00:00Z"
        self.write_entry()
        self.assertEqual([], CHECK.check_catalog(self.root))

    def test_calendar_month_boundary_clamps_to_month_end(self):
        self.data["evaluated_at"] = "2025-05-31T00:00:00Z"
        self.data["snapshot"]["last_success_at"] = "2025-05-31T00:00:00Z"
        activity = self.data["metadata"]["activity_evidence"][0]
        activity.update(occurred_at="2025-02-28T00:00:00Z", reviewed_at="2025-06-01T00:00:00Z")
        self.write_entry()
        self.change("docs/example.md", "| 2026-11-16T00:00:00Z |", "| 2025-05-31T00:00:00Z |")
        self.assertEqual([], CHECK.check_catalog(self.root))

    def test_real_repository(self):
        self.assertEqual([], CHECK.check_catalog(REPO))


if __name__ == "__main__":
    unittest.main()
