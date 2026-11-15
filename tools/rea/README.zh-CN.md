# REA — Reverse Engineer Anything

简体中文 | [English](README.en.md) | [全部导入记录](../../docs/imports/2026-11-15.md)

## 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

当前资格请运行 `python3 scripts/catalog.py search rea --all`（仓库根目录）。Star 和时间数据见 [GitHub 快照](../../data/github/rea.json)，核对依据见 [元数据](tool.json)。

## 原始中文记录（历史快照）

## 018 REA — Reverse Engineer Anything

仓库：[morluto/rea](https://github.com/morluto/rea)

### 1. 简介

通过 MCP 和 CLI 连接逆向分析工具。可分析原生二进制、JavaScript、Electron、.NET 及网站。

### 2. 适用场景

理解没有源码的桌面应用行为。检查 Electron 的模块与 IPC。辅助原生二进制逆向分析。

### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 原生二进制分析 | 接入 Hopper、Ghidra、IDA 或 Kuna，获得伪代码、汇编、字符串、符号、调用与引用。 | What you can analyze |
| JavaScript 与 Electron 检查 | 静态检查模块、导入、source map、路由、IPC 和原生插件关系。可分析解包目录或 ASAR。 | Quick start / What you can analyze |
| .NET 静态检查 | 读取程序集元数据、CIL 指令和原生依赖声明，并比较构建结果。此路径不需要原生反编译引擎。 | What you can analyze |
| 网页与网络记录分析 | 可观察网页结构、脚本和网络请求，也能分析保存的 HAR 或 SAZ 等记录。不同格式有不同外部工具依赖。 | What you can analyze |
| Android 应用检查 | 使用 JADX 和 JDK 检查 APK 的 Manifest、类、反编译方法和引用。 | What you can analyze |
| 运行行为与本地证据 | 可记录受控进程的终端交互、退出和文件变化。输出给出观察证据及推断限制。 | How REA works / What you can analyze |
| 智能体与终端接口 | 以 MCP、工作流说明和 CLI 提供分析操作。静态 JavaScript 路径可独立于原生分析引擎运行。 | Quick start / How REA works |

官方来源入口：[官方 README](https://github.com/morluto/rea/blob/main/README.md)。 能力按原卡核对日期理解。

### 4. 使用限制

**平台与环境**

- 目标与后端决定主机范围，不能概括为所有功能跨平台
- JavaScript 静态分析依赖 Node.js/npm；原生分析依赖相应引擎
- 部分记录、固件与诊断路径仅在 Linux 验证；Windows Ghidra 支持标为实验性

- REA 自有代码为 MIT。商业逆向工具、反编译器和所接编码模型可能分别收费，REA 不授予第三方工具的许可或激活权。

- 原生工具、浏览器、JDK、抓包解析器等依所选目标分别配置。
- 静态关系、推断和运行观察的证据强度不同，结论需保留限制。
- 本轮未执行任何二进制、应用、安装器或分析引擎。

**容易找错的需求（不属于本项目能力）**

- 不能承诺恢复一份与原作者完全一致、可直接重建的源码。
- 不是绕过软件授权、破解激活或免费获得商业反编译器的工具许可。

### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/morluto/rea/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- MCP 服务
- rea / rea-agents CLI
- 智能体工作流说明
- Hopper、Ghidra、IDA、Kuna 等 provider

### 6. 替代选择

- [storytold/craft-anything](../craft-anything/README.zh-CN.md)：本项目连接逆向分析工具，检查程序行为；后者将研究结果用于构建与比较新版本。

### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/morluto/rea/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/018_morluto-rea.md`。
