# ai-memory

简体中文 | [English](README.en.md) | [全部导入记录](../../docs/imports/2026-11-15.md)

## 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

当前资格请运行 `python3 scripts/catalog.py search ai-memory --all`（仓库根目录）。Star 和时间数据见 [GitHub 快照](../../data/github/ai-memory.json)，核对依据见 [元数据](tool.json)。

## 原始中文记录（历史快照）

## 003 ai-memory

仓库：[akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)

### 1. 简介

为 AI 编码工具提供跨会话记忆和跨工具交接。使用 Git 管理的 Markdown 保存知识，并提供检索和摘要注入。

### 2. 适用场景

在 Claude Code 与 Codex 之间交接任务。跨电脑延续项目上下文。团队共享项目记忆。

### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 自动记录与整理 | 生命周期钩子记录提示、工具调用和会话边界。会话结束后将整理结果写成可读的知识页。 | Why ai-memory / How it works |
| 跨工具交接 | 给下一会话提供当前进度、失败尝试和待处理事项。交接带所有者和领取规则，适合不同编码助手续接。 | Why ai-memory |
| 项目记忆检索 | 检索知识页、实体与链接。支持路径、标签和知识类型筛选，也能搜索不带空格的中文等文本。 | Everyday use |
| Markdown 权威源 | 知识正文是 Git 管理的 Markdown。数据库是可重建索引，可用普通编辑器、Obsidian 或文本搜索查看。 | Why ai-memory / Architecture |
| 跨电脑与团队共享 | 多台电脑或成员可连接同一服务。项目知识共享，个人交接分别保留，并记录写入归属。 | Teams and multiple machines |
| 既有资料导入 | 可选导入器接收 PDF、DOCX、PPTX、XLSX、Markdown 与 VTT/SRT 等文件。导入结果带来源并经过清理。 | Everyday use |
| 可选模型增强 | 基础捕获、搜索与交接不要求大模型调用。可配置模型增强摘要、语义搜索及默认关闭的综合回答等功能。 | LLM providers |

官方来源入口：[官方 README](https://github.com/akitaonrails/ai-memory/blob/main/README.md)。 能力按原卡核对日期理解。

### 4. 使用限制

**平台与环境**

- Linux、macOS、NixOS
- Windows 经 WSL2 支持；原生 Windows 标为实验性
- 支持的助手包括 Claude Code、Codex、Cursor、Gemini CLI 等，集成能力各异

- 代码使用 MIT。基础记忆路径不要求大模型调用；可选摘要、嵌入等模型功能按所用服务计费。运行服务器和编码助手的费用不由 MIT 许可覆盖。

- 自动捕获与交接需要先安装集成，不会追溯所有未被记录的历史。
- 共享记忆与原生聊天会话恢复是不同能力；不能承诺完整还原所有界面状态。
- 每个数据目录只能由一个服务实例管理；原生 Windows 仍属实验性。

**容易找错的需求（不属于本项目能力）**

- 不能据此声称它会训练或微调一个记住全部项目的大模型。
- 不是通用跨电脑文件同步工具，也不是独立完成编码任务的模型。

### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/akitaonrails/ai-memory/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- CLI
- MCP 服务与客户端集成
- 生命周期钩子
- 可选只读 Web 页面与 HTTP API

### 6. 替代选择

- [Graphify-Labs/graphify](../graphify/README.zh-CN.md)：本项目把跨会话记忆保存在 Git 管理的 Markdown 中；后者把资料组织成可查询的关系图谱。

### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/akitaonrails/ai-memory/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/003_akitaonrails-ai-memory.md`。
