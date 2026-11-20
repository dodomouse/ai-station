# Playwright MCP

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 自动化 / Automation |
| 状态 / Status | 已收录 / Included |
| Star | 39780 |
| 评估时间 / Evaluated at | 2026-11-17T14:27:00.364201Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:32.017Z |

## 中文

通过 MCP 为 AI 提供浏览器导航、页面结构读取和交互工具。

让智能体利用结构化页面快照执行网页任务和检查界面行为。

### 主要功能

- 基于 Playwright 操作浏览器并读取可访问性结构。
- 通过 MCP 配置接入多种编码客户端。
- 支持本地启动、HTTP 服务或 Docker 运行方式。

### 环境要求

- 需要 Node.js 18+ 和兼容 MCP 的客户端。
- 浏览器及相关系统依赖须按运行方式安装；容器方式需要 Docker。

### 使用限制

- 官方说明本服务不是安全隔离边界。
- 当前 Docker 实现只支持无界面的 Chromium，不能据此推断所有浏览器均可用。

### 开始使用

1. 按 README 在 MCP 客户端配置 `@playwright/mcp`。
2. 确认浏览器可以启动，并读取一个公开网页的结构快照。
3. 再测试点击或输入，按业务场景设置会话和访问范围。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:32.017Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-16 · commit](https://github.com/microsoft/playwright-mcp/commit/a62ea28698af6d9bc89438bcec50c63377cef957)。devops: pin exact Node.js version in the Docker image and roll it with Playwright (#1867)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/microsoft/playwright-mcp/blob/main/README.md)
- [GitHub 元数据 / Repository metadata](https://api.github.com/repos/microsoft/playwright-mcp)

## English

Provides browser navigation, page-structure reading and interaction tools to AI through MCP.

Lets agents perform web tasks and inspect interface behavior using structured page snapshots.

### Features

- Operates browsers with Playwright and reads accessibility structure.
- Integrates with coding clients through MCP configuration.
- Supports local launch, HTTP service operation and Docker.

### Requirements

- Requires Node.js 18+ and an MCP-compatible client.
- Install browser and system dependencies for the selected mode; container operation requires Docker.

### Limitations

- The project explicitly states that the server is not a security boundary.
- The current Docker implementation supports headless Chromium only, not every browser mode.

### Getting started

1. Configure `@playwright/mcp` in the MCP client using the README.
2. Confirm the browser launches and read a structured snapshot of a public page.
3. Then test clicks or input and configure session and access scope for the use case.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:32.017Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-16 · commit](https://github.com/microsoft/playwright-mcp/commit/a62ea28698af6d9bc89438bcec50c63377cef957).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/microsoft/playwright-mcp/blob/main/README.md)
- [GitHub 元数据 / Repository metadata](https://api.github.com/repos/microsoft/playwright-mcp)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:27:00.364201Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "playwright-mcp",
    "name": "Playwright MCP",
    "repository": "microsoft/playwright-mcp",
    "repo_node_id": "R_kgDOOMjd8A",
    "category": "automation",
    "summary": {
      "zh-CN": "通过 MCP 为 AI 提供浏览器导航、页面结构读取和交互工具。",
      "en": "Provides browser navigation, page-structure reading and interaction tools to AI through MCP."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:27:00.364201Z",
        "en": "2026-11-17T14:27:00.364201Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "让智能体利用结构化页面快照执行网页任务和检查界面行为。",
        "en": "Lets agents perform web tasks and inspect interface behavior using structured page snapshots."
      },
      "source_url": "https://github.com/microsoft/playwright-mcp/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/microsoft/playwright-mcp/commit/a62ea28698af6d9bc89438bcec50c63377cef957",
        "occurred_at": "2026-11-16T22:57:05Z",
        "reviewed_at": "2026-11-17T14:27:00.364201Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "devops: pin exact Node.js version in the Docker image and roll it with Playwright (#1867) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/microsoft/playwright-mcp/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / Repository metadata",
        "url": "https://api.github.com/repos/microsoft/playwright-mcp"
      }
    ]
  },
  "snapshot": {
    "full_name": "microsoft/playwright-mcp",
    "repo_node_id": "R_kgDOOMjd8A",
    "stargazers_count": 39780,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:32.017Z",
    "source_url": "https://api.github.com/repos/microsoft/playwright-mcp"
  }
}
```

</details>
