# Qwen-Image

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[QwenLM/Qwen-Image](https://github.com/QwenLM/Qwen-Image)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 8487 |
| 评估时间 / Evaluated at | 2026-11-17T14:44:11.078779Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:39:45.759Z |

## 中文

提供文生图和图像编辑模型及示例，支持画面中的文字生成和多图编辑。

把文字指令或参考图转成视觉素材，供 AI 制作海报、插图或修改已有图像。

### 主要功能

- 通过 Diffusers 调用 Qwen-Image 文生图模型。
- Qwen-Image-Edit-2511 支持多图输入和文字指令编辑。
- 文生图示例支持选择画面比例、随机种子及采样参数。
- 提供多 GPU API 服务示例，包含 Gradio 界面和任务队列。

### 环境要求

- 需要 Python、PyTorch，以及 Transformers 4.51.3 或更高版本。
- README 要求安装最新 Diffusers；编辑示例使用 CUDA 和 bfloat16。
- 需要下载选定模型权重，并准备对应存储及运行内存。

### 使用限制

- 不同模型使用不同流水线。早期 Qwen-Image-Edit 仅支持单图输入。
- 文生图示例有 CPU 加载分支，但采样生成器仍指定 CUDA。CPU 运行需调整并验证。
- 可选提示词增强会调用 Qwen-Plus 或 Qwen-VL-Max，需要外部服务配置。
- 本次 PR #295 未合并，仅用于证明活动；不能据此认定默认采样步数已变更。

### 开始使用

1. 按[快速入门](https://github.com/QwenLM/Qwen-Image/blob/main/README.md#quick-start)准备 PyTorch 和 Transformers。运行 `pip install git+https://github.com/huggingface/diffusers`。
2. 选择文生图或编辑示例。用对应流水线的 `from_pretrained` 加载模型权重。
3. 先核对代码中的设备与精度设置。填写提示词及所需参考图，按示例运行并保存输出。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:39:45.759Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-11 · pr](https://github.com/QwenLM/Qwen-Image/pull/295)。Feat/default steps 25

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README 与快速入门 / Official README and quickstart](https://github.com/QwenLM/Qwen-Image/blob/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/QwenLM/Qwen-Image)
- [活动记录 PR #295 / Activity record PR #295](https://github.com/QwenLM/Qwen-Image/pull/295)

## English

Models and examples for text-to-image generation and image editing, including text rendering within images and editing with multiple input images.

It turns text instructions or reference images into visual assets for AI-assisted posters, illustrations, and edits to existing images.

### Features

- Call Qwen-Image text-to-image models through Diffusers.
- Qwen-Image-Edit-2511 supports multiple image inputs and editing through text instructions.
- Text-to-image examples expose aspect ratios, random seeds, and sampling settings.
- Provide a multi-GPU API server example with a Gradio interface and task queue.

### Requirements

- Requires Python, PyTorch, and Transformers 4.51.3 or later.
- The README calls for the latest Diffusers; the editing example uses CUDA and bfloat16.
- Download the selected model weights and provide the required storage and runtime memory.

### Limitations

- Different models use different pipelines. The original Qwen-Image-Edit accepts only one input image.
- The text-to-image example has a CPU loading branch but still specifies CUDA for its sampling generator. CPU execution needs adaptation and verification.
- Optional prompt enhancement calls Qwen-Plus or Qwen-VL-Max and requires external service configuration.
- PR #295 is unmerged and establishes activity only; it does not establish a change to the default sampling-step count.

### Getting started

1. Prepare PyTorch and Transformers using the [quickstart](https://github.com/QwenLM/Qwen-Image/blob/main/README.md#quick-start), then run `pip install git+https://github.com/huggingface/diffusers`.
2. Choose a text-to-image or editing example and load its model weights through the matching pipeline's `from_pretrained` method.
3. Check the device and precision settings first. Set the prompt and any required reference images, then run the example and save the output.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:39:45.759Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-11 · pr](https://github.com/QwenLM/Qwen-Image/pull/295).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README 与快速入门 / Official README and quickstart](https://github.com/QwenLM/Qwen-Image/blob/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/QwenLM/Qwen-Image)
- [活动记录 PR #295 / Activity record PR #295](https://github.com/QwenLM/Qwen-Image/pull/295)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:44:11.078779Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "qwen-image",
    "name": "Qwen-Image",
    "repository": "QwenLM/Qwen-Image",
    "repo_node_id": "R_kgDOPXe32Q",
    "category": "media",
    "summary": {
      "zh-CN": "提供文生图和图像编辑模型及示例，支持画面中的文字生成和多图编辑。",
      "en": "Models and examples for text-to-image generation and image editing, including text rendering within images and editing with multiple input images."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:44:11.078779Z",
        "en": "2026-11-17T14:44:11.078779Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "把文字指令或参考图转成视觉素材，供 AI 制作海报、插图或修改已有图像。",
        "en": "It turns text instructions or reference images into visual assets for AI-assisted posters, illustrations, and edits to existing images."
      },
      "source_url": "https://github.com/QwenLM/Qwen-Image/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "pr",
        "url": "https://github.com/QwenLM/Qwen-Image/pull/295",
        "occurred_at": "2026-11-11T04:45:01Z",
        "reviewed_at": "2026-11-17T14:44:11.078779Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "Feat/default steps 25 此记录用于证明窗口内活动。",
          "en": "The recorded pr establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README 与快速入门 / Official README and quickstart",
        "url": "https://github.com/QwenLM/Qwen-Image/blob/main/README.md"
      },
      {
        "title": "GitHub 仓库元数据 / Repository metadata",
        "url": "https://api.github.com/repos/QwenLM/Qwen-Image"
      },
      {
        "title": "活动记录 PR #295 / Activity record PR #295",
        "url": "https://github.com/QwenLM/Qwen-Image/pull/295"
      }
    ]
  },
  "snapshot": {
    "full_name": "QwenLM/Qwen-Image",
    "repo_node_id": "R_kgDOPXe32Q",
    "stargazers_count": 8487,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:39:45.759Z",
    "source_url": "https://api.github.com/repos/QwenLM/Qwen-Image"
  }
}
```

</details>
