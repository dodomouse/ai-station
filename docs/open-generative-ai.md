# Open Generative AI

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 35058 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T04:07:37.959341+00:00 |

## 中文

可自行部署的 AI 图像和视频创作界面，连接 MuAPI 云模型；桌面版还提供本地推理引擎接入。

### 用途与功能

- 提供文生图、图生图、文生视频及图生视频工作区。
- 组合多种创作流程，包括参考图、音频与口型同步。
- 保存生成历史，并可使用节点式工作流串联模型。

### 环境与限制

云端生成需要 MuAPI 密钥，输入会发送到该服务并受其费用和条款约束。桌面本地模式需下载模型；sd.cpp 和自行安装的 Wan2GP 有不同硬件要求。源码开发需要 Node.js 18+、子模块和工作区构建。MIT 覆盖本项目代码，不自动覆盖模型、子模块或生成素材权利。

### 开始使用

从发行版选择桌面安装包，或按 README 克隆含子模块的源码并运行 setup。在设置中配置 MuAPI 或桌面本地模型。

参阅[官方 README](https://github.com/Anil-matcha/Open-Generative-AI/blob/810b52c1996af20b0ddeff52a3c1864a66984e91/README.md)。

### 收录与来源

适合需要统一管理不同生成模型、参考素材和多步创作流程的用户。

维护证据：[增加明暗主题切换和本地保存，并在页面首次绘制前恢复主题](https://github.com/Anil-matcha/Open-Generative-AI/commit/4c17b87afacc9a1b6d4eb2ecc35199a4291133b4)（2026-11-16）。

发现于 [GitHub 月榜](https://github.com/trending/javascript?since=monthly)。2026-11-17 的榜单记录新增 4,570 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

A self-hostable interface for AI image and video creation through MuAPI cloud models, with local inference-engine integrations in the desktop app.

### Uses and features

- Provide text-to-image, image-to-image, text-to-video and image-to-video workspaces.
- Combine reference images, audio and lip-sync workflows.
- Save generation history and chain models with node-based workflows.

### Requirements and limits

Cloud generation requires a MuAPI key and sends inputs to that service under its costs and terms. Desktop local mode requires model downloads; sd.cpp and a separately installed Wan2GP have different hardware requirements. Source development needs Node.js 18+, submodules and workspace builds. MIT covers this project’s code, not automatically models, submodules or rights in generated assets.

### Getting started

Choose a desktop release, or follow the README to clone with submodules and run setup. Configure MuAPI or desktop local models in settings.

See the [official README](https://github.com/Anil-matcha/Open-Generative-AI/blob/810b52c1996af20b0ddeff52a3c1864a66984e91/README.md).

### Review and provenance

Useful for managing multiple generation models, reference assets and multistep creative workflows in one interface.

Maintenance evidence: [Adds a persistent light/dark theme toggle and restores the saved theme before the first page paint](https://github.com/Anil-matcha/Open-Generative-AI/commit/4c17b87afacc9a1b6d4eb2ecc35199a4291133b4) (2026-11-16).

Discovered in [GitHub monthly Trending](https://github.com/trending/javascript?since=monthly), which recorded 4,570 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:07:37.959341+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "open-generative-ai",
    "name": "Open Generative AI",
    "repository": "Anil-matcha/Open-Generative-AI",
    "repo_node_id": "R_kgDOJg7yeg",
    "category": "media",
    "summary": {
      "zh-CN": "可自行部署的 AI 图像和视频创作界面，连接 MuAPI 云模型；桌面版还提供本地推理引擎接入。",
      "en": "A self-hostable interface for AI image and video creation through MuAPI cloud models, with local inference-engine integrations in the desktop app."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:07:37.959341+00:00",
        "en": "2026-11-17T04:07:37.959341+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合需要统一管理不同生成模型、参考素材和多步创作流程的用户。",
      "en": "Useful for managing multiple generation models, reference assets and multistep creative workflows in one interface.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/Anil-matcha/Open-Generative-AI/blob/810b52c1996af20b0ddeff52a3c1864a66984e91/LICENSE",
      "license_sha256": "17cd23239df0ac94d279e0d4da4f2a34148346f9af3407b085b15772673522b6",
      "source_commit": "810b52c1996af20b0ddeff52a3c1864a66984e91",
      "reviewed_at": "2026-11-17T04:07:37.959341+00:00",
      "evidence_pinned_at": "2026-11-17T04:07:37.959341+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "MIT covers this repository code. MuAPI service terms, submodule licenses, local inference engines and model licenses must be considered separately."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-16T14:25:35Z",
        "reviewed_at": "2026-11-17T04:07:37.959341+00:00",
        "url": "https://github.com/Anil-matcha/Open-Generative-AI/commit/4c17b87afacc9a1b6d4eb2ecc35199a4291133b4",
        "qualifies": true,
        "reason": {
          "zh-CN": "增加明暗主题切换和本地保存，并在页面首次绘制前恢复主题",
          "en": "Adds a persistent light/dark theme toggle and restores the saved theme before the first page paint"
        },
        "reviewed_files": [
          "components/ThemeToggle.js",
          "app/layout.js"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/Anil-matcha/Open-Generative-AI",
        "accessed_at": "2026-11-17T04:07:37.959341+00:00"
      },
      {
        "url": "https://github.com/Anil-matcha/Open-Generative-AI/blob/810b52c1996af20b0ddeff52a3c1864a66984e91/README.md",
        "accessed_at": "2026-11-17T04:07:37.959341+00:00"
      },
      {
        "url": "https://github.com/Anil-matcha/Open-Generative-AI/blob/810b52c1996af20b0ddeff52a3c1864a66984e91/LICENSE",
        "accessed_at": "2026-11-17T04:07:37.959341+00:00"
      },
      {
        "url": "https://github.com/Anil-matcha/Open-Generative-AI/commit/4c17b87afacc9a1b6d4eb2ecc35199a4291133b4",
        "accessed_at": "2026-11-17T04:07:37.959341+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 4570,
      "source_url": "https://github.com/trending/javascript?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOJg7yeg",
    "full_name": "Anil-matcha/Open-Generative-AI",
    "stargazers_count": 35058,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "17cd23239df0ac94d279e0d4da4f2a34148346f9af3407b085b15772673522b6",
    "last_success_at": "2026-11-17T03:52:17.622204+00:00"
  }
}
```

</details>
