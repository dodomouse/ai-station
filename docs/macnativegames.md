# MacNativeGames

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[ly05010419/MacNativeGames](https://github.com/ly05010419/MacNativeGames)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 7913 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:34:39.666Z |

## 中文

研究将指定游戏的图形与系统调用适配到 Apple 芯片和 Metal。

### 用途与功能

- 研究ARM64程序与图形接口移植

提供构建脚本、补丁、宿主系统服务和图形转换实现；支持范围按游戏版本与设备列出。

### 环境与限制

属于技术探索，兼容性有限。正式快照需 Apple Silicon Mac 与 macOS26；部分iOS路径需iOS/iPadOS26和相应设备。仓库不含游戏、密钥或固件，用户须自备合法持有的文件；构建产物含游戏内容，不应任意分享。依赖代码各保留许可。

### 开始使用

先核对具体游戏版本与设备，再按安装文档从自己的文件构建。 参阅[官方 README](https://github.com/ly05010419/MacNativeGames/blob/main/README.md)。

### 收录与来源

有实际移植、图形处理和构建实现，研究范围与输入条件有明确说明。 最近维护：[v2026.10.25](https://github.com/ly05010419/MacNativeGames/releases/tag/v2026.10.25)（2026-10-25T13:13:06Z）。正式快照交付已实现的手机显示、存档与图形路径改进；仅提供源码。

通过逛逛GitHub的第三方文章索引发现。索引记录了下列文章；本次未读取微信原文，不据此声称已阅读全文。

- 2026-10-27：[在电脑和手机上玩 Switch 游戏？这 5 个GitHub 项目值得看看。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538101&idx=1&sn=9586777b5d22d5b3dbfbc0693fda1098)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。

## English

Explores adapting selected games' graphics and system calls to Apple silicon and Metal.

### Uses and features

- Study ARM64 program and graphics-interface porting

Provides build scripts, patches, host system services and graphics translation, with support listed by game version and device.

### Requirements and limits

A technical exploration with limited compatibility. The tagged snapshot requires an Apple Silicon Mac and macOS 26; some mobile paths require iOS/iPadOS 26 and supported devices. Games, keys and firmware are not included; users need their own lawfully held files, and built game-containing apps are not for unrestricted redistribution. Dependencies retain their own licenses.

### Getting started

Check the exact game version and device, then follow the installation guide to build from your own files. See the [official README](https://github.com/ly05010419/MacNativeGames/blob/main/README.md).

### Review and provenance

Contains porting, graphics and build implementation with explicit research scope and input requirements. Recent maintenance: [v2026.10.25](https://github.com/ly05010419/MacNativeGames/releases/tag/v2026.10.25) (2026-10-25T13:13:06Z). The formal source snapshot delivers implemented mobile display, save and graphics-path improvements.

Discovered through a third-party index of 逛逛GitHub articles. The index records the articles below; the original WeChat pages were not read in this review. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:34:39.666Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "macnativegames",
    "name": "MacNativeGames",
    "repository": "ly05010419/MacNativeGames",
    "repo_node_id": "R_kgDOVNvIig",
    "category": "development",
    "tags": [],
    "forms": [
      "cli"
    ],
    "platforms": [
      "macos",
      "ios"
    ],
    "aliases": {
      "zh-CN": [
        "MacNativeGames"
      ],
      "en": [
        "MacNativeGames"
      ]
    },
    "summary": {
      "zh-CN": "研究将指定游戏的图形与系统调用适配到 Apple 芯片和 Metal。",
      "en": "Explores adapting selected games' graphics and system calls to Apple silicon and Metal."
    },
    "use_cases": {
      "zh-CN": [
        "研究ARM64程序与图形接口移植"
      ],
      "en": [
        "Study ARM64 program and graphics-interface porting"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:34:39.666Z",
        "en": "2026-11-16T14:34:39.666Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "a035ee21f927d2247f30bedc8964c95b3a4d794f76c78cad178b68731815a79a",
      "source_url": "https://github.com/ly05010419/MacNativeGames/blob/39c122c50edcb92cb6d3b286dca3fa4927f2685e/LICENSE",
      "reviewed_at": "2026-11-16T14:34:39.666Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "39c122c50edcb92cb6d3b286dca3fa4927f2685e"
    },
    "activity_evidence": [
      {
        "type": "release",
        "url": "https://github.com/ly05010419/MacNativeGames/releases/tag/v2026.10.25",
        "occurred_at": "2026-10-25T13:13:06Z",
        "reason": {
          "zh-CN": "正式快照交付已实现的手机显示、存档与图形路径改进；仅提供源码。",
          "en": "The formal source snapshot delivers implemented mobile display, save and graphics-path improvements."
        },
        "reviewed_at": "2026-11-16T14:34:39.666Z",
        "qualifies": true
      }
    ],
    "sources": [
      {
        "url": "https://github.com/ly05010419/MacNativeGames/blob/main/README.md",
        "accessed_at": "2026-11-16T14:34:39.666Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/ly05010419/MacNativeGames/blob/39c122c50edcb92cb6d3b286dca3fa4927f2685e/LICENSE",
        "accessed_at": "2026-11-16T14:34:39.666Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.noking.tech/github-radar/data/library.json",
        "accessed_at": "2026-11-16T14:34:39.666Z",
        "supports": {
          "zh-CN": "第三方索引中的公众号文章归属、时间与项目发现线索；非原文阅读证据。",
          "en": "Third-party account attribution, article dates and discovery leads; not proof of reading the originals."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538101&idx=1&sn=9586777b5d22d5b3dbfbc0693fda1098",
        "accessed_at": "2026-11-16T14:34:39.666Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-10-27 在电脑和手机上玩 Switch 游戏？这 5 个GitHub 项目值得看看。；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-10-27; not directly read in this review."
        }
      }
    ],
    "quality_review": {
      "basis": {
        "zh-CN": "有实际移植、图形处理和构建实现，研究范围与输入条件有明确说明。",
        "en": "Contains porting, graphics and build implementation with explicit research scope and input requirements."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVNvIig",
    "full_name": "ly05010419/MacNativeGames",
    "stargazers_count": 7913,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "a035ee21f927d2247f30bedc8964c95b3a4d794f76c78cad178b68731815a79a",
    "last_success_at": "2026-11-16T14:19:06.272Z"
  }
}
```

</details>

