# Guidance

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[guidance-ai/guidance](https://github.com/guidance-ai/guidance)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 21825 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:53.149208Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:39.670Z |

## 中文

在 Python 中组合生成、条件和循环，并使用正则或语法约束输出。

让 AI 按任务要求生成受约束的数据和文本，支持工具使用与分步控制；能力依赖模型后端。

### 主要功能

- 将条件、循环和生成步骤写在同一程序中。
- 使用正则表达式或上下文无关文法约束生成。
- 用 Mock 模型离线检查文法。

### 环境要求

- 需要 Python 和可用的模型后端。
- 可用后端包括 Transformers、llama.cpp 和 OpenAI。

### 使用限制

- 完整文法约束依赖后端支持，不能假定所有模型接口能力一致。
- 文法只限定输出形式，业务内容仍需验证。

### 开始使用

1. 按[安装说明](https://github.com/guidance-ai/guidance/blob/main/README.md#install)准备后端和库。
2. 按[功能示例](https://github.com/guidance-ai/guidance/blob/main/README.md#features)定义一个约束。
3. 先检查文法，再用目标模型测试输出。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:39.670Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-05 · pr](https://github.com/guidance-ai/guidance/pull/1559)。新建 PR：[Doc] Explain stop regex token boundaries

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/guidance-ai/guidance/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/guidance-ai/guidance)
- [安装说明 / installation instructions](https://github.com/guidance-ai/guidance/blob/main/README.md#install)
- [功能示例 / feature examples](https://github.com/guidance-ai/guidance/blob/main/README.md#features)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

Combines model generation with Python control flow and output constraints expressed as regex or grammars.

Helps AI generate task-specific structured text and data; supported constraints depend on the model backend.

### Features

- Combine conditions, loops and generation in one program.
- Constrain generation with regular expressions or context-free grammars.
- Check grammars offline with the Mock model.

### Requirements

- Requires Python and an available model backend.
- Supported backends include Transformers, llama.cpp and OpenAI.

### Limitations

- Full grammar constraints depend on backend support; model interfaces do not all provide identical capabilities.
- Grammars constrain output form; task content still needs validation.

### Getting started

1. Prepare a backend and the library using the [installation instructions](https://github.com/guidance-ai/guidance/blob/main/README.md#install).
2. Define a constraint using the [feature examples](https://github.com/guidance-ai/guidance/blob/main/README.md#features).
3. Check the grammar, then test output with the target model.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:39.670Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-05 · pr](https://github.com/guidance-ai/guidance/pull/1559).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/guidance-ai/guidance/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/guidance-ai/guidance)
- [安装说明 / installation instructions](https://github.com/guidance-ai/guidance/blob/main/README.md#install)
- [功能示例 / feature examples](https://github.com/guidance-ai/guidance/blob/main/README.md#features)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:53.149208Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "guidance",
    "name": "Guidance",
    "repository": "guidance-ai/guidance",
    "repo_node_id": "R_kgDOIaS4dw",
    "category": "development",
    "summary": {
      "zh-CN": "在 Python 中组合生成、条件和循环，并使用正则或语法约束输出。",
      "en": "Combines model generation with Python control flow and output constraints expressed as regex or grammars."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:53.149208Z",
        "en": "2026-11-17T14:24:53.149208Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "让 AI 按任务要求生成受约束的数据和文本，支持工具使用与分步控制；能力依赖模型后端。",
        "en": "Helps AI generate task-specific structured text and data; supported constraints depend on the model backend."
      },
      "source_url": "https://github.com/guidance-ai/guidance/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "pr",
        "url": "https://github.com/guidance-ai/guidance/pull/1559",
        "occurred_at": "2026-11-05T06:51:58Z",
        "reviewed_at": "2026-11-17T14:24:53.149208Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "新建 PR：[Doc] Explain stop regex token boundaries 此记录用于证明窗口内活动。",
          "en": "The recorded pr establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/guidance-ai/guidance/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / GitHub metadata",
        "url": "https://api.github.com/repos/guidance-ai/guidance"
      },
      {
        "title": "安装说明 / installation instructions",
        "url": "https://github.com/guidance-ai/guidance/blob/main/README.md#install"
      },
      {
        "title": "功能示例 / feature examples",
        "url": "https://github.com/guidance-ai/guidance/blob/main/README.md#features"
      }
    ]
  },
  "snapshot": {
    "full_name": "guidance-ai/guidance",
    "repo_node_id": "R_kgDOIaS4dw",
    "stargazers_count": 21825,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:39.670Z",
    "source_url": "https://api.github.com/repos/guidance-ai/guidance"
  }
}
```

</details>
