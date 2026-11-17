# verl

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[verl-project/verl](https://github.com/verl-project/verl)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 24264 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.604893Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:26.960Z |

## 中文

将模型训练、采样和奖励计算组合成强化学习流程的库。

为语言模型的数学、代码及多轮工具任务开展后训练。

### 主要功能

- 支持监督微调及强化学习流程，例如 PPO 和 GRPO。
- 组合训练与采样后端，例如 FSDP、Megatron-LM、vLLM 和 SGLang。
- 支持函数奖励、模型奖励及带工具调用的多轮任务。

### 环境要求

- 需要匹配的加速器环境、训练后端、采样后端和模型权重。
- 需准备后训练数据与奖励函数，并配置设备分配。

### 使用限制

- 算法配方可能固定到特定标签或提交，应读取对应的 `REQUIRED_VERL.txt`。
- 主线 PPO 已移除 V0 训练器；全异步和 one-step-off 训练器已移至独立配方仓库。

### 开始使用

1. 按[安装说明](https://verl.readthedocs.io/en/latest/start/install.html)选择后端组合。
2. 按[数据准备](https://verl.readthedocs.io/en/latest/preparation/prepare_data.html)配置数据与奖励。
3. 运行[快速开始](https://verl.readthedocs.io/en/latest/start/quickstart.html)，检查训练曲线和评测结果。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:26.960Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/verl-project/verl/commit/cc35929bf8eedf5f3eb7c4ace3441dfd9f6d4c0e)。[perf] feat: mstx profiler support schedule to actor update mini batch (#8687)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://github.com/verl-project/verl/blob/main/README.md)
- [Installation](https://verl.readthedocs.io/en/latest/start/install.html)
- [Data preparation](https://verl.readthedocs.io/en/latest/preparation/prepare_data.html)
- [Quickstart](https://verl.readthedocs.io/en/latest/start/quickstart.html)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

A library for composing reinforcement-learning workflows from model training, rollout generation, and reward computation.

Supports language-model post-training for math, code, and multi-turn tool tasks.

### Features

- Provides PPO, GRPO, and other training workflows plus supervised fine-tuning.
- Combines training backends such as FSDP and Megatron-LM with vLLM or SGLang rollout backends.
- Supports function-based rewards, model-based rewards, and multi-turn tasks with tool calls.

### Requirements

- Requires compatible accelerators, training and rollout backends, and model weights.
- Prepare post-training data and reward functions and configure device placement.

### Limitations

- Algorithm recipes may pin a tag or commit; read the corresponding `REQUIRED_VERL.txt`.
- Mainline PPO has removed the V0 trainer; fully asynchronous and one-step-off trainers moved to a separate recipe repository.

### Getting started

1. Choose a backend combination using the [installation guide](https://verl.readthedocs.io/en/latest/start/install.html).
2. Configure data and rewards using the [data preparation guide](https://verl.readthedocs.io/en/latest/preparation/prepare_data.html).
3. Run the [quickstart](https://verl.readthedocs.io/en/latest/start/quickstart.html) and inspect training curves and evaluation results.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:26.960Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/verl-project/verl/commit/cc35929bf8eedf5f3eb7c4ace3441dfd9f6d4c0e).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://github.com/verl-project/verl/blob/main/README.md)
- [Installation](https://verl.readthedocs.io/en/latest/start/install.html)
- [Data preparation](https://verl.readthedocs.io/en/latest/preparation/prepare_data.html)
- [Quickstart](https://verl.readthedocs.io/en/latest/start/quickstart.html)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.604893Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "verl",
    "name": "verl",
    "repository": "verl-project/verl",
    "repo_node_id": "R_kgDONIZfbg",
    "category": "ai",
    "summary": {
      "zh-CN": "将模型训练、采样和奖励计算组合成强化学习流程的库。",
      "en": "A library for composing reinforcement-learning workflows from model training, rollout generation, and reward computation."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.604893Z",
        "en": "2026-11-17T14:24:07.604893Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "为语言模型的数学、代码及多轮工具任务开展后训练。",
        "en": "Supports language-model post-training for math, code, and multi-turn tool tasks."
      },
      "source_url": "https://github.com/verl-project/verl/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/verl-project/verl/commit/cc35929bf8eedf5f3eb7c4ace3441dfd9f6d4c0e",
        "occurred_at": "2026-11-17T11:15:47Z",
        "reviewed_at": "2026-11-17T14:24:07.604893Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "[perf] feat: mstx profiler support schedule to actor update mini batch (#8687) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/verl-project/verl/blob/main/README.md"
      },
      {
        "title": "Installation",
        "url": "https://verl.readthedocs.io/en/latest/start/install.html"
      },
      {
        "title": "Data preparation",
        "url": "https://verl.readthedocs.io/en/latest/preparation/prepare_data.html"
      },
      {
        "title": "Quickstart",
        "url": "https://verl.readthedocs.io/en/latest/start/quickstart.html"
      }
    ]
  },
  "snapshot": {
    "full_name": "verl-project/verl",
    "repo_node_id": "R_kgDONIZfbg",
    "stargazers_count": 24264,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:26.960Z",
    "source_url": "https://api.github.com/repos/verl-project/verl"
  }
}
```

</details>
