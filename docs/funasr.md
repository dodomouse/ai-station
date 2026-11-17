# FunASR

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[modelscope/FunASR](https://github.com/modelscope/FunASR)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 21058 |
| 评估时间 / Evaluated at | 2026-11-17T14:28:37.558681Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:26.700Z |

## 中文

集成语音识别、语音检测、标点和说话人处理的音频工具集。

将音频转换成文本、字幕或结构化结果，让智能体读取和处理语音资料。

### 主要功能

- 组合离线或流式识别模型，以及 VAD、标点和说话人模块。
- 提供 Python AutoModel 调用接口。
- CLI 可输出 JSON、SRT，并处理批量音频。

### 环境要求

- 需要 Python 3.8 或更高版本，先安装 PyTorch 和 torchaudio。
- GPU 使用需安装匹配驱动的 PyTorch，并确认设备可用。

### 使用限制

- 语言、流式处理、时间戳和说话人能力随模型及调用方式变化。
- 需要下载对应模型，不能把某一模型的功能视为全部模型共有。

### 开始使用

1. 按 README 安装 PyTorch、torchaudio，再运行 `pip install funasr`。
2. 运行 `funasr audio.wav --output-format json`，检查识别结果。
3. 按 Usage 和模型列表选择语言及模型，再启用字幕、时间戳或批处理。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:26.700Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/modelscope/FunASR/commit/e227484d98ca90aa829a0ae180731c9ee2e87e77)。提交 FunASR 1.4.27 发行更新。

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://raw.githubusercontent.com/modelscope/FunASR/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/modelscope/FunASR)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

An audio toolkit combining speech recognition, voice activity detection, punctuation, and speaker processing.

It converts audio into text, subtitles, or structured results that agents can read and process.

### Features

- Compose offline or streaming recognition models with VAD, punctuation, and speaker modules.
- Provide the Python AutoModel interface.
- The CLI outputs JSON or SRT and processes batches of audio.

### Requirements

- Requires Python 3.8 or later, with PyTorch and torchaudio installed first.
- GPU use requires a driver-compatible PyTorch installation and an available device.

### Limitations

- Language support, streaming, timestamps, and speaker features vary by model and calling route.
- The matching models must be downloaded; a feature of one model is not shared by every model.

### Getting started

1. Install PyTorch and torchaudio as described in the README, then run `pip install funasr`.
2. Run `funasr audio.wav --output-format json` and inspect the transcript.
3. Use the Usage section and model list to select a language and model, then enable subtitles, timestamps, or batch processing.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:26.700Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/modelscope/FunASR/commit/e227484d98ca90aa829a0ae180731c9ee2e87e77).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://raw.githubusercontent.com/modelscope/FunASR/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/modelscope/FunASR)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:28:37.558681Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "funasr",
    "name": "FunASR",
    "repository": "modelscope/FunASR",
    "repo_node_id": "R_kgDOIfjisw",
    "category": "media",
    "summary": {
      "zh-CN": "集成语音识别、语音检测、标点和说话人处理的音频工具集。",
      "en": "An audio toolkit combining speech recognition, voice activity detection, punctuation, and speaker processing."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:28:37.558681Z",
        "en": "2026-11-17T14:28:37.558681Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "将音频转换成文本、字幕或结构化结果，让智能体读取和处理语音资料。",
        "en": "It converts audio into text, subtitles, or structured results that agents can read and process."
      },
      "source_url": "https://raw.githubusercontent.com/modelscope/FunASR/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/modelscope/FunASR/commit/e227484d98ca90aa829a0ae180731c9ee2e87e77",
        "occurred_at": "2026-11-17T05:33:29Z",
        "reviewed_at": "2026-11-17T14:28:37.558681Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "提交 FunASR 1.4.27 发行更新。 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://raw.githubusercontent.com/modelscope/FunASR/main/README.md"
      },
      {
        "title": "GitHub 仓库元数据 / Repository metadata",
        "url": "https://api.github.com/repos/modelscope/FunASR"
      }
    ]
  },
  "snapshot": {
    "full_name": "modelscope/FunASR",
    "repo_node_id": "R_kgDOIfjisw",
    "stargazers_count": 21058,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:26.700Z",
    "source_url": "https://api.github.com/repos/modelscope/FunASR"
  }
}
```

</details>
