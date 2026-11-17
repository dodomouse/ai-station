# Code-Graph-RAG

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[vitali87/code-graph-rag](https://github.com/vitali87/code-graph-rag)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 5369 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T06:06:21.875414+00:00 |

## 中文

将多语言代码仓库解析为知识图谱，供智能体检索代码结构、回答问题和辅助修改。

### 用途与功能

- 用 Tree-sitter 提取定义、导入和调用关系，支持增量更新及可选编译器信息、运行时轨迹。
- 通过 CLI 或 MCP 查询定义、调用方和被调用方；自然语言查询可由模型生成 Cypher。
- 提供语义检索、AST 结构搜索和代码编辑工具，并可用只读 MCP 模式限制写操作。

### 环境与限制

需要 CPython 3.12+、ripgrep 和受 cgr-graph-rs 原生包支持的平台：Linux x86_64/aarch64、macOS 或 Windows x64。默认 SQLite 图存储无需服务器；Memgraph、Neo4j、语义检索与编译器分析需另配依赖。索引和确定性 MCP 查询不要求模型；自然语言查询需本地模型服务或云 API。语言和调用关系覆盖并不完整，运行时轨迹只反映实际执行的代码；云模型和网页搜索可能向外部服务发送内容。

### 开始使用

用 uv tool install 安装 code-graph-rag 及所需语言扩展，配置问答模型后运行 `cgr start --repo-path /path/to/repo --update-graph` 建图，再用同命令去掉 --update-graph 查询。已有索引可通过 `cgr mcp-server --read-only` 接入智能体。

参阅[官方 README](https://github.com/vitali87/code-graph-rag/blob/b65e009f8c687d3addf3dadf553e9145944b34cb/README.md)。

### 收录与来源

把代码关系和原始源码关联起来，提供不依赖模型的精确名称查询，以及基于图谱的自然语言入口，便于调查陌生仓库和修改影响。已核对增量图更新源码与回归用例，未安装运行。

维护证据：[修复增量图更新：清理标记已存在但无法更新时间时保留待清理状态，不再触发删除目录时间缓存的回退，避免下一轮不必要的全量重解析](https://github.com/vitali87/code-graph-rag/commit/b5b3ff7273484c47b22168bc9a581ebd80b0e457)（2026-11-16）。

用户于 2026-11-17 提供仓库链接。本条按工程通用标准复核，不设 Star 门槛。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Parses multilingual repositories into a knowledge graph for agents to retrieve code structure, answer questions and assist with edits.

### Uses and features

- Extracts definitions, imports and calls with Tree-sitter, with incremental updates and optional compiler facts or runtime traces.
- Queries definitions, callers and callees through CLI or MCP; model-generated Cypher supports natural-language questions.
- Provides semantic retrieval, AST-based search and editing tools, with a read-only MCP mode that disables writes.

### Requirements and limits

Requires CPython 3.12+, ripgrep and a platform supported by cgr-graph-rs wheels: Linux x86_64/aarch64, macOS or Windows x64. Default SQLite storage needs no server; Memgraph, Neo4j, semantic search and compiler analysis require additional dependencies. Indexing and deterministic MCP queries need no model; natural-language queries need a local model service or cloud API. Language and call-graph coverage is incomplete, runtime traces only cover executed code, and cloud models or web search may send content to external services.

### Getting started

Install code-graph-rag and the required language extras with uv tool install. Configure a model for questions, run `cgr start --repo-path /path/to/repo --update-graph` to index, then omit --update-graph to query. Expose an existing index to an agent with `cgr mcp-server --read-only`.

See the [official README](https://github.com/vitali87/code-graph-rag/blob/b65e009f8c687d3addf3dadf553e9145944b34cb/README.md).

### Review and provenance

Connects code relationships to source and combines model-free exact-name queries with a graph-backed natural-language interface for exploring unfamiliar code and change impact. Incremental graph-update source and regression cases were reviewed; the software was not installed or run.

Maintenance evidence: [Fixes incremental graph updates so an existing cleanup marker whose timestamp cannot be refreshed still records pending cleanup, avoiding the directory-mtime-cache fallback and an unnecessary full reparse on the next run](https://github.com/vitali87/code-graph-rag/commit/b5b3ff7273484c47b22168bc9a581ebd80b0e457) (2026-11-16).

Submitted by the user on 2026-11-17 and reviewed against the general catalog criteria, with no star threshold.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T06:06:21.875414+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "code-graph-rag",
    "name": "Code-Graph-RAG",
    "repository": "vitali87/code-graph-rag",
    "repo_node_id": "R_kgDOO8k4_w",
    "category": "development",
    "summary": {
      "zh-CN": "将多语言代码仓库解析为知识图谱，供智能体检索代码结构、回答问题和辅助修改。",
      "en": "Parses multilingual repositories into a knowledge graph for agents to retrieve code structure, answer questions and assist with edits."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T06:06:21.875414+00:00",
        "en": "2026-11-17T06:06:21.875414+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "把代码关系和原始源码关联起来，提供不依赖模型的精确名称查询，以及基于图谱的自然语言入口，便于调查陌生仓库和修改影响。已核对增量图更新源码与回归用例，未安装运行。",
      "en": "Connects code relationships to source and combines model-free exact-name queries with a graph-backed natural-language interface for exploring unfamiliar code and change impact. Incremental graph-update source and regression cases were reviewed; the software was not installed or run.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/vitali87/code-graph-rag/blob/b65e009f8c687d3addf3dadf553e9145944b34cb/LICENSE",
      "license_sha256": "b0c4bc8ac9df66d9d0a9d204af48b5cba2e7d469c2ff6ab51512de5e31319963",
      "source_commit": "b65e009f8c687d3addf3dadf553e9145944b34cb",
      "reviewed_at": "2026-11-17T06:06:21.875414+00:00",
      "evidence_pinned_at": "2026-11-17T06:06:21.875414+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "MIT covers the repository software under the pinned root LICENSE, also declared in pyproject.toml. Third-party parsers, native dependencies, graph backends, model weights and hosted model or enterprise services retain their own licenses and terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-16T17:27:03Z",
        "reviewed_at": "2026-11-17T06:06:21.875414+00:00",
        "url": "https://github.com/vitali87/code-graph-rag/commit/b5b3ff7273484c47b22168bc9a581ebd80b0e457",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复增量图更新：清理标记已存在但无法更新时间时保留待清理状态，不再触发删除目录时间缓存的回退，避免下一轮不必要的全量重解析",
          "en": "Fixes incremental graph updates so an existing cleanup marker whose timestamp cannot be refreshed still records pending cleanup, avoiding the directory-mtime-cache fallback and an unnecessary full reparse on the next run"
        },
        "reviewed_files": [
          "codebase_rag/graph_updater.py"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/vitali87/code-graph-rag",
        "accessed_at": "2026-11-17T06:06:21.875414+00:00"
      },
      {
        "url": "https://github.com/vitali87/code-graph-rag/blob/b65e009f8c687d3addf3dadf553e9145944b34cb/README.md",
        "accessed_at": "2026-11-17T06:06:21.875414+00:00"
      },
      {
        "url": "https://github.com/vitali87/code-graph-rag/blob/b65e009f8c687d3addf3dadf553e9145944b34cb/LICENSE",
        "accessed_at": "2026-11-17T06:06:21.875414+00:00"
      },
      {
        "url": "https://github.com/vitali87/code-graph-rag/commit/b5b3ff7273484c47b22168bc9a581ebd80b0e457",
        "accessed_at": "2026-11-17T06:06:21.875414+00:00"
      },
      {
        "url": "https://github.com/vitali87/code-graph-rag/blob/b65e009f8c687d3addf3dadf553e9145944b34cb/pyproject.toml",
        "accessed_at": "2026-11-17T06:06:21.875414+00:00"
      },
      {
        "url": "https://github.com/vitali87/code-graph-rag/blob/b65e009f8c687d3addf3dadf553e9145944b34cb/codebase_rag/graph_updater.py",
        "accessed_at": "2026-11-17T06:06:21.875414+00:00"
      },
      {
        "url": "https://github.com/vitali87/code-graph-rag/blob/b65e009f8c687d3addf3dadf553e9145944b34cb/docs/guide/mcp-server.md",
        "accessed_at": "2026-11-17T06:06:21.875414+00:00"
      },
      {
        "url": "https://github.com/vitali87/code-graph-rag/blob/b65e009f8c687d3addf3dadf553e9145944b34cb/docs/architecture/embedded-graph.md",
        "accessed_at": "2026-11-17T06:06:21.875414+00:00"
      },
      {
        "url": "https://github.com/vitali87/code-graph-rag/blob/b65e009f8c687d3addf3dadf553e9145944b34cb/docs/getting-started/configuration.md",
        "accessed_at": "2026-11-17T06:06:21.875414+00:00"
      }
    ],
    "discovery": {
      "kind": "user_submission",
      "submitted_date": "2026-11-17",
      "source_url": "https://github.com/vitali87/code-graph-rag",
      "repository_url": "https://github.com/vitali87/code-graph-rag"
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOO8k4_w",
    "full_name": "vitali87/code-graph-rag",
    "stargazers_count": 5369,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "api_license_spdx": "MIT",
    "license_sha256": "b0c4bc8ac9df66d9d0a9d204af48b5cba2e7d469c2ff6ab51512de5e31319963",
    "last_success_at": "2026-11-17T05:36:10.802783+00:00"
  }
}
```

</details>
