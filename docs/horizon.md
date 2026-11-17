# Horizon：AI 信息聚合与双语新闻简报

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[Thysrael/Horizon](https://github.com/Thysrael/Horizon)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Productivity |
| 状态 / Status | 已收录 / Included |
| Star | 14389 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T10:48:23.757Z |

以上为历史核对结果，使用前请复核上游状态。 / This is a dated review; check the current upstream state before use.

## 中文

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

### 原始中文记录（历史快照）

### 058 Horizon：AI 信息聚合与双语新闻简报

仓库：[Thysrael/Horizon](https://github.com/Thysrael/Horizon)

#### 1. 简介

聚合 RSS、社区、GitHub 与新闻等信息源，按 Profile 评分、筛选和去重，生成中英双语 Markdown 日报。

#### 2. 适用场景

每日汇总 AI 与技术新闻。跟踪项目 Release。提炼技术长文。通过 Pages、邮件或 Webhook 分发简报。

#### 3. 主要功能

以下能力以核验版本的官方 README 为依据。

| 能力 | 具体作用与条件 |
| --- | --- |
| 多源采集 | 支持 RSS/Atom、Hacker News、Reddit、Telegram 公开频道、X、GitHub、OpenBB、OSS Insight、GDELT 与 Google News；不同来源各有配置条件。 |
| 按兴趣筛选 | 可指定或自动匹配 Profile，自定义评分、摘要及背景等区块；同一 Profile 下可合并重复话题。 |
| 控制阅读量 | 可限制日报总条数和各类内容份额，配置后才应用限额。 |
| 补充背景与讨论 | 按需搜索背景、摘要社区评论；评论采集只适用于部分信息源。 |
| 日报输出与投递 | 生成中英双语 Markdown，可发布到 GitHub Pages、邮件或 Webhook；列有飞书、钉钉、Slack、Discord 等通知渠道。微信另需 iLink Bot 登录，受回复额度限制。 |
| 助手与定时入口 | 提供 CLI、MCP 和 Agent Skill；GitHub Actions 每日工作流是默认禁用的模板，需自行配置启用。 |

官方来源入口：[官方中文 README](https://github.com/Thysrael/Horizon/blob/main/README_zh.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

- 环境：`pyproject.toml` 要求 Python 3.11 或以上；可用 `uv` 安装，也提供 Docker 入口。
- 模型与信息源：需配置可用的模型服务；部分来源另需凭据、服务额度或可选依赖。MIT 许可不代表模型和数据服务免费。
- 可选依赖：OpenBB 使用 `openbb` extra；`twitter` extra 涉及 Playwright，官方说明当前 Dockerfile 不会安装所需浏览器及系统组件。
- 配置与运行：在独立项目目录执行 `uv sync`、`uv run horizon-wizard` 配置来源与兴趣，再用 `uv run horizon` 生成日报。默认抓取最近 24 小时，默认结果目录为 `data/summaries/`。
- 助手入口：官方提供 `horizon` Skill 和 MCP 服务；本次只收录资料，未安装技能或接入助手。

- AI 评分和摘要属于自动处理结果，重要信息仍应回到原文核对。定时生成、站点发布和渠道推送都需要部署配置。
- [BettaFish](bettafish.md#中文)偏向舆情、社媒评论和多来源研究分析；Horizon 偏向持续采集与个人日常阅读简报。
- [Vibe-Research](vibe-research.md#中文)偏向投资研究工作台；Horizon 的金融新闻源用于信息采集，不据此推导估值或回测能力。
- [cc-connect](cc-connect.md#中文)把编码助手接入聊天平台；Horizon 的通知用途是投递简报与运行结果。

知识卡未提供完整部署费用或付费服务价格；未记录的费用项目需要另行核对。

#### 5. 开始使用

安装与入门文档：[官方中文 README](https://github.com/Thysrael/Horizon/blob/main/README_zh.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

其他入口：[中文 README](https://github.com/Thysrael/Horizon/blob/cdd86ff263f170f1675fab5bddd3bc1dfeacc6b5/README_zh.md)、[配置指南](https://github.com/Thysrael/Horizon/blob/main/docs/configuration.md)。

初次使用所需环境及调用示例见上节“使用限制”。

#### 6. 替代选择

- [KKKKhazix/agent-autoloop](agent-autoloop.md#中文)：本项目直接组织信息源、评分、去重和双语日报；后者提供通用的定时与事件执行框架。

#### 7. 复核说明

- 知识库记录日期：2026-11-11；卡片最后确认日期：2026-11-11。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：已核对官方中英文 README、依赖清单、仓库元信息和许可；未安装运行。分类、问法和匹配理由属于检索整理判断。

**来源与版本记录**

- 当前入口：[官方中文 README](https://github.com/Thysrael/Horizon/blob/main/README_zh.md)、[英文 README](https://github.com/Thysrael/Horizon/blob/main/README.md)。
- 核验版本：默认分支 `main`，提交 [`cdd86ff263f170f1675fab5bddd3bc1dfeacc6b5`](https://github.com/Thysrael/Horizon/commit/cdd86ff263f170f1675fab5bddd3bc1dfeacc6b5)。
- 固定版本来源：[中文 README](https://github.com/Thysrael/Horizon/blob/cdd86ff263f170f1675fab5bddd3bc1dfeacc6b5/README_zh.md)、[依赖与命令入口](https://github.com/Thysrael/Horizon/blob/cdd86ff263f170f1675fab5bddd3bc1dfeacc6b5/pyproject.toml)、[MIT 许可](https://github.com/Thysrael/Horizon/blob/cdd86ff263f170f1675fab5bddd3bc1dfeacc6b5/LICENSE)。
- 后续配置入口：[配置指南](https://github.com/Thysrael/Horizon/blob/main/docs/configuration.md)、[Profile 指南](https://github.com/Thysrael/Horizon/blob/main/docs/profiles.md)、[MCP 工具](https://github.com/Thysrael/Horizon/blob/main/src/mcp/README.md)、[Agent Skill](https://github.com/Thysrael/Horizon/blob/main/docs/agent-skill.md)。这些链接供后续部署时查阅，本次未逐项验证。
- 按仓库 ID `1162410458` 去重；后续复核来源、投递渠道及环境要求时，同步更新用途索引与最后确认日期。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/058_Thysrael-Horizon.md`。

## English

Collects information from RSS, communities and other configured sources, filters and scores it, and produces bilingual reading reports.

### Use cases

- Prepare a personal news brief
- Combine recurring information sources

### Requirements and limits

Requires Python 3.11+ or the documented container setup, model access and sometimes source credentials. Optional integrations have extra dependencies; the documented Docker image does not include every browser component. Summaries need checks against originals. Scheduling, publishing and notifications require deployment configuration.

### Getting started

Read the [official documentation](https://github.com/Thysrael/Horizon/blob/main/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [Agent Autoloop](agent-autoloop.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:23.757Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

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
    "id": "horizon",
    "name": "Horizon：AI 信息聚合与双语新闻简报",
    "repository": "Thysrael/Horizon",
    "repo_node_id": "R_kgDORUj52g",
    "category": "productivity",
    "tags": [
      "news",
      "research",
      "automation"
    ],
    "forms": [
      "cli",
      "service"
    ],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "Horizon：AI 信息聚合与双语新闻简报"
      ],
      "en": [
        "Horizon"
      ]
    },
    "summary": {
      "zh-CN": "聚合 RSS、社区、GitHub 与新闻等信息源，按 Profile 评分、筛选和去重，生成中英双语 Markdown 日报。",
      "en": "Collects information from RSS, communities and other configured sources, filters and scores it, and produces bilingual reading reports."
    },
    "use_cases": {
      "zh-CN": [
        "每日汇总 AI 与技术新闻。跟踪项目 Release。提炼技术长文。通过 Pages、邮件或 Webhook 分发简报。"
      ],
      "en": [
        "Prepare a personal news brief",
        "Combine recurring information sources"
      ]
    },
    "alternatives": [
      "agent-autoloop"
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
      "license_sha256": "65cf34e685cb1dd4e18e44502d476240a028d42e295b48ffdc601968ca3ce033",
      "source_url": "https://github.com/Thysrael/Horizon/blob/12d5fbde4d9e0776a48618ea65d16fe6d1e1b606/LICENSE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "12d5fbde4d9e0776a48618ea65d16fe6d1e1b606"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-15T09:27:46Z",
        "reviewed_at": "2026-11-15T11:03:50.120930Z",
        "url": "https://github.com/Thysrael/Horizon/commit/12d5fbde4d9e0776a48618ea65d16fe6d1e1b606",
        "qualifies": true,
        "reason": {
          "zh-CN": "跳过无效的 OpenBB 新闻记录。已核对提交中的实现文件与差异；未运行上游测试。",
          "en": "Skips invalid OpenBB news rows. Reviewed implementation changes; upstream tests were not run."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/Thysrael/Horizon",
        "accessed_at": "2026-11-15T10:48:23.757Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/Thysrael/Horizon/blob/main/README.md",
        "accessed_at": "2026-11-15T10:54:07.276Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      },
      {
        "url": "https://github.com/Thysrael/Horizon/blob/12d5fbde4d9e0776a48618ea65d16fe6d1e1b606/LICENSE",
        "accessed_at": "2026-11-15T10:53:18.707Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "058",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "a5d09a5d37269c6aa52cdb5c632688e2910294447d1c88fb5e0add84a86202a1",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "tool",
      "pending_reasons": [],
      "english_scope": "editorial_digest",
      "source_card_preserved": true
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDORUj52g",
    "full_name": "Thysrael/Horizon",
    "stargazers_count": 14389,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "65cf34e685cb1dd4e18e44502d476240a028d42e295b48ffdc601968ca3ce033",
    "last_success_at": "2026-11-15T10:48:23.757Z"
  }
}
```

</details>
