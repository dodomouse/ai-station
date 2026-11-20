# Agno

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[agno-agi/agno](https://github.com/agno-agi/agno)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 43216 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:53.147366Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:38.876Z |

## 中文

将智能体、团队和工作流部署为带 API、MCP、存储及调度能力的服务。

为 AI 配置知识、记忆、工具和任务编排，并让其持续执行组织内的工作。

### 主要功能

- 组合智能体、团队和工作流。
- 通过 AgentOS 提供 API、MCP、审批和恢复执行。
- 保存会话、记忆和平台活动。

### 环境要求

- 选择官方部署模板及其云或本地运行环境。
- 官方平台模板包含 PostgreSQL 存储，模型连接需另行配置。

### 使用限制

- 部署模板和外部模型仍需运维。平台编排不替代工具权限配置。

### 开始使用

1. 按[平台指南](https://docs.agno.com/agent-platform/overview)选择模板。
2. 按[API 教程](https://docs.agno.com/tutorials/agents-as-api)配置并启动智能体。
3. 运行一项任务，在 AgentOS UI 中检查轨迹。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:38.876Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/agno-agi/agno/commit/8b5ce9f85812519a2452ff47981964b202e23828)。fix: postgres drop a failed table from MetaData so a retry can create it (#11723)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/agno-agi/agno/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/agno-agi/agno)
- [平台指南 / platform guide](https://docs.agno.com/agent-platform/overview)
- [API 教程 / API tutorial](https://docs.agno.com/tutorials/agents-as-api)

## English

Deploys agents, teams and workflows as services with APIs, MCP, storage and scheduling.

Configures knowledge, memory, tools and orchestration so agents can carry out continuing organizational work.

### Features

- Compose agents, teams and workflows.
- Serve agents through AgentOS with APIs, MCP, approvals and execution recovery.
- Store conversations, memory and platform activity.

### Requirements

- Choose an official deployment template and its cloud or local runtime.
- The platform template includes PostgreSQL storage; model connections need separate configuration.

### Limitations

- Deployment templates and external models still need operations work. Orchestration does not replace tool permission configuration.

### Getting started

1. Choose a template using the [platform guide](https://docs.agno.com/agent-platform/overview).
2. Configure and start an agent using the [API tutorial](https://docs.agno.com/tutorials/agents-as-api).
3. Run a task and inspect its trace in the AgentOS UI.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:38.876Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/agno-agi/agno/commit/8b5ce9f85812519a2452ff47981964b202e23828).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/agno-agi/agno/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/agno-agi/agno)
- [平台指南 / platform guide](https://docs.agno.com/agent-platform/overview)
- [API 教程 / API tutorial](https://docs.agno.com/tutorials/agents-as-api)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:53.147366Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "agno",
    "name": "Agno",
    "repository": "agno-agi/agno",
    "repo_node_id": "R_kgDOHSAURg",
    "category": "ai",
    "summary": {
      "zh-CN": "将智能体、团队和工作流部署为带 API、MCP、存储及调度能力的服务。",
      "en": "Deploys agents, teams and workflows as services with APIs, MCP, storage and scheduling."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:53.147366Z",
        "en": "2026-11-17T14:24:53.147366Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "为 AI 配置知识、记忆、工具和任务编排，并让其持续执行组织内的工作。",
        "en": "Configures knowledge, memory, tools and orchestration so agents can carry out continuing organizational work."
      },
      "source_url": "https://github.com/agno-agi/agno/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/agno-agi/agno/commit/8b5ce9f85812519a2452ff47981964b202e23828",
        "occurred_at": "2026-11-17T10:06:55Z",
        "reviewed_at": "2026-11-17T14:24:53.147366Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "fix: postgres drop a failed table from MetaData so a retry can create it (#11723) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/agno-agi/agno/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / GitHub metadata",
        "url": "https://api.github.com/repos/agno-agi/agno"
      },
      {
        "title": "平台指南 / platform guide",
        "url": "https://docs.agno.com/agent-platform/overview"
      },
      {
        "title": "API 教程 / API tutorial",
        "url": "https://docs.agno.com/tutorials/agents-as-api"
      }
    ]
  },
  "snapshot": {
    "full_name": "agno-agi/agno",
    "repo_node_id": "R_kgDOHSAURg",
    "stargazers_count": 43216,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:38.876Z",
    "source_url": "https://api.github.com/repos/agno-agi/agno"
  }
}
```

</details>
