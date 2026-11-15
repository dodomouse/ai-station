# Anatomy

简体中文 | [English](README.en.md) | [全部导入记录](../../docs/imports/2026-11-15.md)

## 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

当前资格请运行 `python3 scripts/catalog.py search anatomy --all`（仓库根目录）。Star 和时间数据见 [GitHub 快照](../../data/github/anatomy.json)，核对依据见 [元数据](tool.json)。

## 原始中文记录（历史快照）

## 027 Anatomy

仓库：[wheresryan22/anatomy](https://github.com/wheresryan22/anatomy)

### 1. 简介

用交互式等轴测图解释机械、仪器和抽象机制。生成 SVG、HTML 或 React 组件，可叠加 WebGL 与 3D 效果。

### 2. 适用场景

制作交互式原理说明图。用机械隐喻解释软件概念。绘制机器或仪器的结构示意。

### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 机制转物理模型 | 将技术概念映射为可运作的实体模型，如锁、机械装置或仪器，借其动作解释原理。 | 简介 / How it works |
| 等轴测 SVG 绘图 | 核心用带明暗层次的等轴测零件组成图示，支持指针、键盘交互和运动。 | What it makes |
| WebGL 视觉层 | 可在 SVG 图层间加入火焰、水、光等着色器效果，并保持相同相机关系。 | What it makes |
| 试验性 3D 运动 | 3D 模式可让局部零件真正旋转或重新投影。README 明确标为 beta。 | What it makes / Limits |
| 模型驱动读数 | 读数和零件运动由同一个小模型驱动，适合解释仪器或机制的因果变化。 | 简介 / How it works |
| 可嵌入交付 | 可输出独立 HTML、带样式的 SVG 或 React/Next.js 组件，并提供图像采集与几何检查脚本。 | What it makes / Requirements |

官方来源入口：[官方 README](https://github.com/wheresryan22/anatomy/blob/main/README.md)。 能力按原卡核对日期理解。

### 4. 使用限制

**平台与环境**

- 可由 Claude Code、Codex、Antigravity、OpenCode、MiniMax Code 等支持技能的助手使用
- 生成与检查使用 Node.js 及 Chrome/Chromium；React 输出另需 React
- 图示可在兼容浏览器查看，WebGL 和减少动态效果设置会改变呈现

- 代码为 MIT。技能工具包使用 Node 内置模块，不要求专属生图 API；所用编程助手、模型及可选托管仍可能收费。无需专属 key 不等于所有使用成本为零。

- 3D 模式为 beta；不把示例表现当成所有项目的性能保证。
- 适合机器、仪器、工具和机制，不适合人物或精确地图。
- 不是数据图表库，没有通用坐标轴与序列绘图接口。
- 制作需零件、几何、交互和检查步骤，不承诺一键即时完成。

**容易找错的需求（不属于本项目能力）**

- 不匹配“生成出版级科学曲线或统计图表”的需求。
- 不能据此承诺工程精度、真实材料参数或受力仿真的正确性。

### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/wheresryan22/anatomy/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- Agent Skill，自然语言调用
- Node 内置模块脚本
- 浏览器 SVG/WebGL
- React/Next.js 输出接口

### 6. 替代选择

- [elvarofficial/teardown](../teardown/README.zh-CN.md)：本项目侧重交互式等轴测说明图；后者侧重可运动、拆解和剖视的 3D 机械演示。

### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/wheresryan22/anatomy/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/027_wheresryan22-anatomy.md`。
