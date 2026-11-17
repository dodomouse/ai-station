# Animated Resume Claude Skill

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[dooa-ansari/animated-resume-claude-skill](https://github.com/dooa-ansari/animated-resume-claude-skill)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 2 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T06:06:21.892652+00:00 |

## 中文

引导 AI 助手把简历事实整理为结构化资料，再生成带职业关卡、动画头像和项目关系图的单页 HTML 作品集。

### 用途与功能

- 从简历、用户回答及可选项目 README 提取可追溯事实，生成 profile.json，要求不虚构雇主、数字、经历或性格。
- Python 构建脚本检查必填字段和预设值，将资料嵌入 HTML/CSS/JavaScript 模板，可重复修改 JSON 后重建。
- 提供主题、头像外观、可选双语与项目关系图，并包含减少动态效果支持；输出可放到静态网站托管服务。

### 环境与限制

需要可读简历并使用技能的 AI 助手；标准构建方式需要 Python 3，预览需要现代浏览器。构建脚本使用标准库，不需要 Node 构建链。页面主体在一个 HTML 文件内，但模板默认从 Google Fonts 加载字体，严格离线使用需自行替换或本地化字体。输出是展示型网页，不是 DOCX/PDF 简历生成器，也不保证招聘系统可解析；常规投递仍需保留适合招聘方要求的简历。发布前核对资料和联系信息，模型处理及托管服务的成本与条款另计。

### 开始使用

按官方 README 安装 animated-resume 技能，提供简历并选择语言、主题和头像外观。让助手按 schema 生成 profile.json，再执行 `python3 <skill-dir>/scripts/build.py profile.json index.html`。在桌面和手机宽度预览，确认内容后再决定是否托管。

参阅[官方 README](https://github.com/dooa-ansari/animated-resume-claude-skill/blob/3b464f3e13b033201f24aa77ca1667a168ab03be/README.md)。

### 收录与来源

仓库同时提供结构化资料约定、可检查的 Python 构建器和实际页面模板，适合希望用互动网页展示经历和项目的人。已核对布局修复的实际补丁；未运行生成器或浏览器实测，不能据此保证所有屏幕表现或招聘系统兼容性。

维护证据：[按轮换标题的最大高度预留角色行空间，并在窗口变化和字体就绪时重新计算，修复长标题换行造成的页面跳动](https://github.com/dooa-ansari/animated-resume-claude-skill/commit/56094f73e90657d3c969ed03141954d0539b5b81)（2026-10-13）。

仓库来自用户于 2026-11-17 提供的办公技能 PDF，已另行核对上游。本条按工程通用标准复核，不设 Star 门槛。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Guides an AI assistant to turn resume facts into structured profile data and generate a single-page HTML portfolio with career levels, an animated avatar and a project graph.

### Uses and features

- Extracts traceable facts from resumes, user answers and optional project READMEs into profile.json, with rules against inventing employers, numbers, experience or traits.
- A Python build script checks required fields and preset values, then embeds profile data in an HTML/CSS/JavaScript template; edits are made in JSON and rebuilt.
- Themes, avatar appearance, optional bilingual content and a project graph are supported, along with reduced-motion behavior; output can be served by a static host.

### Requirements and limits

An AI assistant able to read resumes and use the skill is required; the standard build uses Python 3 and previews need a modern browser. The builder uses the standard library and needs no Node build chain. The page body is in one HTML file, but the template loads Google Fonts by default; strict offline use requires replacing or hosting fonts locally. The output is a showcase website, not a DOCX/PDF resume generator, and recruiting-system parsing is not guaranteed; retain a resume suited to the employer’s submission requirements. Check profile and contact details before publishing; model and hosting costs and terms are separate.

### Getting started

Install the animated-resume skill using the official README, provide a resume and choose language, theme and avatar preferences. Have the assistant produce profile.json using the schema, then run `python3 <skill-dir>/scripts/build.py profile.json index.html`. Preview at desktop and phone widths and check the content before deciding whether to host it.

See the [official README](https://github.com/dooa-ansari/animated-resume-claude-skill/blob/3b464f3e13b033201f24aa77ca1667a168ab03be/README.md).

### Review and provenance

The repository provides a profile schema, inspectable Python builder and actual page template for people who want an interactive presentation of their experience and projects. A real layout-fix patch was reviewed. The generator and browser output were not tested, so this review does not establish behavior on every screen or compatibility with recruiting systems.

Maintenance evidence: [Reserves the role line’s maximum rotating-headline height and recalculates it after resizing or font loading, fixing layout jumps when long headlines wrap](https://github.com/dooa-ansari/animated-resume-claude-skill/commit/56094f73e90657d3c969ed03141954d0539b5b81) (2026-10-13).

Identified in an office-skills PDF supplied by the user on 2026-11-17, independently checked against upstream sources and reviewed against the general catalog criteria, with no star threshold.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T06:06:21.892652+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "animated-resume-claude-skill",
    "name": "Animated Resume Claude Skill",
    "repository": "dooa-ansari/animated-resume-claude-skill",
    "repo_node_id": "R_kgDOVGZYKw",
    "category": "productivity",
    "summary": {
      "zh-CN": "引导 AI 助手把简历事实整理为结构化资料，再生成带职业关卡、动画头像和项目关系图的单页 HTML 作品集。",
      "en": "Guides an AI assistant to turn resume facts into structured profile data and generate a single-page HTML portfolio with career levels, an animated avatar and a project graph."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T06:06:21.892652+00:00",
        "en": "2026-11-17T06:06:21.892652+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "仓库同时提供结构化资料约定、可检查的 Python 构建器和实际页面模板，适合希望用互动网页展示经历和项目的人。已核对布局修复的实际补丁；未运行生成器或浏览器实测，不能据此保证所有屏幕表现或招聘系统兼容性。",
      "en": "The repository provides a profile schema, inspectable Python builder and actual page template for people who want an interactive presentation of their experience and projects. A real layout-fix patch was reviewed. The generator and browser output were not tested, so this review does not establish behavior on every screen or compatibility with recruiting systems.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/dooa-ansari/animated-resume-claude-skill/blob/3b464f3e13b033201f24aa77ca1667a168ab03be/LICENSE",
      "license_sha256": "4619fac7633322071be96db094e0a9374bb6c51c63ea26a5f06b15af2f583a37",
      "source_commit": "3b464f3e13b033201f24aa77ca1667a168ab03be",
      "reviewed_at": "2026-11-17T06:06:21.892652+00:00",
      "evidence_pinned_at": "2026-11-17T06:06:21.892652+00:00",
      "evidence_status": "hash_matched",
      "scope_note": {
        "zh-CN": "根 LICENSE 为 MIT，覆盖该技能、构建脚本和模板。用户简历、头像素材、外部字体、模型服务及托管服务不因此统一变为 MIT；示例资料为虚构人物。",
        "en": "The root MIT LICENSE covers the skill, build script and template. User resumes, avatar assets, external fonts, model services and hosting do not all become MIT-licensed; the included example profile is fictional."
      }
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-10-13T11:52:10Z",
        "reviewed_at": "2026-11-17T06:06:21.892652+00:00",
        "url": "https://github.com/dooa-ansari/animated-resume-claude-skill/commit/56094f73e90657d3c969ed03141954d0539b5b81",
        "qualifies": true,
        "reason": {
          "zh-CN": "按轮换标题的最大高度预留角色行空间，并在窗口变化和字体就绪时重新计算，修复长标题换行造成的页面跳动",
          "en": "Reserves the role line’s maximum rotating-headline height and recalculates it after resizing or font loading, fixing layout jumps when long headlines wrap"
        },
        "reviewed_files": [
          "skills/animated-resume/assets/template.html",
          "index.html"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/dooa-ansari/animated-resume-claude-skill",
        "accessed_at": "2026-11-17T06:06:21.892652+00:00"
      },
      {
        "url": "https://github.com/dooa-ansari/animated-resume-claude-skill/blob/3b464f3e13b033201f24aa77ca1667a168ab03be/README.md",
        "accessed_at": "2026-11-17T06:06:21.892652+00:00"
      },
      {
        "url": "https://github.com/dooa-ansari/animated-resume-claude-skill/blob/3b464f3e13b033201f24aa77ca1667a168ab03be/LICENSE",
        "accessed_at": "2026-11-17T06:06:21.892652+00:00"
      },
      {
        "url": "https://github.com/dooa-ansari/animated-resume-claude-skill/commit/56094f73e90657d3c969ed03141954d0539b5b81",
        "accessed_at": "2026-11-17T06:06:21.892652+00:00"
      },
      {
        "url": "https://github.com/dooa-ansari/animated-resume-claude-skill/blob/3b464f3e13b033201f24aa77ca1667a168ab03be/skills/animated-resume/SKILL.md",
        "accessed_at": "2026-11-17T06:06:21.892652+00:00"
      },
      {
        "url": "https://github.com/dooa-ansari/animated-resume-claude-skill/blob/3b464f3e13b033201f24aa77ca1667a168ab03be/skills/animated-resume/scripts/build.py",
        "accessed_at": "2026-11-17T06:06:21.892652+00:00"
      },
      {
        "url": "https://github.com/dooa-ansari/animated-resume-claude-skill/blob/3b464f3e13b033201f24aa77ca1667a168ab03be/skills/animated-resume/assets/template.html",
        "accessed_at": "2026-11-17T06:06:21.892652+00:00"
      }
    ],
    "discovery": {
      "kind": "user_pdf",
      "submitted_date": "2026-11-17",
      "source_url": "https://github.com/dooa-ansari/animated-resume-claude-skill",
      "repository_url": "https://github.com/dooa-ansari/animated-resume-claude-skill",
      "source_title": "办公室 Skill 从夯到拉(纯主观)",
      "source_pages": [
        8
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVGZYKw",
    "full_name": "dooa-ansari/animated-resume-claude-skill",
    "stargazers_count": 2,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "api_license_spdx": "MIT",
    "license_sha256": "4619fac7633322071be96db094e0a9374bb6c51c63ea26a5f06b15af2f583a37",
    "last_success_at": "2026-11-17T05:46:33.629788+00:00"
  }
}
```

</details>
