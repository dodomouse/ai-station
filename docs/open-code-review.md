# Open Code Review

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[alibaba/open-code-review](https://github.com/alibaba/open-code-review)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 52711 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:34:40.000Z |

## 中文

读取 Git 差异或整份文件，让可配置模型生成带行号的代码审查意见。

### 用途与功能

- 审查提交差异
- 检查陌生仓库或无差异文件

审查智能体可读取上下文文件、搜索代码并交叉查看修改；提供workspace、会话恢复及结构化反馈。

### 环境与限制

支持Windows、macOS、Linux；需要Git和可用模型端点。代码会按配置发送给服务商，费用和数据条件另计。模型可能遗漏或误报问题，上游基准结果未复测。

### 开始使用

按README安装CLI并配置模型，先在小范围差异上运行review或scan。 参阅[官方 README](https://github.com/alibaba/open-code-review/blob/main/README.md)。

### 收录与来源

提供可运行审查器、代码上下文工具和会话管理，支持具体文件级反馈。 最近维护：[v1.13.10](https://github.com/alibaba/open-code-review/releases/tag/v1.13.10)（2026-11-15T02:56:09Z）。正式版增加workspace恢复、比较侧代码访问和Markdown总结渲染。

通过逛逛GitHub的第三方文章索引发现。索引记录了下列文章；本次未读取微信原文，不据此声称已阅读全文。

- 2026-10-05：[盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537550&idx=1&sn=29715a80ebde4036ab57651905d6bc3f)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。


补充核对作者在公开平台发布或授权发布的文章，确认署名、日期与仓库关联：

- 2026-10-06：[盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。](https://www.woshipm.com/share/6473850.html)

## English

Reviews Git diffs or whole files with a configurable model and produces line-level findings.

### Uses and features

- Review commit differences
- Audit unfamiliar repositories or files without a diff

The review agent can read contextual files, search code and inspect related changes, with workspace mode, session resumption and structured feedback.

### Requirements and limits

Supports Windows, macOS and Linux and needs Git and a usable model endpoint. Code is sent according to provider configuration, with separate costs and data terms. Models can miss defects or report false positives; upstream benchmarks were not reproduced.

### Getting started

Install the CLI, configure a model and begin with review or scan on a small scope. See the [official README](https://github.com/alibaba/open-code-review/blob/main/README.md).

### Review and provenance

Provides an executable reviewer, code-context tools and session management with file-level feedback. Recent maintenance: [v1.13.10](https://github.com/alibaba/open-code-review/releases/tag/v1.13.10) (2026-11-15T02:56:09Z). The formal release adds workspace resumption, comparison-side code access and Markdown summary rendering.

Discovered through a third-party index of 逛逛GitHub articles. The index records the articles below; the original WeChat pages were not read in this review. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.


Public articles published or authorized by the author were also checked for attribution, date and repository links. See the additional links in the Chinese section.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:34:40.000Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "open-code-review",
    "name": "Open Code Review",
    "repository": "alibaba/open-code-review",
    "repo_node_id": "R_kgDOSgbPIg",
    "category": "development",
    "tags": [],
    "forms": [
      "cli"
    ],
    "platforms": [
      "linux",
      "macos",
      "windows"
    ],
    "aliases": {
      "zh-CN": [
        "Open Code Review"
      ],
      "en": [
        "Open Code Review"
      ]
    },
    "summary": {
      "zh-CN": "读取 Git 差异或整份文件，让可配置模型生成带行号的代码审查意见。",
      "en": "Reviews Git diffs or whole files with a configurable model and produces line-level findings."
    },
    "use_cases": {
      "zh-CN": [
        "审查提交差异",
        "检查陌生仓库或无差异文件"
      ],
      "en": [
        "Review commit differences",
        "Audit unfamiliar repositories or files without a diff"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:34:40.000Z",
        "en": "2026-11-16T14:34:40.000Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "1945665fdb6968a66ea29438ddee0aee23035365c862e5c4a75b62b303340acf",
      "source_url": "https://github.com/alibaba/open-code-review/blob/dd1a7e12a3565f5f7396acb394d83ab18102e6ce/LICENSE",
      "reviewed_at": "2026-11-16T14:34:40.000Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "dd1a7e12a3565f5f7396acb394d83ab18102e6ce"
    },
    "activity_evidence": [
      {
        "type": "release",
        "url": "https://github.com/alibaba/open-code-review/releases/tag/v1.13.10",
        "occurred_at": "2026-11-15T02:56:09Z",
        "reason": {
          "zh-CN": "正式版增加workspace恢复、比较侧代码访问和Markdown总结渲染。",
          "en": "The formal release adds workspace resumption, comparison-side code access and Markdown summary rendering."
        },
        "reviewed_at": "2026-11-16T14:34:40.000Z",
        "qualifies": true
      }
    ],
    "sources": [
      {
        "url": "https://github.com/alibaba/open-code-review/blob/main/README.md",
        "accessed_at": "2026-11-16T14:34:40.000Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/alibaba/open-code-review/blob/dd1a7e12a3565f5f7396acb394d83ab18102e6ce/LICENSE",
        "accessed_at": "2026-11-16T14:34:40.000Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.noking.tech/github-radar/data/library.json",
        "accessed_at": "2026-11-16T14:34:40.000Z",
        "supports": {
          "zh-CN": "第三方索引中的公众号文章归属、时间与项目发现线索；非原文阅读证据。",
          "en": "Third-party account attribution, article dates and discovery leads; not proof of reading the originals."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537550&idx=1&sn=29715a80ebde4036ab57651905d6bc3f",
        "accessed_at": "2026-11-16T14:34:40.000Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-10-05 盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-10-05; not directly read in this review."
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
      }
    ],
    "quality_review": {
      "basis": {
        "zh-CN": "提供可运行审查器、代码上下文工具和会话管理，支持具体文件级反馈。",
        "en": "Provides an executable reviewer, code-context tools and session management with file-level feedback."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOSgbPIg",
    "full_name": "alibaba/open-code-review",
    "stargazers_count": 52711,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "1945665fdb6968a66ea29438ddee0aee23035365c862e5c4a75b62b303340acf",
    "last_success_at": "2026-11-16T14:19:44.267Z"
  }
}
```

</details>

