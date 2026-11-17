# Stitch Design Skills

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[google-labs-code/stitch-skills](https://github.com/google-labs-code/stitch-skills)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 9786 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-17T04:00:03.486610+00:00 |

## 中文

通过 Google Stitch 的 MCP 接口，为智能体提供界面设计、设计系统提取和前端实现技能。

### 用途与功能

- 从文本、图片或前端代码创建与整理 Stitch 设计。
- 提供 React、React Native 转换及设计说明生成工作流。

### 环境与限制

需要配置 Stitch MCP、凭据及兼容智能体；部分技能有相互依赖。仓库并非 Google 官方支持产品，代码许可不覆盖 Stitch 服务。

### 开始使用

配置 Stitch MCP 后，用 npx skills add google-labs-code/stitch-skills 选择技能，先在测试项目生成一个页面。

参阅[官方 README](https://github.com/google-labs-code/stitch-skills/blob/0337446dadde6f8c94210444e2aa9d546126480f/README.md)。

### 收录与来源

连接设计输入、设计规范和前端转换步骤，便于在智能体会话中复用界面实现流程。

维护证据：[合入 SITE.md 技能，按需求生成项目身份、视觉语言、目录、站点地图与待办并写入 .stitch/SITE.md。](https://github.com/google-labs-code/stitch-skills/commit/0337446dadde6f8c94210444e2aa9d546126480f)（2026-08-17）。

发现于 [GitHub 月榜](https://github.com/trending/typescript?since=monthly)。2026-11-17 的榜单记录新增 1,163 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Agent skills for UI design, design-system extraction and frontend implementation through Google Stitch MCP.

### Uses and features

- Creates and organizes Stitch designs from text, images or frontend code.
- Provides React and React Native conversion and design-document workflows.

### Requirements and limits

Requires configured Stitch MCP, credentials and a compatible agent; some skills depend on others. This is not an officially supported Google product, and the repository license does not cover the Stitch service.

### Getting started

Configure Stitch MCP, select skills with npx skills add google-labs-code/stitch-skills and generate one screen in a test project.

See the [official README](https://github.com/google-labs-code/stitch-skills/blob/0337446dadde6f8c94210444e2aa9d546126480f/README.md).

### Review and provenance

Connects design inputs, design specifications and frontend conversion into reusable agent workflows.

Maintenance evidence: [Merges a SITE.md skill that derives project identity, visual language, structure, sitemap and backlog from requirements and writes .stitch/SITE.md.](https://github.com/google-labs-code/stitch-skills/commit/0337446dadde6f8c94210444e2aa9d546126480f) (2026-08-17).

Discovered in [GitHub monthly Trending](https://github.com/trending/typescript?since=monthly), which recorded 1,163 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:00:03.486610+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "stitch-skills",
    "name": "Stitch Design Skills",
    "repository": "google-labs-code/stitch-skills",
    "repo_node_id": "R_kgDOQ7Opvg",
    "category": "development",
    "summary": {
      "zh-CN": "通过 Google Stitch 的 MCP 接口，为智能体提供界面设计、设计系统提取和前端实现技能。",
      "en": "Agent skills for UI design, design-system extraction and frontend implementation through Google Stitch MCP."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:00:03.486610+00:00",
        "en": "2026-11-17T04:00:03.486610+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "连接设计输入、设计规范和前端转换步骤，便于在智能体会话中复用界面实现流程。",
      "en": "Connects design inputs, design specifications and frontend conversion into reusable agent workflows.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "source_url": "https://github.com/google-labs-code/stitch-skills/blob/0337446dadde6f8c94210444e2aa9d546126480f/LICENSE",
      "license_sha256": "b4133a55232c0996713349891dc55469d46a16ec027c033c9e4108b2149abb42",
      "source_commit": "0337446dadde6f8c94210444e2aa9d546126480f",
      "reviewed_at": "2026-11-17T04:00:03.486610+00:00",
      "evidence_pinned_at": "2026-11-17T04:00:03.486610+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "Apache-2.0 covers repository skills and supporting code; Google Stitch access and generated or uploaded assets have separate terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-08-17T20:20:22Z",
        "reviewed_at": "2026-11-17T04:00:03.486610+00:00",
        "url": "https://github.com/google-labs-code/stitch-skills/commit/0337446dadde6f8c94210444e2aa9d546126480f",
        "qualifies": true,
        "reason": {
          "zh-CN": "合入 SITE.md 技能，按需求生成项目身份、视觉语言、目录、站点地图与待办并写入 .stitch/SITE.md。",
          "en": "Merges a SITE.md skill that derives project identity, visual language, structure, sitemap and backlog from requirements and writes .stitch/SITE.md."
        },
        "reviewed_files": [
          "plugins/stitch-utilities/skills/site-md/SKILL.md"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/google-labs-code/stitch-skills",
        "accessed_at": "2026-11-17T04:00:03.486610+00:00"
      },
      {
        "url": "https://github.com/google-labs-code/stitch-skills/blob/0337446dadde6f8c94210444e2aa9d546126480f/README.md",
        "accessed_at": "2026-11-17T04:00:03.486610+00:00"
      },
      {
        "url": "https://github.com/google-labs-code/stitch-skills/blob/0337446dadde6f8c94210444e2aa9d546126480f/LICENSE",
        "accessed_at": "2026-11-17T04:00:03.486610+00:00"
      },
      {
        "url": "https://github.com/google-labs-code/stitch-skills/commit/0337446dadde6f8c94210444e2aa9d546126480f",
        "accessed_at": "2026-11-17T04:00:03.486610+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 1163,
      "source_url": "https://github.com/trending/typescript?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOQ7Opvg",
    "full_name": "google-labs-code/stitch-skills",
    "stargazers_count": 9786,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "b4133a55232c0996713349891dc55469d46a16ec027c033c9e4108b2149abb42",
    "last_success_at": "2026-11-17T03:54:48.140629+00:00"
  }
}
```

</details>
