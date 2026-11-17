# SCM（Screen Memories）

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[allenv0/SCM](https://github.com/allenv0/SCM)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 529 |
| 评估时间 / Evaluated at | 2026-11-17T15:22:59Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T15:22:59Z |

## 中文

在 Mac 本地索引图片、截图和视频。按画面描述、可见文字或对白查找素材，并跳转到匹配的视频时间位置。

适合剪辑前筛选本机素材。AI 视觉检索缩小候选范围，文字、对白和时间位置帮助复核镜头。

### 主要功能

- 「Files」按画面含义搜索图片和视频。文件名和短语匹配也参与排序。
- 「Scenes」索引视频场景。打开结果可跳转到匹配的时间位置。
- 「OCR」使用光学字符识别，匹配图片和视频帧中的文字。「Dialogue」检索 Whisper 转写的对白。
- 监视导入目录并自动处理新素材，通过内容哈希识别改名文件。常用查询可保存为标签页。

### 环境要求

- 官方安装包面向 Apple Silicon Mac，要求 macOS 12 或更新版本。
- 首次使用所选模型时需要下载权重。后续媒体分析和检索在本机运行，模型与索引占用本地存储空间。
- Homebrew 安装需遵循官方 tap 说明。当前发布包使用本地开发证书。cask 会在安装和升级时清除应用的 macOS 隔离标记。

### 使用限制

- 视频场景检索受抽样预算限制。默认 balanced 模式按每 30 秒约 1 个检索点计算预算，每个视频最多 128 点。更密的模式也有上限，可能漏掉未采样的短镜头。
- 默认语音模型 `tiny.en` 仅用于英语。中文对白需在「Speech model」中选择多语言 `tiny` 或 `base`。切换后，SCM 会在后台重新转写视频。
- README 将「LLMs」问答模式标为开发中。本次未验证该模式的稳定性和适用范围。
- 检索结果需要回看原片确认。本次未验证几百 GB 素材库的索引耗时、资源占用或检索质量。

### 开始使用

1. 阅读[官方 Homebrew tap](https://github.com/allenv0/homebrew-scm)的安装与隔离标记说明。按该页步骤安装 SCM。
2. 通过「Settings → Library → Import photos」（⌘I）导入测试素材。SCM 会下载所需模型并在后台建立索引。
3. 索引完成后，用「Files」或「Scenes」搜索素材。打开命中结果，核对画面和视频时间位置。

### 收录与来源

AI 任务用途已依据官方文档核对。2026-11-17T15:22:59Z 的快照为 529 Star，未达总量 1,000 的门槛。近 1 个日历月的 Star 净增尚未核实。用户明确指定本次正式收录，仅豁免 Star 条件。AI 任务用途与近 3 个日历月活动仍已核对。

活动记录：[2026-11-03 · commit](https://github.com/allenv0/SCM/commit/cefbce025805d0ab81dcc10e180f8722ce471d19)。调整 Dependabot 配置及公开目录保护。

本次为文档复核，未安装或运行上游项目。上述提交证明窗口内活动，不代表软件运行验证。许可不作为本次准入条件。

- [Official README](https://github.com/allenv0/SCM/blob/main/README.md)
- [Homebrew installation and quarantine handling](https://github.com/allenv0/homebrew-scm/blob/main/README.md)
- [Video sampling budgets and presets](https://github.com/allenv0/SCM/blob/main/indexer/video-budget.ts)
- [Speech model registry and default](https://github.com/allenv0/SCM/blob/main/indexer/whisper-models.ts)
- [Video search and speech settings](https://github.com/allenv0/SCM/blob/main/src/components/settings/VideoSection.tsx)
- [Library import and watched folders](https://github.com/allenv0/SCM/blob/main/src/components/LibrarySection.tsx)
- [OCR language support](https://github.com/allenv0/SCM/blob/main/indexer/ocr-lang-list.ts)

## English

Index photos, screenshots, and videos locally on a Mac. Search by visual descriptions, visible text, or dialogue, and jump to matching moments in videos.

Useful for selecting local footage before editing. AI visual search narrows the candidates, while visible text, dialogue, and timestamps help verify specific shots.

### Features

- Files mode searches photos and videos by visual meaning. Filename and phrase matches also contribute to ranking.
- Scenes mode indexes video scenes. Opening a result jumps to the matching timestamp.
- OCR (optical character recognition) mode matches text in images and video frames. Dialogue mode searches speech transcribed by Whisper.
- Watched folders import new media automatically, and content hashes identify renamed files. Frequently used queries can be saved as tabs.

### Requirements

- The official package targets Apple Silicon Macs running macOS 12 or later.
- Selected models require an initial weight download. Subsequent media analysis and search run locally, with disk space needed for models and indexes.
- Follow the official tap instructions for Homebrew installation. Current packages use a local development certificate. The cask removes the app's macOS quarantine attribute during installation and upgrades.

### Limitations

- Scene search has a sampling budget. The default balanced preset targets roughly one search point per 30 seconds, capped at 128 points per video. Denser presets also have caps and may miss short shots that are not sampled.
- The default speech model, `tiny.en`, is English-only. For Chinese dialogue, select multilingual `tiny` or `base` under Speech model. SCM then retranscribes videos in the background.
- The README marks LLMs question answering as work in progress. Its stability and supported use cases have not been verified in this review.
- Review the source footage to confirm matches. This review did not verify indexing time, resource use, or retrieval quality for a media library containing hundreds of gigabytes.

### Getting started

1. Read the [official Homebrew tap](https://github.com/allenv0/homebrew-scm) installation and quarantine-handling notes. Follow its steps to install SCM.
2. Import test media through Settings → Library → Import photos (⌘I). SCM downloads the required models and builds indexes in the background.
3. Once indexing finishes, search in Files or Scenes mode. Open matches to verify the visuals and video timestamps.

### Review and sources

The documented AI task use was reviewed. The snapshot at 2026-11-17T15:22:59Z records 529 Stars, below the total threshold of 1,000. Net Star growth over the past calendar month is unverified.

The user explicitly requested formal inclusion for this review, waiving only the Star criterion. AI task relevance and activity within the past three calendar months were still checked.

Recent activity: [2026-11-03 · commit](https://github.com/allenv0/SCM/commit/cefbce025805d0ab81dcc10e180f8722ce471d19). The commit adjusts Dependabot configuration and public-tree protection.

This is a documentation review; the upstream software was not installed or run. The cited commit establishes activity within the review window, not runtime validation. Licensing is not an admission criterion.

- [Official README](https://github.com/allenv0/SCM/blob/main/README.md)
- [Homebrew installation and quarantine handling](https://github.com/allenv0/homebrew-scm/blob/main/README.md)
- [Video sampling budgets and presets](https://github.com/allenv0/SCM/blob/main/indexer/video-budget.ts)
- [Speech model registry and default](https://github.com/allenv0/SCM/blob/main/indexer/whisper-models.ts)
- [Video search and speech settings](https://github.com/allenv0/SCM/blob/main/src/components/settings/VideoSection.tsx)
- [Library import and watched folders](https://github.com/allenv0/SCM/blob/main/src/components/LibrarySection.tsx)
- [OCR language support](https://github.com/allenv0/SCM/blob/main/indexer/ocr-lang-list.ts)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T15:22:59Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "user_directed_exception",
    "exception_id": "scm-star-2026-11-17"
  },
  "metadata": {
    "schema_version": 1,
    "id": "scm",
    "name": "SCM",
    "repository": "allenv0/SCM",
    "repo_node_id": "R_kgDOU6YAgA",
    "category": "media",
    "summary": {
      "zh-CN": "在 Mac 本地索引图片、截图和视频。按画面描述、可见文字或对白查找素材，并跳转到匹配的视频时间位置。",
      "en": "Index photos, screenshots, and videos locally on a Mac. Search by visual descriptions, visible text, or dialogue, and jump to matching moments in videos."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T15:22:59Z",
        "en": "2026-11-17T15:22:59Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "适合剪辑前筛选本机素材。AI 视觉检索缩小候选范围，文字、对白和时间位置帮助复核镜头。",
        "en": "Useful for selecting local footage before editing. AI visual search narrows the candidates, while visible text, dialogue, and timestamps help verify specific shots."
      },
      "source_url": "https://github.com/allenv0/SCM/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/allenv0/SCM/commit/cefbce025805d0ab81dcc10e180f8722ce471d19",
        "occurred_at": "2026-11-03T07:33:59Z",
        "reviewed_at": "2026-11-17T15:22:59Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "调整 Dependabot 配置及公开目录保护。 此记录用于证明窗口内活动。",
          "en": "The commit updates Dependabot configuration and guards the public tree. It establishes activity within the review window, not runtime validation."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/allenv0/SCM/blob/main/README.md"
      },
      {
        "title": "Homebrew installation and quarantine handling",
        "url": "https://github.com/allenv0/homebrew-scm/blob/main/README.md"
      },
      {
        "title": "Video sampling budgets and presets",
        "url": "https://github.com/allenv0/SCM/blob/main/indexer/video-budget.ts"
      },
      {
        "title": "Speech model registry and default",
        "url": "https://github.com/allenv0/SCM/blob/main/indexer/whisper-models.ts"
      },
      {
        "title": "Video search and speech settings",
        "url": "https://github.com/allenv0/SCM/blob/main/src/components/settings/VideoSection.tsx"
      },
      {
        "title": "Library import and watched folders",
        "url": "https://github.com/allenv0/SCM/blob/main/src/components/LibrarySection.tsx"
      },
      {
        "title": "OCR language support",
        "url": "https://github.com/allenv0/SCM/blob/main/indexer/ocr-lang-list.ts"
      }
    ]
  },
  "snapshot": {
    "full_name": "allenv0/SCM",
    "repo_node_id": "R_kgDOU6YAgA",
    "stargazers_count": 529,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T15:22:59Z",
    "source_url": "https://api.github.com/repos/allenv0/SCM"
  }
}
```

</details>
