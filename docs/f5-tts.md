# F5-TTS

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[SWivid/F5-TTS](https://github.com/SWivid/F5-TTS)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 15607 |
| 评估时间 / Evaluated at | 2026-11-17T14:28:37.558905Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:25.889Z |

## 中文

通过参考音频生成语音，提供命令行、Gradio 界面和微调工具。

将文本转成参考声音的朗读，并支持多说话人或多风格语音制作。

### 主要功能

- 提供分块 TTS 推理。
- 支持多风格、多说话人生成和语音聊天示例。
- 提供 CLI、Gradio 和训练或微调入口。

### 环境要求

- 需要 Python 3.10 或更高版本，以及 FFmpeg。
- 先安装适配设备的 PyTorch；推理还需要模型和参考音频。

### 使用限制

- 参考音频需配套转写文本；留空时会调用 ASR，增加 GPU 内存使用。
- 训练与微调应按源码安装流程准备，不能只依据推理包步骤。

### 开始使用

1. 按 Installation 准备 Python、FFmpeg 和 PyTorch，再运行 `pip install f5-tts`。
2. 运行 `f5-tts_infer-gradio` 打开界面。
3. 提供参考音频、对应文本和待生成文本，检查输出。批处理可改用 README 的 CLI 示例。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:25.889Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-03 · commit](https://github.com/SWivid/F5-TTS/commit/600e5fdfbf319f84735557aca80a7aaf60d487e6)。修复 torch、torchaudio 与 torchcodec 不兼容问题。

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://raw.githubusercontent.com/SWivid/F5-TTS/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/SWivid/F5-TTS)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

Generate speech from reference audio using command-line tools, a Gradio interface, and fine-tuning utilities.

It turns text into speech with a reference voice and supports production with multiple speakers or styles.

### Features

- Provide chunked TTS inference.
- Support generation with multiple styles or speakers and a voice-chat example.
- Provide CLI, Gradio, and training or fine-tuning entry points.

### Requirements

- Requires Python 3.10 or later and FFmpeg.
- Install device-compatible PyTorch first; inference also needs a model and reference audio.

### Limitations

- Reference audio needs its transcript; leaving it empty invokes ASR and adds GPU memory usage.
- Training and fine-tuning require the source-installation workflow rather than only the inference-package steps.

### Getting started

1. Prepare Python, FFmpeg, and PyTorch using Installation, then run `pip install f5-tts`.
2. Run `f5-tts_infer-gradio` to open the interface.
3. Supply reference audio, its transcript, and the text to generate, then inspect the output; use the README's CLI example for scripted processing.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:25.889Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-03 · commit](https://github.com/SWivid/F5-TTS/commit/600e5fdfbf319f84735557aca80a7aaf60d487e6).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://raw.githubusercontent.com/SWivid/F5-TTS/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/SWivid/F5-TTS)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:28:37.558905Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "f5-tts",
    "name": "F5-TTS",
    "repository": "SWivid/F5-TTS",
    "repo_node_id": "R_kgDOM9RF8g",
    "category": "media",
    "summary": {
      "zh-CN": "通过参考音频生成语音，提供命令行、Gradio 界面和微调工具。",
      "en": "Generate speech from reference audio using command-line tools, a Gradio interface, and fine-tuning utilities."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:28:37.558905Z",
        "en": "2026-11-17T14:28:37.558905Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "将文本转成参考声音的朗读，并支持多说话人或多风格语音制作。",
        "en": "It turns text into speech with a reference voice and supports production with multiple speakers or styles."
      },
      "source_url": "https://raw.githubusercontent.com/SWivid/F5-TTS/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/SWivid/F5-TTS/commit/600e5fdfbf319f84735557aca80a7aaf60d487e6",
        "occurred_at": "2026-11-03T15:05:09Z",
        "reviewed_at": "2026-11-17T14:28:37.558905Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复 torch、torchaudio 与 torchcodec 不兼容问题。 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://raw.githubusercontent.com/SWivid/F5-TTS/main/README.md"
      },
      {
        "title": "GitHub 仓库元数据 / Repository metadata",
        "url": "https://api.github.com/repos/SWivid/F5-TTS"
      }
    ]
  },
  "snapshot": {
    "full_name": "SWivid/F5-TTS",
    "repo_node_id": "R_kgDOM9RF8g",
    "stargazers_count": 15607,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:25.889Z",
    "source_url": "https://api.github.com/repos/SWivid/F5-TTS"
  }
}
```

</details>
