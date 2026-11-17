# Reason Network

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[reason-machines/reason-network](https://github.com/reason-machines/reason-network)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 自动化 / Automation |
| 状态 / Status | 已收录 / Included |
| Star | 1748 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T10:48:20.592Z |

以上为历史核对结果，使用前请复核上游状态。 / This is a dated review; check the current upstream state before use.

## 中文

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

代码提供 MIT 或 Apache-2.0 双许可。快照保留 API 的 Apache-2.0 字段，并用对应许可证文件建立指纹。

### 原始中文记录（历史快照）

### 041 Reason Network

仓库：[reason-machines/reason-network](https://github.com/reason-machines/reason-network)

#### 1. 简介

每台电脑运行后台程序，共享团队 Agent 会话的人员、设备、项目、分支与工作概况。

#### 2. 适用场景

- 让我的 Codex 找同事的 Claude Code。
- 不同电脑上的 Agent 直接传话。
- 谁的 Agent 正在改哪个仓库和分支。

#### 3. 主要功能

- 每台电脑运行后台程序，共享团队 Agent 会话的人员、设备、项目、分支与工作概况。
- 工具包括 list_team、send_message、message_status 和 ask_user。不同宿主的消息送达时机不同。
- 局域网或互联网尝试点对点连接，无法直连时使用中继。官方声明传输端到端加密，并支持自有中继。
- 支持多个宿主，例如 Claude Code、Codex、Cursor 和 Gemini CLI。托管助手可通过模型上下文协议（MCP）接入。

官方来源入口：[官方 README](https://github.com/reason-machines/reason-network/blob/main/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

需要安装后台程序、登录账号并加入网络。团队可见会话元信息，可按文件夹排除。消息送达或被回复不等于任务完成。PDF 称文件冲突提醒仍在开发，本次未把它认定为已交付能力，也未验证跨机加密实现。

知识卡未提供完整部署费用或付费服务价格；未记录的费用项目需要另行核对。

#### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/reason-machines/reason-network/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

#### 6. 替代选择

- [stablyai/orca](orca.md#中文)：本项目共享团队助手的会话概况并支持通信；后者侧重同一开发工作台内的任务与差异管理。

#### 7. 复核说明

- 知识库记录日期：2026-11-06；卡片最后确认日期：2026-11-06。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 核验范围：已读取官方 README 和仓库元数据。公开仓库，核验时未归档或禁用；本次未安装或运行。

**来源与版本记录**

- [官方 README](https://github.com/reason-machines/reason-network/blob/main/README.md)，读取日期：2026-11-06。
- [仓库元数据](https://api.github.com/repos/reason-machines/reason-network)，仓库 ID：`1422344223`。
- 本次读取的 README Git blob SHA：`f3c7d074cdb8a7a835e3a1dc491d211723880153`。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/041_reason-machines-reason-network.md`。

## English

A background network for communication between agent sessions across teammates, devices and projects.

### Use cases

- Coordinate agent sessions
- Exchange context across machines

### Requirements and limits

Requires installation, an account and network membership. Teams can see session metadata; folders can be excluded. Message delivery or a reply does not establish task completion. Conflict alerts were described as unfinished in the source material, and cross-device encryption was not verified. Code offers MIT or Apache-2.0.

### Getting started

Read the [official documentation](https://github.com/reason-machines/reason-network/blob/main/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [Orca](orca.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:20.592Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

Code offers MIT or Apache-2.0. The snapshot preserves the API’s Apache-2.0 field and fingerprints its matching file.

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
    "id": "reason-network",
    "name": "Reason Network",
    "repository": "reason-machines/reason-network",
    "repo_node_id": "R_kgDOVMdAHw",
    "category": "automation",
    "tags": [
      "agents",
      "collaboration",
      "network"
    ],
    "forms": [
      "service"
    ],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "Reason Network"
      ],
      "en": [
        "Reason Network"
      ]
    },
    "summary": {
      "zh-CN": "每台电脑运行后台程序，共享团队 Agent 会话的人员、设备、项目、分支与工作概况。",
      "en": "A background network for communication between agent sessions across teammates, devices and projects."
    },
    "use_cases": {
      "zh-CN": [
        "- 让我的 Codex 找同事的 Claude Code。\n- 不同电脑上的 Agent 直接传话。\n- 谁的 Agent 正在改哪个仓库和分支。"
      ],
      "en": [
        "Coordinate agent sessions",
        "Exchange context across machines"
      ]
    },
    "alternatives": [
      "orca"
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
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
      "source_url": "https://github.com/reason-machines/reason-network/blob/5442c8b551a6897b596c7695e51b0329551aaa6c/LICENSE-APACHE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "5442c8b551a6897b596c7695e51b0329551aaa6c"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-07T06:48:57Z",
        "reviewed_at": "2026-11-15T11:03:50.120930Z",
        "url": "https://github.com/reason-machines/reason-network/commit/5442c8b551a6897b596c7695e51b0329551aaa6c",
        "qualifies": true,
        "reason": {
          "zh-CN": "拒绝在无法读取或解析配置时启动。已核对提交中的实现文件与差异；未运行上游测试。",
          "en": "Refuses startup when configuration cannot be read or parsed. Reviewed implementation changes; upstream tests were not run."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/reason-machines/reason-network",
        "accessed_at": "2026-11-15T10:48:20.592Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/reason-machines/reason-network/blob/main/README.md",
        "accessed_at": "2026-11-15T10:54:04.507Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      },
      {
        "url": "https://github.com/reason-machines/reason-network/blob/5442c8b551a6897b596c7695e51b0329551aaa6c/LICENSE-APACHE",
        "accessed_at": "2026-11-15T10:53:15.536Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "041",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "744b20e21650ed6da3cc8fc3f81023f099c32dbb30a8b6ddcd556a6c69d14039",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "tool",
      "pending_reasons": [],
      "english_scope": "editorial_digest",
      "source_card_preserved": true,
      "notes": {
        "zh-CN": "代码提供 MIT 或 Apache-2.0 双许可。快照保留 API 的 Apache-2.0 字段，并用对应许可证文件建立指纹。",
        "en": "Code offers MIT or Apache-2.0. The snapshot preserves the API’s Apache-2.0 field and fingerprints its matching file."
      }
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVMdAHw",
    "full_name": "reason-machines/reason-network",
    "stargazers_count": 1748,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
    "last_success_at": "2026-11-15T10:48:20.592Z"
  }
}
```

</details>
