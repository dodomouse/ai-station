# LlamaIndex Framework

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[run-llama/llama_index](https://github.com/run-llama/llama_index)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 52926 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.603500Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:26.898Z |

## 中文

连接数据、索引与语言模型的 RAG 和智能体开发框架。

让应用检索自有资料，并把检索结果送入语言模型。

### 主要功能

- 通过连接器导入文件、API 和其他数据源。
- 提供索引、检索器、查询引擎和重排序扩展接口。
- 可选择模型、嵌入和向量存储集成。

### 环境要求

- 需要 Python 与所选集成包；模型可使用托管服务或本地运行方式。

### 使用限制

- 默认示例的数据存于内存，需要持久化时应显式保存。
- 团队当前重点转向 LlamaParse。该文档平台是独立服务，不等同于本框架。

### 开始使用

1. 按[框架文档](https://developers.llamaindex.ai/python/framework/)选择入门包或核心加集成包。
2. 配置语言模型与嵌入模型，读取样本文档并创建索引。
3. 测试查询并检查来源，再配置持久化和应用接口。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:26.898Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-14 · commit](https://github.com/run-llama/llama_index/commit/99d7433f6f71888951379ccca9294e272442c832)。llama-dev: install changed sibling packages without -U (#24141)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://github.com/run-llama/llama_index/blob/main/README.md)
- [Framework documentation](https://developers.llamaindex.ai/python/framework/)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

A framework for RAG and agent applications that connects data, indexes, and language models.

Lets applications retrieve their own data and supply the results to language models.

### Features

- Ingests files, APIs, and other data sources through connectors.
- Provides indexes, retrievers, query engines, and reranking extension points.
- Offers selectable model, embedding, and vector-store integrations.

### Requirements

- Requires Python and selected integration packages; models can use hosted services or local runtimes.

### Limitations

- Default example data is held in memory; save it explicitly when persistence is needed.
- The team's current focus has shifted toward LlamaParse, a separate document platform rather than this framework.

### Getting started

1. Choose the starter package or core plus integrations using the [framework documentation](https://developers.llamaindex.ai/python/framework/).
2. Configure language and embedding models, load sample documents, and create an index.
3. Test queries and inspect sources, then configure persistence and application interfaces.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:26.898Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-14 · commit](https://github.com/run-llama/llama_index/commit/99d7433f6f71888951379ccca9294e272442c832).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://github.com/run-llama/llama_index/blob/main/README.md)
- [Framework documentation](https://developers.llamaindex.ai/python/framework/)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.603500Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "llama-index",
    "name": "LlamaIndex Framework",
    "repository": "run-llama/llama_index",
    "repo_node_id": "R_kgDOIWuq5w",
    "category": "ai",
    "summary": {
      "zh-CN": "连接数据、索引与语言模型的 RAG 和智能体开发框架。",
      "en": "A framework for RAG and agent applications that connects data, indexes, and language models."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.603500Z",
        "en": "2026-11-17T14:24:07.603500Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "让应用检索自有资料，并把检索结果送入语言模型。",
        "en": "Lets applications retrieve their own data and supply the results to language models."
      },
      "source_url": "https://github.com/run-llama/llama_index/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/run-llama/llama_index/commit/99d7433f6f71888951379ccca9294e272442c832",
        "occurred_at": "2026-11-14T02:10:23Z",
        "reviewed_at": "2026-11-17T14:24:07.603500Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "llama-dev: install changed sibling packages without -U (#24141) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/run-llama/llama_index/blob/main/README.md"
      },
      {
        "title": "Framework documentation",
        "url": "https://developers.llamaindex.ai/python/framework/"
      }
    ]
  },
  "snapshot": {
    "full_name": "run-llama/llama_index",
    "repo_node_id": "R_kgDOIWuq5w",
    "stargazers_count": 52926,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:26.898Z",
    "source_url": "https://api.github.com/repos/run-llama/llama_index"
  }
}
```

</details>
