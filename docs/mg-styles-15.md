# 15 种动态设计风格

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[Vincentwei1021/mg-styles-15](https://github.com/Vincentwei1021/mg-styles-15)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 3540 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T10:48:21.042Z |

以上为历史核对结果，使用前请复核上游状态。 / This is a dated review; check the current upstream state before use.

## 中文

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

### 原始中文记录（历史快照）

### 044 15 种动态设计风格

仓库：[Vincentwei1021/mg-styles-15](https://github.com/Vincentwei1021/mg-styles-15)

#### 1. 简介

15 支 10 秒动态设计示例，逐项公开风格说明、完整提示词与源码。

#### 2. 适用场景

- 找 10 秒动态设计样片和源码。
- MG 动效提示词有哪些。
- 画面和音乐都用代码生成的参考。

#### 3. 主要功能

- 15 支 10 秒动态设计示例，逐项公开风格说明、完整提示词与源码。
- 画面主要使用 SVG、Canvas、WebGL 和 Three.js；3D 示例使用 Blender。
- 浏览器按时间渲染画面，Python 脚本制作声音，FFmpeg 合成影片。

官方来源入口：[官方 README](https://github.com/Vincentwei1021/mg-styles-15/blob/main/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

官方示例由 Claude Opus 5.5 编写，不代表其他模型能同等复现。渲染需 Node 至少 22.12、Chrome、FFmpeg；3D 路线另需 Blender，声音脚本需相应 Python 依赖。

知识卡未提供完整部署费用或付费服务价格；未记录的费用项目需要另行核对。

#### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/Vincentwei1021/mg-styles-15/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

#### 6. 替代选择

- [lemomo-ai/lemo-opuscar](lemo-opuscar.md#中文)：本项目提供 15 支 10 秒样片的完整提示词和源码；后者提供更多风格入口。

#### 7. 复核说明

- 知识库记录日期：2026-11-06；卡片最后确认日期：2026-11-06。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 核验范围：已读取官方 README 和仓库元数据。公开仓库，核验时未归档或禁用；本次未安装或运行。

**来源与版本记录**

- [官方 README](https://github.com/Vincentwei1021/mg-styles-15/blob/main/README.md)，读取日期：2026-11-06。
- [仓库元数据](https://api.github.com/repos/Vincentwei1021/mg-styles-15)，仓库 ID：`1401461555`。
- 本次读取的 README Git blob SHA：`93806b4ecab984fa6e46a272d82313d96ce5a5af`。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/044_Vincentwei1021-mg-styles-15.md`。

## English

Fifteen short motion-design examples with style prompts, source code and audio tooling.

### Use cases

- Compare short-film styles
- Adapt motion and sound examples

### Requirements and limits

Needs Node 22.12+, Chrome and FFmpeg in the source card; 3D paths add Blender and audio tools add Python dependencies. Examples from one model do not guarantee other models reproduce them. Third-party assets retain their conditions, and local rendering was not tested.

### Getting started

Read the [official documentation](https://github.com/Vincentwei1021/mg-styles-15/blob/main/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [Lemo-Opuscar](lemo-opuscar.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:21.042Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

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
    "id": "mg-styles-15",
    "name": "15 种动态设计风格",
    "repository": "Vincentwei1021/mg-styles-15",
    "repo_node_id": "R_kgDOU4ibMw",
    "category": "media",
    "tags": [
      "animation",
      "examples",
      "audio"
    ],
    "forms": [
      "cli"
    ],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "15 种动态设计风格"
      ],
      "en": [
        "MG Styles 15"
      ]
    },
    "summary": {
      "zh-CN": "15 支 10 秒动态设计示例，逐项公开风格说明、完整提示词与源码。",
      "en": "Fifteen short motion-design examples with style prompts, source code and audio tooling."
    },
    "use_cases": {
      "zh-CN": [
        "- 找 10 秒动态设计样片和源码。\n- MG 动效提示词有哪些。\n- 画面和音乐都用代码生成的参考。"
      ],
      "en": [
        "Compare short-film styles",
        "Adapt motion and sound examples"
      ]
    },
    "alternatives": [
      "lemo-opuscar"
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
      "license_sha256": "7f03fee9299a401615e13e2c636ead0394f47395da4f816ae60b35ed2d91a932",
      "source_url": "https://github.com/Vincentwei1021/mg-styles-15/blob/main/LICENSE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-09T15:47:38Z",
        "reviewed_at": "2026-11-15T11:03:50.120930Z",
        "url": "https://github.com/Vincentwei1021/mg-styles-15/commit/269f6ed788cf60aaf9c276b110c548d6e7d353e1",
        "qualifies": true,
        "reason": {
          "zh-CN": "刷新缓存乐器的音频采样可用性。已核对提交中的实现文件与差异；未运行上游测试。",
          "en": "Refreshes sample availability for cached instruments. Reviewed implementation changes; upstream tests were not run."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/Vincentwei1021/mg-styles-15",
        "accessed_at": "2026-11-15T10:48:21.042Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/Vincentwei1021/mg-styles-15/blob/main/README.md",
        "accessed_at": "2026-11-15T10:54:05.094Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      },
      {
        "url": "https://github.com/Vincentwei1021/mg-styles-15/blob/main/LICENSE",
        "accessed_at": "2026-11-15T10:53:16.102Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "044",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "9f15abf63c28029168b56ce75127a4abe75a5e5dc347df799087bfdb93f04231",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "tool",
      "pending_reasons": [],
      "english_scope": "editorial_digest",
      "source_card_preserved": true
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOU4ibMw",
    "full_name": "Vincentwei1021/mg-styles-15",
    "stargazers_count": 3540,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "7f03fee9299a401615e13e2c636ead0394f47395da4f816ae60b35ed2d91a932",
    "last_success_at": "2026-11-15T10:48:21.042Z"
  }
}
```

</details>
