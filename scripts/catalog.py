"""Maintain a bilingual tool catalog using only the Python standard library."""

import argparse
import calendar
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
import re
import shutil
import sys
import tempfile
import unicodedata
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
LOCALES = ("zh-CN", "en")
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")
REPOSITORY = re.compile(r"[A-Za-z0-9][A-Za-z0-9_.-]*/[A-Za-z0-9_.-]+\Z")


class CatalogError(ValueError):
    pass


def require(condition, message):
    if not condition:
        raise CatalogError(message)


def read_json(path):
    def unique(pairs):
        result = {}
        for key, value in pairs:
            require(key not in result, f"{path}: duplicate JSON key {key}")
            result[key] = value
        return result

    try:
        result = json.loads(path.read_text(encoding="utf-8"), object_pairs_hook=unique)
    except (OSError, ValueError) as error:
        raise CatalogError(f"{path}: {error}") from error
    require(isinstance(result, dict), f"{path}: expected a JSON object")
    return result


def timestamp(value):
    require(isinstance(value, str), f"Expected an ISO 8601 timestamp, got {value!r}")
    try:
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as error:
        raise CatalogError(f"Invalid timestamp: {value}") from error
    require(result.tzinfo is not None, f"Timestamp needs a timezone: {value}")
    return result.astimezone(timezone.utc)


def iso(value):
    return value.astimezone(timezone.utc).isoformat().replace("+00:00", "Z")


def months_before(value, months):
    index = value.year * 12 + value.month - 1 - months
    year, month = divmod(index, 12)
    require(year >= 1, "Evaluation date is too early for the activity window")
    month += 1
    return value.replace(year=year, month=month, day=min(value.day, calendar.monthrange(year, month)[1]))


def text(value):
    return isinstance(value, str) and bool(value.strip())


def strings(value):
    return isinstance(value, list) and all(text(item) for item in value) and len(value) == len(set(value))


def url(value):
    return isinstance(value, str) and urlparse(value).scheme == "https" and bool(urlparse(value).netloc)


def localized(value, predicate):
    return isinstance(value, dict) and set(value) == set(LOCALES) and all(predicate(value[k]) for k in LOCALES)


def fingerprint(value):
    return value is None or (isinstance(value, str) and re.fullmatch(r"[0-9a-f]{64}", value) is not None)


