# Data format

[简体中文](data-format.md) | English

Each tool lives in `tools/<id>/`, containing `tool.json`, `README.zh-CN.md` and `README.en.md`. Repository data lives in `data/github/<id>.json`. JSON files use UTF-8 and must not contain duplicate keys.

## Shared metadata

See the complete [template](../templates/tool/tool.json). Retain all fields. Use `null` for unknown values where the template allows it.

| Field | Type and purpose |
| --- | --- |
| `schema_version` | Integer; currently `1` |
| `id` | Lowercase letters or digits separated by hyphens; matches the directory name |
| `name` | Official product name, usually untranslated |
| `repository` | GitHub `owner/repository` |
| `repo_node_id` | GitHub repository `node_id`, or `null` before verification |
| `category` | One category ID from `config/taxonomy.json` |
| `tags` | Unique lowercase tag IDs, such as `backup` |
| `forms`, `platforms` | Unique arrays using the taxonomy values |
| `summary` | Strings keyed by `zh-CN` and `en` |
| `aliases`, `use_cases` | String arrays keyed by `zh-CN` and `en` |
| `alternatives` | Existing tool IDs; no self-reference |
| `editorial` | Content status, review dates for both languages and review method |
| `license_review` | Human license review |
| `activity_evidence` | Maintenance evidence array |
| `sources` | Sources supporting features, limitations and other descriptions |

`editorial.status` is `draft` or `reviewed`. `reviewed_at` contains a timestamp for each language. `verification_level` is `docs` or `tested`.

Drafts may have empty summaries, use cases and evidence, and an unknown repository identity. Both description files must exist. Reviewed entries require summaries, use cases and review dates in both languages, plus at least one source. Remove `{{...}}` placeholders from descriptions before review.

Validation checks structure and recorded evidence. Editors remain responsible for factual accuracy, translation equivalence and the meaning of maintenance activity.

## License review

`license_review` contains `spdx`, `osi_approved`, `license_sha256`, `source_url` and `reviewed_at`. The SPDX identifier and file fingerprint must match the snapshot. Compute `license_sha256` from the raw bytes of the upstream license file and use a 64-character lowercase hexadecimal string.

An unknown license identifier, missing review or changed fingerprint prevents default inclusion. `osi_approved` records a human judgment; the program does not interpret license terms.

## Maintenance evidence

This example shows the fields. Replace its dates and URL with verified values:

```json
{
  "type": "merged_pr",
  "occurred_at": "2026-11-01T10:00:00Z",
  "reviewed_at": "2026-11-02T10:00:00Z",
  "url": "https://github.com/owner/repository/pull/123",
  "reason": {
    "zh-CN": "修复文件同步时的重复写入问题。",
    "en": "Fixes duplicate writes during file synchronization."
  },
  "qualifies": true
}
```

`type` supports `commit`, `merged_pr` and `release`. `occurred_at` is the actual event time, not the date the entry was added. `reviewed_at` cannot precede the event.

Feature changes and bug fixes must reach the default branch or an explicitly maintained release branch. Releases must be stable. Evidence with `qualifies=false` is retained but cannot establish eligibility.

## Content sources

Each source has an HTTPS `url`, a timezone-aware `accessed_at` and bilingual `supports` text:

```json
{
  "url": "https://github.com/owner/repository",
  "accessed_at": "2026-11-02T10:00:00Z",
  "supports": {
    "zh-CN": "安装方法与平台支持。",
    "en": "Installation and supported platforms."
  }
}
```

## GitHub snapshot

See the [snapshot template](../templates/github-snapshot.json).

- `repo_node_id` is the GitHub repository `node_id`, bound to the entry.
- `full_name` is `owner/repository`, compared without case sensitivity.
- `stargazers_count` is a nonnegative integer, or `null` when unknown.
- `archived` and `disabled` are booleans, or `null` when unknown.
- `visibility` is `public`, `private`, `internal` or `null`.
- `license_spdx` and `license_sha256` identify the license and its file fingerprint.
- `last_success_at` records when this snapshot was successfully verified.

Snapshots with unknown fields can pass structural validation, but the entry remains `unknown`. Orphan snapshots, duplicate repository names and duplicate repository identities fail validation.

## Eligibility and time

| Status | Evaluation order and meaning |
| --- | --- |
| `unknown` | Missing, incomplete, expired or future snapshot; repository identity or license needs review |
| `ineligible` | Available data fails the star, visibility, archive or open source requirements |
| `needs_review` | Bilingual content needs review, or no qualifying maintenance evidence remains in the window |
| `eligible` | All conditions pass; shown in default search and indexes |

Timestamps must include a timezone and are normalized to UTC. The activity window starts 3 calendar months before evaluation. Month-end dates clamp to the last day of the target month. Both endpoints are inclusive. A snapshot exactly 7 days old is valid; an older one is not.

Thresholds live in `config/policy.json`. Search uses the current time. Tests and builds can specify `--as-of` for reproducibility. Future activities or review dates cannot establish eligibility.

## Search and generated output

Search covers names, aliases, summaries, use cases, category labels, tags and descriptions in both languages. It ignores English case and normalizes full-width characters. Space-separated terms must all match; continuous Chinese phrases use substring matching. Editors maintain aliases; queries are not translated automatically.

Exact name or alias matches rank first, then exact use cases or tags. Other matches sort by stable ID. Filters include `--category` and `--platform`. `--lang` only changes the display language.

`build` validates all inputs before generating two Markdown indexes and `dist/catalog.json`. JSON includes every entry and its eligibility reasons. Markdown includes only `eligible` entries. Input validation failures preserve existing output. Each file is replaced atomically; the set of output files is not a transaction.

`dist/catalog.json` is an export, not yet a web full-text search index. A website, automatic collection and scheduled tasks remain future work.
