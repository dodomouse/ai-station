# Crawl4AI

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[unclecode/crawl4ai](https://github.com/unclecode/crawl4ai)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 数据处理 / Data processing |
| 状态 / Status | 已收录 / Included |
| Star | 87470 |
| 评估时间 / Evaluated at | 2026-11-17T14:27:00.364278Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:31.722Z |

## 中文

把网页抓取为 Markdown 或结构化数据，支持自行部署和托管 API。

为 AI 搜索、研究和知识库建立流程提供可处理的网页内容。

### 主要功能

- 使用浏览器抓取网页并生成 Markdown。
- 支持结构化提取，并提供云端抓取与搜索接口。
- 可通过 Python 包或 Docker 服务接入应用。

### 环境要求

- 当前项目要求 Python 3.10+，本地抓取需安装浏览器及其系统依赖。
- 容器服务需要配置访问令牌；托管云 API 使用独立的账号凭据。

### 使用限制

- 托管服务负责浏览器和代理；自行部署时这些资源由使用者维护。
- 依赖模型的提取需另配模型访问，网页登录与访问限制也会影响结果。

### 开始使用

1. 按 README 安装 Crawl4AI，并运行 `crawl4ai-setup` 和 `crawl4ai-doctor`。
2. 用一个公开 URL 检查本地抓取和 Markdown 输出。
3. 再按任务配置结构化提取、服务认证或托管 API。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:31.722Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/unclecode/crawl4ai/commit/bf0c7925e21992af972039672fecd8e85163b575)。docs: remove retired aravind@crawl4ai.com from SECURITY.md contacts (#2570)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/unclecode/crawl4ai/blob/main/README.md)
- [GitHub 元数据 / Repository metadata](https://api.github.com/repos/unclecode/crawl4ai)
- [Python 环境要求 / Python requirements](https://github.com/unclecode/crawl4ai/blob/main/pyproject.toml)

## English

Crawls web pages into Markdown or structured data through self-hosted and hosted options.

Provides processable web content for AI search, research and knowledge-base ingestion.

### Features

- Uses browsers to crawl pages and generate Markdown.
- Supports structured extraction and hosted scraping and search APIs.
- Integrates through a Python package or Docker service.

### Requirements

- The current project requires Python 3.10+; local crawling needs browser and system dependencies.
- The container service requires an access token; the hosted API uses separate account credentials.

### Limitations

- The hosted service manages browsers and proxies; self-hosted users maintain these resources.
- Model-based extraction requires separate model access, and site sign-in or access restrictions affect results.

### Getting started

1. Install Crawl4AI from the README, then run `crawl4ai-setup` and `crawl4ai-doctor`.
2. Check local crawling and Markdown output using one public URL.
3. Then configure structured extraction, service authentication or the hosted API for the task.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:31.722Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/unclecode/crawl4ai/commit/bf0c7925e21992af972039672fecd8e85163b575).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/unclecode/crawl4ai/blob/main/README.md)
- [GitHub 元数据 / Repository metadata](https://api.github.com/repos/unclecode/crawl4ai)
- [Python 环境要求 / Python requirements](https://github.com/unclecode/crawl4ai/blob/main/pyproject.toml)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:27:00.364278Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "crawl4ai",
    "name": "Crawl4AI",
    "repository": "unclecode/crawl4ai",
    "repo_node_id": "R_kgDOL5OWWw",
    "category": "data",
    "summary": {
      "zh-CN": "把网页抓取为 Markdown 或结构化数据，支持自行部署和托管 API。",
      "en": "Crawls web pages into Markdown or structured data through self-hosted and hosted options."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:27:00.364278Z",
        "en": "2026-11-17T14:27:00.364278Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "为 AI 搜索、研究和知识库建立流程提供可处理的网页内容。",
        "en": "Provides processable web content for AI search, research and knowledge-base ingestion."
      },
      "source_url": "https://github.com/unclecode/crawl4ai/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/unclecode/crawl4ai/commit/bf0c7925e21992af972039672fecd8e85163b575",
        "occurred_at": "2026-11-17T10:19:36Z",
        "reviewed_at": "2026-11-17T14:27:00.364278Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "docs: remove retired aravind@crawl4ai.com from SECURITY.md contacts (#2570) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/unclecode/crawl4ai/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / Repository metadata",
        "url": "https://api.github.com/repos/unclecode/crawl4ai"
      },
      {
        "title": "Python 环境要求 / Python requirements",
        "url": "https://github.com/unclecode/crawl4ai/blob/main/pyproject.toml"
      }
    ]
  },
  "snapshot": {
    "full_name": "unclecode/crawl4ai",
    "repo_node_id": "R_kgDOL5OWWw",
    "stargazers_count": 87470,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:31.722Z",
    "source_url": "https://api.github.com/repos/unclecode/crawl4ai"
  }
}
```

</details>
