# CleanYourTV

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[Gathin23/cleanyourtv](https://github.com/Gathin23/cleanyourtv)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 部署与运维 / Deployment and operations |
| 状态 / Status | 已收录 / Included |
| Star | 58509 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:32:13.862Z |

## 中文

为 Android TV/Google TV 提供可恢复的预装软件停用流程和轻量桌面启动器。

### 用途与功能

- 整理电视预装应用与主页
- 建立可恢复的电视配置记录

通过 ADB 备份包列表与设置，再停用所选包；提供原生launcher、主题与恢复脚本。

### 环境与限制

只适用于 Android TV/Google TV，不支持 Tizen、webOS、Roku 或 VIDAA。需启用调试并连接同一网络；构建需 Python 3、JDK 17–22 与 Android SDK 34。软件包差异可能影响厂商功能，应按设备确认。字体采用独立OFL许可。

### 开始使用

按 README 识别电视系统与型号，准备构建环境，备份后使用仓库脚本；需要恢复时使用生成的记录。 参阅[官方 README](https://github.com/Gathin23/cleanyourtv/blob/main/README.md)。

### 收录与来源

包含备份、恢复与launcher实现，不仅是让智能体执行命令的提示。 最近维护：[v3.5.0](https://github.com/Gathin23/cleanyourtv/releases/tag/v3.5.0)（2026-11-14T12:41:45Z）。正式版修复设置变化造成的主页内存保留，并增加电视适配与主题。

通过逛逛GitHub的第三方文章索引发现。索引记录了下列文章；本次未读取微信原文，不据此声称已阅读全文。

- 2026-10-30：[这 6 个 GitHub 项目是刚开源，但是 Star 攀升很快的几个。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538171&idx=1&sn=cd8f63d5332497b649d72590298e1a05)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。


补充核对作者在公开平台发布或授权发布的文章，确认署名、日期与仓库关联：

- 2026-10-30：[这 6 个 GitHub 项目是刚开源，但是 Star 攀升很快的几个。](https://www.woshipm.com/ai/6486928.html)

## English

Provides reversible package-disabling workflows and a lightweight launcher for Android TV/Google TV.

### Uses and features

- Clean up TV preloads and the home screen
- Maintain restorable TV configuration records

Uses ADB to back up package lists and settings before disabling selected packages, with a native launcher, themes and restore scripts.

### Requirements and limits

Targets Android TV/Google TV, not Tizen, webOS, Roku or VIDAA. Debugging and same-network access are required; builds need Python 3, JDK 17–22 and Android SDK 34. Package differences can affect vendor features, so review each device. The font has a separate OFL license.

### Getting started

Identify the TV OS and model, prepare the build tools and use repository scripts after backup; retain the generated records for restoration. See the [official README](https://github.com/Gathin23/cleanyourtv/blob/main/README.md).

### Review and provenance

Includes backup, restore and launcher implementation beyond an agent prompt. Recent maintenance: [v3.5.0](https://github.com/Gathin23/cleanyourtv/releases/tag/v3.5.0) (2026-11-14T12:41:45Z). The formal release fixes retained home-screen memory after settings changes and adds TV profiles and themes.

Discovered through a third-party index of 逛逛GitHub articles. The index records the articles below; the original WeChat pages were not read in this review. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.


Public articles published or authorized by the author were also checked for attribution, date and repository links. See the additional links in the Chinese section.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:32:13.862Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "cleanyourtv",
    "name": "CleanYourTV",
    "repository": "Gathin23/cleanyourtv",
    "repo_node_id": "R_kgDOVNLNMw",
    "category": "operations",
    "tags": [],
    "forms": [
      "cli",
      "desktop"
    ],
    "platforms": [
      "android"
    ],
    "aliases": {
      "zh-CN": [
        "CleanYourTV"
      ],
      "en": [
        "CleanYourTV"
      ]
    },
    "summary": {
      "zh-CN": "为 Android TV/Google TV 提供可恢复的预装软件停用流程和轻量桌面启动器。",
      "en": "Provides reversible package-disabling workflows and a lightweight launcher for Android TV/Google TV."
    },
    "use_cases": {
      "zh-CN": [
        "整理电视预装应用与主页",
        "建立可恢复的电视配置记录"
      ],
      "en": [
        "Clean up TV preloads and the home screen",
        "Maintain restorable TV configuration records"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:32:13.862Z",
        "en": "2026-11-16T14:32:13.862Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "e0941eca3b403700368b495fd9a91af4e15242fabb992ed27af95c0d4cdc6f83",
      "source_url": "https://github.com/Gathin23/cleanyourtv/blob/c2d6e79381add9daa83e116882f6d6b130dc4a73/LICENSE",
      "reviewed_at": "2026-11-16T14:32:13.862Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "c2d6e79381add9daa83e116882f6d6b130dc4a73"
    },
    "activity_evidence": [
      {
        "type": "release",
        "reason": {
          "zh-CN": "正式版修复设置变化造成的主页内存保留，并增加电视适配与主题。",
          "en": "The formal release fixes retained home-screen memory after settings changes and adds TV profiles and themes."
        },
        "reviewed_at": "2026-11-16T14:32:13.862Z",
        "qualifies": true,
        "url": "https://github.com/Gathin23/cleanyourtv/releases/tag/v3.5.0",
        "occurred_at": "2026-11-14T12:41:45Z"
      }
    ],
    "sources": [
      {
        "url": "https://github.com/Gathin23/cleanyourtv/blob/main/README.md",
        "accessed_at": "2026-11-16T14:32:13.862Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/Gathin23/cleanyourtv/blob/c2d6e79381add9daa83e116882f6d6b130dc4a73/LICENSE",
        "accessed_at": "2026-11-16T14:32:13.862Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.noking.tech/github-radar/data/library.json",
        "accessed_at": "2026-11-16T14:32:13.862Z",
        "supports": {
          "zh-CN": "第三方索引中的公众号文章归属、时间与项目发现线索；非原文阅读证据。",
          "en": "Third-party account attribution, article dates and discovery leads; not proof of reading the originals."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538171&idx=1&sn=cd8f63d5332497b649d72590298e1a05",
        "accessed_at": "2026-11-16T14:32:13.862Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-10-30 这 6 个 GitHub 项目是刚开源，但是 Star 攀升很快的几个。；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-10-30; not directly read in this review."
        }
      },
      {
        "url": "https://www.woshipm.com/ai/6486928.html",
        "accessed_at": "2026-11-16T14:26:00.391353+00:00",
        "published_date": "2026-10-30",
        "author": "逛逛GitHub",
        "supports": {
          "zh-CN": "作者公开发表或授权的文章；已核对署名、日期与仓库链接。",
          "en": "Author-published or authorized public article; attribution, date and repository links checked."
        }
      }
    ],
    "quality_review": {
      "basis": {
        "zh-CN": "包含备份、恢复与launcher实现，不仅是让智能体执行命令的提示。",
        "en": "Includes backup, restore and launcher implementation beyond an agent prompt."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVNLNMw",
    "full_name": "Gathin23/cleanyourtv",
    "stargazers_count": 58509,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "e0941eca3b403700368b495fd9a91af4e15242fabb992ed27af95c0d4cdc6f83",
    "last_success_at": "2026-11-16T14:19:06.268Z"
  }
}
```

</details>

