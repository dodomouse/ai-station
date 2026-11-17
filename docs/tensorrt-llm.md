# TensorRT-LLM

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[NVIDIA/TensorRT-LLM](https://github.com/NVIDIA/TensorRT-LLM)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 15084 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.603913Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:28.092Z |

## 中文

面向 NVIDIA GPU 的语言模型与视觉生成推理优化库。

用推理内核、缓存与并行策略构建模型服务。

### 主要功能

- 优化推理运算，包括注意力、矩阵乘法和混合专家运算。
- 提供预填充与解码分离、推测解码和并行执行。
- 用 Python LLM API 支持单 GPU、多 GPU 和多节点部署。

### 环境要求

- 需要支持矩阵列出的 NVIDIA GPU 与软件组合。
- 应按安装文档准备容器或 Python 环境及模型权重。

### 使用限制

- 模型、精度和并行功能的支持取决于硬件与版本，不能套用所有配置。
- 默认启用遥测；可按 README 的退出说明关闭。

### 开始使用

1. 先核对[支持矩阵](https://nvidia.github.io/TensorRT-LLM/reference/support-matrix.html)。
2. 按[安装指南](https://nvidia.github.io/TensorRT-LLM/installation/index.html)配置环境。
3. 运行[快速开始](https://nvidia.github.io/TensorRT-LLM/quick-start-guide.html)中的模型示例，再测试目标负载。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:28.092Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/NVIDIA/TensorRT-LLM/commit/b63aca8de25fe4989509e97678d968c393255cc6)。[https://nvbugs/7105739][fix] Restore generation-only perf-sanity coverage (#22438)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://github.com/NVIDIA/TensorRT-LLM/blob/main/README.md)
- [Support matrix](https://nvidia.github.io/TensorRT-LLM/reference/support-matrix.html)
- [Installation](https://nvidia.github.io/TensorRT-LLM/installation/index.html)
- [Quickstart](https://nvidia.github.io/TensorRT-LLM/quick-start-guide.html)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

An inference optimization library for language models and visual generation on NVIDIA GPUs.

Builds model services with inference kernels, caching, and parallelism strategies.

### Features

- Optimizes inference operations such as attention, matrix multiplication, and mixture-of-experts execution.
- Provides prefill/decode disaggregation, speculative decoding, and parallel execution.
- Supports single-GPU, multi-GPU, and multi-node deployment through a Python LLM API.

### Requirements

- Requires an NVIDIA GPU and software combination listed in the support matrix.
- Prepare a container or Python environment and model weights using the installation guide.

### Limitations

- Model, precision, and parallelism support depend on hardware and version; configurations are not universal.
- Telemetry is enabled by default and can be disabled using the README instructions.

### Getting started

1. Check the [support matrix](https://nvidia.github.io/TensorRT-LLM/reference/support-matrix.html).
2. Configure the environment using the [installation guide](https://nvidia.github.io/TensorRT-LLM/installation/index.html).
3. Run a model example from the [quickstart](https://nvidia.github.io/TensorRT-LLM/quick-start-guide.html), then test the target workload.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:28.092Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/NVIDIA/TensorRT-LLM/commit/b63aca8de25fe4989509e97678d968c393255cc6).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://github.com/NVIDIA/TensorRT-LLM/blob/main/README.md)
- [Support matrix](https://nvidia.github.io/TensorRT-LLM/reference/support-matrix.html)
- [Installation](https://nvidia.github.io/TensorRT-LLM/installation/index.html)
- [Quickstart](https://nvidia.github.io/TensorRT-LLM/quick-start-guide.html)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.603913Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "tensorrt-llm",
    "name": "TensorRT-LLM",
    "repository": "NVIDIA/TensorRT-LLM",
    "repo_node_id": "R_kgDOKH5Now",
    "category": "ai",
    "summary": {
      "zh-CN": "面向 NVIDIA GPU 的语言模型与视觉生成推理优化库。",
      "en": "An inference optimization library for language models and visual generation on NVIDIA GPUs."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.603913Z",
        "en": "2026-11-17T14:24:07.603913Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "用推理内核、缓存与并行策略构建模型服务。",
        "en": "Builds model services with inference kernels, caching, and parallelism strategies."
      },
      "source_url": "https://github.com/NVIDIA/TensorRT-LLM/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/NVIDIA/TensorRT-LLM/commit/b63aca8de25fe4989509e97678d968c393255cc6",
        "occurred_at": "2026-11-17T13:29:45Z",
        "reviewed_at": "2026-11-17T14:24:07.603913Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "[https://nvbugs/7105739][fix] Restore generation-only perf-sanity coverage (#22438) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/NVIDIA/TensorRT-LLM/blob/main/README.md"
      },
      {
        "title": "Support matrix",
        "url": "https://nvidia.github.io/TensorRT-LLM/reference/support-matrix.html"
      },
      {
        "title": "Installation",
        "url": "https://nvidia.github.io/TensorRT-LLM/installation/index.html"
      },
      {
        "title": "Quickstart",
        "url": "https://nvidia.github.io/TensorRT-LLM/quick-start-guide.html"
      }
    ]
  },
  "snapshot": {
    "full_name": "NVIDIA/TensorRT-LLM",
    "repo_node_id": "R_kgDOKH5Now",
    "stargazers_count": 15084,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:28.092Z",
    "source_url": "https://api.github.com/repos/NVIDIA/TensorRT-LLM"
  }
}
```

</details>
