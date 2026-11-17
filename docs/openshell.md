# OpenShell

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 部署与运维 / Deployment and operations |
| 状态 / Status | 已收录 / Included |
| Star | 21676 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:34:39.604Z |

## 中文

为智能体提供隔离运行环境，按策略控制文件、网络和凭据访问。

### 用途与功能

- 为自动化智能体限制运行权限

实现内核级隔离、网络出口检查、按目标注入凭据，以及策略变更分析和扩展接口。

### 环境与限制

需 Linux、Apple Silicon macOS 或实验性 WSL2，配合 Docker、Podman 或宿主虚拟化。原生Windows路径另有分支说明。沙箱能力受平台、配置和应用兼容性影响，不能推断为绝对安全。

### 开始使用

按支持矩阵选择运行方式，再创建最小权限的测试环境。 参阅[官方 README](https://github.com/NVIDIA/OpenShell/blob/main/README.md)。

### 收录与来源

包含隔离运行时、策略执行和凭据路由代码，并提供平台文档。 最近维护：[v0.1.8](https://github.com/NVIDIA/OpenShell/releases/tag/v0.1.8)（2026-11-10T18:14:42Z）。正式版修复凭据放置与HTTP升级策略，明确升级顺序和配置变化。

通过逛逛GitHub的第三方文章索引发现。索引记录了下列文章；本次未读取微信原文，不据此声称已阅读全文。

- 2026-10-27：[盘点 3 个安全相关的开源 Skill，都是最近登上热榜的。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538101&idx=2&sn=078856eda8d5566656a5ef45fdd0f971)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。

## English

Provides isolated agent runtimes with policy controls for files, networking and credentials.

### Uses and features

- Constrain permissions for autonomous agents

Implements kernel isolation, network egress checks, endpoint-bound credential injection, policy-change analysis and extension interfaces.

### Requirements and limits

Requires Linux, Apple Silicon macOS or experimental WSL2, with Docker, Podman or host virtualization. Native Windows has a separate branch guide. Isolation depends on platform, policy and application compatibility and is not an absolute safety guarantee.

### Getting started

Choose a runtime from the support matrix and start with a minimally privileged test environment. See the [official README](https://github.com/NVIDIA/OpenShell/blob/main/README.md).

### Review and provenance

Includes isolation, policy enforcement and credential-routing implementation with platform documentation. Recent maintenance: [v0.1.8](https://github.com/NVIDIA/OpenShell/releases/tag/v0.1.8) (2026-11-10T18:14:42Z). The formal release fixes credential placement and HTTP upgrade policy and documents upgrade order and configuration changes.

Discovered through a third-party index of 逛逛GitHub articles. The index records the articles below; the original WeChat pages were not read in this review. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:34:39.604Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "openshell",
    "name": "OpenShell",
    "repository": "NVIDIA/OpenShell",
    "repo_node_id": "R_kgDORYG5fg",
    "category": "operations",
    "tags": [],
    "forms": [
      "cli",
      "service"
    ],
    "platforms": [
      "linux",
      "macos",
      "windows"
    ],
    "aliases": {
      "zh-CN": [
        "OpenShell"
      ],
      "en": [
        "OpenShell"
      ]
    },
    "summary": {
      "zh-CN": "为智能体提供隔离运行环境，按策略控制文件、网络和凭据访问。",
      "en": "Provides isolated agent runtimes with policy controls for files, networking and credentials."
    },
    "use_cases": {
      "zh-CN": [
        "为自动化智能体限制运行权限"
      ],
      "en": [
        "Constrain permissions for autonomous agents"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:34:39.604Z",
        "en": "2026-11-16T14:34:39.604Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "d07c0367e2861e7fe70fa1b679f879f4fa2f9138ade4457d44ecf8b2e135bb45",
      "source_url": "https://github.com/NVIDIA/OpenShell/blob/bdb8be39312fc77c9dd9c3b760fd90c59354391b/LICENSE",
      "reviewed_at": "2026-11-16T14:34:39.604Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "bdb8be39312fc77c9dd9c3b760fd90c59354391b"
    },
    "activity_evidence": [
      {
        "type": "release",
        "url": "https://github.com/NVIDIA/OpenShell/releases/tag/v0.1.8",
        "occurred_at": "2026-11-10T18:14:42Z",
        "reason": {
          "zh-CN": "正式版修复凭据放置与HTTP升级策略，明确升级顺序和配置变化。",
          "en": "The formal release fixes credential placement and HTTP upgrade policy and documents upgrade order and configuration changes."
        },
        "reviewed_at": "2026-11-16T14:34:39.604Z",
        "qualifies": true
      }
    ],
    "sources": [
      {
        "url": "https://github.com/NVIDIA/OpenShell/blob/main/README.md",
        "accessed_at": "2026-11-16T14:34:39.604Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/NVIDIA/OpenShell/blob/bdb8be39312fc77c9dd9c3b760fd90c59354391b/LICENSE",
        "accessed_at": "2026-11-16T14:34:39.604Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.noking.tech/github-radar/data/library.json",
        "accessed_at": "2026-11-16T14:34:39.604Z",
        "supports": {
          "zh-CN": "第三方索引中的公众号文章归属、时间与项目发现线索；非原文阅读证据。",
          "en": "Third-party account attribution, article dates and discovery leads; not proof of reading the originals."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538101&idx=2&sn=078856eda8d5566656a5ef45fdd0f971",
        "accessed_at": "2026-11-16T14:34:39.604Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-10-27 盘点 3 个安全相关的开源 Skill，都是最近登上热榜的。；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-10-27; not directly read in this review."
        }
      }
    ],
    "quality_review": {
      "basis": {
        "zh-CN": "包含隔离运行时、策略执行和凭据路由代码，并提供平台文档。",
        "en": "Includes isolation, policy enforcement and credential-routing implementation with platform documentation."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDORYG5fg",
    "full_name": "NVIDIA/OpenShell",
    "stargazers_count": 21676,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "d07c0367e2861e7fe70fa1b679f879f4fa2f9138ade4457d44ecf8b2e135bb45",
    "last_success_at": "2026-11-16T14:19:06.417Z"
  }
}
```

</details>

