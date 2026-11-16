# 词光 Word Atlas

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[designfuchen/word-atlas](https://github.com/designfuchen/word-atlas)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 4915 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:19:06.010Z |

## 中文

用插画、发音和间隔复习学习英语词汇的网页应用。

### 主要功能

- 按词条查看释义、例句、英美发音和插画。
- 在本机保存学习进度，使用 FSRS 安排复习。

### 环境与限制

- 源码运行需要 Node.js 20+ 和 npm，图形视图需要 WebGL2。
- MIT 覆盖代码，词库与媒体采用 CC BY 4.0，AI 生成内容未逐条人工校对。

### 开始使用

从[官方说明](https://github.com/designfuchen/word-atlas/blob/main/README.en.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/designfuchen/word-atlas/releases)可用于确认版本。

### 收录复核

用插画、发音和间隔复习学习英语词汇的网页应用。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。

有效维护证据：[4ff9c42974](https://github.com/designfuchen/word-atlas/commit/4ff9c429745c12506a9d07d3c29f0791a66191d5)，2026-10-25T10:34:16Z。首次提交可运行应用；已核对新增 src/store/srs.ts，并读取该提交中的 FSRS 调度实现。

文章来源：[逛逛GitHub署名文章](https://www.woshipm.com/share/6487219.html)，平台日期 2026-10-31。已通过公开正文核对仓库链接与作者归属；微信正文未直接读取。

本次为文档与实现证据复核，未安装或运行上游项目。

## English

A vocabulary web app combining illustrations, pronunciation and spaced review.

### Features

- Shows definitions, examples, British and American pronunciation, and illustrations.
- Stores progress locally and schedules review with FSRS.

### Requirements and limits

- Source setup needs Node.js 20+ and npm
- graphical views require WebGL2.
- Code is MIT
- vocabulary and media are CC BY 4.0, and AI-generated content has not been individually proofread.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/designfuchen/word-atlas/blob/main/README.en.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/designfuchen/word-atlas/releases) for versions.

### Review and provenance

A vocabulary web app combining illustrations, pronunciation and spaced review. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.

Activity: [4ff9c42974](https://github.com/designfuchen/word-atlas/commit/4ff9c429745c12506a9d07d3c29f0791a66191d5), 2026-10-25T10:34:16Z. Initial functional app commit; verified src/store/srs.ts was added and read its FSRS scheduling implementation at that SHA.

Discovery: [an author-attributed 逛逛GitHub article](https://www.woshipm.com/share/6487219.html), dated 2026-10-31 on the public platform. Repository links and attribution were checked in its public body; the WeChat body was not read directly.

This review covers documentation and implementation evidence. The upstream project was not installed or run.

## Review evidence

```json
{
  "evaluated_at": "2026-11-16T14:58:29.135174Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "word-atlas",
    "name": "词光 Word Atlas",
    "repository": "designfuchen/word-atlas",
    "repo_node_id": "R_kgDOVWmLuw",
    "category": "productivity",
    "summary": {
      "zh-CN": "用插画、发音和间隔复习学习英语词汇的网页应用。",
      "en": "A vocabulary web app combining illustrations, pronunciation and spaced review."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:58:29.135174Z",
        "en": "2026-11-16T14:58:29.135174Z"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "用插画、发音和间隔复习学习英语词汇的网页应用。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。",
      "en": "A vocabulary web app combining illustrations, pronunciation and spaced review. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "83d3aff30ac8f86748449ea43c29eb69e6d6baf021a9ae2df1961f5e5f58b0a5",
      "source_url": "https://github.com/designfuchen/word-atlas/blob/main/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "MIT covers source code and UI. Vocabulary, illustrations and recordings are CC BY 4.0; fonts and dependencies retain their licenses."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-10-25T10:34:16Z",
        "reviewed_at": "2026-11-16T14:58:29.135174Z",
        "url": "https://github.com/designfuchen/word-atlas/commit/4ff9c429745c12506a9d07d3c29f0791a66191d5",
        "qualifies": true,
        "reason": {
          "zh-CN": "首次提交可运行应用；已核对新增 src/store/srs.ts，并读取该提交中的 FSRS 调度实现。",
          "en": "Initial functional app commit; verified src/store/srs.ts was added and read its FSRS scheduling implementation at that SHA."
        },
        "reviewed_files": [
          "src/store/srs.ts"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/designfuchen/word-atlas",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/designfuchen/word-atlas/blob/main/README.en.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/designfuchen/word-atlas/blob/main/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/designfuchen/word-atlas/commit/4ff9c429745c12506a9d07d3c29f0791a66191d5",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://www.woshipm.com/share/6487219.html",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      }
    ],
    "article_source": {
      "article_id": "2247538180_1",
      "title": "我在 GitHub 上搜罗了 6 个高质量数据集，看看哪些会用到。",
      "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538180&idx=1&sn=f8f37078438b90a2815051c5012a8acc",
      "published_date": "2026-10-31",
      "account": "逛逛GitHub",
      "content_review_url": "https://www.woshipm.com/share/6487219.html",
      "content_review_kind": "author-attributed public article",
      "wechat_direct_body_read": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVWmLuw",
    "full_name": "designfuchen/word-atlas",
    "stargazers_count": 4915,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "NOASSERTION",
    "license_sha256": "83d3aff30ac8f86748449ea43c29eb69e6d6baf021a9ae2df1961f5e5f58b0a5",
    "last_success_at": "2026-11-16T14:19:06.010Z"
  }
}
```
