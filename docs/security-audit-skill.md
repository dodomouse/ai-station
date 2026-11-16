# Security Audit Skill

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 73608 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:18:44.115Z |

## 中文

组织源码安全审计，并用脚本检查覆盖记录和结构化发现。

### 主要功能

- 分阶段检查入口、边界、候选问题和独立复核。
- 输出可追溯的发现记录，并验证 JSON 结构与关联字段。

### 环境与限制

- 需要支持工具调用的编码智能体、Node.js 和适用的沙箱。
- 仅在获授权的源码范围使用，报告仍需人工确认。

### 开始使用

从[官方说明](https://github.com/cloudflare/security-audit-skill/blob/main/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/cloudflare/security-audit-skill/releases)可用于确认版本。

### 收录复核

组织源码安全审计，并用脚本检查覆盖记录和结构化发现。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。

有效维护证据：[158eb44803](https://github.com/cloudflare/security-audit-skill/commit/158eb448038e65f05bc5f2ba36c7e981e6890cea)，2026-09-10T10:11:38Z。增加覆盖台账校验，并重做发现结构验证器。

文章来源：[逛逛GitHub署名文章](https://www.woshipm.com/ai/6487701.html)，平台日期 2026-11-02。已通过公开正文核对仓库链接与作者归属；微信正文未直接读取。

本次为文档与实现证据复核，未安装或运行上游项目。

## English

A source-security audit skill with validators for coverage records and structured findings.

### Features

- Organizes entry-point review, boundary analysis, candidate verification and independent review.
- Produces traceable findings and validates JSON structure and linked fields.

### Requirements and limits

- Requires a tool-capable coding agent, Node.js and an appropriate sandbox.
- Use on authorized source code and review the findings manually.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/cloudflare/security-audit-skill/blob/main/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/cloudflare/security-audit-skill/releases) for versions.

### Review and provenance

A source-security audit skill with validators for coverage records and structured findings. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.

Activity: [158eb44803](https://github.com/cloudflare/security-audit-skill/commit/158eb448038e65f05bc5f2ba36c7e981e6890cea), 2026-09-10T10:11:38Z. Adds coverage-ledger validation and revises findings-contract validators.

Discovery: [an author-attributed 逛逛GitHub article](https://www.woshipm.com/ai/6487701.html), dated 2026-11-02 on the public platform. Repository links and attribution were checked in its public body; the WeChat body was not read directly.

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
    "id": "security-audit-skill",
    "name": "Security Audit Skill",
    "repository": "cloudflare/security-audit-skill",
    "repo_node_id": "R_kgDOS-b1TA",
    "category": "development",
    "summary": {
      "zh-CN": "组织源码安全审计，并用脚本检查覆盖记录和结构化发现。",
      "en": "A source-security audit skill with validators for coverage records and structured findings."
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
      "zh-CN": "组织源码安全审计，并用脚本检查覆盖记录和结构化发现。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。",
      "en": "A source-security audit skill with validators for coverage records and structured findings. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "e598e694aa506650c7192d5ea3be0e50aca0d356ea00551c53429f0b01eb6391",
      "source_url": "https://github.com/cloudflare/security-audit-skill/blob/main/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "Root license reviewed. External dependencies and assets retain their individual licenses."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-09-10T10:11:38Z",
        "reviewed_at": "2026-11-16T14:58:29.135174Z",
        "url": "https://github.com/cloudflare/security-audit-skill/commit/158eb448038e65f05bc5f2ba36c7e981e6890cea",
        "qualifies": true,
        "reason": {
          "zh-CN": "增加覆盖台账校验，并重做发现结构验证器。",
          "en": "Adds coverage-ledger validation and revises findings-contract validators."
        },
        "reviewed_files": [
          "skills/security-audit/validate-coverage-ledger.cjs",
          "skills/security-audit/validate-coverage-ledger.test.cjs",
          "skills/security-audit/validate-findings.cjs"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/cloudflare/security-audit-skill",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/cloudflare/security-audit-skill/blob/main/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/cloudflare/security-audit-skill/blob/main/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/cloudflare/security-audit-skill/commit/158eb448038e65f05bc5f2ba36c7e981e6890cea",
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
    "repo_node_id": "R_kgDOS-b1TA",
    "full_name": "cloudflare/security-audit-skill",
    "stargazers_count": 73608,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "e598e694aa506650c7192d5ea3be0e50aca0d356ea00551c53429f0b01eb6391",
    "last_success_at": "2026-11-16T14:18:44.115Z"
  }
}
```
