# Rakazo

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[elie222/rakazo](https://github.com/elie222/rakazo)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 8776 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:19:44.682Z |

## 中文

可自行部署的 AI 团队工作台，集中管理长期记忆、例行任务与智能体电脑。

### 主要功能

- 提供群聊、委派、浏览器操作和应用连接。
- 可使用本机或远程沙箱，并配置自己的模型服务。

### 环境与限制

- 常规自托管需要 Docker 与 Compose，源码开发另有 Node.js 与 pnpm 版本要求。
- 模型、远程电脑和外部服务可能收费，需管理各智能体权限。

### 开始使用

从[官方说明](https://github.com/elie222/rakazo/blob/main/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/elie222/rakazo/releases)可用于确认版本。

### 收录复核

可自行部署的 AI 团队工作台，集中管理长期记忆、例行任务与智能体电脑。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。

有效维护证据：[v0.11.0](https://github.com/elie222/rakazo/releases/tag/v0.11.0)，2026-11-12T14:44:13Z。模型路由在各付费模式下优先使用用户已连接的凭据，避免错误消耗托管额度。 2026-11-17 已读取[实现提交](https://github.com/elie222/rakazo/commit/beec8f5909840397d783a3cbf1cab9cb463c8588)的差异；未运行上游测试。

文章来源：[逛逛GitHub署名文章](https://www.woshipm.com/ai/6475152.html)，平台日期 2026-10-09。已通过公开正文核对仓库链接与作者归属；微信正文未直接读取。

本次为文档与实现证据复核，未安装或运行上游项目。

## English

A self-hostable AI team workspace with persistent memory, routines and agent computers.

### Features

- Provides group chats, delegation, browser use and app integrations.
- Uses local or remote sandboxes with your own model services.

### Requirements and limits

- Typical self-hosting needs Docker and Compose
- source development has additional Node.js and pnpm version requirements.
- Models, remote computers and services may incur charges, and agent permissions need configuration.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/elie222/rakazo/blob/main/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/elie222/rakazo/releases) for versions.

### Review and provenance

A self-hostable AI team workspace with persistent memory, routines and agent computers. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.

Activity: [v0.11.0](https://github.com/elie222/rakazo/releases/tag/v0.11.0), 2026-11-12T14:44:13Z. Makes connected user credentials take precedence over hosted credits in every funding mode. On 2026-11-17, the [implementation diff](https://github.com/elie222/rakazo/commit/beec8f5909840397d783a3cbf1cab9cb463c8588) was inspected; upstream tests were not run.

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
    "id": "rakazo",
    "name": "Rakazo",
    "repository": "elie222/rakazo",
    "repo_node_id": "R_kgDOT3ChxQ",
    "category": "ai",
    "summary": {
      "zh-CN": "可自行部署的 AI 团队工作台，集中管理长期记忆、例行任务与智能体电脑。",
      "en": "A self-hostable AI team workspace with persistent memory, routines and agent computers."
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
      "zh-CN": "可自行部署的 AI 团队工作台，集中管理长期记忆、例行任务与智能体电脑。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。",
      "en": "A self-hostable AI team workspace with persistent memory, routines and agent computers. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "b9738182c46747cb7cd36cad62d55c8922ca8d0029df280d3d73bb3c95d34935",
      "source_url": "https://github.com/elie222/rakazo/blob/cbe3645b9f0f3c1026ec46bc31d6ab87c5487f92/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "Root license reviewed. External dependencies and assets retain their individual licenses.",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "cbe3645b9f0f3c1026ec46bc31d6ab87c5487f92"
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-11-12T14:44:13Z",
        "reviewed_at": "2026-11-17T03:15:51.892548+00:00",
        "url": "https://github.com/elie222/rakazo/releases/tag/v0.11.0",
        "qualifies": true,
        "reason": {
          "zh-CN": "模型路由在各付费模式下优先使用用户已连接的凭据，避免错误消耗托管额度。",
          "en": "Makes connected user credentials take precedence over hosted credits in every funding mode."
        },
        "draft": false,
        "prerelease": false,
        "implementation_evidence": {
          "type": "commit",
          "url": "https://github.com/elie222/rakazo/commit/beec8f5909840397d783a3cbf1cab9cb463c8588",
          "sha": "beec8f5909840397d783a3cbf1cab9cb463c8588",
          "occurred_at": "2026-11-12T14:20:41Z",
          "reviewed_at": "2026-11-17T03:15:51.892548+00:00",
          "reviewed_files": [
            "packages/adapters/src/model-selection.ts"
          ],
          "verification_level": "source_review",
          "upstream_tests_run": false
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/elie222/rakazo",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/elie222/rakazo/blob/main/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/elie222/rakazo/blob/cbe3645b9f0f3c1026ec46bc31d6ab87c5487f92/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/elie222/rakazo/releases/tag/v0.11.0",
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
    "repo_node_id": "R_kgDOT3ChxQ",
    "full_name": "elie222/rakazo",
    "stargazers_count": 8776,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "b9738182c46747cb7cd36cad62d55c8922ca8d0029df280d3d73bb3c95d34935",
    "last_success_at": "2026-11-16T14:19:44.682Z"
  }
}
```

</details>
