# DSPy

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[stanfordnlp/dspy](https://github.com/stanfordnlp/dspy)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 39107 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:53.148599Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:39.608Z |

## 中文

用模块化程序组织语言模型调用，并优化提示词与模型参数。

构建和优化分类、RAG 与智能体流程。

### 主要功能

- 用 Python 模块描述语言模型任务。
- 优化程序中的提示和模型参数。
- 组合分类、检索与智能体调用流程。

### 环境要求

- 需要 Python 环境及可用的模型接口。
- 优化任务需要定义评价指标和任务样本。

### 使用限制

- 优化效果取决于样本和指标，不能视为所有任务的通用提升。
- 当前模型集成已改用原生 lm15 引擎，旧 LiteLLM 配置需按迁移说明调整。

### 开始使用

1. 按[DSPy 文档](https://dspy.ai/)安装并配置模型。
2. 定义一个模块和可核对的任务指标。
3. 升级旧项目时，阅读[模型接口迁移说明](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/community/normalized-lm-api-migration.md)。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:39.608Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-12 · commit](https://github.com/stanfordnlp/dspy/commit/2c07ebbee3a66f6e04b71e141c6c198f1b31a129)。chore: refresh model metadata provenance to LiteLLM 1.109.1 (#10878)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/stanfordnlp/dspy/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/stanfordnlp/dspy)
- [DSPy 文档 / DSPy docs](https://dspy.ai/)
- [模型接口迁移说明 / model API migration guide](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/community/normalized-lm-api-migration.md)

## English

Organizes model calls as modular programs and optimizes prompts or model parameters.

Builds and optimizes classification, retrieval-augmented generation and agent workflows.

### Features

- Describe language-model tasks with Python modules.
- Optimize prompts and model parameters within programs.
- Compose classification, retrieval and agent-call workflows.

### Requirements

- Requires Python and an available model interface.
- Optimization requires task examples and an evaluation metric.

### Limitations

- Optimization depends on examples and metrics; gains do not apply automatically to every task.
- The current model integration uses native lm15 engines; older LiteLLM configurations need the documented migration.

### Getting started

1. Install and configure a model using the [DSPy docs](https://dspy.ai/).
2. Define a module and a measurable task metric.
3. For an existing project, read the [model API migration guide](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/community/normalized-lm-api-migration.md).

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:39.608Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-12 · commit](https://github.com/stanfordnlp/dspy/commit/2c07ebbee3a66f6e04b71e141c6c198f1b31a129).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/stanfordnlp/dspy/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/stanfordnlp/dspy)
- [DSPy 文档 / DSPy docs](https://dspy.ai/)
- [模型接口迁移说明 / model API migration guide](https://github.com/stanfordnlp/dspy/blob/main/docs/docs/community/normalized-lm-api-migration.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:53.148599Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "dspy",
    "name": "DSPy",
    "repository": "stanfordnlp/dspy",
    "repo_node_id": "R_kgDOIv2ufA",
    "category": "ai",
    "summary": {
      "zh-CN": "用模块化程序组织语言模型调用，并优化提示词与模型参数。",
      "en": "Organizes model calls as modular programs and optimizes prompts or model parameters."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:53.148599Z",
        "en": "2026-11-17T14:24:53.148599Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "构建和优化分类、RAG 与智能体流程。",
        "en": "Builds and optimizes classification, retrieval-augmented generation and agent workflows."
      },
      "source_url": "https://github.com/stanfordnlp/dspy/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/stanfordnlp/dspy/commit/2c07ebbee3a66f6e04b71e141c6c198f1b31a129",
        "occurred_at": "2026-11-12T14:09:40Z",
        "reviewed_at": "2026-11-17T14:24:53.148599Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "chore: refresh model metadata provenance to LiteLLM 1.109.1 (#10878) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/stanfordnlp/dspy/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / GitHub metadata",
        "url": "https://api.github.com/repos/stanfordnlp/dspy"
      },
      {
        "title": "DSPy 文档 / DSPy docs",
        "url": "https://dspy.ai/"
      },
      {
        "title": "模型接口迁移说明 / model API migration guide",
        "url": "https://github.com/stanfordnlp/dspy/blob/main/docs/docs/community/normalized-lm-api-migration.md"
      }
    ]
  },
  "snapshot": {
    "full_name": "stanfordnlp/dspy",
    "repo_node_id": "R_kgDOIv2ufA",
    "stargazers_count": 39107,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:39.608Z",
    "source_url": "https://api.github.com/repos/stanfordnlp/dspy"
  }
}
```

</details>
