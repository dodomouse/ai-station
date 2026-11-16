<p align="center">
  <img src="assets/readme/logo.svg" alt="ai-station" width="96" />
</p>

<a id="ai-station"></a>

<h1 align="center">ai-station</h1>

<p align="center">中英文 GitHub 工具目录。按用途查找，先看环境与限制。</p>

<p align="center">
  <a href="#included"><img src="https://img.shields.io/badge/included-182-2563eb?style=flat-square" alt="182 included projects" /></a>
  <a href="#candidates"><img src="https://img.shields.io/badge/candidates-27-64748b?style=flat-square" alt="27 candidates" /></a>
  <a href="#categories"><img src="https://img.shields.io/badge/categories-9-0f766e?style=flat-square" alt="9 categories" /></a>
  <img src="https://img.shields.io/badge/languages-中文%20%2F%20English-7c3aed?style=flat-square" alt="Chinese and English" />
</p>

<p align="center"><strong>简体中文</strong> · <a href="README.en.md">English</a></p>

<p align="center"><a href="#featured">精选入口</a> · <a href="#categories">分类浏览</a> · <a href="#criteria">收录标准</a> · <a href="reviews/2026-11-16-wechat.md">复核记录</a></p>

<p align="center">
  <img src="assets/readme/hero.zh-CN.svg" alt="按开发、AI、媒体、文档和运维等用途组织的工具目录" width="960" />
</p>

现有 209 个项目，分为 **182 个已收录**、**27 个候选**，覆盖九类用途。每个项目用一份双语词条说明用途、功能、环境、限制、入门方式和复核证据。

可以按任务寻找工具、比较使用条件，也可以挑选适合学习的源码项目。在浏览器中阅读目录，选定项目后再按其官方说明配置环境。

<a id="start"></a>

## 如何查找

