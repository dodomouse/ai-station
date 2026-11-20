# Graphiti

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[getzep/graphiti](https://github.com/getzep/graphiti)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 32877 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:53.148706Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:38.739Z |

## 中文

构建保留时间与来源信息的上下文图谱，支持语义、关键词和图遍历检索。

帮助 AI 查询人物、事件和关系随时间的变化，为持续任务补充可追溯上下文。

### 主要功能

- 从结构化与非结构化信息生成图谱。
- 保留事实的有效时间和来源记录。
- 结合语义、关键词和关系检索。

### 环境要求

- 需要 Python 3.10 或更新版本。
- 需要图数据库、语言模型和嵌入模型。数据库可选 Neo4j、FalkorDB 或 Amazon Neptune。

### 使用限制

- Graphiti 提供建图框架，接入服务、租户权限和运维由使用方实现。
- 自动抽取的实体和关系仍需按任务验证。

### 开始使用

1. 按[README 安装说明](https://github.com/getzep/graphiti/blob/main/README.md#installation)准备依赖。
2. 运行[快速入门示例](https://github.com/getzep/graphiti/blob/main/examples/quickstart/README.md)。
3. 写入一组带时间的信息，再检查检索结果及来源。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:38.739Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-15 · commit](https://github.com/getzep/graphiti/commit/869c1b279e01a2767a464581e1cb657ce0e39271)。Add concurrent ingestion for one graph (#2154)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/getzep/graphiti/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/getzep/graphiti)
- [README 安装说明 / README installation instructions](https://github.com/getzep/graphiti/blob/main/README.md#installation)
- [快速入门示例 / quickstart example](https://github.com/getzep/graphiti/blob/main/examples/quickstart/README.md)

## English

Builds context graphs that retain time and provenance, with semantic, keyword and graph-traversal retrieval.

Helps AI query how people, events and relationships change over time and retrieve context for continuing tasks.

### Features

- Build graphs from structured and unstructured information.
- Preserve facts' validity periods and source records.
- Combine semantic, keyword and relationship retrieval.

### Requirements

- Requires Python 3.10 or later.
- Requires a graph database, language model and embedding model. Database options include Neo4j, FalkorDB and Amazon Neptune.

### Limitations

- Graphiti supplies the graph framework; users implement the surrounding service, tenant permissions and operations.
- Automatically extracted entities and relationships still need task-specific validation.

### Getting started

1. Prepare dependencies using the [README installation instructions](https://github.com/getzep/graphiti/blob/main/README.md#installation).
2. Run the [quickstart example](https://github.com/getzep/graphiti/blob/main/examples/quickstart/README.md).
3. Ingest a set of dated information, then inspect retrieval results and provenance.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:38.739Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-15 · commit](https://github.com/getzep/graphiti/commit/869c1b279e01a2767a464581e1cb657ce0e39271).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/getzep/graphiti/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/getzep/graphiti)
- [README 安装说明 / README installation instructions](https://github.com/getzep/graphiti/blob/main/README.md#installation)
- [快速入门示例 / quickstart example](https://github.com/getzep/graphiti/blob/main/examples/quickstart/README.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:53.148706Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "graphiti",
    "name": "Graphiti",
    "repository": "getzep/graphiti",
    "repo_node_id": "R_kgDOMhI98g",
    "category": "ai",
    "summary": {
      "zh-CN": "构建保留时间与来源信息的上下文图谱，支持语义、关键词和图遍历检索。",
      "en": "Builds context graphs that retain time and provenance, with semantic, keyword and graph-traversal retrieval."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:53.148706Z",
        "en": "2026-11-17T14:24:53.148706Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "帮助 AI 查询人物、事件和关系随时间的变化，为持续任务补充可追溯上下文。",
        "en": "Helps AI query how people, events and relationships change over time and retrieve context for continuing tasks."
      },
      "source_url": "https://github.com/getzep/graphiti/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/getzep/graphiti/commit/869c1b279e01a2767a464581e1cb657ce0e39271",
        "occurred_at": "2026-11-15T20:27:41Z",
        "reviewed_at": "2026-11-17T14:24:53.148706Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "Add concurrent ingestion for one graph (#2154) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/getzep/graphiti/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / GitHub metadata",
        "url": "https://api.github.com/repos/getzep/graphiti"
      },
      {
        "title": "README 安装说明 / README installation instructions",
        "url": "https://github.com/getzep/graphiti/blob/main/README.md#installation"
      },
      {
        "title": "快速入门示例 / quickstart example",
        "url": "https://github.com/getzep/graphiti/blob/main/examples/quickstart/README.md"
      }
    ]
  },
  "snapshot": {
    "full_name": "getzep/graphiti",
    "repo_node_id": "R_kgDOMhI98g",
    "stargazers_count": 32877,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:38.739Z",
    "source_url": "https://api.github.com/repos/getzep/graphiti"
  }
}
```

</details>
