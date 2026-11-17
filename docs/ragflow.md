# RAGFlow

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[infiniflow/ragflow](https://github.com/infiniflow/ragflow)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 94306 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.602902Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:26.158Z |

## 中文

结合文档解析、知识组织和智能体检索的 RAG 引擎。

把复杂文档转成知识库，为问答与智能体提供可追溯上下文。

### 主要功能

- 解析多种文档，并用模板划分文本块。
- 生成多种知识结果，包括图谱、树和 Wiki。
- 支持多轮检索、重排序和引用查看。

### 环境要求

- Docker 部署需要 Docker 与 Compose；还需配置语言模型、嵌入模型和重排序模型。
- 源码运行另需 Go 和原生编译依赖；前端开发需要 Node.js。

### 使用限制

- README 明确当前平台部署指南不支持 macOS。部署前应核对目标平台。
- 资源用量随文档引擎、数据量、解析任务和并发变化。

### 开始使用

1. 按[本地部署](https://github.com/infiniflow/ragflow#-local-deployment)准备平台和依赖。
2. 按官方 Compose 配置启动服务并检查健康状态。
3. 配置模型后导入样本文档，检查分块、检索及引用。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:26.158Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/infiniflow/ragflow/commit/cbffd01860ba441acb2c2d5c472c64f4a8a118d4)。fix(docker): authenticate search engine health checks (#22361)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://github.com/infiniflow/ragflow/blob/main/README.md)
- [Quickstart](https://github.com/infiniflow/ragflow/blob/main/docs/quickstart.mdx)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

A RAG engine combining document parsing, knowledge organization, and agentic retrieval.

Turns complex documents into knowledge bases that provide traceable context for question answering and agents.

### Features

- Parses multiple document formats and chunks content with templates.
- Organizes knowledge into graphs, trees, wikis, and other structures.
- Supports multi-step retrieval, reranking, and reference inspection.

### Requirements

- Docker deployment requires Docker and Compose plus configured language, embedding, and reranking models.
- Running from source also requires Go and native build dependencies; frontend development needs Node.js.

### Limitations

- The README states that the current platform deployment guide does not support macOS; check the target platform before deployment.
- Resource use depends on the document engine, data volume, parsing tasks, and concurrency.

### Getting started

1. Prepare the platform and dependencies using [local deployment](https://github.com/infiniflow/ragflow#-local-deployment).
2. Start services with the official Compose configuration and check health.
3. Configure models, import sample documents, and inspect chunks, retrieval, and citations.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:26.158Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/infiniflow/ragflow/commit/cbffd01860ba441acb2c2d5c472c64f4a8a118d4).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://github.com/infiniflow/ragflow/blob/main/README.md)
- [Quickstart](https://github.com/infiniflow/ragflow/blob/main/docs/quickstart.mdx)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.602902Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "ragflow",
    "name": "RAGFlow",
    "repository": "infiniflow/ragflow",
    "repo_node_id": "R_kgDOK4sStA",
    "category": "ai",
    "summary": {
      "zh-CN": "结合文档解析、知识组织和智能体检索的 RAG 引擎。",
      "en": "A RAG engine combining document parsing, knowledge organization, and agentic retrieval."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.602902Z",
        "en": "2026-11-17T14:24:07.602902Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "把复杂文档转成知识库，为问答与智能体提供可追溯上下文。",
        "en": "Turns complex documents into knowledge bases that provide traceable context for question answering and agents."
      },
      "source_url": "https://github.com/infiniflow/ragflow/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/infiniflow/ragflow/commit/cbffd01860ba441acb2c2d5c472c64f4a8a118d4",
        "occurred_at": "2026-11-17T11:28:12Z",
        "reviewed_at": "2026-11-17T14:24:07.602902Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "fix(docker): authenticate search engine health checks (#22361) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/infiniflow/ragflow/blob/main/README.md"
      },
      {
        "title": "Quickstart",
        "url": "https://github.com/infiniflow/ragflow/blob/main/docs/quickstart.mdx"
      }
    ]
  },
  "snapshot": {
    "full_name": "infiniflow/ragflow",
    "repo_node_id": "R_kgDOK4sStA",
    "stargazers_count": 94306,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:26.158Z",
    "source_url": "https://api.github.com/repos/infiniflow/ragflow"
  }
}
```

</details>
