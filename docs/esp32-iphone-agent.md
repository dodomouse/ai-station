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

有效维护证据：[v1.0.6-build17](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.6-build17)，2026-11-15T18:38:54Z。修复设备重启后统计事件包含非 JSON 值导致应用崩溃的问题，并为发送前的数据校验增加防护。 2026-11-17 已读取[实现提交](https://github.com/onehumanbeing/esp32-iphone-agent/commit/d39d6a8414298dc58900713baa19a9f49f277dd1)的差异；未运行上游测试。

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

Activity: [v1.0.6-build17](https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.6-build17), 2026-11-15T18:38:54Z. Fixes crashes from non-JSON values in board-reboot analytics and validates events before sending. On 2026-11-17, the [implementation diff](https://github.com/onehumanbeing/esp32-iphone-agent/commit/d39d6a8414298dc58900713baa19a9f49f277dd1) was inspected; upstream tests were not run.

Discovery: [an indexed WeChat article](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537991&idx=1&sn=69fafc227ed7436bf409e5cd3dd1a43d). This is a secondary discovery record; the WeChat article body was not read. Features and limits come from upstream documentation.

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
      "source_url": "https://github.com/onehumanbeing/esp32-iphone-agent/blob/936d9e12c57f15253b35f4ce704ebebd945a1591/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "Root license reviewed. External dependencies and assets retain their individual licenses.",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "936d9e12c57f15253b35f4ce704ebebd945a1591"
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-11-15T18:38:54Z",
        "reviewed_at": "2026-11-17T03:15:51.892548+00:00",
        "url": "https://github.com/onehumanbeing/esp32-iphone-agent/releases/tag/v1.0.6-build17",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复设备重启后统计事件包含非 JSON 值导致应用崩溃的问题，并为发送前的数据校验增加防护。",
          "en": "Fixes crashes from non-JSON values in board-reboot analytics and validates events before sending."
        },
        "draft": false,
        "prerelease": false,
        "implementation_evidence": {
          "type": "commit",
          "url": "https://github.com/onehumanbeing/esp32-iphone-agent/commit/d39d6a8414298dc58900713baa19a9f49f277dd1",
          "sha": "d39d6a8414298dc58900713baa19a9f49f277dd1",
          "occurred_at": "2026-11-15T18:32:19Z",
          "reviewed_at": "2026-11-17T03:15:51.892548+00:00",
          "reviewed_files": [
            "ios/IPhoneAgent/App/AppModel.swift",
            "ios/IPhoneAgent/Services/Analytics.swift"
          ],
          "verification_level": "source_review",
          "upstream_tests_run": false
        }
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
        "url": "https://github.com/onehumanbeing/esp32-iphone-agent/blob/936d9e12c57f15253b35f4ce704ebebd945a1591/LICENSE",
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

</details>
