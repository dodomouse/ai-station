# Mem0

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[mem0ai/mem0](https://github.com/mem0ai/mem0)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 69107 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:53.148812Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:38.289Z |

## 中文

为智能体和应用提取、保存并检索用户、会话和任务记忆。

让 AI 在后续任务中复用用户偏好和历史事实，降低跨会话重复说明；托管版与开源 SDK 能力不同。

### 主要功能

- 保存用户、会话和智能体层面的记忆。
- 根据任务检索记忆与历史上下文。
- 通过 SDK、自托管服务或 Cloud 接入应用。

### 环境要求

- 需要语言模型；可按官方列表配置不同模型供应商。
- 选择 Python 或 JavaScript SDK，或准备自托管服务环境。

### 使用限制

- README 的基准结果来自托管平台，不能直接套用于开源 SDK。
- 自托管服务默认启用认证。升级旧部署时需要配置管理员认证。

### 开始使用

1. 按[快速入门](https://docs.mem0.ai/quickstart)选择接入方式。
2. 按[模型说明](https://docs.mem0.ai/components/llms/overview)配置语言模型。
3. 保存一个会话事实，再执行检索检查。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:38.289Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-06 · commit](https://github.com/mem0ai/mem0/commit/f1791daa86d469249c9b002f62644d58a1eb96a0)。fix(security): upgrade @azure/msal-node to 7.x via @azure/identity 4.14.1 (CVE-2026-109461) (#7850)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/mem0ai/mem0/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/mem0ai/mem0)
- [快速入门 / quickstart](https://docs.mem0.ai/quickstart)
- [模型说明 / model guide](https://docs.mem0.ai/components/llms/overview)

## English

Extracts, stores and retrieves user, session and task memories for agents and applications.

Lets AI reuse preferences and historical facts in later tasks; the hosted platform and open-source SDK differ.

### Features

- Store memory at user, session and agent levels.
- Retrieve memories and historical context for a task.
- Integrate through an SDK, self-hosted service or Cloud.

### Requirements

- Requires a language model; providers can be configured from the official supported list.
- Choose a Python or JavaScript SDK, or prepare a self-hosted service environment.

### Limitations

- README benchmark results describe the managed platform and do not transfer directly to the open-source SDK.
- Self-hosted authentication is enabled by default. Older deployments need administrator authentication configured during upgrades.

### Getting started

1. Choose an integration route using the [quickstart](https://docs.mem0.ai/quickstart).
2. Configure a language model using the [model guide](https://docs.mem0.ai/components/llms/overview).
3. Save a conversation fact, then check retrieval.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:38.289Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-06 · commit](https://github.com/mem0ai/mem0/commit/f1791daa86d469249c9b002f62644d58a1eb96a0).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/mem0ai/mem0/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/mem0ai/mem0)
- [快速入门 / quickstart](https://docs.mem0.ai/quickstart)
- [模型说明 / model guide](https://docs.mem0.ai/components/llms/overview)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:53.148812Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "mem0",
    "name": "Mem0",
    "repository": "mem0ai/mem0",
    "repo_node_id": "R_kgDOJxtHSw",
    "category": "ai",
    "summary": {
      "zh-CN": "为智能体和应用提取、保存并检索用户、会话和任务记忆。",
      "en": "Extracts, stores and retrieves user, session and task memories for agents and applications."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:53.148812Z",
        "en": "2026-11-17T14:24:53.148812Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "让 AI 在后续任务中复用用户偏好和历史事实，降低跨会话重复说明；托管版与开源 SDK 能力不同。",
        "en": "Lets AI reuse preferences and historical facts in later tasks; the hosted platform and open-source SDK differ."
      },
      "source_url": "https://github.com/mem0ai/mem0/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/mem0ai/mem0/commit/f1791daa86d469249c9b002f62644d58a1eb96a0",
        "occurred_at": "2026-11-06T16:53:06Z",
        "reviewed_at": "2026-11-17T14:24:53.148812Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "fix(security): upgrade @azure/msal-node to 7.x via @azure/identity 4.14.1 (CVE-2026-109461) (#7850) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/mem0ai/mem0/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / GitHub metadata",
        "url": "https://api.github.com/repos/mem0ai/mem0"
      },
      {
        "title": "快速入门 / quickstart",
        "url": "https://docs.mem0.ai/quickstart"
      },
      {
        "title": "模型说明 / model guide",
        "url": "https://docs.mem0.ai/components/llms/overview"
      }
    ]
  },
  "snapshot": {
    "full_name": "mem0ai/mem0",
    "repo_node_id": "R_kgDOJxtHSw",
    "stargazers_count": 69107,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:38.289Z",
    "source_url": "https://api.github.com/repos/mem0ai/mem0"
  }
}
```

</details>
