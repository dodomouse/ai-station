# Serena

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[oraios/serena](https://github.com/oraios/serena)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 31391 |
| 许可证 / License | 待复核 / Review needed |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T10:48:16.306Z |




历史资格见[收录依据](#review-evidence)中的 `eligibility_history`。 / Earlier decisions are retained in `eligibility_history` in the [review evidence](#review-evidence).

## 中文

### 当前收录状态

2026-11-17 按用户要求转为正式收录。本次是目录状态迁移，未重新核实全部新准入条件。原有 Star、活动与功能记录保留原核对日期，许可不再决定收录状态。

### 先前介绍与复核记录（历史）

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

已有许可记录区分 SolidLSP 的 MIT 与 Serena 应用的 GPL-3.0-or-later。API 的 NOASSERTION 不构成排除依据；当前待办是明确收录组件范围并完成双语内容复核。

### 原始中文记录（历史快照）

### 020 Serena

仓库：[oraios/serena](https://github.com/oraios/serena)

#### 1. 简介

为编程智能体提供符号级检索、编辑、重构和调试工具。通过 MCP 接入助手，使用语言服务器或 JetBrains 后端。

#### 2. 适用场景

按符号查定义与引用。让智能体执行语义重构。给现有助手补充 IDE 式代码工具。

#### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 符号级检索 | 提供查符号、文件符号概要、引用、声明与实现等查询，具体覆盖取决于后端和语言。 | Features / Retrieval |
| 语义重构 | LSP 后端支持符号重命名；JetBrains 后端还提供移动、内联和传播删除等操作。 | Features / Refactoring |
| 符号级编辑 | 提供替换符号主体、在符号前后插入内容及安全删除等接口。 | Features / Symbolic Editing |
| 诊断与 IDE 分析 | 语言服务器或 JetBrains 提供诊断；部分类型层次和依赖内搜索仅 JetBrains 支持。 | Features / Retrieval |
| 交互调试 | JetBrains 插件可让 Agent 设置断点、查看变量、求值和控制执行流程。 | Features / Interactive Debugging |
| 跨会话记忆和配置 | 提供可选记忆系统，以及全局、项目、上下文和 mode 等多层 YAML 配置。 | Features / Memory Management / Configurability |
| MCP 接入现有助手 | 作为 MCP server 为 Claude Code、Codex、IDE 插件或桌面客户端提供工具。 | How Serena Works |

官方来源入口：[官方 README](https://github.com/oraios/serena/blob/main/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

**平台与环境**

- 有相应语言服务器的开发环境
- 支持 MCP 的终端、IDE 或桌面助手
- JetBrains 插件支持的 IDE；README 明确 Rider 与 CLion 不支持该插件

- README 标为 GPL-3.0-or-later，语言服务器后端为默认免费开源路线。
- JetBrains 插件为收费组件，提供免费试用。
- 大模型助手的订阅或 API 另计；工具本身不附送 AI 算力。
- GitHub API 许可证字段是 NOASSERTION，采用前应以当前 LICENSE 核对。

- 不是大模型，需要客户端组织工具调用。
- LSP 与 JetBrains 的功能不同，不能把所有功能都视为默认可用。
- 静态引用和重构受语言后端限制；修改后仍需正常验证。
- 本次没有安装插件、启动服务或修改源码。

**容易找错的需求（不属于本项目能力）**

- 不是侧重构建持久关系图、路径图和图报告的 Graphify。
- 不是独立完成需求到交付的免费编程大模型。

#### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/oraios/serena/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- MCP server（由客户端启动或 HTTP 模式）
- Serena REPL 式 Agent 接口
- 配置与启动 CLI

#### 6. 替代选择

- [tirth8205/code-review-graph](code-review-graph.md#中文)：本项目提供符号级检索、编辑及部分重构工具；后者提供代码关系与审查上下文，侧重点是分析。

#### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/oraios/serena/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/020_oraios-serena.md`。

## English

### Current catalog status

Promoted to an included entry on 2026-11-17 at the user’s request. This is a catalog transition, not a new verification of every admission criterion. Stars, activity and feature records retain their original review dates; licensing no longer determines admission.

### Earlier description and review (historical)

Code navigation and editing tools that use language servers or an optional JetBrains integration to work with symbols.

### Use cases

- Find definitions and references
- Perform agent-assisted code edits

### Requirements and limits

Language and backend support determine capabilities; the JetBrains plugin excludes Rider and CLion in the source card and may require payment. Current licensing separates MIT SolidLSP from the GPL-3.0-or-later application. GitHub's NOASSERTION does not itself prevent inclusion; component scope and bilingual review remain pending. Changes still need normal tests.

### Getting started

Read the [official documentation](https://github.com/oraios/serena/blob/main/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [Code Review Graph](code-review-graph.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:16.306Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

Existing license records distinguish MIT SolidLSP from the GPL-3.0-or-later Serena application. API detection of NOASSERTION is not an exclusion rule; the remaining work is to define the included component scope and complete bilingual review.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

保留原始核对数据，便于追溯来源、许可和维护证据。 / Original review data preserves source, license and maintenance evidence.

```json
{
  "evaluated_at": "2026-11-15T11:54:08.129868Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "admission_basis": "user_directed_transition",
    "policy_id": "ai-activity-stars-2026-11-17",
    "admitted_at": "2026-11-17T13:33:30.547820+00:00"
  },
  "metadata": {
    "schema_version": 1,
    "id": "serena",
    "name": "Serena",
    "repository": "oraios/serena",
    "repo_node_id": "R_kgDOONgOeg",
    "category": "development",
    "tags": [
      "code-navigation",
      "refactoring",
      "mcp"
    ],
    "forms": [
      "service"
    ],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "Serena"
      ],
      "en": [
        "Serena"
      ]
    },
    "summary": {
      "zh-CN": "为编程智能体提供符号级检索、编辑、重构和调试工具。通过 MCP 接入助手，使用语言服务器或 JetBrains 后端。",
      "en": "Code navigation and editing tools that use language servers or an optional JetBrains integration to work with symbols."
    },
    "use_cases": {
      "zh-CN": [
        "按符号查定义与引用。让智能体执行语义重构。给现有助手补充 IDE 式代码工具。"
      ],
      "en": [
        "Find definitions and references",
        "Perform agent-assisted code edits"
      ]
    },
    "alternatives": [
      "code-review-graph"
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
      "license_sha256": "6239f4be78ccff409aedfbce88ac89b26f488f76aac7ab199fb6876dc7fdeb4c",
      "source_url": "https://github.com/oraios/serena/blob/6b39542bb108ce77901072deac699d770b302d52/LICENSE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "6b39542bb108ce77901072deac699d770b302d52"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-14T13:40:52Z",
        "reviewed_at": "2026-11-15T11:03:50.120930Z",
        "url": "https://github.com/oraios/serena/commit/6b39542bb108ce77901072deac699d770b302d52",
        "qualifies": true,
        "reason": {
          "zh-CN": "限制工具调用后的符号缓存写入频率。已核对提交中的实现文件与差异；未运行上游测试。",
          "en": "Limits symbol-cache writes following tool calls. Reviewed implementation changes; upstream tests were not run."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/oraios/serena",
        "accessed_at": "2026-11-15T10:48:16.306Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/oraios/serena/blob/main/README.md",
        "accessed_at": "2026-11-15T10:54:01.744Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      },
      {
        "url": "https://github.com/oraios/serena/blob/6b39542bb108ce77901072deac699d770b302d52/LICENSE",
        "accessed_at": "2026-11-15T10:53:10.771Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "020",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "0493757a170847b67630c4bcdab918c2e7c3f9a60fa8fef5e91e4c8f19776731",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "tool",
      "pending_reasons": [
        "license_review_pending"
      ],
      "english_scope": "editorial_digest",
      "source_card_preserved": true,
      "notes": {
        "zh-CN": "当前许可按组件区分：SolidLSP 为 MIT，Serena 应用为 GPL-3.0-or-later。API 返回 NOASSERTION；当前单一许可门禁不能完整表达该结构，暂留候选，不等于判定闭源。",
        "en": "SolidLSP is MIT and the application GPL-3.0-or-later. API detection is NOASSERTION; the current single-license gate keeps the entry pending rather than declaring it closed source."
      },
      "historical": true
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOONgOeg",
    "full_name": "oraios/serena",
    "stargazers_count": 31391,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "NOASSERTION",
    "license_sha256": "6239f4be78ccff409aedfbce88ac89b26f488f76aac7ab199fb6876dc7fdeb4c",
    "last_success_at": "2026-11-15T10:48:16.306Z"
  },
  "eligibility_history": [
    {
      "evaluated_at": "2026-11-15T11:54:08.129868Z",
      "status": "unknown",
      "reasons": [
        "license_needs_review"
      ]
    },
    {
      "status": "needs_review",
      "reasons": [
        "component_license_review_pending"
      ],
      "evaluated_at": "2026-11-15T11:54:08.129868Z",
      "superseded_at": "2026-11-17T13:33:30.547820+00:00",
      "superseded_by": "user_directed_transition_2026_11_17",
      "pending_actions": {
        "zh-CN": [
          "明确拟收录组件与排除范围，并完成双语内容复核。"
        ],
        "en": [
          "Define the included components and exclusions, then complete bilingual review."
        ]
      },
      "reviewed_at": "2026-11-17T03:11:46.178386+00:00",
      "review_basis": "existing_evidence_status_clarification"
    }
  ]
}
```

</details>
