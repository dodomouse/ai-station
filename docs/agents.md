# LiveKit Agents

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[livekit/agents](https://github.com/livekit/agents)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 15259 |
| 评估时间 / Evaluated at | 2026-11-17T14:28:37.557732Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:26.738Z |

## 中文

LiveKit 的 Python 智能体框架，用于实时语音和多模态会话。

将语音识别、模型推理和语音合成串联起来，让 AI 通过音视频会话与用户交互。

### 主要功能

- 组合 STT、LLM、TTS 或实时模型服务。
- 通过 LiveKit 房间接入客户端和电话集成。
- 支持工具调用、多智能体交接，以及会话行为测试。

### 环境要求

- 需要 Python 环境及所选模型插件。
- 客户端会话需要 LiveKit Cloud 或自建服务器；模型服务也需相应配置。

### 使用限制

- 终端 console 模式可用于本地音频测试，但不能代替客户端与电话链路验证。
- 延迟和响应质量取决于模型、传输与部署环境。

### 开始使用

1. 按 README 运行 `pip install "livekit-agents[openai,deepgram,cartesia]"`。
2. 将官方语音示例保存为 `myagent.py`，配置模型服务后运行 `python myagent.py console`。
3. 配置 LiveKit 连接，运行 `python myagent.py dev`，再用客户端或 Playground 测试。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:26.738Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/livekit/agents/commit/0cfc0306335cc8b3633ec2cdce072a3f340cb14e)。调整 AWS 转写流依赖的版本上限。

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://raw.githubusercontent.com/livekit/agents/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/livekit/agents)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

LiveKit's Python agent framework for real-time voice and multimodal conversations.

It connects speech recognition, model reasoning, and speech synthesis so AI can interact with users through audio and video sessions.

### Features

- Compose STT, LLM, TTS, or real-time model services.
- Connect clients and telephony integrations through LiveKit rooms.
- Support tool calls, agent handoffs, and tests of conversational behavior.

### Requirements

- Requires Python and the selected model plugins.
- Client sessions require LiveKit Cloud or a self-hosted server; model services also need configuration.

### Limitations

- Terminal console mode supports local audio testing but does not validate the client or telephony path.
- Latency and response quality depend on models, transport, and deployment.

### Getting started

1. Run `pip install "livekit-agents[openai,deepgram,cartesia]"` following the README.
2. Save the official voice example as `myagent.py`, configure the model services, and run `python myagent.py console`.
3. Configure the LiveKit connection, run `python myagent.py dev`, and test with a client or the Playground.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:26.738Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/livekit/agents/commit/0cfc0306335cc8b3633ec2cdce072a3f340cb14e).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://raw.githubusercontent.com/livekit/agents/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/livekit/agents)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:28:37.557732Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "agents",
    "name": "LiveKit Agents",
    "repository": "livekit/agents",
    "repo_node_id": "R_kgDOKiqzdw",
    "category": "development",
    "summary": {
      "zh-CN": "LiveKit 的 Python 智能体框架，用于实时语音和多模态会话。",
      "en": "LiveKit's Python agent framework for real-time voice and multimodal conversations."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:28:37.557732Z",
        "en": "2026-11-17T14:28:37.557732Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "将语音识别、模型推理和语音合成串联起来，让 AI 通过音视频会话与用户交互。",
        "en": "It connects speech recognition, model reasoning, and speech synthesis so AI can interact with users through audio and video sessions."
      },
      "source_url": "https://raw.githubusercontent.com/livekit/agents/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/livekit/agents/commit/0cfc0306335cc8b3633ec2cdce072a3f340cb14e",
        "occurred_at": "2026-11-17T07:22:33Z",
        "reviewed_at": "2026-11-17T14:28:37.557732Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "调整 AWS 转写流依赖的版本上限。 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://raw.githubusercontent.com/livekit/agents/main/README.md"
      },
      {
        "title": "GitHub 仓库元数据 / Repository metadata",
        "url": "https://api.github.com/repos/livekit/agents"
      }
    ]
  },
  "snapshot": {
    "full_name": "livekit/agents",
    "repo_node_id": "R_kgDOKiqzdw",
    "stargazers_count": 15259,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:26.738Z",
    "source_url": "https://api.github.com/repos/livekit/agents"
  }
}
```

</details>
