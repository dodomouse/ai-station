# Activepieces

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[activepieces/activepieces](https://github.com/activepieces/activepieces)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 自动化 / Automation |
| 状态 / Status | 已收录 / Included |
| Star | 25581 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:53.146814Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:37.918Z |

## 中文

用 TypeScript 集成组件和可视化流程构建 AI 自动化。

组件可作为 MCP 工具供模型调用，并支持分支、重试和人工审批。

### 主要功能

- 用可视化节点配置循环、分支和重试。
- 把集成组件发布为 MCP 工具。
- 通过聊天、表单或审批节点收集人工输入。

### 环境要求

- 使用浏览器访问流程编辑器。自托管环境按官方部署指南准备。
- 连接外部应用时，需要对应账户和访问权限。

### 使用限制

- 集成组件有各自的认证和接口限制。流程重试不消除外部服务的配额。

### 开始使用

1. 按[部署指南](https://www.activepieces.com/docs/install/overview)选择运行方式。
2. 按[官方文档](https://www.activepieces.com/docs)连接应用并创建流程。
3. 运行一个测试任务，检查分支和审批结果。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:37.918Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/activepieces/activepieces/commit/0f039962c863915544219ccf4ec60cec5091e4d7)。feat(web): redesign the ai provider connect dialog (#17573)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/activepieces/activepieces/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/activepieces/activepieces)
- [部署指南 / deployment guide](https://www.activepieces.com/docs/install/overview)
- [官方文档 / official docs](https://www.activepieces.com/docs)

## English

Builds AI automation with TypeScript integrations and a visual workflow editor.

Integration pieces can become MCP tools for models, with branches, retries and human approvals.

### Features

- Configure loops, branches and retries in a visual editor.
- Expose integration pieces as MCP tools.
- Collect human input through chat, forms or approval steps.

### Requirements

- Use a browser for the workflow editor. Prepare self-hosted infrastructure using the deployment guide.
- External app connections require the corresponding accounts and access permissions.

### Limitations

- Integrations have their own authentication and API limits. Workflow retries do not remove external service quotas.

### Getting started

1. Choose a deployment option in the [deployment guide](https://www.activepieces.com/docs/install/overview).
2. Connect an app and create a workflow using the [official docs](https://www.activepieces.com/docs).
3. Run a test task and inspect its branch and approval results.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:37.918Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/activepieces/activepieces/commit/0f039962c863915544219ccf4ec60cec5091e4d7).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/activepieces/activepieces/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/activepieces/activepieces)
- [部署指南 / deployment guide](https://www.activepieces.com/docs/install/overview)
- [官方文档 / official docs](https://www.activepieces.com/docs)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:53.146814Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "activepieces",
    "name": "Activepieces",
    "repository": "activepieces/activepieces",
    "repo_node_id": "R_kgDOIjFiOQ",
    "category": "automation",
    "summary": {
      "zh-CN": "用 TypeScript 集成组件和可视化流程构建 AI 自动化。",
      "en": "Builds AI automation with TypeScript integrations and a visual workflow editor."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:53.146814Z",
        "en": "2026-11-17T14:24:53.146814Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "组件可作为 MCP 工具供模型调用，并支持分支、重试和人工审批。",
        "en": "Integration pieces can become MCP tools for models, with branches, retries and human approvals."
      },
      "source_url": "https://github.com/activepieces/activepieces/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/activepieces/activepieces/commit/0f039962c863915544219ccf4ec60cec5091e4d7",
        "occurred_at": "2026-11-17T13:20:16Z",
        "reviewed_at": "2026-11-17T14:24:53.146814Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "feat(web): redesign the ai provider connect dialog (#17573) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/activepieces/activepieces/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / GitHub metadata",
        "url": "https://api.github.com/repos/activepieces/activepieces"
      },
      {
        "title": "部署指南 / deployment guide",
        "url": "https://www.activepieces.com/docs/install/overview"
      },
      {
        "title": "官方文档 / official docs",
        "url": "https://www.activepieces.com/docs"
      }
    ]
  },
  "snapshot": {
    "full_name": "activepieces/activepieces",
    "repo_node_id": "R_kgDOIjFiOQ",
    "stargazers_count": 25581,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:37.918Z",
    "source_url": "https://api.github.com/repos/activepieces/activepieces"
  }
}
```

</details>
