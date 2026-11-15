# 代码手绘插画与动画

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[alexgreensh/anidoodle](https://github.com/alexgreensh/anidoodle)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 1693 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T10:48:21.510Z |

以上为历史核对结果，使用前请复核上游状态。 / This is a dated review; check the current upstream state before use.

## 中文

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

### 原始中文记录（历史快照）

### 046 代码手绘插画与动画

仓库：[alexgreensh/anidoodle](https://github.com/alexgreensh/anidoodle)

#### 1. 简介

以代码描述笔画，提供 32 种插画风格和逐笔绘制示例。

#### 2. 适用场景

- 用代码画手绘插画并逐笔播放。
- 同一个角色连续几个镜头不变样。
- 插画视频和交互网页一起做。

#### 3. 主要功能

- 以代码描述笔画，提供 32 种插画风格和逐笔绘制示例。
- 覆盖静态插画、绘画延时、短片、讲解和交互网页艺术。
- 包含运动编排、角色连续性和代码配乐工具，可结合自带参考图调整作品。

官方来源入口：[官方 README](https://github.com/alexgreensh/anidoodle/blob/main/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

官方支持能读取技能的 Claude Code、Codex 和 Grok Build。静态图需要浏览器，动态内容还需 FFmpeg，README 要求 Node 至少 20；画面一致性和输出效果未实测。

知识卡未提供完整部署费用或付费服务价格；未记录的费用项目需要另行核对。

#### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/alexgreensh/anidoodle/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

#### 6. 替代选择

- [helloianneo/ian-xiaohei-illustrations](ian-xiaohei-illustrations.md#中文)：本项目用代码描述笔画和逐笔动画；后者专门为中文正文生成小黑风格 PNG。
- [threerocks/sweety-handdraw-video](sweety-handdraw-video.md#中文)：本项目聚焦插画与动画；后者侧重口播、描线和声音的同步。

#### 7. 复核说明

- 知识库记录日期：2026-11-06；卡片最后确认日期：2026-11-06。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 核验范围：已读取官方 README 和仓库元数据。公开仓库，核验时未归档或禁用；本次未安装或运行。

**来源与版本记录**

- [官方 README](https://github.com/alexgreensh/anidoodle/blob/main/README.md)，读取日期：2026-11-06。
- [仓库元数据](https://api.github.com/repos/alexgreensh/anidoodle)，仓库 ID：`1381356320`。
- 本次读取的 README Git blob SHA：`06877244f1abf0cab77e5060bfdc5cac4d19cd63`。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/046_alexgreensh-anidoodle.md`。

## English

A code-based drawing and animation toolkit for stylized illustrations, characters and interactive browser output.

### Use cases

- Make illustrated explainers
- Animate a consistent visual style

### Requirements and limits

Requires a compatible skill host and Node 20+ in the source card. Static output needs a browser; video adds FFmpeg. Newer tooling includes further rendering workflows, but consistency, quality and cross-host behavior were not tested. Model and asset costs depend on the chosen setup.

### Getting started

Read the [official documentation](https://github.com/alexgreensh/anidoodle/blob/main/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [Ian Xiaohei Illustrations](ian-xiaohei-illustrations.md#english)
- [Sweety Handdraw Video](sweety-handdraw-video.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:21.510Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

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
    "id": "anidoodle",
    "name": "代码手绘插画与动画",
    "repository": "alexgreensh/anidoodle",
    "repo_node_id": "R_kgDOUlXTIA",
    "category": "media",
    "tags": [
      "agent-skill",
      "animation",
      "illustration"
    ],
    "forms": [],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "代码手绘插画与动画"
      ],
      "en": [
        "Anidoodle"
      ]
    },
    "summary": {
      "zh-CN": "以代码描述笔画，提供 32 种插画风格和逐笔绘制示例。",
      "en": "A code-based drawing and animation toolkit for stylized illustrations, characters and interactive browser output."
    },
    "use_cases": {
      "zh-CN": [
        "- 用代码画手绘插画并逐笔播放。\n- 同一个角色连续几个镜头不变样。\n- 插画视频和交互网页一起做。"
      ],
      "en": [
        "Make illustrated explainers",
        "Animate a consistent visual style"
      ]
    },
    "alternatives": [
      "ian-xiaohei-illustrations",
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
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "aa7ba36133bb07559b8f2f96eb4d7e2e95003432238973b31b6727517bd6c0a0",
      "source_url": "https://github.com/alexgreensh/anidoodle/blob/main/LICENSE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-10-29T14:22:45Z",
        "reviewed_at": "2026-11-15T11:03:50.120930Z",
        "url": "https://github.com/alexgreensh/anidoodle/commit/8cdabc03e8aafac33241ab32da1ccaff83854b0e",
        "qualifies": true,
        "reason": {
          "zh-CN": "修正影片按路径导入字体时的脚手架错误。已核对提交中的实现文件与差异；未运行上游测试。",
          "en": "Fixes scaffolding when a film imports a font by path. Reviewed implementation changes; upstream tests were not run."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/alexgreensh/anidoodle",
        "accessed_at": "2026-11-15T10:48:21.510Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/alexgreensh/anidoodle/blob/main/README.md",
        "accessed_at": "2026-11-15T10:54:05.468Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      },
      {
        "url": "https://github.com/alexgreensh/anidoodle/blob/main/LICENSE",
        "accessed_at": "2026-11-15T10:53:17.007Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "046",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "cead52977f3d8ff3f4013412119fb19061cced22dd1fa643e50e944f86f347ae",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "agent-skill",
      "pending_reasons": [],
      "english_scope": "editorial_digest",
      "source_card_preserved": true
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOUlXTIA",
    "full_name": "alexgreensh/anidoodle",
    "stargazers_count": 1693,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "aa7ba36133bb07559b8f2f96eb4d7e2e95003432238973b31b6727517bd6c0a0",
    "last_success_at": "2026-11-15T10:48:21.510Z"
  }
}
```

</details>
