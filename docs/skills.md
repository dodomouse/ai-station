# Skills For Real Engineers（Matt Pocock）

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[mattpocock/skills](https://github.com/mattpocock/skills)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 324716 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T10:48:15.523Z |

以上为历史核对结果，使用前请复核上游状态。 / This is a dated review; check the current upstream state before use.

## 中文

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

### 原始中文记录（历史快照）

### 017 Skills For Real Engineers（Matt Pocock）

仓库：[mattpocock/skills](https://github.com/mattpocock/skills)

#### 1. 简介

面向编程智能体的工程技能集合。覆盖需求澄清、架构决策、测试驱动开发、重构和任务组织。

#### 2. 适用场景

为 Claude Code 或 Codex 补充工程技能。在编码前澄清需求与记录设计决定。组织测试驱动开发及重构任务。

#### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 需求访谈与文档化 | grill-me 与 grill-with-docs 通过访谈澄清目标；工程版本同步形成领域词汇和 ADR。 | Why These Skills Exist / Reference |
| 领域模型与架构设计 | domain-modeling、codebase-design 和 improve-codebase-architecture 约束术语、模块边界并寻找架构改进点。 | Reference / Engineering |
| 规格与任务拆分 | to-spec 汇总讨论形成规格，to-tickets 拆成声明依赖关系的纵向切片任务。 | Reference / Engineering |
| 测试驱动实现 | tdd 使用 red-green-refactor；implement 按约定接口或边界驱动实现并执行评审。 | Reference / Engineering |
| 故障诊断与代码审查 | diagnosing-bugs 建立复现和假设验证循环；code-review 分别核对规范与规格。 | Reference / Engineering |
| 大型任务与多智能体安排 | wayfinder 维护超出单会话的大任务地图，implement-spec 描述按任务依赖并发执行。 | Reference / Engineering |
| 通用知识工作技能 | research、writing-for-agents、teach 等用于资料调查、编写智能体文档和教学。 | Reference / Productivity |

官方来源入口：[官方 README](https://github.com/mattpocock/skills/blob/main/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

**平台与环境**

- Claude Code、Codex、GitHub Copilot、Gemini CLI 等支持技能的助手

- 技能仓库采用 MIT；技能文件本身不提供模型算力。
- 运行使用所选助手的订阅或 API；issue tracker 和其他工具成本另计。
- 不要在同一助手混装插件和复制式技能，否则可能重复。

- 是可组合工程方法，不是独立 Agent Runtime。
- README 区分用户主动调用与模型可调用的技能。
- 某些技能涉及提交、创建任务或外部服务；使用时仍服从具体仓库授权。
- 本次只读功能说明，未安装或执行任何技能。

**容易找错的需求（不属于本项目能力）**

- 不是免费模型额度领取或请求转发服务。
- 不是自动扫描并直接保证架构正确的静态分析器。

#### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/mattpocock/skills/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- 各助手的插件安装方式
- skills.sh 可编辑技能文件
- 斜杠命令与按适用任务调用的技能

#### 6. 替代选择

- [github/spec-kit](spec-kit.md#中文)：本项目提供需求、设计、测试和重构技能；后者围绕规格组织计划、任务及实现。
- [xstongxue/best-skills](best-skills.md#中文)：本项目聚焦工程技能；后者的范围还包括论文、汇报、自媒体和图表。

#### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/mattpocock/skills/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/017_mattpocock-skills.md`。

## English

Composable coding-assistant skills for requirements, architecture, implementation, review and refactoring.

### Use cases

- Guide requirements discussions
- Apply repeatable engineering workflows

### Requirements and limits

These are agent instructions, not a standalone runtime or static proof of correctness. Some workflows use Git branches, issue trackers and external actions; repository-specific authorization still applies. Host model and service costs are separate. Installing overlapping plugin and copied editions can duplicate skills.

### Getting started

Read the [official documentation](https://github.com/mattpocock/skills/blob/main/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [Spec Kit](spec-kit.md#english)
- [Best Skills](best-skills.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:15.523Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

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
    "id": "skills",
    "name": "Skills For Real Engineers（Matt Pocock）",
    "repository": "mattpocock/skills",
    "repo_node_id": "R_kgDORHkddg",
    "category": "development",
    "tags": [
      "agent-skill",
      "engineering",
      "workflow"
    ],
    "forms": [],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "Skills For Real Engineers（Matt Pocock）"
      ],
      "en": [
        "Skills for Real Engineers"
      ]
    },
    "summary": {
      "zh-CN": "面向编程智能体的工程技能集合。覆盖需求澄清、架构决策、测试驱动开发、重构和任务组织。",
      "en": "Composable coding-assistant skills for requirements, architecture, implementation, review and refactoring."
    },
    "use_cases": {
      "zh-CN": [
        "为 Claude Code 或 Codex 补充工程技能。在编码前澄清需求与记录设计决定。组织测试驱动开发及重构任务。"
      ],
      "en": [
        "Guide requirements discussions",
        "Apply repeatable engineering workflows"
      ]
    },
    "alternatives": [
      "spec-kit",
      "best-skills"
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
      "license_sha256": "0e7ac423bf2c6e223b7c5b156f8cf72da49d748e56a1641402c31f22ad07dbb5",
      "source_url": "https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/LICENSE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "5863806dd4e15c63174bee4e7515a4256792ecfa"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-10-29T10:42:51Z",
        "reviewed_at": "2026-11-15T11:03:50.120930Z",
        "url": "https://github.com/mattpocock/skills/commit/a496f5513d4a4cf889bc48e189e579f4b0bdf6aa",
        "qualifies": true,
        "reason": {
          "zh-CN": "调整 implement-spec 技能的逐任务执行者分配行为。已核对直接控制助手行为的技能内容差异，并非仅修改介绍。",
          "en": "Changes per-ticket implementer allocation in the implement-spec skill. Reviewed executable skill instructions, rather than descriptive README changes."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/mattpocock/skills",
        "accessed_at": "2026-11-15T10:48:15.523Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/mattpocock/skills/blob/main/README.md",
        "accessed_at": "2026-11-15T10:54:01.878Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      },
      {
        "url": "https://github.com/mattpocock/skills/blob/5863806dd4e15c63174bee4e7515a4256792ecfa/LICENSE",
        "accessed_at": "2026-11-15T10:53:10.260Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "017",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "9d25d4ddc30984c5426c9897730dc85fc535822ab0bdc72877c0b4ce8592ed51",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "agent-skill",
      "pending_reasons": [],
      "english_scope": "editorial_digest",
      "source_card_preserved": true
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDORHkddg",
    "full_name": "mattpocock/skills",
    "stargazers_count": 324716,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "0e7ac423bf2c6e223b7c5b156f8cf72da49d748e56a1641402c31f22ad07dbb5",
    "last_success_at": "2026-11-15T10:48:15.523Z"
  }
}
```

</details>
