# WhisperX

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[m-bain/whisperX](https://github.com/m-bain/whisperX)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 25405 |
| 评估时间 / Evaluated at | 2026-11-17T14:28:37.558600Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:25.936Z |

## 中文

在 Whisper 转写基础上增加逐词时间戳、对齐和说话人区分。

将录音转换为带时间和说话人信息的文本，供字幕、检索或后续 AI 分析使用。

### 主要功能

- 批量转写音频，并通过 VAD 切分语音。
- 使用语言相关的对齐模型生成逐词时间戳。
- 可加入说话人区分，并导出字幕。

### 环境要求

- 需要 Python；GPU 安装说明要求 CUDA 12.8，CPU 使用可跳过 CUDA。
- 说话人区分需访问相应 Hugging Face 模型，并完成该模型的访问设置。

### 使用限制

- 重叠语音和说话人区分仍可能出错。
- 对齐模型词典之外的字符可能没有词级时间戳；语言还需对应对齐模型。

### 开始使用

1. 按 README 准备 CPU 或 GPU 环境，运行 `pip install whisperx`。
2. 运行 `whisperx path/to/audio.wav`，检查转写和字幕时间。
3. 若要加入说话人信息，按 Speaker Diarization 部分配置模型访问并启用区分功能。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:25.936Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-12 · commit](https://github.com/m-bain/whisperX/commit/b904f02b7e1f26fd10fb04840d655ff27e88e464)。合并 Ascend NPU 设备支持的 PR。

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://raw.githubusercontent.com/m-bain/whisperX/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/m-bain/whisperX)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

Add word-level timestamps, alignment, and speaker diarization to Whisper transcription.

It turns recordings into text with timing and speaker information for subtitles, retrieval, or further AI analysis.

### Features

- Transcribe audio in batches and segment speech using VAD.
- Generate word-level timestamps with language-specific alignment models.
- Optionally add speaker diarization and export subtitles.

### Requirements

- Requires Python; the GPU setup specifies CUDA 12.8, while CPU use can skip CUDA.
- Speaker diarization requires access to the relevant Hugging Face model and completion of its access setup.

### Limitations

- Overlapping speech and speaker assignments can still be incorrect.
- Characters outside the alignment model's dictionary may lack word timings; each language also needs an appropriate alignment model.

### Getting started

1. Prepare a CPU or GPU environment from the README and run `pip install whisperx`.
2. Run `whisperx path/to/audio.wav` and check the transcript and subtitle timings.
3. For speaker labels, configure model access and enable diarization using the Speaker Diarization section.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:25.936Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-12 · commit](https://github.com/m-bain/whisperX/commit/b904f02b7e1f26fd10fb04840d655ff27e88e464).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://raw.githubusercontent.com/m-bain/whisperX/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/m-bain/whisperX)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:28:37.558600Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "whisperx",
    "name": "WhisperX",
    "repository": "m-bain/whisperX",
    "repo_node_id": "R_kgDOIlaj4w",
    "category": "media",
    "summary": {
      "zh-CN": "在 Whisper 转写基础上增加逐词时间戳、对齐和说话人区分。",
      "en": "Add word-level timestamps, alignment, and speaker diarization to Whisper transcription."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:28:37.558600Z",
        "en": "2026-11-17T14:28:37.558600Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "将录音转换为带时间和说话人信息的文本，供字幕、检索或后续 AI 分析使用。",
        "en": "It turns recordings into text with timing and speaker information for subtitles, retrieval, or further AI analysis."
      },
      "source_url": "https://raw.githubusercontent.com/m-bain/whisperX/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/m-bain/whisperX/commit/b904f02b7e1f26fd10fb04840d655ff27e88e464",
        "occurred_at": "2026-11-12T17:34:05Z",
        "reviewed_at": "2026-11-17T14:28:37.558600Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "合并 Ascend NPU 设备支持的 PR。 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://raw.githubusercontent.com/m-bain/whisperX/main/README.md"
      },
      {
        "title": "GitHub 仓库元数据 / Repository metadata",
        "url": "https://api.github.com/repos/m-bain/whisperX"
      }
    ]
  },
  "snapshot": {
    "full_name": "m-bain/whisperX",
    "repo_node_id": "R_kgDOIlaj4w",
    "stargazers_count": 25405,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:25.936Z",
    "source_url": "https://api.github.com/repos/m-bain/whisperX"
  }
}
```

</details>
