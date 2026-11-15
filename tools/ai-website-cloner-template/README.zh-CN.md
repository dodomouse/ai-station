# AI Website Cloner Template：网站复刻与迁移模板

简体中文 | [English](README.en.md) | [全部导入记录](../../docs/imports/2026-11-15.md)

## 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

当前资格请运行 `python3 scripts/catalog.py search ai-website-cloner-template --all`（仓库根目录）。Star 和时间数据见 [GitHub 快照](../../data/github/ai-website-cloner-template.json)，核对依据见 [元数据](tool.json)。

## 原始中文记录（历史快照）

## 057 AI Website Cloner Template：网站复刻与迁移模板

仓库：[JCodesMore/ai-website-cloner-template](https://github.com/JCodesMore/ai-website-cloner-template)

### 1. 简介

用编码助手观察目标网页，再以 Next.js 重建页面、素材和交互。通过浏览器对照差异并修正。

### 2. 适用场景

迁移自有网站。重建遗失源码的网站前端。学习响应式布局与滚动动画。

### 3. 主要功能

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

### 4. 使用限制

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

### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/JCodesMore/ai-website-cloner-template/blob/master/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

其他入口：[技能说明](https://github.com/JCodesMore/ai-website-cloner-template/blob/ee3f5a2f31fd549b9593fa4f7cf6d2955ee593bb/.agents/skills/clone-website/SKILL.md)。

初次使用所需环境及调用示例见上节“使用限制”。

### 6. 替代选择

- [storytold/craft-anything](../craft-anything/README.zh-CN.md)：本项目专注网页观察、Next.js 重建和浏览器对照；后者还涉及应用与游戏研究。

### 7. 复核说明

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
