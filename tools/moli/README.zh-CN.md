# Moli：面向 AI 智能体的无头浏览器

简体中文 | [English](README.en.md) | [全部导入记录](../../docs/imports/2026-11-15.md)

## 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

当前资格请运行 `python3 scripts/catalog.py search moli --all`（仓库根目录）。Star 和时间数据见 [GitHub 快照](../../data/github/moli.json)，核对依据见 [元数据](tool.json)。

源码默认可选 Apache-2.0 或 MIT。API 单值仍保存 Apache-2.0，指纹对应 LICENSE-APACHE；第三方组件和测试素材仍按各自声明。

## 原始中文记录（历史快照）

## 059 Moli：面向 AI 智能体的无头浏览器

仓库：[lexmount/moli](https://github.com/lexmount/moli)

### 1. 简介

Rust 编写的独立无头浏览器，支持 JavaScript 网页运行、Markdown 与语义树提取、按需布局，以及 CLI、CDP 和 WebDriver 自动化。

### 2. 适用场景

把网页转为 AI 可读内容。提取动态页面。为智能体提供浏览器后端。按需截图、导出 PDF 或连接 Playwright。

### 3. 主要功能

以下以核验版本的官方 README 为依据；网页搜索另参考 `moli-websearch` 技能说明。

| 能力 | 具体作用与条件 |
| --- | --- |
| 网页提取 | CLI 可输出 HTML、Markdown、JSON 和语义文本树，支持选择器、脚本及响应等待。 |
| 网页运行与交互 | 执行 JavaScript，处理 DOM、iframe、worker、Fetch/XHR/WebSocket、Cookie 和按 Profile 隔离的存储。 |
| 自动化协议 | 同一服务端点提供 CDP、WebDriver Classic 和 WebDriver BiDi；README 给出 Playwright 通过 CDP 连接的示例。 |
| 按需视觉输出 | `--layout` 启用真实布局、坐标输入、截图和低频软件渲染录屏帧；CLI 可输出视口截图、整页截图及分页 PDF。 |
| 运行控制 | 可配置代理、超时、资源类型、Cookie、缓存和 Profile；可选图片、字体及媒体资源需按需启用。 |
| 智能体技能 | 提供 `moli-webfetch`、`moli-websearch`、`moli-cdp-server`。搜索技能通过浏览器访问搜索引擎，并包含关键词与以图搜图路线。 |

官方来源入口：[官方 README](https://github.com/lexmount/moli/blob/main/README.md)。 能力按原卡核对日期理解。

### 4. 使用限制

- 官方列出 Linux、macOS、Windows 支持，提供预编译二进制与安装脚本。适用平台及安装方式以实际版本为准，本次未下载安装。
- 开源无头浏览器可独立使用；Lexmount Browser 是围绕它提供的托管云运行时与控制平台。
- 提取页面的官方示例：

```bash
moli fetch --dump markdown --wait-until done https://example.com
```

- 自动化服务入口为 `moli serve`；需要真实布局与视觉能力时用 `moli serve --layout`。默认模式不执行真实布局和绘制，不能将其几何结果当作页面真实坐标。
- 许可默认可选 Apache-2.0 或 MIT；另有声明的文件、目录和第三方组件遵循各自许可与通知。GitHub API 的单一许可字段不能完整表达双许可口径。

- 官方说明它不追求与 Chrome 像素级一致，也不提供高保真 Canvas、WebGL 或媒体播放。复杂视觉页面和现有自动化脚本需要单独验收。
- 官方基准与“可用于生产”等表述属于项目方评估；本次未复现，不把它们视为性能或稳定性保证。
- [CLI-Anything](../cli-anything/README.zh-CN.md)为软件生成命令行操作接口；Moli 本身是网页运行与自动化后端。
- [AI Website Cloner Template](../ai-website-cloner-template/README.zh-CN.md)组织网页观察与前端重建；Moli 提供网页访问能力，两者的接入兼容性未验证。
- [Horizon](../horizon/README.zh-CN.md)组织资讯采集和日报生成；Moli 提供更底层的网页提取与浏览器操作能力，不据此推定 Horizon 已接入 Moli。

知识卡未提供完整部署费用或付费服务价格；未记录的费用项目需要另行核对。

### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/lexmount/moli/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

其他入口：[网页搜索技能](https://github.com/lexmount/moli/blob/95bbf1531f2df5b24571b7c23612ef833dd071c7/skills/moli-websearch/SKILL.md)、[官方中文说明](https://github.com/lexmount/moli/blob/main/docs/README.zh-CN.md)、[技能目录](https://github.com/lexmount/moli/tree/main/skills)、[发行版本](https://github.com/lexmount/moli/releases)。

初次使用所需环境及调用示例见上节“使用限制”。

### 6. 替代选择

- [HKUDS/CLI-Anything](../cli-anything/README.zh-CN.md)：本项目是网页访问与自动化后端；后者为其他软件生成 CLI。两者可解决不同层次的工具接入问题。

### 7. 复核说明

- 知识库记录日期：2026-11-11；卡片最后确认日期：2026-11-11。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：已核对官方 README、Cargo 许可声明、许可元数据、技能目录及网页搜索技能说明；未安装运行。分类、问法和匹配理由属于检索整理判断。

**来源与版本记录**

- 当前入口：[官方 README](https://github.com/lexmount/moli/blob/main/README.md)。
- 核验版本：默认分支 `main`，提交 [`95bbf1531f2df5b24571b7c23612ef833dd071c7`](https://github.com/lexmount/moli/commit/95bbf1531f2df5b24571b7c23612ef833dd071c7)。
- 固定版本：[README](https://github.com/lexmount/moli/blob/95bbf1531f2df5b24571b7c23612ef833dd071c7/README.md)、[Cargo 声明](https://github.com/lexmount/moli/blob/95bbf1531f2df5b24571b7c23612ef833dd071c7/Cargo.toml)、[许可元数据](https://github.com/lexmount/moli/blob/95bbf1531f2df5b24571b7c23612ef833dd071c7/license-metadata.json)、[网页搜索技能](https://github.com/lexmount/moli/blob/95bbf1531f2df5b24571b7c23612ef833dd071c7/skills/moli-websearch/SKILL.md)。
- 后续入口：[官方中文说明](https://github.com/lexmount/moli/blob/main/docs/README.zh-CN.md)、[技能目录](https://github.com/lexmount/moli/tree/main/skills)、[发行版本](https://github.com/lexmount/moli/releases)。本次未验证各发行包或逐项执行技能。
- 按仓库 ID `1329849289` 去重；后续复核平台、协议兼容和许可时，同步更新用途索引与最后确认日期。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/059_lexmount-moli.md`。
