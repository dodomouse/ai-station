# DeerFlow

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[bytedance/deer-flow](https://github.com/bytedance/deer-flow)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 85439 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:53.147497Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:38.337Z |

## 中文

组合子智能体、记忆、技能和沙箱执行较长的任务。

适合研究、编程和内容制作，能够把复杂工作拆成多个执行步骤。

### 主要功能

- 用子智能体分工执行任务。
- 通过技能扩展工具与工作方法。
- 在沙箱中运行命令并处理文件。

### 环境要求

- 按官方指南选择 Docker 或本地部署。
- 配置真实模型凭据。本地前端使用仓库固定的 pnpm 版本。

### 使用限制

- DeerFlow 可读写文件并执行命令。Gateway 管理账户具有宿主机代码执行能力。
- 2.0 是重写版本；旧版研究框架位于 main-1.x 分支。

### 开始使用

1. 按[部署指南](https://github.com/bytedance/deer-flow/blob/main/docs/guide/deployment.md)准备环境。
2. 配置模型后，按 README 运行 `make doctor`。
3. 阅读[安全说明](https://github.com/bytedance/deer-flow/blob/main/docs/guide/security.md)，再测试文件任务。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:38.337Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/bytedance/deer-flow/commit/3751eb8daf491324e728f63bcc773e0f081eb7e5)。feat(extensions): pass a task's final status, error, goal verdict and run metadata to on_task_stop (#8304)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/bytedance/deer-flow/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/bytedance/deer-flow)
- [部署指南 / deployment guide](https://github.com/bytedance/deer-flow/blob/main/docs/guide/deployment.md)
- [安全说明 / security notice](https://github.com/bytedance/deer-flow/blob/main/docs/guide/security.md)

## English

Combines subagents, memory, skills and sandboxes to carry out extended tasks.

Supports research, coding and content creation by splitting complex work into executable steps.

### Features

- Delegate task steps to subagents.
- Extend tools and working procedures through skills.
- Run commands and process files in a sandbox.

### Requirements

- Choose Docker or local deployment using the official guide.
- Configure valid model credentials. Local frontend setup uses the repository-pinned pnpm version.

### Limitations

- DeerFlow can read/write files and execute commands. A Gateway administrator account has host code-execution capability.
- Version 2.0 is a rewrite; the earlier research framework lives on the main-1.x branch.

### Getting started

1. Prepare the environment using the [deployment guide](https://github.com/bytedance/deer-flow/blob/main/docs/guide/deployment.md).
2. After configuring a model, run `make doctor` as described in the README.
3. Read the [security notice](https://github.com/bytedance/deer-flow/blob/main/docs/guide/security.md), then test a file task.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:38.337Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/bytedance/deer-flow/commit/3751eb8daf491324e728f63bcc773e0f081eb7e5).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/bytedance/deer-flow/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/bytedance/deer-flow)
- [部署指南 / deployment guide](https://github.com/bytedance/deer-flow/blob/main/docs/guide/deployment.md)
- [安全说明 / security notice](https://github.com/bytedance/deer-flow/blob/main/docs/guide/security.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:53.147497Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "deer-flow",
    "name": "DeerFlow",
    "repository": "bytedance/deer-flow",
    "repo_node_id": "R_kgDOOlwd1Q",
    "category": "ai",
    "summary": {
      "zh-CN": "组合子智能体、记忆、技能和沙箱执行较长的任务。",
      "en": "Combines subagents, memory, skills and sandboxes to carry out extended tasks."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:53.147497Z",
        "en": "2026-11-17T14:24:53.147497Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "适合研究、编程和内容制作，能够把复杂工作拆成多个执行步骤。",
        "en": "Supports research, coding and content creation by splitting complex work into executable steps."
      },
      "source_url": "https://github.com/bytedance/deer-flow/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/bytedance/deer-flow/commit/3751eb8daf491324e728f63bcc773e0f081eb7e5",
        "occurred_at": "2026-11-17T11:57:40Z",
        "reviewed_at": "2026-11-17T14:24:53.147497Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "feat(extensions): pass a task's final status, error, goal verdict and run metadata to on_task_stop (#8304) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/bytedance/deer-flow/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / GitHub metadata",
        "url": "https://api.github.com/repos/bytedance/deer-flow"
      },
      {
        "title": "部署指南 / deployment guide",
        "url": "https://github.com/bytedance/deer-flow/blob/main/docs/guide/deployment.md"
      },
      {
        "title": "安全说明 / security notice",
        "url": "https://github.com/bytedance/deer-flow/blob/main/docs/guide/security.md"
      }
    ]
  },
  "snapshot": {
    "full_name": "bytedance/deer-flow",
    "repo_node_id": "R_kgDOOlwd1Q",
    "stargazers_count": 85439,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:38.337Z",
    "source_url": "https://api.github.com/repos/bytedance/deer-flow"
  }
}
```

</details>
