# SGLang

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[sgl-project/sglang](https://github.com/sgl-project/sglang)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 38977 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.603989Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:28.396Z |

## 中文

面向语言、多模态和扩散模型的推理框架。

为智能体服务、大规模模型调用及强化学习采样提供运行后端。

### 主要功能

- 运行语言模型与视觉语言模型服务。
- 内置 SGLang Diffusion，用于图像、视频、音频及动作生成。
- 提供多种硬件运行路径，并与训练和部署框架集成。

### 环境要求

- 可使用官方 Docker 镜像或 Python 环境安装。
- 需按硬件指南选择后端，并准备兼容的模型权重。

### 使用限制

- 各硬件平台的模型与功能支持不同；列为集成中的平台不能视为已支持。
- 服务容量依赖模型、上下文和并发配置，应测试实际负载。

### 开始使用

1. 按[快速开始](https://docs.sglang.io/docs/get-started/quickstart)安装依赖。
2. 在 [Cookbook](https://cookbook.sglang.io/) 中选择匹配模型与硬件的配置。
3. 启动模型并发送测试请求，再调整并发和资源配置。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:28.396Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/sgl-project/sglang/commit/703e763d5f3af75ea3587275d79155c28d3c5d4f)。[Perf] [AMD] qwen3: Fuse prefill QK-norm + RoPE on ROCm with the JIT qknorm_rope kernel (#47052)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://github.com/sgl-project/sglang/blob/main/README.md)
- [Quickstart](https://docs.sglang.io/docs/get-started/quickstart)
- [Cookbook](https://cookbook.sglang.io/)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

An inference framework for language, multimodal, and diffusion models.

Provides a runtime for agent serving, large-scale model requests, and reinforcement-learning rollouts.

### Features

- Serves language and vision-language models.
- Includes SGLang Diffusion for image, video, audio, and action generation.
- Provides multiple hardware execution paths and integrates with training and deployment frameworks.

### Requirements

- Install with an official Docker image or in a Python environment.
- Choose a backend using the hardware guide and prepare compatible model weights.

### Limitations

- Model and feature support vary by hardware; platforms marked as work in progress are not established support.
- Serving capacity depends on the model, context, and concurrency settings; test the real workload.

### Getting started

1. Install dependencies using the [quickstart](https://docs.sglang.io/docs/get-started/quickstart).
2. Choose a configuration matching the model and hardware in the [Cookbook](https://cookbook.sglang.io/).
3. Start the model and send a test request, then tune concurrency and resources.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:28.396Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/sgl-project/sglang/commit/703e763d5f3af75ea3587275d79155c28d3c5d4f).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://github.com/sgl-project/sglang/blob/main/README.md)
- [Quickstart](https://docs.sglang.io/docs/get-started/quickstart)
- [Cookbook](https://cookbook.sglang.io/)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.603989Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "sglang",
    "name": "SGLang",
    "repository": "sgl-project/sglang",
    "repo_node_id": "R_kgDOLCAjRg",
    "category": "ai",
    "summary": {
      "zh-CN": "面向语言、多模态和扩散模型的推理框架。",
      "en": "An inference framework for language, multimodal, and diffusion models."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.603989Z",
        "en": "2026-11-17T14:24:07.603989Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "为智能体服务、大规模模型调用及强化学习采样提供运行后端。",
        "en": "Provides a runtime for agent serving, large-scale model requests, and reinforcement-learning rollouts."
      },
      "source_url": "https://github.com/sgl-project/sglang/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/sgl-project/sglang/commit/703e763d5f3af75ea3587275d79155c28d3c5d4f",
        "occurred_at": "2026-11-17T11:19:50Z",
        "reviewed_at": "2026-11-17T14:24:07.603989Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "[Perf] [AMD] qwen3: Fuse prefill QK-norm + RoPE on ROCm with the JIT qknorm_rope kernel (#47052) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/sgl-project/sglang/blob/main/README.md"
      },
      {
        "title": "Quickstart",
        "url": "https://docs.sglang.io/docs/get-started/quickstart"
      },
      {
        "title": "Cookbook",
        "url": "https://cookbook.sglang.io/"
      }
    ]
  },
  "snapshot": {
    "full_name": "sgl-project/sglang",
    "repo_node_id": "R_kgDOLCAjRg",
    "stargazers_count": 38977,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:28.396Z",
    "source_url": "https://api.github.com/repos/sgl-project/sglang"
  }
}
```

</details>
