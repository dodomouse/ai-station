# AI Berkshire

简体中文 | [English](README.en.md) | [全部导入记录](../../docs/imports/2026-11-15.md)

## 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

当前资格请运行 `python3 scripts/catalog.py search ai-berkshire --all`（仓库根目录）。Star 和时间数据见 [GitHub 快照](../../data/github/ai-berkshire.json)，核对依据见 [元数据](tool.json)。

## 原始中文记录（历史快照）

## 028 AI Berkshire

仓库：[xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire)

### 1. 简介

基于 Claude Code 与 Codex 的价值投资研究技能。通过多个分析视角组织公司研究、财报、估值、组合复盘和论点跟踪。

### 2. 适用场景

组织上市公司深度研究。精读财报与复核估值。并行比较多个分析视角。跟踪投资论点和组合变化。

### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 公司与估值研究 | 提供公司深研、内在价值、现金流、SOTP和反向估值等入口。 | Skills 一览 / 深度研究类 |
| 多视角并行研究 | 团队型技能调度多个投资方法视角独立研究并互相挑战。 | 整体架构 / 多Agent并行 |
| 财报精读 | earnings-review强调阅读原始财报，团队入口可组织多视角精读。 | 财报分析类 |
| 行业与初筛 | 提供行业研究、漏斗筛选、质量筛选及买入前检查表。 | 行业筛选类 |
| 组合与论点跟踪 | 覆盖组合复盘、投资论点持续跟踪和两份报告的漂移检查。 | 持仓管理类 |
| 数据核对规范 | 提供财务数据获取、独立来源交叉核对和精确计算规范。 | 金融数据的精确性 / 思维工具类 |
| Claude Code和Codex入口 | 同一工作流提供Claude Code commands与Codex skills。 | 快速开始 |

官方来源入口：[官方 README](https://github.com/xbtlin/ai-berkshire/blob/main/README.md)。 能力按原卡核对日期理解。

### 4. 使用限制

**平台与环境**

- 取决于Claude Code/Codex运行环境；README含macOS、Linux、Windows安装指引

- MIT开源；需要用户自己的AI客户端及模型服务。
- README明确深度投研多轮、多Agent流程token消耗较高。
- 较强模型与更完整研究可能增加成本，不是免费投研算力。

- 多视角是提示与工作流设计，不能当成大师本人背书。
- README展示的历史收益、质量宣传和部分客户端能力未独立核实。
- 未运行任何研究或投资评估，报告不是确定性收益保证。

**容易找错的需求（不属于本项目能力）**

- 照着输出交易就能复制作者宣传的收益率。
- 无需数据或模型额度就能免费自动理财。

### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/xbtlin/ai-berkshire/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- Claude Code commands
- Codex skills
- 计算、检索、报告抽检工具

### 6. 替代选择

- [simonlin1212/Vibe-Research](../vibe-research/README.zh-CN.md)：本项目以多个分析视角组织公司研究；后者另含自选、持仓、研报库和历史回测。

### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/xbtlin/ai-berkshire/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/028_xbtlin-ai-berkshire.md`。
