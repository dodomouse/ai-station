# OpenCompass

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[open-compass/opencompass](https://github.com/open-compass/opencompass)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 7599 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:53.149948Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:39.184Z |

## 中文

通过统一流程配置模型推理、基准评测和结果汇总。

比较模型在不同任务上的能力，为 AI 模型选型提供可复查记录。

### 主要功能

- 统一配置模型、数据集、推理和评分。
- 连接本地模型和外部 API。
- 扩展评测器并分配并行任务。

### 环境要求

- 常规与完整安装支持 Python 3.12，官方推荐 conda。
- 依赖 pyext 的代码执行数据集需要 Python 3.10。
- 按所选模型安装推理后端并准备数据集。

### 使用限制

- Python >=3.11 跳过 pyext==0.7，相关代码评测能力会受影响。
- 不同推理后端可能有依赖冲突，应按官方说明隔离环境。

### 开始使用

1. 按[安装指南](https://opencompass.readthedocs.io/en/latest/get_started/installation.html)创建环境。
2. 按[快速入门](https://opencompass.readthedocs.io/en/latest/get_started/quick_start.html)选择模型和数据集。
3. 运行评测并核对配置、评分和汇总结果。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:39.184Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-11 · commit](https://github.com/open-compass/opencompass/commit/8b4193ff01cfbdb870a573330b2b199e20242bba)。[Fix] Restore missing comma in mathbench first_option_postprocess answer patterns (#2705)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/open-compass/opencompass/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/open-compass/opencompass)
- [安装指南 / installation guide](https://opencompass.readthedocs.io/en/latest/get_started/installation.html)
- [快速入门 / quickstart](https://opencompass.readthedocs.io/en/latest/get_started/quick_start.html)

## English

Configures model inference, benchmark evaluation and result summaries in a common workflow.

Compares models across task capabilities and supports repeatable AI model selection.

### Features

- Configure models, datasets, inference and scoring in one workflow.
- Connect local models and external APIs.
- Extend evaluators and distribute parallel tasks.

### Requirements

- Regular and full installations support Python 3.12; conda is recommended.
- Code-execution datasets that depend on pyext require Python 3.10.
- Install the selected model backend and prepare its datasets.

### Limitations

- Python >=3.11 skips pyext==0.7, affecting the related code-evaluation capabilities.
- Inference backends may have conflicting dependencies; isolate environments as documented.

### Getting started

1. Create an environment using the [installation guide](https://opencompass.readthedocs.io/en/latest/get_started/installation.html).
2. Choose a model and dataset using the [quickstart](https://opencompass.readthedocs.io/en/latest/get_started/quick_start.html).
3. Run evaluation and check configuration, scores and summary results.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:39.184Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-11 · commit](https://github.com/open-compass/opencompass/commit/8b4193ff01cfbdb870a573330b2b199e20242bba).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/open-compass/opencompass/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/open-compass/opencompass)
- [安装指南 / installation guide](https://opencompass.readthedocs.io/en/latest/get_started/installation.html)
- [快速入门 / quickstart](https://opencompass.readthedocs.io/en/latest/get_started/quick_start.html)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:53.149948Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "opencompass",
    "name": "OpenCompass",
    "repository": "open-compass/opencompass",
    "repo_node_id": "R_kgDOJv0mSQ",
    "category": "development",
    "summary": {
      "zh-CN": "通过统一流程配置模型推理、基准评测和结果汇总。",
      "en": "Configures model inference, benchmark evaluation and result summaries in a common workflow."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:53.149948Z",
        "en": "2026-11-17T14:24:53.149948Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "比较模型在不同任务上的能力，为 AI 模型选型提供可复查记录。",
        "en": "Compares models across task capabilities and supports repeatable AI model selection."
      },
      "source_url": "https://github.com/open-compass/opencompass/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/open-compass/opencompass/commit/8b4193ff01cfbdb870a573330b2b199e20242bba",
        "occurred_at": "2026-11-11T11:08:57Z",
        "reviewed_at": "2026-11-17T14:24:53.149948Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "[Fix] Restore missing comma in mathbench first_option_postprocess answer patterns (#2705) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/open-compass/opencompass/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / GitHub metadata",
        "url": "https://api.github.com/repos/open-compass/opencompass"
      },
      {
        "title": "安装指南 / installation guide",
        "url": "https://opencompass.readthedocs.io/en/latest/get_started/installation.html"
      },
      {
        "title": "快速入门 / quickstart",
        "url": "https://opencompass.readthedocs.io/en/latest/get_started/quick_start.html"
      }
    ]
  },
  "snapshot": {
    "full_name": "open-compass/opencompass",
    "repo_node_id": "R_kgDOJv0mSQ",
    "stargazers_count": 7599,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:39.184Z",
    "source_url": "https://api.github.com/repos/open-compass/opencompass"
  }
}
```

</details>