def load(root):
    policy = read_json(root / "config/policy.json")
    taxonomy = read_json(root / "config/taxonomy.json")
    require(type(policy.get("schema_version")) is int and policy["schema_version"] == 1 and policy.get("locales") == list(LOCALES), "Unsupported policy version or locales")
    for key in ("min_stars", "activity_months", "snapshot_max_age_days"):
        require(type(policy.get(key)) is int and policy[key] > 0, f"Invalid policy: {key}")
    require(policy["activity_months"] <= 120, "Activity window must not exceed 120 months")
    categories = taxonomy.get("categories")
    require(isinstance(categories, dict) and categories and all(SLUG.fullmatch(k) and localized(v, text) for k, v in categories.items()), "Invalid bilingual categories")
    for key in ("forms", "platforms"):
        require(strings(taxonomy.get(key)), f"Invalid taxonomy: {key}")
    entries, repositories, identities = [], set(), set()
    for directory in sorted((root / "tools").iterdir()):
        if directory.name.startswith("."):
            continue
        require(directory.is_dir() and not directory.is_symlink() and SLUG.fullmatch(directory.name), f"Invalid tool directory: {directory}")
        data = read_json(directory / "tool.json")
        try:
            require(type(data["schema_version"]) is int and data["schema_version"] == 1 and data["id"] == directory.name, "Invalid version or id")
            require(text(data["name"]) and REPOSITORY.fullmatch(data["repository"]) and data["repository"].split('/')[1] not in ('.', '..'), "Invalid name or repository")
            require(data["repository"].casefold() not in repositories, "Duplicate repository")
            repositories.add(data["repository"].casefold())
            identity = data["repo_node_id"]
            require(identity is None or text(identity), "Invalid repository identity")
            if identity:
                require(identity not in identities, "Duplicate repository identity")
                identities.add(identity)
            require(data["category"] in categories, "Unknown category")
            for key in ("tags", "forms", "platforms", "alternatives"):
                require(strings(data[key]), f"Invalid {key}")
            require(all(SLUG.fullmatch(tag) for tag in data["tags"]), "Tags must be stable lowercase IDs")
            for key in ("forms", "platforms"):
                require(set(data[key]) <= set(taxonomy[key]), f"Unknown {key}")
            require(localized(data["summary"], lambda v: isinstance(v, str)), "Invalid bilingual summary")
            for key in ("aliases", "use_cases"):
                require(localized(data[key], strings), f"Invalid bilingual {key}")
            editorial = data["editorial"]
            require(editorial["status"] in ("draft", "reviewed"), "Invalid editorial status")
            require(editorial["verification_level"] in ("docs", "tested"), "Invalid verification level")
            require(localized(editorial["reviewed_at"], lambda v: v is None or bool(timestamp(v))), "Invalid review timestamps")
            bodies = {locale: (directory / f"README.{locale}.md").read_text(encoding="utf-8") for locale in LOCALES}
            require(all(text(body) for body in bodies.values()), "Both language documents are required")
            license_review = data["license_review"]
            require(type(license_review["osi_approved"]) is bool, "osi_approved must be boolean")
            for key in ("spdx", "license_sha256"):
                require(license_review[key] is None or text(license_review[key]), f"Invalid license {key}")
            require(fingerprint(license_review["license_sha256"]), "Invalid license SHA-256")
            require(license_review["source_url"] is None or url(license_review["source_url"]), "Invalid license URL")
            if license_review["reviewed_at"] is not None:
                timestamp(license_review["reviewed_at"])
            require(isinstance(data["activity_evidence"], list), "Invalid activity evidence")
            for item in data["activity_evidence"]:
                require(item["type"] in ("commit", "merged_pr", "release"), "Invalid activity type")
                require(url(item["url"]) and localized(item["reason"], text), "Activity needs a URL and bilingual reason")
                require(type(item["qualifies"]) is bool, "Activity qualifies must be boolean")
                require(timestamp(item["occurred_at"]) <= timestamp(item["reviewed_at"]), "Activity reviewed before it occurred")
            require(isinstance(data["sources"], list), "Invalid sources")
            for item in data["sources"]:
                require(url(item["url"]) and localized(item["supports"], text), "Invalid source")
                timestamp(item["accessed_at"])
            if editorial["status"] == "reviewed":
                require(localized(data["summary"], text), "Reviewed entries need both summaries")
                require(all(data["use_cases"][k] and editorial["reviewed_at"][k] for k in LOCALES), "Review both languages and supply use cases")
                require(data["sources"], "Reviewed entries need sources")
                require(not any("{{" in body for body in bodies.values()) and "{{" not in data["name"], "Remove template placeholders before review")
            snapshot_path = root / "data/github" / f"{data['id']}.json"
            snapshot = read_json(snapshot_path) if snapshot_path.exists() else None
            if snapshot is not None:
                require(type(snapshot["schema_version"]) is int and snapshot["schema_version"] == 1, "Invalid snapshot version")
                require(REPOSITORY.fullmatch(snapshot["full_name"]), "Invalid snapshot repository")
                for key in ("repo_node_id", "license_spdx", "license_sha256"):
                    require(snapshot[key] is None or text(snapshot[key]), f"Invalid snapshot {key}")
                require(fingerprint(snapshot["license_sha256"]), "Invalid snapshot license SHA-256")
                require(snapshot["stargazers_count"] is None or (type(snapshot["stargazers_count"]) is int and snapshot["stargazers_count"] >= 0), "Invalid Star count")
                for key in ("archived", "disabled"):
                    require(snapshot[key] is None or type(snapshot[key]) is bool, f"Invalid snapshot {key}")
                require(snapshot["visibility"] in (None, "public", "private", "internal"), "Invalid visibility")
                if snapshot["last_success_at"] is not None:
                    timestamp(snapshot["last_success_at"])
            entries.append({"metadata": data, "bodies": bodies, "snapshot": snapshot})
        except (KeyError, TypeError, OSError, CatalogError) as error:
            raise CatalogError(f"{directory}: {error}") from error
    ids = {entry["metadata"]["id"] for entry in entries}
    for entry in entries:
        data = entry["metadata"]
        require(data["id"] not in data["alternatives"] and set(data["alternatives"]) <= ids, f"{data['id']}: invalid alternative reference")
    for path in (root / "data/github").glob("*.json"):
        require(path.stem in ids, f"Orphan snapshot: {path}")
    return policy, taxonomy, entries


