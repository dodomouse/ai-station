# Langflow

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[langflow-ai/langflow](https://github.com/langflow-ai/langflow)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 156718 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:53.148110Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:37.942Z |

## 中文

以可视化组件构建 Agent 和工作流，并提供 API 与 MCP 服务入口。

把模型、向量数据库和工具组成可复用的 AI 功能。

### 主要功能

- 拖放组件并编辑其 Python 实现。
- 在 Playground 中逐步测试流程。
- 发布 API 或将流程暴露为 MCP 工具。

### 环境要求

- Python 包需要 Python 3.10–3.14，官方推荐 uv。
- 桌面版支持 Windows 和 macOS。也可采用 Docker 部署。

### 使用限制

- 官方 Docker 镜像默认要求认证。旧自动登录部署需按指南迁移。
- 流程中的模型和外部数据库需要分别配置。

### 开始使用

1. 按[安装指南](https://docs.langflow.org/get-started-installation#install-and-run-the-langflow-oss-python-package)选择运行方式。
2. 在可视化编辑器中连接模型和任务组件。
3. 按[Docker 指南](https://docs.langflow.org/deployment-docker)或所选部署方式发布流程。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:37.942Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-16 · commit](https://github.com/langflow-ai/langflow/commit/86fde091f88a8b40507512d36ed78b5917dc165e)。test(google): tolerate timeout reconstruction across worker threads

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/langflow-ai/langflow/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/langflow-ai/langflow)
- [安装指南 / installation guide](https://docs.langflow.org/get-started-installation#install-and-run-the-langflow-oss-python-package)
- [Docker 指南 / Docker guide](https://docs.langflow.org/deployment-docker)

## English

Builds agents and workflows visually and exposes them through API and MCP servers.

Combines models, vector databases and tools into reusable AI functions.

### Features

- Arrange components visually and edit their Python implementations.
- Test flows step by step in the playground.
- Publish APIs or expose flows as MCP tools.

### Requirements

- The Python package requires Python 3.10–3.14; uv is recommended.
- The desktop app supports Windows and macOS. Docker deployment is also available.

### Limitations

- Official Docker images require authentication by default. Existing auto-login deployments need the documented migration.
- Models and external databases used by a flow need separate configuration.

### Getting started

1. Choose a runtime using the [installation guide](https://docs.langflow.org/get-started-installation#install-and-run-the-langflow-oss-python-package).
2. Connect a model and task components in the visual editor.
3. Publish the flow using the [Docker guide](https://docs.langflow.org/deployment-docker) or your chosen deployment method.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:37.942Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-16 · commit](https://github.com/langflow-ai/langflow/commit/86fde091f88a8b40507512d36ed78b5917dc165e).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/langflow-ai/langflow/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/langflow-ai/langflow)
- [安装指南 / installation guide](https://docs.langflow.org/get-started-installation#install-and-run-the-langflow-oss-python-package)
- [Docker 指南 / Docker guide](https://docs.langflow.org/deployment-docker)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:53.148110Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "langflow",
    "name": "Langflow",
    "repository": "langflow-ai/langflow",
    "repo_node_id": "R_kgDOI7jmAw",
    "category": "ai",
    "summary": {
      "zh-CN": "以可视化组件构建 Agent 和工作流，并提供 API 与 MCP 服务入口。",
      "en": "Builds agents and workflows visually and exposes them through API and MCP servers."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:53.148110Z",
        "en": "2026-11-17T14:24:53.148110Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "把模型、向量数据库和工具组成可复用的 AI 功能。",
        "en": "Combines models, vector databases and tools into reusable AI functions."
      },
      "source_url": "https://github.com/langflow-ai/langflow/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/langflow-ai/langflow/commit/86fde091f88a8b40507512d36ed78b5917dc165e",
        "occurred_at": "2026-11-16T18:16:58Z",
        "reviewed_at": "2026-11-17T14:24:53.148110Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "test(google): tolerate timeout reconstruction across worker threads 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/langflow-ai/langflow/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / GitHub metadata",
        "url": "https://api.github.com/repos/langflow-ai/langflow"
      },
      {
        "title": "安装指南 / installation guide",
        "url": "https://docs.langflow.org/get-started-installation#install-and-run-the-langflow-oss-python-package"
      },
      {
        "title": "Docker 指南 / Docker guide",
        "url": "https://docs.langflow.org/deployment-docker"
      }
    ]
  },
  "snapshot": {
    "full_name": "langflow-ai/langflow",
    "repo_node_id": "R_kgDOI7jmAw",
    "stargazers_count": 156718,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:37.942Z",
    "source_url": "https://api.github.com/repos/langflow-ai/langflow"
  }
}
```

</details>
