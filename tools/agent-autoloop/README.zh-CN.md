# Agent Autoloop

简体中文 | [English](README.en.md) | [全部导入记录](../../docs/imports/2026-11-15.md)

## 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

当前资格请运行 `python3 scripts/catalog.py search agent-autoloop --all`（仓库根目录）。Star 和时间数据见 [GitHub 快照](../../data/github/agent-autoloop.json)，核对依据见 [元数据](tool.json)。

## 原始中文记录（历史快照）

## 033 Agent Autoloop

仓库：[KKKKhazix/agent-autoloop](https://github.com/KKKKhazix/agent-autoloop)

### 1. 简介

把命令行智能体接入事件调度和后台执行。支持人工卡片、回答后继续、定时复查、日志重放及可选 PR 交付。

### 2. 适用场景

下表按官方现成场景模板整理。使用前需要填写自己的目录、数据来源、助手和通知配置。

| 想做的事情 | 它可以怎样帮忙 | 结果或后续动作 |
| --- | --- | --- |
| 每天自动写早报 | 定时整理本地笔记和 Git 提交。 | 生成按日期保存的本地 Markdown 早报。 |
| 跟进 GitHub Issue | 定期查新 Issue，交给编码助手阅读并修改本地代码。 | 通知用户查看修改。官方模板默认不提交、不推送、不回复 Issue。 |
| 排查线上告警 | 接收错误事件，让助手对照代码查原因。 | 需要重启服务时发卡片询问，收到决定后继续。 |
| 跟进用户反馈 | 读取反馈当前状态，组织修复、核实交付结果并准备回复。 | 需要决定时通过飞书询问，回答后继续。 |
| 定时巡检网站 | 固定脚本检查网站状态和关键内容，异常时交给助手排查。 | 持续异常不重复提醒，恢复后更新原卡片。 |
| 整理飞书周报和业务摘要 | 按本人权限读取汇报及指定表格，生成本地摘要。 | 飞书发送简短摘要，完整稿保存在本机。 |
| 跟进 PR 到发布 | 按标签和配置启动审查，等待持续集成（CI）检查、合并和发布。 | 配置健康接口后，继续核对线上版本。 |
| 委托另一个助手处理网页 | 使用浏览器交接模板，把网页步骤交给已配置的助手入口。 | 网页步骤结束后，由原任务继续跟进。浏览器工具需要另外配置。 |

场景模板见[官方 README](https://github.com/KKKKhazix/agent-autoloop/blob/cecec75be3ca26e6ca1d6833b50152ee9450088d/README.md#拿来即用的场景模板)。巡检模板在正常时只运行固定脚本，异常时才调用模型。

### 3. 主要功能

| 功能 | 对日常使用的帮助 |
| --- | --- |
| 定时触发 | 每天、每周或按设定频率自动运行任务。 |
| 外部事件触发 | GitHub、HTTP 接口及轮询脚本发现新事情后，把任务交给助手。 |
| 多助手接入 | 内置 Claude Code、Codex、智能体客户端协议（ACP）和通用命令接入。 |
| 按规则分派 | 为不同任务指定助手、工作目录和任务说明。 |
| 人工问题卡片 | 把需要用户选择的事项发出来，回答后继续执行。 |
| 延后复查 | 约定时间再检查进展，例如稍后核实发布结果。 |
| 排队与并发 | 控制同组任务同时运行的数量，合并排队期间到来的同事项事件。 |
| 会话接续与失败重试 | 尽量沿用原会话，临时失败后延迟重试。 |
| 状态与历史查询 | 通过命令行查看任务、回答问题、停止执行，以及追查运行过程。 |
| 用量查看 | 汇总今天及最近 7 天已结束轮次的已上报 Token 和费用。 |
| 插件扩展 | 替换或新增事件来源、助手、通知通道和交付流程。 |

**通知与回答通道**

- 桌面通知：在本机提醒，使用命令行查看和回答。
- 飞书：发送问题卡片，支持按钮回答和卡片更新。
- 钉钉、企业微信、Slack、Discord：通过 Webhook 模板发送通知，使用回答链接作决定。
- 命令行和模型上下文协议（MCP）：查看及回答卡片。

通道需要各自配置。使用回答链接时，链接地址必须能从回答设备访问。官方对部分通道和业务模板只做了本地模拟验证。

官方来源入口：[官方 README](https://github.com/KKKKhazix/agent-autoloop/blob/cecec75be3ca26e6ca1d6833b50152ee9450088d/README.md)。 能力按原卡核对日期理解。

### 4. 使用限制

- 支持 macOS、Linux。官方要求 Node.js ≥24、Git、curl。
- 需要本机已安装并登录的命令行助手。模型调用使用自己的账号和额度。
- GitHub Issue 轮询和 PR 交付另需已登录的 GitHub CLI（`gh`）。
- 机器和中台需要保持运行。只使用本地定时或轮询时，无需开放公网端口；Webhook 需要来源能够连接中台。
- 浏览器、业务接口和飞书资料读取需要已有工具与访问权限。
- 失败后可能重复执行，发信和发布动作需要先核实当前状态。
- 代码采用 MIT 许可。实际能力取决于所接助手、任务说明和工具权限。

### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/KKKKhazix/agent-autoloop/blob/cecec75be3ca26e6ca1d6833b50152ee9450088d/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

其他入口：[安装说明](https://github.com/KKKKhazix/agent-autoloop/blob/cecec75be3ca26e6ca1d6833b50152ee9450088d/INSTALL.md)、[配置手册](https://github.com/KKKKhazix/agent-autoloop/blob/cecec75be3ca26e6ca1d6833b50152ee9450088d/skills/agent-autoloop/SKILL.md)。

### 6. 替代选择

- [chenhg5/cc-connect](../cc-connect/README.zh-CN.md)：本项目负责事件调度、后台执行和延后复查；后者侧重通过聊天平台操作已有编程助手。

### 7. 复核说明

- 知识库记录日期：2026-11-04；卡片最后确认日期：2026-11-05。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 核对版本：`v1.0.0`，提交 `cecec75be3ca26e6ca1d6833b50152ee9450088d`。
- 信息口径：根据官方文档整理功能与用途；未安装实测。

功能卡采用 v1.0.0 固定提交，官方来源确认日期为 2026-11-04。2026-11-05 的日期还包含运行机制专题入口更新，两者版本口径不合并。

**来源与版本记录**

- [官方 README](https://github.com/KKKKhazix/agent-autoloop/blob/cecec75be3ca26e6ca1d6833b50152ee9450088d/README.md)：项目定位、功能、场景模板与通道。
- [安装说明](https://github.com/KKKKhazix/agent-autoloop/blob/cecec75be3ca26e6ca1d6833b50152ee9450088d/INSTALL.md)：运行环境与接入条件。
- [配置手册](https://github.com/KKKKhazix/agent-autoloop/blob/cecec75be3ca26e6ca1d6833b50152ee9450088d/skills/agent-autoloop/SKILL.md)：规则、助手、通道和交付配置。
- [通信协议](https://github.com/KKKKhazix/agent-autoloop/blob/cecec75be3ca26e6ca1d6833b50152ee9450088d/docs/protocol.md)：人工问答、延后复查、会话接续与失败重试。

来源确认日期均为 2026-11-04。项目后续版本可能变化，使用前复核当前说明。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/033_KKKKhazix-agent-autoloop.md`。
