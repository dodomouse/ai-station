# E2B

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[e2b-dev/E2B](https://github.com/e2b-dev/E2B)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 14906 |
| 评估时间 / Evaluated at | 2026-11-17T14:27:00.362818Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:28.793Z |

## 中文

通过 Python 或 JavaScript SDK 管理供智能体使用的隔离执行环境。

为 AI 运行生成代码、处理文件和操作桌面应用提供执行工具。

### 主要功能

- 创建沙箱并执行命令，获取标准输出。
- 通过 Code Interpreter SDK 运行代码。
- 通过 Desktop SDK 操作鼠标、键盘、截图和桌面流。

### 环境要求

- 使用 Python 或 JavaScript/TypeScript 运行环境及对应 SDK。
- 托管服务需要 E2B 账号和 API 凭据；自部署需单独配置 runtime 基础设施。

### 使用限制

- 基础 SDK、Code Interpreter 与 Desktop 是不同安装包。
- 自部署不是仅安装 SDK；云服务用量与基础设施需分别管理。

### 开始使用

1. 按官方 README 安装 `e2b`，并配置托管服务凭据。
2. 用创建沙箱和执行命令的示例确认连接与返回结果。
3. 按任务选择 Code Interpreter 或 Desktop SDK，完成后关闭沙箱。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:28.793Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-16 · commit](https://github.com/e2b-dev/E2B/commit/c4bab34e85a82cf55bbec5ce89d91d1abf299b1a)。chore(deps): bump the uv group across 3 directories with 2 updates (#2143)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/e2b-dev/E2B/blob/main/README.md)
- [GitHub 元数据 / Repository metadata](https://api.github.com/repos/e2b-dev/E2B)

## English

Manages isolated execution environments for agents through Python and JavaScript SDKs.

Provides tools for AI-generated code, file processing and desktop application interaction.

### Features

- Creates sandboxes, runs commands and returns standard output.
- Runs code through the Code Interpreter SDK.
- Provides mouse, keyboard, screenshot and desktop-streaming APIs through the Desktop SDK.

### Requirements

- Requires a Python or JavaScript/TypeScript environment and its SDK.
- Hosted use requires an E2B account and API credentials; self-hosting requires a separate runtime infrastructure setup.

### Limitations

- The base SDK, Code Interpreter and Desktop are separate packages.
- Installing an SDK does not deploy the runtime; hosted usage and infrastructure are managed separately.

### Getting started

1. Install `e2b` using the README and configure hosted-service credentials.
2. Follow the create-sandbox and command-execution example to check connectivity and returned output.
3. Add the Code Interpreter or Desktop SDK for the task, then close the sandbox.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:28.793Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-16 · commit](https://github.com/e2b-dev/E2B/commit/c4bab34e85a82cf55bbec5ce89d91d1abf299b1a).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/e2b-dev/E2B/blob/main/README.md)
- [GitHub 元数据 / Repository metadata](https://api.github.com/repos/e2b-dev/E2B)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:27:00.362818Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "e2b",
    "name": "E2B",
    "repository": "e2b-dev/E2B",
    "repo_node_id": "R_kgDOJFTWgw",
    "category": "development",
    "summary": {
      "zh-CN": "通过 Python 或 JavaScript SDK 管理供智能体使用的隔离执行环境。",
      "en": "Manages isolated execution environments for agents through Python and JavaScript SDKs."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:27:00.362818Z",
        "en": "2026-11-17T14:27:00.362818Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "为 AI 运行生成代码、处理文件和操作桌面应用提供执行工具。",
        "en": "Provides tools for AI-generated code, file processing and desktop application interaction."
      },
      "source_url": "https://github.com/e2b-dev/E2B/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/e2b-dev/E2B/commit/c4bab34e85a82cf55bbec5ce89d91d1abf299b1a",
        "occurred_at": "2026-11-16T16:53:35Z",
        "reviewed_at": "2026-11-17T14:27:00.362818Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "chore(deps): bump the uv group across 3 directories with 2 updates (#2143) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/e2b-dev/E2B/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / Repository metadata",
        "url": "https://api.github.com/repos/e2b-dev/E2B"
      }
    ]
  },
  "snapshot": {
    "full_name": "e2b-dev/E2B",
    "repo_node_id": "R_kgDOJFTWgw",
    "stargazers_count": 14906,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:28.793Z",
    "source_url": "https://api.github.com/repos/e2b-dev/E2B"
  }
}
```

</details>
