# Letta Code

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[letta-ai/letta-code](https://github.com/letta-ai/letta-code)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 3862 |
| 评估时间 / Evaluated at | 2026-11-17T14:27:00.363309Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:29.281Z |

## 中文

带持久记忆、技能和跨会话状态的终端智能体工具。

让 AI 在连续编码任务中复用项目背景，并结合子智能体和工具执行工作。

### 主要功能

- 保存与检索会话记忆，使用 Git 跟踪上下文。
- 加载全局、项目和智能体技能，支持子智能体调用。
- 通过 CLI 或远程机器运行任务，并配置定时工作。

### 环境要求

- 可通过 npm 安装，或使用捆绑 Node.js 的 uv/pipx 包。后者要求 Python 3.9+。
- 首次启动选择 Letta Cloud 或本地后端，并连接所需模型。

### 使用限制

- Python wheel 路线不支持 Alpine/musl、32 位系统及 Windows ARM64。
- 远程机器等云功能需要登录；原生 Windows 默认关闭自动后台记忆反思。

### 开始使用

1. 按 README 选择 npm、uv 或 pipx 安装方式。
2. 在项目目录运行 `letta`，完成后端选择和模型连接。
3. 用小型代码任务检查工具权限、记忆内容及后续会话复用。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:29.281Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/letta-ai/letta-code/commit/b622fb1bc0941981e08da5ec2b2736d897e9bde1)。fix(skills): look up named real things before drawing them (#5755)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/letta-ai/letta-code/blob/main/README.md)
- [GitHub 元数据 / Repository metadata](https://api.github.com/repos/letta-ai/letta-code)

## English

A terminal agent harness with persistent memory, skills and state across sessions.

Lets AI reuse project context across coding tasks and combine subagents with execution tools.

### Features

- Stores and retrieves conversation memory, with Git-tracked context.
- Loads global, project and agent skills, and supports subagent calls.
- Runs tasks through the CLI or remote computers and supports scheduling.

### Requirements

- Install through npm or the uv/pipx package that bundles Node.js; the latter requires Python 3.9+.
- Choose Letta Cloud or the local backend on first launch and connect the required model.

### Limitations

- The Python-wheel installation does not support Alpine/musl, 32-bit systems or Windows ARM64.
- Cloud features such as remote computers require sign-in; automatic background reflection is disabled by default on native Windows.

### Getting started

1. Choose npm, uv or pipx installation from the README.
2. Run `letta` in the project directory, select a backend and connect a model.
3. Use a small coding task to inspect tool permissions, memory and reuse in a later session.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:29.281Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/letta-ai/letta-code/commit/b622fb1bc0941981e08da5ec2b2736d897e9bde1).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/letta-ai/letta-code/blob/main/README.md)
- [GitHub 元数据 / Repository metadata](https://api.github.com/repos/letta-ai/letta-code)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:27:00.363309Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "letta-code",
    "name": "Letta Code",
    "repository": "letta-ai/letta-code",
    "repo_node_id": "R_kgDOQIyqvg",
    "category": "development",
    "summary": {
      "zh-CN": "带持久记忆、技能和跨会话状态的终端智能体工具。",
      "en": "A terminal agent harness with persistent memory, skills and state across sessions."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:27:00.363309Z",
        "en": "2026-11-17T14:27:00.363309Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "让 AI 在连续编码任务中复用项目背景，并结合子智能体和工具执行工作。",
        "en": "Lets AI reuse project context across coding tasks and combine subagents with execution tools."
      },
      "source_url": "https://github.com/letta-ai/letta-code/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/letta-ai/letta-code/commit/b622fb1bc0941981e08da5ec2b2736d897e9bde1",
        "occurred_at": "2026-11-17T03:51:16Z",
        "reviewed_at": "2026-11-17T14:27:00.363309Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "fix(skills): look up named real things before drawing them (#5755) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/letta-ai/letta-code/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / Repository metadata",
        "url": "https://api.github.com/repos/letta-ai/letta-code"
      }
    ]
  },
  "snapshot": {
    "full_name": "letta-ai/letta-code",
    "repo_node_id": "R_kgDOQIyqvg",
    "stargazers_count": 3862,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:29.281Z",
    "source_url": "https://api.github.com/repos/letta-ai/letta-code"
  }
}
```

</details>
