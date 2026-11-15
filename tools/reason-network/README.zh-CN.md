# Reason Network

简体中文 | [English](README.en.md) | [全部导入记录](../../docs/imports/2026-11-15.md)

## 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

当前资格请运行 `python3 scripts/catalog.py search reason-network --all`（仓库根目录）。Star 和时间数据见 [GitHub 快照](../../data/github/reason-network.json)，核对依据见 [元数据](tool.json)。

代码提供 MIT 或 Apache-2.0 双许可。快照保留 API 的 Apache-2.0 字段，并用对应许可证文件建立指纹。

## 原始中文记录（历史快照）

## 041 Reason Network

仓库：[reason-machines/reason-network](https://github.com/reason-machines/reason-network)

### 1. 简介

每台电脑运行后台程序，共享团队 Agent 会话的人员、设备、项目、分支与工作概况。

### 2. 适用场景

- 让我的 Codex 找同事的 Claude Code。
- 不同电脑上的 Agent 直接传话。
- 谁的 Agent 正在改哪个仓库和分支。

### 3. 主要功能

- 每台电脑运行后台程序，共享团队 Agent 会话的人员、设备、项目、分支与工作概况。
- 工具包括 list_team、send_message、message_status 和 ask_user。不同宿主的消息送达时机不同。
- 局域网或互联网尝试点对点连接，无法直连时使用中继。官方声明传输端到端加密，并支持自有中继。
- 支持多个宿主，例如 Claude Code、Codex、Cursor 和 Gemini CLI。托管助手可通过模型上下文协议（MCP）接入。

官方来源入口：[官方 README](https://github.com/reason-machines/reason-network/blob/main/README.md)。 能力按原卡核对日期理解。

### 4. 使用限制

需要安装后台程序、登录账号并加入网络。团队可见会话元信息，可按文件夹排除。消息送达或被回复不等于任务完成。PDF 称文件冲突提醒仍在开发，本次未把它认定为已交付能力，也未验证跨机加密实现。

知识卡未提供完整部署费用或付费服务价格；未记录的费用项目需要另行核对。

### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/reason-machines/reason-network/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

### 6. 替代选择

- [stablyai/orca](../orca/README.zh-CN.md)：本项目共享团队助手的会话概况并支持通信；后者侧重同一开发工作台内的任务与差异管理。

### 7. 复核说明

- 知识库记录日期：2026-11-06；卡片最后确认日期：2026-11-06。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 核验范围：已读取官方 README 和仓库元数据。公开仓库，核验时未归档或禁用；本次未安装或运行。

**来源与版本记录**

- [官方 README](https://github.com/reason-machines/reason-network/blob/main/README.md)，读取日期：2026-11-06。
- [仓库元数据](https://api.github.com/repos/reason-machines/reason-network)，仓库 ID：`1422344223`。
- 本次读取的 README Git blob SHA：`f3c7d074cdb8a7a835e3a1dc491d211723880153`。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/041_reason-machines-reason-network.md`。
