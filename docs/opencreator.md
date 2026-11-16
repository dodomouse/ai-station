# OpenCreator

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[krillinai/OpenCreator](https://github.com/krillinai/OpenCreator)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 14380 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:29:18.253Z |

## 中文

以对话与可视化工作区组织内容制作，管理生成任务、素材、字幕和版本。

### 用途与功能

- 制作图片、视频和字幕内容
- 通过可复用技能与定时任务管理创作流程

以 Codex CLI 为执行引擎，提供本地 Runtime、Web 与 Electron 桌面端；支持技能、MCP、任务历史、进度与版本管理。v3.3.2 发布说明包含独立转录与字幕编辑器。

### 环境与限制

桌面安装包提供 macOS ARM/Intel 和 Windows x64。源码运行需 Node.js 22+、pnpm 9.15.0 和可用 Codex CLI。真实任务需要有效的模型登录或 API 配置；本地保存项目不表示推理离线。媒体工具和各模型服务另有依赖、可用范围、费用与许可。

### 开始使用

从 Releases 安装匹配平台的桌面包，完成模型配置，再建立项目；开发者可按 README 启动 Web。 参阅[官方 README](https://github.com/krillinai/OpenCreator/blob/master/README.md)。

### 收录与来源

同时提供执行后端、可视化编辑和发布包，适合需要保留创作过程与版本的工作流。 最近维护：[v3.3.2](https://github.com/krillinai/OpenCreator/releases/tag/v3.3.2)（2026-11-16T07:09:39Z）。正式版修复桌面与生产 Web 登录网关，并改进历史、字幕和媒体制作流程。

由 Frontier Now 二级索引发现，其页面记录 AI开源求索于 2026-10-14 介绍 OpenCreator；本次未取得该公众号原文。

- 2026-10-14：[Frontier Now 的 OpenCreator 条目](https://frontiernow.dev/zh/github/opencreator/)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。

## English

Organizes content creation through conversation and a visual workspace, managing runs, media, subtitles and revisions.

### Uses and features

- Create images, video and subtitles
- Manage creative workflows with reusable skills and schedules

Uses Codex CLI as its execution engine with a local runtime, Web UI and Electron desktop app. Provides skills, MCP, run history, progress and revision management. Release v3.3.2 documents standalone transcription and subtitle editing.

### Requirements and limits

Desktop installers target macOS ARM/Intel and Windows x64. Source use requires Node.js 22+, pnpm 9.15.0 and Codex CLI. Real tasks require working model authentication or API configuration; local project storage does not imply offline inference. Media tools and model services have separate dependencies, availability, costs and terms.

### Getting started

Install the matching desktop release, configure model access and create a project; developers can start the Web version using the README. See the [official README](https://github.com/krillinai/OpenCreator/blob/master/README.md).

### Review and provenance

Provides an execution backend, visual editing and packaged releases for workflows that retain creative history and revisions. Recent maintenance: [v3.3.2](https://github.com/krillinai/OpenCreator/releases/tag/v3.3.2) (2026-11-16T07:09:39Z). The formal release fixes desktop and production Web sign-in gateway behavior and improves history, subtitles and media workflows.

Discovered through Frontier Now, which attributes an OpenCreator article to AI开源求索 on 2026-10-14. The original account article was not obtained. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:29:18.253Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "opencreator",
    "name": "OpenCreator",
    "repository": "krillinai/OpenCreator",
    "repo_node_id": "R_kgDONeluaA",
    "category": "media",
    "tags": [],
    "forms": [
      "desktop",
      "service"
    ],
    "platforms": [
      "macos",
      "windows",
      "linux"
    ],
    "aliases": {
      "zh-CN": [
        "OpenCreator"
      ],
      "en": [
        "OpenCreator"
      ]
    },
    "summary": {
      "zh-CN": "以对话与可视化工作区组织内容制作，管理生成任务、素材、字幕和版本。",
      "en": "Organizes content creation through conversation and a visual workspace, managing runs, media, subtitles and revisions."
    },
    "use_cases": {
      "zh-CN": [
        "制作图片、视频和字幕内容",
        "通过可复用技能与定时任务管理创作流程"
      ],
      "en": [
        "Create images, video and subtitles",
        "Manage creative workflows with reusable skills and schedules"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:29:18.253Z",
        "en": "2026-11-16T14:29:18.253Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
      "source_url": "https://github.com/krillinai/OpenCreator/blob/master/LICENSE",
      "reviewed_at": "2026-11-16T14:29:18.253Z"
    },
    "activity_evidence": [
      {
        "type": "release",
        "url": "https://github.com/krillinai/OpenCreator/releases/tag/v3.3.2",
        "occurred_at": "2026-11-16T07:09:39Z",
        "reason": {
          "zh-CN": "正式版修复桌面与生产 Web 登录网关，并改进历史、字幕和媒体制作流程。",
          "en": "The formal release fixes desktop and production Web sign-in gateway behavior and improves history, subtitles and media workflows."
        },
        "reviewed_at": "2026-11-16T14:29:18.253Z",
        "qualifies": true
      }
    ],
    "sources": [
      {
        "url": "https://github.com/krillinai/OpenCreator/blob/master/README.md",
        "accessed_at": "2026-11-16T14:29:18.253Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/krillinai/OpenCreator/blob/master/LICENSE",
        "accessed_at": "2026-11-16T14:29:18.253Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://frontiernow.dev/zh/github/opencreator/",
        "accessed_at": "2026-11-16T14:29:18.153Z",
        "supports": {
          "zh-CN": "二级索引中 AI开源求索的归属、日期和发现线索。",
          "en": "Secondary attribution to AI开源求索, date and discovery lead."
        }
      }
    ],
    "quality_review": {
      "basis": {
        "zh-CN": "同时提供执行后端、可视化编辑和发布包，适合需要保留创作过程与版本的工作流。",
        "en": "Provides an execution backend, visual editing and packaged releases for workflows that retain creative history and revisions."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDONeluaA",
    "full_name": "krillinai/OpenCreator",
    "stargazers_count": 14380,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
    "last_success_at": "2026-11-16T14:21:01Z"
  }
}
```

</details>

