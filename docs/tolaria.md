# Tolaria

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[refactoringhq/tolaria](https://github.com/refactoringhq/tolaria)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 20559 |
| 许可证 / License | AGPL-3.0-or-later |
| 评估时间 / Evaluated at | 2026-11-17T06:06:21.871807+00:00 |

## 中文

用 Markdown 文件和 Git 管理知识库，并通过桌面 AI 面板与 MCP 让模型和编程智能体检索、讨论或编辑笔记。

### 用途与功能

- 以 Markdown 和 YAML frontmatter 保存笔记，并通过 Git 查看差异、历史和同步变更。
- 在桌面 AI 面板中调用已安装的编程智能体，或连接本地、云端模型讨论笔记上下文。
- 提供 MCP 搜索、读取、创建、更新和追加笔记工具，供外部智能体使用。
- 为编程智能体提供不同工具权限模式；直接模型连接保持对话模式，不获得笔记写入或 shell 工具。

### 环境与限制

桌面支持 macOS、Windows 和 Linux，其中 Windows/Linux 仍标为早期支持；iPhone/iPad 为 TestFlight 测试版，尚无桌面 AI 面板。编程智能体需单独安装并完成其自身认证；本地模型需 Ollama、LM Studio 等服务，云模型需相应凭据并可能产生服务费用。Linux 的外部 AI/MCP 流程还需要系统 Node.js。

直接模型会接收当前笔记、链接上下文和对话历史；云端处理受所选服务的数据条款约束。智能体可按权限修改知识库，Power User 模式可能允许 shell 操作。离线笔记管理不代表所有 AI 或 Git 远程同步都离线。代码采用 AGPL-3.0-or-later，名称和标识另受商标政策约束。

### 开始使用

从官方安装页选择桌面版本，首次启动时打开已有知识库或克隆入门示例。在设置中选择已安装的智能体或配置模型服务，再从 AI 面板处理笔记；需要外部工具访问时，显式配置 MCP。源码开发需 Node.js 20+、pnpm 8+、Rust 和对应 Tauri 系统依赖。

参阅[官方 README](https://github.com/refactoringhq/tolaria/blob/2629c2bdb8a5f346c7bd0caab2d3bf453876a990/README.md)。

### 收录与来源

适合希望保留可移植 Markdown、用 Git 检查修改，并让 AI 使用同一套知识库的个人或团队。AI 面板和 MCP 有具体实现；它仍可作为普通笔记应用使用，模型推理能力与费用来自所接服务。

维护证据：[修复触屏布局中笔记列表标题被操作控件挤压的问题，分行排列标题和操作区，并增加标题未被裁切的断言](https://github.com/refactoringhq/tolaria/commit/2d6da35528c6bcf472791673deb98f63dd5ab3cd)（2026-11-17）。

用户于 2026-11-17 提供仓库链接。本条按工程通用标准复核，不设 Star 门槛。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Manage knowledge bases as Markdown files and Git repositories, with a desktop AI panel and MCP integration for models and coding agents to search, discuss or edit notes.

### Uses and features

- Store notes as Markdown with YAML frontmatter, using Git for diffs, history and synchronization.
- Use installed coding agents in the desktop AI panel, or connect local and hosted models to discuss note context.
- Expose MCP tools to search, read, create, update and append notes for external agents.
- Offer tool-permission modes for coding agents; direct model connections remain in chat mode without note-write or shell tools.

### Requirements and limits

Desktop releases support macOS, Windows and Linux, with Windows/Linux marked as early support. iPhone/iPad is a TestFlight beta without the desktop AI panel. Coding agents must be installed and authenticated separately. Local models require services such as Ollama or LM Studio; hosted models require provider credentials and may incur service charges. The Linux external AI/MCP flow also requires system Node.js.

Direct models receive the active note, linked context and conversation history; hosted processing follows the selected provider’s data terms. Agents may edit the vault according to their permissions, and Power User mode can allow shell actions. Offline note management does not make all AI or remote Git synchronization offline. Code uses AGPL-3.0-or-later, while the name and logo have a separate trademark policy.

### Getting started

Choose a desktop build from the official installation page, then open an existing vault or clone the getting-started example. Select an installed agent or configure a model provider in Settings and use the AI panel for note work. Explicitly configure MCP when external tools need access. Source development requires Node.js 20+, pnpm 8+, Rust and platform-specific Tauri dependencies.

See the [official README](https://github.com/refactoringhq/tolaria/blob/2629c2bdb8a5f346c7bd0caab2d3bf453876a990/README.md).

### Review and provenance

Useful for individuals or teams retaining portable Markdown, reviewing edits with Git and letting AI work with the same knowledge base. The AI panel and MCP have concrete integrations. It also works as a conventional note app, while model capabilities and costs come from connected services.

Maintenance evidence: [Fixes note-list titles being squeezed by controls on touch layouts, placing titles and actions on separate rows and adding assertions that titles remain unclipped](https://github.com/refactoringhq/tolaria/commit/2d6da35528c6bcf472791673deb98f63dd5ab3cd) (2026-11-17).

Submitted by the user on 2026-11-17 and reviewed against the general catalog criteria, with no star threshold.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T06:06:21.871807+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "tolaria",
    "name": "Tolaria",
    "repository": "refactoringhq/tolaria",
    "repo_node_id": "R_kgDORQcoNw",
    "category": "productivity",
    "summary": {
      "zh-CN": "用 Markdown 文件和 Git 管理知识库，并通过桌面 AI 面板与 MCP 让模型和编程智能体检索、讨论或编辑笔记。",
      "en": "Manage knowledge bases as Markdown files and Git repositories, with a desktop AI panel and MCP integration for models and coding agents to search, discuss or edit notes."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T06:06:21.871807+00:00",
        "en": "2026-11-17T06:06:21.871807+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合希望保留可移植 Markdown、用 Git 检查修改，并让 AI 使用同一套知识库的个人或团队。AI 面板和 MCP 有具体实现；它仍可作为普通笔记应用使用，模型推理能力与费用来自所接服务。",
      "en": "Useful for individuals or teams retaining portable Markdown, reviewing edits with Git and letting AI work with the same knowledge base. The AI panel and MCP have concrete integrations. It also works as a conventional note app, while model capabilities and costs come from connected services.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "AGPL-3.0-or-later",
      "osi_approved": true,
      "source_url": "https://github.com/refactoringhq/tolaria/blob/2629c2bdb8a5f346c7bd0caab2d3bf453876a990/LICENSE",
      "license_sha256": "0d96a4ff68ad6d4b6f1f30f713b18d5184912ba8dd389f86aa7710db079abcb0",
      "source_commit": "2629c2bdb8a5f346c7bd0caab2d3bf453876a990",
      "reviewed_at": "2026-11-17T06:06:21.871807+00:00",
      "evidence_pinned_at": "2026-11-17T06:06:21.871807+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "Repository code is AGPL-3.0-or-later as explicitly stated in the pinned README and trademarks.md. The Tolaria name and logo follow the separate trademark policy. Dependencies, external agents, model weights and model services retain their own terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-17T03:06:34Z",
        "reviewed_at": "2026-11-17T06:06:21.871807+00:00",
        "url": "https://github.com/refactoringhq/tolaria/commit/2d6da35528c6bcf472791673deb98f63dd5ab3cd",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复触屏布局中笔记列表标题被操作控件挤压的问题，分行排列标题和操作区，并增加标题未被裁切的断言",
          "en": "Fixes note-list titles being squeezed by controls on touch layouts, placing titles and actions on separate rows and adding assertions that titles remain unclipped"
        },
        "reviewed_files": [
          "src/components/note-list/NoteListHeader.tsx",
          "src/components/note-list/NoteListHeader.expand.test.tsx",
          "apps/web/tests/locale-catalog.spec.ts"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/refactoringhq/tolaria",
        "accessed_at": "2026-11-17T06:06:21.871807+00:00"
      },
      {
        "url": "https://github.com/refactoringhq/tolaria/blob/2629c2bdb8a5f346c7bd0caab2d3bf453876a990/README.md",
        "accessed_at": "2026-11-17T06:06:21.871807+00:00"
      },
      {
        "url": "https://github.com/refactoringhq/tolaria/blob/2629c2bdb8a5f346c7bd0caab2d3bf453876a990/LICENSE",
        "accessed_at": "2026-11-17T06:06:21.871807+00:00"
      },
      {
        "url": "https://github.com/refactoringhq/tolaria/commit/2d6da35528c6bcf472791673deb98f63dd5ab3cd",
        "accessed_at": "2026-11-17T06:06:21.871807+00:00"
      },
      {
        "url": "https://github.com/refactoringhq/tolaria/blob/2629c2bdb8a5f346c7bd0caab2d3bf453876a990/site/concepts/ai.md",
        "accessed_at": "2026-11-17T06:06:21.871807+00:00"
      },
      {
        "url": "https://github.com/refactoringhq/tolaria/blob/2629c2bdb8a5f346c7bd0caab2d3bf453876a990/site/guides/use-ai-panel.md",
        "accessed_at": "2026-11-17T06:06:21.871807+00:00"
      },
      {
        "url": "https://github.com/refactoringhq/tolaria/blob/2629c2bdb8a5f346c7bd0caab2d3bf453876a990/site/guides/configure-ai-models.md",
        "accessed_at": "2026-11-17T06:06:21.871807+00:00"
      },
      {
        "url": "https://github.com/refactoringhq/tolaria/blob/2629c2bdb8a5f346c7bd0caab2d3bf453876a990/site/reference/supported-platforms.md",
        "accessed_at": "2026-11-17T06:06:21.871807+00:00"
      },
      {
        "url": "https://github.com/refactoringhq/tolaria/blob/2629c2bdb8a5f346c7bd0caab2d3bf453876a990/trademarks.md",
        "accessed_at": "2026-11-17T06:06:21.871807+00:00"
      },
      {
        "url": "https://github.com/refactoringhq/tolaria/blob/2629c2bdb8a5f346c7bd0caab2d3bf453876a990/mcp-server/tool-service.js",
        "accessed_at": "2026-11-17T06:06:21.871807+00:00"
      }
    ],
    "discovery": {
      "kind": "user_submission",
      "submitted_date": "2026-11-17",
      "source_url": "https://github.com/refactoringhq/tolaria",
      "repository_url": "https://github.com/refactoringhq/tolaria"
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDORQcoNw",
    "full_name": "refactoringhq/tolaria",
    "stargazers_count": 20559,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "AGPL-3.0-or-later",
    "api_license_spdx": "AGPL-3.0",
    "license_sha256": "0d96a4ff68ad6d4b6f1f30f713b18d5184912ba8dd389f86aa7710db079abcb0",
    "last_success_at": "2026-11-17T05:28:54.066887+00:00"
  }
}
```

</details>
