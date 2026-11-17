#!/usr/bin/env python3
"""Read-only, offline checks for the Markdown catalog (Python standard library)."""

import argparse
import calendar
from collections import Counter
from datetime import datetime, timezone
import json
from pathlib import Path
import re
import sys
import unicodedata
from urllib.parse import unquote, urlsplit


CATEGORIES = {
    "ai": ("AI 工具", "AI tools"),
    "development": ("开发辅助", "Development", "Development tools"),
    "media": ("图像与音视频", "Images, audio and video"),
    "productivity": ("文档与效率", "Documents and productivity", "Productivity"),
    "automation": ("自动化", "Automation"),
    "operations": ("部署与运维", "Operations", "Deployment and operations"),
    "data": ("数据处理", "Data processing"),
    "terminal": ("终端与 Shell", "Terminal and shell", "Terminal and Shell"),
    "knowledge": ("知识与学习", "Knowledge and learning"),
}
JSON_BLOCK = re.compile(r"^```json\s*\n(.*?)\n```", re.M | re.S)
LINK = re.compile(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)|(?:href|src)=[\'"]([^\'"]+)[\'"]')
POLICY = {
    "schema_version": 1,
    "policy_id": "ai-activity-stars-2026-11-17",
    "activity_months": 3,
    "min_stars": 1000,
    "star_growth_months": 1,
    "min_star_growth": 500,
    "license_required": False,
    "ai_task_relevance_required": True,
}
ACTIVITY_TYPES = {"commit", "pr", "pull_request", "issue", "release"}


def months_before(value, months):
    year, month0 = divmod(value.year * 12 + value.month - 1 - months, 12)
    month = month0 + 1
    return value.replace(year=year, month=month,
                         day=min(value.day, calendar.monthrange(year, month)[1]))


def web_url(value):
    if not isinstance(value, str) or any(c.isspace() for c in value):
        return False
    try:
        parts = urlsplit(value)
        return parts.scheme in {"http", "https"} and bool(parts.hostname) and not parts.username
    except ValueError:
        return False


def event_url(value, repo, event_type):
    if not web_url(value) or not isinstance(repo, str):
        return False
    parts = urlsplit(value)
    if parts.scheme != "https":
        return False
    if parts.hostname == "github.com":
        prefix = "/" + repo + "/"
        endings = {"commit": r"commit/[0-9a-fA-F]{40}",
                   "pr": r"pull/[1-9][0-9]*", "pull_request": r"pull/[1-9][0-9]*",
                   "issue": r"issues/[1-9][0-9]*", "release": r"releases/(?:tag/[^?#]+|[1-9][0-9]*)"}
    elif parts.hostname == "api.github.com":
        prefix = "/repos/" + repo + "/"
        endings = {"commit": r"commits/[0-9a-fA-F]{40}",
                   "pr": r"pulls/[1-9][0-9]*", "pull_request": r"pulls/[1-9][0-9]*",
                   "issue": r"issues/[1-9][0-9]*", "release": r"releases/(?:tags/[^?#]+|[1-9][0-9]*)"}
    else:
        return False
    return (parts.path[:len(prefix)].lower() == prefix.lower()
            and re.fullmatch(endings.get(event_type, r"(?!)"), parts.path[len(prefix):]) is not None)


