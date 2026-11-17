# bitsandbytes

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[bitsandbytes-foundation/bitsandbytes](https://github.com/bitsandbytes-foundation/bitsandbytes)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 8543 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.603738Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:27.812Z |

## 中文

为 PyTorch 提供低位宽量化与优化器的库。

降低语言模型推理和微调中的权重或优化器状态内存用量。

### 主要功能

- 提供 8 位优化器和对应量化运算。
- 通过 LLM.int8() 支持 8 位推理。
- 提供 4 位线性层，可用于 QLoRA 微调。

### 环境要求

- 需要 Python 3.10+ 和 PyTorch 2.4+。
- 需按操作系统、加速器与功能核对支持矩阵。

### 使用限制

- README 的加速器表对应开发分支，稳定版能力应以对应版本文档为准。
- 不同后端的量化和优化器支持不完全一致，不能假定所有设备功能相同。

### 开始使用

1. 按[官方文档](https://huggingface.co/docs/bitsandbytes/main)选择支持的安装方式。
2. 按 [Transformers 集成](https://huggingface.co/docs/transformers/quantization/bitsandbytes)加载量化模型。
3. 检查内存和任务输出；需要微调时再配置 PEFT。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:27.812Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-10-27 · commit](https://github.com/bitsandbytes-foundation/bitsandbytes/commit/a616886cacf86701514f0cb1d6be760f967481c0)。Cache the hipBLASLt int8 matmul algo per problem on ROCm (#2100)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/main/README.md)
- [Documentation](https://huggingface.co/docs/bitsandbytes/main)
- [Transformers integration](https://huggingface.co/docs/transformers/quantization/bitsandbytes)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

A library providing low-bit quantization and optimizers for PyTorch.

Reduces memory used by weights or optimizer states during language-model inference and fine-tuning.

### Features

- Provides 8-bit optimizers and quantization operations.
- Supports 8-bit inference through LLM.int8().
- Provides 4-bit linear layers for QLoRA fine-tuning.

### Requirements

- Requires Python 3.10+ and PyTorch 2.4+.
- Check the support matrix for the operating system, accelerator, and feature.

### Limitations

- The README accelerator table describes the development branch; consult release-specific documentation for stable support.
- Quantization and optimizer support differ across backends; device capabilities are not interchangeable.

### Getting started

1. Choose a supported installation path in the [documentation](https://huggingface.co/docs/bitsandbytes/main).
2. Load a quantized model using the [Transformers integration](https://huggingface.co/docs/transformers/quantization/bitsandbytes).
3. Inspect memory use and task outputs, then configure PEFT if fine-tuning is needed.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:27.812Z meets the total-Star threshold of 1,000.

Recent activity: [2026-10-27 · commit](https://github.com/bitsandbytes-foundation/bitsandbytes/commit/a616886cacf86701514f0cb1d6be760f967481c0).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/main/README.md)
- [Documentation](https://huggingface.co/docs/bitsandbytes/main)
- [Transformers integration](https://huggingface.co/docs/transformers/quantization/bitsandbytes)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.603738Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "bitsandbytes",
    "name": "bitsandbytes",
    "repository": "bitsandbytes-foundation/bitsandbytes",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkzNzM2NzQyNTg=",
    "category": "ai",
    "summary": {
      "zh-CN": "为 PyTorch 提供低位宽量化与优化器的库。",
      "en": "A library providing low-bit quantization and optimizers for PyTorch."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.603738Z",
        "en": "2026-11-17T14:24:07.603738Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "降低语言模型推理和微调中的权重或优化器状态内存用量。",
        "en": "Reduces memory used by weights or optimizer states during language-model inference and fine-tuning."
      },
      "source_url": "https://github.com/bitsandbytes-foundation/bitsandbytes/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/bitsandbytes-foundation/bitsandbytes/commit/a616886cacf86701514f0cb1d6be760f967481c0",
        "occurred_at": "2026-10-27T21:18:29Z",
        "reviewed_at": "2026-11-17T14:24:07.603738Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "Cache the hipBLASLt int8 matmul algo per problem on ROCm (#2100) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/bitsandbytes-foundation/bitsandbytes/blob/main/README.md"
      },
      {
        "title": "Documentation",
        "url": "https://huggingface.co/docs/bitsandbytes/main"
      },
      {
        "title": "Transformers integration",
        "url": "https://huggingface.co/docs/transformers/quantization/bitsandbytes"
      }
    ]
  },
  "snapshot": {
    "full_name": "bitsandbytes-foundation/bitsandbytes",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkzNzM2NzQyNTg=",
    "stargazers_count": 8543,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:27.812Z",
    "source_url": "https://api.github.com/repos/bitsandbytes-foundation/bitsandbytes"
  }
}
```

</details>
