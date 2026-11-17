# llama.cpp

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 135378 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T04:07:37.960167+00:00 |

## 中文

基于 ggml 的 C/C++ 模型推理引擎，提供本地命令行、服务接口及多模态模型支持。

### 用途与功能

- 从本地文件或模型仓库加载兼容模型并推理。
- 提供命令行对话和 OpenAI 兼容 API 服务。
- 提供不同硬件后端、构建与多 GPU 使用说明。

### 环境与限制

需选用支持的模型格式、模型架构和硬件后端；模型文件及上下文占用仍受内存限制。可使用预编译版本、Docker 或源码构建。MIT 适用于引擎，模型及第三方组件各有许可。

### 开始使用

从发行版或构建指南安装，按 README 用 `llama cli` 运行模型，或用 `llama serve` 启动 API。

参阅[官方 README](https://github.com/ggml-org/llama.cpp/blob/9581154a2250cc9e6948e4c2a2fc4b4e19d1a57e/README.md)。

### 收录与来源

适合需要直接控制推理后端、模型文件和服务部署方式的开发者。

维护证据：[修复 Muse Glimmer 视觉位置嵌入的宽高插值顺序，使其与训练端一致](https://github.com/ggml-org/llama.cpp/commit/9581154a2250cc9e6948e4c2a2fc4b4e19d1a57e)（2026-11-16）。

发现于 [GitHub 月榜](https://github.com/trending/c%2B%2B?since=monthly)。2026-11-17 的榜单记录新增 4,449 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

A ggml-based C/C++ inference engine with local command-line tools, serving interfaces and multimodal model support.

### Uses and features

- Load compatible models from local files or model repositories for inference.
- Provide CLI chat and an OpenAI-compatible API server.
- Provide hardware backend, build and multi-GPU usage documentation.

### Requirements and limits

Requires supported model formats, architectures and hardware backends; model files and context remain bounded by available memory. Use prebuilt binaries, Docker or a source build. MIT covers the engine; models and third-party components have separate licenses.

### Getting started

Install from a release or the build guide, then use `llama cli` to run a model or `llama serve` to start an API as shown in the README.

See the [official README](https://github.com/ggml-org/llama.cpp/blob/9581154a2250cc9e6948e4c2a2fc4b4e19d1a57e/README.md).

### Review and provenance

Useful for developers needing direct control over inference backends, model files and serving deployment.

Maintenance evidence: [Corrects the height/width interpolation order of Muse Glimmer vision positional embeddings to match training](https://github.com/ggml-org/llama.cpp/commit/9581154a2250cc9e6948e4c2a2fc4b4e19d1a57e) (2026-11-16).

Discovered in [GitHub monthly Trending](https://github.com/trending/c%2B%2B?since=monthly), which recorded 4,449 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:07:37.960167+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "llama-cpp",
    "name": "llama.cpp",
    "repository": "ggml-org/llama.cpp",
    "repo_node_id": "R_kgDOJH_K4A",
    "category": "ai",
    "summary": {
      "zh-CN": "基于 ggml 的 C/C++ 模型推理引擎，提供本地命令行、服务接口及多模态模型支持。",
      "en": "A ggml-based C/C++ inference engine with local command-line tools, serving interfaces and multimodal model support."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:07:37.960167+00:00",
        "en": "2026-11-17T04:07:37.960167+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合需要直接控制推理后端、模型文件和服务部署方式的开发者。",
      "en": "Useful for developers needing direct control over inference backends, model files and serving deployment.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/ggml-org/llama.cpp/blob/9581154a2250cc9e6948e4c2a2fc4b4e19d1a57e/LICENSE",
      "license_sha256": "94f29bbed6a22c35b992c5c6ebf0e7c92f13b836b90f36f461c9cf2f0f1d010d",
      "source_commit": "9581154a2250cc9e6948e4c2a2fc4b4e19d1a57e",
      "reviewed_at": "2026-11-17T04:07:37.960167+00:00",
      "evidence_pinned_at": "2026-11-17T04:07:37.960167+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "MIT covers llama.cpp code, subject to third-party component notices. Downloaded model weights retain their own licenses."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-16T23:29:02Z",
        "reviewed_at": "2026-11-17T04:07:37.960167+00:00",
        "url": "https://github.com/ggml-org/llama.cpp/commit/9581154a2250cc9e6948e4c2a2fc4b4e19d1a57e",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复 Muse Glimmer 视觉位置嵌入的宽高插值顺序，使其与训练端一致",
          "en": "Corrects the height/width interpolation order of Muse Glimmer vision positional embeddings to match training"
        },
        "reviewed_files": [
          "tools/mtmd/models/muse-glimmer.cpp"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/ggml-org/llama.cpp",
        "accessed_at": "2026-11-17T04:07:37.960167+00:00"
      },
      {
        "url": "https://github.com/ggml-org/llama.cpp/blob/9581154a2250cc9e6948e4c2a2fc4b4e19d1a57e/README.md",
        "accessed_at": "2026-11-17T04:07:37.960167+00:00"
      },
      {
        "url": "https://github.com/ggml-org/llama.cpp/blob/9581154a2250cc9e6948e4c2a2fc4b4e19d1a57e/LICENSE",
        "accessed_at": "2026-11-17T04:07:37.960167+00:00"
      },
      {
        "url": "https://github.com/ggml-org/llama.cpp/commit/9581154a2250cc9e6948e4c2a2fc4b4e19d1a57e",
        "accessed_at": "2026-11-17T04:07:37.960167+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 4449,
      "source_url": "https://github.com/trending/c%2B%2B?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOJH_K4A",
    "full_name": "ggml-org/llama.cpp",
    "stargazers_count": 135378,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "94f29bbed6a22c35b992c5c6ebf0e7c92f13b836b90f36f461c9cf2f0f1d010d",
    "last_success_at": "2026-11-17T03:52:19.322163+00:00"
  }
}
```

</details>
