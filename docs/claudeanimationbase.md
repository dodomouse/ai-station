# Claude Animation Base

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[JohnHeibel/ClaudeAnimationBase](https://github.com/JohnHeibel/ClaudeAnimationBase)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 2995 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T10:48:22.225Z |

以上为历史核对结果，使用前请复核上游状态。 / This is a dated review; check the current upstream state before use.

## 中文

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

### 原始中文记录（历史快照）

### 050 Claude Animation Base

仓库：[JohnHeibel/ClaudeAnimationBase](https://github.com/JohnHeibel/ClaudeAnimationBase)

#### 1. 简介

以 p5.js 与 p5.brush 绘制角色，提供 Clawd 角色、核心绘画工具和时间线。

#### 2. 适用场景

- 用 Clawd 表情角色做卡通故事。
- 找 p5.js 手绘动画起始工程。
- 角色逐镜头表演再渲染 MP4。

#### 3. 主要功能

- 以 p5.js 与 p5.brush 绘制角色，提供 Clawd 角色、核心绘画工具和时间线。
- ANIMATION_GUIDE.md 说明分镜、逐镜头构建、接触表检查和动画原则。
- 提供浏览器预览与无头渲染，输出 MP4、静帧和画面检查素材。

官方来源入口：[官方 README](https://github.com/JohnHeibel/ClaudeAnimationBase/blob/main/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

需要 Node.js、Google Chrome 和 FFmpeg。官方测试样片使用 Claude Opus 5.5；集成显卡下水彩填色可能按秒计每帧。PDF 的 31 种表情是文章口径，README 本次未复述数量。

知识卡未提供完整部署费用或付费服务价格；未记录的费用项目需要另行核对。

#### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/JohnHeibel/ClaudeAnimationBase/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

#### 6. 替代选择

- [alexgreensh/anidoodle](anidoodle.md#中文)：本项目以 p5.js、p5.brush 和 Clawd 角色为起点；后者提供多种插画风格及逐笔绘制方式。

#### 7. 复核说明

- 知识库记录日期：2026-11-06；卡片最后确认日期：2026-11-06。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 核验范围：已读取官方 README 和仓库元数据。公开仓库，核验时未归档或禁用；本次未安装或运行。

**来源与版本记录**

- [官方 README](https://github.com/JohnHeibel/ClaudeAnimationBase/blob/main/README.md)，读取日期：2026-11-06。
- [仓库元数据](https://api.github.com/repos/JohnHeibel/ClaudeAnimationBase)，仓库 ID：`1384159311`。
- 本次读取的 README Git blob SHA：`53816fa825aad75212c43f6145abdd77d55c2064`。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/050_JohnHeibel-ClaudeAnimationBase.md`。

## English

A p5.js and p5.brush animation starter with drawing primitives, character scenes, timelines and MP4 rendering.

### Use cases

- Build hand-drawn animation scenes
- Render procedural illustrations to video

### Requirements and limits

Needs Node.js, Chrome and FFmpeg. Watercolor effects can be slow on integrated graphics. Demonstrations made with one model do not establish universal output quality. The source card did not independently confirm expression counts or benchmark rendering.

### Getting started

Read the [official documentation](https://github.com/JohnHeibel/ClaudeAnimationBase/blob/main/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [Anidoodle](anidoodle.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:22.225Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

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
    "id": "claudeanimationbase",
    "name": "Claude Animation Base",
    "repository": "JohnHeibel/ClaudeAnimationBase",
    "repo_node_id": "R_kgDOUoCYTw",
    "category": "media",
    "tags": [
      "animation",
      "illustration",
      "p5js"
    ],
    "forms": [
      "cli"
    ],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "Claude Animation Base"
      ],
      "en": [
        "Claude Animation Base"
      ]
    },
    "summary": {
      "zh-CN": "以 p5.js 与 p5.brush 绘制角色，提供 Clawd 角色、核心绘画工具和时间线。",
      "en": "A p5.js and p5.brush animation starter with drawing primitives, character scenes, timelines and MP4 rendering."
    },
    "use_cases": {
      "zh-CN": [
        "- 用 Clawd 表情角色做卡通故事。\n- 找 p5.js 手绘动画起始工程。\n- 角色逐镜头表演再渲染 MP4。"
      ],
      "en": [
        "Build hand-drawn animation scenes",
        "Render procedural illustrations to video"
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
      "license_sha256": "7d25ae95b305b884c08ce898e53b58d2e180ff0119e5d203d8b4ae30420f3b33",
      "source_url": "https://github.com/JohnHeibel/ClaudeAnimationBase/blob/0ac8bf2b31942376cb6b8c4074715595d512acd2/LICENSE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "0ac8bf2b31942376cb6b8c4074715595d512acd2"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-09-24T07:40:01Z",
        "reviewed_at": "2026-11-15T11:03:50.120930Z",
        "url": "https://github.com/JohnHeibel/ClaudeAnimationBase/commit/ff391da46bff3f5ca08244fd71e1b183da412647",
        "qualifies": true,
        "reason": {
          "zh-CN": "修正放大镜头下的图形轮廓绘制。已核对提交中的实现文件与差异；未运行上游测试。",
          "en": "Fixes shape outlines under camera zoom. Reviewed implementation changes; upstream tests were not run."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/JohnHeibel/ClaudeAnimationBase",
        "accessed_at": "2026-11-15T10:48:22.225Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/JohnHeibel/ClaudeAnimationBase/blob/main/README.md",
        "accessed_at": "2026-11-15T10:54:06.074Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      },
      {
        "url": "https://github.com/JohnHeibel/ClaudeAnimationBase/blob/0ac8bf2b31942376cb6b8c4074715595d512acd2/LICENSE",
        "accessed_at": "2026-11-15T10:53:17.234Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "050",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "635f87524330f528f41af2a281d916004b1b1f92b27619ac72a5ec55ba927330",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "tool",
      "pending_reasons": [],
      "english_scope": "editorial_digest",
      "source_card_preserved": true
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOUoCYTw",
    "full_name": "JohnHeibel/ClaudeAnimationBase",
    "stargazers_count": 2995,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "7d25ae95b305b884c08ce898e53b58d2e180ff0119e5d203d8b4ae30420f3b33",
    "last_success_at": "2026-11-15T10:48:22.225Z"
  }
}
```

</details>
