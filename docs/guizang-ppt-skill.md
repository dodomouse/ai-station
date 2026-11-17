# Guizang PPT Skill

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[op7418/guizang-ppt-skill](https://github.com/op7418/guizang-ppt-skill)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 29911 |
| 许可证 / License | AGPL-3.0 |
| 评估时间 / Evaluated at | 2026-11-17T06:06:21.879399+00:00 |

## 中文

指导智能体制作单文件 HTML 演示文稿，提供电子杂志和瑞士网格风格，以及本地浏览器演讲者视图。

### 用途与功能

- 通过模板、主题色和布局规范生成横向翻页演示页面。
- 提供备注、计时、排练、观众窗口同步、标注和静态展示模式。
- 用 Node.js 校验脚本检查版式与演讲者结构，可选 Playwright 做渲染测量。

### 环境与限制

需要支持技能的智能体和浏览器，校验及主题生成需要 Node.js；渲染测量需 Playwright。核心产物是 HTML，PPTX 转换不是主流程。字体、外链素材和可选图像生成服务可能需要网络；应在实际演示设备上检查字体、窗口权限及动画效果，不能仅凭模板校验认定无障碍达标。

### 开始使用

按 README 将技能安装到所用智能体，说明内容、受众和风格。让智能体复制对应 HTML 模板并填充页面，再执行校验、浏览器预览及演讲者窗口检查。

参阅[官方 README](https://github.com/op7418/guizang-ppt-skill/blob/93d21bf4a73a851907a6eb00acbf30618236667a/README.md)。

### 收录与来源

适合直接在浏览器展示的分享和发布会材料，模板约束可帮助维持视觉一致性。已读技能流程及主题对比度计算补丁，未运行浏览器演示。

维护证据：[主题生成器增加强调色块上的正文色选择与对比度检查，并按纸色和灰底中较难的背景调整强调文字色，同步两套 HTML 模板](https://github.com/op7418/guizang-ppt-skill/commit/93d21bf4a73a851907a6eb00acbf30618236667a)（2026-10-30）。

仓库来自用户于 2026-11-17 提供的办公技能 PDF，已另行核对上游。本条按工程通用标准复核，不设 Star 门槛。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Guides agents to create single-file HTML slide decks with magazine and Swiss-grid styles plus a local browser presenter view.

### Uses and features

- Builds horizontally navigated slide decks from templates, constrained themes and layout rules.
- Includes notes, timers, rehearsal, audience-window synchronization, annotations and a static display mode.
- Uses Node.js validators for layout and presenter structure, with optional Playwright-based rendering measurements.

### Requirements and limits

Requires a skill-capable agent and browser; validation and theme generation need Node.js, with Playwright for rendered measurements. The main output is HTML, not a native PPTX conversion workflow. Fonts, linked assets and optional image generation may need network access. Check fonts, popup permissions and animation on the presentation device; template validation alone does not establish accessibility compliance.

### Getting started

Install the skill for your agent following the README and specify content, audience and style. Have the agent populate the appropriate HTML template, then validate it and inspect browser and presenter-window behavior.

See the [official README](https://github.com/op7418/guizang-ppt-skill/blob/93d21bf4a73a851907a6eb00acbf30618236667a/README.md).

### Review and provenance

Suitable for browser-based talks and launches, with template constraints to maintain visual consistency. The skill workflow and contrast-calculation patch were reviewed; the presentation runtime was not executed.

Maintenance evidence: [Adds body-text color selection and contrast checks on accent blocks, checks accent text against the harder of paper and gray backgrounds, and updates both HTML templates](https://github.com/op7418/guizang-ppt-skill/commit/93d21bf4a73a851907a6eb00acbf30618236667a) (2026-10-30).

Identified in an office-skills PDF supplied by the user on 2026-11-17, independently checked against upstream sources and reviewed against the general catalog criteria, with no star threshold.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T06:06:21.879399+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "guizang-ppt-skill",
    "name": "Guizang PPT Skill",
    "repository": "op7418/guizang-ppt-skill",
    "repo_node_id": "R_kgDOSKkbmA",
    "category": "productivity",
    "summary": {
      "zh-CN": "指导智能体制作单文件 HTML 演示文稿，提供电子杂志和瑞士网格风格，以及本地浏览器演讲者视图。",
      "en": "Guides agents to create single-file HTML slide decks with magazine and Swiss-grid styles plus a local browser presenter view."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T06:06:21.879399+00:00",
        "en": "2026-11-17T06:06:21.879399+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合直接在浏览器展示的分享和发布会材料，模板约束可帮助维持视觉一致性。已读技能流程及主题对比度计算补丁，未运行浏览器演示。",
      "en": "Suitable for browser-based talks and launches, with template constraints to maintain visual consistency. The skill workflow and contrast-calculation patch were reviewed; the presentation runtime was not executed.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "AGPL-3.0",
      "osi_approved": true,
      "source_url": "https://github.com/op7418/guizang-ppt-skill/blob/93d21bf4a73a851907a6eb00acbf30618236667a/LICENSE",
      "license_sha256": "0d96a4ff68ad6d4b6f1f30f713b18d5184912ba8dd389f86aa7710db079abcb0",
      "source_commit": "93d21bf4a73a851907a6eb00acbf30618236667a",
      "reviewed_at": "2026-11-17T06:06:21.879399+00:00",
      "evidence_pinned_at": "2026-11-17T06:06:21.879399+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "AGPL-3.0 covers the repository skill, scripts and templates under the pinned root license. Fonts, icons, external assets, model services and user-provided materials retain their own licenses; generated HTML may incorporate licensed template/runtime code.",
      "files": [
        {
          "spdx": "AGPL-3.0",
          "osi_approved": true,
          "source_url": "https://github.com/op7418/guizang-ppt-skill/blob/93d21bf4a73a851907a6eb00acbf30618236667a/LICENSE",
          "license_sha256": "0d96a4ff68ad6d4b6f1f30f713b18d5184912ba8dd389f86aa7710db079abcb0",
          "source_commit": "93d21bf4a73a851907a6eb00acbf30618236667a",
          "reviewed_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_pinned_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_status": "hash_matched",
          "scope": "AGPL-3.0 covers the repository skill, scripts and templates under the pinned root license. Fonts, icons, external assets, model services and user-provided materials retain their own licenses; generated HTML may incorporate licensed template/runtime code."
        }
      ]
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-10-30T11:40:22Z",
        "reviewed_at": "2026-11-17T06:06:21.879399+00:00",
        "url": "https://github.com/op7418/guizang-ppt-skill/commit/93d21bf4a73a851907a6eb00acbf30618236667a",
        "qualifies": true,
        "reason": {
          "zh-CN": "主题生成器增加强调色块上的正文色选择与对比度检查，并按纸色和灰底中较难的背景调整强调文字色，同步两套 HTML 模板",
          "en": "Adds body-text color selection and contrast checks on accent blocks, checks accent text against the harder of paper and gray backgrounds, and updates both HTML templates"
        },
        "reviewed_files": [
          "scripts/gz-theme.mjs",
          "assets/template.html",
          "assets/template-swiss.html"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/op7418/guizang-ppt-skill",
        "accessed_at": "2026-11-17T06:06:21.879399+00:00"
      },
      {
        "url": "https://github.com/op7418/guizang-ppt-skill/blob/93d21bf4a73a851907a6eb00acbf30618236667a/README.md",
        "accessed_at": "2026-11-17T06:06:21.879399+00:00"
      },
      {
        "url": "https://github.com/op7418/guizang-ppt-skill/blob/93d21bf4a73a851907a6eb00acbf30618236667a/LICENSE",
        "accessed_at": "2026-11-17T06:06:21.879399+00:00"
      },
      {
        "url": "https://github.com/op7418/guizang-ppt-skill/commit/93d21bf4a73a851907a6eb00acbf30618236667a",
        "accessed_at": "2026-11-17T06:06:21.879399+00:00"
      },
      {
        "url": "https://github.com/op7418/guizang-ppt-skill/blob/93d21bf4a73a851907a6eb00acbf30618236667a/SKILL.md",
        "accessed_at": "2026-11-17T06:06:21.879399+00:00"
      }
    ],
    "discovery": {
      "kind": "user_pdf",
      "submitted_date": "2026-11-17",
      "source_url": "https://github.com/op7418/guizang-ppt-skill",
      "repository_url": "https://github.com/op7418/guizang-ppt-skill",
      "source_title": "办公室 Skill 从夯到拉(纯主观)",
      "source_pages": [
        1
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOSKkbmA",
    "full_name": "op7418/guizang-ppt-skill",
    "stargazers_count": 29911,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "AGPL-3.0",
    "api_license_spdx": "AGPL-3.0",
    "license_sha256": "0d96a4ff68ad6d4b6f1f30f713b18d5184912ba8dd389f86aa7710db079abcb0",
    "last_success_at": "2026-11-17T05:44:49.734550+00:00"
  }
}
```

</details>
