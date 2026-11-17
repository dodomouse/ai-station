# Stagehand

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[browserbase/stagehand](https://github.com/browserbase/stagehand)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 自动化 / Automation |
| 状态 / Status | 已收录 / Included |
| Star | 26077 |
| 评估时间 / Evaluated at | 2026-11-17T14:29:34.728840Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:30.586Z |

## 中文

为浏览器智能体提供交互、观察和结构化数据提取 SDK。

让 AI 使用自然语言与常规定位器组合完成网页操作和数据采集。

### 主要功能

- 通过 act、observe 和 extract 操作页面并提取结构化结果。
- 支持持久浏览器会话，以及 TypeScript、Python 和 Go 接口。
- 提供面向编码智能体的 browse CLI。

### 环境要求

- 本地运行需要安装 Chrome，以及所选 SDK 的语言环境。
- SDK 的模型辅助操作需要模型访问。可自配供应商或使用 Browserbase Model Gateway。本地 browse CLI 不要求模型密钥或 Browserbase 账号。

### 使用限制

- CLI、本地 SDK 和托管 MCP 的依赖及能力不同，需选择匹配的接入方式。
- 自然语言操作受页面状态与模型结果影响；持久配置目录会保留登录状态。

### 开始使用

1. 阅读 README，选择 SDK 或 browse CLI。
2. 本地安装 Chrome，按示例创建浏览器会话；使用 SDK 时选择模型访问方式。
3. 先执行页面读取或结构化提取，检查结果后再组合多步骤交互。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:30.586Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/browserbase/stagehand/commit/0f9a64c141d929b0595b4d909d89fb02e37c1ca4)。[Claimed #3463] fix(cli): decode daemon replies as streaming UTF-8 (#3473)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/browserbase/stagehand/blob/main/README.md)
- [GitHub 元数据 / Repository metadata](https://api.github.com/repos/browserbase/stagehand)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

Provides browser-agent SDKs for interaction, observation and structured data extraction.

Lets AI combine natural-language instructions with conventional locators for web actions and data collection.

### Features

- Uses act, observe and extract to operate pages and return structured results.
- Supports persistent browser sessions and TypeScript, Python and Go interfaces.
- Provides the browse CLI for coding agents.

### Requirements

- Local operation requires Chrome and the runtime for the selected SDK.
- Model-assisted SDK operations need model access through a configured provider or Browserbase Model Gateway; local browse CLI use requires neither a model key nor a Browserbase account.

### Limitations

- The CLI, local SDK and hosted MCP differ in requirements and capabilities; choose the appropriate integration.
- Natural-language actions depend on page state and model output; persistent profile directories retain sign-in state.

### Getting started

1. Choose the SDK or browse CLI from the README.
2. Install Chrome locally and create a browser session from the example; choose a model access option when using the SDK.
3. Start with page reading or structured extraction, inspect the result, then compose multistep interactions.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:30.586Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/browserbase/stagehand/commit/0f9a64c141d929b0595b4d909d89fb02e37c1ca4).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/browserbase/stagehand/blob/main/README.md)
- [GitHub 元数据 / Repository metadata](https://api.github.com/repos/browserbase/stagehand)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:29:34.728840Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "stagehand",
    "name": "Stagehand",
    "repository": "browserbase/stagehand",
    "repo_node_id": "R_kgDOLk6wNA",
    "category": "automation",
    "summary": {
      "zh-CN": "为浏览器智能体提供交互、观察和结构化数据提取 SDK。",
      "en": "Provides browser-agent SDKs for interaction, observation and structured data extraction."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:29:34.728840Z",
        "en": "2026-11-17T14:29:34.728840Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "让 AI 使用自然语言与常规定位器组合完成网页操作和数据采集。",
        "en": "Lets AI combine natural-language instructions with conventional locators for web actions and data collection."
      },
      "source_url": "https://github.com/browserbase/stagehand/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/browserbase/stagehand/commit/0f9a64c141d929b0595b4d909d89fb02e37c1ca4",
        "occurred_at": "2026-11-17T01:05:08Z",
        "reviewed_at": "2026-11-17T14:29:34.728840Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "[Claimed #3463] fix(cli): decode daemon replies as streaming UTF-8 (#3473) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/browserbase/stagehand/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / Repository metadata",
        "url": "https://api.github.com/repos/browserbase/stagehand"
      }
    ]
  },
  "snapshot": {
    "full_name": "browserbase/stagehand",
    "repo_node_id": "R_kgDOLk6wNA",
    "stargazers_count": 26077,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:30.586Z",
    "source_url": "https://api.github.com/repos/browserbase/stagehand"
  }
}
```

</details>
