# Vercel Skills CLI

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[vercel-labs/skills](https://github.com/vercel-labs/skills)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 39716 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T03:59:14.751398+00:00 |

## 中文

搜索、安装和管理 AI 编程智能体技能的命令行工具，支持按项目或全局配置技能。

### 用途与功能

- 搜索技能并选择安装到指定智能体。
- 检查更新、升级、移除技能并创建技能模板。
- 通过锁文件记录内容哈希与来源提交，用于还原安装。

### 环境与限制

需要 Node.js 22.20 或更高版本和兼容智能体。CLI 的 MIT 许可不覆盖其下载的第三方技能；技能可能附带脚本或外部服务要求。实验命令的接口可能变化。

### 开始使用

运行 `npx skills find` 查找技能，再用 `npx skills add` 选择来源、技能和目标智能体；复用环境可记录锁文件。

参阅[官方 README](https://github.com/vercel-labs/skills/blob/57217cf86ba38148a57af9e90d14a4c049558330/README.md)。

### 收录与来源

适合在多个智能体之间管理技能安装位置和版本，减少手工复制目录。

维护证据：[修复智能体技能目录本身为符号链接时生成失效相对链接的问题](https://github.com/vercel-labs/skills/commit/af860243b8c68053b3b5151e3732b9322933674d)（2026-11-16）。

发现于 [GitHub 月榜](https://github.com/trending/typescript?since=monthly)。2026-11-17 的榜单记录新增 4,576 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

A CLI for discovering, installing and managing AI coding-agent skills at project or global scope.

### Uses and features

- Search skills and install them for selected agents.
- Check updates, upgrade or remove skills, and create skill templates.
- Record content hashes and source commits in a lockfile for reproducible restoration.

### Requirements and limits

Requires Node.js 22.20 or later and a compatible agent. The CLI’s MIT license does not cover third-party skills it downloads, which may include scripts or external-service requirements. Experimental command interfaces may change.

### Getting started

Run `npx skills find` to discover skills, then use `npx skills add` to select a source, skill and target agent. Keep the lockfile when restoring environments.

See the [official README](https://github.com/vercel-labs/skills/blob/57217cf86ba38148a57af9e90d14a4c049558330/README.md).

### Review and provenance

Useful for managing skill locations and versions across agents with less manual directory copying.

Maintenance evidence: [Fixes invalid relative links when the agent skills directory is itself a symlink](https://github.com/vercel-labs/skills/commit/af860243b8c68053b3b5151e3732b9322933674d) (2026-11-16).

Discovered in [GitHub monthly Trending](https://github.com/trending/typescript?since=monthly), which recorded 4,576 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T03:59:14.751398+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "vercel-skills",
    "name": "Vercel Skills CLI",
    "repository": "vercel-labs/skills",
    "repo_node_id": "R_kgDOQ5_BBQ",
    "category": "development",
    "summary": {
      "zh-CN": "搜索、安装和管理 AI 编程智能体技能的命令行工具，支持按项目或全局配置技能。",
      "en": "A CLI for discovering, installing and managing AI coding-agent skills at project or global scope."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T03:59:14.751398+00:00",
        "en": "2026-11-17T03:59:14.751398+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合在多个智能体之间管理技能安装位置和版本，减少手工复制目录。",
      "en": "Useful for managing skill locations and versions across agents with less manual directory copying.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/vercel-labs/skills/blob/57217cf86ba38148a57af9e90d14a4c049558330/LICENSE",
      "license_sha256": "661142e53c313d2bb5e1b055f5c0a39001450ff1b5e27b89dc4bc7de9a6352ca",
      "source_commit": "57217cf86ba38148a57af9e90d14a4c049558330",
      "reviewed_at": "2026-11-17T03:59:14.751398+00:00",
      "evidence_pinned_at": "2026-11-17T03:59:14.751398+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "MIT covers the CLI. Installed skills, referenced tools and services have their own licenses and terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-16T03:36:57Z",
        "reviewed_at": "2026-11-17T03:59:14.751398+00:00",
        "url": "https://github.com/vercel-labs/skills/commit/af860243b8c68053b3b5151e3732b9322933674d",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复智能体技能目录本身为符号链接时生成失效相对链接的问题",
          "en": "Fixes invalid relative links when the agent skills directory is itself a symlink"
        },
        "reviewed_files": [
          "src/installer.ts"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/vercel-labs/skills",
        "accessed_at": "2026-11-17T03:59:14.751398+00:00"
      },
      {
        "url": "https://github.com/vercel-labs/skills/blob/57217cf86ba38148a57af9e90d14a4c049558330/README.md",
        "accessed_at": "2026-11-17T03:59:14.751398+00:00"
      },
      {
        "url": "https://github.com/vercel-labs/skills/blob/57217cf86ba38148a57af9e90d14a4c049558330/LICENSE",
        "accessed_at": "2026-11-17T03:59:14.751398+00:00"
      },
      {
        "url": "https://github.com/vercel-labs/skills/commit/af860243b8c68053b3b5151e3732b9322933674d",
        "accessed_at": "2026-11-17T03:59:14.751398+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 4576,
      "source_url": "https://github.com/trending/typescript?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOQ5_BBQ",
    "full_name": "vercel-labs/skills",
    "stargazers_count": 39716,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "661142e53c313d2bb5e1b055f5c0a39001450ff1b5e27b89dc4bc7de9a6352ca",
    "last_success_at": "2026-11-17T03:52:08.718211+00:00"
  }
}
```

</details>
