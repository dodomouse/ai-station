# OpenBot application template

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[CopilotKit/OpenBot](https://github.com/CopilotKit/OpenBot)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 12624 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T04:07:37.956750+00:00 |

## 中文

用于构建 AI 助手工作区的开源应用模板。连接模型、AG-UI 智能体和 MCP 工具。运行依赖单独许可的 CopilotKit Intelligence。

### 用途与功能

- 在统一界面中管理助手对话、例行任务和技能。
- 通过 AG-UI 接入外部智能体，通过 MCP 接入工具。
- 提供工具权限、操作审批、审计和人工接管入口。

### 环境与限制

源码运行需要 Docker、Bun 1.4+、CopilotKit 账户以及模型服务配置。MIT 仅覆盖 OpenBot 应用模板。必需的 Intelligence 按个人本地、试用或生产场景采用单独条款。本地许可续期需要联网。外部模型和应用调用仍受各自服务条款约束。

### 开始使用

从 README 的 Run from source 入口配置 Intelligence 和模型，再启动 Docker 服务与前端；团队部署参阅随发行版提供的 Helm 说明。

参阅[官方 README](https://github.com/CopilotKit/OpenBot/blob/c3a5de754ea4101d3de00d3b80baa53af16923d2/README.md)。

### 收录与来源

适合需要定制助手界面、接入已有智能体并集中管理工具权限的开发者。收录范围是可修改的应用模板。

维护证据：[为中断的本地设置界面提供排障日志，并记录经过脱敏的 Intelligence 连接失败原因](https://github.com/CopilotKit/OpenBot/commit/aaef53ad9339ee7fbbb464622a39c9d3f8748af4)（2026-11-17）。

发现于 [GitHub 月榜](https://github.com/trending/typescript?since=monthly)。2026-11-17 的榜单记录新增 6,079 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

An open-source application template for AI coworker workspaces connecting models, AG-UI agents and MCP tools; operation requires separately licensed CopilotKit Intelligence.

### Uses and features

- Manage agent conversations, routines and skills in one interface.
- Connect external agents through AG-UI and tools through MCP.
- Provide tool permissions, action approvals, audit records and human takeover.

### Requirements and limits

Running from source requires Docker, Bun 1.4+, a CopilotKit account and model configuration. MIT covers the OpenBot application template only. Required Intelligence uses separate terms for personal local use, trials or production; local license renewal needs internet access. External models and connected apps retain their own service terms.

### Getting started

Follow Run from source in the README to configure Intelligence and a model, then start the Docker services and frontend. For team deployment, use the Helm documentation shipped with the release.

See the [official README](https://github.com/CopilotKit/OpenBot/blob/c3a5de754ea4101d3de00d3b80baa53af16923d2/README.md).

### Review and provenance

Useful for developers customizing an assistant interface, connecting existing agents and managing tool permissions centrally. This entry covers the modifiable application template.

Maintenance evidence: [Adds troubleshooting logs to stopped local setup and records scrubbed Intelligence connection failures](https://github.com/CopilotKit/OpenBot/commit/aaef53ad9339ee7fbbb464622a39c9d3f8748af4) (2026-11-17).

Discovered in [GitHub monthly Trending](https://github.com/trending/typescript?since=monthly), which recorded 6,079 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:07:37.956750+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "copilotkit-openbot",
    "name": "OpenBot application template",
    "repository": "CopilotKit/OpenBot",
    "repo_node_id": "R_kgDOT6ln0w",
    "category": "ai",
    "summary": {
      "zh-CN": "用于构建 AI 助手工作区的开源应用模板。连接模型、AG-UI 智能体和 MCP 工具。运行依赖单独许可的 CopilotKit Intelligence。",
      "en": "An open-source application template for AI coworker workspaces connecting models, AG-UI agents and MCP tools; operation requires separately licensed CopilotKit Intelligence."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:07:37.956750+00:00",
        "en": "2026-11-17T04:07:37.956750+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合需要定制助手界面、接入已有智能体并集中管理工具权限的开发者。收录范围是可修改的应用模板。",
      "en": "Useful for developers customizing an assistant interface, connecting existing agents and managing tool permissions centrally. This entry covers the modifiable application template.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/CopilotKit/OpenBot/blob/c3a5de754ea4101d3de00d3b80baa53af16923d2/LICENSE",
      "license_sha256": "6d35a6bb107ae508da34636387f6208e75a6938e797bc0d5bfa9489d2ca95bad",
      "source_commit": "c3a5de754ea4101d3de00d3b80baa53af16923d2",
      "reviewed_at": "2026-11-17T04:07:37.956750+00:00",
      "evidence_pinned_at": "2026-11-17T04:07:37.956750+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "MIT applies to the OpenBot application template. Required CopilotKit Intelligence is separately licensed; model providers and connected services have separate terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-17T03:01:44Z",
        "reviewed_at": "2026-11-17T04:07:37.956750+00:00",
        "url": "https://github.com/CopilotKit/OpenBot/commit/aaef53ad9339ee7fbbb464622a39c9d3f8748af4",
        "qualifies": true,
        "reason": {
          "zh-CN": "为中断的本地设置界面提供排障日志，并记录经过脱敏的 Intelligence 连接失败原因",
          "en": "Adds troubleshooting logs to stopped local setup and records scrubbed Intelligence connection failures"
        },
        "reviewed_files": [
          "desktop/src-tauri/src/local_eval.rs",
          "desktop/src/LocalIntelligence.tsx"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/CopilotKit/OpenBot",
        "accessed_at": "2026-11-17T04:07:37.956750+00:00"
      },
      {
        "url": "https://github.com/CopilotKit/OpenBot/blob/c3a5de754ea4101d3de00d3b80baa53af16923d2/README.md",
        "accessed_at": "2026-11-17T04:07:37.956750+00:00"
      },
      {
        "url": "https://github.com/CopilotKit/OpenBot/blob/c3a5de754ea4101d3de00d3b80baa53af16923d2/LICENSE",
        "accessed_at": "2026-11-17T04:07:37.956750+00:00"
      },
      {
        "url": "https://github.com/CopilotKit/OpenBot/commit/aaef53ad9339ee7fbbb464622a39c9d3f8748af4",
        "accessed_at": "2026-11-17T04:07:37.956750+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 6079,
      "source_url": "https://github.com/trending/typescript?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOT6ln0w",
    "full_name": "CopilotKit/OpenBot",
    "stargazers_count": 12624,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "6d35a6bb107ae508da34636387f6208e75a6938e797bc0d5bfa9489d2ca95bad",
    "last_success_at": "2026-11-17T03:51:44.124115+00:00"
  }
}
```

</details>
