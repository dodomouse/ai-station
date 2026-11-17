# Browser Use

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[browser-use/browser-use](https://github.com/browser-use/browser-use)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 自动化 / Automation |
| 状态 / Status | 已收录 / Included |
| Star | 121292 |
| 评估时间 / Evaluated at | 2026-11-17T14:27:00.363870Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:30.525Z |

## 中文

让模型通过 Python 与浏览器工具执行真实网页任务。

为 AI 提供网页导航、交互和信息读取能力，连接本地或云浏览器。

### 主要功能

- 在持久 Python REPL 中调用浏览器助手与 Chrome DevTools Protocol。
- 提供 Python 库、CLI 和托管 Agent API 入口。
- 支持本地浏览器与云浏览器，并可选择模型。

### 环境要求

- Python 库要求 Python 3.11+；本地方式需要可连接的浏览器。
- 默认托管模型与云浏览器需要登录或 API 凭据；自选模型需相应配置。

### 使用限制

- 1.0 与旧版本接口不同，升级需核对迁移说明并固定使用版本。
- 云浏览器和模型有独立使用条件；交互实时链接可用于控制会话，应按会话权限管理。

### 开始使用

1. 从 README 选择 Python 库、CLI 或托管方式。
2. 按所选方式安装并连接模型、账号与浏览器。
3. 用读取公开页面信息的小任务检查执行记录，再接入业务流程。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:30.525Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/browser-use/browser-use/commit/197972b206d3a6ec9fb30afcf76149c07fb8ee61)。README: Browser Use for enterprises (#6442)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/browser-use/browser-use/blob/main/README.md)
- [GitHub 元数据 / Repository metadata](https://api.github.com/repos/browser-use/browser-use)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

Lets models carry out real web tasks using Python and browser tools.

Gives AI navigation, interaction and information-reading tools connected to local or cloud browsers.

### Features

- Calls browser helpers and the Chrome DevTools Protocol from a persistent Python REPL.
- Provides Python-library, CLI and hosted Agent API entry points.
- Supports local and cloud browsers with model selection.

### Requirements

- The Python library requires Python 3.11+; local operation needs a connectable browser.
- The default hosted model and cloud browser require sign-in or API credentials; alternative models require their own configuration.

### Limitations

- Version 1.0 differs from earlier APIs; consult the migration guide and pin the selected version.
- Cloud browsers and models have their own usage conditions; interactive live-view links can control a session and need appropriate access handling.

### Getting started

1. Choose the Python library, CLI or hosted route from the README.
2. Install the selected route and connect the model, account and browser.
3. Use a small public-page reading task to inspect execution before connecting a business workflow.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:30.525Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/browser-use/browser-use/commit/197972b206d3a6ec9fb30afcf76149c07fb8ee61).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/browser-use/browser-use/blob/main/README.md)
- [GitHub 元数据 / Repository metadata](https://api.github.com/repos/browser-use/browser-use)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:27:00.363870Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "browser-use",
    "name": "Browser Use",
    "repository": "browser-use/browser-use",
    "repo_node_id": "R_kgDONIn9tw",
    "category": "automation",
    "summary": {
      "zh-CN": "让模型通过 Python 与浏览器工具执行真实网页任务。",
      "en": "Lets models carry out real web tasks using Python and browser tools."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:27:00.363870Z",
        "en": "2026-11-17T14:27:00.363870Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "为 AI 提供网页导航、交互和信息读取能力，连接本地或云浏览器。",
        "en": "Gives AI navigation, interaction and information-reading tools connected to local or cloud browsers."
      },
      "source_url": "https://github.com/browser-use/browser-use/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/browser-use/browser-use/commit/197972b206d3a6ec9fb30afcf76149c07fb8ee61",
        "occurred_at": "2026-11-17T04:48:53Z",
        "reviewed_at": "2026-11-17T14:27:00.363870Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "README: Browser Use for enterprises (#6442) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/browser-use/browser-use/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / Repository metadata",
        "url": "https://api.github.com/repos/browser-use/browser-use"
      }
    ]
  },
  "snapshot": {
    "full_name": "browser-use/browser-use",
    "repo_node_id": "R_kgDONIn9tw",
    "stargazers_count": 121292,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:30.525Z",
    "source_url": "https://api.github.com/repos/browser-use/browser-use"
  }
}
```

</details>
