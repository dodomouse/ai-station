# 100 个可帮助 AI 完成任务的 GitHub 仓库

[中文目录](../README.md) · [English index](../README.en.md) · [完整核验数据](2026-11-17-ai-repository-shortlist.json)

复核日期：**2026-11-17**。本次从 110 个通过核验的仓库中整理出 100 个，覆盖 12 类用途。每项都有简述、Star 快照、官方文档和具体活动链接。

这 100 项已全部正式收录，目录总数为 **375 项**。每项均有完整双语词条，按本库的九类目录组织；下表保留筛选时的 12 类任务分组。新增项目与原有 275 项按仓库名称和 GitHub 稳定 ID 去重，无重复。

点击每行的“正式词条”查看中英文描述、功能、环境要求、使用限制、入门步骤和来源。本表保留筛选时的 Star 与活动快照。正式词条另记录入库时重新获取的 Star 快照，因此数值可能略有差异。

筛选条件：

- 与 AI 相关，且能帮助 AI 完成任务。用途依据各仓库官方 README。
- 活动窗口为 **2026-08-17 至 2026-11-17**，截至各项核验时间。文档和机器人提交也计入活动。
- Star 总数 **≥ 1,000**，或近 1 个日历月净增 **≥ 500**。本表 100 项均满足总量条件，最低为 **3,862** Star，因此没有采集或推断月增长。
- 许可不作为筛选门槛。

本次通过 GitHub 搜索及主题补充发现项目，再读取官方元数据、README 和具体活动。清单兼顾任务类型，不是全站排名。仅核对文档和公开记录，未安装或运行上游软件。

活动证据包含 93 条 commit、5 条 PR 创建记录和 2 条 issue 创建记录。PR 和 issue 只证明发生了活动，不代表功能已合并或问题已修复。表内日期统一为 UTC；精确时间、提交标题、稳定 ID 和 Star 数据源见 JSON。

## 按任务浏览

