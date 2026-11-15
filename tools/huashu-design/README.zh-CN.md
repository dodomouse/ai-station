# Huashu Design

简体中文 | [English](README.en.md) | [全部导入记录](../../docs/imports/2026-11-15.md)

## 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

当前资格请运行 `python3 scripts/catalog.py search huashu-design --all`（仓库根目录）。Star 和时间数据见 [GitHub 快照](../../data/github/huashu-design.json)，核对依据见 [元数据](tool.json)。

当前 README 说明演示贴纸采用单独许可，主代码的 MIT 许可不覆盖这些素材。

## 原始中文记录（历史快照）

## 004 Huashu Design

仓库：[alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design)

### 1. 简介

面向智能体的 HTML 原生设计技能。可制作网页、App 原型、可编辑 PPTX、动画和信息图。

### 2. 适用场景

制作网页与 App 原型。制作可编辑演示文稿。设计信息图或小红书图文。比较多个视觉方向。

### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 网页和App原型 | 生成 HTML 原型，组织多屏、点击和状态交互。 | 能做什么 / iOS App 原型 |
| 幻灯片与PPTX | 制作浏览器演示的 HTML deck，并导出保留文本框的可编辑 PPTX。 | 能做什么 / HTML Slides → 可编辑 PPTX |
| 时间轴动画 | 提供动画输出流程，可交付 MP4、GIF 等。 | 能做什么 / Motion Design 引擎 |
| 信息图与图文 | 制作信息图、可视化及 3:4 小红书图文，支持图片或 PDF 等输出。 | 能做什么 / 信息图 / 数据可视化 |
| 多个视觉方向 | 先形成六个缩略候选，再挑三个方向制作真实视觉供比较。 | 设计方向顾问（Fallback） |
| 品牌与设计检查 | 读取提供的品牌资产，结合外观账本、设计体检及评审流程约束结果。 | 品牌资产协议 / 越用越懂你：经验、外观账本与设计体检 |

官方来源入口：[官方 README](https://github.com/alchaincyf/huashu-design/blob/master/README.md)。 能力按原卡核对日期理解。

### 4. 使用限制

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

### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/alchaincyf/huashu-design/blob/master/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- Claude Code、Codex、Cursor 等支持 skills 的智能体
- 本地脚本及HTML渲染/导出流程

### 6. 替代选择

- [VoltAgent/awesome-design-md](../awesome-design-md/README.zh-CN.md)：本项目提供设计与制作流程；后者提供 DESIGN.md 设计规范，适合作为风格输入。
- [alchaincyf/huashu-art-motion](../huashu-art-motion/README.zh-CN.md)：本项目覆盖网页、演示文稿与图文；后者集中于艺术动画和解说片段。

### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/alchaincyf/huashu-design/blob/master/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/004_alchaincyf-huashu-design.md`。
