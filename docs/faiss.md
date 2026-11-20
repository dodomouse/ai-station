# Faiss

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[facebookresearch/faiss](https://github.com/facebookresearch/faiss)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 数据处理 / Data processing |
| 状态 / Status | 已收录 / Included |
| Star | 41767 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.602639Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:26.402Z |

## 中文

用于稠密向量相似度搜索和聚类的库。

为嵌入召回构建索引，并比较检索速度、内存与召回质量。

### 主要功能

- 提供精确搜索、近似索引及向量压缩方法。
- 支持 L2 距离和内积；归一化向量可用于余弦相似度。
- 提供 C++ 接口、Python 包装及部分算法的 GPU 实现。

### 环境要求

- C++ 构建依赖 BLAS。Python 可使用预编译包；GPU 功能需匹配 CUDA 或 ROCm。

### 使用限制

- Faiss 接收向量，不负责生成文本嵌入。
- 压缩和近似索引需权衡速度、内存与搜索精度。部分索引需要训练。

### 开始使用

1. 按[安装说明](https://github.com/facebookresearch/faiss/blob/main/INSTALL.md)选择 CPU 或 GPU 包。
2. 按[入门教程](https://github.com/facebookresearch/faiss/wiki/Getting-started)准备向量并创建索引。
3. 添加向量、运行查询，再用样本比较不同索引参数。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:26.402Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-16 · commit](https://github.com/facebookresearch/faiss/commit/c8f283867285af547db7a701c1b8dfa89631b3ea)。Add IndexIVFRaBitQSSD: IVF-RaBitQ with codes split across RAM and SSD (#5746)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://github.com/facebookresearch/faiss/blob/main/README.md)
- [Installation](https://github.com/facebookresearch/faiss/blob/main/INSTALL.md)
- [Getting started](https://github.com/facebookresearch/faiss/wiki/Getting-started)

## English

A library for similarity search and clustering of dense vectors.

Builds indexes for embedding retrieval and helps compare speed, memory use, and retrieval quality.

### Features

- Provides exact search, approximate indexes, and vector compression methods.
- Supports L2 distance and inner products; normalized vectors enable cosine similarity.
- Provides C++ interfaces, Python wrappers, and GPU implementations of selected algorithms.

### Requirements

- C++ builds require BLAS. Python can use prebuilt packages; GPU features require compatible CUDA or ROCm.

### Limitations

- Faiss consumes vectors rather than generating text embeddings.
- Compressed and approximate indexes trade accuracy against speed and memory; some indexes require training.

### Getting started

1. Choose a CPU or GPU package using the [installation guide](https://github.com/facebookresearch/faiss/blob/main/INSTALL.md).
2. Prepare vectors and create an index using the [getting-started tutorial](https://github.com/facebookresearch/faiss/wiki/Getting-started).
3. Add vectors, run queries, and compare index parameters on representative samples.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:26.402Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-16 · commit](https://github.com/facebookresearch/faiss/commit/c8f283867285af547db7a701c1b8dfa89631b3ea).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://github.com/facebookresearch/faiss/blob/main/README.md)
- [Installation](https://github.com/facebookresearch/faiss/blob/main/INSTALL.md)
- [Getting started](https://github.com/facebookresearch/faiss/wiki/Getting-started)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.602639Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "faiss",
    "name": "Faiss",
    "repository": "facebookresearch/faiss",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnk4MTIyNzAwNQ==",
    "category": "data",
    "summary": {
      "zh-CN": "用于稠密向量相似度搜索和聚类的库。",
      "en": "A library for similarity search and clustering of dense vectors."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.602639Z",
        "en": "2026-11-17T14:24:07.602639Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "为嵌入召回构建索引，并比较检索速度、内存与召回质量。",
        "en": "Builds indexes for embedding retrieval and helps compare speed, memory use, and retrieval quality."
      },
      "source_url": "https://github.com/facebookresearch/faiss/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/facebookresearch/faiss/commit/c8f283867285af547db7a701c1b8dfa89631b3ea",
        "occurred_at": "2026-11-16T20:48:07Z",
        "reviewed_at": "2026-11-17T14:24:07.602639Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "Add IndexIVFRaBitQSSD: IVF-RaBitQ with codes split across RAM and SSD (#5746) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/facebookresearch/faiss/blob/main/README.md"
      },
      {
        "title": "Installation",
        "url": "https://github.com/facebookresearch/faiss/blob/main/INSTALL.md"
      },
      {
        "title": "Getting started",
        "url": "https://github.com/facebookresearch/faiss/wiki/Getting-started"
      }
    ]
  },
  "snapshot": {
    "full_name": "facebookresearch/faiss",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnk4MTIyNzAwNQ==",
    "stargazers_count": 41767,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:26.402Z",
    "source_url": "https://api.github.com/repos/facebookresearch/faiss"
  }
}
```

</details>
