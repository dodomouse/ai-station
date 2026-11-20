<p align="center">
  <img src="assets/readme/logo.svg" alt="ai-station" width="96" />
</p>

<a id="ai-station"></a>

<h1 align="center">ai-station</h1>

<p align="center">中英文 GitHub 工具目录。按用途查找，先看环境与限制。</p>

<p align="center">
  <a href="#included"><img src="https://img.shields.io/badge/included-394-2563eb?style=flat-square" alt="394 included projects" /></a>
  <a href="#categories"><img src="https://img.shields.io/badge/categories-9-0f766e?style=flat-square" alt="9 categories" /></a>
  <img src="https://img.shields.io/badge/languages-中文%20%2F%20English-7c3aed?style=flat-square" alt="Chinese and English" />
</p>

<p align="center"><strong>简体中文</strong> · <a href="README.en.md">English</a></p>

<p align="center"><a href="#featured">精选入口</a> · <a href="#categories">分类浏览</a> · <a href="#criteria">收录标准</a> · <a href="reviews/2026-11-16-wechat.md">复核记录</a></p>

<p align="center">
  <img src="assets/readme/hero.zh-CN.svg" alt="按开发、AI、媒体、文档和运维等用途组织的工具目录" width="960" />
</p>

现有 **394 个已收录项目**，覆盖九类用途。每个项目用一份双语词条说明用途、功能、环境、限制、入门方式和复核证据。

**2026-11-17 新增收录：** [100 个可帮助 AI 完成任务的仓库](reviews/2026-11-17-ai-repository-shortlist.md)已全部整理为正式双语词条。它们按主要用途并入下方目录。筛选记录保留 Star 快照和近三个月活动，可按 12 类任务浏览。

