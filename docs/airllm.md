# AirLLM

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[lyogavin/airllm](https://github.com/lyogavin/airllm)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 42524 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-17T03:59:14.752762+00:00 |

## 中文

通过逐层加载和卸载模型权重降低大语言模型的显存需求，并提供部分模型的流式 LoRA 训练接口。

### 用途与功能

- 通过 AutoModel 根据模型配置选择加载实现。
- 拆分权重为分层文件，并提供压缩及预取配置。
- 为部分架构提供适配器训练示例。

### 环境与限制

需要 Python、PyTorch、匹配模型的依赖，以及存放原始与分层权重的磁盘空间。低显存占用不代表低延迟，磁盘读写会影响速度。macOS 路径需 Apple Silicon、MLX，目前仅支持 Llama/Mistral 风格架构。Apache-2.0 不覆盖模型权重。

### 开始使用

按 README 安装 airllm，从 AutoModel 推理示例开始，先核对模型架构、依赖与磁盘容量。

参阅[官方 README](https://github.com/lyogavin/airllm/blob/fb1e0b810cbd750d0822d017b1924473bbd4acc1/README.md)。

### 收录与来源

适合显存受限、能够接受权重换入换出开销的模型实验；具体吞吐和容量需自行实测。

维护证据：[在 macOS 下载和拆分权重前检查模型架构，提前拒绝 MLX 后端不支持的模型](https://github.com/lyogavin/airllm/commit/f83bfdab815671ceae0ca8eeb22ddc177b180f3a)（2026-10-14）。

发现于 [GitHub 月榜](https://github.com/trending/jupyter-notebook?since=monthly)。2026-11-17 的榜单记录新增 3,699 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Reduce LLM VRAM demand by loading and offloading weights layer by layer, with streamed LoRA training interfaces for selected models.

### Uses and features

- Select a loading implementation from model configuration through AutoModel.
- Split weights into per-layer files with compression and prefetch options.
- Provide adapter-training examples for selected architectures.

### Requirements and limits

Requires Python, PyTorch, model-specific dependencies and disk space for original and split weights. Low VRAM usage does not imply low latency; disk I/O affects performance. The macOS path needs Apple Silicon and MLX and currently supports only Llama/Mistral-style architectures. Apache-2.0 does not cover model weights.

### Getting started

Install airllm following the README and start with the AutoModel inference example after checking architecture support, dependencies and disk capacity.

See the [official README](https://github.com/lyogavin/airllm/blob/fb1e0b810cbd750d0822d017b1924473bbd4acc1/README.md).

### Review and provenance

Useful for model experiments with limited VRAM where weight-streaming overhead is acceptable; throughput and capacity require measurement on the actual setup.

Maintenance evidence: [Checks model architecture before downloading and splitting weights on macOS, rejecting architectures unsupported by the MLX backend](https://github.com/lyogavin/airllm/commit/f83bfdab815671ceae0ca8eeb22ddc177b180f3a) (2026-10-14).

Discovered in [GitHub monthly Trending](https://github.com/trending/jupyter-notebook?since=monthly), which recorded 3,699 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T03:59:14.752762+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "airllm",
    "name": "AirLLM",
    "repository": "lyogavin/airllm",
    "repo_node_id": "R_kgDOJueYYw",
    "category": "ai",
    "summary": {
      "zh-CN": "通过逐层加载和卸载模型权重降低大语言模型的显存需求，并提供部分模型的流式 LoRA 训练接口。",
      "en": "Reduce LLM VRAM demand by loading and offloading weights layer by layer, with streamed LoRA training interfaces for selected models."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T03:59:14.752762+00:00",
        "en": "2026-11-17T03:59:14.752762+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合显存受限、能够接受权重换入换出开销的模型实验；具体吞吐和容量需自行实测。",
      "en": "Useful for model experiments with limited VRAM where weight-streaming overhead is acceptable; throughput and capacity require measurement on the actual setup.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "source_url": "https://github.com/lyogavin/airllm/blob/fb1e0b810cbd750d0822d017b1924473bbd4acc1/LICENSE",
      "license_sha256": "c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4",
      "source_commit": "fb1e0b810cbd750d0822d017b1924473bbd4acc1",
      "reviewed_at": "2026-11-17T03:59:14.752762+00:00",
      "evidence_pinned_at": "2026-11-17T03:59:14.752762+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "Apache-2.0 covers AirLLM software. Models, remote model code and training data retain their own licenses."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-10-14T01:44:21Z",
        "reviewed_at": "2026-11-17T03:59:14.752762+00:00",
        "url": "https://github.com/lyogavin/airllm/commit/f83bfdab815671ceae0ca8eeb22ddc177b180f3a",
        "qualifies": true,
        "reason": {
          "zh-CN": "在 macOS 下载和拆分权重前检查模型架构，提前拒绝 MLX 后端不支持的模型",
          "en": "Checks model architecture before downloading and splitting weights on macOS, rejecting architectures unsupported by the MLX backend"
        },
        "reviewed_files": [
          "air_llm/airllm/auto_model.py"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/lyogavin/airllm",
        "accessed_at": "2026-11-17T03:59:14.752762+00:00"
      },
      {
        "url": "https://github.com/lyogavin/airllm/blob/fb1e0b810cbd750d0822d017b1924473bbd4acc1/README.md",
        "accessed_at": "2026-11-17T03:59:14.752762+00:00"
      },
      {
        "url": "https://github.com/lyogavin/airllm/blob/fb1e0b810cbd750d0822d017b1924473bbd4acc1/LICENSE",
        "accessed_at": "2026-11-17T03:59:14.752762+00:00"
      },
      {
        "url": "https://github.com/lyogavin/airllm/commit/f83bfdab815671ceae0ca8eeb22ddc177b180f3a",
        "accessed_at": "2026-11-17T03:59:14.752762+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 3699,
      "source_url": "https://github.com/trending/jupyter-notebook?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOJueYYw",
    "full_name": "lyogavin/airllm",
    "stargazers_count": 42524,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4",
    "last_success_at": "2026-11-17T03:52:28.329829+00:00"
  }
}
```

</details>
