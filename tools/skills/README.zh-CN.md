# Skills For Real Engineers（Matt Pocock）

简体中文 | [English](README.en.md) | [全部导入记录](../../docs/imports/2026-11-15.md)

## 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

当前资格请运行 `python3 scripts/catalog.py search skills --all`（仓库根目录）。Star 和时间数据见 [GitHub 快照](../../data/github/skills.json)，核对依据见 [元数据](tool.json)。

## 原始中文记录（历史快照）

## 017 Skills For Real Engineers（Matt Pocock）

仓库：[mattpocock/skills](https://github.com/mattpocock/skills)

### 1. 简介

面向编程智能体的工程技能集合。覆盖需求澄清、架构决策、测试驱动开发、重构和任务组织。

### 2. 适用场景

为 Claude Code 或 Codex 补充工程技能。在编码前澄清需求与记录设计决定。组织测试驱动开发及重构任务。

### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 需求访谈与文档化 | grill-me 与 grill-with-docs 通过访谈澄清目标；工程版本同步形成领域词汇和 ADR。 | Why These Skills Exist / Reference |
| 领域模型与架构设计 | domain-modeling、codebase-design 和 improve-codebase-architecture 约束术语、模块边界并寻找架构改进点。 | Reference / Engineering |
| 规格与任务拆分 | to-spec 汇总讨论形成规格，to-tickets 拆成声明依赖关系的纵向切片任务。 | Reference / Engineering |
| 测试驱动实现 | tdd 使用 red-green-refactor；implement 按约定接口或边界驱动实现并执行评审。 | Reference / Engineering |
| 故障诊断与代码审查 | diagnosing-bugs 建立复现和假设验证循环；code-review 分别核对规范与规格。 | Reference / Engineering |
| 大型任务与多智能体安排 | wayfinder 维护超出单会话的大任务地图，implement-spec 描述按任务依赖并发执行。 | Reference / Engineering |
| 通用知识工作技能 | research、writing-for-agents、teach 等用于资料调查、编写智能体文档和教学。 | Reference / Productivity |

官方来源入口：[官方 README](https://github.com/mattpocock/skills/blob/main/README.md)。 能力按原卡核对日期理解。

### 4. 使用限制

**平台与环境**

- Claude Code、Codex、GitHub Copilot、Gemini CLI 等支持技能的助手

- 技能仓库采用 MIT；技能文件本身不提供模型算力。
- 运行使用所选助手的订阅或 API；issue tracker 和其他工具成本另计。
- 不要在同一助手混装插件和复制式技能，否则可能重复。

- 是可组合工程方法，不是独立 Agent Runtime。
- README 区分用户主动调用与模型可调用的技能。
- 某些技能涉及提交、创建任务或外部服务；使用时仍服从具体仓库授权。
- 本次只读功能说明，未安装或执行任何技能。

**容易找错的需求（不属于本项目能力）**

- 不是免费模型额度领取或请求转发服务。
- 不是自动扫描并直接保证架构正确的静态分析器。

### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/mattpocock/skills/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- 各助手的插件安装方式
- skills.sh 可编辑技能文件
- 斜杠命令与按适用任务调用的技能

### 6. 替代选择

- [github/spec-kit](../spec-kit/README.zh-CN.md)：本项目提供需求、设计、测试和重构技能；后者围绕规格组织计划、任务及实现。
- [xstongxue/best-skills](../best-skills/README.zh-CN.md)：本项目聚焦工程技能；后者的范围还包括论文、汇报、自媒体和图表。

### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/mattpocock/skills/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/017_mattpocock-skills.md`。
