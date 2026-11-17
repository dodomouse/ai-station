# LanceDB

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[lancedb/lancedb](https://github.com/lancedb/lancedb)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 数据处理 / Data processing |
| 状态 / Status | 已收录 / Included |
| Star | 11913 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.602999Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:27.320Z |

## 中文

基于 Lance 列式格式管理向量和多模态数据的数据库。

把向量检索、全文检索和数据分析接入 AI 应用。

### 主要功能

- 存储多种数据，包括向量、元数据、文本、图像和视频。
- 提供向量搜索、全文搜索和 SQL 查询能力。
- 支持数据版本和工具集成，例如 Arrow 与 Pandas。

### 环境要求

- 嵌入式版本运行在应用进程中，数据可存于本地磁盘或对象存储。
- 提供 Python、TypeScript 和 Rust SDK。

### 使用限制

- 企业版的分布式检索、索引和维护能力属于单独产品。
- 索引和存储配置需按数据规模及查询方式选择。

### 开始使用

1. 按[快速开始](https://docs.lancedb.com/quickstart)安装 SDK 并连接数据库路径。
2. 创建表并写入样本向量与元数据。
3. 测试向量或全文查询，再按[文档](https://docs.lancedb.com)配置索引。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:27.320Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/lancedb/lancedb/commit/1670859327d5503e8bf7e02c58f93260da4881b4)。fix(deps): ignore unmaintained chrono family advisories (#5073)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://github.com/lancedb/lancedb/blob/main/README.md)
- [Quickstart](https://docs.lancedb.com/quickstart)
- [Documentation](https://docs.lancedb.com)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

A database built on the Lance columnar format for vectors and multimodal data.

Brings vector search, full-text search, and data analysis into AI applications.

### Features

- Stores vectors, metadata, text, images, video, and other data.
- Provides vector search, full-text search, and SQL querying.
- Supports data versions and integrates with tools such as Arrow and Pandas.

### Requirements

- The embedded version runs inside the application process with data on local disk or object storage.
- Provides Python, TypeScript, and Rust SDKs.

### Limitations

- Distributed search, indexing, and maintenance in the enterprise edition belong to a separate product.
- Choose indexing and storage configurations for the data scale and query pattern.

### Getting started

1. Install an SDK and connect to a database path using the [quickstart](https://docs.lancedb.com/quickstart).
2. Create a table and insert sample vectors and metadata.
3. Test vector or full-text queries, then configure indexes using the [documentation](https://docs.lancedb.com).

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:27.320Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/lancedb/lancedb/commit/1670859327d5503e8bf7e02c58f93260da4881b4).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://github.com/lancedb/lancedb/blob/main/README.md)
- [Quickstart](https://docs.lancedb.com/quickstart)
- [Documentation](https://docs.lancedb.com)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.602999Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "lancedb",
    "name": "LanceDB",
    "repository": "lancedb/lancedb",
    "repo_node_id": "R_kgDOJDTTIg",
    "category": "data",
    "summary": {
      "zh-CN": "基于 Lance 列式格式管理向量和多模态数据的数据库。",
      "en": "A database built on the Lance columnar format for vectors and multimodal data."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.602999Z",
        "en": "2026-11-17T14:24:07.602999Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "把向量检索、全文检索和数据分析接入 AI 应用。",
        "en": "Brings vector search, full-text search, and data analysis into AI applications."
      },
      "source_url": "https://github.com/lancedb/lancedb/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/lancedb/lancedb/commit/1670859327d5503e8bf7e02c58f93260da4881b4",
        "occurred_at": "2026-11-17T12:58:43Z",
        "reviewed_at": "2026-11-17T14:24:07.602999Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "fix(deps): ignore unmaintained chrono family advisories (#5073) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/lancedb/lancedb/blob/main/README.md"
      },
      {
        "title": "Quickstart",
        "url": "https://docs.lancedb.com/quickstart"
      },
      {
        "title": "Documentation",
        "url": "https://docs.lancedb.com"
      }
    ]
  },
  "snapshot": {
    "full_name": "lancedb/lancedb",
    "repo_node_id": "R_kgDOJDTTIg",
    "stargazers_count": 11913,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:27.320Z",
    "source_url": "https://api.github.com/repos/lancedb/lancedb"
  }
}
```

</details>
