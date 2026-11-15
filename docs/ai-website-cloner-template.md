# AI Website Cloner Template：网站复刻与迁移模板

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 39159 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T10:48:23.782Z |

以上为历史核对结果，使用前请复核上游状态。 / This is a dated review; check the current upstream state before use.

## 中文

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

### 原始中文记录（历史快照）

### 057 AI Website Cloner Template：网站复刻与迁移模板

仓库：[JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)

#### 1. 简介

用编码助手观察目标网页，再以 Next.js 重建页面、素材和交互。通过浏览器对照差异并修正。

#### 2. 适用场景

迁移自有网站。重建遗失源码的网站前端。学习响应式布局与滚动动画。

#### 3. 主要功能

| 能力 | 具体作用 | 核对来源 |
| --- | --- | --- |
| 路由规划 | 建立来源网址到本地路由的对应表。增补页面时保留已有路由、素材和样式。 | 技能第 1 节 |
| 页面观察 | 检查桌面与手机页面，采集文字、字体、图片和视频。记录菜单、悬停、滚动和时间驱动的状态。 | 技能第 2 节 |
| 代码重建 | 编写可编辑组件，复现布局和指定交互。共享组件与素材按站点组织。 | 技能第 3 节 |
| 视觉与行为对照 | 在相同窗口尺寸、滚动位置和状态下对照原站与本地页面，再修复差异。 | 技能第 4 节 |
| 动画页面检查 | 技能附有 Framer、粘性定位场景和动画媒体的检查指引。 | README、技能第 2 节 |
| 检查与交付 | 要求生产构建和页面对照均完成。交付运行说明、路由表、对照截图及剩余差异。 | 技能第 4 节与 Deliver |

这些是官方规定的执行流程，效果取决于助手、浏览器工具和目标页面。

