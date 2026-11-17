# LlamaFactory

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 76084 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.604287Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:27.026Z |

## 中文

通过命令行与 Web 界面配置语言模型微调的工具。

把数据准备、微调、推理和适配器合并集中到同一套配置流程。

### 主要功能

- 支持监督微调、奖励建模和多种偏好训练方法。
- 支持全参数、冻结参数、LoRA 和量化 LoRA 训练。
- 提供 LlamaBoard 界面及实验记录工具集成。

### 环境要求

- 需要 Python、PyTorch 和所选加速器对应的依赖，或使用官方容器。
- 自定义数据需按文档注册到 `data/dataset_info.json`。

### 使用限制

- 模型和训练方法并非任意组合都可用，需核对示例与依赖。
- Windows GPU 环境需单独准备支持 CUDA 的 PyTorch；量化及 Flash Attention 还有额外要求。

### 开始使用

1. 按[安装章节](https://github.com/hiyouga/LlamaFactory#getting-started)准备环境。
2. 按[数据说明](https://github.com/hiyouga/LlamaFactory/blob/main/data/README.md)配置训练集。
3. 选择[官方示例](https://github.com/hiyouga/LlamaFactory/blob/main/examples/README.md)，运行微调并检查推理结果。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:27.026Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/hiyouga/LlamaFactory/commit/885a4ca65cebf17a92e869af13c2ce42caca314a)。[deps] upgrade transformers to 5.17.0 (#10869)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://github.com/hiyouga/LlamaFactory/blob/main/README.md)
- [Data guide](https://github.com/hiyouga/LlamaFactory/blob/main/data/README.md)
- [Examples](https://github.com/hiyouga/LlamaFactory/blob/main/examples/README.md)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

A tool for configuring language-model fine-tuning through a CLI and web interface.

Organizes data preparation, fine-tuning, inference, and adapter merging in one configuration workflow.

### Features

- Supports supervised fine-tuning, reward modeling, and several preference-training methods.
- Supports full, frozen-parameter, LoRA, and quantized LoRA training.
- Provides the LlamaBoard interface and experiment-tracking integrations.

### Requirements

- Requires Python, PyTorch, and dependencies for the selected accelerator, or an official container.
- Register custom datasets in `data/dataset_info.json` as documented.

### Limitations

- Not every model and training-method combination is supported; check examples and dependencies.
- Windows GPU setups require a CUDA-enabled PyTorch installation; quantization and Flash Attention have additional requirements.

### Getting started

1. Prepare the environment using the [installation section](https://github.com/hiyouga/LlamaFactory#getting-started).
2. Configure the training set using the [data guide](https://github.com/hiyouga/LlamaFactory/blob/main/data/README.md).
3. Choose an [official example](https://github.com/hiyouga/LlamaFactory/blob/main/examples/README.md), fine-tune, and inspect inference results.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:27.026Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/hiyouga/LlamaFactory/commit/885a4ca65cebf17a92e869af13c2ce42caca314a).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://github.com/hiyouga/LlamaFactory/blob/main/README.md)
- [Data guide](https://github.com/hiyouga/LlamaFactory/blob/main/data/README.md)
- [Examples](https://github.com/hiyouga/LlamaFactory/blob/main/examples/README.md)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.604287Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "llamafactory",
    "name": "LlamaFactory",
    "repository": "hiyouga/LlamaFactory",
    "repo_node_id": "R_kgDOJodxvg",
    "category": "ai",
    "summary": {
      "zh-CN": "通过命令行与 Web 界面配置语言模型微调的工具。",
      "en": "A tool for configuring language-model fine-tuning through a CLI and web interface."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.604287Z",
        "en": "2026-11-17T14:24:07.604287Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "把数据准备、微调、推理和适配器合并集中到同一套配置流程。",
        "en": "Organizes data preparation, fine-tuning, inference, and adapter merging in one configuration workflow."
      },
      "source_url": "https://github.com/hiyouga/LlamaFactory/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/hiyouga/LlamaFactory/commit/885a4ca65cebf17a92e869af13c2ce42caca314a",
        "occurred_at": "2026-11-17T04:25:41Z",
        "reviewed_at": "2026-11-17T14:24:07.604287Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "[deps] upgrade transformers to 5.17.0 (#10869) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/hiyouga/LlamaFactory/blob/main/README.md"
      },
      {
        "title": "Data guide",
        "url": "https://github.com/hiyouga/LlamaFactory/blob/main/data/README.md"
      },
      {
        "title": "Examples",
        "url": "https://github.com/hiyouga/LlamaFactory/blob/main/examples/README.md"
      }
    ]
  },
  "snapshot": {
    "full_name": "hiyouga/LlamaFactory",
    "repo_node_id": "R_kgDOJodxvg",
    "stargazers_count": 76084,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:27.026Z",
    "source_url": "https://api.github.com/repos/hiyouga/LlamaFactory"
  }
}
```

</details>
