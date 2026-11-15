# Serena

简体中文 | [English](README.en.md) | [全部导入记录](../../docs/imports/2026-11-15.md)

## 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

当前资格请运行 `python3 scripts/catalog.py search serena --all`（仓库根目录）。Star 和时间数据见 [GitHub 快照](../../data/github/serena.json)，核对依据见 [元数据](tool.json)。

当前许可按组件区分：SolidLSP 为 MIT，Serena 应用为 GPL-3.0-or-later。API 返回 NOASSERTION；当前单一许可门禁不能完整表达该结构，暂留候选，不等于判定闭源。

## 原始中文记录（历史快照）

## 020 Serena

仓库：[oraios/serena](https://github.com/oraios/serena)

### 1. 简介

为编程智能体提供符号级检索、编辑、重构和调试工具。通过 MCP 接入助手，使用语言服务器或 JetBrains 后端。

### 2. 适用场景

按符号查定义与引用。让智能体执行语义重构。给现有助手补充 IDE 式代码工具。

### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 符号级检索 | 提供查符号、文件符号概要、引用、声明与实现等查询，具体覆盖取决于后端和语言。 | Features / Retrieval |
| 语义重构 | LSP 后端支持符号重命名；JetBrains 后端还提供移动、内联和传播删除等操作。 | Features / Refactoring |
| 符号级编辑 | 提供替换符号主体、在符号前后插入内容及安全删除等接口。 | Features / Symbolic Editing |
| 诊断与 IDE 分析 | 语言服务器或 JetBrains 提供诊断；部分类型层次和依赖内搜索仅 JetBrains 支持。 | Features / Retrieval |
| 交互调试 | JetBrains 插件可让 Agent 设置断点、查看变量、求值和控制执行流程。 | Features / Interactive Debugging |
| 跨会话记忆和配置 | 提供可选记忆系统，以及全局、项目、上下文和 mode 等多层 YAML 配置。 | Features / Memory Management / Configurability |
| MCP 接入现有助手 | 作为 MCP server 为 Claude Code、Codex、IDE 插件或桌面客户端提供工具。 | How Serena Works |

官方来源入口：[官方 README](https://github.com/oraios/serena/blob/main/README.md)。 能力按原卡核对日期理解。

### 4. 使用限制

**平台与环境**

- 有相应语言服务器的开发环境
- 支持 MCP 的终端、IDE 或桌面助手
- JetBrains 插件支持的 IDE；README 明确 Rider 与 CLion 不支持该插件

- README 标为 GPL-3.0-or-later，语言服务器后端为默认免费开源路线。
- JetBrains 插件为收费组件，提供免费试用。
- 大模型助手的订阅或 API 另计；工具本身不附送 AI 算力。
- GitHub API 许可证字段是 NOASSERTION，采用前应以当前 LICENSE 核对。

- 不是大模型，需要客户端组织工具调用。
- LSP 与 JetBrains 的功能不同，不能把所有功能都视为默认可用。
- 静态引用和重构受语言后端限制；修改后仍需正常验证。
- 本次没有安装插件、启动服务或修改源码。

**容易找错的需求（不属于本项目能力）**

- 不是侧重构建持久关系图、路径图和图报告的 Graphify。
- 不是独立完成需求到交付的免费编程大模型。

### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/oraios/serena/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- MCP server（由客户端启动或 HTTP 模式）
- Serena REPL 式 Agent 接口
- 配置与启动 CLI

### 6. 替代选择

- [tirth8205/code-review-graph](../code-review-graph/README.zh-CN.md)：本项目提供符号级检索、编辑及部分重构工具；后者提供代码关系与审查上下文，侧重点是分析。

### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/oraios/serena/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/020_oraios-serena.md`。
