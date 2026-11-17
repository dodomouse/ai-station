# colibri

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[JustVugg/colibri](https://github.com/JustVugg/colibri)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 51605 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-17T04:07:37.952522+00:00 |

## 中文

以 C 推理引擎按需从内存和磁盘加载权重，并可结合 GPU 运行本地模型。

### 用途与功能

- 按使用情况将混合专家模型权重放在显存、内存或磁盘。
- 提供 CPU、Vulkan 和 CUDA 后端，具体模型支持有差异。
- 通过聊天界面及 OpenAI、Anthropic 兼容接口提供模型服务。

### 环境与限制

需要下载匹配的模型权重并遵守模型许可。官方入门要求至少 8 GB 内存，最小模型约需 22 GB 磁盘。大型模型空间需求更高，磁盘流式读取的速度取决于硬件。源码安装需要编译工具，设置和 API 网关使用 Python。

### 开始使用

按平台完成 README 的安装步骤，让设置程序检查硬件并选择模型，再用 coli chat 或 coli serve 验证。

参阅[官方 README](https://github.com/JustVugg/colibri/blob/0a5504a1dc64f86fcd0fe7db298b0448c730e7e6/README.md)。

### 收录与来源

适合研究模型权重分层加载及在有限内存机器上运行本地推理的取舍。

维护证据：[修复 Windows Vulkan 主机内存池的对齐分配，使用匹配的 _aligned_malloc 和 _aligned_free 替代不可用的 POSIX 接口。](https://github.com/JustVugg/colibri/commit/b19fb369ed94a5910c1e9cc1dcc2df7882087efb)（2026-10-31）。

发现于 [GitHub 月榜](https://github.com/trending/c?since=monthly)。2026-11-17 的榜单记录新增 9,415 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Runs local models with C inference engines that load weights from RAM and disk on demand, with optional GPU acceleration.

### Uses and features

- Places mixture-of-experts weights in VRAM, RAM or disk according to usage.
- Offers CPU, Vulkan and CUDA backends with model-specific support.
- Serves models through chat interfaces and OpenAI- and Anthropic-compatible APIs.

### Requirements and limits

Requires compatible model downloads under their own licenses. The quick start specifies at least 8 GB RAM and about 22 GB disk for the smallest model; larger models need more storage and disk-streaming speed depends on hardware. Source setup needs build tools, while setup and the API gateway use Python.

### Getting started

Follow the platform setup in the README, let the setup check hardware and select a model, then verify with coli chat or coli serve.

See the [official README](https://github.com/JustVugg/colibri/blob/0a5504a1dc64f86fcd0fe7db298b0448c730e7e6/README.md).

### Review and provenance

Useful for studying tiered weight loading and the tradeoffs of local inference on memory-constrained machines.

Maintenance evidence: [Fixes aligned allocation for the Vulkan host pool on Windows using paired _aligned_malloc and _aligned_free calls instead of unavailable POSIX allocation.](https://github.com/JustVugg/colibri/commit/b19fb369ed94a5910c1e9cc1dcc2df7882087efb) (2026-10-31).

Discovered in [GitHub monthly Trending](https://github.com/trending/c?since=monthly), which recorded 9,415 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:07:37.952522+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "colibri",
    "name": "colibri",
    "repository": "JustVugg/colibri",
    "repo_node_id": "R_kgDOTKgHjQ",
    "category": "ai",
    "summary": {
      "zh-CN": "以 C 推理引擎按需从内存和磁盘加载权重，并可结合 GPU 运行本地模型。",
      "en": "Runs local models with C inference engines that load weights from RAM and disk on demand, with optional GPU acceleration."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:07:37.952522+00:00",
        "en": "2026-11-17T04:07:37.952522+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合研究模型权重分层加载及在有限内存机器上运行本地推理的取舍。",
      "en": "Useful for studying tiered weight loading and the tradeoffs of local inference on memory-constrained machines.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "source_url": "https://github.com/JustVugg/colibri/blob/0a5504a1dc64f86fcd0fe7db298b0448c730e7e6/LICENSE",
      "license_sha256": "fb9b97e1cc193452870025f6cf501003130561681659e265e5fdf6c023f71325",
      "source_commit": "0a5504a1dc64f86fcd0fe7db298b0448c730e7e6",
      "reviewed_at": "2026-11-17T04:07:37.952522+00:00",
      "evidence_pinned_at": "2026-11-17T04:07:37.952522+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "Applies to repository code and documentation; external models, services, data and assets retain their own terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-10-31T05:30:41Z",
        "reviewed_at": "2026-11-17T04:07:37.952522+00:00",
        "url": "https://github.com/JustVugg/colibri/commit/b19fb369ed94a5910c1e9cc1dcc2df7882087efb",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复 Windows Vulkan 主机内存池的对齐分配，使用匹配的 _aligned_malloc 和 _aligned_free 替代不可用的 POSIX 接口。",
          "en": "Fixes aligned allocation for the Vulkan host pool on Windows using paired _aligned_malloc and _aligned_free calls instead of unavailable POSIX allocation."
        },
        "reviewed_files": [
          "c/backend_vulkan.c"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/JustVugg/colibri",
        "accessed_at": "2026-11-17T04:07:37.952522+00:00"
      },
      {
        "url": "https://github.com/JustVugg/colibri/blob/0a5504a1dc64f86fcd0fe7db298b0448c730e7e6/README.md",
        "accessed_at": "2026-11-17T04:07:37.952522+00:00"
      },
      {
        "url": "https://github.com/JustVugg/colibri/blob/0a5504a1dc64f86fcd0fe7db298b0448c730e7e6/LICENSE",
        "accessed_at": "2026-11-17T04:07:37.952522+00:00"
      },
      {
        "url": "https://github.com/JustVugg/colibri/commit/b19fb369ed94a5910c1e9cc1dcc2df7882087efb",
        "accessed_at": "2026-11-17T04:07:37.952522+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 9415,
      "source_url": "https://github.com/trending/c?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOTKgHjQ",
    "full_name": "JustVugg/colibri",
    "stargazers_count": 51605,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "fb9b97e1cc193452870025f6cf501003130561681659e265e5fdf6c023f71325",
    "last_success_at": "2026-11-17T03:53:54.730056+00:00"
  }
}
```

</details>
