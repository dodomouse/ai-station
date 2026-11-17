# dsh-superagent 研究原型

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[deepseek-ai/dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 23202 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T10:48:14.655Z |

以上为历史核对结果，使用前请复核上游状态。 / This is a dated review; check the current upstream state before use.

## 中文

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

### 原始中文记录（历史快照）

### 010 dsh-superagent 研究原型

仓库：[deepseek-ai/dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype)

#### 1. 简介

面向单个 GitHub 仓库的主动编码智能体研究原型。监听 GitHub 和可选飞书消息，按授权创建并执行工作项。

#### 2. 适用场景

研究团队编码智能体的授权模型。了解消息触发的 GitHub 工作项流程。参考智能体执行与人工面板设计。

#### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 单仓库消息入口 | 面向一个 GitHub 仓库监听请求，并可选接入飞书。 | dsh-superagent 项目简介 |
| 授权触发 | 仅在允许的人员提出工作或团队规则允许时行动。 | 工作原则 / docs/000-philosophy.md入口 |
| 工作项与隔离执行 | 接到工作后创建工作项，在各自智能体会话与目录中处理。 | dsh-superagent 项目简介 |
| 回到原会话交付 | 在请求的原对话中回应，README举例为提交拉取请求。 | dsh-superagent 项目简介 |
| 人工面板 | Web面板集中展示哪些事项需要人处理。 | dsh-superagent 项目简介 / Documentation |

官方来源入口：[官方 README](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/main/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

**平台与环境**

- 以DeepSeek Harness部署环境为前提；README未明确操作系统兼容矩阵

- 代码采用MIT；部署、模型服务与其他所接平台成本另计。
- 研究原型不附送DeepSeek或其他模型额度。

- README明确：研究参考代码，不是DeepSeek官方产品，不是生产就绪软件。
- 部分文章设计属于未来方向，原型没有全部实现。
- 未部署、未核验授权与通知行为，不能作为上线保证。

**容易找错的需求（不属于本项目能力）**

- 直接作为多仓库、无需配置的正式团队SaaS上线。
- 已经实现相关文章里所有未来设计。

#### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- GitHub事件与会话
- 可选飞书
- Web人工面板
- DeepSeek Harness bundle

#### 6. 替代选择

- [KKKKhazix/agent-autoloop](agent-autoloop.md#中文)：本项目是围绕单个 GitHub 仓库的主动编码研究原型；后者提供本地事件调度及后台任务跟进。

#### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/010_deepseek-ai-dsh-superagent-prototype.md`。

## English

Research code for an agent that monitors one GitHub repository and optionally Feishu, then works on authorized tasks.

### Use cases

- Study event-driven agent workflows
- Explore GitHub-based task handling

### Requirements and limits

Requires the DeepSeek Harness environment and configured services. It is research reference code, not an official production product. Some ideas discussed in related articles are future directions. Model usage and hosting are separate costs; deployment and authorization behavior were not tested.

### Getting started

Read the [official documentation](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/main/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [Agent Autoloop](agent-autoloop.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:14.655Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

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
    "id": "dsh-superagent-prototype",
    "name": "dsh-superagent 研究原型",
    "repository": "deepseek-ai/dsh-superagent-prototype",
    "repo_node_id": "R_kgDOVd9sjw",
    "category": "ai",
    "tags": [
      "agents",
      "research",
      "github"
    ],
    "forms": [
      "service"
    ],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "dsh-superagent 研究原型"
      ],
      "en": [
        "DSH Superagent Prototype"
      ]
    },
    "summary": {
      "zh-CN": "面向单个 GitHub 仓库的主动编码智能体研究原型。监听 GitHub 和可选飞书消息，按授权创建并执行工作项。",
      "en": "Research code for an agent that monitors one GitHub repository and optionally Feishu, then works on authorized tasks."
    },
    "use_cases": {
      "zh-CN": [
        "研究团队编码智能体的授权模型。了解消息触发的 GitHub 工作项流程。参考智能体执行与人工面板设计。"
      ],
      "en": [
        "Study event-driven agent workflows",
        "Explore GitHub-based task handling"
      ]
    },
    "alternatives": [
      "agent-autoloop"
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
      "license_sha256": "6d66f91815b720e18cfb2b3552043a0359236aec9a1a6917787900546f6ce550",
      "source_url": "https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/LICENSE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "8c32a9dc5d72c033816c6a8110b37f40cf94fba4"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-10-31T12:06:31Z",
        "reviewed_at": "2026-11-15T11:03:50.120930Z",
        "url": "https://github.com/deepseek-ai/dsh-superagent-prototype/commit/8c32a9dc5d72c033816c6a8110b37f40cf94fba4",
        "qualifies": true,
        "reason": {
          "zh-CN": "新增研究原型的服务、任务处理及执行代码。已核对提交中的实现文件与差异；未运行上游测试。",
          "en": "Introduces the prototype service and task execution code. Reviewed implementation changes; upstream tests were not run."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/deepseek-ai/dsh-superagent-prototype",
        "accessed_at": "2026-11-15T10:48:14.655Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/deepseek-ai/dsh-superagent-prototype/blob/main/README.md",
        "accessed_at": "2026-11-15T10:53:59.972Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      },
      {
        "url": "https://github.com/deepseek-ai/dsh-superagent-prototype/blob/8c32a9dc5d72c033816c6a8110b37f40cf94fba4/LICENSE",
        "accessed_at": "2026-11-15T10:53:08.329Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "010",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "71f7732b199a1e09cd81829e4382981dc1e1a0886b7dcd78a2881bfe2afcbd5f",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "tool",
      "pending_reasons": [],
      "english_scope": "editorial_digest",
      "source_card_preserved": true
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVd9sjw",
    "full_name": "deepseek-ai/dsh-superagent-prototype",
    "stargazers_count": 23202,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "6d66f91815b720e18cfb2b3552043a0359236aec9a1a6917787900546f6ce550",
    "last_success_at": "2026-11-15T10:48:14.655Z"
  }
}
```

</details>
