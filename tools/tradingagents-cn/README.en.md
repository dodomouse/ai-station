# TradingAgents-CN

[简体中文](README.zh-CN.md) | English

TradingAgents-CN is a multi-agent research assistant for Chinese A-shares. Its current default branch, `v3.0`, is the Community Edition, with single-stock research, topic research, natural-language screening, learning material and paper trading. Several model roles organize analysis and discussion.

This entry remains a reference candidate because licensing differs by component. Some directories use Apache-2.0, while the application layer is proprietary source-available code. The complete Community Edition therefore cannot be described as wholly open-source software. GitHub reports `NOASSERTION`, which the existing catalog records as eligibility `unknown`.

## Use cases

- Study how multiple agents organize A-share analysis and debate.
- Structure research questions through stock, topic and screening workflows.
- Explore the Community Edition's courses, skill management and paper trading.

## Community features

| Area | Scope described by the official README |
| --- | --- |
| Single-stock research | Multiple analyst roles, debate, five analysis-depth levels and scenario-based views. |
| General research and screening | Natural-language questions, condition-based screening and candidate stock pools. |
| Assistant | Web search, tool calls and project-level memory. |
| Skill center | Creation and management of custom data-retrieval skills. |
| Learning and simulation | Community courses, guides, paper trading and review. |

The project lists the custom Agent workshop, strategy system, scheduled or batch analysis, professional Word/PDF exports and advanced courses as Pro features. They are not counted as Community features here. See the [current README](https://github.com/hsliuping/TradingAgents-CN/blob/51060a7682cf51810b4bc3a704829438d18cd8dc/README.md).

## Requirements, costs and limits

- The README specifies Python 3.11, Node.js 18+, MongoDB 7.0+ and Redis 6+. Databases must be installed separately.
- The backend uses FastAPI and the frontend Vue 3. Database connections, authentication settings and model services require configuration.
- `pyproject.toml` declares Python `>=3.10`, which differs from the README's 3.11 baseline. Lower-version compatibility was not tested; the starting instructions here follow the README.
- Model APIs, data access, hosting and databases can incur separate costs. Source availability does not make those services free.
- The current README limits the supported research market to A-shares. Older descriptions or installed dependencies do not establish support for other markets.
- Paper trading does not establish live brokerage execution. The project frames output as learning and research material and excludes target-price or trade-timing instructions.
- Data quality, report accuracy, research effectiveness and investment returns were not validated here.

## License scope

The [root license](https://github.com/hsliuping/TradingAgents-CN/blob/51060a7682cf51810b4bc3a704829438d18cd8dc/LICENSE) separates two groups:

| Scope | Stated terms |
| --- | --- |
| `tradingagents/`, `cli/`, `docs/`, `tests/`, `web/` and root configuration | Apache-2.0. |
| `app/`, `frontend/` and `core/` | Proprietary source-available components allowing personal use, evaluation and education, with redistribution and commercial-use restrictions. |

Commercial permission must be obtained separately under the upstream terms. This is a summary of the project's statements, not authorization for a particular use.

## Getting started

1. Read the Community [README](https://github.com/hsliuping/TradingAgents-CN/tree/v3.0#readme) and [license scope](https://github.com/hsliuping/TradingAgents-CN/blob/v3.0/LICENSE) for the intended version and use.
2. Prepare Python, Node.js, MongoDB and Redis as documented.
3. Configure `.env` in your own environment and follow the upstream frontend/backend startup steps.
4. After login, configure model access and required data sources, then inspect the output from one research question.

This import did not run the application, configure credentials, call models or execute paper trades.

## Related choices

- [Vibe Research](../vibe-research/README.en.md) focuses on watchlists, holdings, report storage and research workflows.
- [AI Berkshire](../ai-berkshire/README.en.md) supplies research skills for coding assistants and has a different setup model.
- [easyquotation](../easyquotation/README.en.md) retrieves market data inside Python programs without the full research interface described above.

These comparisons do not establish feature parity or tested integration.

## Review

On 2026-11-15, this review checked the default branch, README, component licenses, Python package declaration and the Community Edition's 2026-09-22 initial commit. That commit includes application startup and model-capability configuration code, providing functional activity within the window. A newer repository push date is not used as a substitute.

Verification level: `docs`. Only documentation and selected code were inspected; license scope keeps the entry outside the default catalog. See [shared metadata](tool.json) and the [GitHub snapshot](../../data/github/tradingagents-cn.json).
