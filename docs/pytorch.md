# PyTorch

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[pytorch/pytorch](https://github.com/pytorch/pytorch)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 105706 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.604817Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:29.353Z |

## 中文

提供张量计算、自动微分和神经网络组件的深度学习框架。

为模型开发、训练、推理和自定义算子实验提供基础计算能力。

### 主要功能

- 在 CPU 和受支持的加速器上执行张量运算。
- 用自动微分与 `torch.nn` 构建和训练神经网络。
- 提供数据加载、多进程及 C++ 扩展接口。

### 环境要求

- 需要匹配操作系统、Python 版本和计算后端的安装包。
- 源码编译需另行准备编译器及相应后端工具链。

### 使用限制

- 不同平台和后端的算子支持不同，需核对安装选项与模型依赖。
- 框架不附带完整任务模型和训练数据，具体资源需求取决于工作负载。

### 开始使用

1. 用[官方安装选择器](https://pytorch.org/get-started/locally/)选择匹配环境的版本。
2. 按[基础教程](https://pytorch.org/tutorials/beginner/basics/intro.html)运行张量、数据加载和训练示例。
3. 替换成目标数据与模型，检查设备使用和评测结果。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:29.353Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/pytorch/pytorch/commit/6af6987aa3603504c75df85c0906be686e0b8454)。[CD] Remove redundant libgomp NEEDED replacement (#201032)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://github.com/pytorch/pytorch/blob/main/README.md)
- [Installation](https://pytorch.org/get-started/locally/)
- [Basics](https://pytorch.org/tutorials/beginner/basics/intro.html)

## English

A deep-learning framework providing tensor computation, automatic differentiation, and neural-network components.

Provides the computational foundation for model development, training, inference, and custom-operator experiments.

### Features

- Executes tensor operations on CPUs and supported accelerators.
- Builds and trains neural networks with automatic differentiation and `torch.nn`.
- Provides data loading, multiprocessing, and C++ extension interfaces.

### Requirements

- Requires a package matching the operating system, Python version, and compute backend.
- Source builds also require a compiler and the relevant backend toolchain.

### Limitations

- Operator support differs across platforms and backends; check installation options and model dependencies.
- The framework does not supply complete task models or training data; resource needs depend on the workload.

### Getting started

1. Select a compatible version using the [official installation selector](https://pytorch.org/get-started/locally/).
2. Run tensor, data-loading, and training examples from the [basics tutorial](https://pytorch.org/tutorials/beginner/basics/intro.html).
3. Substitute target data and models, then inspect device use and evaluation results.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:29.353Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/pytorch/pytorch/commit/6af6987aa3603504c75df85c0906be686e0b8454).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://github.com/pytorch/pytorch/blob/main/README.md)
- [Installation](https://pytorch.org/get-started/locally/)
- [Basics](https://pytorch.org/tutorials/beginner/basics/intro.html)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.604817Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "pytorch",
    "name": "PyTorch",
    "repository": "pytorch/pytorch",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnk2NTYwMDk3NQ==",
    "category": "development",
    "summary": {
      "zh-CN": "提供张量计算、自动微分和神经网络组件的深度学习框架。",
      "en": "A deep-learning framework providing tensor computation, automatic differentiation, and neural-network components."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.604817Z",
        "en": "2026-11-17T14:24:07.604817Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "为模型开发、训练、推理和自定义算子实验提供基础计算能力。",
        "en": "Provides the computational foundation for model development, training, inference, and custom-operator experiments."
      },
      "source_url": "https://github.com/pytorch/pytorch/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/pytorch/pytorch/commit/6af6987aa3603504c75df85c0906be686e0b8454",
        "occurred_at": "2026-11-17T12:59:02Z",
        "reviewed_at": "2026-11-17T14:24:07.604817Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "[CD] Remove redundant libgomp NEEDED replacement (#201032) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/pytorch/pytorch/blob/main/README.md"
      },
      {
        "title": "Installation",
        "url": "https://pytorch.org/get-started/locally/"
      },
      {
        "title": "Basics",
        "url": "https://pytorch.org/tutorials/beginner/basics/intro.html"
      }
    ]
  },
  "snapshot": {
    "full_name": "pytorch/pytorch",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnk2NTYwMDk3NQ==",
    "stargazers_count": 105706,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:29.353Z",
    "source_url": "https://api.github.com/repos/pytorch/pytorch"
  }
}
```

</details>
