# Haystack

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[deepset-ai/haystack](https://github.com/deepset-ai/haystack)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 27027 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.602418Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:26.033Z |

## 中文

用组件、流水线和智能体组织语言模型应用的 Python 框架。

将检索、路由、记忆和生成组合成可定制的知识问答流程。

### 主要功能

- 组合索引、检索、工具调用和评测组件。
- 用分支、循环及条件逻辑控制流水线。
- 支持异步执行、流式输出和多个模型提供商。

### 环境要求

- 需要 Python 环境；模型和文档存储按所选集成配置。

### 使用限制

- 使用托管模型时，需要服务账号与可用配额。
- 默认收集组件使用统计，可按官方遥测文档关闭。

### 开始使用

1. 按[安装文档](https://docs.haystack.deepset.ai/docs/installation)安装 `haystack-ai`。
2. 跟随[快速开始](https://haystack.deepset.ai/overview/quick-start)配置模型并连接首条流水线。
3. 用自己的文档测试检索结果，再添加路由或智能体工具。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:26.033Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/deepset-ai/haystack/commit/2b85450acc16c28f6069ed3644f0eed31c76c249)。fix: preserve non-string dict keys in pipeline snapshot serialization (#13732)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://github.com/deepset-ai/haystack/blob/main/README.md)
- [Installation](https://docs.haystack.deepset.ai/docs/installation)
- [Quickstart](https://haystack.deepset.ai/overview/quick-start)
- [Telemetry](https://docs.haystack.deepset.ai/docs/telemetry)

## English

A Python framework for composing language-model applications with components, pipelines, and agents.

Combines retrieval, routing, memory, and generation into configurable knowledge-answering workflows.

### Features

- Compose indexing, retrieval, tool-calling, and evaluation components.
- Control pipelines with branches, loops, and conditional logic.
- Supports asynchronous execution, streaming output, and multiple model providers.

### Requirements

- Requires Python; configure models and document stores for the chosen integrations.

### Limitations

- Hosted models require a service account and available quota.
- Component usage telemetry is enabled by default and can be disabled as documented.

### Getting started

1. Install `haystack-ai` using the [installation guide](https://docs.haystack.deepset.ai/docs/installation).
2. Configure a model and connect your first pipeline using the [quickstart](https://haystack.deepset.ai/overview/quick-start).
3. Test retrieval with your documents, then add routing or agent tools.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:26.033Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/deepset-ai/haystack/commit/2b85450acc16c28f6069ed3644f0eed31c76c249).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://github.com/deepset-ai/haystack/blob/main/README.md)
- [Installation](https://docs.haystack.deepset.ai/docs/installation)
- [Quickstart](https://haystack.deepset.ai/overview/quick-start)
- [Telemetry](https://docs.haystack.deepset.ai/docs/telemetry)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.602418Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "haystack",
    "name": "Haystack",
    "repository": "deepset-ai/haystack",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkyMjE2NTQ2Nzg=",
    "category": "ai",
    "summary": {
      "zh-CN": "用组件、流水线和智能体组织语言模型应用的 Python 框架。",
      "en": "A Python framework for composing language-model applications with components, pipelines, and agents."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.602418Z",
        "en": "2026-11-17T14:24:07.602418Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "将检索、路由、记忆和生成组合成可定制的知识问答流程。",
        "en": "Combines retrieval, routing, memory, and generation into configurable knowledge-answering workflows."
      },
      "source_url": "https://github.com/deepset-ai/haystack/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/deepset-ai/haystack/commit/2b85450acc16c28f6069ed3644f0eed31c76c249",
        "occurred_at": "2026-11-17T13:15:04Z",
        "reviewed_at": "2026-11-17T14:24:07.602418Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "fix: preserve non-string dict keys in pipeline snapshot serialization (#13732) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/deepset-ai/haystack/blob/main/README.md"
      },
      {
        "title": "Installation",
        "url": "https://docs.haystack.deepset.ai/docs/installation"
      },
      {
        "title": "Quickstart",
        "url": "https://haystack.deepset.ai/overview/quick-start"
      },
      {
        "title": "Telemetry",
        "url": "https://docs.haystack.deepset.ai/docs/telemetry"
      }
    ]
  },
  "snapshot": {
    "full_name": "deepset-ai/haystack",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkyMjE2NTQ2Nzg=",
    "stargazers_count": 27027,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:26.033Z",
    "source_url": "https://api.github.com/repos/deepset-ai/haystack"
  }
}
```

</details>
