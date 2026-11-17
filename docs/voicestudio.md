# VoiceStudio

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 110994 |
| 许可证 / License | AGPL-3.0 |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T11:46:23.015Z |

以上为历史核对结果，使用前请复核上游状态。 / This is a dated review; check the current upstream state before use.

## 中文

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

### 原始中文记录（历史快照）

### 009 VoiceStudio

仓库：[debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio)

#### 1. 简介

在本地运行语音克隆、声音设计、转录和视频配音。另提供听写、有声书、批量任务及本地 API 与 MCP 接口。

#### 2. 适用场景

把文字转成语音或有声书。本地语音转录与听写。翻译并重新配音视频。

#### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 参考声音克隆 | 用清晰参考录音生成相近音色的语音。效果依赖参考质量和所选引擎。 | What you can do / Get started |
| 文字设计音色 | 用文字描述声音特征，在声音设计工作区生成声音。 | What you can do |
| 视频翻译与配音 | 为视频翻译并生成配音，使语音时序匹配原视频。提供多说话人配音等相关指南。 | What you can do / Documentation |
| 听写与转录 | 提供浮动听写组件和本地转录，将语音内容转为文字。 | What you can do |
| 旁白、有声书与队列 | 支持故事、有声书和批量排队任务，适合重复生成语音。 | What you can do |
| 本地模型管理 | 按需选择引擎并下载所需模型，下载前询问用户。可使用 CPU，硬件加速按引擎和平台变化。 | What you can do / Platforms / Get started |
| 自动化接入 | 提供本地 API、MCP、可复用配方及监控文件夹，供其他流程调用语音能力。 | What you can do / Documentation |

官方来源入口：[官方 README](https://github.com/debpalash/VoiceStudio/blob/main/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

**平台与环境**

- macOS 13.3+ Apple Silicon 为稳定本地路径；Intel Mac UI 需连接远程后端，标为 Limited
- Windows 10/11 x64；Windows ARM 为实验性
- Linux 与 Docker
- Android 10+、iOS/iPadOS 17+ 为 Preview，模型下载后可本地离线运行

- 应用为 AGPL-3.0。模型权重、声音与生成输出各有许可，不能用应用开源推断所有音色都可自由商用。本地生成消耗本机算力、存储和电力，CPU/GPU 成本自理。

- 语言覆盖与功能随所选引擎而变，不沿用宣传中的语言总数。
- 克隆声音需所有者许可，清晰参考录音不等于保证完美复刻。
- 本地运行路径依平台而变；Intel Mac、Windows ARM 和手机版本需注意上述状态。
- 本轮没有验证生成质量、翻译准确率或设备速度。

**容易找错的需求（不属于本项目能力）**

- 不能据此满足“无参考、百分之百复刻任意人的声音”。
- 不能承诺给视频人物自动改口型；README 的配音时序对齐不等同唇形重建。

#### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/debpalash/VoiceStudio/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- 桌面工作区与浮动听写组件
- 本地 API
- MCP
- 配方、队列及监控文件夹

#### 6. 替代选择

- [threerocks/sweety-handdraw-video](sweety-handdraw-video.md#中文)：本项目提供语音克隆、转录和配音；后者围绕手绘视频组织口播、画面和声音对齐。后者只覆盖部分制作需求。

#### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/debpalash/VoiceStudio/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/009_debpalash-VoiceStudio.md`。

## English

Voice software for cloning, speech design, transcription and dubbing, with batch processing and agent interfaces.

### Use cases

- Prepare narrated audio
- Transcribe recordings and create dubbing workflows

### Requirements and limits

Platform maturity varies: Intel Mac needs a remote backend, Windows ARM is experimental and mobile paths are previews in the source card. Models and voices have separate terms. Cloning requires permission, language coverage depends on the engine, and timing alignment does not imply lip reconstruction. Quality and speed were not tested.

### Getting started

Read the [official documentation](https://github.com/debpalash/VoiceStudio/blob/main/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [Sweety Handdraw Video](sweety-handdraw-video.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:13.877Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

保留原始核对数据，便于追溯来源、许可和维护证据。 / Original review data preserves source, license and maintenance evidence.

```json
{
  "evaluated_at": "2026-11-15T11:54:08.129868Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "voicestudio",
    "name": "VoiceStudio",
    "repository": "debpalash/VoiceStudio",
    "repo_node_id": "R_kgDOR-gPKw",
    "category": "media",
    "tags": [
      "audio",
      "speech",
      "voice-cloning"
    ],
    "forms": [
      "desktop",
      "cli",
      "service"
    ],
    "platforms": [
      "linux",
      "macos",
      "windows",
      "android",
      "ios"
    ],
    "aliases": {
      "zh-CN": [
        "VoiceStudio"
      ],
      "en": [
        "VoiceStudio"
      ]
    },
    "summary": {
      "zh-CN": "在本地运行语音克隆、声音设计、转录和视频配音。另提供听写、有声书、批量任务及本地 API 与 MCP 接口。",
      "en": "Voice software for cloning, speech design, transcription and dubbing, with batch processing and agent interfaces."
    },
    "use_cases": {
      "zh-CN": [
        "把文字转成语音或有声书。本地语音转录与听写。翻译并重新配音视频。"
      ],
      "en": [
        "Prepare narrated audio",
        "Transcribe recordings and create dubbing workflows"
      ]
    },
    "alternatives": [
      "sweety-handdraw-video"
    ],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-15T11:03:50.120930Z",
        "en": "2026-11-15T11:03:50.120930Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "AGPL-3.0",
      "osi_approved": true,
      "license_sha256": "0d96a4ff68ad6d4b6f1f30f713b18d5184912ba8dd389f86aa7710db079abcb0",
      "source_url": "https://github.com/debpalash/VoiceStudio/blob/5eefe8b1e902a90bc9a23984aa69797ee9d476e1/LICENSE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "5eefe8b1e902a90bc9a23984aa69797ee9d476e1"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-15T10:37:53Z",
        "reviewed_at": "2026-11-15T11:03:50.120930Z",
        "url": "https://github.com/debpalash/VoiceStudio/commit/2c1f3f7784be2893fed65ae9ebd257f885503434",
        "qualifies": true,
        "reason": {
          "zh-CN": "在移动端配音导出前检查可用空间。已核对提交中的实现文件与差异；未运行上游测试。",
          "en": "Checks available storage before mobile dubbing exports. Reviewed implementation changes; upstream tests were not run."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/debpalash/VoiceStudio",
        "accessed_at": "2026-11-15T10:48:13.877Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/debpalash/VoiceStudio/blob/main/README.md",
        "accessed_at": "2026-11-15T10:53:59.937Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      },
      {
        "url": "https://github.com/debpalash/VoiceStudio/blob/5eefe8b1e902a90bc9a23984aa69797ee9d476e1/LICENSE",
        "accessed_at": "2026-11-15T10:53:08.351Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "009",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "a4e22adab93ef3b401f2b0cf1ce8e8d30cfdb5a263d07aac7994e5369dde004e",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "tool",
      "pending_reasons": [],
      "english_scope": "editorial_digest",
      "source_card_preserved": true
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOR-gPKw",
    "full_name": "debpalash/VoiceStudio",
    "stargazers_count": 110994,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "AGPL-3.0",
    "license_sha256": "0d96a4ff68ad6d4b6f1f30f713b18d5184912ba8dd389f86aa7710db079abcb0",
    "last_success_at": "2026-11-15T11:46:23.015Z"
  }
}
```

</details>
