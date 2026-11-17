# FastAPI-MCP

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[tadata-org/fastapi_mcp](https://github.com/tadata-org/fastapi_mcp)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 12029 |
| 评估时间 / Evaluated at | 2026-11-17T14:27:00.363783Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:30.395Z |

## 中文

将 FastAPI 路由转换为 MCP 工具，并复用应用的模型和依赖认证。

让 AI 调用已有业务 API，减少另写工具服务的工作。

### 主要功能

- 保留请求、响应模型和接口说明。
- 复用 FastAPI 的认证依赖，并直接通过 ASGI 调用应用。
- 支持挂载到原应用，也可单独部署。

### 环境要求

- 需要 Python 3.10+ 和已有 FastAPI 应用；README 推荐 Python 3.12。
- 可通过 uv 或 pip 安装，并使用兼容的 MCP 客户端。

### 使用限制

- 转换接口不替代原应用的权限设计和输入校验。
- 路径参数编码存在问题报告；所引活动 PR 也不代表问题已修复。

### 开始使用

1. 按 README 安装 `fastapi-mcp`。
2. 用 `FastApiMCP(app)` 包装应用并挂载 MCP 入口。
3. 从一个有明确请求模型的接口开始，验证认证、参数与返回结果。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:30.395Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-16 · pr](https://github.com/tadata-org/fastapi_mcp/pull/360)。新建 PR：fix: expose non-object JSON bodies as MCP tool arguments

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/tadata-org/fastapi_mcp/blob/main/README.md)
- [GitHub 元数据 / Repository metadata](https://api.github.com/repos/tadata-org/fastapi_mcp)
- [路径参数问题报告 / Path-parameter issue](https://github.com/tadata-org/fastapi_mcp/issues/354)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

Exposes FastAPI routes as MCP tools while reusing application schemas and dependency-based authentication.

Lets AI call existing business APIs without writing a separate tool service.

### Features

- Preserves request and response schemas and endpoint documentation.
- Reuses FastAPI authentication dependencies and invokes the app through ASGI.
- Supports mounting in the original application or deploying separately.

### Requirements

- Requires Python 3.10+ and an existing FastAPI application; the README recommends Python 3.12.
- Install with uv or pip and use a compatible MCP client.

### Limitations

- Exposing an interface does not replace authorization design and input validation in the original application.
- Path-parameter encoding has a reported issue; the cited activity PR does not establish that it is fixed.

### Getting started

1. Install `fastapi-mcp` using the README.
2. Wrap the application with `FastApiMCP(app)` and mount its MCP endpoint.
3. Start with an endpoint that has an explicit request schema, then check authentication, parameters and returned results.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:30.395Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-16 · pr](https://github.com/tadata-org/fastapi_mcp/pull/360).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/tadata-org/fastapi_mcp/blob/main/README.md)
- [GitHub 元数据 / Repository metadata](https://api.github.com/repos/tadata-org/fastapi_mcp)
- [路径参数问题报告 / Path-parameter issue](https://github.com/tadata-org/fastapi_mcp/issues/354)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:27:00.363783Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "fastapi-mcp",
    "name": "FastAPI-MCP",
    "repository": "tadata-org/fastapi_mcp",
    "repo_node_id": "R_kgDOOFMy0Q",
    "category": "development",
    "summary": {
      "zh-CN": "将 FastAPI 路由转换为 MCP 工具，并复用应用的模型和依赖认证。",
      "en": "Exposes FastAPI routes as MCP tools while reusing application schemas and dependency-based authentication."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:27:00.363783Z",
        "en": "2026-11-17T14:27:00.363783Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "让 AI 调用已有业务 API，减少另写工具服务的工作。",
        "en": "Lets AI call existing business APIs without writing a separate tool service."
      },
      "source_url": "https://github.com/tadata-org/fastapi_mcp/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "pr",
        "url": "https://github.com/tadata-org/fastapi_mcp/pull/360",
        "occurred_at": "2026-11-16T11:35:29Z",
        "reviewed_at": "2026-11-17T14:27:00.363783Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "新建 PR：fix: expose non-object JSON bodies as MCP tool arguments 此记录用于证明窗口内活动。",
          "en": "The recorded pr establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/tadata-org/fastapi_mcp/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / Repository metadata",
        "url": "https://api.github.com/repos/tadata-org/fastapi_mcp"
      },
      {
        "title": "路径参数问题报告 / Path-parameter issue",
        "url": "https://github.com/tadata-org/fastapi_mcp/issues/354"
      }
    ]
  },
  "snapshot": {
    "full_name": "tadata-org/fastapi_mcp",
    "repo_node_id": "R_kgDOOFMy0Q",
    "stargazers_count": 12029,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:30.395Z",
    "source_url": "https://api.github.com/repos/tadata-org/fastapi_mcp"
  }
}
```

</details>
