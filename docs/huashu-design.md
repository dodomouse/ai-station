# Huashu Design

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 29538 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T10:48:12.517Z |

以上为历史核对结果，使用前请复核上游状态。 / This is a dated review; check the current upstream state before use.

## 中文

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

当前 README 说明演示贴纸采用单独许可，主代码的 MIT 许可不覆盖这些素材。

### 原始中文记录（历史快照）

### 004 Huashu Design

仓库：[alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design)

#### 1. 简介

面向智能体的 HTML 原生设计技能。可制作网页、App 原型、可编辑 PPTX、动画和信息图。

#### 2. 适用场景

制作网页与 App 原型。制作可编辑演示文稿。设计信息图或小红书图文。比较多个视觉方向。

#### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 网页和App原型 | 生成 HTML 原型，组织多屏、点击和状态交互。 | 能做什么 / iOS App 原型 |
| 幻灯片与PPTX | 制作浏览器演示的 HTML deck，并导出保留文本框的可编辑 PPTX。 | 能做什么 / HTML Slides → 可编辑 PPTX |
| 时间轴动画 | 提供动画输出流程，可交付 MP4、GIF 等。 | 能做什么 / Motion Design 引擎 |
| 信息图与图文 | 制作信息图、可视化及 3:4 小红书图文，支持图片或 PDF 等输出。 | 能做什么 / 信息图 / 数据可视化 |
| 多个视觉方向 | 先形成六个缩略候选，再挑三个方向制作真实视觉供比较。 | 设计方向顾问（Fallback） |
| 品牌与设计检查 | 读取提供的品牌资产，结合外观账本、设计体检及评审流程约束结果。 | 品牌资产协议 / 越用越懂你：经验、外观账本与设计体检 |

官方来源入口：[官方 README](https://github.com/alchaincyf/huashu-design/blob/master/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

**平台与环境**

- HTML产物通过浏览器查看；README 未给完整操作系统兼容矩阵

- 技能采用 MIT，README 明确允许个人和商用免费。
- 智能体模型订阅/API另计；项目开源不附赠模型额度。
- 可选TTS配音、AI看片评审使用用户自己的云服务key。

- HTML渲染与导出链路被文档描述为本地运行；不代表调用智能体模型也免费或离线。
- README 不支持图层级 PPTX 到 Figma；复杂 3D、物理和粒子动画超出范围。
- 未运行生成或导出，视觉质量和文件兼容性需实际验收。

**容易找错的需求（不属于本项目能力）**

- 直接交付能上App Store的原生手机应用。
- 把任意PPT完整无损转为可编辑Figma图层。

#### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/alchaincyf/huashu-design/blob/master/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- Claude Code、Codex、Cursor 等支持 skills 的智能体
- 本地脚本及HTML渲染/导出流程

#### 6. 替代选择

- [VoltAgent/awesome-design-md](awesome-design-md.md#中文)：本项目提供设计与制作流程；后者提供 DESIGN.md 设计规范，适合作为风格输入。
- [alchaincyf/huashu-art-motion](huashu-art-motion.md#中文)：本项目覆盖网页、演示文稿与图文；后者集中于艺术动画和解说片段。

#### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/alchaincyf/huashu-design/blob/master/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/004_alchaincyf-huashu-design.md`。

## English

An agent skill for producing HTML designs, app prototypes, presentations, animations and explanatory graphics.

### Use cases

- Prototype web interfaces
- Create editable presentations and visual explanations

### Requirements and limits

Model subscriptions and optional speech or image-review services are separate. Local rendering does not make model use offline. Complex 3D and layer-preserving PPTX-to-Figma conversion are outside the described scope. Current documentation excludes demonstration stickers under a separate license from the main MIT grant.

### Getting started

Read the [official documentation](https://github.com/alchaincyf/huashu-design/blob/master/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [Awesome Design MD](awesome-design-md.md#english)
- [Huashu Art Motion](huashu-art-motion.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:12.517Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

Demo stickers have separate terms; the main MIT license does not cover them.

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
    "id": "huashu-design",
    "name": "Huashu Design",
    "repository": "alchaincyf/huashu-design",
    "repo_node_id": "R_kgDOSG2mmQ",
    "category": "media",
    "tags": [
      "agent-skill",
      "design",
      "presentations"
    ],
    "forms": [],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "Huashu Design"
      ],
      "en": [
        "Huashu Design"
      ]
    },
    "summary": {
      "zh-CN": "面向智能体的 HTML 原生设计技能。可制作网页、App 原型、可编辑 PPTX、动画和信息图。",
      "en": "An agent skill for producing HTML designs, app prototypes, presentations, animations and explanatory graphics."
    },
    "use_cases": {
      "zh-CN": [
        "制作网页与 App 原型。制作可编辑演示文稿。设计信息图或小红书图文。比较多个视觉方向。"
      ],
      "en": [
        "Prototype web interfaces",
        "Create editable presentations and visual explanations"
      ]
    },
    "alternatives": [
      "awesome-design-md",
      "huashu-art-motion"
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
      "license_sha256": "6d6a2a9caf2e6d2b76974050427053b2892d8aa4c33fd168ce63a537fcee9d96",
      "source_url": "https://github.com/alchaincyf/huashu-design/blob/e8d1148a80d5a281d4247cffe320add3df017928/LICENSE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "e8d1148a80d5a281d4247cffe320add3df017928"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-10T00:12:07Z",
        "reviewed_at": "2026-11-15T11:03:50.120930Z",
        "url": "https://github.com/alchaincyf/huashu-design/commit/99a8364536b601bc28af6dc1c96876b6a0ec5f49",
        "qualifies": true,
        "reason": {
          "zh-CN": "修正隐藏 SVG 与混合 Canvas 的 PPTX 截图。已核对提交中的实现文件与差异；未运行上游测试。",
          "en": "Fixes PPTX capture of hidden SVG and mixed Canvas content. Reviewed implementation changes; upstream tests were not run."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/alchaincyf/huashu-design",
        "accessed_at": "2026-11-15T10:48:12.517Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/alchaincyf/huashu-design/blob/master/README.md",
        "accessed_at": "2026-11-15T10:53:58.979Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      },
      {
        "url": "https://github.com/alchaincyf/huashu-design/blob/e8d1148a80d5a281d4247cffe320add3df017928/LICENSE",
        "accessed_at": "2026-11-15T10:53:07.589Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "004",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "058f36e38f1d8febd5513884b79b53588a98aac6076dfd4a13208e3346c97077",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "agent-skill",
      "pending_reasons": [],
      "english_scope": "editorial_digest",
      "source_card_preserved": true,
      "notes": {
        "zh-CN": "当前 README 说明演示贴纸采用单独许可，主代码的 MIT 许可不覆盖这些素材。",
        "en": "Demo stickers have separate terms; the main MIT license does not cover them."
      }
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOSG2mmQ",
    "full_name": "alchaincyf/huashu-design",
    "stargazers_count": 29538,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "6d6a2a9caf2e6d2b76974050427053b2892d8aa4c33fd168ce63a537fcee9d96",
    "last_success_at": "2026-11-15T10:48:12.517Z"
  }
}
```

</details>
