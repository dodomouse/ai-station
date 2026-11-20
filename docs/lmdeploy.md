# LMDeploy

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[InternLM/lmdeploy](https://github.com/InternLM/lmdeploy)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 8149 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.603830Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:28.027Z |

## 中文

用于语言模型和视觉语言模型压缩、推理及服务部署的工具集。

把模型部署为批量推理任务或应用可调用的推理服务。

### 主要功能

- 提供 TurboMind 与 PyTorch 两种推理引擎。
- 支持权重量化、KV 缓存量化和连续批处理。
- 提供离线批量推理、多模型服务及多设备部署。

### 环境要求

- README 建议 Python 3.10–3.13 环境；预编译包需匹配对应 CUDA 环境。
- 非 CUDA 平台需遵循对应后端的安装与模型支持说明。

### 使用限制

- 两种引擎支持的模型及数据类型不同，部署前应核对支持表。
- 模型下载来源和显存用量取决于所选模型、量化方式及上下文配置。

### 开始使用

1. 按[快速开始](https://lmdeploy.readthedocs.io/en/latest/get_started/get_started.html)安装匹配环境的版本。
2. 在[支持表](https://github.com/InternLM/lmdeploy/blob/main/docs/en/supported_models/supported_models.md)中选择模型和引擎。
3. 先运行离线推理，再按官方教程配置服务。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:28.027Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/InternLM/lmdeploy/commit/fc33f69736ff48c10ad720593b021dcdaedcb80d)。fix(vl): honor request-local multimodal processor options (#5113)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://github.com/InternLM/lmdeploy/blob/main/README.md)
- [Quickstart](https://lmdeploy.readthedocs.io/en/latest/get_started/get_started.html)
- [Supported models](https://github.com/InternLM/lmdeploy/blob/main/docs/en/supported_models/supported_models.md)

## English

A toolkit for compressing, running, and serving language and vision-language models.

Deploys models for batch inference or inference services callable by applications.

### Features

- Provides TurboMind and PyTorch inference engines.
- Supports weight quantization, KV-cache quantization, and continuous batching.
- Provides offline batch inference, multi-model serving, and multi-device deployment.

### Requirements

- The README recommends Python 3.10–3.13; prebuilt packages must match the CUDA environment.
- Non-CUDA platforms require their backend-specific installation and model support guides.

### Limitations

- The engines support different models and data types; check the matrix before deployment.
- Model sources and GPU memory use depend on the model, quantization method, and context configuration.

### Getting started

1. Install a compatible version using the [quickstart](https://lmdeploy.readthedocs.io/en/latest/get_started/get_started.html).
2. Choose a model and engine from the [support table](https://github.com/InternLM/lmdeploy/blob/main/docs/en/supported_models/supported_models.md).
3. Run offline inference first, then configure serving using the official tutorials.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:28.027Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/InternLM/lmdeploy/commit/fc33f69736ff48c10ad720593b021dcdaedcb80d).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://github.com/InternLM/lmdeploy/blob/main/README.md)
- [Quickstart](https://lmdeploy.readthedocs.io/en/latest/get_started/get_started.html)
- [Supported models](https://github.com/InternLM/lmdeploy/blob/main/docs/en/supported_models/supported_models.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.603830Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "lmdeploy",
    "name": "LMDeploy",
    "repository": "InternLM/lmdeploy",
    "repo_node_id": "R_kgDOJv0ecQ",
    "category": "ai",
    "summary": {
      "zh-CN": "用于语言模型和视觉语言模型压缩、推理及服务部署的工具集。",
      "en": "A toolkit for compressing, running, and serving language and vision-language models."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.603830Z",
        "en": "2026-11-17T14:24:07.603830Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "把模型部署为批量推理任务或应用可调用的推理服务。",
        "en": "Deploys models for batch inference or inference services callable by applications."
      },
      "source_url": "https://github.com/InternLM/lmdeploy/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/InternLM/lmdeploy/commit/fc33f69736ff48c10ad720593b021dcdaedcb80d",
        "occurred_at": "2026-11-17T08:29:21Z",
        "reviewed_at": "2026-11-17T14:24:07.603830Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "fix(vl): honor request-local multimodal processor options (#5113) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/InternLM/lmdeploy/blob/main/README.md"
      },
      {
        "title": "Quickstart",
        "url": "https://lmdeploy.readthedocs.io/en/latest/get_started/get_started.html"
      },
      {
        "title": "Supported models",
        "url": "https://github.com/InternLM/lmdeploy/blob/main/docs/en/supported_models/supported_models.md"
      }
    ]
  },
  "snapshot": {
    "full_name": "InternLM/lmdeploy",
    "repo_node_id": "R_kgDOJv0ecQ",
    "stargazers_count": 8149,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:28.027Z",
    "source_url": "https://api.github.com/repos/InternLM/lmdeploy"
  }
}
```

</details>
