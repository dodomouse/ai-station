# Marketing Skills

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 60867 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T06:06:21.886126+00:00 |

## 中文

为 AI 智能体提供营销任务技能，围绕产品定位组织文案、SEO、转化分析、外联和增长工作流。

### 用途与功能

- 用共享产品营销上下文衔接不同技能，覆盖内容制作、渠道规划、分析和销售支持。
- cold-email 技能指导 B2B 邮件草拟、跟进和回复处理；directory-submissions 提供目录筛选、材料准备和提交记录流程。
- 附带工具接入指南和部分 Node.js CLI，可按需连接分析、广告或其他营销账户。

### 环境与限制

需要支持 Agent Skills 的智能体；纯文案任务可直接使用提示词，仓库 CLI 需要 Node.js 18+，MCP 连接需宿主支持和独立授权。安装技能不会自动开通账户、配置凭据或提供服务额度。外联、表单提交、发布和付费服务应按授权范围执行；内容与投放结果需实际验证，不保证送达率、转化率或增长收益。

### 开始使用

按 README 安装所需营销技能，先建立产品、目标客户和定位上下文，再选择文案、SEO 或外联任务。若需要账户数据，按 tools/SETUP.md 仅连接所需服务并从小范围只读请求验证。

参阅[官方 README](https://github.com/coreyhaines31/marketingskills/blob/1f837447b20bb6f0e72d87b80ece1c221c362c7d/README.md)。

### 收录与来源

把营销指令和工具接入步骤组织成可复用流程，适合由智能体辅助准备和执行营销工作。已读冷邮件技能、工具接入约束及目录表单工作流补丁，未发送消息、提交表单或调用营销账户。

维护证据：[目录提交技能增加浏览器表单流程，按 API、CLI/PR、网页表单选择路径，要求逐项映射字段、核对完成表单、保存确认记录，并将登录和验证码交给用户](https://github.com/coreyhaines31/marketingskills/commit/310ebb96a9cb185de6648fcbb2b4f01844f41a38)（2026-11-11）。

仓库来自用户于 2026-11-17 提供的办公技能 PDF，已另行核对上游。本条按工程通用标准复核，不设 Star 门槛。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Provides marketing skills for AI agents, organizing copywriting, SEO, conversion analysis, outreach and growth workflows around product positioning.

### Uses and features

- Uses shared product-marketing context across content creation, channel planning, analytics and sales-support skills.
- The cold-email skill guides B2B drafting, follow-ups and reply handling; directory-submissions covers directory selection, listing materials and submission logs.
- Includes tool-connection guides and some Node.js CLIs for optional analytics, advertising and other marketing accounts.

### Requirements and limits

Requires an Agent Skills-compatible host. Text tasks can use the instructions directly; repository CLIs require Node.js 18+, while MCP connections need host support and separate authorization. Installing skills does not provision accounts, credentials or service quota. Outreach, form submissions, publishing and paid services must stay within authorized scope; delivery, conversion and growth outcomes require measurement and are not guaranteed.

### Getting started

Install the required skills following the README, establish product, audience and positioning context, then choose a copywriting, SEO or outreach task. For account data, follow tools/SETUP.md to connect only the required service and begin with a small read-only request.

See the [official README](https://github.com/coreyhaines31/marketingskills/blob/1f837447b20bb6f0e72d87b80ece1c221c362c7d/README.md).

### Review and provenance

Organizes marketing guidance and tool connections into reusable workflows for agent-assisted preparation and execution. Cold-email guidance, connection boundaries and the directory-form workflow patch were reviewed; no messages, forms or marketing-account calls were made.

Maintenance evidence: [Adds a browser-form workflow to directory submissions, choosing among API, CLI/PR and web forms, mapping visible fields, reviewing completed forms, logging confirmations and handing login/CAPTCHA steps to the user](https://github.com/coreyhaines31/marketingskills/commit/310ebb96a9cb185de6648fcbb2b4f01844f41a38) (2026-11-11).

Identified in an office-skills PDF supplied by the user on 2026-11-17, independently checked against upstream sources and reviewed against the general catalog criteria, with no star threshold.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T06:06:21.886126+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "marketingskills",
    "name": "Marketing Skills",
    "repository": "coreyhaines31/marketingskills",
    "repo_node_id": "R_kgDOQ6n2Jw",
    "category": "productivity",
    "summary": {
      "zh-CN": "为 AI 智能体提供营销任务技能，围绕产品定位组织文案、SEO、转化分析、外联和增长工作流。",
      "en": "Provides marketing skills for AI agents, organizing copywriting, SEO, conversion analysis, outreach and growth workflows around product positioning."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T06:06:21.886126+00:00",
        "en": "2026-11-17T06:06:21.886126+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "把营销指令和工具接入步骤组织成可复用流程，适合由智能体辅助准备和执行营销工作。已读冷邮件技能、工具接入约束及目录表单工作流补丁，未发送消息、提交表单或调用营销账户。",
      "en": "Organizes marketing guidance and tool connections into reusable workflows for agent-assisted preparation and execution. Cold-email guidance, connection boundaries and the directory-form workflow patch were reviewed; no messages, forms or marketing-account calls were made.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/coreyhaines31/marketingskills/blob/1f837447b20bb6f0e72d87b80ece1c221c362c7d/LICENSE",
      "license_sha256": "b70d71e24e40fce5da8f4b6f9cd862096a048e433db7f3c8cac5e348e6d34591",
      "source_commit": "1f837447b20bb6f0e72d87b80ece1c221c362c7d",
      "reviewed_at": "2026-11-17T06:06:21.886126+00:00",
      "evidence_pinned_at": "2026-11-17T06:06:21.886126+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "MIT covers the repository-authored skills, reference files and CLI code under the pinned root LICENSE. External integrations, MCP servers, data providers, platforms, linked commercial training and supplied customer/prospect data retain their own terms.",
      "files": [
        {
          "spdx": "MIT",
          "osi_approved": true,
          "source_url": "https://github.com/coreyhaines31/marketingskills/blob/1f837447b20bb6f0e72d87b80ece1c221c362c7d/LICENSE",
          "license_sha256": "b70d71e24e40fce5da8f4b6f9cd862096a048e433db7f3c8cac5e348e6d34591",
          "source_commit": "1f837447b20bb6f0e72d87b80ece1c221c362c7d",
          "reviewed_at": "2026-11-17T05:54:50.206488+00:00",
          "evidence_pinned_at": "2026-11-17T05:54:50.206488+00:00",
          "evidence_status": "hash_matched",
          "scope": "MIT covers the repository-authored skills, reference files and CLI code under the pinned root LICENSE. External integrations, MCP servers, data providers, platforms, linked commercial training and supplied customer/prospect data retain their own terms."
        }
      ]
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-11T17:42:55Z",
        "reviewed_at": "2026-11-17T06:06:21.886126+00:00",
        "url": "https://github.com/coreyhaines31/marketingskills/commit/310ebb96a9cb185de6648fcbb2b4f01844f41a38",
        "qualifies": true,
        "reason": {
          "zh-CN": "目录提交技能增加浏览器表单流程，按 API、CLI/PR、网页表单选择路径，要求逐项映射字段、核对完成表单、保存确认记录，并将登录和验证码交给用户",
          "en": "Adds a browser-form workflow to directory submissions, choosing among API, CLI/PR and web forms, mapping visible fields, reviewing completed forms, logging confirmations and handing login/CAPTCHA steps to the user"
        },
        "reviewed_files": [
          "skills/directory-submissions/SKILL.md"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/coreyhaines31/marketingskills",
        "accessed_at": "2026-11-17T06:06:21.886126+00:00"
      },
      {
        "url": "https://github.com/coreyhaines31/marketingskills/blob/1f837447b20bb6f0e72d87b80ece1c221c362c7d/README.md",
        "accessed_at": "2026-11-17T06:06:21.886126+00:00"
      },
      {
        "url": "https://github.com/coreyhaines31/marketingskills/blob/1f837447b20bb6f0e72d87b80ece1c221c362c7d/LICENSE",
        "accessed_at": "2026-11-17T06:06:21.886126+00:00"
      },
      {
        "url": "https://github.com/coreyhaines31/marketingskills/commit/310ebb96a9cb185de6648fcbb2b4f01844f41a38",
        "accessed_at": "2026-11-17T06:06:21.886126+00:00"
      },
      {
        "url": "https://github.com/coreyhaines31/marketingskills/blob/1f837447b20bb6f0e72d87b80ece1c221c362c7d/skills/cold-email/SKILL.md",
        "accessed_at": "2026-11-17T06:06:21.886126+00:00"
      },
      {
        "url": "https://github.com/coreyhaines31/marketingskills/blob/1f837447b20bb6f0e72d87b80ece1c221c362c7d/tools/SETUP.md",
        "accessed_at": "2026-11-17T06:06:21.886126+00:00"
      },
      {
        "url": "https://github.com/coreyhaines31/marketingskills/blob/1f837447b20bb6f0e72d87b80ece1c221c362c7d/skills/directory-submissions/SKILL.md",
        "accessed_at": "2026-11-17T06:06:21.886126+00:00"
      }
    ],
    "discovery": {
      "kind": "user_pdf",
      "submitted_date": "2026-11-17",
      "source_url": "https://github.com/coreyhaines31/marketingskills",
      "repository_url": "https://github.com/coreyhaines31/marketingskills",
      "source_title": "办公室 Skill 从夯到拉(纯主观)",
      "source_pages": [
        7
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOQ6n2Jw",
    "full_name": "coreyhaines31/marketingskills",
    "stargazers_count": 60867,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "api_license_spdx": "MIT",
    "license_sha256": "b70d71e24e40fce5da8f4b6f9cd862096a048e433db7f3c8cac5e348e6d34591",
    "last_success_at": "2026-11-17T05:46:00.549291+00:00"
  }
}
```

</details>
