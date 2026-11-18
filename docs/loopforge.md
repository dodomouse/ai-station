# LoopForge

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[Tencent/LoopForge](https://github.com/Tencent/LoopForge)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 自动化 / Automation |
| 状态 / Status | 已收录 / Included |
| Star | 3731 |
| 评估时间 / Evaluated at | 2026-11-18T13:55:08.307724Z |

## 中文

LoopForge 是自托管的工作区，供团队用编码 Agent 交付软件。在聊天中向 Main Bot 描述需求，它会打开 Docker 沙箱、检出仓库、把工作派发给项目角色，并提交 PR。当某种工作方式被验证有效后，可保存为 SOP（由 Agent、脚本与人工审批节点组成的标准流程），使下一个需求按同样方式交付，并内置评审与审批。

编码 Agent 的 CLI 负责实际执行：CodeBuddy、Codex、Claude Code、OpenCode、Cursor CLI、Antigravity、Kimi Code、Pi、DeepSeek Harness 与 ZCode。LoopForge 在其外层提供角色、沙箱、检查点与历史记录，全部运行在自有基础设施上。

### 主要功能

- 聊天工作台：Main Bot 支持按会话选择执行器、模型与权限模式；可用 `@` 引用角色、技能、需求、SOP 与仓库；回复运行中可排队消息或用 Steer 立即插话；生成的文件在侧栏预览、查看源码与下载。
- 会话工作区：按需创建带项目仓库的 Docker 沙箱，项目角色作为原生子代理运行，对正在运行的 SOP 工作区可直接暂停、恢复或接管。
- SOP 设计器：可视化画布支持 Agent、Script、Human gate（人工审批）、Sub-SOP 与 Preview 节点，可配置失败回退边、校验、版本历史与发布；内置后端、前端、缺陷修复与产品四类 SOP。
- 角色：可复用的定义，包含提示词、执行器、模型、规则、Skills、MCP 工具、产物与门禁，在 SOP 节点与聊天子代理间共享。
- 需求到交付：需求在 SOP 或聊天路径上端到端跟踪，含 PR/MR 状态跟踪、合并检测与直接合并到共享分支（`mode=direct`）。
- 运行与审批：实时节点状态、工具轨迹、worker 日志、逐节点产物快照与工作区预览，统一的 Needs review 收件箱。
- AI 定时任务：可复用的周期性代理任务，拥有完整工作区、SOP 与 MCP 访问权限，并提供带版本与参数的模板市场及新需求自动派发 SOP。
- 洞察与成本：工程指标、静态 HTML/SVG 导出的业务报告，以及按公开标价核算 SOP 与会话的 token/成本。
- 执行环境：平台 worker、Docker 沙箱，或接入使用自有工具与仓库的本地执行机。
- 团队能力：密码账号、项目与成员、明暗主题，以及 OpenAPI 描述的 HTTP 与 MCP API。

### 环境要求

- 平台版需先安装 Git 并克隆仓库；安装器检查 Docker、Compose、Python 3 与 curl，并可安装缺失组件。Python/curl 安装支持 Linux 上的 apt、dnf 与 yum；Compose 插件支持 x86_64/arm64 并校验官方发布 SHA-256。macOS 需要可用的 Python 3 与 Docker Desktop，可用 Homebrew 安装缺失组件。普通 Linux 用户通过 docker 组或 sudo 支持。宿主无需安装 Go 与 Node.js。
- 包与镜像下载需要联网。默认监听 `0.0.0.0:8090`，云主机上安装器会从云厂商元数据服务读取公网 IP 并打印，需在安全组放行端口或前置 HTTPS 反向代理。
- 聊天、文档与 SOP 的 Agent 步骤需要所选执行器的 API key（个人 key，或管理员为聊天与 SOP 运行配置的共享 key）。Claude Code、OpenCode、Kimi Code、Pi 首次使用时从 npm 安装并缓存。
- LoopForge Local 需 Node.js 20+、Python 3.8+ 与一个受支持的编码助手。

### 使用限制

- 默认 Compose 安装中，SOP 运行与会话工作区都通过宿主 Docker socket 启动沙箱容器；Docker socket 访问等于可控制宿主守护进程，此配置面向可信团队，不是不可信多租户隔离。
- 新安装监听所有网卡，登录用户可读取实例内项目数据，且队友可从登录页注册；对外暴露前应阅读账号与访问模型，并可用 `AGENTFLOW_ALLOW_SIGNUP=false` 关闭注册。
- 管理页面为英文与中文，聊天工作台目前仅为中文。
- 模型用量不含在内，需自备凭据；无 API key 时只能运行仅由脚本与人工审批组成的演示 SOP。
- 需求澄清、AI 通知摘要、Bot 回复与运行评估目前使用 CodeBuddy，其模型选择器只列出 CodeBuddy 模型，服务端会拒绝其他 CLI 的模型而非自动切换。
- Cursor CLI 与 Antigravity 首次聊天时由提供方安装，不安装进 SOP 沙箱；ZCode 未随附，需自行安装在服务或执行机的 PATH 中。
- 连接 GitLab、Gitea、Gogs 等 Git 主机需按部署文档配置 Git SSH；PR/MR 与 Issue 自动化还需要托管平台 API token 或单独配置的 MCP。
- Local 版目前只运行内置的 Classic/Portable 工作流，将平台 SOP 导出用于本地独立执行仍在计划中。

### 开始使用

1. 克隆仓库并运行 `./start.sh`。它会拉取 `compose.yaml` 中固定的 GHCR 发布镜像（不在本地构建），创建 MySQL 与平台服务，生成配置与会话密钥，并安装内置沙箱、入门 SOP 与欢迎项目。`bash scripts/install.sh` 效果相同。可用 `./start.sh logs|stop|restart|pull` 管理，`./start.sh dev` 从源码构建。
2. 打开安装器打印的地址并创建账号，第一个账号成为管理员。
3. 按首页快速指引添加模型 key、连接仓库并选择 SOP。若只想先体验，可切换到演示项目，在 Templates 中打开 “Platform check · script & approval”，点击 Run SOP，脚本写入报告后会在审批步骤等待，从 Needs review 或运行页批准后继续到最终产物。
4. 若要修改现有仓库并提交 PR，在个人设置中选择 Connect GitHub，在 GitHub 上批准设备码后选择仓库（内置 LoopForge OAuth App，无需 PAT，也可手动填入 PAT），再设置执行器凭据或绑定本地执行机。
5. 若 `ghcr.io` 下载缓慢，可设置 `MIRROR` 指向可替代 `ghcr.io` 的镜像站；该变量会把下载标记为官方名称，因此需信任该主机，可用 `docker image inspect` 核对摘要与 GitHub Release 记录一致。

### 收录与来源

AI 任务用途依据官方 README 核对：LoopForge 编排编码 Agent 完成需求澄清、实现、独立评审、测试与交付，并在人工审批门禁处暂停等待确认。

Star 为 2026-11-18T13:55:08Z 的快照，共 3731，达到总量 ≥1,000 条件；本次未核对近 1 个日历月的 Star 净增数据。

近期活动：[2026-11-18 · commit](https://github.com/Tencent/LoopForge/commit/48cdf0c2e2149c53d69cac089142f46c4b2e47f7)，标题为 `feat(runtime): custom run credentials for self-hosted deployments (#1032)`。

本次为文档复核，未安装或运行上游项目；上述提交只证明窗口内活动，不代表运行验证。许可不作为本次准入条件（README 徽章标注 MIT）。README 正文在抓取时被截断，功能与限制仅依据已获取的官方内容与官方文档链接。

- [Official README](https://github.com/Tencent/LoopForge/blob/main/README.md)
- [Deployment](https://github.com/Tencent/LoopForge/blob/main/docs/deployment.md)
- [Conversation workspaces](https://github.com/Tencent/LoopForge/blob/main/docs/conversation-workspaces.md)
- [Local usage](https://github.com/Tencent/LoopForge/blob/main/docs/local/usage.md)
- [Validation record](https://github.com/Tencent/LoopForge/blob/main/docs/validation.md)

## English

LoopForge is a self-hosted workspace where a team ships software with coding agents. Describe what you need to **Main Bot** in chat: it opens a Docker sandbox, checks out your repositories, delegates to project roles, and opens the PR. When a way of working proves itself, save it as an **SOP** (a standard workflow of agents, scripts and human gates) so the next requirement is delivered the same way, with review and approval built in.

Coding-agent CLIs do the work: CodeBuddy, Codex, Claude Code, OpenCode, Cursor CLI, Antigravity, Kimi Code, Pi, DeepSeek Harness and ZCode. LoopForge adds the roles, sandboxes, checkpoints and history around them, all on your own infrastructure.

### Features

- Chat workbench: Main Bot with per-conversation executor, model and permission mode; `@` references for roles, skills, requirements, SOPs and repositories; messages queue while a reply runs and *Steer* sends now; generated files open in a side panel with preview, source and download.
- Conversation workspaces: on-demand Docker sandboxes with the project's repositories checked out, project roles as native subagents, and direct control of a running SOP workspace (pause, resume, take over).
- SOP designer: visual canvas with Agent, Script, Human gate, Sub-SOP and Preview nodes, rework-on-failure edges, validation, version history and publishing; built-in backend, frontend, bug-fix and product SOPs.
- Roles: reusable definitions of prompt, executor, model, rules, Skills, MCP tools, artifacts and gates, shared across SOP nodes and chat subagents.
- Requirement → delivery: requirements tracked end to end on both the SOP and chat paths, with PR/MR status tracking, merge detection and direct merges into a shared branch (`mode=direct`).
- Runs and approvals: live node status, tool traces, worker logs, per-node artifact snapshots and workspace previews, with a single *Needs review* inbox.
- AI scheduled tasks: recurring agent tasks with full workspace, SOP and MCP access, a market of versioned parameterized task templates, and automatic SOP dispatch for new requirements.
- Insights and cost: engineering metrics, business-domain reports exportable as static HTML/SVG, and token/cost accounting for SOPs and conversations at public list prices.
- Execution environments: platform workers, Docker sandboxes, or a connected local execution machine using your own tools and repositories.
- Team-ready: password accounts, projects and members, light/dark/system themes, and an OpenAPI-described HTTP and MCP API.

### Requirements

- The platform install needs Git and a clone of the repository. The installer checks Docker, Compose, Python 3 and curl and offers to install missing components. Python/curl installation supports apt, dnf and yum on Linux; the Compose plugin supports x86_64/arm64 and verifies the official release SHA-256. macOS needs a working Python 3 and Docker Desktop, with Homebrew able to install missing components. Ordinary Linux users are supported through Docker group access or sudo. Host Go and Node.js installations are not required.
- Package and image downloads require internet access. The service listens on `0.0.0.0:8090` by default; on a cloud host the installer reads the public IP from the provider's metadata service and prints it, so the port must be allowed in the security group or fronted by an HTTPS reverse proxy.
- Chat, documents and SOP agent steps need an API key for the selected executor: a personal key, or a shared key an administrator configures for chat and SOP runs. Claude Code, OpenCode, Kimi Code and Pi are installed from npm on first use and then cached.
- LoopForge Local needs Node.js 20+, Python 3.8+ and a supported coding assistant.

### Limitations

- In the default Compose installation, SOP runs and conversation workspaces both start sandbox containers through the host Docker socket. Docker socket access grants control of the host daemon, so this setup is for trusted teams, not untrusted multi-tenant isolation.
- New installations listen on all interfaces; signed-in users can read project data across the instance and teammates can sign up from the login page. Read the account and access model before exposing it, and use `AGENTFLOW_ALLOW_SIGNUP=false` to turn signup off.
- Management pages are in English and Chinese; the chat workbench is Chinese for now.
- Model usage is not included; you bring your own credentials. Without an API key only the demo SOP, made of a script and a human gate, can run.
- Requirement clarification, AI notification summaries, Bot replies and run evals currently use CodeBuddy; their model pickers list CodeBuddy models only and the server refuses a model of another CLI instead of switching it.
- Cursor CLI and Antigravity are installed by the provider installer on first chat use and are not installed into SOP sandboxes; ZCode is not bundled and must be on the service or execution machine PATH.
- GitLab, Gitea, Gogs and other hosts need Git SSH configured as described in the deployment docs; PR/MR and Issue automation also needs a hosting API token or a separately configured MCP.
- Local runs the built-in Classic/Portable workflows today; exporting a platform SOP for standalone local execution is planned.

### Getting started

1. Clone the repository and run `./start.sh`. It pulls the GHCR release image pinned in `compose.yaml` without building locally, creates the MySQL and platform services, generates configuration and session secrets, and installs the built-in sandboxes, starter SOPs and welcome project. `bash scripts/install.sh` does the same. Manage it with `./start.sh logs|stop|restart|pull`, or build the checkout from source with `./start.sh dev`.
2. Open the address printed by the installer and create your account; the first one becomes the administrator.
3. Follow the home page's quick-access guide to add a model key, connect a repository and choose an SOP. To try it without a key, switch to the demo project, open *Templates → Platform check · script & approval*, run the SOP; a real script writes a report and the run waits at the approval step, which you approve from *Needs review* or the run page.
4. To change an existing repository and open a PR, choose *Connect GitHub* in personal settings, approve the device code on GitHub and pick a repository (the LoopForge OAuth App is built in, no PAT required, manual PAT entry still works), then set executor credentials or bind a local execution machine.
5. If downloads from `ghcr.io` stall, set `MIRROR` to a registry host that can stand in for `ghcr.io`. Setting `MIRROR` trusts that host, because the download is tagged with the official name; verify the digest with `docker image inspect` against the GitHub Release record.

### Review and sources

The documented AI task use was reviewed: LoopForge orchestrates coding agents through requirement clarification, implementation, independent review, testing and delivery, pausing at human approval gates.

The Star snapshot at 2026-11-18T13:55:08Z is 3731, meeting the total-Star threshold of 1,000. Star growth over the last calendar month was not checked.

Recent activity: [2026-11-18 · commit](https://github.com/Tencent/LoopForge/commit/48cdf0c2e2149c53d69cac089142f46c4b2e47f7), `feat(runtime): custom run credentials for self-hosted deployments (#1032)`.

This is a documentation review; the upstream software was not installed or run. The cited commit establishes activity within the review window, not runtime validation. Licensing is not an admission criterion (the README badge states MIT). The README body was truncated during retrieval, so features and limitations rely only on the retrieved official content and the official documentation links.

- [Official README](https://github.com/Tencent/LoopForge/blob/main/README.md)
- [Deployment](https://github.com/Tencent/LoopForge/blob/main/docs/deployment.md)
- [Conversation workspaces](https://github.com/Tencent/LoopForge/blob/main/docs/conversation-workspaces.md)
- [Local usage](https://github.com/Tencent/LoopForge/blob/main/docs/local/usage.md)
- [Validation record](https://github.com/Tencent/LoopForge/blob/main/docs/validation.md)

## Review evidence

本次依据公开文章和 GitHub 官方文档复核，未安装或运行上游项目。

Reviewed against public articles and official GitHub documentation; upstream software was not installed or run.

- [GitHub activity](https://github.com/Tencent/LoopForge/commit/48cdf0c2e2149c53d69cac089142f46c4b2e47f7) (2026-11-18T08:36:16Z)
- [Discovery article](https://mp.weixin.qq.com/s?__biz=MzIyOTY1ODAzNQ==&mid=2247489266&idx=1&sn=6d76b348d95bc1ea60b57d6b1d0c612f&chksm=e8be0a2edfc983383f2cc7604e7e2917761350fba4bc95d762e0209e6bce8e6a2ba6a94976a4)

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-18T13:55:08.307724Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "loopforge",
    "name": "LoopForge",
    "repository": "Tencent/LoopForge",
    "repo_node_id": "R_kgDOTlnVHA",
    "category": "automation",
    "summary": {
      "zh-CN": "自托管的编码 Agent 交付编排平台，用 SOP、Docker 沙箱与人工审批组织 CodeBuddy、Codex、Claude Code 等执行器完成需求交付。",
      "en": "Self-hosted orchestration platform that runs coding agents through SOPs, Docker sandboxes and human approval gates to deliver requirements."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-18T13:55:08.307724Z",
        "en": "2026-11-18T13:55:08.307724Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "自托管的编码 Agent 交付编排平台，用 SOP、Docker 沙箱与人工审批组织 CodeBuddy、Codex、Claude Code 等执行器完成需求交付。",
        "en": "Self-hosted orchestration platform that runs coding agents through SOPs, Docker sandboxes and human approval gates to deliver requirements."
      },
      "source_url": "https://github.com/Tencent/LoopForge/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/Tencent/LoopForge/commit/48cdf0c2e2149c53d69cac089142f46c4b2e47f7",
        "occurred_at": "2026-11-18T08:36:16Z",
        "reviewed_at": "2026-11-18T13:55:08.307724Z",
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
        "url": "https://github.com/Tencent/LoopForge/blob/main/README.md"
      },
      {
        "title": "Discovery article",
        "url": "https://mp.weixin.qq.com/s?__biz=MzIyOTY1ODAzNQ==&mid=2247489266&idx=1&sn=6d76b348d95bc1ea60b57d6b1d0c612f&chksm=e8be0a2edfc983383f2cc7604e7e2917761350fba4bc95d762e0209e6bce8e6a2ba6a94976a4"
      }
    ]
  },
  "snapshot": {
    "full_name": "Tencent/LoopForge",
    "repo_node_id": "R_kgDOTlnVHA",
    "stargazers_count": 3731,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-18T13:55:08.307724Z",
    "source_url": "https://api.github.com/repos/Tencent/LoopForge"
  }
}
```

</details>
