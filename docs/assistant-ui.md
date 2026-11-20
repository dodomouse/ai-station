# assistant-ui

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[assistant-ui/assistant-ui](https://github.com/assistant-ui/assistant-ui)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 13288 |
| 评估时间 / Evaluated at | 2026-11-17T14:28:37.556774Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:26.138Z |

## 中文

为 React 应用构建 AI 对话界面的 TypeScript 组件库。

将模型回复、工具调用和人工确认放入应用界面，便于用户参与 AI 任务。

### 主要功能

- 组合会话、消息、输入框和历史列表组件。
- 支持流式输出、附件、Markdown、重试和键盘操作。
- 把工具结果渲染为 React 组件，接入 Vercel AI SDK 或自定义后端。

### 环境要求

- 需要 React 项目及可运行 npm/npx 的 JavaScript 开发环境。
- 需要模型后端；按所用适配器配置连接。

### 使用限制

- 界面组件不包含模型推理服务。
- 托管历史、遥测和文件存储由独立的 assistant-cloud 提供。

### 开始使用

1. 按官方 README 运行 `npx assistant-ui@latest create` 创建示例项目。
2. 已有项目可运行 `npx assistant-ui@latest init`，再按 Usage 示例连接运行时。
3. 配置模型后端，使用 `Thread` 组件测试消息与工具结果。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:26.138Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/assistant-ui/assistant-ui/commit/a4c705b08dbe04159c0a10f1cf9e737928d54c3c)。更新文档中的语音输入支持示例，改为通过 useSyncExternalStore 读取状态。

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://raw.githubusercontent.com/assistant-ui/assistant-ui/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/assistant-ui/assistant-ui)

## English

A TypeScript component library for building AI chat interfaces in React applications.

It brings model responses, tool calls, and human approvals into an application so users can participate in AI tasks.

### Features

- Compose threads, messages, input controls, and conversation lists.
- Support streaming, attachments, Markdown, retries, and keyboard interaction.
- Render tool results as React components and connect to the Vercel AI SDK or a custom backend.

### Requirements

- Requires a React project and a JavaScript development environment that can run npm/npx.
- Requires a model backend configured for the selected runtime adapter.

### Limitations

- The UI components do not include a model inference service.
- Managed history, telemetry, and file storage are provided separately through assistant-cloud.

### Getting started

1. Run `npx assistant-ui@latest create` following the official README to create a starter project.
2. For an existing project, run `npx assistant-ui@latest init` and connect a runtime using the Usage example.
3. Configure the model backend and test messages and tool results with the `Thread` component.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:26.138Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/assistant-ui/assistant-ui/commit/a4c705b08dbe04159c0a10f1cf9e737928d54c3c).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://raw.githubusercontent.com/assistant-ui/assistant-ui/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/assistant-ui/assistant-ui)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:28:37.556774Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "assistant-ui",
    "name": "assistant-ui",
    "repository": "assistant-ui/assistant-ui",
    "repo_node_id": "R_kgDOKwunUQ",
    "category": "development",
    "summary": {
      "zh-CN": "为 React 应用构建 AI 对话界面的 TypeScript 组件库。",
      "en": "A TypeScript component library for building AI chat interfaces in React applications."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:28:37.556774Z",
        "en": "2026-11-17T14:28:37.556774Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "将模型回复、工具调用和人工确认放入应用界面，便于用户参与 AI 任务。",
        "en": "It brings model responses, tool calls, and human approvals into an application so users can participate in AI tasks."
      },
      "source_url": "https://raw.githubusercontent.com/assistant-ui/assistant-ui/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/assistant-ui/assistant-ui/commit/a4c705b08dbe04159c0a10f1cf9e737928d54c3c",
        "occurred_at": "2026-11-17T13:37:16Z",
        "reviewed_at": "2026-11-17T14:28:37.556774Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "更新文档中的语音输入支持示例，改为通过 useSyncExternalStore 读取状态。 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://raw.githubusercontent.com/assistant-ui/assistant-ui/main/README.md"
      },
      {
        "title": "GitHub 仓库元数据 / Repository metadata",
        "url": "https://api.github.com/repos/assistant-ui/assistant-ui"
      }
    ]
  },
  "snapshot": {
    "full_name": "assistant-ui/assistant-ui",
    "repo_node_id": "R_kgDOKwunUQ",
    "stargazers_count": 13288,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:26.138Z",
    "source_url": "https://api.github.com/repos/assistant-ui/assistant-ui"
  }
}
```

</details>
