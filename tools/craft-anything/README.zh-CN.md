# Craft Anything

简体中文 | [English](README.en.md) | [全部导入记录](../../docs/imports/2026-11-15.md)

## 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

当前资格请运行 `python3 scripts/catalog.py search craft-anything --all`（仓库根目录）。Star 和时间数据见 [GitHub 快照](../../data/github/craft-anything.json)，核对依据见 [元数据](tool.json)。

## 原始中文记录（历史快照）

## 032 Craft Anything

仓库：[storytold/craft-anything](https://github.com/storytold/craft-anything)

### 1. 简介

研究网站、应用或游戏，再让编码智能体创建自己的版本。提供研究、构建、比较与修改流程，以及 CLI、MCP 和检查证据。

### 2. 适用场景

照着参考网站创建新项目。仅从截图研究界面。深入分析程序。比较生成结果与原目标。

### 3. 主要功能

| 能力 | 具体作用 | 官方核对位置 |
| --- | --- | --- |
| 多类目标研究 | 研究网站、原生程序、移动应用、游戏和文件。内置 Rust 格式解析、反汇编及反编译工具。 | README / Under the hood |
| 默认 Clean room 模式 | 从截图、访客可见内容和界面布局收集依据。不读取目标源码、内部文件或网页源。 | README / Clean room or Deep；STATUS / Clean room and Deep mode |
| Deep 深入研究 | 分析代码、程序文件和网页 JavaScript。Ghidra 可在安装后补充内置引擎。 | README / Clean room or Deep |
| 研究到重建的流程 | 串联研究、构建、比较和修改。按需求指定的语言、框架或引擎创建项目。 | README / How it works；STATUS / Rebuild workflow |
| 网站比较 | 比较多个页面在桌面、平板和手机宽度下的布局、视觉与部分交互。输出差异后继续修改。 | STATUS / Websites as targets、Rebuild workflow |
| 桌面与智能体接口 | 提供 Simple、Advanced 工作台、CLI 和 MCP。智能体可调用检查工具或发起重建。 | README / Two ways to use it、Built for agents |
| 可追溯检查记录 | 结果保留证据、置信度、覆盖范围与限制。大型结果支持分页浏览。项目保存构建与比较历史。 | README / Built for agents、Get started |
| 继续已有项目 | 支持指定项目目录、继续修改生成结果或编辑已有项目。工作台展示待处理问题与执行进度。 | README / Get started；STATUS / Rebuild workflow |

官方来源入口：[官方 README](https://github.com/storytold/craft-anything/blob/main/README.md)。 能力按原卡核对日期理解。

### 4. 使用限制

**平台与环境**

- README 列出 Windows、macOS、Linux 和 FreeBSD 的发行目标。
- 浏览器查看器通过 WebAssembly 查看文件，不等于桌面版重建工作台。
- 源码构建有 Rust 与平台依赖要求，以当前安装说明为准。
- 安装包说明与首次公开发行待办在 README 中并存。是否已有可用发行需再查 Releases。

- 仓库代码采用 MIT 或 Apache-2.0 双许可，二选一。
- 基础软件检查不要求模型调用。AI 问答和构建使用所配助手、订阅或模型服务。
- 构建使用本机已安装的编码助手；工具不附送 Claude、Codex 或其他模型额度。
- 可选图片、三维素材生成依赖另外配置的服务，并可能收费；默认不启用。
- 目标软件、生成素材、品牌标识和第三方资源各有自己的使用条件。

- 项目仍为早期 Alpha。本次只核对文档，没有验证安装或执行效果。
- 官方 STATUS 更新于 2026-11-02。部分引擎工具只用合成样本或替身验证。
- 官方没有实跑完整 Clean room 构建。部分智能体未接入相同权限约束，不能当作绝对隔离保证。
- 应用、游戏的行为验证尚不完整；生成游戏的自测由游戏自身报告。
- Codex 适配尚未在真实安装上验证。ACP 助手仅有部分实跑记录。
- API 构建循环已有实现，但尚未实跑确认；部分接入文档对此仍有旧描述。
- Clean room 是研究模式，不自动证明重建结果、功能完整性或素材使用条件符合要求。

**容易找错的需求（不属于本项目能力）**

- “把任意闭源商业软件一键完整复制”：官方没有这样的效果证据。
- “绕过 DRM、登录或反作弊”：README 明确不提供这些能力。
- “不接模型也自动写完新项目”：无需 AI 的是基础检查，构建仍需编码智能体。

### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/storytold/craft-anything/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- 桌面应用的 Simple 与 Advanced 两种工作台。
- `craft-anything-cli` 命令行与 MCP 服务。
- Claude Code 是官方首个已实跑的构建助手。
- Codex 适配和其他 ACP 助手分别有验证限制。列在支持清单中不等于已经实跑。

### 6. 替代选择

- [JCodesMore/ai-website-cloner-template](../ai-website-cloner-template/README.zh-CN.md)：本项目覆盖网站、应用和游戏的研究与重建；后者集中于网页观察与 Next.js 前端重建。
- [morluto/rea](../rea/README.zh-CN.md)：本项目包含构建和结果比较流程；后者集中于逆向分析与行为检查。

### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：功能来自官方文档。问法与用途属于检索整理判断，本次未安装实测。

**来源与版本记录**

- [官方 README](https://github.com/storytold/craft-anything/blob/main/README.md)：定位、模式、流程、接入与许可。确认日期：2026-11-03。
- [官方 STATUS](https://github.com/storytold/craft-anything/blob/main/docs/STATUS.md)：实现状态、验证方式与缺项。文档日期：2026-11-02；确认日期：2026-11-03。
- [Claude Code 接入说明](https://github.com/storytold/craft-anything/blob/main/docs/claude-code.md)：本机助手接入及其他后端边界。确认日期：2026-11-03。
- 项目变化较快。采用前复核实际版本、平台发行、智能体适配与检查覆盖范围。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/032_storytold-craft-anything.md`。
