# MinerU

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[opendatalab/MinerU](https://github.com/opendatalab/MinerU)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 83808 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.603260Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:27.579Z |

## 中文

将复杂文档解析为结构化内容，并提供文档库和读取接口的工具。

帮助智能体读取长文档、识别扫描件，并按页或内容块保留引用位置。

### 主要功能

- 解析 PDF、图像及多种 Office、网页和电子书格式。
- 提供分档解析、文档搜索及按页或内容块继续读取。
- 提供 Python SDK、API、命令行与 Web 界面。

### 环境要求

- 需要 Python 3.11–3.14；支持 Windows、Linux 和 macOS。
- 模型后端与加速方式取决于硬件和解析档位。

### 使用限制

- PDF 和图像支持四种档位，Office 等格式使用本地 Flash 解析。
- `mineru parse` 默认读取前 10 页，需按返回位置继续。不同接口支持的导出格式也有区别。

### 开始使用

1. 按[安装指南](https://opendatalab.github.io/MinerU/quick_start/)安装并选择合适的运行环境。
2. 按[档位说明](https://opendatalab.github.io/MinerU/usage/tiers/)解析样本文档。
3. 检查结果与引用位置，再按 [SDK/API 指南](https://opendatalab.github.io/MinerU/usage/sdk_api/)接入应用。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:27.579Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-16 · commit](https://github.com/opendatalab/MinerU/commit/b4efa4b2b76ebb012c476b79bdfc6f18a95aacd6)。chore: sync recent releases in issue templates

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://github.com/opendatalab/MinerU/blob/master/README.md)
- [Installation](https://opendatalab.github.io/MinerU/quick_start/)
- [Tiers](https://opendatalab.github.io/MinerU/usage/tiers/)
- [SDK and API](https://opendatalab.github.io/MinerU/usage/sdk_api/)

## English

A tool for parsing complex documents into structured content, with a document library and reading interfaces.

Helps agents read long documents, recognize scans, and retain page or block references.

### Features

- Parses PDFs, images, and multiple Office, web, and ebook formats.
- Provides parsing tiers, document search, and page or block continuation.
- Provides a Python SDK, API, CLI, and web interface.

### Requirements

- Requires Python 3.11–3.14 on Windows, Linux, or macOS.
- Model backends and acceleration depend on hardware and parsing tier.

### Limitations

- PDFs and images support four tiers; formats such as Office use local Flash parsing.
- `mineru parse` defaults to the first 10 pages and requires continuation; export formats also vary by interface.

### Getting started

1. Install and select a runtime using the [installation guide](https://opendatalab.github.io/MinerU/quick_start/).
2. Parse a sample document using the [tier guide](https://opendatalab.github.io/MinerU/usage/tiers/).
3. Inspect results and citation locations, then integrate using the [SDK/API guide](https://opendatalab.github.io/MinerU/usage/sdk_api/).

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:27.579Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-16 · commit](https://github.com/opendatalab/MinerU/commit/b4efa4b2b76ebb012c476b79bdfc6f18a95aacd6).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://github.com/opendatalab/MinerU/blob/master/README.md)
- [Installation](https://opendatalab.github.io/MinerU/quick_start/)
- [Tiers](https://opendatalab.github.io/MinerU/usage/tiers/)
- [SDK and API](https://opendatalab.github.io/MinerU/usage/sdk_api/)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.603260Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "mineru",
    "name": "MinerU",
    "repository": "opendatalab/MinerU",
    "repo_node_id": "R_kgDOLZpAvQ",
    "category": "productivity",
    "summary": {
      "zh-CN": "将复杂文档解析为结构化内容，并提供文档库和读取接口的工具。",
      "en": "A tool for parsing complex documents into structured content, with a document library and reading interfaces."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.603260Z",
        "en": "2026-11-17T14:24:07.603260Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "帮助智能体读取长文档、识别扫描件，并按页或内容块保留引用位置。",
        "en": "Helps agents read long documents, recognize scans, and retain page or block references."
      },
      "source_url": "https://github.com/opendatalab/MinerU/blob/master/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/opendatalab/MinerU/commit/b4efa4b2b76ebb012c476b79bdfc6f18a95aacd6",
        "occurred_at": "2026-11-16T18:13:52Z",
        "reviewed_at": "2026-11-17T14:24:07.603260Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "chore: sync recent releases in issue templates 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/opendatalab/MinerU/blob/master/README.md"
      },
      {
        "title": "Installation",
        "url": "https://opendatalab.github.io/MinerU/quick_start/"
      },
      {
        "title": "Tiers",
        "url": "https://opendatalab.github.io/MinerU/usage/tiers/"
      },
      {
        "title": "SDK and API",
        "url": "https://opendatalab.github.io/MinerU/usage/sdk_api/"
      }
    ]
  },
  "snapshot": {
    "full_name": "opendatalab/MinerU",
    "repo_node_id": "R_kgDOLZpAvQ",
    "stargazers_count": 83808,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:27.579Z",
    "source_url": "https://api.github.com/repos/opendatalab/MinerU"
  }
}
```

</details>
