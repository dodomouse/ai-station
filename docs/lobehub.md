# LobeHub

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[lobehub/lobehub](https://github.com/lobehub/lobehub)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 85696 |
| 评估时间 / Evaluated at | 2026-11-17T14:28:37.557815Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:25.929Z |

## 中文

支持模型对话、智能体协作和工具集成的 AI 工作台，可自行部署。

为 AI 任务组织智能体、资料和工具，并通过协作及消息入口处理工作。

### 主要功能

- 连接不同模型，并为智能体配置角色和工具。
- 通过 MCP、Skills 和市场扩展智能体能力。
- 支持多智能体协作及团队使用场景。

### 环境要求

- 推荐部署使用 Docker Compose；支持 Linux、macOS，以及 Windows WSL 2。
- 完整部署包括 PostgreSQL、Redis、RustFS、SearXNG 和智能体网关。

### 使用限制

- 自行部署需要维护数据库、存储和其他服务。
- 模型、消息平台和工具连接仍需分别配置。

### 开始使用

1. 按 README 的 Self Hosting 部分准备 Docker Compose 环境。
2. 运行官方安装流程，完成配置后执行 `docker compose up -d`。
3. 打开 `http://localhost:3210`，连接模型并创建一个带所需工具的智能体。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:25.929Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/lobehub/lobehub/commit/88a905b8cf671ee4097db80bc988e153ad545448)。调整设置中的套餐页宽度，让四张套餐卡完整排列。

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://raw.githubusercontent.com/lobehub/lobehub/canary/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/lobehub/lobehub)

## English

An AI workspace for model conversations, agent collaboration, and tool integrations, with a self-hosting option.

It organizes agents, materials, and tools for AI tasks, with collaboration and messaging interfaces.

### Features

- Connect different models and configure agent roles and tools.
- Extend agent capabilities through MCP, Skills, and the marketplace.
- Support collaboration between agents and team usage.

### Requirements

- The recommended deployment uses Docker Compose on Linux, macOS, or Windows through WSL 2.
- The full deployment includes PostgreSQL, Redis, RustFS, SearXNG, and an agent gateway.

### Limitations

- Self-hosting requires maintaining the database, storage, and supporting services.
- Model, messaging-platform, and tool connections require separate configuration.

### Getting started

1. Prepare Docker Compose using the README's Self Hosting section.
2. Follow the official setup flow, complete its configuration, and run `docker compose up -d`.
3. Open `http://localhost:3210`, connect a model, and create an agent with the required tools.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:25.929Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/lobehub/lobehub/commit/88a905b8cf671ee4097db80bc988e153ad545448).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://raw.githubusercontent.com/lobehub/lobehub/canary/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/lobehub/lobehub)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:28:37.557815Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "lobehub",
    "name": "LobeHub",
    "repository": "lobehub/lobehub",
    "repo_node_id": "R_kgDOJlox8w",
    "category": "ai",
    "summary": {
      "zh-CN": "支持模型对话、智能体协作和工具集成的 AI 工作台，可自行部署。",
      "en": "An AI workspace for model conversations, agent collaboration, and tool integrations, with a self-hosting option."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:28:37.557815Z",
        "en": "2026-11-17T14:28:37.557815Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "为 AI 任务组织智能体、资料和工具，并通过协作及消息入口处理工作。",
        "en": "It organizes agents, materials, and tools for AI tasks, with collaboration and messaging interfaces."
      },
      "source_url": "https://raw.githubusercontent.com/lobehub/lobehub/canary/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/lobehub/lobehub/commit/88a905b8cf671ee4097db80bc988e153ad545448",
        "occurred_at": "2026-11-17T13:39:15Z",
        "reviewed_at": "2026-11-17T14:28:37.557815Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "调整设置中的套餐页宽度，让四张套餐卡完整排列。 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://raw.githubusercontent.com/lobehub/lobehub/canary/README.md"
      },
      {
        "title": "GitHub 仓库元数据 / Repository metadata",
        "url": "https://api.github.com/repos/lobehub/lobehub"
      }
    ]
  },
  "snapshot": {
    "full_name": "lobehub/lobehub",
    "repo_node_id": "R_kgDOJlox8w",
    "stargazers_count": 85696,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:25.929Z",
    "source_url": "https://api.github.com/repos/lobehub/lobehub"
  }
}
```

</details>
