# vLLM

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[vllm-project/vllm](https://github.com/vllm-project/vllm)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 97064 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-17T03:59:14.753179+00:00 |

## 中文

面向语言和多模态模型的推理与服务框架，提供请求批处理、分布式推理及兼容常见客户端的 API。

### 用途与功能

- 通过 PagedAttention、连续批处理和前缀缓存管理推理资源。
- 提供 OpenAI 兼容服务、流式输出、工具调用和结构化输出。
- 支持多种量化方案、并行方式及多模态模型架构。

### 环境与限制

需按官方安装矩阵匹配 Python、推理后端、驱动及硬件；不同模型和加速器支持范围不同。多卡部署还需通信与显存规划。Apache-2.0 覆盖框架代码，模型权重和硬件插件各有许可。

### 开始使用

从 README 链接的安装与 Quickstart 指南选择硬件路径，安装 vLLM 后选兼容模型启动服务。

参阅[官方 README](https://github.com/vllm-project/vllm/blob/444a9f5b39ea25e9b1e864cb4802589d518994a5/README.md)。

### 收录与来源

适合需要集中服务模型、多请求调度和分布式推理的应用后端。

维护证据：[为 Nemotron VL 增加 GPU 图像与视频帧缩放路径，并纳入多模态输入和显存估算](https://github.com/vllm-project/vllm/commit/444a9f5b39ea25e9b1e864cb4802589d518994a5)（2026-11-17）。

发现于 [GitHub 月榜](https://github.com/trending/python?since=monthly)。2026-11-17 的榜单记录新增 3,311 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

An inference and serving framework for language and multimodal models, with request batching, distributed inference and APIs compatible with common clients.

### Uses and features

- Manage inference resources through PagedAttention, continuous batching and prefix caching.
- Provide OpenAI-compatible serving, streaming, tool calling and structured outputs.
- Support multiple quantization formats, parallelism strategies and multimodal architectures.

### Requirements and limits

Match Python, inference backend, drivers and hardware using the official installation matrix; support varies by model and accelerator. Multi-device deployment also needs communication and memory planning. Apache-2.0 covers framework code; weights and hardware plugins retain their licenses.

### Getting started

Choose a hardware path in the installation and Quickstart guides linked from the README, install vLLM and start serving a compatible model.

See the [official README](https://github.com/vllm-project/vllm/blob/444a9f5b39ea25e9b1e864cb4802589d518994a5/README.md).

### Review and provenance

Useful for application backends requiring shared model serving, concurrent request scheduling and distributed inference.

Maintenance evidence: [Adds GPU resizing for Nemotron VL images and video frames, integrating it into multimodal inputs and memory profiling](https://github.com/vllm-project/vllm/commit/444a9f5b39ea25e9b1e864cb4802589d518994a5) (2026-11-17).

Discovered in [GitHub monthly Trending](https://github.com/trending/python?since=monthly), which recorded 3,311 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T03:59:14.753179+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "vllm",
    "name": "vLLM",
    "repository": "vllm-project/vllm",
    "repo_node_id": "R_kgDOI7xefg",
    "category": "ai",
    "summary": {
      "zh-CN": "面向语言和多模态模型的推理与服务框架，提供请求批处理、分布式推理及兼容常见客户端的 API。",
      "en": "An inference and serving framework for language and multimodal models, with request batching, distributed inference and APIs compatible with common clients."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T03:59:14.753179+00:00",
        "en": "2026-11-17T03:59:14.753179+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合需要集中服务模型、多请求调度和分布式推理的应用后端。",
      "en": "Useful for application backends requiring shared model serving, concurrent request scheduling and distributed inference.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "source_url": "https://github.com/vllm-project/vllm/blob/444a9f5b39ea25e9b1e864cb4802589d518994a5/LICENSE",
      "license_sha256": "c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4",
      "source_commit": "444a9f5b39ea25e9b1e864cb4802589d518994a5",
      "reviewed_at": "2026-11-17T03:59:14.753179+00:00",
      "evidence_pinned_at": "2026-11-17T03:59:14.753179+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "Apache-2.0 applies to framework code. Model weights, hardware plugins and third-party dependencies retain separate licenses."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-17T03:35:18Z",
        "reviewed_at": "2026-11-17T03:59:14.753179+00:00",
        "url": "https://github.com/vllm-project/vllm/commit/444a9f5b39ea25e9b1e864cb4802589d518994a5",
        "qualifies": true,
        "reason": {
          "zh-CN": "为 Nemotron VL 增加 GPU 图像与视频帧缩放路径，并纳入多模态输入和显存估算",
          "en": "Adds GPU resizing for Nemotron VL images and video frames, integrating it into multimodal inputs and memory profiling"
        },
        "reviewed_files": [
          "vllm/model_executor/models/nano_nemotron_vl.py"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/vllm-project/vllm",
        "accessed_at": "2026-11-17T03:59:14.753179+00:00"
      },
      {
        "url": "https://github.com/vllm-project/vllm/blob/444a9f5b39ea25e9b1e864cb4802589d518994a5/README.md",
        "accessed_at": "2026-11-17T03:59:14.753179+00:00"
      },
      {
        "url": "https://github.com/vllm-project/vllm/blob/444a9f5b39ea25e9b1e864cb4802589d518994a5/LICENSE",
        "accessed_at": "2026-11-17T03:59:14.753179+00:00"
      },
      {
        "url": "https://github.com/vllm-project/vllm/commit/444a9f5b39ea25e9b1e864cb4802589d518994a5",
        "accessed_at": "2026-11-17T03:59:14.753179+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 3311,
      "source_url": "https://github.com/trending/python?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOI7xefg",
    "full_name": "vllm-project/vllm",
    "stargazers_count": 97064,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4",
    "last_success_at": "2026-11-17T03:52:30.261826+00:00"
  }
}
```

</details>
