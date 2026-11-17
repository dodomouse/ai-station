# Clash Verge Rev

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 部署与运维 / Operations |
| 状态 / Status | 已收录 / Included |
| Star | 158520 |
| 许可证 / License | GPL-3.0 |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T10:48:13.339Z |

以上为历史核对结果，使用前请复核上游状态。 / This is a dated review; check the current upstream state before use.

## 中文

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

### 原始中文记录（历史快照）

### 006 Clash Verge Rev

仓库：[clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev)

#### 1. 简介

基于 Tauri 的 mihomo 图形代理客户端。提供配置管理、规则编辑、系统代理、TUN 模式和 WebDAV 同步。

#### 2. 适用场景

管理代理节点与分流规则。在桌面切换代理配置。同步配置文件。

#### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 代理配置管理 | 导入并管理配置文件，提供语法提示。支持 Merge 与 Script 增强配置。 | Features |
| 系统代理与 TUN | 提供系统代理及守卫功能，并支持 TUN 虚拟网卡模式。 | Features |
| 节点与规则可视化 | 在图形界面编辑节点、代理组与分流规则。 | Features |
| 配置备份和同步 | 支持通过 WebDAV 备份、同步配置。 | Features |
| 桌面外观定制 | 支持主题色、代理组与托盘图标定制，也支持 CSS 注入。 | Features |
| mihomo 内核管理 | 内置 Clash.Meta/mihomo，并提供 Alpha 内核切换入口。 | Features |

官方来源入口：[官方 README](https://github.com/clash-verge-rev/clash-verge-rev/blob/dev/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

**平台与环境**

- Windows x64/x86
- Linux x64/arm64
- macOS 11+，Intel 与 Apple Silicon

- 代码标示 GPL-3.0。客户端许可不提供代理节点或网络套餐；节点、订阅服务及 WebDAV 托管可能另有费用。README 的推广服务不等于软件内置免费服务。

- 需要可用节点与正确配置，安装客户端本身不能保证网络可达。
- 不同系统的 TUN、服务模式与权限要求需另查官方文档。
- 性能、隐私和连接质量未在本轮运行核验。

**容易找错的需求（不属于本项目能力）**

- 不匹配“免费送可用代理节点或网络套餐”的需求。
- 不是 WireGuard/OpenVPN 通用配置兼容性的已验证替代品。

#### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/clash-verge-rev/clash-verge-rev/blob/dev/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- 桌面图形界面
- 托盘
- 系统代理与 TUN
- 配置文件、Merge、Script
- WebDAV

#### 6. 替代选择

- [clashbk/clash](clash.md#中文)：本项目是可运行的桌面代理客户端；后者汇总客户端入口和教程。

#### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/clash-verge-rev/clash-verge-rev/blob/dev/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/006_clash-verge-rev-clash-verge-rev.md`。

## English

A graphical proxy client built around Mihomo, with profile management, routing rules, system proxy and TUN controls.

### Use cases

- Manage proxy profiles
- Configure routing and system proxy behavior

### Requirements and limits

The client supplies no network subscription or proxy nodes. TUN permissions and service modes vary by system. Connection quality, privacy and performance were not tested. Third-party subscription and storage services may charge separately.

### Getting started

Read the [official documentation](https://github.com/clash-verge-rev/clash-verge-rev/blob/dev/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [Clash Navigation](clash.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:13.339Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

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
    "id": "clash-verge-rev",
    "name": "Clash Verge Rev",
    "repository": "clash-verge-rev/clash-verge-rev",
    "repo_node_id": "R_kgDOKwVKzA",
    "category": "operations",
    "tags": [
      "proxy",
      "network",
      "desktop"
    ],
    "forms": [
      "desktop"
    ],
    "platforms": [
      "linux",
      "macos",
      "windows"
    ],
    "aliases": {
      "zh-CN": [
        "Clash Verge Rev"
      ],
      "en": [
        "Clash Verge Rev"
      ]
    },
    "summary": {
      "zh-CN": "基于 Tauri 的 mihomo 图形代理客户端。提供配置管理、规则编辑、系统代理、TUN 模式和 WebDAV 同步。",
      "en": "A graphical proxy client built around Mihomo, with profile management, routing rules, system proxy and TUN controls."
    },
    "use_cases": {
      "zh-CN": [
        "管理代理节点与分流规则。在桌面切换代理配置。同步配置文件。"
      ],
      "en": [
        "Manage proxy profiles",
        "Configure routing and system proxy behavior"
      ]
    },
    "alternatives": [
      "clash"
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
      "spdx": "GPL-3.0",
      "osi_approved": true,
      "license_sha256": "3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986",
      "source_url": "https://github.com/clash-verge-rev/clash-verge-rev/blob/b2689b4220fd4cb8255b1f55331254a469870aff/LICENSE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "b2689b4220fd4cb8255b1f55331254a469870aff"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-14T17:38:07Z",
        "reviewed_at": "2026-11-15T11:03:50.120930Z",
        "url": "https://github.com/clash-verge-rev/clash-verge-rev/commit/41ad2d6d02366d24528b79fd5e8d7f6b164fbb64",
        "qualifies": true,
        "reason": {
          "zh-CN": "使 TUN 使用界面显示的默认 MTU。已核对提交中的实现文件与差异；未运行上游测试。",
          "en": "Applies the displayed default MTU to TUN. Reviewed implementation changes; upstream tests were not run."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/clash-verge-rev/clash-verge-rev",
        "accessed_at": "2026-11-15T10:48:13.339Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/clash-verge-rev/clash-verge-rev/blob/dev/README.md",
        "accessed_at": "2026-11-15T10:53:59.629Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      },
      {
        "url": "https://github.com/clash-verge-rev/clash-verge-rev/blob/b2689b4220fd4cb8255b1f55331254a469870aff/LICENSE",
        "accessed_at": "2026-11-15T10:53:07.631Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "006",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "204b98b475333e331a952a959d11f2075769f6f63a663de2b20eedb6c20b66c1",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "tool",
      "pending_reasons": [],
      "english_scope": "editorial_digest",
      "source_card_preserved": true
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOKwVKzA",
    "full_name": "clash-verge-rev/clash-verge-rev",
    "stargazers_count": 158520,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "GPL-3.0",
    "license_sha256": "3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986",
    "last_success_at": "2026-11-15T10:48:13.339Z"
  }
}
```

</details>
