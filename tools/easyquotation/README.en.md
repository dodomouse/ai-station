# easyquotation

[简体中文](README.zh-CN.md) | English

easyquotation is a Python library for reading stock quotations. It wraps selected Sina, Tencent and Jisilu endpoints and returns quote dictionaries to Python programs. It suits users adding market-data retrieval to an existing script.

This entry remains a candidate. The latest default-branch commit is a documentation change dated 2026-02-28, and this review found no qualifying maintenance within three months. Stars meet the threshold; see the [GitHub snapshot](../../data/github/easyquotation.json).

## Use cases

- Fetch single-symbol, multi-symbol or whole-market quotation snapshots in Python.
- Retrieve the Tencent Hong Kong quotes and daily bars described by the project.
- Query Jisilu index ETF data subject to that service's access conditions.

## Features

| Interface | Documented purpose |
| --- | --- |
| `easyquotation.use()` | Select a Sina, Tencent, Hong Kong quote, daily-bar or Jisilu adapter. |
| `market_snapshot(prefix=True)` | Fetch a market snapshot with market prefixes in symbol keys. |
| `real()` | Request one or more symbols, using prefixes to distinguish overlapping stock and index codes. |
| `update_stock_codes()` | Update the locally used market symbol list. |
| `etfindex()` | Query index ETFs through Jisilu; the documentation excludes gold and money-market ETFs. |

These interfaces are described in the [official README](https://github.com/shidenggui/easyquotation/blob/7778c1b9f93afb2ce2cf431de393fe690d4ec07c/README.md). No live quotation request was made during this review, so current adapter availability is unverified.

## Requirements and limits

- `setup.py` declares Python `>=3.6` and `requests` as the main runtime dependency. This does not establish tested compatibility across Python versions.
- External endpoints can change or impose authentication, rate limits and network restrictions. The software license does not grant data redistribution rights.
- Jisilu access is limited without a configured Cookie according to the documentation. Keep account cookies out of public code and version control.
- Real-time positioning and latency claims come from the project. This review did not measure delay, completeness or accuracy.
- Data retrieval does not establish broker order placement, strategy execution or backtesting capabilities.
- The root [LICENSE](https://github.com/shidenggui/easyquotation/blob/7778c1b9f93afb2ce2cf431de393fe690d4ec07c/LICENSE) and README use MIT, while `setup.py` still labels the package BSD. This entry records the root license and flags the discrepancy. Check the license bundled with any particular release.

## Getting started

Follow the [official installation instructions](https://github.com/shidenggui/easyquotation#安装) in your Python environment. This example illustrates the API and was not executed here:

```bash
python -m pip install easyquotation
```

```python
import easyquotation

quotation = easyquotation.use("sina")
quotes = quotation.real(["sh000001", "sz000001"], prefix=True)
```

Check timestamps, market prefixes and field meanings before integrating the results.

## Related choices

- [Vibe Research](../vibe-research/README.en.md) provides a research workspace, reports and watchlists; easyquotation focuses on data retrieval inside programs.
- [TradingAgents-CN](../tradingagents-cn/README.en.md) provides multi-agent research with its own model, database and licensing requirements.

These are purpose comparisons. Direct integration with easyquotation was not verified.

## Review

On 2026-11-15, this review checked the default branch, recent commits, release list, README, `setup.py` and MIT file. The latest commit only adds project guidance and predates the activity window; the release list is empty. These observations do not establish that every interface is unusable.

Verification level: `docs`. No package was installed and no quotes were requested. Use `search easyquotation --all` to find the candidate. Evidence is in [tool.json](tool.json).
