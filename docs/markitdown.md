# MarkItDown

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[microsoft/markitdown](https://github.com/microsoft/markitdown)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 195977 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.603093Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:28.325Z |

## 中文

将多种文件转换为 Markdown 的 Python 工具。

为语言模型阅读和分析资料保留标题、列表、表格及链接。

### 主要功能

- 转换 Office、PDF、HTML 和多种文本格式。
- 提供命令行与 Python 接口，并可按格式安装依赖。
- 可接入图像描述、语音转写和 Azure 文档分析服务。

### 环境要求

- 需要 Python 3.10–3.14；按输入格式安装可选依赖。
- 图像描述和语音转写依赖在线服务。

### 使用限制

- 输出面向文本分析，不保证还原原文件的视觉版式。
- 转换器使用当前进程的文件和网络权限。处理不可信输入时需限制可访问资源。

### 开始使用

1. 按 [README](https://github.com/microsoft/markitdown#installation)安装基础包和所需格式依赖。
2. 用命令行或 Python 接口转换一个本地文件。
3. 检查 Markdown 内容；需要云端能力时再配置对应服务。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:28.325Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-07 · commit](https://github.com/microsoft/markitdown/commit/ed178952a6672abdfd35b5f9e76a80b6cefc086e)。fix: match ExifTool directories case-insensitively on Windows (#2837)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://github.com/microsoft/markitdown/blob/main/README.md)
- [Usage](https://github.com/microsoft/markitdown#usage)
- [Security considerations](https://github.com/microsoft/markitdown#security-considerations)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

A Python tool that converts multiple file formats to Markdown.

Preserves headings, lists, tables, and links for language-model reading and analysis.

### Features

- Converts Office, PDF, HTML, and several text formats.
- Provides CLI and Python interfaces with format-specific optional dependencies.
- Can integrate image descriptions, speech transcription, and Azure document analysis services.

### Requirements

- Requires Python 3.10–3.14 and optional dependencies for the input formats.
- Image captioning and speech transcription depend on online services.

### Limitations

- Output targets text analysis and does not guarantee visual fidelity to the source.
- Converters use the process's file and network permissions; restrict accessible resources for untrusted inputs.

### Getting started

1. Install the package and required format extras using the [README](https://github.com/microsoft/markitdown#installation).
2. Convert a local file through the CLI or Python API.
3. Inspect the Markdown, and configure a service if cloud capabilities are needed.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:28.325Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-07 · commit](https://github.com/microsoft/markitdown/commit/ed178952a6672abdfd35b5f9e76a80b6cefc086e).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://github.com/microsoft/markitdown/blob/main/README.md)
- [Usage](https://github.com/microsoft/markitdown#usage)
- [Security considerations](https://github.com/microsoft/markitdown#security-considerations)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.603093Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "markitdown",
    "name": "MarkItDown",
    "repository": "microsoft/markitdown",
    "repo_node_id": "R_kgDONO810w",
    "category": "productivity",
    "summary": {
      "zh-CN": "将多种文件转换为 Markdown 的 Python 工具。",
      "en": "A Python tool that converts multiple file formats to Markdown."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.603093Z",
        "en": "2026-11-17T14:24:07.603093Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "为语言模型阅读和分析资料保留标题、列表、表格及链接。",
        "en": "Preserves headings, lists, tables, and links for language-model reading and analysis."
      },
      "source_url": "https://github.com/microsoft/markitdown/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/microsoft/markitdown/commit/ed178952a6672abdfd35b5f9e76a80b6cefc086e",
        "occurred_at": "2026-11-07T00:14:01Z",
        "reviewed_at": "2026-11-17T14:24:07.603093Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "fix: match ExifTool directories case-insensitively on Windows (#2837) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/microsoft/markitdown/blob/main/README.md"
      },
      {
        "title": "Usage",
        "url": "https://github.com/microsoft/markitdown#usage"
      },
      {
        "title": "Security considerations",
        "url": "https://github.com/microsoft/markitdown#security-considerations"
      }
    ]
  },
  "snapshot": {
    "full_name": "microsoft/markitdown",
    "repo_node_id": "R_kgDONO810w",
    "stargazers_count": 195977,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:28.325Z",
    "source_url": "https://api.github.com/repos/microsoft/markitdown"
  }
}
```

</details>
