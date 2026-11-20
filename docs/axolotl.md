# Axolotl

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[axolotl-ai-cloud/axolotl](https://github.com/axolotl-ai-cloud/axolotl)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 12735 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.604138Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:27.061Z |

## 中文

用配置文件组织语言模型微调和后训练的工具。

把数据预处理、训练、评测与导出串成可重复的模型适配流程。

### 主要功能

- 支持全参数微调、LoRA、量化微调和偏好训练。
- 支持文本及多模态模型，并加载本地或远程数据集。
- 通过 YAML 配置训练流程，并支持多 GPU 与多节点训练。

### 环境要求

- README 要求 Python 3.12+、PyTorch 2.13.0+，以及支持的 NVIDIA 或 AMD GPU。
- 需要模型权重和符合所选格式的训练数据。

### 使用限制

- 模型、训练方法和加速功能的组合受支持矩阵限制。
- 默认启用遥测，可按官方说明退出。

### 开始使用

1. 按[安装说明](https://docs.axolotl.ai/docs/installation.html)配置环境，并核对[支持矩阵](https://docs.axolotl.ai/docs/support-matrix.html)。
2. 复制官方模型示例，设置数据来源和训练参数。
3. 按[入门指南](https://docs.axolotl.ai/docs/getting-started.html)预处理数据、训练并检查输出。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:27.061Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-13 · commit](https://github.com/axolotl-ai-cloud/axolotl/commit/f2158ff1922b2bcf701854a17e47cc91ba26e7e9)。Resolve the parallel layout once into a typed MeshSpec (dense-degree dp_shard_size) (#4299)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://github.com/axolotl-ai-cloud/axolotl/blob/main/README.md)
- [Installation](https://docs.axolotl.ai/docs/installation.html)
- [Support matrix](https://docs.axolotl.ai/docs/support-matrix.html)
- [Getting started](https://docs.axolotl.ai/docs/getting-started.html)

## English

A tool for organizing language-model fine-tuning and post-training through configuration files.

Connects preprocessing, training, evaluation, and export into a repeatable model adaptation workflow.

### Features

- Supports full fine-tuning, LoRA, quantized fine-tuning, and preference training.
- Supports text and multimodal models with local or remote datasets.
- Configures training workflows in YAML and supports multi-GPU and multi-node training.

### Requirements

- The README requires Python 3.12+, PyTorch 2.13.0+, and a supported NVIDIA or AMD GPU.
- Requires model weights and training data in the chosen format.

### Limitations

- Combinations of models, training methods, and acceleration features are constrained by the support matrix.
- Telemetry is enabled by default and can be disabled as documented.

### Getting started

1. Set up the environment using the [installation guide](https://docs.axolotl.ai/docs/installation.html) and check the [support matrix](https://docs.axolotl.ai/docs/support-matrix.html).
2. Copy an official model example and set data sources and training parameters.
3. Preprocess data, train, and inspect outputs using the [getting-started guide](https://docs.axolotl.ai/docs/getting-started.html).

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:27.061Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-13 · commit](https://github.com/axolotl-ai-cloud/axolotl/commit/f2158ff1922b2bcf701854a17e47cc91ba26e7e9).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://github.com/axolotl-ai-cloud/axolotl/blob/main/README.md)
- [Installation](https://docs.axolotl.ai/docs/installation.html)
- [Support matrix](https://docs.axolotl.ai/docs/support-matrix.html)
- [Getting started](https://docs.axolotl.ai/docs/getting-started.html)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.604138Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "axolotl",
    "name": "Axolotl",
    "repository": "axolotl-ai-cloud/axolotl",
    "repo_node_id": "R_kgDOJWpdTQ",
    "category": "ai",
    "summary": {
      "zh-CN": "用配置文件组织语言模型微调和后训练的工具。",
      "en": "A tool for organizing language-model fine-tuning and post-training through configuration files."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.604138Z",
        "en": "2026-11-17T14:24:07.604138Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "把数据预处理、训练、评测与导出串成可重复的模型适配流程。",
        "en": "Connects preprocessing, training, evaluation, and export into a repeatable model adaptation workflow."
      },
      "source_url": "https://github.com/axolotl-ai-cloud/axolotl/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/axolotl-ai-cloud/axolotl/commit/f2158ff1922b2bcf701854a17e47cc91ba26e7e9",
        "occurred_at": "2026-11-13T19:22:33Z",
        "reviewed_at": "2026-11-17T14:24:07.604138Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "Resolve the parallel layout once into a typed MeshSpec (dense-degree dp_shard_size) (#4299) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/axolotl-ai-cloud/axolotl/blob/main/README.md"
      },
      {
        "title": "Installation",
        "url": "https://docs.axolotl.ai/docs/installation.html"
      },
      {
        "title": "Support matrix",
        "url": "https://docs.axolotl.ai/docs/support-matrix.html"
      },
      {
        "title": "Getting started",
        "url": "https://docs.axolotl.ai/docs/getting-started.html"
      }
    ]
  },
  "snapshot": {
    "full_name": "axolotl-ai-cloud/axolotl",
    "repo_node_id": "R_kgDOJWpdTQ",
    "stargazers_count": 12735,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:27.061Z",
    "source_url": "https://api.github.com/repos/axolotl-ai-cloud/axolotl"
  }
}
```

</details>