def no_duplicate_keys(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key: " + key)
        result[key] = value
    return result


def anchors(text):
    text = re.sub(r"^```.*?^```\s*$", "", text, flags=re.M | re.S)
    result = set(re.findall(r'(?:id|name)=[\'"]([^\'"]+)', text))
    counts = Counter()
    for heading in re.findall(r"^#{1,6}\s+(.+?)\s*#*\s*$", text, re.M):
        heading = re.sub(r"<[^>]+>", "", heading).lower()
        slug = "".join(c for c in heading if c in "_- " or unicodedata.category(c)[0] not in "PSZC").replace(" ", "-")
        number = counts[slug]
        counts[slug] += 1
        result.add(slug + ("-" + str(number) if number else ""))
    return result


def check_catalog(root, now=None):
    root = Path(root).resolve()
    now = (now or datetime.now(timezone.utc)).astimezone(timezone.utc)
    errors, entries, texts = [], {}, {}

    def error(path, message):
        errors.append(f"{path}: {message}")

    def required(obj, key, kind, path):
        value = obj.get(key) if isinstance(obj, dict) else None
        if not isinstance(value, kind) or (kind is int and isinstance(value, bool)):
            error(path, f"{key} must be {kind.__name__}")
            return {} if kind is dict else [] if kind is list else None
        if kind is str and not value.strip():
            error(path, f"{key} must not be empty")
        return value

    def timestamp(value, field, path):
        try:
            parsed = datetime.fromisoformat(value.replace("Z", "+00:00"))
            if parsed.tzinfo is None:
                raise ValueError("timezone required")
            parsed = parsed.astimezone(timezone.utc)
        except (AttributeError, TypeError, ValueError, OverflowError):
            error(path, f"{field} must be an ISO timestamp with a timezone")
            return None
        if parsed > now:
            error(path, f"{field} must not be in the future")
        return parsed

    def source(obj, key, path):
        value = required(obj, key, str, path)
        if not web_url(value):
            error(path, f"{key} must be an HTTP(S) source URL")
        return value

    def bilingual(obj, path):
        for language in ("zh-CN", "en"):
            required(obj, language, str, path)

    policy_path = "catalog-policy.json"
    try:
        policy = json.loads((root / policy_path).read_text(encoding="utf-8"), object_pairs_hook=no_duplicate_keys)
    except (OSError, ValueError) as exc:
        error(policy_path, f"cannot read policy: {exc}")
        policy = {}
    for key, expected in POLICY.items():
        value = policy.get(key) if isinstance(policy, dict) else None
        if type(value) is not type(expected) or value != expected:
            error(policy_path, f"{key} must equal {expected!r} for this policy")
    legacy_records = required(policy, "legacy_admissions", list, policy_path)
    legacy = {}
    legacy_keys = [set(), set(), set()]
    for record in legacy_records:
        fields = tuple(required(record, k, str, policy_path) for k in ("id", "repository", "repo_node_id"))
        baseline = timestamp(required(record, "baseline_evaluated_at", str, policy_path),
                             "legacy baseline_evaluated_at", policy_path)
        if not all(fields):
            continue
        if not re.fullmatch(r"[^/\s]+/[^/\s]+", fields[1]):
            error(policy_path, "legacy repository must be owner/name")
        keys = (fields[0].lower(), fields[1].lower(), fields[2])
        for key_set, key in zip(legacy_keys, keys):
            if key in key_set:
                error(policy_path, "duplicate legacy identity: " + key)
            key_set.add(key)
        legacy[fields] = baseline

    def growth_evidence(metadata, snapshot_at, stars, evaluated_at, path):
        start_errors = len(errors)
        growth = required(metadata, "star_growth_evidence", dict, path)
        start_at = timestamp(required(growth, "start_at", str, path), "star_growth_evidence.start_at", path)
        end_at = timestamp(required(growth, "end_at", str, path), "star_growth_evidence.end_at", path)
        start_stars = required(growth, "start_stars", int, path)
        end_stars = required(growth, "end_stars", int, path)
        source(growth, "source_url", path)
        source(growth, "baseline_source_url", path)
        if any(value is not None and value < 0 for value in (start_stars, end_stars)):
            error(path, "star growth counts must not be negative")
        if end_at and snapshot_at and end_at != snapshot_at:
            error(path, "star growth end_at must match snapshot.last_success_at")
        if end_at and evaluated_at and end_at > evaluated_at:
            error(path, "star growth end_at must not follow evaluation")
        if end_at and evaluated_at and end_at.date() != evaluated_at.date():
            error(path, "star growth end_at must be on the evaluation's UTC date")
        if start_at and end_at:
            try:
                expected_start = months_before(end_at, POLICY["star_growth_months"])
            except ValueError:
                expected_start = None
            if start_at != expected_start:
                error(path, "star growth start_at must be exactly one calendar month before end_at")
        if end_stars is not None and end_stars != stars:
            error(path, "star growth end_stars must match snapshot Stars")
        if start_stars is not None and end_stars is not None and end_stars - start_stars < POLICY["min_star_growth"]:
            error(path, "star growth must be at least 500 net Stars")
        return len(errors) == start_errors

    docs = sorted((root / "docs").glob("*.md"))
    if not docs:
        error("docs", "no entries found")
    for file in docs:
        path = file.relative_to(root).as_posix()
        text = file.read_text(encoding="utf-8")
        texts[path] = text
        blocks = list(JSON_BLOCK.finditer(text))
        if len(blocks) != 1:
            error(path, "expected exactly one JSON evidence block")
            continue
        block = blocks[0]
        before = text[:block.start()]
        if before.rfind("<details>") < before.rfind("</details>") or "<details>" not in before or "</details>" not in text[block.end():]:
            error(path, "review JSON must be inside a details block")
        if "review-evidence" not in anchors(text):
            error(path, "missing review-evidence anchor")
        if not {"中文", "english"} <= anchors(text):
            error(path, "entry requires Chinese and English sections")
        try:
            data = json.loads(block[1], object_pairs_hook=no_duplicate_keys)
        except ValueError as exc:
            error(path, f"invalid JSON: {exc}")
            continue
        if not isinstance(data, dict):
            error(path, "JSON evidence must be an object")
            continue
        evaluated_at = timestamp(required(data, "evaluated_at", str, path), "evaluated_at", path)
        eligibility = required(data, "eligibility", dict, path)
        metadata = required(data, "metadata", dict, path)
        snapshot = required(data, "snapshot", dict, path)
        status = required(eligibility, "status", str, path)
        reasons = required(eligibility, "reasons", list, path)
        if status != "eligible":
            error(path, "all catalog entries must have eligible status; candidates are not supported")
        if reasons:
            error(path, "eligible entry must have no blocking reasons")
        if any(not isinstance(reason, str) for reason in reasons):
            error(path, "eligibility reasons must be strings")
        entry_id = required(metadata, "id", str, path)
        repo = required(metadata, "repository", str, path)
        node_id = required(metadata, "repo_node_id", str, path)
        category = required(metadata, "category", str, path)
        required(metadata, "name", str, path)
        bilingual(required(metadata, "summary", dict, path), path)
        if entry_id != file.stem:
            error(path, "metadata.id must match filename")
        if category not in CATEGORIES:
            error(path, "unknown category")
        if not isinstance(repo, str) or not re.fullmatch(r"[^/\s]+/[^/\s]+", repo):
            error(path, "repository must be owner/name")
        identity = (entry_id, repo, node_id)
        legacy_identity = identity in legacy
        is_legacy = legacy_identity and evaluated_at is not None and evaluated_at == legacy[identity]
        identity_keys = ((entry_id or "").lower(), (repo or "").lower(), node_id)
        if not legacy_identity and any(key in keys for key, keys in zip(identity_keys, legacy_keys)):
            error(path, "legacy admission identity mismatch: id, repository and repo_node_id must all match")
        stars = required(snapshot, "stargazers_count", int, path)
        if stars is not None and stars < 0:
            error(path, "Stars must not be negative")
        if snapshot.get("full_name") != repo or snapshot.get("repo_node_id") != node_id:
            error(path, "snapshot identity differs from metadata")
        for key in ("archived", "disabled"):
            required(snapshot, key, bool, path)
        required(snapshot, "visibility", str, path)
        snapshot_at = timestamp(required(snapshot, "last_success_at", str, path), "snapshot.last_success_at", path)
        # Total-Star admissions have no snapshot-age threshold. Only the monthly
        # growth route binds its end snapshot to the evaluation's UTC date.
        if evaluated_at and snapshot_at and snapshot_at > evaluated_at:
            error(path, "snapshot must not be later than evaluation")

        # Historical admissions preserve an exact identity at its original review
        # time. Changing that review time requires the current admission policy.
        if not is_legacy or "ai_task_relevance" in metadata:
            relevance = required(metadata, "ai_task_relevance", dict, path)
            supports = required(relevance, "supports_ai_tasks", bool, path)
            bilingual(required(relevance, "reason", dict, path), path)
            source(relevance, "source_url", path)
            if not is_legacy and supports is not True:
                error(path, "new entry must explicitly support AI tasks")
        if not is_legacy:
            growth_ok = False
            if "star_growth_evidence" in metadata or (stars is not None and stars < POLICY["min_stars"]):
                growth_ok = growth_evidence(metadata, snapshot_at, stars, evaluated_at, path)
            if stars is not None and stars < POLICY["min_stars"] and not growth_ok:
                error(path, "new entry requires at least 1000 Stars or qualifying monthly growth")

        activities = required(metadata, "activity_evidence", list, path) if not is_legacy or "activity_evidence" in metadata else []
        qualifying = 0
        for activity in activities:
            if not isinstance(activity, dict):
                error(path, "activity evidence must be an object")
                continue
            if "qualifies" in activity:
                required(activity, "qualifies", bool, path)
            if is_legacy:
                # Check declared field types, but do not retroactively require new
                # evidence, dates within the new window, or a qualifying event.
                for key in ("type", "url", "occurred_at", "reviewed_at"):
                    if key in activity:
                        required(activity, key, str, path)
                if "reason" in activity:
                    bilingual(required(activity, "reason", dict, path), path)
                continue
            event_type = required(activity, "type", str, path)
            event_type = (event_type or "").lower()
            if event_type not in ACTIVITY_TYPES:
                error(path, "activity type must be commit, PR, issue or release")
            url = required(activity, "url", str, path)
            if not event_url(url, repo, event_type):
                error(path, "activity URL must identify the matching repository event")
            occurred_at = timestamp(required(activity, "occurred_at", str, path), "activity.occurred_at", path)
            if "reviewed_at" in activity:
                reviewed_at = timestamp(required(activity, "reviewed_at", str, path), "activity.reviewed_at", path)
                if occurred_at and reviewed_at and occurred_at > reviewed_at:
                    error(path, "activity cannot occur after its review")
            bilingual(required(activity, "reason", dict, path), path)
            in_window = False
            if occurred_at and evaluated_at:
                try:
                    cutoff = months_before(evaluated_at, POLICY["activity_months"]).date()
                    in_window = cutoff <= occurred_at.date() and occurred_at <= evaluated_at
                except ValueError:
                    pass
                if not in_window:
                    error(path, "activity must be within the three-calendar-month evaluation window")
            if in_window and activity.get("qualifies", True) is not False:
                qualifying += 1
        if not is_legacy and not qualifying:
            error(path, "new entry requires recent activity evidence")

        headers = dict(re.findall(r"^\| ([^|\n]+) \| ([^|\n]*) \|$", before, re.M))
        if headers.get("Star") != str(stars):
            error(path, "Star header differs from snapshot")
        if headers.get("状态 / Status") != "已收录 / Included":
            error(path, "status header must be 已收录 / Included")
        labels = headers.get("分类 / Category", "").split(" / ")
        if category in CATEGORIES and (not labels or any(label not in CATEGORIES[category] for label in labels)):
            error(path, "category header differs from metadata")
        if headers.get("评估时间 / Evaluated at") != data.get("evaluated_at"):
            error(path, "evaluation header differs from evidence")
        entries[path] = {"id": entry_id, "repo": repo, "node_id": node_id,
                         "category": category, "stars": stars, "legacy": is_legacy}

    for field in ("id", "repo", "node_id"):
        counts = Counter((str(e[field]).lower() if field != "node_id" else str(e[field])) for e in entries.values())
        for value, count in counts.items():
            if count > 1:
                error("docs", f"duplicate {field}: {value}")

    expected_counts = Counter(e["category"] for e in entries.values())
    for readme in ("README.md", "README.en.md"):
        file = root / readme
        if not file.is_file():
            error(readme, "missing catalog index")
            continue
        text = file.read_text(encoding="utf-8")
        texts[readme] = text
        if re.search(r'^##\s+(?:候选|Candidates)(?:\s|[（(]|$)|/badge/candidates-|(?:id|href)=[\'"]#?candidates?(?:-|[\'"])', text, re.M | re.I):
            error(readme, "candidate sections, anchors and badges are not supported")
        section = None
        seen, nav_seen, summary_seen = Counter(), Counter(), Counter()
        for line_no, line in enumerate(text.splitlines(), 1):
            if line.startswith("## ") or "</details>" in line:
                section = None
            marker = re.search(r'id=[\'"]included-([^\'"]+)[\'"]', line)
            if marker:
                section = marker[1]
                if section not in expected_counts:
                    error(readme, f"line {line_no}: unknown category section {section}")
            summary = re.search(r"<summary>.*?·\s*(\d+)\s*(?:项|projects)", line)
            if summary and section:
                summary_seen[section] += 1
                if int(summary[1]) != expected_counts[section]:
                    error(readme, f"line {line_no}: category summary count differs from entries")
            match = re.match(r"\| \[.*?\]\((docs/[^)#]+)(?:#([^)]+))?\) \|", line)
            if match and section:
                path = match[1]
                seen[path] += 1
                if path not in entries:
                    error(readme, f"line {line_no}: unknown entry {path}")
                    continue
                entry = entries[path]
                if section != entry["category"]:
                    error(readme, f"line {line_no}: index category differs for {path}")
                columns = line.strip().strip("|").split("|")
                if len(columns) < 4:
                    error(readme, f"line {line_no}: index row requires at least four columns")
                    continue
                expected_anchor = "english" if readme == "README.en.md" else "中文"
                if match[2] != expected_anchor:
                    error(readme, f"line {line_no}: entry link must target {expected_anchor}")
                if columns[-1].strip() != str(entry["stars"]):
                    error(readme, f"line {line_no}: index Stars differ for {path}")
                if columns[-2].strip() not in CATEGORIES.get(entry["category"], ()):
                    error(readme, f"line {line_no}: index category label differs for {path}")
            nav = re.match(r"\| \[.*?\]\(#included-([^)]+)\) \|", line)
            if nav:
                category = nav[1]
                nav_seen[category] += 1
                columns = [c.strip() for c in line.strip().strip("|").split("|")]
                if len(columns) != 3:
                    error(readme, f"line {line_no}: category navigation must have three columns")
                else:
                    number = re.fullmatch(r"(?:\[(\d+)\]\(#included-" + re.escape(category) + r"\)|(\d+))", columns[2])
                    if not number or int(number[1] or number[2]) != expected_counts[category]:
                        error(readme, f"line {line_no}: navigation count differs from entries")
                if category not in expected_counts:
                    error(readme, f"line {line_no}: unknown navigation category {category}")
        for category in expected_counts:
            if nav_seen[category] != 1:
                error(readme, f"navigation must contain category exactly once: {category}")
            if summary_seen[category] != 1:
                error(readme, f"category summary must appear exactly once: {category}")
        totals = re.findall(
            r"(?:现有\s*|The catalog contains\s+)(\d+)(?:\s*个(?:已收录)?项目| (?:included )?projects)",
            text.replace("**", ""),
        )
        if not totals or any(int(n) != len(entries) for n in totals):
            error(readme, "intro project count differs from entries")
        for path in entries:
            if seen[path] != 1:
                error(readme, f"entry must appear exactly once in category lists: {path} (found {seen[path]})")
        for badge, expected in (("included", len(entries)), ("categories", len(expected_counts))):
            values = re.findall(r"/badge/" + badge + r"-(\d+)-", text)
            if not values or any(int(v) != expected for v in values):
                error(readme, f"{badge} badge count differs from entries")
        values = re.findall(r"^## (?:已收录|Included)\s*[（(](\d+)[）)]", text, re.M)
        if len(values) != 1 or int(values[0]) != len(entries):
            error(readme, "included heading count differs from entries")

    for file in sorted((root / "reviews").glob("*.md")):
        texts[file.relative_to(root).as_posix()] = file.read_text(encoding="utf-8")
    for path, text in texts.items():
        prose = re.sub(r"^```.*?^```\s*$", "", text, flags=re.M | re.S)
        for match in LINK.finditer(prose):
            url = match[1] or match[2]
            try:
                parts = urlsplit(url)
            except ValueError:
                error(path, "invalid link: " + url)
                continue
            if parts.scheme or parts.netloc:
                continue
            target = ((root / path).parent / unquote(parts.path)).resolve() if parts.path else root / path
            if not target.is_relative_to(root):
                error(path, "local link escapes repository: " + url)
            elif not target.exists():
                error(path, "broken local link: " + url)
            elif parts.fragment and target.is_file() and target.suffix == ".md":
                target_text = texts.get(target.relative_to(root).as_posix())
                if target_text is None:
                    target_text = target.read_text(encoding="utf-8")
                if unquote(parts.fragment) not in anchors(target_text):
                    error(path, "missing local anchor: " + url)
    return errors


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    errors = check_catalog(args.root)
    for message in errors:
        print(message, file=sys.stderr)
    print(f"Catalog check: {'FAIL' if errors else 'PASS'} ({len(errors)} errors)")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
