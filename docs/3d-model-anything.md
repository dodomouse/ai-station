# 3D Model Anything

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[wesbos/3d-model-anything](https://github.com/wesbos/3d-model-anything)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 3031 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:19:06.276Z |

## 中文

把房间扫描资料转成可编辑 Three.js 场景的工具与智能体工作流程。

### 主要功能

- 从扫描和照片组织房间几何与材质。
- 提供浏览、行走和交互式修改场景的页面。

### 环境与限制

- 源码需要 Node.js 22.12+，原始采集流程需要带 LiDAR 的 iPhone 和相应构建环境。
- MIT 只覆盖代码与技能，演示数据及图片有独立使用限制。

### 开始使用

从[官方说明](https://github.com/wesbos/3d-model-anything/blob/main/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/wesbos/3d-model-anything/releases)可用于确认版本。

### 收录复核

把房间扫描资料转成可编辑 Three.js 场景的工具与智能体工作流程。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。

有效维护证据：[db785be4ca](https://github.com/wesbos/3d-model-anything/commit/db785be4cad4573221f7c282e7f92655b495a468)，2026-10-21T19:44:02Z。在异步房间初始化前绑定导航事件，修复页面跳转入口。

文章来源：[逛逛GitHub署名文章](https://www.woshipm.com/ai/6486928.html)，平台日期 2026-10-30。已通过公开正文核对仓库链接与作者归属；微信正文未直接读取。

本次为文档与实现证据复核，未安装或运行上游项目。

## English

Tools and agent workflows for turning room scans into editable Three.js scenes.

### Features

- Organizes room geometry and materials from scans and photos.
- Provides scene viewers, walkthroughs and interactive editing workflows.

### Requirements and limits

- Source setup needs Node.js 22.12+
- original capture needs a LiDAR iPhone and its build environment.
- MIT covers code and skills only
- demo data and images have separate restrictions.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/wesbos/3d-model-anything/blob/main/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/wesbos/3d-model-anything/releases) for versions.

### Review and provenance

Tools and agent workflows for turning room scans into editable Three.js scenes. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.

Activity: [db785be4ca](https://github.com/wesbos/3d-model-anything/commit/db785be4cad4573221f7c282e7f92655b495a468), 2026-10-21T19:44:02Z. Binds navigation before asynchronous room initialization so the navigation entry works.

Discovery: [an author-attributed 逛逛GitHub article](https://www.woshipm.com/ai/6486928.html), dated 2026-10-30 on the public platform. Repository links and attribution were checked in its public body; the WeChat body was not read directly.

This review covers documentation and implementation evidence. The upstream project was not installed or run.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:58:29.135174Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "3d-model-anything",
    "name": "3D Model Anything",
    "repository": "wesbos/3d-model-anything",
    "repo_node_id": "R_kgDOVSqAyw",
    "category": "media",
    "summary": {
      "zh-CN": "把房间扫描资料转成可编辑 Three.js 场景的工具与智能体工作流程。",
      "en": "Tools and agent workflows for turning room scans into editable Three.js scenes."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:58:29.135174Z",
        "en": "2026-11-16T14:58:29.135174Z"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "把房间扫描资料转成可编辑 Three.js 场景的工具与智能体工作流程。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。",
      "en": "Tools and agent workflows for turning room scans into editable Three.js scenes. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "7b41d61a4569d103d9968cbb246c9e489ae14797b171d26ef47825a040c958b4",
      "source_url": "https://github.com/wesbos/3d-model-anything/blob/31b2dc9da3fb541e501f2f0936e55b32afb70ee8/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "MIT covers source code and skills; demo data and images have separate restricted terms and are excluded from this code-license finding.",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "31b2dc9da3fb541e501f2f0936e55b32afb70ee8"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-10-21T19:44:02Z",
        "reviewed_at": "2026-11-16T14:58:29.135174Z",
        "url": "https://github.com/wesbos/3d-model-anything/commit/db785be4cad4573221f7c282e7f92655b495a468",
        "qualifies": true,
        "reason": {
          "zh-CN": "在异步房间初始化前绑定导航事件，修复页面跳转入口。",
          "en": "Binds navigation before asynchronous room initialization so the navigation entry works."
        },
        "reviewed_files": [
          "apps/room-viewer/src/main.ts"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/wesbos/3d-model-anything",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/wesbos/3d-model-anything/blob/main/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/wesbos/3d-model-anything/blob/31b2dc9da3fb541e501f2f0936e55b32afb70ee8/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/wesbos/3d-model-anything/commit/db785be4cad4573221f7c282e7f92655b495a468",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://www.woshipm.com/ai/6486928.html",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      }
    ],
    "article_source": {
      "article_id": "2247538171_1",
      "title": "这 6 个 GitHub 项目是刚开源，但是 Star 攀升很快的几个。",
      "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538171&idx=1&sn=cd8f63d5332497b649d72590298e1a05",
      "published_date": "2026-10-30",
      "account": "逛逛GitHub",
      "content_review_url": "https://www.woshipm.com/ai/6486928.html",
      "content_review_kind": "author-attributed public article",
      "wechat_direct_body_read": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVSqAyw",
    "full_name": "wesbos/3d-model-anything",
    "stargazers_count": 3031,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "NOASSERTION",
    "license_sha256": "7b41d61a4569d103d9968cbb246c9e489ae14797b171d26ef47825a040c958b4",
    "last_success_at": "2026-11-16T14:19:06.276Z"
  }
}
```

</details>
