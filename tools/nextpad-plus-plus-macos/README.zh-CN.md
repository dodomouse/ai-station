# Nextpad++ for macOS

简体中文 | [English](README.en.md) | [全部导入记录](../../docs/imports/2026-11-15.md)

## 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

当前资格请运行 `python3 scripts/catalog.py search nextpad-plus-plus-macos --all`（仓库根目录）。Star 和时间数据见 [GitHub 快照](../../data/github/nextpad-plus-plus-macos.json)，核对依据见 [元数据](tool.json)。

当前项目名为 Nextpad++ for macOS，旧名称保留为别名。API 返回 NOASSERTION，许可说明仍待进一步核对。

## 原始中文记录（历史快照）

## 019 Nextpad++ for macOS

仓库：[nextpad-plus-plus/nextpad-plus-plus-macos](https://github.com/nextpad-plus-plus/nextpad-plus-plus-macos)

### 1. 简介

基于 Notepad++ 代码库的原生 macOS 编辑器。提供多标签、分屏、语法高亮、正则搜索、宏和逐步移植的插件。

### 2. 适用场景

在 macOS 编辑文本和代码。跨文件查找与正则替换。录制宏处理重复编辑。使用分屏比较文档。

### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 原生macOS编辑器 | README描述为基于原Notepad++代码库的原生移植，支持Apple Silicon和Intel。 | What this is |
| 语言编辑能力 | 提供语法高亮、代码折叠和自定义语言。 | Features |
| 查找与替换 | 支持正则、文件内/跨文件查找、增量搜索及书签行。 | Features |
| 宏录制 | 把重复编辑操作录成宏。 | Features |
| 多标签与分屏 | 同时编辑多个文档，或并排查看文档的不同部分。 | Features |
| 插件与辅助面板 | 提供原生Plugin Admin，以及文档地图、列编辑器等面板。 | Features / FAQ |

官方来源入口：[官方 README](https://github.com/nextpad-plus-plus/nextpad-plus-plus-macos/blob/main/README.md)。 能力按原卡核对日期理解。

### 4. 使用限制

**平台与环境**

- macOS 11+
- Apple Silicon与Intel，README称提供Universal Binary

- README标注GPL-3.0，免费开源，无订阅。
- 插件或外部资源的条件以相应项目为准。

- Windows插件需要移植，文档旧版数量/时间预测不能证明当前兼容率。
- 本轮未安装，不验证签名、速度、内存或插件功能。
- 不是Windows版二进制直接运行。

**容易找错的需求（不属于本项目能力）**

- 把所有Windows插件不经修改直接加载进Mac版本。
- 自动理解和重构整个大型代码仓的AI IDE。

### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/nextpad-plus-plus/nextpad-plus-plus-macos/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- 原生macOS图形界面
- 插件管理器
- 菜单、快捷键、命令面板

### 6. 替代选择

- [ghostty-org/ghostty](../ghostty/README.zh-CN.md)：本项目用于文本编辑、搜索替换和宏操作；后者用于运行和组织终端会话。它们不是同一种编辑工具。

### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/nextpad-plus-plus/nextpad-plus-plus-macos/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/019_nextpad-plus-plus-nextpad-plus-plus-macos.md`。
