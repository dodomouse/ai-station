# Hindsight

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 61351 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:34:40.048Z |

## 中文

为智能体保存事实与经历，并按问题检索或综合相关记忆。

### 用途与功能

- 建立长期智能体记忆
- 按任务检索既有经历

用 retain、recall、reflect 接口组织记忆。提供服务端、多语言 SDK、可视化与编码智能体集成。

### 环境与限制

可使用Docker或源码部署，存储依赖PostgreSQL相关路径；各平台支持不同。提取和反思需要模型配置，服务费与数据处理另计。自托管与Hindsight Cloud应分别评估。

### 开始使用

按README启动推荐的本地部署，配置模型，再用一个SDK写入与检索少量记忆。 参阅[官方 README](https://github.com/vectorize-io/hindsight/blob/main/README.md)。

### 收录与来源

具备完整记忆服务、检索接口和SDK，且有运行时缺陷修复。 最近维护：[v1.2.1](https://github.com/vectorize-io/hindsight/releases/tag/v1.2.1)（2026-11-10T14:34:26Z）。正式版统一bank、alias和mental model的标识校验，并限制分页token量。

通过逛逛GitHub的第三方文章索引发现。索引记录了下列文章；本次未读取微信原文，不据此声称已阅读全文。

- 2026-10-05：[盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537550&idx=1&sn=29715a80ebde4036ab57651905d6bc3f)
- 2026-09-27：[推荐 8 个最近火火火火的开源项目，登上 GitHub 今日热榜。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537385&idx=1&sn=6f57abbd0554d6288c4aa1b3566ef704)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。


补充核对作者在公开平台发布或授权发布的文章，确认署名、日期与仓库关联：

- 2026-10-06：[盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。](https://www.woshipm.com/share/6473850.html)
- 2026-09-28：[推荐 8 个最近火火火火的开源项目，登上 GitHub 今日热榜。](https://www.woshipm.com/share/6470709.html)

## English

Stores facts and experiences for agents and retrieves or synthesizes relevant memory.

### Uses and features

- Build persistent agent memory
- Retrieve prior experience for tasks

Organizes memory through retain, recall and reflect interfaces, with a server, language SDKs, a UI and coding-agent integrations.

### Requirements and limits

Can use Docker or source deployments with PostgreSQL-related storage paths; platform support varies. Extraction and reflection require model configuration with separate costs and data processing. Evaluate self-hosting separately from Hindsight Cloud.

### Getting started

Start the recommended local deployment, configure a model and use an SDK to retain and recall a small set of memories. See the [official README](https://github.com/vectorize-io/hindsight/blob/main/README.md).

### Review and provenance

Provides a memory service, retrieval APIs and SDKs with runtime defect fixes. Recent maintenance: [v1.2.1](https://github.com/vectorize-io/hindsight/releases/tag/v1.2.1) (2026-11-10T14:34:26Z). The formal release unifies identifiers for banks, aliases and mental models and bounds page token budgets.

Discovered through a third-party index of 逛逛GitHub articles. The index records the articles below; the original WeChat pages were not read in this review. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.


Public articles published or authorized by the author were also checked for attribution, date and repository links. See the additional links in the Chinese section.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:34:40.048Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "hindsight",
    "name": "Hindsight",
    "repository": "vectorize-io/hindsight",
    "repo_node_id": "R_kgDOQMFwdQ",
    "category": "ai",
    "tags": [],
    "forms": [
      "service",
      "library",
      "cli"
    ],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "Hindsight"
      ],
      "en": [
        "Hindsight"
      ]
    },
    "summary": {
      "zh-CN": "为智能体保存事实与经历，并按问题检索或综合相关记忆。",
      "en": "Stores facts and experiences for agents and retrieves or synthesizes relevant memory."
    },
    "use_cases": {
      "zh-CN": [
        "建立长期智能体记忆",
        "按任务检索既有经历"
      ],
      "en": [
        "Build persistent agent memory",
        "Retrieve prior experience for tasks"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:34:40.048Z",
        "en": "2026-11-16T14:34:40.048Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "01fde0bedf83bdc185065d7af524a61690efe576a67f922eaff3a1280c17b63a",
      "source_url": "https://github.com/vectorize-io/hindsight/blob/937216ffb7eed86df2088842b67dd3c4bc2ec3b1/LICENSE",
      "reviewed_at": "2026-11-16T14:34:40.048Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "937216ffb7eed86df2088842b67dd3c4bc2ec3b1"
    },
    "activity_evidence": [
      {
        "type": "release",
        "url": "https://github.com/vectorize-io/hindsight/releases/tag/v1.2.1",
        "occurred_at": "2026-11-10T14:34:26Z",
        "reason": {
          "zh-CN": "正式版统一bank、alias和mental model的标识校验，并限制分页token量。",
          "en": "The formal release unifies identifiers for banks, aliases and mental models and bounds page token budgets."
        },
        "reviewed_at": "2026-11-16T14:34:40.048Z",
        "qualifies": true
      }
    ],
    "sources": [
      {
        "url": "https://github.com/vectorize-io/hindsight/blob/main/README.md",
        "accessed_at": "2026-11-16T14:34:40.048Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/vectorize-io/hindsight/blob/937216ffb7eed86df2088842b67dd3c4bc2ec3b1/LICENSE",
        "accessed_at": "2026-11-16T14:34:40.048Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.noking.tech/github-radar/data/library.json",
        "accessed_at": "2026-11-16T14:34:40.048Z",
        "supports": {
          "zh-CN": "第三方索引中的公众号文章归属、时间与项目发现线索；非原文阅读证据。",
          "en": "Third-party account attribution, article dates and discovery leads; not proof of reading the originals."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537550&idx=1&sn=29715a80ebde4036ab57651905d6bc3f",
        "accessed_at": "2026-11-16T14:34:40.048Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-10-05 盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-10-05; not directly read in this review."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537385&idx=1&sn=6f57abbd0554d6288c4aa1b3566ef704",
        "accessed_at": "2026-11-16T14:34:40.048Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-09-27 推荐 8 个最近火火火火的开源项目，登上 GitHub 今日热榜。；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-09-27; not directly read in this review."
        }
      },
      {
        "url": "https://www.woshipm.com/share/6473850.html",
        "accessed_at": "2026-11-16T14:26:02.487400+00:00",
        "published_date": "2026-10-06",
        "author": "逛逛GitHub",
        "supports": {
          "zh-CN": "作者公开发表或授权的文章；已核对署名、日期与仓库链接。",
          "en": "Author-published or authorized public article; attribution, date and repository links checked."
        }
      },
      {
        "url": "https://www.woshipm.com/share/6470709.html",
        "accessed_at": "2026-11-16T14:26:01.891924+00:00",
        "published_date": "2026-09-28",
        "author": "逛逛GitHub",
        "supports": {
          "zh-CN": "作者公开发表或授权的文章；已核对署名、日期与仓库链接。",
          "en": "Author-published or authorized public article; attribution, date and repository links checked."
        }
      }
    ],
    "quality_review": {
      "basis": {
        "zh-CN": "具备完整记忆服务、检索接口和SDK，且有运行时缺陷修复。",
        "en": "Provides a memory service, retrieval APIs and SDKs with runtime defect fixes."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOQMFwdQ",
    "full_name": "vectorize-io/hindsight",
    "stargazers_count": 61351,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "01fde0bedf83bdc185065d7af524a61690efe576a67f922eaff3a1280c17b63a",
    "last_success_at": "2026-11-16T14:19:44.847Z"
  }
}
```

</details>

