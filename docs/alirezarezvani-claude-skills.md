# Claude Skills by Alireza Rezvani

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 29928 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T06:06:21.883381+00:00 |

## 中文

为 AI 智能体提供跨工程、产品、营销、财务和合规领域的技能、角色指令及辅助脚本。

### 用途与功能

- 按专业领域组合技能、角色和工作流，支持多种编程智能体的安装方式。
- 财务技能读取结构化财务数据，辅助比率分析、DCF 估值、预算差异与滚动预测；不等同于完整会计系统。
- 国际化技能检查缺失翻译键、占位符和复数形式，并生成伪本地化文件；其检查脚本不调用翻译服务。

### 环境与限制

需要支持技能的 AI 智能体；已核对的财务和国际化脚本使用 Python 标准库，其他任务仍需各自工具与数据。宿主模型、外部连接和服务额度另行配置。财务和合规输出依赖输入、假设及规则适用范围，不能作为准确性或合规保证；本地脚本不代表宿主模型不会外发资料。

### 开始使用

按 README 安装所需领域插件或技能，不必一次安装全部。先准备脱敏输入，阅读选中技能的输入格式，再用示例核对脚本结果和模型解释。

参阅[官方 README](https://github.com/alirezarezvani/claude-skills/blob/4680893d91f2aee6f77ca1519fd1b86b7a104c87/README.md)。

### 收录与来源

把领域指令与可检查脚本结合，便于为智能体配置不同工作角色。已核对财务与国际化技能及 FMEA 汇总修复；未运行上游，也未验证专业判断质量。

维护证据：[FMEA 风险改善率计算对没有修订评分的条目保留原风险优先数，不再把这些条目从修订后总量中漏掉而夸大改善率](https://github.com/alirezarezvani/claude-skills/commit/adcc2861a3fb12878d5dd13b5311913906598437)（2026-11-16）。

仓库来自用户于 2026-11-17 提供的办公技能 PDF，已另行核对上游。本条按工程通用标准复核，不设 Star 门槛。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Provides skills, role instructions and helper scripts for AI agents across engineering, product, marketing, finance and compliance.

### Uses and features

- Combines domain skills, roles and workflows with installation paths for multiple coding agents.
- Finance skills use structured financial data for ratios, DCF valuation, budget variances and rolling forecasts; they are not a full accounting system.
- Internationalization skills check missing keys, placeholders and plural forms, and generate pseudo-locales; their checking scripts do not call translation services.

### Requirements and limits

Requires a skill-capable AI agent. The reviewed finance and localization scripts use the Python standard library; other tasks still need their own tools and data. Configure the host model, external connections and service quota separately. Financial and compliance outputs depend on inputs, assumptions and applicable rules, without an accuracy or compliance guarantee. Local scripts do not imply the host model keeps all data local.

### Getting started

Follow the README to install the required domain plugin or skills rather than the entire collection. Prepare sanitized inputs, read the selected skill’s input schema and check script results and model explanations against examples.

See the [official README](https://github.com/alirezarezvani/claude-skills/blob/4680893d91f2aee6f77ca1519fd1b86b7a104c87/README.md).

### Review and provenance

Combines domain instructions with inspectable scripts to configure agents for different roles. Finance/localization skills and an FMEA summary fix were reviewed; upstream software and professional-judgment quality were not tested.

Maintenance evidence: [Keeps original risk-priority numbers for FMEA entries without revised scores when computing improvement, avoiding an inflated improvement rate from omitting those entries](https://github.com/alirezarezvani/claude-skills/commit/adcc2861a3fb12878d5dd13b5311913906598437) (2026-11-16).

Identified in an office-skills PDF supplied by the user on 2026-11-17, independently checked against upstream sources and reviewed against the general catalog criteria, with no star threshold.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T06:06:21.883381+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "alirezarezvani-claude-skills",
    "name": "Claude Skills by Alireza Rezvani",
    "repository": "alirezarezvani/claude-skills",
    "repo_node_id": "R_kgDOQFGGXQ",
    "category": "ai",
    "summary": {
      "zh-CN": "为 AI 智能体提供跨工程、产品、营销、财务和合规领域的技能、角色指令及辅助脚本。",
      "en": "Provides skills, role instructions and helper scripts for AI agents across engineering, product, marketing, finance and compliance."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T06:06:21.883381+00:00",
        "en": "2026-11-17T06:06:21.883381+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "把领域指令与可检查脚本结合，便于为智能体配置不同工作角色。已核对财务与国际化技能及 FMEA 汇总修复；未运行上游，也未验证专业判断质量。",
      "en": "Combines domain instructions with inspectable scripts to configure agents for different roles. Finance/localization skills and an FMEA summary fix were reviewed; upstream software and professional-judgment quality were not tested.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/alirezarezvani/claude-skills/blob/4680893d91f2aee6f77ca1519fd1b86b7a104c87/LICENSE",
      "license_sha256": "a20126646f93d32a8989c3cf4772d59194f405034f7babe7daebeac22b8ab151",
      "source_commit": "4680893d91f2aee6f77ca1519fd1b86b7a104c87",
      "reviewed_at": "2026-11-17T06:06:21.883381+00:00",
      "evidence_pinned_at": "2026-11-17T06:06:21.883381+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "MIT covers the repository-authored skills, instructions and scripts under the pinned root LICENSE. External tools, imported components, reference material, models, user financial data and hosted services retain their own licenses and terms.",
      "files": [
        {
          "spdx": "MIT",
          "osi_approved": true,
          "source_url": "https://github.com/alirezarezvani/claude-skills/blob/4680893d91f2aee6f77ca1519fd1b86b7a104c87/LICENSE",
          "license_sha256": "a20126646f93d32a8989c3cf4772d59194f405034f7babe7daebeac22b8ab151",
          "source_commit": "4680893d91f2aee6f77ca1519fd1b86b7a104c87",
          "reviewed_at": "2026-11-17T05:54:50.206488+00:00",
          "evidence_pinned_at": "2026-11-17T05:54:50.206488+00:00",
          "evidence_status": "hash_matched",
          "scope": "MIT covers the repository-authored skills, instructions and scripts under the pinned root LICENSE. External tools, imported components, reference material, models, user financial data and hosted services retain their own licenses and terms."
        }
      ]
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-16T06:41:16Z",
        "reviewed_at": "2026-11-17T06:06:21.883381+00:00",
        "url": "https://github.com/alirezarezvani/claude-skills/commit/adcc2861a3fb12878d5dd13b5311913906598437",
        "qualifies": true,
        "reason": {
          "zh-CN": "FMEA 风险改善率计算对没有修订评分的条目保留原风险优先数，不再把这些条目从修订后总量中漏掉而夸大改善率",
          "en": "Keeps original risk-priority numbers for FMEA entries without revised scores when computing improvement, avoiding an inflated improvement rate from omitting those entries"
        },
        "reviewed_files": [
          "ra-qm-team/skills/risk-management-specialist/scripts/fmea_analyzer.py"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/alirezarezvani/claude-skills",
        "accessed_at": "2026-11-17T06:06:21.883381+00:00"
      },
      {
        "url": "https://github.com/alirezarezvani/claude-skills/blob/4680893d91f2aee6f77ca1519fd1b86b7a104c87/README.md",
        "accessed_at": "2026-11-17T06:06:21.883381+00:00"
      },
      {
        "url": "https://github.com/alirezarezvani/claude-skills/blob/4680893d91f2aee6f77ca1519fd1b86b7a104c87/LICENSE",
        "accessed_at": "2026-11-17T06:06:21.883381+00:00"
      },
      {
        "url": "https://github.com/alirezarezvani/claude-skills/commit/adcc2861a3fb12878d5dd13b5311913906598437",
        "accessed_at": "2026-11-17T06:06:21.883381+00:00"
      },
      {
        "url": "https://github.com/alirezarezvani/claude-skills/blob/4680893d91f2aee6f77ca1519fd1b86b7a104c87/finance/skills/financial-analyst/SKILL.md",
        "accessed_at": "2026-11-17T06:06:21.883381+00:00"
      },
      {
        "url": "https://github.com/alirezarezvani/claude-skills/blob/4680893d91f2aee6f77ca1519fd1b86b7a104c87/engineering/skills/i18n-localization/SKILL.md",
        "accessed_at": "2026-11-17T06:06:21.883381+00:00"
      }
    ],
    "discovery": {
      "kind": "user_pdf",
      "submitted_date": "2026-11-17",
      "source_url": "https://github.com/alirezarezvani/claude-skills",
      "repository_url": "https://github.com/alirezarezvani/claude-skills",
      "source_title": "办公室 Skill 从夯到拉(纯主观)",
      "source_pages": [
        4
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOQFGGXQ",
    "full_name": "alirezarezvani/claude-skills",
    "stargazers_count": 29928,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "api_license_spdx": "MIT",
    "license_sha256": "a20126646f93d32a8989c3cf4772d59194f405034f7babe7daebeac22b8ab151",
    "last_success_at": "2026-11-17T05:45:42.053396+00:00"
  }
}
```

</details>
