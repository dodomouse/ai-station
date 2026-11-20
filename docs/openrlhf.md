# OpenRLHF

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[OpenRLHF/OpenRLHF](https://github.com/OpenRLHF/OpenRLHF)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 10162 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.604741Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:27.782Z |

## 中文

基于 Ray、vLLM 和 DeepSpeed 的语言模型强化学习训练框架。

用奖励模型、自定义奖励或多轮环境交互训练模型行为。

### 主要功能

- 支持监督微调和奖励建模。强化学习方法包括 PPO 和 GRPO。
- 通过 Ray 调度训练与采样组件，并以 vLLM 生成样本。
- 支持单轮与多轮智能体执行、自定义奖励和异步训练。

### 环境要求

- 需准备匹配的 GPU、模型权重和训练数据；官方推荐 Docker 环境。
- 分布式流程依赖 Ray、vLLM、DeepSpeed 及对应通信组件。

### 使用限制

- 异步模式可能影响训练稳定性，官方要求验证收敛后再采用。
- 数据字段、聊天模板和奖励接口必须与所选任务匹配。

### 开始使用

1. 按[快速开始](https://github.com/OpenRLHF/OpenRLHF#quick-start)准备容器和依赖。
2. 配置模型、数据字段与奖励，选择[官方脚本](https://github.com/OpenRLHF/OpenRLHF/tree/main/examples/scripts)。
3. 先验证训练与评测结果，再调整并行布局或异步模式。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:27.782Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-03 · commit](https://github.com/OpenRLHF/OpenRLHF/commit/26494490bc237f6c3af62dab6117e6bbb0a78dba)。docs: make the Molt recommendation concise and actionable (#1391)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://github.com/OpenRLHF/OpenRLHF/blob/main/README.md)
- [Documentation](https://openrlhf.readthedocs.io/)
- [Training examples](https://github.com/OpenRLHF/OpenRLHF/tree/main/examples/scripts)

## English

A language-model reinforcement-learning framework built on Ray, vLLM, and DeepSpeed.

Trains model behavior using reward models, custom rewards, or multi-turn environment interactions.

### Features

- Provides supervised fine-tuning, reward modeling, and methods such as PPO and GRPO.
- Schedules training and rollout components with Ray and generates samples with vLLM.
- Supports single-turn and multi-turn agent execution, custom rewards, and asynchronous training.

### Requirements

- Prepare compatible GPUs, model weights, and training data; Docker is the recommended environment.
- Distributed workflows depend on Ray, vLLM, DeepSpeed, and matching communication components.

### Limitations

- Asynchronous mode can affect training stability; the documentation calls for validating convergence before adoption.
- Data fields, chat templates, and reward interfaces must match the selected task.

### Getting started

1. Prepare a container and dependencies using the [quickstart](https://github.com/OpenRLHF/OpenRLHF#quick-start).
2. Configure models, data fields, and rewards, then choose an [official script](https://github.com/OpenRLHF/OpenRLHF/tree/main/examples/scripts).
3. Validate training and evaluation results before changing parallel placement or asynchronous execution.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:27.782Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-03 · commit](https://github.com/OpenRLHF/OpenRLHF/commit/26494490bc237f6c3af62dab6117e6bbb0a78dba).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://github.com/OpenRLHF/OpenRLHF/blob/main/README.md)
- [Documentation](https://openrlhf.readthedocs.io/)
- [Training examples](https://github.com/OpenRLHF/OpenRLHF/tree/main/examples/scripts)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.604741Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "openrlhf",
    "name": "OpenRLHF",
    "repository": "OpenRLHF/OpenRLHF",
    "repo_node_id": "R_kgDOKBQ9ow",
    "category": "ai",
    "summary": {
      "zh-CN": "基于 Ray、vLLM 和 DeepSpeed 的语言模型强化学习训练框架。",
      "en": "A language-model reinforcement-learning framework built on Ray, vLLM, and DeepSpeed."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.604741Z",
        "en": "2026-11-17T14:24:07.604741Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "用奖励模型、自定义奖励或多轮环境交互训练模型行为。",
        "en": "Trains model behavior using reward models, custom rewards, or multi-turn environment interactions."
      },
      "source_url": "https://github.com/OpenRLHF/OpenRLHF/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/OpenRLHF/OpenRLHF/commit/26494490bc237f6c3af62dab6117e6bbb0a78dba",
        "occurred_at": "2026-11-03T03:17:18Z",
        "reviewed_at": "2026-11-17T14:24:07.604741Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "docs: make the Molt recommendation concise and actionable (#1391) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/OpenRLHF/OpenRLHF/blob/main/README.md"
      },
      {
        "title": "Documentation",
        "url": "https://openrlhf.readthedocs.io/"
      },
      {
        "title": "Training examples",
        "url": "https://github.com/OpenRLHF/OpenRLHF/tree/main/examples/scripts"
      }
    ]
  },
  "snapshot": {
    "full_name": "OpenRLHF/OpenRLHF",
    "repo_node_id": "R_kgDOKBQ9ow",
    "stargazers_count": 10162,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:27.782Z",
    "source_url": "https://api.github.com/repos/OpenRLHF/OpenRLHF"
  }
}
```

</details>
