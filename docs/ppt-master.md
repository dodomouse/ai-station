# PPT Master

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[hugohe3/ppt-master](https://github.com/hugohe3/ppt-master)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 77626 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T06:06:21.878663+00:00 |

## 中文

在智能体中组织资料分析、页面设计和本地导出，将主题或文档制作成可继续编辑的 PowerPoint 演示文稿。

### 用途与功能

- 将网页、文档等来源转为中间资料，经 SVG 页面设计导出原生 DrawingML 元素。
- 提供新建演示文稿、复用模板、编辑现有 PPTX，以及添加动画和旁白的流程。
- 支持页面预览与检查；图表和表格默认可编辑形状，专门导出选项可生成带数据的原生图表与表格。

### 环境与限制

需要可读写文件和执行脚本的 AI 智能体、Python 3.10–3.14 及对应依赖；部分旧文档格式需 Pandoc，PDF 转换依赖另行授权的 PyMuPDF。云模型、搜索、配图和语音服务可向外部发送资料并产生费用。本地导出不代表全程离线；字体、复杂版式和不同演示软件的兼容性需检查，不能保证完整还原 PowerPoint 所有功能。

### 开始使用

克隆仓库并在独立 Python 环境安装 requirements.txt，用支持技能的智能体加载 skills/ppt-master，提供源文件、受众和演示目标。检查生成页面及导出的 PPTX；配图和语音按需配置服务。

参阅[官方 README](https://github.com/hugohe3/ppt-master/blob/3af3e8ef774c4d67ee57e1306d9256d08c9ee1bf/README.md)。

### 收录与来源

把内容组织、版式制作和可编辑交付连接在同一流程中，适合需要继续修改的汇报材料。已核对技能入口、依赖、素材许可说明及网页图片路径修复，未执行上游或测量生成质量。

维护证据：[网页转 Markdown 时用 URL 正斜杠拼接下载图片的相对路径，避免 Windows 的反斜杠使图片引用失效](https://github.com/hugohe3/ppt-master/commit/e2820d326d049f1fcbe90523983def3d52280233)（2026-11-11）。

仓库来自用户于 2026-11-17 提供的办公技能 PDF，已另行核对上游。本条按工程通用标准复核，不设 Star 门槛。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

An agent workflow for source analysis, slide design and local export, turning topics or documents into editable PowerPoint presentations.

### Uses and features

- Converts web pages and documents into source material, then exports SVG slide designs as native DrawingML elements.
- Provides workflows for new decks, reusable templates, existing PPTX edits, animations and narration.
- Includes slide previews and checks; charts and tables default to editable shapes, with an export option for native data-backed chart and table objects.

### Requirements and limits

Requires an AI agent with file and script access, Python 3.10–3.14 and the relevant dependencies. Some legacy formats need Pandoc; PDF conversion uses separately licensed PyMuPDF. Cloud model, search, image and speech services may send source material externally and incur charges. Local export does not make the whole workflow offline; fonts, complex layouts and presentation-software compatibility need checking, and full PowerPoint feature parity is not guaranteed.

### Getting started

Clone the repository, install requirements.txt in a separate Python environment, and load skills/ppt-master in a compatible agent. Provide source files, audience and presentation goals, then inspect the rendered slides and exported PPTX. Configure image or speech services only as needed.

See the [official README](https://github.com/hugohe3/ppt-master/blob/3af3e8ef774c4d67ee57e1306d9256d08c9ee1bf/README.md).

### Review and provenance

Connects content planning, slide construction and editable delivery for presentations that need further revision. The skill entry, dependencies, asset notices and web-image path fix were reviewed; no upstream code or generation-quality benchmark was run.

Maintenance evidence: [Builds downloaded-image Markdown paths with URL forward slashes instead of OS-dependent joins, avoiding broken image references on Windows](https://github.com/hugohe3/ppt-master/commit/e2820d326d049f1fcbe90523983def3d52280233) (2026-11-11).

Identified in an office-skills PDF supplied by the user on 2026-11-17, independently checked against upstream sources and reviewed against the general catalog criteria, with no star threshold.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T06:06:21.878663+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "ppt-master",
    "name": "PPT Master",
    "repository": "hugohe3/ppt-master",
    "repo_node_id": "R_kgDOQl_Gyg",
    "category": "productivity",
    "summary": {
      "zh-CN": "在智能体中组织资料分析、页面设计和本地导出，将主题或文档制作成可继续编辑的 PowerPoint 演示文稿。",
      "en": "An agent workflow for source analysis, slide design and local export, turning topics or documents into editable PowerPoint presentations."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T06:06:21.878663+00:00",
        "en": "2026-11-17T06:06:21.878663+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "把内容组织、版式制作和可编辑交付连接在同一流程中，适合需要继续修改的汇报材料。已核对技能入口、依赖、素材许可说明及网页图片路径修复，未执行上游或测量生成质量。",
      "en": "Connects content planning, slide construction and editable delivery for presentations that need further revision. The skill entry, dependencies, asset notices and web-image path fix were reviewed; no upstream code or generation-quality benchmark was run.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/hugohe3/ppt-master/blob/3af3e8ef774c4d67ee57e1306d9256d08c9ee1bf/LICENSE",
      "license_sha256": "80cefc234c1ec12a8cece4344f16300c634fa03df7891686fcf979e3828f0921",
      "source_commit": "3af3e8ef774c4d67ee57e1306d9256d08c9ee1bf",
      "reviewed_at": "2026-11-17T06:06:21.878663+00:00",
      "evidence_pinned_at": "2026-11-17T06:06:21.878663+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "MIT covers PPT Master software and workflow instructions. Bundled icons retain separate MIT, CC BY 4.0, CC0 and per-brand trademark conditions described in THIRD_PARTY_NOTICES.md. PyMuPDF is an optional AGPL-3.0 dependency; other dependencies, model services, inputs and generated media are outside the root MIT grant.",
      "files": [
        {
          "spdx": "MIT",
          "osi_approved": true,
          "source_url": "https://github.com/hugohe3/ppt-master/blob/3af3e8ef774c4d67ee57e1306d9256d08c9ee1bf/LICENSE",
          "license_sha256": "80cefc234c1ec12a8cece4344f16300c634fa03df7891686fcf979e3828f0921",
          "source_commit": "3af3e8ef774c4d67ee57e1306d9256d08c9ee1bf",
          "reviewed_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_pinned_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_status": "hash_matched",
          "scope": "MIT covers PPT Master software and workflow instructions. Bundled icons retain separate MIT, CC BY 4.0, CC0 and per-brand trademark conditions described in THIRD_PARTY_NOTICES.md. PyMuPDF is an optional AGPL-3.0 dependency; other dependencies, model services, inputs and generated media are outside the root MIT grant."
        }
      ]
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-11T08:07:23Z",
        "reviewed_at": "2026-11-17T06:06:21.878663+00:00",
        "url": "https://github.com/hugohe3/ppt-master/commit/e2820d326d049f1fcbe90523983def3d52280233",
        "qualifies": true,
        "reason": {
          "zh-CN": "网页转 Markdown 时用 URL 正斜杠拼接下载图片的相对路径，避免 Windows 的反斜杠使图片引用失效",
          "en": "Builds downloaded-image Markdown paths with URL forward slashes instead of OS-dependent joins, avoiding broken image references on Windows"
        },
        "reviewed_files": [
          "skills/ppt-master/scripts/source_to_md/web_to_md.py"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/hugohe3/ppt-master",
        "accessed_at": "2026-11-17T06:06:21.878663+00:00"
      },
      {
        "url": "https://github.com/hugohe3/ppt-master/blob/3af3e8ef774c4d67ee57e1306d9256d08c9ee1bf/README.md",
        "accessed_at": "2026-11-17T06:06:21.878663+00:00"
      },
      {
        "url": "https://github.com/hugohe3/ppt-master/blob/3af3e8ef774c4d67ee57e1306d9256d08c9ee1bf/LICENSE",
        "accessed_at": "2026-11-17T06:06:21.878663+00:00"
      },
      {
        "url": "https://github.com/hugohe3/ppt-master/commit/e2820d326d049f1fcbe90523983def3d52280233",
        "accessed_at": "2026-11-17T06:06:21.878663+00:00"
      },
      {
        "url": "https://github.com/hugohe3/ppt-master/blob/3af3e8ef774c4d67ee57e1306d9256d08c9ee1bf/skills/ppt-master/SKILL.md",
        "accessed_at": "2026-11-17T06:06:21.878663+00:00"
      },
      {
        "url": "https://github.com/hugohe3/ppt-master/blob/3af3e8ef774c4d67ee57e1306d9256d08c9ee1bf/skills/ppt-master/requirements.txt",
        "accessed_at": "2026-11-17T06:06:21.878663+00:00"
      },
      {
        "url": "https://github.com/hugohe3/ppt-master/blob/3af3e8ef774c4d67ee57e1306d9256d08c9ee1bf/skills/ppt-master/templates/icons/THIRD_PARTY_NOTICES.md",
        "accessed_at": "2026-11-17T06:06:21.878663+00:00"
      }
    ],
    "discovery": {
      "kind": "user_pdf",
      "submitted_date": "2026-11-17",
      "source_url": "https://github.com/hugohe3/ppt-master",
      "repository_url": "https://github.com/hugohe3/ppt-master",
      "source_title": "办公室 Skill 从夯到拉(纯主观)",
      "source_pages": [
        1
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOQl_Gyg",
    "full_name": "hugohe3/ppt-master",
    "stargazers_count": 77626,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "api_license_spdx": "MIT",
    "license_sha256": "80cefc234c1ec12a8cece4344f16300c634fa03df7891686fcf979e3828f0921",
    "last_success_at": "2026-11-17T05:45:14.266381+00:00"
  }
}
```

</details>
