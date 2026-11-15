# Spec Kit

简体中文 | [English](README.en.md) | [全部导入记录](../../docs/imports/2026-11-15.md)

## 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

当前资格请运行 `python3 scripts/catalog.py search spec-kit --all`（仓库根目录）。Star 和时间数据见 [GitHub 快照](../../data/github/spec-kit.json)，核对依据见 [元数据](tool.json)。

## 原始中文记录（历史快照）

## 013 Spec Kit

仓库：[github/spec-kit](https://github.com/github/spec-kit)

### 1. 简介

提供规格驱动开发的 CLI、技能和模板。把需求规格转换为计划、任务和代码，并支持检查与缺陷修复流程。

### 2. 适用场景

按规格组织新功能开发。将需求拆成计划和可执行任务。建立团队共用开发模板与流程。组织缺陷修复流程。

### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 规格驱动开发 | 从原则和需求规格进入计划、任务、实现和收敛检查。 | Spec-Driven Development |
| 独立缺陷流程 | bug扩展分评估、修复、测试，输出修复验证报告。 | Bug fixing |
| 想法评估 | assess扩展组织证据，给出继续、澄清或停止判断。 | Idea assessment |
| 流程定制 | 用扩展、预设、工作流、覆盖层和自定义步骤组装流程。 | Capabilities |
| 团队与目录 | 通过Bundle和Catalog分发团队选用的组件，支持本地源与自托管目录。 | Capabilities |
| 多智能体集成 | 通过Integration接入或切换编码智能体。 | Capabilities / Supported AI coding agent integrations |

官方来源入口：[官方 README](https://github.com/github/spec-kit/blob/main/README.md)。 能力按原卡核对日期理解。

### 4. 使用限制

**平台与环境**

- Linux
- macOS
- Windows；README要求Python 3.11+与uv

- 工具开源MIT；所用编码智能体订阅/API、外部服务和运行环境费用另计。

- 需要受支持的AI编码智能体。
- SDD在核心内，Bug和想法评估需按需安装扩展。
- 社区目录不代表审计或官方背书；本轮未安装执行。

**容易找错的需求（不属于本项目能力）**

- 不用任何模型或开发环境就自动完成软件交付。
- 保证一套规格能证明系统绝无缺陷。

### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/github/spec-kit/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- Specify命令行
- 受支持编码智能体中的技能/命令
- 扩展、预设、Workflow、Bundle、Catalog

### 6. 替代选择

- [mattpocock/skills](../skills/README.zh-CN.md)：本项目提供规格、计划和任务模板的开发流程；后者按工程任务提供独立技能。

### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/github/spec-kit/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/013_github-spec-kit.md`。