**媒体工具补充：** 新增 7 个[图像与音视频词条](#included-media)，覆盖视频制作、图片生成与分割、智能照片和视频库。

**素材检索补充：** [SCM](docs/scm.md#中文) 用于 Mac 本地素材搜索；[FiftyOne](docs/fiftyone.md#中文) 用于视觉数据集检索、筛选和评估。

可以按任务寻找工具、比较使用条件，也可以挑选适合学习的源码项目。在浏览器中阅读目录，选定项目后再按其官方说明配置环境。

<a id="start"></a>

## 如何查找

1. **从任务出发。** 先看[精选入口](#featured)，或进入[九类目录](#categories)。
2. **缩小范围。** 展开分类后，用 Ctrl/⌘+F 搜索名称或用途；也可用 GitHub 仓库内搜索查找 `docs/` 中的词条。
3. **判断是否适合。** 打开词条，查看环境、使用限制与复核日期，再前往上游官方文档。

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

后续新增与复核采用以下三条标准：

1. **能帮助 AI 完成任务。** 项目与 AI 相关，并有可说明的任务用途，例如模型运行、智能体工具、编码、检索或内容处理。
2. **近 3 个日历月有活动。** 提供可追溯的 commit、PR、issue 或 release 链接及日期。文档更新和机器人提交均可计入，不要求功能修改或缺陷修复；仅有 `pushed_at` 不足以定位具体活动。
3. **达到 Star 门槛。** 当前 Star 总数 **≥ 1,000**，或近 **1 个日历月净增 ≥ 500**，满足其一即可。记录快照日期；使用净增条件时，提供对应窗口的可核对数据。

时间窗口以复核日为终点，分别向前推 3 个或 1 个日历月。许可不作为准入条件，也不要求许可审查或文件哈希。

本标准自 **2026-11-17** 起用于后续新增与复核。按用户指令，规则调整时原有的 **275 个项目全部保留为正式收录**，其中包含本次转正的 29 个原候选。这不表示已逐项按新标准重新核验。原有词条事实、快照日期和历史评估保留。收录不等于完成性能、兼容性或安全实测。

本次保留资格绑定原评估记录。项目再次复核时，须按当前标准记录新证据。

**指定例外：** 用户于 2026-11-17 明确指定 [SCM](docs/scm.md#review-evidence) 正式收录。该次快照为 529 Star，近一个日历月净增尚未核实。本次仅豁免 SCM 的 Star 条件，AI 用途及近三个月活动已核对。例外绑定本次评估，独立记入 `catalog-policy.json` 的 `explicit_admissions`；不扩展到其他项目或未来复核。

<a id="categories"></a>

## 分类导航

选择分类后展开列表。394 个项目按主要用途各列一次。

| 分类 | 可以找到 | 数量 |
| --- | --- | ---: |
| [AI 工具](#included-ai) | 模型、智能体、记忆与知识库 | [98](#included-ai) |
| [开发辅助](#included-development) | 编码、审查、界面与工程工具 | [101](#included-development) |
| [图像与音视频](#included-media) | 图像、动画、音频与视频制作 | [68](#included-media) |
| [文档与效率](#included-productivity) | 写作、笔记、办公与日常工具 | [59](#included-productivity) |
| [自动化](#included-automation) | 任务调度、设备与应用控制 | [20](#included-automation) |
| [部署与运维](#included-operations) | 部署、监控、系统与服务管理 | [19](#included-operations) |
| [数据处理](#included-data) | 数据查询、研究与分析流程 | [22](#included-data) |
| [终端与 Shell](#included-terminal) | 终端环境与命令行工具 | [3](#included-terminal) |
| [知识与学习](#included-knowledge) | 教材、图谱与交互学习材料 | [4](#included-knowledge) |

<a id="included"></a>

## 已收录（394）

点击名称查看双语介绍与带日期的证据。下表 Star 为复核时快照，不作实时排名。

<a id="included-ai"></a>

<details>
<summary><strong>AI 工具</strong> · 98 项</summary>

| 项目 | 用途 | 分类 | Star |
| --- | --- | --- | ---: |
| [Agency Agents](docs/agency-agents.md#中文) | 提供按专业角色组织的 AI 智能体指令、工作步骤和交付模板。 | AI 工具 | 168864 |
| [Agent Beacon](docs/agent-beacon.md#中文) | 收集多个编程智能体的会话轨迹，将经过审阅的工作经验提供给后续智能体复用。 | AI 工具 | 3543 |
| [Agent Reach](docs/agent-reach.md#中文) | 为 Agent 提供网页与社交平台的搜索、阅读和内容获取能力，整合视频、论坛及多个中文平台渠道。 | AI 工具 | 112225 |
| [Agenta](docs/agenta.md#中文) | 通过对话配置团队智能体，连接应用，并按计划或事件执行任务。 | AI 工具 | 4915 |
| [Agno](docs/agno.md#中文) | 将智能体、团队和工作流部署为带 API、MCP、存储及调度能力的服务。 | AI 工具 | 43216 |
| [ai-memory](docs/ai-memory.md#中文) | 为 AI 编码工具提供跨会话记忆和跨工具交接。使用 Git 管理的 Markdown 保存知识，并提供检索和摘要注入。 | AI 工具 | 15919 |
| [AirLLM](docs/airllm.md#中文) | 通过逐层加载和卸载模型权重降低大语言模型的显存需求，并提供部分模型的流式 LoRA 训练接口。 | AI 工具 | 42524 |
| [AstrBot](docs/astrbot.md#中文) | 将大模型对话和智能体接入多种即时通讯平台，提供插件、知识库及网页管理界面。 | AI 工具 | 47065 |
| [Axolotl](docs/axolotl.md#中文) | 用配置文件组织语言模型微调和后训练的工具。 | AI 工具 | 12735 |
| [bitsandbytes](docs/bitsandbytes.md#中文) | 为 PyTorch 提供低位宽量化与优化器的库。 | AI 工具 | 8543 |
| [Cherry Studio](docs/cherry-studio.md#中文) | 整合模型对话、智能体、知识库和文件工具的桌面 AI 工作台。 | AI 工具 | 53595 |
| [Claude Skills by Alireza Rezvani](docs/alirezarezvani-claude-skills.md#中文) | 为 AI 智能体提供跨工程、产品、营销、财务和合规领域的技能、角色指令及辅助脚本。 | AI 工具 | 29928 |
| [Claude-Mem](docs/claude-mem.md#中文) | 记录编码智能体的工作观察，在后续会话中检索和恢复相关记忆。 | AI 工具 | 117552 |
| [Codex ChatGPT Web Bridge](docs/codex-chatgpt-web.md#中文) | 通过本机登录的ChatGPT网页会话，为Codex提供第三方模型桥接。 | AI 工具 | 15746 |
| [colibri](docs/colibri.md#中文) | 以 C 推理引擎按需从内存和磁盘加载权重，并可结合 GPU 运行本地模型。 | AI 工具 | 51605 |
| [CrewAI](docs/crewai.md#中文) | 以角色化 Agent 协作和事件驱动流程组织多步骤工作。 | AI 工具 | 61025 |
| [DeepInfer](docs/deepinfer.md#中文) | 面向 DeepSeek 模型的推理实现，提供高性能计算与分布式执行组件。 | AI 工具 | 26102 |
| [DeepSeek chat-demo](docs/deepseek-chat-demo.md#中文) | 通过 DeepSeek API 提供聊天界面的静态网页示例。支持流式回答、会话分支、附件和历史导入导出。 | AI 工具 | 3890 |
| [DeepSpeed](docs/deepspeed.md#中文) | 用于模型训练与推理的分布式优化库。 | AI 工具 | 43332 |
| [DeepTutor](docs/deeptutor.md#中文) | 将学习资料、辅导对话、练习和学习记录组织到同一 AI 学习工作区。 | AI 工具 | 59827 |
| [DeerFlow](docs/deer-flow.md#中文) | 组合子智能体、记忆、技能和沙箱执行较长的任务。 | AI 工具 | 85439 |
| [Dify](docs/dify.md#中文) | 通过可视化工作区构建 AI 流程、RAG 管线和 Agent 应用。 | AI 工具 | 161353 |
| [DSH Desktop](docs/dsh-desktop.md#中文) | DeepSeek Harness 桌面工作台，组织模型、Office 模板、技能和插件，可生成或处理文档、表格与演示文稿。 | AI 工具 | 19341 |
| [dsh-superagent 研究原型](docs/dsh-superagent-prototype.md#中文) | 面向单个 GitHub 仓库的主动编码智能体研究原型。监听 GitHub 和可选飞书消息，按授权创建并执行工作项。 | AI 工具 | 23202 |
| [DSPy](docs/dspy.md#中文) | 用模块化程序组织语言模型调用，并优化提示词与模型参数。 | AI 工具 | 39107 |
| [fast-agent](docs/fast-agent.md#中文) | 提供终端智能体、技能、MCP 连接、Shell 工具和多模型工作流。 | AI 工具 | 3972 |
| [FreeLLM API](docs/freellmapi.md#中文) | 把用户自己的多个模型提供商账号接到本地网关，提供兼容 OpenAI 的接口、路由、失败切换和额度跟踪。 | AI 工具 | 53227 |
| [FreeToken](docs/freetoken.md#中文) | 在本地运行混合专家模型的推理引擎。组合 GPU、CPU 和系统内存，提供专家缓存和模型服务接口。 | AI 工具 | 17244 |
| [Gemini CLI](docs/gemini-cli.md#中文) | 面向企业 Gemini Code Assist 工作流的终端 AI 智能体，可读取代码、编辑文件和运行工具。 | AI 工具 | 108884 |
| [Geo Sleuth](docs/geo-sleuth.md#中文) | 为 Agent 提供照片地理定位流程，综合地形、天际线、道路和地图检索，输出候选位置、观察方向与证据。 | AI 工具 | 7109 |
| [Graphiti](docs/graphiti.md#中文) | 构建保留时间与来源信息的上下文图谱，支持语义、关键词和图遍历检索。 | AI 工具 | 32877 |
| [Haystack](docs/haystack.md#中文) | 用组件、流水线和智能体组织语言模型应用的 Python 框架。 | AI 工具 | 27027 |
| [Heretic](docs/heretic.md#中文) | 通过免训练的参数修改研究语言模型的回答风格、拒答与迎合行为。 | AI 工具 | 40743 |
| [Hindsight](docs/hindsight.md#中文) | 为智能体保存事实与经历，并按问题检索或综合相关记忆。 | AI 工具 | 61351 |
| [Jev Chat Jarvis](docs/jev-chat-jarvis.md#中文) | Android 聊天辅助浮层，使用无障碍与 OCR 获取当前聊天上下文，生成分析和回复草稿，由用户选择插入。 | AI 工具 | 8409 |
| [LangChain](docs/langchain.md#中文) | 用模型、工具及外部集成组件构建 Agent 和 LLM 应用。 | AI 工具 | 149768 |
| [Langflow](docs/langflow.md#中文) | 以可视化组件构建 Agent 和工作流，并提供 API 与 MCP 服务入口。 | AI 工具 | 156718 |
| [LangGraph](docs/langgraph.md#中文) | 构建具有状态、持久执行和人工介入能力的 Agent 工作流。 | AI 工具 | 45067 |
| [Laya](docs/laya.md#中文) | 面向文本分类、选项判断、评分和路由的非自回归决策引擎，输出结构化结果与置信信息。 | AI 工具 | 35592 |
| [Laya-MLX](docs/laya-mlx.md#中文) | 在Apple Silicon上用MLX运行结构化选择、评分和真假判断模型。 | AI 工具 | 7107 |
| [LibreChat](docs/librechat.md#中文) | 可自行部署的多模型聊天与智能体工作台，支持文件和工具调用。 | AI 工具 | 47227 |
| [LightRAG](docs/lightrag.md#中文) | 结合知识图谱与向量检索的 RAG 框架。 | AI 工具 | 40741 |
| [llama.cpp](docs/llama-cpp.md#中文) | 基于 ggml 的 C/C++ 模型推理引擎，提供本地命令行、服务接口及多模态模型支持。 | AI 工具 | 135378 |
| [LlamaFactory](docs/llamafactory.md#中文) | 通过命令行与 Web 界面配置语言模型微调的工具。 | AI 工具 | 76084 |
| [LlamaIndex Framework](docs/llama-index.md#中文) | 连接数据、索引与语言模型的 RAG 和智能体开发框架。 | AI 工具 | 52926 |
| [llmfit](docs/llmfit.md#中文) | 检测 CPU、内存和 GPU 显存，估算本地模型及量化版本的适配程度，并提供 TUI、网页、CLI/API 与基准测试入口。 | AI 工具 | 39014 |
| [LMDeploy](docs/lmdeploy.md#中文) | 用于语言模型和视觉语言模型压缩、推理及服务部署的工具集。 | AI 工具 | 8149 |
| [LobeHub](docs/lobehub.md#中文) | 支持模型对话、智能体协作和工具集成的 AI 工作台，可自行部署。 | AI 工具 | 85696 |
| [Magpie](docs/magpie.md#中文) | 通过本地网关统一管理编码智能体的模型与服务商。提供多账号路由、故障转移及可选请求脱敏。 | AI 工具 | 36740 |
| [Mem0](docs/mem0.md#中文) | 为智能体和应用提取、保存并检索用户、会话和任务记忆。 | AI 工具 | 69107 |
| [micrograd](docs/micrograd.md#中文) | 用于学习反向自动微分的微型标量引擎，并附带简单神经网络模块。 | AI 工具 | 18968 |
| [MiniMind](docs/minimind.md#中文) | 用较小语言模型学习从预训练、微调到推理服务的完整实现。 | AI 工具 | 65498 |
| [MiroFish](docs/mirofish.md#中文) | 根据输入资料构建多智能体模拟环境，探索群体互动和不同情景。 | AI 工具 | 85784 |
| [MLX LM](docs/mlx-lm.md#中文) | 基于 MLX 在 Apple 芯片上生成文本和微调语言模型的 Python 包。 | AI 工具 | 7671 |
| [Not Sandboxed（Cybersecurity Projects 子项目）](docs/cybersecurity-projects.md#中文) | Cybersecurity Projects 中的 LLM 提示注入防护子项目，提供来源标记、工具权限策略和输出检查的 Python 库、CLI 及实验代理。 | AI 工具 | 9554 |
| [Octop](docs/octop.md#中文) | 可自托管的多用户、多 Agent 助手，提供专家库、网页/CLI/消息渠道、定时任务、知识库及 MCP/ACP 接口。 | AI 工具 | 12113 |
| [Ollama](docs/ollama.md#中文) | 下载、管理和运行语言模型，通过命令行及本地 API 为应用和智能体提供模型访问。 | AI 工具 | 187285 |
| [oMLX](docs/omlx.md#中文) | 为 Apple 芯片 Mac 提供本地模型推理服务和菜单栏管理界面。 | AI 工具 | 23663 |
| [Open Interpreter](docs/open-interpreter.md#中文) | 当前主线是基于 Rust 的终端编码 Agent，连接模型提供商，提供工具调用、MCP/ACP、技能和原生沙箱。 | AI 工具 | 68895 |
| [Open WebUI](docs/open-webui.md#中文) | 可自行部署的 AI 网页界面，连接本地模型和兼容 API 的模型服务。 | AI 工具 | 158918 |
| [OpenAI Agents SDK](docs/openai-agents-python.md#中文) | 提供多智能体工作流、工具调用、交接、追踪和语音交互组件。 | AI 工具 | 30735 |
| [OpenBot application template](docs/copilotkit-openbot.md#中文) | 用于构建 AI 助手工作区的开源应用模板。连接模型、AG-UI 智能体和 MCP 工具。运行依赖单独许可的 CopilotKit Intelligence。 | AI 工具 | 12624 |
| [OpenCode](docs/opencode.md#中文) | 在终端或桌面界面中调用模型，完成代码探索、规划和修改。 | AI 工具 | 227359 |
| [OpenDots](docs/opendots.md#中文) | 持久化 AI 同事的社区模板，通过网页、手机和消息渠道与 Agent 交互，并提供各自的电脑工作区。 | AI 工具 | 6624 |
| [OpenFuse（原OpenMuse）](docs/openfuse.md#中文) | 提供带浏览器、终端和文件工作区的个人智能体应用模板。 | AI 工具 | 6496 |
| [OpenHands](docs/openhands.md#中文) | 用于软件开发任务的智能体工作台，提供会话、工具执行与变更审查。 | AI 工具 | 93582 |
| [OpenMAIC](docs/openmaic.md#中文) | 把主题或文档转成包含 AI 教师与同学的交互式课堂。 | AI 工具 | 43722 |
| [OpenMausBot](docs/openmausbot.md#中文) | 以联系人和群聊组织多个编码智能体。可为各机器人配置模型、工作目录、连接应用和执行环境。 | AI 工具 | 23982 |
| [OpenRLHF](docs/openrlhf.md#中文) | 基于 Ray、vLLM 和 DeepSpeed 的语言模型强化学习训练框架。 | AI 工具 | 10162 |
| [OpenViking](docs/openviking.md#中文) | 用可浏览的虚拟文件系统组织智能体知识、记忆和技能。 | AI 工具 | 42305 |
| [Paperclip](docs/paperclip.md#中文) | 管理 AI 团队的组织、目标、任务、权限和预算，连接已有 Agent，并跟踪执行与模型成本。 | AI 工具 | 114265 |
| [PEFT](docs/peft.md#中文) | 通过训练部分参数适配预训练模型的库。 | AI 工具 | 21899 |
| [PilotDeck](docs/pilotdeck.md#中文) | 围绕独立工作区组织智能体任务、记忆、技能和长期运行。 | AI 工具 | 4998 |
| [Prime Agent](docs/prime-agent.md#中文) | 以持久Python环境、子智能体和后台会话执行编码与研究任务。 | AI 工具 | 22746 |
| [Pydantic AI](docs/pydantic-ai.md#中文) | 提供有类型的智能体循环、工具调用、持久执行、评测和多模型接口。 | AI 工具 | 21255 |
| [Qwen Code](docs/qwen-code.md#中文) | 跨终端、编辑器和桌面的 AI 编程智能体，可理解仓库、修改代码并调用开发工具。 | AI 工具 | 30668 |
| [RAGFlow](docs/ragflow.md#中文) | 结合文档解析、知识组织和智能体检索的 RAG 引擎。 | AI 工具 | 94306 |
| [Rakazo](docs/rakazo.md#中文) | 可自行部署的 AI 团队工作台，集中管理长期记忆、例行任务与智能体电脑。 | AI 工具 | 8776 |
| [Ruflo](docs/ruflo.md#中文) | 为编码智能体提供任务编排、共享记忆和 MCP 工具集成。 | AI 工具 | 81892 |
| [SGLang](docs/sglang.md#中文) | 面向语言、多模态和扩散模型的推理框架。 | AI 工具 | 38977 |
| [Skid Homework](docs/skid-homework.md#中文) | 在浏览器中调用多模态模型分析题目图片、PDF 和文本，辅助理解解题过程。 | AI 工具 | 1947 |
| [smolagents](docs/smolagents.md#中文) | 让智能体用代码表达操作，支持多种模型、MCP 工具和沙箱执行环境。 | AI 工具 | 30404 |
| [StarNet](docs/starnet.md#中文) | 以像素空间站界面管理多个在本机工作的智能体。 | AI 工具 | 1854 |
| [Suparagent](docs/suparagent.md#中文) | 为多个具名智能体提供会话、工作区、记忆、例行任务与审批界面。 | AI 工具 | 7087 |
| [Supermemory](docs/supermemory.md#中文) | 提供记忆与上下文接口、助手插件和 MCP 接入，用于提取事实和检索历史。 | AI 工具 | 31641 |
| [SuperMimic](docs/supermimic.md#中文) | 面向人形机器人的动作跟踪研究实现。使用可微世界模型训练全身动作控制策略。 | AI 工具 | 1646 |
| [TensorRT-LLM](docs/tensorrt-llm.md#中文) | 面向 NVIDIA GPU 的语言模型与视觉生成推理优化库。 | AI 工具 | 15084 |
| [TimesFM（开源代码与 ≤2.5 权重）](docs/timesfm.md#中文) | Google Research 的时间序列预测代码库，提供预训练模型调用、分位数预测和协变量支持；本词条收录 Apache-2.0 源代码及 2.5 或更早的开源权重。 | AI 工具 | 35602 |
| [Transformers](docs/transformers.md#中文) | 用于加载、训练和推理文本、视觉、音频及多模态模型的 Python 模型框架。 | AI 工具 | 169089 |
| [TRL](docs/trl.md#中文) | 提供监督微调、偏好优化和强化学习训练器的后训练库。 | AI 工具 | 19750 |
| [Unsloth](docs/unsloth.md#中文) | 模型运行与微调工具，覆盖语言、扩散、语音和嵌入模型，并提供本地桌面/Studio 工作流。 | AI 工具 | 79601 |
| [uzu](docs/uzu.md#中文) | 将模型下载、聊天会话和本地推理嵌入应用的 Rust 引擎，提供多语言绑定。 | AI 工具 | 3358 |
| [verl](docs/verl.md#中文) | 将模型训练、采样和奖励计算组合成强化学习流程的库。 | AI 工具 | 24264 |
| [vLLM](docs/vllm.md#中文) | 面向语言和多模态模型的推理与服务框架，提供请求批处理、分布式推理及兼容常见客户端的 API。 | AI 工具 | 97064 |
| [WeKnora](docs/weknora.md#中文) | 企业文档知识库与 RAG 问答服务，整合文档解析、检索、Agent 和 Wiki 工作流。 | AI 工具 | 37540 |
| [XERJ](docs/xerj.md#中文) | 面向 AI 智能体的开源搜索引擎，索引代码、文档和日志，提供全文、向量与混合检索。 | AI 工具 | 19162 |
| [微舆（BettaFish）](docs/bettafish.md#中文) | 多智能体舆情分析系统，组合网页搜索、社媒分析和数据库查询。通过协作汇总资料，输出 HTML 等格式的分析报告。 | AI 工具 | 42701 |
| [Last30Days Skill](docs/last30days-skill.md#中文) | AI 智能体主导的搜索引擎，跨多平台检索并按真实互动评分综合成简报，帮助 AI 完成调研任务。 | AI 工具 | 69671 |

</details>

<a id="included-development"></a>

<details>
<summary><strong>开发辅助</strong> · 101 项</summary>

| 项目 | 用途 | 分类 | Star |
| --- | --- | --- | ---: |
| [2010 Rust Rewrite Mashup](docs/2010-rust-rewrite-mashup.md#中文) | 以 Rust 实现的游戏混搭实验，把 MW2 风格场景、滑板和体素地图组合起来，可用于学习游戏重实现与资源兼容。 | 开发辅助 | 951 |
| [agent-browser](docs/agent-browser.md#中文) | 为 AI 智能体提供网页快照、元素操作和浏览器会话管理命令。 | 开发辅助 | 52076 |
| [AI Infra Book](docs/ai-infra-book.md#中文) | AI 基础设施教材与计算工具，覆盖硬件、模型架构、推理和训练，并提供在线版、PDF/EPUB 及容量估算脚本。 | 开发辅助 | 7897 |
| [AI Website Cloner Template：网站复刻与迁移模板](docs/ai-website-cloner-template.md#中文) | 用编码助手观察目标网页，再以 Next.js 重建页面、素材和交互。通过浏览器对照差异并修正。 | 开发辅助 | 39159 |
| [AnyPS5](docs/anyps5.md#中文) | 研究把控制台可执行文件重链接到桌面平台的兼容性工具。 | 开发辅助 | 54377 |
| [Archify](docs/archify.md#中文) | 把想法、计划或代码仓资料生成交互式 HTML 图示。可制作架构图、流程图和带来源的解释页面。 | 开发辅助 | 96538 |
| [assistant-ui](docs/assistant-ui.md#中文) | 为 React 应用构建 AI 对话界面的 TypeScript 组件库。 | 开发辅助 | 13288 |
| [Chainlit](docs/chainlit.md#中文) | 用 Python 编写对话式 AI 应用，并在浏览器中展示消息与工具执行步骤。 | 开发辅助 | 12503 |
| [Claude Code Game Studios](docs/claude-code-game-studios.md#中文) | 为 Claude Code 提供游戏开发模板和技能。可从玩法描述生成简要设计、浏览器原型，并逐步修改和扩展。 | 开发辅助 | 39708 |
| [Claude Code Templates](docs/claude-code-templates.md#中文) | 提供 Claude Code 组件目录和命令行安装工具，用于选择技能、子智能体、命令、Hooks、MCP 配置及插件。 | 开发辅助 | 33885 |
| [Claude Community Plugins：目录与校验器](docs/claude-plugins-community.md#中文) | 提供Claude社区插件目录，以及可复用的插件市场CI校验器。 | 开发辅助 | 4903 |
| [Claude Plugins Official](docs/claude-plugins-official.md#中文) | Anthropic 维护的 Claude 插件目录，提供开发与工作流程扩展。 | 开发辅助 | 47430 |
| [Claude Red](docs/claude-red.md#中文) | 面向授权安全研究和 CTF 的 Claude Code 技能集合。 | 开发辅助 | 11091 |
| [CLI-Anything](docs/cli-anything.md#中文) | 分析软件源码，为真实应用后端生成 CLI harness。提供结构化命令、JSON 输出、交互式 REPL 及测试流程。 | 开发辅助 | 58741 |
| [Code-Graph-RAG](docs/code-graph-rag.md#中文) | 将多语言代码仓库解析为知识图谱，供智能体检索代码结构、回答问题和辅助修改。 | 开发辅助 | 5369 |
| [code-review-graph](docs/code-review-graph.md#中文) | 用 Tree-sitter 建立并增量更新本地代码结构图。通过 MCP 和 CLI 提供依赖、变更影响及审查上下文。 | 开发辅助 | 32776 |
| [Codex CLI](docs/codex.md#中文) | 在本机工程中运行的编码智能体，支持终端与编辑器入口。 | 开发辅助 | 135635 |
| [Codex with ChatGPT](docs/codex-with-chatgpt.md#中文) | 用只读 MCP 连接将 ChatGPT 网页的规划与审查接入 Codex 工作区。 | 开发辅助 | 7718 |
| [CopilotKit](docs/copilotkit.md#中文) | 把智能体接入应用的开发框架，提供对话、动态界面和人工确认组件。 | 开发辅助 | 38763 |
| [Cordis](docs/cordis.md#中文) | 用于 TypeScript 应用的组件、服务依赖和生命周期管理框架。 | 开发辅助 | 9915 |
| [Craft Anything](docs/craft-anything.md#中文) | 研究网站、应用或游戏，再让编码智能体创建自己的版本。提供研究、构建、比较与修改流程，以及 CLI、MCP 和检查证据。 | 开发辅助 | 33239 |
| [DeepEval](docs/deepeval.md#中文) | 评测大语言模型应用、智能体轨迹和单步工具行为。 | 开发辅助 | 19527 |
| [E2B](docs/e2b.md#中文) | 通过 Python 或 JavaScript SDK 管理供智能体使用的隔离执行环境。 | 开发辅助 | 14906 |
| [ECC](docs/ecc.md#中文) | 为编码智能体组合规划、审查、记忆、上下文管理和工程检查。 | 开发辅助 | 304243 |
| [ego-browser for ego lite](docs/ego-lite.md#中文) | 为 AI 智能体连接 ego lite 浏览器的开源 Skill 与工具层，通过 JavaScript 操作页面并使用独立任务工作区。 | 开发辅助 | 23215 |
| [Expo Skills](docs/expo-skills.md#中文) | 为 AI 编程智能体提供 Expo 应用开发、升级、调试和 EAS 发布工作流。 | 开发辅助 | 4177 |
| [FastAPI-MCP](docs/fastapi-mcp.md#中文) | 将 FastAPI 路由转换为 MCP 工具，并复用应用的模型和依赖认证。 | 开发辅助 | 12029 |
| [FastMCP (Python)](docs/fastmcp.md#中文) | 用 Python 构建 MCP 服务端、客户端和交互应用。 | 开发辅助 | 28617 |
| [Flutter](docs/flutter.md#中文) | 使用 Dart 为移动端、网页和桌面端构建应用的 UI 工具包。 | 开发辅助 | 181237 |
| [Garden Skills](docs/garden-skills.md#中文) | 为 AI 编程智能体提供可复用的技能、脚本和模板。覆盖网页设计、演示内容、图像创作与本地知识检索。 | 开发辅助 | 15316 |
| [Ghidra](docs/ghidra.md#中文) | 用于分析编译后程序的逆向工程框架，提供反汇编、反编译与脚本扩展。 | 开发辅助 | 100277 |
| [GitHub MCP Server](docs/github-mcp-server.md#中文) | GitHub 官方 MCP 服务，把仓库、代码和协作流程提供给智能体。 | 开发辅助 | 34544 |
| [Godogen](docs/godogen.md#中文) | 通过编码 Agent 生成独立游戏工程与素材，支持 Godot、Bevy、Babylon.js 和 Three.js 等目标，并提供运行验证流程。 | 开发辅助 | 7354 |
| [GPUI Kit](docs/gpui-kit.md#中文) | 基于 Rust GPUI 的桌面界面组件库，提供表格、编辑器、布局、可访问性支持与可选 JavaScript 宿主。 | 开发辅助 | 20833 |
| [Gradio](docs/gradio.md#中文) | 用 Python 为模型、API 或函数构建可交互的网页界面。 | 开发辅助 | 44073 |
| [Graphify](docs/graphify.md#中文) | 把源码、文档及多媒体资料组织成可查询知识图谱。提供关系解释、路径查询、子图检索和交互图页面。 | 开发辅助 | 148039 |
| [Guidance](docs/guidance.md#中文) | 在 Python 中组合生成、条件和循环，并使用正则或语法约束输出。 | 开发辅助 | 21825 |
| [Hallmark](docs/hallmark.md#中文) | 帮助编码智能体选择视觉风格、制作界面并检查页面设计。 | 开发辅助 | 55872 |
| [Henge](docs/henge.md#中文) | 在 iPhone 和 iPad 上以 JIT 模拟器运行 macOS，用于系统兼容性实验。 | 开发辅助 | 2357 |
| [Impeccable](docs/impeccable.md#中文) | 为编码智能体提供前端设计、审查和调整命令。 | 开发辅助 | 111148 |
| [Instructor](docs/instructor.md#中文) | 基于 Pydantic 将模型响应解析为有类型的数据，并处理校验失败和重试。 | 开发辅助 | 14118 |
| [islandcn](docs/islandcn.md#中文) | 为 React 网页提供灵动岛样式的活动提示组件。包含活动状态、展开收起、动画和多个用途预设。 | 开发辅助 | 760 |
| [JADX](docs/jadx.md#中文) | 把 Android DEX、APK 和 Java 字节码转换为便于阅读的 Java 源码。 | 开发辅助 | 51846 |
| [LASRecomp](docs/lasrecomp.md#中文) | 将《塞尔达传说：织梦岛》Switch 版本重编译为桌面或移动端原生程序，提供图形、输入和平台兼容代码。 | 开发辅助 | 2451 |
| [Letta Code](docs/letta-code.md#中文) | 带持久记忆、技能和跨会话状态的终端智能体工具。 | 开发辅助 | 3862 |
| [Lightpanda Browser](docs/lightpanda.md#中文) | 面向自动化和智能体的无头浏览器。执行网页脚本、操作页面并提取 HTML、Markdown 或结构化内容。 | 开发辅助 | 42129 |
| [LiveKit Agents](docs/agents.md#中文) | LiveKit 的 Python 智能体框架，用于实时语音和多模态会话。 | 开发辅助 | 15259 |
| [LM Evaluation Harness](docs/lm-evaluation-harness.md#中文) | 通过可配置任务、指标和模型后端运行语言模型基准评测。 | 开发辅助 | 14492 |
| [MacNativeGames](docs/macnativegames.md#中文) | 研究将指定游戏的图形与系统调用适配到 Apple 芯片和 Metal。 | 开发辅助 | 7913 |
| [MCP Reference Servers](docs/servers.md#中文) | MCP 官方参考服务集合，展示工具、资源和数据接入方式。 | 开发辅助 | 92065 |
| [mcpo](docs/mcpo.md#中文) | 将 MCP 服务代理为 OpenAPI HTTP 接口，供 AI 应用调用。 | 开发辅助 | 4429 |
| [MiniMax Skills](docs/minimax-skills.md#中文) | 为编程智能体提供前端、全栈和移动开发技能，并附带文档处理及 MiniMax 多模态素材生成流程。 | 开发辅助 | 13846 |
| [MLX](docs/mlx.md#中文) | 提供数组计算、自动微分和神经网络组件的机器学习框架。 | 开发辅助 | 29192 |
| [Moli：面向 AI 智能体的无头浏览器](docs/moli.md#中文) | Rust 编写的独立无头浏览器，支持 JavaScript 网页运行、Markdown 与语义树提取、按需布局，以及 CLI、CDP 和 WebDriver 自动化。 | 开发辅助 | 23783 |
| [Nextpad++ for macOS](docs/nextpad-plus-plus-macos.md#中文) | 基于 Notepad++ 代码库的原生 macOS 编辑器。提供多标签、分屏、语法高亮、正则搜索、宏和逐步移植的插件。 | 开发辅助 | 1445 |
| [nxnative](docs/nxnative.md#中文) | 将用户自有 Switch 游戏程序转换为原生 Apple 平台应用，提供 Horizon 系统调用和图形接口的兼容层，适合研究静态重编译。 | 开发辅助 | 15844 |
| [Obscura](docs/obscura.md#中文) | 面向 AI 智能体和网页采集的 Rust 无头浏览器，通过 V8 执行 JavaScript，并提供 CDP 与 MCP 接口。 | 开发辅助 | 36016 |
| [Open Code Review](docs/open-code-review.md#中文) | 读取 Git 差异或整份文件，让可配置模型生成带行号的代码审查意见。 | 开发辅助 | 52711 |
| [OpenCompass](docs/opencompass.md#中文) | 通过统一流程配置模型推理、基准评测和结果汇总。 | 开发辅助 | 7599 |
| [OpenSmash-Ultimate](docs/opensmash-ultimate.md#中文) | 通过静态重编译研究让用户自备的特定 Switch 游戏在桌面平台运行。 | 开发辅助 | 188 |
| [OpenTest（功能待公开）](docs/opentest.md#中文) | 公开 README 仅有 OpenTest 标志和 Coming soon。尚无功能说明，暂无法判断项目用途。 | 开发辅助 | 3 |
| [Orca（智能体开发工作台）](docs/orca.md#中文) | 统一管理多个编程智能体的开发工作台。提供并行工作目录、终端、差异审查、手机端及 SSH 远程环境。 | 开发辅助 | 125338 |
| [Outlines](docs/outlines.md#中文) | 用 Python 类型、Pydantic 模型和约束生成定义语言模型输出结构。 | 开发辅助 | 16013 |
| [Pipecat](docs/pipecat.md#中文) | 用 Python 编排实时语音与多模态智能体的处理流水线。 | 开发辅助 | 17304 |
| [Plannotator](docs/plannotator.md#中文) | 为 AI 智能体提供本地浏览器审阅界面。支持批注计划、文档、网页产物和代码差异，并把反馈送回会话。 | 开发辅助 | 12679 |
| [Ponytail](docs/ponytail.md#中文) | 帮助编码智能体复用已有实现、审查变更，并记录任务成本与测试状态。 | 开发辅助 | 191880 |
| [PR-Agent](docs/pr-agent.md#中文) | 用大模型分析拉取请求，生成变更说明、代码审查意见和针对差异的问答。 | 开发辅助 | 16305 |
| [Promptfoo](docs/promptfoo.md#中文) | 用配置和命令行比较提示与模型，执行评测、红队测试和 CI 检查。 | 开发辅助 | 27370 |
| [Public APIs](docs/public-apis.md#中文) | 按领域收集公开 API，列出认证、HTTPS 和 CORS 信息。当前也包含供智能体使用的 MCP 服务目录。 | 开发辅助 | 499152 |
| [PyTorch](docs/pytorch.md#中文) | 提供张量计算、自动微分和神经网络组件的深度学习框架。 | 开发辅助 | 105706 |
| [Ragas](docs/ragas.md#中文) | 用模型评分和传统指标评测大语言模型应用，并生成测试数据。 | 开发辅助 | 16354 |
| [REA — Reverse Engineer Anything](docs/rea.md#中文) | 通过 MCP 和 CLI 连接逆向分析工具。可分析原生二进制、JavaScript、Electron、.NET 及网站。 | 开发辅助 | 460761 |
| [S2Arm](docs/s2arm.md#中文) | 将用户自备的部分 Switch 游戏代码转换为苹果设备的 ARM64 程序，并提供图形化打包与游戏库管理。 | 开发辅助 | 3346 |
| [Screenshot to Code](docs/screenshot-to-code.md#中文) | 根据截图、设计图或录屏生成网页界面代码，并迭代调整。 | 开发辅助 | 81243 |
| [Security Audit Skill](docs/security-audit-skill.md#中文) | 组织源码安全审计，并用脚本检查覆盖记录和结构化发现。 | 开发辅助 | 73608 |
| [Semantica](docs/semantica.md#中文) | 把多来源资料组织为知识图谱与上下文图，并记录数据来源和推理过程。 | 开发辅助 | 14627 |
| [Serena](docs/serena.md#中文) | 为编程智能体提供符号级检索、编辑、重构和调试工具。通过 MCP 接入助手，使用语言服务器或 JetBrains 后端。 | 开发辅助 | 31391 |
| [Skills For Real Engineers（Matt Pocock）](docs/skills.md#中文) | 面向编程智能体的工程技能集合。覆盖需求澄清、架构决策、测试驱动开发、重构和任务组织。 | 开发辅助 | 324716 |
| [SkillSpector](docs/skillspector.md#中文) | 扫描智能体技能中的可疑指令、代码行为和安全问题。 | 开发辅助 | 26363 |
| [Spec Kit](docs/spec-kit.md#中文) | 提供规格驱动开发的 CLI、技能和模板。把需求规格转换为计划、任务和代码，并支持检查与缺陷修复流程。 | 开发辅助 | 149841 |
| [Stack Diagram](docs/stack-diagram.md#中文) | 把技术栈描述转换为带服务图标和连线的架构图，支持 SVG、HTML、PNG 和明暗主题，适合项目说明与设计文档。 | 开发辅助 | 2537 |
| [Stitch Design Skills](docs/stitch-skills.md#中文) | 通过 Google Stitch 的 MCP 接口，为智能体提供界面设计、设计系统提取和前端实现技能。 | 开发辅助 | 9786 |
| [Superpowers](docs/superpowers.md#中文) | 为编码智能体提供需求澄清、任务规划、测试和代码审查技能。 | 开发辅助 | 318748 |
| [T3 Code](docs/t3code.md#中文) | 统一管理多个编码 Agent 的会话、变更差异和远程连接，可从桌面、网页或手机继续开发任务。 | 开发辅助 | 62317 |
| [Taste Skill](docs/taste-skill.md#中文) | 为编码智能体提供网页设计流程、素材工具和浏览器检查脚本。 | 开发辅助 | 116605 |
| [Text to CAD](docs/text-to-cad.md#中文) | 把自然语言设计需求转成参数化 CAD 脚本和制造文件的智能体工具。 | 开发辅助 | 26417 |
| [ThinkRail](docs/thinkrail.md#中文) | 围绕 pi 编码智能体提供工作区、编辑器、变更审查和项目规格管理。 | 开发辅助 | 8310 |
| [TokenEconomizer](docs/token-economizer.md#中文) | 为编程智能体复用仓库经验、裁剪少用工具并识别失败循环，记录包含插件自身模型调用的会话成本。 | 开发辅助 | 7272 |
| [Univer](docs/univer.md#中文) | 用于嵌入网页的电子表格与文档 SDK，提供公式计算、渲染、编辑和程序接口，也支持无界面处理。 | 开发辅助 | 27511 |
| [Universal Modder](docs/universal-modder.md#中文) | 提供游戏模组制作的 Agent 技能、um 命令行工具和知识库，覆盖引擎识别、资源处理与游戏内验证。 | 开发辅助 | 9725 |
| [Unreal Engine Skills for Claude Code](docs/unreal-engine-skills.md#中文) | 指导 Claude Code 通过 MCP 操作 Unreal Editor 的技能和会话钩子。 | 开发辅助 | 1980 |
| [Vercel Skills CLI](docs/vercel-skills.md#中文) | 搜索、安装和管理 AI 编程智能体技能的命令行工具，支持按项目或全局配置技能。 | 开发辅助 | 39716 |
| [Voxel Musou](docs/voxel-musou.md#中文) | 浏览器 Three.js 体素动作游戏示例，包含多角色、章节与试炼，适合研究轻量游戏逻辑、渲染和本地进度管理。 | 开发辅助 | 178 |
| [vphone-cli](docs/vphone-cli.md#中文) | 在Apple Silicon Mac上运行用于研究与调试的虚拟iPhone。 | 开发辅助 | 16695 |
| [Wakaru](docs/wakaru.md#中文) | JavaScript 反编译工具，可拆分打包文件、展开压缩代码并恢复部分转译结构，提供 CLI 和网页试用。 | 开发辅助 | 1090 |
| [Worktrunk](docs/worktrunk.md#中文) | 简化 Git worktree 的切换、查看和清理，支持并行编码任务。 | 开发辅助 | 12565 |
| [Claude-BugHunter](docs/claude-bughunter.md#中文) | 用于授权范围内漏洞赏金与外部红队工作的 Claude Code 技能包，帮助 AI 完成安全测试与报告。 | 开发辅助 | 10641 |
| [SkillEvaluator](docs/skill-evaluator.md#中文) | 多层框架，用于评估 AI 智能体技能与插件的质量、安全、重叠、兼容性及真实效果。 | 开发辅助 | 3513 |
| [Cursor Plugins](docs/cursor-plugins.md#中文) | Cursor 官方插件规范与插件集合，面向 AI 编码智能体，提供开发工具、集成与效率类插件，帮助智能体完成代码审查、分支管理与第三方服务操作等任务。 | 开发辅助 | 17282 |
| [BLA (Blind LLM Agents)](docs/bla.md#中文) | 以 MCP 服务与 CLI 形式供 AI 编程智能体调用，加固软件发布产物以抵御 REA 等 AI 逆向工程 Agent。 | 开发辅助 | 6188 |
| [App Store Compliance Playbook](docs/app-store-compliance.md#中文) | 将 iOS/Android 应用被 App Store 与 Google Play 拒绝的原因整理为参考手册与提交前 guard，可作为 skill 安装进 AI 编码工具，让代理在提交前审计应用并阻断高风险提交。 | 开发辅助 | 1965 |

</details>

<a id="included-media"></a>

<details>
<summary><strong>图像与音视频</strong> · 68 项</summary>

| 项目 | 用途 | 分类 | Star |
| --- | --- | --- | ---: |
| [15 种动态设计风格](docs/mg-styles-15.md#中文) | 15 支 10 秒动态设计示例，逐项公开风格说明、完整提示词与源码。 | 图像与音视频 | 3540 |
| [3D Model Anything](docs/3d-model-anything.md#中文) | 把房间扫描资料转成可编辑 Three.js 场景的工具与智能体工作流程。 | 图像与音视频 | 3031 |
| [Abyssal Garden](docs/abyssal-garden.md#中文) | 以单个 HTML 展示可交互的海底场景。使用 WebGPU 绘制地形和生物，并实时合成声音。 | 图像与音视频 | 1440 |
| [Anatomy](docs/anatomy.md#中文) | 用交互式等轴测图解释机械、仪器和抽象机制。生成 SVG、HTML 或 React 组件，可叠加 WebGL 与 3D 效果。 | 图像与音视频 | 27394 |
| [Animate 程序化动画](docs/animate.md#中文) | 以单个 Canvas 程序化绘制和配乐，用无头浏览器与 FFmpeg 输出 MP4。 | 图像与音视频 | 1967 |
| [Arnis](docs/arnis.md#中文) | 把真实地理与高程数据转换成方块游戏世界。 | 图像与音视频 | 18642 |
| [ArtCraft](docs/artcraft.md#中文) | 桌面 AI 创作工作台，结合二维画面编排、三维场景和图像/视频模型，组织生成素材与创作流程。 | 图像与音视频 | 41207 |
| [ASCII](docs/ascii.md#中文) | 可嵌入网页的 TypeScript ASCII 动画组件，支持 React、Next.js、Astro、Web Components 和普通 HTML，也可生成 SVG。 | 图像与音视频 | 1232 |
| [Awesome DESIGN.md](docs/awesome-design-md.md#中文) | 收集知名网站设计语言的 DESIGN.md 文档。向编码智能体提供配色、字体、设计变量和界面规则。 | 图像与音视频 | 127606 |
| [Bang Motion](docs/bang-motion.md#中文) | 将开场、宣传片、产品演示、动态文字和讲解组织成可播放的单个 index.html。 | 图像与音视频 | 2201 |
| [cinecode](docs/cinecode.md#中文) | 面向编码智能体的影片制作技能。用网页画布或 Three.js 编排画面与声音，通过浏览器和 FFmpeg 输出 MP4。 | 图像与音视频 | 2593 |
| [Claude Animated Shorts](docs/claude-animated-shorts.md#中文) | 面向 Claude Code 的竖屏动画短片技能。用 Three.js 与 Remotion 渲染角色、场景和声音，附带桥梁故事示例。 | 图像与音视频 | 3658 |
| [Claude Animation Base](docs/claudeanimationbase.md#中文) | 以 p5.js 与 p5.brush 绘制角色，提供 Clawd 角色、核心绘画工具和时间线。 | 图像与音视频 | 2995 |
| [ComfyUI](docs/comfyui.md#中文) | 用节点图构建和复用图像、视频、音频及其他生成式 AI 工作流。 | 图像与音视频 | 147310 |
| [CosyVoice](docs/cosyvoice.md#中文) | 支持声音克隆、跨语言合成和流式输出的语音生成工具。 | 图像与音视频 | 24432 |
| [Deskworlds](docs/deskworlds.md#中文) | 在Mac桌面运行可交互的本地3D场景，也可在浏览器中体验。 | 图像与音视频 | 468 |
| [Diagram Design](docs/diagram-design.md#中文) | 把结构、流程和比较关系制作成独立 HTML 与 SVG 图表的智能体技能。 | 图像与音视频 | 67558 |
| [Diffusers](docs/diffusers.md#中文) | 基于 PyTorch 的扩散模型工具库，提供图像、视频和音频生成流水线。 | 图像与音视频 | 34932 |
| [F5-TTS](docs/f5-tts.md#中文) | 通过参考音频生成语音，提供命令行、Gradio 界面和微调工具。 | 图像与音视频 | 15607 |
| [faster-whisper](docs/faster-whisper.md#中文) | 基于 CTranslate2 运行 Whisper 的 Python 语音转写库。 | 图像与音视频 | 26823 |
| [Fish Speech](docs/fish-speech.md#中文) | 提供多角色语音生成、声音克隆和语音编辑的模型与推理工具。 | 图像与音视频 | 33764 |
| [FunASR](docs/funasr.md#中文) | 集成语音识别、语音检测、标点和说话人处理的音频工具集。 | 图像与音视频 | 21058 |
| [GIF 工厂 / GIF Factory](docs/gif-factory.md#中文) | 面向编码智能体的图像与动画技能集合。提供表情包、动态海报、签名、绘本和知识短片的制作说明与脚本。 | 图像与音视频 | 1940 |
| [God's Eye View](docs/gods-eye-view.md#中文) | 在交互式三维地球上叠加公开交通、地理与环境数据。 | 图像与音视频 | 65241 |
| [GPT-SoVITS](docs/gpt-sovits.md#中文) | 提供声音克隆、语音合成和少样本微调的 WebUI 与训练工具。 | 图像与音视频 | 65252 |
| [Handy](docs/handy.md#中文) | 通过快捷键录音，在本地识别语音，再把文字粘贴到当前输入位置。可选择 Whisper 或 Parakeet 等模型。 | 图像与音视频 | 38948 |
| [Hex](docs/hex.md#中文) | 在本机把语音转成文字并输入当前应用。支持词汇表、转写历史、文本处理步骤和录音文件转写。 | 图像与音视频 | 7045 |
| [Heytea Doodle Poster：实物照片与小人涂鸦](docs/heytea-style.md#中文) | heytea-doodle-poster 技能保留实物摄影质感，加入黑色简笔小人、留白和可选标题。 | 图像与音视频 | 350 |
| [Holo Card Studio](docs/holo-card-studio.md#中文) | 把分层图片制作成可旋转的全息卡网页和可编辑Blender工程。 | 图像与音视频 | 2106 |
| [HolyArrs](docs/holyarrs.md#中文) | 在自托管网页中管理媒体请求、筛选规则、字幕和文件入库。可连接现有下载器与媒体服务器。 | 图像与音视频 | 1325 |
| [Huashu Design](docs/huashu-design.md#中文) | 面向智能体的 HTML 原生设计技能。可制作网页、App 原型、可编辑 PPTX、动画和信息图。 | 图像与音视频 | 29538 |
| [Hunyuan3D 2](docs/hunyuan3d-2.md#中文) | 通过形状生成和纹理合成两个阶段，把图像转换为带纹理的 3D 资产。 | 图像与音视频 | 15462 |
| [Hyperframes](docs/hyperframes.md#中文) | 用 HTML/CSS 和可定位时间的动画制作视频，通过无头浏览器与 FFmpeg 确定性渲染 MP4；提供 CLI、Agent 技能和桌面工作台。 | 图像与音视频 | 85034 |
| [Ian Xiaohei Illustrations](docs/ian-xiaohei-illustrations.md#中文) | 为中文正文生成白底手绘“小黑”风格的 PNG 插图。技能先提炼文章观点，再规划分镜并生成配图。 | 图像与音视频 | 13217 |
| [Immich](docs/immich.md#中文) | Immich 是自托管的照片与视频库，提供手机自动上传、相册管理、人脸识别和 CLIP 检索。 | 图像与音视频 | 119440 |
| [InvokeAI](docs/invokeai.md#中文) | 面向图像创作的本地 AI 应用，结合画布编辑、节点工作流和模型管理。 | 图像与音视频 | 29105 |
| [Lemo-Opuscar](docs/lemo-opuscar.md#中文) | 提供动画风格指南、提示词、示例代码和短片。当前 README 列出 99 种风格。 | 图像与音视频 | 16446 |
| [LivePortrait](docs/liveportrait.md#中文) | 用驱动视频或运动模板为人物及动物肖像生成动画。 | 图像与音视频 | 19514 |
| [LTX-2](docs/ltx-2.md#中文) | 用于同步音视频生成、视频转换和局部片段重生成的 Python 工具库。 | 图像与音视频 | 10280 |
| [Mac Duo](docs/mac-duo.md#中文) | 根据 MacBook 屏幕开合角度，为实时桌面画面添加倾斜、模糊和渐暗效果。 | 图像与音视频 | 1236 |
| [MCP for Blender](docs/mcp-for-blender.md#中文) | 通过 MCP 把 Agent 连接到 Blender，用自然语言组织场景、模型、材质和渲染，并接入可选素材服务。 | 图像与音视频 | 34616 |
| [MoneyPrinterTurbo](docs/moneyprinterturbo.md#中文) | 将主题或关键词转成脚本、配音、素材和字幕，并合成短视频。 | 图像与音视频 | 144052 |
| [MyGo Music](docs/mygo-music.md#中文) | 原生桌面音乐播放器，支持本地音乐、歌词、播放列表和插件。插件可接入音乐目录、播客和电台。 | 图像与音视频 | 1408 |
| [Open Generative AI](docs/open-generative-ai.md#中文) | 可自行部署的 AI 图像和视频创作界面，连接 MuAPI 云模型；桌面版还提供本地推理引擎接入。 | 图像与音视频 | 35058 |
| [OpenCreator](docs/opencreator.md#中文) | 以对话与可视化工作区组织内容制作，管理生成任务、素材、字幕和版本。 | 图像与音视频 | 14380 |
| [Photo Relic Editorial：照片与纸上印迹](docs/photo-relic-editorial.md#中文) | 上方保持真实照片，下方将源图轮廓、光线和配色提炼为纸张版画式印迹。 | 图像与音视频 | 454 |
| [Photo-to-Zine：照片明信片正反面](docs/photo-to-zine-postcard.md#中文) | 保留原照，结合手绘元素、三个色块与协调的背面，生成 2:3 明信片正反面。 | 图像与音视频 | 289 |
| [PhotoPrism](docs/photoprism.md#中文) | PhotoPrism 是自托管的照片与视频管理工具，可自动生成标签、识别人脸，并按内容及元数据筛选素材。 | 图像与音视频 | 40456 |
| [Qwen-Image](docs/qwen-image.md#中文) | 提供文生图和图像编辑模型及示例，支持画面中的文字生成和多图编辑。 | 图像与音视频 | 8487 |
| [Remotion](docs/remotion.md#中文) | 用 React 和网页技术制作视频，支持编码智能体生成工程、交互预览和批量渲染。 | 图像与音视频 | 73840 |
| [SAM 3](docs/sam3.md#中文) | 按文字、点、框或掩码提示分割图像与视频，并跟踪视频中的目标。 | 图像与音视频 | 12319 |
| [SCM](docs/scm.md#中文) | 在 Mac 本地索引图片、截图和视频。按画面描述、可见文字或对白查找素材，并跳转到匹配的视频时间位置。 | 图像与音视频 | 529 |
| [Subvox](docs/subvox.md#中文) | 研究 AirPods 头部运动数据能否识别无声口型的小词汇量实验原型。 | 图像与音视频 | 838 |
| [SwarmUI](docs/swarmui.md#中文) | 为图像、视频及部分音频生成模型提供可扩展的网页界面。 | 图像与音视频 | 4791 |
| [Teardown：交互式机械拆解与3D演示](docs/teardown.md#中文) | 面向 Claude Code 的 3D 机械原理演示技能。支持部件拆解、剖视、联动、自动演示与人工交互，可构建离线 HTML 并录制 MP4。 | 图像与音视频 | 3534 |
| [Turbo Kart Rally](docs/turbo-kart-rally.md#中文) | 在浏览器中运行的 Three.js 卡丁车游戏和程序化内容示例。 | 图像与音视频 | 50 |
| [Upscayl](docs/upscayl.md#中文) | 使用 AI 超分辨率模型放大低分辨率图像的桌面工具，支持批量处理和模型选择。 | 图像与音视频 | 52784 |
| [VoiceStudio](docs/voicestudio.md#中文) | 在本地运行语音克隆、声音设计、转录和视频配音。另提供听写、有声书、批量任务及本地 API 与 MCP 接口。 | 图像与音视频 | 110994 |
| [Wan2.2](docs/wan2-2.md#中文) | 用于文生视频、图生视频和角色动画的模型与推理代码。 | 图像与音视频 | 18725 |
| [Whisper](docs/whisper.md#中文) | 将音频转写为文本的多语言语音识别模型与工具，支持语言检测和将语音翻译为英语。 | 图像与音视频 | 112864 |
| [WhisperX](docs/whisperx.md#中文) | 在 Whisper 转写基础上增加逐词时间戳、对齐和说话人区分。 | 图像与音视频 | 25405 |
| [YuE2 推理代码 / YuE2 inference code](docs/yue.md#中文) | 通过可编辑旋律与和弦计划生成包含人声和伴奏的歌曲。 | 图像与音视频 | 13534 |
| [产品宣传片制作](docs/video-shotcraft.md#中文) | 面向产品发布和功能演示，采集真实页面素材后用 Remotion 编排影片。 | 图像与音视频 | 19790 |
| [代码手绘插画与动画](docs/anidoodle.md#中文) | 以代码描述笔画，提供 32 种插画风格和逐笔绘制示例。 | 图像与音视频 | 1693 |
| [手绘口播视频](docs/sweety-handdraw-video.md#中文) | Agent 整理内容、口播和分镜，本地工具执行描线、填色、手写文字与声音对齐。 | 图像与音视频 | 1218 |
| [拾景纸刊：照片与撕纸拼贴](docs/gathered-scenes-zine-skill.md#中文) | scenes-gathered-zine-v1-3 保留照片片段，延展插画、结构色和撕纸边界，默认 3:5。 | 图像与音视频 | 5660 |
| [照片转海报：厚涂微缩景观与水彩旅行卡](docs/photo-to-poster-skills.md#中文) | 将参考照片整体重绘为厚涂微缩景观或水彩旅行卡。两个技能同属一个仓库，默认均为 3:4 竖图。 | 图像与音视频 | 36 |
| [花叔艺术动画](docs/huashu-art-motion.md#中文) | 当前 README 列出 36 种艺术风格、9 种解说语法和 8 种参数化片段。 | 图像与音视频 | 6941 |

</details>

<a id="included-productivity"></a>

<details>
<summary><strong>文档与效率</strong> · 59 项</summary>

| 项目 | 用途 | 分类 | Star |
| --- | --- | --- | ---: |
| [Aerial TV](docs/aerial-tv.md#中文) | Android TV 桌面启动器，提供应用网格、文件夹、HDMI 入口、壁纸屏保和手机遥控管理。 | 文档与效率 | 12155 |
| [AirCursor](docs/aircursor.md#中文) | 把支持头部追踪的耳机动作转换为Mac鼠标移动与点击。 | 文档与效率 | 226 |
| [Animated Resume Claude Skill](docs/animated-resume-claude-skill.md#中文) | 引导 AI 助手把简历事实整理为结构化资料，再生成带职业关卡、动画头像和项目关系图的单页 HTML 作品集。 | 文档与效率 | 2 |
| [Anki Desktop](docs/anki.md#中文) | 用记忆卡片与间隔重复安排复习。 | 文档与效率 | 32834 |
| [Answer me with HTML](docs/answer-me-with-html.md#中文) | 供 AI Agent 使用的技能和本地渲染 CLI，将 Markdown 回答转换为包含图表、代码和交互反馈的单页 HTML。 | 文档与效率 | 6390 |
| [Anthropic Skills](docs/anthropic-skills.md#中文) | Anthropic 的智能体技能示例仓库；本条重点收录当前采用 Apache 2.0 的 Word、PDF、PowerPoint 和表格文档技能及辅助脚本。 | 文档与效率 | 196194 |
| [best-skills](docs/best-skills.md#中文) | 收集采用 SKILL.md 格式的智能体工作流程。覆盖论文、专利、汇报、自媒体、图表和代码文档。 | 文档与效率 | 3176 |
| [Call Notes to Actions](docs/call-notes-to-actions-skill.md#中文) | 将会议转录或零散笔记整理成摘要、决策、行动表和跟进邮件草稿的轻量智能体技能。 | 文档与效率 | 0 |
| [CCBaga](docs/ccbaga.md#中文) | 管理本机 Claude 身份配置、客户端工具和配套浏览器环境。 | 文档与效率 | 3618 |
| [Clash 客户端导航（clashbk）](docs/clash.md#中文) | 汇总 Clash 相关客户端的项目入口、下载地址和教程。另列已停更版本的备份入口，属于导航资料库。 | 文档与效率 | 11389 |
| [Claude PowerPoint Skill](docs/claude-powerpoint-skill.md#中文) | 为 AI 编程助手提供 PowerPoint 构建、检查和逐页渲染复核流程，支持跨平台生成 PPTX 及 Windows 下操作桌面 PowerPoint。 | 文档与效率 | 6 |
| [ColaMD](docs/colamd.md#中文) | 跨平台 Markdown 编辑器，提供所见即所得与源码视图、文件同步、大纲和主题，并支持导出常用文档格式。 | 文档与效率 | 1303 |
| [Docling](docs/docling.md#中文) | 解析文档版面与内容，并导出结构化结果的工具。 | 文档与效率 | 70696 |
| [Echo Loop](docs/echo-loop.md#中文) | 通过精听、跟读、复述和复习流程练习英语听说。 | 文档与效率 | 4772 |
| [Filee](docs/filee.md#中文) | 本地文件转换器，提供可选的 Ollama 文档翻译、Whisper 音视频转写和 AI 图像放大模块。 | 文档与效率 | 28180 |
| [GenOffice](docs/genoffice.md#中文) | 提供 Office、PDF、Markdown 和 HTML 文件编辑。包含桌面编辑器、CLI、MCP 和智能体技能，可创建、转换和检索文件。 | 文档与效率 | 12376 |
| [Guizang PPT Skill](docs/guizang-ppt-skill.md#中文) | 指导智能体制作单文件 HTML 演示文稿，提供电子杂志和瑞士网格风格，以及本地浏览器演讲者视图。 | 文档与效率 | 29911 |
| [Horizon：AI 信息聚合与双语新闻简报](docs/horizon.md#中文) | 聚合 RSS、社区、GitHub 与新闻等信息源，按 Profile 评分、筛选和去重，生成中英双语 Markdown 日报。 | 文档与效率 | 14389 |
| [i-have-adhd](docs/i-have-adhd.md#中文) | 调整编码智能体的回答格式，使行动步骤和关键信息更容易找到。 | 文档与效率 | 61361 |
| [Joplin 客户端 / Joplin clients](docs/joplin.md#中文) | 以Markdown笔记本组织笔记、待办和附件，支持搜索与同步。 | 文档与效率 | 57204 |
| [KISS Translator](docs/kiss-translator.md#中文) | 支持网页双语阅读、划词和字幕翻译的浏览器扩展与用户脚本，可选择传统翻译引擎、云端大模型或本地 AI。 | 文档与效率 | 13389 |
| [Knowledge Work Plugins](docs/knowledge-work-plugins.md#中文) | 为知识工作提供按岗位组织的智能体技能、命令和连接器配置。 | 文档与效率 | 36258 |
| [Marketing Skills](docs/marketingskills.md#中文) | 为 AI 智能体提供营销任务技能，围绕产品定位组织文案、SEO、转化分析、外联和增长工作流。 | 文档与效率 | 60867 |
| [MarkItDown](docs/markitdown.md#中文) | 将多种文件转换为 Markdown 的 Python 工具。 | 文档与效率 | 195977 |
| [MarkText](docs/marktext.md#中文) | 支持实时预览与文件管理的跨平台 Markdown 编辑器。 | 文档与效率 | 64049 |
| [MinerU](docs/mineru.md#中文) | 将复杂文档解析为结构化内容，并提供文档库和读取接口的工具。 | 文档与效率 | 83808 |
| [NewsNow](docs/newsnow.md#中文) | 聚合多站热点与实时新闻，支持 GitHub 登录同步，并通过官方 MCP 为 AI 客户端提供新闻标题和原文链接。 | 文档与效率 | 22489 |
| [OpenLogi](docs/openlogi.md#中文) | Rust 原生 Logitech 设备工具，通过 HID++/UVC 配置鼠标、键盘与摄像头，提供按钮、DPI、滚轮和跨电脑 Flow 等能力。 | 文档与效率 | 25783 |
| [OpenWhispr](docs/openwhispr.md#中文) | 跨平台语音输入与会议转写应用，通过快捷键把语音转换为当前光标处的文本，提供笔记、说话人区分和可选 AI 助手。 | 文档与效率 | 11669 |
| [PaddleOCR](docs/paddleocr.md#中文) | 识别图像文字并解析文档结构的 OCR 工具集。 | 文档与效率 | 92809 |
| [PlayCover](docs/playcover.md#中文) | 在 Apple Silicon Mac 上运行兼容的 iOS 应用，提供键鼠和手柄映射。 | 文档与效率 | 12156 |
| [PPT Master](docs/ppt-master.md#中文) | 在智能体中组织资料分析、页面设计和本地导出，将主题或文档制作成可继续编辑的 PowerPoint 演示文稿。 | 文档与效率 | 77626 |
| [Prosyo GTM Skills](docs/gtm-skill.md#中文) | 面向 AI 助手的营销与销售技能集，提供客户研究、开发信起草、跟进、邮件送达率检查和客户访谈流程。 | 文档与效率 | 12 |
| [Read Frog](docs/read-frog.md#中文) | 结合网页翻译、字幕翻译和词汇复习的浏览器语言学习扩展。 | 文档与效率 | 10456 |
| [Tendedero](docs/tendedero.md#中文) | 在 macOS 屏幕顶部暂存截图、复制文本和链接，便于拖放与再次使用。 | 文档与效率 | 3263 |
| [Tolaria](docs/tolaria.md#中文) | 用 Markdown 文件和 Git 管理知识库，并通过桌面 AI 面板与 MCP 让模型和编程智能体检索、讨论或编辑笔记。 | 文档与效率 | 20559 |
| [Unstructured](docs/unstructured.md#中文) | 把非结构化文档拆分为内容元素的 Python 库。 | 文档与效率 | 15755 |
| [VNote](docs/vnote.md#中文) | 在本地管理笔记，并编辑Markdown、Typst、文本和思维导图。 | 文档与效率 | 13048 |
| [Window Sweaters](docs/window-sweaters.md#中文) | 给 macOS 窗口添加针织风格边框，可为不同应用设置颜色或关闭装饰，并区分活动窗口。 | 文档与效率 | 1495 |
| [Yank Note](docs/yank-note.md#中文) | 以本地 Markdown 文件保存笔记的可扩展编辑器。 | 文档与效率 | 6784 |
| [YiShu5 Agent Skills](docs/yishu5-claude-skills.md#中文) | 面向中文办公与创作的 AI Agent 技能集，包含会议纪要、日报周报、页面演示、写作和公众号工作流。 | 文档与效率 | 130 |
| [Yogurt](docs/yogurt.md#中文) | 在本机记录会议语音、生成转写和纪要，并从历史会议中回答问题、附上出处。 | 文档与效率 | 1788 |
| [Zettlr](docs/zettlr.md#中文) | 面向研究与长文写作的 Markdown 编辑器，提供文献引用、笔记链接、全文搜索和多格式导出。 | 文档与效率 | 13922 |
| [中国专利 Skill](docs/patent-disclosure-skill.md#中文) | 从技术资料整理专利交底草稿，并辅助检索、阅读和案卷整理。 | 文档与效率 | 13513 |
| [中国独立开发者项目列表](docs/chinese-independent-developer.md#中文) | 汇集中国独立开发者的网站、App 和产品。按日期、作者、项目简介与上线状态组织条目。 | 文档与效率 | 62115 |
| [中小学·高中知识图谱（cn-math-taxonomy）](docs/cn-math-taxonomy.md#中文) | 按知识点和先修关系组织中小学至高中多学科资料。提供图谱浏览、题库和自适应前置诊断，追溯基础知识薄弱点。 | 文档与效率 | 8095 |
| [人情世故指南](docs/howtogetalong.md#中文) | 10 章 77 条经验建议，覆盖合作、求助、拒绝、金钱、礼节与冲突。 | 文档与效率 | 2048 |
| [人生进阶指南](docs/up.md#中文) | 开放书稿从英语学习扩展到终身学习、AI 协作、项目实践与复盘。 | 文档与效率 | 70565 |
| [妙言 / MiaoYan](docs/miaoyan.md#中文) | Swift 原生 macOS Markdown 笔记应用，管理本地文件与文件夹，支持双向链接、公式、Mermaid、历史记录和演示。 | 文档与效率 | 8781 |
| [投资入门指南](docs/investing-for-beginners.md#中文) | 官方定位是中文投资入门资料，主题包含美股、期权和加密资产。 | 文档与效率 | 4539 |
| [数字员工配置包（开源样例）](docs/digital-employee-pack.md#中文) | 面向 AI Agent 的三个中文办公技能样例，帮助整理周报、会议纪要和 PPT 逐页内容大纲。 | 文档与效率 | 0 |
| [狗头军师](docs/goutoujunshi.md#中文) | 可分析用户叙述、聊天截图和已导出文本，给出回复草案与行动选项。 | 文档与效率 | 9693 |
| [百智办公 MonkeyAI（MonkeyCode）](docs/monkeycode.md#中文) | 面向团队 AI 办公的服务端与管理后台，统一配置模型、知识库、技能和 MCP 连接器，供兼容客户端执行办公、编程与设计任务。 | 文档与效率 | 5244 |
| [知了 Cicada](docs/cicada.md#中文) | 为会议和直播提供双语字幕、同声传译与会议纪要。直接读取系统声音，支持转写搜索和记录导出。 | 文档与效率 | 2347 |
| [程序员做饭指南](docs/howtocook.md#中文) | 按菜品组织食材、用量和制作步骤，适合按明确流程学做饭。 | 文档与效率 | 103951 |
| [程序员延寿指南](docs/howtolivelonger.md#中文) | README 列出 64 篇研究摘要，覆盖食物、运动、睡眠和日常习惯。 | 文档与效率 | 36107 |
| [词光 Word Atlas](docs/word-atlas.md#中文) | 用插画、发音和间隔复习学习英语词汇的网页应用。 | 文档与效率 | 4915 |
| [高性价比人生指南](docs/howtolivebetter.md#中文) | 覆盖生活开支、应急、健康、社保、就业、法律边界和家庭事务。条目说明成本、收益、证据和出处。 | 文档与效率 | 75865 |
| [PaperOrchestra](docs/paper-orchestra.md#中文) | 多智能体框架，将想法与实验日志自动写成可提交的 LaTeX 论文并完成文献综述与图表。 | 文档与效率 | 3837 |

</details>

<a id="included-automation"></a>

<details>
<summary><strong>自动化</strong> · 20 项</summary>

| 项目 | 用途 | 分类 | Star |
| --- | --- | --- | ---: |
| [Activepieces](docs/activepieces.md#中文) | 用 TypeScript 集成组件和可视化流程构建 AI 自动化。 | 自动化 | 25581 |
| [Agent Autoloop](docs/agent-autoloop.md#中文) | 把命令行智能体接入事件调度和后台执行。支持人工卡片、回答后继续、定时复查、日志重放及可选 PR 交付。 | 自动化 | 5427 |
| [agent-desktop](docs/agent-desktop.md#中文) | 通过操作系统无障碍接口，为 AI 智能体提供桌面快照和界面操作。 | 自动化 | 24668 |
| [agentes.chat](docs/agentes-chat.md#中文) | 让团队成员和智能体在频道与私信中协作。为智能体配置角色、模型、预算、工具和执行环境。 | 自动化 | 1597 |
| [AX](docs/google-ax.md#中文) | 用声明式配置调度沙箱中的智能体任务和工作区。 | 自动化 | 14733 |
| [Browser Use](docs/browser-use.md#中文) | 让模型通过 Python 与浏览器工具执行真实网页任务。 | 自动化 | 121292 |
| [cc-connect](docs/cc-connect.md#中文) | 把本机编程智能体接入聊天平台，包括飞书和钉钉。从聊天端管理会话、切换模型、安排任务及传递文件。 | 自动化 | 16376 |
| [Chrome DevTools MCP](docs/chrome-devtools-mcp.md#中文) | 通过 MCP 让编码智能体控制 Chrome，并读取调试和性能信息。 | 自动化 | 57952 |
| [Cua（MIT 桌面自动化组件）](docs/cua-mit-components.md#中文) | 收录 Cua 的 MIT 许可 SDK、CLI、Driver 和 Lume，用于 Agent 截图、输入控制及本地虚拟电脑管理。 | 自动化 | 32442 |
| [ESP32 iPhone Agent](docs/esp32-iphone-agent.md#中文) | 让智能体通过 ESP32-S3 与真实 iPhone 交互的软硬件项目。 | 自动化 | 5022 |
| [Mobile MCP](docs/mobile-mcp.md#中文) | 通过 MCP 让智能体操作 Android 与 iOS 应用、模拟器及真实设备。 | 自动化 | 10616 |
| [n8n](docs/n8n.md#中文) | 把可视化流程、自定义代码、业务集成和 AI Agent 组合起来。 | 自动化 | 210807 |
| [PhoneBox](docs/phonebox.md#中文) | 把 Android 手机用作电脑的桌面面板和触控控制台，提供系统指标、AI 编程会话、配额及可选权限响应模块。 | 自动化 | 2004 |
| [Playwright MCP](docs/playwright-mcp.md#中文) | 通过 MCP 为 AI 提供浏览器导航、页面结构读取和交互工具。 | 自动化 | 39780 |
| [Reason Network](docs/reason-network.md#中文) | 每台电脑运行后台程序，共享团队 Agent 会话的人员、设备、项目、分支与工作概况。 | 自动化 | 1748 |
| [Stagehand](docs/stagehand.md#中文) | 为浏览器智能体提供交互、观察和结构化数据提取 SDK。 | 自动化 | 26077 |
| [Voice Control Agent](docs/voice-control-agent.md#中文) | 为 Mac 上的 Codex 桌面会话提供本机唤醒、语音输入和回复朗读入口。 | 自动化 | 5 |
| [XGIMI Agent](docs/xgimi-agent.md#中文) | macOS 菜单栏与 Agent 技能，通过局域网控制用户自己的极米投影仪，提供遥控、截图与实验性蓝牙唤醒。 | 自动化 | 7 |
| [XiaoZhi ESP32](docs/xiaozhi-esp32.md#中文) | 面向 ESP32 设备的语音交互固件，将语音模型和 MCP 设备控制接到硬件上。 | 自动化 | 33330 |
| [LoopForge](docs/loopforge.md#中文) | 自托管的编码 Agent 交付编排平台，用 SOP、Docker 沙箱与人工审批组织 CodeBuddy、Codex、Claude Code 等执行器完成需求交付。 | 自动化 | 3731 |

</details>

<a id="included-operations"></a>

<details>
<summary><strong>部署与运维</strong> · 19 项</summary>

| 项目 | 用途 | 分类 | Star |
| --- | --- | --- | ---: |
| [1Panel](docs/1panel.md#中文) | Linux 服务器的网页管理面板，管理容器、数据库、文件、站点与证书，并提供部分模型和 GPU 管理能力。 | 部署与运维 | 37458 |
| [Anthropic Sandbox Runtime](docs/anthropic-sandbox-runtime.md#中文) | 为智能体、MCP 服务和命令提供操作系统级文件与网络访问限制的运行时。 | 部署与运维 | 7155 |
| [Arize Phoenix](docs/phoenix.md#中文) | 提供 OpenTelemetry 追踪、数据集、实验和提示管理，并支持 MCP 查询。 | 部署与运维 | 12325 |
| [Clash Verge Rev](docs/clash-verge-rev.md#中文) | 基于 Tauri 的 mihomo 图形代理客户端。提供配置管理、规则编辑、系统代理、TUN 模式和 WebDAV 同步。 | 部署与运维 | 158520 |
| [Claude Cage](docs/claude-cage.md#中文) | 用于运行 Claude Code 和相关开发工具的桌面工作台，管理本地虚拟机、项目共享与独立网络配置，也可连接自有 Linux 服务器。 | 部署与运维 | 6137 |
| [CleanYourTV](docs/cleanyourtv.md#中文) | 为 Android TV/Google TV 提供可恢复的预装软件停用流程和轻量桌面启动器。 | 部署与运维 | 58509 |
| [Helicone](docs/helicone.md#中文) | 结合模型网关、请求日志、会话分析和提示版本管理的 LLM 平台。 | 部署与运维 | 6286 |
| [JumpServer](docs/jumpserver.md#中文) | 集中管理服务器、数据库和其他基础设施的特权访问与审计。 | 部署与运维 | 31970 |
| [Langfuse](docs/langfuse.md#中文) | 汇集模型调用、智能体轨迹、提示版本和评测结果的 AI 工程平台。 | 部署与运维 | 37546 |
| [LangWatch](docs/langwatch.md#中文) | 统一查看智能体轨迹、模拟测试、编码助手会话和模型网关用量。 | 部署与运维 | 5042 |
| [Netdata Agent](docs/netdata.md#中文) | 采集主机、容器与应用指标，并在本地存储、检测异常和触发告警。 | 部署与运维 | 81435 |
| [Omarchy](docs/omarchy.md#中文) | 为开发与日常使用预配置桌面、终端、快捷键和工具的Linux发行版。 | 部署与运维 | 47063 |
| [OpenBao](docs/openbao.md#中文) | 集中保存和分发机密、证书与密钥，并管理访问、租约和撤销。 | 部署与运维 | 9049 |
| [OpenSandbox](docs/open-sandbox.md#中文) | 在自有 Docker 或 Kubernetes 基础设施上管理 AI 智能体的隔离执行环境。 | 部署与运维 | 17391 |
| [OpenShell](docs/openshell.md#中文) | 为智能体提供隔离运行环境，按策略控制文件、网络和凭据访问。 | 部署与运维 | 21676 |
| [Portkey AI Gateway](docs/gateway.md#中文) | 为多家模型提供统一调用接口、条件路由、重试、回退和护栏。 | 部署与运维 | 13390 |
| [TelemetryCleaner](docs/telemetrycleaner.md#中文) | 通过 Shizuku 检查 Android 预装运营商组件，查看各空间状态与权限，并管理卸载、恢复及失败后的停用。 | 部署与运维 | 807 |
| [Triton Inference Server](docs/server.md#中文) | 统一部署和调用多种机器学习模型的推理服务器。 | 部署与运维 | 11146 |
| [wifit3](docs/wifit3.md#中文) | 使用支持的USB无线网卡分析无线网络状态与安全配置。 | 部署与运维 | 3593 |

</details>

<a id="included-data"></a>

<details>
<summary><strong>数据处理</strong> · 22 项</summary>

| 项目 | 用途 | 分类 | Star |
| --- | --- | --- | ---: |
| [AI Berkshire](docs/ai-berkshire.md#中文) | 基于 Claude Code 与 Codex 的价值投资研究技能。通过多个分析视角组织公司研究、财报、估值、组合复盘和论点跟踪。 | 数据处理 | 17140 |
| [Chroma](docs/chroma.md#中文) | 管理文档、向量嵌入和元数据的检索数据库。 | 数据处理 | 29704 |
| [Claude for Financial Services](docs/financial-services.md#中文) | 为金融研究与运营提供智能体模板、技能、数据连接器和部署脚本。 | 数据处理 | 41340 |
| [Claude SEO](docs/claude-seo.md#中文) | 在 Claude Code 中检查网站技术 SEO、内容和结构化数据，并整理改进建议。 | 数据处理 | 30107 |
| [Crawl4AI](docs/crawl4ai.md#中文) | 把网页抓取为 Markdown 或结构化数据，支持自行部署和托管 API。 | 数据处理 | 87470 |
| [Datasets](docs/datasets.md#中文) | 加载、转换和流式读取机器学习数据集的 Python 库。 | 数据处理 | 22151 |
| [easyquotation](docs/easyquotation.md#中文) | 封装新浪、腾讯和集思录部分接口的 Python 行情库，用于单只、多只股票及市场快照读取。 | 数据处理 | 5478 |
| [Faiss](docs/faiss.md#中文) | 用于稠密向量相似度搜索和聚类的库。 | 数据处理 | 41767 |
| [FiftyOne](docs/fiftyone.md#中文) | FiftyOne 将本地图片和视频整理为可筛选的数据集。它提供 Python 接口与可视化应用，用于检索、标注和模型评估。 | 数据处理 | 11315 |
| [Firecrawl](docs/firecrawl.md#中文) | 提供网页搜索、抓取、交互与文档解析接口，为 AI 整理网页内容。 | 数据处理 | 202520 |
| [LanceDB](docs/lancedb.md#中文) | 基于 Lance 列式格式管理向量和多模态数据的数据库。 | 数据处理 | 11913 |
| [Milvus](docs/milvus.md#中文) | 存储向量与标量数据，并提供相似度检索的数据库。 | 数据处理 | 46677 |
| [OpenSEO](docs/open-seo.md#中文) | 自托管关键词、排名、外链和网站审计工作台，并向智能体提供MCP接口。 | 数据处理 | 27897 |
| [Qdrant](docs/qdrant.md#中文) | 存储向量及附加数据，并提供相似度搜索的数据库。 | 数据处理 | 35603 |
| [Resource Radar (Freebie Radar)](docs/freebie-radar.md#中文) | 自托管的信息聚合与筛选工具，从社区、RSS 和资源站采集条目，用规则和可选 AI 审核分类、评分，再供网页浏览或 Telegram 推送。 | 数据处理 | 1214 |
| [Sentence Transformers](docs/sentence-transformers.md#中文) | 计算、训练向量嵌入和重排序模型的 Python 库。 | 数据处理 | 19289 |
| [The Well](docs/the-well.md#中文) | 提供物理时空模拟数据的统一读取、下载和模型基准工具。 | 数据处理 | 4577 |
| [TradingAgents](docs/tradingagents.md#中文) | 通过多种大模型角色组织金融研究，包括分析师、研究员和风险管理角色。 | 数据处理 | 122872 |
| [TradingAgents-CN](docs/tradingagents-cn.md#中文) | 面向 A 股的多智能体研究辅助系统，社区版提供研究、筛选、课程和模拟交易；应用层采用专有许可。 | 数据处理 | 32957 |
| [Vibe Research](docs/vibe-research.md#中文) | 面向 A 股、美股和港股的投研工作台。整合自选、持仓、每日复盘、产业与公司研究、历史回测和研报库。 | 数据处理 | 3720 |
| [Weaviate](docs/weaviate.md#中文) | 结合向量检索、关键词搜索和模型集成的数据库。 | 数据处理 | 16952 |
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
<summary><strong>知识与学习</strong> · 4 项</summary>

| 项目 | 用途 | 分类 | Star |
| --- | --- | --- | ---: |
| [AI Agent 工程实践书](docs/ai-agent-book.md#中文) | 通过公开教材、配套实验和技能包学习 AI Agent 的设计与工程实现。 | 知识与学习 | 58306 |
| [Human Atlas](docs/human-atlas.md#中文) | 可在浏览器中旋转、拆分、搜索和选择人体结构的三维解剖图谱。 | 知识与学习 | 4571 |
| [Many PPT Skills](docs/many-ppt-skills.md#中文) | 面向智能体的 AI 幻灯片工具登记册和查询脚本，按可编辑性、备注、模板与交付格式筛选技能及视觉样式。 | 知识与学习 | 81 |
| [Scientific Agent Skills](docs/scientific-agent-skills.md#中文) | 为科学计算、资料检索和研究流程提供可组合的智能体技能。 | 知识与学习 | 57421 |

</details>

[返回分类导航](#categories)

<a id="review"></a>

## 历史复核记录与覆盖范围

以下记录描述本次规则调整前的复核。许可审查、实质维护、候选状态及批次 Star 条件均为当时的标准或结论；当前规则见[收录标准](#criteria)。

2026-11-17 复核用户提供的仓库链接，新增 **26 个双语词条**。按主要用途分类，并分别检查许可、近期实质维护和使用限制。未通过项目及依据见[链接收录复核记录](reviews/2026-11-17-submitted-repositories.md)。

2026-11-17 从此前筛选的 GitHub 月榜名单新增 **40 个 AI 相关双语词条**：**38 个已收录**、**2 个候选**。本批要求月榜新增至少 1,000 Star，并按主要用途归类。这是当时本批选项的门槛，不作为当前规则。详情见[趋势榜复核记录](reviews/2026-11-17-ai-trending.md)。

2026-11-16 本轮新增 **147 个双语词条**，其中 **10 个项目低于 1,000 Star**。原有 **62 个词条**保留 2026-11-15 的记录，未在本轮重新评估：35 个原已收录加 147 个新增，合计 182 个已收录，另有 27 个原候选。

本轮检查 **2026-08-16 至 2026-11-16** 的公开文章线索，包括 **逛逛GitHub**、**AI开源求索**的署名转载与第三方索引。两个账号都属于部分覆盖：转载或索引不能证明已经读取微信原文，部分公众号归属仍待核实。仓库是否符合条件，另依据上游许可、实现与活动证据判断。

2026-11-17 修订了候选状态表达、许可作用范围及维护证据，并补充固定版本的许可来源。原 Star 与仓库状态快照保留原日期；证据整理不等于重新试用所有项目。

本轮未安装或运行上游软件。[公众号文章复核记录](reviews/2026-11-16-wechat.md)列出覆盖范围、筛选结论、未新增原因和带日期的来源；每个新增词条保留对应证据等级。

<a id="contributing"></a>

## 新增或更新词条

在 `docs/<项目名>.md` 中维护双语介绍。写明仓库、AI 任务用途、功能、环境、限制、入门方式和来源。记录 Star 快照、所用门槛的证据、近 3 个日历月活动及复核日期。达标项目直接加入正式目录，不建立候选词条；未达标或证据不足时说明原因。同步更新两份目录，保持用途、分类与 Star 快照一致。仅阅读文档时注明“文档复核”，实际测试另行记录。

提交前运行以下离线检查（Python 3.10+，仅使用标准库）：

```bash
python3 scripts/check_catalog.py
python3 -m unittest discover -s tests
```

检查覆盖目录与词条的一致性、本地链接、证据结构和历史状态隔离。AI 任务用途、活动来源、Star 数据及外链可用性仍需人工复核。GitHub Actions 会运行相同检查。

| 位置 | 内容 |
| --- | --- |
| [README.md](README.md) / [README.en.md](README.en.md) | 中英文说明与目录 |
| [docs/](docs/) | 每个项目一份双语词条 |
| [reviews/](reviews/) | 来源覆盖与复核结论 |
| [assets/readme/](assets/readme/) | 首页插图 |

## 许可证

本仓库采用 [Apache License 2.0](LICENSE)。各工具保留自己的许可证，具体范围见词条与上游条款。

[返回顶部](#ai-station) · [分类浏览](#categories) · [English](README.en.md)
