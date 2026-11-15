# ai-station

**A bilingual open source tool dictionary, organized by use case and backed by sources.**

[简体中文](README.md) | English

ai-station catalogs useful tools hosted on GitHub. Each entry has Chinese and English descriptions covering use cases, features, limitations, getting started and alternatives. The catalog covers general-purpose tools, with AI as one category.

[Browse in English](indexes/README.en.md) · [浏览中文目录](indexes/README.md) · [Contributing](CONTRIBUTING.en.md) · [Data format](docs/data-format.en.md)

## Current status

The catalog contains 62 projects, 124 language documents and 62 GitHub snapshots. At the latest 2026-11-15 review, 35 qualified for the default catalog and 27 remained searchable candidates. See the [additions and refresh report](docs/imports/2026-11-15-additions.en.md) and [initial 59-entry import](docs/imports/2026-11-15.en.md). Automated GitHub collection, scheduled refresh and web search are not implemented.

## Inclusion criteria

The default catalog only lists tools that meet every condition:

- At least **1,000 GitHub stars**.
- Human-reviewed evidence of meaningful maintenance within the last **3 calendar months**.
- A public GitHub repository that is neither archived nor disabled.
- A reviewed open source license and reviewed content in both languages.
- A GitHub snapshot no more than **7 days** old at evaluation time.

Feature changes, bug fixes, merged pull requests and stable releases can provide maintenance evidence. Documentation-only changes and mechanical bot updates do not qualify on their own. Stars and activity are filters, not proof of quality.

Entries that no longer qualify remain in the repository and are available through `search --all`. Local search evaluates eligibility on each run. Markdown indexes show the build-time result and its evaluation timestamp.

## Categories

| Category | Typical uses |
| --- | --- |
| AI tools | Local inference, coding assistance, knowledge retrieval |
| Development | API debugging, code navigation, development environments |
| Terminal and shell | Command-line search, terminal interfaces, shell workflows |
| Data processing | Cleaning, conversion, querying, visualization |
| Automation | Batch processing, task orchestration, integration |
| Operations | Deployment, monitoring, logging, backups |
| Productivity | Notes, knowledge management, file organization |
| Images, audio and video | Editing, conversion, compression, recording |

## Local usage

Use Python 3.10 or later. No third-party packages are required. Run these commands from the repository root:

```bash
python3 scripts/catalog.py validate
python3 -m unittest discover -s tests -v
python3 scripts/catalog.py build
python3 scripts/catalog.py search "terminal" --lang en
python3 scripts/catalog.py search "终端" --lang en
```

Queries search content in both languages. `--lang` selects the summary language and the linked entry document.

```bash
python3 scripts/catalog.py search --category ai --platform linux --lang en
python3 scripts/catalog.py search --all --lang en --json
```

Use `search --all` to include candidates outside the default catalog. `build` generates two Markdown indexes and `dist/catalog.json`. Supply an evaluation time for a reproducible build:

```bash
python3 scripts/catalog.py build --as-of 2026-11-15T11:54:08.129868Z
```

## Add a tool

This command creates a draft. Replace `example-tool` and `owner/repository` with real values:

```bash
python3 scripts/catalog.py new example-tool --repository owner/repository
```

Fill in the shared metadata and both descriptions. Follow the [contribution guide](CONTRIBUTING.en.md) to add sources, license review, maintenance evidence and a repository snapshot. Drafts can pass structural validation. Default inclusion requires bilingual review and a successful eligibility evaluation.

## Repository structure

```text
config/                   Inclusion policy and bilingual categories
tools/<id>/              One directory per tool
   tool.json              Shared structured metadata
   README.zh-CN.md         Chinese description
   README.en.md            English description
data/github/<id>.json    GitHub snapshot
templates/               Entry and snapshot templates
scripts/catalog.py       Create, validate, build and search
indexes/                 Generated bilingual indexes
tests/                   Behavior and boundary tests
docs/                    Design and format references
```

Editors maintain the metadata and descriptions. Scripts generate the indexes. Star counts live in snapshots so translations do not maintain separate copies.

## Contributing

Read the [English contribution guide](CONTRIBUTING.en.md) or [中文贡献指南](CONTRIBUTING.md). Field definitions are in the [English format reference](docs/data-format.en.md) and [中文格式说明](docs/data-format.md).

Contributions can add real entries, improve translations, update maintenance evidence or explain alternatives. Mark documentation-based descriptions as documentation reviews.

## License

This repository uses the [Apache License 2.0](LICENSE). Listed tools retain their own licenses.
