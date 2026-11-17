# LTX-2

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[Lightricks/LTX-2](https://github.com/Lightricks/LTX-2)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 10280 |
| 评估时间 / Evaluated at | 2026-11-17T14:46:04.520061Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:39:45.800Z |

## 中文

用于同步音视频生成、视频转换和局部片段重生成的 Python 工具库。

把文本、图片或参考音视频转成新的视频，并通过局部修改反复调整 AI 生成结果。

### 主要功能

- 从文字或图片生成同步音视频，提供蒸馏和两阶段流水线。
- 通过 IC-LoRA 转换视频，通过 Retake 重生成指定时间片段。
- 支持音频驱动视频生成，以及关键帧插值。
- 提供 LoRA 训练工具，用于定制基础模型。

### 环境要求

- 需要 Python 3.10 或更高版本及 uv。PyTorch 和设备依赖按官方配置安装。
- 需下载所选流水线的模型组件。当前 LTX-2.5 快速入门下载约 66 GiB 文件。
- 训练指南面向 Linux 与 CUDA，需 NVIDIA GPU。推理资源需求随流水线和卸载配置变化。

### 使用限制

- DFR 使用蒸馏模型和额外的细节 LoRA，不能换成完整 dev 模型。它比入门流水线耗时更长，也需要更多显存。
- `natten` 加速仅用于 Linux 与 CUDA。Windows 和 macOS 安装时会自动跳过，并使用其他解码后端。
- 整合权重路径与拆分组件路径不能混用。所需组件须与流水线一致。

### 开始使用

1. 克隆仓库，按 README 运行 `uv sync --extra natten`。
2. 按 Quick Start 下载 LTX-2.5 组件，并保留其目录结构。若下载提示无权限，按模型页面完成访问设置。
3. 运行 Quick Start 的 `ltx_pipelines.distilled` 示例并检查输出。需要编辑时，再按[流水线指南](https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-pipelines/docs/pipelines.md)选择功能。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:39:45.800Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-12 · commit](https://github.com/Lightricks/LTX-2/commit/f0f2f8607189c78a72420b2b63cb1975b5eca179)。Automated PR - 2026-11-12

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/Lightricks/LTX-2/blob/main/README.md)
- [安装与用法 / Installation and usage](https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-pipelines/docs/installation.md)
- [Python 版本声明 / Python requirement](https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-pipelines/pyproject.toml)
- [训练指南入口 / Training guide](https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-trainer/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/Lightricks/LTX-2)

## English

A Python toolkit for synchronized audio-video generation, video transformations, and regenerating selected segments.

Turn text, images, or reference audio and video into new clips, then revise selected regions of AI-generated output.

### Features

- Generate synchronized audio and video from text or images using distilled or two-stage pipelines.
- Transform video with IC-LoRA and regenerate a specified time region with Retake.
- Support audio-conditioned video generation and keyframe interpolation.
- Provide LoRA training tools for customizing a base model.

### Requirements

- Requires Python 3.10 or later and uv. Install PyTorch and device dependencies using the official configuration.
- Download the model components required by the selected pipeline. The current LTX-2.5 quickstart downloads about 66 GiB.
- The training guide targets Linux with CUDA and requires an NVIDIA GPU. Inference resource needs vary with the pipeline and offloading configuration.

### Limitations

- DFR uses the distilled model and an additional detailing LoRA, not the full dev model. It takes longer and uses more VRAM than the starter pipeline.
- The natten acceleration extra is limited to Linux and CUDA. It is skipped automatically on Windows and macOS, where decoding uses another backend.
- Monolithic checkpoint paths and split-component paths cannot be mixed. Required components must match the selected pipeline.

### Getting started

1. Clone the repository and run `uv sync --extra natten` as described in the README.
2. Download the LTX-2.5 components from Quick Start and preserve their directory layout. If access is denied, complete the access setup on the model page.
3. Run the Quick Start example for `ltx_pipelines.distilled` and inspect its output. For editing, choose a function using the [pipeline guide](https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-pipelines/docs/pipelines.md).

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:39:45.800Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-12 · commit](https://github.com/Lightricks/LTX-2/commit/f0f2f8607189c78a72420b2b63cb1975b5eca179).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/Lightricks/LTX-2/blob/main/README.md)
- [安装与用法 / Installation and usage](https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-pipelines/docs/installation.md)
- [Python 版本声明 / Python requirement](https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-pipelines/pyproject.toml)
- [训练指南入口 / Training guide](https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-trainer/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/Lightricks/LTX-2)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:46:04.520061Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "ltx-2",
    "name": "LTX-2",
    "repository": "Lightricks/LTX-2",
    "repo_node_id": "R_kgDOQzA71Q",
    "category": "media",
    "summary": {
      "zh-CN": "用于同步音视频生成、视频转换和局部片段重生成的 Python 工具库。",
      "en": "A Python toolkit for synchronized audio-video generation, video transformations, and regenerating selected segments."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:46:04.520061Z",
        "en": "2026-11-17T14:46:04.520061Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "把文本、图片或参考音视频转成新的视频，并通过局部修改反复调整 AI 生成结果。",
        "en": "Turn text, images, or reference audio and video into new clips, then revise selected regions of AI-generated output."
      },
      "source_url": "https://github.com/Lightricks/LTX-2/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/Lightricks/LTX-2/commit/f0f2f8607189c78a72420b2b63cb1975b5eca179",
        "occurred_at": "2026-11-12T13:27:53Z",
        "reviewed_at": "2026-11-17T14:46:04.520061Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "Automated PR - 2026-11-12 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/Lightricks/LTX-2/blob/main/README.md"
      },
      {
        "title": "安装与用法 / Installation and usage",
        "url": "https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-pipelines/docs/installation.md"
      },
      {
        "title": "Python 版本声明 / Python requirement",
        "url": "https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-pipelines/pyproject.toml"
      },
      {
        "title": "训练指南入口 / Training guide",
        "url": "https://github.com/Lightricks/LTX-2/blob/main/packages/ltx-trainer/README.md"
      },
      {
        "title": "GitHub 仓库元数据 / Repository metadata",
        "url": "https://api.github.com/repos/Lightricks/LTX-2"
      }
    ]
  },
  "snapshot": {
    "full_name": "Lightricks/LTX-2",
    "repo_node_id": "R_kgDOQzA71Q",
    "stargazers_count": 10280,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:39:45.800Z",
    "source_url": "https://api.github.com/repos/Lightricks/LTX-2"
  }
}
```

</details>
