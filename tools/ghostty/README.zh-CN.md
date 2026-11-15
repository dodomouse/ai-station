# Ghostty

简体中文 | [English](README.en.md) | [全部导入记录](../../docs/imports/2026-11-15.md)

## 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

当前资格请运行 `python3 scripts/catalog.py search ghostty --all`（仓库根目录）。Star 和时间数据见 [GitHub 快照](../../data/github/ghostty.json)，核对依据见 [元数据](tool.json)。

## 原始中文记录（历史快照）

## 012 Ghostty

仓库：[ghostty-org/ghostty](https://github.com/ghostty-org/ghostty)

### 1. 简介

使用原生界面和 GPU 渲染的终端模拟器。支持多窗口、标签页与分屏，另提供可嵌入终端库。

### 2. 适用场景

在 macOS 或 Linux 使用命令行。管理多个终端会话。为应用嵌入终端模拟能力。

### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 原生终端模拟 | 提供终端模拟与 GPU 渲染。macOS 使用 Metal，Linux 使用 OpenGL。 | About / Roadmap and Status — Competitive Performance |
| 窗口、标签与分屏 | 桌面应用支持多窗口、标签页、分屏及标签重命名等组织功能。 | Roadmap and Status — Rich Windowing Features |
| 现代终端协议 | 支持图像、剪贴板、同步渲染、明暗主题通知等现代终端控制序列。 | Roadmap and Status — Standards-Compliant Terminal Emulation |
| 平台集成 | macOS 采用 SwiftUI、CoreText 并支持 AppleScript 和 Shortcuts。Linux 使用 GTK，并可与 systemd 集成。 | Roadmap and Status — Native Platform Experiences |
| 可嵌入终端库 | 以 libghostty 提供终端嵌入能力。libghostty-vt 可供 Zig/C 使用，并覆盖桌面之外的平台。 | Roadmap and Status — libghostty |

官方来源入口：[官方 README](https://github.com/ghostty-org/ghostty/blob/main/README.md)。 能力按原卡核对日期理解。

### 4. 使用限制

**平台与环境**

- 原生桌面应用：macOS、Linux
- libghostty-vt：macOS、Linux、Windows、WebAssembly；不可等同桌面应用支持范围

- GitHub 元数据标示 MIT。终端本身不要求模型 API；在其中运行的编码助手、远程主机及其他程序可能独立收费。

- 终端模拟器不提供自身的大模型能力，也不替代 shell。
- 桌面应用与可嵌入库的平台支持和成熟度不同。
- 项目性能自述未在本轮复现。

**容易找错的需求（不属于本项目能力）**

- 不是按计划自动运行命令或管理任务队列的调度器。
- 不能仅凭 libghostty-vt 跨平台说明声称有正式 Windows 桌面版。

### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/ghostty-org/ghostty/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- 桌面图形界面
- shell/终端输入输出
- macOS AppleScript 与 Shortcuts
- libghostty 的 C/Zig 嵌入接口

### 6. 替代选择

- [nextpad-plus-plus/nextpad-plus-plus-macos](../nextpad-plus-plus-macos/README.zh-CN.md)：本项目承载 shell 和终端会话；后者编辑文本和代码。两者覆盖桌面开发中的不同需求。

### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/ghostty-org/ghostty/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/012_ghostty-org-ghostty.md`。
