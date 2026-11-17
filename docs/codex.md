# Codex CLI

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[openai/codex](https://github.com/openai/codex)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 135635 |
| 评估时间 / Evaluated at | 2026-11-17T14:27:00.363607Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:30.445Z |

## 中文

在本机工程中运行的编码智能体，支持终端与编辑器入口。

让 AI 阅读和修改代码、执行工程命令，并检查开发任务的结果。

### 主要功能

- 通过终端围绕本地项目执行编码任务。
- 提供编辑器集成和桌面应用入口。
- 支持 ChatGPT 登录或按官方说明配置 API 认证。

### 环境要求

- 选择与操作系统和处理器匹配的安装包；也可使用 npm 或 Homebrew。
- 需要所选模型服务的认证和网络连接；工程命令还依赖项目自身工具链。

### 使用限制

- 本仓库主要提供本地 CLI；网页端与桌面入口有各自的使用方式。
- 登录方式、模型用量及功能取决于账号配置；生成的变更仍需检查和测试。

### 开始使用

1. 按 README 安装适合本机的 Codex CLI。
2. 在项目目录运行 `codex` 并完成 ChatGPT 或 API 认证。
3. 从一个明确的小任务开始，检查修改差异和项目验证结果。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:30.445Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/openai/codex/commit/49d657aad0e878fb7ab156b91126828c21a0005f)。Add a keyboard diagram to TUI shortcut help (#62048)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/openai/codex/blob/main/README.md)
- [GitHub 元数据 / Repository metadata](https://api.github.com/repos/openai/codex)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

A coding agent that works in local projects through terminal and editor interfaces.

Lets AI read and edit code, run project commands and check development results.

### Features

- Performs coding tasks in a local project from the terminal.
- Provides editor integration and a desktop-app entry point.
- Supports ChatGPT sign-in or API authentication configured through the official instructions.

### Requirements

- Choose an installer matching the operating system and processor, or use npm or Homebrew.
- Requires authentication and network access for the model service; project commands also need the project's own toolchain.

### Limitations

- This repository primarily supplies the local CLI; web and desktop entry points have their own usage flows.
- Authentication, usage and features depend on account configuration; generated changes still require review and testing.

### Getting started

1. Install the Codex CLI for the local platform using the README.
2. Run `codex` in a project directory and complete ChatGPT or API authentication.
3. Start with a small, explicit task and inspect the changes and project validation results.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:30.445Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/openai/codex/commit/49d657aad0e878fb7ab156b91126828c21a0005f).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/openai/codex/blob/main/README.md)
- [GitHub 元数据 / Repository metadata](https://api.github.com/repos/openai/codex)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:27:00.363607Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "codex",
    "name": "Codex CLI",
    "repository": "openai/codex",
    "repo_node_id": "R_kgDOOYsS4Q",
    "category": "development",
    "summary": {
      "zh-CN": "在本机工程中运行的编码智能体，支持终端与编辑器入口。",
      "en": "A coding agent that works in local projects through terminal and editor interfaces."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:27:00.363607Z",
        "en": "2026-11-17T14:27:00.363607Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "让 AI 阅读和修改代码、执行工程命令，并检查开发任务的结果。",
        "en": "Lets AI read and edit code, run project commands and check development results."
      },
      "source_url": "https://github.com/openai/codex/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/openai/codex/commit/49d657aad0e878fb7ab156b91126828c21a0005f",
        "occurred_at": "2026-11-17T13:39:08Z",
        "reviewed_at": "2026-11-17T14:27:00.363607Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "Add a keyboard diagram to TUI shortcut help (#62048) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/openai/codex/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / Repository metadata",
        "url": "https://api.github.com/repos/openai/codex"
      }
    ]
  },
  "snapshot": {
    "full_name": "openai/codex",
    "repo_node_id": "R_kgDOOYsS4Q",
    "stargazers_count": 135635,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:30.445Z",
    "source_url": "https://api.github.com/repos/openai/codex"
  }
}
```

</details>
