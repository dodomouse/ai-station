# SAM 3

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[facebookresearch/sam3](https://github.com/facebookresearch/sam3)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 12319 |
| 评估时间 / Evaluated at | 2026-11-17T14:44:11.079215Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:39:45.788Z |

## 中文

按文字、点、框或掩码提示分割图像与视频，并跟踪视频中的目标。

为 AI 图像处理提供目标掩码、边界框和评分，可用于选区编辑、素材提取或视频分析。

### 主要功能

- 按文字概念查找并分割匹配的目标实例。
- 支持视觉提示，并可添加点提示修正结果。
- 图像接口返回掩码、边界框和评分；视频接口管理会话与目标跟踪。
- 提供批量图像推理、视频处理和智能体调用的 Notebook 示例。

### 环境要求

- 官方安装指南要求 Python 3.12 或更高版本，以及 PyTorch 2.7 或更高版本。
- 按官方路线需支持 CUDA 的 GPU，CUDA 版本不低于 12.6。
- 使用权重前需申请 [Hugging Face 模型访问](https://huggingface.co/facebook/sam3)，获批后完成认证。
- 运行 Notebook 还需安装 `.[notebooks]` 附加依赖。

### 使用限制

- 安装代码不会自动获得模型权重访问权限。
- 包元数据写 Python 3.8 起，与 README 的安装要求不一致。本条按 README 的 Python 3.12 起说明。
- 代码有 CPU 设备分支，但本次未验证 CPU、Apple MPS 或 macOS 的完整运行流程。
- 分割结果是模型预测，仍需检查目标边界和漏检情况。

### 开始使用

1. 按[安装说明](https://github.com/facebookresearch/sam3/blob/main/README.md#installation)准备 Conda、PyTorch 和 CUDA。下载仓库后运行 `pip install -e .`。
2. 申请模型访问并等待获批。按官方认证说明运行 `hf auth login`，以便下载权重。
3. 运行 `pip install -e ".[notebooks]"`。用 `jupyter notebook examples/sam3_image_predictor_example.ipynb` 打开图像示例，输入图片与提示并检查掩码。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:39:45.788Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/facebookresearch/sam3/commit/31cb7e624e4fe95301b1be1d4e809111593d2e45)。Upgrade packages to Pyrefly R1546.1 (landing group 10)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README 与安装说明 / Official README and installation](https://github.com/facebookresearch/sam3/blob/main/README.md)
- [包配置 / Package configuration](https://github.com/facebookresearch/sam3/blob/main/pyproject.toml)
- [模型加载与设备选择 / Model loading and device selection](https://github.com/facebookresearch/sam3/blob/main/sam3/model_builder.py)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/facebookresearch/sam3)

## English

Segment images and videos using text, points, boxes, or masks, and track objects across video frames.

It supplies object masks, bounding boxes, and scores for AI workflows such as region editing, asset extraction, and video analysis.

### Features

- Find and segment object instances matching a text concept.
- Support visual prompts and refine results by adding point prompts.
- The image interface returns masks, bounding boxes, and scores; the video interface manages sessions and object tracking.
- Provide notebooks for batched image inference, video processing, and agent use.

### Requirements

- The official installation guide requires Python 3.12 or later and PyTorch 2.7 or later.
- The documented setup requires a CUDA-compatible GPU with CUDA 12.6 or later.
- Request [Hugging Face model access](https://huggingface.co/facebook/sam3) before using the weights, then authenticate after approval.
- Running the notebooks also requires the `.[notebooks]` extra dependencies.

### Limitations

- Installing the code does not automatically grant access to the model weights.
- Package metadata allows Python from 3.8, which differs from the README's installation requirements. This entry follows the README's Python 3.12 baseline.
- The code includes a CPU device branch, but this review did not validate complete CPU, Apple MPS, or macOS execution.
- Segmentation results are model predictions; object boundaries and missed objects still need inspection.

### Getting started

1. Prepare Conda, PyTorch, and CUDA using the [installation instructions](https://github.com/facebookresearch/sam3/blob/main/README.md#installation), download the repository, and run `pip install -e .`.
2. Request model access and wait for approval. Follow the official authentication instructions with `hf auth login` to enable weight downloads.
3. Run `pip install -e ".[notebooks]"`, then open `jupyter notebook examples/sam3_image_predictor_example.ipynb`. Supply an image and prompt and inspect the masks.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:39:45.788Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/facebookresearch/sam3/commit/31cb7e624e4fe95301b1be1d4e809111593d2e45).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README 与安装说明 / Official README and installation](https://github.com/facebookresearch/sam3/blob/main/README.md)
- [包配置 / Package configuration](https://github.com/facebookresearch/sam3/blob/main/pyproject.toml)
- [模型加载与设备选择 / Model loading and device selection](https://github.com/facebookresearch/sam3/blob/main/sam3/model_builder.py)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/facebookresearch/sam3)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:44:11.079215Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "sam3",
    "name": "SAM 3",
    "repository": "facebookresearch/sam3",
    "repo_node_id": "R_kgDOPOQxCg",
    "category": "media",
    "summary": {
      "zh-CN": "按文字、点、框或掩码提示分割图像与视频，并跟踪视频中的目标。",
      "en": "Segment images and videos using text, points, boxes, or masks, and track objects across video frames."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:44:11.079215Z",
        "en": "2026-11-17T14:44:11.079215Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "为 AI 图像处理提供目标掩码、边界框和评分，可用于选区编辑、素材提取或视频分析。",
        "en": "It supplies object masks, bounding boxes, and scores for AI workflows such as region editing, asset extraction, and video analysis."
      },
      "source_url": "https://github.com/facebookresearch/sam3/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/facebookresearch/sam3/commit/31cb7e624e4fe95301b1be1d4e809111593d2e45",
        "occurred_at": "2026-11-17T09:32:39Z",
        "reviewed_at": "2026-11-17T14:44:11.079215Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "Upgrade packages to Pyrefly R1546.1 (landing group 10) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README 与安装说明 / Official README and installation",
        "url": "https://github.com/facebookresearch/sam3/blob/main/README.md"
      },
      {
        "title": "包配置 / Package configuration",
        "url": "https://github.com/facebookresearch/sam3/blob/main/pyproject.toml"
      },
      {
        "title": "模型加载与设备选择 / Model loading and device selection",
        "url": "https://github.com/facebookresearch/sam3/blob/main/sam3/model_builder.py"
      },
      {
        "title": "GitHub 仓库元数据 / Repository metadata",
        "url": "https://api.github.com/repos/facebookresearch/sam3"
      }
    ]
  },
  "snapshot": {
    "full_name": "facebookresearch/sam3",
    "repo_node_id": "R_kgDOPOQxCg",
    "stargazers_count": 12319,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:39:45.788Z",
    "source_url": "https://api.github.com/repos/facebookresearch/sam3"
  }
}
```

</details>
