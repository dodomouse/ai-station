# Arize Phoenix

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[Arize-ai/phoenix](https://github.com/Arize-ai/phoenix)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 部署与运维 / Operations |
| 状态 / Status | 已收录 / Included |
| Star | 12325 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:53.149391Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:39.609Z |

## 中文

提供 OpenTelemetry 追踪、数据集、实验和提示管理，并支持 MCP 查询。

让编码智能体读取执行轨迹、数据集和实验结果，辅助排查与改进 AI 工作流。

### 主要功能

- 追踪模型、检索和工具调用。
- 对数据集运行实验和评测。
- 通过 MCP 查询轨迹与实验记录。

### 环境要求

- 可使用 Python 包，也可用 Docker 或 Kubernetes 部署。
- 应用需接入 OpenTelemetry 或 OpenInference 埋点。

### 使用限制

- 未接入埋点的调用不会自动成为可观测轨迹。
- Phoenix 自托管平台与 Arize AX 托管服务是不同产品形态。

### 开始使用

1. 按[自托管指南](https://arize.com/docs/phoenix/self-hosting)启动 Phoenix。
2. 按[追踪快速入门](https://arize.com/docs/phoenix/get-started/get-started-tracing)接入应用。
3. 运行一个 AI 任务并检查调用轨迹。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:39.609Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/Arize-ai/phoenix/commit/8b409d4531cda2844d5f172119835cfe43ab8a9b)。chore(skills): update external skills (#18002)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/Arize-ai/phoenix/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/Arize-ai/phoenix)
- [自托管指南 / self-hosting guide](https://arize.com/docs/phoenix/self-hosting)
- [追踪快速入门 / tracing quickstart](https://arize.com/docs/phoenix/get-started/get-started-tracing)

## English

Provides OpenTelemetry tracing, datasets, experiments, prompt management and MCP access.

Lets coding agents query traces, datasets and experiments to diagnose and improve AI workflows.

### Features

- Trace model, retrieval and tool calls.
- Run experiments and evaluations on datasets.
- Query traces and experiment records through MCP.

### Requirements

- Use the Python package, or deploy with Docker or Kubernetes.
- Applications need OpenTelemetry or OpenInference instrumentation.

### Limitations

- Calls without instrumentation do not automatically become observable traces.
- Self-hosted Phoenix and managed Arize AX are distinct product offerings.

### Getting started

1. Start Phoenix using the [self-hosting guide](https://arize.com/docs/phoenix/self-hosting).
2. Instrument an application using the [tracing quickstart](https://arize.com/docs/phoenix/get-started/get-started-tracing).
3. Run an AI task and inspect its trace.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:39.609Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/Arize-ai/phoenix/commit/8b409d4531cda2844d5f172119835cfe43ab8a9b).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/Arize-ai/phoenix/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/Arize-ai/phoenix)
- [自托管指南 / self-hosting guide](https://arize.com/docs/phoenix/self-hosting)
- [追踪快速入门 / tracing quickstart](https://arize.com/docs/phoenix/get-started/get-started-tracing)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:53.149391Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "phoenix",
    "name": "Arize Phoenix",
    "repository": "Arize-ai/phoenix",
    "repo_node_id": "R_kgDOIZ8Rag",
    "category": "operations",
    "summary": {
      "zh-CN": "提供 OpenTelemetry 追踪、数据集、实验和提示管理，并支持 MCP 查询。",
      "en": "Provides OpenTelemetry tracing, datasets, experiments, prompt management and MCP access."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:53.149391Z",
        "en": "2026-11-17T14:24:53.149391Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "让编码智能体读取执行轨迹、数据集和实验结果，辅助排查与改进 AI 工作流。",
        "en": "Lets coding agents query traces, datasets and experiments to diagnose and improve AI workflows."
      },
      "source_url": "https://github.com/Arize-ai/phoenix/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/Arize-ai/phoenix/commit/8b409d4531cda2844d5f172119835cfe43ab8a9b",
        "occurred_at": "2026-11-17T11:11:54Z",
        "reviewed_at": "2026-11-17T14:24:53.149391Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "chore(skills): update external skills (#18002) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/Arize-ai/phoenix/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / GitHub metadata",
        "url": "https://api.github.com/repos/Arize-ai/phoenix"
      },
      {
        "title": "自托管指南 / self-hosting guide",
        "url": "https://arize.com/docs/phoenix/self-hosting"
      },
      {
        "title": "追踪快速入门 / tracing quickstart",
        "url": "https://arize.com/docs/phoenix/get-started/get-started-tracing"
      }
    ]
  },
  "snapshot": {
    "full_name": "Arize-ai/phoenix",
    "repo_node_id": "R_kgDOIZ8Rag",
    "stargazers_count": 12325,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:39.609Z",
    "source_url": "https://api.github.com/repos/Arize-ai/phoenix"
  }
}
```

</details>
