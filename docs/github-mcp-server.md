# GitHub MCP Server

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[github/github-mcp-server](https://github.com/github/github-mcp-server)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 34544 |
| 评估时间 / Evaluated at | 2026-11-17T14:27:00.363167Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:29.374Z |

## 中文

GitHub 官方 MCP 服务，把仓库、代码和协作流程提供给智能体。

让 AI 检索代码、分析提交、处理工作项并检查 CI 结果。

### 主要功能

- 浏览仓库和代码，检索文件及提交。
- 读取和管理 Issue、PR 与开发工作流。
- 按工具集配置可用能力，支持远程或本地服务。

### 环境要求

- 需要兼容 MCP 的客户端和 GitHub 身份认证。
- 远程方式需要客户端支持 HTTP；本地容器方式需要运行中的 Docker。

### 使用限制

- 可访问的仓库和操作受账号权限及组织策略限制。
- 工具集和认证支持因客户端与部署方式而异；GitHub Enterprise 有单独配置。

### 开始使用

1. 在 README 中选择远程服务或本地 Docker 安装方式。
2. 按所用客户端配置 OAuth 或个人访问令牌，并选择所需工具集。
3. 先读取一个有权访问的仓库，检查返回内容后再配置写操作。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:29.374Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-16 · commit](https://github.com/github/github-mcp-server/commit/67d4dc489700ec955ad255d098396dd86c729523)。Add public agent automation tools (#3719)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/github/github-mcp-server/blob/main/README.md)
- [GitHub 元数据 / Repository metadata](https://api.github.com/repos/github/github-mcp-server)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

GitHub's official MCP server exposes repositories, code and collaboration workflows to agents.

Lets AI search code, analyze commits, manage work items and inspect CI results.

### Features

- Browses repositories and code, and searches files and commits.
- Reads and manages issues, pull requests and development workflows.
- Configures enabled toolsets and supports remote or local service deployment.

### Requirements

- Requires an MCP-compatible client and GitHub authentication.
- Remote mode needs HTTP-server support in the client; the local container requires Docker to be running.

### Limitations

- Accessible repositories and actions depend on account permissions and organization policy.
- Toolset and authentication support vary by client and deployment; GitHub Enterprise needs separate configuration.

### Getting started

1. Choose the remote service or local Docker installation in the README.
2. Configure OAuth or a personal access token for the chosen client, then select the required toolsets.
3. Read a repository you can access first and inspect the result before configuring write operations.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:29.374Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-16 · commit](https://github.com/github/github-mcp-server/commit/67d4dc489700ec955ad255d098396dd86c729523).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/github/github-mcp-server/blob/main/README.md)
- [GitHub 元数据 / Repository metadata](https://api.github.com/repos/github/github-mcp-server)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:27:00.363167Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "github-mcp-server",
    "name": "GitHub MCP Server",
    "repository": "github/github-mcp-server",
    "repo_node_id": "R_kgDOODGMVA",
    "category": "development",
    "summary": {
      "zh-CN": "GitHub 官方 MCP 服务，把仓库、代码和协作流程提供给智能体。",
      "en": "GitHub's official MCP server exposes repositories, code and collaboration workflows to agents."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:27:00.363167Z",
        "en": "2026-11-17T14:27:00.363167Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "让 AI 检索代码、分析提交、处理工作项并检查 CI 结果。",
        "en": "Lets AI search code, analyze commits, manage work items and inspect CI results."
      },
      "source_url": "https://github.com/github/github-mcp-server/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/github/github-mcp-server/commit/67d4dc489700ec955ad255d098396dd86c729523",
        "occurred_at": "2026-11-16T12:36:47Z",
        "reviewed_at": "2026-11-17T14:27:00.363167Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "Add public agent automation tools (#3719) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/github/github-mcp-server/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / Repository metadata",
        "url": "https://api.github.com/repos/github/github-mcp-server"
      }
    ]
  },
  "snapshot": {
    "full_name": "github/github-mcp-server",
    "repo_node_id": "R_kgDOODGMVA",
    "stargazers_count": 34544,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:29.374Z",
    "source_url": "https://api.github.com/repos/github/github-mcp-server"
  }
}
```

</details>
