# Prosyo GTM Skills

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[prosyo-ai/gtm-skill](https://github.com/prosyo-ai/gtm-skill)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 12 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T06:06:21.891612+00:00 |

## 中文

面向 AI 助手的营销与销售技能集，提供客户研究、开发信起草、跟进、邮件送达率检查和客户访谈流程。

### 用途与功能

- 按业务任务组织 SKILL.md 和参考模板，可供 Claude、Codex 等支持 Agent Skills 的助手使用。
- cold-email-writer 根据客户背景、单一问题和经认可的证据生成三组简短邮件及主题行，明确禁止虚构个性化信息。
- 全局规则要求个性化信息有来源，实际发送和批量修改前展示具体动作并获得用户确认；另有访谈提纲与转写材料归纳流程。

### 环境与限制

需要支持 Agent Skills 或 Claude Code 插件的 AI 助手。技能主要是工作指令与模板，本身不提供邮箱、CRM、联系人数据库或模型；需要真实数据时须另行连接相应工具并提供访问权限。助手/模型与外部服务可能收费。先加载 gtm-global-rules 并配置公司信息、已批准的事实、发送限制和审批人。这些约束由助手遵循，不是独立的强制权限网关，也不能保证营销效果或替代地区规则复核。

### 开始使用

按官方 README 安装技能集，先选择 gtm-global-rules，再安装 cold-email-writer 等所需技能。提供目标客户或细分群体、产品价值与可引用证据，请助手起草三种邮件方案并人工复核；不要把安装技能等同于已连接邮箱或已获准发送。

参阅[官方 README](https://github.com/prosyo-ai/gtm-skill/blob/db157476d0eaf40683d3a0c1e906702900206182/README.md)。

### 收录与来源

具体价值在于把营销与销售任务拆成可检查的输入、步骤、输出和参考模板；已核对开发信规则、全局规则及新增客户访谈技能的实际内容。适合作为 AI 助手的工作流程库，效果取决于输入事实、模型和已接工具；仓库较新，不据此声称长期维护或实际转化提升。

维护证据：[新增客户访谈技能，明确招募对象、按购买历程提问、保留原话及多次访谈主题归纳步骤](https://github.com/prosyo-ai/gtm-skill/commit/d211fb8a0c64de36bdd0b2699062cf5f15d44813)（2026-10-23）。

仓库来自用户于 2026-11-17 提供的办公技能 PDF，已另行核对上游。本条按工程通用标准复核，不设 Star 门槛。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

A marketing and sales skill collection for AI assistants, covering customer research, cold-email drafting, follow-ups, deliverability checks and customer interviews.

### Uses and features

- Task-specific SKILL.md files and reference templates work with Claude, Codex and other Agent Skills-compatible assistants.
- cold-email-writer uses prospect context, one problem and approved proof to draft three short variants and subject lines, with explicit rules against invented personalization.
- Global instructions require sources for personalized claims and user approval of concrete sends or bulk changes; customer-interview guides also cover interview planning and transcript synthesis.

### Requirements and limits

An Agent Skills-compatible assistant or Claude Code plugin host is required. These are instructions and templates, not a mailbox, CRM, contact database or model; live-data tasks require separately connected tools and permissions. Assistant/model access and external services may incur fees. Load gtm-global-rules first and configure company details, approved claims, sending limits and the approver. These are agent instructions rather than an independently enforced permission gateway, and do not guarantee marketing outcomes or replace review of applicable local rules.

### Getting started

Follow the official README to install gtm-global-rules first, then selected skills such as cold-email-writer. Supply the prospect or segment, offer and approved proof, ask for three draft variants, and review them. Installing a skill does not connect a mailbox or authorize sending.

See the [official README](https://github.com/prosyo-ai/gtm-skill/blob/db157476d0eaf40683d3a0c1e906702900206182/README.md).

### Review and provenance

Its concrete value is a collection of inspectable task inputs, steps, outputs and reference templates. This review checked the cold-email and global rules and the substantive addition of a customer-interview skill. It serves as an AI assistant workflow library; results depend on supplied facts, the model and connected tools. The repository is new, so this review does not claim a long maintenance record or demonstrated conversion gains.

Maintenance evidence: [Adds a customer-interview skill defining participant recruitment, buying-story questions, quote capture and synthesis across interviews](https://github.com/prosyo-ai/gtm-skill/commit/d211fb8a0c64de36bdd0b2699062cf5f15d44813) (2026-10-23).

Identified in an office-skills PDF supplied by the user on 2026-11-17, independently checked against upstream sources and reviewed against the general catalog criteria, with no star threshold.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T06:06:21.891612+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "gtm-skill",
    "name": "Prosyo GTM Skills",
    "repository": "prosyo-ai/gtm-skill",
    "repo_node_id": "R_kgDOVT8RUg",
    "category": "productivity",
    "summary": {
      "zh-CN": "面向 AI 助手的营销与销售技能集，提供客户研究、开发信起草、跟进、邮件送达率检查和客户访谈流程。",
      "en": "A marketing and sales skill collection for AI assistants, covering customer research, cold-email drafting, follow-ups, deliverability checks and customer interviews."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T06:06:21.891612+00:00",
        "en": "2026-11-17T06:06:21.891612+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "具体价值在于把营销与销售任务拆成可检查的输入、步骤、输出和参考模板；已核对开发信规则、全局规则及新增客户访谈技能的实际内容。适合作为 AI 助手的工作流程库，效果取决于输入事实、模型和已接工具；仓库较新，不据此声称长期维护或实际转化提升。",
      "en": "Its concrete value is a collection of inspectable task inputs, steps, outputs and reference templates. This review checked the cold-email and global rules and the substantive addition of a customer-interview skill. It serves as an AI assistant workflow library; results depend on supplied facts, the model and connected tools. The repository is new, so this review does not claim a long maintenance record or demonstrated conversion gains.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/prosyo-ai/gtm-skill/blob/db157476d0eaf40683d3a0c1e906702900206182/LICENSE",
      "license_sha256": "7bfcbd3ab4f73f94110eaa2882a4159d3d6819ec6bd2caeb5443c0d4d4a1e5bf",
      "source_commit": "db157476d0eaf40683d3a0c1e906702900206182",
      "reviewed_at": "2026-11-17T06:06:21.891612+00:00",
      "evidence_pinned_at": "2026-11-17T06:06:21.891612+00:00",
      "evidence_status": "hash_matched",
      "scope_note": {
        "zh-CN": "根 LICENSE 为 MIT，覆盖仓库技能与工具源码；每个技能保留作者归属。该许可不覆盖使用者的客户数据、模型服务或外部工具条款。",
        "en": "The root MIT LICENSE covers repository skills and tool source, with skill-author attribution retained. It does not cover users’ customer data, model services or external-tool terms."
      }
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-10-23T09:52:35Z",
        "reviewed_at": "2026-11-17T06:06:21.891612+00:00",
        "url": "https://github.com/prosyo-ai/gtm-skill/commit/d211fb8a0c64de36bdd0b2699062cf5f15d44813",
        "qualifies": true,
        "reason": {
          "zh-CN": "新增客户访谈技能，明确招募对象、按购买历程提问、保留原话及多次访谈主题归纳步骤",
          "en": "Adds a customer-interview skill defining participant recruitment, buying-story questions, quote capture and synthesis across interviews"
        },
        "reviewed_files": [
          "skills/customer-interview-guide/SKILL.md"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/prosyo-ai/gtm-skill",
        "accessed_at": "2026-11-17T06:06:21.891612+00:00"
      },
      {
        "url": "https://github.com/prosyo-ai/gtm-skill/blob/db157476d0eaf40683d3a0c1e906702900206182/README.md",
        "accessed_at": "2026-11-17T06:06:21.891612+00:00"
      },
      {
        "url": "https://github.com/prosyo-ai/gtm-skill/blob/db157476d0eaf40683d3a0c1e906702900206182/LICENSE",
        "accessed_at": "2026-11-17T06:06:21.891612+00:00"
      },
      {
        "url": "https://github.com/prosyo-ai/gtm-skill/commit/d211fb8a0c64de36bdd0b2699062cf5f15d44813",
        "accessed_at": "2026-11-17T06:06:21.891612+00:00"
      },
      {
        "url": "https://github.com/prosyo-ai/gtm-skill/blob/db157476d0eaf40683d3a0c1e906702900206182/skills/gtm-global-rules/SKILL.md",
        "accessed_at": "2026-11-17T06:06:21.891612+00:00"
      },
      {
        "url": "https://github.com/prosyo-ai/gtm-skill/blob/db157476d0eaf40683d3a0c1e906702900206182/skills/cold-email-writer/SKILL.md",
        "accessed_at": "2026-11-17T06:06:21.891612+00:00"
      }
    ],
    "discovery": {
      "kind": "user_pdf",
      "submitted_date": "2026-11-17",
      "source_url": "https://github.com/prosyo-ai/gtm-skill",
      "repository_url": "https://github.com/prosyo-ai/gtm-skill",
      "source_title": "办公室 Skill 从夯到拉(纯主观)",
      "source_pages": [
        7
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVT8RUg",
    "full_name": "prosyo-ai/gtm-skill",
    "stargazers_count": 12,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "api_license_spdx": "MIT",
    "license_sha256": "7bfcbd3ab4f73f94110eaa2882a4159d3d6819ec6bd2caeb5443c0d4d4a1e5bf",
    "last_success_at": "2026-11-17T05:46:39.314464+00:00"
  }
}
```

</details>
