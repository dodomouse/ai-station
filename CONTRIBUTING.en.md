# Contributing

[简体中文](CONTRIBUTING.md) | English

Each tool has one stable ID, shared metadata and Chinese and English descriptions. Check existing entries before adding a tool. Repository renames, mirrors and translations should not create duplicate entries.

## Create a draft

Run this from the repository root, replacing the example values:

```bash
python3 scripts/catalog.py new example-tool --repository owner/repository
```

The command creates `tools/example-tool/` with `draft` status. Duplicate IDs or repositories cause an error. Existing entries are not overwritten.

## Write both descriptions

Edit the name, summaries, aliases, use cases, category and tags in `tool.json`. Write `README.zh-CN.md` and `README.en.md`. Both versions should convey the same features, limitations and degree of certainty; they do not need to be literal translations.

Explain the purpose, use cases, features, limitations, setup and alternatives. Preserve product names, commands, links and license identifiers. Remove template placeholders. Do not describe documentation claims as hands-on test results.

The `summary`, `aliases` and `use_cases` fields use `zh-CN` and `en` keys. Tags use stable lowercase English IDs. Put Chinese synonyms in aliases or use cases.

## Record evidence

Use the source, license and maintenance fields in the [format reference](docs/data-format.en.md).

Copy `templates/github-snapshot.json` to `data/github/<id>.json`. Verify the repository identity, stars, archive status and license against GitHub, then fill in the snapshot. The current tool does not collect data from the network.

Compute `license_sha256` from the raw bytes of the upstream license file. The entry and snapshot fingerprints must match. Set `osi_approved` to `true` only after checking the [OSI license list](https://opensource.org/licenses).

Maintenance evidence includes the event time, source URL, a reason in each language and the review time. Set `qualifies` to `true` after confirming meaningful maintenance. Keep it `false` for documentation-only changes or mechanical bot updates.

## Review the entry

After reviewing each language, set its `editorial.reviewed_at` timestamp. Then change `editorial.status` to `reviewed`.

Use `docs` or `tested` for `verification_level`. For hands-on testing, document the version, environment, steps and results in both descriptions.

Content review does not guarantee inclusion. Reviewed entries may leave the default catalog when snapshots or maintenance evidence expire, or when stars fall below the threshold.

## Validate changes

```bash
python3 scripts/catalog.py validate
python3 -m unittest discover -s tests -v
python3 scripts/catalog.py build
python3 scripts/catalog.py search --all --lang en --json
```

Check both indexes for correct links and summaries. Include updated `indexes/` files with content changes. `dist/` contains ignored build output. Do not edit generated indexes by hand.

## Update an existing tool

Keep the tool ID when a repository is renamed or transferred. Verify `repo_node_id` before updating its path. A different repository identity requires a new review. Update stars, archive status and detected license only in the snapshot.

Snapshots record the last successful check. A failed request must not overwrite successful data or advance `last_success_at`. Apply the same rule when maintaining snapshots manually.
