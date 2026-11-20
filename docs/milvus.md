# Milvus

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[milvus-io/milvus](https://github.com/milvus-io/milvus)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 数据处理 / Data processing |
| 状态 / Status | 已收录 / Included |
| Star | 46677 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.603180Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:27.202Z |

## 中文

存储向量与标量数据，并提供相似度检索的数据库。

保存模型生成的嵌入，为 RAG、语义搜索和多模态检索提供服务。

### 主要功能

- 提供向量索引、元数据过滤和混合搜索。
- 支持稀疏向量、全文检索及多种索引算法。
- 提供 Lite、单机和分布式部署方式。

### 环境要求

- Python 使用 PyMilvus 客户端；服务端按单机或 Kubernetes 部署指南准备环境。
- 向量维度与所用嵌入模型必须一致。

### 使用限制

- Lite 适合入门和本地使用；分布式能力需部署对应服务。
- 索引算法和硬件配置影响内存、延迟与召回效果。

### 开始使用

1. 按 [README 快速开始](https://github.com/milvus-io/milvus#quickstart)安装客户端并选择 Lite 或服务端。
2. 创建集合，写入向量及需要过滤的字段。
3. 测试向量查询，再按[官方文档](https://milvus.io/docs)选择索引和部署方式。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:27.202Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/milvus-io/milvus/commit/663f0d57407a489030b94e986ea60ad615b930d1)。enhance: propagate candidates and null rejection to element predicates (#55529)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://github.com/milvus-io/milvus/blob/master/README.md)
- [Documentation](https://milvus.io/docs)
- [Milvus Lite](https://milvus.io/docs/milvus_lite.md)

## English

A database that stores vectors and scalar data and provides similarity search.

Stores model-generated embeddings for RAG, semantic search, and multimodal retrieval.

### Features

- Provides vector indexes, metadata filters, and hybrid search.
- Supports sparse vectors, full-text search, and multiple indexing algorithms.
- Offers Lite, standalone, and distributed deployment modes.

### Requirements

- Python uses the PyMilvus client; prepare server infrastructure using standalone or Kubernetes deployment guides.
- Vector dimensions must match the embedding model.

### Limitations

- Lite suits getting started and local use; distributed capabilities require the corresponding service deployment.
- Index algorithms and hardware affect memory use, latency, and retrieval quality.

### Getting started

1. Install a client and choose Lite or server mode using the [README quickstart](https://github.com/milvus-io/milvus#quickstart).
2. Create a collection and insert vectors with filtering fields.
3. Test vector queries, then choose indexes and deployment modes using the [documentation](https://milvus.io/docs).

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:27.202Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/milvus-io/milvus/commit/663f0d57407a489030b94e986ea60ad615b930d1).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://github.com/milvus-io/milvus/blob/master/README.md)
- [Documentation](https://milvus.io/docs)
- [Milvus Lite](https://milvus.io/docs/milvus_lite.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.603180Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "milvus",
    "name": "Milvus",
    "repository": "milvus-io/milvus",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkyMDg3Mjg3NzI=",
    "category": "data",
    "summary": {
      "zh-CN": "存储向量与标量数据，并提供相似度检索的数据库。",
      "en": "A database that stores vectors and scalar data and provides similarity search."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.603180Z",
        "en": "2026-11-17T14:24:07.603180Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "保存模型生成的嵌入，为 RAG、语义搜索和多模态检索提供服务。",
        "en": "Stores model-generated embeddings for RAG, semantic search, and multimodal retrieval."
      },
      "source_url": "https://github.com/milvus-io/milvus/blob/master/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/milvus-io/milvus/commit/663f0d57407a489030b94e986ea60ad615b930d1",
        "occurred_at": "2026-11-17T12:22:07Z",
        "reviewed_at": "2026-11-17T14:24:07.603180Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "enhance: propagate candidates and null rejection to element predicates (#55529) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/milvus-io/milvus/blob/master/README.md"
      },
      {
        "title": "Documentation",
        "url": "https://milvus.io/docs"
      },
      {
        "title": "Milvus Lite",
        "url": "https://milvus.io/docs/milvus_lite.md"
      }
    ]
  },
  "snapshot": {
    "full_name": "milvus-io/milvus",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkyMDg3Mjg3NzI=",
    "stargazers_count": 46677,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:27.202Z",
    "source_url": "https://api.github.com/repos/milvus-io/milvus"
  }
}
```

</details>
