# PEFT

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[huggingface/peft](https://github.com/huggingface/peft)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 21899 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.604434Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:26.689Z |

## 中文

通过训练部分参数适配预训练模型的库。

用 LoRA 等方法开展任务微调，减少训练参数与适配器存储量。

### 主要功能

- 提供 LoRA、提示学习及其他参数高效微调方法。
- 保存和加载适配器，并可结合量化模型训练。
- 与 Transformers、Diffusers 和 Accelerate 集成。

### 环境要求

- 需要 Python、兼容的模型框架和基础模型权重。
- 量化与分布式训练需安装对应后端和依赖。

### 使用限制

- 适配器需与对应基础模型及目标模块匹配，不能单独替代完整模型。
- Transformers 集成不包含 PEFT 的全部功能，例如部分适配器合并操作。

### 开始使用

1. 按 [README 快速开始](https://github.com/huggingface/peft#quickstart)安装并加载基础模型。
2. 选择适配方法与目标模块，创建可训练的 PEFT 模型。
3. 训练并保存适配器，重新加载后用任务数据评测。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:26.689Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/huggingface/peft/commit/3a6d5808712f5756aa7b4b02d1619f6887ddc196)。Fix HRA Conv2d string padding (#4159)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://github.com/huggingface/peft/blob/main/README.md)
- [Documentation](https://huggingface.co/docs/peft)
- [Adapter concepts](https://huggingface.co/docs/peft/en/conceptual_guides/adapter)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

A library for adapting pretrained models by training a subset of parameters.

Uses methods such as LoRA for task adaptation with fewer trainable parameters and smaller adapter checkpoints.

### Features

- Provides LoRA, prompt learning, and other parameter-efficient fine-tuning methods.
- Saves and loads adapters and can train with quantized models.
- Integrates with Transformers, Diffusers, and Accelerate.

### Requirements

- Requires Python, a compatible model framework, and base-model weights.
- Quantized and distributed training require the corresponding backends and dependencies.

### Limitations

- Adapters must match their base model and target modules; they do not independently replace the full model.
- The Transformers integration does not expose every PEFT feature, including some adapter-merging operations.

### Getting started

1. Install and load a base model using the [README quickstart](https://github.com/huggingface/peft#quickstart).
2. Choose an adaptation method and target modules, then create a trainable PEFT model.
3. Train and save the adapter, reload it, and evaluate on task data.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:26.689Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/huggingface/peft/commit/3a6d5808712f5756aa7b4b02d1619f6887ddc196).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://github.com/huggingface/peft/blob/main/README.md)
- [Documentation](https://huggingface.co/docs/peft)
- [Adapter concepts](https://huggingface.co/docs/peft/en/conceptual_guides/adapter)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.604434Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "peft",
    "name": "PEFT",
    "repository": "huggingface/peft",
    "repo_node_id": "R_kgDOIf9iDA",
    "category": "ai",
    "summary": {
      "zh-CN": "通过训练部分参数适配预训练模型的库。",
      "en": "A library for adapting pretrained models by training a subset of parameters."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.604434Z",
        "en": "2026-11-17T14:24:07.604434Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "用 LoRA 等方法开展任务微调，减少训练参数与适配器存储量。",
        "en": "Uses methods such as LoRA for task adaptation with fewer trainable parameters and smaller adapter checkpoints."
      },
      "source_url": "https://github.com/huggingface/peft/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/huggingface/peft/commit/3a6d5808712f5756aa7b4b02d1619f6887ddc196",
        "occurred_at": "2026-11-17T12:34:13Z",
        "reviewed_at": "2026-11-17T14:24:07.604434Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "Fix HRA Conv2d string padding (#4159) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/huggingface/peft/blob/main/README.md"
      },
      {
        "title": "Documentation",
        "url": "https://huggingface.co/docs/peft"
      },
      {
        "title": "Adapter concepts",
        "url": "https://huggingface.co/docs/peft/en/conceptual_guides/adapter"
      }
    ]
  },
  "snapshot": {
    "full_name": "huggingface/peft",
    "repo_node_id": "R_kgDOIf9iDA",
    "stargazers_count": 21899,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:26.689Z",
    "source_url": "https://api.github.com/repos/huggingface/peft"
  }
}
```

</details>
