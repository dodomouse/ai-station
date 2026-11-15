# dsh-superagent 研究原型

简体中文 | [English](README.en.md) | [全部导入记录](../../docs/imports/2026-11-15.md)

## 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

当前资格请运行 `python3 scripts/catalog.py search dsh-superagent-prototype --all`（仓库根目录）。Star 和时间数据见 [GitHub 快照](../../data/github/dsh-superagent-prototype.json)，核对依据见 [元数据](tool.json)。

## 原始中文记录（历史快照）

## 010 dsh-superagent 研究原型

仓库：[deepseek-ai/dsh-superagent-prototype](https://github.com/deepseek-ai/dsh-superagent-prototype)

### 1. 简介

面向单个 GitHub 仓库的主动编码智能体研究原型。监听 GitHub 和可选飞书消息，按授权创建并执行工作项。

### 2. 适用场景

研究团队编码智能体的授权模型。了解消息触发的 GitHub 工作项流程。参考智能体执行与人工面板设计。

### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 单仓库消息入口 | 面向一个 GitHub 仓库监听请求，并可选接入飞书。 | dsh-superagent 项目简介 |
| 授权触发 | 仅在允许的人员提出工作或团队规则允许时行动。 | 工作原则 / docs/000-philosophy.md入口 |
| 工作项与隔离执行 | 接到工作后创建工作项，在各自智能体会话与目录中处理。 | dsh-superagent 项目简介 |
| 回到原会话交付 | 在请求的原对话中回应，README举例为提交拉取请求。 | dsh-superagent 项目简介 |
| 人工面板 | Web面板集中展示哪些事项需要人处理。 | dsh-superagent 项目简介 / Documentation |

官方来源入口：[官方 README](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/main/README.md)。 能力按原卡核对日期理解。

### 4. 使用限制

**平台与环境**

- 以DeepSeek Harness部署环境为前提；README未明确操作系统兼容矩阵

- 代码采用MIT；部署、模型服务与其他所接平台成本另计。
- 研究原型不附送DeepSeek或其他模型额度。

- README明确：研究参考代码，不是DeepSeek官方产品，不是生产就绪软件。
- 部分文章设计属于未来方向，原型没有全部实现。
- 未部署、未核验授权与通知行为，不能作为上线保证。

**容易找错的需求（不属于本项目能力）**

- 直接作为多仓库、无需配置的正式团队SaaS上线。
- 已经实现相关文章里所有未来设计。

### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- GitHub事件与会话
- 可选飞书
- Web人工面板
- DeepSeek Harness bundle

### 6. 替代选择

- [KKKKhazix/agent-autoloop](../agent-autoloop/README.zh-CN.md)：本项目是围绕单个 GitHub 仓库的主动编码研究原型；后者提供本地事件调度及后台任务跟进。

### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/deepseek-ai/dsh-superagent-prototype/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/010_deepseek-ai-dsh-superagent-prototype.md`。
