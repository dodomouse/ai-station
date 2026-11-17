# CopilotKit

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 38763 |
| 评估时间 / Evaluated at | 2026-11-17T14:28:37.557461Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:26.162Z |

## 中文

把智能体接入应用的开发框架，提供对话、动态界面和人工确认组件。

让 AI 读取应用状态、调用前端工具，并在执行前向用户收集输入或确认。

### 主要功能

- 提供聊天组件，以及由智能体驱动的界面。
- 在前端和智能体之间同步状态。
- 通过 AG-UI 连接多种智能体框架，支持人工介入流程。

### 环境要求

- 需要受支持的前端环境，以及智能体运行时或模型服务。
- React/Next.js 示例使用 npm；其他框架应按对应指南接入。

### 使用限制

- 前端工具的实际操作仍需应用代码实现。
- Slack 和 Teams 入口依赖云端 CopilotKit Intelligence，不能视为核心组件自动具备的能力。

### 开始使用

1. 运行 `npx copilotkit@latest create` 创建项目。
2. 按官方 README 的 Next.js 示例配置 Runtime 和 Provider。
3. 在[对应框架指南](https://docs.copilotkit.ai/quickstart?ref=github_readme)中连接自己的智能体，再测试状态同步或人工确认。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:26.162Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/CopilotKit/CopilotKit/commit/d6067175e8fdb365f5671cfdd9aea0c0252cdc8b)。更新 GitHub Actions 中 actions/setup-go 的依赖摘要。

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://raw.githubusercontent.com/CopilotKit/CopilotKit/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/CopilotKit/CopilotKit)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

A framework for connecting agents to applications through chat, generated interfaces, and human approval components.

It lets AI read application state, call frontend tools, and request user input or confirmation before acting.

### Features

- Provide chat components and interfaces driven by agents.
- Synchronize state between the frontend and the agent.
- Connect multiple agent frameworks through AG-UI and support human participation in workflows.

### Requirements

- Requires a supported frontend environment and an agent runtime or model service.
- The React/Next.js example uses npm; other frameworks have separate integration guides.

### Limitations

- Application code must implement the operations exposed through frontend tools.
- Slack and Teams depend on cloud-hosted CopilotKit Intelligence and are not automatically provided by the core components.

### Getting started

1. Run `npx copilotkit@latest create` to create a project.
2. Configure the Runtime and Provider using the Next.js example in the official README.
3. Connect your agent with the [appropriate framework guide](https://docs.copilotkit.ai/quickstart?ref=github_readme), then test state synchronization or human approval.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:26.162Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/CopilotKit/CopilotKit/commit/d6067175e8fdb365f5671cfdd9aea0c0252cdc8b).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://raw.githubusercontent.com/CopilotKit/CopilotKit/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/CopilotKit/CopilotKit)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:28:37.557461Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "copilotkit",
    "name": "CopilotKit",
    "repository": "CopilotKit/CopilotKit",
    "repo_node_id": "R_kgDOJxJfAQ",
    "category": "development",
    "summary": {
      "zh-CN": "把智能体接入应用的开发框架，提供对话、动态界面和人工确认组件。",
      "en": "A framework for connecting agents to applications through chat, generated interfaces, and human approval components."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:28:37.557461Z",
        "en": "2026-11-17T14:28:37.557461Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "让 AI 读取应用状态、调用前端工具，并在执行前向用户收集输入或确认。",
        "en": "It lets AI read application state, call frontend tools, and request user input or confirmation before acting."
      },
      "source_url": "https://raw.githubusercontent.com/CopilotKit/CopilotKit/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/CopilotKit/CopilotKit/commit/d6067175e8fdb365f5671cfdd9aea0c0252cdc8b",
        "occurred_at": "2026-11-17T09:47:31Z",
        "reviewed_at": "2026-11-17T14:28:37.557461Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "更新 GitHub Actions 中 actions/setup-go 的依赖摘要。 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://raw.githubusercontent.com/CopilotKit/CopilotKit/main/README.md"
      },
      {
        "title": "GitHub 仓库元数据 / Repository metadata",
        "url": "https://api.github.com/repos/CopilotKit/CopilotKit"
      }
    ]
  },
  "snapshot": {
    "full_name": "CopilotKit/CopilotKit",
    "repo_node_id": "R_kgDOJxJfAQ",
    "stargazers_count": 38763,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:26.162Z",
    "source_url": "https://api.github.com/repos/CopilotKit/CopilotKit"
  }
}
```

</details>
