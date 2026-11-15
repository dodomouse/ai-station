# Vibe Research

简体中文 | [English](README.en.md) | [全部导入记录](../../docs/imports/2026-11-15.md)

## 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

当前资格请运行 `python3 scripts/catalog.py search vibe-research --all`（仓库根目录）。Star 和时间数据见 [GitHub 快照](../../data/github/vibe-research.json)，核对依据见 [元数据](tool.json)。

## 原始中文记录（历史快照）

## 022 Vibe Research

仓库：[simonlin1212/Vibe-Research](https://github.com/simonlin1212/Vibe-Research)

### 1. 简介

面向 A 股、美股和港股的投研工作台。整合自选、持仓、每日复盘、产业与公司研究、历史回测和研报库。

### 2. 适用场景

整理自选与持仓流水。生成公司或产业研究报告。检索自有 PDF/Word 研报。验证历史回测想法。

### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 自选与持仓 | 按交易流水记录持仓，展示盈亏、集中度等，并有事件日历。 | 功能 / 我的股票 |
| 每日复盘与资讯 | 整理市场状态、资金、产业资讯和行业信号。 | 每日复盘 / 产业研究 |
| 公司研究 | 按公司画像、财务、盈利预期、估值、风险和报告开展研究。 | 个股深挖 / 功能总览 |
| 研报库 | 导入PDF/Word等资料，检索、提问并回查引用原文。 | 功能总览 / 我的研报 |
| 回测与研究记录 | 用对话描述想法做历史回测，并保存报告、辩论和研究记录。 | 回测 / 研究记录 |
| AI来源接入 | 使用已登录Claude Code、Codex、WorkBuddy/CodeBuddy，或兼容模型API。 | 支持的 AI |
| MCP接口 | 向支持MCP的客户端提供取数、报告、证据和研究工具。 | 在 Claude Code / Codex / Cursor 里调用 VR |

官方来源入口：[官方 README](https://github.com/simonlin1212/Vibe-Research/blob/main/README.md)。 能力按原卡核对日期理解。

### 4. 使用限制

**平台与环境**

- 源码支持macOS、Linux、Windows；Node≥22.18、Python≥3.11
- Windows/macOS免安装包；README说明并非全部平台均实机验收
- 远程访问仅macOS/Linux

- MIT开源；AI订阅/API需用户自行提供，产品不附赠额度。
- 只取数、读报告与证据无需AI；发起研究会消耗所选AI额度。
- 外部数据及模型服务可用性和费用另计。

- 不能下单交易；多空辩论及MCP发起研究目前只支持A股。
- 第三方数据可能延迟、缺失或有误，端点存在不保证随时可用。
- 模型API需支持Chat Completions与工具调用，README未把所有模板标成实测。
- ADR与本地股换股比例本版不处理；本轮未运行研究或回测。

**容易找错的需求（不属于本项目能力）**

- 直接连接券商自动买卖股票。
- 保证研报全部事实正确并给出稳赚收益。

### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/simonlin1212/Vibe-Research/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- 本地浏览器页面
- MCP（7个只读工具、1个研究发起工具）
- 命令行研究入口
- Claude Code/Codex/WorkBuddy/CodeBuddy订阅与Chat Completions API

### 6. 替代选择

- [xbtlin/ai-berkshire](../ai-berkshire/README.zh-CN.md)：本项目是含持仓、研报库和回测的投研工作台；后者以技能组织财报、估值与投资论点研究。

### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/simonlin1212/Vibe-Research/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/022_simonlin1212-Vibe-Research.md`。
