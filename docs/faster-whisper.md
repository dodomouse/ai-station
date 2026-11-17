# faster-whisper

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 26823 |
| 评估时间 / Evaluated at | 2026-11-17T14:28:37.558977Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:26.659Z |

## 中文

基于 CTranslate2 运行 Whisper 的 Python 语音转写库。

为 AI 音频处理流程提供转写文本和时间信息，可在 CPU 或受支持的 GPU 上运行。

### 主要功能

- 提供量化推理及批量转写接口。
- 可输出逐词时间戳，并使用 VAD 过滤非语音片段。
- 通过 PyAV 解码音频，无需单独安装系统 FFmpeg。

### 环境要求

- 需要 Python 3.9 或更高版本及所选模型。
- 当前 GPU 依赖说明要求 CUDA 12 的 cuBLAS 和 cuDNN 9；其他组合须按兼容说明选择版本。

### 使用限制

- 转写返回的 segments 是惰性生成器，迭代后才实际执行。
- 速度与内存受硬件、模型、量化和解码参数影响，不能直接照搬基准结果。

### 开始使用

1. 运行 `pip install faster-whisper`，按设备准备依赖。
2. 按 Usage 示例创建 `WhisperModel`，选择 CPU INT8 或兼容的 GPU 配置。
3. 调用 `model.transcribe` 后遍历 segments，保存文本和时间信息。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:26.659Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-12 · commit](https://github.com/SYSTRAN/faster-whisper/commit/6cb639e70786aea42b9233006ae60eaf07190bdb)。调整批量转写，使未启用 VAD 时接受一个完整窗口。

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://raw.githubusercontent.com/SYSTRAN/faster-whisper/master/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/SYSTRAN/faster-whisper)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

A Python speech-transcription library that runs Whisper through CTranslate2.

It supplies transcripts and timing information to AI audio workflows on CPUs or supported GPUs.

### Features

- Provide quantized inference and batched transcription interfaces.
- Optionally return word-level timestamps and filter non-speech segments with VAD.
- Decode audio through PyAV without a separate system FFmpeg installation.

### Requirements

- Requires Python 3.9 or later and the selected model.
- Current GPU requirements specify cuBLAS for CUDA 12 and cuDNN 9; other combinations require the documented compatibility versions.

### Limitations

- The returned segments object is a lazy generator; transcription runs when it is iterated.
- Speed and memory depend on hardware, model, quantization, and decoding settings, so benchmark results do not transfer directly.

### Getting started

1. Run `pip install faster-whisper` and prepare the dependencies for your device.
2. Create a `WhisperModel` from the Usage example with CPU INT8 or a compatible GPU configuration.
3. Call `model.transcribe`, iterate over segments, and save the text and timing information.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:26.659Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-12 · commit](https://github.com/SYSTRAN/faster-whisper/commit/6cb639e70786aea42b9233006ae60eaf07190bdb).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://raw.githubusercontent.com/SYSTRAN/faster-whisper/master/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/SYSTRAN/faster-whisper)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:28:37.558977Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "faster-whisper",
    "name": "faster-whisper",
    "repository": "SYSTRAN/faster-whisper",
    "repo_node_id": "R_kgDOI8jj-Q",
    "category": "media",
    "summary": {
      "zh-CN": "基于 CTranslate2 运行 Whisper 的 Python 语音转写库。",
      "en": "A Python speech-transcription library that runs Whisper through CTranslate2."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:28:37.558977Z",
        "en": "2026-11-17T14:28:37.558977Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "为 AI 音频处理流程提供转写文本和时间信息，可在 CPU 或受支持的 GPU 上运行。",
        "en": "It supplies transcripts and timing information to AI audio workflows on CPUs or supported GPUs."
      },
      "source_url": "https://raw.githubusercontent.com/SYSTRAN/faster-whisper/master/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/SYSTRAN/faster-whisper/commit/6cb639e70786aea42b9233006ae60eaf07190bdb",
        "occurred_at": "2026-11-12T09:05:55Z",
        "reviewed_at": "2026-11-17T14:28:37.558977Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "调整批量转写，使未启用 VAD 时接受一个完整窗口。 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://raw.githubusercontent.com/SYSTRAN/faster-whisper/master/README.md"
      },
      {
        "title": "GitHub 仓库元数据 / Repository metadata",
        "url": "https://api.github.com/repos/SYSTRAN/faster-whisper"
      }
    ]
  },
  "snapshot": {
    "full_name": "SYSTRAN/faster-whisper",
    "repo_node_id": "R_kgDOI8jj-Q",
    "stargazers_count": 26823,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:26.659Z",
    "source_url": "https://api.github.com/repos/SYSTRAN/faster-whisper"
  }
}
```

</details>
