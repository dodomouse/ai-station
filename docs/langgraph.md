# LangGraph

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[langchain-ai/langgraph](https://github.com/langchain-ai/langgraph)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 45067 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:53.148008Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:39.049Z |

## 中文

构建具有状态、持久执行和人工介入能力的 Agent 工作流。

适合需要恢复执行、分支控制和长期状态的多步骤 AI 任务。

### 主要功能

- 用图和状态转移组织工作流。
- 持久保存状态并从中断处恢复。
- 在执行过程中检查或修改状态。

### 环境要求

- 本仓库提供 Python 实现；JavaScript 实现另有仓库。
- 使用模型或持久存储时，需要配置对应服务。

### 使用限制

- LangGraph 是底层编排框架，任务节点和恢复策略仍需开发者设计。
- LangSmith 托管部署不是本地库自动提供的服务。

### 开始使用

1. 运行[快速入门](https://docs.langchain.com/oss/python/langgraph/quickstart)示例。
2. 按[持久执行说明](https://docs.langchain.com/oss/python/langgraph/durable-execution)添加状态存储。
3. 测试一次中断与恢复，核对任务状态。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:39.049Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-16 · commit](https://github.com/langchain-ai/langgraph/commit/02f2c2e6c992ffccce9e9129781fdd04f015c6fa)。chore(deps): bump opentelemetry-api from 1.45.1 to 1.45.2 in /libs/cli (#9695)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/langchain-ai/langgraph/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/langchain-ai/langgraph)
- [快速入门 / quickstart](https://docs.langchain.com/oss/python/langgraph/quickstart)
- [持久执行说明 / durable execution guide](https://docs.langchain.com/oss/python/langgraph/durable-execution)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

Builds agent workflows with state, durable execution and human intervention.

Supports multistep AI tasks that need execution recovery, branching and long-lived state.

### Features

- Organize workflows through graphs and state transitions.
- Persist state and resume interrupted execution.
- Inspect or change state during execution.

### Requirements

- This repository provides the Python implementation; JavaScript has a separate repository.
- Model use and persistent storage require their respective service configuration.

### Limitations

- LangGraph is a low-level orchestration framework; developers still design task nodes and recovery behavior.
- LangSmith hosted deployment is not automatically supplied by the local library.

### Getting started

1. Run the [quickstart](https://docs.langchain.com/oss/python/langgraph/quickstart) example.
2. Add state persistence using the [durable execution guide](https://docs.langchain.com/oss/python/langgraph/durable-execution).
3. Test interruption and recovery, then check the task state.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:39.049Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-16 · commit](https://github.com/langchain-ai/langgraph/commit/02f2c2e6c992ffccce9e9129781fdd04f015c6fa).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/langchain-ai/langgraph/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/langchain-ai/langgraph)
- [快速入门 / quickstart](https://docs.langchain.com/oss/python/langgraph/quickstart)
- [持久执行说明 / durable execution guide](https://docs.langchain.com/oss/python/langgraph/durable-execution)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:53.148008Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "langgraph",
    "name": "LangGraph",
    "repository": "langchain-ai/langgraph",
    "repo_node_id": "R_kgDOKFU0lQ",
    "category": "ai",
    "summary": {
      "zh-CN": "构建具有状态、持久执行和人工介入能力的 Agent 工作流。",
      "en": "Builds agent workflows with state, durable execution and human intervention."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:53.148008Z",
        "en": "2026-11-17T14:24:53.148008Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "适合需要恢复执行、分支控制和长期状态的多步骤 AI 任务。",
        "en": "Supports multistep AI tasks that need execution recovery, branching and long-lived state."
      },
      "source_url": "https://github.com/langchain-ai/langgraph/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/langchain-ai/langgraph/commit/02f2c2e6c992ffccce9e9129781fdd04f015c6fa",
        "occurred_at": "2026-11-16T08:59:08Z",
        "reviewed_at": "2026-11-17T14:24:53.148008Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "chore(deps): bump opentelemetry-api from 1.45.1 to 1.45.2 in /libs/cli (#9695) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/langchain-ai/langgraph/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / GitHub metadata",
        "url": "https://api.github.com/repos/langchain-ai/langgraph"
      },
      {
        "title": "快速入门 / quickstart",
        "url": "https://docs.langchain.com/oss/python/langgraph/quickstart"
      },
      {
        "title": "持久执行说明 / durable execution guide",
        "url": "https://docs.langchain.com/oss/python/langgraph/durable-execution"
      }
    ]
  },
  "snapshot": {
    "full_name": "langchain-ai/langgraph",
    "repo_node_id": "R_kgDOKFU0lQ",
    "stargazers_count": 45067,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:39.049Z",
    "source_url": "https://api.github.com/repos/langchain-ai/langgraph"
  }
}
```

</details>
