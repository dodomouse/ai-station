# Abyssal Garden

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[Noniv/abyssal-garden](https://github.com/Noniv/abyssal-garden)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 1440 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:30:19.931551Z |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:27:09.985Z |

## 中文

### 用途与功能

以单个 HTML 展示可交互的海底场景。使用 WebGPU 绘制地形和生物，并实时合成声音。

提供键鼠导航、画质档位和可读源码。适合学习程序化场景、着色器和自适应画质。

### 环境与限制

运行需要支持 WebGPU 的浏览器与显卡。触屏支持仍属实验功能。修改后重新构建需要 Node.js 18+；性能数据为上游自述。

### 入门与收录判断

从[官方 README](https://github.com/Noniv/abyssal-garden/blob/main/README.md)查阅安装和使用步骤。提供完整离线示例和拆分源码，比单纯效果视频更适合学习与修改。

本轮为文档复核，未安装、运行或测试上游项目。2026-11-14 修复绘制距离外水域发黑，修改渲染流程和着色器。详见[维护记录](https://github.com/Noniv/abyssal-garden/commit/c628d18c708ce12849085f3e4ec4a0136e5efd5b)。

### 文章来源

发现于“逛逛GitHub”在 2026-11-16 发布的[《8 个开源工具速览》](https://www.woshipm.com/ai/6494405.html)。已读取作者署名正文，功能和限制另按当前上游复核。

## English

### Purpose and features

An interactive underwater scene packaged as one HTML file, using WebGPU graphics and synthesized audio.

Includes keyboard navigation, quality settings and readable source for studying procedural scenes, shaders and adaptive quality.

### Requirements and limits

Requires a WebGPU-capable browser and GPU. Touch support is experimental. Rebuilding modified source needs Node.js 18+; performance figures remain upstream claims.

### Getting started and review

Use the [official README](https://github.com/Noniv/abyssal-garden/blob/main/README.md) for installation and usage. This is a documentation review; the software was not installed or tested. The 2026-11-14 change fixes black water beyond the draw distance in the renderer and shaders. See the [activity evidence](https://github.com/Noniv/abyssal-garden/commit/c628d18c708ce12849085f3e4ec4a0136e5efd5b).

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
    "id": "abyssal-garden",
    "name": "Abyssal Garden",
    "repository": "Noniv/abyssal-garden",
    "repo_node_id": "R_kgDOVr8_yw",
    "category": "media",
    "summary": {
      "zh-CN": "以单个 HTML 展示可交互的海底场景。使用 WebGPU 绘制地形和生物，并实时合成声音。",
      "en": "An interactive underwater scene packaged as one HTML file, using WebGPU graphics and synthesized audio."
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
      "basis": "提供完整离线示例和拆分源码，比单纯效果视频更适合学习与修改。",
      "rationale": "提供完整离线示例和拆分源码，比单纯效果视频更适合学习与修改。",
      "stars_are_advisory": true,
      "reviewed_at": "2026-11-16T14:30:19.931551Z"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "b108a76735ab7cc0eab686fc3e85ca668bdb8866977093846d01bac5b6440453",
      "source_url": "https://github.com/Noniv/abyssal-garden/blob/a596354eff400d458bc2aeb9bdf5e0a9734b2bcf/LICENSE",
      "reviewed_at": "2026-11-16T14:30:19.931551Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "a596354eff400d458bc2aeb9bdf5e0a9734b2bcf"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-14T17:00:25Z",
        "reviewed_at": "2026-11-16T14:30:19.931551Z",
        "url": "https://github.com/Noniv/abyssal-garden/commit/c628d18c708ce12849085f3e4ec4a0136e5efd5b",
        "qualifies": true,
        "reason": {
          "zh-CN": "2026-11-14 修复绘制距离外水域发黑，修改渲染流程和着色器。",
          "en": "The 2026-11-14 change fixes black water beyond the draw distance in the renderer and shaders."
        },
        "reviewed_files": [
          "source/src/main.js",
          "source/src/shaders.js"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/Noniv/abyssal-garden",
        "accessed_at": "2026-11-16T14:27:09.985Z",
        "supports": "Repository identity, Stars and public state."
      },
      {
        "url": "https://github.com/Noniv/abyssal-garden/blob/main/README.md",
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
    "repo_node_id": "R_kgDOVr8_yw",
    "full_name": "Noniv/abyssal-garden",
    "stargazers_count": 1440,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "b108a76735ab7cc0eab686fc3e85ca668bdb8866977093846d01bac5b6440453",
    "last_success_at": "2026-11-16T14:27:09.985Z"
  }
}
```

</details>
