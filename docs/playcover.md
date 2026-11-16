# PlayCover

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[PlayCover/PlayCover](https://github.com/PlayCover/PlayCover)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 12156 |
| 许可证 / License | GPL-3.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:34:39.717Z |

## 中文

在 Apple Silicon Mac 上运行兼容的 iOS 应用，提供键鼠和手柄映射。

### 用途与功能

- 在Mac上使用兼容iOS应用

通过应用包装运行原生ARM应用，提供触控映射、分辨率和应用管理。

### 环境与限制

要求Apple Silicon与macOS12+，不支持Intel Mac。并非所有应用或游戏可运行；应用文件及账户使用遵循各自条件。近期修复存在于开发线，旧稳定发行不必然包含。

### 开始使用

先核对官方兼容说明，再从 Releases 选择合适版本并按文档导入应用。 参阅[官方 README](https://github.com/PlayCover/PlayCover/blob/develop/README.md)。

### 收录与来源

有应用包装与输入映射实现，近期修复直接处理启动兼容性。 最近维护：[实现提交](https://github.com/PlayCover/PlayCover/commit/24bbed786fe1d5acfb0ffc2e619e126bdc09f22b)（2026-10-22T14:31:08Z）。已核对Swift实现：在准备和重签应用包后重建启动别名，避免过期Info.plist。

通过逛逛GitHub的第三方文章索引发现。索引记录了下列文章；本次未读取微信原文，不据此声称已阅读全文。

- 2026-10-24：[最近又刷到 4 个黑科技 GitHub 项目，第 3 个重点看看。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537991&idx=1&sn=69fafc227ed7436bf409e5cd3dd1a43d)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。

## English

Runs compatible iOS applications on Apple Silicon Macs with keyboard, mouse and controller mapping.

### Uses and features

- Use compatible iOS applications on a Mac

Wraps native ARM applications and provides touch mappings, resolution and application management.

### Requirements and limits

Requires Apple Silicon and macOS 12+; Intel Macs are unsupported. Not every app or game works, and app files and accounts retain their own terms. Recent fixes are in development history and may not be present in the older stable release.

### Getting started

Check official compatibility guidance, then choose a release and import an application as documented. See the [official README](https://github.com/PlayCover/PlayCover/blob/develop/README.md).

### Review and provenance

Implements application wrapping and input mapping, with recent fixes addressing launch compatibility. Recent maintenance: [implementation commit](https://github.com/PlayCover/PlayCover/commit/24bbed786fe1d5acfb0ffc2e619e126bdc09f22b) (2026-10-22T14:31:08Z). Reviewed Swift changes rebuilding the launch alias after bundle preparation and signing to avoid stale Info.plist data.

Discovered through a third-party index of 逛逛GitHub articles. The index records the articles below; the original WeChat pages were not read in this review. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:34:39.717Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "playcover",
    "name": "PlayCover",
    "repository": "PlayCover/PlayCover",
    "repo_node_id": "R_kgDOHoPqDw",
    "category": "productivity",
    "tags": [],
    "forms": [
      "desktop"
    ],
    "platforms": [
      "macos"
    ],
    "aliases": {
      "zh-CN": [
        "PlayCover"
      ],
      "en": [
        "PlayCover"
      ]
    },
    "summary": {
      "zh-CN": "在 Apple Silicon Mac 上运行兼容的 iOS 应用，提供键鼠和手柄映射。",
      "en": "Runs compatible iOS applications on Apple Silicon Macs with keyboard, mouse and controller mapping."
    },
    "use_cases": {
      "zh-CN": [
        "在Mac上使用兼容iOS应用"
      ],
      "en": [
        "Use compatible iOS applications on a Mac"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:34:39.717Z",
        "en": "2026-11-16T14:34:39.717Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "GPL-3.0",
      "osi_approved": true,
      "license_sha256": "3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986",
      "source_url": "https://github.com/PlayCover/PlayCover/blob/develop/LICENSE",
      "reviewed_at": "2026-11-16T14:34:39.717Z"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/PlayCover/PlayCover/commit/24bbed786fe1d5acfb0ffc2e619e126bdc09f22b",
        "occurred_at": "2026-10-22T14:31:08Z",
        "reason": {
          "zh-CN": "已核对Swift实现：在准备和重签应用包后重建启动别名，避免过期Info.plist。",
          "en": "Reviewed Swift changes rebuilding the launch alias after bundle preparation and signing to avoid stale Info.plist data."
        },
        "reviewed_at": "2026-11-16T14:34:39.717Z",
        "qualifies": true
      }
    ],
    "sources": [
      {
        "url": "https://github.com/PlayCover/PlayCover/blob/develop/README.md",
        "accessed_at": "2026-11-16T14:34:39.717Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/PlayCover/PlayCover/blob/develop/LICENSE",
        "accessed_at": "2026-11-16T14:34:39.717Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.noking.tech/github-radar/data/library.json",
        "accessed_at": "2026-11-16T14:34:39.717Z",
        "supports": {
          "zh-CN": "第三方索引中的公众号文章归属、时间与项目发现线索；非原文阅读证据。",
          "en": "Third-party account attribution, article dates and discovery leads; not proof of reading the originals."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537991&idx=1&sn=69fafc227ed7436bf409e5cd3dd1a43d",
        "accessed_at": "2026-11-16T14:34:39.717Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-10-24 最近又刷到 4 个黑科技 GitHub 项目，第 3 个重点看看。；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-10-24; not directly read in this review."
        }
      }
    ],
    "quality_review": {
      "basis": {
        "zh-CN": "有应用包装与输入映射实现，近期修复直接处理启动兼容性。",
        "en": "Implements application wrapping and input mapping, with recent fixes addressing launch compatibility."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOHoPqDw",
    "full_name": "PlayCover/PlayCover",
    "stargazers_count": 12156,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "GPL-3.0",
    "license_sha256": "3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986",
    "last_success_at": "2026-11-16T14:19:06.360Z"
  }
}
```

</details>

