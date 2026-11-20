# LibreChat

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[LibreChat-AI/LibreChat](https://github.com/LibreChat-AI/LibreChat)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 47227 |
| 评估时间 / Evaluated at | 2026-11-17T14:31:52.707546Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:25.810Z |

## 中文

可自行部署的多模型聊天与智能体工作台，支持文件和工具调用。

把模型、资料和工具放在同一对话流程中，支持检索、代码执行及智能体任务。

### 主要功能

- 接入多种模型供应商并管理聊天与智能体。
- 统一处理附件，按需要启用文件搜索和代码工具。
- 提供工具权限控制、上下文统计和执行追踪。

### 环境要求

- 官方本地快速部署使用 Docker；需要模型供应商连接或兼容服务。
- 文件搜索、代码执行及附加服务须按部署文档配置。

### 使用限制

- README 将 Agent Channels 标为 beta，将附加工作区标为高度实验性。
- 文件写入和命令执行受部署与角色权限限制。

### 开始使用

1. 按[本地部署指南](https://www.librechat.ai/docs/quick_start/local_setup)下载仓库并安装 Docker。
2. 复制官方环境模板并完成配置，再运行 `docker compose up -d`。
3. 打开 `http://localhost:3080` 注册账号，连接模型并测试第一条消息。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:25.810Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/LibreChat-AI/LibreChat/commit/c1d3e2358bf68c33f9f771a6b7b18a31b05b6de1)。修复启动时的触发器索引兼容性。

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://raw.githubusercontent.com/LibreChat-AI/LibreChat/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/LibreChat-AI/LibreChat)
- [官方本地部署指南 / Official local setup](https://www.librechat.ai/docs/quick_start/local_setup)

## English

A self-hosted workspace for conversations with multiple models, agents, files, and tools.

It combines models, documents, and tools within a conversation for retrieval, code execution, and agent tasks.

### Features

- Connect multiple model providers and manage chats and agents.
- Handle attachments through a common flow and enable file search or code tools when needed.
- Provide tool permission controls, context usage views, and execution traces.

### Requirements

- The official local quickstart uses Docker and requires a model provider connection or compatible service.
- File search, code execution, and supporting services require deployment-specific configuration.

### Limitations

- The README labels Agent Channels as beta and attached workspaces as highly experimental.
- File writes and command execution depend on deployment and role permissions.

### Getting started

1. Download the repository and install Docker using the [local setup guide](https://www.librechat.ai/docs/quick_start/local_setup).
2. Copy and configure the official environment template, then run `docker compose up -d`.
3. Open `http://localhost:3080`, register an account, connect a model, and test the first message.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:25.810Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/LibreChat-AI/LibreChat/commit/c1d3e2358bf68c33f9f771a6b7b18a31b05b6de1).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://raw.githubusercontent.com/LibreChat-AI/LibreChat/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/LibreChat-AI/LibreChat)
- [官方本地部署指南 / Official local setup](https://www.librechat.ai/docs/quick_start/local_setup)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:31:52.707546Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "librechat",
    "name": "LibreChat",
    "repository": "LibreChat-AI/LibreChat",
    "repo_node_id": "R_kgDOI8xhwA",
    "category": "ai",
    "summary": {
      "zh-CN": "可自行部署的多模型聊天与智能体工作台，支持文件和工具调用。",
      "en": "A self-hosted workspace for conversations with multiple models, agents, files, and tools."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:31:52.707546Z",
        "en": "2026-11-17T14:31:52.707546Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "把模型、资料和工具放在同一对话流程中，支持检索、代码执行及智能体任务。",
        "en": "It combines models, documents, and tools within a conversation for retrieval, code execution, and agent tasks."
      },
      "source_url": "https://raw.githubusercontent.com/LibreChat-AI/LibreChat/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/LibreChat-AI/LibreChat/commit/c1d3e2358bf68c33f9f771a6b7b18a31b05b6de1",
        "occurred_at": "2026-11-17T13:16:57Z",
        "reviewed_at": "2026-11-17T14:31:52.707546Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复启动时的触发器索引兼容性。 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://raw.githubusercontent.com/LibreChat-AI/LibreChat/main/README.md"
      },
      {
        "title": "GitHub 仓库元数据 / Repository metadata",
        "url": "https://api.github.com/repos/LibreChat-AI/LibreChat"
      },
      {
        "title": "官方本地部署指南 / Official local setup",
        "url": "https://www.librechat.ai/docs/quick_start/local_setup"
      }
    ]
  },
  "snapshot": {
    "full_name": "LibreChat-AI/LibreChat",
    "repo_node_id": "R_kgDOI8xhwA",
    "stargazers_count": 47227,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:25.810Z",
    "source_url": "https://api.github.com/repos/LibreChat-AI/LibreChat"
  }
}
```

</details>
