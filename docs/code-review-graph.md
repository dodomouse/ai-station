# code-review-graph

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 32776 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T10:48:17.008Z |

以上为历史核对结果，使用前请复核上游状态。 / This is a dated review; check the current upstream state before use.

## 中文

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

### 原始中文记录（历史快照）

### 024 code-review-graph

仓库：[tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph)

#### 1. 简介

用 Tree-sitter 建立并增量更新本地代码结构图。通过 MCP 和 CLI 提供依赖、变更影响及审查上下文。

#### 2. 适用场景

为跨文件代码审查筛选上下文。查询函数与文件依赖。分析改动的潜在影响范围。

#### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 结构图构建 | 用 Tree-sitter 等解析函数、类、导入、调用、继承及测试关系，保存本地代码图。 | How It Works / Language coverage and notebooks |
| 变更影响分析 | 沿调用和导入关系追踪可能受影响的函数、依赖与测试，为审查提供候选阅读范围。 | Blast-radius analysis |
| 增量更新 | 通过编辑器钩子、Git pre-commit 或 watch 更新。只重解析内容哈希变化的文件。 | Incremental updates |
| 定向查询与可选语义搜索 | 按问题取子图而非整仓上下文。可选接本地或外部嵌入模型增强语义搜索。 | Whole codebase or targeted answer? / Features |
| 图形与结构诊断 | 提供交互式可视化、社区分析、枢纽与桥节点识别，以及耦合和知识缺口线索。 | Features |
| CI 风险审查 | GitHub Action 可根据差异生成带风险评分的 PR 评论，并提供可选风险门禁。 | Risk-scored PR reviews in CI (GitHub Action) |
| 多格式导出 | 可导出 GraphML、Neo4j Cypher、Obsidian vault、JSON 和 SVG 等格式。SVG 有额外依赖。 | Features |

官方来源入口：[官方 README](https://github.com/tirth8205/code-review-graph/blob/staging/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

**平台与环境**

- Python 3.10+ 环境，具体安装方式按文档
- 可接 Codex、Claude Code、Cursor 等受支持客户端
- 语言与框架覆盖各异；不是所有文件类型都能提取语义关系

- 代码为 MIT。基础静态建图和查询在本地运行；可选嵌入模型、编码助手及 CI 算力可能收费。节省 token 的项目报告未经本轮复现，不能预设必省费用。

- 小范围修改可能增加图元信息开销。
- 搜索排名、部分语言入口流程识别和动态关系存在限制。
- EXTRACTED 与 INFERRED 等证据类型及置信度不能省略；影响预测是保守线索。
- 代码图谱不能替代实际测试、编译或运行观测。

**容易找错的需求（不属于本项目能力）**

- 不匹配“精确证明所有运行时影响，绝无遗漏或误报”的要求。
- 不是给任意 PDF、音视频资料建立通用知识图谱的首选定位。

#### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/tirth8205/code-review-graph/blob/staging/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- CLI
- MCP stdio 或 Streamable HTTP
- 编辑器钩子、Git hook 与 watch
- GitHub Action
- 交互式图页面

#### 6. 替代选择

- [Graphify-Labs/graphify](graphify.md#中文)：本项目集中于代码结构与变更影响；后者还纳入文档和多媒体资料。
- [oraios/serena](serena.md#中文)：本项目提供审查所需关系；后者还能按符号编辑代码，部分后端支持重构与调试。

#### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/tirth8205/code-review-graph/blob/staging/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/024_tirth8205-code-review-graph.md`。

## English

Builds an incremental local code graph for dependency queries, impact exploration and review context.

### Use cases

- Navigate relationships around a change
- Gather context for code review

### Requirements and limits

Language and framework coverage vary. Inferred relationships and conservative impact predictions are not runtime proof. Small edits can incur extra graph-context overhead. Optional embeddings and CI resources may cost extra. Graph results do not replace builds or tests.

### Getting started

Read the [official documentation](https://github.com/tirth8205/code-review-graph/blob/staging/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [Graphify](graphify.md#english)
- [Serena](serena.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:17.008Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

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
    "id": "code-review-graph",
    "name": "code-review-graph",
    "repository": "tirth8205/code-review-graph",
    "repo_node_id": "R_kgDORZsJNQ",
    "category": "development",
    "tags": [
      "code-analysis",
      "knowledge-graph",
      "mcp"
    ],
    "forms": [
      "cli",
      "service"
    ],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "code-review-graph"
      ],
      "en": [
        "Code Review Graph"
      ]
    },
    "summary": {
      "zh-CN": "用 Tree-sitter 建立并增量更新本地代码结构图。通过 MCP 和 CLI 提供依赖、变更影响及审查上下文。",
      "en": "Builds an incremental local code graph for dependency queries, impact exploration and review context."
    },
    "use_cases": {
      "zh-CN": [
        "为跨文件代码审查筛选上下文。查询函数与文件依赖。分析改动的潜在影响范围。"
      ],
      "en": [
        "Navigate relationships around a change",
        "Gather context for code review"
      ]
    },
    "alternatives": [
      "graphify",
      "serena"
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
      "license_sha256": "4608284d776c4ca9b88d05c7210f71ab03400520bf7334d72404eba53f56dd4e",
      "source_url": "https://github.com/tirth8205/code-review-graph/blob/bbdda4b9e4b4818a9f04d7ef96ac0e50da13f208/LICENSE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "bbdda4b9e4b4818a9f04d7ef96ac0e50da13f208"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-12T15:47:46Z",
        "reviewed_at": "2026-11-15T11:03:50.120930Z",
        "url": "https://github.com/tirth8205/code-review-graph/commit/b891b6abca7edff503cfd3daeee0d6c0f6a5209b",
        "qualifies": true,
        "reason": {
          "zh-CN": "排序歧义调用目标并修正升级检查。已核对提交中的实现文件与差异；未运行上游测试。",
          "en": "Sorts ambiguous call targets and fixes upgrade checks. Reviewed implementation changes; upstream tests were not run."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/tirth8205/code-review-graph",
        "accessed_at": "2026-11-15T10:48:17.008Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/tirth8205/code-review-graph/blob/staging/README.md",
        "accessed_at": "2026-11-15T10:54:03.126Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      },
      {
        "url": "https://github.com/tirth8205/code-review-graph/blob/bbdda4b9e4b4818a9f04d7ef96ac0e50da13f208/LICENSE",
        "accessed_at": "2026-11-15T10:53:11.360Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "024",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "9cfddee71853e500408506a2e05c31c32885bf77ee111513675c2504e9f51c5e",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "tool",
      "pending_reasons": [],
      "english_scope": "editorial_digest",
      "source_card_preserved": true
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDORZsJNQ",
    "full_name": "tirth8205/code-review-graph",
    "stargazers_count": 32776,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "4608284d776c4ca9b88d05c7210f71ab03400520bf7334d72404eba53f56dd4e",
    "last_success_at": "2026-11-15T10:48:17.008Z"
  }
}
```

</details>
