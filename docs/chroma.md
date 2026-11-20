# Chroma

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[chroma-core/chroma](https://github.com/chroma-core/chroma)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 数据处理 / Data processing |
| 状态 / Status | 已收录 / Included |
| Star | 29704 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.602056Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:25.963Z |

## 中文

管理文档、向量嵌入和元数据的检索数据库。

为检索增强生成（RAG）提供语义召回和元数据过滤。

### 主要功能

- 通过集合接口添加、更新、查询和删除文档。
- 自动生成嵌入，也可导入已有向量。
- 按语义相似度检索，并按元数据或文档内容过滤。

### 环境要求

- 可用 Python 或 JavaScript 客户端；支持本地及客户端—服务器模式。

### 使用限制

- 内存客户端用于原型。需要保留数据时，应配置持久化。
- Chroma Cloud 是单独的托管服务，其套餐与功能需另行核对。

### 开始使用

1. 按 [README](https://github.com/chroma-core/chroma#readme) 安装所用语言的客户端。
2. 创建集合，加入文档、标识符和需要过滤的元数据。
3. 参考[官方文档](https://docs.trychroma.com)测试查询，再配置持久化或服务部署。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:25.963Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-07 · commit](https://github.com/chroma-core/chroma/commit/1a3ac2c7c623adbd03ed2508dc27b98cdf26016d)。[DOC] Remove the retired BYOC option from the Cloud docs (#7945)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://github.com/chroma-core/chroma/blob/main/README.md)
- [Documentation](https://docs.trychroma.com)

## English

A retrieval database for documents, vector embeddings, and metadata.

Provides semantic retrieval and metadata filtering for retrieval-augmented generation (RAG).

### Features

- Add, update, query, and delete documents through collections.
- Generate embeddings automatically or import existing vectors.
- Search by semantic similarity with metadata or document-content filters.

### Requirements

- Use Python or JavaScript clients in local or client-server mode.

### Limitations

- The in-memory client suits prototypes; configure persistence to retain data.
- Chroma Cloud is a separate hosted service with its own plans and feature scope.

### Getting started

1. Install the client for your language using the [README](https://github.com/chroma-core/chroma#readme).
2. Create a collection and add documents, identifiers, and filtering metadata.
3. Test queries using the [documentation](https://docs.trychroma.com), then configure persistence or a server deployment.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:25.963Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-07 · commit](https://github.com/chroma-core/chroma/commit/1a3ac2c7c623adbd03ed2508dc27b98cdf26016d).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://github.com/chroma-core/chroma/blob/main/README.md)
- [Documentation](https://docs.trychroma.com)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.602056Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "chroma",
    "name": "Chroma",
    "repository": "chroma-core/chroma",
    "repo_node_id": "R_kgDOII5zmA",
    "category": "data",
    "summary": {
      "zh-CN": "管理文档、向量嵌入和元数据的检索数据库。",
      "en": "A retrieval database for documents, vector embeddings, and metadata."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.602056Z",
        "en": "2026-11-17T14:24:07.602056Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "为检索增强生成（RAG）提供语义召回和元数据过滤。",
        "en": "Provides semantic retrieval and metadata filtering for retrieval-augmented generation (RAG)."
      },
      "source_url": "https://github.com/chroma-core/chroma/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/chroma-core/chroma/commit/1a3ac2c7c623adbd03ed2508dc27b98cdf26016d",
        "occurred_at": "2026-11-07T04:52:06Z",
        "reviewed_at": "2026-11-17T14:24:07.602056Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "[DOC] Remove the retired BYOC option from the Cloud docs (#7945) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/chroma-core/chroma/blob/main/README.md"
      },
      {
        "title": "Documentation",
        "url": "https://docs.trychroma.com"
      }
    ]
  },
  "snapshot": {
    "full_name": "chroma-core/chroma",
    "repo_node_id": "R_kgDOII5zmA",
    "stargazers_count": 29704,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:25.963Z",
    "source_url": "https://api.github.com/repos/chroma-core/chroma"
  }
}
```

</details>
