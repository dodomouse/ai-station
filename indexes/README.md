# 开源工具目录

[English](README.en.md)

评估时间：2026-11-15T11:54:08.129868Z

此索引是构建时的快照。本地 search 命令会重新评估资格。

## AI 工具

- [ai-memory](../tools/ai-memory/README.zh-CN.md) — 为 AI 编码工具提供跨会话记忆和跨工具交接。使用 Git 管理的 Markdown 保存知识，并提供检索和摘要注入。
- [dsh-superagent 研究原型](../tools/dsh-superagent-prototype/README.zh-CN.md) — 面向单个 GitHub 仓库的主动编码智能体研究原型。监听 GitHub 和可选飞书消息，按授权创建并执行工作项。
- [Magpie](../tools/magpie/README.zh-CN.md) — 通过本地网关统一管理编码智能体的模型与服务商。提供多账号路由、故障转移及可选请求脱敏。

## 开发辅助

- [AI Website Cloner Template：网站复刻与迁移模板](../tools/ai-website-cloner-template/README.zh-CN.md) — 用编码助手观察目标网页，再以 Next.js 重建页面、素材和交互。通过浏览器对照差异并修正。
- [Archify](../tools/archify/README.zh-CN.md) — 把想法、计划或代码仓资料生成交互式 HTML 图示。可制作架构图、流程图和带来源的解释页面。
- [CLI-Anything](../tools/cli-anything/README.zh-CN.md) — 分析软件源码，为真实应用后端生成 CLI harness。提供结构化命令、JSON 输出、交互式 REPL 及测试流程。
- [code-review-graph](../tools/code-review-graph/README.zh-CN.md) — 用 Tree-sitter 建立并增量更新本地代码结构图。通过 MCP 和 CLI 提供依赖、变更影响及审查上下文。
- [Craft Anything](../tools/craft-anything/README.zh-CN.md) — 研究网站、应用或游戏，再让编码智能体创建自己的版本。提供研究、构建、比较与修改流程，以及 CLI、MCP 和检查证据。
- [Graphify](../tools/graphify/README.zh-CN.md) — 把源码、文档及多媒体资料组织成可查询知识图谱。提供关系解释、路径查询、子图检索和交互图页面。
- [Moli：面向 AI 智能体的无头浏览器](../tools/moli/README.zh-CN.md) — Rust 编写的独立无头浏览器，支持 JavaScript 网页运行、Markdown 与语义树提取、按需布局，以及 CLI、CDP 和 WebDriver 自动化。
- [Orca（智能体开发工作台）](../tools/orca/README.zh-CN.md) — 统一管理多个编程智能体的开发工作台。提供并行工作目录、终端、差异审查、手机端及 SSH 远程环境。
- [REA — Reverse Engineer Anything](../tools/rea/README.zh-CN.md) — 通过 MCP 和 CLI 连接逆向分析工具。可分析原生二进制、JavaScript、Electron、.NET 及网站。
- [Skills For Real Engineers（Matt Pocock）](../tools/skills/README.zh-CN.md) — 面向编程智能体的工程技能集合。覆盖需求澄清、架构决策、测试驱动开发、重构和任务组织。
- [Spec Kit](../tools/spec-kit/README.zh-CN.md) — 提供规格驱动开发的 CLI、技能和模板。把需求规格转换为计划、任务和代码，并支持检查与缺陷修复流程。

## 终端与 Shell

- [Ghostty](../tools/ghostty/README.zh-CN.md) — 使用原生界面和 GPU 渲染的终端模拟器。支持多窗口、标签页与分屏，另提供可嵌入终端库。

## 数据处理

- [AI Berkshire](../tools/ai-berkshire/README.zh-CN.md) — 基于 Claude Code 与 Codex 的价值投资研究技能。通过多个分析视角组织公司研究、财报、估值、组合复盘和论点跟踪。
- [Vibe Research](../tools/vibe-research/README.zh-CN.md) — 面向 A 股、美股和港股的投研工作台。整合自选、持仓、每日复盘、产业与公司研究、历史回测和研报库。

