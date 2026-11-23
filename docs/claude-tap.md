# claude-tap

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[liaohch3/claude-tap](https://github.com/liaohch3/claude-tap)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 3365 |
| 评估时间 / Evaluated at | 2026-11-23T16:00:50.764479Z |

## 中文

claude-tap 是面向 AI 编程智能体的本地代理与 Trace 查看器。让 CLI 客户端通过它运行，或监听本地应用会话记录，即可查看真实 API 流量与智能体上下文：系统提示词、对话历史、工具定义、工具调用、流式响应、Token 用量以及相邻请求 Diff。

它帮助 AI 编程智能体的开发者调试行为异常、核对提示词是否生效、拆解 Token 开销并归档会话，用于排查“失忆”、成本暴涨等黑箱问题。

### 主要功能

- 记录原始请求与响应：完整 System Prompt、消息列表与角色、工具调用与返回、工具定义与参数 Schema、流式响应分片，以及逐请求 Token 统计（输入、输出、缓存读写）。
- 相邻请求 Diff（Diff with Prev）：字符级高亮对比两轮请求的新增消息、删除内容、系统提示词微调与工具参数变化。
- 两种流量捕获：反向代理（可配置 BaseURL 的客户端，如 Claude Code、Codex CLI）与正向代理（不支持改 BaseURL 的客户端，自动注入代理环境变量与本地 CA 证书完成 TLS 解密）。
- Trace 以 JSONL 写入本地；实时面板通过 SSE 推送；会话退出可导出自包含 HTML 查看器，便于复盘与分享。
- 认证请求头落盘前整体替换为 `***`（不保留凭证前缀），上游仍收到原始请求头；无需云端仪表盘。
- 支持多种客户端：Claude Code、Codex CLI/App、Gemini CLI、Grok Build CLI、DeepSeek Harness、Kimi CLI、MiMo Code、OpenCode、OpenClaw、Pi、Hermes Agent、Cursor CLI/IDE Agent、Qoder CLI、Antigravity CLI、CodeBuddy CLI。

### 环境要求

- Python 3.11 及以上，并安装待观测的客户端。
- 安装：`uv tool install claude-tap`，或 `pip install claude-tap`。

### 使用限制

- Cursor CLI/IDE Agent 通过监听本地 transcript 记录工作，不是代理抓取原始 HTTP 请求体，只能拿到整理后的会话。
- 流式事件默认不写入 Trace；需要完整 SSE 分片时追加 `--tap-store-stream-events`。
- 脱敏仅覆盖认证请求头；请求体、响应体、URL 与诊断文本不会脱敏，导出的 Trace 文件不要随意外发。
- 部分上游（如 AWS 原生 Bedrock 的 SigV4 签名请求）需使用正向代理模式，避免改写 Base URL 破坏签名校验。

### 开始使用

1. 用 `uv tool install claude-tap` 或 `pip install claude-tap` 安装。
2. 通过 `claude-tap` 启动目标客户端（默认录制 Claude Code 并开启实时浏览器查看）；其他客户端用 `claude-tap --tap-client codex`、`claude-tap --tap-client gemini -- -p "hello"` 等。
3. 在实时面板查看每次调用，使用相邻请求 Diff 定位上下文变化，并按需导出自包含 HTML 归档。

### 收录与来源

AI 任务用途已依据官方 README 核对。Star 为 2026-11-23T16:00:50.764479Z 的快照，3365 Star，达到总量 ≥1,000 条件；月净增基线缺失，未用于准入。

近期活动：[2026-11-16 · commit](https://github.com/liaohch3/claude-tap/commit/b21d17157b674a0562e0ed08f4c4c607e8e5a56f)，标题「fix: fully mask sensitive trace headers (#480)」。

本次为文档复核，未安装或运行上游项目。上述提交证明复核日前推 3 个日历月窗口内的活动，不代表软件运行验证。许可不作为本次准入条件。

- [Official README](https://github.com/liaohch3/claude-tap/blob/main/README.md)
- [Local AI Agent Trace Viewer](https://liaohch3.com/claude-tap/)
- [How to view agent traces locally](https://github.com/liaohch3/claude-tap/blob/main/docs/guides/agent-trace-viewer.md)

## English

claude-tap is a local proxy and trace viewer for AI coding agents. Run your CLI through it, or listen to local app transcripts, then inspect the real API traffic and agent context: system prompts, conversation history, tool schemas, tool calls, streaming responses, token usage, and request diffs.

It helps developers of AI coding agents debug abnormal behavior, verify that prompts reached the agent, break down token costs, and archive sessions for reviewing black-box issues such as context loss or cost spikes.

### Features

- Record raw requests and responses: full system prompt, message lists and roles, tool calls and results, tool definitions and parameter schemas, streaming chunks, and per-request token usage (input, output, cache read/write).
- Diff with Prev: character-level highlight comparison of adjacent requests, showing added messages, removed content, system prompt tweaks, and tool parameter changes.
- Two capture modes: reverse proxy for clients with a configurable BaseURL (Claude Code, Codex CLI) and forward proxy for clients without one, which injects proxy environment variables and a local CA certificate for TLS decryption.
- Traces are written as JSONL locally; the live panel is driven by SSE; sessions can export a self-contained HTML viewer for review and sharing.
- Auth headers are fully replaced with `***` before recording (without retaining credential prefixes), while upstream still receives the original headers; no hosted dashboard is required.
- Supports many clients: Claude Code, Codex CLI/App, Gemini CLI, Grok Build CLI, DeepSeek Harness, Kimi CLI, MiMo Code, OpenCode, OpenClaw, Pi, Hermes Agent, Cursor CLI/IDE Agent, Qoder CLI, Antigravity CLI, and CodeBuddy CLI.

### Requirements

- Python 3.11+ and the client you want to trace.
- Install with `uv tool install claude-tap` or `pip install claude-tap`.

### Limitations

- Cursor CLI/IDE Agent works by watching local transcripts rather than proxying raw HTTP request bodies, so only the organized conversation is available.
- Streaming events are not recorded by default; add `--tap-store-stream-events` to keep full SSE chunks.
- Redaction covers auth headers only; request bodies, response bodies, URLs, and diagnostic text are not redacted, so do not share exported traces freely.
- Some upstreams (such as native AWS Bedrock SigV4 requests) need forward proxy mode to avoid rewriting the base URL and breaking signature validation.

### Getting started

1. Install with `uv tool install claude-tap` or `pip install claude-tap`.
2. Launch the target client through `claude-tap` (Claude Code by default, with the live browser viewer on); for other clients use `claude-tap --tap-client codex`, `claude-tap --tap-client gemini -- -p "hello"`, etc.
3. Inspect each call in the live panel, use the adjacent-request diff to locate context changes, and export a self-contained HTML archive as needed.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-23T16:00:50.764479Z is 3365, meeting the total-Star threshold of 1,000. The monthly-growth baseline is missing and was not used for admission.

Recent activity: [2026-11-16 · commit](https://github.com/liaohch3/claude-tap/commit/b21d17157b674a0562e0ed08f4c4c607e8e5a56f), titled 'fix: fully mask sensitive trace headers (#480)'.

This is a documentation review; the upstream software was not installed or run. The cited commit establishes activity within the three-calendar-month review window, not runtime validation. Licensing is not an admission criterion.

- [Official README](https://github.com/liaohch3/claude-tap/blob/main/README.md)
- [Local AI Agent Trace Viewer](https://liaohch3.com/claude-tap/)
- [How to view agent traces locally](https://github.com/liaohch3/claude-tap/blob/main/docs/guides/agent-trace-viewer.md)

## Review evidence

本次依据公开文章和 GitHub 官方文档复核，未安装或运行上游项目。

Reviewed against public articles and official GitHub documentation; upstream software was not installed or run.

- [GitHub activity](https://github.com/liaohch3/claude-tap/commit/b21d17157b674a0562e0ed08f4c4c607e8e5a56f) (2026-11-16T14:07:32Z)
- [Discovery article](https://mp.weixin.qq.com/s?__biz=MzIyOTY1ODAzNQ==&mid=2247489418&idx=1&sn=1a07fbd26540fcf944e1a141efc8f3ca&chksm=e8be0b56dfc982405d33734e652965c373cb00a8e1dd0904e3d38337449a3825e6c638d4cfc3)

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-23T16:00:50.764479Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "claude-tap",
    "name": "claude-tap",
    "repository": "liaohch3/claude-tap",
    "repo_node_id": "R_kgDORQz-bQ",
    "category": "development",
    "summary": {
      "zh-CN": "面向 AI 编程智能体的本地代理与 Trace 查看器，记录并展示真实 API 流量、上下文、Token 用量与请求 Diff，用于调试智能体行为。",
      "en": "A local proxy and trace viewer for AI coding agents that records real API traffic, context, token usage, and request diffs for debugging agent behavior."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-23T16:00:50.764479Z",
        "en": "2026-11-23T16:00:50.764479Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "面向 AI 编程智能体的本地代理与 Trace 查看器，记录并展示真实 API 流量、上下文、Token 用量与请求 Diff，用于调试智能体行为。",
        "en": "A local proxy and trace viewer for AI coding agents that records real API traffic, context, token usage, and request diffs for debugging agent behavior."
      },
      "source_url": "https://github.com/liaohch3/claude-tap/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/liaohch3/claude-tap/commit/b21d17157b674a0562e0ed08f4c4c607e8e5a56f",
        "occurred_at": "2026-11-16T14:07:32Z",
        "reviewed_at": "2026-11-23T16:00:50.764479Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "GitHub API 记录的具体活动，证明复核窗口内有活动；不代表运行验证。",
          "en": "A specific GitHub API activity establishes activity in the review window, not runtime validation."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/liaohch3/claude-tap/blob/main/README.md"
      },
      {
        "title": "Discovery article",
        "url": "https://mp.weixin.qq.com/s?__biz=MzIyOTY1ODAzNQ==&mid=2247489418&idx=1&sn=1a07fbd26540fcf944e1a141efc8f3ca&chksm=e8be0b56dfc982405d33734e652965c373cb00a8e1dd0904e3d38337449a3825e6c638d4cfc3"
      }
    ]
  },
  "snapshot": {
    "full_name": "liaohch3/claude-tap",
    "repo_node_id": "R_kgDORQz-bQ",
    "stargazers_count": 3365,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-23T16:00:50.764479Z",
    "source_url": "https://api.github.com/repos/liaohch3/claude-tap"
  }
}
```

</details>
