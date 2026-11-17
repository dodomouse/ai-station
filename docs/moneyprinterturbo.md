# MoneyPrinterTurbo

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 144052 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T03:59:03.771151+00:00 |

## 中文

将主题或关键词转成脚本、配音、素材和字幕，并合成短视频。

### 用途与功能

- 支持自定义脚本、配音及本地素材。
- 可接入模型、语音和素材服务，生成多种画幅的视频。
- 提供 WebUI、API 和 CLI，并显示制作阶段进度。

### 环境与限制

本地部署需要 Python 3.11+ 及视频处理依赖。所选云端模型、语音和素材服务可能需要账号或 API Key；素材授权须另行核对。GPU 非必需，重型本地处理取决于硬件。

### 开始使用

按 README 安装官方包或使用 Docker，配置模型和素材来源，先用短脚本生成并检查一段视频。

参阅[官方 README](https://github.com/harry0703/MoneyPrinterTurbo/blob/92e0f9a55b91e353565015aab74b7c50cc28f148/README.md)。

### 收录与来源

适合把脚本、配音、字幕和剪辑步骤组合成可重复的视频制作流程。

维护证据：[将 LoomLoom 视频文件下载接入共享 HTTP 追踪器，补齐流式下载请求的脱敏诊断记录。](https://github.com/harry0703/MoneyPrinterTurbo/commit/8dc9b41eb72aa5fbe835c4bac51f071dc6c0fe30)（2026-11-16）。

发现于 [GitHub 月榜](https://github.com/trending/python?since=monthly)。2026-11-17 的榜单记录新增 12,631 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Turns topics or keywords into scripts, narration, assets and subtitles, then composes short videos.

### Uses and features

- Accepts custom scripts, narration and local assets.
- Connects model, speech and asset services to produce videos in several aspect ratios.
- Provides a WebUI, API and CLI with production-stage progress.

### Requirements and limits

Local deployment requires Python 3.11+ and video-processing dependencies. Selected cloud models, speech and asset services may require accounts or API keys; asset rights need separate review. A GPU is optional, with heavier local processing depending on hardware.

### Getting started

Install the official package or use Docker as documented, configure model and asset sources, then generate and inspect a short sample.

See the [official README](https://github.com/harry0703/MoneyPrinterTurbo/blob/92e0f9a55b91e353565015aab74b7c50cc28f148/README.md).

### Review and provenance

Useful for combining scripting, narration, subtitles and editing into a repeatable video-production workflow.

Maintenance evidence: [Routes LoomLoom video downloads through the shared HTTP tracer to include streaming-download requests in redacted diagnostics.](https://github.com/harry0703/MoneyPrinterTurbo/commit/8dc9b41eb72aa5fbe835c4bac51f071dc6c0fe30) (2026-11-16).

Discovered in [GitHub monthly Trending](https://github.com/trending/python?since=monthly), which recorded 12,631 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T03:59:03.771151+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "moneyprinterturbo",
    "name": "MoneyPrinterTurbo",
    "repository": "harry0703/MoneyPrinterTurbo",
    "repo_node_id": "R_kgDOLeediw",
    "category": "media",
    "summary": {
      "zh-CN": "将主题或关键词转成脚本、配音、素材和字幕，并合成短视频。",
      "en": "Turns topics or keywords into scripts, narration, assets and subtitles, then composes short videos."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T03:59:03.771151+00:00",
        "en": "2026-11-17T03:59:03.771151+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合把脚本、配音、字幕和剪辑步骤组合成可重复的视频制作流程。",
      "en": "Useful for combining scripting, narration, subtitles and editing into a repeatable video-production workflow.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/harry0703/MoneyPrinterTurbo/blob/92e0f9a55b91e353565015aab74b7c50cc28f148/LICENSE",
      "license_sha256": "87dd19b6a0779e14a91c1b06423ef251df37e89666160c031130a26bae68c229",
      "source_commit": "92e0f9a55b91e353565015aab74b7c50cc28f148",
      "reviewed_at": "2026-11-17T03:59:03.771151+00:00",
      "evidence_pinned_at": "2026-11-17T03:59:03.771151+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "Applies to repository code and documentation; external models, services, data and assets retain their own terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-16T06:14:51Z",
        "reviewed_at": "2026-11-17T03:59:03.771151+00:00",
        "url": "https://github.com/harry0703/MoneyPrinterTurbo/commit/8dc9b41eb72aa5fbe835c4bac51f071dc6c0fe30",
        "qualifies": true,
        "reason": {
          "zh-CN": "将 LoomLoom 视频文件下载接入共享 HTTP 追踪器，补齐流式下载请求的脱敏诊断记录。",
          "en": "Routes LoomLoom video downloads through the shared HTTP tracer to include streaming-download requests in redacted diagnostics."
        },
        "reviewed_files": [
          "app/services/loomloom.py"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/harry0703/MoneyPrinterTurbo",
        "accessed_at": "2026-11-17T03:59:03.771151+00:00"
      },
      {
        "url": "https://github.com/harry0703/MoneyPrinterTurbo/blob/92e0f9a55b91e353565015aab74b7c50cc28f148/README.md",
        "accessed_at": "2026-11-17T03:59:03.771151+00:00"
      },
      {
        "url": "https://github.com/harry0703/MoneyPrinterTurbo/blob/92e0f9a55b91e353565015aab74b7c50cc28f148/LICENSE",
        "accessed_at": "2026-11-17T03:59:03.771151+00:00"
      },
      {
        "url": "https://github.com/harry0703/MoneyPrinterTurbo/commit/8dc9b41eb72aa5fbe835c4bac51f071dc6c0fe30",
        "accessed_at": "2026-11-17T03:59:03.771151+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 12631,
      "source_url": "https://github.com/trending/python?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOLeediw",
    "full_name": "harry0703/MoneyPrinterTurbo",
    "stargazers_count": 144052,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "87dd19b6a0779e14a91c1b06423ef251df37e89666160c031130a26bae68c229",
    "last_success_at": "2026-11-17T03:53:32.909163+00:00"
  }
}
```

</details>
