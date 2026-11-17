# Pydantic AI

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 21255 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:53.148494Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:38.770Z |

## 中文

提供有类型的智能体循环、工具调用、持久执行、评测和多模型接口。

用类型校验、工具能力和任务状态管理构建可执行长任务的 AI 智能体。

### 主要功能

- 校验工具参数和结构化输出。
- 组合记忆、计划、子智能体和持久执行能力。
- 用 Pydantic Evals 检查结果和工具轨迹。

### 环境要求

- 需要 Python 环境及所选模型供应商的配置。
- 语音、沙箱或持久队列功能需相应后端。

### 使用限制

- 类型校验约束数据结构，不证明输出事实正确。
- Logfire 与托管 AI Gateway 需要单独配置。

### 开始使用

1. 按[官方概览](https://pydantic.dev/docs/ai/)安装并配置模型。
2. 按[工具指南](https://pydantic.dev/docs/ai/tools-toolsets/tools/)定义函数和输出类型。
3. 运行一个任务，再用[评测模块](https://pydantic.dev/docs/ai/evals/evals/)检查结果。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:38.770Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/pydantic/pydantic-ai/commit/89287c2c53431e2615859134d44b0006f29fb0ba)。Add `/sandbox` to clai2: run a new conversation in an E2B, boxd, Daytona, OpenSandbox, Modal, Render, Sprites or Kubernetes sandbox, signed in to GitHub (#13592)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/pydantic/pydantic-ai/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/pydantic/pydantic-ai)
- [官方概览 / official overview](https://pydantic.dev/docs/ai/)
- [工具指南 / tools guide](https://pydantic.dev/docs/ai/tools-toolsets/tools/)
- [评测模块 / evaluation module](https://pydantic.dev/docs/ai/evals/evals/)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

Provides typed agent loops, tool calls, durable execution, evaluations and model-provider interfaces.

Uses type validation, tool capabilities and task state to build agents for long-running work.

### Features

- Validate tool arguments and structured outputs.
- Compose memory, planning, subagents and durable execution.
- Evaluate outputs and tool trajectories with Pydantic Evals.

### Requirements

- Requires Python and configuration for the chosen model provider.
- Voice, sandbox and durable-queue features require their respective backends.

### Limitations

- Type validation constrains data structure; it does not prove factual correctness.
- Logfire and the hosted AI Gateway require separate setup.

### Getting started

1. Install and configure a model using the [official overview](https://pydantic.dev/docs/ai/).
2. Define functions and output types using the [tools guide](https://pydantic.dev/docs/ai/tools-toolsets/tools/).
3. Run a task, then check its result using the [evaluation module](https://pydantic.dev/docs/ai/evals/evals/).

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:38.770Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/pydantic/pydantic-ai/commit/89287c2c53431e2615859134d44b0006f29fb0ba).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/pydantic/pydantic-ai/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/pydantic/pydantic-ai)
- [官方概览 / official overview](https://pydantic.dev/docs/ai/)
- [工具指南 / tools guide](https://pydantic.dev/docs/ai/tools-toolsets/tools/)
- [评测模块 / evaluation module](https://pydantic.dev/docs/ai/evals/evals/)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:53.148494Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "pydantic-ai",
    "name": "Pydantic AI",
    "repository": "pydantic/pydantic-ai",
    "repo_node_id": "R_kgDOMMa-Pg",
    "category": "ai",
    "summary": {
      "zh-CN": "提供有类型的智能体循环、工具调用、持久执行、评测和多模型接口。",
      "en": "Provides typed agent loops, tool calls, durable execution, evaluations and model-provider interfaces."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:53.148494Z",
        "en": "2026-11-17T14:24:53.148494Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "用类型校验、工具能力和任务状态管理构建可执行长任务的 AI 智能体。",
        "en": "Uses type validation, tool capabilities and task state to build agents for long-running work."
      },
      "source_url": "https://github.com/pydantic/pydantic-ai/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/pydantic/pydantic-ai/commit/89287c2c53431e2615859134d44b0006f29fb0ba",
        "occurred_at": "2026-11-17T13:17:25Z",
        "reviewed_at": "2026-11-17T14:24:53.148494Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "Add `/sandbox` to clai2: run a new conversation in an E2B, boxd, Daytona, OpenSandbox, Modal, Render, Sprites or Kubernetes sandbox, signed in to GitHub (#13592) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/pydantic/pydantic-ai/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / GitHub metadata",
        "url": "https://api.github.com/repos/pydantic/pydantic-ai"
      },
      {
        "title": "官方概览 / official overview",
        "url": "https://pydantic.dev/docs/ai/"
      },
      {
        "title": "工具指南 / tools guide",
        "url": "https://pydantic.dev/docs/ai/tools-toolsets/tools/"
      },
      {
        "title": "评测模块 / evaluation module",
        "url": "https://pydantic.dev/docs/ai/evals/evals/"
      }
    ]
  },
  "snapshot": {
    "full_name": "pydantic/pydantic-ai",
    "repo_node_id": "R_kgDOMMa-Pg",
    "stargazers_count": 21255,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:38.770Z",
    "source_url": "https://api.github.com/repos/pydantic/pydantic-ai"
  }
}
```

</details>
