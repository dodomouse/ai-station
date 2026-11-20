# Chainlit

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[Chainlit/chainlit](https://github.com/Chainlit/chainlit)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 12503 |
| 评估时间 / Evaluated at | 2026-11-17T14:28:37.557224Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:25.897Z |

## 中文

用 Python 编写对话式 AI 应用，并在浏览器中展示消息与工具执行步骤。

为模型或工具调用提供交互入口，适合调试和演示 AI 工作流。

### 主要功能

- 通过消息回调处理用户输入。
- 用步骤装饰器显示工具执行过程。
- 提供开发时自动重载，以及模型和检索服务集成示例。

### 环境要求

- 需要 Python 环境及浏览器。
- 从源码安装开发版本还需要 Node 和 pnpm。

### 使用限制

- 本次 GitHub 快照显示仓库已归档。README 仍保留社区维护说明，后续维护状态需另行核对。
- 快速示例使用模拟工具；真实模型或服务需要自行接入。

### 开始使用

1. 运行 `pip install chainlit`，再用 `chainlit hello` 检查浏览器界面。
2. 按官方 Quickstart 创建 `demo.py`，加入消息回调和工具步骤。
3. 运行 `chainlit run demo.py -w`，再把模拟工具替换为实际调用。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:25.897Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-08-26 · commit](https://github.com/Chainlit/chainlit/commit/190ea74239d9e84b26e7c91bc2882dd038942564)。为 CI 增加检查：声明但未实际应用的 pnpm.overrides 固定项会导致检查失败。

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://raw.githubusercontent.com/Chainlit/chainlit/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/Chainlit/chainlit)

## English

Build conversational AI applications in Python, with browser views for messages and tool execution steps.

It provides an interactive entry point for model and tool calls, useful for debugging and demonstrating AI workflows.

### Features

- Handle user input through message callbacks.
- Display tool execution with step decorators.
- Provide development reloads and integration examples for model and retrieval services.

### Requirements

- Requires Python and a browser.
- Installing the development version from source also requires Node and pnpm.

### Limitations

- The current GitHub snapshot marks the repository as archived. The README still describes community maintenance; future maintenance status requires a separate check.
- The quickstart uses a mock tool; real models or services must be connected separately.

### Getting started

1. Run `pip install chainlit`, then use `chainlit hello` to check the browser interface.
2. Create `demo.py` from the official Quickstart with a message callback and tool step.
3. Run `chainlit run demo.py -w`, then replace the mock tool with a real integration.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:25.897Z meets the total-Star threshold of 1,000.

Recent activity: [2026-08-26 · commit](https://github.com/Chainlit/chainlit/commit/190ea74239d9e84b26e7c91bc2882dd038942564).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://raw.githubusercontent.com/Chainlit/chainlit/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/Chainlit/chainlit)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:28:37.557224Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "chainlit",
    "name": "Chainlit",
    "repository": "Chainlit/chainlit",
    "repo_node_id": "R_kgDOJJioGw",
    "category": "development",
    "summary": {
      "zh-CN": "用 Python 编写对话式 AI 应用，并在浏览器中展示消息与工具执行步骤。",
      "en": "Build conversational AI applications in Python, with browser views for messages and tool execution steps."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:28:37.557224Z",
        "en": "2026-11-17T14:28:37.557224Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "为模型或工具调用提供交互入口，适合调试和演示 AI 工作流。",
        "en": "It provides an interactive entry point for model and tool calls, useful for debugging and demonstrating AI workflows."
      },
      "source_url": "https://raw.githubusercontent.com/Chainlit/chainlit/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/Chainlit/chainlit/commit/190ea74239d9e84b26e7c91bc2882dd038942564",
        "occurred_at": "2026-08-26T08:54:31Z",
        "reviewed_at": "2026-11-17T14:28:37.557224Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "为 CI 增加检查：声明但未实际应用的 pnpm.overrides 固定项会导致检查失败。 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://raw.githubusercontent.com/Chainlit/chainlit/main/README.md"
      },
      {
        "title": "GitHub 仓库元数据 / Repository metadata",
        "url": "https://api.github.com/repos/Chainlit/chainlit"
      }
    ]
  },
  "snapshot": {
    "full_name": "Chainlit/chainlit",
    "repo_node_id": "R_kgDOJJioGw",
    "stargazers_count": 12503,
    "archived": true,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:25.897Z",
    "source_url": "https://api.github.com/repos/Chainlit/chainlit"
  }
}
```

</details>
