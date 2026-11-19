# Cursor Plugins

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[cursor/plugins](https://github.com/cursor/plugins)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 17282 |
| 评估时间 / Evaluated at | 2026-11-19T04:00:25.255927Z |

## 中文

Cursor Plugins 是 Cursor 官方维护的插件规范与插件集合，面向 AI 编码智能体。仓库中每个插件是一个独立目录，带有 .cursor-plugin/plugin.json 清单，覆盖开发工具、集成与效率等类别，让编码智能体能够调用外部工具与服务。

它帮助 AI 编码智能体在 Cursor 中完成具体任务，例如代码审查、分支管理、检索文档与操作第三方 SaaS 服务。

### 主要功能

- 提供 Cursor 插件规范；每个插件以独立目录和 .cursor-plugin/plugin.json 清单描述。
- 收录 Cursor 官方及第三方插件，涵盖 Utilities、Developer Tools、Productivity、Integrations 等类别。
- 开发工具类包括教学、持续学习、团队 CI 与审查工作流、脚手架、Ralph Loop、代理兼容性扫描、PR/Docs Canvas、Cursor SDK 与 Origin API 等插件。
- 集成类插件连接 Gmail、Google Drive、Salesforce、GitHub、Playwright、Zoom、X 等外部服务，供智能体查询与操作。
- 提供 create-plugin 插件用于脚手架与校验新插件。

### 环境要求

- 需要安装支持插件的 Cursor 编辑器或智能体；本仓库本身是规范与插件清单集合，不是独立运行的应用程序。
- 核心规范与多数开发工具插件不需要额外的模型密钥或统一的数据服务配置。
- 第三方集成插件需要对应外部服务的账号与授权（例如 Google Workspace、Salesforce、GitHub 等）；具体依赖以各插件目录内的清单与说明为准，本仓库不统一配置全部服务密钥。

### 使用限制

- 本仓库提供插件规范与插件目录，并非可直接运行的软件；插件需在 Cursor 中安装后使用。
- 集成类插件依赖外部服务的可用性与授权，能力受各服务接口与权限范围限制。
- 输入证据中的 README 被截断，完整插件列表以仓库 README 与各插件目录为准。

### 开始使用

1. 安装 Cursor，并在插件市场浏览可用插件。
2. 参考仓库 README 的插件表格，按类别（Utilities / Developer Tools / Productivity / Integrations）选择所需插件。
3. 每个插件为独立目录并含 .cursor-plugin/plugin.json 清单；按该插件目录的说明安装与配置，集成类插件按提示完成对应服务授权。

### 收录与来源

AI 任务用途已依据官方 README 核对。Star 为 2026-11-19T04:00:25.255927Z 的快照，共 17282，达到总量 ≥1,000 条件；近一个月 Star 净增基线缺失，未用于本次判定。

近期活动：[2026-11-18 · commit](https://github.com/cursor/plugins/commit/35a90942a7f02e1ebbc2443643179815f2147954)，合并 add-hospitable-plugin 插件。

本次为文档复核，未安装或运行上游项目。上述提交证明窗口内活动，不代表运行验证。许可不作为本次准入条件。

- [Official README](https://github.com/cursor/plugins/blob/main/README.md)
- [GitHub API snapshot](https://api.github.com/repos/cursor/plugins)

## English

Cursor Plugins is the official plugin specification and plugin collection maintained by Cursor for AI coding agents. Each plugin is a standalone directory with a .cursor-plugin/plugin.json manifest, spanning developer tools, integrations, and productivity so coding agents can call external tools and services.

It helps AI coding agents complete concrete tasks in Cursor, such as code review, branch management, documentation retrieval, and operating third-party SaaS services.

### Features

- Provides the Cursor plugin specification; each plugin is a standalone directory described by a .cursor-plugin/plugin.json manifest.
- Includes first-party and third-party Cursor plugins across Utilities, Developer Tools, Productivity, and Integrations.
- Developer tools cover teaching, continual learning, team CI and review workflows, scaffolding, Ralph loops, agent compatibility scans, PR and docs canvases, the Cursor SDK, and Origin API skills.
- Integration plugins connect external services such as Gmail, Google Drive, Salesforce, GitHub, Playwright, Zoom, and X for agent queries and actions.
- The create-plugin plugin scaffolds and validates new plugins.

### Requirements

- Requires a Cursor editor or agent that supports plugins. The repository itself is a specification and a set of plugin manifests, not a standalone runnable application.
- The core specification and most developer-tool plugins need no extra model keys or shared data-service configuration.
- Third-party integration plugins need an account and authorization for the corresponding service (for example Google Workspace, Salesforce, or GitHub). Exact dependencies are defined in each plugin directory; this repository does not require a single set of all provider keys.

### Limitations

- This repository provides a plugin specification and plugin directories, not directly runnable software; plugins must be installed in Cursor to be used.
- Integration plugins depend on external service availability and authorization, and are bounded by each service's API and permission scope.
- The README in the supplied evidence is truncated; the complete plugin list is in the repository README and each plugin directory.

### Getting started

1. Install Cursor and browse available plugins in its plugin marketplace.
2. Use the plugin table in the repository README to select plugins by category (Utilities, Developer Tools, Productivity, Integrations).
3. Each plugin is a standalone directory with a .cursor-plugin/plugin.json manifest; follow that directory's instructions to install and configure it, completing service authorization for integration plugins as prompted.

### Review and sources

The documented AI task use was reviewed against the official README. The Star snapshot at 2026-11-19T04:00:25.255927Z is 17282, meeting the total-Star threshold of 1,000. The monthly Star-growth baseline is missing and was not used for this decision.

Recent activity: [2026-11-18 · commit](https://github.com/cursor/plugins/commit/35a90942a7f02e1ebbc2443643179815f2147954), merging the add-hospitable-plugin plugin.

This is a documentation review; the upstream software was not installed or run. The cited commit establishes activity within the review window, not runtime validation. Licensing is not an admission criterion.

- [Official README](https://github.com/cursor/plugins/blob/main/README.md)
- [GitHub API snapshot](https://api.github.com/repos/cursor/plugins)

## Review evidence

本次从 GitHub Trending 日榜发现项目，并依据 GitHub 官方文档复核，未安装或运行上游项目。榜单显示的今日新增 Star 仅用于挑选复核对象，不作为近一个月净增证据。

Discovered on GitHub Trending daily and reviewed against official GitHub documentation; upstream software was not installed or run. Today's stars select review candidates, not evidence of net growth over a calendar month.

- [GitHub activity](https://github.com/cursor/plugins/commit/35a90942a7f02e1ebbc2443643179815f2147954) (2026-11-18T12:24:36Z)
- [GitHub Trending daily](https://github.com/trending?since=daily)

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-19T04:00:25.255927Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "cursor-plugins",
    "name": "Cursor Plugins",
    "repository": "cursor/plugins",
    "repo_node_id": "R_kgDOQ_aGvg",
    "category": "development",
    "summary": {
      "zh-CN": "Cursor 官方插件规范与插件集合，面向 AI 编码智能体，提供开发工具、集成与效率类插件，帮助智能体完成代码审查、分支管理与第三方服务操作等任务。",
      "en": "Official Cursor plugin specification and plugin collection for AI coding agents, offering developer, integration, and productivity plugins for code review, branch management, and third-party service operations."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-19T04:00:25.255927Z",
        "en": "2026-11-19T04:00:25.255927Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "Cursor 官方插件规范与插件集合，面向 AI 编码智能体，提供开发工具、集成与效率类插件，帮助智能体完成代码审查、分支管理与第三方服务操作等任务。",
        "en": "Official Cursor plugin specification and plugin collection for AI coding agents, offering developer, integration, and productivity plugins for code review, branch management, and third-party service operations."
      },
      "source_url": "https://github.com/cursor/plugins/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/cursor/plugins/commit/35a90942a7f02e1ebbc2443643179815f2147954",
        "occurred_at": "2026-11-18T12:24:36Z",
        "reviewed_at": "2026-11-19T04:00:25.255927Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "GitHub API 记录的具体活动，证明复核窗口内有活动；不代表运行验证。",
          "en": "A specific GitHub API activity establishes activity in the review window, not runtime validation."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/cursor/plugins/blob/main/README.md"
      },
      {
        "title": "GitHub Trending daily",
        "url": "https://github.com/trending?since=daily"
      }
    ]
  },
  "snapshot": {
    "full_name": "cursor/plugins",
    "repo_node_id": "R_kgDOQ_aGvg",
    "stargazers_count": 17282,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-19T04:00:25.255927Z",
    "source_url": "https://api.github.com/repos/cursor/plugins"
  }
}
```

</details>
