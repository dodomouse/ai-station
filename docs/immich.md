# Immich

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[immich-app/immich](https://github.com/immich-app/immich)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 119440 |
| 评估时间 / Evaluated at | 2026-11-17T14:45:29.295891Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:39:45.776Z |

## 中文

Immich 是自托管的照片与视频库，提供手机自动上传、相册管理、人脸识别和 CLIP 检索。

可用 AI 按画面内容和人脸检索已有素材，减少为 AI 辅助编辑、整理或内容制作寻找原文件的时间。

### 主要功能

- 通过手机和浏览器上传、浏览和下载照片及视频；手机端支持选择相册并在后台上传。
- 结合元数据、对象、CLIP 和人脸检索素材，并对识别出的人脸分组。
- 管理普通相册、共享相册和多用户图库，支持公开分享及伴侣共享。
- 支持 RAW、LivePhoto 和 MotionPhoto，并展示 EXIF 信息及拍摄位置。

### 环境要求

- 官方推荐 64 位 Linux 和 Docker Compose 插件。最低为 2 核 CPU、6 GB 内存，推荐 4 核、8 GB；支持 amd64 和 arm64。
- 自 v3 起，amd64 机器学习容器要求 x86-64-v2 或更新指令集；只有 4 GB 内存时须关闭机器学习功能。
- PostgreSQL 数据目录需支持 Unix 文件权限，不能放在网络共享上；官方建议使用本地 SSD。为缩略图和视频转码预留额外存储空间。

### 使用限制

- 自动数据库备份只含元数据，不含照片和视频。还须备份上传目录，并按官方建议保留 3-2-1 备份。
- 不要在文件系统中直接移动、修改或删除 Immich 管理的素材。这会使数据库记录与文件不一致。请通过应用管理素材。
- Windows 和 macOS 可借助 Docker Desktop 部署，但官方不推荐这些服务端环境，相关部署与排障支持有限。

### 开始使用

1. 按[环境要求](https://docs.immich.app/install/requirements/)准备主机。从[Compose 部署指南](https://docs.immich.app/install/docker-compose/)获取官方发行配置。设置媒体和数据库目录。
2. 按部署指南启动服务。按[安装后步骤](https://docs.immich.app/install/post-install/)注册管理员并连接手机端。上传样例素材。
3. 检查素材浏览和搜索结果。按[备份与恢复指南](https://docs.immich.app/administration/backup-and-restore/)配置数据库与媒体文件备份。完成后再导入主要图库。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:39:45.776Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/immich-app/immich/commit/1f6d98d92133ee81b68eb72b5d939cc042528a7d)。chore(npm): update typescript-projects (#33388)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/immich-app/immich/blob/main/README.md)
- [环境要求 / Requirements](https://docs.immich.app/install/requirements/)
- [Compose 部署 / Compose installation](https://docs.immich.app/install/docker-compose/)
- [安装后步骤 / Post-installation steps](https://docs.immich.app/install/post-install/)
- [备份与恢复 / Backup and restore](https://docs.immich.app/administration/backup-and-restore/)

## English

Immich is a self-hosted photo and video library with automatic mobile uploads, albums, face recognition, and CLIP search.

Its AI search helps find existing media by visual content and faces, reducing the work of locating source files for AI-assisted editing, organization, or content production.

### Features

- Upload, browse, and download photos and videos from mobile apps and a browser; mobile apps support selected albums and background uploads.
- Search media using metadata, objects, CLIP, and faces, and group recognized faces.
- Manage albums, shared albums, and multiple users, with public links and partner sharing.
- Support RAW, LivePhoto, and MotionPhoto files, with EXIF details and capture locations.

### Requirements

- The recommended setup is 64-bit Linux with the Docker Compose plugin. The minimum is 2 CPU cores and 6 GB RAM; 4 cores and 8 GB are recommended. Supported platforms are amd64 and arm64.
- From v3, the amd64 machine-learning container requires x86-64-v2 or later instructions. Systems with only 4 GB RAM must disable machine learning.
- The PostgreSQL data directory needs Unix filesystem permissions and cannot reside on a network share; local SSD storage is recommended. Allow extra space for thumbnails and transcoded videos.

### Limitations

- Automatic database backups contain metadata, not photos or videos. Back up the upload directory as well and follow the recommended 3-2-1 backup strategy.
- Do not move, change, or delete managed assets directly in the filesystem: database records can become inconsistent with the files. Manage assets through the application.
- Windows and macOS can use Docker Desktop, but the project discourages these server environments and offers limited setup and troubleshooting support for them.

### Getting started

1. Prepare a host using the [requirements](https://docs.immich.app/install/requirements/), then obtain the official release configuration from the [Compose guide](https://docs.immich.app/install/docker-compose/) and set the media and database directories.
2. Start the services as documented, then follow the [post-installation steps](https://docs.immich.app/install/post-install/) to register an administrator, connect a mobile app, and upload a small sample.
3. Check browsing and search results, then configure database and media-file backups using the [backup and restore guide](https://docs.immich.app/administration/backup-and-restore/) before importing the main library.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:39:45.776Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/immich-app/immich/commit/1f6d98d92133ee81b68eb72b5d939cc042528a7d).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/immich-app/immich/blob/main/README.md)
- [环境要求 / Requirements](https://docs.immich.app/install/requirements/)
- [Compose 部署 / Compose installation](https://docs.immich.app/install/docker-compose/)
- [安装后步骤 / Post-installation steps](https://docs.immich.app/install/post-install/)
- [备份与恢复 / Backup and restore](https://docs.immich.app/administration/backup-and-restore/)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:45:29.295891Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "immich",
    "name": "Immich",
    "repository": "immich-app/immich",
    "repo_node_id": "R_kgDOGyI-8A",
    "category": "media",
    "summary": {
      "zh-CN": "Immich 是自托管的照片与视频库，提供手机自动上传、相册管理、人脸识别和 CLIP 检索。",
      "en": "Immich is a self-hosted photo and video library with automatic mobile uploads, albums, face recognition, and CLIP search."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:45:29.295891Z",
        "en": "2026-11-17T14:45:29.295891Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "可用 AI 按画面内容和人脸检索已有素材，减少为 AI 辅助编辑、整理或内容制作寻找原文件的时间。",
        "en": "Its AI search helps find existing media by visual content and faces, reducing the work of locating source files for AI-assisted editing, organization, or content production."
      },
      "source_url": "https://github.com/immich-app/immich/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/immich-app/immich/commit/1f6d98d92133ee81b68eb72b5d939cc042528a7d",
        "occurred_at": "2026-11-17T14:31:03Z",
        "reviewed_at": "2026-11-17T14:45:29.295891Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "chore(npm): update typescript-projects (#33388) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/immich-app/immich/blob/main/README.md"
      },
      {
        "title": "环境要求 / Requirements",
        "url": "https://docs.immich.app/install/requirements/"
      },
      {
        "title": "Compose 部署 / Compose installation",
        "url": "https://docs.immich.app/install/docker-compose/"
      },
      {
        "title": "安装后步骤 / Post-installation steps",
        "url": "https://docs.immich.app/install/post-install/"
      },
      {
        "title": "备份与恢复 / Backup and restore",
        "url": "https://docs.immich.app/administration/backup-and-restore/"
      }
    ]
  },
  "snapshot": {
    "full_name": "immich-app/immich",
    "repo_node_id": "R_kgDOGyI-8A",
    "stargazers_count": 119440,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:39:45.776Z",
    "source_url": "https://api.github.com/repos/immich-app/immich"
  }
}
```

</details>
