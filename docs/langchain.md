# LangChain

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[langchain-ai/langchain](https://github.com/langchain-ai/langchain)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 149768 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:53.147915Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:38.446Z |

## 中文

用模型、工具及外部集成组件构建 Agent 和 LLM 应用。

帮助 AI 连接数据源和业务工具，并组合调用过程。

### 主要功能

- 通过统一接口调用模型与工具。
- 接入检索、嵌入和第三方服务组件。
- 与 LangGraph 组合编排有状态任务。

### 环境要求

- 本仓库面向 Python。JavaScript/TypeScript 实现位于 LangChain.js。
- 按集成组件安装依赖并配置服务凭据。

### 使用限制

- 模型能力、费用和工具限制取决于所连接的服务。
- LangSmith 调试与部署服务需要单独配置。

### 开始使用

1. 阅读[Python 概览](https://docs.langchain.com/oss/python/langchain/overview)。
2. 按[集成指南](https://docs.langchain.com/oss/python/integrations/providers/overview)接入模型和工具。
3. 运行 README 示例，再加入任务所需组件。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:38.446Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-16 · commit](https://github.com/langchain-ai/langchain/commit/92c7defb0ac54ca2be18fca1bcf89cc88d9356c6)。docs: update OpenWiki (#41862)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/langchain-ai/langchain/blob/master/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/langchain-ai/langchain)
- [Python 概览 / Python overview](https://docs.langchain.com/oss/python/langchain/overview)
- [集成指南 / integration guide](https://docs.langchain.com/oss/python/integrations/providers/overview)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

Builds agents and LLM applications from models, tools and third-party integrations.

Connects AI to data sources and business tools and composes the calls needed for a task.

### Features

- Call models and tools through common interfaces.
- Integrate retrieval, embeddings and third-party services.
- Combine with LangGraph to orchestrate stateful tasks.

### Requirements

- This repository targets Python. JavaScript/TypeScript support is in LangChain.js.
- Install dependencies and configure service credentials for the selected integrations.

### Limitations

- Model capabilities, costs and tool limits depend on the connected services.
- LangSmith debugging and deployment services require separate setup.

### Getting started

1. Read the [Python overview](https://docs.langchain.com/oss/python/langchain/overview).
2. Connect a model and tools using the [integration guide](https://docs.langchain.com/oss/python/integrations/providers/overview).
3. Run the README example, then add the components your task requires.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:38.446Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-16 · commit](https://github.com/langchain-ai/langchain/commit/92c7defb0ac54ca2be18fca1bcf89cc88d9356c6).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/langchain-ai/langchain/blob/master/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/langchain-ai/langchain)
- [Python 概览 / Python overview](https://docs.langchain.com/oss/python/langchain/overview)
- [集成指南 / integration guide](https://docs.langchain.com/oss/python/integrations/providers/overview)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:53.147915Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "langchain",
    "name": "LangChain",
    "repository": "langchain-ai/langchain",
    "repo_node_id": "R_kgDOIPDwlg",
    "category": "ai",
    "summary": {
      "zh-CN": "用模型、工具及外部集成组件构建 Agent 和 LLM 应用。",
      "en": "Builds agents and LLM applications from models, tools and third-party integrations."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:53.147915Z",
        "en": "2026-11-17T14:24:53.147915Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "帮助 AI 连接数据源和业务工具，并组合调用过程。",
        "en": "Connects AI to data sources and business tools and composes the calls needed for a task."
      },
      "source_url": "https://github.com/langchain-ai/langchain/blob/master/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/langchain-ai/langchain/commit/92c7defb0ac54ca2be18fca1bcf89cc88d9356c6",
        "occurred_at": "2026-11-16T19:55:28Z",
        "reviewed_at": "2026-11-17T14:24:53.147915Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "docs: update OpenWiki (#41862) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/langchain-ai/langchain/blob/master/README.md"
      },
      {
        "title": "GitHub 元数据 / GitHub metadata",
        "url": "https://api.github.com/repos/langchain-ai/langchain"
      },
      {
        "title": "Python 概览 / Python overview",
        "url": "https://docs.langchain.com/oss/python/langchain/overview"
      },
      {
        "title": "集成指南 / integration guide",
        "url": "https://docs.langchain.com/oss/python/integrations/providers/overview"
      }
    ]
  },
  "snapshot": {
    "full_name": "langchain-ai/langchain",
    "repo_node_id": "R_kgDOIPDwlg",
    "stargazers_count": 149768,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:38.446Z",
    "source_url": "https://api.github.com/repos/langchain-ai/langchain"
  }
}
```

</details>
