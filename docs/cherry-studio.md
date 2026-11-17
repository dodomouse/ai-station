# Cherry Studio

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 53595 |
| 评估时间 / Evaluated at | 2026-11-17T14:28:37.557351Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:26.895Z |

## 中文

整合模型对话、智能体、知识库和文件工具的桌面 AI 工作台。

让智能体读取资料、使用工具并处理多步任务，也可用本地知识库辅助回答。

### 主要功能

- 配置云端模型，或通过 Ollama、LM Studio 使用本地模型。
- 为智能体设置工作区、指令和权限，并通过 Skills、MCP 扩展工具。
- 从文件、文件夹和网页建立知识库，处理 PDF、Office 文档及 OCR。

### 环境要求

- 桌面版面向 Windows、macOS 和 Linux。
- 按功能配置模型凭据、本地模型、附加依赖或系统权限。

### 使用限制

- 模型和工具是否可用取决于供应商、操作系统及配置。
- 本地保存会话不等于所有处理都在本地；云端模型仍调用外部服务。

### 开始使用

1. 从[官方下载页](https://cherryai.com/download)安装适合系统的桌面版。
2. 按[入门指南](https://cherryai.com/docs/en/getting-started/quick-start/)连接一个模型并测试对话。
3. 添加一份资料到知识库，或创建智能体并设置所需工具权限。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:26.895Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/CherryHQ/cherry-studio/commit/195e7f6bf7bdedf5d73ac85ca3f28a39895f295d)。调整额度拒绝处理，由服务端决定是否拒绝请求。

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://raw.githubusercontent.com/CherryHQ/cherry-studio/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/CherryHQ/cherry-studio)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

A desktop AI workspace combining model conversations, agents, knowledge bases, and file tools.

Agents can read materials, use tools, and handle multiple steps, while local knowledge bases supply context for answers.

### Features

- Configure cloud models or use local models through Ollama and LM Studio.
- Set agent workspaces, instructions, and permissions, and extend tools through Skills and MCP.
- Build knowledge bases from files, folders, and web pages, including PDF, Office document, and OCR workflows.

### Requirements

- The desktop application targets Windows, macOS, and Linux.
- Configure provider credentials, local models, additional dependencies, or system permissions for the chosen features.

### Limitations

- Model and tool availability depends on the provider, operating system, and configuration.
- Locally stored conversations do not imply local processing; cloud models still call external services.

### Getting started

1. Install the desktop build for your system from the [official download page](https://cherryai.com/download).
2. Connect a model using the [getting-started guide](https://cherryai.com/docs/en/getting-started/quick-start/) and test a conversation.
3. Add a document to a knowledge base, or create an agent and set the required tool permissions.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:26.895Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/CherryHQ/cherry-studio/commit/195e7f6bf7bdedf5d73ac85ca3f28a39895f295d).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://raw.githubusercontent.com/CherryHQ/cherry-studio/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/CherryHQ/cherry-studio)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:28:37.557351Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "cherry-studio",
    "name": "Cherry Studio",
    "repository": "CherryHQ/cherry-studio",
    "repo_node_id": "R_kgDOL_2xwg",
    "category": "ai",
    "summary": {
      "zh-CN": "整合模型对话、智能体、知识库和文件工具的桌面 AI 工作台。",
      "en": "A desktop AI workspace combining model conversations, agents, knowledge bases, and file tools."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:28:37.557351Z",
        "en": "2026-11-17T14:28:37.557351Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "让智能体读取资料、使用工具并处理多步任务，也可用本地知识库辅助回答。",
        "en": "Agents can read materials, use tools, and handle multiple steps, while local knowledge bases supply context for answers."
      },
      "source_url": "https://raw.githubusercontent.com/CherryHQ/cherry-studio/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/CherryHQ/cherry-studio/commit/195e7f6bf7bdedf5d73ac85ca3f28a39895f295d",
        "occurred_at": "2026-11-17T13:33:00Z",
        "reviewed_at": "2026-11-17T14:28:37.557351Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "调整额度拒绝处理，由服务端决定是否拒绝请求。 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://raw.githubusercontent.com/CherryHQ/cherry-studio/main/README.md"
      },
      {
        "title": "GitHub 仓库元数据 / Repository metadata",
        "url": "https://api.github.com/repos/CherryHQ/cherry-studio"
      }
    ]
  },
  "snapshot": {
    "full_name": "CherryHQ/cherry-studio",
    "repo_node_id": "R_kgDOL_2xwg",
    "stargazers_count": 53595,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:26.895Z",
    "source_url": "https://api.github.com/repos/CherryHQ/cherry-studio"
  }
}
```

</details>
