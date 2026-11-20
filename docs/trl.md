# TRL

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[huggingface/trl](https://github.com/huggingface/trl)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 19750 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.604509Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:27.735Z |

## 中文

提供监督微调、偏好优化和强化学习训练器的后训练库。

用示例、偏好数据或奖励函数调整语言模型的任务行为。

### 主要功能

- 提供多种训练器，包括 SFT、DPO、GRPO 和 KTO。
- 与 PEFT 和 Accelerate 集成，支持适配器及分布式训练。
- 提供命令行入口及异步 GRPO 采样训练方式。

### 环境要求

- 需要 Python、Transformers 生态依赖、模型权重和对应训练数据。
- 异步 GRPO 示例需 vLLM 与训练器分用 GPU，并安装所需额外依赖。

### 使用限制

- 不同训练器需要不同的数据字段或奖励函数。
- `trl.experimental` 接口不稳定，可能在任意版本变更或移除。

### 开始使用

1. 按[官方文档](https://huggingface.co/docs/trl/index)安装并选择训练方法。
2. 参考对应训练器示例，准备数据或奖励函数。
3. 先运行样本训练并评测，再配置分布式或异步执行。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:27.735Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/huggingface/trl/commit/b2686bf5c300756cdf878b84f83a48f794e2fb94)。Add support for vLLM 0.34.x (#8418)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://github.com/huggingface/trl/blob/main/README.md)
- [Documentation](https://huggingface.co/docs/trl/index)
- [SFT trainer](https://huggingface.co/docs/trl/sft_trainer)
- [Async GRPO](https://huggingface.co/docs/trl/async_grpo_trainer)

## English

A post-training library with trainers for supervised fine-tuning, preference optimization, and reinforcement learning.

Adapts language-model behavior using demonstrations, preference data, or reward functions.

### Features

- Provides trainers for SFT, DPO, GRPO, KTO, and other methods.
- Integrates with PEFT and Accelerate for adapters and distributed training.
- Provides a CLI and asynchronous GRPO rollout/training execution.

### Requirements

- Requires Python, Transformers ecosystem dependencies, model weights, and appropriate training data.
- The asynchronous GRPO example uses separate GPUs for vLLM and the trainer and requires extra dependencies.

### Limitations

- Different trainers require different data fields or reward functions.
- Interfaces under `trl.experimental` are unstable and may change or be removed in any release.

### Getting started

1. Install and select a training method using the [documentation](https://huggingface.co/docs/trl/index).
2. Prepare data or a reward function using the relevant trainer example.
3. Run and evaluate a sample training job before configuring distributed or asynchronous execution.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:27.735Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/huggingface/trl/commit/b2686bf5c300756cdf878b84f83a48f794e2fb94).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://github.com/huggingface/trl/blob/main/README.md)
- [Documentation](https://huggingface.co/docs/trl/index)
- [SFT trainer](https://huggingface.co/docs/trl/sft_trainer)
- [Async GRPO](https://huggingface.co/docs/trl/async_grpo_trainer)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.604509Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "trl",
    "name": "TRL",
    "repository": "huggingface/trl",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkyNTA1MTAwNzU=",
    "category": "ai",
    "summary": {
      "zh-CN": "提供监督微调、偏好优化和强化学习训练器的后训练库。",
      "en": "A post-training library with trainers for supervised fine-tuning, preference optimization, and reinforcement learning."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.604509Z",
        "en": "2026-11-17T14:24:07.604509Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "用示例、偏好数据或奖励函数调整语言模型的任务行为。",
        "en": "Adapts language-model behavior using demonstrations, preference data, or reward functions."
      },
      "source_url": "https://github.com/huggingface/trl/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/huggingface/trl/commit/b2686bf5c300756cdf878b84f83a48f794e2fb94",
        "occurred_at": "2026-11-17T11:57:32Z",
        "reviewed_at": "2026-11-17T14:24:07.604509Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "Add support for vLLM 0.34.x (#8418) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/huggingface/trl/blob/main/README.md"
      },
      {
        "title": "Documentation",
        "url": "https://huggingface.co/docs/trl/index"
      },
      {
        "title": "SFT trainer",
        "url": "https://huggingface.co/docs/trl/sft_trainer"
      },
      {
        "title": "Async GRPO",
        "url": "https://huggingface.co/docs/trl/async_grpo_trainer"
      }
    ]
  },
  "snapshot": {
    "full_name": "huggingface/trl",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkyNTA1MTAwNzU=",
    "stargazers_count": 19750,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:27.735Z",
    "source_url": "https://api.github.com/repos/huggingface/trl"
  }
}
```

</details>
