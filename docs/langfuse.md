# Langfuse

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[langfuse/langfuse](https://github.com/langfuse/langfuse)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 部署与运维 / Operations |
| 状态 / Status | 已收录 / Included |
| Star | 37546 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:53.149757Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:39.655Z |

## 中文

汇集模型调用、智能体轨迹、提示版本和评测结果的 AI 工程平台。

为 AI 应用记录工具调用与检索过程，帮助定位失败步骤、比较提示版本和监测成本。

### 主要功能

- 通过 OpenTelemetry 记录模型与工具轨迹。
- 管理提示和技能版本。
- 用数据集、实验和评分器评测任务。

### 环境要求

- 自托管支持 Docker Compose 或 Kubernetes Helm。
- 应用需配置 SDK 或 OpenTelemetry 轨迹导出。

### 使用限制

- README 将技能管理和 AI Gateway 标为 beta。
- 平台只分析已接入的调用和反馈。评分结果依赖数据与评分器。

### 开始使用

1. 按[Docker Compose 指南](https://langfuse.com/self-hosting/deployment/docker-compose)启动服务。
2. 按[可观测指南](https://langfuse.com/docs/observability/overview)接入应用。
3. 按[评测指南](https://langfuse.com/docs/evaluation/overview)建立一组任务样本。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:39.655Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/langfuse/langfuse/commit/364223f2fba19695491d5ae54b5ab6f2e911b7a1)。perf(ci): pilot larger worker test runners (#20265)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/langfuse/langfuse/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/langfuse/langfuse)
- [Docker Compose 指南 / Docker Compose guide](https://langfuse.com/self-hosting/deployment/docker-compose)
- [可观测指南 / observability guide](https://langfuse.com/docs/observability/overview)
- [评测指南 / evaluation guide](https://langfuse.com/docs/evaluation/overview)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

Collects model calls, agent traces, prompt versions and evaluation results in an AI engineering platform.

Records tool use and retrieval so teams can diagnose failed steps, compare prompts and monitor cost.

### Features

- Record model and tool traces through OpenTelemetry.
- Manage prompt and skill versions.
- Evaluate tasks using datasets, experiments and scorers.

### Requirements

- Self-hosting supports Docker Compose or Kubernetes Helm.
- Applications must configure an SDK or OpenTelemetry trace export.

### Limitations

- The README marks skill management and AI Gateway as beta.
- The platform analyzes integrated calls and feedback. Evaluation results depend on data and scorers.

### Getting started

1. Start the service using the [Docker Compose guide](https://langfuse.com/self-hosting/deployment/docker-compose).
2. Instrument the application using the [observability guide](https://langfuse.com/docs/observability/overview).
3. Create task examples using the [evaluation guide](https://langfuse.com/docs/evaluation/overview).

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:39.655Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/langfuse/langfuse/commit/364223f2fba19695491d5ae54b5ab6f2e911b7a1).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/langfuse/langfuse/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/langfuse/langfuse)
- [Docker Compose 指南 / Docker Compose guide](https://langfuse.com/self-hosting/deployment/docker-compose)
- [可观测指南 / observability guide](https://langfuse.com/docs/observability/overview)
- [评测指南 / evaluation guide](https://langfuse.com/docs/evaluation/overview)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:53.149757Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "langfuse",
    "name": "Langfuse",
    "repository": "langfuse/langfuse",
    "repo_node_id": "R_kgDOJku7Qg",
    "category": "operations",
    "summary": {
      "zh-CN": "汇集模型调用、智能体轨迹、提示版本和评测结果的 AI 工程平台。",
      "en": "Collects model calls, agent traces, prompt versions and evaluation results in an AI engineering platform."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:53.149757Z",
        "en": "2026-11-17T14:24:53.149757Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "为 AI 应用记录工具调用与检索过程，帮助定位失败步骤、比较提示版本和监测成本。",
        "en": "Records tool use and retrieval so teams can diagnose failed steps, compare prompts and monitor cost."
      },
      "source_url": "https://github.com/langfuse/langfuse/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/langfuse/langfuse/commit/364223f2fba19695491d5ae54b5ab6f2e911b7a1",
        "occurred_at": "2026-11-17T13:14:33Z",
        "reviewed_at": "2026-11-17T14:24:53.149757Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "perf(ci): pilot larger worker test runners (#20265) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/langfuse/langfuse/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / GitHub metadata",
        "url": "https://api.github.com/repos/langfuse/langfuse"
      },
      {
        "title": "Docker Compose 指南 / Docker Compose guide",
        "url": "https://langfuse.com/self-hosting/deployment/docker-compose"
      },
      {
        "title": "可观测指南 / observability guide",
        "url": "https://langfuse.com/docs/observability/overview"
      },
      {
        "title": "评测指南 / evaluation guide",
        "url": "https://langfuse.com/docs/evaluation/overview"
      }
    ]
  },
  "snapshot": {
    "full_name": "langfuse/langfuse",
    "repo_node_id": "R_kgDOJku7Qg",
    "stargazers_count": 37546,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:39.655Z",
    "source_url": "https://api.github.com/repos/langfuse/langfuse"
  }
}
```

</details>
