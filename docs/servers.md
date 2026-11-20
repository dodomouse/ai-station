# MCP Reference Servers

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 92065 |
| 评估时间 / Evaluated at | 2026-11-17T14:27:00.363411Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:28.740Z |

## 中文

MCP 官方参考服务集合，展示工具、资源和数据接入方式。

为开发 AI 工具连接层提供文件、Git、抓取和记忆服务示例。

### 主要功能

- 包含 Everything、Fetch、Filesystem、Git、Memory、Time 等参考实现。
- 演示工具、资源、提示以及客户端连接。
- 所有当前参考服务支持 stdio，Everything 还支持 Streamable HTTP。

### 环境要求

- 需要 MCP 客户端；TypeScript 服务使用 Node.js/npx，Python 服务使用 uvx 或 pip。
- 文件系统和 Git 服务需配置允许访问的目录或仓库。

### 使用限制

- 官方明确这些是教学参考实现，不是开箱即用的生产方案。
- 部分旧服务已移至归档仓库；独立启动 stdio 服务不会开放 HTTP 端口。

### 开始使用

1. 从 README 的当前参考服务列表选择一个实现。
2. 按该服务说明配置 MCP 客户端命令及允许访问的资源。
3. 使用客户端或 MCP Inspector 检查工具列表并调用一个简单操作。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:28.740Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-11 · commit](https://github.com/modelcontextprotocol/servers/commit/e1dc4b18dbb948921da37f3d4224a628730b43b0)。Merge pull request #5518 from modelcontextprotocol/v2/chore/5509-release-v2.4.0

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/modelcontextprotocol/servers/blob/main/README.md)
- [GitHub 元数据 / Repository metadata](https://api.github.com/repos/modelcontextprotocol/servers)

## English

Official MCP reference servers demonstrating tools, resources and data access.

Provides filesystem, Git, fetching and memory examples for building an AI tool connection layer.

### Features

- Includes reference implementations such as Everything, Fetch, Filesystem, Git, Memory and Time.
- Demonstrates tools, resources, prompts and client connections.
- All current reference servers support stdio; Everything also supports Streamable HTTP.

### Requirements

- Requires an MCP client; TypeScript servers use Node.js/npx and Python servers use uvx or pip.
- Filesystem and Git servers require configuration of allowed directories or repositories.

### Limitations

- The project explicitly describes these as educational reference implementations, not production-ready solutions.
- Some former servers are archived; starting a stdio server alone does not expose an HTTP port.

### Getting started

1. Choose a current reference implementation from the README.
2. Configure the MCP client command and permitted resources using that server's instructions.
3. Inspect its tool list and make a simple call through the client or MCP Inspector.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:28.740Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-11 · commit](https://github.com/modelcontextprotocol/servers/commit/e1dc4b18dbb948921da37f3d4224a628730b43b0).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/modelcontextprotocol/servers/blob/main/README.md)
- [GitHub 元数据 / Repository metadata](https://api.github.com/repos/modelcontextprotocol/servers)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:27:00.363411Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "servers",
    "name": "MCP Reference Servers",
    "repository": "modelcontextprotocol/servers",
    "repo_node_id": "R_kgDONRaG_w",
    "category": "development",
    "summary": {
      "zh-CN": "MCP 官方参考服务集合，展示工具、资源和数据接入方式。",
      "en": "Official MCP reference servers demonstrating tools, resources and data access."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:27:00.363411Z",
        "en": "2026-11-17T14:27:00.363411Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "为开发 AI 工具连接层提供文件、Git、抓取和记忆服务示例。",
        "en": "Provides filesystem, Git, fetching and memory examples for building an AI tool connection layer."
      },
      "source_url": "https://github.com/modelcontextprotocol/servers/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/modelcontextprotocol/servers/commit/e1dc4b18dbb948921da37f3d4224a628730b43b0",
        "occurred_at": "2026-11-11T06:50:30Z",
        "reviewed_at": "2026-11-17T14:27:00.363411Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "Merge pull request #5518 from modelcontextprotocol/v2/chore/5509-release-v2.4.0 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/modelcontextprotocol/servers/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / Repository metadata",
        "url": "https://api.github.com/repos/modelcontextprotocol/servers"
      }
    ]
  },
  "snapshot": {
    "full_name": "modelcontextprotocol/servers",
    "repo_node_id": "R_kgDONRaG_w",
    "stargazers_count": 92065,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:28.740Z",
    "source_url": "https://api.github.com/repos/modelcontextprotocol/servers"
  }
}
```

</details>
