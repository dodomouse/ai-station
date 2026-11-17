# Orca（智能体开发工作台）

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[stablyai/orca](https://github.com/stablyai/orca)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 125338 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T10:48:17.008Z |

以上为历史核对结果，使用前请复核上游状态。 / This is a dated review; check the current upstream state before use.

## 中文

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

### 原始中文记录（历史快照）

### 023 Orca（智能体开发工作台）

仓库：[stablyai/orca](https://github.com/stablyai/orca)

#### 1. 简介

统一管理多个编程智能体的开发工作台。提供并行工作目录、终端、差异审查、手机端及 SSH 远程环境。

#### 2. 适用场景

并行推进多个编程任务。在同一工作台审查智能体修改。用手机或 SSH 跟进远程开发任务。

#### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 并行智能体与 worktree | 可在各自隔离 Git worktree 中运行不同智能体，并比较或合并结果。 | Features / Parallel Worktrees |
| 终端与编辑器工作台 | 提供可分屏终端、保留滚动记录，以及文件编辑和拖入 Agent 的交互。 | Features / Terminal Splits / Drag Files to Agents |
| 手机伴随应用 | 手机配对桌面后可监控任务、接收完成通知并发送后续指令。 | Features / Mobile Companion / Install |
| SSH 远程工作环境 | 在远程机器运行智能体，提供文件编辑、Git、终端、重连和端口转发。 | Features / SSH Worktrees |
| 网页设计定位 | 内嵌 Chromium 的 Design Mode 可将被选元素的 HTML、CSS 和局部截图发给 Agent。 | Features / Design Mode |
| 差异审查与反馈 | 可在 diff 的代码行上添加评论并发送回 Agent，继续审查、编辑或提交。 | Features / Annotate AI Diffs |
| 任务与代码托管集成 | 在应用中浏览 GitHub 和 Linear 的 PR、issue 与项目看板，并从任务进入工作区。 | Features / GitHub & Linear, Native |

官方来源入口：[官方 README](https://github.com/stablyai/orca/blob/main/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

**平台与环境**

- macOS（Apple Silicon 与 Intel）、Windows、Linux 桌面
- iOS、Android 手机伴随应用
- 具备 SSH 的远程运行环境

- 工作台代码按 MIT 开源，README 写 free and open source。
- 所选编程智能体、模型订阅或 API 和远程机器成本另计。
- 手机配对中继和具体托管服务是否收费，README 没有完整价格表，需用前核对。

- 并行隔离依赖 Git worktree，不能据此自动获取创建分支权限。
- 手机端用于配对桌面，不应理解为手机独立承担所有模型和开发环境。
- 功能描述来自 README，未安装、运行或测量效率提升。

**容易找错的需求（不属于本项目能力）**

- 不是 Plotly 的同名图形导出 Orca。
- 不是把本地 Agent 接入飞书或钉钉的 cc-connect 类消息桥。

#### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/stablyai/orca/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- 桌面 GUI 与集成终端
- 内嵌 Chromium / Design Mode
- iOS 与 Android 伴随应用
- SSH 连接

#### 6. 替代选择

- [chenhg5/cc-connect](cc-connect.md#中文)：本项目集中管理开发工作区、终端和差异审查；后者把本机编程助手接到聊天平台。
- [reason-machines/reason-network](reason-network.md#中文)：本项目组织开发任务；后者共享团队助手的会话概况并提供通信。

#### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/stablyai/orca/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/023_stablyai-orca.md`。

## English

A coding-agent workspace with multiple project views, terminals, change review, remote SSH and mobile companions.

### Use cases

- Manage concurrent coding sessions
- Review agent changes across projects

### Requirements and limits

Parallel work can use Git worktrees but does not itself authorize branch creation. Mobile companions pair with desktop infrastructure. Models, remote hosts and relay services may have separate costs. This is unrelated to Plotly's same-name export utility; efficiency claims were not measured.

### Getting started

Read the [official documentation](https://github.com/stablyai/orca/blob/main/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [cc-connect](cc-connect.md#english)
- [Reason Network](reason-network.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:17.008Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

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
    "id": "orca",
    "name": "Orca（智能体开发工作台）",
    "repository": "stablyai/orca",
    "repo_node_id": "R_kgDORpCz1g",
    "category": "development",
    "tags": [
      "agents",
      "workspace",
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
        "Orca（智能体开发工作台）"
      ],
      "en": [
        "Orca"
      ]
    },
    "summary": {
      "zh-CN": "统一管理多个编程智能体的开发工作台。提供并行工作目录、终端、差异审查、手机端及 SSH 远程环境。",
      "en": "A coding-agent workspace with multiple project views, terminals, change review, remote SSH and mobile companions."
    },
    "use_cases": {
      "zh-CN": [
        "并行推进多个编程任务。在同一工作台审查智能体修改。用手机或 SSH 跟进远程开发任务。"
      ],
      "en": [
        "Manage concurrent coding sessions",
        "Review agent changes across projects"
      ]
    },
    "alternatives": [
      "cc-connect",
      "reason-network"
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
      "license_sha256": "ff1b611f80580d49f4b97e93a97b24eb050b0671b26b8afe16341fab699112f3",
      "source_url": "https://github.com/stablyai/orca/blob/409ce31fb483c4c24989a22c10d0bc2b32211c63/LICENSE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "409ce31fb483c4c24989a22c10d0bc2b32211c63"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-15T10:45:45Z",
        "reviewed_at": "2026-11-15T11:03:50.120930Z",
        "url": "https://github.com/stablyai/orca/commit/506d116ee3db9f4bf63e206d069b52e30e755b3c",
        "qualifies": true,
        "reason": {
          "zh-CN": "把服务器配置读写移出主线程。已核对提交中的实现文件与差异；未运行上游测试。",
          "en": "Moves saved-server reads and writes off the main thread. Reviewed implementation changes; upstream tests were not run."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/stablyai/orca",
        "accessed_at": "2026-11-15T10:48:17.008Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/stablyai/orca/blob/main/README.md",
        "accessed_at": "2026-11-15T10:54:02.303Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      },
      {
        "url": "https://github.com/stablyai/orca/blob/409ce31fb483c4c24989a22c10d0bc2b32211c63/LICENSE",
        "accessed_at": "2026-11-15T10:53:10.953Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "023",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "104af1fb90d01d6eeb3ae33e6f2df11c2955dabc854961f2bce14513df7299da",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "tool",
      "pending_reasons": [],
      "english_scope": "editorial_digest",
      "source_card_preserved": true
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDORpCz1g",
    "full_name": "stablyai/orca",
    "stargazers_count": 125338,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "ff1b611f80580d49f4b97e93a97b24eb050b0671b26b8afe16341fab699112f3",
    "last_success_at": "2026-11-15T10:48:17.008Z"
  }
}
```

</details>
