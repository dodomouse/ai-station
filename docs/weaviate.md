# Weaviate

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[weaviate/weaviate](https://github.com/weaviate/weaviate)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 数据处理 / Data processing |
| 状态 / Status | 已收录 / Included |
| Star | 16952 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.603660Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:26.849Z |

## 中文

结合向量检索、关键词搜索和模型集成的数据库。

为语义搜索和知识问答存储对象、生成嵌入并检索上下文。

### 主要功能

- 导入已有向量，或调用集成模型生成向量。
- 组合向量搜索、关键词查询和条件过滤。
- 支持生成式检索、重排序、多租户和访问控制。

### 环境要求

- 可使用 Docker、Kubernetes 或托管服务；应用需配置对应客户端。
- 自动向量化和生成式检索需要可用的模型服务。

### 使用限制

- 导入自有向量时需保持维度和语义空间一致。
- 托管模型和数据库服务有独立的账号、配额及部署要求。

### 开始使用

1. 按[本地快速开始](https://docs.weaviate.io/weaviate/quickstart/local)启动数据库和所需模型服务。
2. 创建集合，选择向量化方式并导入样本对象。
3. 测试语义与混合查询，再配置访问控制和持久化。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:26.849Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/weaviate/weaviate/commit/a33c0ef138d41eef14247aba4fd70d63c007ee88)。feat(sacr): draft shard sizes on each node before a rebalance plan completes (#13887)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://github.com/weaviate/weaviate/blob/main/README.md)
- [Local quickstart](https://docs.weaviate.io/weaviate/quickstart/local)
- [Model providers](https://docs.weaviate.io/weaviate/model-providers)

## English

A database combining vector retrieval, keyword search, and model integrations.

Stores objects, generates embeddings, and retrieves context for semantic search and knowledge answering.

### Features

- Imports existing vectors or generates them through integrated models.
- Combines vector search, keyword queries, and conditional filtering.
- Supports generative retrieval, reranking, multi-tenancy, and access control.

### Requirements

- Use Docker, Kubernetes, or a hosted service and configure the appropriate client.
- Automatic vectorization and generative retrieval require available model services.

### Limitations

- Imported vectors must use consistent dimensions and embedding spaces.
- Hosted models and database services have separate account, quota, and deployment requirements.

### Getting started

1. Start the database and required model services using the [local quickstart](https://docs.weaviate.io/weaviate/quickstart/local).
2. Create a collection, select a vectorization method, and import sample objects.
3. Test semantic and hybrid queries, then configure access control and persistence.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:26.849Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/weaviate/weaviate/commit/a33c0ef138d41eef14247aba4fd70d63c007ee88).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://github.com/weaviate/weaviate/blob/main/README.md)
- [Local quickstart](https://docs.weaviate.io/weaviate/quickstart/local)
- [Model providers](https://docs.weaviate.io/weaviate/model-providers)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.603660Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "weaviate",
    "name": "Weaviate",
    "repository": "weaviate/weaviate",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnk1NTA3MjY3Nw==",
    "category": "data",
    "summary": {
      "zh-CN": "结合向量检索、关键词搜索和模型集成的数据库。",
      "en": "A database combining vector retrieval, keyword search, and model integrations."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.603660Z",
        "en": "2026-11-17T14:24:07.603660Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "为语义搜索和知识问答存储对象、生成嵌入并检索上下文。",
        "en": "Stores objects, generates embeddings, and retrieves context for semantic search and knowledge answering."
      },
      "source_url": "https://github.com/weaviate/weaviate/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/weaviate/weaviate/commit/a33c0ef138d41eef14247aba4fd70d63c007ee88",
        "occurred_at": "2026-11-17T12:54:29Z",
        "reviewed_at": "2026-11-17T14:24:07.603660Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "feat(sacr): draft shard sizes on each node before a rebalance plan completes (#13887) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/weaviate/weaviate/blob/main/README.md"
      },
      {
        "title": "Local quickstart",
        "url": "https://docs.weaviate.io/weaviate/quickstart/local"
      },
      {
        "title": "Model providers",
        "url": "https://docs.weaviate.io/weaviate/model-providers"
      }
    ]
  },
  "snapshot": {
    "full_name": "weaviate/weaviate",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnk1NTA3MjY3Nw==",
    "stargazers_count": 16952,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:26.849Z",
    "source_url": "https://api.github.com/repos/weaviate/weaviate"
  }
}
```

</details>
