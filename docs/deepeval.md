# DeepEval

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[confident-ai/deepeval](https://github.com/confident-ai/deepeval)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 19527 |
| 评估时间 / Evaluated at | 2026-11-17T14:27:35.789235Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:38.842Z |

## 中文

评测大语言模型应用、智能体轨迹和单步工具行为。

为 AI 开发加入任务完成度、检索和工具调用检查。

### 主要功能

- 评测应用输出和完整智能体轨迹。
- 检查模型调用、检索和子智能体交接。
- 将评测套件接入 CI/CD。

### 环境要求

- 需要 Python 3.10 或更新版本。
- 使用模型评分指标时，需要配置评分模型或自定义模型。

### 使用限制

- 模型评分会受评分模型和测试样本影响。
- 登录 Confident AI 后，测试用例会自动记录到平台。需核对数据记录设置。

### 开始使用

1. 按[入门指南](https://deepeval.com/docs/getting-started)安装工具。
2. 按[指标说明](https://deepeval.com/docs/metrics-introduction#using-a-custom-llm)选择评分模型。
3. 创建任务用例并运行评测套件。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:38.842Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-16 · commit](https://github.com/confident-ai/deepeval/commit/c0bd9c89f33853b2dedc7db8415b3036894fb204)。Merge pull request #3622 from ykocaogullar/main

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/confident-ai/deepeval/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/confident-ai/deepeval)
- [入门指南 / getting-started guide](https://deepeval.com/docs/getting-started)
- [指标说明 / metrics guide](https://deepeval.com/docs/metrics-introduction#using-a-custom-llm)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

Evaluates LLM applications, agent trajectories and individual steps using automated metrics.

Adds task-completion, retrieval and tool-use checks to AI development and regression testing.

### Features

- Evaluate application outputs and complete agent trajectories.
- Assess model calls, retrieval and subagent handoffs.
- Integrate evaluation suites into CI/CD.

### Requirements

- Requires Python 3.10 or later.
- Model-based metrics require a configured judge model or custom model.

### Limitations

- Model-based scores depend on the judge and test examples.
- After signing into Confident AI, test cases are automatically logged to the platform. Review data-logging settings.

### Getting started

1. Install the tool using the [getting-started guide](https://deepeval.com/docs/getting-started).
2. Choose a judge model using the [metrics guide](https://deepeval.com/docs/metrics-introduction#using-a-custom-llm).
3. Create task cases and run the evaluation suite.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:38.842Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-16 · commit](https://github.com/confident-ai/deepeval/commit/c0bd9c89f33853b2dedc7db8415b3036894fb204).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/confident-ai/deepeval/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/confident-ai/deepeval)
- [入门指南 / getting-started guide](https://deepeval.com/docs/getting-started)
- [指标说明 / metrics guide](https://deepeval.com/docs/metrics-introduction#using-a-custom-llm)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:27:35.789235Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "deepeval",
    "name": "DeepEval",
    "repository": "confident-ai/deepeval",
    "repo_node_id": "R_kgDOKFeYBA",
    "category": "development",
    "summary": {
      "zh-CN": "评测大语言模型应用、智能体轨迹和单步工具行为。",
      "en": "Evaluates LLM applications, agent trajectories and individual steps using automated metrics."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:27:35.789235Z",
        "en": "2026-11-17T14:27:35.789235Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "为 AI 开发加入任务完成度、检索和工具调用检查。",
        "en": "Adds task-completion, retrieval and tool-use checks to AI development and regression testing."
      },
      "source_url": "https://github.com/confident-ai/deepeval/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/confident-ai/deepeval/commit/c0bd9c89f33853b2dedc7db8415b3036894fb204",
        "occurred_at": "2026-11-16T00:36:10Z",
        "reviewed_at": "2026-11-17T14:27:35.789235Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "Merge pull request #3622 from ykocaogullar/main 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/confident-ai/deepeval/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / GitHub metadata",
        "url": "https://api.github.com/repos/confident-ai/deepeval"
      },
      {
        "title": "入门指南 / getting-started guide",
        "url": "https://deepeval.com/docs/getting-started"
      },
      {
        "title": "指标说明 / metrics guide",
        "url": "https://deepeval.com/docs/metrics-introduction#using-a-custom-llm"
      }
    ]
  },
  "snapshot": {
    "full_name": "confident-ai/deepeval",
    "repo_node_id": "R_kgDOKFeYBA",
    "stargazers_count": 19527,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:38.842Z",
    "source_url": "https://api.github.com/repos/confident-ai/deepeval"
  }
}
```

</details>
