# Knowledge Work Plugins

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 36258 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:18:44.158Z |

## 中文

为知识工作提供按岗位组织的智能体技能、命令和连接器配置。

### 主要功能

- 覆盖的工作流程包括文档、分析和运营。
- 将操作说明、参考资料和连接器组合为可安装插件。

### 环境与限制

- 主要面向 Claude Cowork，部分插件适用于 Claude Code。
- 宿主订阅、业务系统账号和第三方插件各有要求与许可。

### 开始使用

从[官方说明](https://github.com/anthropics/knowledge-work-plugins/blob/main/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/anthropics/knowledge-work-plugins/releases)可用于确认版本。

### 收录复核

为知识工作提供按岗位组织的智能体技能、命令和连接器配置。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。

有效维护证据：[0c35ee357e](https://github.com/anthropics/knowledge-work-plugins/commit/0c35ee357e67e634c5f63940294f05ad97225725)，2026-11-12T20:18:21Z。修正 invoice-chase 技能实际调用的生产 Airwallex 连接器名称。该变更影响技能执行目标，不只是 README。

文章来源：[逛逛GitHub署名文章](https://www.woshipm.com/ai/6487701.html)，平台日期 2026-11-02。已通过公开正文核对仓库链接与作者归属；微信正文未直接读取。

本次为文档与实现证据复核，未安装或运行上游项目。


补充核对作者在公开平台发布或授权发布的文章，确认署名、日期与仓库关联：

- 2026-10-06：[盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。](https://www.woshipm.com/share/6473850.html)

## English

Role-oriented agent skills, commands and connector configurations for knowledge work.

### Features

- Covers document, analysis and operations workflows.
- Packages instructions, references and connectors as installable plugins.

### Requirements and limits

- Primarily targets Claude Cowork, with some plugins usable in Claude Code.
- Host subscriptions, connected business accounts and third-party plugins have separate requirements and licenses.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/anthropics/knowledge-work-plugins/blob/main/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/anthropics/knowledge-work-plugins/releases) for versions.

### Review and provenance

Role-oriented agent skills, commands and connector configurations for knowledge work. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.

Activity: [0c35ee357e](https://github.com/anthropics/knowledge-work-plugins/commit/0c35ee357e67e634c5f63940294f05ad97225725), 2026-11-12T20:18:21Z. Corrects the production Airwallex connector used by the invoice-chase skill, changing its execution target rather than only the README.

Discovery: [an author-attributed 逛逛GitHub article](https://www.woshipm.com/ai/6487701.html), dated 2026-11-02 on the public platform. Repository links and attribution were checked in its public body; the WeChat body was not read directly.

This review covers documentation and implementation evidence. The upstream project was not installed or run.


Public articles published or authorized by the author were also checked for attribution, date and repository links. See the additional links in the Chinese section.

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
    "id": "knowledge-work-plugins",
    "name": "Knowledge Work Plugins",
    "repository": "anthropics/knowledge-work-plugins",
    "repo_node_id": "R_kgDOQ_-q4g",
    "category": "productivity",
    "summary": {
      "zh-CN": "为知识工作提供按岗位组织的智能体技能、命令和连接器配置。",
      "en": "Role-oriented agent skills, commands and connector configurations for knowledge work."
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
      "zh-CN": "为知识工作提供按岗位组织的智能体技能、命令和连接器配置。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。",
      "en": "Role-oriented agent skills, commands and connector configurations for knowledge work. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "a6946284993aeec75c7d75906064b66210c46051e562077efb30eb6dcfe72e26",
      "source_url": "https://github.com/anthropics/knowledge-work-plugins/blob/e91a134584eb798bac7fb0379358006a2b63b965/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "Root license reviewed. External dependencies and assets retain their individual licenses.",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "e91a134584eb798bac7fb0379358006a2b63b965"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-12T20:18:21Z",
        "reviewed_at": "2026-11-16T14:58:29.135174Z",
        "url": "https://github.com/anthropics/knowledge-work-plugins/commit/0c35ee357e67e634c5f63940294f05ad97225725",
        "qualifies": true,
        "reason": {
          "zh-CN": "修正 invoice-chase 技能实际调用的生产 Airwallex 连接器名称。该变更影响技能执行目标，不只是 README。",
          "en": "Corrects the production Airwallex connector used by the invoice-chase skill, changing its execution target rather than only the README."
        },
        "reviewed_files": [
          "small-business/skills/invoice-chase/SKILL.md"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/anthropics/knowledge-work-plugins",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/anthropics/knowledge-work-plugins/blob/main/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/anthropics/knowledge-work-plugins/blob/e91a134584eb798bac7fb0379358006a2b63b965/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/anthropics/knowledge-work-plugins/commit/0c35ee357e67e634c5f63940294f05ad97225725",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://www.woshipm.com/ai/6487701.html",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
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
    "repo_node_id": "R_kgDOQ_-q4g",
    "full_name": "anthropics/knowledge-work-plugins",
    "stargazers_count": 36258,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "a6946284993aeec75c7d75906064b66210c46051e562077efb30eb6dcfe72e26",
    "last_success_at": "2026-11-16T14:18:44.158Z"
  }
}
```

</details>
