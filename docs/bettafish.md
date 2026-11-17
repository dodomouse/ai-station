# 微舆（BettaFish）

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[666ghj/BettaFish](https://github.com/666ghj/BettaFish)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 候选 / Candidate |
| Star | 42701 |
| 许可证 / License | 待复核 / Review needed |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T10:48:12.351Z |

候选原因：许可原文与范围待复核。
Candidate reason: License text and scope require review.

状态整理：2026-11-17，依据已有证据区分当前待办与历史结论；未重新完成全部准入复核，Star 与快照日期保持原值。
Status clarified on 2026-11-17 from existing evidence; this is not a complete new eligibility review. Stars and snapshot dates retain their original values.

下一步：取得许可原文并核对适用范围。
Next step: Obtain the license text and confirm its scope.

历史资格见[收录依据](#review-evidence)中的 `eligibility_history`。 / Earlier decisions are retained in `eligibility_history` in the [review evidence](#review-evidence).

## 中文

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

当前 README 仍有禁止商业用途的说明，与 GPL 标识并存。许可证口径未解决，暂不正式收录。

### 原始中文记录（历史快照）

### 002 微舆（BettaFish）

仓库：[666ghj/BettaFish](https://github.com/666ghj/BettaFish)

#### 1. 简介

多智能体舆情分析系统，组合网页搜索、社媒分析和数据库查询。通过协作汇总资料，输出 HTML 等格式的分析报告。

#### 2. 适用场景

舆情与品牌声誉研究。社媒评论与情感分析。多来源资料汇总成报告。

#### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 多来源搜索与舆情整理 | Query Agent 搜索公开网页，Media Agent 分析多模态内容，Insight Agent 查询私有舆情数据库。 | 系统架构 / 整体架构图 |
| 论坛式多智能体协作 | 多个 Agent 在主持人引导下交流研究结果，并据此调整后续检索方向。 | 系统架构 / 一次完整分析流程 |
| 评论情感分析 | InsightEngine 集成情感分析组件，README 列出微调模型和统计方法等选项。 | 项目代码结构树 / 更改情感分析模型 |
| 结构化报告生成 | Report Agent 组织章节和中间表示，渲染交互式 HTML 报告。 | 一次完整分析流程 |
| 报告导出 | 项目提供命令行报告生成工具，并说明 PDF 与 Markdown 输出选项。 | 源码启动指南 / 命令行报告生成工具 |
| 接入自定义数据与报告模板 | README 说明自定义数据库工具的集成方式，以及 Web 上传或文件方式添加报告模板。 | 接入自定义业务数据库 / 自定义报告模板 |

官方来源入口：[官方 README](https://github.com/666ghj/BettaFish/blob/main/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

**平台与环境**

- Docker 部署
- Python 3.9+ 源码环境；爬虫需 Playwright 等依赖

- 代码标为 GPL-2.0，可自行部署；部署、模型调用和数据服务成本另计。
- README 同时写仅供学习、学术和教育，禁止商业用途及将结果用于商业决策。该说明与许可证使用口径须另行核对。
- 赞助商 API 广告不代表免费模型额度或永久免费服务。

- 需配置模型服务和数据库；部分数据采集依赖浏览器及外部网站。
- 预测走向、分析质量和数据覆盖是项目方主张，本次未实测。
- 只归纳项目公开功能，不能据此认可其分析结论。

**容易找错的需求（不属于本项目能力）**

- 不是用于薅免费模型额度的工具，也不保证 AI 调用免费。
- 不是可直接信赖的投资决策或精确事件预测系统。

#### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/666ghj/BettaFish/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- Flask Web 界面
- 各 Agent 独立入口
- 命令行报告工具

#### 6. 替代选择

- [simonlin1212/Vibe-Research](vibe-research.md#中文)：本项目侧重网页、社媒和数据库资料的舆情汇总；后者侧重自选、持仓、公司研究和回测。

#### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/666ghj/BettaFish/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/002_666ghj-BettaFish.md`。

## English

Multi-agent research software that combines web, social and database material into public-opinion reports.

### Use cases

- Summarize public discussion
- Generate reports from multiple sources

### Requirements and limits

Requires model services, a database and crawler dependencies. Hosting and APIs have separate costs. The README prohibits commercial use while the repository advertises GPL-2.0; this inconsistency remains unresolved. Analysis and forecasts were not tested.

### Getting started

Read the [official documentation](https://github.com/666ghj/BettaFish/blob/main/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [Vibe Research](vibe-research.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:12.351Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

The current README still restricts commercial use alongside a GPL label. License scope remains unresolved.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

保留原始核对数据，便于追溯来源、许可和维护证据。 / Original review data preserves source, license and maintenance evidence.

```json
{
  "evaluated_at": "2026-11-15T11:54:08.129868Z",
  "eligibility": {
    "status": "unknown",
    "reasons": [
      "license_needs_review"
    ],
    "reviewed_at": "2026-11-17T03:11:46.178386+00:00",
    "review_basis": "existing_evidence_status_clarification",
    "pending_actions": {
      "zh-CN": [
        "取得许可原文并核对适用范围。"
      ],
      "en": [
        "Obtain the license text and confirm its scope."
      ]
    }
  },
  "metadata": {
    "schema_version": 1,
    "id": "bettafish",
    "name": "微舆（BettaFish）",
    "repository": "666ghj/BettaFish",
    "repo_node_id": "R_kgDOMQfyrg",
    "category": "ai",
    "tags": [
      "research",
      "sentiment",
      "agents"
    ],
    "forms": [
      "web",
      "cli"
    ],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "微舆（BettaFish）"
      ],
      "en": [
        "BettaFish"
      ]
    },
    "summary": {
      "zh-CN": "多智能体舆情分析系统，组合网页搜索、社媒分析和数据库查询。通过协作汇总资料，输出 HTML 等格式的分析报告。",
      "en": "Multi-agent research software that combines web, social and database material into public-opinion reports."
    },
    "use_cases": {
      "zh-CN": [
        "舆情与品牌声誉研究。社媒评论与情感分析。多来源资料汇总成报告。"
      ],
      "en": [
        "Summarize public discussion",
        "Generate reports from multiple sources"
      ]
    },
    "alternatives": [
      "vibe-research"
    ],
    "editorial": {
      "status": "draft",
      "reviewed_at": {
        "zh-CN": "2026-11-15T11:03:50.120930Z",
        "en": "2026-11-15T11:03:50.120930Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": null,
      "osi_approved": false,
      "license_sha256": "44686cfd8b09cd489ecbd2f740e0a31d7006584b90e7446dd29661f06f0213ec",
      "source_url": "https://github.com/666ghj/BettaFish/blob/b67928ff1ce515dd7672408221fb1e9500d0972d/LICENSE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "b67928ff1ce515dd7672408221fb1e9500d0972d"
    },
    "activity_evidence": [],
    "sources": [
      {
        "url": "https://github.com/666ghj/BettaFish",
        "accessed_at": "2026-11-15T10:48:12.351Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/666ghj/BettaFish/blob/main/README.md",
        "accessed_at": "2026-11-15T10:53:59.305Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      },
      {
        "url": "https://github.com/666ghj/BettaFish/blob/b67928ff1ce515dd7672408221fb1e9500d0972d/LICENSE",
        "accessed_at": "2026-11-15T10:53:07.814Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "002",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "a18a9a6cb02277ced39875a4186740ed85c45b86073aef1702d1fc0e149f127b",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "tool",
      "pending_reasons": [
        "license_review_pending",
        "activity_not_confirmed"
      ],
      "english_scope": "editorial_digest",
      "source_card_preserved": true,
      "notes": {
        "zh-CN": "当前 README 仍有禁止商业用途的说明，与 GPL 标识并存。许可证口径未解决，暂不正式收录。",
        "en": "The current README still restricts commercial use alongside a GPL label. License scope remains unresolved."
      },
      "historical": true
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOMQfyrg",
    "full_name": "666ghj/BettaFish",
    "stargazers_count": 42701,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "GPL-2.0",
    "license_sha256": "44686cfd8b09cd489ecbd2f740e0a31d7006584b90e7446dd29661f06f0213ec",
    "last_success_at": "2026-11-15T10:48:12.351Z"
  },
  "eligibility_history": [
    {
      "evaluated_at": "2026-11-15T11:54:08.129868Z",
      "status": "unknown",
      "reasons": [
        "license_needs_review"
      ]
    }
  ]
}
```

</details>
