# LangWatch

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[langwatch/langwatch](https://github.com/langwatch/langwatch)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 部署与运维 / Operations |
| 状态 / Status | 已收录 / Included |
| Star | 5042 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:53.149856Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:39.739Z |

## 中文

统一查看智能体轨迹、模拟测试、编码助手会话和模型网关用量。

用模拟对话测试 AI 任务流程，定位失败调用，并限制智能体模型调用预算。

### 主要功能

- 记录智能体和编码助手会话。
- 用模拟任务测试智能体。
- 用网关配置路由、虚拟密钥和预算。

### 环境要求

- README 的本地启动要求 Node.js 24 或更新版本。
- 该本地路径支持 macOS 或使用 glibc 的 Linux。

### 使用限制

- 生产部署需按自托管指南配置，不能仅沿用本地启动设置。
- 观测与费用分析依赖接入的数据源和模型调用。

### 开始使用

1. 按[自托管指南](https://langwatch.ai/docs/self-hosting/overview)准备服务。
2. 按[可观测说明](https://langwatch.ai/docs/observability/overview)连接应用。
3. 按[智能体测试指南](https://langwatch.ai/docs/agent-testing/overview)运行模拟任务。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:39.739Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/langwatch/langwatch/commit/396d2727b93e08cd4aec407dbadba2ecbc6afec5)。chore(main): release clickhouse-serverless 0.5.0 (#8203)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/langwatch/langwatch/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/langwatch/langwatch)
- [自托管指南 / self-hosting guide](https://langwatch.ai/docs/self-hosting/overview)
- [可观测说明 / observability guide](https://langwatch.ai/docs/observability/overview)
- [智能体测试指南 / agent-testing guide](https://langwatch.ai/docs/agent-testing/overview)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

Combines agent traces, simulation tests, coding-assistant sessions and model-gateway usage.

Tests AI workflows through simulated interactions, diagnoses failed calls and controls model budgets.

### Features

- Record agent and coding-assistant sessions.
- Test agents through simulated tasks.
- Configure routing, virtual keys and budgets through the gateway.

### Requirements

- The README's local setup requires Node.js 24 or later.
- That local setup supports macOS or glibc-based Linux.

### Limitations

- Production deployments require the self-hosting guide rather than only the local startup settings.
- Observability and cost analysis depend on connected data sources and model calls.

### Getting started

1. Prepare the service using the [self-hosting guide](https://langwatch.ai/docs/self-hosting/overview).
2. Connect the application using the [observability guide](https://langwatch.ai/docs/observability/overview).
3. Run a simulation using the [agent-testing guide](https://langwatch.ai/docs/agent-testing/overview).

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:39.739Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/langwatch/langwatch/commit/396d2727b93e08cd4aec407dbadba2ecbc6afec5).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/langwatch/langwatch/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/langwatch/langwatch)
- [自托管指南 / self-hosting guide](https://langwatch.ai/docs/self-hosting/overview)
- [可观测说明 / observability guide](https://langwatch.ai/docs/observability/overview)
- [智能体测试指南 / agent-testing guide](https://langwatch.ai/docs/agent-testing/overview)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:53.149856Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "langwatch",
    "name": "LangWatch",
    "repository": "langwatch/langwatch",
    "repo_node_id": "R_kgDOKRXhvA",
    "category": "operations",
    "summary": {
      "zh-CN": "统一查看智能体轨迹、模拟测试、编码助手会话和模型网关用量。",
      "en": "Combines agent traces, simulation tests, coding-assistant sessions and model-gateway usage."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:53.149856Z",
        "en": "2026-11-17T14:24:53.149856Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "用模拟对话测试 AI 任务流程，定位失败调用，并限制智能体模型调用预算。",
        "en": "Tests AI workflows through simulated interactions, diagnoses failed calls and controls model budgets."
      },
      "source_url": "https://github.com/langwatch/langwatch/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/langwatch/langwatch/commit/396d2727b93e08cd4aec407dbadba2ecbc6afec5",
        "occurred_at": "2026-11-17T11:00:41Z",
        "reviewed_at": "2026-11-17T14:24:53.149856Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "chore(main): release clickhouse-serverless 0.5.0 (#8203) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/langwatch/langwatch/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / GitHub metadata",
        "url": "https://api.github.com/repos/langwatch/langwatch"
      },
      {
        "title": "自托管指南 / self-hosting guide",
        "url": "https://langwatch.ai/docs/self-hosting/overview"
      },
      {
        "title": "可观测说明 / observability guide",
        "url": "https://langwatch.ai/docs/observability/overview"
      },
      {
        "title": "智能体测试指南 / agent-testing guide",
        "url": "https://langwatch.ai/docs/agent-testing/overview"
      }
    ]
  },
  "snapshot": {
    "full_name": "langwatch/langwatch",
    "repo_node_id": "R_kgDOKRXhvA",
    "stargazers_count": 5042,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:39.739Z",
    "source_url": "https://api.github.com/repos/langwatch/langwatch"
  }
}
```

</details>
