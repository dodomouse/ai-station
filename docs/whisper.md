# Whisper

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[openai/whisper](https://github.com/openai/whisper)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 112864 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T03:59:14.755230+00:00 |

## 中文

将音频转写为文本的多语言语音识别模型与工具，支持语言检测和将语音翻译为英语。

### 用途与功能

- 通过 CLI 或 Python 接口转写音频文件。
- 提供多种模型尺寸及部分英语专用版本。
- 支持语言检测，以及多语言模型的英语翻译任务。

### 环境与限制

需要 Python、PyTorch、ffmpeg 和模型权重；显存需求因模型而异。turbo 未针对翻译训练，应按任务选择模型。识别质量随语言、录音和背景噪声变化。官方 README 明确代码与官方模型权重均采用 MIT。

### 开始使用

按 README 安装 openai-whisper 与 ffmpeg，使用 `whisper audio.wav --model turbo` 转写，或通过 Python 的 load_model 与 transcribe 接口调用。

参阅[官方 README](https://github.com/openai/whisper/blob/86098128c0b4f24f0e2aa2994de830614b474227/README.md)。

### 收录与来源

适合需要可本地运行的音频转写流程，以及在应用中直接调用语音识别模型。

维护证据：[修复英语数字归一化，仅将独立的 1 改为 one，保留金额、百分比和小数中的数字](https://github.com/openai/whisper/commit/86098128c0b4f24f0e2aa2994de830614b474227)（2026-08-31）。

发现于 [GitHub 月榜](https://github.com/trending/python?since=monthly&spoken_language_code=en)。2026-11-17 的榜单记录新增 2,465 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

A multilingual speech-recognition model and toolkit for transcription, language detection and speech translation into English.

### Uses and features

- Transcribe audio files through the CLI or Python API.
- Offer multiple model sizes and selected English-only variants.
- Support language detection and translation into English with multilingual models.

### Requirements and limits

Requires Python, PyTorch, ffmpeg and model weights; memory requirements vary by model. turbo is not trained for translation, so choose the model for the task. Quality varies by language, recording and background noise. The official README explicitly places code and official model weights under MIT.

### Getting started

Install openai-whisper and ffmpeg following the README, transcribe with `whisper audio.wav --model turbo`, or use Python load_model and transcribe.

See the [official README](https://github.com/openai/whisper/blob/86098128c0b4f24f0e2aa2994de830614b474227/README.md).

### Review and provenance

Useful for local audio-transcription workflows and applications calling speech-recognition models directly.

Maintenance evidence: [Fixes English number normalization to spell out only standalone 1 while preserving currency, percentages and decimals](https://github.com/openai/whisper/commit/86098128c0b4f24f0e2aa2994de830614b474227) (2026-08-31).

Discovered in [GitHub monthly Trending](https://github.com/trending/python?since=monthly&spoken_language_code=en), which recorded 2,465 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T03:59:14.755230+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "whisper",
    "name": "Whisper",
    "repository": "openai/whisper",
    "repo_node_id": "R_kgDOIAstBQ",
    "category": "media",
    "summary": {
      "zh-CN": "将音频转写为文本的多语言语音识别模型与工具，支持语言检测和将语音翻译为英语。",
      "en": "A multilingual speech-recognition model and toolkit for transcription, language detection and speech translation into English."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T03:59:14.755230+00:00",
        "en": "2026-11-17T03:59:14.755230+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合需要可本地运行的音频转写流程，以及在应用中直接调用语音识别模型。",
      "en": "Useful for local audio-transcription workflows and applications calling speech-recognition models directly.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/openai/whisper/blob/86098128c0b4f24f0e2aa2994de830614b474227/LICENSE",
      "license_sha256": "b5d65a59060e68c4ff940e1eddfa6f94b2d68fdf58ed7f4dd57721c997e35e9d",
      "source_commit": "86098128c0b4f24f0e2aa2994de830614b474227",
      "reviewed_at": "2026-11-17T03:59:14.755230+00:00",
      "evidence_pinned_at": "2026-11-17T03:59:14.755230+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "The official README states that Whisper code and official model weights are MIT licensed. Input audio, third-party adaptations and datasets are not automatically covered."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-08-31T17:19:19Z",
        "reviewed_at": "2026-11-17T03:59:14.755230+00:00",
        "url": "https://github.com/openai/whisper/commit/86098128c0b4f24f0e2aa2994de830614b474227",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复英语数字归一化，仅将独立的 1 改为 one，保留金额、百分比和小数中的数字",
          "en": "Fixes English number normalization to spell out only standalone 1 while preserving currency, percentages and decimals"
        },
        "reviewed_files": [
          "whisper/normalizers/english.py"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/openai/whisper",
        "accessed_at": "2026-11-17T03:59:14.755230+00:00"
      },
      {
        "url": "https://github.com/openai/whisper/blob/86098128c0b4f24f0e2aa2994de830614b474227/README.md",
        "accessed_at": "2026-11-17T03:59:14.755230+00:00"
      },
      {
        "url": "https://github.com/openai/whisper/blob/86098128c0b4f24f0e2aa2994de830614b474227/LICENSE",
        "accessed_at": "2026-11-17T03:59:14.755230+00:00"
      },
      {
        "url": "https://github.com/openai/whisper/commit/86098128c0b4f24f0e2aa2994de830614b474227",
        "accessed_at": "2026-11-17T03:59:14.755230+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 2465,
      "source_url": "https://github.com/trending/python?since=monthly&spoken_language_code=en",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOIAstBQ",
    "full_name": "openai/whisper",
    "stargazers_count": 112864,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "b5d65a59060e68c4ff940e1eddfa6f94b2d68fdf58ed7f4dd57721c997e35e9d",
    "last_success_at": "2026-11-17T03:53:51.462717+00:00"
  }
}
```

</details>
