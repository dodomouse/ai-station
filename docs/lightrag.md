# LightRAG

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[HKUDS/LightRAG](https://github.com/HKUDS/LightRAG)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 40741 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.602727Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:26.069Z |

## 中文

结合知识图谱与向量检索的 RAG 框架。

利用实体关系和语义召回，为文档问答准备上下文。

### 主要功能

- 从文档提取实体与关系，建立图谱及向量索引。
- 支持增量更新、选择性删除和可选重排序。
- 提供 Web 界面、REST API 和多种存储后端。

### 环境要求

- 需要 Python 3.11 或更高版本，或使用 Docker 部署。
- 需配置语言模型和嵌入模型；正式部署应选择合适的数据库。

### 使用限制

- 默认内存存储仅适合小规模测试。更换嵌入模型需要重新索引。
- 服务器默认关闭认证且监听所有网卡。共享网络部署前应限制监听地址或配置认证。

### 开始使用

1. 按[安装章节](https://github.com/HKUDS/LightRAG#installation)选择包安装或容器部署。
2. 配置模型、嵌入维度、存储与认证。
3. 按[使用指南](https://github.com/HKUDS/LightRAG/blob/main/docs/ExploreLightRAG.md)导入文档并检查查询结果。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:26.069Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/HKUDS/LightRAG/commit/2ecced370abaca1a73364733ba13f737fa97d476)。Merge pull request #3930 from adity982/fix/custom-chunk-ingress-token-limits

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://github.com/HKUDS/LightRAG/blob/main/README.md)
- [Usage guide](https://github.com/HKUDS/LightRAG/blob/main/docs/ExploreLightRAG.md)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

A RAG framework combining knowledge graphs and vector retrieval.

Uses entity relationships and semantic retrieval to prepare context for document question answering.

### Features

- Extracts entities and relationships and builds graph and vector indexes.
- Supports incremental updates, selective deletion, and optional reranking.
- Provides a web interface, REST API, and multiple storage backends.

### Requirements

- Requires Python 3.11 or later, or a Docker deployment.
- Configure language and embedding models; choose suitable databases for production.

### Limitations

- Default in-memory stores suit small tests only; changing the embedding model requires reindexing.
- Authentication is off and all interfaces are bound by default. Restrict binding or configure authentication before shared-network deployment.

### Getting started

1. Choose a package or container installation in the [installation section](https://github.com/HKUDS/LightRAG#installation).
2. Configure models, embedding dimensions, storage, and authentication.
3. Import documents and inspect query results using the [usage guide](https://github.com/HKUDS/LightRAG/blob/main/docs/ExploreLightRAG.md).

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:26.069Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/HKUDS/LightRAG/commit/2ecced370abaca1a73364733ba13f737fa97d476).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://github.com/HKUDS/LightRAG/blob/main/README.md)
- [Usage guide](https://github.com/HKUDS/LightRAG/blob/main/docs/ExploreLightRAG.md)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.602727Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "lightrag",
    "name": "LightRAG",
    "repository": "HKUDS/LightRAG",
    "repo_node_id": "R_kgDOM6XxNA",
    "category": "ai",
    "summary": {
      "zh-CN": "结合知识图谱与向量检索的 RAG 框架。",
      "en": "A RAG framework combining knowledge graphs and vector retrieval."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.602727Z",
        "en": "2026-11-17T14:24:07.602727Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "利用实体关系和语义召回，为文档问答准备上下文。",
        "en": "Uses entity relationships and semantic retrieval to prepare context for document question answering."
      },
      "source_url": "https://github.com/HKUDS/LightRAG/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/HKUDS/LightRAG/commit/2ecced370abaca1a73364733ba13f737fa97d476",
        "occurred_at": "2026-11-17T10:06:05Z",
        "reviewed_at": "2026-11-17T14:24:07.602727Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "Merge pull request #3930 from adity982/fix/custom-chunk-ingress-token-limits 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/HKUDS/LightRAG/blob/main/README.md"
      },
      {
        "title": "Usage guide",
        "url": "https://github.com/HKUDS/LightRAG/blob/main/docs/ExploreLightRAG.md"
      }
    ]
  },
  "snapshot": {
    "full_name": "HKUDS/LightRAG",
    "repo_node_id": "R_kgDOM6XxNA",
    "stargazers_count": 40741,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:26.069Z",
    "source_url": "https://api.github.com/repos/HKUDS/LightRAG"
  }
}
```

</details>
