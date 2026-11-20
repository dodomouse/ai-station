# Datasets

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[huggingface/datasets](https://github.com/huggingface/datasets)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 数据处理 / Data processing |
| 状态 / Status | 已收录 / Included |
| Star | 22151 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.604360Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:27.778Z |

## 中文

加载、转换和流式读取机器学习数据集的 Python 库。

为模型训练、评测及智能体轨迹分析准备可复用的数据处理流程。

### 主要功能

- 从 Hub、本地文件或 Python 对象加载数据。
- 使用映射、缓存及多进程处理文本和多模态数据。
- 提供 Arrow 数据集与流式 IterableDataset。

### 环境要求

- 需要 Python 环境。额外功能需按需安装依赖，例如音频与视频处理。
- 远程数据需可访问对应来源；本地处理需准备存储空间。

### 使用限制

- 流式数据按迭代读取，不具备普通 Dataset 的全部随机访问行为。
- 上游数据可变化。可复现实验应固定数据仓库的 revision。

### 开始使用

1. 按[安装说明](https://huggingface.co/docs/datasets/installation)安装所需功能。
2. 按[快速开始](https://huggingface.co/docs/datasets/quickstart)加载样本并查看字段。
3. 编写转换函数，并选择缓存或[流式读取](https://huggingface.co/docs/datasets/stream)。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:27.778Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/huggingface/datasets/commit/167807008ac3aa96f9b377efde58767e53a7f3b3)。Support STS session traces (#9065)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://github.com/huggingface/datasets/blob/main/README.md)
- [Installation](https://huggingface.co/docs/datasets/installation)
- [Quickstart](https://huggingface.co/docs/datasets/quickstart)
- [Streaming](https://huggingface.co/docs/datasets/stream)

## English

A Python library for loading, transforming, and streaming machine-learning datasets.

Prepares reusable data workflows for model training, evaluation, and agent-trace analysis.

### Features

- Loads data from the Hub, local files, or Python objects.
- Processes text and multimodal data with mapping, caching, and multiprocessing.
- Provides Arrow-backed datasets and streaming IterableDataset objects.

### Requirements

- Requires Python; install optional dependencies for features such as audio and video.
- Remote data requires access to its source; local processing requires storage.

### Limitations

- Streaming data is read by iteration and does not offer every random-access behavior of a regular Dataset.
- Upstream data can change; pin the dataset repository revision for reproducible experiments.

### Getting started

1. Install the required features using the [installation guide](https://huggingface.co/docs/datasets/installation).
2. Load a sample and inspect its fields using the [quickstart](https://huggingface.co/docs/datasets/quickstart).
3. Write a transformation function and choose caching or [streaming](https://huggingface.co/docs/datasets/stream).

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:27.778Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/huggingface/datasets/commit/167807008ac3aa96f9b377efde58767e53a7f3b3).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://github.com/huggingface/datasets/blob/main/README.md)
- [Installation](https://huggingface.co/docs/datasets/installation)
- [Quickstart](https://huggingface.co/docs/datasets/quickstart)
- [Streaming](https://huggingface.co/docs/datasets/stream)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.604360Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "datasets",
    "name": "Datasets",
    "repository": "huggingface/datasets",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkyNTAyMTMyODY=",
    "category": "data",
    "summary": {
      "zh-CN": "加载、转换和流式读取机器学习数据集的 Python 库。",
      "en": "A Python library for loading, transforming, and streaming machine-learning datasets."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.604360Z",
        "en": "2026-11-17T14:24:07.604360Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "为模型训练、评测及智能体轨迹分析准备可复用的数据处理流程。",
        "en": "Prepares reusable data workflows for model training, evaluation, and agent-trace analysis."
      },
      "source_url": "https://github.com/huggingface/datasets/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/huggingface/datasets/commit/167807008ac3aa96f9b377efde58767e53a7f3b3",
        "occurred_at": "2026-11-17T13:08:56Z",
        "reviewed_at": "2026-11-17T14:24:07.604360Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "Support STS session traces (#9065) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/huggingface/datasets/blob/main/README.md"
      },
      {
        "title": "Installation",
        "url": "https://huggingface.co/docs/datasets/installation"
      },
      {
        "title": "Quickstart",
        "url": "https://huggingface.co/docs/datasets/quickstart"
      },
      {
        "title": "Streaming",
        "url": "https://huggingface.co/docs/datasets/stream"
      }
    ]
  },
  "snapshot": {
    "full_name": "huggingface/datasets",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkyNTAyMTMyODY=",
    "stargazers_count": 22151,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:27.778Z",
    "source_url": "https://api.github.com/repos/huggingface/datasets"
  }
}
```

</details>