| 用途 | 数量 |
| --- | ---: |
| [智能体与工作流](#group-1) | 15 |
| [编码与工具接入](#group-2) | 8 |
| [浏览器与网页采集](#group-3) | 6 |
| [文档与知识检索](#group-4) | 16 |
| [记忆与上下文](#group-5) | 3 |
| [结构化输出与模型网关](#group-6) | 4 |
| [评测与可观测](#group-7) | 9 |
| [模型推理与服务](#group-8) | 5 |
| [模型开发与训练](#group-9) | 11 |
| [AI 应用与交互](#group-10) | 10 |
| [图像、视频与 3D](#group-11) | 6 |
| [语音识别与合成](#group-12) | 7 |

<a id="group-1"></a>

## 智能体与工作流（15）

| 序号 | 仓库 | 简述与 AI 用途 | Star | 近期活动（UTC） |
| ---: | --- | --- | ---: | --- |
| 1 | [activepieces/activepieces](https://github.com/activepieces/activepieces) · [正式词条](../docs/activepieces.md#中文) · [文档](https://github.com/activepieces/activepieces/blob/main/README.md) | 用 TypeScript 集成组件和可视化流程构建 AI 自动化。组件可作为 MCP 工具供模型调用，并支持分支、重试和人工审批。 | 25,581 | [2026-11-17 · commit](https://github.com/activepieces/activepieces/commit/0f039962c863915544219ccf4ec60cec5091e4d7) |
| 2 | [Agenta-AI/agenta](https://github.com/Agenta-AI/agenta) · [正式词条](../docs/agenta.md#中文) · [文档](https://github.com/Agenta-AI/agenta/blob/main/README.md) | 通过对话配置团队智能体，连接应用，并按计划或事件执行任务。给 AI 提供应用工具、浏览器、共享文件和权限控制，完成团队运营与文档任务。 | 4,915 | [2026-11-13 · commit](https://github.com/Agenta-AI/agenta/commit/8d6f0dff68eab619a4b5ae32970c342f005df74e) |
| 3 | [agno-agi/agno](https://github.com/agno-agi/agno) · [正式词条](../docs/agno.md#中文) · [文档](https://github.com/agno-agi/agno/blob/main/README.md) | 将智能体、团队和工作流部署为带 API、MCP、存储及调度能力的服务。为 AI 配置知识、记忆、工具和任务编排，并让其持续执行组织内的工作。 | 43,215 | [2026-11-17 · commit](https://github.com/agno-agi/agno/commit/8b5ce9f85812519a2452ff47981964b202e23828) |
| 4 | [bytedance/deer-flow](https://github.com/bytedance/deer-flow) · [正式词条](../docs/deer-flow.md#中文) · [文档](https://github.com/bytedance/deer-flow/blob/main/README.md) | 组合子智能体、记忆、技能和沙箱执行较长的任务。适合研究、编程和内容制作，能够把复杂工作拆成多个执行步骤。 | 85,439 | [2026-11-17 · commit](https://github.com/bytedance/deer-flow/commit/3751eb8daf491324e728f63bcc773e0f081eb7e5) |
| 5 | [crewAIInc/crewAI](https://github.com/crewAIInc/crewAI) · [正式词条](../docs/crewai.md#中文) · [文档](https://github.com/crewAIInc/crewAI/blob/main/README.md) | 以角色化 Agent 协作和事件驱动流程组织多步骤工作。可将研究、工具调用和结果整理分配给多个智能体，并控制任务流程。 | 61,024 | [2026-11-16 · commit](https://github.com/crewAIInc/crewAI/commit/96c4d85b6423dd06b7f1c38f12dd472399c6ce43) |
| 6 | [evalstate/fast-agent](https://github.com/evalstate/fast-agent) · [正式词条](../docs/fast-agent.md#中文) · [文档](https://github.com/evalstate/fast-agent/blob/main/README.md) | 提供终端智能体、技能、MCP 连接、Shell 工具和多模型工作流。把提示、MCP 服务和执行工具组合成 AI 任务流程，并用回放模型辅助开发与评测。 | 3,972 | [2026-11-16 · commit](https://github.com/evalstate/fast-agent/commit/fed14e0d96e9c4a965dd93a918ebe6c28a5df010) |
| 7 | [huggingface/smolagents](https://github.com/huggingface/smolagents) · [正式词条](../docs/smolagents.md#中文) · [文档](https://github.com/huggingface/smolagents/blob/main/README.md) | 让智能体用代码表达操作，支持多种模型、MCP 工具和沙箱执行环境。使 AI 编写并运行任务代码，组合搜索或其他工具来完成多步工作。 | 30,403 | [2026-11-17 · commit](https://github.com/huggingface/smolagents/commit/8469d427d08655209a5a5e26242dba759b213206) |
| 8 | [langchain-ai/langchain](https://github.com/langchain-ai/langchain) · [正式词条](../docs/langchain.md#中文) · [文档](https://github.com/langchain-ai/langchain/blob/master/README.md) | 用模型、工具及外部集成组件构建 Agent 和 LLM 应用。帮助 AI 连接数据源和业务工具，并组合调用过程。 | 149,765 | [2026-11-16 · commit](https://github.com/langchain-ai/langchain/commit/92c7defb0ac54ca2be18fca1bcf89cc88d9356c6) |
| 9 | [langchain-ai/langgraph](https://github.com/langchain-ai/langgraph) · [正式词条](../docs/langgraph.md#中文) · [文档](https://github.com/langchain-ai/langgraph/blob/main/README.md) | 构建具有状态、持久执行和人工介入能力的 Agent 工作流。适合需要恢复执行、分支控制和长期状态的多步骤 AI 任务。 | 45,066 | [2026-11-16 · commit](https://github.com/langchain-ai/langgraph/commit/02f2c2e6c992ffccce9e9129781fdd04f015c6fa) |
| 10 | [langflow-ai/langflow](https://github.com/langflow-ai/langflow) · [正式词条](../docs/langflow.md#中文) · [文档](https://github.com/langflow-ai/langflow/blob/main/README.md) | 以可视化组件构建 Agent 和工作流，并提供 API 与 MCP 服务入口。把模型、向量数据库和工具组成可复用的 AI 功能。 | 156,718 | [2026-11-16 · commit](https://github.com/langflow-ai/langflow/commit/86fde091f88a8b40507512d36ed78b5917dc165e) |
| 11 | [langgenius/dify](https://github.com/langgenius/dify) · [正式词条](../docs/dify.md#中文) · [文档](https://github.com/langgenius/dify/blob/main/README.md) | 通过可视化工作区构建 AI 流程、RAG 管线和 Agent 应用。为 AI 连接模型、知识库与工具，并管理应用的部署和运行记录。 | 161,349 | [2026-11-17 · commit](https://github.com/langgenius/dify/commit/39addda308deb3f24885bc1e5ebaa6f160f2f492) |
| 12 | [n8n-io/n8n](https://github.com/n8n-io/n8n) · [正式词条](../docs/n8n.md#中文) · [文档](https://github.com/n8n-io/n8n/blob/master/README.md) | 把可视化流程、自定义代码、业务集成和 AI Agent 组合起来。帮助 AI 调用业务系统、处理数据，并在多步骤流程中接入人工审批。 | 210,777 | [2026-11-17 · commit](https://github.com/n8n-io/n8n/commit/12360b360184edb4f2fe96a3fd7e002e398e42f7) |
| 13 | [openai/openai-agents-python](https://github.com/openai/openai-agents-python) · [正式词条](../docs/openai-agents-python.md#中文) · [文档](https://github.com/openai/openai-agents-python/blob/main/README.md) | 提供多智能体工作流、工具调用、交接、追踪和语音交互组件。用于构建由多个 Agent 协作、可检查执行过程的应用。 | 30,735 | [2026-11-17 · commit](https://github.com/openai/openai-agents-python/commit/9e05bd5bf299a5ddbb25f7fec8da10bf2baf6133) |
| 14 | [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai) · [正式词条](../docs/pydantic-ai.md#中文) · [文档](https://github.com/pydantic/pydantic-ai/blob/main/README.md) | 提供有类型的智能体循环、工具调用、持久执行、评测和多模型接口。用类型校验、工具能力和任务状态管理构建可执行长任务的 AI 智能体。 | 21,254 | [2026-11-17 · commit](https://github.com/pydantic/pydantic-ai/commit/89287c2c53431e2615859134d44b0006f29fb0ba) |
| 15 | [stanfordnlp/dspy](https://github.com/stanfordnlp/dspy) · [正式词条](../docs/dspy.md#中文) · [文档](https://github.com/stanfordnlp/dspy/blob/main/README.md) | 用模块化程序组织语言模型调用，并优化提示词与模型参数。构建和优化分类、RAG 与智能体流程。 | 39,108 | [2026-11-12 · commit](https://github.com/stanfordnlp/dspy/commit/2c07ebbee3a66f6e04b71e141c6c198f1b31a129) |

<a id="group-2"></a>

## 编码与工具接入（8）

| 序号 | 仓库 | 简述与 AI 用途 | Star | 近期活动（UTC） |
| ---: | --- | --- | ---: | --- |
| 16 | [e2b-dev/E2B](https://github.com/e2b-dev/E2B) · [正式词条](../docs/e2b.md#中文) · [文档](https://github.com/e2b-dev/E2B/blob/main/README.md) | 通过 Python 或 JavaScript SDK 管理隔离的代码执行环境。为 Agent 执行生成代码、处理文件和调用桌面工具提供运行环境。 | 14,905 | [2026-11-16 · commit](https://github.com/e2b-dev/E2B/commit/c4bab34e85a82cf55bbec5ce89d91d1abf299b1a) |
| 17 | [github/github-mcp-server](https://github.com/github/github-mcp-server) · [正式词条](../docs/github-mcp-server.md#中文) · [文档](https://github.com/github/github-mcp-server/blob/main/README.md) | GitHub 官方 MCP 服务，为智能体提供仓库、代码、Issue、PR 和工作流接口。让 AI 读取代码、分析提交、管理工作项并检查 CI，完成开发协作任务。 | 34,544 | [2026-11-16 · commit](https://github.com/github/github-mcp-server/commit/67d4dc489700ec955ad255d098396dd86c729523) |
| 18 | [letta-ai/letta-code](https://github.com/letta-ai/letta-code) · [正式词条](../docs/letta-code.md#中文) · [文档](https://github.com/letta-ai/letta-code/blob/main/README.md) | 具有持久记忆、技能和身份状态的智能体运行工具，支持终端及远程使用。让 AI 在多轮编码任务间保留项目上下文，并执行工具操作；按当前 letta-code 仓库独立核验。 | 3,862 | [2026-11-17 · commit](https://github.com/letta-ai/letta-code/commit/b622fb1bc0941981e08da5ec2b2736d897e9bde1) |
| 19 | [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers) · [正式词条](../docs/servers.md#中文) · [文档](https://github.com/modelcontextprotocol/servers/blob/main/README.md) | MCP 官方参考服务集合，演示如何向模型提供工具和数据访问接口。可用来开发 Agent 的工具连接层；这些是参考实现，部署前需补齐自身场景要求。 | 92,064 | [2026-11-11 · commit](https://github.com/modelcontextprotocol/servers/commit/e1dc4b18dbb948921da37f3d4224a628730b43b0) |
| 20 | [open-webui/mcpo](https://github.com/open-webui/mcpo) · [正式词条](../docs/mcpo.md#中文) · [文档](https://github.com/open-webui/mcpo/blob/main/README.md) | 将 MCP 服务代理为 OpenAPI HTTP 接口，并生成工具 API 文档。让使用 OpenAPI 工具接口的 AI 应用复用 MCP 服务，适合连接 Open WebUI 等客户端。 | 4,429 | [2026-11-04 · issue 创建](https://github.com/open-webui/mcpo/issues/318) |
| 21 | [openai/codex](https://github.com/openai/codex) · [正式词条](../docs/codex.md#中文) · [文档](https://github.com/openai/codex/blob/main/README.md) | 在终端运行的编码智能体，可接入代码编辑器并围绕本地工程开展工作。让 AI 阅读代码、修改文件、执行命令和验证结果，完成开发与排错任务。 | 135,635 | [2026-11-17 · commit](https://github.com/openai/codex/commit/49d657aad0e878fb7ab156b91126828c21a0005f) |
| 22 | [PrefectHQ/fastmcp](https://github.com/PrefectHQ/fastmcp) · [正式词条](../docs/fastmcp.md#中文) · [文档](https://github.com/PrefectHQ/fastmcp/blob/main/README.md) | 用 Python 构建 MCP 服务端、客户端和交互应用，自动生成工具定义与校验。将业务函数和数据封装为 AI 可调用的工具，并处理 MCP 连接、认证及协议交互。 | 28,616 | [2026-11-17 · commit](https://github.com/PrefectHQ/fastmcp/commit/10083f77731f90ba6191f0a8d2c23d9adf0aacce) |
| 23 | [tadata-org/fastapi_mcp](https://github.com/tadata-org/fastapi_mcp) · [正式词条](../docs/fastapi-mcp.md#中文) · [文档](https://github.com/tadata-org/fastapi_mcp/blob/main/README.md) | 把 FastAPI 路由转换为 MCP 工具，保留模型结构、说明和现有依赖认证。使 AI 调用既有业务 API；仓库有路径参数编码问题报告，部署前需核对该问题处理状态。 [问题报告](https://github.com/tadata-org/fastapi_mcp/issues/354) | 12,029 | [2026-11-16 · PR 创建](https://github.com/tadata-org/fastapi_mcp/pull/360) |

<a id="group-3"></a>

## 浏览器与网页采集（6）

| 序号 | 仓库 | 简述与 AI 用途 | Star | 近期活动（UTC） |
| ---: | --- | --- | ---: | --- |
| 24 | [browser-use/browser-use](https://github.com/browser-use/browser-use) · [正式词条](../docs/browser-use.md#中文) · [文档](https://github.com/browser-use/browser-use/blob/main/README.md) | 让模型在真实浏览器中用 Python 和浏览器工具执行任务。适合跨页面浏览、信息提取和网页操作；本地库与托管服务是不同使用入口。 | 121,289 | [2026-11-17 · commit](https://github.com/browser-use/browser-use/commit/197972b206d3a6ec9fb30afcf76149c07fb8ee61) |
| 25 | [browserbase/stagehand](https://github.com/browserbase/stagehand) · [正式词条](../docs/stagehand.md#中文) · [文档](https://github.com/browserbase/stagehand/blob/main/README.md) | 提供浏览器交互与结构化数据提取 SDK，并配有面向编码智能体的 CLI。让 AI 按页面上下文操作网站，复用登录会话和可检查的浏览器步骤。 | 26,077 | [2026-11-17 · commit](https://github.com/browserbase/stagehand/commit/0f9a64c141d929b0595b4d909d89fb02e37c1ca4) |
| 26 | [ChromeDevTools/chrome-devtools-mcp](https://github.com/ChromeDevTools/chrome-devtools-mcp) · [正式词条](../docs/chrome-devtools-mcp.md#中文) · [文档](https://github.com/ChromeDevTools/chrome-devtools-mcp/blob/main/README.md) | 让编码智能体控制 Chrome，并读取调试和性能信息。帮助 AI 检查页面行为、定位前端错误和分析运行性能。 | 57,942 | [2026-11-17 · commit](https://github.com/ChromeDevTools/chrome-devtools-mcp/commit/ec0abfc80568b9585299d739debb8869fabd710f) |
| 27 | [firecrawl/firecrawl](https://github.com/firecrawl/firecrawl) · [正式词条](../docs/firecrawl.md#中文) · [文档](https://github.com/firecrawl/firecrawl/blob/main/README.md) | 提供网页搜索、抓取、交互和文档解析接口。向 Agent 提供网页上下文，例如 Markdown、结构化 JSON 与截图。 | 202,506 | [2026-11-17 · commit](https://github.com/firecrawl/firecrawl/commit/8e7e5887cfd69e1db2d3f16be22a642a02370aec) |
| 28 | [microsoft/playwright-mcp](https://github.com/microsoft/playwright-mcp) · [正式词条](../docs/playwright-mcp.md#中文) · [文档](https://github.com/microsoft/playwright-mcp/blob/main/README.md) | 通过 MCP 把浏览器导航、交互和页面结构读取交给 AI。适合网页操作、探索式测试与表单流程，主要使用可访问性快照。 | 39,778 | [2026-11-16 · commit](https://github.com/microsoft/playwright-mcp/commit/a62ea28698af6d9bc89438bcec50c63377cef957) |
| 29 | [unclecode/crawl4ai](https://github.com/unclecode/crawl4ai) · [正式词条](../docs/crawl4ai.md#中文) · [文档](https://github.com/unclecode/crawl4ai/blob/main/README.md) | 提供可自行部署的爬取器，也有托管的网页抓取与搜索接口。帮助 AI 从网页获取干净文本和结构化数据，用于 RAG 或信息整理。 | 87,468 | [2026-11-17 · commit](https://github.com/unclecode/crawl4ai/commit/bf0c7925e21992af972039672fecd8e85163b575) |

<a id="group-4"></a>

## 文档与知识检索（16）

| 序号 | 仓库 | 简述与 AI 用途 | Star | 近期活动（UTC） |
| ---: | --- | --- | ---: | --- |
| 30 | [chroma-core/chroma](https://github.com/chroma-core/chroma) · [正式词条](../docs/chroma.md#中文) · [文档](https://github.com/chroma-core/chroma/blob/main/README.md) | 管理文档、嵌入和元数据的 AI 数据基础设施，提供集合与查询接口。快速建立 RAG 原型，按语义相似度和元数据检索文档。 | 29,704 | [2026-11-07 · commit](https://github.com/chroma-core/chroma/commit/1a3ac2c7c623adbd03ed2508dc27b98cdf26016d) |
| 31 | [deepset-ai/haystack](https://github.com/deepset-ai/haystack) · [正式词条](../docs/haystack.md#中文) · [文档](https://github.com/deepset-ai/haystack/blob/main/README.md) | 用可组合流水线和智能体工作流组织检索、路由、记忆与生成。开发可定制的 RAG、语义搜索与问答应用。 | 27,027 | [2026-11-17 · commit](https://github.com/deepset-ai/haystack/commit/2b85450acc16c28f6069ed3644f0eed31c76c249) |
| 32 | [docling-project/docling](https://github.com/docling-project/docling) · [正式词条](../docs/docling.md#中文) · [文档](https://github.com/docling-project/docling/blob/main/README.md) | 解析多种资料并提取结构化内容，例如 PDF、Office、网页、图像和音频。为生成式 AI 和 RAG 准备文档，处理版面、阅读顺序和表格结构。 | 70,693 | [2026-11-17 · commit](https://github.com/docling-project/docling/commit/48f272b99c90616222901a0f3ee73bf367d0c592) |
| 33 | [facebookresearch/faiss](https://github.com/facebookresearch/faiss) · [正式词条](../docs/faiss.md#中文) · [文档](https://github.com/facebookresearch/faiss/blob/main/README.md) | 提供稠密向量相似度搜索、索引与聚类算法的库。为嵌入召回构建 CPU 或 GPU 索引，并比较检索参数。 | 41,766 | [2026-11-16 · commit](https://github.com/facebookresearch/faiss/commit/c8f283867285af547db7a701c1b8dfa89631b3ea) |
| 34 | [HKUDS/LightRAG](https://github.com/HKUDS/LightRAG) · [正式词条](../docs/lightrag.md#中文) · [文档](https://github.com/HKUDS/LightRAG/blob/main/README.md) | 结合知识图谱与向量嵌入的 RAG 框架，支持文档增量更新。构建兼顾实体关系与语义召回的知识问答系统。 | 40,740 | [2026-11-17 · commit](https://github.com/HKUDS/LightRAG/commit/2ecced370abaca1a73364733ba13f737fa97d476) |
| 35 | [huggingface/sentence-transformers](https://github.com/huggingface/sentence-transformers) · [正式词条](../docs/sentence-transformers.md#中文) · [文档](https://github.com/huggingface/sentence-transformers/blob/main/README.md) | 计算和训练向量嵌入、重排序、稀疏编码与多向量检索模型。为语义搜索和 RAG 构建召回、相似度评分与重排序能力。 | 19,289 | [2026-11-17 · commit](https://github.com/huggingface/sentence-transformers/commit/ea66116aeea5e827963bedaa0c38ed4a4681229a) |
| 36 | [infiniflow/ragflow](https://github.com/infiniflow/ragflow) · [正式词条](../docs/ragflow.md#中文) · [文档](https://github.com/infiniflow/ragflow/blob/main/README.md) | 结合文档解析、知识组织、检索和智能体能力的 RAG 引擎。把复杂文档转成知识库，为问答和智能体提供上下文。 | 94,304 | [2026-11-17 · commit](https://github.com/infiniflow/ragflow/commit/cbffd01860ba441acb2c2d5c472c64f4a8a118d4) |
| 37 | [lancedb/lancedb](https://github.com/lancedb/lancedb) · [正式词条](../docs/lancedb.md#中文) · [文档](https://github.com/lancedb/lancedb/blob/main/README.md) | 基于 Lance 列式格式管理向量、多模态数据与版本的数据库。把向量检索、全文检索和数据分析用于 AI 应用。 | 11,913 | [2026-11-17 · commit](https://github.com/lancedb/lancedb/commit/1670859327d5503e8bf7e02c58f93260da4881b4) |
| 38 | [microsoft/markitdown](https://github.com/microsoft/markitdown) · [正式词条](../docs/markitdown.md#中文) · [文档](https://github.com/microsoft/markitdown/blob/main/README.md) | 把 Office、PDF 及多种文件转换成适合文本处理的 Markdown。为 LLM 阅读和分析资料保留文档结构，例如标题、列表与表格。 | 195,964 | [2026-11-07 · commit](https://github.com/microsoft/markitdown/commit/ed178952a6672abdfd35b5f9e76a80b6cefc086e) |
| 39 | [milvus-io/milvus](https://github.com/milvus-io/milvus) · [正式词条](../docs/milvus.md#中文) · [文档](https://github.com/milvus-io/milvus/blob/master/README.md) | 面向大规模向量的数据库，支持元数据过滤、混合检索和分布式部署。保存模型生成的嵌入，为 RAG 和语义搜索提供检索服务。 | 46,677 | [2026-11-17 · commit](https://github.com/milvus-io/milvus/commit/663f0d57407a489030b94e986ea60ad615b930d1) |
| 40 | [opendatalab/MinerU](https://github.com/opendatalab/MinerU) · [正式词条](../docs/mineru.md#中文) · [文档](https://github.com/opendatalab/MinerU/blob/master/README.md) | 把复杂 PDF、扫描件和 Office 文件解析为 Markdown 或 JSON。帮助 Agent 读取文档、OCR、定位页面内容并保留可引用的段落位置。 | 83,800 | [2026-11-16 · commit](https://github.com/opendatalab/MinerU/commit/b4efa4b2b76ebb012c476b79bdfc6f18a95aacd6) |
| 41 | [PaddlePaddle/PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR) · [正式词条](../docs/paddleocr.md#中文) · [文档](https://raw.githubusercontent.com/PaddlePaddle/PaddleOCR/main/README.md) | 识别图像和 PDF 中的文字、表格与公式，并把文档结构转换为 Markdown 或 JSON。为语言模型和 RAG 流程提取文档内容，将扫描件与复杂版式转为可检索的结构化输入。 | 92,802 | [2026-09-16 · commit](https://github.com/PaddlePaddle/PaddleOCR/commit/dab3fe35379033fdcb2d0e9572fac0b36c9a9ebf) |
| 42 | [qdrant/qdrant](https://github.com/qdrant/qdrant) · [正式词条](../docs/qdrant.md#中文) · [文档](https://github.com/qdrant/qdrant/blob/master/README.md) | 存储向量及其附加数据，提供相似度搜索和细粒度过滤。将嵌入模型接入检索、匹配和推荐应用。 | 35,604 | [2026-11-16 · commit](https://github.com/qdrant/qdrant/commit/23065a0bf6857c3e5da45f6c8939cc746cc0580e) |
| 43 | [run-llama/llama_index](https://github.com/run-llama/llama_index) · [正式词条](../docs/llama-index.md#中文) · [文档](https://github.com/run-llama/llama_index/blob/main/README.md) | 用于构建 RAG 和智能体应用的开放编排框架。连接文档与语言模型，组织数据检索和智能体应用流程。 | 52,925 | [2026-11-14 · commit](https://github.com/run-llama/llama_index/commit/99d7433f6f71888951379ccca9294e272442c832) |
| 44 | [Unstructured-IO/unstructured](https://github.com/Unstructured-IO/unstructured) · [正式词条](../docs/unstructured.md#中文) · [文档](https://raw.githubusercontent.com/Unstructured-IO/unstructured/main/README.md) | 解析非结构化材料，例如 PDF、HTML、Word 和图像。提供文档分区和预处理组件。把原始文档转为语言模型可使用的结构化片段，为检索、总结和数据准备提供输入。 | 15,755 | [2026-11-17 · commit](https://github.com/Unstructured-IO/unstructured/commit/0c166fc21b65de8d398ff3ba13976882266916a4) |
| 45 | [weaviate/weaviate](https://github.com/weaviate/weaviate) · [正式词条](../docs/weaviate.md#中文) · [文档](https://github.com/weaviate/weaviate/blob/main/README.md) | 结合向量搜索、关键词过滤、RAG 与重排序的向量数据库。构建语义检索与知识问答，使用自带或外部嵌入模型。 | 16,952 | [2026-11-17 · commit](https://github.com/weaviate/weaviate/commit/a33c0ef138d41eef14247aba4fd70d63c007ee88) |

<a id="group-5"></a>

## 记忆与上下文（3）

| 序号 | 仓库 | 简述与 AI 用途 | Star | 近期活动（UTC） |
| ---: | --- | --- | ---: | --- |
| 46 | [getzep/graphiti](https://github.com/getzep/graphiti) · [正式词条](../docs/graphiti.md#中文) · [文档](https://github.com/getzep/graphiti/blob/main/README.md) | 构建保留时间与来源信息的上下文图谱，支持语义、关键词和图遍历检索。帮助 AI 查询人物、事件和关系随时间的变化，为持续任务补充可追溯上下文。 | 32,877 | [2026-11-15 · commit](https://github.com/getzep/graphiti/commit/869c1b279e01a2767a464581e1cb657ce0e39271) |
| 47 | [mem0ai/mem0](https://github.com/mem0ai/mem0) · [正式词条](../docs/mem0.md#中文) · [文档](https://github.com/mem0ai/mem0/blob/main/README.md) | 为智能体和应用提取、保存并检索用户、会话和任务记忆。让 AI 在后续任务中复用用户偏好和历史事实，降低跨会话重复说明；托管版与开源 SDK 能力不同。 | 69,106 | [2026-11-06 · commit](https://github.com/mem0ai/mem0/commit/f1791daa86d469249c9b002f62644d58a1eb96a0) |
| 48 | [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) · [正式词条](../docs/supermemory.md#中文) · [文档](https://github.com/supermemoryai/supermemory/blob/main/README.md) | 提供记忆与上下文接口、助手插件和 MCP 接入，用于提取事实和检索历史。让编码助手与应用在不同会话中检索项目背景、偏好和已完成的讨论。 | 31,641 | [2026-11-16 · commit](https://github.com/supermemoryai/supermemory/commit/fb105722a4a86b0e4010c09851c83fb93655b121) |

<a id="group-6"></a>

## 结构化输出与模型网关（4）

| 序号 | 仓库 | 简述与 AI 用途 | Star | 近期活动（UTC） |
| ---: | --- | --- | ---: | --- |
| 49 | [567-labs/instructor](https://github.com/567-labs/instructor) · [正式词条](../docs/instructor.md#中文) · [文档](https://github.com/567-labs/instructor/blob/main/README.md) | 基于 Pydantic 将模型响应解析为有类型的数据，并处理校验失败和重试。让 AI 从文本提取可验证的结构化字段，便于后续工具调用、表单和数据处理。 | 14,117 | [2026-11-15 · commit](https://github.com/567-labs/instructor/commit/1e85ddf38807084182aeefb5bb67f4deee821163) |
| 50 | [dottxt-ai/outlines](https://github.com/dottxt-ai/outlines) · [正式词条](../docs/outlines.md#中文) · [文档](https://github.com/dottxt-ai/outlines/blob/main/README.md) | 用 Python 类型、Pydantic 模型和约束生成定义语言模型输出结构。把 AI 输出约束为分类标签、数字或 JSON 对象，减少任务流水线中的格式解析失败。 | 16,012 | [2026-08-24 · commit](https://github.com/dottxt-ai/outlines/commit/c52af8472c6fe8a607a733ec11b709476af77a96) |
| 51 | [guidance-ai/guidance](https://github.com/guidance-ai/guidance) · [正式词条](../docs/guidance.md#中文) · [文档](https://github.com/guidance-ai/guidance/blob/main/README.md) | 在 Python 中组合生成、条件和循环，并使用正则或语法约束输出。让 AI 按任务要求生成受约束的数据和文本，支持工具使用与分步控制；能力依赖模型后端。 | 21,825 | [2026-11-05 · PR 创建](https://github.com/guidance-ai/guidance/pull/1559) |
| 52 | [Portkey-AI/gateway](https://github.com/Portkey-AI/gateway) · [正式词条](../docs/gateway.md#中文) · [文档](https://github.com/Portkey-AI/gateway/blob/main/README.md) | 为多家模型提供统一调用接口、条件路由、重试、回退和护栏。让 AI 工作流在模型供应商之间切换，并在调用失败时重试或选择后备模型。 | 13,390 | [2026-11-16 · PR 创建](https://github.com/Portkey-AI/gateway/pull/1903) |

<a id="group-7"></a>

## 评测与可观测（9）

| 序号 | 仓库 | 简述与 AI 用途 | Star | 近期活动（UTC） |
| ---: | --- | --- | ---: | --- |
| 53 | [Arize-ai/phoenix](https://github.com/Arize-ai/phoenix) · [正式词条](../docs/phoenix.md#中文) · [文档](https://github.com/Arize-ai/phoenix/blob/main/README.md) | 提供 OpenTelemetry 追踪、数据集、实验和提示管理，并支持 MCP 查询。让编码智能体读取执行轨迹、数据集和实验结果，辅助排查与改进 AI 工作流。 | 12,325 | [2026-11-17 · commit](https://github.com/Arize-ai/phoenix/commit/8b409d4531cda2844d5f172119835cfe43ab8a9b) |
| 54 | [confident-ai/deepeval](https://github.com/confident-ai/deepeval) · [正式词条](../docs/deepeval.md#中文) · [文档](https://github.com/confident-ai/deepeval/blob/main/README.md) | 面向 LLM 应用的测试框架，评估回答、检索和智能体执行轨迹。将质量评测加入应用测试流程，比较模型、提示词和架构。 | 19,525 | [2026-11-16 · commit](https://github.com/confident-ai/deepeval/commit/c0bd9c89f33853b2dedc7db8415b3036894fb204) |
| 55 | [EleutherAI/lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) · [正式词条](../docs/lm-evaluation-harness.md#中文) · [文档](https://github.com/EleutherAI/lm-evaluation-harness/blob/main/README.md) | 用统一接口在多类基准任务上测试生成式语言模型。复用公开任务、提示词和指标，比较模型及适配器表现。 | 14,492 | [2026-09-14 · commit](https://github.com/EleutherAI/lm-evaluation-harness/commit/d6de81643928d653435c431bae19945d41d32520) |
| 56 | [Helicone/helicone](https://github.com/Helicone/helicone) · [正式词条](../docs/helicone.md#中文) · [文档](https://github.com/Helicone/helicone/blob/main/README.md) | 结合模型网关、请求日志、会话分析和提示版本管理的 LLM 平台。为智能体选择模型、处理路由回退，并追踪任务中的成本、延迟和请求结果。 | 6,286 | [2026-11-17 · commit](https://github.com/Helicone/helicone/commit/5a21c3a1be183c684b49136eb5abc5e95ed6ba26) |
| 57 | [langfuse/langfuse](https://github.com/langfuse/langfuse) · [正式词条](../docs/langfuse.md#中文) · [文档](https://github.com/langfuse/langfuse/blob/main/README.md) | 汇集模型调用、智能体轨迹、提示版本和评测结果的 AI 工程平台。为 AI 应用记录工具调用与检索过程，帮助定位失败步骤、比较提示版本和监测成本。 | 37,546 | [2026-11-17 · commit](https://github.com/langfuse/langfuse/commit/364223f2fba19695491d5ae54b5ab6f2e911b7a1) |
| 58 | [langwatch/langwatch](https://github.com/langwatch/langwatch) · [正式词条](../docs/langwatch.md#中文) · [文档](https://github.com/langwatch/langwatch/blob/main/README.md) | 统一查看智能体轨迹、模拟测试、编码助手会话和模型网关用量。用模拟对话测试 AI 任务流程，定位失败调用，并限制智能体模型调用预算。 | 5,042 | [2026-11-17 · commit](https://github.com/langwatch/langwatch/commit/396d2727b93e08cd4aec407dbadba2ecbc6afec5) |
| 59 | [open-compass/opencompass](https://github.com/open-compass/opencompass) · [正式词条](../docs/opencompass.md#中文) · [文档](https://github.com/open-compass/opencompass/blob/main/README.md) | 统一模型与数据配置、推理、评测和结果汇总的模型评测平台。比较本地或 API 模型的知识、推理、代码和多模态能力。 | 7,599 | [2026-11-11 · commit](https://github.com/open-compass/opencompass/commit/8b4193ff01cfbdb870a573330b2b199e20242bba) |
| 60 | [promptfoo/promptfoo](https://github.com/promptfoo/promptfoo) · [正式词条](../docs/promptfoo.md#中文) · [文档](https://github.com/promptfoo/promptfoo/blob/main/README.md) | 用配置和命令行比较提示与模型，执行评测、红队测试和 CI 检查。验证 AI 的回答与工具流程是否达到预期，把回归用例和安全测试纳入开发流程。 | 27,370 | [2026-11-17 · commit](https://github.com/promptfoo/promptfoo/commit/9a7187a33b53277295151cc20d24cf96fa0d5cfb) |
| 61 | [vibrantlabsai/ragas](https://github.com/vibrantlabsai/ragas) · [正式词条](../docs/ragas.md#中文) · [文档](https://github.com/vibrantlabsai/ragas/blob/main/README.md) | 为 LLM 应用提供评测指标、测试数据生成和反馈分析工具。评估 RAG 与模型输出质量，并建立可重复的测试数据。 | 16,354 | [2026-11-14 · commit](https://github.com/vibrantlabsai/ragas/commit/8c63f10d500c44efbf24fdb9e2920de2104c321c) |

<a id="group-8"></a>

## 模型推理与服务（5）

| 序号 | 仓库 | 简述与 AI 用途 | Star | 近期活动（UTC） |
| ---: | --- | --- | ---: | --- |
| 62 | [bitsandbytes-foundation/bitsandbytes](https://github.com/bitsandbytes-foundation/bitsandbytes) · [正式词条](../docs/bitsandbytes.md#中文) · [文档](https://github.com/bitsandbytes-foundation/bitsandbytes/blob/main/README.md) | 提供低比特量化、8 位优化器和 4 位线性层的 PyTorch 扩展。降低模型推理和 QLoRA 微调的显存需求。 | 8,543 | [2026-10-27 · commit](https://github.com/bitsandbytes-foundation/bitsandbytes/commit/a616886cacf86701514f0cb1d6be760f967481c0) |
| 63 | [InternLM/lmdeploy](https://github.com/InternLM/lmdeploy) · [正式词条](../docs/lmdeploy.md#中文) · [文档](https://github.com/InternLM/lmdeploy/blob/main/README.md) | 集成大模型量化、压缩、部署与服务的工具链。把语言或视觉语言模型部署为可调用服务，减少推理资源需求。 | 8,149 | [2026-11-17 · commit](https://github.com/InternLM/lmdeploy/commit/fc33f69736ff48c10ad720593b021dcdaedcb80d) |
| 64 | [NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM) · [正式词条](../docs/tensorrt-llm.md#中文) · [文档](https://github.com/NVIDIA/TensorRT-LLM/blob/main/README.md) | 为 NVIDIA GPU 上的大模型和视觉生成模型提供推理内核与运行时。构建、优化和部署模型推理服务。 | 15,084 | [2026-11-17 · commit](https://github.com/NVIDIA/TensorRT-LLM/commit/b63aca8de25fe4989509e97678d968c393255cc6) |
| 65 | [sgl-project/sglang](https://github.com/sgl-project/sglang) · [正式词条](../docs/sglang.md#中文) · [文档](https://github.com/sgl-project/sglang/blob/main/README.md) | 面向语言和多模态模型的推理服务框架，支持批处理、缓存与分布式执行。部署模型 API，支持智能体请求和强化学习 rollout。 | 38,977 | [2026-11-17 · commit](https://github.com/sgl-project/sglang/commit/703e763d5f3af75ea3587275d79155c28d3c5d4f) |
| 66 | [triton-inference-server/server](https://github.com/triton-inference-server/server) · [正式词条](../docs/server.md#中文) · [文档](https://github.com/triton-inference-server/server/blob/main/README.md) | 统一托管多种机器学习框架模型的推理服务器，提供并发执行和动态批处理。为模型部署提供 HTTP/gRPC 接口、模型流水线与运行指标。 | 11,146 | [2026-11-16 · commit](https://github.com/triton-inference-server/server/commit/24af411c99d09cfb60259dceb63a718606148aa2) |

<a id="group-9"></a>

## 模型开发与训练（11）

| 序号 | 仓库 | 简述与 AI 用途 | Star | 近期活动（UTC） |
| ---: | --- | --- | ---: | --- |
| 67 | [axolotl-ai-cloud/axolotl](https://github.com/axolotl-ai-cloud/axolotl) · [正式词条](../docs/axolotl.md#中文) · [文档](https://github.com/axolotl-ai-cloud/axolotl/blob/main/README.md) | 用 YAML 配置组织大模型数据预处理、微调、评测、量化和推理。运行全量微调、LoRA、QLoRA 及分布式后训练。 | 12,735 | [2026-11-13 · commit](https://github.com/axolotl-ai-cloud/axolotl/commit/f2158ff1922b2bcf701854a17e47cc91ba26e7e9) |
| 68 | [deepspeedai/DeepSpeed](https://github.com/deepspeedai/DeepSpeed) · [正式词条](../docs/deepspeed.md#中文) · [文档](https://github.com/deepspeedai/DeepSpeed/blob/master/README.md) | 为大规模深度学习提供 ZeRO、并行训练和内存管理优化。把大型模型训练扩展到多 GPU，并降低训练资源开销。 | 43,331 | [2026-11-17 · commit](https://github.com/deepspeedai/DeepSpeed/commit/fd8be8161176d0359060cc44faa98383382b70d3) |
| 69 | [hiyouga/LlamaFactory](https://github.com/hiyouga/LlamaFactory) · [正式词条](../docs/llamafactory.md#中文) · [文档](https://github.com/hiyouga/LlamaFactory/blob/main/README.md) | 统一多种模型的预训练、监督微调和偏好优化，提供配置与图形入口。以统一流程准备数据、微调模型并部署推理接口。 | 76,082 | [2026-11-17 · commit](https://github.com/hiyouga/LlamaFactory/commit/885a4ca65cebf17a92e869af13c2ce42caca314a) |
| 70 | [huggingface/datasets](https://github.com/huggingface/datasets) · [正式词条](../docs/datasets.md#中文) · [文档](https://github.com/huggingface/datasets/blob/main/README.md) | 加载公开或本地数据集，并提供可复现的数据预处理接口。准备模型训练和评测所需的数据，处理多种文件格式。 | 22,151 | [2026-11-17 · commit](https://github.com/huggingface/datasets/commit/167807008ac3aa96f9b377efde58767e53a7f3b3) |
| 71 | [huggingface/peft](https://github.com/huggingface/peft) · [正式词条](../docs/peft.md#中文) · [文档](https://github.com/huggingface/peft/blob/main/README.md) | 实现 LoRA 等参数高效微调方法，只更新少量参数以适配预训练模型。在较小计算和存储预算下完成模型领域适配。 | 21,900 | [2026-11-17 · commit](https://github.com/huggingface/peft/commit/3a6d5808712f5756aa7b4b02d1619f6887ddc196) |
| 72 | [huggingface/trl](https://github.com/huggingface/trl) · [正式词条](../docs/trl.md#中文) · [文档](https://github.com/huggingface/trl/blob/main/README.md) | 提供基础模型后训练方法及训练器，例如 SFT、GRPO 和 DPO。执行监督微调、偏好优化和强化学习训练。 | 19,750 | [2026-11-17 · commit](https://github.com/huggingface/trl/commit/b2686bf5c300756cdf878b84f83a48f794e2fb94) |
| 73 | [ml-explore/mlx](https://github.com/ml-explore/mlx) · [正式词条](../docs/mlx.md#中文) · [文档](https://github.com/ml-explore/mlx/blob/main/README.md) | 面向 Apple 芯片的机器学习数组框架，提供统一内存、自动微分和模型组件。在 Mac 上实现、训练和运行机器学习模型。 | 29,192 | [2026-11-17 · commit](https://github.com/ml-explore/mlx/commit/fbedcee5f4a0c7b2cbb642ea91d4c555460d3e48) |
| 74 | [ml-explore/mlx-lm](https://github.com/ml-explore/mlx-lm) · [正式词条](../docs/mlx-lm.md#中文) · [文档](https://github.com/ml-explore/mlx-lm/blob/main/README.md) | 基于 MLX 在 Apple 芯片上生成文本、量化和微调大语言模型。在 Mac 上运行模型，执行低秩或全量微调。 | 7,671 | [2026-11-16 · commit](https://github.com/ml-explore/mlx-lm/commit/c4c9c762cc797fd979fc98645f5db5112753bbe9) |
| 75 | [OpenRLHF/OpenRLHF](https://github.com/OpenRLHF/OpenRLHF) · [正式词条](../docs/openrlhf.md#中文) · [文档](https://github.com/OpenRLHF/OpenRLHF/blob/main/README.md) | 结合 Ray、vLLM 与 DeepSpeed 的分布式 RLHF 框架。组织奖励模型、强化学习训练和多轮智能体训练流程。 | 10,161 | [2026-11-03 · commit](https://github.com/OpenRLHF/OpenRLHF/commit/26494490bc237f6c3af62dab6117e6bbb0a78dba) |
| 76 | [pytorch/pytorch](https://github.com/pytorch/pytorch) · [正式词条](../docs/pytorch.md#中文) · [文档](https://github.com/pytorch/pytorch/blob/main/README.md) | 提供 GPU 张量计算、自动微分与神经网络开发的 Python 框架。编写、训练和调试深度学习模型，并扩展自定义算子。 | 105,672 | [2026-11-17 · commit](https://github.com/pytorch/pytorch/commit/6af6987aa3603504c75df85c0906be686e0b8454) |
| 77 | [verl-project/verl](https://github.com/verl-project/verl) · [正式词条](../docs/verl.md#中文) · [文档](https://github.com/verl-project/verl/blob/main/README.md) | 基于 HybridFlow 的大语言模型强化学习训练库，集成训练与推理基础设施。实现和扩展后训练数据流，例如 GRPO 和 PPO。 | 24,263 | [2026-11-17 · commit](https://github.com/verl-project/verl/commit/cc35929bf8eedf5f3eb7c4ace3441dfd9f6d4c0e) |

<a id="group-10"></a>

## AI 应用与交互（10）

| 序号 | 仓库 | 简述与 AI 用途 | Star | 近期活动（UTC） |
| ---: | --- | --- | ---: | --- |
| 78 | [assistant-ui/assistant-ui](https://github.com/assistant-ui/assistant-ui) · [正式词条](../docs/assistant-ui.md#中文) · [文档](https://raw.githubusercontent.com/assistant-ui/assistant-ui/main/README.md) | 为 React 应用提供 AI 聊天组件，支持流式消息、附件、生成式界面及工具审批。将智能体的工具调用呈现为可操作界面，并在需要时收集人的批准或补充输入。 | 13,287 | [2026-11-17 · commit](https://github.com/assistant-ui/assistant-ui/commit/a4c705b08dbe04159c0a10f1cf9e737928d54c3c) |
| 79 | [Chainlit/chainlit](https://github.com/Chainlit/chainlit) · [正式词条](../docs/chainlit.md#中文) · [文档](https://raw.githubusercontent.com/Chainlit/chainlit/main/README.md) | 用 Python 构建对话式 AI 应用，展示消息、工具步骤及交互结果。为智能体提供对话入口和工具执行过程展示，帮助完成需要用户输入与反馈的任务。 | 12,503 | [2026-08-26 · commit](https://github.com/Chainlit/chainlit/commit/190ea74239d9e84b26e7c91bc2882dd038942564) |
| 80 | [CherryHQ/cherry-studio](https://github.com/CherryHQ/cherry-studio) · [正式词条](../docs/cherry-studio.md#中文) · [文档](https://raw.githubusercontent.com/CherryHQ/cherry-studio/main/README.md) | 提供跨平台 AI 工作区，整合多模型、智能体、知识库、图像生成和定时任务。让智能体使用文件、命令、浏览器及 MCP 工具，并结合本地知识库处理日常任务。 | 53,595 | [2026-11-17 · commit](https://github.com/CherryHQ/cherry-studio/commit/195e7f6bf7bdedf5d73ac85ca3f28a39895f295d) |
| 81 | [CopilotKit/CopilotKit](https://github.com/CopilotKit/CopilotKit) · [正式词条](../docs/copilotkit.md#中文) · [文档](https://raw.githubusercontent.com/CopilotKit/CopilotKit/main/README.md) | 把已有智能体接入前端应用，提供聊天、生成式界面、共享状态和人工参与流程。让智能体读取应用状态、展示交互结果并与用户共同完成界面中的多步任务。 | 38,761 | [2026-11-17 · commit](https://github.com/CopilotKit/CopilotKit/commit/d6067175e8fdb365f5671cfdd9aea0c0252cdc8b) |
| 82 | [gradio-app/gradio](https://github.com/gradio-app/gradio) · [正式词条](../docs/gradio.md#中文) · [文档](https://raw.githubusercontent.com/gradio-app/gradio/main/README.md) | 用 Python 为模型、API 或函数创建网页应用。提供聊天、图像和音频交互组件。把 AI 模型能力封装为可交互的应用，让用户提交多模态输入并查看生成结果。 | 44,073 | [2026-11-13 · commit](https://github.com/gradio-app/gradio/commit/ec06278ed72e5eb73494a9d171ca851d553dc82a) |
| 83 | [LibreChat-AI/LibreChat](https://github.com/LibreChat-AI/LibreChat) · [正式词条](../docs/librechat.md#中文) · [文档](https://raw.githubusercontent.com/LibreChat-AI/LibreChat/main/README.md) | 提供多模型对话与智能体工作区，支持 MCP、技能、附件、代码执行和工具权限控制。让智能体读取文件、运行工具和处理多步任务，同时呈现过程并收集执行批准。 | 47,224 | [2026-11-17 · commit](https://github.com/LibreChat-AI/LibreChat/commit/c1d3e2358bf68c33f9f771a6b7b18a31b05b6de1) |
| 84 | [livekit/agents](https://github.com/livekit/agents) · [正式词条](../docs/agents.md#中文) · [文档](https://raw.githubusercontent.com/livekit/agents/main/README.md) | 构建实时语音与多模态智能体，提供模型插件、WebRTC、任务调度、电话与 MCP 接入。让智能体通过语音或电话与用户交互、调用工具，并把结果及时返回会话。 | 15,259 | [2026-11-17 · commit](https://github.com/livekit/agents/commit/0cfc0306335cc8b3633ec2cdce072a3f340cb14e) |
| 85 | [lobehub/lobehub](https://github.com/lobehub/lobehub) · [正式词条](../docs/lobehub.md#中文) · [文档](https://raw.githubusercontent.com/lobehub/lobehub/canary/README.md) | 组织模型、智能体、MCP 和技能，并将智能体接入团队聊天与并行任务工作区。把智能体放入已有团队沟通渠道，提供上下文、工具和协作入口来承接具体工作。 | 85,694 | [2026-11-17 · commit](https://github.com/lobehub/lobehub/commit/88a905b8cf671ee4097db80bc988e153ad545448) |
| 86 | [open-webui/open-webui](https://github.com/open-webui/open-webui) · [正式词条](../docs/open-webui.md#中文) · [文档](https://raw.githubusercontent.com/open-webui/open-webui/main/README.md) | 提供可自行部署的 AI 交互平台，连接 Ollama 和兼容 OpenAI 的本地或云端模型。为模型任务提供统一对话工作区，并可通过配套知识库和终端组件扩展检索与执行能力。 | 158,914 | [2026-11-08 · commit](https://github.com/open-webui/open-webui/commit/b0e6098e940942281d9c83f3529ea117287a3a22) |
| 87 | [pipecat-ai/pipecat](https://github.com/pipecat-ai/pipecat) · [正式词条](../docs/pipecat.md#中文) · [文档](https://raw.githubusercontent.com/pipecat-ai/pipecat/main/README.md) | 用 Python 编排实时语音与多模态智能体，组合识别、模型、合成、传输和多智能体流程。把语音识别、工具调用和语音回复串成实时对话任务，并支持专家智能体交接或并行协作。 | 17,304 | [2026-11-16 · commit](https://github.com/pipecat-ai/pipecat/commit/6203e080683aaaaf49d4f801d75eb22526ee0a68) |

<a id="group-11"></a>

## 图像、视频与 3D（6）

| 序号 | 仓库 | 简述与 AI 用途 | Star | 近期活动（UTC） |
| ---: | --- | --- | ---: | --- |
| 88 | [Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI) · [正式词条](../docs/comfyui.md#中文) · [文档](https://raw.githubusercontent.com/Comfy-Org/ComfyUI/master/README.md) | 用节点工作流组合图像、视频、音频和 3D 内容生成，提供本地运行与 API 接入。让智能体通过 API 调用可复用的生成流程，将提示词和素材转为图像、视频或音频。 | 147,306 | [2026-11-17 · commit](https://github.com/Comfy-Org/ComfyUI/commit/ee34406f56f84f6bc89996b8b77a4bedec98a2b9) |
| 89 | [huggingface/diffusers](https://github.com/huggingface/diffusers) · [正式词条](../docs/diffusers.md#中文) · [文档](https://raw.githubusercontent.com/huggingface/diffusers/main/README.md) | 通过 Python 扩散模型管线、调度器和模型组件完成图像、视频及音频生成与训练。将预训练生成模型接入 AI 应用，用可组合的推理管线执行媒体生成和编辑任务。 | 34,932 | [2026-11-17 · commit](https://github.com/huggingface/diffusers/commit/d9586a3dc62cce5091bdb7cff981d725f4a6dfe5) |
| 90 | [invoke-ai/InvokeAI](https://github.com/invoke-ai/InvokeAI) · [正式词条](../docs/invokeai.md#中文) · [文档](https://raw.githubusercontent.com/invoke-ai/InvokeAI/main/README.md) | 以画布、局部重绘和节点工作流组织 AI 图像创作，并管理模型与生成素材。为图像生成模型提供可反复调整的创作流程，完成局部重绘、扩图和素材迭代。 | 29,105 | [2026-11-17 · commit](https://github.com/invoke-ai/InvokeAI/commit/471bb0f4de2d09efcdfe5d4e0326c1c1ee593f87) |
| 91 | [KlingAIResearch/LivePortrait](https://github.com/KlingAIResearch/LivePortrait) · [正式词条](../docs/liveportrait.md#中文) · [文档](https://raw.githubusercontent.com/KlingAIResearch/LivePortrait/main/readme.md) | 用驱动视频或图像控制人像与动物肖像动画，提供姿态编辑和 Gradio 操作界面。把静态角色素材转成受控的人像动画，作为 AI 视频和虚拟角色制作的生成环节。 | 19,513 | [2026-10-23 · PR 创建](https://github.com/KlingAIResearch/LivePortrait/pull/577) |
| 92 | [mcmonkeyprojects/SwarmUI](https://github.com/mcmonkeyprojects/SwarmUI) · [正式词条](../docs/swarmui.md#中文) · [文档](https://raw.githubusercontent.com/mcmonkeyprojects/SwarmUI/master/README.md) | 提供面向图像、视频和部分音频模型的生成界面，可使用 Comfy 工作流与批量参数工具。把生成模型、参数和工作流组织成可重复的媒体任务，支持编辑图像和比较批量生成结果。 | 4,791 | [2026-11-12 · commit](https://github.com/mcmonkeyprojects/SwarmUI/commit/d347f3061ce9aa19e0d3950e5189415022de6659) |
| 93 | [Tencent-Hunyuan/Hunyuan3D-2](https://github.com/Tencent-Hunyuan/Hunyuan3D-2) · [正式词条](../docs/hunyuan3d-2.md#中文) · [文档](https://raw.githubusercontent.com/Tencent-Hunyuan/Hunyuan3D-2/main/README.md) | 从图像生成 3D 形状与纹理，提供推理管线、示例和 Blender 插件。将 AI 创作中的参考图转成带纹理的 3D 资产，也可为已有网格生成纹理。 | 15,461 | [2026-11-08 · PR 创建](https://github.com/Tencent-Hunyuan/Hunyuan3D-2/pull/385) |

<a id="group-12"></a>

## 语音识别与合成（7）

| 序号 | 仓库 | 简述与 AI 用途 | Star | 近期活动（UTC） |
| ---: | --- | --- | ---: | --- |
| 94 | [fishaudio/fish-speech](https://github.com/fishaudio/fish-speech) · [正式词条](../docs/fish-speech.md#中文) · [文档](https://raw.githubusercontent.com/fishaudio/fish-speech/main/README.md) | 提供语音生成的命令行、API 服务与网页界面，支持多角色、声音克隆和局部音频编辑。将 AI 编写的对话转为多角色音频，并根据文字反馈修改语气或局部台词。 | 33,763 | [2026-10-29 · commit](https://github.com/fishaudio/fish-speech/commit/0f8a12e8a651062fdee9c33a894bdccd3a8513f1) |
| 95 | [m-bain/whisperX](https://github.com/m-bain/whisperX) · [正式词条](../docs/whisperx.md#中文) · [文档](https://raw.githubusercontent.com/m-bain/whisperX/main/README.md) | 组合语音识别、音素对齐和说话人区分，生成带词级时间戳的转写结果。为 AI 字幕、会议总结和音视频检索提供带时间轴与说话人信息的文本。 | 25,403 | [2026-11-12 · commit](https://github.com/m-bain/whisperX/commit/b904f02b7e1f26fd10fb04840d655ff27e88e464) |
| 96 | [modelscope/FunASR](https://github.com/modelscope/FunASR) · [正式词条](../docs/funasr.md#中文) · [文档](https://raw.githubusercontent.com/modelscope/FunASR/main/README.md) | 提供离线与流式语音识别、语音检测、标点和说话人处理，支持 API 与 MCP 服务。将音频转为智能体可处理的文字，并通过兼容接口把转写能力接入助手和自动化流程。 | 21,058 | [2026-11-17 · commit](https://github.com/modelscope/FunASR/commit/e227484d98ca90aa829a0ae180731c9ee2e87e77) |
| 97 | [QwenAudio/CosyVoice](https://github.com/QwenAudio/CosyVoice) · [正式词条](../docs/cosyvoice.md#中文) · [文档](https://raw.githubusercontent.com/QwenAudio/CosyVoice/main/README.md) | 提供多语言语音合成、声音克隆和流式推理，支持语速、情绪与发音控制。把智能体生成的文本转成连续语音，或按参考音频和指令生成配音。 | 24,432 | [2026-11-03 · issue 创建](https://github.com/QwenAudio/CosyVoice/issues/1964) |
| 98 | [RVC-Boss/GPT-SoVITS](https://github.com/RVC-Boss/GPT-SoVITS) · [正式词条](../docs/gpt-sovits.md#中文) · [文档](https://raw.githubusercontent.com/RVC-Boss/GPT-SoVITS/main/README.md) | 使用参考语音完成语音合成和微调。提供数据准备工具，例如切分、识别和标注。让 AI 文本生成流程输出指定音色的多语言配音，同时辅助准备语音训练数据。 | 65,251 | [2026-11-11 · commit](https://github.com/RVC-Boss/GPT-SoVITS/commit/6d51ffceafbf240145619af4c92408a6e54b7924) |
| 99 | [SWivid/F5-TTS](https://github.com/SWivid/F5-TTS) · [正式词条](../docs/f5-tts.md#中文) · [文档](https://raw.githubusercontent.com/SWivid/F5-TTS/main/README.md) | 提供语音合成与微调工具，包含 CLI 和 Gradio 界面，支持分段及多风格、多说话人生成。将生成文本与参考音频组合为配音，支持 AI 故事、角色对话及语音交互流程。 | 15,607 | [2026-11-03 · commit](https://github.com/SWivid/F5-TTS/commit/600e5fdfbf319f84735557aca80a7aaf60d487e6) |
| 100 | [SYSTRAN/faster-whisper](https://github.com/SYSTRAN/faster-whisper) · [正式词条](../docs/faster-whisper.md#中文) · [文档](https://raw.githubusercontent.com/SYSTRAN/faster-whisper/master/README.md) | 以 CTranslate2 运行 Whisper 转写，支持批量推理及 CPU、GPU 量化。把会议、录音或视频音轨转成文字，为语言模型提供可总结、检索和分析的输入。 | 26,822 | [2026-11-12 · commit](https://github.com/SYSTRAN/faster-whisper/commit/6cb639e70786aea42b9233006ae60eaf07190bdb) |

## 数据说明

每个 Star 数字是核验时的快照，后续可能变化。仓库迁移按 GitHub 返回的规范名称记录；稳定 ID 用于识别改名或转移。用途摘要根据官方文档改写，工具能力与部署条件仍以所链接的上游说明为准。

JSON 保存逐项来源和核验时间，可用于后续重新筛选。再次复核时需重新判断活动窗口和 Star 门槛，不能把本次快照视为持续达标证明。
