# Suparagent

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[Anil-matcha/suparagent](https://github.com/Anil-matcha/suparagent)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 7087 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:58:29.135174Z |

## 中文

为多个具名智能体提供会话、工作区、记忆、例行任务与审批界面。

### 主要功能

- 支持团队协作与重复任务。
- 可连接本机 CLI 或 API 引擎，并按需使用隔离电脑。

### 环境与限制

- 源码桌面版需要 Node.js 22+、uv 和可用的模型引擎，隔离电脑另需 Docker。
- 安装包仍属实验性版本，模型订阅不包含在项目内。

### 开始使用

从[官方说明](https://github.com/Anil-matcha/suparagent/blob/main/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/Anil-matcha/suparagent/releases)可用于确认版本。

### 收录复核

为多个具名智能体提供会话、工作区、记忆、例行任务与审批界面。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。

有效维护证据：[a0ed297d45](https://github.com/Anil-matcha/suparagent/commit/a0ed297d454fa210b11c5eb84fa50b563dd74cfb)，2026-11-13T10:34:36Z。修复同毫秒内连续恢复导致撤销快照名称冲突的问题。

文章来源：[逛逛GitHub署名文章](https://www.woshipm.com/ai/6475152.html)，平台日期 2026-10-09。已通过公开正文核对仓库链接与作者归属；微信正文未直接读取。

本次为文档与实现证据复核，未安装或运行上游项目。

## English

A workspace for named agents with conversations, workspaces, memory, routines and approval controls.

### Features

- Supports team coordination and recurring tasks.
- Connects local CLI or API engines and optional isolated computers.

### Requirements and limits

- The source desktop app needs Node.js 22+, uv and an available model engine
- isolated computers also need Docker.
- Installers remain experimental, and model subscriptions are not included.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/Anil-matcha/suparagent/blob/main/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/Anil-matcha/suparagent/releases) for versions.

### Review and provenance

A workspace for named agents with conversations, workspaces, memory, routines and approval controls. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.

Activity: [a0ed297d45](https://github.com/Anil-matcha/suparagent/commit/a0ed297d454fa210b11c5eb84fa50b563dd74cfb), 2026-11-13T10:34:36Z. Prevents undo-snapshot name collisions during consecutive restores within one millisecond.

Discovery: [an author-attributed 逛逛GitHub article](https://www.woshipm.com/ai/6475152.html), dated 2026-10-09 on the public platform. Repository links and attribution were checked in its public body; the WeChat body was not read directly.

This review covers documentation and implementation evidence. The upstream project was not installed or run.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:58:29.135174Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "suparagent",
    "name": "Suparagent",
    "repository": "Anil-matcha/suparagent",
    "repo_node_id": "R_kgDOJne9Sg",
    "category": "ai",
    "summary": {
      "zh-CN": "为多个具名智能体提供会话、工作区、记忆、例行任务与审批界面。",
      "en": "A workspace for named agents with conversations, workspaces, memory, routines and approval controls."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:58:29.135174Z",
        "en": "2026-11-16T14:58:29.135174Z"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "为多个具名智能体提供会话、工作区、记忆、例行任务与审批界面。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。",
      "en": "A workspace for named agents with conversations, workspaces, memory, routines and approval controls. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "c95bae1d1ce0235ecccd3560b772ec1efb97f348a79f0fbe0a634f0c2ccefe2c",
      "source_url": "https://github.com/Anil-matcha/suparagent/blob/5fd98bba9a022a0edb9105b8310752dbb383171f/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "Root license reviewed. External dependencies and assets retain their individual licenses.",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "5fd98bba9a022a0edb9105b8310752dbb383171f"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-13T10:34:36Z",
        "reviewed_at": "2026-11-16T14:58:29.135174Z",
        "url": "https://github.com/Anil-matcha/suparagent/commit/a0ed297d454fa210b11c5eb84fa50b563dd74cfb",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复同毫秒内连续恢复导致撤销快照名称冲突的问题。",
          "en": "Prevents undo-snapshot name collisions during consecutive restores within one millisecond."
        },
        "reviewed_files": [
          "backend/app/services/workspace_snapshots.py",
          "backend/tests/test_workspace_snapshots.py"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/Anil-matcha/suparagent",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/Anil-matcha/suparagent/blob/main/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/Anil-matcha/suparagent/blob/5fd98bba9a022a0edb9105b8310752dbb383171f/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/Anil-matcha/suparagent/commit/a0ed297d454fa210b11c5eb84fa50b563dd74cfb",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://www.woshipm.com/ai/6475152.html",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      }
    ],
    "article_source": {
      "article_id": "2247537624_1",
      "title": "3 个最近爆火的 Personal Agent ，在 GitHub 上有开源平替了。",
      "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537624&idx=1&sn=10eccfc7b58a97b27b2144654b7ddd35",
      "published_date": "2026-10-08",
      "account": "逛逛GitHub",
      "content_review_url": "https://www.woshipm.com/ai/6475152.html",
      "content_review_kind": "author-attributed public article",
      "wechat_direct_body_read": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOJne9Sg",
    "full_name": "Anil-matcha/suparagent",
    "stargazers_count": 7087,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "c95bae1d1ce0235ecccd3560b772ec1efb97f348a79f0fbe0a634f0c2ccefe2c",
    "last_success_at": "2026-11-16T14:58:29.135174Z"
  }
}
```

</details>
