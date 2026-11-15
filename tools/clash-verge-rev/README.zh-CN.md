# Clash Verge Rev

简体中文 | [English](README.en.md) | [全部导入记录](../../docs/imports/2026-11-15.md)

## 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

当前资格请运行 `python3 scripts/catalog.py search clash-verge-rev --all`（仓库根目录）。Star 和时间数据见 [GitHub 快照](../../data/github/clash-verge-rev.json)，核对依据见 [元数据](tool.json)。

## 原始中文记录（历史快照）

## 006 Clash Verge Rev

仓库：[clash-verge-rev/clash-verge-rev](https://github.com/clash-verge-rev/clash-verge-rev)

### 1. 简介

基于 Tauri 的 mihomo 图形代理客户端。提供配置管理、规则编辑、系统代理、TUN 模式和 WebDAV 同步。

### 2. 适用场景

管理代理节点与分流规则。在桌面切换代理配置。同步配置文件。

### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 代理配置管理 | 导入并管理配置文件，提供语法提示。支持 Merge 与 Script 增强配置。 | Features |
| 系统代理与 TUN | 提供系统代理及守卫功能，并支持 TUN 虚拟网卡模式。 | Features |
| 节点与规则可视化 | 在图形界面编辑节点、代理组与分流规则。 | Features |
| 配置备份和同步 | 支持通过 WebDAV 备份、同步配置。 | Features |
| 桌面外观定制 | 支持主题色、代理组与托盘图标定制，也支持 CSS 注入。 | Features |
| mihomo 内核管理 | 内置 Clash.Meta/mihomo，并提供 Alpha 内核切换入口。 | Features |

官方来源入口：[官方 README](https://github.com/clash-verge-rev/clash-verge-rev/blob/dev/README.md)。 能力按原卡核对日期理解。

### 4. 使用限制

**平台与环境**

- Windows x64/x86
- Linux x64/arm64
- macOS 11+，Intel 与 Apple Silicon

- 代码标示 GPL-3.0。客户端许可不提供代理节点或网络套餐；节点、订阅服务及 WebDAV 托管可能另有费用。README 的推广服务不等于软件内置免费服务。

- 需要可用节点与正确配置，安装客户端本身不能保证网络可达。
- 不同系统的 TUN、服务模式与权限要求需另查官方文档。
- 性能、隐私和连接质量未在本轮运行核验。

**容易找错的需求（不属于本项目能力）**

- 不匹配“免费送可用代理节点或网络套餐”的需求。
- 不是 WireGuard/OpenVPN 通用配置兼容性的已验证替代品。

### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/clash-verge-rev/clash-verge-rev/blob/dev/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- 桌面图形界面
- 托盘
- 系统代理与 TUN
- 配置文件、Merge、Script
- WebDAV

### 6. 替代选择

- [clashbk/clash](../clash/README.zh-CN.md)：本项目是可运行的桌面代理客户端；后者汇总客户端入口和教程。

### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/clash-verge-rev/clash-verge-rev/blob/dev/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/006_clash-verge-rev-clash-verge-rev.md`。
