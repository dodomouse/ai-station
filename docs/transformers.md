# Transformers

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[huggingface/transformers](https://github.com/huggingface/transformers)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 169089 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-17T04:00:03.483574+00:00 |

## 中文

用于加载、训练和推理文本、视觉、音频及多模态模型的 Python 模型框架。

### 用途与功能

- 用统一模型与处理器接口复用不同架构。
- 通过 pipeline 组合预处理、模型推理和结果处理。

### 环境与限制

当前 README 要求 Python 3.11+ 和 PyTorch 2.6+。模型需单独下载，计算资源、访问权限和权重许可随模型变化。

### 开始使用

在虚拟环境安装 transformers[torch]，选择一个可访问的模型，先运行官方 pipeline 示例。

参阅[官方 README](https://github.com/huggingface/transformers/blob/44a7a2090208be1f8b10d3db27a430b52887365d/README.md)。

### 收录与来源

统一处理器和模型接口便于对比模型，并可衔接既有训练与推理工具。

维护证据：[修复 Qwen3 Omni 处理器漏传 audio_kwargs，并将 n_window 传入多模态 token 计数。](https://github.com/huggingface/transformers/commit/44a7a2090208be1f8b10d3db27a430b52887365d)（2026-11-17）。

发现于 [GitHub 月榜](https://github.com/trending/python?since=monthly&spoken_language_code=en)。2026-11-17 的榜单记录新增 1,723 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

A Python framework for loading, training and running text, vision, audio and multimodal models.

### Uses and features

- Reuses model architectures through shared model and processor interfaces.
- Combines preprocessing, inference and postprocessing through pipelines.

### Requirements and limits

The current README requires Python 3.11+ and PyTorch 2.6+. Model downloads, compute needs, access permissions and weight licenses vary by model.

### Getting started

Install transformers[torch] in a virtual environment, choose an accessible model and run an official pipeline example.

See the [official README](https://github.com/huggingface/transformers/blob/44a7a2090208be1f8b10d3db27a430b52887365d/README.md).

### Review and provenance

Shared processor and model interfaces simplify model comparisons and integration with training and inference tools.

Maintenance evidence: [Fixes forwarding of audio_kwargs in the Qwen3 Omni processor and carries n_window into multimodal token counting.](https://github.com/huggingface/transformers/commit/44a7a2090208be1f8b10d3db27a430b52887365d) (2026-11-17).

Discovered in [GitHub monthly Trending](https://github.com/trending/python?since=monthly&spoken_language_code=en), which recorded 1,723 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:00:03.483574+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "transformers",
    "name": "Transformers",
    "repository": "huggingface/transformers",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkxNTUyMjA2NDE=",
    "category": "ai",
    "summary": {
      "zh-CN": "用于加载、训练和推理文本、视觉、音频及多模态模型的 Python 模型框架。",
      "en": "A Python framework for loading, training and running text, vision, audio and multimodal models."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:00:03.483574+00:00",
        "en": "2026-11-17T04:00:03.483574+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "统一处理器和模型接口便于对比模型，并可衔接既有训练与推理工具。",
      "en": "Shared processor and model interfaces simplify model comparisons and integration with training and inference tools.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "source_url": "https://github.com/huggingface/transformers/blob/44a7a2090208be1f8b10d3db27a430b52887365d/LICENSE",
      "license_sha256": "77fd4710def9ec3c0f6225800e0235f15a425abd4a8b03559127fcd782612049",
      "source_commit": "44a7a2090208be1f8b10d3db27a430b52887365d",
      "reviewed_at": "2026-11-17T04:00:03.483574+00:00",
      "evidence_pinned_at": "2026-11-17T04:00:03.483574+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "Root license applies to repository software code; models, data, assets and external services have separate terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-17T02:44:14Z",
        "reviewed_at": "2026-11-17T04:00:03.483574+00:00",
        "url": "https://github.com/huggingface/transformers/commit/44a7a2090208be1f8b10d3db27a430b52887365d",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复 Qwen3 Omni 处理器漏传 audio_kwargs，并将 n_window 传入多模态 token 计数。",
          "en": "Fixes forwarding of audio_kwargs in the Qwen3 Omni processor and carries n_window into multimodal token counting."
        },
        "reviewed_files": [
          "src/transformers/models/qwen3_omni_moe/processing_qwen3_omni_moe.py",
          "src/transformers/models/qwen3_omni_moe/modular_qwen3_omni_moe.py"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/huggingface/transformers",
        "accessed_at": "2026-11-17T04:00:03.483574+00:00"
      },
      {
        "url": "https://github.com/huggingface/transformers/blob/44a7a2090208be1f8b10d3db27a430b52887365d/README.md",
        "accessed_at": "2026-11-17T04:00:03.483574+00:00"
      },
      {
        "url": "https://github.com/huggingface/transformers/blob/44a7a2090208be1f8b10d3db27a430b52887365d/LICENSE",
        "accessed_at": "2026-11-17T04:00:03.483574+00:00"
      },
      {
        "url": "https://github.com/huggingface/transformers/commit/44a7a2090208be1f8b10d3db27a430b52887365d",
        "accessed_at": "2026-11-17T04:00:03.483574+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 1723,
      "source_url": "https://github.com/trending/python?since=monthly&spoken_language_code=en",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkxNTUyMjA2NDE=",
    "full_name": "huggingface/transformers",
    "stargazers_count": 169089,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "77fd4710def9ec3c0f6225800e0235f15a425abd4a8b03559127fcd782612049",
    "last_success_at": "2026-11-17T03:51:16.744013+00:00"
  }
}
```

</details>
