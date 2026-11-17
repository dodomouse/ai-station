# Pipecat

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[pipecat-ai/pipecat](https://github.com/pipecat-ai/pipecat)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 17304 |
| 评估时间 / Evaluated at | 2026-11-17T14:28:37.557981Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:26.139Z |

## 中文

用 Python 编排实时语音与多模态智能体的处理流水线。

把音频输入、语音识别、模型和语音输出连成可交互流程，用于网页或电话智能体。

### 主要功能

- 组合多家语音识别、模型和语音合成服务。
- 支持实时传输，并提供网页、移动端和电话应用示例。
- 提供项目脚手架、结构化对话及调试配套工具。

### 环境要求

- 支持 Python 3.11 至 3.14；README 当前不支持 Python 3.15。
- CLI 入门使用 uv；第三方服务需安装对应 extras 并配置连接。

### 使用限制

- 核心安装不包含所有供应商集成。
- 客户端、电话接入和云端部署需要按具体应用配置。

### 开始使用

1. 准备受支持的 Python 和 uv，运行 `uv tool install "pipecat-ai[cli]"`。
2. 运行 `pipecat init`，选择网页或电话项目并配置所需服务。
3. 按[官方快速入门](https://docs.pipecat.ai/getting-started/quickstart)启动示例，测试一轮语音对话。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:26.139Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-16 · commit](https://github.com/pipecat-ai/pipecat/commit/6203e080683aaaaf49d4f801d75eb22526ee0a68)。合并评估指标相关 PR。

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://raw.githubusercontent.com/pipecat-ai/pipecat/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/pipecat-ai/pipecat)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

A Python framework for composing processing pipelines for real-time voice and multimodal agents.

It connects audio input, speech recognition, models, and speech output into interactive web or telephone agents.

### Features

- Combine speech recognition, model, and speech synthesis services from multiple providers.
- Support real-time transport with examples for web, mobile, and telephone applications.
- Provide project scaffolding, structured conversations, and companion debugging tools.

### Requirements

- Supports Python 3.11 through 3.14; the README currently excludes Python 3.15.
- The CLI quickstart uses uv; third-party services require their extras and connection configuration.

### Limitations

- The core installation does not include every provider integration.
- Clients, telephony connections, and cloud deployment need application-specific configuration.

### Getting started

1. Prepare a supported Python version and uv, then run `uv tool install "pipecat-ai[cli]"`.
2. Run `pipecat init`, choose a web or telephone project, and configure its services.
3. Launch the example using the [official quickstart](https://docs.pipecat.ai/getting-started/quickstart) and test a voice conversation.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:26.139Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-16 · commit](https://github.com/pipecat-ai/pipecat/commit/6203e080683aaaaf49d4f801d75eb22526ee0a68).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://raw.githubusercontent.com/pipecat-ai/pipecat/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/pipecat-ai/pipecat)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:28:37.557981Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "pipecat",
    "name": "Pipecat",
    "repository": "pipecat-ai/pipecat",
    "repo_node_id": "R_kgDOK-Kftw",
    "category": "development",
    "summary": {
      "zh-CN": "用 Python 编排实时语音与多模态智能体的处理流水线。",
      "en": "A Python framework for composing processing pipelines for real-time voice and multimodal agents."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:28:37.557981Z",
        "en": "2026-11-17T14:28:37.557981Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "把音频输入、语音识别、模型和语音输出连成可交互流程，用于网页或电话智能体。",
        "en": "It connects audio input, speech recognition, models, and speech output into interactive web or telephone agents."
      },
      "source_url": "https://raw.githubusercontent.com/pipecat-ai/pipecat/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/pipecat-ai/pipecat/commit/6203e080683aaaaf49d4f801d75eb22526ee0a68",
        "occurred_at": "2026-11-16T23:57:54Z",
        "reviewed_at": "2026-11-17T14:28:37.557981Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "合并评估指标相关 PR。 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://raw.githubusercontent.com/pipecat-ai/pipecat/main/README.md"
      },
      {
        "title": "GitHub 仓库元数据 / Repository metadata",
        "url": "https://api.github.com/repos/pipecat-ai/pipecat"
      }
    ]
  },
  "snapshot": {
    "full_name": "pipecat-ai/pipecat",
    "repo_node_id": "R_kgDOK-Kftw",
    "stargazers_count": 17304,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:26.139Z",
    "source_url": "https://api.github.com/repos/pipecat-ai/pipecat"
  }
}
```

</details>