def eligibility(entry, policy, now):
    data, snapshot = entry["metadata"], entry["snapshot"]
    result = lambda status, *reasons: {"status": status, "reasons": list(reasons)}
    if not snapshot or any(snapshot.get(k) is None for k in ("last_success_at", "repo_node_id", "stargazers_count", "archived", "disabled", "visibility")):
        return result("unknown", "snapshot_missing_or_incomplete")
    age = now - timestamp(snapshot["last_success_at"])
    if age < timedelta(0) or age > timedelta(days=policy["snapshot_max_age_days"]):
        return result("unknown", "snapshot_not_current")
    if snapshot["repo_node_id"] != data["repo_node_id"] or snapshot["full_name"].casefold() != data["repository"].casefold():
        return result("unknown", "repository_identity_changed")
    license_review = data["license_review"]
    if (not all(license_review.get(k) for k in ("spdx", "license_sha256", "source_url", "reviewed_at"))
            or snapshot["license_spdx"] in (None, "NOASSERTION")
            or snapshot["license_spdx"] != license_review["spdx"]
            or snapshot["license_sha256"] != license_review["license_sha256"]
            or timestamp(license_review["reviewed_at"]) > now):
        return result("unknown", "license_needs_review")
    reasons = []
    for failed, reason in ((snapshot["stargazers_count"] < policy["min_stars"], "below_star_threshold"),
                           (snapshot["archived"], "archived"), (snapshot["disabled"], "disabled"),
                           (snapshot["visibility"] != "public", "not_public"),
                           (not license_review["osi_approved"], "license_not_approved")):
        if failed:
            reasons.append(reason)
    if reasons:
        return result("ineligible", *reasons)
    editorial = data["editorial"]
    if editorial["status"] != "reviewed" or any(not editorial["reviewed_at"][k] or timestamp(editorial["reviewed_at"][k]) > now for k in LOCALES):
        return result("needs_review", "bilingual_content_needs_review")
    cutoff = months_before(now, policy["activity_months"])
    if not any(item["qualifies"] and cutoff <= timestamp(item["occurred_at"]) <= now and timestamp(item["reviewed_at"]) <= now for item in data["activity_evidence"]):
        return result("needs_review", "activity_evidence_expired_or_missing")
    return result("eligible")


def normalize(value):
    return unicodedata.normalize("NFKC", value).casefold()


def search(entries, policy, taxonomy, now, query="", include_all=False, category=None, platform=None):
    matches = []
    for entry in entries:
        data = entry["metadata"]
        state = eligibility(entry, policy, now)
        if (not include_all and state["status"] != "eligible") or (category and data["category"] != category) or (platform and platform not in data["platforms"]):
            continue
        names = [data["id"], data["name"], data["repository"], *sum(data["aliases"].values(), [])]
        phrases = [*data["tags"], *sum(data["use_cases"].values(), []), *taxonomy["categories"][data["category"]].values()]
        haystack = normalize("\n".join(names + phrases + list(data["summary"].values()) + list(entry["bodies"].values())))
        if not all(normalize(term) in haystack for term in query.split()):
            continue
        rank = 0 if normalize(query) in map(normalize, names) else 1 if normalize(query) in map(normalize, phrases) else 2
        matches.append((rank, data["id"], entry, state))
    return sorted(matches, key=lambda item: item[:2])


def write_text(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent, delete=False) as handle:
        temporary = Path(handle.name)
        handle.write(content)
    try:
        temporary.replace(path)
    finally:
        temporary.unlink(missing_ok=True)


