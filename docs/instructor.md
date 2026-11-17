# Instructor

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[567-labs/instructor](https://github.com/567-labs/instructor)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 14118 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:53.149019Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:38.587Z |

## 中文

基于 Pydantic 将模型响应解析为有类型的数据，并处理校验失败和重试。

让 AI 从文本提取可验证的结构化字段，便于后续工具调用、表单和数据处理。

### 主要功能

- 用 Pydantic 定义输出结构。
- 校验返回值并重试失败的抽取。
- 处理嵌套对象及流式部分结果。

### 环境要求

- 需要 Python、Pydantic 及所选模型客户端。
- 需要配置模型服务访问方式。

### 使用限制

- 结构校验不能保证抽取事实正确。重试可能增加调用量。
- Instructor 聚焦数据抽取，不提供完整智能体编排。

### 开始使用

1. 按[官方文档](https://python.useinstructor.com)安装并配置客户端。
2. 从[示例](https://python.useinstructor.com/examples/)选择结构化抽取任务。
3. 定义输出类型并核对返回字段。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:38.587Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-15 · commit](https://github.com/567-labs/instructor/commit/1e85ddf38807084182aeefb5bb67f4deee821163)。fix: 1.18 community batch (CLI, batch, token limits, providers, DSL) (#3056)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/567-labs/instructor/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/567-labs/instructor)
- [官方文档 / official docs](https://python.useinstructor.com)
- [示例 / examples](https://python.useinstructor.com/examples/)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

Parses model responses into typed data with Pydantic, validation and retries.

Helps AI extract validated fields from text for tools, forms and data-processing workflows.

### Features

- Define output schemas with Pydantic.
- Validate responses and retry failed extractions.
- Handle nested objects and partial streaming results.

### Requirements

- Requires Python, Pydantic and a client for the selected model.
- Model-service access must be configured.

### Limitations

- Schema validation does not guarantee factual extraction accuracy. Retries may increase model calls.
- Instructor focuses on extraction rather than complete agent orchestration.

### Getting started

1. Install and configure a client using the [official docs](https://python.useinstructor.com).
2. Choose an extraction task from the [examples](https://python.useinstructor.com/examples/).
3. Define the output type and verify the returned fields.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:38.587Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-15 · commit](https://github.com/567-labs/instructor/commit/1e85ddf38807084182aeefb5bb67f4deee821163).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/567-labs/instructor/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/567-labs/instructor)
- [官方文档 / official docs](https://python.useinstructor.com)
- [示例 / examples](https://python.useinstructor.com/examples/)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:53.149019Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "instructor",
    "name": "Instructor",
    "repository": "567-labs/instructor",
    "repo_node_id": "R_kgDOJvT6bg",
    "category": "development",
    "summary": {
      "zh-CN": "基于 Pydantic 将模型响应解析为有类型的数据，并处理校验失败和重试。",
      "en": "Parses model responses into typed data with Pydantic, validation and retries."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:53.149019Z",
        "en": "2026-11-17T14:24:53.149019Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "让 AI 从文本提取可验证的结构化字段，便于后续工具调用、表单和数据处理。",
        "en": "Helps AI extract validated fields from text for tools, forms and data-processing workflows."
      },
      "source_url": "https://github.com/567-labs/instructor/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/567-labs/instructor/commit/1e85ddf38807084182aeefb5bb67f4deee821163",
        "occurred_at": "2026-11-15T02:21:50Z",
        "reviewed_at": "2026-11-17T14:24:53.149019Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "fix: 1.18 community batch (CLI, batch, token limits, providers, DSL) (#3056) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/567-labs/instructor/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / GitHub metadata",
        "url": "https://api.github.com/repos/567-labs/instructor"
      },
      {
        "title": "官方文档 / official docs",
        "url": "https://python.useinstructor.com"
      },
      {
        "title": "示例 / examples",
        "url": "https://python.useinstructor.com/examples/"
      }
    ]
  },
  "snapshot": {
    "full_name": "567-labs/instructor",
    "repo_node_id": "R_kgDOJvT6bg",
    "stargazers_count": 14118,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:38.587Z",
    "source_url": "https://api.github.com/repos/567-labs/instructor"
  }
}
```

</details>
