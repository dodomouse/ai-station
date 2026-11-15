# Archify

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[tt-a1i/archify](https://github.com/tt-a1i/archify)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 96538 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T10:48:17.071Z |

以上为历史核对结果，使用前请复核上游状态。 / This is a dated review; check the current upstream state before use.

## 中文

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

### 原始中文记录（历史快照）

### 025 Archify

仓库：[tt-a1i/archify](https://github.com/tt-a1i/archify)

#### 1. 简介

把想法、计划或代码仓资料生成交互式 HTML 图示。可制作架构图、流程图和带来源的解释页面。

#### 2. 适用场景

制作代码仓架构图与流程图。生成带引用的技术解释页面。探索节点关系和路径。分享独立 HTML 或导出图片。

#### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 多类图示 | 支持架构、流程、时序、数据流、生命周期、ERD、类、树、时间线和瀑布图。 | Choose the right diagram |
| 交互探索 | 查看节点关系，跟踪路径及作者提供的上下游关系。 | Explore and share the output |
| 源码关联 | 从仓库资料绘图，来源卡片可链接到固定提交的代码片段。 | Understand a real repository / Ask a question, get a one-page answer |
| 单页解释 | 把结论、表格、步骤、代码和校验图组合成解释页。 | Ask a question, get a one-page answer |
| 便携分享与导出 | 交付单个HTML，支持图像导出和打印PDF等分享方式。 | Download it. Open it. Explore it. / Ask a question, get a one-page answer |
| 前后结构比较 | Architecture Delta比较已验证的Before/Delta/After快照。 | Choose the right diagram |

官方来源入口：[官方 README](https://github.com/tt-a1i/archify/blob/main/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

**平台与环境**

- HTML通过浏览器查看
- 完整渲染需相应Node环境；具体集成版本条件各异

- Apache-2.0开源；生成所用智能体、模型或外部服务费用另计。
- 第三方在线服务或付费计划不代表Archify官方。

- 绘图及可达关系来自作者描述/来源，不自动等于运行时影响。
- 架构差异不能证明风险、测试充分或合并安全。
- 不是线上基础设施扫描器；本轮未生成和验证图示。

**容易找错的需求（不属于本项目能力）**

- 自动抓到生产环境真实链路并持续监控。
- 看完架构差异自动保证此次代码可以安全合并。

#### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/tt-a1i/archify/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- Claude Code、Codex CLI、OpenCode等技能环境
- Node CLI与图示校验工作流
- Claude.ai技能（取决于沙箱Node访问）
- 可选Hermes Agent和DeepSeek Harness社区集成

#### 6. 替代选择

- [wheresryan22/anatomy](anatomy.md#中文)：本项目侧重带来源的架构、流程和解释图；后者以等轴测图解释机械与抽象机制。

#### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/tt-a1i/archify/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/025_tt-a1i-archify.md`。

## English

Turns ideas, plans and repository material into interactive HTML diagrams and explanatory pages with source references.

### Use cases

- Explain system architecture
- Create navigable flow and relationship diagrams

### Requirements and limits

Diagrams depend on their input evidence and do not prove runtime behavior, test coverage or merge safety. Rendering needs the documented Node environment; models and external services cost extra. A recent fix to piped Explainer receipts provides code-level maintenance evidence.

### Getting started

Read the [official documentation](https://github.com/tt-a1i/archify/blob/main/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [Anatomy](anatomy.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:17.071Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

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
    "id": "archify",
    "name": "Archify",
    "repository": "tt-a1i/archify",
    "repo_node_id": "R_kgDOSDCHbQ",
    "category": "development",
    "tags": [
      "architecture",
      "diagrams",
      "html"
    ],
    "forms": [
      "cli",
      "web"
    ],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "Archify"
      ],
      "en": [
        "Archify"
      ]
    },
    "summary": {
      "zh-CN": "把想法、计划或代码仓资料生成交互式 HTML 图示。可制作架构图、流程图和带来源的解释页面。",
      "en": "Turns ideas, plans and repository material into interactive HTML diagrams and explanatory pages with source references."
    },
    "use_cases": {
      "zh-CN": [
        "制作代码仓架构图与流程图。生成带引用的技术解释页面。探索节点关系和路径。分享独立 HTML 或导出图片。"
      ],
      "en": [
        "Explain system architecture",
        "Create navigable flow and relationship diagrams"
      ]
    },
    "alternatives": [
      "anatomy"
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
      "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
      "source_url": "https://github.com/tt-a1i/archify/blob/main/LICENSE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-10T01:32:12Z",
        "reviewed_at": "2026-11-15T11:03:50.120930Z",
        "url": "https://github.com/tt-a1i/archify/commit/7e45f36c66de1254d5ad6ba1d878f6499ea269fd",
        "qualifies": true,
        "reason": {
          "zh-CN": "修正通过管道输出时 Explainer 检查回执被截断的问题。已核对提交中的实现文件与差异；未运行上游测试。",
          "en": "Flushes complete Explainer check receipts through piped stdout. Reviewed implementation changes; upstream tests were not run."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/tt-a1i/archify",
        "accessed_at": "2026-11-15T10:48:17.071Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/tt-a1i/archify/blob/main/README.md",
        "accessed_at": "2026-11-15T10:54:02.708Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      },
      {
        "url": "https://github.com/tt-a1i/archify/blob/main/LICENSE",
        "accessed_at": "2026-11-15T10:53:11.721Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "025",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "5d4f0c3819dc7c499e40882c761ae07ccc5346b0d57847a414461b2cbb091746",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "tool",
      "pending_reasons": [],
      "english_scope": "editorial_digest",
      "source_card_preserved": true
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOSDCHbQ",
    "full_name": "tt-a1i/archify",
    "stargazers_count": 96538,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
    "last_success_at": "2026-11-15T10:48:17.071Z"
  }
}
```

</details>
