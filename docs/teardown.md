# Teardown：交互式机械拆解与3D演示

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[elvarofficial/teardown](https://github.com/elvarofficial/teardown)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 3534 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T10:48:22.290Z |

以上为历史核对结果，使用前请复核上游状态。 / This is a dated review; check the current upstream state before use.

## 中文

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

### 原始中文记录（历史快照）

### 051 Teardown：交互式机械拆解与3D演示

仓库：[elvarofficial/teardown](https://github.com/elvarofficial/teardown)

#### 1. 简介

面向 Claude Code 的 3D 机械原理演示技能。支持部件拆解、剖视、联动、自动演示与人工交互，可构建离线 HTML 并录制 MP4。

#### 2. 适用场景

制作发动机、起落架和连杆机构等机械教学页面、产品结构说明或原理动画。

#### 3. 主要功能

| 能力 | 具体作用 | 核对来源 |
| --- | --- | --- |
| 机械运动与联动 | 用统一状态驱动零件姿态和面板读数；运动学模型与 Three.js 绘制分开。 | SKILL.md、V8 运动学源码 |
| 拆解与剖视 | 按子系统查看部件，提供实体、透明、剖切显示方式和观察视角。 | README、SKILL.md |
| 自动讲解与人工探索 | 空闲时按路线演示；点击、拖动、滚轮或键盘操作后交给观众控制，空闲后恢复。 | SKILL.md |
| 离线页面 | 构建脚本将 Three.js、字体和样式嵌入 HTML；也支持配置外部大资源。 | sims/build.mjs |
| 视频与截图 | Playwright 控制 Chromium 逐帧采集，支持 MP4、静帧和联系表；视频默认 60 fps。 | sims/capture.mjs |

官方来源入口：[当前 README](https://github.com/elvarofficial/teardown/blob/main/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

- **制作环境**：官方面向 Claude Code；Node.js 要求 20 或以上，依赖 Three.js、esbuild 和 Playwright。采集需安装 Playwright Chromium；视频编码需 FFmpeg，程序化音效生成另需 Python 3。观看已打包页面与制作、录制的依赖不同。
- **输入资料**：技能要求查找参考尺寸、图片或手册，再建立几何和运动关系。复杂机器的准确结构不能仅靠一句描述保证。
- **精度**：源码包含运动学和压力等演示模型。本轮只核对文档与静态代码。机械精度、物理计算和工程适用性未经验证。工程计算须另核对参数、假设和结果。
- **设备**：技能采用 1600 × 900 的固定逻辑画布，并考虑集成显卡的绘制负担。本轮未验证 iPad、触摸操作和小屏排版，也未验证 Codex 直接接入。
- **许可**：仓库为 MIT。使用外部模型、图片或音频时，还需分别核对素材许可。

知识卡未提供完整部署费用或付费服务价格；未记录的费用项目需要另行核对。

#### 5. 开始使用

安装与入门文档：[当前 README](https://github.com/elvarofficial/teardown/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

其他入口：[当前技能说明](https://github.com/elvarofficial/teardown/blob/main/SKILL.md)。

#### 6. 替代选择

- [wheresryan22/anatomy](anatomy.md#中文)：本项目侧重 3D 机械运动、拆解与剖视；后者偏向等轴测结构和机制说明。

#### 7. 复核说明

- 知识库记录日期：2026-11-06；卡片最后确认日期：2026-11-06。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：核对官方 README、SKILL.md、依赖清单和关键源码，未安装运行。问法、分类和匹配理由为检索整理判断。

**来源与版本记录**

- [当前 README](https://github.com/elvarofficial/teardown/blob/main/README.md)、[当前技能说明](https://github.com/elvarofficial/teardown/blob/main/SKILL.md)、[提交历史](https://github.com/elvarofficial/teardown/commits/main/)用于后续更新。
- 本次核验提交：[`a91262ac1109051e014662d42ecb0b7bc1f113b1`](https://github.com/elvarofficial/teardown/commit/a91262ac1109051e014662d42ecb0b7bc1f113b1)。
- 固定版本：[README](https://github.com/elvarofficial/teardown/blob/a91262ac1109051e014662d42ecb0b7bc1f113b1/README.md)、[SKILL.md](https://github.com/elvarofficial/teardown/blob/a91262ac1109051e014662d42ecb0b7bc1f113b1/SKILL.md)、[依赖与 Node 要求](https://github.com/elvarofficial/teardown/blob/a91262ac1109051e014662d42ecb0b7bc1f113b1/package.json)。
- 实现核对：[页面构建](https://github.com/elvarofficial/teardown/blob/a91262ac1109051e014662d42ecb0b7bc1f113b1/sims/build.mjs)、[录制工具](https://github.com/elvarofficial/teardown/blob/a91262ac1109051e014662d42ecb0b7bc1f113b1/sims/capture.mjs)、[V8 运动学模型](https://github.com/elvarofficial/teardown/blob/a91262ac1109051e014662d42ecb0b7bc1f113b1/sims/v8-shared/kin.js)。
- README Git blob SHA：`ba138fb0f6cfd3cd62ac5ed021e2c16374dad645`；SKILL.md Git blob SHA：`9505e4aa15caa097260cd982d1a91312dd45859a`。
- 更新时按仓库 ID `1439522537` 去重，复核默认分支、提交、能力与依赖，同步本卡和用途索引，更新最后确认日期。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/051_elvarofficial-teardown.md`。

## English

A Claude Code skill for interactive 3D mechanism explanations, exploded views, sections and recorded video.

### Use cases

- Explain a machine's parts and motion
- Build browser-based mechanism demonstrations

### Requirements and limits

Authoring requires Node 20+, Three.js, esbuild and Playwright; recording adds Chromium and FFmpeg, and sound tools use Python. Reference dimensions and manuals matter. The fixed logical canvas, touch behavior, physical models and engineering precision were not validated. External assets keep their own licenses.

### Getting started

Read the [official documentation](https://github.com/elvarofficial/teardown/blob/main/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [Anatomy](anatomy.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:22.290Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

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
    "id": "teardown",
    "name": "Teardown：交互式机械拆解与3D演示",
    "repository": "elvarofficial/teardown",
    "repo_node_id": "R_kgDOVc1e6Q",
    "category": "media",
    "tags": [
      "agent-skill",
      "3d",
      "mechanisms"
    ],
    "forms": [],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "Teardown：交互式机械拆解与3D演示"
      ],
      "en": [
        "Teardown"
      ]
    },
    "summary": {
      "zh-CN": "面向 Claude Code 的 3D 机械原理演示技能。支持部件拆解、剖视、联动、自动演示与人工交互，可构建离线 HTML 并录制 MP4。",
      "en": "A Claude Code skill for interactive 3D mechanism explanations, exploded views, sections and recorded video."
    },
    "use_cases": {
      "zh-CN": [
        "制作发动机、起落架和连杆机构等机械教学页面、产品结构说明或原理动画。"
      ],
      "en": [
        "Explain a machine's parts and motion",
        "Build browser-based mechanism demonstrations"
      ]
    },
    "alternatives": [
      "anatomy"
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
      "license_sha256": "489451d9c7bd0c07b21c7f094f24d290d52c757bf71fc988ec880aa673fb3820",
      "source_url": "https://github.com/elvarofficial/teardown/blob/main/LICENSE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-10-30T09:28:29Z",
        "reviewed_at": "2026-11-15T11:03:50.120930Z",
        "url": "https://github.com/elvarofficial/teardown/commit/e7e668cd44f48ba79a3c575e9f55c7e194d26eef",
        "qualifies": true,
        "reason": {
          "zh-CN": "新增三维机制生成、渲染与声音工具。已核对提交中的实现文件与差异；未运行上游测试。",
          "en": "Introduces mechanism-generation, rendering and sound tools. Reviewed implementation changes; upstream tests were not run."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/elvarofficial/teardown",
        "accessed_at": "2026-11-15T10:48:22.290Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/elvarofficial/teardown/blob/main/README.md",
        "accessed_at": "2026-11-15T10:54:06.110Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      },
      {
        "url": "https://github.com/elvarofficial/teardown/blob/main/LICENSE",
        "accessed_at": "2026-11-15T10:53:17.492Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "051",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "04363c56463b7c192f8fa0ce32426b41ce6d6d3d5d3595540fec1e1e212aff06",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "agent-skill",
      "pending_reasons": [],
      "english_scope": "editorial_digest",
      "source_card_preserved": true
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVc1e6Q",
    "full_name": "elvarofficial/teardown",
    "stargazers_count": 3534,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "489451d9c7bd0c07b21c7f094f24d290d52c757bf71fc988ec880aa673fb3820",
    "last_success_at": "2026-11-15T10:48:22.290Z"
  }
}
```

</details>
