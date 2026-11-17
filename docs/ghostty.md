# Ghostty

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[ghostty-org/ghostty](https://github.com/ghostty-org/ghostty)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 终端与 Shell / Terminal and shell |
| 状态 / Status | 已收录 / Included |
| Star | 64125 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T10:48:14.646Z |

以上为历史核对结果，使用前请复核上游状态。 / This is a dated review; check the current upstream state before use.

## 中文

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

### 原始中文记录（历史快照）

### 012 Ghostty

仓库：[ghostty-org/ghostty](https://github.com/ghostty-org/ghostty)

#### 1. 简介

使用原生界面和 GPU 渲染的终端模拟器。支持多窗口、标签页与分屏，另提供可嵌入终端库。

#### 2. 适用场景

在 macOS 或 Linux 使用命令行。管理多个终端会话。为应用嵌入终端模拟能力。

#### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 原生终端模拟 | 提供终端模拟与 GPU 渲染。macOS 使用 Metal，Linux 使用 OpenGL。 | About / Roadmap and Status — Competitive Performance |
| 窗口、标签与分屏 | 桌面应用支持多窗口、标签页、分屏及标签重命名等组织功能。 | Roadmap and Status — Rich Windowing Features |
| 现代终端协议 | 支持图像、剪贴板、同步渲染、明暗主题通知等现代终端控制序列。 | Roadmap and Status — Standards-Compliant Terminal Emulation |
| 平台集成 | macOS 采用 SwiftUI、CoreText 并支持 AppleScript 和 Shortcuts。Linux 使用 GTK，并可与 systemd 集成。 | Roadmap and Status — Native Platform Experiences |
| 可嵌入终端库 | 以 libghostty 提供终端嵌入能力。libghostty-vt 可供 Zig/C 使用，并覆盖桌面之外的平台。 | Roadmap and Status — libghostty |

官方来源入口：[官方 README](https://github.com/ghostty-org/ghostty/blob/main/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

**平台与环境**

- 原生桌面应用：macOS、Linux
- libghostty-vt：macOS、Linux、Windows、WebAssembly；不可等同桌面应用支持范围

- GitHub 元数据标示 MIT。终端本身不要求模型 API；在其中运行的编码助手、远程主机及其他程序可能独立收费。

- 终端模拟器不提供自身的大模型能力，也不替代 shell。
- 桌面应用与可嵌入库的平台支持和成熟度不同。
- 项目性能自述未在本轮复现。

**容易找错的需求（不属于本项目能力）**

- 不是按计划自动运行命令或管理任务队列的调度器。
- 不能仅凭 libghostty-vt 跨平台说明声称有正式 Windows 桌面版。

#### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/ghostty-org/ghostty/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- 桌面图形界面
- shell/终端输入输出
- macOS AppleScript 与 Shortcuts
- libghostty 的 C/Zig 嵌入接口

#### 6. 替代选择

- [nextpad-plus-plus/nextpad-plus-plus-macos](nextpad-plus-plus-macos.md#中文)：本项目承载 shell 和终端会话；后者编辑文本和代码。两者覆盖桌面开发中的不同需求。

#### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/ghostty-org/ghostty/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/012_ghostty-org-ghostty.md`。

## English

A terminal emulator with a native interface, GPU rendering, tabs and split panes.

### Use cases

- Run shells and command-line programs
- Manage multiple terminal views

### Requirements and limits

The desktop app supports macOS and Linux. Broader libghostty-vt platform support does not establish a Windows desktop app. Ghostty does not provide a model, task scheduler or shell. Performance claims were not benchmarked here.

### Getting started

Read the [official documentation](https://github.com/ghostty-org/ghostty/blob/main/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [Nextpad++ for macOS](nextpad-plus-plus-macos.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:14.646Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

保留原始核对数据，便于追溯来源、许可和维护证据。 / Original review data preserves source, license and maintenance evidence.

```json
{
  "evaluated_at": "2026-11-15T11:54:08.129868Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "ghostty",
    "name": "Ghostty",
    "repository": "ghostty-org/ghostty",
    "repo_node_id": "R_kgDOHFhdAg",
    "category": "terminal",
    "tags": [
      "terminal",
      "gpu",
      "desktop"
    ],
    "forms": [
      "desktop"
    ],
    "platforms": [
      "linux",
      "macos"
    ],
    "aliases": {
      "zh-CN": [
        "Ghostty"
      ],
      "en": [
        "Ghostty"
      ]
    },
    "summary": {
      "zh-CN": "使用原生界面和 GPU 渲染的终端模拟器。支持多窗口、标签页与分屏，另提供可嵌入终端库。",
      "en": "A terminal emulator with a native interface, GPU rendering, tabs and split panes."
    },
    "use_cases": {
      "zh-CN": [
        "在 macOS 或 Linux 使用命令行。管理多个终端会话。为应用嵌入终端模拟能力。"
      ],
      "en": [
        "Run shells and command-line programs",
        "Manage multiple terminal views"
      ]
    },
    "alternatives": [
      "nextpad-plus-plus-macos"
    ],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-15T11:03:50.120930Z",
        "en": "2026-11-15T11:03:50.120930Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "386211873e5b7a02f663ae4d7adf96285999f91608f8f9f31fecfd0f4095e6f1",
      "source_url": "https://github.com/ghostty-org/ghostty/blob/7fa26e8b675f3248975479d88274c937d7e63905/LICENSE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "7fa26e8b675f3248975479d88274c937d7e63905"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-15T04:04:27Z",
        "reviewed_at": "2026-11-15T11:03:50.120930Z",
        "url": "https://github.com/ghostty-org/ghostty/commit/7fa26e8b675f3248975479d88274c937d7e63905",
        "qualifies": true,
        "reason": {
          "zh-CN": "修正终端扩展行数时的完整性检查时机。已核对提交中的实现文件与差异；未运行上游测试。",
          "en": "Fixes integrity checks while terminal rows are being expanded. Reviewed implementation changes; upstream tests were not run."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/ghostty-org/ghostty",
        "accessed_at": "2026-11-15T10:48:14.646Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/ghostty-org/ghostty/blob/main/README.md",
        "accessed_at": "2026-11-15T10:54:00.354Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      },
      {
        "url": "https://github.com/ghostty-org/ghostty/blob/7fa26e8b675f3248975479d88274c937d7e63905/LICENSE",
        "accessed_at": "2026-11-15T10:53:08.350Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "012",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "e65f808f5196c51f24f5f0da71a5fdeea8b87bca1ee380dc3c68185f17595fe6",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "tool",
      "pending_reasons": [],
      "english_scope": "editorial_digest",
      "source_card_preserved": true
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOHFhdAg",
    "full_name": "ghostty-org/ghostty",
    "stargazers_count": 64125,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "386211873e5b7a02f663ae4d7adf96285999f91608f8f9f31fecfd0f4095e6f1",
    "last_success_at": "2026-11-15T10:48:14.646Z"
  }
}
```

</details>
