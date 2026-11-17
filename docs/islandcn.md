# islandcn

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[opencoredev/islandcn](https://github.com/opencoredev/islandcn)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 760 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:30:19.931551Z |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:27:10.010Z |

## 中文

### 用途与功能

为 React 网页提供灵动岛样式的活动提示组件。包含活动状态、展开收起、动画和多个用途预设。

可用于上传进度、计时器、播放状态或录音。支持通过 shadcn 引入源码，并提供交互示例和文档。

### 环境与限制

需要 React 工程；开发示例使用 pnpm。项目未包含用于运动对比的参考录屏，对应比较功能和测试受限。并非 Apple 官方组件，商标和视觉使用需另行判断。

### 入门与收录判断

从[官方 README](https://github.com/opencoredev/islandcn/blob/main/README.md)查阅安装和使用步骤。虽不足 1000 Star，但活动状态和动画已有完整实现，并有安装入口、预设和可读 API 文档。

本轮为文档复核，未安装、运行或测试上游项目。2026-11-13 首次公开活动状态存储、动画引擎、预设和组件实现。已核对提交文件及固定版本源码。详见[维护记录](https://github.com/opencoredev/islandcn/commit/dfa6ad7a39750c822c7807fcd892e9394aa57318)。

### 文章来源

发现于“逛逛GitHub”在 2026-11-16 发布的[《8 个开源工具速览》](https://www.woshipm.com/ai/6494405.html)。已读取作者署名正文，功能和限制另按当前上游复核。

## English

### Purpose and features

A Dynamic Island-style activity component for React, with state management, transitions, animation and reusable presets.

Supports uploads, timers, playback and recording, with source installation through shadcn and interactive examples.

### Requirements and limits

Requires a React project; the development site uses pnpm. Reference recordings are absent, limiting comparison features and one test. This is not an official Apple component.

### Getting started and review

Use the [official README](https://github.com/opencoredev/islandcn/blob/main/README.md) for installation and usage. This is a documentation review; the software was not installed or tested. The 2026-11-13 implementation adds the activity store, animation engine, presets and components; commit files and pinned source were reviewed. See the [activity evidence](https://github.com/opencoredev/islandcn/commit/dfa6ad7a39750c822c7807fcd892e9394aa57318).

The project appears in the account's [author-published article dated 2026-11-16](https://www.woshipm.com/ai/6494405.html). Current upstream documentation supports the feature descriptions.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:30:19.931551Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "islandcn",
    "name": "islandcn",
    "repository": "opencoredev/islandcn",
    "repo_node_id": "R_kgDOVtD-og",
    "category": "development",
    "summary": {
      "zh-CN": "为 React 网页提供灵动岛样式的活动提示组件。包含活动状态、展开收起、动画和多个用途预设。",
      "en": "A Dynamic Island-style activity component for React, with state management, transitions, animation and reusable presets."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:30:19.931551Z",
        "en": "2026-11-16T14:30:19.931551Z"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "basis": "虽不足 1000 Star，但活动状态和动画已有完整实现，并有安装入口、预设和可读 API 文档。",
      "rationale": "虽不足 1000 Star，但活动状态和动画已有完整实现，并有安装入口、预设和可读 API 文档。",
      "stars_are_advisory": true,
      "reviewed_at": "2026-11-16T14:30:19.931551Z"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "0fdb775e00e6fdde23984b4f1184cd13c34135caac1e714ad489141c239704bc",
      "source_url": "https://github.com/opencoredev/islandcn/blob/0011a41ea4882f3818caf35c98f3ee46b80c4a2c/LICENSE",
      "reviewed_at": "2026-11-16T14:30:19.931551Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "0011a41ea4882f3818caf35c98f3ee46b80c4a2c"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-13T11:50:49Z",
        "reviewed_at": "2026-11-16T14:30:19.931551Z",
        "url": "https://github.com/opencoredev/islandcn/commit/dfa6ad7a39750c822c7807fcd892e9394aa57318",
        "qualifies": true,
        "reason": {
          "zh-CN": "2026-11-13 首次公开活动状态存储、动画引擎、预设和组件实现。已核对提交文件及固定版本源码。",
          "en": "The 2026-11-13 implementation adds the activity store, animation engine, presets and components; commit files and pinned source were reviewed."
        },
        "reviewed_files": [
          "lib/island/README.md",
          "lib/island/choreography.ts",
          "lib/island/clock.ts",
          "lib/island/config.ts",
          "lib/island/context.ts",
          "lib/island/devtools.ts",
          "lib/island/frame.ts",
          "lib/island/geometry.ts",
          "lib/island/index.ts",
          "lib/island/island-root.tsx",
          "lib/island/layer.tsx",
          "lib/island/metrics.ts"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/opencoredev/islandcn",
        "accessed_at": "2026-11-16T14:27:10.010Z",
        "supports": "Repository identity, Stars and public state."
      },
      {
        "url": "https://github.com/opencoredev/islandcn/blob/main/README.md",
        "accessed_at": "2026-11-16T14:30:19.931551Z",
        "supports": "Capabilities, requirements and limits."
      },
      {
        "url": "https://www.woshipm.com/ai/6494405.html",
        "published_date": "2026-11-16",
        "accessed_at": "2026-11-16T14:30:19.931551Z",
        "supports": "Author-published article body and account attribution."
      }
    ],
    "discovery": {
      "account": "逛逛GitHub",
      "article_url": "https://www.woshipm.com/ai/6494405.html",
      "published_date": "2026-11-16",
      "body_verification": "author_published_article"
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVtD-og",
    "full_name": "opencoredev/islandcn",
    "stargazers_count": 760,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "0fdb775e00e6fdde23984b4f1184cd13c34135caac1e714ad489141c239704bc",
    "last_success_at": "2026-11-16T14:27:10.010Z"
  }
}
```

</details>
