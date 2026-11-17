# Cordis

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[cordiverse/cordis](https://github.com/cordiverse/cordis)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 9915 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:20:19.629Z |

## 中文

用于 TypeScript 应用的组件、服务依赖和生命周期管理框架。

### 主要功能

- 按上下文组合组件并管理服务注入。
- 配套模块包括计时器、加载器与热重载。

### 环境与限制

- 需要 JavaScript/TypeScript 工程环境，并按包文档配置依赖。
- API 尚不稳定，当前正式文档仍在建设，升级应检查迁移说明。

### 开始使用

从[官方说明](https://github.com/cordiverse/cordis/blob/main/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/cordiverse/cordis/releases)可用于确认版本。

### 收录复核

用于 TypeScript 应用的组件、服务依赖和生命周期管理框架。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。

有效维护证据：[bdd4126856](https://github.com/cordiverse/cordis/commit/bdd41268564dc82012523cfb90202ccca2d54de4)，2026-11-15T15:48:52Z。修复计时器回调重入时丢失后续句柄的问题。

发现线索：[公开索引](https://www.noking.tech/github-radar/)记录的[微信文章](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536122&idx=1&sn=b7a284d06296707235d8dde07c6f6d4e)，索引日期 2026-08-23。仅核对公开索引，未直接读取该篇微信全文；功能与限制以上游资料为依据。

本次为文档与实现证据复核，未安装或运行上游项目。

## English

A TypeScript framework for components, service dependencies and lifecycle management.

### Features

- Composes components in contexts and manages service injection.
- Provides companion timer, loader and hot-reload modules.

### Requirements and limits

- Requires a JavaScript/TypeScript project environment and package-specific dependencies.
- The API is unstable and official documentation is still being built
- check migration notes before upgrading.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/cordiverse/cordis/blob/main/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/cordiverse/cordis/releases) for versions.

### Review and provenance

A TypeScript framework for components, service dependencies and lifecycle management. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.

Activity: [bdd4126856](https://github.com/cordiverse/cordis/commit/bdd41268564dc82012523cfb90202ccca2d54de4), 2026-11-15T15:48:52Z. Preserves the trailing timer handle when a callback re-enters.

Discovery: [an indexed WeChat article](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536122&idx=1&sn=b7a284d06296707235d8dde07c6f6d4e). This is a secondary discovery record; the WeChat article body was not read. Features and limits come from upstream documentation.

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
    "id": "cordis",
    "name": "Cordis",
    "repository": "cordiverse/cordis",
    "repo_node_id": "R_kgDOHWhUTA",
    "category": "development",
    "summary": {
      "zh-CN": "用于 TypeScript 应用的组件、服务依赖和生命周期管理框架。",
      "en": "A TypeScript framework for components, service dependencies and lifecycle management."
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
      "zh-CN": "用于 TypeScript 应用的组件、服务依赖和生命周期管理框架。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。",
      "en": "A TypeScript framework for components, service dependencies and lifecycle management. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "034fb52b1d57360ecbae6cb1632a88f86fd7c3d3f5631a5f082710203dda0be7",
      "source_url": "https://github.com/cordiverse/cordis/blob/c9fe179ce5ac484620a387a1697409cb007d4178/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "Root license reviewed. External dependencies and assets retain their individual licenses.",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "c9fe179ce5ac484620a387a1697409cb007d4178"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-15T15:48:52Z",
        "reviewed_at": "2026-11-16T14:58:29.135174Z",
        "url": "https://github.com/cordiverse/cordis/commit/bdd41268564dc82012523cfb90202ccca2d54de4",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复计时器回调重入时丢失后续句柄的问题。",
          "en": "Preserves the trailing timer handle when a callback re-enters."
        },
        "reviewed_files": [
          "packages/timer/src/index.ts",
          "packages/timer/tests/index.spec.ts"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/cordiverse/cordis",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/cordiverse/cordis/blob/main/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/cordiverse/cordis/blob/c9fe179ce5ac484620a387a1697409cb007d4178/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/cordiverse/cordis/commit/bdd41268564dc82012523cfb90202ccca2d54de4",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536122&idx=1&sn=b7a284d06296707235d8dde07c6f6d4e",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      }
    ],
    "article_source": {
      "article_id": "2247536122_1",
      "title": "一周没逛 GitHub 不要紧，这 TOP 10 的热门开源项目整理好了。",
      "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536122&idx=1&sn=b7a284d06296707235d8dde07c6f6d4e",
      "published_date": "2026-08-23",
      "account": "逛逛GitHub",
      "content_review_url": null,
      "content_review_kind": "secondary article index only",
      "wechat_direct_body_read": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOHWhUTA",
    "full_name": "cordiverse/cordis",
    "stargazers_count": 9915,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "034fb52b1d57360ecbae6cb1632a88f86fd7c3d3f5631a5f082710203dda0be7",
    "last_success_at": "2026-11-16T14:20:19.629Z"
  }
}
```

</details>
