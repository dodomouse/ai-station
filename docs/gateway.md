# Portkey AI Gateway

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[Portkey-AI/gateway](https://github.com/Portkey-AI/gateway)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 部署与运维 / Operations |
| 状态 / Status | 已收录 / Included |
| Star | 13390 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:53.149300Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:39.304Z |

## 中文

为多家模型提供统一调用接口、条件路由、重试、回退和护栏。

让 AI 工作流在模型供应商之间切换，并在调用失败时重试或选择后备模型。

### 主要功能

- 统一转发多家模型供应商的请求。
- 配置负载均衡、条件路由和回退。
- 在调用路径中加入护栏。

### 环境要求

- 按部署方式准备 Node.js、Docker 或 Cloudflare 环境。
- 需要模型供应商的访问凭据和网关配置。

### 使用限制

- README 将 Gateway 2.0 标为预发布，不能把该分支能力当作稳定版本保证。
- 供应商的模型参数、配额和收费仍然适用。

### 开始使用

1. 按[部署说明](https://github.com/Portkey-AI/gateway/blob/main/docs/installation-deployments.md)启动网关。
2. 按[README 快速入门](https://github.com/Portkey-AI/gateway/blob/main/README.md#quickstart-2-mins)连接供应商。
3. 发送测试请求并检查路由和回退结果。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:39.304Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-16 · pr](https://github.com/Portkey-AI/gateway/pull/1903)。新建 PR：improvement: count tokens for newer Claude models on Bedrock via bedrock-mantle

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/Portkey-AI/gateway/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/Portkey-AI/gateway)
- [部署说明 / deployment instructions](https://github.com/Portkey-AI/gateway/blob/main/docs/installation-deployments.md)
- [README 快速入门 / README quickstart](https://github.com/Portkey-AI/gateway/blob/main/README.md#quickstart-2-mins)

## English

Provides a unified model API with conditional routing, retries, fallbacks and guardrails.

Lets AI workflows switch model providers and retry or fall back when calls fail.

### Features

- Route requests to multiple model providers through a common API.
- Configure load balancing, conditional routing and fallbacks.
- Add guardrails to the request path.

### Requirements

- Prepare Node.js, Docker or Cloudflare infrastructure for the chosen deployment.
- Requires model-provider credentials and gateway configuration.

### Limitations

- The README marks Gateway 2.0 as a prerelease; its capabilities are not a stable-release guarantee.
- Provider-specific parameters, quotas and charges still apply.

### Getting started

1. Start the gateway using the [deployment instructions](https://github.com/Portkey-AI/gateway/blob/main/docs/installation-deployments.md).
2. Connect a provider using the [README quickstart](https://github.com/Portkey-AI/gateway/blob/main/README.md#quickstart-2-mins).
3. Send test requests and inspect routing and fallback results.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:39.304Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-16 · pr](https://github.com/Portkey-AI/gateway/pull/1903).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/Portkey-AI/gateway/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/Portkey-AI/gateway)
- [部署说明 / deployment instructions](https://github.com/Portkey-AI/gateway/blob/main/docs/installation-deployments.md)
- [README 快速入门 / README quickstart](https://github.com/Portkey-AI/gateway/blob/main/README.md#quickstart-2-mins)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:53.149300Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "gateway",
    "name": "Portkey AI Gateway",
    "repository": "Portkey-AI/gateway",
    "repo_node_id": "R_kgDOKKe4LA",
    "category": "operations",
    "summary": {
      "zh-CN": "为多家模型提供统一调用接口、条件路由、重试、回退和护栏。",
      "en": "Provides a unified model API with conditional routing, retries, fallbacks and guardrails."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:53.149300Z",
        "en": "2026-11-17T14:24:53.149300Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "让 AI 工作流在模型供应商之间切换，并在调用失败时重试或选择后备模型。",
        "en": "Lets AI workflows switch model providers and retry or fall back when calls fail."
      },
      "source_url": "https://github.com/Portkey-AI/gateway/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "pr",
        "url": "https://github.com/Portkey-AI/gateway/pull/1903",
        "occurred_at": "2026-11-16T06:11:14Z",
        "reviewed_at": "2026-11-17T14:24:53.149300Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "新建 PR：improvement: count tokens for newer Claude models on Bedrock via bedrock-mantle 此记录用于证明窗口内活动。",
          "en": "The recorded pr establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/Portkey-AI/gateway/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / GitHub metadata",
        "url": "https://api.github.com/repos/Portkey-AI/gateway"
      },
      {
        "title": "部署说明 / deployment instructions",
        "url": "https://github.com/Portkey-AI/gateway/blob/main/docs/installation-deployments.md"
      },
      {
        "title": "README 快速入门 / README quickstart",
        "url": "https://github.com/Portkey-AI/gateway/blob/main/README.md#quickstart-2-mins"
      }
    ]
  },
  "snapshot": {
    "full_name": "Portkey-AI/gateway",
    "repo_node_id": "R_kgDOKKe4LA",
    "stargazers_count": 13390,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:39.304Z",
    "source_url": "https://api.github.com/repos/Portkey-AI/gateway"
  }
}
```

</details>
