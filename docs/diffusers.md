# Diffusers

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[huggingface/diffusers](https://github.com/huggingface/diffusers)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 34932 |
| 评估时间 / Evaluated at | 2026-11-17T14:28:37.558140Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:26.401Z |

## 中文

基于 PyTorch 的扩散模型工具库，提供图像、视频和音频生成流水线。

让开发者在代码中调用生成模型，替换采样调度器，或构建自己的扩散处理流程。

### 主要功能

- 通过预训练流水线加载模型并生成内容。
- 组合模型模块和调度器，调整采样过程。
- 提供训练、微调和推理优化的文档与示例。

### 环境要求

- 需要 Python 与适配设备的 PyTorch，建议使用虚拟环境。
- 需要下载所选模型；GPU 和内存要求由模型决定。

### 使用限制

- README 的快速示例使用 CUDA，其他设备应按对应指南调整。
- 不同流水线的输入、支持模型和资源消耗并不相同。

### 开始使用

1. 在虚拟环境中运行 `pip install --upgrade 'diffusers[torch]'`。
2. 按 README 用 `DiffusionPipeline.from_pretrained` 加载选定模型，并设置兼容设备。
3. 运行一个提示词示例，检查输出后再调整调度器或流水线。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:26.401Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/huggingface/diffusers/commit/d9586a3dc62cce5091bdb7cff981d725f4a6dfe5)。为 PAB 和 FasterCache 实现 cache_context。

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://raw.githubusercontent.com/huggingface/diffusers/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/huggingface/diffusers)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

A PyTorch-based diffusion library with pipelines for image, video, and audio generation.

It lets developers call generative models in code, replace sampling schedulers, or build their own diffusion workflows.

### Features

- Load models and generate content through pretrained pipelines.
- Combine model components and schedulers to control sampling.
- Provide documentation and examples for training, fine-tuning, and inference optimization.

### Requirements

- Requires Python and a device-compatible PyTorch installation; a virtual environment is recommended.
- Requires downloading the selected model; GPU and memory needs depend on that model.

### Limitations

- The README quickstart uses CUDA; other devices require their corresponding setup guidance.
- Inputs, supported models, and resource usage differ between pipelines.

### Getting started

1. Run `pip install --upgrade 'diffusers[torch]'` in a virtual environment.
2. Use `DiffusionPipeline.from_pretrained` from the README to load a model and select a compatible device.
3. Run a prompt example, inspect the output, and then adjust the scheduler or pipeline.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:26.401Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/huggingface/diffusers/commit/d9586a3dc62cce5091bdb7cff981d725f4a6dfe5).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://raw.githubusercontent.com/huggingface/diffusers/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/huggingface/diffusers)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:28:37.558140Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "diffusers",
    "name": "Diffusers",
    "repository": "huggingface/diffusers",
    "repo_node_id": "R_kgDOHa8MBQ",
    "category": "media",
    "summary": {
      "zh-CN": "基于 PyTorch 的扩散模型工具库，提供图像、视频和音频生成流水线。",
      "en": "A PyTorch-based diffusion library with pipelines for image, video, and audio generation."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:28:37.558140Z",
        "en": "2026-11-17T14:28:37.558140Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "让开发者在代码中调用生成模型，替换采样调度器，或构建自己的扩散处理流程。",
        "en": "It lets developers call generative models in code, replace sampling schedulers, or build their own diffusion workflows."
      },
      "source_url": "https://raw.githubusercontent.com/huggingface/diffusers/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/huggingface/diffusers/commit/d9586a3dc62cce5091bdb7cff981d725f4a6dfe5",
        "occurred_at": "2026-11-17T13:09:16Z",
        "reviewed_at": "2026-11-17T14:28:37.558140Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "为 PAB 和 FasterCache 实现 cache_context。 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://raw.githubusercontent.com/huggingface/diffusers/main/README.md"
      },
      {
        "title": "GitHub 仓库元数据 / Repository metadata",
        "url": "https://api.github.com/repos/huggingface/diffusers"
      }
    ]
  },
  "snapshot": {
    "full_name": "huggingface/diffusers",
    "repo_node_id": "R_kgDOHa8MBQ",
    "stargazers_count": 34932,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:26.401Z",
    "source_url": "https://api.github.com/repos/huggingface/diffusers"
  }
}
```

</details>
