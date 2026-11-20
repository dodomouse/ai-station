# Unstructured

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 15755 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.603585Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:27.354Z |

## 中文

把非结构化文档拆分为内容元素的 Python 库。

为语言模型的数据准备、检索和总结提供结构化片段。

### 主要功能

- 处理 PDF、HTML、Word、图像和其他格式。
- 自动识别文件类型并路由到对应解析器。
- 提供文档分区、预处理及与数据流程的集成。

### 环境要求

- 需要 Python，或使用官方容器；按文档类型安装可选依赖。
- 图像和 PDF 可能需要 Tesseract、Poppler；Office 处理可能需要 LibreOffice。

### 使用限制

- 基础安装不包含所有格式依赖，缺少系统组件会影响解析。
- Transform API 的模型与服务独立于本地库，不能把云端效果视为本地能力。

### 开始使用

1. 按[安装文档](https://docs.unstructured.io/open-source/installation/full-installation)准备包与系统依赖。
2. 按[快速开始](https://docs.unstructured.io/open-source/introduction/quick-start)分区一个样本文档。
3. 检查元素内容与类型，再接入自己的数据预处理流程。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:27.354Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/Unstructured-IO/unstructured/commit/0c166fc21b65de8d398ff3ba13976882266916a4)。修复 JSON 内容结构检测前的 UTF-8 BOM 处理。

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://raw.githubusercontent.com/Unstructured-IO/unstructured/main/README.md)
- [Installation](https://docs.unstructured.io/open-source/installation/full-installation)
- [Quickstart](https://docs.unstructured.io/open-source/introduction/quick-start)

## English

A Python library that partitions unstructured documents into content elements.

Prepares structured segments for language-model data processing, retrieval, and summarization.

### Features

- Processes PDF, HTML, Word, images, and other formats.
- Detects file types and routes them to the appropriate parser.
- Provides document partitioning, preprocessing, and data-pipeline integration.

### Requirements

- Requires Python or an official container; install extras for the document types.
- Images and PDFs may require Tesseract and Poppler; Office processing may require LibreOffice.

### Limitations

- The base installation does not include every format dependency; missing system components affect parsing.
- Transform API models and services are separate from the local library; cloud results do not establish local capabilities.

### Getting started

1. Prepare package and system dependencies using the [installation guide](https://docs.unstructured.io/open-source/installation/full-installation).
2. Partition a sample document using the [quickstart](https://docs.unstructured.io/open-source/introduction/quick-start).
3. Inspect element content and types, then integrate your preprocessing workflow.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:27.354Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/Unstructured-IO/unstructured/commit/0c166fc21b65de8d398ff3ba13976882266916a4).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://raw.githubusercontent.com/Unstructured-IO/unstructured/main/README.md)
- [Installation](https://docs.unstructured.io/open-source/installation/full-installation)
- [Quickstart](https://docs.unstructured.io/open-source/introduction/quick-start)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.603585Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "unstructured",
    "name": "Unstructured",
    "repository": "Unstructured-IO/unstructured",
    "repo_node_id": "R_kgDOIEsvCg",
    "category": "productivity",
    "summary": {
      "zh-CN": "把非结构化文档拆分为内容元素的 Python 库。",
      "en": "A Python library that partitions unstructured documents into content elements."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.603585Z",
        "en": "2026-11-17T14:24:07.603585Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "为语言模型的数据准备、检索和总结提供结构化片段。",
        "en": "Prepares structured segments for language-model data processing, retrieval, and summarization."
      },
      "source_url": "https://raw.githubusercontent.com/Unstructured-IO/unstructured/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/Unstructured-IO/unstructured/commit/0c166fc21b65de8d398ff3ba13976882266916a4",
        "occurred_at": "2026-11-17T00:54:36Z",
        "reviewed_at": "2026-11-17T14:24:07.603585Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复 JSON 内容结构检测前的 UTF-8 BOM 处理。 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://raw.githubusercontent.com/Unstructured-IO/unstructured/main/README.md"
      },
      {
        "title": "Installation",
        "url": "https://docs.unstructured.io/open-source/installation/full-installation"
      },
      {
        "title": "Quickstart",
        "url": "https://docs.unstructured.io/open-source/introduction/quick-start"
      }
    ]
  },
  "snapshot": {
    "full_name": "Unstructured-IO/unstructured",
    "repo_node_id": "R_kgDOIEsvCg",
    "stargazers_count": 15755,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:27.354Z",
    "source_url": "https://api.github.com/repos/Unstructured-IO/unstructured"
  }
}
```

</details>
