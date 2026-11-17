# Firecrawl

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[firecrawl/firecrawl](https://github.com/firecrawl/firecrawl)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 数据处理 / Data processing |
| 状态 / Status | 已收录 / Included |
| Star | 202520 |
| 评估时间 / Evaluated at | 2026-11-17T14:27:00.364121Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:32.024Z |

## 中文

提供网页搜索、抓取、交互与文档解析接口，为 AI 整理网页内容。

向智能体和知识检索流程提供 Markdown、结构化数据和网页来源。

### 主要功能

- 搜索网页并抓取内容，支持整站抓取和批量处理。
- 输出 Markdown、JSON 与截图。
- 提供托管 Agent 数据收集接口及多语言 SDK。

### 环境要求

- 托管服务需要 Firecrawl 账号和 API 凭据。
- 可选择 Python、Node.js 或 Go SDK；自部署需按独立指南配置服务组件。

### 使用限制

- 托管服务与自部署功能不完全一致，例如 Alexandria 不包含在自部署服务中。
- 抓取结果受目标网站访问条件影响，批量任务需设置范围并检查返回来源。

### 开始使用

1. 从 README 选择托管 API 或自部署路线。
2. 安装对应 SDK 并配置服务地址和认证。
3. 先抓取一个公开 URL，检查 Markdown 与来源，再启用搜索或有范围限制的整站抓取。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:32.024Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/firecrawl/firecrawl/commit/8e7e5887cfd69e1db2d3f16be22a642a02370aec)。fix(api): log where a firebill call's time went, and keep its connections alive (#5799)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/firecrawl/firecrawl/blob/main/README.md)
- [GitHub 元数据 / Repository metadata](https://api.github.com/repos/firecrawl/firecrawl)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

Provides web search, scraping, interaction and document-parsing APIs for AI-ready web content.

Supplies Markdown, structured data and web sources to agents and retrieval workflows.

### Features

- Searches and scrapes pages, with crawling and batch processing.
- Returns Markdown, JSON and screenshots.
- Provides a hosted data-gathering Agent endpoint and SDKs for multiple languages.

### Requirements

- Hosted use requires a Firecrawl account and API credentials.
- Choose a Python, Node.js or Go SDK; self-hosting needs the service components in its separate guide.

### Limitations

- Hosted and self-hosted features differ; for example, Alexandria is not included in the self-hosted server.
- Results depend on target-site access conditions; bound batch jobs and inspect their returned sources.

### Getting started

1. Choose hosted API access or self-hosting from the README.
2. Install the matching SDK and configure the service endpoint and authentication.
3. Scrape one public URL, inspect Markdown and provenance, then enable search or a bounded crawl.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:32.024Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/firecrawl/firecrawl/commit/8e7e5887cfd69e1db2d3f16be22a642a02370aec).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/firecrawl/firecrawl/blob/main/README.md)
- [GitHub 元数据 / Repository metadata](https://api.github.com/repos/firecrawl/firecrawl)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:27:00.364121Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "firecrawl",
    "name": "Firecrawl",
    "repository": "firecrawl/firecrawl",
    "repo_node_id": "R_kgDOLunVBg",
    "category": "data",
    "summary": {
      "zh-CN": "提供网页搜索、抓取、交互与文档解析接口，为 AI 整理网页内容。",
      "en": "Provides web search, scraping, interaction and document-parsing APIs for AI-ready web content."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:27:00.364121Z",
        "en": "2026-11-17T14:27:00.364121Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "向智能体和知识检索流程提供 Markdown、结构化数据和网页来源。",
        "en": "Supplies Markdown, structured data and web sources to agents and retrieval workflows."
      },
      "source_url": "https://github.com/firecrawl/firecrawl/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/firecrawl/firecrawl/commit/8e7e5887cfd69e1db2d3f16be22a642a02370aec",
        "occurred_at": "2026-11-17T05:35:29Z",
        "reviewed_at": "2026-11-17T14:27:00.364121Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "fix(api): log where a firebill call's time went, and keep its connections alive (#5799) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/firecrawl/firecrawl/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / Repository metadata",
        "url": "https://api.github.com/repos/firecrawl/firecrawl"
      }
    ]
  },
  "snapshot": {
    "full_name": "firecrawl/firecrawl",
    "repo_node_id": "R_kgDOLunVBg",
    "stargazers_count": 202520,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:32.024Z",
    "source_url": "https://api.github.com/repos/firecrawl/firecrawl"
  }
}
```

</details>
