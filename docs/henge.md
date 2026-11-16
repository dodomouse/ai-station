# Henge

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[Leviidev/Henge](https://github.com/Leviidev/Henge)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 2357 |
| 许可证 / License | GPL-2.0-or-later |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:18:43.351Z |

## 中文

在 iPhone 和 iPad 上以 JIT 模拟器运行 macOS，用于系统兼容性实验。

### 主要功能

- 提供图形显示、触控输入、键鼠连接和文件交换。
- 从安装界面下载支持的 macOS 恢复镜像。

### 环境与限制

- 要求 iOS 17+、A14/M1 或更新芯片，以及可用的 JIT。
- 镜像和虚拟磁盘占用大量存储，设备兼容性仍有限。 上游仅在 iPhone 17 Pro 实机测试，iPad 尚未实机验证。
- macOS 和 boot ROM 不属于本仓代码开源授权。

### 开始使用

从[官方说明](https://github.com/Leviidev/Henge/blob/main/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/Leviidev/Henge/releases)可用于确认版本。

### 收录复核

在 iPhone 和 iPad 上以 JIT 模拟器运行 macOS，用于系统兼容性实验。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。

有效维护证据：[0.3](https://github.com/Leviidev/Henge/releases/tag/0.3)，2026-11-10T23:53:38Z。已核对正式发行 0.3 的发布状态与时间。

文章来源：[逛逛GitHub署名文章](https://www.woshipm.com/ai/6492489.html)，平台日期 2026-11-12。已通过公开正文核对仓库链接与作者归属；微信正文未直接读取。

本次为文档与实现证据复核，未安装或运行上游项目。

## English

A JIT emulator for running macOS on iPhone and iPad for compatibility experiments.

### Features

- Provides graphics, touch input, keyboard and mouse support, and file exchange.
- Downloads supported macOS restore images through its installer.

### Requirements and limits

- Requires iOS 17+, A14/M1 or newer hardware and available JIT.
- Images and virtual disks need substantial storage, and device compatibility remains limited. Upstream has tested only an iPhone 17 Pro
- iPad has not been tested on hardware. macOS and boot ROMs are excluded from the repository code license.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/Leviidev/Henge/blob/main/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/Leviidev/Henge/releases) for versions.

### Review and provenance

A JIT emulator for running macOS on iPhone and iPad for compatibility experiments. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.

Activity: [0.3](https://github.com/Leviidev/Henge/releases/tag/0.3), 2026-11-10T23:53:38Z. Checked the non-draft, non-prerelease publication 0.3 and its date.

Discovery: [an author-attributed 逛逛GitHub article](https://www.woshipm.com/ai/6492489.html), dated 2026-11-12 on the public platform. Repository links and attribution were checked in its public body; the WeChat body was not read directly.

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
    "id": "henge",
    "name": "Henge",
    "repository": "Leviidev/Henge",
    "repo_node_id": "R_kgDOVfjofA",
    "category": "development",
    "summary": {
      "zh-CN": "在 iPhone 和 iPad 上以 JIT 模拟器运行 macOS，用于系统兼容性实验。",
      "en": "A JIT emulator for running macOS on iPhone and iPad for compatibility experiments."
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
      "zh-CN": "在 iPhone 和 iPad 上以 JIT 模拟器运行 macOS，用于系统兼容性实验。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。",
      "en": "A JIT emulator for running macOS on iPhone and iPad for compatibility experiments. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "GPL-2.0-or-later",
      "osi_approved": true,
      "license_sha256": "6f04ae8364d0079a192b14635f4b1da294ce18724c034c39a6a41d1b09df6100",
      "source_url": "https://github.com/Leviidev/Henge/blob/main/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "GPL-2.0-or-later covers emulator code; macOS and boot ROMs are outside that grant."
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-11-10T23:53:38Z",
        "reviewed_at": "2026-11-16T14:58:29.135174Z",
        "url": "https://github.com/Leviidev/Henge/releases/tag/0.3",
        "qualifies": true,
        "reason": {
          "zh-CN": "已核对正式发行 0.3 的发布状态与时间。",
          "en": "Checked the non-draft, non-prerelease publication 0.3 and its date."
        },
        "draft": false,
        "prerelease": false
      }
    ],
    "sources": [
      {
        "url": "https://github.com/Leviidev/Henge",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/Leviidev/Henge/blob/main/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/Leviidev/Henge/blob/main/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/Leviidev/Henge/releases/tag/0.3",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://www.woshipm.com/ai/6492489.html",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      }
    ],
    "article_source": {
      "article_id": "2247538432_1",
      "title": "又 3 个刚开源但要火的 GitHub 项目，在 iPhone 上跑 macOS。",
      "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538432&idx=1&sn=631a5c0b7a3a95abf4d4efc11f80d944",
      "published_date": "2026-11-11",
      "account": "逛逛GitHub",
      "content_review_url": "https://www.woshipm.com/ai/6492489.html",
      "content_review_kind": "author-attributed public article",
      "wechat_direct_body_read": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVfjofA",
    "full_name": "Leviidev/Henge",
    "stargazers_count": 2357,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "GPL-2.0",
    "license_sha256": "6f04ae8364d0079a192b14635f4b1da294ce18724c034c39a6a41d1b09df6100",
    "last_success_at": "2026-11-16T14:18:43.351Z"
  }
}
```
