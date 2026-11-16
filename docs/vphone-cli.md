# vphone-cli

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[Lakr233/vphone-cli](https://github.com/Lakr233/vphone-cli)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 16695 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:50:00.638Z |

## 中文

在Apple Silicon Mac上运行用于研究与调试的虚拟iPhone。

### 用途与功能

- 调试与研究iOS虚拟环境

基于Apple虚拟化与PCC研究虚拟机，提供图形窗口、固件准备、快照克隆和可选自动化接口。

### 环境与限制

需物理Apple Silicon Mac、macOS15+，不支持嵌套macOS虚拟机。默认虚拟盘64GB且固件另占空间，恢复需联网。运行需调整宿主研究来宾与调试安全设置，应在研究设备上评估；项目许可不授予Apple固件权利。

### 开始使用

先阅读[宿主要求](https://lakr233.github.io/vphone-cli/get-started/overview.html)与安全设置说明，再选择匹配的Launchpad和Core Bundle。 参阅[官方 README](https://github.com/Lakr233/vphone-cli/blob/main/README.md)。

### 收录与来源

实现虚拟机生命周期、固件处理和自动化接口，并持续修复实际设备兼容性。 最近维护：[2.17.1](https://github.com/Lakr233/vphone-cli/releases/tag/2.17.1)（2026-11-13T09:01:22Z）。正式版修复iPad横屏指针与辅助功能插件的ARM指令兼容。

来源为2026-09-05公开转载文章，文末明确署名逛逛GitHub；已从公开正文提取仓库链接。

- 2026-09-05：[GitHub 周报：科研、语音、SEO，一个清单看懂 14 个 AI 项目](https://www.woshipm.com/ai/6460165.html)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。

## English

Runs a virtual iPhone on Apple Silicon Macs for research and debugging.

### Uses and features

- Debug and study virtual iOS environments

Uses Apple virtualization and PCC research VMs with a graphical window, firmware preparation, snapshots, cloning and optional automation APIs.

### Requirements and limits

Needs a physical Apple Silicon Mac with macOS 15+; nested macOS VMs are unsupported. Default virtual disks are 64 GB plus firmware space, and restoration needs networking. Running it requires changes to research-guest and debugging security settings; assess this on research hardware. The project license does not grant rights to Apple firmware.

### Getting started

Read the [host requirements](https://lakr233.github.io/vphone-cli/get-started/overview.html) and security-setting guide before choosing matching Launchpad and Core Bundle versions. See the [official README](https://github.com/Lakr233/vphone-cli/blob/main/README.md).

### Review and provenance

Implements VM lifecycle, firmware processing and automation APIs with ongoing compatibility fixes. Recent maintenance: [2.17.1](https://github.com/Lakr233/vphone-cli/releases/tag/2.17.1) (2026-11-13T09:01:22Z). The formal release fixes iPad landscape pointers and ARM instruction compatibility in accessibility plug-ins.

The source is a public republication dated 2026-09-05 with explicit attribution to 逛逛GitHub; repository links were extracted from its public body. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:50:00.638Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "vphone-cli",
    "name": "vphone-cli",
    "repository": "Lakr233/vphone-cli",
    "repo_node_id": "R_kgDORZbd0w",
    "category": "development",
    "tags": [],
    "forms": [
      "cli",
      "desktop"
    ],
    "platforms": [
      "macos"
    ],
    "aliases": {
      "zh-CN": [
        "vphone-cli"
      ],
      "en": [
        "vphone-cli"
      ]
    },
    "summary": {
      "zh-CN": "在Apple Silicon Mac上运行用于研究与调试的虚拟iPhone。",
      "en": "Runs a virtual iPhone on Apple Silicon Macs for research and debugging."
    },
    "use_cases": {
      "zh-CN": [
        "调试与研究iOS虚拟环境"
      ],
      "en": [
        "Debug and study virtual iOS environments"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:50:00.638Z",
        "en": "2026-11-16T14:50:00.638Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "1f4b38df6a142e678a85d84c3a7ec4d1db328a556483241df714156134e81615",
      "source_url": "https://github.com/Lakr233/vphone-cli/blob/main/LICENSE",
      "reviewed_at": "2026-11-16T14:50:00.638Z"
    },
    "activity_evidence": [
      {
        "type": "release",
        "url": "https://github.com/Lakr233/vphone-cli/releases/tag/2.17.1",
        "occurred_at": "2026-11-13T09:01:22Z",
        "reason": {
          "zh-CN": "正式版修复iPad横屏指针与辅助功能插件的ARM指令兼容。",
          "en": "The formal release fixes iPad landscape pointers and ARM instruction compatibility in accessibility plug-ins."
        },
        "reviewed_at": "2026-11-16T14:50:00.638Z",
        "qualifies": true
      }
    ],
    "sources": [
      {
        "url": "https://github.com/Lakr233/vphone-cli/blob/main/README.md",
        "accessed_at": "2026-11-16T14:50:00.638Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/Lakr233/vphone-cli/blob/main/LICENSE",
        "accessed_at": "2026-11-16T14:50:00.638Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.woshipm.com/ai/6460165.html",
        "accessed_at": "2026-11-16T14:50:00.307Z",
        "supports": {
          "zh-CN": "已核对作者署名、日期与正文仓库链接。",
          "en": "Verified author attribution, date and repository links in the public article body."
        }
      }
    ],
    "quality_review": {
      "basis": {
        "zh-CN": "实现虚拟机生命周期、固件处理和自动化接口，并持续修复实际设备兼容性。",
        "en": "Implements VM lifecycle, firmware processing and automation APIs with ongoing compatibility fixes."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDORZbd0w",
    "full_name": "Lakr233/vphone-cli",
    "stargazers_count": 16695,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "1f4b38df6a142e678a85d84c3a7ec4d1db328a556483241df714156134e81615",
    "last_success_at": "2026-11-16T14:35:03.454Z"
  }
}
```

</details>

