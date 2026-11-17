# Remotion

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[remotion-dev/remotion](https://github.com/remotion-dev/remotion)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 73840 |
| 评估时间 / Evaluated at | 2026-11-17T14:46:39.921047Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:39:45.859Z |

## 中文

用 React 和网页技术制作视频，支持编码智能体生成工程、交互预览和批量渲染。

让 AI 编码智能体把视频需求转成可编辑的组件、动画和渲染任务。

### 主要功能

- 用组件组织画面、字幕、音频和转场。
- 在 Remotion Studio 预览内容，再通过本地或服务端流程渲染。
- 提供模板和 Agent Skills，支持参数化视频与批量制作。

### 环境要求

- 命令行路线需要 Node.js 16 或更高版本。也可使用 Bun 1.0.3 或更高版本。按所选模板配置包管理器。
- macOS 需要 15 或更新版本。Linux 通常需要 glibc 2.35 起及官方列出的额外依赖。Amazon Linux 2023 的 ARM64 支持 glibc 2.34。
- 通过提示生成视频时，还需安装并配置兼容的编码智能体。其模型或订阅费用由对应提供商决定。

### 使用限制

- 空白模板需要添加画面内容后才有可用成片。生成的代码仍需预览和检查。
- Alpine Linux、nixOS 和 Amazon Linux 2023 x64 不受支持。
- 本地渲染、浏览器渲染和云端渲染的配置不同，应按所选方式配置运行环境。
- 部分企业使用情形需要 Company License，使用前应核对上游条款。许可不影响本库的收录资格。

### 开始使用

1. 按[安装指南](https://www.remotion.dev/docs)准备 Node.js，运行 `npx create-video@latest` 并选择模板。
2. 进入工程，按[Agent 指南](https://www.remotion.dev/docs/ai/coding-agents)添加技能，运行 `npm run dev` 打开预览。
3. 让编码智能体实现画面和动画，检查预览后按[渲染指南](https://www.remotion.dev/docs/render)导出视频。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:39:45.859Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/remotion-dev/remotion/commit/47fa0af4d8a89c7e442e3ab4fe6ff67eb7fe16cd)。Merge pull request #13497 from remotion-dev/codex/transition-premount-warmup

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/remotion-dev/remotion/blob/main/README.md)
- [GitHub 元数据 / Repository metadata](https://api.github.com/repos/remotion-dev/remotion)
- [创建工程 / Creating a project](https://www.remotion.dev/docs)
- [编码智能体接入 / Coding-agent workflow](https://www.remotion.dev/docs/ai/coding-agents)
- [上游使用条款 / Upstream usage terms](https://github.com/remotion-dev/remotion/blob/main/LICENSE.md)

## English

Creates videos with React and web technology, with coding-agent workflows, interactive previews and batch rendering.

Lets AI coding agents turn video requests into editable components, animations and rendering jobs.

### Features

- Builds scenes, captions, audio and transitions from components.
- Previews content in Remotion Studio and renders it through local or server-side workflows.
- Provides templates and Agent Skills for parameterized videos and batch production.

### Requirements

- The command-line workflow requires Node.js 16 or later, or Bun 1.0.3 or later. Use the package manager for the selected template.
- Requires macOS 15 or later. Linux generally needs glibc 2.35 or later and the listed extra dependencies; Amazon Linux 2023 on ARM64 supports glibc 2.34.
- Prompt-driven video creation also requires a compatible, configured coding agent; its provider determines model or subscription charges.

### Limitations

- The blank template needs content before it produces a usable video. Generated code still requires preview and review.
- Alpine Linux, nixOS and Amazon Linux 2023 on x64 are unsupported.
- Local, browser and cloud rendering use different configurations; follow the guide for the selected runtime.
- Some company use cases require a Company License. Check upstream terms before use; licensing does not determine catalog admission.

### Getting started

1. Prepare Node.js using the [installation guide](https://www.remotion.dev/docs), run `npx create-video@latest` and select a template.
2. Enter the project, add skills using the [agent guide](https://www.remotion.dev/docs/ai/coding-agents), and run `npm run dev` to open the preview.
3. Use the coding agent to implement scenes and animation, review the preview, then export using the [rendering guide](https://www.remotion.dev/docs/render).

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:39:45.859Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/remotion-dev/remotion/commit/47fa0af4d8a89c7e442e3ab4fe6ff67eb7fe16cd).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/remotion-dev/remotion/blob/main/README.md)
- [GitHub 元数据 / Repository metadata](https://api.github.com/repos/remotion-dev/remotion)
- [创建工程 / Creating a project](https://www.remotion.dev/docs)
- [编码智能体接入 / Coding-agent workflow](https://www.remotion.dev/docs/ai/coding-agents)
- [上游使用条款 / Upstream usage terms](https://github.com/remotion-dev/remotion/blob/main/LICENSE.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:46:39.921047Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "remotion",
    "name": "Remotion",
    "repository": "remotion-dev/remotion",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkyNzQ0OTU0MjU=",
    "category": "media",
    "summary": {
      "zh-CN": "用 React 和网页技术制作视频，支持编码智能体生成工程、交互预览和批量渲染。",
      "en": "Creates videos with React and web technology, with coding-agent workflows, interactive previews and batch rendering."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:46:39.921047Z",
        "en": "2026-11-17T14:46:39.921047Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "让 AI 编码智能体把视频需求转成可编辑的组件、动画和渲染任务。",
        "en": "Lets AI coding agents turn video requests into editable components, animations and rendering jobs."
      },
      "source_url": "https://github.com/remotion-dev/remotion/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/remotion-dev/remotion/commit/47fa0af4d8a89c7e442e3ab4fe6ff67eb7fe16cd",
        "occurred_at": "2026-11-17T14:26:44Z",
        "reviewed_at": "2026-11-17T14:46:39.921047Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "Merge pull request #13497 from remotion-dev/codex/transition-premount-warmup 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/remotion-dev/remotion/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / Repository metadata",
        "url": "https://api.github.com/repos/remotion-dev/remotion"
      },
      {
        "title": "创建工程 / Creating a project",
        "url": "https://www.remotion.dev/docs"
      },
      {
        "title": "编码智能体接入 / Coding-agent workflow",
        "url": "https://www.remotion.dev/docs/ai/coding-agents"
      },
      {
        "title": "上游使用条款 / Upstream usage terms",
        "url": "https://github.com/remotion-dev/remotion/blob/main/LICENSE.md"
      }
    ]
  },
  "snapshot": {
    "full_name": "remotion-dev/remotion",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkyNzQ0OTU0MjU=",
    "stargazers_count": 73840,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:39:45.859Z",
    "source_url": "https://api.github.com/repos/remotion-dev/remotion"
  }
}
```

</details>
