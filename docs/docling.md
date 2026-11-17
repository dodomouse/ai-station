# Docling

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[docling-project/docling](https://github.com/docling-project/docling)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 70696 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.602539Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:26.525Z |

## 中文

解析文档版面与内容，并导出结构化结果的工具。

把 PDF、Office 文件、图像和音频转成 AI 可处理的资料。

### 主要功能

- 提取 PDF 内容，包括阅读顺序、表格、公式和代码。
- 支持扫描件文字识别及音频语音识别。
- 导出 Markdown、HTML 和 JSON，并可接入智能体框架。

### 环境要求

- 需要 Python 3.10 或更高版本。支持 macOS、Linux 和 Windows。
- 按解析任务准备所需模型；离线部署需预先备齐资源。

### 使用限制

- 不同格式和模型支持的提取能力不同，应检查样本文档的阅读顺序与表格。

### 开始使用

1. 按[安装说明](https://docling-project.github.io/docling/getting_started/installation/)安装 Docling。
2. 用 README 中的命令行或 Python 示例转换一个文档。
3. 查看输出，再按[示例](https://docling-project.github.io/docling/examples/)接入检索或智能体流程。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:26.525Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/docling-project/docling/commit/48f272b99c90616222901a0f3ee73bf367d0c592)。fix(html): add the quotation marks of inline quotations (#5388)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://github.com/docling-project/docling/blob/main/README.md)
- [Installation](https://docling-project.github.io/docling/getting_started/installation/)
- [Examples](https://docling-project.github.io/docling/examples/)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

A document parser that extracts layout and content into structured outputs.

Prepares PDFs, Office files, images, and audio for AI processing.

### Features

- Extracts PDF reading order, tables, formulas, code, and other content.
- Supports OCR for scans and speech recognition for audio.
- Exports Markdown, HTML, and JSON and integrates with agent frameworks.

### Requirements

- Requires Python 3.10 or later on macOS, Linux, or Windows.
- Prepare models for the chosen parsing tasks; provision resources before offline deployment.

### Limitations

- Extraction capabilities vary by format and model; inspect reading order and tables on sample documents.

### Getting started

1. Install Docling using the [installation guide](https://docling-project.github.io/docling/getting_started/installation/).
2. Convert a document using the README's CLI or Python example.
3. Inspect the output, then use the [examples](https://docling-project.github.io/docling/examples/) to integrate retrieval or agent workflows.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:26.525Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/docling-project/docling/commit/48f272b99c90616222901a0f3ee73bf367d0c592).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://github.com/docling-project/docling/blob/main/README.md)
- [Installation](https://docling-project.github.io/docling/getting_started/installation/)
- [Examples](https://docling-project.github.io/docling/examples/)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.602539Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "docling",
    "name": "Docling",
    "repository": "docling-project/docling",
    "repo_node_id": "R_kgDOMT5TYA",
    "category": "productivity",
    "summary": {
      "zh-CN": "解析文档版面与内容，并导出结构化结果的工具。",
      "en": "A document parser that extracts layout and content into structured outputs."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.602539Z",
        "en": "2026-11-17T14:24:07.602539Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "把 PDF、Office 文件、图像和音频转成 AI 可处理的资料。",
        "en": "Prepares PDFs, Office files, images, and audio for AI processing."
      },
      "source_url": "https://github.com/docling-project/docling/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/docling-project/docling/commit/48f272b99c90616222901a0f3ee73bf367d0c592",
        "occurred_at": "2026-11-17T10:35:08Z",
        "reviewed_at": "2026-11-17T14:24:07.602539Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "fix(html): add the quotation marks of inline quotations (#5388) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/docling-project/docling/blob/main/README.md"
      },
      {
        "title": "Installation",
        "url": "https://docling-project.github.io/docling/getting_started/installation/"
      },
      {
        "title": "Examples",
        "url": "https://docling-project.github.io/docling/examples/"
      }
    ]
  },
  "snapshot": {
    "full_name": "docling-project/docling",
    "repo_node_id": "R_kgDOMT5TYA",
    "stargazers_count": 70696,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:26.525Z",
    "source_url": "https://api.github.com/repos/docling-project/docling"
  }
}
```

</details>
