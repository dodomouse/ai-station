# Bang Motion

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[bangtutorial/bang-motion](https://github.com/bangtutorial/bang-motion)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 2201 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T10:48:22.955Z |

以上为历史核对结果，使用前请复核上游状态。 / This is a dated review; check the current upstream state before use.

## 中文

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

### 原始中文记录（历史快照）

### 049 Bang Motion

仓库：[bangtutorial/bang-motion](https://github.com/bangtutorial/bang-motion)

#### 1. 简介

将开场、宣传片、产品演示、动态文字和讲解组织成可播放的单个 index.html。

#### 2. 适用场景

- 把图片文字素材编成动态讲解网页。
- 动画不要像幻灯片要连续镜头。
- 网页动画导出横屏或竖屏视频。

#### 3. 主要功能

- 将开场、宣传片、产品演示、动态文字和讲解组织成可播放的单个 index.html。
- 场景由共享主体、移动镜头与时间线连接，可加入用户的图片或视频素材。
- 支持横竖屏讲解和可选口播同步；可逐帧导出 MP4。

官方来源入口：[官方 README](https://github.com/bangtutorial/bang-motion/blob/main/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

需要可读取技能的编码助手。浏览器可播放网页，自动截帧需 Node/Puppeteer，MP4 导出另需 FFmpeg。支持的宿主包括 Claude Code、Codex、Gemini CLI 和 Cursor；实际兼容性未测。

知识卡未提供完整部署费用或付费服务价格；未记录的费用项目需要另行核对。

#### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/bangtutorial/bang-motion/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

#### 6. 替代选择

- [Vincentwei1021/video-shotcraft](video-shotcraft.md#中文)：本项目适合把图片与文字编成动态网页；后者侧重真实产品素材与发布宣传片。

#### 7. 复核说明

- 知识库记录日期：2026-11-06；卡片最后确认日期：2026-11-06。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 核验范围：已读取官方 README 和仓库元数据。公开仓库，核验时未归档或禁用；本次未安装或运行。

**来源与版本记录**

- [官方 README](https://github.com/bangtutorial/bang-motion/blob/main/README.md)，读取日期：2026-11-06。
- [仓库元数据](https://api.github.com/repos/bangtutorial/bang-motion)，仓库 ID：`1358561036`。
- 本次读取的 README Git blob SHA：`85143d82b377ad1ccc69222c475d3704c992aaca`。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/049_bangtutorial-bang-motion.md`。

## English

Creates openers, promos, product clips and typography as a single HTML animation with optional video export.

### Use cases

- Make looping brand animations
- Create short motion explainers

### Requirements and limits

Requires a compatible coding assistant. Browser playback differs from automated capture, which needs Node/Puppeteer, and MP4 export adds FFmpeg. Model and footage costs are separate. Host compatibility and export quality were not verified during import.

### Getting started

Read the [official documentation](https://github.com/bangtutorial/bang-motion/blob/main/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [Video Shotcraft](video-shotcraft.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:22.955Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

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
    "id": "bang-motion",
    "name": "Bang Motion",
    "repository": "bangtutorial/bang-motion",
    "repo_node_id": "R_kgDOUPn_DA",
    "category": "media",
    "tags": [
      "agent-skill",
      "animation",
      "html"
    ],
    "forms": [],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "Bang Motion"
      ],
      "en": [
        "Bang Motion"
      ]
    },
    "summary": {
      "zh-CN": "将开场、宣传片、产品演示、动态文字和讲解组织成可播放的单个 index.html。",
      "en": "Creates openers, promos, product clips and typography as a single HTML animation with optional video export."
    },
    "use_cases": {
      "zh-CN": [
        "- 把图片文字素材编成动态讲解网页。\n- 动画不要像幻灯片要连续镜头。\n- 网页动画导出横屏或竖屏视频。"
      ],
      "en": [
        "Make looping brand animations",
        "Create short motion explainers"
      ]
    },
    "alternatives": [
      "video-shotcraft"
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
      "license_sha256": "5baa6f2a531baa97eb2d3dea7778990fb244d5c6627025b5c2a5bdebd8d1bf5c",
      "source_url": "https://github.com/bangtutorial/bang-motion/blob/main/LICENSE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-09-15T04:45:26Z",
        "reviewed_at": "2026-11-15T11:03:50.120930Z",
        "url": "https://github.com/bangtutorial/bang-motion/commit/c1aa65e921c970d858705fcb4a53a8294d1a4131",
        "qualifies": true,
        "reason": {
          "zh-CN": "在动画技能中增加镜头景别与面向元素的运镜规则。已核对直接控制助手行为的技能内容差异，并非仅修改介绍。",
          "en": "Adds shot sizing and element-directed camera behavior to the animation skill. Reviewed executable skill instructions, rather than descriptive README changes."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/bangtutorial/bang-motion",
        "accessed_at": "2026-11-15T10:48:22.955Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/bangtutorial/bang-motion/blob/main/README.md",
        "accessed_at": "2026-11-15T10:54:06.240Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      },
      {
        "url": "https://github.com/bangtutorial/bang-motion/blob/main/LICENSE",
        "accessed_at": "2026-11-15T10:53:17.527Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "049",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "123550b0a4a02ef4673b0e4f752595f5f518d6114816eec0de4fa0bc61eec972",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "agent-skill",
      "pending_reasons": [],
      "english_scope": "editorial_digest",
      "source_card_preserved": true
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOUPn_DA",
    "full_name": "bangtutorial/bang-motion",
    "stargazers_count": 2201,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "5baa6f2a531baa97eb2d3dea7778990fb244d5c6627025b5c2a5bdebd8d1bf5c",
    "last_success_at": "2026-11-15T10:48:22.955Z"
  }
}
```

</details>
