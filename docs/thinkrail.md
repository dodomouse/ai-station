# ThinkRail

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[JetBrains/thinkrail](https://github.com/JetBrains/thinkrail)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 8310 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-17T04:07:37.954529+00:00 |

## 中文

围绕 pi 编码智能体提供工作区、编辑器、变更审查和项目规格管理。

### 用途与功能

- 组织多个工作区与智能体会话，并显示代码差异。
- 维护相互关联的 SPEC.md 规格和可复用技能。
- 提供桌面及浏览器界面，并接入 MCP 和模型服务。

### 环境与限制

需要 Git 和模型服务访问权限；独立工作区使用 git worktree 和分支。桌面安装有平台依赖，例如 macOS 14+，Linux 需要相应 GTK、WebKitGTK 和 glibc。模型账号及服务条款独立适用。

### 开始使用

安装对应平台的桌面包或 CLI，连接模型并打开现有项目。从一个小任务检查对话、规格和差异视图。

参阅[官方 README](https://github.com/JetBrains/thinkrail/blob/10319b4ad8fc5f75dafd730d84b4a8a9e83f9959/README.md)。

### 收录与来源

适合需要同时查看智能体过程、项目意图和代码变更的开发者。

维护证据：[修复提问卡片的焦点可见性，并在用户选择方案后关闭对比浮层。](https://github.com/JetBrains/thinkrail/commit/10319b4ad8fc5f75dafd730d84b4a8a9e83f9959)（2026-11-17）。

发现于 [GitHub 月榜](https://github.com/trending/typescript?since=monthly)。2026-11-17 的榜单记录新增 7,833 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Builds workspace, editor, change-review and project-specification tools around the pi coding agent.

### Uses and features

- Organizes workspaces and agent sessions with code-diff views.
- Maintains linked SPEC.md specifications and reusable skills.
- Provides desktop and browser interfaces with MCP and model-provider integration.

### Requirements and limits

Requires Git and model-provider access; isolated workspaces use git worktrees and branches. Desktop installation has platform dependencies such as macOS 14+ or the documented GTK, WebKitGTK and glibc libraries on Linux. Model accounts and service terms apply separately.

### Getting started

Install the desktop package or CLI, connect a model and open an existing project, then inspect chat, specifications and diffs with a small task.

See the [official README](https://github.com/JetBrains/thinkrail/blob/10319b4ad8fc5f75dafd730d84b4a8a9e83f9959/README.md).

### Review and provenance

Useful for developers who want to inspect agent work, project intent and code changes together.

Maintenance evidence: [Keeps question-card focus visible and closes the comparison overlay after an option is chosen.](https://github.com/JetBrains/thinkrail/commit/10319b4ad8fc5f75dafd730d84b4a8a9e83f9959) (2026-11-17).

Discovered in [GitHub monthly Trending](https://github.com/trending/typescript?since=monthly), which recorded 7,833 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:07:37.954529+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "thinkrail",
    "name": "ThinkRail",
    "repository": "JetBrains/thinkrail",
    "repo_node_id": "R_kgDOTRU_yQ",
    "category": "development",
    "summary": {
      "zh-CN": "围绕 pi 编码智能体提供工作区、编辑器、变更审查和项目规格管理。",
      "en": "Builds workspace, editor, change-review and project-specification tools around the pi coding agent."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:07:37.954529+00:00",
        "en": "2026-11-17T04:07:37.954529+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合需要同时查看智能体过程、项目意图和代码变更的开发者。",
      "en": "Useful for developers who want to inspect agent work, project intent and code changes together.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "source_url": "https://github.com/JetBrains/thinkrail/blob/10319b4ad8fc5f75dafd730d84b4a8a9e83f9959/LICENSE",
      "license_sha256": "8634c6a81dfa39860c8a9e508b3dcd8255b242a2c080f3ce59e29afd5f300579",
      "source_commit": "10319b4ad8fc5f75dafd730d84b4a8a9e83f9959",
      "reviewed_at": "2026-11-17T04:07:37.954529+00:00",
      "evidence_pinned_at": "2026-11-17T04:07:37.954529+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "Applies to repository code and documentation; external models, services, data and assets retain their own terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-17T02:00:48Z",
        "reviewed_at": "2026-11-17T04:07:37.954529+00:00",
        "url": "https://github.com/JetBrains/thinkrail/commit/10319b4ad8fc5f75dafd730d84b4a8a9e83f9959",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复提问卡片的焦点可见性，并在用户选择方案后关闭对比浮层。",
          "en": "Keeps question-card focus visible and closes the comparison overlay after an option is chosen."
        },
        "reviewed_files": [
          "thinkrail-extensions/ask-user-question/web/focus.ts",
          "thinkrail-extensions/ask-user-question/web/CompareOverlay.tsx"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/JetBrains/thinkrail",
        "accessed_at": "2026-11-17T04:07:37.954529+00:00"
      },
      {
        "url": "https://github.com/JetBrains/thinkrail/blob/10319b4ad8fc5f75dafd730d84b4a8a9e83f9959/README.md",
        "accessed_at": "2026-11-17T04:07:37.954529+00:00"
      },
      {
        "url": "https://github.com/JetBrains/thinkrail/blob/10319b4ad8fc5f75dafd730d84b4a8a9e83f9959/LICENSE",
        "accessed_at": "2026-11-17T04:07:37.954529+00:00"
      },
      {
        "url": "https://github.com/JetBrains/thinkrail/commit/10319b4ad8fc5f75dafd730d84b4a8a9e83f9959",
        "accessed_at": "2026-11-17T04:07:37.954529+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 7833,
      "source_url": "https://github.com/trending/typescript?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOTRU_yQ",
    "full_name": "JetBrains/thinkrail",
    "stargazers_count": 8310,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "8634c6a81dfa39860c8a9e508b3dcd8255b242a2c080f3ce59e29afd5f300579",
    "last_success_at": "2026-11-17T03:56:39.255037+00:00"
  }
}
```

</details>
