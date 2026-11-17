# HolyArrs

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[HolyArrs/HolyArrs](https://github.com/HolyArrs/HolyArrs)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 1325 |
| 许可证 / License | AGPL-3.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:30:19.931551Z |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:27:10.582Z |

## 中文

### 用途与功能

在自托管网页中管理媒体请求、筛选规则、字幕和文件入库。可连接现有下载器与媒体服务器。

适合家庭媒体库管理。支持配置来源、批准请求，以及从其他媒体管理工具导入设置。

### 环境与限制

通常通过 Docker 部署，支持 amd64、arm64、armv7。仍需独立下载器和有权使用的媒体来源。默认媒体元数据来自维护者服务器；自托管不等于所有数据离线。音乐浏览等功能尚未完整。

### 入门与收录判断

从[官方 README](https://github.com/HolyArrs/HolyArrs/blob/main/README.md)查阅安装和使用步骤。把请求、筛选与入库管理集中在一个界面，文档列出依赖和迁移边界。

本轮为文档复核，未安装、运行或测试上游项目。正式 1.1.4 修复媒体名称匹配、登录校验及日期显示。详见[维护记录](https://github.com/HolyArrs/HolyArrs/releases/tag/1.1.4)。

### 文章来源

发现于“逛逛GitHub”在 2026-11-16 发布的[《8 个开源工具速览》](https://www.woshipm.com/ai/6494405.html)。已读取作者署名正文，功能和限制另按当前上游复核。

## English

### Purpose and features

A self-hosted web application for media requests, selection rules, subtitles and library imports, connecting existing downloaders and media servers.

Supports source configuration, request approvals and importing settings from other media-management tools.

### Requirements and limits

Usually deployed with Docker on amd64, arm64 or armv7. Requires a separate downloader and authorized media sources. Metadata defaults to the maintainer's server, and some music-browsing features are unfinished.

### Getting started and review

Use the [official README](https://github.com/HolyArrs/HolyArrs/blob/main/README.md) for installation and usage. This is a documentation review; the software was not installed or tested. Stable 1.1.4 fixes media-name matching, sign-in checks and date display. See the [activity evidence](https://github.com/HolyArrs/HolyArrs/releases/tag/1.1.4).

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
    "id": "holyarrs",
    "name": "HolyArrs",
    "repository": "HolyArrs/HolyArrs",
    "repo_node_id": "R_kgDOVovjIg",
    "category": "media",
    "summary": {
      "zh-CN": "在自托管网页中管理媒体请求、筛选规则、字幕和文件入库。可连接现有下载器与媒体服务器。",
      "en": "A self-hosted web application for media requests, selection rules, subtitles and library imports, connecting existing downloaders and media servers."
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
      "basis": "把请求、筛选与入库管理集中在一个界面，文档列出依赖和迁移边界。",
      "rationale": "把请求、筛选与入库管理集中在一个界面，文档列出依赖和迁移边界。",
      "stars_are_advisory": true,
      "reviewed_at": "2026-11-16T14:30:19.931551Z"
    },
    "license_review": {
      "spdx": "AGPL-3.0",
      "osi_approved": true,
      "license_sha256": "0d96a4ff68ad6d4b6f1f30f713b18d5184912ba8dd389f86aa7710db079abcb0",
      "source_url": "https://github.com/HolyArrs/HolyArrs/blob/25f120e60842ce8b3ff58dcae4756e72b65768f7/LICENSE",
      "reviewed_at": "2026-11-16T14:30:19.931551Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "25f120e60842ce8b3ff58dcae4756e72b65768f7"
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-11-14T01:51:41Z",
        "reviewed_at": "2026-11-16T14:30:19.931551Z",
        "url": "https://github.com/HolyArrs/HolyArrs/releases/tag/1.1.4",
        "qualifies": true,
        "reason": {
          "zh-CN": "正式 1.1.4 修复媒体名称匹配、登录校验及日期显示。",
          "en": "Stable 1.1.4 fixes media-name matching, sign-in checks and date display."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/HolyArrs/HolyArrs",
        "accessed_at": "2026-11-16T14:27:10.582Z",
        "supports": "Repository identity, Stars and public state."
      },
      {
        "url": "https://github.com/HolyArrs/HolyArrs/blob/main/README.md",
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
    "repo_node_id": "R_kgDOVovjIg",
    "full_name": "HolyArrs/HolyArrs",
    "stargazers_count": 1325,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "AGPL-3.0",
    "license_sha256": "0d96a4ff68ad6d4b6f1f30f713b18d5184912ba8dd389f86aa7710db079abcb0",
    "last_success_at": "2026-11-16T14:27:10.582Z"
  }
}
```

</details>
