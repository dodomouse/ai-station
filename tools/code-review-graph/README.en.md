# Code Review Graph

[简体中文](README.zh-CN.md) | English | [Import report](../../docs/imports/2026-11-15.en.md)

Builds an incremental local code graph for dependency queries, impact exploration and review context.

## Use cases

- Navigate relationships around a change
- Gather context for code review

## Requirements and limits

Language and framework coverage vary. Inferred relationships and conservative impact predictions are not runtime proof. Small edits can incur extra graph-context overhead. Optional embeddings and CI resources may cost extra. Graph results do not replace builds or tests.

## Getting started

Read the [official documentation](https://github.com/tirth8205/code-review-graph/blob/staging/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

## Related entries

- [Graphify](../graphify/README.en.md)
- [Serena](../serena/README.en.md)

Related entries can serve different needs; this list does not claim feature parity.

## Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](README.zh-CN.md) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:17.008Z. [Shared metadata](tool.json) contains license and commit evidence; the [snapshot](../../data/github/code-review-graph.json) contains Stars and repository state. Eligibility changes with time and is recalculated by local search.
