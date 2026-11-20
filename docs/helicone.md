# Helicone

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[Helicone/helicone](https://github.com/Helicone/helicone)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 部署与运维 / Operations |
| 状态 / Status | 已收录 / Included |
| Star | 6286 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:53.149666Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:39.406Z |

## 中文

结合模型网关、请求日志、会话分析和提示版本管理的 LLM 平台。

为智能体选择模型、处理路由回退，并追踪任务中的成本、延迟和请求结果。

### 主要功能

- 通过网关路由模型请求并自动回退。
- 查看智能体会话及调用轨迹。
- 比较提示版本、延迟和费用。

### 环境要求

- 托管网关需要账户与可用额度。
- 自托管可观测平台可使用 Docker Compose。

### 使用限制

- 托管网关和自托管可观测部署的使用方式不同。
- 日志只覆盖接入 Helicone 的调用。企业 Helm 方案需联系项目方。

### 开始使用

1. 按[网关指南](https://docs.helicone.ai/gateway/overview)或[自托管指南](https://docs.helicone.ai/getting-started/self-deploy-docker)选择方式。
2. 按官方示例配置客户端地址与认证。
3. 发送测试调用并检查会话、延迟和费用记录。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:39.406Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/Helicone/helicone/commit/5a21c3a1be183c684b49136eb5abc5e95ed6ba26)。fix(bifrost): restore Contact Us booking embed (#5874)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/Helicone/helicone/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/Helicone/helicone)
- [网关指南 / gateway guide](https://docs.helicone.ai/gateway/overview)
- [自托管指南 / self-hosting guide](https://docs.helicone.ai/getting-started/self-deploy-docker)

## English

Combines an AI gateway, request logs, session analysis and prompt versioning.

Routes model calls, handles fallbacks and tracks the cost, latency and outcomes of agent tasks.

### Features

- Route model requests through a gateway with automatic fallbacks.
- Inspect agent sessions and request traces.
- Compare prompt versions, latency and cost.

### Requirements

- The hosted gateway requires an account and available credit.
- The self-hosted observability platform can use Docker Compose.

### Limitations

- Hosted-gateway and self-hosted observability deployments work differently.
- Logs cover calls integrated with Helicone. The enterprise Helm offering requires contacting the project team.

### Getting started

1. Choose a route using the [gateway guide](https://docs.helicone.ai/gateway/overview) or [self-hosting guide](https://docs.helicone.ai/getting-started/self-deploy-docker).
2. Configure the client endpoint and authentication using the official example.
3. Send a test call and inspect session, latency and cost records.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:39.406Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/Helicone/helicone/commit/5a21c3a1be183c684b49136eb5abc5e95ed6ba26).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/Helicone/helicone/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/Helicone/helicone)
- [网关指南 / gateway guide](https://docs.helicone.ai/gateway/overview)
- [自托管指南 / self-hosting guide](https://docs.helicone.ai/getting-started/self-deploy-docker)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:53.149666Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "helicone",
    "name": "Helicone",
    "repository": "Helicone/helicone",
    "repo_node_id": "R_kgDOI4Othg",
    "category": "operations",
    "summary": {
      "zh-CN": "结合模型网关、请求日志、会话分析和提示版本管理的 LLM 平台。",
      "en": "Combines an AI gateway, request logs, session analysis and prompt versioning."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:53.149666Z",
        "en": "2026-11-17T14:24:53.149666Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "为智能体选择模型、处理路由回退，并追踪任务中的成本、延迟和请求结果。",
        "en": "Routes model calls, handles fallbacks and tracks the cost, latency and outcomes of agent tasks."
      },
      "source_url": "https://github.com/Helicone/helicone/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/Helicone/helicone/commit/5a21c3a1be183c684b49136eb5abc5e95ed6ba26",
        "occurred_at": "2026-11-17T00:37:41Z",
        "reviewed_at": "2026-11-17T14:24:53.149666Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "fix(bifrost): restore Contact Us booking embed (#5874) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/Helicone/helicone/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / GitHub metadata",
        "url": "https://api.github.com/repos/Helicone/helicone"
      },
      {
        "title": "网关指南 / gateway guide",
        "url": "https://docs.helicone.ai/gateway/overview"
      },
      {
        "title": "自托管指南 / self-hosting guide",
        "url": "https://docs.helicone.ai/getting-started/self-deploy-docker"
      }
    ]
  },
  "snapshot": {
    "full_name": "Helicone/helicone",
    "repo_node_id": "R_kgDOI4Othg",
    "stargazers_count": 6286,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:39.406Z",
    "source_url": "https://api.github.com/repos/Helicone/helicone"
  }
}
```

</details>
