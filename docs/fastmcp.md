# FastMCP (Python)

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 28617 |
| 评估时间 / Evaluated at | 2026-11-17T14:27:00.363697Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:30.779Z |

## 中文

用 Python 构建 MCP 服务端、客户端和交互应用。

将业务函数、资源和提示封装为 AI 可调用的工具接口。

### 主要功能

- 从 Python 函数生成工具定义、校验和说明。
- 为本地或远程 MCP 服务提供客户端连接。
- 支持在对话中呈现交互应用，并提供认证及协议生命周期组件。

### 环境要求

- 当前项目配置要求 Python 3.11+，README 推荐使用 uv 安装。
- 需要兼容所选传输方式的 MCP 客户端；业务工具的外部依赖需另行配置。

### 使用限制

- 独立 FastMCP 与早期内置于官方 SDK 的版本不同，升级需阅读对应迁移说明。
- 企业 FastMCP Gateway 是单独的服务，不等同于安装本库。

### 开始使用

1. 在 Python 项目中按 README 执行 `uv add fastmcp`。
2. 使用 `FastMCP` 和工具装饰器定义一个简单函数。
3. 启动服务后用 MCP 客户端调用函数，再加入认证和业务资源。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:30.779Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/PrefectHQ/fastmcp/commit/10083f77731f90ba6191f0a8d2c23d9adf0aacce)。Raise opentelemetry-api floor past traceparent ReDoS (#6513)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/PrefectHQ/fastmcp/blob/main/README.md)
- [GitHub 元数据 / Repository metadata](https://api.github.com/repos/PrefectHQ/fastmcp)
- [Python 环境要求 / Python requirements](https://github.com/PrefectHQ/fastmcp/blob/main/pyproject.toml)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

Builds MCP servers, clients and interactive applications in Python.

Wraps business functions, resources and prompts as interfaces AI can call.

### Features

- Generates tool schemas, validation and documentation from Python functions.
- Provides client connections to local or remote MCP servers.
- Supports interactive apps within conversations and components for authentication and protocol lifecycle management.

### Requirements

- The current project configuration requires Python 3.11+; the README recommends uv.
- Requires an MCP client compatible with the selected transport; external dependencies of business tools need separate setup.

### Limitations

- Standalone FastMCP differs from the early version bundled in the official SDK; upgrades require the matching migration guide.
- The enterprise FastMCP Gateway is a separate service, not an automatic part of installing this library.

### Getting started

1. Run `uv add fastmcp` in a Python project as documented in the README.
2. Define a simple function with `FastMCP` and its tool decorator.
3. Start the server, call the function from an MCP client, then add authentication and business resources.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:30.779Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/PrefectHQ/fastmcp/commit/10083f77731f90ba6191f0a8d2c23d9adf0aacce).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/PrefectHQ/fastmcp/blob/main/README.md)
- [GitHub 元数据 / Repository metadata](https://api.github.com/repos/PrefectHQ/fastmcp)
- [Python 环境要求 / Python requirements](https://github.com/PrefectHQ/fastmcp/blob/main/pyproject.toml)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:27:00.363697Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "fastmcp",
    "name": "FastMCP (Python)",
    "repository": "PrefectHQ/fastmcp",
    "repo_node_id": "R_kgDONWxneQ",
    "category": "development",
    "summary": {
      "zh-CN": "用 Python 构建 MCP 服务端、客户端和交互应用。",
      "en": "Builds MCP servers, clients and interactive applications in Python."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:27:00.363697Z",
        "en": "2026-11-17T14:27:00.363697Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "将业务函数、资源和提示封装为 AI 可调用的工具接口。",
        "en": "Wraps business functions, resources and prompts as interfaces AI can call."
      },
      "source_url": "https://github.com/PrefectHQ/fastmcp/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/PrefectHQ/fastmcp/commit/10083f77731f90ba6191f0a8d2c23d9adf0aacce",
        "occurred_at": "2026-11-17T06:41:43Z",
        "reviewed_at": "2026-11-17T14:27:00.363697Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "Raise opentelemetry-api floor past traceparent ReDoS (#6513) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/PrefectHQ/fastmcp/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / Repository metadata",
        "url": "https://api.github.com/repos/PrefectHQ/fastmcp"
      },
      {
        "title": "Python 环境要求 / Python requirements",
        "url": "https://github.com/PrefectHQ/fastmcp/blob/main/pyproject.toml"
      }
    ]
  },
  "snapshot": {
    "full_name": "PrefectHQ/fastmcp",
    "repo_node_id": "R_kgDONWxneQ",
    "stargazers_count": 28617,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:30.779Z",
    "source_url": "https://api.github.com/repos/PrefectHQ/fastmcp"
  }
}
```

</details>
