# Qdrant

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[qdrant/qdrant](https://github.com/qdrant/qdrant)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 数据处理 / Data processing |
| 状态 / Status | 已收录 / Included |
| Star | 35603 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.603413Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:27.485Z |

## 中文

存储向量及附加数据，并提供相似度搜索的数据库。

将嵌入模型接入语义检索、匹配和推荐任务。

### 主要功能

- 支持稠密、稀疏和多向量搜索。
- 按附加 JSON 数据执行文本、数值及地理条件过滤。
- 提供混合搜索、REST/gRPC 接口和多语言客户端。

### 环境要求

- 服务端可用 Docker 部署；应用通过客户端连接。
- 需要准备嵌入向量，并按查询任务配置集合。

### 使用限制

- README 的默认容器示例没有认证且监听所有网卡。正式部署前需配置访问保护。
- Qdrant Edge 在应用进程中运行，其部署方式与服务器不同。

### 开始使用

1. 按[快速开始](https://qdrant.tech/documentation/quickstart/)启动实例并连接客户端。
2. 创建集合，写入向量与附加数据，再测试查询过滤。
3. 按[部署安全说明](https://qdrant.tech/documentation/security/)配置认证与网络访问。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:27.485Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-16 · commit](https://github.com/qdrant/qdrant/commit/23065a0bf6857c3e5da45f6c8939cc746cc0580e)。Bump version to 1.20.2 (#11558)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://github.com/qdrant/qdrant/blob/master/README.md)
- [Quickstart](https://qdrant.tech/documentation/quickstart/)
- [Security](https://qdrant.tech/documentation/security/)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

A database that stores vectors and associated payloads for similarity search.

Connects embedding models to semantic retrieval, matching, and recommendation tasks.

### Features

- Supports dense, sparse, and multi-vector search.
- Filters JSON payloads with text, numeric, and geographic conditions.
- Provides hybrid search, REST/gRPC interfaces, and clients for multiple languages.

### Requirements

- The server can run in Docker, with applications connecting through clients.
- Prepare embedding vectors and configure collections for the query task.

### Limitations

- The default README container example has no authentication and binds all interfaces; configure access protection before production deployment.
- Qdrant Edge runs in the application process and has a different deployment model from the server.

### Getting started

1. Start an instance and connect a client using the [quickstart](https://qdrant.tech/documentation/quickstart/).
2. Create a collection, insert vectors and payloads, and test filtered queries.
3. Configure authentication and network access using the [deployment security guide](https://qdrant.tech/documentation/security/).

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:27.485Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-16 · commit](https://github.com/qdrant/qdrant/commit/23065a0bf6857c3e5da45f6c8939cc746cc0580e).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://github.com/qdrant/qdrant/blob/master/README.md)
- [Quickstart](https://qdrant.tech/documentation/quickstart/)
- [Security](https://qdrant.tech/documentation/security/)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.603413Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "qdrant",
    "name": "Qdrant",
    "repository": "qdrant/qdrant",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkyNjgxNjM2MDk=",
    "category": "data",
    "summary": {
      "zh-CN": "存储向量及附加数据，并提供相似度搜索的数据库。",
      "en": "A database that stores vectors and associated payloads for similarity search."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.603413Z",
        "en": "2026-11-17T14:24:07.603413Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "将嵌入模型接入语义检索、匹配和推荐任务。",
        "en": "Connects embedding models to semantic retrieval, matching, and recommendation tasks."
      },
      "source_url": "https://github.com/qdrant/qdrant/blob/master/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/qdrant/qdrant/commit/23065a0bf6857c3e5da45f6c8939cc746cc0580e",
        "occurred_at": "2026-11-16T09:12:16Z",
        "reviewed_at": "2026-11-17T14:24:07.603413Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "Bump version to 1.20.2 (#11558) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/qdrant/qdrant/blob/master/README.md"
      },
      {
        "title": "Quickstart",
        "url": "https://qdrant.tech/documentation/quickstart/"
      },
      {
        "title": "Security",
        "url": "https://qdrant.tech/documentation/security/"
      }
    ]
  },
  "snapshot": {
    "full_name": "qdrant/qdrant",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkyNjgxNjM2MDk=",
    "stargazers_count": 35603,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:27.485Z",
    "source_url": "https://api.github.com/repos/qdrant/qdrant"
  }
}
```

</details>
