# CLI-Anything

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 58741 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T10:48:15.531Z |

以上为历史核对结果，使用前请复核上游状态。 / This is a dated review; check the current upstream state before use.

## 中文

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

### 原始中文记录（历史快照）

### 016 CLI-Anything

仓库：[HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything)

#### 1. 简介

分析软件源码，为真实应用后端生成 CLI harness。提供结构化命令、JSON 输出、交互式 REPL 及测试流程。

#### 2. 适用场景

为开源 GUI 软件构建命令行接口。让智能体调用真实专业软件。把分散 API 组织为一致命令。查找已有 CLI harness。

#### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 生成CLI harness | 从本地源码或GitHub仓库分析软件并生成命令行控制层。 | Plugin Commands / Fully Automated 7-Phase Pipeline |
| 调用真实软件 | 封装真实应用后端，最终文件由实际软件处理或渲染。 | Authentic Software Integration |
| 结构化与交互输出 | 生成CLI提供JSON和人类可读输出，支持统一REPL与会话状态。 | Smart Session Management / Clean Package Architecture |
| 完善与验证 | refine扩展覆盖，test记录结果，validate检查HARNESS标准。 | Plugin Commands |
| 生成技能说明 | 从命令元数据形成SKILL.md，帮助智能体发现工具。 | SKILL.md Generation |
| 工具发现管理 | CLI-Hub用于浏览、安装和管理已有CLI工具。 | Empower Your Agents with CLI-Hub |
| 组织API | README描述可将服务API文档或SDK材料整合为一致CLI。 | Unify Scattered APIs into One CLI |

官方来源入口：[官方 README](https://github.com/HKUDS/CLI-Anything/blob/main/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

**平台与环境**

- 取决于目标软件与harness；不能据通用框架推定每个目标跨平台
- 生成CLI采用Python，README标示Python≥3.10

- 框架Apache-2.0；模型调用、目标软件许可和外部API费用另计。
- 生成harness和执行真实后端需要本地资源。

- 需要较强基础模型；弱模型可能生成不完整或错误CLI。
- 主要依赖源码；二进制反编译场景覆盖明显下降。
- 通常需迭代完善，不能据“自动生成”认定覆盖全部能力。
- 本轮未生成、安装或运行任何harness。

**容易找错的需求（不属于本项目能力）**

- 对任意闭源二进制自动获得完整无损控制接口。
- 不安装目标软件就保证生成真实渲染结果。

#### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/HKUDS/CLI-Anything/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- 编码智能体中的生成/refine/test/validate入口
- 生成后的CLI命令与REPL
- CLI-Hub

#### 6. 替代选择

- [lexmount/moli](moli.md#中文)：本项目为真实软件后端生成 CLI；后者本身就是网页运行和自动化后端。网页任务可考察后者，通用软件接入仍需相应接口。

#### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/HKUDS/CLI-Anything/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/016_HKUDS-CLI-Anything.md`。

## English

A framework for building command-line interfaces that drive real application backends, including JSON output and interactive workflows.

### Use cases

- Give agents a structured application interface
- Build and test CLI harnesses for existing software

### Requirements and limits

Usually depends on source access, the target application and a capable coding model. Binary-only targets have weaker coverage. Generated harnesses need iteration and backend tests; no harness was installed or executed during this import. Platform support and licensing depend on each target.

### Getting started

Read the [official documentation](https://github.com/HKUDS/CLI-Anything/blob/main/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [Moli](moli.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:15.531Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

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
    "id": "cli-anything",
    "name": "CLI-Anything",
    "repository": "HKUDS/CLI-Anything",
    "repo_node_id": "R_kgDORhiEjA",
    "category": "development",
    "tags": [
      "cli",
      "agents",
      "automation"
    ],
    "forms": [
      "cli"
    ],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "CLI-Anything"
      ],
      "en": [
        "CLI-Anything"
      ]
    },
    "summary": {
      "zh-CN": "分析软件源码，为真实应用后端生成 CLI harness。提供结构化命令、JSON 输出、交互式 REPL 及测试流程。",
      "en": "A framework for building command-line interfaces that drive real application backends, including JSON output and interactive workflows."
    },
    "use_cases": {
      "zh-CN": [
        "为开源 GUI 软件构建命令行接口。让智能体调用真实专业软件。把分散 API 组织为一致命令。查找已有 CLI harness。"
      ],
      "en": [
        "Give agents a structured application interface",
        "Build and test CLI harnesses for existing software"
      ]
    },
    "alternatives": [
      "moli"
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
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "0cff1a8ac2a381870a2c57cbe9b25f95bea0925b39b7fbf6a04ec23df7c77760",
      "source_url": "https://github.com/HKUDS/CLI-Anything/blob/34f519533bc175d2fe287ab8316b0dd99bb9cc43/LICENSE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "34f519533bc175d2fe287ab8316b0dd99bb9cc43"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-08-21T07:25:41Z",
        "reviewed_at": "2026-11-15T11:03:50.120930Z",
        "url": "https://github.com/HKUDS/CLI-Anything/commit/b6da3c8f1012b431982b8a735db7b0789976b78a",
        "qualifies": true,
        "reason": {
          "zh-CN": "修正 GBK 控制台的 CLI 输出编码。已核对提交中的实现文件与差异；未运行上游测试。",
          "en": "Fixes CLI output encoding on GBK consoles. Reviewed implementation changes; upstream tests were not run."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/HKUDS/CLI-Anything",
        "accessed_at": "2026-11-15T10:48:15.531Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/HKUDS/CLI-Anything/blob/main/README.md",
        "accessed_at": "2026-11-15T10:54:01.152Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      },
      {
        "url": "https://github.com/HKUDS/CLI-Anything/blob/34f519533bc175d2fe287ab8316b0dd99bb9cc43/LICENSE",
        "accessed_at": "2026-11-15T10:53:09.593Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "016",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "1b0cc5ff2c7514d7198bef40465546d7e14ad7b8377d436a6d31ecb6dae7ff92",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "tool",
      "pending_reasons": [],
      "english_scope": "editorial_digest",
      "source_card_preserved": true
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDORhiEjA",
    "full_name": "HKUDS/CLI-Anything",
    "stargazers_count": 58741,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "0cff1a8ac2a381870a2c57cbe9b25f95bea0925b39b7fbf6a04ec23df7c77760",
    "last_success_at": "2026-11-15T10:48:15.531Z"
  }
}
```

</details>
