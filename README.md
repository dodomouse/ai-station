# ai-station

中英文 GitHub 工具字典，按用途查找项目。

简体中文 | [English](README.en.md)

现有 62 个项目，每个项目用一份 Markdown 保存中英文介绍。2026-11-15 的核对结果为 35 个已收录、27 个候选。Star、维护活动和许可信息均为当时记录，需要人工更新。

## 查询

使用浏览器查找（Ctrl/⌘+F）搜索名称或用途，也可使用 GitHub 仓库搜索。点击项目名称查看介绍、环境、限制和来源。候选项目也列在本页。

## 收录标准

- 至少 1000 Star。
- 最近 3 个日历月内有确认的功能或缺陷修复、已合并 PR 或正式发行。纯文档或机器人更新不单独计入。
- 仓库公开，未归档、未禁用；开源许可证和中英文内容已复核。
- 核对所用 GitHub 快照不超过 7 天。记录过期后需重新核对。

未达标或证据不足的项目保留为候选，并注明原因。Star 和活跃度不能替代质量判断。

## 已收录（35）

| 项目 | 用途 | 分类 | Star |
| --- | --- | --- | ---: |
| [ai-memory](docs/ai-memory.md#中文) | 为 AI 编码工具提供跨会话记忆和跨工具交接。使用 Git 管理的 Markdown 保存知识，并提供检索和摘要注入。 | AI 工具 | 15919 |
| [dsh-superagent 研究原型](docs/dsh-superagent-prototype.md#中文) | 面向单个 GitHub 仓库的主动编码智能体研究原型。监听 GitHub 和可选飞书消息，按授权创建并执行工作项。 | AI 工具 | 23202 |
| [Magpie](docs/magpie.md#中文) | 通过本地网关统一管理编码智能体的模型与服务商。提供多账号路由、故障转移及可选请求脱敏。 | AI 工具 | 36740 |
| [Agent Autoloop](docs/agent-autoloop.md#中文) | 把命令行智能体接入事件调度和后台执行。支持人工卡片、回答后继续、定时复查、日志重放及可选 PR 交付。 | 自动化 | 5427 |
| [Reason Network](docs/reason-network.md#中文) | 每台电脑运行后台程序，共享团队 Agent 会话的人员、设备、项目、分支与工作概况。 | 自动化 | 1748 |
| [AI Berkshire](docs/ai-berkshire.md#中文) | 基于 Claude Code 与 Codex 的价值投资研究技能。通过多个分析视角组织公司研究、财报、估值、组合复盘和论点跟踪。 | 数据处理 | 17140 |
| [Vibe Research](docs/vibe-research.md#中文) | 面向 A 股、美股和港股的投研工作台。整合自选、持仓、每日复盘、产业与公司研究、历史回测和研报库。 | 数据处理 | 3720 |
| [AI Website Cloner Template：网站复刻与迁移模板](docs/ai-website-cloner-template.md#中文) | 用编码助手观察目标网页，再以 Next.js 重建页面、素材和交互。通过浏览器对照差异并修正。 | 开发辅助 | 39159 |
| [Archify](docs/archify.md#中文) | 把想法、计划或代码仓资料生成交互式 HTML 图示。可制作架构图、流程图和带来源的解释页面。 | 开发辅助 | 96538 |
| [CLI-Anything](docs/cli-anything.md#中文) | 分析软件源码，为真实应用后端生成 CLI harness。提供结构化命令、JSON 输出、交互式 REPL 及测试流程。 | 开发辅助 | 58741 |
| [code-review-graph](docs/code-review-graph.md#中文) | 用 Tree-sitter 建立并增量更新本地代码结构图。通过 MCP 和 CLI 提供依赖、变更影响及审查上下文。 | 开发辅助 | 32776 |
| [Craft Anything](docs/craft-anything.md#中文) | 研究网站、应用或游戏，再让编码智能体创建自己的版本。提供研究、构建、比较与修改流程，以及 CLI、MCP 和检查证据。 | 开发辅助 | 33239 |
| [Graphify](docs/graphify.md#中文) | 把源码、文档及多媒体资料组织成可查询知识图谱。提供关系解释、路径查询、子图检索和交互图页面。 | 开发辅助 | 148039 |
| [Moli：面向 AI 智能体的无头浏览器](docs/moli.md#中文) | Rust 编写的独立无头浏览器，支持 JavaScript 网页运行、Markdown 与语义树提取、按需布局，以及 CLI、CDP 和 WebDriver 自动化。 | 开发辅助 | 23783 |
| [Orca（智能体开发工作台）](docs/orca.md#中文) | 统一管理多个编程智能体的开发工作台。提供并行工作目录、终端、差异审查、手机端及 SSH 远程环境。 | 开发辅助 | 125338 |
| [REA — Reverse Engineer Anything](docs/rea.md#中文) | 通过 MCP 和 CLI 连接逆向分析工具。可分析原生二进制、JavaScript、Electron、.NET 及网站。 | 开发辅助 | 460761 |
| [Skills For Real Engineers（Matt Pocock）](docs/skills.md#中文) | 面向编程智能体的工程技能集合。覆盖需求澄清、架构决策、测试驱动开发、重构和任务组织。 | 开发辅助 | 324716 |
| [Spec Kit](docs/spec-kit.md#中文) | 提供规格驱动开发的 CLI、技能和模板。把需求规格转换为计划、任务和代码，并支持检查与缺陷修复流程。 | 开发辅助 | 149841 |
| [Anatomy](docs/anatomy.md#中文) | 用交互式等轴测图解释机械、仪器和抽象机制。生成 SVG、HTML 或 React 组件，可叠加 WebGL 与 3D 效果。 | 图像与音视频 | 27394 |
| [代码手绘插画与动画](docs/anidoodle.md#中文) | 以代码描述笔画，提供 32 种插画风格和逐笔绘制示例。 | 图像与音视频 | 1693 |
| [Animate 程序化动画](docs/animate.md#中文) | 以单个 Canvas 程序化绘制和配乐，用无头浏览器与 FFmpeg 输出 MP4。 | 图像与音视频 | 1967 |
| [Bang Motion](docs/bang-motion.md#中文) | 将开场、宣传片、产品演示、动态文字和讲解组织成可播放的单个 index.html。 | 图像与音视频 | 2201 |
| [Claude Animation Base](docs/claudeanimationbase.md#中文) | 以 p5.js 与 p5.brush 绘制角色，提供 Clawd 角色、核心绘画工具和时间线。 | 图像与音视频 | 2995 |
| [花叔艺术动画](docs/huashu-art-motion.md#中文) | 当前 README 列出 36 种艺术风格、9 种解说语法和 8 种参数化片段。 | 图像与音视频 | 6941 |
| [Huashu Design](docs/huashu-design.md#中文) | 面向智能体的 HTML 原生设计技能。可制作网页、App 原型、可编辑 PPTX、动画和信息图。 | 图像与音视频 | 29538 |
| [15 种动态设计风格](docs/mg-styles-15.md#中文) | 15 支 10 秒动态设计示例，逐项公开风格说明、完整提示词与源码。 | 图像与音视频 | 3540 |
| [手绘口播视频](docs/sweety-handdraw-video.md#中文) | Agent 整理内容、口播和分镜，本地工具执行描线、填色、手写文字与声音对齐。 | 图像与音视频 | 1218 |
| [Teardown：交互式机械拆解与3D演示](docs/teardown.md#中文) | 面向 Claude Code 的 3D 机械原理演示技能。支持部件拆解、剖视、联动、自动演示与人工交互，可构建离线 HTML 并录制 MP4。 | 图像与音视频 | 3534 |
| [产品宣传片制作](docs/video-shotcraft.md#中文) | 面向产品发布和功能演示，采集真实页面素材后用 Remotion 编排影片。 | 图像与音视频 | 19790 |
| [VoiceStudio](docs/voicestudio.md#中文) | 在本地运行语音克隆、声音设计、转录和视频配音。另提供听写、有声书、批量任务及本地 API 与 MCP 接口。 | 图像与音视频 | 110994 |
| [Clash Verge Rev](docs/clash-verge-rev.md#中文) | 基于 Tauri 的 mihomo 图形代理客户端。提供配置管理、规则编辑、系统代理、TUN 模式和 WebDAV 同步。 | 部署与运维 | 158520 |
| [best-skills](docs/best-skills.md#中文) | 收集采用 SKILL.md 格式的智能体工作流程。覆盖论文、专利、汇报、自媒体、图表和代码文档。 | 文档与效率 | 3176 |
| [GenOffice](docs/genoffice.md#中文) | 提供 Office、PDF、Markdown 和 HTML 文件编辑。包含桌面编辑器、CLI、MCP 和智能体技能，可创建、转换和检索文件。 | 文档与效率 | 12376 |
| [Horizon：AI 信息聚合与双语新闻简报](docs/horizon.md#中文) | 聚合 RSS、社区、GitHub 与新闻等信息源，按 Profile 评分、筛选和去重，生成中英双语 Markdown 日报。 | 文档与效率 | 14389 |
| [Ghostty](docs/ghostty.md#中文) | 使用原生界面和 GPU 渲染的终端模拟器。支持多窗口、标签页与分屏，另提供可嵌入终端库。 | 终端与 Shell | 64125 |

## 候选（27）

| 项目 | 候选原因 | 分类 | Star |
| --- | --- | --- | ---: |
| [微舆（BettaFish）](docs/bettafish.md#中文) | 许可证待复核 | AI 工具 | 42701 |
| [cc-connect](docs/cc-connect.md#中文) | 许可证待复核 | 自动化 | 16376 |
| [easyquotation](docs/easyquotation.md#中文) | 缺少近期有效维护证据 | 数据处理 | 5478 |
| [TradingAgents-CN](docs/tradingagents-cn.md#中文) | 应用层采用专有许可 | 数据处理 | 32957 |
| [Nextpad++ for macOS](docs/nextpad-plus-plus-macos.md#中文) | 许可证待复核 | 开发辅助 | 1445 |
| [OpenTest（功能待公开）](docs/opentest.md#中文) | 许可证待复核 | 开发辅助 | 3 |
| [Public APIs](docs/public-apis.md#中文) | 双语内容待复核 | 开发辅助 | 499152 |
| [Serena](docs/serena.md#中文) | 许可证待复核 | 开发辅助 | 31391 |
| [Awesome DESIGN.md](docs/awesome-design-md.md#中文) | 双语内容待复核 | 图像与音视频 | 127606 |
| [拾景纸刊：照片与撕纸拼贴](docs/gathered-scenes-zine-skill.md#中文) | 许可证待复核 | 图像与音视频 | 5660 |
| [Heytea Doodle Poster：实物照片与小人涂鸦](docs/heytea-style.md#中文) | Star 未满 1000 | 图像与音视频 | 350 |
| [Ian Xiaohei Illustrations](docs/ian-xiaohei-illustrations.md#中文) | 双语内容待复核 | 图像与音视频 | 13217 |
| [Lemo-Opuscar](docs/lemo-opuscar.md#中文) | 许可证待复核 | 图像与音视频 | 16446 |
| [Photo Relic Editorial：照片与纸上印迹](docs/photo-relic-editorial.md#中文) | Star 未满 1000 | 图像与音视频 | 454 |
| [照片转海报：厚涂微缩景观与水彩旅行卡](docs/photo-to-poster-skills.md#中文) | Star 未满 1000 | 图像与音视频 | 36 |
| [Photo-to-Zine：照片明信片正反面](docs/photo-to-zine-postcard.md#中文) | Star 未满 1000 | 图像与音视频 | 289 |
| [TelemetryCleaner](docs/telemetrycleaner.md#中文) | Star 未满 1000 | 部署与运维 | 807 |
| [中国独立开发者项目列表](docs/chinese-independent-developer.md#中文) | 许可证待复核 | 文档与效率 | 62115 |
| [Clash 客户端导航（clashbk）](docs/clash.md#中文) | 许可证待复核 | 文档与效率 | 11389 |
| [中小学·高中知识图谱（cn-math-taxonomy）](docs/cn-math-taxonomy.md#中文) | 许可证待复核 | 文档与效率 | 8095 |
| [狗头军师](docs/goutoujunshi.md#中文) | 双语内容待复核 | 文档与效率 | 9693 |
| [程序员做饭指南](docs/howtocook.md#中文) | 双语内容待复核 | 文档与效率 | 103951 |
| [人情世故指南](docs/howtogetalong.md#中文) | 许可证待复核 | 文档与效率 | 2048 |
| [高性价比人生指南](docs/howtolivebetter.md#中文) | 许可证不符合开源条件 | 文档与效率 | 75865 |
| [程序员延寿指南](docs/howtolivelonger.md#中文) | 双语内容待复核 | 文档与效率 | 36107 |
| [投资入门指南](docs/investing-for-beginners.md#中文) | 许可证待复核 | 文档与效率 | 4539 |
| [人生进阶指南](docs/up.md#中文) | 许可证待复核 | 文档与效率 | 70565 |

## 新增或更新

在 `docs/<项目名>.md` 中维护一份双语介绍，包含 GitHub 地址、用途、功能、环境、限制、入门方式和来源。记录 Star、许可证、有效维护证据和核对日期，再更新两份 README 中的目录行。

仅阅读文档时注明“文档复核”；未安装或试用的功能不能写成实测结果。参考现有词条的格式即可。

## 目录结构

```text
README.md          中文说明与目录
README.en.md       English guide and index
docs/<项目名>.md   每个项目一份双语介绍
LICENSE            仓库许可证
.gitignore         本地文件忽略规则
```

## 许可证

本仓库采用 [Apache License 2.0](LICENSE)。各工具保留自己的许可证，具体限制见项目介绍和上游文件。