def build(root, now):
    policy, taxonomy, entries = load(root)
    rows = [{**entry["metadata"], "snapshot": entry["snapshot"], "eligibility": eligibility(entry, policy, now),
             "documents": {k: f"tools/{entry['metadata']['id']}/README.{k}.md" for k in LOCALES}} for entry in entries]
    output = {"schema_version": 1, "evaluated_at": iso(now), "policy": policy, "entries": rows}
    rendered = {}
    for locale in LOCALES:
        zh = locale == "zh-CN"
        lines = ["# 开源工具目录" if zh else "# Open source tool catalog", "", "[English](README.en.md)" if zh else "[简体中文](README.md)", "",
                 ("评估时间：" if zh else "Evaluated at: ") + iso(now), "",
                 "此索引是构建时的快照。本地 search 命令会重新评估资格。" if zh else "This index is a build-time snapshot. Local search evaluates eligibility again.", ""]
        visible = [row for row in rows if row["eligibility"]["status"] == "eligible"]
        if not visible:
            lines += ["暂无符合收录条件的词条。" if zh else "No entries currently meet the inclusion criteria.", ""]
        for category, labels in taxonomy["categories"].items():
            lines += ["## " + labels[locale], ""]
            for row in visible:
                if row["category"] == category:
                    # Plain text rendering prevents metadata from creating Markdown links.
                    safe = lambda s: re.sub(r"([\\`*_{}\[\]<>()#|!])", r"\\\1", s).replace("\n", " ")
                    lines += [f"- [{safe(row['name'])}](../{row['documents'][locale]}) — {safe(row['summary'][locale])}"]
            lines += [""]
        rendered[root / "indexes" / ("README.md" if zh else "README.en.md")] = "\n".join(lines)
    rendered[root / "dist/catalog.json"] = json.dumps(output, ensure_ascii=False, indent=2) + "\n"
    # All inputs are validated and rendered before replacing any output.
    for path, content in rendered.items():
        write_text(path, content)
    return len(rows)


def new_entry(root, identifier, repository):
    require(SLUG.fullmatch(identifier), "Tool id must be lowercase words separated by hyphens")
    require(REPOSITORY.fullmatch(repository) and repository.split('/')[1] not in ('.', '..'), "Use a GitHub owner/repository name")
    _, _, entries = load(root)
    require(all(e["metadata"]["repository"].casefold() != repository.casefold() for e in entries), "Repository already exists")
    destination = root / "tools" / identifier
    require(not destination.exists(), "Tool id already exists")
    with tempfile.TemporaryDirectory(prefix=".draft-", dir=root / "tools") as temporary:
        source = Path(temporary) / identifier
        shutil.copytree(root / "templates/tool", source)
        data = read_json(source / "tool.json")
        data.update(id=identifier, name=identifier, repository=repository)
        (source / "tool.json").write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        for locale in LOCALES:
            path = source / f"README.{locale}.md"
            path.write_text(path.read_text(encoding="utf-8").replace("{{name}}", identifier), encoding="utf-8")
        source.rename(destination)
    return destination


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT, help="Catalog root (default: this repository)")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("validate", help="Validate all entries, both languages and snapshots")
    creator = commands.add_parser("new", help="Create a bilingual draft")
    creator.add_argument("id")
    creator.add_argument("--repository", required=True)
    for command in ("build", "search"):
        sub = commands.add_parser(command)
        sub.add_argument("--as-of", help="ISO timestamp with timezone, for reproducible evaluation")
        if command == "search":
            sub.add_argument("query", nargs="?", default="")
            sub.add_argument("--lang", choices=LOCALES, default="zh-CN")
            sub.add_argument("--all", action="store_true", help="Include drafts and entries that do not currently qualify")
            sub.add_argument("--category")
            sub.add_argument("--platform")
            sub.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)
    try:
        root = args.root.resolve()
        if args.command == "new":
            print(new_entry(root, args.id, args.repository))
        elif args.command == "validate":
            print(f"Valid: {len(load(root)[2])} entries / 词条")
        else:
            now = timestamp(args.as_of) if args.as_of else datetime.now(timezone.utc)
            if args.command == "build":
                print(f"Built: {build(root, now)} entries / 词条; indexes/ + dist/catalog.json")
            else:
                policy, taxonomy, entries = load(root)
                require(not args.category or args.category in taxonomy["categories"], "Unknown category")
                require(not args.platform or args.platform in taxonomy["platforms"], "Unknown platform")
                matches = search(entries, policy, taxonomy, now, args.query, args.all, args.category, args.platform)
                result = [{"id": e["metadata"]["id"], "name": e["metadata"]["name"], "summary": e["metadata"]["summary"][args.lang],
                           "eligibility": state, "document": f"tools/{e['metadata']['id']}/README.{args.lang}.md"} for _, _, e, state in matches]
                if args.json:
                    print(json.dumps({"evaluated_at": iso(now), "results": result}, ensure_ascii=False, indent=2))
                else:
                    print("\n".join(f"{r['name']} [{r['eligibility']['status']}] — {r['summary']}\n  {r['document']}" for r in result) or ("没有匹配的工具。" if args.lang == "zh-CN" else "No matching tools."))
    except (CatalogError, OSError) as error:
        print(f"Error / 错误: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
