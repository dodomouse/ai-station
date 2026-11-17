"""Regression checks using isolated, offline catalogs and explicit evidence."""

import copy
from datetime import datetime, timezone
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("check_catalog", REPO / "scripts/check_catalog.py")
CHECK = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(CHECK)
NOW = datetime(2026, 11, 17, 12, tzinfo=timezone.utc)


class CatalogChecks(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / "docs").mkdir()
        self.policy = {**CHECK.POLICY, "legacy_admissions": []}
        self.data = {
            "evaluated_at": "2026-11-16T00:00:00Z",
            "eligibility": {"status": "eligible", "reasons": []},
            "metadata": {
                "id": "example", "name": "Example", "repository": "owner/example",
                "repo_node_id": "R_example", "category": "ai",
                "summary": {"zh-CN": "示例", "en": "Example"},
                "ai_task_relevance": {"supports_ai_tasks": True,
                    "reason": {"zh-CN": "为智能体提供查询接口。", "en": "Provides a query interface for agents."},
                    "source_url": "https://github.com/owner/example#readme"},
                "activity_evidence": [{"type": "commit", "qualifies": True,
                    "url": "https://github.com/owner/example/commit/" + "c" * 40,
                    "occurred_at": "2026-11-15T00:00:00Z",
                    "reason": {"zh-CN": "机器人更新了文档链接。", "en": "A bot updated documentation links."}}],
            },
            "snapshot": {"full_name": "owner/example", "repo_node_id": "R_example", "stargazers_count": 1000,
                "archived": False, "disabled": False, "visibility": "public", "last_success_at": "2026-11-16T00:00:00Z"},
        }
        self.write_catalog()

    def write_catalog(self, records=None):
        records = records if records is not None else [self.data]
        for path in (self.root / "docs").glob("*.md"):
            path.unlink()
        for index, data in enumerate(records):
            metadata = data.get("metadata") if isinstance(data.get("metadata"), dict) else {}
            snapshot = data.get("snapshot") if isinstance(data.get("snapshot"), dict) else {}
            name = metadata.get("id", "example" if index == 0 else "other")
            stars = snapshot.get("stargazers_count", 1000)
            evaluated = data.get("evaluated_at", "")
            text = f"""# Example
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | {stars} |
| 评估时间 / Evaluated at | {evaluated} |
## 中文
示例。
## English
Example. [Evidence](#review-evidence)
## Review evidence
<details>
<summary>Evidence</summary>

```json
{json.dumps(data, ensure_ascii=False, indent=2)}
```
</details>
"""
            (self.root / "docs" / (name + ".md")).write_text(text, encoding="utf-8")
        for name in ("README.md", "README.en.md"):
            anchor = "english" if name == "README.en.md" else "中文"
            count = len(records)
            text = f"""# Catalog
The catalog contains {count} projects.
![Included](https://img.shields.io/badge/included-{count}-blue)
![Categories](https://img.shields.io/badge/categories-1-blue)
| [AI tools](#included-ai) | Models | [{count}](#included-ai) |
<a id="included"></a>

## Included ({count})
<a id="included-ai"></a>
<details>
<summary>AI tools · {count} projects</summary>
"""
            for index, data in enumerate(records):
                metadata = data.get("metadata") if isinstance(data.get("metadata"), dict) else {}
                snapshot = data.get("snapshot") if isinstance(data.get("snapshot"), dict) else {}
                entry = metadata.get("id", "example" if index == 0 else "other")
                text += f"| [Example](docs/{entry}.md#{anchor}) | Purpose | AI tools | {snapshot.get('stargazers_count', 1000)} |\n"
            (self.root / name).write_text(text + "</details>\n", encoding="utf-8")
        (self.root / "catalog-policy.json").write_text(json.dumps(self.policy), encoding="utf-8")

    def change(self, path, old, new):
        file = self.root / path
        text = file.read_text(encoding="utf-8")
        self.assertIn(old, text)
        file.write_text(text.replace(old, new), encoding="utf-8")

    def errors(self):
        return CHECK.check_catalog(self.root, now=NOW)

    def assert_error(self, fragment):
        errors = self.errors()
        self.assertTrue(any(fragment in e for e in errors), (fragment, errors))

    def assert_valid(self):
        self.assertEqual([], self.errors())

    def growth(self, start=499, end=999, start_at="2026-10-16T00:00:00Z", end_at="2026-11-16T00:00:00Z"):
        self.data["snapshot"]["stargazers_count"] = end
        self.data["metadata"]["star_growth_evidence"] = {
            "start_at": start_at, "end_at": end_at, "start_stars": start, "end_stars": end,
            "source_url": "https://api.github.com/repos/owner/example",
            "baseline_source_url": "https://example.org/snapshots/owner-example-2026-10-16.json",
        }

    def make_legacy(self):
        self.policy["legacy_admissions"] = [{k: self.data["metadata"][k] for k in ("id", "repository", "repo_node_id")}]
        self.policy["legacy_admissions"][0]["baseline_evaluated_at"] = self.data["evaluated_at"]
        self.data["metadata"].pop("ai_task_relevance")
        self.data["metadata"]["activity_evidence"] = []
        self.data["snapshot"]["stargazers_count"] = 2

    def test_legacy_reassessment_must_meet_current_policy(self):
        original = copy.deepcopy(self.data)
        self.make_legacy()
        self.data["evaluated_at"] = "2026-11-17T00:00:00Z"
        self.write_catalog()
        self.assert_error("ai_task_relevance must be dict")
        self.assert_error("1000 Stars or qualifying monthly growth")
        self.assert_error("requires recent activity evidence")
        self.assertFalse(any("legacy admission identity mismatch" in error for error in self.errors()))
        self.data["metadata"] = original["metadata"]
        self.data["snapshot"]["stargazers_count"] = 1000
        self.write_catalog()
        self.assert_valid()

    def test_legacy_baseline_is_required_and_must_be_valid(self):
        self.make_legacy()
        baseline = self.policy["legacy_admissions"][0]
        for value in [None, True, "not-a-date", "2026-11-16T00:00:00", "2027-01-01T00:00:00Z"]:
            with self.subTest(value=value):
                baseline["baseline_evaluated_at"] = value
                self.write_catalog()
                self.assert_error("baseline_evaluated_at")

    def test_valid_unlicensed_entry_is_read_only(self):
        before = {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()}
        self.assert_valid()
        self.assertEqual(before, {p: p.read_bytes() for p in self.root.rglob("*") if p.is_file()})

    def test_license_fields_are_not_admission_requirements(self):
        self.data["metadata"]["license_review"] = {"osi_approved": False, "spdx": "LicenseRef-Proprietary", "source_url": None}
        self.data["snapshot"]["license_sha256"] = "not-a-digest"
        self.write_catalog()
        self.assert_valid()

    def test_total_star_boundary(self):
        self.assert_valid()  # Exactly 1000 does not need a growth record.
        self.data["snapshot"]["stargazers_count"] = 999
        self.write_catalog()
        self.assert_error("1000 Stars or qualifying monthly growth")

    def test_growth_boundary(self):
        self.growth(499, 999)
        self.write_catalog()
        self.assert_valid()  # Exactly 500 net new Stars.
        self.growth(500, 999)
        self.write_catalog()
        self.assert_error("at least 500 net Stars")

    def test_growth_has_exact_snapshot_and_calendar_binding(self):
        self.growth()
        good = copy.deepcopy(self.data)
        cases = [("end_at", "2026-11-15T00:00:00Z", "match snapshot"),
                 ("start_at", "2026-10-17T00:00:00Z", "one calendar month"),
                 ("end_stars", 998, "match snapshot Stars")]
        for key, value, message in cases:
            with self.subTest(key=key):
                self.data = copy.deepcopy(good)
                self.data["metadata"]["star_growth_evidence"][key] = value
                self.write_catalog()
                self.assert_error(message)

    def test_growth_rejects_a_past_month_unrelated_to_evaluation(self):
        self.data["snapshot"]["last_success_at"] = "2026-08-16T00:00:00Z"
        self.growth(start_at="2026-07-16T00:00:00Z", end_at="2026-08-16T00:00:00Z")
        self.write_catalog()
        self.assert_error("end_at must be on the evaluation's UTC date")
        self.assert_error("1000 Stars or qualifying monthly growth")

    def test_growth_accepts_earlier_snapshot_on_same_utc_review_date(self):
        self.data["evaluated_at"] = "2026-11-16T18:00:00Z"
        # The local calendar date differs; both timestamps are November 16 UTC.
        self.data["snapshot"]["last_success_at"] = "2026-11-17T01:00:00+08:00"
        self.growth(start_at="2026-10-16T17:00:00Z", end_at="2026-11-16T17:00:00Z")
        self.write_catalog()
        self.assert_valid()

    def test_total_star_route_has_no_snapshot_freshness_threshold(self):
        self.data["snapshot"]["last_success_at"] = "2026-08-16T00:00:00Z"
        self.write_catalog()
        self.assert_valid()  # 1000 total Stars; the monthly-growth route is unused.

    def test_growth_clamps_calendar_month_end_not_thirty_days(self):
        self.data["evaluated_at"] = self.data["snapshot"]["last_success_at"] = "2025-03-31T00:00:00Z"
        self.data["metadata"]["activity_evidence"][0]["occurred_at"] = "2025-03-30T00:00:00Z"
        self.growth(start_at="2025-02-28T00:00:00Z", end_at="2025-03-31T00:00:00Z")
        self.write_catalog()
        self.assert_valid()
        self.data["metadata"]["star_growth_evidence"]["start_at"] = "2025-03-01T00:00:00Z"
        self.write_catalog()
        self.assert_error("one calendar month")

    def test_growth_rejects_missing_sources_boolean_and_negative_counts(self):
        self.growth()
        good = copy.deepcopy(self.data)
        for key, value, message in [("source_url", "", "source_url"), ("baseline_source_url", None, "baseline_source_url"),
                ("source_url", "not-a-url", "HTTP(S)"), ("start_stars", True, "start_stars must be int"),
                ("end_stars", False, "end_stars must be int"), ("start_stars", -1, "must not be negative")]:
            with self.subTest(key=key, value=value):
                self.data = copy.deepcopy(good)
                self.data["metadata"]["star_growth_evidence"][key] = value
                self.write_catalog()
                self.assert_error(message)

    def test_growth_rejects_future_dates(self):
        self.growth(start_at="2027-01-16T00:00:00Z", end_at="2027-02-16T00:00:00Z")
        self.write_catalog()
        self.assert_error("start_at must not be in the future")
        self.assert_error("end_at must not be in the future")

    def test_ai_relevance_requires_true_bilingual_reason_and_source(self):
        good = copy.deepcopy(self.data)
        for field, value, message in [("supports_ai_tasks", False, "explicitly support AI tasks"),
                ("supports_ai_tasks", 1, "must be bool"), ("reason", {"zh-CN": "说明", "en": " "}, "en must not be empty"),
                ("source_url", "", "source_url")]:
            with self.subTest(field=field):
                self.data = copy.deepcopy(good)
                self.data["metadata"]["ai_task_relevance"][field] = value
                self.write_catalog()
                self.assert_error(message)
        self.data["metadata"].pop("ai_task_relevance")
        self.write_catalog()
        self.assert_error("ai_task_relevance must be dict")

    def test_docs_bots_issues_prs_and_releases_are_activity(self):
        for kind, tail in [("commit", "commit/" + "a" * 40), ("PR", "pull/12"),
                ("pull_request", "pull/13"), ("issue", "issues/15"), ("release", "releases/tag/v1.0")]:
            with self.subTest(kind=kind):
                activity = self.data["metadata"]["activity_evidence"][0]
                activity.update(type=kind, url="https://github.com/owner/example/" + tail)
                self.write_catalog()
                self.assert_valid()
        self.data["metadata"]["activity_evidence"][0].update(type="issue", url="https://api.github.com/repos/owner/example/issues/15")
        self.write_catalog()
        self.assert_valid()

    def test_activity_requires_traceable_matching_event(self):
        good = copy.deepcopy(self.data)
        cases = [("type", "push", "activity type"), ("url", "https://github.com/unrelated/repo/issues/1", "matching repository event"),
                 ("occurred_at", "2026-11-15", "ISO timestamp"), ("reason", {"zh-CN": "说明"}, "en must be str"),
                 ("qualifies", "true", "qualifies must be bool")]
        for key, value, message in cases:
            with self.subTest(key=key):
                self.data = copy.deepcopy(good)
                self.data["metadata"]["activity_evidence"][0][key] = value
                self.write_catalog()
                self.assert_error(message)
        self.data["metadata"]["activity_evidence"] = []
        self.write_catalog()
        self.assert_error("requires recent activity")

    def test_activity_calendar_window_includes_cutoff_date(self):
        activity = self.data["metadata"]["activity_evidence"][0]
        activity["occurred_at"] = "2026-08-16T00:00:00Z"
        self.write_catalog()
        self.assert_valid()
        for value in ("2026-08-15T23:59:59Z", "2026-11-16T00:00:01Z"):
            activity["occurred_at"] = value
            self.write_catalog()
            self.assert_error("three-calendar-month")

    def test_activity_month_end_clamp_and_review_order(self):
        self.data["evaluated_at"] = self.data["snapshot"]["last_success_at"] = "2025-05-31T12:00:00Z"
        activity = self.data["metadata"]["activity_evidence"][0]
        activity["occurred_at"] = "2025-02-28T00:00:00Z"
        self.write_catalog()
        self.assert_valid()
        activity["reviewed_at"] = "2025-02-27T00:00:00Z"
        self.write_catalog()
        self.assert_error("after its review")

    def test_explicit_legacy_exemption_preserves_unreviewed_entry(self):
        self.make_legacy()
        self.write_catalog()
        self.assert_valid()
        self.data["metadata"].pop("activity_evidence")
        self.write_catalog()
        self.assert_valid()

    def test_legacy_cannot_be_forged_using_any_single_identifier(self):
        self.make_legacy()
        original = copy.deepcopy(self.data)
        for field, value in [("id", "new-id"), ("repository", "different/repository"), ("repo_node_id", "R_different")]:
            with self.subTest(field=field):
                self.data = copy.deepcopy(original)
                self.data["metadata"][field] = value
                if field == "repository":
                    self.data["snapshot"]["full_name"] = value
                if field == "repo_node_id":
                    self.data["snapshot"]["repo_node_id"] = value
                self.write_catalog()
                self.assert_error("legacy admission identity mismatch")
                self.assert_error("ai_task_relevance")
                self.assert_error("requires recent activity")

    def test_unregistered_legacy_claim_has_no_effect(self):
        self.data["metadata"]["legacy"] = True
        self.data["metadata"].pop("ai_task_relevance")
        self.data["snapshot"]["stargazers_count"] = 1
        self.write_catalog()
        self.assert_error("ai_task_relevance")
        self.assert_error("1000 Stars or qualifying monthly growth")

    def test_policy_is_required_and_cannot_weaken_thresholds(self):
        (self.root / "catalog-policy.json").unlink()
        self.assert_error("cannot read policy")
        for field, value in [("min_stars", 0), ("schema_version", True), ("activity_months", 12),
                ("min_star_growth", 1), ("license_required", True), ("legacy_admissions", {})]:
            with self.subTest(field=field):
                self.policy = {**CHECK.POLICY, "legacy_admissions": []}
                self.policy[field] = value
                self.write_catalog()
                self.assert_error(field)

    def test_policy_rejects_duplicate_legacy_identities(self):
        self.make_legacy()
        self.policy["legacy_admissions"] *= 2
        self.write_catalog()
        self.assert_error("duplicate legacy identity")

    def test_candidates_rejected_even_for_legacy(self):
        self.make_legacy()
        self.data["eligibility"] = {"status": "needs_review", "reasons": ["historical"]}
        self.write_catalog()
        self.assert_error("all catalog entries must have eligible status")
        self.change("README.md", "## Included (1)", "## Included (1)\n## Candidates (0)")
        self.assert_error("candidate sections")

    def test_candidate_badges_and_four_column_navigation_rejected(self):
        self.change("README.md", "# Catalog", "# Catalog\n![Candidates](https://img.shields.io/badge/candidates-0-blue)")
        self.assert_error("candidate sections")
        self.change("README.en.md", "| Models | [1](#included-ai) |", "| Models | [1](#included-ai) | 0 |")
        self.assert_error("navigation must have three columns")

    def test_boolean_stars_and_duplicate_json_keys_rejected(self):
        self.data["snapshot"]["stargazers_count"] = True
        self.write_catalog()
        self.assert_error("stargazers_count must be int")
        self.change("docs/example.md", '"status": "eligible",', '"status": "eligible", "status": "unknown",')
        self.assert_error("duplicate JSON key")

    def test_malformed_fields_report_errors_without_crashing(self):
        original = copy.deepcopy(self.data)
        for key, replacement in [("metadata", []), ("snapshot", "wrong"), ("eligibility", None)]:
            with self.subTest(key=key):
                self.data = copy.deepcopy(original)
                self.data[key] = replacement
                self.write_catalog()
                self.assert_error(key + " must be dict")

    def test_repository_state_does_not_add_admission_conditions(self):
        for key, value in [("archived", True), ("disabled", True), ("visibility", "private")]:
            with self.subTest(key=key):
                old = self.data["snapshot"][key]
                self.data["snapshot"][key] = value
                self.write_catalog()
                self.assert_valid()
                self.data["snapshot"][key] = old

    def test_timestamps_and_snapshot_window(self):
        for value, message in [("not-a-date", "ISO timestamp"), ("2026-11-16T00:00:00", "ISO timestamp"),
                ("2026-11-16T00:00:01Z", "must not be later than evaluation"),
                ("2027-01-01T00:00:00Z", "must not be in the future")]:
            with self.subTest(value=value):
                self.data["snapshot"]["last_success_at"] = value
                self.write_catalog()
                self.assert_error(message)
        self.data["snapshot"]["last_success_at"] = "2026-08-01T00:00:00Z"
        self.write_catalog()
        self.assert_valid()

    def test_broken_link_and_anchor(self):
        self.change("README.md", "docs/example.md#中文", "docs/missing.md#english")
        self.assert_error("broken local link")
        self.change("README.md", "docs/missing.md#english", "docs/example.md#missing")
        self.assert_error("missing local anchor")

    def test_counts_stars_status_and_language_drift(self):
        self.change("README.md", "included-1-blue", "included-2-blue")
        self.assert_error("badge count")
        self.change("README.md", "AI tools | 1000", "AI tools | 9")
        self.assert_error("index Stars")
        self.change("docs/example.md", "已收录 / Included", "候选 / Candidate")
        self.assert_error("status header")
        self.change("README.en.md", "docs/example.md#english", "docs/example.md#中文")
        self.assert_error("entry link must target english")

    def test_duplicate_repository_and_stable_node_identity(self):
        other = copy.deepcopy(self.data)
        other["metadata"]["id"] = "other"
        self.write_catalog([self.data, other])
        self.assert_error("duplicate repo")
        other["metadata"]["repository"] = other["snapshot"]["full_name"] = "owner/other"
        self.write_catalog([self.data, other])
        self.assert_error("duplicate node_id")

    def test_evidence_fold_and_short_row(self):
        self.change("docs/example.md", "<details>", "")
        self.assert_error("details block")
        self.change("README.md", " | Purpose | AI tools | 1000 |", " |")
        self.assert_error("index row requires at least four columns")

    def test_navigation_counts_and_duplicate_rows(self):
        self.change("README.md", "| Models | [1](#included-ai) |", "| Models | [2](#included-ai) |")
        self.assert_error("navigation count")
        self.change("README.en.md", "| [Example](docs/example.md#english) | Purpose | AI tools | 1000 |",
                    "| [Example](docs/example.md#english) | Purpose | AI tools | 1000 |\n| [Example](docs/example.md#english) | Purpose | AI tools | 1000 |")
        self.assert_error("exactly once in category lists")


class RepositoryChecks(unittest.TestCase):
    def test_real_repository(self):
        self.assertEqual([], CHECK.check_catalog(REPO))


if __name__ == "__main__":
    unittest.main()
