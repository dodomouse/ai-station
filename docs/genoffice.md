# GenOffice

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Productivity |
| 状态 / Status | 已收录 / Included |
| Star | 12376 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T10:48:14.753Z |

以上为历史核对结果，使用前请复核上游状态。 / This is a dated review; check the current upstream state before use.

## 中文

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

当前 README 说明 ee/ 为未来企业模块预留，并采用单独许可。Apache-2.0 仅按主代码范围记录，不能扩大到全部企业能力。

### 原始中文记录（历史快照）

### 011 GenOffice

仓库：[genspark-ai/genoffice](https://github.com/genspark-ai/genoffice)

#### 1. 简介

提供 Office、PDF、Markdown 和 HTML 文件编辑。包含桌面编辑器、CLI、MCP 和智能体技能，可创建、转换和检索文件。

#### 2. 适用场景

用智能体生成或修改 Office 文件。在本机转换 PDF 与文档格式。跨办公文件搜索和问答。

#### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 文字文档编辑与审阅 | 打开和保存 .docx，支持文档结构、修订和撤销；AI 修改进入可审查的编辑流程。 | Demo / Docs |
| 电子表格与公式 | 编辑 .xlsx，生成公式、图表，提供透视表、条件格式等表格能力。 | Demo / Sheets |
| 演示文稿创作 | 生成和编辑真实 .pptx 的页面、布局和内容，保留可继续修改的画布元素。 | Demo / Slides |
| PDF 编辑和本地转换 | 改写 PDF 页面的文字或图片，支持在本机转换为 Word、Excel 或 PowerPoint。 | Demo / PDF / FAQ |
| Markdown 和 HTML 编辑 | 提供纯 .md 的块编辑和 HTML 页面编辑，并支持导出 Word。 | Demo / HTML / Markdown / FAQ |
| 跨文档搜索和有来源问答 | 本地索引文件名与全文；对收藏文件集提问，回答给出文件出处。 | Demo / Search / Ask AI |
| CLI、技能与 MCP | 无界面调用同一文档引擎，供脚本、Claude Code、Codex 等助手创建、转换、读取和编辑文件。 | Command line and agent skill / MCP server |

官方来源入口：[官方 README](https://github.com/genspark-ai/genoffice/blob/main/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

**平台与环境**

- macOS（Apple Silicon 与 Intel）
- Windows
- Linux；扫描 PDF 的系统 OCR 说明主要针对 macOS 和 Windows

- 应用按 Apache-2.0 开源，README 表明应用本身没有收费档或试用限制。
- AI 可用 Genspark 登录或自带提供方凭据；不能由应用免费推出所有 AI 调用免费。
- 可选文件搜索重排、搜索和图片等服务可能产生提供方费用；本次未核对其价格。

- 本地打开、编辑、保存和转换与 AI 推理的联网路径应分开判断。
- 可选 Jev 重排会发送搜索命中的摘要；AI 编辑会向所选后端发送所需内容。
- 部分旧格式和 ODF 仅导入为 OOXML 副本，不写回原格式。
- 兼容性与保真主张来自 README，未实测。

**容易找错的需求（不属于本项目能力）**

- 不是薅免费 AI 模型额度或绕过模型计费的工具。
- 不是默认所有 AI 功能都离线的办公软件。

#### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/genspark-ai/genoffice/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- 桌面 GUI
- genoffice CLI
- agent skill
- MCP server

#### 6. 替代选择

- [alchaincyf/huashu-design](huashu-design.md#中文)：本项目侧重 Office、PDF 等文件的编辑和转换；后者侧重视觉设计与演示内容制作。

#### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/genspark-ai/genoffice/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/011_genspark-ai-genoffice.md`。

## English

An office workspace with desktop, CLI and MCP interfaces for editing, converting and searching documents.

### Use cases

- Edit office documents
- Convert files and connect document tools to agents

### Requirements and limits

Some legacy formats import as OOXML copies without writing back to the original format. AI processing can send document content to configured providers; optional reranking sends excerpts. Current documentation reserves ee/ for future enterprise modules under separate terms, alongside the Apache-2.0 core. Provider charges, fidelity and format compatibility require separate checks.

### Getting started

Read the [official documentation](https://github.com/genspark-ai/genoffice/blob/main/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [Huashu Design](huashu-design.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:14.753Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

Current documentation reserves ee/ for future enterprise modules under separate terms. Apache-2.0 is recorded for the core, not all enterprise functionality.

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
    "id": "genoffice",
    "name": "GenOffice",
    "repository": "genspark-ai/genoffice",
    "repo_node_id": "R_kgDOTpHwCA",
    "category": "productivity",
    "tags": [
      "office",
      "documents",
      "mcp"
    ],
    "forms": [
      "desktop",
      "cli",
      "service"
    ],
    "platforms": [
      "linux",
      "macos",
      "windows"
    ],
    "aliases": {
      "zh-CN": [
        "GenOffice"
      ],
      "en": [
        "GenOffice"
      ]
    },
    "summary": {
      "zh-CN": "提供 Office、PDF、Markdown 和 HTML 文件编辑。包含桌面编辑器、CLI、MCP 和智能体技能，可创建、转换和检索文件。",
      "en": "An office workspace with desktop, CLI and MCP interfaces for editing, converting and searching documents."
    },
    "use_cases": {
      "zh-CN": [
        "用智能体生成或修改 Office 文件。在本机转换 PDF 与文档格式。跨办公文件搜索和问答。"
      ],
      "en": [
        "Edit office documents",
        "Convert files and connect document tools to agents"
      ]
    },
    "alternatives": [
      "huashu-design"
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
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "68e32334df324ef4fc79fad3a26487e5abac36055a484bb6c8d7ecf9d8350885",
      "source_url": "https://github.com/genspark-ai/genoffice/blob/main/LICENSE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-14T03:34:43Z",
        "reviewed_at": "2026-11-15T11:03:50.120930Z",
        "url": "https://github.com/genspark-ai/genoffice/commit/a58f354e5dcfc0bacf31e712ea54c0ae63ffbb8c",
        "qualifies": true,
        "reason": {
          "zh-CN": "为应用内 MCP 提供文档块读取接口。已核对提交中的实现文件与差异；未运行上游测试。",
          "en": "Exposes document-block reads through the in-app MCP server. Reviewed implementation changes; upstream tests were not run."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/genspark-ai/genoffice",
        "accessed_at": "2026-11-15T10:48:14.753Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/genspark-ai/genoffice/blob/main/README.md",
        "accessed_at": "2026-11-15T10:54:00.465Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      },
      {
        "url": "https://github.com/genspark-ai/genoffice/blob/main/LICENSE",
        "accessed_at": "2026-11-15T10:53:08.979Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "011",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "14566ae3ff806ef229b73f0ef9d3b9eaa5ee882c35f0a8fd643d800e42c3bcbd",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "tool",
      "pending_reasons": [],
      "english_scope": "editorial_digest",
      "source_card_preserved": true,
      "notes": {
        "zh-CN": "当前 README 说明 ee/ 为未来企业模块预留，并采用单独许可。Apache-2.0 仅按主代码范围记录，不能扩大到全部企业能力。",
        "en": "Current documentation reserves ee/ for future enterprise modules under separate terms. Apache-2.0 is recorded for the core, not all enterprise functionality."
      }
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOTpHwCA",
    "full_name": "genspark-ai/genoffice",
    "stargazers_count": 12376,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "68e32334df324ef4fc79fad3a26487e5abac36055a484bb6c8d7ecf9d8350885",
    "last_success_at": "2026-11-15T10:48:14.753Z"
  }
}
```

</details>
