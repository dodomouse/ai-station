# fast-agent

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[evalstate/fast-agent](https://github.com/evalstate/fast-agent)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 3972 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:53.147714Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:37.596Z |

## 中文

提供终端智能体、技能、MCP 连接、Shell 工具和多模型工作流。

把提示、MCP 服务和执行工具组合成 AI 任务流程，并用回放模型辅助开发与评测。

### 主要功能

- 在终端运行多模型智能体。
- 连接 MCP 工具并管理技能。
- 用声明式工作流及回放模型开发任务。

### 环境要求

- 官方入门流程使用 Python 工具 uv。
- 配置托管模型凭据，或连接本地模型服务。

### 使用限制

- Shell 工具会执行本地命令，需限制可访问目录和工具。
- Windows 的文件系统和 Docker MCP 配置需要单独调整。

### 开始使用

1. 按[官方文档](https://fast-agent.ai)安装工具。
2. 按[README](https://github.com/evalstate/fast-agent/blob/main/README.md)配置模型与 MCP 服务。
3. 运行一个工作流，检查工具调用与输出。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:37.596Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-16 · commit](https://github.com/evalstate/fast-agent/commit/fed14e0d96e9c4a965dd93a918ebe6c28a5df010)。Release 0.10.56: PTC model text without shell aliases or schema bounds (#1079)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [README / README](https://github.com/evalstate/fast-agent/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/evalstate/fast-agent)
- [官方文档 / official docs](https://fast-agent.ai)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

Provides terminal agents, skills, MCP connections, shell tools and workflows across model providers.

Combines prompts, MCP services and execution tools into AI workflows, with playback models for development and evaluation.

### Features

- Run agents with multiple model providers in the terminal.
- Connect MCP tools and manage skills.
- Develop tasks using declarative workflows and playback models.

### Requirements

- The official setup uses uv for the Python environment.
- Configure hosted-model credentials or connect a local model service.

### Limitations

- Shell tools execute local commands; constrain accessible directories and tools.
- Filesystem and Docker MCP configuration needs specific adjustments on Windows.

### Getting started

1. Install the tool using the [official docs](https://fast-agent.ai).
2. Configure a model and MCP services using the [README](https://github.com/evalstate/fast-agent/blob/main/README.md).
3. Run a workflow and inspect its tool calls and output.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:37.596Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-16 · commit](https://github.com/evalstate/fast-agent/commit/fed14e0d96e9c4a965dd93a918ebe6c28a5df010).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [README / README](https://github.com/evalstate/fast-agent/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/evalstate/fast-agent)
- [官方文档 / official docs](https://fast-agent.ai)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:53.147714Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "fast-agent",
    "name": "fast-agent",
    "repository": "evalstate/fast-agent",
    "repo_node_id": "R_kgDONsNzVQ",
    "category": "ai",
    "summary": {
      "zh-CN": "提供终端智能体、技能、MCP 连接、Shell 工具和多模型工作流。",
      "en": "Provides terminal agents, skills, MCP connections, shell tools and workflows across model providers."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:53.147714Z",
        "en": "2026-11-17T14:24:53.147714Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "把提示、MCP 服务和执行工具组合成 AI 任务流程，并用回放模型辅助开发与评测。",
        "en": "Combines prompts, MCP services and execution tools into AI workflows, with playback models for development and evaluation."
      },
      "source_url": "https://github.com/evalstate/fast-agent/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/evalstate/fast-agent/commit/fed14e0d96e9c4a965dd93a918ebe6c28a5df010",
        "occurred_at": "2026-11-16T23:24:36Z",
        "reviewed_at": "2026-11-17T14:24:53.147714Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "Release 0.10.56: PTC model text without shell aliases or schema bounds (#1079) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "README / README",
        "url": "https://github.com/evalstate/fast-agent/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / GitHub metadata",
        "url": "https://api.github.com/repos/evalstate/fast-agent"
      },
      {
        "title": "官方文档 / official docs",
        "url": "https://fast-agent.ai"
      }
    ]
  },
  "snapshot": {
    "full_name": "evalstate/fast-agent",
    "repo_node_id": "R_kgDONsNzVQ",
    "stargazers_count": 3972,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:37.596Z",
    "source_url": "https://api.github.com/repos/evalstate/fast-agent"
  }
}
```

</details>
