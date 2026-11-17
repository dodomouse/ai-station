# Animate 程序化动画

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[cth9191/animate](https://github.com/cth9191/animate)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 1967 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T10:48:21.655Z |

以上为历史核对结果，使用前请复核上游状态。 / This is a dated review; check the current upstream state before use.

## 中文

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

### 原始中文记录（历史快照）

### 047 Animate 程序化动画

仓库：[cth9191/animate](https://github.com/cth9191/animate)

#### 1. 简介

以单个 Canvas 程序化绘制和配乐，用无头浏览器与 FFmpeg 输出 MP4。

#### 2. 适用场景

- 先确认故事和分镜再生成动画。
- 照参考图片的画风做科普短片。
- 数学像素剪纸动画 Skill。

#### 3. 主要功能

- 以单个 Canvas 程序化绘制和配乐，用无头浏览器与 FFmpeg 输出 MP4。
- 内置剪纸、排线、孔版印刷、素描、数学、像素与等距风格；可从参考图设计新风格。
- 流程包含需求问答、故事检查、风格帧确认、分镜确认、制作和交付检查。

官方来源入口：[官方 README](https://github.com/cth9191/animate/blob/main/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

官方面向 Claude Code，要求 Node 至少 18、Playwright Chromium 和 FFmpeg。口播时间戳另需 Python/faster-whisper，配音可接可选服务。确认流程是技能约定，未实际执行验证。

知识卡未提供完整部署费用或付费服务价格；未记录的费用项目需要另行核对。

#### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/cth9191/animate/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

#### 6. 替代选择

- [bangtutorial/bang-motion](bang-motion.md#中文)：本项目用 Canvas 绘制和配乐并输出 MP4；后者以可播放的单个 HTML 为主要组织形式。

#### 7. 复核说明

- 知识库记录日期：2026-11-06；卡片最后确认日期：2026-11-06。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 核验范围：已读取官方 README 和仓库元数据。公开仓库，核验时未归档或禁用；本次未安装或运行。

**来源与版本记录**

- [官方 README](https://github.com/cth9191/animate/blob/main/README.md)，读取日期：2026-11-06。
- [仓库元数据](https://api.github.com/repos/cth9191/animate)，仓库 ID：`1403731980`。
- 本次读取的 README Git blob SHA：`c409111ba7a6709d728bafacbbd9aacfdc8bf300`。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/047_cth9191-animate.md`。

## English

Builds procedural Canvas animations with music and timed narration, then renders video using browser tools and FFmpeg.

### Use cases

- Create short explanatory videos
- Align animated scenes with voice-over timing

### Requirements and limits

The documented host is Claude Code. Requires Node 18+, Playwright Chromium and FFmpeg; word timestamps add Python/faster-whisper. Optional voice services have separate costs. Review checkpoints are skill instructions, not evidence that this import executed a production run.

### Getting started

Read the [official documentation](https://github.com/cth9191/animate/blob/main/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [Bang Motion](bang-motion.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:21.655Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

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
    "id": "animate",
    "name": "Animate 程序化动画",
    "repository": "cth9191/animate",
    "repo_node_id": "R_kgDOU6tADA",
    "category": "media",
    "tags": [
      "agent-skill",
      "canvas",
      "video"
    ],
    "forms": [],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "Animate 程序化动画"
      ],
      "en": [
        "Animate"
      ]
    },
    "summary": {
      "zh-CN": "以单个 Canvas 程序化绘制和配乐，用无头浏览器与 FFmpeg 输出 MP4。",
      "en": "Builds procedural Canvas animations with music and timed narration, then renders video using browser tools and FFmpeg."
    },
    "use_cases": {
      "zh-CN": [
        "- 先确认故事和分镜再生成动画。\n- 照参考图片的画风做科普短片。\n- 数学像素剪纸动画 Skill。"
      ],
      "en": [
        "Create short explanatory videos",
        "Align animated scenes with voice-over timing"
      ]
    },
    "alternatives": [
      "bang-motion"
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
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "fe0cbecb2244c397885aae6962df8a0b7d43805d663ee9cda344d05b87bd8625",
      "source_url": "https://github.com/cth9191/animate/blob/7e5eb56feb2dd573f890e1b7b34748af43d58263/LICENSE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "7e5eb56feb2dd573f890e1b7b34748af43d58263"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-10-05T20:31:47Z",
        "reviewed_at": "2026-11-15T11:03:50.120930Z",
        "url": "https://github.com/cth9191/animate/commit/7e5eb56feb2dd573f890e1b7b34748af43d58263",
        "qualifies": true,
        "reason": {
          "zh-CN": "增加按语音词级时间组织动画的流程与工具。已核对提交中的实现文件与差异；未运行上游测试。",
          "en": "Adds tools and workflow for word-timed voice-over animation. Reviewed implementation changes; upstream tests were not run."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/cth9191/animate",
        "accessed_at": "2026-11-15T10:48:21.655Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/cth9191/animate/blob/main/README.md",
        "accessed_at": "2026-11-15T10:54:05.444Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      },
      {
        "url": "https://github.com/cth9191/animate/blob/7e5eb56feb2dd573f890e1b7b34748af43d58263/LICENSE",
        "accessed_at": "2026-11-15T10:53:16.677Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "047",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "c83909cb9babb206bb7b2e852aa28ac314eaba60ccb5738b7931e010222a3cb7",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "agent-skill",
      "pending_reasons": [],
      "english_scope": "editorial_digest",
      "source_card_preserved": true
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOU6tADA",
    "full_name": "cth9191/animate",
    "stargazers_count": 1967,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "fe0cbecb2244c397885aae6962df8a0b7d43805d663ee9cda344d05b87bd8625",
    "last_success_at": "2026-11-15T10:48:21.655Z"
  }
}
```

</details>
