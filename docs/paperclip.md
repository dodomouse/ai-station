# Paperclip

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[paperclipai/paperclip](https://github.com/paperclipai/paperclip)

| 项目 / Field | 内容 / Value |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 114265 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:50:50.290410+00:00 |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:19:44.333Z |

## 中文

管理 AI 团队的组织、目标、任务、权限和预算，连接已有 Agent，并跟踪执行与模型成本。

**环境与限制：** 本地运行需要 Node.js 24.11 和 pnpm 9.15，使用内嵌 PostgreSQL；生产环境按部署说明配置数据库。Agent 登录、模型服务和费用另行提供，部分集成需要 Python 3。

**入门：** 从[官方说明](https://raw.githubusercontent.com/paperclipai/paperclip/master/README.md)确认安装与配置步骤，再查看[发布版本](https://github.com/paperclipai/paperclip/releases)。本次为文档、许可原文与维护证据审查，未安装运行。

**近期维护：** [v2026.1106.0 增加原生 Runner 与 Agent harness 支持。](https://github.com/paperclipai/paperclip/releases/tag/v2026.1106.0)（2026-11-06）

## English

Coordinates AI teams through organizations, goals, tasks, permissions and budgets, connecting existing agents and tracking execution and model costs.

**Requirements and limitations:** Local setup requires Node.js 24.11 and pnpm 9.15 with embedded PostgreSQL; production databases follow deployment instructions. Supply agent logins and model access separately; some integrations require Python 3.

**Getting started:** Follow the [official documentation](https://raw.githubusercontent.com/paperclipai/paperclip/master/README.md) for setup, then check [releases](https://github.com/paperclipai/paperclip/releases). This review examined documentation, license text and maintenance evidence; the software was not installed or run.

**Recent maintenance:** [v2026.1106.0 adds native runner and agent-harness support.](https://github.com/paperclipai/paperclip/releases/tag/v2026.1106.0) (2026-11-06)

## Review evidence

发现线索来自第三方公众号文章索引，原始微信正文未完整读取；用途、环境、许可与维护状态依据仓库当前资料复核。

Discovery uses a third-party WeChat article index; the original article body was not fully read. Current repository sources were reviewed for function, requirements, licensing and maintenance.

- 公众号索引原文 / Indexed WeChat source：[盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537550&idx=1&sn=29715a80ebde4036ab57651905d6bc3f)（2026-10-05）
- 作者署名转载 / Author-attributed repost：[盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。](https://www.woshipm.com/share/6473850.html)（2026-10-06）；仓库链接映射已交叉核对 / repository mapping corroborated.

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-16T14:50:50.290410+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "paperclip",
    "name": "Paperclip",
    "repository": "paperclipai/paperclip",
    "repo_node_id": "R_kgDORclPyA",
    "category": "ai",
    "summary": {
      "zh-CN": "管理 AI 团队的组织、目标、任务、权限和预算，连接已有 Agent，并跟踪执行与模型成本。",
      "en": "Coordinates AI teams through organizations, goals, tasks, permissions and budgets, connecting existing agents and tracking execution and model costs."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:50:50.290410+00:00",
        "en": "2026-11-16T14:50:50.290410+00:00"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "7f8a27f0979bded50e240caa8c8c29f3088ddf87032cb83e5a9732bff91d18b4",
      "source_url": "https://github.com/paperclipai/paperclip/blob/b4fa1c7fb1c9adafc6407bc46381a0ab89f4b4fd/LICENSE",
      "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
      "files": [
        {
          "path": "LICENSE",
          "source_url": "https://github.com/paperclipai/paperclip/blob/b4fa1c7fb1c9adafc6407bc46381a0ab89f4b4fd/LICENSE",
          "fetched_at": "2026-11-16T14:23:28.167Z",
          "sha256": "7f8a27f0979bded50e240caa8c8c29f3088ddf87032cb83e5a9732bff91d18b4",
          "source_commit": "b4fa1c7fb1c9adafc6407bc46381a0ab89f4b4fd"
        }
      ],
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "b4fa1c7fb1c9adafc6407bc46381a0ab89f4b4fd"
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-11-06T22:31:53Z",
        "url": "https://github.com/paperclipai/paperclip/releases/tag/v2026.1106.0",
        "tag": "v2026.1106.0",
        "summary": "v2026.1106.0",
        "draft": false,
        "prerelease": false,
        "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
        "qualifies": true,
        "reason": {
          "zh-CN": "v2026.1106.0 增加原生 Runner 与 Agent harness 支持。",
          "en": "v2026.1106.0 adds native runner and agent-harness support."
        }
      }
    ],
    "sources": [
      {
        "article_id": "2247537550_1",
        "title": "盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537550&idx=1&sn=29715a80ebde4036ab57651905d6bc3f",
        "published_date": "2026-10-05",
        "account": "逛逛GitHub",
        "source_strength": "third_party_index",
        "index_url": "https://www.noking.tech/github-radar/data/library.json",
        "original_article_body_read": false
      },
      {
        "article_id": "2247537385_1",
        "title": "推荐 8 个最近火火火火的开源项目，登上 GitHub 今日热榜。",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537385&idx=1&sn=6f57abbd0554d6288c4aa1b3566ef704",
        "published_date": "2026-09-27",
        "account": "逛逛GitHub",
        "source_strength": "third_party_index",
        "index_url": "https://www.noking.tech/github-radar/data/library.json",
        "original_article_body_read": false
      },
      {
        "url": "https://www.woshipm.com/share/6473850.html",
        "title": "盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。",
        "published_date": "2026-10-06",
        "account": "逛逛GitHub",
        "source_strength": "author_attributed_repost_repository_mapping",
        "author_attribution_confirmed": true,
        "body_read_method": "public_html_repository_links_and_attribution_extraction",
        "full_text_archived": false
      },
      {
        "url": "https://www.woshipm.com/share/6470709.html",
        "title": "推荐 8 个最近火火火火的开源项目，登上 GitHub 今日热榜。",
        "published_date": "2026-09-28",
        "account": "逛逛GitHub",
        "source_strength": "author_attributed_repost_repository_mapping",
        "author_attribution_confirmed": true,
        "body_read_method": "public_html_repository_links_and_attribution_extraction",
        "full_text_archived": false
      }
    ],
    "discovery": {
      "account": "逛逛GitHub",
      "window_start": "2026-08-16",
      "window_end": "2026-11-16",
      "original_article_body_read": false,
      "repository_review_sources": [
        "https://api.github.com/repos/paperclipai/paperclip",
        "https://raw.githubusercontent.com/paperclipai/paperclip/master/README.md",
        "https://github.com/paperclipai/paperclip/releases/tag/v2026.1106.0",
        "https://github.com/paperclipai/paperclip/blob/b4fa1c7fb1c9adafc6407bc46381a0ab89f4b4fd/LICENSE"
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDORclPyA",
    "full_name": "paperclipai/paperclip",
    "stargazers_count": 114265,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "7f8a27f0979bded50e240caa8c8c29f3088ddf87032cb83e5a9732bff91d18b4",
    "last_success_at": "2026-11-16T14:19:44.333Z"
  }
}
```

</details>
