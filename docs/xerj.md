# XERJ

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[xerj-org/xerj](https://github.com/xerj-org/xerj)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 19162 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-17T03:59:03.770697+00:00 |

## 中文

面向 AI 智能体的开源搜索引擎，索引代码、文档和日志，提供全文、向量与混合检索。

### 用途与功能

- 以本地 Rust 引擎提供 BM25、向量和混合检索。
- 通过 MCP 和 Elasticsearch 兼容接口提供检索能力。
- 支持代码定义查找和智能体记忆存储。

### 环境与限制

本条仅收录 Apache-2.0 搜索引擎源码。rc.101 起发行二进制包含专有 Query-1 组件，模型训练数据未公开；它们不属于本条开源范围。索引目录应与数据目录分开，关闭认证的模式仅适用于受控本机环境。

### 开始使用

依据 README 的源码构建与安装说明准备开源引擎，为项目目录建立索引，再从 CLI 或 MCP 客户端查询。

参阅[官方 README](https://github.com/xerj-org/xerj/blob/50e4ffded5518b1822cfac5450fa34d3829ab8ab/README.md)。

### 收录与来源

适合给编码智能体提供带文件位置的本地检索上下文；未采纳上游速度或 Token 节省宣传。

维护证据：[为全局和索引级批量写入路由增加 PUT 方法，修复 Elasticsearch Python 客户端写入返回 405 的问题。](https://github.com/xerj-org/xerj/commit/42d199cd99af9c85871bb398608d960b2e7407e7)（2026-11-07）。

发现于 [GitHub 月榜](https://github.com/trending/rust?since=monthly)。2026-11-17 的榜单记录新增 14,186 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

An open-source search engine for AI agents, indexing code, documents and logs for full-text, vector and hybrid retrieval.

### Uses and features

- Provides BM25, vector and hybrid retrieval in a local Rust engine.
- Exposes search through MCP and an Elasticsearch-compatible API.
- Supports code-definition lookup and agent-memory storage.

### Requirements and limits

This entry covers only the Apache-2.0 search-engine source. Release binaries from rc.101 include proprietary Query-1 components, and model training data is unpublished; these are outside this entry’s open-source scope. Keep indexed folders separate from storage, and reserve unauthenticated mode for controlled local use.

### Getting started

Follow the README source-build and installation guidance for the open engine, index a project directory, then query it through the CLI or an MCP client.

See the [official README](https://github.com/xerj-org/xerj/blob/50e4ffded5518b1822cfac5450fa34d3829ab8ab/README.md).

### Review and provenance

Useful for supplying coding agents with local search context and file locations; upstream speed and token-saving claims are not adopted.

Maintenance evidence: [Adds PUT support to global and per-index bulk routes, fixing HTTP 405 responses for Elasticsearch Python bulk clients.](https://github.com/xerj-org/xerj/commit/42d199cd99af9c85871bb398608d960b2e7407e7) (2026-11-07).

Discovered in [GitHub monthly Trending](https://github.com/trending/rust?since=monthly), which recorded 14,186 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T03:59:03.770697+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "xerj",
    "name": "XERJ",
    "repository": "xerj-org/xerj",
    "repo_node_id": "R_kgDOTJJATQ",
    "category": "ai",
    "summary": {
      "zh-CN": "面向 AI 智能体的开源搜索引擎，索引代码、文档和日志，提供全文、向量与混合检索。",
      "en": "An open-source search engine for AI agents, indexing code, documents and logs for full-text, vector and hybrid retrieval."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T03:59:03.770697+00:00",
        "en": "2026-11-17T03:59:03.770697+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合给编码智能体提供带文件位置的本地检索上下文；未采纳上游速度或 Token 节省宣传。",
      "en": "Useful for supplying coding agents with local search context and file locations; upstream speed and token-saving claims are not adopted.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "source_url": "https://github.com/xerj-org/xerj/blob/50e4ffded5518b1822cfac5450fa34d3829ab8ab/LICENSE",
      "license_sha256": "c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4",
      "source_commit": "50e4ffded5518b1822cfac5450fa34d3829ab8ab",
      "reviewed_at": "2026-11-17T03:59:03.770697+00:00",
      "evidence_pinned_at": "2026-11-17T03:59:03.770697+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "Apache-2.0 covers the open search-engine source. Proprietary XERJ Query-1 crates in rc.101+ release binaries, model bundles and unpublished training data are excluded from this entry."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-07T05:59:37Z",
        "reviewed_at": "2026-11-17T03:59:03.770697+00:00",
        "url": "https://github.com/xerj-org/xerj/commit/42d199cd99af9c85871bb398608d960b2e7407e7",
        "qualifies": true,
        "reason": {
          "zh-CN": "为全局和索引级批量写入路由增加 PUT 方法，修复 Elasticsearch Python 客户端写入返回 405 的问题。",
          "en": "Adds PUT support to global and per-index bulk routes, fixing HTTP 405 responses for Elasticsearch Python bulk clients."
        },
        "reviewed_files": [
          "engine/crates/xerj-api/src/router.rs",
          "engine/crates/xerj-api/src/authz.rs"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/xerj-org/xerj",
        "accessed_at": "2026-11-17T03:59:03.770697+00:00"
      },
      {
        "url": "https://github.com/xerj-org/xerj/blob/50e4ffded5518b1822cfac5450fa34d3829ab8ab/README.md",
        "accessed_at": "2026-11-17T03:59:03.770697+00:00"
      },
      {
        "url": "https://github.com/xerj-org/xerj/blob/50e4ffded5518b1822cfac5450fa34d3829ab8ab/LICENSE",
        "accessed_at": "2026-11-17T03:59:03.770697+00:00"
      },
      {
        "url": "https://github.com/xerj-org/xerj/commit/42d199cd99af9c85871bb398608d960b2e7407e7",
        "accessed_at": "2026-11-17T03:59:03.770697+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 14186,
      "source_url": "https://github.com/trending/rust?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOTJJATQ",
    "full_name": "xerj-org/xerj",
    "stargazers_count": 19162,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4",
    "last_success_at": "2026-11-17T03:53:28.278736+00:00"
  }
}
```

</details>
