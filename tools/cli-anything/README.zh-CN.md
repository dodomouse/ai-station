# CLI-Anything

简体中文 | [English](README.en.md) | [全部导入记录](../../docs/imports/2026-11-15.md)

## 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

当前资格请运行 `python3 scripts/catalog.py search cli-anything --all`（仓库根目录）。Star 和时间数据见 [GitHub 快照](../../data/github/cli-anything.json)，核对依据见 [元数据](tool.json)。

## 原始中文记录（历史快照）

## 016 CLI-Anything

仓库：[HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything)

### 1. 简介

分析软件源码，为真实应用后端生成 CLI harness。提供结构化命令、JSON 输出、交互式 REPL 及测试流程。

### 2. 适用场景

为开源 GUI 软件构建命令行接口。让智能体调用真实专业软件。把分散 API 组织为一致命令。查找已有 CLI harness。

### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 生成CLI harness | 从本地源码或GitHub仓库分析软件并生成命令行控制层。 | Plugin Commands / Fully Automated 7-Phase Pipeline |
| 调用真实软件 | 封装真实应用后端，最终文件由实际软件处理或渲染。 | Authentic Software Integration |
| 结构化与交互输出 | 生成CLI提供JSON和人类可读输出，支持统一REPL与会话状态。 | Smart Session Management / Clean Package Architecture |
| 完善与验证 | refine扩展覆盖，test记录结果，validate检查HARNESS标准。 | Plugin Commands |
| 生成技能说明 | 从命令元数据形成SKILL.md，帮助智能体发现工具。 | SKILL.md Generation |
| 工具发现管理 | CLI-Hub用于浏览、安装和管理已有CLI工具。 | Empower Your Agents with CLI-Hub |
| 组织API | README描述可将服务API文档或SDK材料整合为一致CLI。 | Unify Scattered APIs into One CLI |

官方来源入口：[官方 README](https://github.com/HKUDS/CLI-Anything/blob/main/README.md)。 能力按原卡核对日期理解。

### 4. 使用限制

**平台与环境**

- 取决于目标软件与harness；不能据通用框架推定每个目标跨平台
- 生成CLI采用Python，README标示Python≥3.10

- 框架Apache-2.0；模型调用、目标软件许可和外部API费用另计。
- 生成harness和执行真实后端需要本地资源。

- 需要较强基础模型；弱模型可能生成不完整或错误CLI。
- 主要依赖源码；二进制反编译场景覆盖明显下降。
- 通常需迭代完善，不能据“自动生成”认定覆盖全部能力。
- 本轮未生成、安装或运行任何harness。

**容易找错的需求（不属于本项目能力）**

- 对任意闭源二进制自动获得完整无损控制接口。
- 不安装目标软件就保证生成真实渲染结果。

### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/HKUDS/CLI-Anything/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- 编码智能体中的生成/refine/test/validate入口
- 生成后的CLI命令与REPL
- CLI-Hub

### 6. 替代选择

- [lexmount/moli](../moli/README.zh-CN.md)：本项目为真实软件后端生成 CLI；后者本身就是网页运行和自动化后端。网页任务可考察后者，通用软件接入仍需相应接口。

### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/HKUDS/CLI-Anything/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/016_HKUDS-CLI-Anything.md`。
