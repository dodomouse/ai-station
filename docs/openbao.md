# OpenBao

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[openbao/openbao](https://github.com/openbao/openbao)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 部署与运维 / Deployment and operations |
| 状态 / Status | 已收录 / Included |
| Star | 9049 |
| 许可证 / License | MPL-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:47:41.365Z |

## 中文

集中保存和分发机密、证书与密钥，并管理访问、租约和撤销。

### 用途与功能

- 管理应用机密与动态凭据

提供加密持久化、动态机密、加解密接口、租约续期和撤销；支持多种存储与认证后端。

### 环境与限制

部署需要正确配置身份、策略、存储、备份和恢复。源码编译需要 Go，版本以仓库固定工具链为准。生产可靠性和密钥管理需结合部署设计，本次未审计安全性。

### 开始使用

从官方文档开始本地开发实例，再按生产部署指南配置持久化与权限。 参阅[官方 README](https://github.com/openbao/openbao/blob/main/README.md)。

### 收录与来源

包含机密生命周期、后端与审计相关实现，并持续发行安全修复。 最近维护：[v2.7.2](https://github.com/openbao/openbao/releases/tag/v2.7.2)（2026-10-26T20:24:37Z）。正式版修复路径规范化、OIDC客户端条件和SSH证书模板限制。

通过逛逛GitHub的第三方文章索引发现。索引记录了下列文章；本次未读取微信原文，不据此声称已阅读全文。

- 2026-09-27：[推荐 8 个最近火火火火的开源项目，登上 GitHub 今日热榜。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537385&idx=1&sn=6f57abbd0554d6288c4aa1b3566ef704)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。


补充核对作者在公开平台发布或授权发布的文章，确认署名、日期与仓库关联：

- 2026-09-28：[推荐 8 个最近火火火火的开源项目，登上 GitHub 今日热榜。](https://www.woshipm.com/share/6470709.html)

## English

Centrally stores and distributes secrets, certificates and keys with access, lease and revocation management.

### Uses and features

- Manage application secrets and dynamic credentials

Provides encrypted persistence, dynamic secrets, encryption APIs, lease renewal and revocation across storage and authentication backends.

### Requirements and limits

As an infrastructure service it requires correct identity, policy, storage, backup and recovery configuration. Development uses Go with the repository's pinned toolchain. Production reliability and key management depend on deployment design; no security audit was performed here.

### Getting started

Start with a local development instance from the official docs, then follow production guidance for persistence and permissions. See the [official README](https://github.com/openbao/openbao/blob/main/README.md).

### Review and provenance

Implements secret lifecycle and backend functionality with ongoing security-fix releases. Recent maintenance: [v2.7.2](https://github.com/openbao/openbao/releases/tag/v2.7.2) (2026-10-26T20:24:37Z). The formal release fixes path canonicalization, OIDC client conditions and SSH certificate template restrictions.

Discovered through a third-party index of 逛逛GitHub articles. The index records the articles below; the original WeChat pages were not read in this review. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.


Public articles published or authorized by the author were also checked for attribution, date and repository links. See the additional links in the Chinese section.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:47:41.365Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "openbao",
    "name": "OpenBao",
    "repository": "openbao/openbao",
    "repo_node_id": "R_kgDOKrhEtA",
    "category": "operations",
    "tags": [],
    "forms": [
      "service",
      "cli"
    ],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "OpenBao"
      ],
      "en": [
        "OpenBao"
      ]
    },
    "summary": {
      "zh-CN": "集中保存和分发机密、证书与密钥，并管理访问、租约和撤销。",
      "en": "Centrally stores and distributes secrets, certificates and keys with access, lease and revocation management."
    },
    "use_cases": {
      "zh-CN": [
        "管理应用机密与动态凭据"
      ],
      "en": [
        "Manage application secrets and dynamic credentials"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:47:41.365Z",
        "en": "2026-11-16T14:47:41.365Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MPL-2.0",
      "osi_approved": true,
      "license_sha256": "d6b1a865f1c8c697d343bd4e0ce61025f91898486a1f00d727f32e8644af77d3",
      "source_url": "https://github.com/openbao/openbao/blob/main/LICENSE",
      "reviewed_at": "2026-11-16T14:47:41.365Z"
    },
    "activity_evidence": [
      {
        "type": "release",
        "url": "https://github.com/openbao/openbao/releases/tag/v2.7.2",
        "occurred_at": "2026-10-26T20:24:37Z",
        "reason": {
          "zh-CN": "正式版修复路径规范化、OIDC客户端条件和SSH证书模板限制。",
          "en": "The formal release fixes path canonicalization, OIDC client conditions and SSH certificate template restrictions."
        },
        "reviewed_at": "2026-11-16T14:47:41.365Z",
        "qualifies": true
      }
    ],
    "sources": [
      {
        "url": "https://github.com/openbao/openbao/blob/main/README.md",
        "accessed_at": "2026-11-16T14:47:41.365Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/openbao/openbao/blob/main/LICENSE",
        "accessed_at": "2026-11-16T14:47:41.365Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.noking.tech/github-radar/data/library.json",
        "accessed_at": "2026-11-16T14:47:41.365Z",
        "supports": {
          "zh-CN": "第三方索引中的公众号文章归属、时间与项目发现线索；非原文阅读证据。",
          "en": "Third-party account attribution, article dates and discovery leads; not proof of reading the originals."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537385&idx=1&sn=6f57abbd0554d6288c4aa1b3566ef704",
        "accessed_at": "2026-11-16T14:47:41.365Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-09-27 推荐 8 个最近火火火火的开源项目，登上 GitHub 今日热榜。；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-09-27; not directly read in this review."
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
        "zh-CN": "包含机密生命周期、后端与审计相关实现，并持续发行安全修复。",
        "en": "Implements secret lifecycle and backend functionality with ongoing security-fix releases."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOKrhEtA",
    "full_name": "openbao/openbao",
    "stargazers_count": 9049,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MPL-2.0",
    "license_sha256": "d6b1a865f1c8c697d343bd4e0ce61025f91898486a1f00d727f32e8644af77d3",
    "last_success_at": "2026-11-16T14:20:00.344Z"
  }
}
```

</details>

