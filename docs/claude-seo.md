# Claude SEO

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 数据处理 / Data processing |
| 状态 / Status | 已收录 / Included |
| Star | 30107 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T04:07:37.951649+00:00 |

## 中文

在 Claude Code 中检查网站技术 SEO、内容和结构化数据，并整理改进建议。

### 用途与功能

- 检查抓取、索引、站点地图和页面性能。
- 分析内容、Schema.org 标记与 AI 搜索可访问性。
- 提供整站和单页审查命令及报告。

### 环境与限制

需要 Claude Code 1.0.33+、Python 3.11–3.14 和浏览器依赖。审查会使用 Claude 配额并向模型发送页面内容；未配置 Google API 时部分性能和索引判断只是估计。排名提升不作保证。

### 开始使用

按 README 安装公开插件，运行 /seo setup 和 /seo doctor，再从 /seo page 检查一个页面。

参阅[官方 README](https://github.com/AgriciDaniel/claude-seo/blob/468ed5b0d9e3249394783710e54abb02837e326b/README.md)。

### 收录与来源

适合把自动检查结果和模型解释汇总成可逐项核对的网站改进清单。

维护证据：[对页面提供的跨源 canonical 地址强制使用公网校验。防止其借用本地目标白名单访问内部地址。](https://github.com/AgriciDaniel/claude-seo/commit/05526d7f32993e0620737b648d1c8062d50d5af7)（2026-11-15）。

发现于 [GitHub 月榜](https://github.com/trending?since=monthly)。2026-11-17 的榜单记录新增 10,989 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Audits technical SEO, content and structured data inside Claude Code and organizes improvement recommendations.

### Uses and features

- Checks crawling, indexing, sitemaps and page performance.
- Analyzes content, Schema.org markup and AI-search accessibility.
- Provides whole-site and single-page audits with reports.

### Requirements and limits

Requires Claude Code 1.0.33+, Python 3.11–3.14 and browser dependencies. Audits consume Claude usage and send page content to the model; some performance and indexing checks are estimates without Google API data. Ranking gains are not guaranteed.

### Getting started

Install the public plugin from the README, run /seo setup and /seo doctor, then audit one page with /seo page.

See the [official README](https://github.com/AgriciDaniel/claude-seo/blob/468ed5b0d9e3249394783710e54abb02837e326b/README.md).

### Review and provenance

Useful for combining automated checks and model explanations into a reviewable website-improvement list.

Maintenance evidence: [Applies public-only URL validation to cross-origin canonical links from pages, preventing them from inheriting the local-target allowlist.](https://github.com/AgriciDaniel/claude-seo/commit/05526d7f32993e0620737b648d1c8062d50d5af7) (2026-11-15).

Discovered in [GitHub monthly Trending](https://github.com/trending?since=monthly), which recorded 10,989 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:07:37.951649+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "claude-seo",
    "name": "Claude SEO",
    "repository": "AgriciDaniel/claude-seo",
    "repo_node_id": "R_kgDORKpZAg",
    "category": "data",
    "summary": {
      "zh-CN": "在 Claude Code 中检查网站技术 SEO、内容和结构化数据，并整理改进建议。",
      "en": "Audits technical SEO, content and structured data inside Claude Code and organizes improvement recommendations."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:07:37.951649+00:00",
        "en": "2026-11-17T04:07:37.951649+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合把自动检查结果和模型解释汇总成可逐项核对的网站改进清单。",
      "en": "Useful for combining automated checks and model explanations into a reviewable website-improvement list.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/AgriciDaniel/claude-seo/blob/468ed5b0d9e3249394783710e54abb02837e326b/LICENSE",
      "license_sha256": "a42b3b0253cecea9af810c5207a67b0be8c9a0cfbf52b9302c3d26b063e7a86b",
      "source_commit": "468ed5b0d9e3249394783710e54abb02837e326b",
      "reviewed_at": "2026-11-17T04:07:37.951649+00:00",
      "evidence_pinned_at": "2026-11-17T04:07:37.951649+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "MIT covers the public plugin. Private Pro extensions, Claude Code access and optional external service subscriptions are outside this license review."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-15T09:28:40Z",
        "reviewed_at": "2026-11-17T04:07:37.951649+00:00",
        "url": "https://github.com/AgriciDaniel/claude-seo/commit/05526d7f32993e0620737b648d1c8062d50d5af7",
        "qualifies": true,
        "reason": {
          "zh-CN": "对页面提供的跨源 canonical 地址强制使用公网校验。防止其借用本地目标白名单访问内部地址。",
          "en": "Applies public-only URL validation to cross-origin canonical links from pages, preventing them from inheriting the local-target allowlist."
        },
        "reviewed_files": [
          "scripts/page_checks.py",
          "scripts/fetch_page.py",
          "scripts/url_safety.py"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/AgriciDaniel/claude-seo",
        "accessed_at": "2026-11-17T04:07:37.951649+00:00"
      },
      {
        "url": "https://github.com/AgriciDaniel/claude-seo/blob/468ed5b0d9e3249394783710e54abb02837e326b/README.md",
        "accessed_at": "2026-11-17T04:07:37.951649+00:00"
      },
      {
        "url": "https://github.com/AgriciDaniel/claude-seo/blob/468ed5b0d9e3249394783710e54abb02837e326b/LICENSE",
        "accessed_at": "2026-11-17T04:07:37.951649+00:00"
      },
      {
        "url": "https://github.com/AgriciDaniel/claude-seo/commit/05526d7f32993e0620737b648d1c8062d50d5af7",
        "accessed_at": "2026-11-17T04:07:37.951649+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 10989,
      "source_url": "https://github.com/trending?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDORKpZAg",
    "full_name": "AgriciDaniel/claude-seo",
    "stargazers_count": 30107,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "a42b3b0253cecea9af810c5207a67b0be8c9a0cfbf52b9302c3d26b063e7a86b",
    "last_success_at": "2026-11-17T03:54:40.068166+00:00"
  }
}
```

</details>
