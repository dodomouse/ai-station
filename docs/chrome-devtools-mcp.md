# Chrome DevTools MCP

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 自动化 / Automation |
| 状态 / Status | 已收录 / Included |
| Star | 57952 |
| 评估时间 / Evaluated at | 2026-11-17T14:27:00.364038Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:31.895Z |

## 中文

通过 MCP 让编码智能体控制 Chrome，并读取调试和性能信息。

帮助 AI 复现网页问题、查看浏览器状态并分析页面性能。

### 主要功能

- 向 MCP 客户端提供浏览器交互与 DevTools 检查能力。
- 记录和分析页面性能追踪。
- 提供独立 CLI，以及配套浏览器操作技能。

### 环境要求

- 需要 Node.js LTS、npm、当前稳定版或更新版 Chrome，以及 MCP 客户端。
- 官方支持 Google Chrome 和 Chrome for Testing。

### 使用限制

- 其他 Chromium 浏览器的兼容性没有保证。
- 工具可读取浏览器内容；默认收集使用统计，性能工具也可能查询 CrUX。相关选项见 README。

### 开始使用

1. 核对 Chrome 与 Node.js 环境，按 README 配置 MCP 客户端启动命令。
2. 让客户端执行一个公开页面的性能检查，确认浏览器能自动启动。
3. 按需要选择工具集合、配置统计选项，并保持技能与服务版本一致。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:31.895Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/ec0abfc80568b9585299d739debb8869fabd710f)。fix(cli): pass option values starting with `-` through to tools (#3501)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/README.md)
- [GitHub 元数据 / Repository metadata](https://api.github.com/repos/ChromeDevTools/chrome-devtools-mcp)

## English

Lets coding agents control Chrome and inspect debugging and performance information through MCP.

Helps AI reproduce web issues, inspect browser state and analyze page performance.

### Features

- Provides browser interaction and DevTools inspection tools to MCP clients.
- Records and analyzes page performance traces.
- Includes a standalone CLI and related browser-operation skills.

### Requirements

- Requires Node.js LTS, npm, current stable Chrome or newer, and an MCP client.
- Official browser support covers Google Chrome and Chrome for Testing.

### Limitations

- Compatibility with other Chromium browsers is not guaranteed.
- Tools can read browser content; usage statistics are enabled by default and performance tools may query CrUX. See the README for the relevant controls.

### Getting started

1. Check Chrome and Node.js, then configure the client's launch command using the README.
2. Run a performance check on a public page to confirm that the browser starts automatically.
3. Select the needed toolset and statistics settings, and keep skills aligned with the server version.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:31.895Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/ec0abfc80568b9585299d739debb8869fabd710f).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/README.md)
- [GitHub 元数据 / Repository metadata](https://api.github.com/repos/ChromeDevTools/chrome-devtools-mcp)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:27:00.364038Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "chrome-devtools-mcp",
    "name": "Chrome DevTools MCP",
    "repository": "ChromeDevTools/chrome-devtools-mcp",
    "repo_node_id": "R_kgDOPt7f_g",
    "category": "automation",
    "summary": {
      "zh-CN": "通过 MCP 让编码智能体控制 Chrome，并读取调试和性能信息。",
      "en": "Lets coding agents control Chrome and inspect debugging and performance information through MCP."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:27:00.364038Z",
        "en": "2026-11-17T14:27:00.364038Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "帮助 AI 复现网页问题、查看浏览器状态并分析页面性能。",
        "en": "Helps AI reproduce web issues, inspect browser state and analyze page performance."
      },
      "source_url": "https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/ec0abfc80568b9585299d739debb8869fabd710f",
        "occurred_at": "2026-11-17T12:31:37Z",
        "reviewed_at": "2026-11-17T14:27:00.364038Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "fix(cli): pass option values starting with `-` through to tools (#3501) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / Repository metadata",
        "url": "https://api.github.com/repos/ChromeDevTools/chrome-devtools-mcp"
      }
    ]
  },
  "snapshot": {
    "full_name": "ChromeDevTools/chrome-devtools-mcp",
    "repo_node_id": "R_kgDOPt7f_g",
    "stargazers_count": 57952,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:31.895Z",
    "source_url": "https://api.github.com/repos/ChromeDevTools/chrome-devtools-mcp"
  }
}
```

</details>
