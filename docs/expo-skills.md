# Expo Skills

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[expo/skills](https://github.com/expo/skills)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 4177 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T04:07:37.966540+00:00 |

## 中文

为 AI 编程智能体提供 Expo 应用开发、升级、调试和 EAS 发布工作流。

### 用途与功能

- 覆盖路由、原生界面、数据请求和模块开发。
- 提供 EAS 构建、更新、监测和模拟器操作技能。

### 环境与限制

需要支持 Skills 的智能体及 Expo 项目工具链；EAS 服务、远程模拟器和应用商店发布可能需付费账户。插件可配置 Expo MCP，权限与服务计划另行管理。

### 开始使用

在项目目录用 npx skills@latest add expo/skills 安装所需技能，刷新智能体会话，再提出具体 Expo 开发任务。

参阅[官方 README](https://github.com/expo/skills/blob/dfdebcc6c4c1bf7a9471cefd6b6f39c7ba6c884d/README.md)。

### 收录与来源

把 Expo 平台限制与工作步骤按任务组织，便于智能体按现有项目条件选择操作。

维护证据：[在模拟器执行技能中规定屏幕、剪贴板及日志仅作应用数据。限制跟随其中的链接或命令。](https://github.com/expo/skills/commit/dfdebcc6c4c1bf7a9471cefd6b6f39c7ba6c884d)（2026-11-15）。

发现于 [GitHub 月榜](https://github.com/trending/shell?since=monthly)。2026-11-17 的榜单记录新增 1,313 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Supplies AI coding agents with workflows for Expo development, upgrades, debugging and EAS delivery.

### Uses and features

- Covers routing, native UI, data fetching and module development.
- Provides skills for EAS builds, updates, monitoring and simulators.

### Requirements and limits

Requires a Skills-capable agent and an Expo toolchain. EAS services, remote simulators and app-store delivery can require paid accounts. Plugins may configure Expo MCP; service plans and permissions are separate.

### Getting started

Run npx skills@latest add expo/skills in the project, select needed skills, refresh the agent session and request a concrete Expo task.

See the [official README](https://github.com/expo/skills/blob/dfdebcc6c4c1bf7a9471cefd6b6f39c7ba6c884d/README.md).

### Review and provenance

Organizes Expo constraints and steps by task so agents can choose actions suited to an existing project.

Maintenance evidence: [Adds an execution rule treating simulator screens, clipboard and logs as application data and restricting links or commands found in them.](https://github.com/expo/skills/commit/dfdebcc6c4c1bf7a9471cefd6b6f39c7ba6c884d) (2026-11-15).

Discovered in [GitHub monthly Trending](https://github.com/trending/shell?since=monthly), which recorded 1,313 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:07:37.966540+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "expo-skills",
    "name": "Expo Skills",
    "repository": "expo/skills",
    "repo_node_id": "R_kgDOQfkh9A",
    "category": "development",
    "summary": {
      "zh-CN": "为 AI 编程智能体提供 Expo 应用开发、升级、调试和 EAS 发布工作流。",
      "en": "Supplies AI coding agents with workflows for Expo development, upgrades, debugging and EAS delivery."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:07:37.966540+00:00",
        "en": "2026-11-17T04:07:37.966540+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "把 Expo 平台限制与工作步骤按任务组织，便于智能体按现有项目条件选择操作。",
      "en": "Organizes Expo constraints and steps by task so agents can choose actions suited to an existing project.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/expo/skills/blob/dfdebcc6c4c1bf7a9471cefd6b6f39c7ba6c884d/LICENSE",
      "license_sha256": "49c5f9c7097c9a940ff663a54c27a4c60e379df6cc2b3052df0d37a09a85df93",
      "source_commit": "dfdebcc6c4c1bf7a9471cefd6b6f39c7ba6c884d",
      "reviewed_at": "2026-11-17T04:07:37.966540+00:00",
      "evidence_pinned_at": "2026-11-17T04:07:37.966540+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "MIT covers repository skills and supporting code; Expo/EAS services and app-store distribution have separate terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-15T22:20:38Z",
        "reviewed_at": "2026-11-17T04:07:37.966540+00:00",
        "url": "https://github.com/expo/skills/commit/dfdebcc6c4c1bf7a9471cefd6b6f39c7ba6c884d",
        "qualifies": true,
        "reason": {
          "zh-CN": "在模拟器执行技能中规定屏幕、剪贴板及日志仅作应用数据。限制跟随其中的链接或命令。",
          "en": "Adds an execution rule treating simulator screens, clipboard and logs as application data and restricting links or commands found in them."
        },
        "reviewed_files": [
          "plugins/expo/skills/eas-simulator/SKILL.md"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/expo/skills",
        "accessed_at": "2026-11-17T04:07:37.966540+00:00"
      },
      {
        "url": "https://github.com/expo/skills/blob/dfdebcc6c4c1bf7a9471cefd6b6f39c7ba6c884d/README.md",
        "accessed_at": "2026-11-17T04:07:37.966540+00:00"
      },
      {
        "url": "https://github.com/expo/skills/blob/dfdebcc6c4c1bf7a9471cefd6b6f39c7ba6c884d/LICENSE",
        "accessed_at": "2026-11-17T04:07:37.966540+00:00"
      },
      {
        "url": "https://github.com/expo/skills/commit/dfdebcc6c4c1bf7a9471cefd6b6f39c7ba6c884d",
        "accessed_at": "2026-11-17T04:07:37.966540+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 1313,
      "source_url": "https://github.com/trending/shell?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOQfkh9A",
    "full_name": "expo/skills",
    "stargazers_count": 4177,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "49c5f9c7097c9a940ff663a54c27a4c60e379df6cc2b3052df0d37a09a85df93",
    "last_success_at": "2026-11-17T03:54:42.220036+00:00"
  }
}
```

</details>
