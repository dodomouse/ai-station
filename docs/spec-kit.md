# Spec Kit

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[github/spec-kit](https://github.com/github/spec-kit)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 149841 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T10:48:14.753Z |

以上为历史核对结果，使用前请复核上游状态。 / This is a dated review; check the current upstream state before use.

## 中文

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

### 原始中文记录（历史快照）

### 013 Spec Kit

仓库：[github/spec-kit](https://github.com/github/spec-kit)

#### 1. 简介

提供规格驱动开发的 CLI、技能和模板。把需求规格转换为计划、任务和代码，并支持检查与缺陷修复流程。

#### 2. 适用场景

按规格组织新功能开发。将需求拆成计划和可执行任务。建立团队共用开发模板与流程。组织缺陷修复流程。

#### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 规格驱动开发 | 从原则和需求规格进入计划、任务、实现和收敛检查。 | Spec-Driven Development |
| 独立缺陷流程 | bug扩展分评估、修复、测试，输出修复验证报告。 | Bug fixing |
| 想法评估 | assess扩展组织证据，给出继续、澄清或停止判断。 | Idea assessment |
| 流程定制 | 用扩展、预设、工作流、覆盖层和自定义步骤组装流程。 | Capabilities |
| 团队与目录 | 通过Bundle和Catalog分发团队选用的组件，支持本地源与自托管目录。 | Capabilities |
| 多智能体集成 | 通过Integration接入或切换编码智能体。 | Capabilities / Supported AI coding agent integrations |

官方来源入口：[官方 README](https://github.com/github/spec-kit/blob/main/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

**平台与环境**

- Linux
- macOS
- Windows；README要求Python 3.11+与uv

- 工具开源MIT；所用编码智能体订阅/API、外部服务和运行环境费用另计。

- 需要受支持的AI编码智能体。
- SDD在核心内，Bug和想法评估需按需安装扩展。
- 社区目录不代表审计或官方背书；本轮未安装执行。

**容易找错的需求（不属于本项目能力）**

- 不用任何模型或开发环境就自动完成软件交付。
- 保证一套规格能证明系统绝无缺陷。

#### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/github/spec-kit/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- Specify命令行
- 受支持编码智能体中的技能/命令
- 扩展、预设、Workflow、Bundle、Catalog

#### 6. 替代选择

- [mattpocock/skills](skills.md#中文)：本项目提供规格、计划和任务模板的开发流程；后者按工程任务提供独立技能。

#### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/github/spec-kit/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/013_github-spec-kit.md`。

## English

A toolkit for specification-driven development, connecting requirements, plans, tasks and implementation through agent workflows.

### Use cases

- Turn requirements into an implementation plan
- Organize agent-assisted development

### Requirements and limits

Requires a supported coding assistant, Python 3.11+ and uv in the source documentation. Model usage is separate. Some bug and idea workflows require extensions. Community listings are not audits, and specifications do not prove software is defect-free.

### Getting started

Read the [official documentation](https://github.com/github/spec-kit/blob/main/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [Skills for Real Engineers](skills.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:14.753Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

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
    "id": "spec-kit",
    "name": "Spec Kit",
    "repository": "github/spec-kit",
    "repo_node_id": "R_kgDOPiFCnQ",
    "category": "development",
    "tags": [
      "specification",
      "agent-skill",
      "cli"
    ],
    "forms": [
      "cli"
    ],
    "platforms": [
      "linux",
      "macos",
      "windows"
    ],
    "aliases": {
      "zh-CN": [
        "Spec Kit"
      ],
      "en": [
        "Spec Kit"
      ]
    },
    "summary": {
      "zh-CN": "提供规格驱动开发的 CLI、技能和模板。把需求规格转换为计划、任务和代码，并支持检查与缺陷修复流程。",
      "en": "A toolkit for specification-driven development, connecting requirements, plans, tasks and implementation through agent workflows."
    },
    "use_cases": {
      "zh-CN": [
        "按规格组织新功能开发。将需求拆成计划和可执行任务。建立团队共用开发模板与流程。组织缺陷修复流程。"
      ],
      "en": [
        "Turn requirements into an implementation plan",
        "Organize agent-assisted development"
      ]
    },
    "alternatives": [
      "skills"
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
      "license_sha256": "2510b446bc1f0cf9702453075d20cd88631e20e5642658edb7325d9c1eb534f7",
      "source_url": "https://github.com/github/spec-kit/blob/main/LICENSE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-12T16:30:46Z",
        "reviewed_at": "2026-11-15T11:03:50.120930Z",
        "url": "https://github.com/github/spec-kit/commit/2ee2b1e8005905db05f5717300a469b3068b908f",
        "qualifies": true,
        "reason": {
          "zh-CN": "修正 PowerShell 对含方括号路径的处理。已核对提交中的实现文件与差异；未运行上游测试。",
          "en": "Handles bracketed paths literally in PowerShell. Reviewed implementation changes; upstream tests were not run."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/github/spec-kit",
        "accessed_at": "2026-11-15T10:48:14.753Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/github/spec-kit/blob/main/README.md",
        "accessed_at": "2026-11-15T10:54:00.523Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      },
      {
        "url": "https://github.com/github/spec-kit/blob/main/LICENSE",
        "accessed_at": "2026-11-15T10:53:08.988Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "013",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "4bf7a846de55bafed2f5fd3a0d55ce747a4fb58f8c1d2d004c03c32b859fd77d",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "agent-skill",
      "pending_reasons": [],
      "english_scope": "editorial_digest",
      "source_card_preserved": true
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOPiFCnQ",
    "full_name": "github/spec-kit",
    "stargazers_count": 149841,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "2510b446bc1f0cf9702453075d20cd88631e20e5642658edb7325d9c1eb534f7",
    "last_success_at": "2026-11-15T10:48:14.753Z"
  }
}
```

</details>
