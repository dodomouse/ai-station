# CCBaga

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[liseami/CCBaga](https://github.com/liseami/CCBaga)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 3618 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:34:39.764Z |

## 中文

管理本机 Claude 身份配置、客户端工具和配套浏览器环境。

### 用途与功能

- 备份和切换自己的本地身份配置
- 核对浏览器与系统环境

主程序负责本机操作，配套 Chromium 使用独立配置。提供可恢复身份档案、CLI 维护、区域设置与环境对照。

### 环境与限制

支持macOS12+ Apple Silicon、Linux x64与Windows10/11 x64，Intel Mac与Linux ARM64不支持。部分安装包未签名，配套浏览器分支安全回补未独立核验。仅管理本人合法身份；环境检查通过不代表获得服务访问资格。

### 开始使用

使用项目维护者发布的对应平台安装包，先查看备份与恢复流程，再调整自己的配置。 参阅[官方 README](https://github.com/liseami/CCBaga/blob/main/README.md)。

### 收录与来源

有独立本机程序、浏览器配置隔离和可恢复导入导出实现。 最近维护：[v0.2.50](https://github.com/liseami/CCBaga/releases/tag/v0.2.50)（2026-10-28T04:48:01Z）。正式版修复身份配置往返导入、浏览器配置归属和区域校验。

通过逛逛GitHub的第三方文章索引发现。索引记录了下列文章；本次未读取微信原文，不据此声称已阅读全文。

- 2026-10-24：[最近又刷到 4 个黑科技 GitHub 项目，第 3 个重点看看。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537991&idx=1&sn=69fafc227ed7436bf409e5cd3dd1a43d)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。

## English

Manages local Claude identity configuration, client tooling and a companion browser environment.

### Uses and features

- Back up and switch personal local identity configurations
- Inspect browser and system environment

A native host manages local operations while a companion Chromium uses an isolated profile. Includes restorable identities, CLI maintenance, region settings and measured environment comparisons.

### Requirements and limits

Supports macOS 12+ on Apple Silicon, Linux x64 and Windows 10/11 x64, not Intel Mac or Linux ARM64. Some installers are unsigned and companion-browser security backports were not independently verified. Manage only your own authorized identities; passing environment checks does not establish service eligibility.

### Getting started

Use the maintainer's platform package and review backup and restoration before changing your own configuration. See the [official README](https://github.com/liseami/CCBaga/blob/main/README.md).

### Review and provenance

Includes native software, browser-profile isolation and restorable import/export implementation. Recent maintenance: [v0.2.50](https://github.com/liseami/CCBaga/releases/tag/v0.2.50) (2026-10-28T04:48:01Z). The formal release fixes identity round trips, browser-profile ownership and region checks.

Discovered through a third-party index of 逛逛GitHub articles. The index records the articles below; the original WeChat pages were not read in this review. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:34:39.764Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "ccbaga",
    "name": "CCBaga",
    "repository": "liseami/CCBaga",
    "repo_node_id": "R_kgDOVEZgvw",
    "category": "productivity",
    "tags": [],
    "forms": [
      "desktop"
    ],
    "platforms": [
      "macos",
      "linux",
      "windows"
    ],
    "aliases": {
      "zh-CN": [
        "CCBaga"
      ],
      "en": [
        "CCBaga"
      ]
    },
    "summary": {
      "zh-CN": "管理本机 Claude 身份配置、客户端工具和配套浏览器环境。",
      "en": "Manages local Claude identity configuration, client tooling and a companion browser environment."
    },
    "use_cases": {
      "zh-CN": [
        "备份和切换自己的本地身份配置",
        "核对浏览器与系统环境"
      ],
      "en": [
        "Back up and switch personal local identity configurations",
        "Inspect browser and system environment"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:34:39.764Z",
        "en": "2026-11-16T14:34:39.764Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "acfcbb3fdae956821acce7ad72ba5c83a3b12d5dc5bc37a78bf2a95e9dbad111",
      "source_url": "https://github.com/liseami/CCBaga/blob/main/LICENSE",
      "reviewed_at": "2026-11-16T14:34:39.764Z"
    },
    "activity_evidence": [
      {
        "type": "release",
        "url": "https://github.com/liseami/CCBaga/releases/tag/v0.2.50",
        "occurred_at": "2026-10-28T04:48:01Z",
        "reason": {
          "zh-CN": "正式版修复身份配置往返导入、浏览器配置归属和区域校验。",
          "en": "The formal release fixes identity round trips, browser-profile ownership and region checks."
        },
        "reviewed_at": "2026-11-16T14:34:39.764Z",
        "qualifies": true
      }
    ],
    "sources": [
      {
        "url": "https://github.com/liseami/CCBaga/blob/main/README.md",
        "accessed_at": "2026-11-16T14:34:39.764Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/liseami/CCBaga/blob/main/LICENSE",
        "accessed_at": "2026-11-16T14:34:39.764Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.noking.tech/github-radar/data/library.json",
        "accessed_at": "2026-11-16T14:34:39.764Z",
        "supports": {
          "zh-CN": "第三方索引中的公众号文章归属、时间与项目发现线索；非原文阅读证据。",
          "en": "Third-party account attribution, article dates and discovery leads; not proof of reading the originals."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537991&idx=1&sn=69fafc227ed7436bf409e5cd3dd1a43d",
        "accessed_at": "2026-11-16T14:34:39.764Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-10-24 最近又刷到 4 个黑科技 GitHub 项目，第 3 个重点看看。；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-10-24; not directly read in this review."
        }
      }
    ],
    "quality_review": {
      "basis": {
        "zh-CN": "有独立本机程序、浏览器配置隔离和可恢复导入导出实现。",
        "en": "Includes native software, browser-profile isolation and restorable import/export implementation."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVEZgvw",
    "full_name": "liseami/CCBaga",
    "stargazers_count": 3618,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "acfcbb3fdae956821acce7ad72ba5c83a3b12d5dc5bc37a78bf2a95e9dbad111",
    "last_success_at": "2026-11-16T14:19:21.730Z"
  }
}
```

</details>

