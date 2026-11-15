# Archify

简体中文 | [English](README.en.md) | [全部导入记录](../../docs/imports/2026-11-15.md)

## 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

当前资格请运行 `python3 scripts/catalog.py search archify --all`（仓库根目录）。Star 和时间数据见 [GitHub 快照](../../data/github/archify.json)，核对依据见 [元数据](tool.json)。

## 原始中文记录（历史快照）

## 025 Archify

仓库：[tt-a1i/archify](https://github.com/tt-a1i/archify)

### 1. 简介

把想法、计划或代码仓资料生成交互式 HTML 图示。可制作架构图、流程图和带来源的解释页面。

### 2. 适用场景

制作代码仓架构图与流程图。生成带引用的技术解释页面。探索节点关系和路径。分享独立 HTML 或导出图片。

### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 多类图示 | 支持架构、流程、时序、数据流、生命周期、ERD、类、树、时间线和瀑布图。 | Choose the right diagram |
| 交互探索 | 查看节点关系，跟踪路径及作者提供的上下游关系。 | Explore and share the output |
| 源码关联 | 从仓库资料绘图，来源卡片可链接到固定提交的代码片段。 | Understand a real repository / Ask a question, get a one-page answer |
| 单页解释 | 把结论、表格、步骤、代码和校验图组合成解释页。 | Ask a question, get a one-page answer |
| 便携分享与导出 | 交付单个HTML，支持图像导出和打印PDF等分享方式。 | Download it. Open it. Explore it. / Ask a question, get a one-page answer |
| 前后结构比较 | Architecture Delta比较已验证的Before/Delta/After快照。 | Choose the right diagram |

官方来源入口：[官方 README](https://github.com/tt-a1i/archify/blob/main/README.md)。 能力按原卡核对日期理解。

### 4. 使用限制

**平台与环境**

- HTML通过浏览器查看
- 完整渲染需相应Node环境；具体集成版本条件各异

- Apache-2.0开源；生成所用智能体、模型或外部服务费用另计。
- 第三方在线服务或付费计划不代表Archify官方。

- 绘图及可达关系来自作者描述/来源，不自动等于运行时影响。
- 架构差异不能证明风险、测试充分或合并安全。
- 不是线上基础设施扫描器；本轮未生成和验证图示。

**容易找错的需求（不属于本项目能力）**

- 自动抓到生产环境真实链路并持续监控。
- 看完架构差异自动保证此次代码可以安全合并。

### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/tt-a1i/archify/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- Claude Code、Codex CLI、OpenCode等技能环境
- Node CLI与图示校验工作流
- Claude.ai技能（取决于沙箱Node访问）
- 可选Hermes Agent和DeepSeek Harness社区集成

### 6. 替代选择

- [wheresryan22/anatomy](../anatomy/README.zh-CN.md)：本项目侧重带来源的架构、流程和解释图；后者以等轴测图解释机械与抽象机制。

### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/tt-a1i/archify/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/025_tt-a1i-archify.md`。
