# MLX

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[ml-explore/mlx](https://github.com/ml-explore/mlx)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 29192 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.604587Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:27.579Z |

## 中文

提供数组计算、自动微分和神经网络组件的机器学习框架。

用于构建、训练和运行模型，尤其适合探索 Apple 芯片上的模型计算。

### 主要功能

- 提供接近 NumPy 的数组接口及神经网络、优化器组件。
- 支持自动微分、向量化和计算图优化。
- 采用惰性计算，并在 Apple 芯片上利用统一内存。

### 环境要求

- macOS 可安装 MLX 包；Linux 有 CUDA 与仅 CPU 的安装选项。
- 按目标后端准备系统环境；也可从源码构建 C++ 或 Python 接口。

### 使用限制

- 不同平台的安装包和硬件路径不同，Apple 统一内存特性不能直接推广到所有后端。
- MLX 是计算框架，具体模型需另行实现或采用示例项目。

### 开始使用

1. 按[安装文档](https://ml-explore.github.io/mlx/build/html/install.html)选择平台后端。
2. 完成[快速开始](https://ml-explore.github.io/mlx/build/html/usage/quick_start.html)中的数组和自动微分示例。
3. 从[模型示例](https://github.com/ml-explore/mlx-examples)选择任务，并检查目标设备上的运行结果。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:27.579Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/ml-explore/mlx/commit/fbedcee5f4a0c7b2cbb642ea91d4c555460d3e48)。Fix: Respect dtype for array values in mx.full (#4901)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://github.com/ml-explore/mlx/blob/main/README.md)
- [Installation](https://ml-explore.github.io/mlx/build/html/install.html)
- [Quickstart](https://ml-explore.github.io/mlx/build/html/usage/quick_start.html)
- [Examples](https://github.com/ml-explore/mlx-examples)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

A machine-learning framework providing array computation, automatic differentiation, and neural-network components.

Supports building, training, and running models, including research into model computation on Apple silicon.

### Features

- Provides NumPy-like array interfaces plus neural-network and optimizer components.
- Supports automatic differentiation, vectorization, and computation-graph optimization.
- Uses lazy computation and unified memory on Apple silicon.

### Requirements

- macOS supports the MLX package; Linux offers CUDA and CPU-only installation options.
- Prepare the system for the target backend, or build C++ or Python interfaces from source.

### Limitations

- Packages and hardware paths vary by platform; Apple unified-memory behavior should not be generalized to every backend.
- MLX is a compute framework; models must be implemented separately or obtained from example projects.

### Getting started

1. Choose a platform backend using the [installation guide](https://ml-explore.github.io/mlx/build/html/install.html).
2. Complete the array and automatic-differentiation examples in the [quickstart](https://ml-explore.github.io/mlx/build/html/usage/quick_start.html).
3. Choose a task from the [model examples](https://github.com/ml-explore/mlx-examples) and inspect its behavior on the target device.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:27.579Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/ml-explore/mlx/commit/fbedcee5f4a0c7b2cbb642ea91d4c555460d3e48).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://github.com/ml-explore/mlx/blob/main/README.md)
- [Installation](https://ml-explore.github.io/mlx/build/html/install.html)
- [Quickstart](https://ml-explore.github.io/mlx/build/html/usage/quick_start.html)
- [Examples](https://github.com/ml-explore/mlx-examples)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.604587Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "mlx",
    "name": "MLX",
    "repository": "ml-explore/mlx",
    "repo_node_id": "R_kgDOKzRn1w",
    "category": "development",
    "summary": {
      "zh-CN": "提供数组计算、自动微分和神经网络组件的机器学习框架。",
      "en": "A machine-learning framework providing array computation, automatic differentiation, and neural-network components."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.604587Z",
        "en": "2026-11-17T14:24:07.604587Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "用于构建、训练和运行模型，尤其适合探索 Apple 芯片上的模型计算。",
        "en": "Supports building, training, and running models, including research into model computation on Apple silicon."
      },
      "source_url": "https://github.com/ml-explore/mlx/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/ml-explore/mlx/commit/fbedcee5f4a0c7b2cbb642ea91d4c555460d3e48",
        "occurred_at": "2026-11-17T12:34:13Z",
        "reviewed_at": "2026-11-17T14:24:07.604587Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "Fix: Respect dtype for array values in mx.full (#4901) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/ml-explore/mlx/blob/main/README.md"
      },
      {
        "title": "Installation",
        "url": "https://ml-explore.github.io/mlx/build/html/install.html"
      },
      {
        "title": "Quickstart",
        "url": "https://ml-explore.github.io/mlx/build/html/usage/quick_start.html"
      },
      {
        "title": "Examples",
        "url": "https://github.com/ml-explore/mlx-examples"
      }
    ]
  },
  "snapshot": {
    "full_name": "ml-explore/mlx",
    "repo_node_id": "R_kgDOKzRn1w",
    "stargazers_count": 29192,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:27.579Z",
    "source_url": "https://api.github.com/repos/ml-explore/mlx"
  }
}
```

</details>
