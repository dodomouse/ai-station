# Claude PowerPoint Skill

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[PeterKalmstrom/claude-powerpoint-skill](https://github.com/PeterKalmstrom/claude-powerpoint-skill)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 6 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T06:06:21.888356+00:00 |

## 中文

为 AI 编程助手提供 PowerPoint 构建、检查和逐页渲染复核流程，支持跨平台生成 PPTX 及 Windows 下操作桌面 PowerPoint。

### 用途与功能

- 从结构化规格或现有模板生成可编辑演示稿，并检查文字溢出、重叠、图片比例和内容问题。
- 组织生成、渲染、查看和修正循环，保留讲稿、引用及人工编辑线索。
- Windows 模式可通过 COM 编辑已打开的 PowerPoint，并提供实时幻灯片视图。

### 环境与限制

基础流程需要支持技能和本地命令的 Agent、Python、python-pptx 等依赖；LibreOffice 可提供近似渲染。Windows 实时编辑和精确渲染另需桌面 PowerPoint 与 pywin32；PowerPoint 的许可不包含在本项目中。可选 Gemini/Veo 媒体生成需 API 密钥，模型服务的费用及文档数据传输规则另行适用。自动检查不能替代人工确认布局和事实。

### 开始使用

按 README 安装 building-powerpoint-decks 技能或 Claude Code 插件，从示例规格或非敏感模板生成一个短演示稿，检查渲染结果，再接入实际文档。Windows 实时模式按 SETUP 配置桌面 PowerPoint。

参阅[官方 README](https://github.com/PeterKalmstrom/claude-powerpoint-skill/blob/46ccda18ad389514e225b62e70e9d1f9524eda27/README.md)。

### 收录与来源

已读 README、MIT、NOTICE 和 2026-11-12 的实际差异：新增 JSON HTTP 辅助调用及错误处理，并修正演示稿 schema 的可访问地址。未运行构建、COM 自动化或上游基准测试。

维护证据：[新增返回 JSON 对象的 HTTP 请求辅助函数及拒绝/异常处理，并修正 deck schema 标识 URL](https://github.com/PeterKalmstrom/claude-powerpoint-skill/commit/46ccda18ad389514e225b62e70e9d1f9524eda27)（2026-11-12）。

仓库来自用户于 2026-11-17 提供的办公技能 PDF，已另行核对上游。本条按工程通用标准复核，不设 Star 门槛。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

An AI coding-agent skill for building, linting and visually reviewing PowerPoint decks, with cross-platform PPTX generation and live PowerPoint automation on Windows.

### Uses and features

- Generate editable decks from structured specifications or templates and check text overflow, overlaps, image proportions and content issues.
- Guide a build, render, inspect and fix loop with speaker notes, citations and workflows for preserving manual edits.
- On Windows, use COM to edit live PowerPoint presentations with a live slide view.

### Requirements and limits

Basic workflows require a skill-capable agent with local command access, Python and packages such as python-pptx. LibreOffice can provide approximate renders. Live editing and exact rendering require Windows, desktop PowerPoint and pywin32; PowerPoint licensing is separate. Optional Gemini/Veo media generation needs API credentials. Model-service costs and document data-processing terms apply. Automated checks do not replace human layout and factual review.

### Getting started

Install the building-powerpoint-decks skill or Claude Code plugin using the README. Start with a sample specification or non-sensitive template, inspect the rendered short deck, then use real documents. Follow SETUP for desktop PowerPoint on Windows.

See the [official README](https://github.com/PeterKalmstrom/claude-powerpoint-skill/blob/46ccda18ad389514e225b62e70e9d1f9524eda27/README.md).

### Review and provenance

Reviewed the README, MIT license, NOTICE and the 2026-11-12 implementation diff adding a JSON HTTP helper/error handling and correcting the deck schema URL. Deck builds, COM automation and upstream benchmarks were not run.

Maintenance evidence: [Adds a JSON-object HTTP helper with refusal/error handling and fixes the deck schema identifier URL](https://github.com/PeterKalmstrom/claude-powerpoint-skill/commit/46ccda18ad389514e225b62e70e9d1f9524eda27) (2026-11-12).

Identified in an office-skills PDF supplied by the user on 2026-11-17, independently checked against upstream sources and reviewed against the general catalog criteria, with no star threshold.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T06:06:21.888356+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "claude-powerpoint-skill",
    "name": "Claude PowerPoint Skill",
    "repository": "PeterKalmstrom/claude-powerpoint-skill",
    "repo_node_id": "R_kgDOSaI1cA",
    "category": "productivity",
    "summary": {
      "zh-CN": "为 AI 编程助手提供 PowerPoint 构建、检查和逐页渲染复核流程，支持跨平台生成 PPTX 及 Windows 下操作桌面 PowerPoint。",
      "en": "An AI coding-agent skill for building, linting and visually reviewing PowerPoint decks, with cross-platform PPTX generation and live PowerPoint automation on Windows."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T06:06:21.888356+00:00",
        "en": "2026-11-17T06:06:21.888356+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "已读 README、MIT、NOTICE 和 2026-11-12 的实际差异：新增 JSON HTTP 辅助调用及错误处理，并修正演示稿 schema 的可访问地址。未运行构建、COM 自动化或上游基准测试。",
      "en": "Reviewed the README, MIT license, NOTICE and the 2026-11-12 implementation diff adding a JSON HTTP helper/error handling and correcting the deck schema URL. Deck builds, COM automation and upstream benchmarks were not run.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/PeterKalmstrom/claude-powerpoint-skill/blob/46ccda18ad389514e225b62e70e9d1f9524eda27/LICENSE",
      "license_sha256": "f21ca4c10d7dd50fbd44aaf2030923cf2ca0d8c7bba240f68124331c55c9315a",
      "source_commit": "46ccda18ad389514e225b62e70e9d1f9524eda27",
      "reviewed_at": "2026-11-17T06:06:21.888356+00:00",
      "evidence_pinned_at": "2026-11-17T06:06:21.888356+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "MIT covers the project code and skill. NOTICE identifies Impeccable-derived material under Apache-2.0 and Lucide/Feather icons under ISC/MIT. Microsoft PowerPoint, external models and media services retain separate terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-12T12:11:18Z",
        "reviewed_at": "2026-11-17T06:06:21.888356+00:00",
        "url": "https://github.com/PeterKalmstrom/claude-powerpoint-skill/commit/46ccda18ad389514e225b62e70e9d1f9524eda27",
        "qualifies": true,
        "reason": {
          "zh-CN": "新增返回 JSON 对象的 HTTP 请求辅助函数及拒绝/异常处理，并修正 deck schema 标识 URL",
          "en": "Adds a JSON-object HTTP helper with refusal/error handling and fixes the deck schema identifier URL"
        },
        "reviewed_files": [
          "scripts/kShared.py",
          "scripts/build_deck.py"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/PeterKalmstrom/claude-powerpoint-skill",
        "accessed_at": "2026-11-17T06:06:21.888356+00:00"
      },
      {
        "url": "https://github.com/PeterKalmstrom/claude-powerpoint-skill/blob/46ccda18ad389514e225b62e70e9d1f9524eda27/README.md",
        "accessed_at": "2026-11-17T06:06:21.888356+00:00"
      },
      {
        "url": "https://github.com/PeterKalmstrom/claude-powerpoint-skill/blob/46ccda18ad389514e225b62e70e9d1f9524eda27/LICENSE",
        "accessed_at": "2026-11-17T06:06:21.888356+00:00"
      },
      {
        "url": "https://github.com/PeterKalmstrom/claude-powerpoint-skill/commit/46ccda18ad389514e225b62e70e9d1f9524eda27",
        "accessed_at": "2026-11-17T06:06:21.888356+00:00"
      },
      {
        "url": "https://github.com/PeterKalmstrom/claude-powerpoint-skill/blob/46ccda18ad389514e225b62e70e9d1f9524eda27/NOTICE",
        "accessed_at": "2026-11-17T06:06:21.888356+00:00"
      }
    ],
    "discovery": {
      "kind": "user_pdf",
      "submitted_date": "2026-11-17",
      "source_url": "https://github.com/PeterKalmstrom/claude-powerpoint-skill",
      "repository_url": "https://github.com/PeterKalmstrom/claude-powerpoint-skill",
      "source_title": "办公室 Skill 从夯到拉(纯主观)",
      "source_pages": [
        2
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOSaI1cA",
    "full_name": "PeterKalmstrom/claude-powerpoint-skill",
    "stargazers_count": 6,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "api_license_spdx": "MIT",
    "license_sha256": "f21ca4c10d7dd50fbd44aaf2030923cf2ca0d8c7bba240f68124331c55c9315a",
    "last_success_at": "2026-11-17T05:47:07.555622+00:00"
  }
}
```

</details>