## 自动化

- [Agent Autoloop](../tools/agent-autoloop/README.zh-CN.md) — 把命令行智能体接入事件调度和后台执行。支持人工卡片、回答后继续、定时复查、日志重放及可选 PR 交付。
- [Reason Network](../tools/reason-network/README.zh-CN.md) — 每台电脑运行后台程序，共享团队 Agent 会话的人员、设备、项目、分支与工作概况。

## 部署与运维

- [Clash Verge Rev](../tools/clash-verge-rev/README.zh-CN.md) — 基于 Tauri 的 mihomo 图形代理客户端。提供配置管理、规则编辑、系统代理、TUN 模式和 WebDAV 同步。

## 文档与效率

- [best-skills](../tools/best-skills/README.zh-CN.md) — 收集采用 SKILL.md 格式的智能体工作流程。覆盖论文、专利、汇报、自媒体、图表和代码文档。
- [GenOffice](../tools/genoffice/README.zh-CN.md) — 提供 Office、PDF、Markdown 和 HTML 文件编辑。包含桌面编辑器、CLI、MCP 和智能体技能，可创建、转换和检索文件。
- [Horizon：AI 信息聚合与双语新闻简报](../tools/horizon/README.zh-CN.md) — 聚合 RSS、社区、GitHub 与新闻等信息源，按 Profile 评分、筛选和去重，生成中英双语 Markdown 日报。

## 图像与音视频

- [Anatomy](../tools/anatomy/README.zh-CN.md) — 用交互式等轴测图解释机械、仪器和抽象机制。生成 SVG、HTML 或 React 组件，可叠加 WebGL 与 3D 效果。
- [代码手绘插画与动画](../tools/anidoodle/README.zh-CN.md) — 以代码描述笔画，提供 32 种插画风格和逐笔绘制示例。
- [Animate 程序化动画](../tools/animate/README.zh-CN.md) — 以单个 Canvas 程序化绘制和配乐，用无头浏览器与 FFmpeg 输出 MP4。
- [Bang Motion](../tools/bang-motion/README.zh-CN.md) — 将开场、宣传片、产品演示、动态文字和讲解组织成可播放的单个 index.html。
- [Claude Animation Base](../tools/claudeanimationbase/README.zh-CN.md) — 以 p5.js 与 p5.brush 绘制角色，提供 Clawd 角色、核心绘画工具和时间线。
- [花叔艺术动画](../tools/huashu-art-motion/README.zh-CN.md) — 当前 README 列出 36 种艺术风格、9 种解说语法和 8 种参数化片段。
- [Huashu Design](../tools/huashu-design/README.zh-CN.md) — 面向智能体的 HTML 原生设计技能。可制作网页、App 原型、可编辑 PPTX、动画和信息图。
- [15 种动态设计风格](../tools/mg-styles-15/README.zh-CN.md) — 15 支 10 秒动态设计示例，逐项公开风格说明、完整提示词与源码。
- [手绘口播视频](../tools/sweety-handdraw-video/README.zh-CN.md) — Agent 整理内容、口播和分镜，本地工具执行描线、填色、手写文字与声音对齐。
- [Teardown：交互式机械拆解与3D演示](../tools/teardown/README.zh-CN.md) — 面向 Claude Code 的 3D 机械原理演示技能。支持部件拆解、剖视、联动、自动演示与人工交互，可构建离线 HTML 并录制 MP4。
- [产品宣传片制作](../tools/video-shotcraft/README.zh-CN.md) — 面向产品发布和功能演示，采集真实页面素材后用 Remotion 编排影片。
- [VoiceStudio](../tools/voicestudio/README.zh-CN.md) — 在本地运行语音克隆、声音设计、转录和视频配音。另提供听写、有声书、批量任务及本地 API 与 MCP 接口。
