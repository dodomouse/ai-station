# Graphify

简体中文 | [English](README.en.md) | [全部导入记录](../../docs/imports/2026-11-15.md)

## 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

当前资格请运行 `python3 scripts/catalog.py search graphify --all`（仓库根目录）。Star 和时间数据见 [GitHub 快照](../../data/github/graphify.json)，核对依据见 [元数据](tool.json)。

## 原始中文记录（历史快照）

## 014 Graphify

仓库：[Graphify-Labs/graphify](https://github.com/Graphify-Labs/graphify)

### 1. 简介

把源码、文档及多媒体资料组织成可查询知识图谱。提供关系解释、路径查询、子图检索和交互图页面。

### 2. 适用场景

理解代码依赖与跨文件关联。追踪两个概念之间的关系路径。为智能体查询项目结构与文档。

### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 本地源码结构抽取 | 用 tree-sitter AST 解析代码并解析跨文件调用、导入和继承等关系。 | What it does / Privacy |
| 代码与资料统一建图 | 除代码外，可对文档、PDF、图片及音视频资料做语义处理并纳入图谱。 | What files it handles / Privacy |
| 查询、路径和关系解释 | query 返回问题相关子图，path 追踪两点关系，explain 解释指定节点。 | See it in action / Common commands |
| 关系证据标签 | 关系标记为 EXTRACTED 或 INFERRED，路径置信度取决于最弱一跳。 | See it in action |
| 交互图与结构报告 | 输出 graph.html、GRAPH_REPORT.md 和 graph.json，显示关联密集节点、社区和关键路径。 | Get started / What is in the report |
| 增量更新和 Git 钩子 | 可仅重新抽取变更文件，也可安装提交或分支切换时更新图谱的钩子。 | Common commands / Team setup |
| 其他图谱导出 | 可生成 Markdown wiki、架构或调用流 HTML，并合并已有图文件。 | Common commands |

官方来源入口：[官方 README](https://github.com/Graphify-Labs/graphify/blob/v8/README.md)。 能力按原卡核对日期理解。

### 4. 使用限制

**平台与环境**

- Python 3.10+
- macOS、Linux、Windows
- Claude Code、Cursor、Codex、Gemini CLI 等助手；可独立 CLI 使用

- 代码按 Apache-2.0 开源，纯代码本地抽取不要求付费模型。
- 文档等语义处理可消耗已有助手订阅或模型 API；也可配置 Ollama 等本地后端。
- Graphify Cloud 是另一个持续服务层，README 宣传 14 天试用，不能视为永久免费。

- 纯代码抽取可离线；文档、PDF、图片通常需语义后端，配置本地模型后另行判断。
- EXTRACTED 与 INFERRED 要分开看，推断边不能直接成为已确认知识。
- 默认大图渲染有节点阈值，超出可能显示聚合社区视图。
- 效率、召回和 Cloud 节省比例是项目方报告，未实测。

**容易找错的需求（不属于本项目能力）**

- 不是针对任意私人文件都默认零模型调用的离线全文搜索。
- 不是可直接执行符号重构和调试的 Serena 类 IDE 工具。

### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/Graphify-Labs/graphify/blob/v8/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- graphify CLI
- /graphify 智能体技能
- MCP 查询接口
- 浏览器打开静态图页面

### 6. 替代选择

- [tirth8205/code-review-graph](../code-review-graph/README.zh-CN.md)：本项目覆盖源码、文档及多媒体的关系图谱；后者侧重本地代码结构、变更影响与审查上下文。

### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/Graphify-Labs/graphify/blob/v8/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/014_Graphify-Labs-graphify.md`。
