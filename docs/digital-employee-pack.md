# 数字员工配置包（开源样例）

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[Hahaknight/digital-employee-pack](https://github.com/Hahaknight/digital-employee-pack)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 0 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T06:06:21.889905+00:00 |

## 中文

面向 AI Agent 的三个中文办公技能样例，帮助整理周报、会议纪要和 PPT 逐页内容大纲。

### 用途与功能

- 根据工作日志、提交记录或用户提供的进展生成周报草稿。
- 从会议要点提取结论、带负责人和截止时间的行动项，以及待确认问题。
- 按受众、时长和目标先拟故事线，再输出逐页标题、要点、图表建议和讲稿提示。

### 环境与限制

需要支持本地技能的 AI Agent；样例主要是提示词和工作流，本身不是独立办公软件，也不直接生成 PPTX 或转写录音。Git 周报来源需本地仓库权限，会议输入需已有要点或文字记录。使用云端 Agent 时，交给它的工作记录可能发送给模型服务，费用及数据条款以该服务为准。输出仍需核对。收录范围仅为主分支三个 MIT 样例；README 另提供完整下载包，其附加技能和 Hooks 未在本次核验。

### 开始使用

按 README 安装三个样例，或将 free-sample/skills 下需要的文件夹复制到 Agent 的技能目录。先用非敏感工作要点尝试周报、会议纪要或 PPT 大纲，并补齐标为待确认的信息。

参阅[官方 README](https://github.com/Hahaknight/digital-employee-pack/blob/a0d26607f690833be6dcda8d1fe861e3b8c224c8/README.md)。

### 收录与来源

已核对主分支 MIT 原文、三个样例和 2026-08-31 新增会议纪要工作流的实际差异，包含输入澄清、结论/行动项结构及禁止编造规则。这是近期完整功能实现，不据此声称长期维护成熟度。未运行 Agent 或核验完整 release 包。

维护证据：[新增会议纪要技能的完整工作流，覆盖原料澄清、结论与行动项提取、固定输出结构和禁止编造约束](https://github.com/Hahaknight/digital-employee-pack/commit/e98b8455586430e019b5a7558f06492db021dbce)（2026-08-31）。

仓库来自用户于 2026-11-17 提供的办公技能 PDF，已另行核对上游。本条按工程通用标准复核，不设 Star 门槛。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Three open-source Chinese office-work skill samples for AI agents: weekly reports, meeting minutes and slide-by-slide presentation outlines.

### Uses and features

- Draft weekly reports from work logs, commit history or user-provided progress.
- Extract meeting decisions, action items with owners/deadlines and unresolved questions.
- Plan a presentation narrative from audience, duration and goals, then produce slide titles, points, chart suggestions and speaking notes.

### Requirements and limits

Requires a local-skill-capable AI agent. These are instructions and workflows, not a standalone office suite, PPTX generator or audio transcriber. Git-based reporting requires local repository access; meeting input needs existing notes or text. Cloud agents may send supplied work records to their model service, whose pricing and data terms apply. Review all outputs. This entry covers only the three MIT samples on the main branch; extra skills and hooks in the separately downloadable full pack were not assessed.

### Getting started

Install the three samples using the README or copy the desired folders from free-sample/skills into your agent’s skill directory. Try non-sensitive work notes and confirm any missing facts in the report, minutes or presentation outline.

See the [official README](https://github.com/Hahaknight/digital-employee-pack/blob/a0d26607f690833be6dcda8d1fe861e3b8c224c8/README.md).

### Review and provenance

Reviewed the main-branch MIT text, all three samples and the 2026-08-31 addition of the meeting-minutes workflow, including input clarification, decisions/action items and anti-fabrication rules. This is a recent complete feature implementation, not proof of long-term maintenance maturity. Agent execution and the full release package were not tested.

Maintenance evidence: [Adds a complete meeting-minutes skill workflow covering input clarification, decisions/action items, output structure and anti-fabrication constraints](https://github.com/Hahaknight/digital-employee-pack/commit/e98b8455586430e019b5a7558f06492db021dbce) (2026-08-31).

Identified in an office-skills PDF supplied by the user on 2026-11-17, independently checked against upstream sources and reviewed against the general catalog criteria, with no star threshold.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T06:06:21.889905+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "digital-employee-pack",
    "name": "数字员工配置包（开源样例）",
    "repository": "Hahaknight/digital-employee-pack",
    "repo_node_id": "R_kgDOUGtxWw",
    "category": "productivity",
    "summary": {
      "zh-CN": "面向 AI Agent 的三个中文办公技能样例，帮助整理周报、会议纪要和 PPT 逐页内容大纲。",
      "en": "Three open-source Chinese office-work skill samples for AI agents: weekly reports, meeting minutes and slide-by-slide presentation outlines."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T06:06:21.889905+00:00",
        "en": "2026-11-17T06:06:21.889905+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "已核对主分支 MIT 原文、三个样例和 2026-08-31 新增会议纪要工作流的实际差异，包含输入澄清、结论/行动项结构及禁止编造规则。这是近期完整功能实现，不据此声称长期维护成熟度。未运行 Agent 或核验完整 release 包。",
      "en": "Reviewed the main-branch MIT text, all three samples and the 2026-08-31 addition of the meeting-minutes workflow, including input clarification, decisions/action items and anti-fabrication rules. This is a recent complete feature implementation, not proof of long-term maintenance maturity. Agent execution and the full release package were not tested.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/Hahaknight/digital-employee-pack/blob/a0d26607f690833be6dcda8d1fe861e3b8c224c8/LICENSE",
      "license_sha256": "8f84e196eec630bd64b453daec2e1f8b55601b06cce10ddad9f6429d8dd30631",
      "source_commit": "a0d26607f690833be6dcda8d1fe861e3b8c224c8",
      "reviewed_at": "2026-11-17T06:06:21.889905+00:00",
      "evidence_pinned_at": "2026-11-17T06:06:21.889905+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "MIT coverage in this entry is limited to the three main-branch free-sample skills and their repository documentation. The separately downloadable full release pack, extra hooks and external AI services were not reviewed as part of this scope."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-08-31T19:39:04Z",
        "reviewed_at": "2026-11-17T06:06:21.889905+00:00",
        "url": "https://github.com/Hahaknight/digital-employee-pack/commit/e98b8455586430e019b5a7558f06492db021dbce",
        "qualifies": true,
        "reason": {
          "zh-CN": "新增会议纪要技能的完整工作流，覆盖原料澄清、结论与行动项提取、固定输出结构和禁止编造约束",
          "en": "Adds a complete meeting-minutes skill workflow covering input clarification, decisions/action items, output structure and anti-fabrication constraints"
        },
        "reviewed_files": [
          "free-sample/skills/meeting-minutes/SKILL.md"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/Hahaknight/digital-employee-pack",
        "accessed_at": "2026-11-17T06:06:21.889905+00:00"
      },
      {
        "url": "https://github.com/Hahaknight/digital-employee-pack/blob/a0d26607f690833be6dcda8d1fe861e3b8c224c8/README.md",
        "accessed_at": "2026-11-17T06:06:21.889905+00:00"
      },
      {
        "url": "https://github.com/Hahaknight/digital-employee-pack/blob/a0d26607f690833be6dcda8d1fe861e3b8c224c8/LICENSE",
        "accessed_at": "2026-11-17T06:06:21.889905+00:00"
      },
      {
        "url": "https://github.com/Hahaknight/digital-employee-pack/commit/e98b8455586430e019b5a7558f06492db021dbce",
        "accessed_at": "2026-11-17T06:06:21.889905+00:00"
      },
      {
        "url": "https://github.com/Hahaknight/digital-employee-pack/blob/a0d26607f690833be6dcda8d1fe861e3b8c224c8/free-sample/skills/meeting-minutes/SKILL.md",
        "accessed_at": "2026-11-17T06:06:21.889905+00:00"
      },
      {
        "url": "https://github.com/Hahaknight/digital-employee-pack/blob/a0d26607f690833be6dcda8d1fe861e3b8c224c8/free-sample/skills/weekly-report/SKILL.md",
        "accessed_at": "2026-11-17T06:06:21.889905+00:00"
      },
      {
        "url": "https://github.com/Hahaknight/digital-employee-pack/blob/a0d26607f690833be6dcda8d1fe861e3b8c224c8/free-sample/skills/ppt-outline/SKILL.md",
        "accessed_at": "2026-11-17T06:06:21.889905+00:00"
      }
    ],
    "discovery": {
      "kind": "user_pdf",
      "submitted_date": "2026-11-17",
      "source_url": "https://github.com/Hahaknight/digital-employee-pack",
      "repository_url": "https://github.com/Hahaknight/digital-employee-pack",
      "source_title": "办公室 Skill 从夯到拉(纯主观)",
      "source_pages": [
        4
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOUGtxWw",
    "full_name": "Hahaknight/digital-employee-pack",
    "stargazers_count": 0,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "api_license_spdx": "MIT",
    "license_sha256": "8f84e196eec630bd64b453daec2e1f8b55601b06cce10ddad9f6429d8dd30631",
    "last_success_at": "2026-11-17T05:47:26.931618+00:00"
  }
}
```

</details>
