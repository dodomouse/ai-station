# OpenSRE

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 部署与运维 / Operations |
| 状态 / Status | 已收录 / Included |
| Star | 13853 |
| 评估时间 / Evaluated at | 2026-11-21T16:00:40.055646Z |

## 中文

OpenSRE 是面向 CI/CD 可靠性的开源 AI SRE 智能体。它作为 CLI 智能体读取失败的 CI 运行、追踪根因并推送修复供人工审查，可自托管并使用自带模型。项目当前处于 Public Alpha。

它帮助运维与开发团队自动调查 CI 失败与生产告警：跨已连接系统收集证据，区分 CI 环境抖动与代码缺陷，并给出带证据链的结论与修复建议。

### 主要功能

- CI 运行失败或收到告警时，自动抓取相关上下文：失败的检查与日志、近期提交与部署，以及关联的日志、指标与 trace。
- 在工具调用循环中跨系统推理验证假设，区分 CI 原因与代码原因；可在调用外部 LLM 前脱敏敏感标识。
- 给出带证据链接的回答，将根因修复推送到 PR 分支供审查，或把摘要发到 Slack、PagerDuty、Telegram。
- 提供交互式 REPL（含 /help、/status、/cost、/sessions、/resume、/compact、/new、/exit，以及 /integrations list、/integrations verify）与无头 CLI，可用 opensre ask 后接自然语言问题发起单次调用。
- 提供 Python API（源码环境下 from surfaces.embedded import start_embedded_session）用于进程内驱动智能体。
- 连接 60+ 集成，覆盖 LLM 提供商、可观测、基础设施、数据库、数据平台、开发工具、事故管理、通信、智能体部署及 MCP 协议。

### 环境要求

- 需在一个代码项目的终端中使用，推荐具备 Git 仓库以演示完整流程。
- macOS / Linux 用 curl 安装脚本（curl -fsSL https://install.opensre.com | bash -s -- -gh）；Windows 用 PowerShell 安装脚本；启动命令为 opensre。
- 需配置 LLM 提供商及其 API key，例如 Anthropic、OpenAI、Ollama、Google Gemini、Bedrock 等。
- 部署可选本地 CLI、Cloud 托管网关、AMI + systemd 网关（仅 Telegram、不含 Docker）或自托管容器（使用仓库 Dockerfile，设置 MODE、LLM_PROVIDER 与 API key；仅当网关需要共享 Postgres 状态时才设置 DATABASE_URL）。

### 使用限制

- Public Alpha：核心工作流可用于早期探索但尚未完全稳定，API 与集成可能变化，不建议无约束接管生产。
- 需要可观测数据；零日志、零监控的环境无法凭空识别异常。
- 交互式 REPL 需要 TTY；无头调用与会话控制依赖相应命令及工具审批机制。
- 部分集成仍在路线图（Linear、Notion、Teams、Confluence）；Trello 仅提供客户端助手；AMI 网关路径仅支持 Telegram 且无 Docker。

### 开始使用

1. 在代码项目终端中安装：macOS/Linux 执行 curl -fsSL https://install.opensre.com | bash -s -- -gh，Windows 按官方 Windows 安装文档用 PowerShell 安装。
2. 运行 opensre 登录并进入 REPL，用自然语言描述事故，观察智能体的调查过程。
3. 配置 LLM 提供商与 API key，用 opensre ask 发起无头调用，并用 opensre integrations setup 管理集成。更多见官方 Quickstart 与 Docs。

### 收录与来源

AI 任务用途已依据官方 README 核对。Star 为 2026-11-21T16:00:40.055646Z 的快照，总数 13,853，达到总量 ≥1,000 条件；因总 Star 条件已满足，未另行核对月净增。近期活动为 2026-11-21 的 commit。本次为文档复核，未安装或运行上游项目，不代表运行验证；许可不作为准入条件。

