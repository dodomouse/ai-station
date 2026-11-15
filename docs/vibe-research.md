# Vibe Research

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 数据处理 / Data processing |
| 状态 / Status | 已收录 / Included |
| Star | 3720 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T11:46:23.164Z |

以上为历史核对结果，使用前请复核上游状态。 / This is a dated review; check the current upstream state before use.

## 中文

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

### 原始中文记录（历史快照）

### 022 Vibe Research

仓库：[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)

#### 1. 简介

面向 A 股、美股和港股的投研工作台。整合自选、持仓、每日复盘、产业与公司研究、历史回测和研报库。

#### 2. 适用场景

整理自选与持仓流水。生成公司或产业研究报告。检索自有 PDF/Word 研报。验证历史回测想法。

#### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 自选与持仓 | 按交易流水记录持仓，展示盈亏、集中度等，并有事件日历。 | 功能 / 我的股票 |
| 每日复盘与资讯 | 整理市场状态、资金、产业资讯和行业信号。 | 每日复盘 / 产业研究 |
| 公司研究 | 按公司画像、财务、盈利预期、估值、风险和报告开展研究。 | 个股深挖 / 功能总览 |
| 研报库 | 导入PDF/Word等资料，检索、提问并回查引用原文。 | 功能总览 / 我的研报 |
| 回测与研究记录 | 用对话描述想法做历史回测，并保存报告、辩论和研究记录。 | 回测 / 研究记录 |
| AI来源接入 | 使用已登录Claude Code、Codex、WorkBuddy/CodeBuddy，或兼容模型API。 | 支持的 AI |
| MCP接口 | 向支持MCP的客户端提供取数、报告、证据和研究工具。 | 在 Claude Code / Codex / Cursor 里调用 VR |

官方来源入口：[官方 README](https://github.com/simonlin1212/Vibe-Research/blob/main/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

**平台与环境**

- 源码支持macOS、Linux、Windows；Node≥22.18、Python≥3.11
- Windows/macOS免安装包；README说明并非全部平台均实机验收
- 远程访问仅macOS/Linux

- MIT开源；AI订阅/API需用户自行提供，产品不附赠额度。
- 只取数、读报告与证据无需AI；发起研究会消耗所选AI额度。
- 外部数据及模型服务可用性和费用另计。

- 不能下单交易；多空辩论及MCP发起研究目前只支持A股。
- 第三方数据可能延迟、缺失或有误，端点存在不保证随时可用。
- 模型API需支持Chat Completions与工具调用，README未把所有模板标成实测。
- ADR与本地股换股比例本版不处理；本轮未运行研究或回测。

**容易找错的需求（不属于本项目能力）**

- 直接连接券商自动买卖股票。
- 保证研报全部事实正确并给出稳赚收益。

#### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/simonlin1212/Vibe-Research/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- 本地浏览器页面
- MCP（7个只读工具、1个研究发起工具）
- 命令行研究入口
- Claude Code/Codex/WorkBuddy/CodeBuddy订阅与Chat Completions API

#### 6. 替代选择

- [xbtlin/ai-berkshire](ai-berkshire.md#中文)：本项目是含持仓、研报库和回测的投研工作台；后者以技能组织财报、估值与投资论点研究。

#### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/simonlin1212/Vibe-Research/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/022_simonlin1212-Vibe-Research.md`。

## English

A research workspace for watchlists, holdings, company and sector studies, reports and backtesting across supported markets.

### Use cases

- Organize investment research
- Maintain a searchable report library

### Requirements and limits

This is not a trading or order-execution system. Source data can be delayed or wrong. Some research features are limited to A-shares and remote access to macOS/Linux. Model services cost extra; reports, backtests and returns were not validated. No investment recommendation is made by this catalog.

### Getting started

Read the [official documentation](https://github.com/simonlin1212/Vibe-Research/blob/main/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [AI Berkshire](ai-berkshire.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:17.178Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

保留原始核对数据，便于追溯来源、许可和维护证据。 / Original review data preserves source, license and maintenance evidence.

```json
{
  "evaluated_at": "2026-11-15T11:54:08.129868Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "vibe-research",
    "name": "Vibe Research",
    "repository": "simonlin1212/Vibe-Research",
    "repo_node_id": "R_kgDOTN_trg",
    "category": "data",
    "tags": [
      "research",
      "finance",
      "reports"
    ],
    "forms": [
      "web",
      "cli"
    ],
    "platforms": [
      "linux",
      "macos",
      "windows"
    ],
    "aliases": {
      "zh-CN": [
        "Vibe Research"
      ],
      "en": [
        "Vibe Research"
      ]
    },
    "summary": {
      "zh-CN": "面向 A 股、美股和港股的投研工作台。整合自选、持仓、每日复盘、产业与公司研究、历史回测和研报库。",
      "en": "A research workspace for watchlists, holdings, company and sector studies, reports and backtesting across supported markets."
    },
    "use_cases": {
      "zh-CN": [
        "整理自选与持仓流水。生成公司或产业研究报告。检索自有 PDF/Word 研报。验证历史回测想法。"
      ],
      "en": [
        "Organize investment research",
        "Maintain a searchable report library"
      ]
    },
    "alternatives": [
      "ai-berkshire"
    ],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-15T11:03:50.120930Z",
        "en": "2026-11-15T11:03:50.120930Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "e68105939fc1699f26fef5dc6d4eea2978c4f7209bf6cd5d9c4eb86395dd7b33",
      "source_url": "https://github.com/simonlin1212/Vibe-Research/blob/main/LICENSE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-12T14:21:57Z",
        "reviewed_at": "2026-11-15T11:03:50.120930Z",
        "url": "https://github.com/simonlin1212/Vibe-Research/commit/58e1265ebbf1c687415e7df02e990ab00d563d35",
        "qualifies": true,
        "reason": {
          "zh-CN": "修正研究输出截断、页面访问及临时工作区清理。已核对提交中的实现文件与差异；未运行上游测试。",
          "en": "Fixes truncated research output, page access and temporary-workspace cleanup. Reviewed implementation changes; upstream tests were not run."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/simonlin1212/Vibe-Research",
        "accessed_at": "2026-11-15T10:48:17.178Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/simonlin1212/Vibe-Research/blob/main/README.md",
        "accessed_at": "2026-11-15T10:54:01.869Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      },
      {
        "url": "https://github.com/simonlin1212/Vibe-Research/blob/main/LICENSE",
        "accessed_at": "2026-11-15T10:53:10.834Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "022",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "2c7fb84bbcc96406ed1e991a52020c31b344983c7dc684679db90cdcf5a5b449",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "tool",
      "pending_reasons": [],
      "english_scope": "editorial_digest",
      "source_card_preserved": true
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOTN_trg",
    "full_name": "simonlin1212/Vibe-Research",
    "stargazers_count": 3720,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "e68105939fc1699f26fef5dc6d4eea2978c4f7209bf6cd5d9c4eb86395dd7b33",
    "last_success_at": "2026-11-15T11:46:23.164Z"
  }
}
```

</details>
