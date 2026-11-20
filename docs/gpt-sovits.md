# GPT-SoVITS

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 65252 |
| 评估时间 / Evaluated at | 2026-11-17T14:28:37.558833Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:26.649Z |

## 中文

提供声音克隆、语音合成和少样本微调的 WebUI 与训练工具。

将文本生成为参考声音的语音，并把音频整理、转写和校对接入训练流程。

### 主要功能

- 支持零样本推理与少样本微调。
- 支持中文、英语、日语、韩语和粤语的跨语言合成。
- 集成伴奏分离、音频切片、ASR 和文本标注工具。

### 环境要求

- 可选择整合包、手动安装或 Docker；手动方式需匹配 Python、PyTorch 和设备环境。
- 需准备预训练模型及音频处理依赖，按安装说明配置 FFmpeg。

### 使用限制

- 应按模型版本和设备选择官方已测试环境对应的流程。
- 微调前需要校对 ASR 文本；自动切片与转写不能代替数据检查。

### 开始使用

1. 按 README 的 Installation 和 Pretrained Models 准备环境与模型。
2. 整合包运行 `go-webui.bat`；手动安装可运行 `python webui.py`。
3. 在推理页面测试参考音频和目标文本。若要微调，按 Finetune 流程切片、转写并校对。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:26.649Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-11 · commit](https://github.com/RVC-Boss/GPT-SoVITS/commit/6d51ffceafbf240145619af4c92408a6e54b7924)。更新 ASR 配置、Faster Whisper、FunASR 和 WebUI。

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://raw.githubusercontent.com/RVC-Boss/GPT-SoVITS/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/RVC-Boss/GPT-SoVITS)

## English

A WebUI and training toolkit for voice cloning, speech synthesis, and fine-tuning with small datasets.

It synthesizes text with a reference voice and connects audio preparation, transcription, and proofreading to training workflows.

### Features

- Support zero-shot inference and fine-tuning with small datasets.
- Support cross-language synthesis with Chinese, English, Japanese, Korean, and Cantonese.
- Integrate vocal/accompaniment separation, audio slicing, ASR, and text labeling.

### Requirements

- Choose an integrated package, manual installation, or Docker; manual setup needs compatible Python, PyTorch, and device support.
- Requires pretrained models and audio-processing dependencies, including FFmpeg as described in the installation instructions.

### Limitations

- Choose the workflow for an officially tested environment matching the model version and device.
- ASR text needs proofreading before fine-tuning; automatic slicing and transcription do not replace data checks.

### Getting started

1. Prepare the environment and models using Installation and Pretrained Models in the README.
2. Run `go-webui.bat` for the integrated package, or `python webui.py` for a manual installation.
3. Test reference audio and target text in the inference page; for fine-tuning, follow Finetune to slice, transcribe, and proofread the data.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:26.649Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-11 · commit](https://github.com/RVC-Boss/GPT-SoVITS/commit/6d51ffceafbf240145619af4c92408a6e54b7924).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://raw.githubusercontent.com/RVC-Boss/GPT-SoVITS/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/RVC-Boss/GPT-SoVITS)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:28:37.558833Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "gpt-sovits",
    "name": "GPT-SoVITS",
    "repository": "RVC-Boss/GPT-SoVITS",
    "repo_node_id": "R_kgDOLEzKcw",
    "category": "media",
    "summary": {
      "zh-CN": "提供声音克隆、语音合成和少样本微调的 WebUI 与训练工具。",
      "en": "A WebUI and training toolkit for voice cloning, speech synthesis, and fine-tuning with small datasets."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:28:37.558833Z",
        "en": "2026-11-17T14:28:37.558833Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "将文本生成为参考声音的语音，并把音频整理、转写和校对接入训练流程。",
        "en": "It synthesizes text with a reference voice and connects audio preparation, transcription, and proofreading to training workflows."
      },
      "source_url": "https://raw.githubusercontent.com/RVC-Boss/GPT-SoVITS/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/RVC-Boss/GPT-SoVITS/commit/6d51ffceafbf240145619af4c92408a6e54b7924",
        "occurred_at": "2026-11-11T16:26:17Z",
        "reviewed_at": "2026-11-17T14:28:37.558833Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "更新 ASR 配置、Faster Whisper、FunASR 和 WebUI。 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://raw.githubusercontent.com/RVC-Boss/GPT-SoVITS/main/README.md"
      },
      {
        "title": "GitHub 仓库元数据 / Repository metadata",
        "url": "https://api.github.com/repos/RVC-Boss/GPT-SoVITS"
      }
    ]
  },
  "snapshot": {
    "full_name": "RVC-Boss/GPT-SoVITS",
    "repo_node_id": "R_kgDOLEzKcw",
    "stargazers_count": 65252,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:26.649Z",
    "source_url": "https://api.github.com/repos/RVC-Boss/GPT-SoVITS"
  }
}
```

</details>
