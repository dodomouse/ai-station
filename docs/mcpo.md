# mcpo

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[open-webui/mcpo](https://github.com/open-webui/mcpo)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 4429 |
| 评估时间 / Evaluated at | 2026-11-17T14:27:00.363506Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:29.357Z |

## 中文

将 MCP 服务代理为 OpenAPI HTTP 接口，供 AI 应用调用。

让使用 OpenAPI 工具接口的模型应用复用现有 MCP 服务。

### 主要功能

- 代理 stdio、SSE 与 Streamable HTTP 服务。
- 为工具生成 OpenAPI 定义和交互文档。
- 支持配置文件、多服务及 Streamable HTTP 的 OAuth 接入。

### 环境要求

- 当前包元数据要求 Python 3.11+，可使用 uv、pip 或 Docker；README 中的 3.8+ 说明与包元数据不一致。
- 被代理服务仍需自身运行环境、网络访问及认证配置。

### 使用限制

- 代理层不能替代上游工具的安装、权限与业务校验。
- 关闭会话时存在异常日志的问题报告，部署前应核对相应 issue 状态。

### 开始使用

1. 按 README 安装 mcpo，并准备一个可正常运行的 MCP 服务。
2. 选择命令行或配置文件方式，配置监听地址和认证。
3. 打开生成的 `/docs` 检查工具，再把 OpenAPI 地址接入 AI 客户端。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:29.357Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-04 · issue](https://github.com/open-webui/mcpo/issues/318)。新建 Issue：issue: suppress(Exception) in _close_session_locked cannot catch CancelledError, so every shutdown logs an ERROR traceback

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/open-webui/mcpo/blob/main/README.md)
- [GitHub 元数据 / Repository metadata](https://api.github.com/repos/open-webui/mcpo)
- [会话关闭问题报告 / Session shutdown issue](https://github.com/open-webui/mcpo/issues/318)
- [包运行环境 / Package runtime requirements](https://github.com/open-webui/mcpo/blob/main/pyproject.toml)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

Proxies MCP servers as OpenAPI HTTP endpoints for AI applications.

Lets model applications that consume OpenAPI tools reuse existing MCP servers.

### Features

- Proxies stdio, SSE and Streamable HTTP servers.
- Generates OpenAPI definitions and interactive tool documentation.
- Supports configuration files, multiple services and OAuth connections for Streamable HTTP.

### Requirements

- Current package metadata requires Python 3.11+, with uv, pip or Docker options; the README still lists 3.8+ and disagrees with the package metadata.
- The proxied server still needs its own runtime, network access and authentication.

### Limitations

- The proxy does not replace installation, permissions or business validation in upstream tools.
- A reported shutdown exception can produce error logs; check the linked issue before deployment.

### Getting started

1. Install mcpo from the README and prepare a working MCP server.
2. Choose command-line or configuration-file setup, including the listening address and authentication.
3. Inspect tools in the generated `/docs` page, then connect the OpenAPI endpoint to the AI client.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:29.357Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-04 · issue](https://github.com/open-webui/mcpo/issues/318).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/open-webui/mcpo/blob/main/README.md)
- [GitHub 元数据 / Repository metadata](https://api.github.com/repos/open-webui/mcpo)
- [会话关闭问题报告 / Session shutdown issue](https://github.com/open-webui/mcpo/issues/318)
- [包运行环境 / Package runtime requirements](https://github.com/open-webui/mcpo/blob/main/pyproject.toml)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:27:00.363506Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "mcpo",
    "name": "mcpo",
    "repository": "open-webui/mcpo",
    "repo_node_id": "R_kgDOORD1Vg",
    "category": "development",
    "summary": {
      "zh-CN": "将 MCP 服务代理为 OpenAPI HTTP 接口，供 AI 应用调用。",
      "en": "Proxies MCP servers as OpenAPI HTTP endpoints for AI applications."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:27:00.363506Z",
        "en": "2026-11-17T14:27:00.363506Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "让使用 OpenAPI 工具接口的模型应用复用现有 MCP 服务。",
        "en": "Lets model applications that consume OpenAPI tools reuse existing MCP servers."
      },
      "source_url": "https://github.com/open-webui/mcpo/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "issue",
        "url": "https://github.com/open-webui/mcpo/issues/318",
        "occurred_at": "2026-11-04T20:04:55Z",
        "reviewed_at": "2026-11-17T14:27:00.363506Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "新建 Issue：issue: suppress(Exception) in _close_session_locked cannot catch CancelledError, so every shutdown logs an ERROR traceback 此记录用于证明窗口内活动。",
          "en": "The recorded issue establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/open-webui/mcpo/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / Repository metadata",
        "url": "https://api.github.com/repos/open-webui/mcpo"
      },
      {
        "title": "会话关闭问题报告 / Session shutdown issue",
        "url": "https://github.com/open-webui/mcpo/issues/318"
      },
      {
        "title": "包运行环境 / Package runtime requirements",
        "url": "https://github.com/open-webui/mcpo/blob/main/pyproject.toml"
      }
    ]
  },
  "snapshot": {
    "full_name": "open-webui/mcpo",
    "repo_node_id": "R_kgDOORD1Vg",
    "stargazers_count": 4429,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:29.357Z",
    "source_url": "https://api.github.com/repos/open-webui/mcpo"
  }
}
```

</details>
