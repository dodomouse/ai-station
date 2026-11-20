# CrewAI

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[crewAIInc/crewAI](https://github.com/crewAIInc/crewAI)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 61025 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:53.147608Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:38.643Z |

## 中文

以角色化 Agent 协作和事件驱动流程组织多步骤工作。

可将研究、工具调用和结果整理分配给多个智能体，并控制任务流程。

### 主要功能

- 用 Crews 定义角色化智能体协作。
- 用 Flows 编排事件驱动任务。
- 在 Python 程序中组合模型调用和工具。

### 环境要求

- 需要 Python >=3.10 且 <3.14。官方使用 uv 管理依赖。
- 配置所选模型供应商和任务工具的访问方式。

### 使用限制

- 商业 AMP 控制平台与本仓库框架的部署方式不同。
- Windows 安装遇到 chroma-hnswlib 编译错误时，可能需要 C++ Build Tools。

### 开始使用

1. 按[安装指南](https://docs.crewai.com/en/installation)准备 Python 和 uv。
2. 按[README 入门步骤](https://github.com/crewAIInc/crewAI/blob/main/README.md#getting-started)创建项目。
3. 定义角色、任务和工具后运行一个 Crew。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:38.643Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-16 · commit](https://github.com/crewAIInc/crewAI/commit/96c4d85b6423dd06b7f1c38f12dd472399c6ce43)。fix(agent): honor max_execution_time without waiting for the worker (#9324)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/crewAIInc/crewAI/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/crewAIInc/crewAI)
- [安装指南 / installation guide](https://docs.crewai.com/en/installation)
- [README 入门步骤 / README getting-started steps](https://github.com/crewAIInc/crewAI/blob/main/README.md#getting-started)

## English

Organizes multistep work through role-based agents and event-driven workflows.

Assigns research, tool use and result preparation to cooperating agents while controlling the task flow.

### Features

- Define role-based collaboration with Crews.
- Orchestrate event-driven tasks with Flows.
- Combine model calls and tools in Python applications.

### Requirements

- Requires Python >=3.10 and <3.14. The official setup uses uv for dependencies.
- Configure access to the selected model provider and task tools.

### Limitations

- The commercial AMP control plane has a different deployment model from this framework.
- If chroma-hnswlib fails to build on Windows, C++ Build Tools may be required.

### Getting started

1. Prepare Python and uv using the [installation guide](https://docs.crewai.com/en/installation).
2. Create a project using the [README getting-started steps](https://github.com/crewAIInc/crewAI/blob/main/README.md#getting-started).
3. Define roles, tasks and tools, then run a Crew.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:38.643Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-16 · commit](https://github.com/crewAIInc/crewAI/commit/96c4d85b6423dd06b7f1c38f12dd472399c6ce43).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/crewAIInc/crewAI/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/crewAIInc/crewAI)
- [安装指南 / installation guide](https://docs.crewai.com/en/installation)
- [README 入门步骤 / README getting-started steps](https://github.com/crewAIInc/crewAI/blob/main/README.md#getting-started)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:53.147608Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "crewai",
    "name": "CrewAI",
    "repository": "crewAIInc/crewAI",
    "repo_node_id": "R_kgDOKlrpgA",
    "category": "ai",
    "summary": {
      "zh-CN": "以角色化 Agent 协作和事件驱动流程组织多步骤工作。",
      "en": "Organizes multistep work through role-based agents and event-driven workflows."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:53.147608Z",
        "en": "2026-11-17T14:24:53.147608Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "可将研究、工具调用和结果整理分配给多个智能体，并控制任务流程。",
        "en": "Assigns research, tool use and result preparation to cooperating agents while controlling the task flow."
      },
      "source_url": "https://github.com/crewAIInc/crewAI/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/crewAIInc/crewAI/commit/96c4d85b6423dd06b7f1c38f12dd472399c6ce43",
        "occurred_at": "2026-11-16T16:53:25Z",
        "reviewed_at": "2026-11-17T14:24:53.147608Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "fix(agent): honor max_execution_time without waiting for the worker (#9324) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/crewAIInc/crewAI/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / GitHub metadata",
        "url": "https://api.github.com/repos/crewAIInc/crewAI"
      },
      {
        "title": "安装指南 / installation guide",
        "url": "https://docs.crewai.com/en/installation"
      },
      {
        "title": "README 入门步骤 / README getting-started steps",
        "url": "https://github.com/crewAIInc/crewAI/blob/main/README.md#getting-started"
      }
    ]
  },
  "snapshot": {
    "full_name": "crewAIInc/crewAI",
    "repo_node_id": "R_kgDOKlrpgA",
    "stargazers_count": 61025,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:38.643Z",
    "source_url": "https://api.github.com/repos/crewAIInc/crewAI"
  }
}
```

</details>
