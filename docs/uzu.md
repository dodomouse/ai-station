# uzu

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[trymirai/uzu](https://github.com/trymirai/uzu)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 3358 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T04:07:37.967141+00:00 |

## 中文

将模型下载、聊天会话和本地推理嵌入应用的 Rust 引擎，提供多语言绑定。

### 用途与功能

- 提供 Rust、Swift、Python 和 TypeScript 接口。
- 支持结构化输出、工具调用及 OpenAI 兼容 HTTP 服务。

### 环境与限制

README 列出 Metal 与 CPU 后端；模型使用项目定义的模型格式，可用 lalamo 转换。需要匹配平台工具链；模型大小和可用内存限制可加载的模型，推理表现取决于设备硬件。模型权重许可需单独核对。

### 开始使用

按所用语言选择官方快速开始示例，先下载一个小模型并创建聊天会话；Rust CLI 入口为 cargo run --release -p cli。

参阅[官方 README](https://github.com/trymirai/uzu/blob/65cd1cdcf2dec7d517ac60e6aa8ff688d063567d/README.md)。

### 收录与来源

用统一会话接口连接模型下载、推理和应用工具调用，适合评估应用内模型集成。

维护证据：[新增 Vulkan DeltaNet 预填充内核，计算衰减状态更新。加入按数据类型和共享内存限制选择的分块执行路径。](https://github.com/trymirai/uzu/commit/65cd1cdcf2dec7d517ac60e6aa8ff688d063567d)（2026-11-17）。

发现于 [GitHub 月榜](https://github.com/trending/rust?since=monthly)。2026-11-17 的榜单记录新增 1,013 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

A Rust engine with language bindings for embedding model downloads, chat sessions and local inference in applications.

### Uses and features

- Provides Rust, Swift, Python and TypeScript interfaces.
- Supports structured output, tool calls and an OpenAI-compatible HTTP server.

### Requirements and limits

The README lists Metal and CPU backends. Models use a project-defined format with lalamo conversion. Requires matching platform tools; model size and available memory limit which models can be loaded, and inference performance depends on device hardware. Check model weight licenses separately.

### Getting started

Choose the official quick start for your language, download a small model and create a chat session; the Rust CLI entry is cargo run --release -p cli.

See the [official README](https://github.com/trymirai/uzu/blob/65cd1cdcf2dec7d517ac60e6aa8ff688d063567d/README.md).

### Review and provenance

A shared session interface connects model downloads, inference and application tool calls for evaluating embedded model integration.

Maintenance evidence: [Adds Vulkan DeltaNet prefill kernels for decayed state updates and a chunked execution path selected by data type and shared-memory limits.](https://github.com/trymirai/uzu/commit/65cd1cdcf2dec7d517ac60e6aa8ff688d063567d) (2026-11-17).

Discovered in [GitHub monthly Trending](https://github.com/trending/rust?since=monthly), which recorded 1,013 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:07:37.967141+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "uzu",
    "name": "uzu",
    "repository": "trymirai/uzu",
    "repo_node_id": "R_kgDOPAsbmQ",
    "category": "ai",
    "summary": {
      "zh-CN": "将模型下载、聊天会话和本地推理嵌入应用的 Rust 引擎，提供多语言绑定。",
      "en": "A Rust engine with language bindings for embedding model downloads, chat sessions and local inference in applications."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:07:37.967141+00:00",
        "en": "2026-11-17T04:07:37.967141+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "用统一会话接口连接模型下载、推理和应用工具调用，适合评估应用内模型集成。",
      "en": "A shared session interface connects model downloads, inference and application tool calls for evaluating embedded model integration.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/trymirai/uzu/blob/65cd1cdcf2dec7d517ac60e6aa8ff688d063567d/LICENSE",
      "license_sha256": "7621d17e34842470f59e711e3087cc4428d1dd41117fc6d3ddeb1e0fa6f56b20",
      "source_commit": "65cd1cdcf2dec7d517ac60e6aa8ff688d063567d",
      "reviewed_at": "2026-11-17T04:07:37.967141+00:00",
      "evidence_pinned_at": "2026-11-17T04:07:37.967141+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "Root license applies to repository software code; models, data, assets and external services have separate terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-17T03:41:43Z",
        "reviewed_at": "2026-11-17T04:07:37.967141+00:00",
        "url": "https://github.com/trymirai/uzu/commit/65cd1cdcf2dec7d517ac60e6aa8ff688d063567d",
        "qualifies": true,
        "reason": {
          "zh-CN": "新增 Vulkan DeltaNet 预填充内核，计算衰减状态更新。加入按数据类型和共享内存限制选择的分块执行路径。",
          "en": "Adds Vulkan DeltaNet prefill kernels for decayed state updates and a chunked execution path selected by data type and shared-memory limits."
        },
        "reviewed_files": [
          "crates/uzu-engine/src/backends/vulkan/kernel/gdn/prefill.slang",
          "crates/uzu-engine/src/backends/vulkan/kernel/gdn/vk_delta_net_chunked_prefill.rs"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/trymirai/uzu",
        "accessed_at": "2026-11-17T04:07:37.967141+00:00"
      },
      {
        "url": "https://github.com/trymirai/uzu/blob/65cd1cdcf2dec7d517ac60e6aa8ff688d063567d/README.md",
        "accessed_at": "2026-11-17T04:07:37.967141+00:00"
      },
      {
        "url": "https://github.com/trymirai/uzu/blob/65cd1cdcf2dec7d517ac60e6aa8ff688d063567d/LICENSE",
        "accessed_at": "2026-11-17T04:07:37.967141+00:00"
      },
      {
        "url": "https://github.com/trymirai/uzu/commit/65cd1cdcf2dec7d517ac60e6aa8ff688d063567d",
        "accessed_at": "2026-11-17T04:07:37.967141+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 1013,
      "source_url": "https://github.com/trending/rust?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOPAsbmQ",
    "full_name": "trymirai/uzu",
    "stargazers_count": 3358,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "7621d17e34842470f59e711e3087cc4428d1dd41117fc6d3ddeb1e0fa6f56b20",
    "last_success_at": "2026-11-17T03:55:04.285249+00:00"
  }
}
```

</details>
