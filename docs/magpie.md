# Magpie

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[yetone/magpie](https://github.com/yetone/magpie)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 36740 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T11:46:22.763Z |

以上为历史核对结果，使用前请复核上游状态。 / This is a dated review; check the current upstream state before use.

## 中文

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

### 原始中文记录（历史快照）

### 031 Magpie

仓库：[yetone/magpie](https://github.com/yetone/magpie)

#### 1. 简介

通过本地网关统一管理编码智能体的模型与服务商。提供多账号路由、故障转移及可选请求脱敏。

#### 2. 适用场景

统一管理多个智能体的模型配置。把多个服务商接到本地网关。在配额用尽时切换可用账号。检查和配置请求脱敏规则。

#### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 统一模型网关 | 在本地转换OpenAI Chat、Responses、Anthropic Messages和Gemini协议，包含流式、工具调用与推理字段。 | How it fits together |
| 为客户端切换模型 | 统一为Claude Code、Codex、Gemini CLI、OpenCode、Cursor CLI等受支持客户端设置模型，Profiles可保存并切换一组配置。 | Supported agents / Any model, any agent |
| 复用已登录订阅 | 把Claude、Codex/ChatGPT、GitHub Copilot、Gemini Code Assist、Antigravity及Grok SuperGrok等已登录订阅作为提供方接给其他Agent。 | Subscriptions |
| 多账号与路由组 | 在账号或模型间故障切换；smart优先用即将续期的剩余额度，order顺序回退，rotate轮换，usage/pace按使用情况分配。 | Routing groups |
| 用量与成本查看 | 按key、计划和账号查看额度窗口、token、缓存、账单与会话；支持设置模型价格。 | Usage and cost |
| 按意图选模型 | 用指定小模型判断新一轮任务，把不同任务分给强模型或较便宜模型。 | Routing groups / Intent routing |
| 可选隐私脱敏 | 启用后在本机替换敏感值，请求发送占位符，回复时还原；支持Mask/Warn/Block规则及审查。 | Privacy masking |

官方来源入口：[官方 README](https://github.com/yetone/magpie/blob/main/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

**平台与环境**

- macOS
- Windows（README另含WSL支持）
- Linux
- Docker
- Android Termux

- Magpie代码MIT开源，不等于上游模型免费。
- API按服务商账户计费；订阅使用已有套餐的可用模型和额度。
- smart等调度旨在减少已有额度浪费，不增加套餐配额。
- 意图路由用的小模型、搜索API及其他云能力可能另消耗额度或费用。
- 本地Ollama/LM Studio模型仍需本地计算资源。

- 单个账号且无路由组时，没有可切换备用，错误仍会返回。
- 订阅桥接、模型支持和协议转换为README声明，本轮未实测所有组合。
- Privacy masking默认关闭；规则可能误判，值本身被遮住时模型也无法直接分析该值。
- 订阅发现可读取Agent登录文件/Keychain，文档提供关闭开关；目录整理不等于授权读取这些凭据。
- 上游计费、可用模型、配额和使用条件仍然适用；无免费无限或绕过限制的证据。
- README说明有可关闭的使用统计，不能称为默认完全无遥测。

**容易找错的需求（不属于本项目能力）**

- 凭空获得没有购买或授权的付费模型、无限免费token。
- 突破上游配额或保证任意客户端与任意订阅完全兼容。

#### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/yetone/magpie/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- 菜单栏、窗口、TUI、Web UI、CLI
- 客户端包括Claude Code、Claude Desktop、Codex、Gemini CLI、OpenCode、DeepSeek Harness、Cursor CLI、Zed、VS Code Chat、Copilot CLI、Kimi Code、Qwen Code、Cline、WorkBuddy、CodeBuddy、OpenClaw等，完整清单见README
- API预设包括Anthropic、OpenAI、Google Gemini/Vertex、AWS Bedrock、DeepSeek、Kimi、智谱GLM、MiniMax、StepFun、Qwen、Mistral、Groq、xAI、OpenRouter、SiliconFlow等
- 本地提供方包括Ollama与LM Studio，也可接兼容OpenAI/Anthropic的URL
- 订阅接入包括Claude、Codex/ChatGPT、GitHub Copilot、Gemini Code Assist、Antigravity、Grok SuperGrok
- 可选MCP搜索/图像工具、插件与远程共享

#### 6. 替代选择

- [stablyai/orca](orca.md#中文)：本项目统一模型服务商、账号路由和故障转移；后者统一开发工作区和任务界面。开发管理需求可看后者，模型路由仍需相应网关。

#### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/yetone/magpie/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/031_yetone-magpie.md`。

## English

A local gateway that routes coding-agent requests across configured model providers and accounts, with optional failover and masking.

### Use cases

- Manage model routing
- Reuse configured accounts across supported clients

### Requirements and limits

It does not create free quota or bypass provider terms. Failover needs actual alternatives. Subscription discovery may read agent login files or Keychain; that requires deliberate configuration. Masking is off by default and may misclassify data. Optional telemetry exists. Compatibility and billing were not tested.

### Getting started

Read the [official documentation](https://github.com/yetone/magpie/blob/main/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [Orca](orca.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:18.536Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

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
    "id": "magpie",
    "name": "Magpie",
    "repository": "yetone/magpie",
    "repo_node_id": "R_kgDOUns_9A",
    "category": "ai",
    "tags": [
      "gateway",
      "models",
      "routing"
    ],
    "forms": [
      "cli",
      "service"
    ],
    "platforms": [
      "linux",
      "macos",
      "windows",
      "android"
    ],
    "aliases": {
      "zh-CN": [
        "Magpie"
      ],
      "en": [
        "Magpie"
      ]
    },
    "summary": {
      "zh-CN": "通过本地网关统一管理编码智能体的模型与服务商。提供多账号路由、故障转移及可选请求脱敏。",
      "en": "A local gateway that routes coding-agent requests across configured model providers and accounts, with optional failover and masking."
    },
    "use_cases": {
      "zh-CN": [
        "统一管理多个智能体的模型配置。把多个服务商接到本地网关。在配额用尽时切换可用账号。检查和配置请求脱敏规则。"
      ],
      "en": [
        "Manage model routing",
        "Reuse configured accounts across supported clients"
      ]
    },
    "alternatives": [
      "orca"
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
      "license_sha256": "79d2c8444715d4bc453ec4f8a0aaf2051a4c1ee5ac08f5bd2e5848aef87c7572",
      "source_url": "https://github.com/yetone/magpie/blob/main/LICENSE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-15T08:45:06Z",
        "reviewed_at": "2026-11-15T11:03:50.120930Z",
        "url": "https://github.com/yetone/magpie/commit/993c8a726704199878677918e2d2eaf15a458817",
        "qualifies": true,
        "reason": {
          "zh-CN": "让分组分类器使用该组配置的账号。已核对提交中的实现文件与差异；未运行上游测试。",
          "en": "Uses a routing group’s accounts for its classifier. Reviewed implementation changes; upstream tests were not run."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/yetone/magpie",
        "accessed_at": "2026-11-15T10:48:18.536Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/yetone/magpie/blob/main/README.md",
        "accessed_at": "2026-11-15T10:54:03.864Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      },
      {
        "url": "https://github.com/yetone/magpie/blob/main/LICENSE",
        "accessed_at": "2026-11-15T10:53:12.923Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "031",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "df32c218358c2198930053fae34fc430d032833abeab6707365e5cee6bb2e107",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "tool",
      "pending_reasons": [],
      "english_scope": "editorial_digest",
      "source_card_preserved": true
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOUns_9A",
    "full_name": "yetone/magpie",
    "stargazers_count": 36740,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "79d2c8444715d4bc453ec4f8a0aaf2051a4c1ee5ac08f5bd2e5848aef87c7572",
    "last_success_at": "2026-11-15T11:46:22.763Z"
  }
}
```

</details>
