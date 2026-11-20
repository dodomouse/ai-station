# LivePortrait

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[KlingAIResearch/LivePortrait](https://github.com/KlingAIResearch/LivePortrait)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 19514 |
| 评估时间 / Evaluated at | 2026-11-17T14:28:37.558293Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:26.140Z |

## 中文

用驱动视频或运动模板为人物及动物肖像生成动画。

将静态肖像或人物视频与参考运动结合，生成可继续剪辑的视频素材。

### 主要功能

- 支持图像或视频作为人物输入。
- 支持驱动视频裁剪和运动模板复用。
- 提供命令行推理和 Gradio 界面，并包含动物模式。

### 环境要求

- 需要 Git、Conda、FFmpeg 和预训练权重。
- 官方环境使用 Python 3.10；Linux/Windows 与 Apple Silicon 使用不同依赖文件。

### 使用限制

- macOS 不支持动物模式，因为其 X-Pose 依赖不支持 macOS；Intel Mac 未获验证。
- 驱动视频应聚焦头部，并以正脸、中性表情开头；裁剪质量会影响结果。

### 开始使用

1. 按 README 创建环境，并安装对应系统的 requirements 文件。
2. 按 Download pretrained weights 部分准备权重。
3. Linux/Windows 可运行 `python inference.py`；Apple Silicon 按 README 添加 MPS 回退设置，再用 `-s`、`-d` 指定自己的输入。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:26.140Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-10-23 · pr](https://github.com/KlingAIResearch/LivePortrait/pull/577)。新建 PR，建议以 float32 计算 channels_first LayerNorm 统计量；作为 PR 活动记录，不据此声称已合并。

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://raw.githubusercontent.com/KlingAIResearch/LivePortrait/main/readme.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/KlingAIResearch/LivePortrait)

## English

Animate human and animal portraits using driving video or motion templates.

It combines a still portrait or source video with reference motion to generate footage for further editing.

### Features

- Accept images or videos as human source inputs.
- Support driving-video cropping and reusable motion templates.
- Provide command-line inference, a Gradio interface, and an animal mode.

### Requirements

- Requires Git, Conda, FFmpeg, and pretrained weights.
- The official environment uses Python 3.10; Linux/Windows and Apple Silicon use different dependency files.

### Limitations

- Animal mode is unavailable on macOS because X-Pose does not support it; Intel Macs are not verified.
- Driving videos should focus on the head and begin with a frontal, neutral expression; cropping quality affects the result.

### Getting started

1. Create the environment and install the requirements file for your operating system using the README.
2. Download the weights following the Download pretrained weights section.
3. On Linux/Windows, run `python inference.py`; on Apple Silicon, apply the README's MPS fallback setting, then use `-s` and `-d` for your own inputs.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:26.140Z meets the total-Star threshold of 1,000.

Recent activity: [2026-10-23 · pr](https://github.com/KlingAIResearch/LivePortrait/pull/577).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://raw.githubusercontent.com/KlingAIResearch/LivePortrait/main/readme.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/KlingAIResearch/LivePortrait)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:28:37.558293Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "liveportrait",
    "name": "LivePortrait",
    "repository": "KlingAIResearch/LivePortrait",
    "repo_node_id": "R_kgDOMRlcpg",
    "category": "media",
    "summary": {
      "zh-CN": "用驱动视频或运动模板为人物及动物肖像生成动画。",
      "en": "Animate human and animal portraits using driving video or motion templates."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:28:37.558293Z",
        "en": "2026-11-17T14:28:37.558293Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "将静态肖像或人物视频与参考运动结合，生成可继续剪辑的视频素材。",
        "en": "It combines a still portrait or source video with reference motion to generate footage for further editing."
      },
      "source_url": "https://raw.githubusercontent.com/KlingAIResearch/LivePortrait/main/readme.md"
    },
    "activity_evidence": [
      {
        "type": "pr",
        "url": "https://github.com/KlingAIResearch/LivePortrait/pull/577",
        "occurred_at": "2026-10-23T21:00:33Z",
        "reviewed_at": "2026-11-17T14:28:37.558293Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "新建 PR，建议以 float32 计算 channels_first LayerNorm 统计量；作为 PR 活动记录，不据此声称已合并。 此记录用于证明窗口内活动。",
          "en": "The recorded pr establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://raw.githubusercontent.com/KlingAIResearch/LivePortrait/main/readme.md"
      },
      {
        "title": "GitHub 仓库元数据 / Repository metadata",
        "url": "https://api.github.com/repos/KlingAIResearch/LivePortrait"
      }
    ]
  },
  "snapshot": {
    "full_name": "KlingAIResearch/LivePortrait",
    "repo_node_id": "R_kgDOMRlcpg",
    "stargazers_count": 19514,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:26.140Z",
    "source_url": "https://api.github.com/repos/KlingAIResearch/LivePortrait"
  }
}
```

</details>
