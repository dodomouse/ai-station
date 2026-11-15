# cc-connect

简体中文 | [English](README.en.md) | [全部导入记录](../../docs/imports/2026-11-15.md)

## 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

当前资格请运行 `python3 scripts/catalog.py search cc-connect --all`（仓库根目录）。Star 和时间数据见 [GitHub 快照](../../data/github/cc-connect.json)，核对依据见 [元数据](tool.json)。

当前 README 自称 MIT，但仓库根目录未找到许可证文件，API 许可证为空。原卡的 MIT 描述保留为历史记录。

## 原始中文记录（历史快照）

## 005 cc-connect

仓库：[chenhg5/cc-connect](https://github.com/chenhg5/cc-connect)

### 1. 简介

把本机编程智能体接入聊天平台，包括飞书和钉钉。从聊天端管理会话、切换模型、安排任务及传递文件。

### 2. 适用场景

从手机远程使用本机编程助手。通过飞书或钉钉触发自动化任务。管理多个项目与智能体会话。

### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 连接本地编程智能体 | 把本机 Claude Code、Codex、Cursor Agent 等智能体接入聊天平台，也支持符合 ACP 的智能体。 | Why cc-connect? / Universal Agent Support |
| 接入聊天平台 | 支持飞书、钉钉、Telegram、Slack、Discord 等；README 的矩阵分别列出文字、附件和语音差异。 | Platform feature snapshot / Platform Flexibility |
| 聊天端会话与模型控制 | 提供会话管理、模型与推理等级切换、权限模式选择和工作目录切换。 | Complete Chat Control / Session Management |
| 多项目和机器人协作 | 一个进程可以绑定多个项目与平台；Multi-Bot Relay 允许群聊中的机器人相互转发。 | Multi-Agent Orchestration / Multi-Project Architecture |
| 定时任务 | 可通过自然语言或相关命令安排 cron 类任务。 | Intelligent Scheduling / Scheduled Tasks |
| 图片、语音与文件传递 | 按平台能力转发图片或语音，并允许智能体回传文件；语音转写和合成需相应服务配置。 | Multimodal Support / Agent Attachment Send-Back |
| 操作系统用户隔离 | run_as_user 选项可把项目绑定到指定系统用户运行。 | OS-User Isolation (`run_as_user`) |

官方来源入口：[官方 README](https://github.com/chenhg5/cc-connect/blob/main/README.md)。 能力按原卡核对日期理解。

### 4. 使用限制

**平台与环境**

- 可运行 Go 发行二进制的本机环境
- 飞书、钉钉、Slack、Telegram、Discord、企业微信等聊天平台，能力各有差异

- 代码采用 MIT，可自行部署桥接进程。
- 不提供模型额度；所接入智能体的订阅或 API、语音服务等按提供方计费。
- 聊天平台的机器人配置、服务限制和可用性另行确认。

- 智能体 CLI 必须先安装和认证。
- 多数平台无需公网 IP，不能推广到所有连接模式。
- 语音、群聊和附件支持以 README 平台矩阵为准。
- 本次没有配置平台、运行任务或发送消息。

**容易找错的需求（不属于本项目能力）**

- 不是独立大模型或可免费无限调用 AI 的服务。
- 不是自带完整桌面 IDE 的 Orca 类工作台。

### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/chenhg5/cc-connect/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- 聊天机器人
- 本地 Web 配置界面
- cc-connect CLI
- ACP 智能体连接

### 6. 替代选择

- [KKKKhazix/agent-autoloop](../agent-autoloop/README.zh-CN.md)：本项目侧重从聊天平台操作本机助手；后者侧重事件触发、后台排队和人工回答后的继续执行。

### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/chenhg5/cc-connect/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/005_chenhg5-cc-connect.md`。
