#!/usr/bin/env python3
"""Read-only, offline checks for the Markdown catalog (Python standard library)."""

import argparse
import calendar
from collections import Counter
from datetime import datetime, timedelta, timezone
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
PIN = re.compile(r"https://(?:github\.com/[^/]+/[^/]+/blob|raw\.githubusercontent\.com/[^/]+/[^/]+)/[0-9a-f]{40}/.+$")
HEX = re.compile(r"[0-9a-f]{64}$")
LINK = re.compile(r'\]\(([^\s)]+)(?:\s+"[^"]*")?\)|(?:href|src)=[\'"]([^\'"]+)[\'"]')
GENERIC_ACTIVITY = re.compile(r"发布状态与时间|Checked the non-draft, non-prerelease publication", re.I)


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


def check_catalog(root):
    root = Path(root).resolve()
    errors = []
    entries = {}
    texts = {}

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
            return parsed.astimezone(timezone.utc)
        except (AttributeError, TypeError, ValueError, OverflowError):
            error(path, f"{field} must be an ISO timestamp with a timezone")
            return None

    def license_source(item, path, repo, allow_missing=False):
        if not isinstance(item, dict):
            error(path, "license evidence must be an object")
            return
        url = item.get("source_url")
        if not url and allow_missing:
            return
        if not isinstance(url, str) or not PIN.fullmatch(url):
            error(path, "license source_url must pin a 40-character commit SHA")
        elif isinstance(repo, str) and "/".join(urlsplit(url).path.split("/")[1:3]).lower() != repo.lower():
            error(path, "license source repository differs from metadata.repository")
        digest = item.get("sha256", item.get("license_sha256"))
        if not isinstance(digest, str) or not HEX.fullmatch(digest):
            error(path, "license evidence requires a SHA-256 digest")

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
        try:
            data = json.loads(block[1], object_pairs_hook=no_duplicate_keys)
        except (ValueError, json.JSONDecodeError) as exc:
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
        if status not in {"eligible", "needs_review", "unknown", "ineligible"}:
            error(path, "unknown eligibility status")
        if any(not isinstance(reason, str) for reason in reasons):
            error(path, "eligibility reasons must be strings")
        if "below_star_threshold" in reasons:
            error(path, "below_star_threshold cannot be a current eligibility reason")
        if status == "eligible" and reasons:
            error(path, "eligible entry must have no blocking reasons")
        if status != "eligible" and not reasons:
            error(path, "candidate requires a current reason")
        entry_id = required(metadata, "id", str, path)
        repo = required(metadata, "repository", str, path)
        category = required(metadata, "category", str, path)
        required(metadata, "name", str, path)
        node_id = required(metadata, "repo_node_id", str, path)
        summary = required(metadata, "summary", dict, path)
        for language in ("zh-CN", "en"):
            required(summary, language, str, path)
        if entry_id != file.stem:
            error(path, "metadata.id must match filename")
        if category not in CATEGORIES:
            error(path, "unknown category")
        if not isinstance(repo, str) or not re.fullmatch(r"[^/\s]+/[^/\s]+", repo):
            error(path, "repository must be owner/name")
        stars = required(snapshot, "stargazers_count", int, path)
        if stars is not None and stars < 0:
            error(path, "Stars must not be negative")
        if snapshot.get("full_name") != repo or snapshot.get("repo_node_id") != node_id:
            error(path, "snapshot identity differs from metadata")
        for key in ("archived", "disabled"):
            required(snapshot, key, bool, path)
        snapshot_at = timestamp(required(snapshot, "last_success_at", str, path), "snapshot.last_success_at", path)
        if evaluated_at and snapshot_at and not timedelta(0) <= evaluated_at - snapshot_at <= timedelta(days=7):
            error(path, "snapshot must precede evaluation by no more than 7 days")
        if status == "eligible" and (snapshot.get("archived") or snapshot.get("disabled") or snapshot.get("visibility") != "public"):
            error(path, "included repository must be public, active and enabled")
        license_review = required(metadata, "license_review", dict, path)
        required(license_review, "osi_approved", bool, path)
        pending = eligibility.get("pending_actions")
        missing_allowed = status != "eligible" and isinstance(pending, dict) and all(isinstance(pending.get(k), list) and pending[k] for k in ("zh-CN", "en"))
        license_source(license_review, path, repo, missing_allowed)
        if license_review.get("evidence_status") == "hash_matched" and snapshot.get("license_sha256") != license_review.get("license_sha256"):
            error(path, "hash-matched license evidence differs from snapshot digest")
        files = license_review.get("files", [])
        if not isinstance(files, list):
            error(path, "license files must be an array")
        else:
            for evidence in files:
                license_source(evidence, path, repo)
        if license_review.get("osi_approved") is True and re.search(r"CC-|LicenseRef-", str(license_review.get("spdx", ""))):
            error(path, "OSI flag cannot cover content or custom licenses")
        components = license_review.get("components", [])
        if not isinstance(components, list):
            error(path, "license components must be an array")
        else:
            for component in components:
                license_source(component, path, repo)
                if not isinstance(component, dict):
                    continue
                required(component, "scope", str, path)
                spdx = required(component, "spdx", str, path)
                osi = required(component, "osi_approved", bool, path)
                if osi is True and re.search(r"CC-|LicenseRef-", spdx or ""):
                    error(path, "component OSI flag cannot cover content or custom licenses")
        if status == "eligible" and (license_review.get("osi_approved") is not True or not license_review.get("spdx")):
            error(path, "included code requires a reviewed open-source license")
        activities = required(metadata, "activity_evidence", list, path)
        qualifying = []
        for activity in activities:
            if not isinstance(activity, dict):
                error(path, "activity evidence must be an object")
                continue
            required(activity, "qualifies", bool, path)
            if "implementation_evidence" in activity:
                implementation = required(activity, "implementation_evidence", dict, path)
                sha = required(implementation, "sha", str, path)
                url = required(implementation, "url", str, path)
                if not sha or not re.fullmatch(r"[0-9a-f]{40}", sha) or url != f"https://github.com/{repo}/commit/{sha}":
                    error(path, "implementation evidence must pin the matching repository commit SHA")
                reviewed_files = required(implementation, "reviewed_files", list, path)
                if not reviewed_files or any(not isinstance(f, str) or not f.strip() for f in reviewed_files):
                    error(path, "implementation evidence requires reviewed files")
            if activity.get("qualifies") is True:
                qualifying.append(activity)
                for key in ("url", "occurred_at", "reviewed_at"):
                    required(activity, key, str, path)
                occurred_at = timestamp(activity.get("occurred_at"), "activity.occurred_at", path)
                reviewed_at = timestamp(activity.get("reviewed_at"), "activity.reviewed_at", path)
                if occurred_at and evaluated_at:
                    month_index = evaluated_at.year * 12 + evaluated_at.month - 1 - 3
                    year, month = divmod(month_index, 12)
                    month += 1
                    day = min(evaluated_at.day, calendar.monthrange(year, month)[1])
                    window_start = evaluated_at.replace(year=year, month=month, day=day).date()
                    if occurred_at > evaluated_at or occurred_at.date() < window_start:
                        error(path, "qualifying activity must be within the three-calendar-month evaluation window")
                if occurred_at and reviewed_at and occurred_at > reviewed_at:
                    error(path, "activity cannot occur after its review")
                reason = required(activity, "reason", dict, path)
                for language in ("zh-CN", "en"):
                    value = required(reason, language, str, path)
                    if value and GENERIC_ACTIVITY.search(value):
                        error(path, "activity reason must describe substantive changes, not only release status")
        if status == "eligible" and not qualifying:
            error(path, "included entry requires qualifying activity evidence")
        headers = dict(re.findall(r"^\| ([^|\n]+) \| ([^|\n]*) \|$", before, re.M))
        if headers.get("Star") != str(stars):
            error(path, "Star header differs from snapshot")
        expected_status = "已收录 / Included" if status == "eligible" else "候选 / Candidate"
        if headers.get("状态 / Status") != expected_status:
            error(path, "status header differs from eligibility")
        labels = headers.get("分类 / Category", "").split(" / ")
        if category in CATEGORIES and (not labels or any(label not in CATEGORIES[category] for label in labels)):
            error(path, "category header differs from metadata")
        if headers.get("评估时间 / Evaluated at") != data.get("evaluated_at"):
            error(path, "evaluation header differs from evidence")
        candidate_reasons = {}
        if status != "eligible":
            for lang, pattern in (("zh", r"^候选原因：(.+)$"), ("en", r"^Candidate reason: (.+)$")):
                found = re.search(pattern, before, re.M)
                if not found:
                    error(path, f"missing {lang} candidate reason")
                candidate_reasons[lang] = found[1].rstrip("。.") if found else ""
        entries[path] = {"id": entry_id, "repo": repo, "category": category, "stars": stars, "group": "included" if status == "eligible" else "candidate", "candidate_reasons": candidate_reasons}

    for field in ("id", "repo"):
        counts = Counter(str(e[field]).lower() for e in entries.values())
        for value, count in counts.items():
            if count > 1:
                error("docs", f"duplicate {field}: {value}")

    expected_counts = Counter((e["group"], e["category"]) for e in entries.values())
    totals = Counter(e["group"] for e in entries.values())
    for readme in ("README.md", "README.en.md"):
        file = root / readme
        if not file.is_file():
            error(readme, "missing catalog index")
            continue
        text = file.read_text(encoding="utf-8")
        texts[readme] = text
        section = None
        seen = Counter()
        nav_seen = Counter()
        for line_no, line in enumerate(text.splitlines(), 1):
            marker = re.search(r'id="(included|candidate)-([^\"]+)"', line)
            if marker:
                section = marker.groups()
            summary = re.search(r"<summary>.*?·\s*(\d+)\s*(?:项|projects)", line)
            if summary and section and int(summary[1]) != expected_counts[section]:
                error(readme, f"line {line_no}: category summary count differs from entries")
            match = re.match(r"\| \[.*?\]\((docs/[^)#]+)(?:#([^)]+))?\) \|", line)
            if match and section:
                path = match[1]
                seen[path] += 1
                if path not in entries:
                    error(readme, f"line {line_no}: unknown entry {path}")
                    continue
                entry = entries[path]
                if section != (entry["group"], entry["category"]):
                    error(readme, f"line {line_no}: index status/category differs for {path}")
                columns = line.strip("|").split("|")
                if len(columns) < 4:
                    error(readme, f"line {line_no}: index row requires at least four columns")
                    continue
                language = "en" if readme == "README.en.md" else "zh"
                expected_anchor = "english" if language == "en" else "中文"
                if match[2] != expected_anchor:
                    error(readme, f"line {line_no}: entry link must target {expected_anchor}")
                if entry["group"] == "candidate" and columns[1].strip().rstrip("。.") != entry["candidate_reasons"].get(language):
                    error(readme, f"line {line_no}: candidate reason differs from entry")
                if columns[-1].strip() != str(entry["stars"]):
                    error(readme, f"line {line_no}: index Stars differ for {path}")
                if columns[-2].strip() not in CATEGORIES.get(entry["category"], ()):
                    error(readme, f"line {line_no}: index category label differs for {path}")
            nav = re.match(r"\| \[.*?\]\(#included-([^)]+)\) \|.*?\| (.*?) \| (.*?) \|$", line)
            if nav:
                nav_seen[nav[1]] += 1
                for group, column in (("included", nav[2]), ("candidate", nav[3])):
                    number = re.search(r"\d+", column)
                    if not number or int(number[0]) != expected_counts[group, nav[1]]:
                        error(readme, f"line {line_no}: navigation count differs from entries")
        for category in {e["category"] for e in entries.values()}:
            if nav_seen[category] != 1:
                error(readme, f"navigation must contain category exactly once: {category}")
        for number in re.findall(r"(?:现有\s*|The catalog contains\s+)(\d+)(?:\s*个项目| projects)", text):
            if int(number) != len(entries):
                error(readme, "intro project count differs from entries")
        for path in entries:
            if seen[path] != 1:
                error(readme, f"entry must appear exactly once in category lists: {path} (found {seen[path]})")
        for badge, expected in (("included", totals["included"]), ("candidates", totals["candidate"]), ("categories", len({e["category"] for e in entries.values()}))):
            values = re.findall(r"/badge/" + badge + r"-(\d+)-", text)
            if not values or any(int(v) != expected for v in values):
                error(readme, f"{badge} badge count differs from entries")
        for pattern, group in ((r"^## (?:已收录|Included)\s*[（(](\d+)[）)]", "included"), (r"^## (?:候选|Candidates)\s*[（(](\d+)[）)]", "candidate")):
            values = re.findall(pattern, text, re.M)
            if not values or any(int(v) != totals[group] for v in values):
                error(readme, f"{group} heading count differs from entries")

    for file in sorted((root / "reviews").glob("*.md")):
        texts[file.relative_to(root).as_posix()] = file.read_text(encoding="utf-8")
    for path, text in texts.items():
        prose = re.sub(r"^```.*?^```\s*$", "", text, flags=re.M | re.S)
        for match in LINK.finditer(prose):
            url = match[1] or match[2]
            parts = urlsplit(url)
            if parts.scheme or parts.netloc:
                continue  # Network availability and upstream claims are checked separately.
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
