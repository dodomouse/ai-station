# Wan2.2

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[Wan-Video/Wan2.2](https://github.com/Wan-Video/Wan2.2)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 18725 |
| 评估时间 / Evaluated at | 2026-11-17T14:42:57.064400Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:39:45.972Z |

## 中文

用于文生视频、图生视频和角色动画的模型与推理代码。

把提示词、图像或语音转成视频素材，支持 AI 视频创作和角色表演任务。

### 主要功能

- 提供独立的文生视频、图生视频模型，以及兼顾两种输入的 TI2V-5B。
- S2V 根据音频和参考图像生成视频，可附加文字提示或姿态视频。
- Animate 支持角色动画和角色替换，可复现源视频中的动作与表情。
- 提供单卡和多卡推理入口，并列出 ComfyUI 与 Diffusers 集成方式。

### 环境要求

- 需要 Python 环境与 PyTorch 2.4.0 或更高版本。另需模型权重及匹配的 GPU 依赖。
- TI2V-5B 的官方单卡示例要求至少 24 GB 显存。该示例使用模型卸载、精度转换和 CPU 文本编码。A14B 文生视频与图生视频示例要求至少 80 GB。

### 使用限制

- 不同任务使用不同权重。Animate 还需先按指南预处理源视频。
- README 的显存要求对应特定示例命令。分辨率、帧数和附加模型会影响资源使用。

### 开始使用

1. 按 [Installation](https://github.com/Wan-Video/Wan2.2#installation) 准备环境，并运行 `pip install -r requirements.txt`。
2. 从 README 的 Model Download 表下载所选模型。初次尝试可按硬件条件选择 TI2V-5B。
3. 运行 README 中对应任务的示例命令。保留与显存配置相符的卸载和精度设置，再替换提示词或参考图像。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:39:45.972Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-09-21 · commit](https://github.com/Wan-Video/Wan2.2/commit/1ea34ff48f87168174e12956e200b1d908b1c5ff)。Merge pull request #392 from JianWang-CMU/add-talkverse-community-work

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/Wan-Video/Wan2.2/blob/main/README.md)
- [依赖声明 / Dependencies](https://github.com/Wan-Video/Wan2.2/blob/main/requirements.txt)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/Wan-Video/Wan2.2)

## English

Models and inference code for text-to-video, image-to-video, and character animation.

Turn prompts, images, or speech into video assets for AI video creation and character performance.

### Features

- Provide dedicated text-to-video and image-to-video models, plus TI2V-5B for both input types.
- S2V generates video from audio and a reference image, with optional text prompts or pose video.
- Animate supports character animation and replacement, reproducing motion and expressions from a source video.
- Provide single-GPU and multi-GPU inference, with documented ComfyUI and Diffusers integrations.

### Requirements

- Requires Python and PyTorch 2.4.0 or later, model weights, and compatible GPU dependencies.
- The official TI2V-5B single-GPU example requires at least 24 GB of VRAM with model offloading, dtype conversion, and CPU text encoding. The A14B text-to-video and image-to-video examples require at least 80 GB.

### Limitations

- Different tasks use different weights. Animate also requires preprocessing the source video according to its guide.
- The README's VRAM requirements apply to specific example commands. Resolution, frame count, and additional models affect resource usage.

### Getting started

1. Prepare the environment using [Installation](https://github.com/Wan-Video/Wan2.2#installation), then run `pip install -r requirements.txt`.
2. Download the selected model from the README's Model Download table. Consider TI2V-5B for a first run if your hardware meets its requirements.
3. Run the README example for the selected task. Keep the offloading and dtype settings appropriate to your VRAM, then replace the prompt or reference image.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:39:45.972Z meets the total-Star threshold of 1,000.

Recent activity: [2026-09-21 · commit](https://github.com/Wan-Video/Wan2.2/commit/1ea34ff48f87168174e12956e200b1d908b1c5ff).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/Wan-Video/Wan2.2/blob/main/README.md)
- [依赖声明 / Dependencies](https://github.com/Wan-Video/Wan2.2/blob/main/requirements.txt)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/Wan-Video/Wan2.2)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:42:57.064400Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "wan2-2",
    "name": "Wan2.2",
    "repository": "Wan-Video/Wan2.2",
    "repo_node_id": "R_kgDOPT-eoA",
    "category": "media",
    "summary": {
      "zh-CN": "用于文生视频、图生视频和角色动画的模型与推理代码。",
      "en": "Models and inference code for text-to-video, image-to-video, and character animation."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:42:57.064400Z",
        "en": "2026-11-17T14:42:57.064400Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "把提示词、图像或语音转成视频素材，支持 AI 视频创作和角色表演任务。",
        "en": "Turn prompts, images, or speech into video assets for AI video creation and character performance."
      },
      "source_url": "https://github.com/Wan-Video/Wan2.2/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/Wan-Video/Wan2.2/commit/1ea34ff48f87168174e12956e200b1d908b1c5ff",
        "occurred_at": "2026-09-21T06:16:22Z",
        "reviewed_at": "2026-11-17T14:42:57.064400Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "Merge pull request #392 from JianWang-CMU/add-talkverse-community-work 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/Wan-Video/Wan2.2/blob/main/README.md"
      },
      {
        "title": "依赖声明 / Dependencies",
        "url": "https://github.com/Wan-Video/Wan2.2/blob/main/requirements.txt"
      },
      {
        "title": "GitHub 仓库元数据 / Repository metadata",
        "url": "https://api.github.com/repos/Wan-Video/Wan2.2"
      }
    ]
  },
  "snapshot": {
    "full_name": "Wan-Video/Wan2.2",
    "repo_node_id": "R_kgDOPT-eoA",
    "stargazers_count": 18725,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:39:45.972Z",
    "source_url": "https://api.github.com/repos/Wan-Video/Wan2.2"
  }
}
```

</details>
