# TradingAgents

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 数据处理 / Data processing |
| 状态 / Status | 已收录 / Included |
| Star | 122872 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-17T04:07:37.951043+00:00 |

## 中文

通过多种大模型角色组织金融研究，包括分析师、研究员和风险管理角色。

### 用途与功能

- 组合基本面、新闻、情绪和技术分析报告。
- 以多空讨论和风险评估整理研究结论。
- 提供 CLI、Python 接口和按日期运行的回测流程。

### 环境与限制

需要 Python 3.11+ 或 Docker，以及所选模型和市场数据源的访问权限。项目定位为研究框架，结果依赖数据和模型，不能视为收益保证。它与目录中的 TradingAgents-CN 是不同仓库。

### 开始使用

按 README 配置模型及数据源，使用 CLI 指定一个标的和研究日期，核对报告引用的数据。

参阅[官方 README](https://github.com/TauricResearch/TradingAgents/blob/9fa1196fffbcfd9de5146d2dd2869df84ab99838/README.md)。

### 收录与来源

适合研究多角色大模型如何汇总金融信息，并比较不同日期和配置下的输出。

维护证据：[将财务报表工具的频率参数限制为 annual 或 quarterly，避免把无效频率静默解释为年度数据。](https://github.com/TauricResearch/TradingAgents/commit/bf7f4b55a300ede4a8106022044cc473fcbe85af)（2026-10-27）。

发现于 [GitHub 月榜](https://github.com/trending/python?since=monthly)。2026-11-17 的榜单记录新增 11,824 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Organizes financial research through model-based analyst, researcher and risk-management roles.

### Uses and features

- Combines fundamental, news, sentiment and technical reports.
- Uses bull/bear discussion and risk assessment to organize findings.
- Provides a CLI, Python interface and date-based backtesting workflows.

### Requirements and limits

Requires Python 3.11+ or Docker and access to selected models and market-data sources. This is a research framework whose results depend on data and models, without a return guarantee. It is a separate repository from the listed TradingAgents-CN project.

### Getting started

Configure models and data sources from the README, select an instrument and research date in the CLI, then check the report against its source data.

See the [official README](https://github.com/TauricResearch/TradingAgents/blob/9fa1196fffbcfd9de5146d2dd2869df84ab99838/README.md).

### Review and provenance

Useful for studying how multiple model roles aggregate financial information and comparing outputs across dates and configurations.

Maintenance evidence: [Restricts financial-statement tool frequency to annual or quarterly instead of silently treating invalid values as annual data.](https://github.com/TauricResearch/TradingAgents/commit/bf7f4b55a300ede4a8106022044cc473fcbe85af) (2026-10-27).

Discovered in [GitHub monthly Trending](https://github.com/trending/python?since=monthly), which recorded 11,824 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:07:37.951043+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "tradingagents",
    "name": "TradingAgents",
    "repository": "TauricResearch/TradingAgents",
    "repo_node_id": "R_kgDONjF_4A",
    "category": "data",
    "summary": {
      "zh-CN": "通过多种大模型角色组织金融研究，包括分析师、研究员和风险管理角色。",
      "en": "Organizes financial research through model-based analyst, researcher and risk-management roles."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:07:37.951043+00:00",
        "en": "2026-11-17T04:07:37.951043+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合研究多角色大模型如何汇总金融信息，并比较不同日期和配置下的输出。",
      "en": "Useful for studying how multiple model roles aggregate financial information and comparing outputs across dates and configurations.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "source_url": "https://github.com/TauricResearch/TradingAgents/blob/9fa1196fffbcfd9de5146d2dd2869df84ab99838/LICENSE",
      "license_sha256": "c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4",
      "source_commit": "9fa1196fffbcfd9de5146d2dd2869df84ab99838",
      "reviewed_at": "2026-11-17T04:07:37.951043+00:00",
      "evidence_pinned_at": "2026-11-17T04:07:37.951043+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "Applies to repository code and documentation; external models, services, data and assets retain their own terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-10-27T08:01:21Z",
        "reviewed_at": "2026-11-17T04:07:37.951043+00:00",
        "url": "https://github.com/TauricResearch/TradingAgents/commit/bf7f4b55a300ede4a8106022044cc473fcbe85af",
        "qualifies": true,
        "reason": {
          "zh-CN": "将财务报表工具的频率参数限制为 annual 或 quarterly，避免把无效频率静默解释为年度数据。",
          "en": "Restricts financial-statement tool frequency to annual or quarterly instead of silently treating invalid values as annual data."
        },
        "reviewed_files": [
          "tradingagents/agents/tools.py"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/TauricResearch/TradingAgents",
        "accessed_at": "2026-11-17T04:07:37.951043+00:00"
      },
      {
        "url": "https://github.com/TauricResearch/TradingAgents/blob/9fa1196fffbcfd9de5146d2dd2869df84ab99838/README.md",
        "accessed_at": "2026-11-17T04:07:37.951043+00:00"
      },
      {
        "url": "https://github.com/TauricResearch/TradingAgents/blob/9fa1196fffbcfd9de5146d2dd2869df84ab99838/LICENSE",
        "accessed_at": "2026-11-17T04:07:37.951043+00:00"
      },
      {
        "url": "https://github.com/TauricResearch/TradingAgents/commit/bf7f4b55a300ede4a8106022044cc473fcbe85af",
        "accessed_at": "2026-11-17T04:07:37.951043+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 11824,
      "source_url": "https://github.com/trending/python?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDONjF_4A",
    "full_name": "TauricResearch/TradingAgents",
    "stargazers_count": 122872,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4",
    "last_success_at": "2026-11-17T03:53:41.737741+00:00"
  }
}
```

</details>
