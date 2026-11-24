# AG-UI

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[ag-ui-protocol/ag-ui](https://github.com/ag-ui-protocol/ag-ui)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 21514 |
| 评估时间 / Evaluated at | 2026-11-24T16:00:56.070203Z |

## 中文

AG-UI 是一个开源、轻量、基于事件的协议，用来标准化 AI 智能体与用户界面的连接方式。智能体会流式输出 token、在执行中调用工具、更新共享状态、暂停等待人工确认、派生子智能体；AG-UI 用一条双向事件流取代各家自定义的接线方式，让同一个智能体可以驱动网页、手机、终端或 Slack 客户端。

它帮助 AI 完成任务：开发者接入不同智能体框架时可复用同一套界面逻辑，智能体把进度和结果以类型化事件推送给应用，并在需要人工拍板时停下等待。

### 主要功能

- 以 RunAgentInput 发起一次运行，智能体返回八类共 31 种类型化事件（生命周期、文本消息、工具调用、状态、推理、活动、子智能体、透传），只有运行生命周期事件是必需的。
- 支持流式聊天、生成式 UI、共享状态（快照与 JSON Patch 增量）、前端工具、human in the loop（interrupt 后批准、编辑或拒绝并续跑）、推理展示、子智能体与多模态。
- 传输无关：规范定义 HTTP + SSE 与 HTTP + Protobuf 二进制绑定，中间件可适配任意来源的事件。
- AG-UI 1.0 提供冻结规范与 JSON Schema，TypeScript、Python、.NET SDK 由规范生成，向后兼容 0.x；与 MCP（工具与上下文）、A2A（智能体协作）互补并可并存。

### 环境要求

- 直接对话协议：Python 3.9+，`pip install ag-ui-protocol fastapi uvicorn` 可起一个智能体服务。
- 客户端示例：Node.js 20+，`npm install @ag-ui/client tsx`。
- 脚手架：`npx create-ag-ui-app@latest` 生成接入所选智能体框架的前端（CopilotKit on Next.js 或终端客户端）；模板调用 OpenAI，需设置 `OPENAI_API_KEY`。

### 使用限制

- AG-UI 是运行时协议，不是生成式 UI 规范；A2UI、MCP Apps、Open-JSON-UI 负责描述界面载荷，AG-UI 负责在智能体与应用之间承载这些载荷。
- 官方列出 LangChain、CrewAI、Microsoft Agent Framework、Google ADK、AWS Strands、Mastra、Pydantic AI、LlamaIndex、Agno、AG2、Claude Agent SDK 等集成；接入未列出的框架需自行实现集成。
- 最小实现只需发出少量生命周期事件，完整能力需按规范逐项增加。

### 开始使用

1. 运行 `npx create-ag-ui-app@latest`，按提示选择前端与智能体框架，设置 `OPENAI_API_KEY` 后 `npm run dev`。
2. 或直接用协议：Python 端按 README 示例写 `RunAgentInput` 端点并流式返回事件（`uvicorn server:app --port 8000`），TypeScript 端用 `HttpAgent` 连接并 `runAgent`。
3. 参考 [Spec](https://docs.ag-ui.com/spec/1.0) 与 [Dojo 示例](https://dojo.ag-ui.com) 扩展生成式 UI、共享状态与人工确认等能力。

### 收录与来源

AI 任务用途已依据官方 README 核对：该项目标准化智能体与应用的事件交互，帮助构建与驱动 AI 智能体。Star 为 2026-11-24T16:00:56.070203Z 的快照，达到总量 ≥1,000 条件，eligibility=true。近期活动：[2026-11-24 · commit](https://github.com/ag-ui-protocol/ag-ui/commit/ed94ca4a3240527d3ef20fd0f0cc63501f44e469)。本次为文档复核，未安装或运行上游项目。

- [Official README](https://github.com/ag-ui-protocol/ag-ui/blob/main/README.md)
- [Spec 1.0](https://docs.ag-ui.com/spec/1.0)
- [Dojo examples](https://dojo.ag-ui.com)

## English

AG-UI is an open, lightweight, event-based protocol that standardizes how AI agents connect to user-facing applications. Agents stream tokens, call tools mid-response, update shared state, pause for a human, and spawn subagents. AG-UI replaces custom wiring with one bi-directional event stream, so the same agent can power a web app, a mobile app, a terminal, or Slack.

It helps AI complete tasks: developers wire up different agent frameworks once and reuse the same client logic, while agents push typed events for progress and results and stop when a human decision is needed.

### Features

- A run starts with RunAgentInput; the agent streams back typed events in eight families (lifecycle, text messages, tool calls, state, reasoning, activity, subagents, passthrough), 31 event types in 1.0. Only the run lifecycle family is required.
- Building blocks: streaming chat, generative UI, shared state with snapshots and JSON Patch deltas, frontend tools, human in the loop (interrupt, then approve, edit or reject and resume), reasoning, subagents, and multimodal input.
- Transport-agnostic: the spec defines HTTP + SSE and a binary HTTP + Protobuf binding, with middleware adapting events from other sources.
- AG-UI 1.0 ships a frozen spec and JSON Schema; TypeScript, Python, and .NET SDKs are generated from it and stay backwards compatible with 0.x. It complements MCP (tools/context) and A2A (agent-to-agent).

### Requirements

- Direct protocol: Python 3.9+; `pip install ag-ui-protocol fastapi uvicorn` runs an agent server.
- Client example: Node.js 20+; `npm install @ag-ui/client tsx`.
- Scaffolding: `npx create-ag-ui-app@latest` generates a frontend (CopilotKit on Next.js or a terminal client) wired to your chosen framework; templates call OpenAI and need `OPENAI_API_KEY`.

### Limitations

- AG-UI is a runtime protocol, not a generative UI spec; A2UI, MCP Apps, and Open-JSON-UI describe the UI payloads that AG-UI carries.
- Documented integrations include LangChain, CrewAI, Microsoft Agent Framework, Google ADK, AWS Strands, Mastra, Pydantic AI, LlamaIndex, Agno, AG2, and Claude Agent SDK; other frameworks need a custom integration.
- A minimal agent emits only a few lifecycle events; full capabilities must be added per spec.

### Getting started

1. Run `npx create-ag-ui-app@latest`, pick a frontend and agent framework, set `OPENAI_API_KEY`, then `npm run dev`.
2. Or speak the protocol directly: implement a Python `RunAgentInput` endpoint streaming events (`uvicorn server:app --port 8000`) and connect with the TypeScript `HttpAgent` client.
3. Use the [Spec](https://docs.ag-ui.com/spec/1.0) and [Dojo](https://dojo.ag-ui.com) to add generative UI, shared state, and human-in-the-loop flows.

### Review and sources

The documented AI task use was reviewed: the project standardizes agent-to-app event interaction for building and driving AI agents. The Star snapshot at 2026-11-24T16:00:56.070203Z meets the 1,000 total-Star threshold; eligibility=true. Recent activity: [2026-11-24 · commit](https://github.com/ag-ui-protocol/ag-ui/commit/ed94ca4a3240527d3ef20fd0f0cc63501f44e469). This is a documentation review; the upstream software was not installed or run.

- [Official README](https://github.com/ag-ui-protocol/ag-ui/blob/main/README.md)
- [Spec 1.0](https://docs.ag-ui.com/spec/1.0)
- [Dojo examples](https://dojo.ag-ui.com)

## Review evidence

本次依据公开文章和 GitHub 官方文档复核，未安装或运行上游项目。

Reviewed against public articles and official GitHub documentation; upstream software was not installed or run.

- [GitHub activity](https://github.com/ag-ui-protocol/ag-ui/commit/ed94ca4a3240527d3ef20fd0f0cc63501f44e469) (2026-11-24T05:54:43Z)
- [Discovery article](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA==&mid=2247538734&idx=1&sn=663aff51de396b45a5d7825f27439e6c&chksm=f9a28be7ced502f1d2d79aee06cdc63c341d4aef6baba8f94daeef6405661ea49ce76ea67c3c)

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-24T16:00:56.070203Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "ag-ui",
    "name": "AG-UI",
    "repository": "ag-ui-protocol/ag-ui",
    "repo_node_id": "R_kgDOOmBWgw",
    "category": "ai",
    "summary": {
      "zh-CN": "标准化 AI 智能体与用户界面的事件交互协议，帮助构建与驱动智能体应用。",
      "en": "An event-based protocol that standardizes how AI agents connect to user-facing applications."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-24T16:00:56.070203Z",
        "en": "2026-11-24T16:00:56.070203Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "标准化 AI 智能体与用户界面的事件交互协议，帮助构建与驱动智能体应用。",
        "en": "An event-based protocol that standardizes how AI agents connect to user-facing applications."
      },
      "source_url": "https://github.com/ag-ui-protocol/ag-ui/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/ag-ui-protocol/ag-ui/commit/ed94ca4a3240527d3ef20fd0f0cc63501f44e469",
        "occurred_at": "2026-11-24T05:54:43Z",
        "reviewed_at": "2026-11-24T16:00:56.070203Z",
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
        "url": "https://github.com/ag-ui-protocol/ag-ui/blob/main/README.md"
      },
      {
        "title": "Discovery article",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA==&mid=2247538734&idx=1&sn=663aff51de396b45a5d7825f27439e6c&chksm=f9a28be7ced502f1d2d79aee06cdc63c341d4aef6baba8f94daeef6405661ea49ce76ea67c3c"
      }
    ]
  },
  "snapshot": {
    "full_name": "ag-ui-protocol/ag-ui",
    "repo_node_id": "R_kgDOOmBWgw",
    "stargazers_count": 21514,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-24T16:00:56.070203Z",
    "source_url": "https://api.github.com/repos/ag-ui-protocol/ag-ui"
  }
}
```

</details>
