# Magpie

[简体中文](README.zh-CN.md) | English | [Import report](../../docs/imports/2026-11-15.en.md)

A local gateway that routes coding-agent requests across configured model providers and accounts, with optional failover and masking.

## Use cases

- Manage model routing
- Reuse configured accounts across supported clients

## Requirements and limits

It does not create free quota or bypass provider terms. Failover needs actual alternatives. Subscription discovery may read agent login files or Keychain; that requires deliberate configuration. Masking is off by default and may misclassify data. Optional telemetry exists. Compatibility and billing were not tested.

## Getting started

Read the [official documentation](https://github.com/yetone/magpie/blob/main/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

## Related entries

- [Orca](../orca/README.en.md)

Related entries can serve different needs; this list does not claim feature parity.

## Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](README.zh-CN.md) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:18.536Z. [Shared metadata](tool.json) contains license and commit evidence; the [snapshot](../../data/github/magpie.json) contains Stars and repository state. Eligibility changes with time and is recalculated by local search.
