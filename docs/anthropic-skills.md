# Anthropic Skills

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[anthropics/skills](https://github.com/anthropics/skills)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 196194 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-17T06:06:21.887249+00:00 |

## 中文

Anthropic 的智能体技能示例仓库；本条重点收录当前采用 Apache 2.0 的 Word、PDF、PowerPoint 和表格文档技能及辅助脚本。

### 用途与功能

- 指导智能体创建、读取和修改文档，提供 OOXML 解包、结构校验及办公软件转换脚本。
- 演示文稿和 Word 流程结合渲染检查；表格流程包含公式重算和结果检查。
- PDF 技能覆盖文本和表格提取、拆分合并、表单及扫描件 OCR 等任务。

### 环境与限制

需要能读取技能并运行脚本的智能体。不同任务需 Python、Node.js、docx/pptxgenjs、openpyxl、LibreOffice、Poppler 或 OCR 依赖；文档中的“预装”描述针对上游环境，本地需自行核实。字体、公式及 Office 与 LibreOffice 差异可能影响结果；云端智能体处理文件时需考虑资料外发和费用。技能示例不保证与托管 Claude 功能完全一致。

### 开始使用

按 README 在 Claude Code 添加 anthropics/skills 插件市场并安装 document-skills，或按宿主方式载入所需技能目录。核对依赖后从样例文档开始，保留原件并检查生成文件、公式和渲染结果。

参阅[官方 README](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/README.md)。

### 收录与来源

提供具体的文件操作步骤和校验脚本，适合研究文档型智能体工作流。当前四个文档技能已于 2026-11-06 改为 Apache 2.0；已核对许可和最近脚本补丁，未执行上游，也未做安全审计。

维护证据：[Office 校验器在比较前先安全解包原始文件；渲染包装器在临时副本中改写非 HTTP(S)/mailto 的外部关系，并限制关系 XML 读取大小，保留源文件](https://github.com/anthropics/skills/commit/e4bb5d960d87126ff3b3a8af1a104b7db67560ba)（2026-11-16）。

仓库来自用户于 2026-11-17 提供的办公技能 PDF，已另行核对上游。本条按工程通用标准复核，不设 Star 门槛。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Anthropic’s agent-skill example repository; this entry focuses on the currently Apache-2.0-licensed Word, PDF, PowerPoint and spreadsheet skills and helper scripts.

### Uses and features

- Guides agents through document creation, reading and editing with OOXML unpacking, structural validation and office-conversion scripts.
- Presentation and Word workflows include render checks; spreadsheet workflows include formula recalculation and result checks.
- PDF guidance covers text and table extraction, splitting and merging, forms and scanned-page OCR.

### Requirements and limits

Requires an agent able to read skills and execute scripts. Tasks may need Python, Node.js, docx/pptxgenjs, openpyxl, LibreOffice, Poppler or OCR dependencies. “Preinstalled” claims refer to the upstream environment and must be checked locally. Fonts, formulas and Office/LibreOffice differences can affect results; cloud agents may send document content externally and incur fees. These examples are not guaranteed to match hosted Claude behavior.

### Getting started

Follow the README to add the anthropics/skills marketplace and install document-skills in Claude Code, or load the required skill folders using your host’s mechanism. Check dependencies, start with a sample document, preserve the original and inspect generated files, formulas and renders.

See the [official README](https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/README.md).

### Review and provenance

Provides concrete file-operation workflows and validation scripts for document-oriented agents. The four document skills moved to Apache 2.0 on 2026-11-06. Their licenses and recent script patches were reviewed; upstream execution and a security audit were not performed.

Maintenance evidence: [Validates original Office packages by unpacking them before comparison; the rendering wrapper rewrites external relationships other than HTTP(S)/mailto in temporary copies and bounds relationship-XML reads while preserving the input file](https://github.com/anthropics/skills/commit/e4bb5d960d87126ff3b3a8af1a104b7db67560ba) (2026-11-16).

Identified in an office-skills PDF supplied by the user on 2026-11-17, independently checked against upstream sources and reviewed against the general catalog criteria, with no star threshold.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T06:06:21.887249+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "anthropic-skills",
    "name": "Anthropic Skills",
    "repository": "anthropics/skills",
    "repo_node_id": "R_kgDOP0wfhg",
    "category": "productivity",
    "summary": {
      "zh-CN": "Anthropic 的智能体技能示例仓库；本条重点收录当前采用 Apache 2.0 的 Word、PDF、PowerPoint 和表格文档技能及辅助脚本。",
      "en": "Anthropic’s agent-skill example repository; this entry focuses on the currently Apache-2.0-licensed Word, PDF, PowerPoint and spreadsheet skills and helper scripts."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T06:06:21.887249+00:00",
        "en": "2026-11-17T06:06:21.887249+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "提供具体的文件操作步骤和校验脚本，适合研究文档型智能体工作流。当前四个文档技能已于 2026-11-06 改为 Apache 2.0；已核对许可和最近脚本补丁，未执行上游，也未做安全审计。",
      "en": "Provides concrete file-operation workflows and validation scripts for document-oriented agents. The four document skills moved to Apache 2.0 on 2026-11-06. Their licenses and recent script patches were reviewed; upstream execution and a security audit were not performed.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "source_url": "https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/pptx/LICENSE.txt",
      "license_sha256": "58d1e17ffe5109a7ae296caafcadfdbe6a7d176f0bc4ab01e12a689b0499d8bd",
      "source_commit": "e4bb5d960d87126ff3b3a8af1a104b7db67560ba",
      "reviewed_at": "2026-11-17T06:06:21.887249+00:00",
      "evidence_pinned_at": "2026-11-17T06:06:21.887249+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "This approval covers skills/docx, skills/pdf, skills/pptx and skills/xlsx, each with a pinned Apache-2.0 LICENSE.txt at the current head. Their previous source-available terms were replaced on 2026-11-06. It does not assert a blanket root license for every repository file, font or example asset; other components, dependencies, model services and user documents retain their own terms.",
      "files": [
        {
          "spdx": "Apache-2.0",
          "osi_approved": true,
          "source_url": "https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/pptx/LICENSE.txt",
          "license_sha256": "58d1e17ffe5109a7ae296caafcadfdbe6a7d176f0bc4ab01e12a689b0499d8bd",
          "source_commit": "e4bb5d960d87126ff3b3a8af1a104b7db67560ba",
          "reviewed_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_pinned_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_status": "hash_matched",
          "scope": "This approval covers skills/docx, skills/pdf, skills/pptx and skills/xlsx, each with a pinned Apache-2.0 LICENSE.txt at the current head. Their previous source-available terms were replaced on 2026-11-06. It does not assert a blanket root license for every repository file, font or example asset; other components, dependencies, model services and user documents retain their own terms."
        },
        {
          "scope": "skills/docx document skill and scripts",
          "spdx": "Apache-2.0",
          "osi_approved": true,
          "source_url": "https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/docx/LICENSE.txt",
          "license_sha256": "58d1e17ffe5109a7ae296caafcadfdbe6a7d176f0bc4ab01e12a689b0499d8bd",
          "source_commit": "e4bb5d960d87126ff3b3a8af1a104b7db67560ba",
          "reviewed_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_pinned_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_status": "hash_matched"
        },
        {
          "scope": "skills/pdf document skill and scripts",
          "spdx": "Apache-2.0",
          "osi_approved": true,
          "source_url": "https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/pdf/LICENSE.txt",
          "license_sha256": "58d1e17ffe5109a7ae296caafcadfdbe6a7d176f0bc4ab01e12a689b0499d8bd",
          "source_commit": "e4bb5d960d87126ff3b3a8af1a104b7db67560ba",
          "reviewed_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_pinned_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_status": "hash_matched"
        },
        {
          "scope": "skills/xlsx document skill and scripts",
          "spdx": "Apache-2.0",
          "osi_approved": true,
          "source_url": "https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/xlsx/LICENSE.txt",
          "license_sha256": "58d1e17ffe5109a7ae296caafcadfdbe6a7d176f0bc4ab01e12a689b0499d8bd",
          "source_commit": "e4bb5d960d87126ff3b3a8af1a104b7db67560ba",
          "reviewed_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_pinned_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_status": "hash_matched"
        }
      ],
      "components": [
        {
          "scope": "skills/docx document skill and scripts",
          "spdx": "Apache-2.0",
          "osi_approved": true,
          "source_url": "https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/docx/LICENSE.txt",
          "license_sha256": "58d1e17ffe5109a7ae296caafcadfdbe6a7d176f0bc4ab01e12a689b0499d8bd",
          "source_commit": "e4bb5d960d87126ff3b3a8af1a104b7db67560ba",
          "reviewed_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_pinned_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_status": "hash_matched"
        },
        {
          "scope": "skills/pdf document skill and scripts",
          "spdx": "Apache-2.0",
          "osi_approved": true,
          "source_url": "https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/pdf/LICENSE.txt",
          "license_sha256": "58d1e17ffe5109a7ae296caafcadfdbe6a7d176f0bc4ab01e12a689b0499d8bd",
          "source_commit": "e4bb5d960d87126ff3b3a8af1a104b7db67560ba",
          "reviewed_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_pinned_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_status": "hash_matched"
        },
        {
          "scope": "skills/pptx document skill and scripts",
          "spdx": "Apache-2.0",
          "osi_approved": true,
          "source_url": "https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/pptx/LICENSE.txt",
          "license_sha256": "58d1e17ffe5109a7ae296caafcadfdbe6a7d176f0bc4ab01e12a689b0499d8bd",
          "source_commit": "e4bb5d960d87126ff3b3a8af1a104b7db67560ba",
          "reviewed_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_pinned_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_status": "hash_matched"
        },
        {
          "scope": "skills/xlsx document skill and scripts",
          "spdx": "Apache-2.0",
          "osi_approved": true,
          "source_url": "https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/xlsx/LICENSE.txt",
          "license_sha256": "58d1e17ffe5109a7ae296caafcadfdbe6a7d176f0bc4ab01e12a689b0499d8bd",
          "source_commit": "e4bb5d960d87126ff3b3a8af1a104b7db67560ba",
          "reviewed_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_pinned_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_status": "hash_matched"
        }
      ]
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-16T14:22:47Z",
        "reviewed_at": "2026-11-17T06:06:21.887249+00:00",
        "url": "https://github.com/anthropics/skills/commit/e4bb5d960d87126ff3b3a8af1a104b7db67560ba",
        "qualifies": true,
        "reason": {
          "zh-CN": "Office 校验器在比较前先安全解包原始文件；渲染包装器在临时副本中改写非 HTTP(S)/mailto 的外部关系，并限制关系 XML 读取大小，保留源文件",
          "en": "Validates original Office packages by unpacking them before comparison; the rendering wrapper rewrites external relationships other than HTTP(S)/mailto in temporary copies and bounds relationship-XML reads while preserving the input file"
        },
        "reviewed_files": [
          "skills/docx/scripts/office/soffice.py",
          "skills/docx/scripts/office/validate.py"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/anthropics/skills",
        "accessed_at": "2026-11-17T06:06:21.887249+00:00"
      },
      {
        "url": "https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/README.md",
        "accessed_at": "2026-11-17T06:06:21.887249+00:00"
      },
      {
        "url": "https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/pptx/LICENSE.txt",
        "accessed_at": "2026-11-17T06:06:21.887249+00:00"
      },
      {
        "url": "https://github.com/anthropics/skills/commit/e4bb5d960d87126ff3b3a8af1a104b7db67560ba",
        "accessed_at": "2026-11-17T06:06:21.887249+00:00"
      },
      {
        "url": "https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/docx/LICENSE.txt",
        "accessed_at": "2026-11-17T06:06:21.887249+00:00"
      },
      {
        "url": "https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/docx/SKILL.md",
        "accessed_at": "2026-11-17T06:06:21.887249+00:00"
      },
      {
        "url": "https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/pdf/LICENSE.txt",
        "accessed_at": "2026-11-17T06:06:21.887249+00:00"
      },
      {
        "url": "https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/pdf/SKILL.md",
        "accessed_at": "2026-11-17T06:06:21.887249+00:00"
      },
      {
        "url": "https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/pptx/SKILL.md",
        "accessed_at": "2026-11-17T06:06:21.887249+00:00"
      },
      {
        "url": "https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/xlsx/LICENSE.txt",
        "accessed_at": "2026-11-17T06:06:21.887249+00:00"
      },
      {
        "url": "https://github.com/anthropics/skills/blob/e4bb5d960d87126ff3b3a8af1a104b7db67560ba/skills/xlsx/SKILL.md",
        "accessed_at": "2026-11-17T06:06:21.887249+00:00"
      }
    ],
    "discovery": {
      "kind": "user_pdf",
      "submitted_date": "2026-11-17",
      "source_url": "https://github.com/anthropics/skills",
      "repository_url": "https://github.com/anthropics/skills",
      "source_title": "办公室 Skill 从夯到拉(纯主观)",
      "source_pages": [
        1,
        3,
        4,
        5,
        9,
        10
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOP0wfhg",
    "full_name": "anthropics/skills",
    "stargazers_count": 196194,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "api_license_spdx": null,
    "license_sha256": "58d1e17ffe5109a7ae296caafcadfdbe6a7d176f0bc4ab01e12a689b0499d8bd",
    "last_success_at": "2026-11-17T05:44:00.108573+00:00"
  }
}
```

</details>
