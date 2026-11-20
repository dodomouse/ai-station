# Sentence Transformers

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[huggingface/sentence-transformers](https://github.com/huggingface/sentence-transformers)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 数据处理 / Data processing |
| 状态 / Status | 已收录 / Included |
| Star | 19289 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.602813Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:27.424Z |

## 中文

计算、训练向量嵌入和重排序模型的 Python 库。

为语义搜索与 RAG 提供召回向量、相关性评分和排序。

### 主要功能

- 运行稠密嵌入、稀疏编码和多向量检索模型。
- 用 Cross Encoder 为查询和文档评分。
- 使用任务数据微调模型，并在训练中评测。

### 环境要求

- 官方建议 Python 3.10+、PyTorch 2.2+ 和 Transformers 5.0+。
- 需要下载所选模型；训练和不同模态可能需要额外依赖。

### 使用限制

- 模型的语言、输入类型和长度范围各不相同，需按任务选型。
- 私有或受限模型需要对应的 Hub 访问权限。

### 开始使用

1. 按[安装文档](https://www.sbert.net/docs/installation.html)配置依赖。
2. 按[快速开始](https://www.sbert.net/docs/quickstart.html)加载模型并编码样本文本。
3. 比较召回和排序结果，再决定是否微调。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:27.424Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/huggingface/sentence-transformers/commit/ea66116aeea5e827963bedaa0c38ed4a4681229a)。[fix] Resolve similarity per call in pairwise evaluators instead of latching onto the first model (#4397)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://github.com/huggingface/sentence-transformers/blob/main/README.md)
- [Installation](https://www.sbert.net/docs/installation.html)
- [Quickstart](https://www.sbert.net/docs/quickstart.html)

## English

A Python library for computing and training embeddings and rerankers.

Supplies retrieval embeddings, relevance scores, and reranking for semantic search and RAG.

### Features

- Runs dense embedding, sparse encoder, and multi-vector retrieval models.
- Scores query-document pairs with Cross Encoders.
- Fine-tunes models on task data with evaluation during training.

### Requirements

- The README recommends Python 3.10+, PyTorch 2.2+, and Transformers 5.0+.
- Download the selected model; training and additional modalities may require extras.

### Limitations

- Models differ in language, input type, and sequence-length support; select one for the task.
- Private or gated models require the appropriate Hub access.

### Getting started

1. Configure dependencies using the [installation guide](https://www.sbert.net/docs/installation.html).
2. Load a model and encode sample text using the [quickstart](https://www.sbert.net/docs/quickstart.html).
3. Compare retrieval and ranking results before deciding whether to fine-tune.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:27.424Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/huggingface/sentence-transformers/commit/ea66116aeea5e827963bedaa0c38ed4a4681229a).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://github.com/huggingface/sentence-transformers/blob/main/README.md)
- [Installation](https://www.sbert.net/docs/installation.html)
- [Quickstart](https://www.sbert.net/docs/quickstart.html)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.602813Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "sentence-transformers",
    "name": "Sentence Transformers",
    "repository": "huggingface/sentence-transformers",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkxOTg2MTY5Nzg=",
    "category": "data",
    "summary": {
      "zh-CN": "计算、训练向量嵌入和重排序模型的 Python 库。",
      "en": "A Python library for computing and training embeddings and rerankers."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.602813Z",
        "en": "2026-11-17T14:24:07.602813Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "为语义搜索与 RAG 提供召回向量、相关性评分和排序。",
        "en": "Supplies retrieval embeddings, relevance scores, and reranking for semantic search and RAG."
      },
      "source_url": "https://github.com/huggingface/sentence-transformers/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/huggingface/sentence-transformers/commit/ea66116aeea5e827963bedaa0c38ed4a4681229a",
        "occurred_at": "2026-11-17T13:02:00Z",
        "reviewed_at": "2026-11-17T14:24:07.602813Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "[fix] Resolve similarity per call in pairwise evaluators instead of latching onto the first model (#4397) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/huggingface/sentence-transformers/blob/main/README.md"
      },
      {
        "title": "Installation",
        "url": "https://www.sbert.net/docs/installation.html"
      },
      {
        "title": "Quickstart",
        "url": "https://www.sbert.net/docs/quickstart.html"
      }
    ]
  },
  "snapshot": {
    "full_name": "huggingface/sentence-transformers",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkxOTg2MTY5Nzg=",
    "stargazers_count": 19289,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:27.424Z",
    "source_url": "https://api.github.com/repos/huggingface/sentence-transformers"
  }
}
```

</details>