1. **从任务出发。** 先看[精选入口](#featured)，或进入[九类目录](#categories)。
2. **缩小范围。** 展开分类后，用 Ctrl/⌘+F 搜索名称或用途；也可用 GitHub 仓库内搜索查找 `docs/` 中的词条。
3. **判断是否适合。** 打开词条，查看环境、许可限制与复核日期，再前往上游官方文档。

<p align="center">
  <img src="assets/readme/workflow.zh-CN.svg" alt="选择用途、阅读词条、核对证据，再按上游说明开始使用" width="960" />
</p>

<a id="featured"></a>

## 精选入口

从常见任务中挑选六个入口，依据已记录的用途展示，不作排名，也不代表经过实机测试。

| 想做什么 | 项目入口 | 使用前先看 |
| --- | --- | --- |
| 看看本机能跑哪些模型 | [llmfit](docs/llmfit.md#中文) | 估算内存与显存适配；估算结果不等于实测速度。 |
| 把技术栈画成架构图 | [Stack Diagram](docs/stack-diagram.md#中文) | 导出 SVG、HTML 或 PNG；PNG 需额外浏览器依赖。 |
| 用网页技术制作视频 | [Hyperframes](docs/hyperframes.md#中文) | HTML/CSS 动画渲染为 MP4；需 Node.js、FFmpeg 与 Chromium。 |
| 整理研究笔记与长文 | [Zettlr](docs/zettlr.md#中文) | Markdown 写作、引用与导出；文献库及导出环境需配置。 |
| 观察主机与服务指标 | [Netdata Agent](docs/netdata.md#中文) | 收录开源 Agent 核心；Web 界面与 Cloud 许可独立。 |
| 把移动设备接入智能体 | [Mobile MCP](docs/mobile-mcp.md#中文) | 操作 Android/iOS 应用；需 MCP 客户端与平台设备工具。 |

<a id="criteria"></a>

## 收录标准

- **具体价值。** 核对用途、功能实现、文档和使用入口。Star 只记录，不设最低值；低 Star 项目须写明具体质量理由，实验项目须说明适用范围。
- **近期实质活动。** 最近 **3 个日历月**内，必须有已确认的功能、缺陷修复、实质合并变更或正式发行。纯文档、机械性机器人更新和 `pushed_at` 不单独计入。首次完整功能实现可以计入，但不能据此声称长期维护。
- **许可与范围清楚。** 仓库公开、未归档、未禁用，并复核开源许可原文。混合许可只收录明确开放的组件；模型权重、数据、素材与付费服务分别核对。
- **证据可追溯。** 中英文内容都需复核，并记录来源、许可、活动证据和日期。所用仓库快照在评估时不超过 7 天，记录过期后应重新核对。

以上标准自 2026-11-16 起采用。收录表示完成了相应复核，不等于已通过性能、兼容性或安全实测；既有候选结论保留为历史记录，等待重新评估。

<a id="categories"></a>

## 分类导航

选择分类后展开列表。分类计数包含原有词条与本轮新增。

| 分类 | 可以找到 | 已收录 | 候选 |
| --- | --- | ---: | ---: |
| [AI 工具](#included-ai) | 模型、智能体、记忆与知识库 | [38](#included-ai) | [1](#candidate-ai) |
| [开发辅助](#included-development) | 编码、审查、界面与工程工具 | [52](#included-development) | [4](#candidate-development) |
| [图像与音视频](#included-media) | 图像、动画、音频与视频制作 | [35](#included-media) | [8](#candidate-media) |
| [文档与效率](#included-productivity) | 写作、笔记、办公与日常工具 | [27](#included-productivity) | [10](#candidate-productivity) |
| [自动化](#included-automation) | 任务调度、设备与应用控制 | [9](#included-automation) | [1](#candidate-automation) |
| [部署与运维](#included-operations) | 部署、监控、系统与服务管理 | [9](#included-operations) | [1](#candidate-operations) |
| [数据处理](#included-data) | 数据查询、研究与分析流程 | [6](#included-data) | [2](#candidate-data) |
| [终端与 Shell](#included-terminal) | 终端环境与命令行工具 | [3](#included-terminal) | 0 |
| [知识与学习](#included-knowledge) | 教材、图谱与交互学习材料 | [3](#included-knowledge) | 0 |

<a id="included"></a>

## 已收录（182）

点击名称查看双语介绍与带日期的证据。下表 Star 为复核时快照，不作实时排名。

<a id="included-ai"></a>

<details>
<summary><strong>AI 工具</strong> · 38 项</summary>

| 项目 | 用途 | 分类 | Star |
| --- | --- | --- | ---: |
| [Agent Reach](docs/agent-reach.md#中文) | 为 Agent 提供网页与社交平台的搜索、阅读和内容获取能力，整合视频、论坛及多个中文平台渠道。 | AI 工具 | 112225 |
| [ai-memory](docs/ai-memory.md#中文) | 为 AI 编码工具提供跨会话记忆和跨工具交接。使用 Git 管理的 Markdown 保存知识，并提供检索和摘要注入。 | AI 工具 | 15919 |
| [Claude-Mem](docs/claude-mem.md#中文) | 记录编码智能体的工作观察，在后续会话中检索和恢复相关记忆。 | AI 工具 | 117552 |
| [Codex ChatGPT Web Bridge](docs/codex-chatgpt-web.md#中文) | 通过本机登录的ChatGPT网页会话，为Codex提供第三方模型桥接。 | AI 工具 | 15746 |
| [DeepInfer](docs/deepinfer.md#中文) | 面向 DeepSeek 模型的推理实现，提供高性能计算与分布式执行组件。 | AI 工具 | 26102 |
| [DeepSeek chat-demo](docs/deepseek-chat-demo.md#中文) | 通过 DeepSeek API 提供聊天界面的静态网页示例。支持流式回答、会话分支、附件和历史导入导出。 | AI 工具 | 3890 |
| [DSH Desktop](docs/dsh-desktop.md#中文) | DeepSeek Harness 桌面工作台，组织模型、Office 模板、技能和插件，可生成或处理文档、表格与演示文稿。 | AI 工具 | 19341 |
| [dsh-superagent 研究原型](docs/dsh-superagent-prototype.md#中文) | 面向单个 GitHub 仓库的主动编码智能体研究原型。监听 GitHub 和可选飞书消息，按授权创建并执行工作项。 | AI 工具 | 23202 |
| [FreeLLM API](docs/freellmapi.md#中文) | 把用户自己的多个模型提供商账号接到本地网关，提供兼容 OpenAI 的接口、路由、失败切换和额度跟踪。 | AI 工具 | 53227 |
| [FreeToken](docs/freetoken.md#中文) | 在本地运行混合专家模型的推理引擎。组合 GPU、CPU 和系统内存，提供专家缓存和模型服务接口。 | AI 工具 | 17244 |
| [Geo Sleuth](docs/geo-sleuth.md#中文) | 为 Agent 提供照片地理定位流程，综合地形、天际线、道路和地图检索，输出候选位置、观察方向与证据。 | AI 工具 | 7109 |
| [Heretic](docs/heretic.md#中文) | 通过免训练的参数修改研究语言模型的回答风格、拒答与迎合行为。 | AI 工具 | 40743 |
| [Hindsight](docs/hindsight.md#中文) | 为智能体保存事实与经历，并按问题检索或综合相关记忆。 | AI 工具 | 61351 |
| [Jev Chat Jarvis](docs/jev-chat-jarvis.md#中文) | Android 聊天辅助浮层，使用无障碍与 OCR 获取当前聊天上下文，生成分析和回复草稿，由用户选择插入。 | AI 工具 | 8409 |
| [Laya-MLX](docs/laya-mlx.md#中文) | 在Apple Silicon上用MLX运行结构化选择、评分和真假判断模型。 | AI 工具 | 7107 |
| [Laya](docs/laya.md#中文) | 面向文本分类、选项判断、评分和路由的非自回归决策引擎，输出结构化结果与置信信息。 | AI 工具 | 35592 |
| [llmfit](docs/llmfit.md#中文) | 检测 CPU、内存和 GPU 显存，估算本地模型及量化版本的适配程度，并提供 TUI、网页、CLI/API 与基准测试入口。 | AI 工具 | 39014 |
| [Magpie](docs/magpie.md#中文) | 通过本地网关统一管理编码智能体的模型与服务商。提供多账号路由、故障转移及可选请求脱敏。 | AI 工具 | 36740 |
| [MiniMind](docs/minimind.md#中文) | 用较小语言模型学习从预训练、微调到推理服务的完整实现。 | AI 工具 | 65498 |
| [Octop](docs/octop.md#中文) | 可自托管的多用户、多 Agent 助手，提供专家库、网页/CLI/消息渠道、定时任务、知识库及 MCP/ACP 接口。 | AI 工具 | 12113 |
| [oMLX](docs/omlx.md#中文) | 为 Apple 芯片 Mac 提供本地模型推理服务和菜单栏管理界面。 | AI 工具 | 23663 |
| [Open Interpreter](docs/open-interpreter.md#中文) | 当前主线是基于 Rust 的终端编码 Agent，连接模型提供商，提供工具调用、MCP/ACP、技能和原生沙箱。 | AI 工具 | 68895 |
| [OpenDots](docs/opendots.md#中文) | 持久化 AI 同事的社区模板，通过网页、手机和消息渠道与 Agent 交互，并提供各自的电脑工作区。 | AI 工具 | 6624 |
| [OpenFuse（原OpenMuse）](docs/openfuse.md#中文) | 提供带浏览器、终端和文件工作区的个人智能体应用模板。 | AI 工具 | 6496 |
| [OpenHands](docs/openhands.md#中文) | 用于软件开发任务的智能体工作台，提供会话、工具执行与变更审查。 | AI 工具 | 93582 |
| [OpenMAIC](docs/openmaic.md#中文) | 把主题或文档转成包含 AI 教师与同学的交互式课堂。 | AI 工具 | 43722 |
| [OpenMausBot](docs/openmausbot.md#中文) | 以联系人和群聊组织多个编码智能体。可为各机器人配置模型、工作目录、连接应用和执行环境。 | AI 工具 | 23982 |
| [OpenViking](docs/openviking.md#中文) | 用可浏览的虚拟文件系统组织智能体知识、记忆和技能。 | AI 工具 | 42305 |
| [Paperclip](docs/paperclip.md#中文) | 管理 AI 团队的组织、目标、任务、权限和预算，连接已有 Agent，并跟踪执行与模型成本。 | AI 工具 | 114265 |
| [PilotDeck](docs/pilotdeck.md#中文) | 围绕独立工作区组织智能体任务、记忆、技能和长期运行。 | AI 工具 | 4998 |
| [Prime Agent](docs/prime-agent.md#中文) | 以持久Python环境、子智能体和后台会话执行编码与研究任务。 | AI 工具 | 22746 |
| [Rakazo](docs/rakazo.md#中文) | 可自行部署的 AI 团队工作台，集中管理长期记忆、例行任务与智能体电脑。 | AI 工具 | 8776 |
| [StarNet](docs/starnet.md#中文) | 以像素空间站界面管理多个在本机工作的智能体。 | AI 工具 | 1854 |
| [Suparagent](docs/suparagent.md#中文) | 为多个具名智能体提供会话、工作区、记忆、例行任务与审批界面。 | AI 工具 | 7087 |
| [SuperMimic](docs/supermimic.md#中文) | 面向人形机器人的动作跟踪研究实现。使用可微世界模型训练全身动作控制策略。 | AI 工具 | 1646 |
| [TimesFM（开源代码与 ≤2.5 权重）](docs/timesfm.md#中文) | Google Research 的时间序列预测代码库，提供预训练模型调用、分位数预测和协变量支持；本词条收录 Apache-2.0 源代码及 2.5 或更早的开源权重。 | AI 工具 | 35602 |
| [Unsloth](docs/unsloth.md#中文) | 模型运行与微调工具，覆盖语言、扩散、语音和嵌入模型，并提供本地桌面/Studio 工作流。 | AI 工具 | 79601 |
| [WeKnora](docs/weknora.md#中文) | 企业文档知识库与 RAG 问答服务，整合文档解析、检索、Agent 和 Wiki 工作流。 | AI 工具 | 37540 |

</details>

<a id="included-development"></a>

<details>
<summary><strong>开发辅助</strong> · 52 项</summary>

| 项目 | 用途 | 分类 | Star |
| --- | --- | --- | ---: |
| [2010 Rust Rewrite Mashup](docs/2010-rust-rewrite-mashup.md#中文) | 以 Rust 实现的游戏混搭实验，把 MW2 风格场景、滑板和体素地图组合起来，可用于学习游戏重实现与资源兼容。 | 开发辅助 | 951 |
| [AI Infra Book](docs/ai-infra-book.md#中文) | AI 基础设施教材与计算工具，覆盖硬件、模型架构、推理和训练，并提供在线版、PDF/EPUB 及容量估算脚本。 | 开发辅助 | 7897 |
| [AI Website Cloner Template：网站复刻与迁移模板](docs/ai-website-cloner-template.md#中文) | 用编码助手观察目标网页，再以 Next.js 重建页面、素材和交互。通过浏览器对照差异并修正。 | 开发辅助 | 39159 |
| [AnyPS5](docs/anyps5.md#中文) | 研究把控制台可执行文件重链接到桌面平台的兼容性工具。 | 开发辅助 | 54377 |
| [Archify](docs/archify.md#中文) | 把想法、计划或代码仓资料生成交互式 HTML 图示。可制作架构图、流程图和带来源的解释页面。 | 开发辅助 | 96538 |
| [Claude Code Game Studios](docs/claude-code-game-studios.md#中文) | 为 Claude Code 提供游戏开发模板和技能。可从玩法描述生成简要设计、浏览器原型，并逐步修改和扩展。 | 开发辅助 | 39708 |
| [Claude Community Plugins：目录与校验器](docs/claude-plugins-community.md#中文) | 提供Claude社区插件目录，以及可复用的插件市场CI校验器。 | 开发辅助 | 4903 |
| [Claude Plugins Official](docs/claude-plugins-official.md#中文) | Anthropic 维护的 Claude 插件目录，提供开发与工作流程扩展。 | 开发辅助 | 47430 |
| [Claude Red](docs/claude-red.md#中文) | 面向授权安全研究和 CTF 的 Claude Code 技能集合。 | 开发辅助 | 11091 |
| [CLI-Anything](docs/cli-anything.md#中文) | 分析软件源码，为真实应用后端生成 CLI harness。提供结构化命令、JSON 输出、交互式 REPL 及测试流程。 | 开发辅助 | 58741 |
| [code-review-graph](docs/code-review-graph.md#中文) | 用 Tree-sitter 建立并增量更新本地代码结构图。通过 MCP 和 CLI 提供依赖、变更影响及审查上下文。 | 开发辅助 | 32776 |
| [Codex with ChatGPT](docs/codex-with-chatgpt.md#中文) | 用只读 MCP 连接将 ChatGPT 网页的规划与审查接入 Codex 工作区。 | 开发辅助 | 7718 |
| [Cordis](docs/cordis.md#中文) | 用于 TypeScript 应用的组件、服务依赖和生命周期管理框架。 | 开发辅助 | 9915 |
| [Craft Anything](docs/craft-anything.md#中文) | 研究网站、应用或游戏，再让编码智能体创建自己的版本。提供研究、构建、比较与修改流程，以及 CLI、MCP 和检查证据。 | 开发辅助 | 33239 |
| [ECC](docs/ecc.md#中文) | 为编码智能体组合规划、审查、记忆、上下文管理和工程检查。 | 开发辅助 | 304243 |
| [Flutter](docs/flutter.md#中文) | 使用 Dart 为移动端、网页和桌面端构建应用的 UI 工具包。 | 开发辅助 | 181237 |
| [Ghidra](docs/ghidra.md#中文) | 用于分析编译后程序的逆向工程框架，提供反汇编、反编译与脚本扩展。 | 开发辅助 | 100277 |
| [Godogen](docs/godogen.md#中文) | 通过编码 Agent 生成独立游戏工程与素材，支持 Godot、Bevy、Babylon.js 和 Three.js 等目标，并提供运行验证流程。 | 开发辅助 | 7354 |
| [GPUI Kit](docs/gpui-kit.md#中文) | 基于 Rust GPUI 的桌面界面组件库，提供表格、编辑器、布局、可访问性支持与可选 JavaScript 宿主。 | 开发辅助 | 20833 |
| [Graphify](docs/graphify.md#中文) | 把源码、文档及多媒体资料组织成可查询知识图谱。提供关系解释、路径查询、子图检索和交互图页面。 | 开发辅助 | 148039 |
| [Hallmark](docs/hallmark.md#中文) | 帮助编码智能体选择视觉风格、制作界面并检查页面设计。 | 开发辅助 | 55872 |
| [Henge](docs/henge.md#中文) | 在 iPhone 和 iPad 上以 JIT 模拟器运行 macOS，用于系统兼容性实验。 | 开发辅助 | 2357 |
| [Impeccable](docs/impeccable.md#中文) | 为编码智能体提供前端设计、审查和调整命令。 | 开发辅助 | 111148 |
| [islandcn](docs/islandcn.md#中文) | 为 React 网页提供灵动岛样式的活动提示组件。包含活动状态、展开收起、动画和多个用途预设。 | 开发辅助 | 760 |
| [JADX](docs/jadx.md#中文) | 把 Android DEX、APK 和 Java 字节码转换为便于阅读的 Java 源码。 | 开发辅助 | 51846 |
| [LASRecomp](docs/lasrecomp.md#中文) | 将《塞尔达传说：织梦岛》Switch 版本重编译为桌面或移动端原生程序，提供图形、输入和平台兼容代码。 | 开发辅助 | 2451 |
| [Lightpanda Browser](docs/lightpanda.md#中文) | 面向自动化和智能体的无头浏览器。执行网页脚本、操作页面并提取 HTML、Markdown 或结构化内容。 | 开发辅助 | 42129 |
| [MacNativeGames](docs/macnativegames.md#中文) | 研究将指定游戏的图形与系统调用适配到 Apple 芯片和 Metal。 | 开发辅助 | 7913 |
| [Moli：面向 AI 智能体的无头浏览器](docs/moli.md#中文) | Rust 编写的独立无头浏览器，支持 JavaScript 网页运行、Markdown 与语义树提取、按需布局，以及 CLI、CDP 和 WebDriver 自动化。 | 开发辅助 | 23783 |
| [nxnative](docs/nxnative.md#中文) | 将用户自有 Switch 游戏程序转换为原生 Apple 平台应用，提供 Horizon 系统调用和图形接口的兼容层，适合研究静态重编译。 | 开发辅助 | 15844 |
| [Open Code Review](docs/open-code-review.md#中文) | 读取 Git 差异或整份文件，让可配置模型生成带行号的代码审查意见。 | 开发辅助 | 52711 |
| [OpenSmash-Ultimate](docs/opensmash-ultimate.md#中文) | 通过静态重编译研究让用户自备的特定 Switch 游戏在桌面平台运行。 | 开发辅助 | 188 |
| [Orca（智能体开发工作台）](docs/orca.md#中文) | 统一管理多个编程智能体的开发工作台。提供并行工作目录、终端、差异审查、手机端及 SSH 远程环境。 | 开发辅助 | 125338 |
| [Ponytail](docs/ponytail.md#中文) | 帮助编码智能体复用已有实现、审查变更，并记录任务成本与测试状态。 | 开发辅助 | 191880 |
| [REA — Reverse Engineer Anything](docs/rea.md#中文) | 通过 MCP 和 CLI 连接逆向分析工具。可分析原生二进制、JavaScript、Electron、.NET 及网站。 | 开发辅助 | 460761 |
| [S2Arm](docs/s2arm.md#中文) | 将用户自备的部分 Switch 游戏代码转换为苹果设备的 ARM64 程序，并提供图形化打包与游戏库管理。 | 开发辅助 | 3346 |
| [Screenshot to Code](docs/screenshot-to-code.md#中文) | 根据截图、设计图或录屏生成网页界面代码，并迭代调整。 | 开发辅助 | 81243 |
| [Security Audit Skill](docs/security-audit-skill.md#中文) | 组织源码安全审计，并用脚本检查覆盖记录和结构化发现。 | 开发辅助 | 73608 |
| [Semantica](docs/semantica.md#中文) | 把多来源资料组织为知识图谱与上下文图，并记录数据来源和推理过程。 | 开发辅助 | 14627 |
| [Skills For Real Engineers（Matt Pocock）](docs/skills.md#中文) | 面向编程智能体的工程技能集合。覆盖需求澄清、架构决策、测试驱动开发、重构和任务组织。 | 开发辅助 | 324716 |
| [SkillSpector](docs/skillspector.md#中文) | 扫描智能体技能中的可疑指令、代码行为和安全问题。 | 开发辅助 | 26363 |
| [Spec Kit](docs/spec-kit.md#中文) | 提供规格驱动开发的 CLI、技能和模板。把需求规格转换为计划、任务和代码，并支持检查与缺陷修复流程。 | 开发辅助 | 149841 |
| [Stack Diagram](docs/stack-diagram.md#中文) | 把技术栈描述转换为带服务图标和连线的架构图，支持 SVG、HTML、PNG 和明暗主题，适合项目说明与设计文档。 | 开发辅助 | 2537 |
| [T3 Code](docs/t3code.md#中文) | 统一管理多个编码 Agent 的会话、变更差异和远程连接，可从桌面、网页或手机继续开发任务。 | 开发辅助 | 62317 |
| [Taste Skill](docs/taste-skill.md#中文) | 为编码智能体提供网页设计流程、素材工具和浏览器检查脚本。 | 开发辅助 | 116605 |
| [Text to CAD](docs/text-to-cad.md#中文) | 把自然语言设计需求转成参数化 CAD 脚本和制造文件的智能体工具。 | 开发辅助 | 26417 |
| [Univer](docs/univer.md#中文) | 用于嵌入网页的电子表格与文档 SDK，提供公式计算、渲染、编辑和程序接口，也支持无界面处理。 | 开发辅助 | 27511 |
| [Universal Modder](docs/universal-modder.md#中文) | 提供游戏模组制作的 Agent 技能、um 命令行工具和知识库，覆盖引擎识别、资源处理与游戏内验证。 | 开发辅助 | 9725 |
| [Voxel Musou](docs/voxel-musou.md#中文) | 浏览器 Three.js 体素动作游戏示例，包含多角色、章节与试炼，适合研究轻量游戏逻辑、渲染和本地进度管理。 | 开发辅助 | 178 |
| [vphone-cli](docs/vphone-cli.md#中文) | 在Apple Silicon Mac上运行用于研究与调试的虚拟iPhone。 | 开发辅助 | 16695 |
| [Wakaru](docs/wakaru.md#中文) | JavaScript 反编译工具，可拆分打包文件、展开压缩代码并恢复部分转译结构，提供 CLI 和网页试用。 | 开发辅助 | 1090 |
| [Worktrunk](docs/worktrunk.md#中文) | 简化 Git worktree 的切换、查看和清理，支持并行编码任务。 | 开发辅助 | 12565 |

</details>

<a id="included-media"></a>

<details>
<summary><strong>图像与音视频</strong> · 35 项</summary>

| 项目 | 用途 | 分类 | Star |
| --- | --- | --- | ---: |
| [3D Model Anything](docs/3d-model-anything.md#中文) | 把房间扫描资料转成可编辑 Three.js 场景的工具与智能体工作流程。 | 图像与音视频 | 3031 |
| [Abyssal Garden](docs/abyssal-garden.md#中文) | 以单个 HTML 展示可交互的海底场景。使用 WebGPU 绘制地形和生物，并实时合成声音。 | 图像与音视频 | 1440 |
| [Anatomy](docs/anatomy.md#中文) | 用交互式等轴测图解释机械、仪器和抽象机制。生成 SVG、HTML 或 React 组件，可叠加 WebGL 与 3D 效果。 | 图像与音视频 | 27394 |
| [代码手绘插画与动画](docs/anidoodle.md#中文) | 以代码描述笔画，提供 32 种插画风格和逐笔绘制示例。 | 图像与音视频 | 1693 |
| [Animate 程序化动画](docs/animate.md#中文) | 以单个 Canvas 程序化绘制和配乐，用无头浏览器与 FFmpeg 输出 MP4。 | 图像与音视频 | 1967 |
| [Arnis](docs/arnis.md#中文) | 把真实地理与高程数据转换成方块游戏世界。 | 图像与音视频 | 18642 |
| [ArtCraft](docs/artcraft.md#中文) | 桌面 AI 创作工作台，结合二维画面编排、三维场景和图像/视频模型，组织生成素材与创作流程。 | 图像与音视频 | 41207 |
| [ASCII](docs/ascii.md#中文) | 可嵌入网页的 TypeScript ASCII 动画组件，支持 React、Next.js、Astro、Web Components 和普通 HTML，也可生成 SVG。 | 图像与音视频 | 1232 |
| [Bang Motion](docs/bang-motion.md#中文) | 将开场、宣传片、产品演示、动态文字和讲解组织成可播放的单个 index.html。 | 图像与音视频 | 2201 |
| [cinecode](docs/cinecode.md#中文) | 面向编码智能体的影片制作技能。用网页画布或 Three.js 编排画面与声音，通过浏览器和 FFmpeg 输出 MP4。 | 图像与音视频 | 2593 |
| [Claude Animated Shorts](docs/claude-animated-shorts.md#中文) | 面向 Claude Code 的竖屏动画短片技能。用 Three.js 与 Remotion 渲染角色、场景和声音，附带桥梁故事示例。 | 图像与音视频 | 3658 |
| [Claude Animation Base](docs/claudeanimationbase.md#中文) | 以 p5.js 与 p5.brush 绘制角色，提供 Clawd 角色、核心绘画工具和时间线。 | 图像与音视频 | 2995 |
| [Deskworlds](docs/deskworlds.md#中文) | 在Mac桌面运行可交互的本地3D场景，也可在浏览器中体验。 | 图像与音视频 | 468 |
| [Diagram Design](docs/diagram-design.md#中文) | 把结构、流程和比较关系制作成独立 HTML 与 SVG 图表的智能体技能。 | 图像与音视频 | 67558 |
| [GIF 工厂 / GIF Factory](docs/gif-factory.md#中文) | 面向编码智能体的图像与动画技能集合。提供表情包、动态海报、签名、绘本和知识短片的制作说明与脚本。 | 图像与音视频 | 1940 |
| [God's Eye View](docs/gods-eye-view.md#中文) | 在交互式三维地球上叠加公开交通、地理与环境数据。 | 图像与音视频 | 65241 |
| [Handy](docs/handy.md#中文) | 通过快捷键录音，在本地识别语音，再把文字粘贴到当前输入位置。可选择 Whisper 或 Parakeet 等模型。 | 图像与音视频 | 38948 |
| [Hex](docs/hex.md#中文) | 在本机把语音转成文字并输入当前应用。支持词汇表、转写历史、文本处理步骤和录音文件转写。 | 图像与音视频 | 7045 |
| [Holo Card Studio](docs/holo-card-studio.md#中文) | 把分层图片制作成可旋转的全息卡网页和可编辑Blender工程。 | 图像与音视频 | 2106 |
| [HolyArrs](docs/holyarrs.md#中文) | 在自托管网页中管理媒体请求、筛选规则、字幕和文件入库。可连接现有下载器与媒体服务器。 | 图像与音视频 | 1325 |
| [花叔艺术动画](docs/huashu-art-motion.md#中文) | 当前 README 列出 36 种艺术风格、9 种解说语法和 8 种参数化片段。 | 图像与音视频 | 6941 |
| [Huashu Design](docs/huashu-design.md#中文) | 面向智能体的 HTML 原生设计技能。可制作网页、App 原型、可编辑 PPTX、动画和信息图。 | 图像与音视频 | 29538 |
| [Hyperframes](docs/hyperframes.md#中文) | 用 HTML/CSS 和可定位时间的动画制作视频，通过无头浏览器与 FFmpeg 确定性渲染 MP4；提供 CLI、Agent 技能和桌面工作台。 | 图像与音视频 | 85034 |
| [Mac Duo](docs/mac-duo.md#中文) | 根据 MacBook 屏幕开合角度，为实时桌面画面添加倾斜、模糊和渐暗效果。 | 图像与音视频 | 1236 |
| [MCP for Blender](docs/mcp-for-blender.md#中文) | 通过 MCP 把 Agent 连接到 Blender，用自然语言组织场景、模型、材质和渲染，并接入可选素材服务。 | 图像与音视频 | 34616 |
| [15 种动态设计风格](docs/mg-styles-15.md#中文) | 15 支 10 秒动态设计示例，逐项公开风格说明、完整提示词与源码。 | 图像与音视频 | 3540 |
| [MyGo Music](docs/mygo-music.md#中文) | 原生桌面音乐播放器，支持本地音乐、歌词、播放列表和插件。插件可接入音乐目录、播客和电台。 | 图像与音视频 | 1408 |
| [OpenCreator](docs/opencreator.md#中文) | 以对话与可视化工作区组织内容制作，管理生成任务、素材、字幕和版本。 | 图像与音视频 | 14380 |
| [Subvox](docs/subvox.md#中文) | 研究 AirPods 头部运动数据能否识别无声口型的小词汇量实验原型。 | 图像与音视频 | 838 |
| [手绘口播视频](docs/sweety-handdraw-video.md#中文) | Agent 整理内容、口播和分镜，本地工具执行描线、填色、手写文字与声音对齐。 | 图像与音视频 | 1218 |
| [Teardown：交互式机械拆解与3D演示](docs/teardown.md#中文) | 面向 Claude Code 的 3D 机械原理演示技能。支持部件拆解、剖视、联动、自动演示与人工交互，可构建离线 HTML 并录制 MP4。 | 图像与音视频 | 3534 |
| [Turbo Kart Rally](docs/turbo-kart-rally.md#中文) | 在浏览器中运行的 Three.js 卡丁车游戏和程序化内容示例。 | 图像与音视频 | 50 |
| [产品宣传片制作](docs/video-shotcraft.md#中文) | 面向产品发布和功能演示，采集真实页面素材后用 Remotion 编排影片。 | 图像与音视频 | 19790 |
| [VoiceStudio](docs/voicestudio.md#中文) | 在本地运行语音克隆、声音设计、转录和视频配音。另提供听写、有声书、批量任务及本地 API 与 MCP 接口。 | 图像与音视频 | 110994 |
| [YuE2 推理代码 / YuE2 inference code](docs/yue.md#中文) | 通过可编辑旋律与和弦计划生成包含人声和伴奏的歌曲。 | 图像与音视频 | 13534 |

</details>

<a id="included-productivity"></a>

<details>
<summary><strong>文档与效率</strong> · 27 项</summary>

| 项目 | 用途 | 分类 | Star |
| --- | --- | --- | ---: |
| [Aerial TV](docs/aerial-tv.md#中文) | Android TV 桌面启动器，提供应用网格、文件夹、HDMI 入口、壁纸屏保和手机遥控管理。 | 文档与效率 | 12155 |
| [AirCursor](docs/aircursor.md#中文) | 把支持头部追踪的耳机动作转换为Mac鼠标移动与点击。 | 文档与效率 | 226 |
| [Anki Desktop](docs/anki.md#中文) | 用记忆卡片与间隔重复安排复习。 | 文档与效率 | 32834 |
| [best-skills](docs/best-skills.md#中文) | 收集采用 SKILL.md 格式的智能体工作流程。覆盖论文、专利、汇报、自媒体、图表和代码文档。 | 文档与效率 | 3176 |
| [CCBaga](docs/ccbaga.md#中文) | 管理本机 Claude 身份配置、客户端工具和配套浏览器环境。 | 文档与效率 | 3618 |
| [知了 Cicada](docs/cicada.md#中文) | 为会议和直播提供双语字幕、同声传译与会议纪要。直接读取系统声音，支持转写搜索和记录导出。 | 文档与效率 | 2347 |
| [ColaMD](docs/colamd.md#中文) | 跨平台 Markdown 编辑器，提供所见即所得与源码视图、文件同步、大纲和主题，并支持导出常用文档格式。 | 文档与效率 | 1303 |
| [Echo Loop](docs/echo-loop.md#中文) | 通过精听、跟读、复述和复习流程练习英语听说。 | 文档与效率 | 4772 |
| [GenOffice](docs/genoffice.md#中文) | 提供 Office、PDF、Markdown 和 HTML 文件编辑。包含桌面编辑器、CLI、MCP 和智能体技能，可创建、转换和检索文件。 | 文档与效率 | 12376 |
| [Horizon：AI 信息聚合与双语新闻简报](docs/horizon.md#中文) | 聚合 RSS、社区、GitHub 与新闻等信息源，按 Profile 评分、筛选和去重，生成中英双语 Markdown 日报。 | 文档与效率 | 14389 |
| [i-have-adhd](docs/i-have-adhd.md#中文) | 调整编码智能体的回答格式，使行动步骤和关键信息更容易找到。 | 文档与效率 | 61361 |
| [Joplin 客户端 / Joplin clients](docs/joplin.md#中文) | 以Markdown笔记本组织笔记、待办和附件，支持搜索与同步。 | 文档与效率 | 57204 |
| [Knowledge Work Plugins](docs/knowledge-work-plugins.md#中文) | 为知识工作提供按岗位组织的智能体技能、命令和连接器配置。 | 文档与效率 | 36258 |
| [MarkText](docs/marktext.md#中文) | 支持实时预览与文件管理的跨平台 Markdown 编辑器。 | 文档与效率 | 64049 |
| [妙言 / MiaoYan](docs/miaoyan.md#中文) | Swift 原生 macOS Markdown 笔记应用，管理本地文件与文件夹，支持双向链接、公式、Mermaid、历史记录和演示。 | 文档与效率 | 8781 |
| [OpenLogi](docs/openlogi.md#中文) | Rust 原生 Logitech 设备工具，通过 HID++/UVC 配置鼠标、键盘与摄像头，提供按钮、DPI、滚轮和跨电脑 Flow 等能力。 | 文档与效率 | 25783 |
| [OpenWhispr](docs/openwhispr.md#中文) | 跨平台语音输入与会议转写应用，通过快捷键把语音转换为当前光标处的文本，提供笔记、说话人区分和可选 AI 助手。 | 文档与效率 | 11669 |
| [中国专利 Skill](docs/patent-disclosure-skill.md#中文) | 从技术资料整理专利交底草稿，并辅助检索、阅读和案卷整理。 | 文档与效率 | 13513 |
| [PlayCover](docs/playcover.md#中文) | 在 Apple Silicon Mac 上运行兼容的 iOS 应用，提供键鼠和手柄映射。 | 文档与效率 | 12156 |
| [Read Frog](docs/read-frog.md#中文) | 结合网页翻译、字幕翻译和词汇复习的浏览器语言学习扩展。 | 文档与效率 | 10456 |
| [Tendedero](docs/tendedero.md#中文) | 在 macOS 屏幕顶部暂存截图、复制文本和链接，便于拖放与再次使用。 | 文档与效率 | 3263 |
| [VNote](docs/vnote.md#中文) | 在本地管理笔记，并编辑Markdown、Typst、文本和思维导图。 | 文档与效率 | 13048 |
| [Window Sweaters](docs/window-sweaters.md#中文) | 给 macOS 窗口添加针织风格边框，可为不同应用设置颜色或关闭装饰，并区分活动窗口。 | 文档与效率 | 1495 |
| [词光 Word Atlas](docs/word-atlas.md#中文) | 用插画、发音和间隔复习学习英语词汇的网页应用。 | 文档与效率 | 4915 |
| [Yank Note](docs/yank-note.md#中文) | 以本地 Markdown 文件保存笔记的可扩展编辑器。 | 文档与效率 | 6784 |
| [Yogurt](docs/yogurt.md#中文) | 在本机记录会议语音、生成转写和纪要，并从历史会议中回答问题、附上出处。 | 文档与效率 | 1788 |
| [Zettlr](docs/zettlr.md#中文) | 面向研究与长文写作的 Markdown 编辑器，提供文献引用、笔记链接、全文搜索和多格式导出。 | 文档与效率 | 13922 |

</details>

<a id="included-automation"></a>

<details>
<summary><strong>自动化</strong> · 9 项</summary>

| 项目 | 用途 | 分类 | Star |
| --- | --- | --- | ---: |
| [Agent Autoloop](docs/agent-autoloop.md#中文) | 把命令行智能体接入事件调度和后台执行。支持人工卡片、回答后继续、定时复查、日志重放及可选 PR 交付。 | 自动化 | 5427 |
| [agentes.chat](docs/agentes-chat.md#中文) | 让团队成员和智能体在频道与私信中协作。为智能体配置角色、模型、预算、工具和执行环境。 | 自动化 | 1597 |
| [Cua（MIT 桌面自动化组件）](docs/cua-mit-components.md#中文) | 收录 Cua 的 MIT 许可 SDK、CLI、Driver 和 Lume，用于 Agent 截图、输入控制及本地虚拟电脑管理。 | 自动化 | 32442 |
| [ESP32 iPhone Agent](docs/esp32-iphone-agent.md#中文) | 让智能体通过 ESP32-S3 与真实 iPhone 交互的软硬件项目。 | 自动化 | 5022 |
| [AX](docs/google-ax.md#中文) | 用声明式配置调度沙箱中的智能体任务和工作区。 | 自动化 | 14733 |
| [Mobile MCP](docs/mobile-mcp.md#中文) | 通过 MCP 让智能体操作 Android 与 iOS 应用、模拟器及真实设备。 | 自动化 | 10616 |
| [Reason Network](docs/reason-network.md#中文) | 每台电脑运行后台程序，共享团队 Agent 会话的人员、设备、项目、分支与工作概况。 | 自动化 | 1748 |
| [Voice Control Agent](docs/voice-control-agent.md#中文) | 为 Mac 上的 Codex 桌面会话提供本机唤醒、语音输入和回复朗读入口。 | 自动化 | 5 |
| [XGIMI Agent](docs/xgimi-agent.md#中文) | macOS 菜单栏与 Agent 技能，通过局域网控制用户自己的极米投影仪，提供遥控、截图与实验性蓝牙唤醒。 | 自动化 | 7 |

</details>

<a id="included-operations"></a>

<details>
<summary><strong>部署与运维</strong> · 9 项</summary>

| 项目 | 用途 | 分类 | Star |
| --- | --- | --- | ---: |
| [1Panel](docs/1panel.md#中文) | Linux 服务器的网页管理面板，管理容器、数据库、文件、站点与证书，并提供部分模型和 GPU 管理能力。 | 部署与运维 | 37458 |
| [Clash Verge Rev](docs/clash-verge-rev.md#中文) | 基于 Tauri 的 mihomo 图形代理客户端。提供配置管理、规则编辑、系统代理、TUN 模式和 WebDAV 同步。 | 部署与运维 | 158520 |
| [CleanYourTV](docs/cleanyourtv.md#中文) | 为 Android TV/Google TV 提供可恢复的预装软件停用流程和轻量桌面启动器。 | 部署与运维 | 58509 |
| [JumpServer](docs/jumpserver.md#中文) | 集中管理服务器、数据库和其他基础设施的特权访问与审计。 | 部署与运维 | 31970 |
| [Netdata Agent](docs/netdata.md#中文) | 采集主机、容器与应用指标，并在本地存储、检测异常和触发告警。 | 部署与运维 | 81435 |
| [Omarchy](docs/omarchy.md#中文) | 为开发与日常使用预配置桌面、终端、快捷键和工具的Linux发行版。 | 部署与运维 | 47063 |
| [OpenBao](docs/openbao.md#中文) | 集中保存和分发机密、证书与密钥，并管理访问、租约和撤销。 | 部署与运维 | 9049 |
| [OpenShell](docs/openshell.md#中文) | 为智能体提供隔离运行环境，按策略控制文件、网络和凭据访问。 | 部署与运维 | 21676 |
| [wifit3](docs/wifit3.md#中文) | 使用支持的USB无线网卡分析无线网络状态与安全配置。 | 部署与运维 | 3593 |

</details>

<a id="included-data"></a>

<details>
<summary><strong>数据处理</strong> · 6 项</summary>

| 项目 | 用途 | 分类 | Star |
| --- | --- | --- | ---: |
| [AI Berkshire](docs/ai-berkshire.md#中文) | 基于 Claude Code 与 Codex 的价值投资研究技能。通过多个分析视角组织公司研究、财报、估值、组合复盘和论点跟踪。 | 数据处理 | 17140 |
| [Claude for Financial Services](docs/financial-services.md#中文) | 为金融研究与运营提供智能体模板、技能、数据连接器和部署脚本。 | 数据处理 | 41340 |
| [OpenSEO](docs/open-seo.md#中文) | 自托管关键词、排名、外链和网站审计工作台，并向智能体提供MCP接口。 | 数据处理 | 27897 |
| [The Well](docs/the-well.md#中文) | 提供物理时空模拟数据的统一读取、下载和模型基准工具。 | 数据处理 | 4577 |
| [Vibe Research](docs/vibe-research.md#中文) | 面向 A 股、美股和港股的投研工作台。整合自选、持仓、每日复盘、产业与公司研究、历史回测和研报库。 | 数据处理 | 3720 |
| [Workout Guide](docs/workout-guide.md#中文) | 包含 302 个动作的可视化资料与 npm 数据包，提供分帧插画、类型化查询、搜索和静态画廊，适合构建运动内容界面。 | 数据处理 | 1440 |

</details>

<a id="included-terminal"></a>

<details>
<summary><strong>终端与 Shell</strong> · 3 项</summary>

| 项目 | 用途 | 分类 | Star |
| --- | --- | --- | ---: |
| [Ghostty](docs/ghostty.md#中文) | 使用原生界面和 GPU 渲染的终端模拟器。支持多窗口、标签页与分屏，另提供可嵌入终端库。 | 终端与 Shell | 64125 |
| [ipatool](docs/ipatool.md#中文) | 通过命令行搜索 App Store 应用、查看已购项目和版本，并下载账号有权取得的 IPA 或 macOS PKG 文件；提供 MCP 接口。 | 终端与 Shell | 12352 |
| [terminal-mac](docs/terminal-mac.md#中文) | 为电脑操作 Agent 启动独立 macOS 虚拟机，把画面流式显示在终端，并提供输入控制接口。 | 终端与 Shell | 2795 |

</details>

<a id="included-knowledge"></a>

<details>
<summary><strong>知识与学习</strong> · 3 项</summary>

| 项目 | 用途 | 分类 | Star |
| --- | --- | --- | ---: |
| [AI Agent 工程实践书](docs/ai-agent-book.md#中文) | 通过公开教材、配套实验和技能包学习 AI Agent 的设计与工程实现。 | 知识与学习 | 58306 |
| [Human Atlas](docs/human-atlas.md#中文) | 可在浏览器中旋转、拆分、搜索和选择人体结构的三维解剖图谱。 | 知识与学习 | 4571 |
| [Scientific Agent Skills](docs/scientific-agent-skills.md#中文) | 为科学计算、资料检索和研究流程提供可组合的智能体技能。 | 知识与学习 | 57421 |

</details>

[返回分类导航](#categories)

<a id="candidates"></a>

## 候选（27）

这里保留原有 27 个候选及其当时原因。“Star 未满 1000”等历史结论尚未按新标准复核，不再作为自动排除条件。本轮未新增项目另记于[复核记录](reviews/2026-11-16-wechat.md)。

<a id="candidate-ai"></a>

<details>
<summary><strong>AI 工具</strong> · 1 项</summary>

| 项目 | 候选原因 | 分类 | Star |
| --- | --- | --- | ---: |
| [微舆（BettaFish）](docs/bettafish.md#中文) | 许可证待复核 | AI 工具 | 42701 |

</details>

<a id="candidate-development"></a>

<details>
<summary><strong>开发辅助</strong> · 4 项</summary>

| 项目 | 候选原因 | 分类 | Star |
| --- | --- | --- | ---: |
| [Nextpad++ for macOS](docs/nextpad-plus-plus-macos.md#中文) | 许可证待复核 | 开发辅助 | 1445 |
| [OpenTest（功能待公开）](docs/opentest.md#中文) | 许可证待复核 | 开发辅助 | 3 |
| [Public APIs](docs/public-apis.md#中文) | 双语内容待复核 | 开发辅助 | 499152 |
| [Serena](docs/serena.md#中文) | 许可证待复核 | 开发辅助 | 31391 |

</details>

<a id="candidate-media"></a>

<details>
<summary><strong>图像与音视频</strong> · 8 项</summary>

| 项目 | 候选原因 | 分类 | Star |
| --- | --- | --- | ---: |
| [Awesome DESIGN.md](docs/awesome-design-md.md#中文) | 双语内容待复核 | 图像与音视频 | 127606 |
| [拾景纸刊：照片与撕纸拼贴](docs/gathered-scenes-zine-skill.md#中文) | 许可证待复核 | 图像与音视频 | 5660 |
| [Heytea Doodle Poster：实物照片与小人涂鸦](docs/heytea-style.md#中文) | Star 未满 1000 | 图像与音视频 | 350 |
| [Ian Xiaohei Illustrations](docs/ian-xiaohei-illustrations.md#中文) | 双语内容待复核 | 图像与音视频 | 13217 |
| [Lemo-Opuscar](docs/lemo-opuscar.md#中文) | 许可证待复核 | 图像与音视频 | 16446 |
| [Photo Relic Editorial：照片与纸上印迹](docs/photo-relic-editorial.md#中文) | Star 未满 1000 | 图像与音视频 | 454 |
| [照片转海报：厚涂微缩景观与水彩旅行卡](docs/photo-to-poster-skills.md#中文) | Star 未满 1000 | 图像与音视频 | 36 |
| [Photo-to-Zine：照片明信片正反面](docs/photo-to-zine-postcard.md#中文) | Star 未满 1000 | 图像与音视频 | 289 |

</details>

<a id="candidate-productivity"></a>

<details>
<summary><strong>文档与效率</strong> · 10 项</summary>

| 项目 | 候选原因 | 分类 | Star |
| --- | --- | --- | ---: |
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

</details>

<a id="candidate-automation"></a>

<details>
<summary><strong>自动化</strong> · 1 项</summary>

| 项目 | 候选原因 | 分类 | Star |
| --- | --- | --- | ---: |
| [cc-connect](docs/cc-connect.md#中文) | 许可证待复核 | 自动化 | 16376 |

</details>

<a id="candidate-operations"></a>

<details>
<summary><strong>部署与运维</strong> · 1 项</summary>

| 项目 | 候选原因 | 分类 | Star |
| --- | --- | --- | ---: |
| [TelemetryCleaner](docs/telemetrycleaner.md#中文) | Star 未满 1000 | 部署与运维 | 807 |

</details>

<a id="candidate-data"></a>

<details>
<summary><strong>数据处理</strong> · 2 项</summary>

| 项目 | 候选原因 | 分类 | Star |
| --- | --- | --- | ---: |
| [easyquotation](docs/easyquotation.md#中文) | 缺少近期有效维护证据 | 数据处理 | 5478 |
| [TradingAgents-CN](docs/tradingagents-cn.md#中文) | 应用层采用专有许可 | 数据处理 | 32957 |

</details>

[返回分类导航](#categories)

<a id="review"></a>

## 复核记录与覆盖范围

2026-11-16 本轮新增 **147 个双语词条**，其中 **10 个项目低于 1,000 Star**。原有 **62 个词条**保留 2026-11-15 的记录，未在本轮重新评估：35 个原已收录加 147 个新增，合计 182 个已收录，另有 27 个原候选。

本轮检查 **2026-08-16 至 2026-11-16** 的公开文章线索，包括 **逛逛GitHub**、**AI开源求索**的署名转载与第三方索引。两个账号都属于部分覆盖：转载或索引不能证明已经读取微信原文，部分公众号归属仍待核实。仓库是否符合条件，另依据上游许可、实现与活动证据判断。

本轮未安装或运行上游软件。[公众号文章复核记录](reviews/2026-11-16-wechat.md)列出覆盖范围、筛选结论、未新增原因和带日期的来源；每个新增词条保留对应证据等级。

<a id="contributing"></a>

## 新增或更新词条

在 `docs/<项目名>.md` 中维护一份双语介绍，写明仓库、用途、功能、环境、限制、入门方式和来源；记录 Star、许可原文、有效活动与复核日期。同步更新两份目录，保持状态与 Star 快照一致。仅阅读文档时注明“文档复核”，实际测试另行记录。

| 位置 | 内容 |
| --- | --- |
| [README.md](README.md) / [README.en.md](README.en.md) | 中英文说明与目录 |
| [docs/](docs/) | 每个项目一份双语词条 |
| [reviews/](reviews/) | 来源覆盖与复核结论 |
| [assets/readme/](assets/readme/) | 首页插图 |

## 许可证

本仓库采用 [Apache License 2.0](LICENSE)。各工具保留自己的许可证，具体范围见词条与上游条款。

[返回顶部](#ai-station) · [分类浏览](#categories) · [English](README.en.md)
