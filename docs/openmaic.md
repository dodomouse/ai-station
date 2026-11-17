# OpenMAIC

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[THU-MAIC/OpenMAIC](https://github.com/THU-MAIC/OpenMAIC)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 43722 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:19:44.254Z |

## 中文

把主题或文档转成包含 AI 教师与同学的交互式课堂。

### 主要功能

- 生成课件、问答、白板、语音和项目式学习活动。
- 提供课程编辑、文档解析及智能体工作台集成。

### 环境与限制

- 源码需要 Node.js 22.19+、pnpm 与 PostgreSQL，也提供 Docker 部署。
- 默认个人部署共享同一资料库，公开服务前需配置身份验证，模型服务另行配置。

### 开始使用

从[官方说明](https://github.com/THU-MAIC/OpenMAIC/blob/main/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/THU-MAIC/OpenMAIC/releases)可用于确认版本。

### 收录复核

把主题或文档转成包含 AI 教师与同学的交互式课堂。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。

有效维护证据：[ae0f3be49d](https://github.com/THU-MAIC/OpenMAIC/commit/ae0f3be49def9325aaf2111a85d487d83be13be4)，2026-11-16T06:28:28Z。新增 MiniCPM-OCR 文档解析服务与设置界面支持。

文章来源：[逛逛GitHub署名文章](https://www.woshipm.com/share/6473850.html)，平台日期 2026-10-06。已通过公开正文核对仓库链接与作者归属；微信正文未直接读取。

本次为文档与实现证据复核，未安装或运行上游项目。

## English

Turns topics or documents into interactive classrooms with AI teachers and classmates.

### Features

- Generates slides, quizzes, whiteboards, speech and project-based activities.
- Includes course editing, document parsing and agent-workbench integrations.

### Requirements and limits

- Source setup requires Node.js 22.19+, pnpm and PostgreSQL, with Docker deployment available.
- The default personal installation shares one library
- public hosting needs identity configuration, and models must be configured separately.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/THU-MAIC/OpenMAIC/blob/main/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/THU-MAIC/OpenMAIC/releases) for versions.

### Review and provenance

Turns topics or documents into interactive classrooms with AI teachers and classmates. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.

Activity: [ae0f3be49d](https://github.com/THU-MAIC/OpenMAIC/commit/ae0f3be49def9325aaf2111a85d487d83be13be4), 2026-11-16T06:28:28Z. Adds a MiniCPM-OCR document parsing provider and settings support.

Discovery: [an author-attributed 逛逛GitHub article](https://www.woshipm.com/share/6473850.html), dated 2026-10-06 on the public platform. Repository links and attribution were checked in its public body; the WeChat body was not read directly.

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
    "id": "openmaic",
    "name": "OpenMAIC",
    "repository": "THU-MAIC/OpenMAIC",
    "repo_node_id": "R_kgDORkIb9w",
    "category": "ai",
    "summary": {
      "zh-CN": "把主题或文档转成包含 AI 教师与同学的交互式课堂。",
      "en": "Turns topics or documents into interactive classrooms with AI teachers and classmates."
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
      "zh-CN": "把主题或文档转成包含 AI 教师与同学的交互式课堂。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。",
      "en": "Turns topics or documents into interactive classrooms with AI teachers and classmates. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "ba252563743227138231604c9138dd400faca5a10c3cf206b466e5466c565a19",
      "source_url": "https://github.com/THU-MAIC/OpenMAIC/blob/a17795c36bbc6475e62c313416f37401ccbf6ab4/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "Root license reviewed. External dependencies and assets retain their individual licenses.",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "a17795c36bbc6475e62c313416f37401ccbf6ab4"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-16T06:28:28Z",
        "reviewed_at": "2026-11-16T14:58:29.135174Z",
        "url": "https://github.com/THU-MAIC/OpenMAIC/commit/ae0f3be49def9325aaf2111a85d487d83be13be4",
        "qualifies": true,
        "reason": {
          "zh-CN": "新增 MiniCPM-OCR 文档解析服务与设置界面支持。",
          "en": "Adds a MiniCPM-OCR document parsing provider and settings support."
        },
        "reviewed_files": [
          ".env.example",
          "app/api/verify-pdf-provider/route.ts",
          "components/settings/pdf-settings.tsx"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/THU-MAIC/OpenMAIC",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/THU-MAIC/OpenMAIC/blob/main/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/THU-MAIC/OpenMAIC/blob/a17795c36bbc6475e62c313416f37401ccbf6ab4/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/THU-MAIC/OpenMAIC/commit/ae0f3be49def9325aaf2111a85d487d83be13be4",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://www.woshipm.com/share/6473850.html",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      }
    ],
    "article_source": {
      "article_id": "2247537550_1",
      "title": "盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。",
      "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537550&idx=1&sn=29715a80ebde4036ab57651905d6bc3f",
      "published_date": "2026-10-05",
      "account": "逛逛GitHub",
      "content_review_url": "https://www.woshipm.com/share/6473850.html",
      "content_review_kind": "author-attributed public article",
      "wechat_direct_body_read": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDORkIb9w",
    "full_name": "THU-MAIC/OpenMAIC",
    "stargazers_count": 43722,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "ba252563743227138231604c9138dd400faca5a10c3cf206b466e5466c565a19",
    "last_success_at": "2026-11-16T14:19:44.254Z"
  }
}
```

</details>
