# OpenMotion

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[nexu-io/openmotion](https://github.com/nexu-io/openmotion)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 16254 |
| 评估时间 / Evaluated at | 2026-11-25T16:00:41.011041Z |

## 中文

OpenMotion 是开源的 Claude Motion 与 CapCut 替代方案，定位为 full-stack 智能体视频工作台。它把视频创作变成可编辑的 HTML 工程：由 Agent 拆解参考视频、重建镜头与转场、补齐缺失素材，在 Studio 中调整时间轴，并从同一工程渲染 MP4。

它帮助 AI 智能体完成视频创作与复刻任务：通过 MCP 接入本地 Agent，用 Motion.md 描述镜头顺序与时间，产出可版本管理的视频工程。

### 主要功能

- 代码化视频：用 HTML 编写视频，Agent 拆解参考视频、重建镜头与转场、生成缺失素材；在 Studio 调整时间并从同一工程渲染 MP4。
- BYOA / BYOK：免费开源，用自带 API 密钥在本地 Agent 中复刻视频；README 列出支持 Claude Code、Codex、WorkBuddy 等，GitHub 描述称支持 22 个 Agent（含 DSH）。
- Motion.md：用 Markdown 描述镜头顺序、时间与转场的标准化格式。
- 多模态素材：GPT Image 2.6 生成图像、Seedance 2.5 添加镜头、Suno 配乐、Eleven v4 旁白。
- 接入方式：ChatGPT Marketplace 一键安装；Skills CLI `npx skills add nexu-io/openmotion --skill openmotion`；Cloud MCP 通过 OAuth 2.1 的 Streamable HTTP `/mcp` 端点连接。
- 模板库提供 300+ Motion.md 指南与模板，覆盖产品发布、品牌片、讲解、数据故事、音乐视觉、口播剪辑等场景。
- 可导入 HyperFrames 工程 ZIP 继续编辑合成与本地素材。

### 环境要求

- ChatGPT Marketplace 安装无需手动配置。
- Agent 接入使用 Skills CLI；连接 Cloud MCP 需 OAuth 授权，参见 `docs/install.md`。
- 本地运行仓库的示例命令使用 Git、npm 与 Node.js 26.11.1（README 徽章标注 Node.js 22.18+）。
- 自托管部署参见 `deploy/README.md`。

### 使用限制

- 默认连接路径是托管的 Cloud MCP（OAuth 2.1）；本地 stdio 与 npm 安装被标为 legacy/archived，需要额外配置。
- 已发布的 npm 版本可能落后于当前仓库检出版本。
- 导入 HyperFrames 工程会创建独立副本，且要求受支持的原生工程结构。
- 本次为文档复核，未安装或运行上游项目，不构成实机验证。

### 开始使用

1. 通过 ChatGPT Marketplace 一键安装，或运行 `npx skills add nexu-io/openmotion --skill openmotion` 安装 Skill。
2. 按 `docs/install.md` 将 Agent 连接 Cloud MCP（OAuth 2.1）；授权后打开模板库，选择模板并发送需求。
3. 本地部署：克隆仓库后执行 `npm ci`、`npm run build:studio`、`npm start`，打开终端输出的 `studioUrl` 或 `previewUrl`。

### 收录与来源

AI 任务用途已依据官方 README 与 GitHub 仓库描述核对。Star 为 2026-11-25T16:00:41Z 的快照，数值 16254，达到总量 ≥1,000 条件。近期活动：[2026-11-25 · commit](https://github.com/nexu-io/openmotion/commit/af8d761badc8d60d58073ebb9fc35b0cbf940088)。本次为文档复核，未安装或运行上游项目；该提交仅证明窗口内活动，不代表运行验证。许可不作为准入条件。

- [Official README](https://github.com/nexu-io/openmotion/blob/main/README.md)
- [Install guide](https://github.com/nexu-io/openmotion/blob/main/docs/install.md)
- [Self-hosted deploy guide](https://github.com/nexu-io/openmotion/blob/main/deploy/README.md)
- [Template library](https://open-design.ai/templates/)

## English

OpenMotion is an open-source alternative to Claude Motion and CapCut, positioned as a full-stack agentic video studio. It turns video creation into an editable HTML project: an agent breaks down a reference video, rebuilds its shots and transitions, and generates missing assets; you adjust timing in Studio and render an MP4 from the same project.

It helps AI agents complete video creation and recreation tasks: via MCP it connects to a local agent, uses Motion.md to describe shot order and timing, and produces a version-controllable video project.

### Features

- Code video in HTML: the agent breaks down a reference video, rebuilds shots and transitions, and generates missing assets; adjust timing in Studio and render an MP4 from the same project.
- BYOA / BYOK: free and open source; recreate videos in a local agent with your own API keys. The README lists Claude Code, Codex, WorkBuddy and others; the GitHub description states support for 22 agents (including DSH).
- Motion.md: a Markdown format describing shot order, timing and transitions.
- Multimodal assets: GPT Image 2.6 for images, Seedance 2.5 for shots, Suno for music, Eleven v4 for narration.
- Entry points: one-click ChatGPT Marketplace install; Skills CLI `npx skills add nexu-io/openmotion --skill openmotion`; Cloud MCP via a Streamable HTTP `/mcp` endpoint with OAuth 2.1.
- A template library of 300+ Motion.md guides and templates covers product launches, brand films, explainers, data stories, music visuals and talking-head edits.
- Import a HyperFrames project ZIP to continue editing its composition and local assets.

### Requirements

- ChatGPT Marketplace installation requires no manual configuration.
- Agent installation uses the Skills CLI; connecting Cloud MCP requires OAuth authorization, see `docs/install.md`.
- The local repository example uses Git, npm and Node.js 26.11.1 (the README badge notes Node.js 22.18+).
- For self-hosted deployments see `deploy/README.md`.

### Limitations

- The default connection path is hosted Cloud MCP (OAuth 2.1); local stdio and npm setup are marked legacy/archived and require extra configuration.
- Published npm versions can lag behind this checkout.
- Importing a HyperFrames project creates an independent copy and requires a supported native project structure.
- This is a documentation review; the upstream software was not installed or run, so it is not runtime validation.

### Getting started

1. Install with one click from ChatGPT Marketplace, or run `npx skills add nexu-io/openmotion --skill openmotion` to add the Skill.
2. Follow `docs/install.md` to connect your agent to Cloud MCP (OAuth 2.1); after authorization, open the template library, choose a template and send your brief.
3. For local deployment, clone the repository, then run `npm ci`, `npm run build:studio`, `npm start`, and open the printed `studioUrl` or `previewUrl`.

### Review and sources

The documented AI task use was reviewed against the official README and GitHub repository description. The Star snapshot at 2026-11-25T16:00:41Z is 16254, meeting the total-Star threshold of 1,000. Recent activity: [2026-11-25 · commit](https://github.com/nexu-io/openmotion/commit/af8d761badc8d60d58073ebb9fc35b0cbf940088). This is a documentation review; the upstream software was not installed or run. The cited commit establishes activity within the review window, not runtime validation. Licensing is not an admission criterion.

- [Official README](https://github.com/nexu-io/openmotion/blob/main/README.md)
- [Install guide](https://github.com/nexu-io/openmotion/blob/main/docs/install.md)
- [Self-hosted deploy guide](https://github.com/nexu-io/openmotion/blob/main/deploy/README.md)
- [Template library](https://open-design.ai/templates/)

## Review evidence

本次依据公开文章和 GitHub 官方文档复核，未安装或运行上游项目。

Reviewed against public articles and official GitHub documentation; upstream software was not installed or run.

- [GitHub activity](https://github.com/nexu-io/openmotion/commit/af8d761badc8d60d58073ebb9fc35b0cbf940088) (2026-11-25T14:38:58Z)
- [Discovery article](https://mp.weixin.qq.com/s?__biz=MzIyOTY1ODAzNQ==&mid=2247489491&idx=1&sn=f38b9c513e90111621f83dfc533e93f3&chksm=e8be0b0fdfc98219acafe3a6f3ff2ca365ad12e09ea42f5bf055099a64e546491dd04ef74383)

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-25T16:00:41.011041Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "openmotion",
    "name": "OpenMotion",
    "repository": "nexu-io/openmotion",
    "repo_node_id": "R_kgDOSaLB4g",
    "category": "media",
    "summary": {
      "zh-CN": "开源智能体视频工作台，用 HTML 与 Motion.md 编写可编辑视频工程，经 MCP 接入本地 Agent 复刻参考视频并渲染 MP4。",
      "en": "Open-source agentic video studio that codes editable video projects in HTML and Motion.md, connects to local agents via MCP, and renders MP4s."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-25T16:00:41.011041Z",
        "en": "2026-11-25T16:00:41.011041Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "开源智能体视频工作台，用 HTML 与 Motion.md 编写可编辑视频工程，经 MCP 接入本地 Agent 复刻参考视频并渲染 MP4。",
        "en": "Open-source agentic video studio that codes editable video projects in HTML and Motion.md, connects to local agents via MCP, and renders MP4s."
      },
      "source_url": "https://github.com/nexu-io/openmotion/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/nexu-io/openmotion/commit/af8d761badc8d60d58073ebb9fc35b0cbf940088",
        "occurred_at": "2026-11-25T14:38:58Z",
        "reviewed_at": "2026-11-25T16:00:41.011041Z",
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
        "url": "https://github.com/nexu-io/openmotion/blob/main/README.md"
      },
      {
        "title": "Discovery article",
        "url": "https://mp.weixin.qq.com/s?__biz=MzIyOTY1ODAzNQ==&mid=2247489491&idx=1&sn=f38b9c513e90111621f83dfc533e93f3&chksm=e8be0b0fdfc98219acafe3a6f3ff2ca365ad12e09ea42f5bf055099a64e546491dd04ef74383"
      }
    ]
  },
  "snapshot": {
    "full_name": "nexu-io/openmotion",
    "repo_node_id": "R_kgDOSaLB4g",
    "stargazers_count": 16254,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-25T16:00:41.011041Z",
    "source_url": "https://api.github.com/repos/nexu-io/openmotion"
  }
}
```

</details>
