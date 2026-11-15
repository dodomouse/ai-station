# Orca（智能体开发工作台）

简体中文 | [English](README.en.md) | [全部导入记录](../../docs/imports/2026-11-15.md)

## 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

当前资格请运行 `python3 scripts/catalog.py search orca --all`（仓库根目录）。Star 和时间数据见 [GitHub 快照](../../data/github/orca.json)，核对依据见 [元数据](tool.json)。

## 原始中文记录（历史快照）

## 023 Orca（智能体开发工作台）

仓库：[stablyai/orca](https://github.com/stablyai/orca)

### 1. 简介

统一管理多个编程智能体的开发工作台。提供并行工作目录、终端、差异审查、手机端及 SSH 远程环境。

### 2. 适用场景

并行推进多个编程任务。在同一工作台审查智能体修改。用手机或 SSH 跟进远程开发任务。

### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 并行智能体与 worktree | 可在各自隔离 Git worktree 中运行不同智能体，并比较或合并结果。 | Features / Parallel Worktrees |
| 终端与编辑器工作台 | 提供可分屏终端、保留滚动记录，以及文件编辑和拖入 Agent 的交互。 | Features / Terminal Splits / Drag Files to Agents |
| 手机伴随应用 | 手机配对桌面后可监控任务、接收完成通知并发送后续指令。 | Features / Mobile Companion / Install |
| SSH 远程工作环境 | 在远程机器运行智能体，提供文件编辑、Git、终端、重连和端口转发。 | Features / SSH Worktrees |
| 网页设计定位 | 内嵌 Chromium 的 Design Mode 可将被选元素的 HTML、CSS 和局部截图发给 Agent。 | Features / Design Mode |
| 差异审查与反馈 | 可在 diff 的代码行上添加评论并发送回 Agent，继续审查、编辑或提交。 | Features / Annotate AI Diffs |
| 任务与代码托管集成 | 在应用中浏览 GitHub 和 Linear 的 PR、issue 与项目看板，并从任务进入工作区。 | Features / GitHub & Linear, Native |

官方来源入口：[官方 README](https://github.com/stablyai/orca/blob/main/README.md)。 能力按原卡核对日期理解。

### 4. 使用限制

**平台与环境**

- macOS（Apple Silicon 与 Intel）、Windows、Linux 桌面
- iOS、Android 手机伴随应用
- 具备 SSH 的远程运行环境

- 工作台代码按 MIT 开源，README 写 free and open source。
- 所选编程智能体、模型订阅或 API 和远程机器成本另计。
- 手机配对中继和具体托管服务是否收费，README 没有完整价格表，需用前核对。

- 并行隔离依赖 Git worktree，不能据此自动获取创建分支权限。
- 手机端用于配对桌面，不应理解为手机独立承担所有模型和开发环境。
- 功能描述来自 README，未安装、运行或测量效率提升。

**容易找错的需求（不属于本项目能力）**

- 不是 Plotly 的同名图形导出 Orca。
- 不是把本地 Agent 接入飞书或钉钉的 cc-connect 类消息桥。

### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/stablyai/orca/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- 桌面 GUI 与集成终端
- 内嵌 Chromium / Design Mode
- iOS 与 Android 伴随应用
- SSH 连接

### 6. 替代选择

- [chenhg5/cc-connect](../cc-connect/README.zh-CN.md)：本项目集中管理开发工作区、终端和差异审查；后者把本机编程助手接到聊天平台。
- [reason-machines/reason-network](../reason-network/README.zh-CN.md)：本项目组织开发任务；后者共享团队助手的会话概况并提供通信。

### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/stablyai/orca/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/023_stablyai-orca.md`。
