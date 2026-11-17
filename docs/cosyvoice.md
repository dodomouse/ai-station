# CosyVoice

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[QwenAudio/CosyVoice](https://github.com/QwenAudio/CosyVoice)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 24432 |
| 评估时间 / Evaluated at | 2026-11-17T14:28:37.558757Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:25.984Z |

## 中文

支持声音克隆、跨语言合成和流式输出的语音生成工具。

把 AI 生成的文本转换为指定声音的语音，并通过指令调节语言、情感或语速。

### 主要功能

- 支持跨语言零样本声音克隆。
- 支持文本流式输入和音频流式输出。
- 提供指令控制、发音修正，以及 Python 和 WebUI 入口。

### 环境要求

- 官方环境使用 Conda 与 Python 3.10，并需仓库子模块和依赖。
- 需要下载对应模型及文本处理资源；部分环境还需处理 SoX 依赖。

### 使用限制

- 不同代际模型和推理模式的能力不同，应使用对应示例。
- 可选 vLLM 加速有特定版本与硬件要求，不能直接套用任意 vLLM 环境。

### 开始使用

1. 按 Clone and install 准备仓库、子模块和 Conda 环境。
2. 按 Model download 下载选定模型及所需资源。
3. 阅读 `example.py` 中对应模型的调用后运行 `python example.py`，或按 Start web demo 启动界面。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:25.984Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-03 · issue](https://github.com/QwenAudio/CosyVoice/issues/1964)。新建 Fun-CosyVoice3 使用条款澄清 issue；作为 issue 活动记录，不代表代码修复或许可判定。

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://raw.githubusercontent.com/QwenAudio/CosyVoice/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/QwenAudio/CosyVoice)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

A speech-generation toolkit supporting voice cloning, cross-language synthesis, and streaming output.

It converts AI-generated text into speech with a selected voice and uses instructions to control language, emotion, or speaking speed.

### Features

- Support zero-shot voice cloning across languages.
- Support streaming text input and streaming audio output.
- Provide instruction controls, pronunciation editing, and Python and WebUI entry points.

### Requirements

- The official environment uses Conda and Python 3.10, with repository submodules and dependencies.
- Requires the selected model and text-processing resources; some environments also need SoX dependency setup.

### Limitations

- Capabilities differ between model generations and inference modes; use the matching example.
- Optional vLLM acceleration has specific version and hardware requirements and cannot use an arbitrary vLLM environment.

### Getting started

1. Prepare the repository, submodules, and Conda environment using Clone and install.
2. Download the selected model and required resources using Model download.
3. Review the matching model calls in `example.py`, then run `python example.py`, or launch the interface through Start web demo.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:25.984Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-03 · issue](https://github.com/QwenAudio/CosyVoice/issues/1964).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://raw.githubusercontent.com/QwenAudio/CosyVoice/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/QwenAudio/CosyVoice)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:28:37.558757Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "cosyvoice",
    "name": "CosyVoice",
    "repository": "QwenAudio/CosyVoice",
    "repo_node_id": "R_kgDOMRSMsg",
    "category": "media",
    "summary": {
      "zh-CN": "支持声音克隆、跨语言合成和流式输出的语音生成工具。",
      "en": "A speech-generation toolkit supporting voice cloning, cross-language synthesis, and streaming output."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:28:37.558757Z",
        "en": "2026-11-17T14:28:37.558757Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "把 AI 生成的文本转换为指定声音的语音，并通过指令调节语言、情感或语速。",
        "en": "It converts AI-generated text into speech with a selected voice and uses instructions to control language, emotion, or speaking speed."
      },
      "source_url": "https://raw.githubusercontent.com/QwenAudio/CosyVoice/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "issue",
        "url": "https://github.com/QwenAudio/CosyVoice/issues/1964",
        "occurred_at": "2026-11-03T15:43:42Z",
        "reviewed_at": "2026-11-17T14:28:37.558757Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "新建 Fun-CosyVoice3 使用条款澄清 issue；作为 issue 活动记录，不代表代码修复或许可判定。 此记录用于证明窗口内活动。",
          "en": "The recorded issue establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://raw.githubusercontent.com/QwenAudio/CosyVoice/main/README.md"
      },
      {
        "title": "GitHub 仓库元数据 / Repository metadata",
        "url": "https://api.github.com/repos/QwenAudio/CosyVoice"
      }
    ]
  },
  "snapshot": {
    "full_name": "QwenAudio/CosyVoice",
    "repo_node_id": "R_kgDOMRSMsg",
    "stargazers_count": 24432,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:25.984Z",
    "source_url": "https://api.github.com/repos/QwenAudio/CosyVoice"
  }
}
```

</details>
