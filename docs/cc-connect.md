# cc-connect

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[chenhg5/cc-connect](https://github.com/chenhg5/cc-connect)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 自动化 / Automation |
| 状态 / Status | 已收录 / Included |
| Star | 16376 |
| 许可证 / License | 待复核 / Review needed |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T10:48:13.241Z |




历史资格见[收录依据](#review-evidence)中的 `eligibility_history`。 / Earlier decisions are retained in `eligibility_history` in the [review evidence](#review-evidence).

## 中文

### 当前收录状态

2026-11-17 按用户要求转为正式收录。本次是目录状态迁移，未重新核实全部新准入条件。原有 Star、活动与功能记录保留原核对日期，许可不再决定收录状态。

### 先前介绍与复核记录（历史）

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

当前 README 自称 MIT，但仓库根目录未找到许可证文件，API 许可证为空。原卡的 MIT 描述保留为历史记录。

### 原始中文记录（历史快照）

### 005 cc-connect

仓库：[chenhg5/cc-connect](https://github.com/chenhg5/cc-connect)

#### 1. 简介

把本机编程智能体接入聊天平台，包括飞书和钉钉。从聊天端管理会话、切换模型、安排任务及传递文件。

#### 2. 适用场景

从手机远程使用本机编程助手。通过飞书或钉钉触发自动化任务。管理多个项目与智能体会话。

#### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 连接本地编程智能体 | 把本机 Claude Code、Codex、Cursor Agent 等智能体接入聊天平台，也支持符合 ACP 的智能体。 | Why cc-connect? / Universal Agent Support |
| 接入聊天平台 | 支持飞书、钉钉、Telegram、Slack、Discord 等；README 的矩阵分别列出文字、附件和语音差异。 | Platform feature snapshot / Platform Flexibility |
| 聊天端会话与模型控制 | 提供会话管理、模型与推理等级切换、权限模式选择和工作目录切换。 | Complete Chat Control / Session Management |
| 多项目和机器人协作 | 一个进程可以绑定多个项目与平台；Multi-Bot Relay 允许群聊中的机器人相互转发。 | Multi-Agent Orchestration / Multi-Project Architecture |
| 定时任务 | 可通过自然语言或相关命令安排 cron 类任务。 | Intelligent Scheduling / Scheduled Tasks |
| 图片、语音与文件传递 | 按平台能力转发图片或语音，并允许智能体回传文件；语音转写和合成需相应服务配置。 | Multimodal Support / Agent Attachment Send-Back |
| 操作系统用户隔离 | run_as_user 选项可把项目绑定到指定系统用户运行。 | OS-User Isolation (`run_as_user`) |

官方来源入口：[官方 README](https://github.com/chenhg5/cc-connect/blob/main/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

**平台与环境**

- 可运行 Go 发行二进制的本机环境
- 飞书、钉钉、Slack、Telegram、Discord、企业微信等聊天平台，能力各有差异

- 代码采用 MIT，可自行部署桥接进程。
- 不提供模型额度；所接入智能体的订阅或 API、语音服务等按提供方计费。
- 聊天平台的机器人配置、服务限制和可用性另行确认。

- 智能体 CLI 必须先安装和认证。
- 多数平台无需公网 IP，不能推广到所有连接模式。
- 语音、群聊和附件支持以 README 平台矩阵为准。
- 本次没有配置平台、运行任务或发送消息。

**容易找错的需求（不属于本项目能力）**

- 不是独立大模型或可免费无限调用 AI 的服务。
- 不是自带完整桌面 IDE 的 Orca 类工作台。

#### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/chenhg5/cc-connect/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- 聊天机器人
- 本地 Web 配置界面
- cc-connect CLI
- ACP 智能体连接

#### 6. 替代选择

- [KKKKhazix/agent-autoloop](agent-autoloop.md#中文)：本项目侧重从聊天平台操作本机助手；后者侧重事件触发、后台排队和人工回答后的继续执行。

#### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/chenhg5/cc-connect/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/005_chenhg5-cc-connect.md`。

## English

### Current catalog status

Promoted to an included entry on 2026-11-17 at the user’s request. This is a catalog transition, not a new verification of every admission criterion. Stars, activity and feature records retain their original review dates; licensing no longer determines admission.

### Earlier description and review (historical)

A bridge between locally installed coding agents and chat platforms, with session controls, files and scheduled tasks.

### Use cases

- Operate a coding agent from team chat
- Route messages and attachments into existing agent sessions

### Requirements and limits

Agents must already be installed and authenticated. Bot setup and voice, group-chat and attachment support vary by platform. Model and chat services have separate terms and costs. The current README says MIT, but no root license file was found and GitHub reports no license; license evidence remains incomplete.

### Getting started

Read the [official documentation](https://github.com/chenhg5/cc-connect/blob/main/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [Agent Autoloop](agent-autoloop.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:13.241Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

The README claims MIT, but no root license file was found and the API license is empty. The original MIT claim is historical.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

保留原始核对数据，便于追溯来源、许可和维护证据。 / Original review data preserves source, license and maintenance evidence.

```json
{
  "evaluated_at": "2026-11-15T11:54:08.129868Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "admission_basis": "user_directed_transition",
    "policy_id": "ai-activity-stars-2026-11-17",
    "admitted_at": "2026-11-17T13:33:30.547820+00:00"
  },
  "metadata": {
    "schema_version": 1,
    "id": "cc-connect",
    "name": "cc-connect",
    "repository": "chenhg5/cc-connect",
    "repo_node_id": "R_kgDORa0x3w",
    "category": "automation",
    "tags": [
      "chat",
      "agents",
      "integration"
    ],
    "forms": [
      "cli",
      "service"
    ],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "cc-connect"
      ],
      "en": [
        "cc-connect"
      ]
    },
    "summary": {
      "zh-CN": "把本机编程智能体接入聊天平台，包括飞书和钉钉。从聊天端管理会话、切换模型、安排任务及传递文件。",
      "en": "A bridge between locally installed coding agents and chat platforms, with session controls, files and scheduled tasks."
    },
    "use_cases": {
      "zh-CN": [
        "从手机远程使用本机编程助手。通过飞书或钉钉触发自动化任务。管理多个项目与智能体会话。"
      ],
      "en": [
        "Operate a coding agent from team chat",
        "Route messages and attachments into existing agent sessions"
      ]
    },
    "alternatives": [
      "agent-autoloop"
    ],
    "editorial": {
      "status": "draft",
      "reviewed_at": {
        "zh-CN": "2026-11-15T11:03:50.120930Z",
        "en": "2026-11-15T11:03:50.120930Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": null,
      "osi_approved": false,
      "license_sha256": null,
      "source_url": null,
      "reviewed_at": null,
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "unavailable"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-15T02:05:42Z",
        "reviewed_at": "2026-11-15T11:03:50.120930Z",
        "url": "https://github.com/chenhg5/cc-connect/commit/0df18338c4838bff28f726fa4f28d4f7defdfa6a",
        "qualifies": true,
        "reason": {
          "zh-CN": "补充飞书工具调用详情汇总。已核对提交中的实现文件与差异；未运行上游测试。",
          "en": "Adds summaries of tool-call details for Feishu. Reviewed implementation changes; upstream tests were not run."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/chenhg5/cc-connect",
        "accessed_at": "2026-11-15T10:48:13.241Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/chenhg5/cc-connect/blob/main/README.md",
        "accessed_at": "2026-11-15T10:53:59.233Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "005",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "d635b6a2816e489d2d11199ac5e921ff4476356c6ea340ce00236b5770856bf4",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "tool",
      "pending_reasons": [
        "license_review_pending"
      ],
      "english_scope": "editorial_digest",
      "source_card_preserved": true,
      "notes": {
        "zh-CN": "当前 README 自称 MIT，但仓库根目录未找到许可证文件，API 许可证为空。原卡的 MIT 描述保留为历史记录。",
        "en": "The README claims MIT, but no root license file was found and the API license is empty. The original MIT claim is historical."
      },
      "historical": true
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDORa0x3w",
    "full_name": "chenhg5/cc-connect",
    "stargazers_count": 16376,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": null,
    "license_sha256": null,
    "last_success_at": "2026-11-15T10:48:13.241Z"
  },
  "eligibility_history": [
    {
      "evaluated_at": "2026-11-15T11:54:08.129868Z",
      "status": "unknown",
      "reasons": [
        "license_needs_review"
      ]
    },
    {
      "status": "unknown",
      "reasons": [
        "license_needs_review"
      ],
      "evaluated_at": "2026-11-15T11:54:08.129868Z",
      "superseded_at": "2026-11-17T13:33:30.547820+00:00",
      "superseded_by": "user_directed_transition_2026_11_17",
      "pending_actions": {
        "zh-CN": [
          "取得许可原文并核对适用范围。"
        ],
        "en": [
          "Obtain the license text and confirm its scope."
        ]
      },
      "reviewed_at": "2026-11-17T03:11:46.178386+00:00",
      "review_basis": "existing_evidence_status_clarification"
    }
  ]
}
```

</details>
