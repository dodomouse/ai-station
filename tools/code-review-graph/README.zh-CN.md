# code-review-graph

简体中文 | [English](README.en.md) | [全部导入记录](../../docs/imports/2026-11-15.md)

## 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

当前资格请运行 `python3 scripts/catalog.py search code-review-graph --all`（仓库根目录）。Star 和时间数据见 [GitHub 快照](../../data/github/code-review-graph.json)，核对依据见 [元数据](tool.json)。

## 原始中文记录（历史快照）

## 024 code-review-graph

仓库：[tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph)

### 1. 简介

用 Tree-sitter 建立并增量更新本地代码结构图。通过 MCP 和 CLI 提供依赖、变更影响及审查上下文。

### 2. 适用场景

为跨文件代码审查筛选上下文。查询函数与文件依赖。分析改动的潜在影响范围。

### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 结构图构建 | 用 Tree-sitter 等解析函数、类、导入、调用、继承及测试关系，保存本地代码图。 | How It Works / Language coverage and notebooks |
| 变更影响分析 | 沿调用和导入关系追踪可能受影响的函数、依赖与测试，为审查提供候选阅读范围。 | Blast-radius analysis |
| 增量更新 | 通过编辑器钩子、Git pre-commit 或 watch 更新。只重解析内容哈希变化的文件。 | Incremental updates |
| 定向查询与可选语义搜索 | 按问题取子图而非整仓上下文。可选接本地或外部嵌入模型增强语义搜索。 | Whole codebase or targeted answer? / Features |
| 图形与结构诊断 | 提供交互式可视化、社区分析、枢纽与桥节点识别，以及耦合和知识缺口线索。 | Features |
| CI 风险审查 | GitHub Action 可根据差异生成带风险评分的 PR 评论，并提供可选风险门禁。 | Risk-scored PR reviews in CI (GitHub Action) |
| 多格式导出 | 可导出 GraphML、Neo4j Cypher、Obsidian vault、JSON 和 SVG 等格式。SVG 有额外依赖。 | Features |

官方来源入口：[官方 README](https://github.com/tirth8205/code-review-graph/blob/staging/README.md)。 能力按原卡核对日期理解。

### 4. 使用限制

**平台与环境**

- Python 3.10+ 环境，具体安装方式按文档
- 可接 Codex、Claude Code、Cursor 等受支持客户端
- 语言与框架覆盖各异；不是所有文件类型都能提取语义关系

- 代码为 MIT。基础静态建图和查询在本地运行；可选嵌入模型、编码助手及 CI 算力可能收费。节省 token 的项目报告未经本轮复现，不能预设必省费用。

- 小范围修改可能增加图元信息开销。
- 搜索排名、部分语言入口流程识别和动态关系存在限制。
- EXTRACTED 与 INFERRED 等证据类型及置信度不能省略；影响预测是保守线索。
- 代码图谱不能替代实际测试、编译或运行观测。

**容易找错的需求（不属于本项目能力）**

- 不匹配“精确证明所有运行时影响，绝无遗漏或误报”的要求。
- 不是给任意 PDF、音视频资料建立通用知识图谱的首选定位。

### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/tirth8205/code-review-graph/blob/staging/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- CLI
- MCP stdio 或 Streamable HTTP
- 编辑器钩子、Git hook 与 watch
- GitHub Action
- 交互式图页面

### 6. 替代选择

- [Graphify-Labs/graphify](../graphify/README.zh-CN.md)：本项目集中于代码结构与变更影响；后者还纳入文档和多媒体资料。
- [oraios/serena](../serena/README.zh-CN.md)：本项目提供审查所需关系；后者还能按符号编辑代码，部分后端支持重构与调试。

### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/tirth8205/code-review-graph/blob/staging/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/024_tirth8205-code-review-graph.md`。
