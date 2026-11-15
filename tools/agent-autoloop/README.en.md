# Agent Autoloop

[简体中文](README.zh-CN.md) | English | [Import report](../../docs/imports/2026-11-15.en.md)

A local event and scheduling service that dispatches tasks to installed command-line agents and records their results.

## Use cases

- Run scheduled agent tasks
- React to selected events and follow up on pending work

## Requirements and limits

Requires Node.js 24+, Git, curl and an authenticated local agent. Some GitHub delivery paths separately require GitHub CLI. The host must stay running; webhooks need reachability. Retries can repeat actions, so delivery requires state checks. This import did not install the service or authorize external actions.

## Getting started

Read the [official documentation](https://github.com/KKKKhazix/agent-autoloop/blob/main/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

## Related entries

- [cc-connect](../cc-connect/README.en.md)

Related entries can serve different needs; this list does not claim feature parity.

## Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](README.zh-CN.md) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:18.663Z. [Shared metadata](tool.json) contains license and commit evidence; the [snapshot](../../data/github/agent-autoloop.json) contains Stars and repository state. Eligibility changes with time and is recalculated by local search.
