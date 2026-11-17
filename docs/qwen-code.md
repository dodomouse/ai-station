# Qwen Code

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[QwenLM/qwen-code](https://github.com/QwenLM/qwen-code)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 30668 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-17T04:07:37.963437+00:00 |

## 中文

跨终端、编辑器和桌面的 AI 编程智能体，可理解仓库、修改代码并调用开发工具。

### 用途与功能

- 连接 Qwen、OpenAI、Anthropic、Gemini 或兼容本地模型接口。
- 通过子智能体、Skills、MCP 和无界面模式扩展开发任务。

### 环境与限制

npm 安装需要 Node.js 22+；需配置模型 API 或 Qwen Plus/Pro 订阅。部分能力仍有实验标记，包括 Web 和团队协作。共享主机上的 daemon 需配置认证。

### 开始使用

安装 @qwen-code/qwen-code 后在项目目录运行 qwen，通过 /auth 配置模型，先请求解释仓库。

参阅[官方 README](https://github.com/QwenLM/qwen-code/blob/56f43c9b47e0b0398bccfc7c0f395ce7ae35683d/README.md)。

### 收录与来源

把仓库上下文、模型接口和工具调用集中在同一会话，适合需要交互开发与脚本调用的项目。

维护证据：[以分词解析器替换托管智能体数据库 DDL 的正则解析，并据解析结果校验列、键和索引。](https://github.com/QwenLM/qwen-code/commit/56f43c9b47e0b0398bccfc7c0f395ce7ae35683d)（2026-11-17）。

发现于 [GitHub 月榜](https://github.com/trending/typescript?since=monthly)。2026-11-17 的榜单记录新增 2,233 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

An AI coding agent for terminals, editors and desktops that explores repositories, edits code and invokes development tools.

### Uses and features

- Connect Qwen, OpenAI, Anthropic, Gemini or compatible local model endpoints.
- Extend development tasks with subagents, Skills, MCP and headless execution.

### Requirements and limits

npm installation requires Node.js 22+ and a model API or Qwen Plus/Pro subscription. Web and team features include experimental paths; configure daemon authentication on shared hosts.

### Getting started

Install @qwen-code/qwen-code, run qwen in the project, configure a model with /auth, and start with a repository explanation.

See the [official README](https://github.com/QwenLM/qwen-code/blob/56f43c9b47e0b0398bccfc7c0f395ce7ae35683d/README.md).

### Review and provenance

Combines repository context, model providers and tool calls in one session for interactive and scripted development.

Maintenance evidence: [Replaces regex parsing of managed-agent database DDL with a tokenizing parser and validates columns, keys and indexes from parsed structures.](https://github.com/QwenLM/qwen-code/commit/56f43c9b47e0b0398bccfc7c0f395ce7ae35683d) (2026-11-17).

Discovered in [GitHub monthly Trending](https://github.com/trending/typescript?since=monthly), which recorded 2,233 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:07:37.963437+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "qwen-code",
    "name": "Qwen Code",
    "repository": "QwenLM/qwen-code",
    "repo_node_id": "R_kgDOPB-92Q",
    "category": "ai",
    "summary": {
      "zh-CN": "跨终端、编辑器和桌面的 AI 编程智能体，可理解仓库、修改代码并调用开发工具。",
      "en": "An AI coding agent for terminals, editors and desktops that explores repositories, edits code and invokes development tools."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:07:37.963437+00:00",
        "en": "2026-11-17T04:07:37.963437+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "把仓库上下文、模型接口和工具调用集中在同一会话，适合需要交互开发与脚本调用的项目。",
      "en": "Combines repository context, model providers and tool calls in one session for interactive and scripted development.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "source_url": "https://github.com/QwenLM/qwen-code/blob/56f43c9b47e0b0398bccfc7c0f395ce7ae35683d/LICENSE",
      "license_sha256": "55367b61ccd2a016a0159ad886bd66a3ee6cb5e873d0c75c803c897dd245b075",
      "source_commit": "56f43c9b47e0b0398bccfc7c0f395ce7ae35683d",
      "reviewed_at": "2026-11-17T04:07:37.963437+00:00",
      "evidence_pinned_at": "2026-11-17T04:07:37.963437+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "Root license applies to repository software code; models, data, assets and external services have separate terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-17T03:42:35Z",
        "reviewed_at": "2026-11-17T04:07:37.963437+00:00",
        "url": "https://github.com/QwenLM/qwen-code/commit/56f43c9b47e0b0398bccfc7c0f395ce7ae35683d",
        "qualifies": true,
        "reason": {
          "zh-CN": "以分词解析器替换托管智能体数据库 DDL 的正则解析，并据解析结果校验列、键和索引。",
          "en": "Replaces regex parsing of managed-agent database DDL with a tokenizing parser and validates columns, keys and indexes from parsed structures."
        },
        "reviewed_files": [
          "packages/managed-agent-server/persistence/src/main/java/com/alibaba/qwen/code/runtimebroker/managedschema/ManagedSchemaCatalog.java"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/QwenLM/qwen-code",
        "accessed_at": "2026-11-17T04:07:37.963437+00:00"
      },
      {
        "url": "https://github.com/QwenLM/qwen-code/blob/56f43c9b47e0b0398bccfc7c0f395ce7ae35683d/README.md",
        "accessed_at": "2026-11-17T04:07:37.963437+00:00"
      },
      {
        "url": "https://github.com/QwenLM/qwen-code/blob/56f43c9b47e0b0398bccfc7c0f395ce7ae35683d/LICENSE",
        "accessed_at": "2026-11-17T04:07:37.963437+00:00"
      },
      {
        "url": "https://github.com/QwenLM/qwen-code/commit/56f43c9b47e0b0398bccfc7c0f395ce7ae35683d",
        "accessed_at": "2026-11-17T04:07:37.963437+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 2233,
      "source_url": "https://github.com/trending/typescript?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOPB-92Q",
    "full_name": "QwenLM/qwen-code",
    "stargazers_count": 30668,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "55367b61ccd2a016a0159ad886bd66a3ee6cb5e873d0c75c803c897dd245b075",
    "last_success_at": "2026-11-17T03:53:31.055887+00:00"
  }
}
```

</details>
