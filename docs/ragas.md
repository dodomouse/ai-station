# Ragas

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[vibrantlabsai/ragas](https://github.com/vibrantlabsai/ragas)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 16354 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:53.150122Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:39.047Z |

## 中文

用模型评分和传统指标评测大语言模型应用，并生成测试数据。

构建任务测试集，为检索和智能体流程提供改进依据。

### 主要功能

- 使用模型评分与传统指标评测应用。
- 生成面向任务的测试数据集。
- 连接模型框架和可观测工具。

### 环境要求

- 需要 Python 环境及评测所用模型的配置。
- 官方快速入门示例需要 OpenAI 访问凭据。

### 使用限制

- 模型生成的测试数据和评分需要结合人工抽查。
- 工具包含遥测；可按 README 设置 RAGAS_DO_NOT_TRACK 退出。

### 开始使用

1. 按[快速入门](https://docs.ragas.io/en/latest/getstarted/quickstart)安装工具。
2. 配置模型并选择一个完整示例项目。
3. 替换为任务数据，核对评分与具体样本。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:39.047Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-14 · commit](https://github.com/vibrantlabsai/ragas/commit/8c63f10d500c44efbf24fdb9e2920de2104c321c)。fix: point deprecation warnings to correct collections metric names (#2974)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/vibrantlabsai/ragas/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/vibrantlabsai/ragas)
- [快速入门 / quickstart](https://docs.ragas.io/en/latest/getstarted/quickstart)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

Evaluates LLM applications and generates test data using model-based and traditional metrics.

Creates task-specific evaluation sets and feedback for improving retrieval and agent workflows.

### Features

- Evaluate applications with model-based and traditional metrics.
- Generate task-oriented test datasets.
- Integrate with model frameworks and observability tools.

### Requirements

- Requires Python and configuration for the evaluation model.
- The official quickstart example requires OpenAI credentials.

### Limitations

- Model-generated test data and scores need human spot checks.
- The tool includes telemetry; the README documents opting out with RAGAS_DO_NOT_TRACK.

### Getting started

1. Install the tool using the [quickstart](https://docs.ragas.io/en/latest/getstarted/quickstart).
2. Configure a model and choose a complete example project.
3. Replace the data with task examples and inspect scores alongside individual cases.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:39.047Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-14 · commit](https://github.com/vibrantlabsai/ragas/commit/8c63f10d500c44efbf24fdb9e2920de2104c321c).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/vibrantlabsai/ragas/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/vibrantlabsai/ragas)
- [快速入门 / quickstart](https://docs.ragas.io/en/latest/getstarted/quickstart)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:53.150122Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "ragas",
    "name": "Ragas",
    "repository": "vibrantlabsai/ragas",
    "repo_node_id": "R_kgDOJgX1Gg",
    "category": "development",
    "summary": {
      "zh-CN": "用模型评分和传统指标评测大语言模型应用，并生成测试数据。",
      "en": "Evaluates LLM applications and generates test data using model-based and traditional metrics."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:53.150122Z",
        "en": "2026-11-17T14:24:53.150122Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "构建任务测试集，为检索和智能体流程提供改进依据。",
        "en": "Creates task-specific evaluation sets and feedback for improving retrieval and agent workflows."
      },
      "source_url": "https://github.com/vibrantlabsai/ragas/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/vibrantlabsai/ragas/commit/8c63f10d500c44efbf24fdb9e2920de2104c321c",
        "occurred_at": "2026-11-14T02:30:59Z",
        "reviewed_at": "2026-11-17T14:24:53.150122Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "fix: point deprecation warnings to correct collections metric names (#2974) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/vibrantlabsai/ragas/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / GitHub metadata",
        "url": "https://api.github.com/repos/vibrantlabsai/ragas"
      },
      {
        "title": "快速入门 / quickstart",
        "url": "https://docs.ragas.io/en/latest/getstarted/quickstart"
      }
    ]
  },
  "snapshot": {
    "full_name": "vibrantlabsai/ragas",
    "repo_node_id": "R_kgDOJgX1Gg",
    "stargazers_count": 16354,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:39.047Z",
    "source_url": "https://api.github.com/repos/vibrantlabsai/ragas"
  }
}
```

</details>
