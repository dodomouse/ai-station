# JumpServer

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[jumpserver/jumpserver](https://github.com/jumpserver/jumpserver)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 部署与运维 / Deployment and operations |
| 状态 / Status | 已收录 / Included |
| Star | 31970 |
| 许可证 / License | GPL-3.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:20:00.701Z |

## 中文

集中管理服务器、数据库和其他基础设施的特权访问与审计。

### 主要功能

- 统一连接多类资源，包括 SSH、RDP、Kubernetes 和数据库。
- 提供身份、权限、会话记录和审计功能。

### 环境与限制

- 官方快速部署要求干净的 64 位 Linux 主机，至少 4 核 CPU 与 8 GB 内存。
- 社区版与企业版功能不同，应按维护周期选择发行系列。

### 开始使用

从[官方说明](https://github.com/jumpserver/jumpserver/blob/dev/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/jumpserver/jumpserver/releases)可用于确认版本。

### 收录复核

集中管理服务器、数据库和其他基础设施的特权访问与审计。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。

有效维护证据：[v3.10.24](https://github.com/jumpserver/jumpserver/releases/tag/v3.10.24)，2026-10-27T09:56:32Z。已核对正式发行 v3.10.24 的发布状态与时间。

文章来源：[逛逛GitHub署名文章](https://www.woshipm.com/share/6471994.html)，平台日期 2026-09-30。已通过公开正文核对仓库链接与作者归属；微信正文未直接读取。

本次为文档与实现证据复核，未安装或运行上游项目。

## English

A platform for managing and auditing privileged access to servers, databases and infrastructure.

### Features

- Unifies access to SSH, RDP, Kubernetes, databases and other resources.
- Provides identity, permissions, session recording and auditing.

### Requirements and limits

- The quickstart requires a clean 64-bit Linux host with at least 4 CPU cores and 8 GB RAM.
- Community and enterprise features differ
- choose a supported release series.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/jumpserver/jumpserver/blob/dev/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/jumpserver/jumpserver/releases) for versions.

### Review and provenance

A platform for managing and auditing privileged access to servers, databases and infrastructure. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.

Activity: [v3.10.24](https://github.com/jumpserver/jumpserver/releases/tag/v3.10.24), 2026-10-27T09:56:32Z. Checked the non-draft, non-prerelease publication v3.10.24 and its date.

Discovery: [an author-attributed 逛逛GitHub article](https://www.woshipm.com/share/6471994.html), dated 2026-09-30 on the public platform. Repository links and attribution were checked in its public body; the WeChat body was not read directly.

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
    "id": "jumpserver",
    "name": "JumpServer",
    "repository": "jumpserver/jumpserver",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkyMTQ4NDc4MQ==",
    "category": "operations",
    "summary": {
      "zh-CN": "集中管理服务器、数据库和其他基础设施的特权访问与审计。",
      "en": "A platform for managing and auditing privileged access to servers, databases and infrastructure."
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
      "zh-CN": "集中管理服务器、数据库和其他基础设施的特权访问与审计。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。",
      "en": "A platform for managing and auditing privileged access to servers, databases and infrastructure. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "GPL-3.0",
      "osi_approved": true,
      "license_sha256": "e57f1c320b8cf8798a7d2ff83a6f9e06a33a03585f6e065fea97f1d86db84052",
      "source_url": "https://github.com/jumpserver/jumpserver/blob/dev/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "Root license reviewed. External dependencies and assets retain their individual licenses."
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-10-27T09:56:32Z",
        "reviewed_at": "2026-11-16T14:58:29.135174Z",
        "url": "https://github.com/jumpserver/jumpserver/releases/tag/v3.10.24",
        "qualifies": true,
        "reason": {
          "zh-CN": "已核对正式发行 v3.10.24 的发布状态与时间。",
          "en": "Checked the non-draft, non-prerelease publication v3.10.24 and its date."
        },
        "draft": false,
        "prerelease": false
      }
    ],
    "sources": [
      {
        "url": "https://github.com/jumpserver/jumpserver",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/jumpserver/jumpserver/blob/dev/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/jumpserver/jumpserver/blob/dev/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/jumpserver/jumpserver/releases/tag/v3.10.24",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://www.woshipm.com/share/6471994.html",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      }
    ],
    "article_source": {
      "article_id": "2247537439_1",
      "title": "GitHub 3.1 万 Star！开源堡垒机 JumpServer 正式进入 V5 时代。",
      "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537439&idx=1&sn=b9a163563c14af097e993f47703ba2a7",
      "published_date": "2026-09-29",
      "account": "逛逛GitHub",
      "content_review_url": "https://www.woshipm.com/share/6471994.html",
      "content_review_kind": "author-attributed public article",
      "wechat_direct_body_read": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkyMTQ4NDc4MQ==",
    "full_name": "jumpserver/jumpserver",
    "stargazers_count": 31970,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "GPL-3.0",
    "license_sha256": "e57f1c320b8cf8798a7d2ff83a6f9e06a33a03585f6e065fea97f1d86db84052",
    "last_success_at": "2026-11-16T14:20:00.701Z"
  }
}
```
