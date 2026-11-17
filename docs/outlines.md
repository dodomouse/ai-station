# Outlines

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[dottxt-ai/outlines](https://github.com/dottxt-ai/outlines)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 16013 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:53.149110Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:39.202Z |

## 中文

用 Python 类型、Pydantic 模型和约束生成定义语言模型输出结构。

把 AI 输出约束为分类标签、数字或 JSON 对象，减少任务流水线中的格式解析失败。

### 主要功能

- 用类型声明分类标签、数字和对象结构。
- 连接本地或托管模型后端。
- 根据函数签名生成工具调用所需结构。

### 环境要求

- 需要 Python 环境及所选模型后端。
- 本地模型需要相应权重、推理依赖和运行资源。

### 使用限制

- 输出格式符合约束不代表内容事实正确。
- 不同模型后端的接入方式和约束支持需按文档核对。

### 开始使用

1. 按[README 快速入门](https://github.com/dottxt-ai/outlines/blob/main/README.md#quickstart)安装并连接模型。
2. 按[输出类型指南](https://dottxt-ai.github.io/outlines/latest/features/core/output_types/#basic-python-types)定义结构。
3. 用一组输入检查结构与业务字段。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:39.202Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-08-24 · commit](https://github.com/dottxt-ai/outlines/commit/c52af8472c6fe8a607a733ec11b709476af77a96)。Give the mypy hook urllib3 so the style check passes

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/dottxt-ai/outlines/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/dottxt-ai/outlines)
- [README 快速入门 / README quickstart](https://github.com/dottxt-ai/outlines/blob/main/README.md#quickstart)
- [输出类型指南 / output-type guide](https://dottxt-ai.github.io/outlines/latest/features/core/output_types/#basic-python-types)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

Defines model output structures using Python types, Pydantic models and constrained generation.

Constrains AI output to labels, numbers or JSON objects to reduce formatting failures in task pipelines.

### Features

- Declare classification labels, numbers and object structures with types.
- Connect local or hosted model backends.
- Derive tool-call structures from function signatures.

### Requirements

- Requires Python and the chosen model backend.
- Local models require their weights, inference dependencies and runtime resources.

### Limitations

- Conforming to an output format does not establish factual correctness.
- Check integration methods and constraint support for each model backend.

### Getting started

1. Install and connect a model using the [README quickstart](https://github.com/dottxt-ai/outlines/blob/main/README.md#quickstart).
2. Define a structure using the [output-type guide](https://dottxt-ai.github.io/outlines/latest/features/core/output_types/#basic-python-types).
3. Check the structure and task-specific fields using a set of inputs.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:39.202Z meets the total-Star threshold of 1,000.

Recent activity: [2026-08-24 · commit](https://github.com/dottxt-ai/outlines/commit/c52af8472c6fe8a607a733ec11b709476af77a96).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/dottxt-ai/outlines/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/dottxt-ai/outlines)
- [README 快速入门 / README quickstart](https://github.com/dottxt-ai/outlines/blob/main/README.md#quickstart)
- [输出类型指南 / output-type guide](https://dottxt-ai.github.io/outlines/latest/features/core/output_types/#basic-python-types)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:53.149110Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "outlines",
    "name": "Outlines",
    "repository": "dottxt-ai/outlines",
    "repo_node_id": "R_kgDOJK5PTA",
    "category": "development",
    "summary": {
      "zh-CN": "用 Python 类型、Pydantic 模型和约束生成定义语言模型输出结构。",
      "en": "Defines model output structures using Python types, Pydantic models and constrained generation."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:53.149110Z",
        "en": "2026-11-17T14:24:53.149110Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "把 AI 输出约束为分类标签、数字或 JSON 对象，减少任务流水线中的格式解析失败。",
        "en": "Constrains AI output to labels, numbers or JSON objects to reduce formatting failures in task pipelines."
      },
      "source_url": "https://github.com/dottxt-ai/outlines/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/dottxt-ai/outlines/commit/c52af8472c6fe8a607a733ec11b709476af77a96",
        "occurred_at": "2026-08-24T14:20:14Z",
        "reviewed_at": "2026-11-17T14:24:53.149110Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "Give the mypy hook urllib3 so the style check passes 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/dottxt-ai/outlines/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / GitHub metadata",
        "url": "https://api.github.com/repos/dottxt-ai/outlines"
      },
      {
        "title": "README 快速入门 / README quickstart",
        "url": "https://github.com/dottxt-ai/outlines/blob/main/README.md#quickstart"
      },
      {
        "title": "输出类型指南 / output-type guide",
        "url": "https://dottxt-ai.github.io/outlines/latest/features/core/output_types/#basic-python-types"
      }
    ]
  },
  "snapshot": {
    "full_name": "dottxt-ai/outlines",
    "repo_node_id": "R_kgDOJK5PTA",
    "stargazers_count": 16013,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:39.202Z",
    "source_url": "https://api.github.com/repos/dottxt-ai/outlines"
  }
}
```

</details>
