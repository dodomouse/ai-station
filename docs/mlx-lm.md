# MLX LM

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[ml-explore/mlx-lm](https://github.com/ml-explore/mlx-lm)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 7671 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.604665Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:27.311Z |

## 中文

基于 MLX 在 Apple 芯片上生成文本和微调语言模型的 Python 包。

在本机运行聊天、批量生成和模型适配任务。

### 主要功能

- 从 Hugging Face Hub 加载兼容模型，支持命令行及 Python 调用。
- 支持量化、低秩及全参数微调。
- 提供流式生成、提示缓存和分布式推理或训练。

### 环境要求

- 需要 Apple 芯片、MLX 与 Python 环境，并准备兼容的模型权重。

### 使用限制

- 模型和缓存会占用统一内存，模型接近可用内存上限时可能变慢。
- 大模型内存锁定优化需要 macOS 15+。部分模型分词器还需用户允许执行远程代码。

### 开始使用

1. 按 [README](https://github.com/ml-explore/mlx-lm#quick-start)安装并选择 MLX 兼容模型。
2. 运行生成或聊天示例，检查内存占用和输出。
3. 需要微调时，按[训练说明](https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/LORA.md)准备数据和适配器配置。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:27.311Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-16 · commit](https://github.com/ml-explore/mlx-lm/commit/c4c9c762cc797fd979fc98645f5db5112753bbe9)。Add Qwen3.8-Flash-Next (qwen4_exp) model support (#1788)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://github.com/ml-explore/mlx-lm/blob/main/README.md)
- [Fine-tuning](https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/LORA.md)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

A Python package for text generation and language-model fine-tuning on Apple silicon with MLX.

Runs local chat, batch generation, and model adaptation tasks.

### Features

- Loads compatible models from the Hugging Face Hub through CLI and Python interfaces.
- Supports quantization, low-rank fine-tuning, and full fine-tuning.
- Provides streaming generation, prompt caching, and distributed inference or training.

### Requirements

- Requires Apple silicon, MLX, a Python environment, and compatible model weights.

### Limitations

- Models and caches consume unified memory; performance may slow when the model approaches available memory.
- The large-model wired-memory optimization requires macOS 15+; some tokenizers also require permission to execute remote code.

### Getting started

1. Install and choose an MLX-compatible model using the [README](https://github.com/ml-explore/mlx-lm#quick-start).
2. Run a generation or chat example and inspect memory use and output.
3. For fine-tuning, prepare data and adapter settings using the [training guide](https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/LORA.md).

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:27.311Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-16 · commit](https://github.com/ml-explore/mlx-lm/commit/c4c9c762cc797fd979fc98645f5db5112753bbe9).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://github.com/ml-explore/mlx-lm/blob/main/README.md)
- [Fine-tuning](https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/LORA.md)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.604665Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "mlx-lm",
    "name": "MLX LM",
    "repository": "ml-explore/mlx-lm",
    "repo_node_id": "R_kgDOOG6IBg",
    "category": "ai",
    "summary": {
      "zh-CN": "基于 MLX 在 Apple 芯片上生成文本和微调语言模型的 Python 包。",
      "en": "A Python package for text generation and language-model fine-tuning on Apple silicon with MLX."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.604665Z",
        "en": "2026-11-17T14:24:07.604665Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "在本机运行聊天、批量生成和模型适配任务。",
        "en": "Runs local chat, batch generation, and model adaptation tasks."
      },
      "source_url": "https://github.com/ml-explore/mlx-lm/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/ml-explore/mlx-lm/commit/c4c9c762cc797fd979fc98645f5db5112753bbe9",
        "occurred_at": "2026-11-16T23:02:24Z",
        "reviewed_at": "2026-11-17T14:24:07.604665Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "Add Qwen3.8-Flash-Next (qwen4_exp) model support (#1788) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/ml-explore/mlx-lm/blob/main/README.md"
      },
      {
        "title": "Fine-tuning",
        "url": "https://github.com/ml-explore/mlx-lm/blob/main/mlx_lm/LORA.md"
      }
    ]
  },
  "snapshot": {
    "full_name": "ml-explore/mlx-lm",
    "repo_node_id": "R_kgDOOG6IBg",
    "stargazers_count": 7671,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:27.311Z",
    "source_url": "https://api.github.com/repos/ml-explore/mlx-lm"
  }
}
```

</details>
