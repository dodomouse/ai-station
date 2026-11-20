# Fish Speech

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[fishaudio/fish-speech](https://github.com/fishaudio/fish-speech)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 33764 |
| 评估时间 / Evaluated at | 2026-11-17T14:28:37.558521Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:26.043Z |

## 中文

提供多角色语音生成、声音克隆和语音编辑的模型与推理工具。

把文本脚本转换为配音；Drama 3 还可按指令修改已有片段，支持音频制作中的反复调整。

### 主要功能

- 支持多说话人及跨语言声音克隆。
- 使用自然语言标签控制情感和表达。
- Drama 3 支持局部编辑和多轮修改，并提供 CLI、API 与 WebUI。

### 环境要求

- 官方安装面向 Linux/WSL，使用 Python 3.12，并需音频依赖和模型权重。
- Drama 3 需要 NVIDIA GPU；S2-Pro 的可用设备范围更广，按安装页选择后端。

### 使用限制

- Drama 3 不支持 CPU、Apple MPS 或 AMD ROCm；不能按 S2-Pro 的设备支持推断。
- S2-Pro 不提供 Drama 3 的局部编辑和多轮修改能力。

### 开始使用

1. 按[官方安装页](https://speech.fish.audio/install/)选择模型、设备与安装方式。
2. 下载对应权重，按官方路径放入 `checkpoints`。
3. 使用安装页的 Docker Compose 或推理流程启动服务，再打开 WebUI 测试文本与参考音频。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:26.043Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-10-29 · commit](https://github.com/fishaudio/fish-speech/commit/0f8a12e8a651062fdee9c33a894bdccd3a8513f1)。提交 Drama 3 的小幅更新。

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://raw.githubusercontent.com/fishaudio/fish-speech/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/fishaudio/fish-speech)
- [官方安装与设备说明 / Official installation and device requirements](https://speech.fish.audio/install/)

## English

Models and inference tools for speech with multiple characters, voice cloning, and audio editing.

It turns text scripts into spoken audio; Drama 3 also supports instruction-based revisions to existing passages for iterative audio production.

### Features

- Support multiple speakers and cross-language voice cloning.
- Control emotion and delivery with natural-language tags.
- Drama 3 supports local edits and multiple revision turns, with CLI, API, and WebUI access.

### Requirements

- The official installation targets Linux/WSL with Python 3.12, audio dependencies, and model weights.
- Drama 3 requires an NVIDIA GPU; S2-Pro supports more device options, selected through the installation guide.

### Limitations

- Drama 3 does not support CPU, Apple MPS, or AMD ROCm; S2-Pro device support does not carry over.
- S2-Pro does not provide Drama 3's local editing or multiple revision turns.

### Getting started

1. Choose a model, device, and installation route using the [official installation page](https://speech.fish.audio/install/).
2. Download the matching weights into the documented `checkpoints` paths.
3. Start the service through the documented Docker Compose or inference flow, then open the WebUI to test text and reference audio.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:26.043Z meets the total-Star threshold of 1,000.

Recent activity: [2026-10-29 · commit](https://github.com/fishaudio/fish-speech/commit/0f8a12e8a651062fdee9c33a894bdccd3a8513f1).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://raw.githubusercontent.com/fishaudio/fish-speech/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/fishaudio/fish-speech)
- [官方安装与设备说明 / Official installation and device requirements](https://speech.fish.audio/install/)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:28:37.558521Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "fish-speech",
    "name": "Fish Speech",
    "repository": "fishaudio/fish-speech",
    "repo_node_id": "R_kgDOKePR1A",
    "category": "media",
    "summary": {
      "zh-CN": "提供多角色语音生成、声音克隆和语音编辑的模型与推理工具。",
      "en": "Models and inference tools for speech with multiple characters, voice cloning, and audio editing."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:28:37.558521Z",
        "en": "2026-11-17T14:28:37.558521Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "把文本脚本转换为配音；Drama 3 还可按指令修改已有片段，支持音频制作中的反复调整。",
        "en": "It turns text scripts into spoken audio; Drama 3 also supports instruction-based revisions to existing passages for iterative audio production."
      },
      "source_url": "https://raw.githubusercontent.com/fishaudio/fish-speech/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/fishaudio/fish-speech/commit/0f8a12e8a651062fdee9c33a894bdccd3a8513f1",
        "occurred_at": "2026-10-29T17:05:07Z",
        "reviewed_at": "2026-11-17T14:28:37.558521Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "提交 Drama 3 的小幅更新。 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://raw.githubusercontent.com/fishaudio/fish-speech/main/README.md"
      },
      {
        "title": "GitHub 仓库元数据 / Repository metadata",
        "url": "https://api.github.com/repos/fishaudio/fish-speech"
      },
      {
        "title": "官方安装与设备说明 / Official installation and device requirements",
        "url": "https://speech.fish.audio/install/"
      }
    ]
  },
  "snapshot": {
    "full_name": "fishaudio/fish-speech",
    "repo_node_id": "R_kgDOKePR1A",
    "stargazers_count": 33764,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:26.043Z",
    "source_url": "https://api.github.com/repos/fishaudio/fish-speech"
  }
}
```

</details>
