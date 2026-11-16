# MarkText

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[marktext/marktext](https://github.com/marktext/marktext)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 64049 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:20:19.637Z |

## 中文

支持实时预览与文件管理的跨平台 Markdown 编辑器。

### 主要功能

- 编辑常见 Markdown 内容、代码块、表格与数学公式。
- 提供主题、搜索和项目文件侧栏。

### 环境与限制

- 当前安装包要求 macOS 13+ 或 Windows 10/11，也提供 Linux 版本。
- 需按机器架构选择安装包，开发分支的新功能可能尚未进入稳定发行。

### 开始使用

从[官方说明](https://github.com/marktext/marktext/blob/develop/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/marktext/marktext/releases)可用于确认版本。

### 收录复核

支持实时预览与文件管理的跨平台 Markdown 编辑器。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。

有效维护证据：[d083522c02](https://github.com/marktext/marktext/commit/d083522c023026973d3322cf37c7cda07c4985b6)，2026-11-13T02:17:33Z。复用侧栏自然排序比较器，减少重复构造开销。

发现线索：[公开索引](https://www.noking.tech/github-radar/)记录的[微信文章](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536039&idx=1&sn=b83b2fd3d42adb14e89649ee7ac0c16a)，索引日期 2026-08-18。仅核对公开索引，未直接读取该篇微信全文；功能与限制以上游资料为依据。

本次为文档与实现证据复核，未安装或运行上游项目。

## English

A cross-platform Markdown editor with live preview and file management.

### Features

- Edits common Markdown content, code blocks, tables and math.
- Provides themes, search and a project file sidebar.

### Requirements and limits

- Current installers require macOS 13+ or Windows 10/11, with Linux builds also available.
- Choose the matching architecture
- development-branch features may not yet be in a stable release.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/marktext/marktext/blob/develop/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/marktext/marktext/releases) for versions.

### Review and provenance

A cross-platform Markdown editor with live preview and file management. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.

Activity: [d083522c02](https://github.com/marktext/marktext/commit/d083522c023026973d3322cf37c7cda07c4985b6), 2026-11-13T02:17:33Z. Reuses the sidebar natural-sort collator to avoid repeated construction.

Discovery: [an indexed WeChat article](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536039&idx=1&sn=b83b2fd3d42adb14e89649ee7ac0c16a). This is a secondary discovery record; the WeChat article body was not read. Features and limits come from upstream documentation.

This review covers documentation and implementation evidence. The upstream project was not installed or run.

## Review evidence

```json
{
  "evaluated_at": "2026-11-16T14:58:29.135174Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "marktext",
    "name": "MarkText",
    "repository": "marktext/marktext",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkxMTA0NDY4NDQ=",
    "category": "productivity",
    "summary": {
      "zh-CN": "支持实时预览与文件管理的跨平台 Markdown 编辑器。",
      "en": "A cross-platform Markdown editor with live preview and file management."
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
      "zh-CN": "支持实时预览与文件管理的跨平台 Markdown 编辑器。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。",
      "en": "A cross-platform Markdown editor with live preview and file management. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "dcba6003d1e8ad62de2e166a2c80ec1ad08cef24f941543ccf8690da7cb89d04",
      "source_url": "https://github.com/marktext/marktext/blob/develop/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "Root license reviewed. External dependencies and assets retain their individual licenses."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-13T02:17:33Z",
        "reviewed_at": "2026-11-16T14:58:29.135174Z",
        "url": "https://github.com/marktext/marktext/commit/d083522c023026973d3322cf37c7cda07c4985b6",
        "qualifies": true,
        "reason": {
          "zh-CN": "复用侧栏自然排序比较器，减少重复构造开销。",
          "en": "Reuses the sidebar natural-sort collator to avoid repeated construction."
        },
        "reviewed_files": [
          "packages/desktop/src/renderer/src/store/treeCtrl.ts"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/marktext/marktext",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/marktext/marktext/blob/develop/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/marktext/marktext/blob/develop/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/marktext/marktext/commit/d083522c023026973d3322cf37c7cda07c4985b6",
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
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkxMTA0NDY4NDQ=",
    "full_name": "marktext/marktext",
    "stargazers_count": 64049,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "dcba6003d1e8ad62de2e166a2c80ec1ad08cef24f941543ccf8690da7cb89d04",
    "last_success_at": "2026-11-16T14:20:19.637Z"
  }
}
```
