# Flutter

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[flutter/flutter](https://github.com/flutter/flutter)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 181237 |
| 许可证 / License | BSD-3-Clause |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:19:06.021Z |

## 中文

使用 Dart 为移动端、网页和桌面端构建应用的 UI 工具包。

### 主要功能

- 提供组件、布局、渲染、调试和测试工具。
- 支持 Android、iOS、Web、Windows、macOS 与 Linux 目标。

### 环境与限制

- 需要 Flutter SDK，并按目标平台安装对应工具链。
- 插件与平台接口的支持程度不同，开发分支不等于稳定发行。

### 开始使用

从[官方说明](https://github.com/flutter/flutter/blob/master/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/flutter/flutter/releases)可用于确认版本。

### 收录复核

使用 Dart 为移动端、网页和桌面端构建应用的 UI 工具包。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。

有效维护证据：[c2df24dfec](https://github.com/flutter/flutter/commit/c2df24dfeca53c6f710a3d896665c2f051d02270)，2026-11-16T09:14:28Z。调整 macOS 测试中的动态库安装名处理，保留无法扩展头部的安装名。

文章来源：[逛逛GitHub署名文章](https://www.woshipm.com/ai/6487701.html)，平台日期 2026-11-02。已通过公开正文核对仓库链接与作者归属；微信正文未直接读取。

本次为文档与实现证据复核，未安装或运行上游项目。

## English

A Dart UI toolkit for building mobile, web and desktop applications.

### Features

- Provides widgets, layout, rendering, debugging and testing tools.
- Targets Android, iOS, web, Windows, macOS and Linux.

### Requirements and limits

- Requires the Flutter SDK and the toolchain for each target platform.
- Plugin and platform API support varies
- development-branch changes are not necessarily in a stable release.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/flutter/flutter/blob/master/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/flutter/flutter/releases) for versions.

### Review and provenance

A Dart UI toolkit for building mobile, web and desktop applications. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.

Activity: [c2df24dfec](https://github.com/flutter/flutter/commit/c2df24dfeca53c6f710a3d896665c2f051d02270), 2026-11-16T09:14:28Z. Adjusts macOS test handling of dylib install names when the header cannot grow.

Discovery: [an author-attributed 逛逛GitHub article](https://www.woshipm.com/ai/6487701.html), dated 2026-11-02 on the public platform. Repository links and attribution were checked in its public body; the WeChat body was not read directly.

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
    "id": "flutter",
    "name": "Flutter",
    "repository": "flutter/flutter",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkzMTc5MjgyNA==",
    "category": "development",
    "summary": {
      "zh-CN": "使用 Dart 为移动端、网页和桌面端构建应用的 UI 工具包。",
      "en": "A Dart UI toolkit for building mobile, web and desktop applications."
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
      "zh-CN": "使用 Dart 为移动端、网页和桌面端构建应用的 UI 工具包。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。",
      "en": "A Dart UI toolkit for building mobile, web and desktop applications. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "BSD-3-Clause",
      "osi_approved": true,
      "license_sha256": "a598db94b6290ffbe10b5ecf911057b6a943351c727fdda9e5f2891d68700a20",
      "source_url": "https://github.com/flutter/flutter/blob/d8bd864cdbca3d0d2cafdb1e6165198858ea3b2b/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "Root license reviewed. External dependencies and assets retain their individual licenses.",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "d8bd864cdbca3d0d2cafdb1e6165198858ea3b2b"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-16T09:14:28Z",
        "reviewed_at": "2026-11-16T14:58:29.135174Z",
        "url": "https://github.com/flutter/flutter/commit/c2df24dfeca53c6f710a3d896665c2f051d02270",
        "qualifies": true,
        "reason": {
          "zh-CN": "调整 macOS 测试中的动态库安装名处理，保留无法扩展头部的安装名。",
          "en": "Adjusts macOS test handling of dylib install names when the header cannot grow."
        },
        "reviewed_files": [
          "packages/flutter_tools/lib/src/isolated/native_assets/macos/native_assets.dart",
          "packages/flutter_tools/lib/src/isolated/native_assets/macos/native_assets_host.dart",
          "packages/flutter_tools/lib/src/isolated/native_assets/native_assets.dart"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/flutter/flutter",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/flutter/flutter/blob/master/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/flutter/flutter/blob/d8bd864cdbca3d0d2cafdb1e6165198858ea3b2b/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/flutter/flutter/commit/c2df24dfeca53c6f710a3d896665c2f051d02270",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://www.woshipm.com/ai/6487701.html",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      }
    ],
    "article_source": {
      "article_id": "2247538256_1",
      "title": "盘点 10 月份 19 个 Star 蹭蹭涨的 GitHub 项目，第一个很有用。",
      "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538256&idx=1&sn=3b97e48392e47b295968f5c66a4ce5f0",
      "published_date": "2026-11-02",
      "account": "逛逛GitHub",
      "content_review_url": "https://www.woshipm.com/ai/6487701.html",
      "content_review_kind": "author-attributed public article",
      "wechat_direct_body_read": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkzMTc5MjgyNA==",
    "full_name": "flutter/flutter",
    "stargazers_count": 181237,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "BSD-3-Clause",
    "license_sha256": "a598db94b6290ffbe10b5ecf911057b6a943351c727fdda9e5f2891d68700a20",
    "last_success_at": "2026-11-16T14:19:06.021Z"
  }
}
```

</details>
