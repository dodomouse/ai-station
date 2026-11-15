# Horizon：AI 信息聚合与双语新闻简报

简体中文 | [English](README.en.md) | [全部导入记录](../../docs/imports/2026-11-15.md)

## 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

当前资格请运行 `python3 scripts/catalog.py search horizon --all`（仓库根目录）。Star 和时间数据见 [GitHub 快照](../../data/github/horizon.json)，核对依据见 [元数据](tool.json)。

## 原始中文记录（历史快照）

## 058 Horizon：AI 信息聚合与双语新闻简报

仓库：[Thysrael/Horizon](https://github.com/Thysrael/Horizon)

### 1. 简介

聚合 RSS、社区、GitHub 与新闻等信息源，按 Profile 评分、筛选和去重，生成中英双语 Markdown 日报。

### 2. 适用场景

每日汇总 AI 与技术新闻。跟踪项目 Release。提炼技术长文。通过 Pages、邮件或 Webhook 分发简报。

### 3. 主要功能

以下能力以核验版本的官方 README 为依据。

| 能力 | 具体作用与条件 |
| --- | --- |
| 多源采集 | 支持 RSS/Atom、Hacker News、Reddit、Telegram 公开频道、X、GitHub、OpenBB、OSS Insight、GDELT 与 Google News；不同来源各有配置条件。 |
| 按兴趣筛选 | 可指定或自动匹配 Profile，自定义评分、摘要及背景等区块；同一 Profile 下可合并重复话题。 |
| 控制阅读量 | 可限制日报总条数和各类内容份额，配置后才应用限额。 |
| 补充背景与讨论 | 按需搜索背景、摘要社区评论；评论采集只适用于部分信息源。 |
| 日报输出与投递 | 生成中英双语 Markdown，可发布到 GitHub Pages、邮件或 Webhook；列有飞书、钉钉、Slack、Discord 等通知渠道。微信另需 iLink Bot 登录，受回复额度限制。 |
| 助手与定时入口 | 提供 CLI、MCP 和 Agent Skill；GitHub Actions 每日工作流是默认禁用的模板，需自行配置启用。 |

官方来源入口：[官方中文 README](https://github.com/Thysrael/Horizon/blob/main/README_zh.md)。 能力按原卡核对日期理解。

### 4. 使用限制

- 环境：`pyproject.toml` 要求 Python 3.11 或以上；可用 `uv` 安装，也提供 Docker 入口。
- 模型与信息源：需配置可用的模型服务；部分来源另需凭据、服务额度或可选依赖。MIT 许可不代表模型和数据服务免费。
- 可选依赖：OpenBB 使用 `openbb` extra；`twitter` extra 涉及 Playwright，官方说明当前 Dockerfile 不会安装所需浏览器及系统组件。
- 配置与运行：在独立项目目录执行 `uv sync`、`uv run horizon-wizard` 配置来源与兴趣，再用 `uv run horizon` 生成日报。默认抓取最近 24 小时，默认结果目录为 `data/summaries/`。
- 助手入口：官方提供 `horizon` Skill 和 MCP 服务；本次只收录资料，未安装技能或接入助手。

- AI 评分和摘要属于自动处理结果，重要信息仍应回到原文核对。定时生成、站点发布和渠道推送都需要部署配置。
- [BettaFish](../bettafish/README.zh-CN.md)偏向舆情、社媒评论和多来源研究分析；Horizon 偏向持续采集与个人日常阅读简报。
- [Vibe-Research](../vibe-research/README.zh-CN.md)偏向投资研究工作台；Horizon 的金融新闻源用于信息采集，不据此推导估值或回测能力。
- [cc-connect](../cc-connect/README.zh-CN.md)把编码助手接入聊天平台；Horizon 的通知用途是投递简报与运行结果。

知识卡未提供完整部署费用或付费服务价格；未记录的费用项目需要另行核对。

### 5. 开始使用

安装与入门文档：[官方中文 README](https://github.com/Thysrael/Horizon/blob/main/README_zh.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

其他入口：[中文 README](https://github.com/Thysrael/Horizon/blob/cdd86ff263f170f1675fab5bddd3bc1dfeacc6b5/README_zh.md)、[配置指南](https://github.com/Thysrael/Horizon/blob/main/docs/configuration.md)。

初次使用所需环境及调用示例见上节“使用限制”。

### 6. 替代选择

- [KKKKhazix/agent-autoloop](../agent-autoloop/README.zh-CN.md)：本项目直接组织信息源、评分、去重和双语日报；后者提供通用的定时与事件执行框架。

### 7. 复核说明

- 知识库记录日期：2026-11-11；卡片最后确认日期：2026-11-11。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：已核对官方中英文 README、依赖清单、仓库元信息和许可；未安装运行。分类、问法和匹配理由属于检索整理判断。

**来源与版本记录**

- 当前入口：[官方中文 README](https://github.com/Thysrael/Horizon/blob/main/README_zh.md)、[英文 README](https://github.com/Thysrael/Horizon/blob/main/README.md)。
- 核验版本：默认分支 `main`，提交 [`cdd86ff263f170f1675fab5bddd3bc1dfeacc6b5`](https://github.com/Thysrael/Horizon/commit/cdd86ff263f170f1675fab5bddd3bc1dfeacc6b5)。
- 固定版本来源：[中文 README](https://github.com/Thysrael/Horizon/blob/cdd86ff263f170f1675fab5bddd3bc1dfeacc6b5/README_zh.md)、[依赖与命令入口](https://github.com/Thysrael/Horizon/blob/cdd86ff263f170f1675fab5bddd3bc1dfeacc6b5/pyproject.toml)、[MIT 许可](https://github.com/Thysrael/Horizon/blob/cdd86ff263f170f1675fab5bddd3bc1dfeacc6b5/LICENSE)。
- 后续配置入口：[配置指南](https://github.com/Thysrael/Horizon/blob/main/docs/configuration.md)、[Profile 指南](https://github.com/Thysrael/Horizon/blob/main/docs/profiles.md)、[MCP 工具](https://github.com/Thysrael/Horizon/blob/main/src/mcp/README.md)、[Agent Skill](https://github.com/Thysrael/Horizon/blob/main/docs/agent-skill.md)。这些链接供后续部署时查阅，本次未逐项验证。
- 按仓库 ID `1162410458` 去重；后续复核来源、投递渠道及环境要求时，同步更新用途索引与最后确认日期。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/058_Thysrael-Horizon.md`。
