# i-have-adhd

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 61361 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:19:44.584Z |

## 中文

调整编码智能体的回答格式，使行动步骤和关键信息更容易找到。

### 主要功能

- 要求先给行动，再列出简短步骤。
- 提供多种智能体的插件与可选会话注入方式。

### 环境与限制

- 需要兼容的智能体宿主，启用持续注入前应检查本机规则冲突。
- 这是写作与交互规则，不提供诊断或治疗功能。

### 开始使用

从[官方说明](https://github.com/ayghri/i-have-adhd/blob/main/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/ayghri/i-have-adhd/releases)可用于确认版本。

### 收录复核

调整编码智能体的回答格式，使行动步骤和关键信息更容易找到。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。

有效维护证据：[707c114cac](https://github.com/ayghri/i-have-adhd/commit/707c114cac4da1e78cbbb4f1f729121b4075de5e)，2026-10-06T22:04:52Z。增加 OpenCode 新版插件 API 兼容实现。

文章来源：[逛逛GitHub署名文章](https://www.woshipm.com/share/6473850.html)，平台日期 2026-10-06。已通过公开正文核对仓库链接与作者归属；微信正文未直接读取。

本次为文档与实现证据复核，未安装或运行上游项目。

## English

Adjusts coding-agent responses to make actions and key information easier to find.

### Features

- Puts actions first and organizes concise steps.
- Provides integrations for multiple agents and optional session injection.

### Requirements and limits

- Requires a compatible agent host
- check local rule conflicts before enabling persistent injection.
- These are writing and interaction rules, not diagnostic or treatment tools.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/ayghri/i-have-adhd/blob/main/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/ayghri/i-have-adhd/releases) for versions.

### Review and provenance

Adjusts coding-agent responses to make actions and key information easier to find. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.

Activity: [707c114cac](https://github.com/ayghri/i-have-adhd/commit/707c114cac4da1e78cbbb4f1f729121b4075de5e), 2026-10-06T22:04:52Z. Adds compatibility with the newer OpenCode plugin API.

Discovery: [an author-attributed 逛逛GitHub article](https://www.woshipm.com/share/6473850.html), dated 2026-10-06 on the public platform. Repository links and attribution were checked in its public body; the WeChat body was not read directly.

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
    "id": "i-have-adhd",
    "name": "i-have-adhd",
    "repository": "ayghri/i-have-adhd",
    "repo_node_id": "R_kgDOScw2eQ",
    "category": "productivity",
    "summary": {
      "zh-CN": "调整编码智能体的回答格式，使行动步骤和关键信息更容易找到。",
      "en": "Adjusts coding-agent responses to make actions and key information easier to find."
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
      "zh-CN": "调整编码智能体的回答格式，使行动步骤和关键信息更容易找到。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。",
      "en": "Adjusts coding-agent responses to make actions and key information easier to find. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "8acbb618089b738404f76ac60fca1aaa995d9a87995eddf95f0b777acd7f7d2c",
      "source_url": "https://github.com/ayghri/i-have-adhd/blob/main/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "Root license reviewed. External dependencies and assets retain their individual licenses."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-10-06T22:04:52Z",
        "reviewed_at": "2026-11-16T14:58:29.135174Z",
        "url": "https://github.com/ayghri/i-have-adhd/commit/707c114cac4da1e78cbbb4f1f729121b4075de5e",
        "qualifies": true,
        "reason": {
          "zh-CN": "增加 OpenCode 新版插件 API 兼容实现。",
          "en": "Adds compatibility with the newer OpenCode plugin API."
        },
        "reviewed_files": [
          ".opencode/plugins/i-have-adhd.js",
          ".opencode/plugins/i-have-adhd.mjs",
          "tests/opencode_plugin_driver.mjs"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/ayghri/i-have-adhd",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/ayghri/i-have-adhd/blob/main/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/ayghri/i-have-adhd/blob/main/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/ayghri/i-have-adhd/commit/707c114cac4da1e78cbbb4f1f729121b4075de5e",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://www.woshipm.com/share/6473850.html",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      }
    ],
    "article_source": {
      "article_id": "2247537550_1",
      "title": "盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。",
      "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537550&idx=1&sn=29715a80ebde4036ab57651905d6bc3f",
      "published_date": "2026-10-05",
      "account": "逛逛GitHub",
      "content_review_url": "https://www.woshipm.com/share/6473850.html",
      "content_review_kind": "author-attributed public article",
      "wechat_direct_body_read": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOScw2eQ",
    "full_name": "ayghri/i-have-adhd",
    "stargazers_count": 61361,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "8acbb618089b738404f76ac60fca1aaa995d9a87995eddf95f0b777acd7f7d2c",
    "last_success_at": "2026-11-16T14:19:44.584Z"
  }
}
```
