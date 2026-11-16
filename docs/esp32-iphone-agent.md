# ESP32 iPhone Agent

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[onehumanbeing/esp32-iphone-agent](https://github.com/onehumanbeing/esp32-iphone-agent)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 自动化 / Automation |
| 状态 / Status | 已收录 / Included |
| Star | 5022 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:19:21.678Z |

## 中文

让智能体通过 ESP32-S3 与真实 iPhone 交互的软硬件项目。

### 主要功能

- 结合屏幕图像与硬件输入执行手机操作。
- 提供固件、iPhone 应用和智能体集成说明。

### 环境与限制

- 要求 iOS 18+、兼容的 ESP32-S3 与 USB 连接。
- 模型服务与硬件需另备，TestFlight 版本与设备兼容性仍在变化。

### 开始使用

从[官方说明](https://github.com/onehumanbeing/esp32-iphone-agent/blob/main/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/onehumanbeing/esp32-iphone-agent/releases)可用于确认版本。

### 收录复核

让智能体通过 ESP32-S3 与真实 iPhone 交互的软硬件项目。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。

有效维护证据：[v1.0.6-build17](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.6-build17)，2026-11-15T18:38:54Z。已核对正式发行 v1.0.6-build17 的发布状态与时间。

发现线索：[公开索引](https://www.noking.tech/github-radar/)记录的[微信文章](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537991&idx=1&sn=69fafc227ed7436bf409e5cd3dd1a43d)，索引日期 2026-10-24。仅核对公开索引，未直接读取该篇微信全文；功能与限制以上游资料为依据。

本次为文档与实现证据复核，未安装或运行上游项目。

## English

A hardware and software project that lets an agent interact with a real iPhone through an ESP32-S3.

### Features

- Combines screen images with hardware input for phone interaction.
- Provides firmware, an iPhone app and agent integration instructions.

### Requirements and limits

- Requires iOS 18+, a compatible ESP32-S3 and USB connectivity.
- Hardware and model access are separate
- TestFlight builds and device compatibility continue to evolve.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/onehumanbeing/esp32-iphone-agent/blob/main/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/onehumanbeing/esp32-iphone-agent/releases) for versions.

### Review and provenance

A hardware and software project that lets an agent interact with a real iPhone through an ESP32-S3. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.

Activity: [v1.0.6-build17](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.6-build17), 2026-11-15T18:38:54Z. Checked the non-draft, non-prerelease publication v1.0.6-build17 and its date.

Discovery: [an indexed WeChat article](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537991&idx=1&sn=69fafc227ed7436bf409e5cd3dd1a43d). This is a secondary discovery record; the WeChat article body was not read. Features and limits come from upstream documentation.

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
    "id": "esp32-iphone-agent",
    "name": "ESP32 iPhone Agent",
    "repository": "onehumanbeing/esp32-iphone-agent",
    "repo_node_id": "R_kgDOVFJing",
    "category": "automation",
    "summary": {
      "zh-CN": "让智能体通过 ESP32-S3 与真实 iPhone 交互的软硬件项目。",
      "en": "A hardware and software project that lets an agent interact with a real iPhone through an ESP32-S3."
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
      "zh-CN": "让智能体通过 ESP32-S3 与真实 iPhone 交互的软硬件项目。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。",
      "en": "A hardware and software project that lets an agent interact with a real iPhone through an ESP32-S3. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "8ced745c0be8568fb1708a4d21665a8dafbaffb1f23bcafcbb105b15001260b2",
      "source_url": "https://github.com/onehumanbeing/esp32-iphone-agent/blob/main/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "Root license reviewed. External dependencies and assets retain their individual licenses."
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-11-15T18:38:54Z",
        "reviewed_at": "2026-11-16T14:58:29.135174Z",
        "url": "https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.6-build17",
        "qualifies": true,
        "reason": {
          "zh-CN": "已核对正式发行 v1.0.6-build17 的发布状态与时间。",
          "en": "Checked the non-draft, non-prerelease publication v1.0.6-build17 and its date."
        },
        "draft": false,
        "prerelease": false
      }
    ],
    "sources": [
      {
        "url": "https://github.com/onehumanbeing/esp32-iphone-agent",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/onehumanbeing/esp32-iphone-agent/blob/main/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/onehumanbeing/esp32-iphone-agent/blob/main/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.6-build17",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537991&idx=1&sn=69fafc227ed7436bf409e5cd3dd1a43d",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      }
    ],
    "article_source": {
      "article_id": "2247537991_1",
      "title": "最近又刷到 4 个黑科技 GitHub 项目，第 3 个重点看看。",
      "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537991&idx=1&sn=69fafc227ed7436bf409e5cd3dd1a43d",
      "published_date": "2026-10-24",
      "account": "逛逛GitHub",
      "content_review_url": null,
      "content_review_kind": "secondary article index only",
      "wechat_direct_body_read": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVFJing",
    "full_name": "onehumanbeing/esp32-iphone-agent",
    "stargazers_count": 5022,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "8ced745c0be8568fb1708a4d21665a8dafbaffb1f23bcafcbb105b15001260b2",
    "last_success_at": "2026-11-16T14:19:21.678Z"
  }
}
```
