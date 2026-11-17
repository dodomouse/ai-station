# Triton Inference Server

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[triton-inference-server/server](https://github.com/triton-inference-server/server)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 部署与运维 / Operations |
| 状态 / Status | 已收录 / Included |
| Star | 11146 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.604063Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:27.834Z |

## 中文

统一部署和调用多种机器学习模型的推理服务器。

将模型包装成可监控的服务，供 AI 应用和流水线调用。

### 主要功能

- 接入多种模型后端，包括 TensorRT、PyTorch、ONNX 和 Python。
- 支持并发模型执行、动态批处理和序列批处理。
- 提供模型组合、HTTP/gRPC 接口及运行指标。

### 环境要求

- 官方建议使用 Docker 镜像；CPU 或 GPU 环境需匹配所选后端。
- 需要准备模型仓库，部分模型还需显式配置文件。

### 使用限制

- 主分支面向下一版本开发，部署时应对照稳定版与容器版本。
- 后端能力和模型格式有差异，不能直接把任意权重文件当作服务模型。

### 开始使用

1. 按[快速开始](https://github.com/triton-inference-server/server/blob/main/docs/getting_started/quickstart.md)选择 CPU 或 GPU 方案。
2. 按[模型仓库说明](https://github.com/triton-inference-server/server/blob/main/docs/user_guide/model_repository.md)准备模型与配置。
3. 启动服务器并发送客户端请求，检查输出与运行指标。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:27.834Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-16 · commit](https://github.com/triton-inference-server/server/commit/24af411c99d09cfb60259dceb63a718606148aa2)。revert(skills): remove triton-pytorch-model-repository (unsigned merge of #9074) (#9079)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://github.com/triton-inference-server/server/blob/main/README.md)
- [Quickstart](https://github.com/triton-inference-server/server/blob/main/docs/getting_started/quickstart.md)
- [Model repository](https://github.com/triton-inference-server/server/blob/main/docs/user_guide/model_repository.md)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

An inference server for deploying and calling models from multiple machine-learning frameworks.

Exposes models as observable services for AI applications and pipelines.

### Features

- Connects model backends such as TensorRT, PyTorch, ONNX, and Python.
- Supports concurrent model execution, dynamic batching, and sequence batching.
- Provides model ensembles, HTTP/gRPC interfaces, and runtime metrics.

### Requirements

- Official guidance recommends Docker images; CPU or GPU environments must match the selected backend.
- Prepare a model repository; some models also require an explicit configuration file.

### Limitations

- The main branch tracks the next release; align stable server and container versions for deployment.
- Backend capabilities and model formats differ; arbitrary weight files are not automatically deployable models.

### Getting started

1. Choose a CPU or GPU setup using the [quickstart](https://github.com/triton-inference-server/server/blob/main/docs/getting_started/quickstart.md).
2. Prepare models and configuration using the [model repository guide](https://github.com/triton-inference-server/server/blob/main/docs/user_guide/model_repository.md).
3. Start the server, send client requests, and inspect outputs and metrics.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:27.834Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-16 · commit](https://github.com/triton-inference-server/server/commit/24af411c99d09cfb60259dceb63a718606148aa2).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://github.com/triton-inference-server/server/blob/main/README.md)
- [Quickstart](https://github.com/triton-inference-server/server/blob/main/docs/getting_started/quickstart.md)
- [Model repository](https://github.com/triton-inference-server/server/blob/main/docs/user_guide/model_repository.md)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.604063Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "server",
    "name": "Triton Inference Server",
    "repository": "triton-inference-server/server",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkxNTE2MzYxOTQ=",
    "category": "operations",
    "summary": {
      "zh-CN": "统一部署和调用多种机器学习模型的推理服务器。",
      "en": "An inference server for deploying and calling models from multiple machine-learning frameworks."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.604063Z",
        "en": "2026-11-17T14:24:07.604063Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "将模型包装成可监控的服务，供 AI 应用和流水线调用。",
        "en": "Exposes models as observable services for AI applications and pipelines."
      },
      "source_url": "https://github.com/triton-inference-server/server/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/triton-inference-server/server/commit/24af411c99d09cfb60259dceb63a718606148aa2",
        "occurred_at": "2026-11-16T22:29:09Z",
        "reviewed_at": "2026-11-17T14:24:07.604063Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "revert(skills): remove triton-pytorch-model-repository (unsigned merge of #9074) (#9079) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/triton-inference-server/server/blob/main/README.md"
      },
      {
        "title": "Quickstart",
        "url": "https://github.com/triton-inference-server/server/blob/main/docs/getting_started/quickstart.md"
      },
      {
        "title": "Model repository",
        "url": "https://github.com/triton-inference-server/server/blob/main/docs/user_guide/model_repository.md"
      }
    ]
  },
  "snapshot": {
    "full_name": "triton-inference-server/server",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkxNTE2MzYxOTQ=",
    "stargazers_count": 11146,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:27.834Z",
    "source_url": "https://api.github.com/repos/triton-inference-server/server"
  }
}
```

</details>
