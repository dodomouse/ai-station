# Call Notes to Actions

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[FairdraftStudio/call-notes-to-actions-skill](https://github.com/FairdraftStudio/call-notes-to-actions-skill)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 0 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T06:06:21.885244+00:00 |

## 中文

将会议转录或零散笔记整理成摘要、决策、行动表和跟进邮件草稿的轻量智能体技能。

### 用途与功能

- 输出简短摘要、决策、负责人和截止时间、待解决问题与风险。
- 把推断的负责人和日期标为 proposed，缺失负责人标为 TBD；有转录时间戳时保留决策出处。
- 要求邮件草稿与行动表一致，默认在对话中交付 Markdown；宿主具备文件能力时可按需生成 DOCX。

### 环境与限制

需要能加载技能的 Claude 或兼容智能体，以及会议文本或笔记；不提供独立录音转写服务。推断标记属于提示词要求，仍需核对姓名、决定和日期，尤其是会议日期缺失时。云模型处理会议内容可能涉及外发和费用；本技能生成邮件草稿，不负责自动发送。

### 开始使用

按 README 安装 call-notes-to-actions 插件或上传仓库提供的技能包，粘贴会议笔记并补充会议日期和参与者。核对 proposed、TBD 与 To confirm 项后再使用行动表或发送草稿。

参阅[官方 README](https://github.com/FairdraftStudio/call-notes-to-actions-skill/blob/9ffb2844ec09dea022308e34a2ce51121ba21f69/README.md)。

### 收录与来源

输入和输出格式明确，适合快速整理客户沟通记录。已核对初始完整技能实现与当前技能文件；本次未运行模型，不能保证不遗漏或不产生错误推断。

维护证据：[首次加入完整会议笔记处理技能，定义输入、推断标记、行动项与邮件输出格式，以及决策、日期和行动表一致性检查](https://github.com/FairdraftStudio/call-notes-to-actions-skill/commit/5188b082171e728ed7f0c87092bc84fcf991408a)（2026-09-11）。

仓库来自用户于 2026-11-17 提供的办公技能 PDF，已另行核对上游。本条按工程通用标准复核，不设 Star 门槛。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

A lightweight agent skill that turns meeting transcripts or rough notes into summaries, decisions, action tables and follow-up email drafts.

### Uses and features

- Outputs a short summary, decisions, owners and due dates, open questions and risks.
- Marks inferred owners/dates as proposed and missing owners as TBD, retaining decision timestamps when present.
- Checks that the email draft matches the action table and defaults to Markdown in chat; DOCX output is optional when supported by the host.

### Requirements and limits

Requires Claude or a compatible skill host plus a meeting transcript or notes; it does not provide standalone audio transcription. Inference labels are prompt requirements, so names, decisions and dates still need review, especially when the meeting date is missing. Cloud processing may disclose meeting content and incur fees. The skill drafts email rather than sending it automatically.

### Getting started

Install the call-notes-to-actions plugin or upload the repository’s skill package as documented. Paste the notes with the meeting date and participants, then review proposed, TBD and To confirm items before using the action table or sending the draft.

See the [official README](https://github.com/FairdraftStudio/call-notes-to-actions-skill/blob/9ffb2844ec09dea022308e34a2ce51121ba21f69/README.md).

### Review and provenance

Has a focused input/output format for organizing client-call records. The initial complete implementation and current skill file were reviewed; no model was run, so omission-free or error-free extraction is not established.

Maintenance evidence: [Adds the complete meeting-notes skill with input requirements, inference labels, action-item and email output formats, and checks for decisions, dates and consistency with the action table](https://github.com/FairdraftStudio/call-notes-to-actions-skill/commit/5188b082171e728ed7f0c87092bc84fcf991408a) (2026-09-11).

Identified in an office-skills PDF supplied by the user on 2026-11-17, independently checked against upstream sources and reviewed against the general catalog criteria, with no star threshold.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T06:06:21.885244+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "call-notes-to-actions-skill",
    "name": "Call Notes to Actions",
    "repository": "FairdraftStudio/call-notes-to-actions-skill",
    "repo_node_id": "R_kgDOUWo7PQ",
    "category": "productivity",
    "summary": {
      "zh-CN": "将会议转录或零散笔记整理成摘要、决策、行动表和跟进邮件草稿的轻量智能体技能。",
      "en": "A lightweight agent skill that turns meeting transcripts or rough notes into summaries, decisions, action tables and follow-up email drafts."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T06:06:21.885244+00:00",
        "en": "2026-11-17T06:06:21.885244+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "输入和输出格式明确，适合快速整理客户沟通记录。已核对初始完整技能实现与当前技能文件；本次未运行模型，不能保证不遗漏或不产生错误推断。",
      "en": "Has a focused input/output format for organizing client-call records. The initial complete implementation and current skill file were reviewed; no model was run, so omission-free or error-free extraction is not established.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/FairdraftStudio/call-notes-to-actions-skill/blob/9ffb2844ec09dea022308e34a2ce51121ba21f69/LICENSE",
      "license_sha256": "9592b2c1f9577311c1ec27c2584f6b6ad00653d7ebc8633a5a8c92abd884f1fe",
      "source_commit": "9ffb2844ec09dea022308e34a2ce51121ba21f69",
      "reviewed_at": "2026-11-17T06:06:21.885244+00:00",
      "evidence_pinned_at": "2026-11-17T06:06:21.885244+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "MIT covers the skill and files in this repository under its pinned root LICENSE. The separately marketed Client-Ops Kit, linked paid templates, model services and user meeting content are not granted this repository’s MIT license.",
      "files": [
        {
          "spdx": "MIT",
          "osi_approved": true,
          "source_url": "https://github.com/FairdraftStudio/call-notes-to-actions-skill/blob/9ffb2844ec09dea022308e34a2ce51121ba21f69/LICENSE",
          "license_sha256": "9592b2c1f9577311c1ec27c2584f6b6ad00653d7ebc8633a5a8c92abd884f1fe",
          "source_commit": "9ffb2844ec09dea022308e34a2ce51121ba21f69",
          "reviewed_at": "2026-11-17T05:54:50.206488+00:00",
          "evidence_pinned_at": "2026-11-17T05:54:50.206488+00:00",
          "evidence_status": "hash_matched",
          "scope": "MIT covers the skill and files in this repository under its pinned root LICENSE. The separately marketed Client-Ops Kit, linked paid templates, model services and user meeting content are not granted this repository’s MIT license."
        }
      ]
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-09-11T11:00:54Z",
        "reviewed_at": "2026-11-17T06:06:21.885244+00:00",
        "url": "https://github.com/FairdraftStudio/call-notes-to-actions-skill/commit/5188b082171e728ed7f0c87092bc84fcf991408a",
        "qualifies": true,
        "reason": {
          "zh-CN": "首次加入完整会议笔记处理技能，定义输入、推断标记、行动项与邮件输出格式，以及决策、日期和行动表一致性检查",
          "en": "Adds the complete meeting-notes skill with input requirements, inference labels, action-item and email output formats, and checks for decisions, dates and consistency with the action table"
        },
        "reviewed_files": [
          "call-notes-to-actions/SKILL.md"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/FairdraftStudio/call-notes-to-actions-skill",
        "accessed_at": "2026-11-17T06:06:21.885244+00:00"
      },
      {
        "url": "https://github.com/FairdraftStudio/call-notes-to-actions-skill/blob/9ffb2844ec09dea022308e34a2ce51121ba21f69/README.md",
        "accessed_at": "2026-11-17T06:06:21.885244+00:00"
      },
      {
        "url": "https://github.com/FairdraftStudio/call-notes-to-actions-skill/blob/9ffb2844ec09dea022308e34a2ce51121ba21f69/LICENSE",
        "accessed_at": "2026-11-17T06:06:21.885244+00:00"
      },
      {
        "url": "https://github.com/FairdraftStudio/call-notes-to-actions-skill/commit/5188b082171e728ed7f0c87092bc84fcf991408a",
        "accessed_at": "2026-11-17T06:06:21.885244+00:00"
      },
      {
        "url": "https://github.com/FairdraftStudio/call-notes-to-actions-skill/blob/9ffb2844ec09dea022308e34a2ce51121ba21f69/plugins/call-notes-to-actions/skills/call-notes-to-actions/SKILL.md",
        "accessed_at": "2026-11-17T06:06:21.885244+00:00"
      }
    ],
    "discovery": {
      "kind": "user_pdf",
      "submitted_date": "2026-11-17",
      "source_url": "https://github.com/FairdraftStudio/call-notes-to-actions-skill",
      "repository_url": "https://github.com/FairdraftStudio/call-notes-to-actions-skill",
      "source_title": "办公室 Skill 从夯到拉(纯主观)",
      "source_pages": [
        6
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOUWo7PQ",
    "full_name": "FairdraftStudio/call-notes-to-actions-skill",
    "stargazers_count": 0,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "api_license_spdx": "MIT",
    "license_sha256": "9592b2c1f9577311c1ec27c2584f6b6ad00653d7ebc8633a5a8c92abd884f1fe",
    "last_success_at": "2026-11-17T05:45:42.024951+00:00"
  }
}
```

</details>
