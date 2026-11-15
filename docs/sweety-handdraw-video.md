# 手绘口播视频

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[threerocks/sweety-handdraw-video](https://github.com/threerocks/sweety-handdraw-video)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 1218 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T10:48:21.724Z |

以上为历史核对结果，使用前请复核上游状态。 / This is a dated review; check the current upstream state before use.

## 中文

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

最新提交包含肖像影片流程修正。原中文卡保留当时范围，英文摘要补充该方向；未运行渲染。

### 原始中文记录（历史快照）

### 048 手绘口播视频

仓库：[threerocks/sweety-handdraw-video](https://github.com/threerocks/sweety-handdraw-video)

#### 1. 简介

Agent 整理内容、口播和分镜，本地工具执行描线、填色、手写文字与声音对齐。

#### 2. 适用场景

- 让画笔跟着文章口播边画边讲。
- 手绘故事视频带旁白字幕。
- 用已有配音生成绘画讲解视频。

#### 3. 主要功能

- Agent 整理内容、口播和分镜，本地工具执行描线、填色、手写文字与声音对齐。
- 支持现成旁白或配置配音后端，按旁白时间戳编排画面。
- 当前 README 的主要渲染栈为 Python/Pillow/SciPy/FFmpeg；交付 MP4、封面、SRT 与口播稿。

官方来源入口：[官方 README](https://github.com/threerocks/sweety-handdraw-video/blob/main/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

官方支持 macOS/Linux、Codex/Claude Code，Windows 暂不承诺。需要 Python 至少 3.9、FFmpeg、字体、插画和配音路径；模型权重不随技能提供。生图或模型宿主可能收费。

知识卡未提供完整部署费用或付费服务价格；未记录的费用项目需要另行核对。

#### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/threerocks/sweety-handdraw-video/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

#### 6. 替代选择

- [alexgreensh/anidoodle](anidoodle.md#中文)：本项目围绕旁白安排描线、填色和手写内容；后者提供多种代码手绘风格和逐笔示例。

#### 7. 复核说明

- 知识库记录日期：2026-11-06；卡片最后确认日期：2026-11-06。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 核验范围：已读取官方 README 和仓库元数据。公开仓库，核验时未归档或禁用；本次未安装或运行。

**来源与版本记录**

- [官方 README](https://github.com/threerocks/sweety-handdraw-video/blob/main/README.md)，读取日期：2026-11-06。
- [仓库元数据](https://api.github.com/repos/threerocks/sweety-handdraw-video)，仓库 ID：`1415556604`。
- 本次读取的 README Git blob SHA：`cecc0ecaf31244a4e26dfd5f0f8173994bae02e0`。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/048_threerocks-sweety-handdraw-video.md`。

## English

A workflow for illustrated narration with local tracing, fills, handwriting and audio alignment, with newer portrait-film tooling.

### Use cases

- Produce hand-drawn explainer videos
- Explore photo-to-painting film workflows

### Requirements and limits

The source card supports macOS/Linux with Codex or Claude Code and does not promise Windows. Needs Python 3.9+, FFmpeg, fonts, illustrations and voice inputs. Model weights and service credits are separate. Third-party stroke data, voices and images retain their own conditions; rendering was not tested.

### Getting started

Read the [official documentation](https://github.com/threerocks/sweety-handdraw-video/blob/main/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [Anidoodle](anidoodle.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:21.724Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

Recent commits include portrait-film workflow fixes. The original card remains historical, and the English digest mentions this addition without claiming a rendering test.

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
    "id": "sweety-handdraw-video",
    "name": "手绘口播视频",
    "repository": "threerocks/sweety-handdraw-video",
    "repo_node_id": "R_kgDOVF-t_A",
    "category": "media",
    "tags": [
      "agent-skill",
      "hand-drawn",
      "video"
    ],
    "forms": [],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "手绘口播视频"
      ],
      "en": [
        "Sweety Handdraw Video"
      ]
    },
    "summary": {
      "zh-CN": "Agent 整理内容、口播和分镜，本地工具执行描线、填色、手写文字与声音对齐。",
      "en": "A workflow for illustrated narration with local tracing, fills, handwriting and audio alignment, with newer portrait-film tooling."
    },
    "use_cases": {
      "zh-CN": [
        "- 让画笔跟着文章口播边画边讲。\n- 手绘故事视频带旁白字幕。\n- 用已有配音生成绘画讲解视频。"
      ],
      "en": [
        "Produce hand-drawn explainer videos",
        "Explore photo-to-painting film workflows"
      ]
    },
    "alternatives": [
      "anidoodle"
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
      "license_sha256": "c56704c3fd6b99de34c7e9d2e5dea8e19a18e1978f3614a3f830f1bdbb93f46c",
      "source_url": "https://github.com/threerocks/sweety-handdraw-video/blob/main/LICENSE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-11T16:29:58Z",
        "reviewed_at": "2026-11-15T11:03:50.120930Z",
        "url": "https://github.com/threerocks/sweety-handdraw-video/commit/84b6eb436fe6173167529631a2fd03c30864ad3e",
        "qualifies": true,
        "reason": {
          "zh-CN": "修正肖像影片的可复现生成流程。已核对提交中的实现文件与差异；未运行上游测试。",
          "en": "Fixes deterministic portrait-film generation. Reviewed implementation changes; upstream tests were not run."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/threerocks/sweety-handdraw-video",
        "accessed_at": "2026-11-15T10:48:21.724Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/threerocks/sweety-handdraw-video/blob/main/README.md",
        "accessed_at": "2026-11-15T10:54:05.683Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      },
      {
        "url": "https://github.com/threerocks/sweety-handdraw-video/blob/main/LICENSE",
        "accessed_at": "2026-11-15T10:53:16.829Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "048",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "edd5847ac619d9c4b954f5a6360c9bedcae83b7401004a69ece37dae57895d62",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "agent-skill",
      "pending_reasons": [],
      "english_scope": "editorial_digest",
      "source_card_preserved": true,
      "notes": {
        "zh-CN": "最新提交包含肖像影片流程修正。原中文卡保留当时范围，英文摘要补充该方向；未运行渲染。",
        "en": "Recent commits include portrait-film workflow fixes. The original card remains historical, and the English digest mentions this addition without claiming a rendering test."
      }
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVF-t_A",
    "full_name": "threerocks/sweety-handdraw-video",
    "stargazers_count": 1218,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "c56704c3fd6b99de34c7e9d2e5dea8e19a18e1978f3614a3f830f1bdbb93f46c",
    "last_success_at": "2026-11-15T10:48:21.724Z"
  }
}
```

</details>
