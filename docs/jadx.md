# JADX

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[skylot/jadx](https://github.com/skylot/jadx)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 51846 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:19:21.931Z |

## 中文

把 Android DEX、APK 和 Java 字节码转换为便于阅读的 Java 源码。

### 主要功能

- 提供命令行与图形界面，支持搜索、跳转、资源解码和插件。
- 包含去混淆及 smali 调试入口。

### 环境与限制

- 通常需要 64 位 Java 11+，附带 JRE 的包除外。
- 反编译可能失败或丢失原始语义，只能作为分析辅助。

### 开始使用

从[官方说明](https://github.com/skylot/jadx/blob/master/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/skylot/jadx/releases)可用于确认版本。

### 收录复核

把 Android DEX、APK 和 Java 字节码转换为便于阅读的 Java 源码。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。

有效维护证据：[469ac588eb](https://github.com/skylot/jadx/commit/469ac588eb89c707c432b5204644883a4b3ee842)，2026-11-13T23:07:08Z。为插件增加依赖关系和共享父级类加载器支持。

文章来源：[逛逛GitHub署名文章](https://www.woshipm.com/ai/6480438.html)，平台日期 2026-10-19。已通过公开正文核对仓库链接与作者归属；微信正文未直接读取。

本次为文档与实现证据复核，未安装或运行上游项目。

## English

A decompiler that turns Android DEX, APK and Java bytecode into readable Java source.

### Features

- Provides CLI and GUI interfaces with search, navigation, resource decoding and plugins.
- Includes deobfuscation and smali-debugging entry points.

### Requirements and limits

- Usually requires 64-bit Java 11+, except bundles that include a JRE.
- Decompilation can fail or lose original semantics and should be treated as an analysis aid.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/skylot/jadx/blob/master/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/skylot/jadx/releases) for versions.

### Review and provenance

A decompiler that turns Android DEX, APK and Java bytecode into readable Java source. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.

Activity: [469ac588eb](https://github.com/skylot/jadx/commit/469ac588eb89c707c432b5204644883a4b3ee842), 2026-11-13T23:07:08Z. Adds plugin dependencies and shared parent classloaders.

Discovery: [an author-attributed 逛逛GitHub article](https://www.woshipm.com/ai/6480438.html), dated 2026-10-19 on the public platform. Repository links and attribution were checked in its public body; the WeChat body was not read directly.

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
    "id": "jadx",
    "name": "JADX",
    "repository": "skylot/jadx",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnk4ODU5NDc0",
    "category": "development",
    "summary": {
      "zh-CN": "把 Android DEX、APK 和 Java 字节码转换为便于阅读的 Java 源码。",
      "en": "A decompiler that turns Android DEX, APK and Java bytecode into readable Java source."
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
      "zh-CN": "把 Android DEX、APK 和 Java 字节码转换为便于阅读的 Java 源码。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。",
      "en": "A decompiler that turns Android DEX, APK and Java bytecode into readable Java source. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "b40930bbcf80744c86c46a12bc9da056641d722716c378f5659b9e555ef833e1",
      "source_url": "https://github.com/skylot/jadx/blob/master/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "Root license reviewed. External dependencies and assets retain their individual licenses."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-13T23:07:08Z",
        "reviewed_at": "2026-11-16T14:58:29.135174Z",
        "url": "https://github.com/skylot/jadx/commit/469ac588eb89c707c432b5204644883a4b3ee842",
        "qualifies": true,
        "reason": {
          "zh-CN": "为插件增加依赖关系和共享父级类加载器支持。",
          "en": "Adds plugin dependencies and shared parent classloaders."
        },
        "reviewed_files": [
          "jadx-cli/src/main/java/jadx/cli/commands/CommandPlugins.java",
          "jadx-cli/src/test/java/jadx/cli/CliPluginDependenciesTest.java",
          "jadx-core/src/main/java/jadx/api/plugins/JadxPluginInfo.java"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/skylot/jadx",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/skylot/jadx/blob/master/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/skylot/jadx/blob/master/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/skylot/jadx/commit/469ac588eb89c707c432b5204644883a4b3ee842",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://www.woshipm.com/ai/6480438.html",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      }
    ],
    "article_source": {
      "article_id": "2247537852_1",
      "title": "火了两周的 30 万 Star 逆向 GitHub 开源神器，网友都用它来干啥？",
      "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537852&idx=1&sn=641d50231c757ac9c628f8657e3024c5",
      "published_date": "2026-10-18",
      "account": "逛逛GitHub",
      "content_review_url": "https://www.woshipm.com/ai/6480438.html",
      "content_review_kind": "author-attributed public article",
      "wechat_direct_body_read": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "MDEwOlJlcG9zaXRvcnk4ODU5NDc0",
    "full_name": "skylot/jadx",
    "stargazers_count": 51846,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "b40930bbcf80744c86c46a12bc9da056641d722716c378f5659b9e555ef833e1",
    "last_success_at": "2026-11-16T14:19:21.931Z"
  }
}
```
