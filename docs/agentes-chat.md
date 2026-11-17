# agentes.chat

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[agentes-chat/agentes-chat](https://github.com/agentes-chat/agentes-chat)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 自动化 / Automation |
| 状态 / Status | 已收录 / Included |
| Star | 1597 |
| 许可证 / License | AGPL-3.0-only |
| 评估时间 / Evaluated at | 2026-11-16T14:30:19.931551Z |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:27:09.977Z |

## 中文

### 用途与功能

让团队成员和智能体在频道与私信中协作。为智能体配置角色、模型、预算、工具和执行环境。

提供任务、定时流程、审批卡片、知识页面和 MCP 连接。适合需要保留团队协作记录的智能体工作流。

### 环境与限制

自托管需要服务端环境及 PostgreSQL，常用部署方式为 Linux 和 Docker。模型、连接器和云服务另有条件与费用。主体为 AGPL-3.0-only，NOTICE 含署名、商标及应用商店条款；部分包另有许可。

### 入门与收录判断

从[官方 README](https://github.com/agentes-chat/agentes-chat/blob/main/README.md)查阅安装和使用步骤。把团队聊天、执行记录和人工批准结合，提供可自托管的完整应用。

本轮为文档复核，未安装、运行或测试上游项目。正式 desktop-v0.8.11 包含多项修复，涉及低内存服务启动、智能体浏览器和例行任务。详见[维护记录](https://github.com/agentes-chat/agentes-chat/releases/tag/desktop-v0.8.11)。

### 文章来源

发现于“逛逛GitHub”在 2026-11-16 发布的[《8 个开源工具速览》](https://www.woshipm.com/ai/6494405.html)。已读取作者署名正文，功能和限制另按当前上游复核。

## English

### Purpose and features

Team chat where people and agents share channels and direct messages, with per-agent roles, models, budgets, tools and execution environments.

Combines tasks, routines, approval cards, knowledge pages and MCP connections for shared agent workflows.

### Requirements and limits

Self-hosting requires a server and PostgreSQL, commonly Linux with Docker. Models, connectors and cloud services have separate requirements and costs. The main license is AGPL-3.0-only; NOTICE covers attribution, trademarks and app-store permission, and some packages have separate licenses.

### Getting started and review

Use the [official README](https://github.com/agentes-chat/agentes-chat/blob/main/README.md) for installation and usage. This is a documentation review; the software was not installed or tested. Stable desktop-v0.8.11 fixes low-memory server startup, agent-browser behavior and routines. See the [activity evidence](https://github.com/agentes-chat/agentes-chat/releases/tag/desktop-v0.8.11).

The project appears in the account's [author-published article dated 2026-11-16](https://www.woshipm.com/ai/6494405.html). Current upstream documentation supports the feature descriptions.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:30:19.931551Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "agentes-chat",
    "name": "agentes.chat",
    "repository": "agentes-chat/agentes-chat",
    "repo_node_id": "R_kgDOVnleRw",
    "category": "automation",
    "summary": {
      "zh-CN": "让团队成员和智能体在频道与私信中协作。为智能体配置角色、模型、预算、工具和执行环境。",
      "en": "Team chat where people and agents share channels and direct messages, with per-agent roles, models, budgets, tools and execution environments."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:30:19.931551Z",
        "en": "2026-11-16T14:30:19.931551Z"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "basis": "把团队聊天、执行记录和人工批准结合，提供可自托管的完整应用。",
      "rationale": "把团队聊天、执行记录和人工批准结合，提供可自托管的完整应用。",
      "stars_are_advisory": true,
      "reviewed_at": "2026-11-16T14:30:19.931551Z"
    },
    "license_review": {
      "spdx": "AGPL-3.0-only",
      "osi_approved": true,
      "license_sha256": "7c107a37ec0994df50a7ecd9e4002187e99148ed6fd98ffee4f23dfc18a363e0",
      "source_url": "https://github.com/agentes-chat/agentes-chat/blob/d7b14e904131588fe733430c7fa3ace7d4e38ec7/LICENSE",
      "reviewed_at": "2026-11-16T14:30:19.931551Z",
      "scope_note": "Main code AGPL-3.0-only with section 7 terms in NOTICE; separate packages and third-party components retain their licenses.",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "d7b14e904131588fe733430c7fa3ace7d4e38ec7",
      "files": [
        {
          "path": "NOTICE",
          "source_url": "https://github.com/agentes-chat/agentes-chat/blob/d7b14e904131588fe733430c7fa3ace7d4e38ec7/NOTICE",
          "source_commit": "d7b14e904131588fe733430c7fa3ace7d4e38ec7",
          "sha256": "d03ec4408a191c9f74f54963ab66bb4f1ab0c4e56004d5694059392b911974ea",
          "fetched_at": "2026-11-17T03:15:49.908584+00:00"
        }
      ]
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-11-16T13:01:34Z",
        "reviewed_at": "2026-11-16T14:30:19.931551Z",
        "url": "https://github.com/agentes-chat/agentes-chat/releases/tag/desktop-v0.8.11",
        "qualifies": true,
        "reason": {
          "zh-CN": "正式 desktop-v0.8.11 修复低内存服务启动、智能体浏览器和例行任务等行为。",
          "en": "Stable desktop-v0.8.11 fixes low-memory server startup, agent-browser behavior and routines."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/agentes-chat/agentes-chat",
        "accessed_at": "2026-11-16T14:27:09.977Z",
        "supports": "Repository identity, Stars and public state."
      },
      {
        "url": "https://github.com/agentes-chat/agentes-chat/blob/main/README.md",
        "accessed_at": "2026-11-16T14:30:19.931551Z",
        "supports": "Capabilities, requirements and limits."
      },
      {
        "url": "https://www.woshipm.com/ai/6494405.html",
        "published_date": "2026-11-16",
        "accessed_at": "2026-11-16T14:30:19.931551Z",
        "supports": "Author-published article body and account attribution."
      },
      {
        "url": "https://github.com/agentes-chat/agentes-chat/blob/main/NOTICE",
        "accessed_at": "2026-11-16T14:30:19.931551Z",
        "supports": "License scope, attribution and additional permission."
      }
    ],
    "discovery": {
      "account": "逛逛GitHub",
      "article_url": "https://www.woshipm.com/ai/6494405.html",
      "published_date": "2026-11-16",
      "body_verification": "author_published_article"
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVnleRw",
    "full_name": "agentes-chat/agentes-chat",
    "stargazers_count": 1597,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "AGPL-3.0",
    "license_sha256": "7c107a37ec0994df50a7ecd9e4002187e99148ed6fd98ffee4f23dfc18a363e0",
    "last_success_at": "2026-11-16T14:27:09.977Z"
  }
}
```

</details>
