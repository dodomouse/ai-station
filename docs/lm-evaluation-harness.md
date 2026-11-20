# LM Evaluation Harness

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 14492 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:53.149572Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:38.787Z |

## 中文

通过可配置任务、指标和模型后端运行语言模型基准评测。

在明确任务上比较模型，为 AI 应用选型提供依据。

### 主要功能

- 用统一任务配置运行语言模型评测。
- 连接本地模型和 API 模型后端。
- 通过插件扩展模型、过滤器和指标。

### 环境要求

- 需要 Python 环境和目标评测数据。
- 基础安装不包含模型后端；需另装 Hugging Face、vLLM 或所选后端依赖。

### 使用限制

- 本地模型的显存和运行资源由模型与后端决定。
- README 将部分多模态任务标为原型功能。基准分数不代表所有实际任务表现。

### 开始使用

1. 按[安装说明](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/README.md#install)安装框架和后端。
2. 按[CLI 参考](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/docs/interface.md)选择模型和任务。
3. 运行小规模评测并保存配置和结果。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:38.787Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-09-14 · commit](https://github.com/EleutherAI/lm-evaluation-harness/commit/d6de81643928d653435c431bae19945d41d32520)。fix(basqueglue): load the f1 metric with evaluate (#4076)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/EleutherAI/lm-evaluation-harness)
- [安装说明 / installation instructions](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/README.md#install)
- [CLI 参考 / CLI reference](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/docs/interface.md)

## English

Runs language-model benchmarks through configurable tasks, metrics and model backends.

Helps compare models on defined tasks before using them in AI applications.

### Features

- Run language-model evaluations with common task configurations.
- Connect local-model and API-model backends.
- Extend models, filters and metrics through plugins.

### Requirements

- Requires Python and the target evaluation data.
- The base installation excludes model backends; install Hugging Face, vLLM or the selected backend's dependencies separately.

### Limitations

- Local-model memory and runtime resources depend on the model and backend.
- The README marks some multimodal tasks as prototypes. Benchmark scores do not represent all real-world tasks.

### Getting started

1. Install the framework and a backend using the [installation instructions](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/README.md#install).
2. Select a model and task using the [CLI reference](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/docs/interface.md).
3. Run a small evaluation and save its configuration and results.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:38.787Z meets the total-Star threshold of 1,000.

Recent activity: [2026-09-14 · commit](https://github.com/EleutherAI/lm-evaluation-harness/commit/d6de81643928d653435c431bae19945d41d32520).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/EleutherAI/lm-evaluation-harness)
- [安装说明 / installation instructions](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/README.md#install)
- [CLI 参考 / CLI reference](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/docs/interface.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:53.149572Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "lm-evaluation-harness",
    "name": "LM Evaluation Harness",
    "repository": "EleutherAI/lm-evaluation-harness",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkyOTA5MDkxOTI=",
    "category": "development",
    "summary": {
      "zh-CN": "通过可配置任务、指标和模型后端运行语言模型基准评测。",
      "en": "Runs language-model benchmarks through configurable tasks, metrics and model backends."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:53.149572Z",
        "en": "2026-11-17T14:24:53.149572Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "在明确任务上比较模型，为 AI 应用选型提供依据。",
        "en": "Helps compare models on defined tasks before using them in AI applications."
      },
      "source_url": "https://github.com/EleutherAI/lm-evaluation-harness/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/EleutherAI/lm-evaluation-harness/commit/d6de81643928d653435c431bae19945d41d32520",
        "occurred_at": "2026-09-14T10:51:05Z",
        "reviewed_at": "2026-11-17T14:24:53.149572Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "fix(basqueglue): load the f1 metric with evaluate (#4076) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/EleutherAI/lm-evaluation-harness/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / GitHub metadata",
        "url": "https://api.github.com/repos/EleutherAI/lm-evaluation-harness"
      },
      {
        "title": "安装说明 / installation instructions",
        "url": "https://github.com/EleutherAI/lm-evaluation-harness/blob/main/README.md#install"
      },
      {
        "title": "CLI 参考 / CLI reference",
        "url": "https://github.com/EleutherAI/lm-evaluation-harness/blob/main/docs/interface.md"
      }
    ]
  },
  "snapshot": {
    "full_name": "EleutherAI/lm-evaluation-harness",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkyOTA5MDkxOTI=",
    "stargazers_count": 14492,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:38.787Z",
    "source_url": "https://api.github.com/repos/EleutherAI/lm-evaluation-harness"
  }
}
```

</details>
