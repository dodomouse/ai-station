# OpenSEO

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[every-app/open-seo](https://github.com/every-app/open-seo)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 数据处理 / Data processing |
| 状态 / Status | 已收录 / Included |
| Star | 27897 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:50:00.691Z |

## 中文

自托管关键词、排名、外链和网站审计工作台，并向智能体提供MCP接口。

### 用途与功能

- 管理网站SEO研究与技术审计

提供关键词研究、排名跟踪、竞争分析、本地SEO与站点审计；技能可调用MCP读取数据。

### 环境与限制

支持Docker或Cloudflare部署。主要数据需要自己的DataForSEO账户并按量付费；托管订阅与MIT源码分开。抓取和排名结果受站点限制、数据源覆盖及区域配置影响。

### 开始使用

按README选择部署路径，配置自己的数据服务，再对少量关键词和自有网站测试。 参阅[官方 README](https://github.com/every-app/open-seo/blob/main/README.md)。

### 收录与来源

实现网站审计、数据工作流和MCP服务，支持实际自部署。 最近维护：[v0.1.27](https://github.com/every-app/open-seo/releases/tag/v0.1.27)（2026-11-11T18:19:38Z）。正式版修复审计页数上限、机器人检查页识别与本地排名匹配，并增加Lighthouse读取。

来源为2026-09-05公开转载文章，文末明确署名逛逛GitHub；已从公开正文提取仓库链接。

- 2026-09-05：[GitHub 周报：科研、语音、SEO，一个清单看懂 14 个 AI 项目](https://www.woshipm.com/ai/6460165.html)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。

## English

A self-hostable workspace for keywords, rankings, backlinks and site audits with MCP access for agents.

### Uses and features

- Manage SEO research and technical site audits

Provides keyword research, rank tracking, competitive analysis, local SEO and site audits; skills can access data through MCP.

### Requirements and limits

Supports Docker or Cloudflare deployment. Main data requires a personal DataForSEO account with usage charges; hosted subscriptions are separate from MIT source. Crawls and rankings depend on site restrictions, source coverage and region configuration.

### Getting started

Choose a deployment path, configure your data provider and test a few keywords and your own site. See the [official README](https://github.com/every-app/open-seo/blob/main/README.md).

### Review and provenance

Implements site audits, data workflows and an MCP service with a self-hosting path. Recent maintenance: [v0.1.27](https://github.com/every-app/open-seo/releases/tag/v0.1.27) (2026-11-11T18:19:38Z). The formal release fixes audit limits, bot-check page detection and local rank matching and adds Lighthouse retrieval.

The source is a public republication dated 2026-09-05 with explicit attribution to 逛逛GitHub; repository links were extracted from its public body. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:50:00.691Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "open-seo",
    "name": "OpenSEO",
    "repository": "every-app/open-seo",
    "repo_node_id": "R_kgDORanENg",
    "category": "data",
    "tags": [],
    "forms": [
      "service",
      "web"
    ],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "OpenSEO"
      ],
      "en": [
        "OpenSEO"
      ]
    },
    "summary": {
      "zh-CN": "自托管关键词、排名、外链和网站审计工作台，并向智能体提供MCP接口。",
      "en": "A self-hostable workspace for keywords, rankings, backlinks and site audits with MCP access for agents."
    },
    "use_cases": {
      "zh-CN": [
        "管理网站SEO研究与技术审计"
      ],
      "en": [
        "Manage SEO research and technical site audits"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:50:00.691Z",
        "en": "2026-11-16T14:50:00.691Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "c23e0aa0cdc924726993ffc8eb96e5283a7e8aaa7e068f1200277eb6df0f0f06",
      "source_url": "https://github.com/every-app/open-seo/blob/2df84ff91461cc55b6c8bb98f3ce0f195d2e463d/LICENSE",
      "reviewed_at": "2026-11-16T14:50:00.691Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "2df84ff91461cc55b6c8bb98f3ce0f195d2e463d"
    },
    "activity_evidence": [
      {
        "type": "release",
        "url": "https://github.com/every-app/open-seo/releases/tag/v0.1.27",
        "occurred_at": "2026-11-11T18:19:38Z",
        "reason": {
          "zh-CN": "正式版修复审计页数上限、机器人检查页识别与本地排名匹配，并增加Lighthouse读取。",
          "en": "The formal release fixes audit limits, bot-check page detection and local rank matching and adds Lighthouse retrieval."
        },
        "reviewed_at": "2026-11-16T14:50:00.691Z",
        "qualifies": true
      }
    ],
    "sources": [
      {
        "url": "https://github.com/every-app/open-seo/blob/main/README.md",
        "accessed_at": "2026-11-16T14:50:00.691Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/every-app/open-seo/blob/2df84ff91461cc55b6c8bb98f3ce0f195d2e463d/LICENSE",
        "accessed_at": "2026-11-16T14:50:00.691Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.woshipm.com/ai/6460165.html",
        "accessed_at": "2026-11-16T14:50:00.307Z",
        "supports": {
          "zh-CN": "已核对作者署名、日期与正文仓库链接。",
          "en": "Verified author attribution, date and repository links in the public article body."
        }
      }
    ],
    "quality_review": {
      "basis": {
        "zh-CN": "实现网站审计、数据工作流和MCP服务，支持实际自部署。",
        "en": "Implements site audits, data workflows and an MCP service with a self-hosting path."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDORanENg",
    "full_name": "every-app/open-seo",
    "stargazers_count": 27897,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "c23e0aa0cdc924726993ffc8eb96e5283a7e8aaa7e068f1200277eb6df0f0f06",
    "last_success_at": "2026-11-16T14:35:03.129Z"
  }
}
```

</details>

