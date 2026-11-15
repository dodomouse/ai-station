# easyquotation

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[shidenggui/easyquotation](https://github.com/shidenggui/easyquotation)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 数据处理 / Data processing |
| 状态 / Status | 候选 / Candidate |
| Star | 5478 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T11:46:23.180Z |

候选原因：缺少近期有效维护证据。
Candidate reason: Recent qualifying maintenance not established.

以上为历史核对结果，使用前请复核上游状态。 / This is a dated review; check the current upstream state before use.

## 中文

easyquotation 是读取股票行情的 Python 库。它封装新浪、腾讯和集思录的部分数据接口，向脚本返回行情字典。适合已有 Python 程序、只需要增加行情读取能力的用户。

当前保留为候选：默认分支最近提交为 2026-02-28 的文档更新，本次未发现三个月内的有效维护证据。Star 已达到门槛，具体数据见 [GitHub 快照](#review-evidence)。

### 适用场景

- 在 Python 脚本中读取单只、多只或全市场的行情快照。
- 获取文档列出的腾讯港股行情和日 K 线。
- 按数据源的访问条件读取集思录指数 ETF 数据。

### 主要功能

| 接口 | 官方文档描述的用途 |
| --- | --- |
| `easyquotation.use()` | 选择新浪、腾讯、港股、日 K 线或集思录适配器。 |
| `market_snapshot(prefix=True)` | 读取市场快照，并保留股票代码的市场前缀。 |
| `real()` | 请求一个或多个代码；指数和股票代码重合时需注意市场前缀。 |
| `update_stock_codes()` | 更新本地使用的全市场股票代码。 |
| `etfindex()` | 通过集思录适配器查询指数 ETF；文档注明不含黄金和货币 ETF。 |

接口范围来自[官方 README](https://github.com/shidenggui/easyquotation/blob/7778c1b9f93afb2ce2cf431de393fe690d4ec07c/README.md)。本次没有请求实际行情，不能据此保证各适配器目前均可用。

### 环境与限制

- 仓库的 `setup.py` 声明 Python `>=3.6`，主要运行依赖为 `requests`。这是包声明，不代表已验证所有 Python 版本组合。
- 数据来自外部服务，可能受到接口变化、登录、限流和网络条件影响。代码许可证不授予数据的再分发权。
- 集思录文档说明，未设置 Cookie 时可获取的数据受限。不要把账号 Cookie 写入公开代码或提交到仓库。
- “实时”和耗时描述属于上游接口定位及作者说明。本次未测量延迟、数据完整性或准确率。
- 本项目提供数据读取接口。券商下单、策略执行和回测不能由这些接口推导出来。
- 根目录 [LICENSE](https://github.com/shidenggui/easyquotation/blob/7778c1b9f93afb2ce2cf431de393fe690d4ec07c/LICENSE) 和 README 为 MIT，但 `setup.py` 仍写 BSD。元数据存在不一致，本词条按当前根许可证记录；采用某个发行包时还需核对包内许可。

### 开始使用

在自己的 Python 环境中按[官方安装说明](https://github.com/shidenggui/easyquotation#安装)安装包。以下是使用方式示例，本次未执行：

```bash
python -m pip install easyquotation
```

```python
import easyquotation

quotation = easyquotation.use("sina")
quotes = quotation.real(["sh000001", "sz000001"], prefix=True)
```

先核对结果中的时间、代码前缀和字段含义，再把数据接入自己的程序。

### 相关选择

- [Vibe Research](vibe-research.md#中文)提供研究工作台、报告和自选管理；easyquotation 侧重程序中的行情读取。
- [TradingAgents-CN](tradingagents-cn.md#中文)提供多智能体研究流程，且有独立的模型、数据库和许可要求。

以上为用途比较，未验证它们与 easyquotation 的直接集成。

### 复核说明

2026-11-15 核对默认分支、最近提交、发行列表、README、`setup.py` 与 MIT 文件。最近提交只新增项目协作说明，且早于活动窗口；发行列表为空。不把这些观察扩大为项目永远不可用的判断。

验证级别为 `docs`，未安装或请求行情。该项目列在目录的候选部分。证据见 [收录依据](#review-evidence)。

## English

easyquotation is a Python library for reading stock quotations. It wraps selected Sina, Tencent and Jisilu endpoints and returns quote dictionaries to Python programs. It suits users adding market-data retrieval to an existing script.

This entry remains a candidate. The latest default-branch commit is a documentation change dated 2026-02-28, and this review found no qualifying maintenance within three months. Stars meet the threshold; see the [GitHub snapshot](#review-evidence).

### Use cases

- Fetch single-symbol, multi-symbol or whole-market quotation snapshots in Python.
- Retrieve the Tencent Hong Kong quotes and daily bars described by the project.
- Query Jisilu index ETF data subject to that service's access conditions.

### Features

| Interface | Documented purpose |
| --- | --- |
| `easyquotation.use()` | Select a Sina, Tencent, Hong Kong quote, daily-bar or Jisilu adapter. |
| `market_snapshot(prefix=True)` | Fetch a market snapshot with market prefixes in symbol keys. |
| `real()` | Request one or more symbols, using prefixes to distinguish overlapping stock and index codes. |
| `update_stock_codes()` | Update the locally used market symbol list. |
| `etfindex()` | Query index ETFs through Jisilu; the documentation excludes gold and money-market ETFs. |

These interfaces are described in the [official README](https://github.com/shidenggui/easyquotation/blob/7778c1b9f93afb2ce2cf431de393fe690d4ec07c/README.md). No live quotation request was made during this review, so current adapter availability is unverified.

### Requirements and limits

- `setup.py` declares Python `>=3.6` and `requests` as the main runtime dependency. This does not establish tested compatibility across Python versions.
- External endpoints can change or impose authentication, rate limits and network restrictions. The software license does not grant data redistribution rights.
- Jisilu access is limited without a configured Cookie according to the documentation. Keep account cookies out of public code and version control.
- Real-time positioning and latency claims come from the project. This review did not measure delay, completeness or accuracy.
- Data retrieval does not establish broker order placement, strategy execution or backtesting capabilities.
- The root [LICENSE](https://github.com/shidenggui/easyquotation/blob/7778c1b9f93afb2ce2cf431de393fe690d4ec07c/LICENSE) and README use MIT, while `setup.py` still labels the package BSD. This entry records the root license and flags the discrepancy. Check the license bundled with any particular release.

### Getting started

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

### Related choices

- [Vibe Research](vibe-research.md#english) provides a research workspace, reports and watchlists; easyquotation focuses on data retrieval inside programs.
- [TradingAgents-CN](tradingagents-cn.md#english) provides multi-agent research with its own model, database and licensing requirements.

These are purpose comparisons. Direct integration with easyquotation was not verified.

### Review

On 2026-11-15, this review checked the default branch, recent commits, release list, README, `setup.py` and MIT file. The latest commit only adds project guidance and predates the activity window; the release list is empty. These observations do not establish that every interface is unusable.

Verification level: `docs`. No package was installed and no quotes were requested. The candidate is listed in the main index. Evidence is in [review evidence](#review-evidence).

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

保留原始核对数据，便于追溯来源、许可和维护证据。 / Original review data preserves source, license and maintenance evidence.

```json
{
  "evaluated_at": "2026-11-15T11:54:08.129868Z",
  "eligibility": {
    "status": "needs_review",
    "reasons": [
      "activity_evidence_expired_or_missing"
    ]
  },
  "metadata": {
    "schema_version": 1,
    "id": "easyquotation",
    "name": "easyquotation",
    "repository": "shidenggui/easyquotation",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnk0ODQ4ODQzMA==",
    "category": "data",
    "tags": [
      "python-library",
      "market-data",
      "finance"
    ],
    "forms": [],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "股票行情读取库",
        "新浪腾讯行情"
      ],
      "en": [
        "Easy Quotation",
        "Python stock quotations"
      ]
    },
    "summary": {
      "zh-CN": "封装新浪、腾讯和集思录部分接口的 Python 行情库，用于单只、多只股票及市场快照读取。",
      "en": "A Python library wrapping selected Sina, Tencent and Jisilu endpoints for symbol quotes and market snapshots."
    },
    "use_cases": {
      "zh-CN": [
        "在 Python 程序中读取股票行情快照",
        "读取文档列出的腾讯港股行情和日 K 线",
        "按访问条件查询集思录指数 ETF 数据"
      ],
      "en": [
        "Read stock quotation snapshots in Python",
        "Retrieve documented Tencent Hong Kong quotes and daily bars",
        "Query Jisilu index ETF data subject to access conditions"
      ]
    },
    "alternatives": [
      "vibe-research",
      "tradingagents-cn"
    ],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-15T11:54:08.129868Z",
        "en": "2026-11-15T11:54:08.129868Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "0f9dab4072cc38aa592391e18f85628af237fc133db318f5b4dc94268bb58f17",
      "source_url": "https://github.com/shidenggui/easyquotation/blob/7778c1b9f93afb2ce2cf431de393fe690d4ec07c/LICENSE",
      "reviewed_at": "2026-11-15T11:54:08.129868Z"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-02-28T07:19:16Z",
        "reviewed_at": "2026-11-15T11:54:08.129868Z",
        "url": "https://github.com/shidenggui/easyquotation/commit/7778c1b9f93afb2ce2cf431de393fe690d4ec07c",
        "qualifies": false,
        "reason": {
          "zh-CN": "最近提交只增加项目协作说明，属于文档更新，且早于三个月窗口；不作为有效维护证据。",
          "en": "The latest commit only adds project guidance and predates the three-month window; it does not qualify as functional maintenance."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/shidenggui/easyquotation/blob/7778c1b9f93afb2ce2cf431de393fe690d4ec07c/README.md",
        "accessed_at": "2026-11-15T11:54:08.129868Z",
        "supports": {
          "zh-CN": "官方用途、功能范围、入门和限制。",
          "en": "Official purpose, feature scope, setup and limitations."
        }
      },
      {
        "url": "https://github.com/shidenggui/easyquotation/blob/7778c1b9f93afb2ce2cf431de393fe690d4ec07c/LICENSE",
        "accessed_at": "2026-11-15T11:54:08.129868Z",
        "supports": {
          "zh-CN": "当前根许可证及适用范围。",
          "en": "Current root license and its scope."
        }
      },
      {
        "url": "https://api.github.com/repos/shidenggui/easyquotation",
        "accessed_at": "2026-11-15T11:46:23.180Z",
        "supports": {
          "zh-CN": "本次仓库身份、Star 和公开状态。",
          "en": "Repository identity, Stars and public state at review time."
        }
      },
      {
        "url": "https://opensource.org/license/mit",
        "accessed_at": "2026-11-15T11:54:08.129868Z",
        "supports": {
          "zh-CN": "MIT 为 OSI 批准的许可证；与根文件许可条款对照。",
          "en": "MIT is OSI-approved; its permission terms were compared with the root file."
        }
      },
      {
        "url": "https://github.com/shidenggui/easyquotation/blob/7778c1b9f93afb2ce2cf431de393fe690d4ec07c/setup.py",
        "accessed_at": "2026-11-15T11:54:08.129868Z",
        "supports": {
          "zh-CN": "Python 下限、requests 依赖及 BSD 标记差异。",
          "en": "Python requirement, requests dependency and conflicting BSD label."
        }
      }
    ],
    "catalog_review": {
      "reviewed_at": "2026-11-15T11:54:08.129868Z",
      "notes": {
        "zh-CN": "默认分支最近提交为 2026-02-28 的文档更新，未满足三个月有效维护要求。根 LICENSE 为 MIT，setup.py 的 BSD 标记与之不一致。",
        "en": "The latest default-branch commit is documentation dated 2026-02-28, outside the activity window. The root MIT license differs from the BSD label in setup.py."
      }
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "MDEwOlJlcG9zaXRvcnk0ODQ4ODQzMA==",
    "full_name": "shidenggui/easyquotation",
    "stargazers_count": 5478,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "0f9dab4072cc38aa592391e18f85628af237fc133db318f5b4dc94268bb58f17",
    "last_success_at": "2026-11-15T11:46:23.180Z"
  }
}
```

</details>
