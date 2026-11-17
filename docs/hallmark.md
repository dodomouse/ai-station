# Hallmark

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[Nutlope/hallmark](https://github.com/Nutlope/hallmark)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 55872 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:18:44.133Z |

## 中文

帮助编码智能体选择视觉风格、制作界面并检查页面设计。

### 主要功能

- 提供多套主题与设计、改版、审查流程。
- 包含静态检查和浏览器截图脚本。

### 环境与限制

- 脚本需要 Node.js 18+。
- 截图功能另需 Chrome 与 puppeteer-core，技能本身不提供模型服务。

### 开始使用

从[官方说明](https://github.com/Nutlope/hallmark/blob/main/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/Nutlope/hallmark/releases)可用于确认版本。

### 收录复核

帮助编码智能体选择视觉风格、制作界面并检查页面设计。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。

有效维护证据：[80fc3c723a](https://github.com/Nutlope/hallmark/commit/80fc3c723ab31eb9a43b7ce6c239d6bce094cdbb)，2026-11-09T06:04:29Z。修复 Windows 截图输出的 HTML 图片路径分隔符。

文章来源：[逛逛GitHub署名文章](https://www.woshipm.com/ai/6487701.html)，平台日期 2026-11-02。已通过公开正文核对仓库链接与作者归属；微信正文未直接读取。

本次为文档与实现证据复核，未安装或运行上游项目。

## English

An agent skill for choosing visual styles, building interfaces and checking page design.

### Features

- Provides themes and workflows for design, redesign and review.
- Includes static checks and browser capture scripts.

### Requirements and limits

- Scripts require Node.js 18+.
- Browser capture also needs Chrome and puppeteer-core
- the skill does not include model access.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/Nutlope/hallmark/blob/main/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/Nutlope/hallmark/releases) for versions.

### Review and provenance

An agent skill for choosing visual styles, building interfaces and checking page design. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.

Activity: [80fc3c723a](https://github.com/Nutlope/hallmark/commit/80fc3c723ab31eb9a43b7ce6c239d6bce094cdbb), 2026-11-09T06:04:29Z. Fixes path separators in generated HTML image references on Windows.

Discovery: [an author-attributed 逛逛GitHub article](https://www.woshipm.com/ai/6487701.html), dated 2026-11-02 on the public platform. Repository links and attribution were checked in its public body; the WeChat body was not read directly.

This review covers documentation and implementation evidence. The upstream project was not installed or run.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:58:29.135174Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "hallmark",
    "name": "Hallmark",
    "repository": "Nutlope/hallmark",
    "repo_node_id": "R_kgDOSOQ9xw",
    "category": "development",
    "summary": {
      "zh-CN": "帮助编码智能体选择视觉风格、制作界面并检查页面设计。",
      "en": "An agent skill for choosing visual styles, building interfaces and checking page design."
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
      "zh-CN": "帮助编码智能体选择视觉风格、制作界面并检查页面设计。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。",
      "en": "An agent skill for choosing visual styles, building interfaces and checking page design. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "06088a8b94598626f27612dea42300154bf7be967c85d9d3eee4490cb056af7d",
      "source_url": "https://github.com/Nutlope/hallmark/blob/04977e15f3dfd6ee4b74c887dac3eb52665d6c92/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "Root license reviewed. External dependencies and assets retain their individual licenses.",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "04977e15f3dfd6ee4b74c887dac3eb52665d6c92"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-09T06:04:29Z",
        "reviewed_at": "2026-11-16T14:58:29.135174Z",
        "url": "https://github.com/Nutlope/hallmark/commit/80fc3c723ab31eb9a43b7ce6c239d6bce094cdbb",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复 Windows 截图输出的 HTML 图片路径分隔符。",
          "en": "Fixes path separators in generated HTML image references on Windows."
        },
        "reviewed_files": [
          "skills/hallmark/scripts/capture.mjs",
          "skills/hallmark/scripts/capture.test.mjs"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/Nutlope/hallmark",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/Nutlope/hallmark/blob/main/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/Nutlope/hallmark/blob/04977e15f3dfd6ee4b74c887dac3eb52665d6c92/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/Nutlope/hallmark/commit/80fc3c723ab31eb9a43b7ce6c239d6bce094cdbb",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://www.woshipm.com/ai/6487701.html",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      }
    ],
    "article_source": {
      "article_id": "2247538256_1",
      "title": "盘点 10 月份 19 个 Star 蹭蹭涨的 GitHub 项目，第一个很有用。",
      "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538256&idx=1&sn=3b97e48392e47b295968f5c66a4ce5f0",
      "published_date": "2026-11-02",
      "account": "逛逛GitHub",
      "content_review_url": "https://www.woshipm.com/ai/6487701.html",
      "content_review_kind": "author-attributed public article",
      "wechat_direct_body_read": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOSOQ9xw",
    "full_name": "Nutlope/hallmark",
    "stargazers_count": 55872,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "06088a8b94598626f27612dea42300154bf7be967c85d9d3eee4490cb056af7d",
    "last_success_at": "2026-11-16T14:18:44.133Z"
  }
}
```

</details>
