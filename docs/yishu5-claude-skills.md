# YiShu5 Agent Skills

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[YiShu5/claude-skills](https://github.com/YiShu5/claude-skills)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 130 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T06:06:21.889151+00:00 |

## 中文

面向中文办公与创作的 AI Agent 技能集，包含会议纪要、日报周报、页面演示、写作和公众号工作流。

### 用途与功能

- 会记成报将转写或笔记整理为纪要、个人日报和周报素材，区分建议、决定及待确认信息。
- 按任务选择中文写作、PRD、HTML 页面和演示、公众号排版与发布等独立技能。
- 提供本地经验记录和面向特定组织的品牌、培训及面聊转写导出流程。

### 环境与限制

需能读取本地 SKILL.md 的 AI Agent；各技能所用脚本、浏览器或外部服务另有依赖。会议整理接收已有转写或笔记，本身不等于录音转写服务。使用云模型时，提供的会议、文档和代码内容可能发送给该模型供应方，费用由所用服务决定。公众号发布和企业微信微盘导出需要相应账号权限；方片专用流程、目录和访问控制需按自身组织改造，不能把提示词里的保密规则当作已实施的权限系统。

### 开始使用

从 README 技能目录选择一个文件夹复制到 Agent 的技能目录并重新加载。会议场景可先选会记成报，用一份脱敏笔记生成草稿，核对负责人、日期和完成状态后再使用。

参阅[官方 README](https://github.com/YiShu5/claude-skills/blob/87caa778a9f6fe3811ee5af6d6a60a95dc334cf9/README.md)。

### 收录与来源

已核对 MIT、技能入口及 2026-10-29 的实际流程修改：面聊导出新增类型字段，并调整人事类转写的分类与导出规则。该 SKILL.md 是功能执行规范，不只是宣传文档。未测试外部账号连接或企业会议系统权限。

维护证据：[面聊导出流程增加普通/人事类的类型字段及分类要求，并调整相应导出和访问范围说明](https://github.com/YiShu5/claude-skills/commit/87caa778a9f6fe3811ee5af6d6a60a95dc334cf9)（2026-10-29）。

仓库来自用户于 2026-11-17 提供的办公技能 PDF，已另行核对上游。本条按工程通用标准复核，不设 Star 门槛。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

A collection of AI agent workflows for Chinese office work and content creation, covering meeting notes, work reports, presentations, writing and WeChat publishing.

### Uses and features

- Turn transcripts or notes into minutes, personal daily reports and weekly-report material, distinguishing suggestions, decisions and unconfirmed facts.
- Choose individual workflows for Chinese writing, PRDs, HTML pages and presentations, or WeChat formatting and publishing.
- Includes local learning records and organization-specific branding, training and conversation-transcript export workflows.

### Requirements and limits

Requires an AI agent that reads local SKILL.md files; individual workflows may need scripts, browser tools or external services. Meeting workflows consume existing transcripts or notes rather than providing audio transcription. Cloud models may receive supplied meeting, document or code content, with provider fees applying. WeChat publishing and enterprise cloud-drive export require account permissions. Adapt Fangpian-specific paths, workflows and access controls to your organization; prompt instructions do not themselves enforce an authorization system.

### Getting started

Choose one skill folder from the README, copy it to your agent’s skill directory and reload. For meetings, start with 会记成报 and sanitized notes, then verify owners, dates and completion status in the draft.

See the [official README](https://github.com/YiShu5/claude-skills/blob/87caa778a9f6fe3811ee5af6d6a60a95dc334cf9/README.md).

### Review and provenance

Reviewed MIT licensing, the meeting skill and the 2026-10-29 workflow change adding a transcript type field and revising personnel-conversation classification/export rules. The SKILL.md defines functional behavior, not just marketing documentation. External integrations and enterprise meeting-system permissions were not tested.

Maintenance evidence: [Adds conversation-type metadata and classification requirements to the transcript export workflow and revises its export/access instructions](https://github.com/YiShu5/claude-skills/commit/87caa778a9f6fe3811ee5af6d6a60a95dc334cf9) (2026-10-29).

Identified in an office-skills PDF supplied by the user on 2026-11-17, independently checked against upstream sources and reviewed against the general catalog criteria, with no star threshold.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T06:06:21.889151+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "yishu5-claude-skills",
    "name": "YiShu5 Agent Skills",
    "repository": "YiShu5/claude-skills",
    "repo_node_id": "R_kgDORoRv_A",
    "category": "productivity",
    "summary": {
      "zh-CN": "面向中文办公与创作的 AI Agent 技能集，包含会议纪要、日报周报、页面演示、写作和公众号工作流。",
      "en": "A collection of AI agent workflows for Chinese office work and content creation, covering meeting notes, work reports, presentations, writing and WeChat publishing."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T06:06:21.889151+00:00",
        "en": "2026-11-17T06:06:21.889151+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "已核对 MIT、技能入口及 2026-10-29 的实际流程修改：面聊导出新增类型字段，并调整人事类转写的分类与导出规则。该 SKILL.md 是功能执行规范，不只是宣传文档。未测试外部账号连接或企业会议系统权限。",
      "en": "Reviewed MIT licensing, the meeting skill and the 2026-10-29 workflow change adding a transcript type field and revising personnel-conversation classification/export rules. The SKILL.md defines functional behavior, not just marketing documentation. External integrations and enterprise meeting-system permissions were not tested.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/YiShu5/claude-skills/blob/87caa778a9f6fe3811ee5af6d6a60a95dc334cf9/LICENSE",
      "license_sha256": "fa84c12ea71cd4b2b74e253dcd597a4b1563176040e968849c936bc1730e2e19",
      "source_commit": "87caa778a9f6fe3811ee5af6d6a60a95dc334cf9",
      "reviewed_at": "2026-11-17T06:06:21.889151+00:00",
      "evidence_pinned_at": "2026-11-17T06:06:21.889151+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "MIT applies to repository software and skill instructions. Third-party brands, supplied documents, model services, WeChat accounts and organization-specific systems are not automatically licensed or provisioned by this repository."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-10-29T09:19:22Z",
        "reviewed_at": "2026-11-17T06:06:21.889151+00:00",
        "url": "https://github.com/YiShu5/claude-skills/commit/87caa778a9f6fe3811ee5af6d6a60a95dc334cf9",
        "qualifies": true,
        "reason": {
          "zh-CN": "面聊导出流程增加普通/人事类的类型字段及分类要求，并调整相应导出和访问范围说明",
          "en": "Adds conversation-type metadata and classification requirements to the transcript export workflow and revises its export/access instructions"
        },
        "reviewed_files": [
          "skills/方片/fangpian-facechat-export/SKILL.md"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/YiShu5/claude-skills",
        "accessed_at": "2026-11-17T06:06:21.889151+00:00"
      },
      {
        "url": "https://github.com/YiShu5/claude-skills/blob/87caa778a9f6fe3811ee5af6d6a60a95dc334cf9/README.md",
        "accessed_at": "2026-11-17T06:06:21.889151+00:00"
      },
      {
        "url": "https://github.com/YiShu5/claude-skills/blob/87caa778a9f6fe3811ee5af6d6a60a95dc334cf9/LICENSE",
        "accessed_at": "2026-11-17T06:06:21.889151+00:00"
      },
      {
        "url": "https://github.com/YiShu5/claude-skills/commit/87caa778a9f6fe3811ee5af6d6a60a95dc334cf9",
        "accessed_at": "2026-11-17T06:06:21.889151+00:00"
      },
      {
        "url": "https://github.com/YiShu5/claude-skills/blob/87caa778a9f6fe3811ee5af6d6a60a95dc334cf9/skills/会记成报.skill/SKILL.md",
        "accessed_at": "2026-11-17T06:06:21.889151+00:00"
      }
    ],
    "discovery": {
      "kind": "user_pdf",
      "submitted_date": "2026-11-17",
      "source_url": "https://github.com/YiShu5/claude-skills",
      "repository_url": "https://github.com/YiShu5/claude-skills",
      "source_title": "办公室 Skill 从夯到拉(纯主观)",
      "source_pages": [
        4,
        6
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDORoRv_A",
    "full_name": "YiShu5/claude-skills",
    "stargazers_count": 130,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "api_license_spdx": "MIT",
    "license_sha256": "fa84c12ea71cd4b2b74e253dcd597a4b1563176040e968849c936bc1730e2e19",
    "last_success_at": "2026-11-17T05:47:17.901868+00:00"
  }
}
```

</details>
