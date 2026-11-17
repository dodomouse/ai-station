# Upscayl

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[upscayl/upscayl](https://github.com/upscayl/upscayl)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 52784 |
| 许可证 / License | AGPL-3.0 |
| 评估时间 / Evaluated at | 2026-11-17T04:01:50.032580+00:00 |

## 中文

使用 AI 超分辨率模型放大低分辨率图像的桌面工具，支持批量处理和模型选择。

### 用途与功能

- 在桌面界面中选择图片、模型和输出位置。
- 使用批量模式处理多张图片。
- 选择 GPU，并可接入兼容的自定义模型。

### 环境与限制

提供 Linux、macOS 12+ 和 Windows 10+ 安装路径，需要 Vulkan 兼容 GPU，多数集成显卡和纯 CPU 环境不适用。超分辨率会推测细节，不能保证恢复真实细节或修复失焦。AGPL-3.0 覆盖应用代码；模型及图片素材许可另行确认。当前最近正式版本发布于 2024-12-25，近期开发分支功能尚未正式发布。

### 开始使用

从 Releases 下载对应平台的正式版，按 README 检查 GPU 兼容性，再选择图片、模型与输出目录并处理。

参阅[官方 README](https://github.com/upscayl/upscayl/blob/a00d55fee90e0f9435d5eaa86e76700df8199af8/README.md)。

### 收录与来源

适合希望在本机批量放大图片的用户。维护判断使用 upgrade-codebase 开发分支的实现证据。默认分支最新提交仅在 2026-03-27 修改文档。最近核对到的代码修复是 2025-09-24 的语言选择器修复。开发分支的背景移除功能不计入正式版功能说明。

维护证据：[upgrade-codebase 开发分支新增本地背景移除的进程调用、进度处理、取消及 PNG 导出逻辑。需另备 WithoutBG 运行资源，尚未正式发布](https://github.com/upscayl/upscayl/commit/648c0c7900cde2bcd42a11f3078989911d1ad371)（2026-08-20）。

发现于 [GitHub 月榜](https://github.com/trending/typescript?since=monthly&spoken_language_code=en)。2026-11-17 的榜单记录新增 2,272 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

A desktop tool that enlarges low-resolution images with AI super-resolution models, supporting batch processing and model selection.

### Uses and features

- Select images, models and an output location in a desktop interface.
- Process multiple images in batch mode.
- Select a GPU and use compatible custom models.

### Requirements and limits

Installation paths cover Linux, macOS 12+ and Windows 10+. A Vulkan-compatible GPU is required; most integrated GPUs and CPU-only systems are unsuitable. Super-resolution infers detail and cannot guarantee recovery of true detail or correction of defocus. AGPL-3.0 covers application code; model and image rights need separate review. The latest stable release was published on 2024-12-25; recent development-branch features are not yet in a stable release.

### Getting started

Download the stable release for your platform, check GPU compatibility in the README, then choose an image, model and output directory.

See the [official README](https://github.com/upscayl/upscayl/blob/a00d55fee90e0f9435d5eaa86e76700df8199af8/README.md).

### Review and provenance

Useful for local batch image upscaling. Maintenance evidence comes from the upgrade-codebase development branch. The default branch’s latest commit only changed documentation on 2026-03-27; its most recent reviewed code fix is the language-selector correction from 2025-09-24. Development-branch background removal is not presented as a stable-release feature.

Maintenance evidence: [The upgrade-codebase development branch adds local background-removal process invocation, progress handling, cancellation and PNG export; it requires separately staged WithoutBG runtime resources and is not in a stable release](https://github.com/upscayl/upscayl/commit/648c0c7900cde2bcd42a11f3078989911d1ad371) (2026-08-20).

Discovered in [GitHub monthly Trending](https://github.com/trending/typescript?since=monthly&spoken_language_code=en), which recorded 2,272 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:01:50.032580+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "upscayl",
    "name": "Upscayl",
    "repository": "upscayl/upscayl",
    "repo_node_id": "R_kgDOHvghIw",
    "category": "media",
    "summary": {
      "zh-CN": "使用 AI 超分辨率模型放大低分辨率图像的桌面工具，支持批量处理和模型选择。",
      "en": "A desktop tool that enlarges low-resolution images with AI super-resolution models, supporting batch processing and model selection."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:01:50.032580+00:00",
        "en": "2026-11-17T04:01:50.032580+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合希望在本机批量放大图片的用户。维护判断使用 upgrade-codebase 开发分支的实现证据。默认分支最新提交仅在 2026-03-27 修改文档。最近核对到的代码修复是 2025-09-24 的语言选择器修复。开发分支的背景移除功能不计入正式版功能说明。",
      "en": "Useful for local batch image upscaling. Maintenance evidence comes from the upgrade-codebase development branch. The default branch’s latest commit only changed documentation on 2026-03-27; its most recent reviewed code fix is the language-selector correction from 2025-09-24. Development-branch background removal is not presented as a stable-release feature.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "AGPL-3.0",
      "osi_approved": true,
      "source_url": "https://github.com/upscayl/upscayl/blob/a00d55fee90e0f9435d5eaa86e76700df8199af8/LICENSE",
      "license_sha256": "8486a10c4393cee1c25392769ddd3b2d6c242d6ec7928e1414efff7dfb2f07ef",
      "source_commit": "a00d55fee90e0f9435d5eaa86e76700df8199af8",
      "reviewed_at": "2026-11-17T04:01:50.032580+00:00",
      "evidence_pinned_at": "2026-11-17T04:01:50.032580+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "AGPL-3.0 covers the Upscayl application. Model weights, third-party components and input image rights require separate review."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-08-20T01:28:45Z",
        "reviewed_at": "2026-11-17T04:01:50.032580+00:00",
        "url": "https://github.com/upscayl/upscayl/commit/648c0c7900cde2bcd42a11f3078989911d1ad371",
        "qualifies": true,
        "reason": {
          "zh-CN": "upgrade-codebase 开发分支新增本地背景移除的进程调用、进度处理、取消及 PNG 导出逻辑。需另备 WithoutBG 运行资源，尚未正式发布",
          "en": "The upgrade-codebase development branch adds local background-removal process invocation, progress handling, cancellation and PNG export; it requires separately staged WithoutBG runtime resources and is not in a stable release"
        },
        "reviewed_files": [
          "electron/commands/remove-background.ts",
          "electron/utils/remove-background.ts",
          "electron/index.ts",
          "resources/withoutbg/README.md"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/upscayl/upscayl",
        "accessed_at": "2026-11-17T04:01:50.032580+00:00"
      },
      {
        "url": "https://github.com/upscayl/upscayl/blob/a00d55fee90e0f9435d5eaa86e76700df8199af8/README.md",
        "accessed_at": "2026-11-17T04:01:50.032580+00:00"
      },
      {
        "url": "https://github.com/upscayl/upscayl/blob/a00d55fee90e0f9435d5eaa86e76700df8199af8/LICENSE",
        "accessed_at": "2026-11-17T04:01:50.032580+00:00"
      },
      {
        "url": "https://github.com/upscayl/upscayl/commit/648c0c7900cde2bcd42a11f3078989911d1ad371",
        "accessed_at": "2026-11-17T04:01:50.032580+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 2272,
      "source_url": "https://github.com/trending/typescript?since=monthly&spoken_language_code=en",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOHvghIw",
    "full_name": "upscayl/upscayl",
    "stargazers_count": 52784,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "AGPL-3.0",
    "license_sha256": "8486a10c4393cee1c25392769ddd3b2d6c242d6ec7928e1414efff7dfb2f07ef",
    "last_success_at": "2026-11-17T03:55:35.400688+00:00"
  }
}
```

</details>
