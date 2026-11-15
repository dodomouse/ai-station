# Public APIs

简体中文 | [English](README.en.md) | [全部导入记录](../../docs/imports/2026-11-15.md)

## 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

当前资格请运行 `python3 scripts/catalog.py search public-apis --all`（仓库根目录）。Star 和时间数据见 [GitHub 快照](../../data/github/public-apis.json)，核对依据见 [元数据](tool.json)。

## 原始中文记录（历史快照）

## 021 Public APIs

仓库：[public-apis/public-apis](https://github.com/public-apis/public-apis)

### 1. 简介

按领域收集公开 API，列出认证、HTTPS 和 CORS 信息。当前也包含供智能体使用的 MCP 服务目录。

### 2. 适用场景

为原型寻找外部数据接口。按领域查找 API。筛选认证与跨域条件。

### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 按领域寻找 API | 领域索引覆盖天气、地理、金融、新闻、开发、开放数据等，可跳转到具体接口条目。 | Index / 各领域分类 |
| 接口基本条件对照 | API 表列出说明、Auth、HTTPS、CORS，帮助初步筛选认证、传输和跨域条件。 | 各领域 API 表 |
| MCP 服务导航 | MCP Servers 单列可供智能体调用的服务，并提供认证、传输和安装入口等信息。 | MCP Servers |
| 服务文档与接入入口 | 接口条目链接到各自的服务或文档。APILayer 部分另列产品及 Postman 等接入入口。 | APILayer APIs / 各领域 API 表 |

官方来源入口：[官方 README](https://github.com/public-apis/public-apis/blob/master/README.md)。 能力按原卡核对日期理解。

### 4. 使用限制

**平台与环境**

- 通过浏览器或 GitHub 阅读，目录无独立运行平台要求
- 具体 API 或 MCP 的客户端兼容范围由各服务决定

- 仓库元数据标示 MIT。被收录 API、MCP 与 APILayer 产品分别定价，可能有免费额度、认证或付费套餐；目录许可不替代服务合同，也不意味着全部免费。

- 条目是发现线索，不代表对外部服务的可用性和数据准确性作验证。
- Auth、HTTPS 和 CORS 字段需按服务当前文档复核。
- README 含商业推广，推广内容与社区目录需区分。

**容易找错的需求（不属于本项目能力）**

- 不匹配“一个接口或一个 key 就能免费调用目录全部服务”的需求。
- 不是自带所有数据、可完全离线运行的 API 服务器。

### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/public-apis/public-apis/blob/master/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- GitHub README 分类目录
- 外部 API 文档链接
- MCP 服务导航；本仓本身不是统一网关

可先阅读 README 与目录，按具体主题进入资料。若要使用附带程序或技能，再按其说明准备环境。

### 6. 替代选择

- [1c7/chinese-independent-developer](../chinese-independent-developer/README.zh-CN.md)：本项目帮助寻找 API 和认证条件；后者帮助寻找已经上线的网站、App 与开发者。

### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/public-apis/public-apis/blob/master/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/021_public-apis-public-apis.md`。
