# Yank Note

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[purocean/yn](https://github.com/purocean/yn)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 6784 |
| 许可证 / License | AGPL-3.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:20:19.265Z |

## 中文

以本地 Markdown 文件保存笔记的可扩展编辑器。

### 主要功能

- 提供 Monaco 编辑、图表、嵌入内容和版本管理。
- 支持插件、可运行代码块及可选 AI 辅助。

### 环境与限制

- 提供 Windows、macOS 和 Linux 安装包。
- 执行代码、宏或插件会影响本机环境，应只运行可信内容，AI 服务另行配置。

### 开始使用

从[官方说明](https://github.com/purocean/yn/blob/develop/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/purocean/yn/releases)可用于确认版本。

### 收录复核

以本地 Markdown 文件保存笔记的可扩展编辑器。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。

有效维护证据：[v3.93.1](https://github.com/purocean/yn/releases/tag/v3.93.1)，2026-10-17T04:43:07Z。HTML 导出改用当前 KaTeX 渲染器版本的样式，避免硬编码旧版 CSS 造成公式显示不一致。 2026-11-17 已读取[实现提交](https://github.com/purocean/yn/commit/00f9607f38b8613db38f09b98ce16896b51d17fe)的差异；未运行上游测试。

发现线索：[公开索引](https://www.noking.tech/github-radar/)记录的[微信文章](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536039&idx=1&sn=b83b2fd3d42adb14e89649ee7ac0c16a)，索引日期 2026-08-18。仅核对公开索引，未直接读取该篇微信全文；功能与限制以上游资料为依据。

本次为文档与实现证据复核，未安装或运行上游项目。

## English

An extensible editor that stores notes as local Markdown files.

### Features

- Provides Monaco editing, diagrams, embedded content and version control.
- Supports plugins, executable code blocks and optional AI assistance.

### Requirements and limits

- Provides Windows, macOS and Linux packages.
- Code blocks, macros and plugins can affect the local machine, so run trusted content only
- AI providers require separate setup.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/purocean/yn/blob/develop/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/purocean/yn/releases) for versions.

### Review and provenance

An extensible editor that stores notes as local Markdown files. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.

Activity: [v3.93.1](https://github.com/purocean/yn/releases/tag/v3.93.1), 2026-10-17T04:43:07Z. Uses styles matching the active KaTeX renderer in HTML exports instead of hard-coded older CSS. On 2026-11-17, the [implementation diff](https://github.com/purocean/yn/commit/00f9607f38b8613db38f09b98ce16896b51d17fe) was inspected; upstream tests were not run.

Discovery: [an indexed WeChat article](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536039&idx=1&sn=b83b2fd3d42adb14e89649ee7ac0c16a). This is a secondary discovery record; the WeChat article body was not read. Features and limits come from upstream documentation.

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
    "id": "yank-note",
    "name": "Yank Note",
    "repository": "purocean/yn",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkxMTkzMzYyOTM=",
    "category": "productivity",
    "summary": {
      "zh-CN": "以本地 Markdown 文件保存笔记的可扩展编辑器。",
      "en": "An extensible editor that stores notes as local Markdown files."
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
      "zh-CN": "以本地 Markdown 文件保存笔记的可扩展编辑器。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。",
      "en": "An extensible editor that stores notes as local Markdown files. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "AGPL-3.0",
      "osi_approved": true,
      "license_sha256": "8486a10c4393cee1c25392769ddd3b2d6c242d6ec7928e1414efff7dfb2f07ef",
      "source_url": "https://github.com/purocean/yn/blob/5822804b83c9492cca2992203e72d74a0b460c8f/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "Root license reviewed. External dependencies and assets retain their individual licenses.",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "5822804b83c9492cca2992203e72d74a0b460c8f"
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-10-17T04:43:07Z",
        "reviewed_at": "2026-11-17T03:15:51.892548+00:00",
        "url": "https://github.com/purocean/yn/releases/tag/v3.93.1",
        "qualifies": true,
        "reason": {
          "zh-CN": "HTML 导出改用当前 KaTeX 渲染器版本的样式，避免硬编码旧版 CSS 造成公式显示不一致。",
          "en": "Uses styles matching the active KaTeX renderer in HTML exports instead of hard-coded older CSS."
        },
        "draft": false,
        "prerelease": false,
        "implementation_evidence": {
          "type": "commit",
          "url": "https://github.com/purocean/yn/commit/00f9607f38b8613db38f09b98ce16896b51d17fe",
          "sha": "00f9607f38b8613db38f09b98ce16896b51d17fe",
          "occurred_at": "2026-10-17T03:53:50Z",
          "reviewed_at": "2026-11-17T03:15:51.892548+00:00",
          "reviewed_files": [
            "src/renderer/services/export.ts"
          ],
          "verification_level": "source_review",
          "upstream_tests_run": false
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/purocean/yn",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/purocean/yn/blob/develop/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/purocean/yn/blob/5822804b83c9492cca2992203e72d74a0b460c8f/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/purocean/yn/releases/tag/v3.93.1",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536039&idx=1&sn=b83b2fd3d42adb14e89649ee7ac0c16a",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      }
    ],
    "article_source": {
      "article_id": "2247536039_1",
      "title": "AI 时代 Markdown 又火了，7 款 GitHub 高赞开源编辑器。",
      "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536039&idx=1&sn=b83b2fd3d42adb14e89649ee7ac0c16a",
      "published_date": "2026-08-18",
      "account": "逛逛GitHub",
      "content_review_url": null,
      "content_review_kind": "secondary article index only",
      "wechat_direct_body_read": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkxMTkzMzYyOTM=",
    "full_name": "purocean/yn",
    "stargazers_count": 6784,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "AGPL-3.0",
    "license_sha256": "8486a10c4393cee1c25392769ddd3b2d6c242d6ec7928e1414efff7dfb2f07ef",
    "last_success_at": "2026-11-16T14:20:19.265Z"
  }
}
```

</details>
