# PaddleOCR

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 92809 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.603337Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:26.933Z |

## 中文

识别图像文字并解析文档结构的 OCR 工具集。

将扫描件与复杂版式转换成语言模型和 RAG 可用的输入。

### 主要功能

- 提供多语言文字检测与识别模型。
- 解析表格、公式和版面，并输出 Markdown 或 JSON。
- 支持多种推理后端及服务化集成。

### 环境要求

- 按所选 OCR 或文档解析流水线安装 Python 依赖与模型运行后端。
- CPU、GPU 和其他加速器的支持范围需按对应部署文档核对。

### 使用限制

- 不同模型的语言、坐标信息和结构解析能力不同。
- 识别结果需用目标文档验证，公开基准成绩不代表所有输入的精度。

### 开始使用

1. 在[流水线总览](https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/pipeline_overview.html)选择文字识别或文档解析。
2. 按对应模型文档安装依赖，并运行图像或 PDF 示例。
3. 检查文字、表格和坐标，再将结构化结果接入 AI 流程。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:26.933Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-09-16 · commit](https://github.com/PaddlePaddle/PaddleOCR/commit/dab3fe35379033fdcb2d0e9572fac0b36c9a9ebf)。更新文档，去重图片并简化仓库克隆。

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://raw.githubusercontent.com/PaddlePaddle/PaddleOCR/main/README.md)
- [OCR guide](https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/OCR.html)
- [Document parsing](https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/PP-StructureV3.html)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

An OCR toolkit for recognizing image text and parsing document structure.

Converts scans and complex layouts into inputs for language models and RAG.

### Features

- Provides multilingual text detection and recognition models.
- Parses tables, formulas, and layouts with Markdown or JSON output.
- Supports multiple inference backends and service integration.

### Requirements

- Install Python dependencies and the model runtime for the selected OCR or document pipeline.
- Check the relevant deployment guide for CPU, GPU, and other accelerator support.

### Limitations

- Language coverage, coordinate detail, and structural parsing vary by model.
- Validate recognition on target documents; public benchmark scores do not establish accuracy for every input.

### Getting started

1. Choose text recognition or document parsing in the [pipeline overview](https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/pipeline_overview.html).
2. Install dependencies from that model's guide and run an image or PDF example.
3. Inspect text, tables, and coordinates, then connect the structured results to an AI workflow.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:26.933Z meets the total-Star threshold of 1,000.

Recent activity: [2026-09-16 · commit](https://github.com/PaddlePaddle/PaddleOCR/commit/dab3fe35379033fdcb2d0e9572fac0b36c9a9ebf).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://raw.githubusercontent.com/PaddlePaddle/PaddleOCR/main/README.md)
- [OCR guide](https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/OCR.html)
- [Document parsing](https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/PP-StructureV3.html)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.603337Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "paddleocr",
    "name": "PaddleOCR",
    "repository": "PaddlePaddle/PaddleOCR",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkyNjIyOTYxMjI=",
    "category": "productivity",
    "summary": {
      "zh-CN": "识别图像文字并解析文档结构的 OCR 工具集。",
      "en": "An OCR toolkit for recognizing image text and parsing document structure."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.603337Z",
        "en": "2026-11-17T14:24:07.603337Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "将扫描件与复杂版式转换成语言模型和 RAG 可用的输入。",
        "en": "Converts scans and complex layouts into inputs for language models and RAG."
      },
      "source_url": "https://raw.githubusercontent.com/PaddlePaddle/PaddleOCR/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/PaddlePaddle/PaddleOCR/commit/dab3fe35379033fdcb2d0e9572fac0b36c9a9ebf",
        "occurred_at": "2026-09-16T03:30:53Z",
        "reviewed_at": "2026-11-17T14:24:07.603337Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "更新文档，去重图片并简化仓库克隆。 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://raw.githubusercontent.com/PaddlePaddle/PaddleOCR/main/README.md"
      },
      {
        "title": "OCR guide",
        "url": "https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/OCR.html"
      },
      {
        "title": "Document parsing",
        "url": "https://www.paddleocr.ai/latest/en/version3.x/pipeline_usage/PP-StructureV3.html"
      }
    ]
  },
  "snapshot": {
    "full_name": "PaddlePaddle/PaddleOCR",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkyNjIyOTYxMjI=",
    "stargazers_count": 92809,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:26.933Z",
    "source_url": "https://api.github.com/repos/PaddlePaddle/PaddleOCR"
  }
}
```

</details>
