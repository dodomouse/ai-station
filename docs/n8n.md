# n8n

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[n8n-io/n8n](https://github.com/n8n-io/n8n)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 自动化 / Automation |
| 状态 / Status | 已收录 / Included |
| Star | 210807 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:53.148298Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:38.292Z |

## 中文

把可视化流程、自定义代码、业务集成和 AI Agent 组合起来。

帮助 AI 调用业务系统、处理数据，并在多步骤流程中接入人工审批。

### 主要功能

- 用可视化节点连接业务应用和模型。
- 在流程中加入 JavaScript 或 Python 代码。
- 配置工具调用、人工审批和执行记录。

### 环境要求

- 官方快速启动使用 Docker；也可选择托管 Cloud。
- 外部模型和业务应用需要对应连接凭据。

### 使用限制

- 自托管需自行维护服务与数据。Cloud 与企业功能有各自的使用条件。
- 流程中的写入操作会影响所连接的业务系统。

### 开始使用

1. 按[Docker 安装指南](https://docs.n8n.io/hosting/installation/docker/)启动服务。
2. 打开编辑器并配置一个模型连接。
3. 从[工作流模板](https://n8n.io/workflows)选择任务并测试。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:38.292Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/n8n-io/n8n/commit/12360b360184edb4f2fe96a3fd7e002e398e42f7)。fix(editor): Keep the canvas visible after a source control pull (#44114)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/n8n-io/n8n/blob/master/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/n8n-io/n8n)
- [Docker 安装指南 / Docker installation guide](https://docs.n8n.io/hosting/installation/docker/)
- [工作流模板 / workflow templates](https://n8n.io/workflows)

## English

Combines visual workflows, custom code, business integrations and AI agents.

Helps AI call business systems, process data and request human approval within multistep workflows.

### Features

- Connect business applications and models with visual nodes.
- Add JavaScript or Python code to workflows.
- Configure tool calls, human approvals and execution records.

### Requirements

- The official quickstart uses Docker; hosted Cloud is another option.
- External models and business applications require connection credentials.

### Limitations

- Self-hosting requires maintaining the service and data. Cloud and enterprise features have their own usage conditions.
- Write operations in a workflow affect the connected business systems.

### Getting started

1. Start the service using the [Docker installation guide](https://docs.n8n.io/hosting/installation/docker/).
2. Open the editor and configure a model connection.
3. Choose a task from the [workflow templates](https://n8n.io/workflows) and test it.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:38.292Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/n8n-io/n8n/commit/12360b360184edb4f2fe96a3fd7e002e398e42f7).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/n8n-io/n8n/blob/master/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/n8n-io/n8n)
- [Docker 安装指南 / Docker installation guide](https://docs.n8n.io/hosting/installation/docker/)
- [工作流模板 / workflow templates](https://n8n.io/workflows)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:53.148298Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "n8n",
    "name": "n8n",
    "repository": "n8n-io/n8n",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkxOTMyMTU1NTQ=",
    "category": "automation",
    "summary": {
      "zh-CN": "把可视化流程、自定义代码、业务集成和 AI Agent 组合起来。",
      "en": "Combines visual workflows, custom code, business integrations and AI agents."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:53.148298Z",
        "en": "2026-11-17T14:24:53.148298Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "帮助 AI 调用业务系统、处理数据，并在多步骤流程中接入人工审批。",
        "en": "Helps AI call business systems, process data and request human approval within multistep workflows."
      },
      "source_url": "https://github.com/n8n-io/n8n/blob/master/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/n8n-io/n8n/commit/12360b360184edb4f2fe96a3fd7e002e398e42f7",
        "occurred_at": "2026-11-17T13:17:26Z",
        "reviewed_at": "2026-11-17T14:24:53.148298Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "fix(editor): Keep the canvas visible after a source control pull (#44114) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/n8n-io/n8n/blob/master/README.md"
      },
      {
        "title": "GitHub 元数据 / GitHub metadata",
        "url": "https://api.github.com/repos/n8n-io/n8n"
      },
      {
        "title": "Docker 安装指南 / Docker installation guide",
        "url": "https://docs.n8n.io/hosting/installation/docker/"
      },
      {
        "title": "工作流模板 / workflow templates",
        "url": "https://n8n.io/workflows"
      }
    ]
  },
  "snapshot": {
    "full_name": "n8n-io/n8n",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkxOTMyMTU1NTQ=",
    "stargazers_count": 210807,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:38.292Z",
    "source_url": "https://api.github.com/repos/n8n-io/n8n"
  }
}
```

</details>
