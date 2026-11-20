# OpenAI Agents SDK

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[openai/openai-agents-python](https://github.com/openai/openai-agents-python)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 30735 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:53.148393Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:38.644Z |

## 中文

提供多智能体工作流、工具调用、交接、追踪和语音交互组件。

用于构建由多个 Agent 协作、可检查执行过程的应用。

### 主要功能

- 为智能体配置工具、护栏和交接。
- 用会话管理保存对话历史。
- 记录执行轨迹，并支持语音与实时智能体。

### 环境要求

- 需要 Python 3.10 或更新版本。
- 需要配置所选模型的访问方式；语音和 Redis 支持使用可选依赖。

### 使用限制

- 本词条对应 Python SDK，JavaScript/TypeScript 使用独立项目。
- 模型、托管工具和语音服务有各自的接口与费用限制。

### 开始使用

1. 按[官方文档](https://openai.github.io/openai-agents-python/)安装 SDK。
2. 按[工具指南](https://openai.github.io/openai-agents-python/tools/)定义一个任务工具。
3. 运行[官方示例](https://github.com/openai/openai-agents-python/tree/main/examples)并检查轨迹。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:38.644Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/openai/openai-agents-python/commit/9e05bd5bf299a5ddbb25f7fec8da10bf2baf6133)。fix: preserve pending input history across streamed retries (#6042)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/openai/openai-agents-python/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/openai/openai-agents-python)
- [官方文档 / official docs](https://openai.github.io/openai-agents-python/)
- [工具指南 / tools guide](https://openai.github.io/openai-agents-python/tools/)
- [官方示例 / official example](https://github.com/openai/openai-agents-python/tree/main/examples)

## English

Provides agents, tools, handoffs, tracing and voice components for multi-agent workflows.

Builds applications where multiple agents cooperate and their execution can be inspected.

### Features

- Configure tools, guardrails and handoffs for agents.
- Preserve conversation history through sessions.
- Record execution traces and support voice and realtime agents.

### Requirements

- Requires Python 3.10 or later.
- Configure access to the chosen model; voice and Redis support use optional dependencies.

### Limitations

- This entry covers the Python SDK; JavaScript/TypeScript uses a separate project.
- Models, hosted tools and voice services have their own API and cost limits.

### Getting started

1. Install the SDK using the [official docs](https://openai.github.io/openai-agents-python/).
2. Define a task tool using the [tools guide](https://openai.github.io/openai-agents-python/tools/).
3. Run an [official example](https://github.com/openai/openai-agents-python/tree/main/examples) and inspect its trace.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:38.644Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/openai/openai-agents-python/commit/9e05bd5bf299a5ddbb25f7fec8da10bf2baf6133).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/openai/openai-agents-python/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/openai/openai-agents-python)
- [官方文档 / official docs](https://openai.github.io/openai-agents-python/)
- [工具指南 / tools guide](https://openai.github.io/openai-agents-python/tools/)
- [官方示例 / official example](https://github.com/openai/openai-agents-python/tree/main/examples)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:53.148393Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "openai-agents-python",
    "name": "OpenAI Agents SDK",
    "repository": "openai/openai-agents-python",
    "repo_node_id": "R_kgDOOGidpw",
    "category": "ai",
    "summary": {
      "zh-CN": "提供多智能体工作流、工具调用、交接、追踪和语音交互组件。",
      "en": "Provides agents, tools, handoffs, tracing and voice components for multi-agent workflows."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:53.148393Z",
        "en": "2026-11-17T14:24:53.148393Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "用于构建由多个 Agent 协作、可检查执行过程的应用。",
        "en": "Builds applications where multiple agents cooperate and their execution can be inspected."
      },
      "source_url": "https://github.com/openai/openai-agents-python/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/openai/openai-agents-python/commit/9e05bd5bf299a5ddbb25f7fec8da10bf2baf6133",
        "occurred_at": "2026-11-17T01:01:56Z",
        "reviewed_at": "2026-11-17T14:24:53.148393Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "fix: preserve pending input history across streamed retries (#6042) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/openai/openai-agents-python/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / GitHub metadata",
        "url": "https://api.github.com/repos/openai/openai-agents-python"
      },
      {
        "title": "官方文档 / official docs",
        "url": "https://openai.github.io/openai-agents-python/"
      },
      {
        "title": "工具指南 / tools guide",
        "url": "https://openai.github.io/openai-agents-python/tools/"
      },
      {
        "title": "官方示例 / official example",
        "url": "https://github.com/openai/openai-agents-python/tree/main/examples"
      }
    ]
  },
  "snapshot": {
    "full_name": "openai/openai-agents-python",
    "repo_node_id": "R_kgDOOGidpw",
    "stargazers_count": 30735,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:38.644Z",
    "source_url": "https://api.github.com/repos/openai/openai-agents-python"
  }
}
```

</details>