- [Official README](https://github.com/Tracer-Cloud/opensre/blob/main/README.md)
- [Quickstart](https://www.opensre.com/docs/getting-started/quickstart)
- [Docs](https://www.opensre.com/docs)
- [Install locally](https://www.opensre.com/docs/install/install-local)
- [Headless CLI](https://www.opensre.com/docs/guides/headless-cli)
- [Python API](https://www.opensre.com/docs/guides/python-api)

## English

OpenSRE is an open-source AI SRE agent for CI/CD reliability. As a CLI agent it reads failed CI runs, traces root causes, and pushes fixes for human review. It is self-hosted and runs with your own models. The project is in Public Alpha.

It helps operations and engineering teams investigate CI failures and production alerts automatically: gathering evidence across connected systems, separating CI-caused failures from code-caused ones, and returning evidence-linked conclusions and fixes.

### Features

- On a failed CI run or an incoming alert, automatically fetches relevant context: failing checks and logs, recent commits and deploys, and correlated logs, metrics, and traces.
- Reasons across connected systems in a tool-calling loop to test hypotheses, separating CI-caused failures from code-caused ones; sensitive identifiers can be masked before external LLM calls.
- Returns an evidence-linked answer, pushes the root-cause fix to the PR branch for review, or posts a summary to Slack, PagerDuty, or Telegram.
- Provides an interactive REPL (with /help, /status, /cost, /sessions, /resume, /compact, /new, /exit, plus /integrations list and /integrations verify) and a headless CLI invoked with opensre ask followed by a natural-language question.
- Offers a Python API (from surfaces.embedded import start_embedded_session from a source checkout) for in-process agent control.
- Connects 60+ integrations across LLM providers, observability, infrastructure, databases, data platforms, dev tools, incident management, communication, agent deployment, and the MCP protocol.

### Requirements

- Run from a terminal inside a code project; a Git repository is recommended for the full workflow.
- On macOS/Linux use the curl install script (curl -fsSL https://install.opensre.com | bash -s -- -gh); on Windows use the PowerShell install script; start with opensre.
- Configure an LLM provider and its API key, for example Anthropic, OpenAI, Ollama, Google Gemini, or Bedrock.
- Deployment options: local CLI, OpenSRE Cloud managed gateway, a gateway AMI + systemd path (Telegram only, no Docker), or a self-hosted container using the repo Dockerfile with MODE, LLM_PROVIDER, and an API key; set DATABASE_URL only when the gateway needs shared Postgres-backed state.

### Limitations

- Public Alpha: core workflows are usable for early exploration but not yet fully stable; APIs and integrations may evolve. Unconstrained takeover of production is not recommended.
- Observability data is required; environments with no logs or metrics cannot be investigated from nothing.
- The interactive REPL requires a TTY; headless calls and session control depend on the documented commands and tool-approval mechanism.
- Some integrations remain on the roadmap (Linear, Notion, Teams, Confluence); Trello offers client helpers only; the AMI gateway path supports Telegram only and no Docker.

### Getting started

1. Install from a terminal in your code project: on macOS/Linux run curl -fsSL https://install.opensre.com | bash -s -- -gh; on Windows follow the official Windows install doc for PowerShell.
2. Run opensre to sign in and open the REPL, then describe an incident in plain language and watch the investigation.
3. Configure an LLM provider and API key, use opensre ask for a headless turn, and manage integrations with opensre integrations setup. See the official Quickstart and Docs for more.

### Review and sources

The documented AI task use was reviewed against the official README. The Star snapshot at 2026-11-21T16:00:40.055646Z shows 13,853 stars, meeting the total-Star threshold of 1,000; monthly net growth was not separately verified because the total-Star condition is met. Recent activity includes a commit on 2026-11-21. This is a documentation review; the upstream software was not installed or run, so this is not runtime validation. Licensing is not an admission criterion.

- [Official README](https://github.com/Tracer-Cloud/opensre/blob/main/README.md)
- [Quickstart](https://www.opensre.com/docs/getting-started/quickstart)
- [Docs](https://www.opensre.com/docs)
- [Install locally](https://www.opensre.com/docs/install/install-local)
- [Headless CLI](https://www.opensre.com/docs/guides/headless-cli)
- [Python API](https://www.opensre.com/docs/guides/python-api)

## Review evidence

本次依据公开文章和 GitHub 官方文档复核，未安装或运行上游项目。

Reviewed against public articles and official GitHub documentation; upstream software was not installed or run.

- [GitHub activity](https://github.com/Tracer-Cloud/opensre/commit/98430da0cce7b43fba2a9f5dc33d148c77356f02) (2026-11-21T07:38:36Z)
- [Discovery article](https://mp.weixin.qq.com/s?__biz=MzIyOTY1ODAzNQ==&mid=2247489348&idx=1&sn=70bb0148d03addd73d5921e85be355ee&chksm=e8be0b98dfc9828e1421e970309231fb2ddaa79cc6aa6d105a3e955d94969fa5c703def712bc)

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-21T16:00:40.055646Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "opensre",
    "name": "OpenSRE",
    "repository": "Tracer-Cloud/opensre",
    "repo_node_id": "R_kgDOQ4pdCg",
    "category": "operations",
    "summary": {
      "zh-CN": "开源 AI SRE 智能体，自动调查 CI/CD 失败与生产告警，跨系统收集证据、区分根因并推送修复供审查，可自托管并使用自带模型。",
      "en": "Open-source AI SRE agent that investigates CI/CD failures and production alerts, gathers evidence across systems, distinguishes root causes, and pushes fixes for review; self-hosted with your own models."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-21T16:00:40.055646Z",
        "en": "2026-11-21T16:00:40.055646Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "开源 AI SRE 智能体，自动调查 CI/CD 失败与生产告警，跨系统收集证据、区分根因并推送修复供审查，可自托管并使用自带模型。",
        "en": "Open-source AI SRE agent that investigates CI/CD failures and production alerts, gathers evidence across systems, distinguishes root causes, and pushes fixes for review; self-hosted with your own models."
      },
      "source_url": "https://github.com/Tracer-Cloud/opensre/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/Tracer-Cloud/opensre/commit/98430da0cce7b43fba2a9f5dc33d148c77356f02",
        "occurred_at": "2026-11-21T07:38:36Z",
        "reviewed_at": "2026-11-21T16:00:40.055646Z",
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
        "url": "https://github.com/Tracer-Cloud/opensre/blob/main/README.md"
      },
      {
        "title": "Discovery article",
        "url": "https://mp.weixin.qq.com/s?__biz=MzIyOTY1ODAzNQ==&mid=2247489348&idx=1&sn=70bb0148d03addd73d5921e85be355ee&chksm=e8be0b98dfc9828e1421e970309231fb2ddaa79cc6aa6d105a3e955d94969fa5c703def712bc"
      }
    ]
  },
  "snapshot": {
    "full_name": "Tracer-Cloud/opensre",
    "repo_node_id": "R_kgDOQ4pdCg",
    "stargazers_count": 13853,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-21T16:00:40.055646Z",
    "source_url": "https://api.github.com/repos/Tracer-Cloud/opensre"
  }
}
```

</details>
