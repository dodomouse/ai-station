# Lemo-Opuscar

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 候选 / Candidate |
| Star | 16446 |
| 许可证 / License | 待复核 / Review needed |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T10:48:20.787Z |

候选原因：许可证待复核。
Candidate reason: License requires review.

以上为历史核对结果，使用前请复核上游状态。 / This is a dated review; check the current upstream state before use.

## 中文

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

当前 README 已更新为 99 种风格，原卡的 66 种属于旧版本。当前许可分为 MIT 代码、CC BY-NC 文档与提示词、CC BY 示例影片，并另列第三方素材及配音例外。

### 原始中文记录（历史快照）

### 042 Lemo-Opuscar

仓库：[lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar)

#### 1. 简介

66 种风格，每种提供风格提示词和代码短片示例。

#### 2. 适用场景

- 挑一种风格让 Agent 做知识短片。
- 白板像素水墨视频的代码模板。
- 想改一个镜头而不是重新抽视频。

#### 3. 主要功能

- 66 种风格，每种提供风格提示词和代码短片示例。
- 可选现成风格，也可修改或创建自己的风格并复用。
- 以代码控制画面和时间线，通过浏览器逐帧渲染并合成影片。

官方来源入口：[官方 README](https://github.com/lemomo-ai/lemo-opuscar/blob/main/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

官方称风格为 Claude Opus 5.5 调整，其他模型不保证复现。README 要求 Node 至少 20、FFmpeg 至少 7、Python 至少 3.11 或 uv；本次未运行。

知识卡未提供完整部署费用或付费服务价格；未记录的费用项目需要另行核对。

#### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/lemomo-ai/lemo-opuscar/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

#### 6. 替代选择

- [alchaincyf/huashu-art-motion](huashu-art-motion.md#中文)：本项目按风格提供提示词与代码短片；后者还按解说语法和参数化片段组织素材。
- [Vincentwei1021/mg-styles-15](mg-styles-15.md#中文)：本项目是较广的风格集合；后者围绕 15 支短片给出提示词与源码。

#### 7. 复核说明

- 知识库记录日期：2026-11-06；卡片最后确认日期：2026-11-06。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 核验范围：已读取官方 README 和仓库元数据。公开仓库，核验时未归档或禁用；本次未安装或运行。

**来源与版本记录**

- [官方 README](https://github.com/lemomo-ai/lemo-opuscar/blob/main/README.md)，读取日期：2026-11-06。
- [仓库元数据](https://api.github.com/repos/lemomo-ai/lemo-opuscar)，仓库 ID：`1389011744`。
- 本次读取的 README Git blob SHA：`18795ca8fec718e70c154755be136c55be3b457c`。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/042_lemomo-ai-lemo-opuscar.md`。

## English

A motion-design library of style guides, prompts, code examples and demonstration films; the current README lists 99 styles.

### Use cases

- Explore animation styles
- Adapt example-driven film workflows

### Requirements and limits

The imported card described 66 styles; 99 is a later documentation update. Current licensing separates MIT code, CC BY-NC Markdown/prompts and CC BY demo films, with third-party and voice exceptions. Needs the documented Node, FFmpeg and Python environment. Model portability, rendering quality and costs were not tested.

### Getting started

Read the [official documentation](https://github.com/lemomo-ai/lemo-opuscar/blob/main/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [Huashu Art Motion](huashu-art-motion.md#english)
- [MG Styles 15](mg-styles-15.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:20.787Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

The README now lists 99 styles; the original 66 refers to an earlier version. Code is MIT, docs/prompts CC BY-NC and demo films CC BY, with additional asset and voice exceptions.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

保留原始核对数据，便于追溯来源、许可和维护证据。 / Original review data preserves source, license and maintenance evidence.

```json
{
  "evaluated_at": "2026-11-15T11:54:08.129868Z",
  "eligibility": {
    "status": "unknown",
    "reasons": [
      "license_needs_review"
    ]
  },
  "metadata": {
    "schema_version": 1,
    "id": "lemo-opuscar",
    "name": "Lemo-Opuscar",
    "repository": "lemomo-ai/lemo-opuscar",
    "repo_node_id": "R_kgDOUsqjIA",
    "category": "media",
    "tags": [
      "agent-skill",
      "animation",
      "noncommercial"
    ],
    "forms": [],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "Lemo-Opuscar"
      ],
      "en": [
        "Lemo-Opuscar"
      ]
    },
    "summary": {
      "zh-CN": "提供动画风格指南、提示词、示例代码和短片。当前 README 列出 99 种风格。",
      "en": "A motion-design library of style guides, prompts, code examples and demonstration films; the current README lists 99 styles."
    },
    "use_cases": {
      "zh-CN": [
        "- 挑一种风格让 Agent 做知识短片。\n- 白板像素水墨视频的代码模板。\n- 想改一个镜头而不是重新抽视频。"
      ],
      "en": [
        "Explore animation styles",
        "Adapt example-driven film workflows"
      ]
    },
    "alternatives": [
      "huashu-art-motion",
      "mg-styles-15"
    ],
    "editorial": {
      "status": "draft",
      "reviewed_at": {
        "zh-CN": "2026-11-15T11:03:50.120930Z",
        "en": "2026-11-15T11:03:50.120930Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": null,
      "osi_approved": false,
      "license_sha256": "aee72797af4389583c0f531f7fc89c87c87cb939bdba43d888926dd8aaea8d26",
      "source_url": "https://github.com/lemomo-ai/lemo-opuscar/blob/main/LICENSE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-12T11:29:01Z",
        "reviewed_at": "2026-11-15T11:03:50.120930Z",
        "url": "https://github.com/lemomo-ai/lemo-opuscar/commit/3a7132b996be0241c1ea0ab180d519f06e6f10b6",
        "qualifies": true,
        "reason": {
          "zh-CN": "修正影片仓库脚本的目录解析和推送前检查。已核对提交中的实现文件与差异；未运行上游测试。",
          "en": "Fixes directory resolution and pre-push checks in the film-repository script. Reviewed implementation changes; upstream tests were not run."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/lemomo-ai/lemo-opuscar",
        "accessed_at": "2026-11-15T10:48:20.787Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/lemomo-ai/lemo-opuscar/blob/main/README.md",
        "accessed_at": "2026-11-15T10:54:04.794Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      },
      {
        "url": "https://github.com/lemomo-ai/lemo-opuscar/blob/main/LICENSE",
        "accessed_at": "2026-11-15T10:53:16.013Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "042",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "1534316e2d5fea251acec109bfe9023559dce24c7b0b4834c13dad6876c5da15",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "agent-skill",
      "pending_reasons": [
        "license_review_pending"
      ],
      "english_scope": "editorial_digest",
      "source_card_preserved": true,
      "notes": {
        "zh-CN": "当前 README 已更新为 99 种风格，原卡的 66 种属于旧版本。当前许可分为 MIT 代码、CC BY-NC 文档与提示词、CC BY 示例影片，并另列第三方素材及配音例外。",
        "en": "The README now lists 99 styles; the original 66 refers to an earlier version. Code is MIT, docs/prompts CC BY-NC and demo films CC BY, with additional asset and voice exceptions."
      }
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOUsqjIA",
    "full_name": "lemomo-ai/lemo-opuscar",
    "stargazers_count": 16446,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "NOASSERTION",
    "license_sha256": "aee72797af4389583c0f531f7fc89c87c87cb939bdba43d888926dd8aaea8d26",
    "last_success_at": "2026-11-15T10:48:20.787Z"
  }
}
```

</details>
