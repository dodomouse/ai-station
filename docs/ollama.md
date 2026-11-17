# Ollama

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[ollama/ollama](https://github.com/ollama/ollama)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 187285 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T03:59:14.750906+00:00 |

## 中文

下载、管理和运行语言模型，通过命令行及本地 API 为应用和智能体提供模型访问。

### 用途与功能

- 通过命令行启动模型对话并管理模型。
- 提供 REST API，以及独立的 Python 和 JavaScript 客户端。
- 通过集成入口连接编程助手等应用。

### 环境与限制

提供 macOS、Windows、Linux 与 Docker 安装路径。模型大小、上下文长度及后端决定内存和显存需求；MIT 软件许可不覆盖下载模型或云服务。使用云模型会调用外部服务。

### 开始使用

从官方安装入口选择平台，运行 `ollama` 按提示选模型；应用集成可从 README 的 REST API 示例开始。

参阅[官方 README](https://github.com/ollama/ollama/blob/312c3c8d0c2709209ebbc816ca352bcaf52c19b5/README.md)。

### 收录与来源

适合需要统一模型下载、交互和 API 调用入口的本地 AI 开发。

维护证据：[修复 Ctrl+C 或 Ctrl+G 丢弃输入后仍停留在多行模式的问题](https://github.com/ollama/ollama/commit/169626b403796ce482b3de0b3dd4bc3afdb15438)（2026-11-17）。

发现于 [GitHub 月榜](https://github.com/trending/go?since=monthly)。2026-11-17 的榜单记录新增 4,744 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Download, manage and run language models, exposing model access to applications and agents through a CLI and local API.

### Uses and features

- Start model conversations and manage models through the CLI.
- Provide a REST API and separate Python and JavaScript clients.
- Connect applications such as coding assistants through integration commands.

### Requirements and limits

Installation paths cover macOS, Windows, Linux and Docker. Memory requirements depend on model size, context length and backend. The MIT software license does not cover downloaded models or cloud services; cloud models call external services.

### Getting started

Choose your platform from the official installation options, run `ollama` to select a model, and use the README REST API example for application integration.

See the [official README](https://github.com/ollama/ollama/blob/312c3c8d0c2709209ebbc816ca352bcaf52c19b5/README.md).

### Review and provenance

Useful for local AI development needing a common entry point for model downloads, interaction and API calls.

Maintenance evidence: [Fixes multiline mode remaining active after Ctrl+C or Ctrl+G discards input](https://github.com/ollama/ollama/commit/169626b403796ce482b3de0b3dd4bc3afdb15438) (2026-11-17).

Discovered in [GitHub monthly Trending](https://github.com/trending/go?since=monthly), which recorded 4,744 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T03:59:14.750906+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "ollama",
    "name": "Ollama",
    "repository": "ollama/ollama",
    "repo_node_id": "R_kgDOJ0Z1Pg",
    "category": "ai",
    "summary": {
      "zh-CN": "下载、管理和运行语言模型，通过命令行及本地 API 为应用和智能体提供模型访问。",
      "en": "Download, manage and run language models, exposing model access to applications and agents through a CLI and local API."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T03:59:14.750906+00:00",
        "en": "2026-11-17T03:59:14.750906+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合需要统一模型下载、交互和 API 调用入口的本地 AI 开发。",
      "en": "Useful for local AI development needing a common entry point for model downloads, interaction and API calls.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/ollama/ollama/blob/312c3c8d0c2709209ebbc816ca352bcaf52c19b5/LICENSE",
      "license_sha256": "5934ed2ce0d15154bcdb9c85203210abac0da4314af34081e36df4599f90b226",
      "source_commit": "312c3c8d0c2709209ebbc816ca352bcaf52c19b5",
      "reviewed_at": "2026-11-17T03:59:14.750906+00:00",
      "evidence_pinned_at": "2026-11-17T03:59:14.750906+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "MIT applies to Ollama software. Models and Ollama cloud services retain their respective licenses and terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-17T02:20:35Z",
        "reviewed_at": "2026-11-17T03:59:14.750906+00:00",
        "url": "https://github.com/ollama/ollama/commit/169626b403796ce482b3de0b3dd4bc3afdb15438",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复 Ctrl+C 或 Ctrl+G 丢弃输入后仍停留在多行模式的问题",
          "en": "Fixes multiline mode remaining active after Ctrl+C or Ctrl+G discards input"
        },
        "reviewed_files": [
          "cmd/interactive.go"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/ollama/ollama",
        "accessed_at": "2026-11-17T03:59:14.750906+00:00"
      },
      {
        "url": "https://github.com/ollama/ollama/blob/312c3c8d0c2709209ebbc816ca352bcaf52c19b5/README.md",
        "accessed_at": "2026-11-17T03:59:14.750906+00:00"
      },
      {
        "url": "https://github.com/ollama/ollama/blob/312c3c8d0c2709209ebbc816ca352bcaf52c19b5/LICENSE",
        "accessed_at": "2026-11-17T03:59:14.750906+00:00"
      },
      {
        "url": "https://github.com/ollama/ollama/commit/169626b403796ce482b3de0b3dd4bc3afdb15438",
        "accessed_at": "2026-11-17T03:59:14.750906+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 4744,
      "source_url": "https://github.com/trending/go?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOJ0Z1Pg",
    "full_name": "ollama/ollama",
    "stargazers_count": 187285,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "5934ed2ce0d15154bcdb9c85203210abac0da4314af34081e36df4599f90b226",
    "last_success_at": "2026-11-17T03:52:05.088128+00:00"
  }
}
```

</details>
