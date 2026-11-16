# llmfit

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[AlexsJones/llmfit](https://github.com/AlexsJones/llmfit)

| 项目 / Field | 内容 / Value |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 39014 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:50:50.290410+00:00 |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:20:19.248Z |

## 中文

检测 CPU、内存和 GPU 显存，估算本地模型及量化版本的适配程度，并提供 TUI、网页、CLI/API 与基准测试入口。

**环境与限制：** 支持 macOS、Linux、Windows。可结合多种运行时，包括 Ollama、llama.cpp 和 MLX。适配估算不是实测吞吐保证，下载和实际运行仍取决于模型许可、运行时与硬件。

**入门：** 从[官方说明](https://raw.githubusercontent.com/AlexsJones/llmfit/main/README.md)确认安装与配置步骤，再查看[发布版本](https://github.com/AlexsJones/llmfit/releases)。本次为文档、许可原文与维护证据审查，未安装运行。

**近期维护：** [v1.1.20 修复不支持格式的处理和注意力参数估算。](https://github.com/AlexsJones/llmfit/releases/tag/v1.1.20)（2026-11-03）

## English

Detects CPU, RAM and GPU memory to estimate local model and quantization fit, exposing TUI, web, CLI/API and benchmarking interfaces.

**Requirements and limitations:** Supports macOS, Linux and Windows with runtimes such as Ollama, llama.cpp and MLX. Fit estimates are not measured throughput guarantees; downloads and execution depend on model licenses, runtimes and hardware.

**Getting started:** Follow the [official documentation](https://raw.githubusercontent.com/AlexsJones/llmfit/main/README.md) for setup, then check [releases](https://github.com/AlexsJones/llmfit/releases). This review examined documentation, license text and maintenance evidence; the software was not installed or run.

**Recent maintenance:** [v1.1.20 fixes unsupported-format handling and attention-parameter estimation.](https://github.com/AlexsJones/llmfit/releases/tag/v1.1.20) (2026-11-03)

## Review evidence

发现线索来自第三方公众号文章索引，原始微信正文未完整读取；用途、环境、许可与维护状态依据仓库当前资料复核。

Discovery uses a third-party WeChat article index; the original article body was not fully read. Current repository sources were reviewed for function, requirements, licensing and maintenance.

- 公众号索引原文 / Indexed WeChat source：[一周没逛 GitHub 不要紧，这 TOP 10 的热门开源项目整理好了。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536122&idx=1&sn=b7a284d06296707235d8dde07c6f6d4e)（2026-08-23）

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-16T14:50:50.290410+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "llmfit",
    "name": "llmfit",
    "repository": "AlexsJones/llmfit",
    "repo_node_id": "R_kgDORQ6nQA",
    "category": "ai",
    "summary": {
      "zh-CN": "检测 CPU、内存和 GPU 显存，估算本地模型及量化版本的适配程度，并提供 TUI、网页、CLI/API 与基准测试入口。",
      "en": "Detects CPU, RAM and GPU memory to estimate local model and quantization fit, exposing TUI, web, CLI/API and benchmarking interfaces."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:50:50.290410+00:00",
        "en": "2026-11-16T14:50:50.290410+00:00"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "b52696dc0457bf58616f5017e5146b2932611b9357bb9824c7c91183fc36471f",
      "source_url": "https://raw.githubusercontent.com/AlexsJones/llmfit/main/LICENSE",
      "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
      "files": [
        {
          "path": "LICENSE",
          "source_url": "https://raw.githubusercontent.com/AlexsJones/llmfit/main/LICENSE",
          "fetched_at": "2026-11-16T14:23:40.610Z",
          "sha256": "b52696dc0457bf58616f5017e5146b2932611b9357bb9824c7c91183fc36471f"
        }
      ]
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-11-03T17:39:35Z",
        "url": "https://github.com/AlexsJones/llmfit/releases/tag/v1.1.20",
        "tag": "v1.1.20",
        "summary": "v1.1.20",
        "draft": false,
        "prerelease": false,
        "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
        "qualifies": true,
        "reason": {
          "zh-CN": "v1.1.20 修复不支持格式的处理和注意力参数估算。",
          "en": "v1.1.20 fixes unsupported-format handling and attention-parameter estimation."
        }
      }
    ],
    "sources": [
      {
        "article_id": "2247536122_1",
        "title": "一周没逛 GitHub 不要紧，这 TOP 10 的热门开源项目整理好了。",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536122&idx=1&sn=b7a284d06296707235d8dde07c6f6d4e",
        "published_date": "2026-08-23",
        "account": "逛逛GitHub",
        "source_strength": "third_party_index",
        "index_url": "https://www.noking.tech/github-radar/data/library.json",
        "original_article_body_read": false
      }
    ],
    "discovery": {
      "account": "逛逛GitHub",
      "window_start": "2026-08-16",
      "window_end": "2026-11-16",
      "original_article_body_read": false,
      "repository_review_sources": [
        "https://api.github.com/repos/alexsjones/llmfit",
        "https://raw.githubusercontent.com/AlexsJones/llmfit/main/README.md",
        "https://github.com/AlexsJones/llmfit/releases/tag/v1.1.20",
        "https://raw.githubusercontent.com/AlexsJones/llmfit/main/LICENSE"
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDORQ6nQA",
    "full_name": "AlexsJones/llmfit",
    "stargazers_count": 39014,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "b52696dc0457bf58616f5017e5146b2932611b9357bb9824c7c91183fc36471f",
    "last_success_at": "2026-11-16T14:20:19.248Z"
  }
}
```

</details>
