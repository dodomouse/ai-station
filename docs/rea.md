# REA — Reverse Engineer Anything

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[morluto/rea](https://github.com/morluto/rea)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 460761 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T10:48:16.197Z |

以上为历史核对结果，使用前请复核上游状态。 / This is a dated review; check the current upstream state before use.

## 中文

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

### 原始中文记录（历史快照）

### 018 REA — Reverse Engineer Anything

仓库：[morluto/rea](https://github.com/morluto/rea)

#### 1. 简介

通过 MCP 和 CLI 连接逆向分析工具。可分析原生二进制、JavaScript、Electron、.NET 及网站。

#### 2. 适用场景

理解没有源码的桌面应用行为。检查 Electron 的模块与 IPC。辅助原生二进制逆向分析。

#### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 原生二进制分析 | 接入 Hopper、Ghidra、IDA 或 Kuna，获得伪代码、汇编、字符串、符号、调用与引用。 | What you can analyze |
| JavaScript 与 Electron 检查 | 静态检查模块、导入、source map、路由、IPC 和原生插件关系。可分析解包目录或 ASAR。 | Quick start / What you can analyze |
| .NET 静态检查 | 读取程序集元数据、CIL 指令和原生依赖声明，并比较构建结果。此路径不需要原生反编译引擎。 | What you can analyze |
| 网页与网络记录分析 | 可观察网页结构、脚本和网络请求，也能分析保存的 HAR 或 SAZ 等记录。不同格式有不同外部工具依赖。 | What you can analyze |
| Android 应用检查 | 使用 JADX 和 JDK 检查 APK 的 Manifest、类、反编译方法和引用。 | What you can analyze |
| 运行行为与本地证据 | 可记录受控进程的终端交互、退出和文件变化。输出给出观察证据及推断限制。 | How REA works / What you can analyze |
| 智能体与终端接口 | 以 MCP、工作流说明和 CLI 提供分析操作。静态 JavaScript 路径可独立于原生分析引擎运行。 | Quick start / How REA works |

官方来源入口：[官方 README](https://github.com/morluto/rea/blob/main/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

**平台与环境**

- 目标与后端决定主机范围，不能概括为所有功能跨平台
- JavaScript 静态分析依赖 Node.js/npm；原生分析依赖相应引擎
- 部分记录、固件与诊断路径仅在 Linux 验证；Windows Ghidra 支持标为实验性

- REA 自有代码为 MIT。商业逆向工具、反编译器和所接编码模型可能分别收费，REA 不授予第三方工具的许可或激活权。

- 原生工具、浏览器、JDK、抓包解析器等依所选目标分别配置。
- 静态关系、推断和运行观察的证据强度不同，结论需保留限制。
- 本轮未执行任何二进制、应用、安装器或分析引擎。

**容易找错的需求（不属于本项目能力）**

- 不能承诺恢复一份与原作者完全一致、可直接重建的源码。
- 不是绕过软件授权、破解激活或免费获得商业反编译器的工具许可。

#### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/morluto/rea/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- MCP 服务
- rea / rea-agents CLI
- 智能体工作流说明
- Hopper、Ghidra、IDA、Kuna 等 provider

#### 6. 替代选择

- [storytold/craft-anything](craft-anything.md#中文)：本项目连接逆向分析工具，检查程序行为；后者将研究结果用于构建与比较新版本。

#### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/morluto/rea/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/018_morluto-rea.md`。

## English

CLI and MCP tooling for examining binaries, JavaScript, desktop apps and websites with multiple analysis backends.

### Use cases

- Investigate software structure
- Collect and compare analysis evidence

### Requirements and limits

Backends, browsers, JDKs and native tools must be configured for the target. Platform coverage differs; some paths are Linux-only or experimental. REA does not grant licenses for commercial analysis tools. Inferences and observed behavior differ, and original source recovery is not guaranteed.

### Getting started

Read the [official documentation](https://github.com/morluto/rea/blob/main/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [Craft Anything](craft-anything.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:16.197Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

保留原始核对数据，便于追溯来源、许可和维护证据。 / Original review data preserves source, license and maintenance evidence.

```json
{
  "evaluated_at": "2026-11-15T11:54:08.129868Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "rea",
    "name": "REA — Reverse Engineer Anything",
    "repository": "morluto/rea",
    "repo_node_id": "R_kgDOSB6hVQ",
    "category": "development",
    "tags": [
      "reverse-engineering",
      "mcp",
      "analysis"
    ],
    "forms": [
      "cli",
      "service"
    ],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "REA — Reverse Engineer Anything"
      ],
      "en": [
        "REA"
      ]
    },
    "summary": {
      "zh-CN": "通过 MCP 和 CLI 连接逆向分析工具。可分析原生二进制、JavaScript、Electron、.NET 及网站。",
      "en": "CLI and MCP tooling for examining binaries, JavaScript, desktop apps and websites with multiple analysis backends."
    },
    "use_cases": {
      "zh-CN": [
        "理解没有源码的桌面应用行为。检查 Electron 的模块与 IPC。辅助原生二进制逆向分析。"
      ],
      "en": [
        "Investigate software structure",
        "Collect and compare analysis evidence"
      ]
    },
    "alternatives": [
      "craft-anything"
    ],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-15T11:03:50.120930Z",
        "en": "2026-11-15T11:03:50.120930Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "798f9e4d18e49b30bf2f12696c8ced73dc4e1413da375a333d01281543a1ea8b",
      "source_url": "https://github.com/morluto/rea/blob/28265927594d6929f6c84d6c65ddd6d72a0b6ee6/LICENSE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "28265927594d6929f6c84d6c65ddd6d72a0b6ee6"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-15T10:38:24Z",
        "reviewed_at": "2026-11-15T11:03:50.120930Z",
        "url": "https://github.com/morluto/rea/commit/28265927594d6929f6c84d6c65ddd6d72a0b6ee6",
        "qualifies": true,
        "reason": {
          "zh-CN": "为应用取消操作强制提供原因。已核对提交中的实现文件与差异；未运行上游测试。",
          "en": "Requires a reason when constructing application cancellations. Reviewed implementation changes; upstream tests were not run."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/morluto/rea",
        "accessed_at": "2026-11-15T10:48:16.197Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/morluto/rea/blob/main/README.md",
        "accessed_at": "2026-11-15T10:54:01.536Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      },
      {
        "url": "https://github.com/morluto/rea/blob/28265927594d6929f6c84d6c65ddd6d72a0b6ee6/LICENSE",
        "accessed_at": "2026-11-15T10:53:10.222Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "018",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "96651d6b8ffc55d17d3bfc6ed5c45ba293206ee633bd3b203311f09e304e7d76",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "tool",
      "pending_reasons": [],
      "english_scope": "editorial_digest",
      "source_card_preserved": true
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOSB6hVQ",
    "full_name": "morluto/rea",
    "stargazers_count": 460761,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "798f9e4d18e49b30bf2f12696c8ced73dc4e1413da375a333d01281543a1ea8b",
    "last_success_at": "2026-11-15T10:48:16.197Z"
  }
}
```

</details>
