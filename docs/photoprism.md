# PhotoPrism

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[photoprism/photoprism](https://github.com/photoprism/photoprism)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 40456 |
| 评估时间 / Evaluated at | 2026-11-17T14:45:29.296349Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:39:45.809Z |

## 中文

PhotoPrism 是自托管的照片与视频管理工具，可自动生成标签、识别人脸，并按内容及元数据筛选素材。

AI 标签和人脸识别帮助整理素材；启用 MCP 后，兼容的 AI 助手还可按授权搜索图库、相册、人物和标签。

### 主要功能

- 按图片内容和位置生成标签，并识别和组织人物照片。
- 可组合标签、地点、分辨率和颜色这些搜索条件。可提取并合并 EXIF 与 XMP 元数据。
- 在浏览器中管理 RAW 照片、视频和 Live Photos，支持通过 WebDAV 访问文件。
- 提供只读 MCP 工具，让 AI 助手检索素材、读取详情、浏览相册并查询 PhotoPrism 的配置和搜索说明。

### 环境要求

- 官方推荐 Docker Compose 和 64 位系统，支持 AMD、Intel 和 ARM 处理器。最低为 2 核 CPU、3 GB 物理内存，并需至少 4 GB 交换空间。
- 数据库和缓存宜放在本地 SSD；浏览器需保持更新。首次索引大量 RAW 或高分辨率全景图时，可能需要更多内存与交换空间。
- 连接 AI 助手需使用包含 MCP 图库工具的版本，并启用实例和账号的 MCP 权限。客户端需支持 Streamable HTTP 与 OAuth；远程助手需能访问服务的 HTTPS 地址。

### 使用限制

- 完整备份至少包含原始照片与视频，以及索引数据库。官方还建议备份 storage 目录；自动数据库备份不能替代原文件备份。
- MCP 工具不能修改或删除图库。管理员可在所有版本使用 MCP。普通用户和只读用户需 Plus 或 Pro。其他角色的权限应按官方说明核对。
- 启用只读模式会禁用向原文件目录写入的功能，包括上传、删除和 WebDAV。

### 开始使用

1. 核对[系统要求](https://docs.photoprism.app/getting-started/)。按[Compose 指南](https://docs.photoprism.app/getting-started/docker-compose/)选择平台配置。设置原文件、storage 和数据库的持久化目录。
2. 启动服务并登录。按[首次使用指南](https://docs.photoprism.app/user-guide/first-steps/)索引一批样例素材。检查标签、人脸和筛选结果。
3. 按[备份指南](https://docs.photoprism.app/getting-started/advanced/backups/)备份原文件与数据库。如需 AI 助手检索，按[MCP 指南](https://docs.photoprism.app/getting-started/advanced/mcp/)注册客户端并批准访问。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:39:45.809Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/photoprism/photoprism/commit/285a4874ef2a3d464916346523a1703db432c1e7)。Downloads: Skip files flagged as missing in the web UI #5830

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/photoprism/photoprism/blob/develop/README.md)
- [系统要求 / System requirements](https://docs.photoprism.app/getting-started/)
- [Compose 部署 / Compose installation](https://docs.photoprism.app/getting-started/docker-compose/)
- [首次使用 / First steps](https://docs.photoprism.app/user-guide/first-steps/)
- [备份指南 / Backup guide](https://docs.photoprism.app/getting-started/advanced/backups/)
- [连接 AI 助手 / Connecting AI assistants](https://docs.photoprism.app/getting-started/advanced/mcp/)

## English

PhotoPrism is a self-hosted photo and video manager that generates labels, recognizes faces, and filters media by content and metadata.

AI labels and face recognition help organize media. With MCP enabled, compatible AI assistants can also search the library, albums, people, and labels within their authorized access.

### Features

- Generate labels from image content and location, and recognize and organize pictures of people.
- Combine filters such as labels, locations, resolution, and color, and extract and merge metadata from EXIF and XMP.
- Manage RAW photos, videos, and Live Photos in a browser, with file access through WebDAV.
- Provide read-only MCP tools for AI assistants to search media, read details, browse albums, and look up PhotoPrism configuration and search documentation.

### Requirements

- The recommended setup uses Docker Compose and a 64-bit system, with AMD, Intel, and ARM processors supported. The minimum is 2 CPU cores and 3 GB physical RAM, plus at least 4 GB swap.
- Use local SSD storage for the database and cache, and keep the browser current. Initial indexing of large RAW collections or high-resolution panoramas may need more RAM and swap.
- AI assistants need a version with MCP library tools and MCP enabled for both the instance and account. Clients must support Streamable HTTP and OAuth; remote assistants need a reachable HTTPS address.

### Limitations

- A complete backup needs at least the original photos and videos plus the index database. The project also recommends backing up the storage directory; automatic database backups do not replace copies of the original files.
- MCP tools cannot edit or delete library items. Admins can use MCP in every edition; users and viewers need Plus or Pro. Check the documented permissions for other roles.
- Read-only mode disables features that write to the originals directory, including uploads, deletion, and WebDAV.

### Getting started

1. Check the [system requirements](https://docs.photoprism.app/getting-started/), choose a platform configuration from the [Compose guide](https://docs.photoprism.app/getting-started/docker-compose/), and configure persistent originals, storage, and database directories.
2. Start the services and sign in, then follow the [first-steps guide](https://docs.photoprism.app/user-guide/first-steps/) to index a small sample and check labels, faces, and filters.
3. Back up originals and the database using the [backup guide](https://docs.photoprism.app/getting-started/advanced/backups/). To let an AI assistant search the library, register a client and approve access as described in the [MCP guide](https://docs.photoprism.app/getting-started/advanced/mcp/).

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:39:45.809Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/photoprism/photoprism/commit/285a4874ef2a3d464916346523a1703db432c1e7).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/photoprism/photoprism/blob/develop/README.md)
- [系统要求 / System requirements](https://docs.photoprism.app/getting-started/)
- [Compose 部署 / Compose installation](https://docs.photoprism.app/getting-started/docker-compose/)
- [首次使用 / First steps](https://docs.photoprism.app/user-guide/first-steps/)
- [备份指南 / Backup guide](https://docs.photoprism.app/getting-started/advanced/backups/)
- [连接 AI 助手 / Connecting AI assistants](https://docs.photoprism.app/getting-started/advanced/mcp/)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:45:29.296349Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "photoprism",
    "name": "PhotoPrism",
    "repository": "photoprism/photoprism",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkxMTkxNjA1NTM=",
    "category": "media",
    "summary": {
      "zh-CN": "PhotoPrism 是自托管的照片与视频管理工具，可自动生成标签、识别人脸，并按内容及元数据筛选素材。",
      "en": "PhotoPrism is a self-hosted photo and video manager that generates labels, recognizes faces, and filters media by content and metadata."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:45:29.296349Z",
        "en": "2026-11-17T14:45:29.296349Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "AI 标签和人脸识别帮助整理素材；启用 MCP 后，兼容的 AI 助手还可按授权搜索图库、相册、人物和标签。",
        "en": "AI labels and face recognition help organize media. With MCP enabled, compatible AI assistants can also search the library, albums, people, and labels within their authorized access."
      },
      "source_url": "https://github.com/photoprism/photoprism/blob/develop/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/photoprism/photoprism/commit/285a4874ef2a3d464916346523a1703db432c1e7",
        "occurred_at": "2026-11-17T14:26:28Z",
        "reviewed_at": "2026-11-17T14:45:29.296349Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "Downloads: Skip files flagged as missing in the web UI #5830 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/photoprism/photoprism/blob/develop/README.md"
      },
      {
        "title": "系统要求 / System requirements",
        "url": "https://docs.photoprism.app/getting-started/"
      },
      {
        "title": "Compose 部署 / Compose installation",
        "url": "https://docs.photoprism.app/getting-started/docker-compose/"
      },
      {
        "title": "首次使用 / First steps",
        "url": "https://docs.photoprism.app/user-guide/first-steps/"
      },
      {
        "title": "备份指南 / Backup guide",
        "url": "https://docs.photoprism.app/getting-started/advanced/backups/"
      },
      {
        "title": "连接 AI 助手 / Connecting AI assistants",
        "url": "https://docs.photoprism.app/getting-started/advanced/mcp/"
      }
    ]
  },
  "snapshot": {
    "full_name": "photoprism/photoprism",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkxMTkxNjA1NTM=",
    "stargazers_count": 40456,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:39:45.809Z",
    "source_url": "https://api.github.com/repos/photoprism/photoprism"
  }
}
```

</details>
