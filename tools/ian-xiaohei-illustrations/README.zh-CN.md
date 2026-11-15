# Ian Xiaohei Illustrations

简体中文 | [English](README.en.md) | [全部导入记录](../../docs/imports/2026-11-15.md)

## 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

当前资格请运行 `python3 scripts/catalog.py search ian-xiaohei-illustrations --all`（仓库根目录）。Star 和时间数据见 [GitHub 快照](../../data/github/ian-xiaohei-illustrations.json)，核对依据见 [元数据](tool.json)。

检查最近 5 个默认分支提交，窗口内可见的是 README 与联系信息更新；未据此确认有效功能维护。

## 原始中文记录（历史快照）

## 015 Ian Xiaohei Illustrations

仓库：[helloianneo/ian-xiaohei-illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations)

### 1. 简介

为中文正文生成白底手绘“小黑”风格的 PNG 插图。技能先提炼文章观点，再规划分镜并生成配图。

### 2. 适用场景

为中文技术文章配图。把抽象概念画成手绘隐喻。先规划一篇文章的配图清单。

### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 文章配图规划 | 读取文章或主题，识别认知锚点。可先只输出放置位置、主题、结构和标注的 shot list。 | 只做配图规划 / 工作流程 |
| 统一小黑视觉语言 | 默认采用白底、黑色手绘线条、少量红橙蓝中文批注。小黑角色参与核心动作。 | 视觉风格 |
| 生成正文 PNG | 默认生成 16:9 横版正文插图，并保存到文章对应资源目录。 | 它会产出什么 |
| 概念与流程隐喻 | 可将判断、流程、结构、状态或隐喻转为解释图，每张图集中表达一个核心意思。 | 这个仓库是什么? / 工作流程 |
| 现有图片调整 | README 提供删除现有图中多余标题或错误文字的使用例子。实际编辑仍需图像模型支持。 | 去掉图里的标题或错误文字 |
| 生成后检查 | 检查白底、留白、角色动作和中文标注。遇到错字、幻觉标签或风格漂移时需要修正或重生成。 | 工作流程 / 注意事项 |

官方来源入口：[官方 README](https://github.com/helloianneo/ian-xiaohei-illustrations/blob/main/README.md)。 能力按原卡核对日期理解。

### 4. 使用限制

**平台与环境**

- 面向 Codex 的技能目录；README 不给出独立桌面应用
- 实际运行平台取决于所用 Codex 与图像工具

- 技能代码标示 MIT。图像生成和编辑依赖所用模型或工具，其额度与费用独立；MIT 不代表生图免费。

- 默认不输出 PPTX、PDF、Keynote、SVG、HTML 或 Canvas 可编辑图。
- 不是传统复杂架构图、精细商业插画或封面 KV 的通用模板。
- 中文标注宜短，生成后需检查错字与虚构标签。

**容易找错的需求（不属于本项目能力）**

- 不匹配“交付能逐个编辑形状的 SVG 或 PPTX”的要求。
- 不匹配“把整篇长文全部文字塞进一张信息图”的需求。

### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/helloianneo/ian-xiaohei-illustrations/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- Codex Skill
- 自然语言规划指令
- 由智能体调用图像生成或编辑能力

### 6. 替代选择

- [alexgreensh/anidoodle](../anidoodle/README.zh-CN.md)：本项目根据中文文章规划并生成小黑风格 PNG；后者用代码描述笔画，并支持逐笔动画。

### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/helloianneo/ian-xiaohei-illustrations/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/015_helloianneo-ian-xiaohei-illustrations.md`。
