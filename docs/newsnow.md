# NewsNow

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[newsnext/newsnow](https://github.com/newsnext/newsnow)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 22489 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-18T02:23:30.692680Z |
| 快照时间 / Snapshot recorded at | 2026-11-18T02:20:28.432933Z |

## 中文

聚合多站热点与实时新闻，支持 GitHub 登录同步，并通过官方 MCP 为 AI 客户端提供新闻标题和原文链接。

适合集中浏览新闻、为 AI 简报准备线索和筛选研究主题。主要用途是新闻阅读与信息整理，因此归入文档与效率。

### 主要功能

- 聚合科技、国内、国际、财经等来源的热点和最新条目，提供标题与原站链接。
- 支持 GitHub OAuth 登录和偏好同步；默认缓存 30 分钟，并按新闻源设置抓取间隔。
- 官方独立包 `newsnow-mcp-server` 通过 stdio 向 AI 客户端提供 `get_hottest_latest_news` 工具，以来源 ID 和数量取回新闻。`BASE_URL` 可指向官方站点或自建服务。
- 使用 React、Vite 与 Nitro 构建前后端；可配置 Cloudflare Pages/D1、Docker 或其他兼容部署。

### 环境与限制

- MCP 0.0.12 的实现返回编号标题和链接，默认 10 条；主站单个来源接口最多取 30 条。它不在该工具中返回文章全文、缓存时间，也不执行模型总结。深入研究需要另行读取原文并核对日期。
- 新闻源可能因站点改版、网络限制或接口变化失效。接口抓取失败时可回退到旧缓存，结果不保证即时更新。
- README 标注 Node.js ≥20，但锁文件中的 Vite 7.3.6 要求 `^20.19.0 || >=22.12.0`，源码 Dockerfile 仍固定为 Node 20.12.2。自行构建前需调整运行环境并核对其他依赖的要求；本次未验证构建成功。Compose 默认拉取预构建镜像，不能据源码 Dockerfile 判断该镜像的实际状态。
- 登录、同步和缓存依赖相应 OAuth、密钥和数据库配置。Vercel 部署需自行配置数据库。
- README 宣布筹备 NewsNext，当前版本不再接受贡献；仓库仍公开且未归档，并有窗口内修复记录。后续功能方向存在变化可能。
- 根 MIT 许可覆盖代码；新闻内容、第三方依赖、品牌素材及外部服务另有条款。官方 MCP 是单独发布的软件包，本次读取了其 MIT 许可和发布代码。

### 开始使用

1. 打开[官方演示](https://newsnow.busiyi.world)，检查需要的新闻源是否可用。
2. 需要 AI 接入时，在支持 stdio MCP 的客户端配置命令 `npx`、参数 `-y newsnow-mcp-server@0.0.12`，并设置环境变量 `BASE_URL=https://newsnow.busiyi.world`。自建服务时替换该地址。
3. 需要自行部署时，按官方 README 配置 Compose 或 Cloudflare Pages；源码构建先处理上述 Node 版本不匹配，再配置 OAuth、数据库与缓存。

### 收录与来源

按仓库名、旧地址 `ourongxing/newsnow` 和稳定 ID 去重，未发现已有词条。官方 MCP 提供明确的 AI 任务入口；快照为 22,489 Star，满足总量条件。

实质维护：[2026-10-12 更新 AIHOT 与靠谱新闻的 RSS 抓取](https://github.com/newsnext/newsnow/commit/30151c169ca7fc9f0392bccf91d8083c758b7802)，在本次复核前三个日历月内。已阅读具体补丁。

本次读取了固定提交的文档、接口实现、依赖及许可，并静态检查 MCP 0.0.12 发布包，未安装或运行上游服务、容器或 MCP 客户端。目录测试只验证本站内容一致性。

## English

Aggregates trending and recent news, supports GitHub sign-in and synchronization, and supplies news titles and original links to AI clients through its official MCP adapter.

Useful for browsing news, preparing leads for AI briefings and selecting research topics. Its primary purpose is news reading and information organization.

### Features

- Aggregates trending and recent items across technology, domestic, international and financial sources, with titles and original links.
- Supports GitHub OAuth sign-in and preference synchronization, with a 30-minute default cache and per-source fetch intervals.
- The separate official `newsnow-mcp-server` package exposes `get_hottest_latest_news` over stdio. It accepts a source ID and count; `BASE_URL` selects the public or self-hosted service.
- Built with React, Vite and Nitro, with Cloudflare Pages/D1, Docker and other compatible deployment options.

### Requirements and limitations

- MCP 0.0.12 returns numbered titles and links, defaulting to ten items. The main service limits each source response to 30 items. This tool does not return article bodies or cache timestamps, or run model summarization. Follow original links and verify dates for deeper research.
- Source changes, network restrictions and API changes can break collection. Failed requests may fall back to older cached results.
- README states Node.js ≥20, but locked Vite 7.3.6 requires `^20.19.0 || >=22.12.0`, while the source Dockerfile pins Node 20.12.2. Align the build environment and check other dependency requirements before building. Compose pulls a prebuilt image; its runtime status cannot be inferred from this Dockerfile alone. Builds were not tested.
- Login, synchronization and caching need the relevant OAuth credentials, secrets and database configuration. Vercel deployments require separate database setup.
- README announces NewsNext and says this version no longer accepts contributions. The repository remains public and unarchived, with a recent source fix; future development direction may change.
- The root MIT license covers code. News content, dependencies, brand assets and external services retain separate terms. The official MCP adapter is a separate package; its published code and MIT license were inspected.

### Getting started

1. Visit the [official demo](https://newsnow.busiyi.world) and check the sources needed for your task.
2. In a client supporting stdio MCP, configure command `npx`, arguments `-y newsnow-mcp-server@0.0.12` and environment variable `BASE_URL=https://newsnow.busiyi.world`. Substitute your domain for a self-hosted service.
3. Follow the official Compose or Cloudflare Pages instructions for deployment. For source builds, resolve the Node version mismatch before configuring OAuth, the database and caching.

### Review and sources

No duplicate was found by canonical repository, former address `ourongxing/newsnow` or stable ID. The official MCP integration establishes AI task relevance; the snapshot of 22,489 Stars meets the total-Star criterion.

Substantive maintenance: [2026-10-12 RSS source fixes for AIHOT and Kaopu](https://github.com/newsnext/newsnow/commit/30151c169ca7fc9f0392bccf91d8083c758b7802), within the preceding three calendar months. The actual patch was reviewed.

This review inspected pinned documentation, endpoint code, dependencies and licensing, plus the published MCP 0.0.12 package. The upstream service, container and MCP client were not installed or run. Catalog tests validate this catalog's consistency only.

### 证据链接 / Evidence links

- [官方中文说明 / Chinese README](https://github.com/newsnext/newsnow/blob/5da836c49c327f2c352216c5cbb4dea1abd9fcd3/README.zh-CN.md)
- [官方英文说明 / English README](https://github.com/newsnext/newsnow/blob/5da836c49c327f2c352216c5cbb4dea1abd9fcd3/README.md)
- [新闻接口 / News endpoint](https://github.com/newsnext/newsnow/blob/5da836c49c327f2c352216c5cbb4dea1abd9fcd3/server/api/s/index.ts)
- [依赖锁文件 / Dependency lockfile](https://github.com/newsnext/newsnow/blob/5da836c49c327f2c352216c5cbb4dea1abd9fcd3/pnpm-lock.yaml)
- [源码容器配置 / Source Dockerfile](https://github.com/newsnext/newsnow/blob/5da836c49c327f2c352216c5cbb4dea1abd9fcd3/Dockerfile)
- [Compose 配置 / Compose configuration](https://github.com/newsnext/newsnow/blob/5da836c49c327f2c352216c5cbb4dea1abd9fcd3/docker-compose.yml)
- [MIT 许可 / MIT license](https://github.com/newsnext/newsnow/blob/5da836c49c327f2c352216c5cbb4dea1abd9fcd3/LICENSE)
- [MCP 0.0.12 包元数据 / MCP package metadata](https://registry.npmjs.org/newsnow-mcp-server/0.0.12)
- [MCP 0.0.12 发布包 / Published MCP package](https://registry.npmjs.org/newsnow-mcp-server/-/newsnow-mcp-server-0.0.12.tgz)

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-18T02:23:30.692680Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "newsnow",
    "name": "NewsNow",
    "repository": "newsnext/newsnow",
    "repo_node_id": "R_kgDOM13h9A",
    "category": "productivity",
    "summary": {
      "zh-CN": "聚合多站热点与实时新闻，支持 GitHub 登录同步，并通过官方 MCP 为 AI 客户端提供新闻标题和原文链接。",
      "en": "Aggregates trending and recent news, supports GitHub sign-in and synchronization, and supplies news titles and original links to AI clients through its official MCP adapter."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-18T02:23:30.692680Z",
        "en": "2026-11-18T02:23:30.692680Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "官方 MCP 按来源提供热点或最新新闻的标题与链接，可作为 AI 新闻简报、选题和后续原文研究的输入。",
        "en": "The official MCP tool returns trending or recent news titles and links by source, providing inputs for AI briefings, topic selection and follow-up research."
      },
      "source_url": "https://github.com/newsnext/newsnow/blob/5da836c49c327f2c352216c5cbb4dea1abd9fcd3/README.md"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/newsnext/newsnow/blob/5da836c49c327f2c352216c5cbb4dea1abd9fcd3/LICENSE",
      "source_commit": "5da836c49c327f2c352216c5cbb4dea1abd9fcd3",
      "license_sha256": "02433847d889ccfc3d80d7d9644a52c4ededb6361ab586b8bc42ce283716c55b",
      "reviewed_at": "2026-11-18T02:23:30.692680Z",
      "evidence_status": "hash_matched",
      "scope_note": {
        "zh-CN": "根 MIT 许可覆盖仓库代码；第三方依赖、新闻内容、品牌素材及外部服务分别适用其自身条款。未发现需随本项目部署的模型权重。",
        "en": "The root MIT license covers repository code. Dependencies, news content, brand assets and external services retain their own terms. No model weights required for this project were identified."
      }
    },
    "activity_evidence": [
      {
        "type": "commit",
        "qualifies": true,
        "url": "https://github.com/newsnext/newsnow/commit/30151c169ca7fc9f0392bccf91d8083c758b7802",
        "occurred_at": "2026-10-12T04:03:23Z",
        "reviewed_at": "2026-11-18T02:23:30.692680Z",
        "reason": {
          "zh-CN": "更新 AIHOT 的 RSS 地址，将靠谱新闻抓取切换为 RSS，并同步来源主页配置。",
          "en": "Updates the AIHOT RSS endpoint, switches Kaopu collection to RSS and synchronizes the source homepage configuration."
        },
        "reviewed_files": [
          "server/sources/aihot.ts",
          "server/sources/kaopu.ts",
          "shared/pre-sources.ts",
          "shared/sources.json"
        ]
      }
    ],
    "integration_review": {
      "package": "newsnow-mcp-server",
      "version": "0.0.12",
      "source_url": "https://registry.npmjs.org/newsnow-mcp-server/0.0.12",
      "integrity": "sha512-b8XZ4tqM4buIO3Ax5ITUrn6Lg4hRaY40pjs8cHI05h96dQyRlqWfic4BCuCoOeblsACSoFikp/GtvLJCbGiRzw==",
      "reviewed_files": [
        "README.md",
        "LICENSE",
        "dist/index.js"
      ],
      "verification_level": "source"
    },
    "sources": [
      {
        "url": "https://github.com/newsnext/newsnow/blob/5da836c49c327f2c352216c5cbb4dea1abd9fcd3/README.zh-CN.md",
        "accessed_at": "2026-11-18T02:23:30.692680Z"
      },
      {
        "url": "https://github.com/newsnext/newsnow/blob/5da836c49c327f2c352216c5cbb4dea1abd9fcd3/README.md",
        "accessed_at": "2026-11-18T02:23:30.692680Z"
      },
      {
        "url": "https://github.com/newsnext/newsnow/blob/5da836c49c327f2c352216c5cbb4dea1abd9fcd3/package.json",
        "accessed_at": "2026-11-18T02:23:30.692680Z"
      },
      {
        "url": "https://github.com/newsnext/newsnow/blob/5da836c49c327f2c352216c5cbb4dea1abd9fcd3/pnpm-lock.yaml",
        "accessed_at": "2026-11-18T02:23:30.692680Z"
      },
      {
        "url": "https://github.com/newsnext/newsnow/blob/5da836c49c327f2c352216c5cbb4dea1abd9fcd3/Dockerfile",
        "accessed_at": "2026-11-18T02:23:30.692680Z"
      },
      {
        "url": "https://github.com/newsnext/newsnow/blob/5da836c49c327f2c352216c5cbb4dea1abd9fcd3/docker-compose.yml",
        "accessed_at": "2026-11-18T02:23:30.692680Z"
      },
      {
        "url": "https://github.com/newsnext/newsnow/blob/5da836c49c327f2c352216c5cbb4dea1abd9fcd3/server/api/s/index.ts",
        "accessed_at": "2026-11-18T02:23:30.692680Z"
      },
      {
        "url": "https://github.com/newsnext/newsnow/blob/5da836c49c327f2c352216c5cbb4dea1abd9fcd3/shared/types.ts",
        "accessed_at": "2026-11-18T02:23:30.692680Z"
      },
      {
        "url": "https://github.com/newsnext/newsnow/blob/5da836c49c327f2c352216c5cbb4dea1abd9fcd3/shared/consts.ts",
        "accessed_at": "2026-11-18T02:23:30.692680Z"
      },
      {
        "url": "https://github.com/newsnext/newsnow/blob/5da836c49c327f2c352216c5cbb4dea1abd9fcd3/LICENSE",
        "accessed_at": "2026-11-18T02:23:30.692680Z"
      },
      {
        "url": "https://github.com/newsnext/newsnow",
        "accessed_at": "2026-11-18T02:23:30.692680Z"
      },
      {
        "url": "https://api.github.com/repos/newsnext/newsnow",
        "accessed_at": "2026-11-18T02:23:30.692680Z"
      },
      {
        "url": "https://github.com/newsnext/newsnow/commit/30151c169ca7fc9f0392bccf91d8083c758b7802",
        "accessed_at": "2026-11-18T02:23:30.692680Z"
      },
      {
        "url": "https://registry.npmjs.org/newsnow-mcp-server/0.0.12",
        "accessed_at": "2026-11-18T02:23:30.692680Z"
      },
      {
        "url": "https://registry.npmjs.org/newsnow-mcp-server/-/newsnow-mcp-server-0.0.12.tgz",
        "accessed_at": "2026-11-18T02:23:30.692680Z"
      }
    ],
    "discovery": {
      "kind": "user_submission",
      "submitted_date": "2026-11-18",
      "source_url": "https://github.com/newsnext/newsnow",
      "repository_url": "https://github.com/newsnext/newsnow"
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOM13h9A",
    "full_name": "newsnext/newsnow",
    "stargazers_count": 22489,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "02433847d889ccfc3d80d7d9644a52c4ededb6361ab586b8bc42ce283716c55b",
    "last_success_at": "2026-11-18T02:20:28.432933Z",
    "head_sha": "5da836c49c327f2c352216c5cbb4dea1abd9fcd3"
  }
}
```

</details>
