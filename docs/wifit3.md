# wifit3

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[derv82/wifit3](https://github.com/derv82/wifit3)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 部署与运维 / Deployment and operations |
| 状态 / Status | 已收录 / Included |
| Star | 3593 |
| 许可证 / License | GPL-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:47:41.313Z |

## 中文

使用支持的USB无线网卡分析无线网络状态与安全配置。

### 用途与功能

- 审计自己管理的无线网络

提供多网卡采集、实时信道扫描、接入点与客户端识别和数据包界面；无线驱动栈在用户态运行。

### 环境与限制

必须具备项目支持的USB适配器，系统权限和USB后端按平台配置。安全测试功能只应在已授权网络使用；硬件、频段与驱动兼容性影响覆盖。Android支持位于独立fork，不属于本词条。

### 开始使用

先核对硬件清单和系统安装说明，在自己的测试网络中使用扫描与观察功能。 参阅[官方 README](https://github.com/derv82/wifit3/blob/master/README.md)。

### 收录与来源

实现USB后端、无线解析与交互式界面，具有明确硬件支持范围。 最近维护：[v0.7.1](https://github.com/derv82/wifit3/releases/tag/v0.7.1)（2026-11-11T22:54:08Z）。正式版增加无线芯片支持并改进USB后端和信道配置。

通过逛逛GitHub的第三方文章索引发现。索引记录了下列文章；本次未读取微信原文，不据此声称已阅读全文。

- 2026-09-27：[推荐 8 个最近火火火火的开源项目，登上 GitHub 今日热榜。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537385&idx=1&sn=6f57abbd0554d6288c4aa1b3566ef704)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。


补充核对作者在公开平台发布或授权发布的文章，确认署名、日期与仓库关联：

- 2026-09-28：[推荐 8 个最近火火火火的开源项目，登上 GitHub 今日热榜。](https://www.woshipm.com/share/6470709.html)

## English

Uses supported USB wireless adapters to analyze wireless-network state and security configuration.

### Uses and features

- Audit wireless networks you administer

Provides multi-adapter capture, channel scanning, access-point and client identification and a packet dashboard with a userspace wireless stack.

### Requirements and limits

Requires a supported USB adapter and platform-specific permissions and USB backend setup. Use security testing only on authorized networks; hardware, bands and driver compatibility limit coverage. Android support is a separate fork outside this entry.

### Getting started

Check the hardware list and platform setup, then use scanning and observation on your own test network. See the [official README](https://github.com/derv82/wifit3/blob/master/README.md).

### Review and provenance

Implements USB backends, wireless parsing and an interactive interface with a documented hardware matrix. Recent maintenance: [v0.7.1](https://github.com/derv82/wifit3/releases/tag/v0.7.1) (2026-11-11T22:54:08Z). The formal release adds chipset support and improves USB backends and channel configuration.

Discovered through a third-party index of 逛逛GitHub articles. The index records the articles below; the original WeChat pages were not read in this review. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.


Public articles published or authorized by the author were also checked for attribution, date and repository links. See the additional links in the Chinese section.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:47:41.313Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "wifit3",
    "name": "wifit3",
    "repository": "derv82/wifit3",
    "repo_node_id": "R_kgDOTAYQNQ",
    "category": "operations",
    "tags": [],
    "forms": [
      "cli"
    ],
    "platforms": [
      "linux",
      "macos",
      "windows"
    ],
    "aliases": {
      "zh-CN": [
        "wifit3"
      ],
      "en": [
        "wifit3"
      ]
    },
    "summary": {
      "zh-CN": "使用支持的USB无线网卡分析无线网络状态与安全配置。",
      "en": "Uses supported USB wireless adapters to analyze wireless-network state and security configuration."
    },
    "use_cases": {
      "zh-CN": [
        "审计自己管理的无线网络"
      ],
      "en": [
        "Audit wireless networks you administer"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:47:41.313Z",
        "en": "2026-11-16T14:47:41.313Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "GPL-2.0",
      "osi_approved": true,
      "license_sha256": "edaef632cbb643e4e7a221717a6c441a4c1a7c918e6e4d56debc3d8739b233f6",
      "source_url": "https://github.com/derv82/wifit3/blob/master/LICENSE",
      "reviewed_at": "2026-11-16T14:47:41.313Z"
    },
    "activity_evidence": [
      {
        "type": "release",
        "url": "https://github.com/derv82/wifit3/releases/tag/v0.7.1",
        "occurred_at": "2026-11-11T22:54:08Z",
        "reason": {
          "zh-CN": "正式版增加无线芯片支持并改进USB后端和信道配置。",
          "en": "The formal release adds chipset support and improves USB backends and channel configuration."
        },
        "reviewed_at": "2026-11-16T14:47:41.313Z",
        "qualifies": true
      }
    ],
    "sources": [
      {
        "url": "https://github.com/derv82/wifit3/blob/master/README.md",
        "accessed_at": "2026-11-16T14:47:41.313Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/derv82/wifit3/blob/master/LICENSE",
        "accessed_at": "2026-11-16T14:47:41.313Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.noking.tech/github-radar/data/library.json",
        "accessed_at": "2026-11-16T14:47:41.313Z",
        "supports": {
          "zh-CN": "第三方索引中的公众号文章归属、时间与项目发现线索；非原文阅读证据。",
          "en": "Third-party account attribution, article dates and discovery leads; not proof of reading the originals."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537385&idx=1&sn=6f57abbd0554d6288c4aa1b3566ef704",
        "accessed_at": "2026-11-16T14:47:41.313Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-09-27 推荐 8 个最近火火火火的开源项目，登上 GitHub 今日热榜。；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-09-27; not directly read in this review."
        }
      },
      {
        "url": "https://www.woshipm.com/share/6470709.html",
        "accessed_at": "2026-11-16T14:26:01.891924+00:00",
        "published_date": "2026-09-28",
        "author": "逛逛GitHub",
        "supports": {
          "zh-CN": "作者公开发表或授权的文章；已核对署名、日期与仓库链接。",
          "en": "Author-published or authorized public article; attribution, date and repository links checked."
        }
      }
    ],
    "quality_review": {
      "basis": {
        "zh-CN": "实现USB后端、无线解析与交互式界面，具有明确硬件支持范围。",
        "en": "Implements USB backends, wireless parsing and an interactive interface with a documented hardware matrix."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOTAYQNQ",
    "full_name": "derv82/wifit3",
    "stargazers_count": 3593,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "GPL-2.0",
    "license_sha256": "edaef632cbb643e4e7a221717a6c441a4c1a7c918e6e4d56debc3d8739b233f6",
    "last_success_at": "2026-11-16T14:20:00.196Z"
  }
}
```

</details>

