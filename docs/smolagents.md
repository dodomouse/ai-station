# smolagents

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[huggingface/smolagents](https://github.com/huggingface/smolagents)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 30404 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:53.147817Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:38.551Z |

## 中文

让智能体用代码表达操作，支持多种模型、MCP 工具和沙箱执行环境。

使 AI 编写并运行任务代码，组合搜索或其他工具来完成多步工作。

### 主要功能

- 用 CodeAgent 生成并执行 Python 操作。
- 用 ToolCallingAgent 调用结构化工具。
- 从 Hub、MCP 或 LangChain 接入工具。

### 环境要求

- 需要 Python 环境及一个可用的模型后端。
- 远程代码执行需配置 Docker、E2B、Modal 或其他支持的沙箱。

### 使用限制

- LocalPythonExecutor 不是安全沙箱，不能作为不可信代码的隔离边界。

### 开始使用

1. 按[官方文档](https://huggingface.co/docs/smolagents/index)安装组件。
2. 按[README 示例](https://github.com/huggingface/smolagents/blob/main/README.md)选择模型、工具和执行环境。
3. 执行一个测试任务，检查生成的代码和结果。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:38.551Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/huggingface/smolagents/commit/8469d427d08655209a5a5e26242dba759b213206)。docs: add Rapid-MLX (Apple Silicon) example for OpenAIModel (#2175)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [README 示例 / README example](https://github.com/huggingface/smolagents/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/huggingface/smolagents)
- [官方文档 / official docs](https://huggingface.co/docs/smolagents/index)

## English

Lets agents express actions as code, with multiple models, MCP tools and sandboxed execution options.

Allows AI to write task code and combine search or other tools to perform multistep work.

### Features

- Generate and execute Python actions with CodeAgent.
- Call structured tools with ToolCallingAgent.
- Load tools from the Hub, MCP or LangChain.

### Requirements

- Requires Python and an available model backend.
- Remote code execution requires Docker, E2B, Modal or another supported sandbox.

### Limitations

- LocalPythonExecutor is not a security sandbox and must not be used as an isolation boundary for untrusted code.

### Getting started

1. Install components using the [official docs](https://huggingface.co/docs/smolagents/index).
2. Choose a model, tools and execution environment using the [README example](https://github.com/huggingface/smolagents/blob/main/README.md).
3. Run a test task and inspect the generated code and result.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:38.551Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/huggingface/smolagents/commit/8469d427d08655209a5a5e26242dba759b213206).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [README 示例 / README example](https://github.com/huggingface/smolagents/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/huggingface/smolagents)
- [官方文档 / official docs](https://huggingface.co/docs/smolagents/index)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:53.147817Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "smolagents",
    "name": "smolagents",
    "repository": "huggingface/smolagents",
    "repo_node_id": "R_kgDONZUqgg",
    "category": "ai",
    "summary": {
      "zh-CN": "让智能体用代码表达操作，支持多种模型、MCP 工具和沙箱执行环境。",
      "en": "Lets agents express actions as code, with multiple models, MCP tools and sandboxed execution options."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:53.147817Z",
        "en": "2026-11-17T14:24:53.147817Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "使 AI 编写并运行任务代码，组合搜索或其他工具来完成多步工作。",
        "en": "Allows AI to write task code and combine search or other tools to perform multistep work."
      },
      "source_url": "https://github.com/huggingface/smolagents/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/huggingface/smolagents/commit/8469d427d08655209a5a5e26242dba759b213206",
        "occurred_at": "2026-11-17T09:55:03Z",
        "reviewed_at": "2026-11-17T14:24:53.147817Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "docs: add Rapid-MLX (Apple Silicon) example for OpenAIModel (#2175) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "README 示例 / README example",
        "url": "https://github.com/huggingface/smolagents/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / GitHub metadata",
        "url": "https://api.github.com/repos/huggingface/smolagents"
      },
      {
        "title": "官方文档 / official docs",
        "url": "https://huggingface.co/docs/smolagents/index"
      }
    ]
  },
  "snapshot": {
    "full_name": "huggingface/smolagents",
    "repo_node_id": "R_kgDONZUqgg",
    "stargazers_count": 30404,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:38.551Z",
    "source_url": "https://api.github.com/repos/huggingface/smolagents"
  }
}
```

</details>