官方来源入口：[官方 README](https://github.com/JCodesMore/ai-website-cloner-template/blob/master/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

- **制作环境**：Node.js 24 或以上；可用的编码助手与浏览器工具。
- **助手支持**：官方列出 Claude Code、Codex CLI、Cursor 和 OpenCode。支持情况来自文档，本次未验证各助手的实际接入。
- **技术栈**：Next.js 16、React 19、TypeScript、Tailwind CSS v4、shadcn/ui。
- **技能位置**：`.agents/skills/clone-website/` 是统一入口。Claude Code 通过 `.claude/commands/clone-website.md` 读取该技能。
- **项目检查**：`npm run check` 依次执行 ESLint 检查、TypeScript 类型检查和生产构建。页面对照仍需浏览器完成。
- **成本**：模板代码采用 MIT 许可。编码助手与模型服务使用用户自己的配置和额度。

实际采用时，在独立项目目录准备模板并安装依赖。README 在 Claude Code 和 Cursor 中给出以下调用示例：

```text
/clone-website https://example.com
```

- 助手交付的是重建代码。截图、内嵌原站页面或下载生产脚本，均不能替代实现。
- 观察到的页面与交互决定重建范围。数据库、支付、登录和后台业务需要另外实现、验证。
- 构建通过只证明项目可构建。视觉相似度、移动端和交互效果还需逐项验收。
- 仓库的 MIT 许可适用于模板代码。原站的品牌、文案和素材仍需分别确认使用条件。
- 官方限制冒充、钓鱼和违反网站使用条款的用途。
- 本次收录仅核对资料，未验证复刻效果、耗时或模型费用。

知识卡未提供完整部署费用或付费服务价格；未记录的费用项目需要另行核对。

#### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/JCodesMore/ai-website-cloner-template/blob/master/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

其他入口：[技能说明](https://github.com/JCodesMore/ai-website-cloner-template/blob/ee3f5a2f31fd549b9593fa4f7cf6d2955ee593bb/.agents/skills/clone-website/SKILL.md)。

初次使用所需环境及调用示例见上节“使用限制”。

#### 6. 替代选择

- [storytold/craft-anything](craft-anything.md#中文)：本项目专注网页观察、Next.js 重建和浏览器对照；后者还涉及应用与游戏研究。

#### 7. 复核说明

- 知识库记录日期：2026-11-08；卡片最后确认日期：2026-11-08。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：已核对官方 README、技能、依赖清单和许可。未安装运行。问法与分类属于检索整理判断。

**来源与版本记录**

- 当前入口：[官方 README](https://github.com/JCodesMore/ai-website-cloner-template/blob/master/README.md)、[提交历史](https://github.com/JCodesMore/ai-website-cloner-template/commits/master/)。
- 核验版本：默认分支 `master`，提交 [`ee3f5a2f31fd549b9593fa4f7cf6d2955ee593bb`](https://github.com/JCodesMore/ai-website-cloner-template/commit/ee3f5a2f31fd549b9593fa4f7cf6d2955ee593bb)。`package.json` 版本字段为 `0.6.1`，不代表已核验发行包。
- 固定版本：[README](https://github.com/JCodesMore/ai-website-cloner-template/blob/ee3f5a2f31fd549b9593fa4f7cf6d2955ee593bb/README.md)、[技能说明](https://github.com/JCodesMore/ai-website-cloner-template/blob/ee3f5a2f31fd549b9593fa4f7cf6d2955ee593bb/.agents/skills/clone-website/SKILL.md)、[依赖和检查命令](https://github.com/JCodesMore/ai-website-cloner-template/blob/ee3f5a2f31fd549b9593fa4f7cf6d2955ee593bb/package.json)、[MIT 许可](https://github.com/JCodesMore/ai-website-cloner-template/blob/ee3f5a2f31fd549b9593fa4f7cf6d2955ee593bb/LICENSE)。确认日期：2026-11-08。
- 助手入口核对：[Claude Code 桥接文件](https://github.com/JCodesMore/ai-website-cloner-template/blob/ee3f5a2f31fd549b9593fa4f7cf6d2955ee593bb/.claude/commands/clone-website.md)。
- 更新时按仓库 ID `1180745961` 去重，复核技能、环境和支持范围，同步用途索引与最后确认日期。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/057_JCodesMore-ai-website-cloner-template.md`。

## English

A Next.js template and agent workflow for observing existing webpages and rebuilding their layout, assets and interactions as editable code.

### Use cases

- Recreate an authorized reference page
- Compare desktop and mobile implementations

### Requirements and limits

Needs Node 24+, a coding assistant and browser tools in the source card. Source branding, text and assets have separate rights. Backends, accounts and payments need independent implementation. A successful build does not prove visual or interaction fidelity; model cost and output quality were not measured.

### Getting started

Read the [official documentation](https://github.com/JCodesMore/ai-website-cloner-template/blob/master/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [Craft Anything](craft-anything.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:23.782Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

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
    "id": "ai-website-cloner-template",
    "name": "AI Website Cloner Template：网站复刻与迁移模板",
    "repository": "JCodesMore/ai-website-cloner-template",
    "repo_node_id": "R_kgDORmDA6Q",
    "category": "development",
    "tags": [
      "agent-skill",
      "web",
      "frontend"
    ],
    "forms": [
      "web"
    ],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "AI Website Cloner Template：网站复刻与迁移模板"
      ],
      "en": [
        "AI Website Cloner Template"
      ]
    },
    "summary": {
      "zh-CN": "用编码助手观察目标网页，再以 Next.js 重建页面、素材和交互。通过浏览器对照差异并修正。",
      "en": "A Next.js template and agent workflow for observing existing webpages and rebuilding their layout, assets and interactions as editable code."
    },
    "use_cases": {
      "zh-CN": [
        "迁移自有网站。重建遗失源码的网站前端。学习响应式布局与滚动动画。"
      ],
      "en": [
        "Recreate an authorized reference page",
        "Compare desktop and mobile implementations"
      ]
    },
    "alternatives": [
      "craft-anything"
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
      "license_sha256": "cfe9368816ead6d3b0a9e0d851dcab796885c72e7b479cff1c7939debea0826d",
      "source_url": "https://github.com/JCodesMore/ai-website-cloner-template/blob/master/LICENSE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-10-05T07:06:22Z",
        "reviewed_at": "2026-11-15T11:03:50.120930Z",
        "url": "https://github.com/JCodesMore/ai-website-cloner-template/commit/bb53ca57b3f8d180bd851fee01e6342c5975aa63",
        "qualifies": true,
        "reason": {
          "zh-CN": "重写网页重建技能的观察、响应式实现和对照流程。已核对直接控制助手行为的技能内容差异，并非仅修改介绍。",
          "en": "Reworks the website skill’s observation, responsive implementation and comparison workflow. Reviewed executable skill instructions, rather than descriptive README changes."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/JCodesMore/ai-website-cloner-template",
        "accessed_at": "2026-11-15T10:48:23.782Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/JCodesMore/ai-website-cloner-template/blob/master/README.md",
        "accessed_at": "2026-11-15T10:54:07.349Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      },
      {
        "url": "https://github.com/JCodesMore/ai-website-cloner-template/blob/master/LICENSE",
        "accessed_at": "2026-11-15T10:53:18.683Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "057",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "a3df937a9a2aca07aa7361c603c0d2b6406a1e0c0e68ff3238b52605eb4198ff",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "agent-skill",
      "pending_reasons": [],
      "english_scope": "editorial_digest",
      "source_card_preserved": true
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDORmDA6Q",
    "full_name": "JCodesMore/ai-website-cloner-template",
    "stargazers_count": 39159,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "cfe9368816ead6d3b0a9e0d851dcab796885c72e7b479cff1c7939debea0826d",
    "last_success_at": "2026-11-15T10:48:23.782Z"
  }
}
```

</details>
