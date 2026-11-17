# PilotDeck

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[OpenBMB/PilotDeck](https://github.com/OpenBMB/PilotDeck)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 4998 |
| 许可证 / License | AGPL-3.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:34:39.859Z |

## 中文

围绕独立工作区组织智能体任务、记忆、技能和长期运行。

### 用途与功能

- 管理多个智能体项目
- 检查和编辑项目记忆

提供工作区文件与记忆隔离、可查看的记忆处理、任务路由、MCP，以及Web、CLI与消息渠道入口。

### 环境与限制

支持Linux、macOS和Windows。源码路径要求Node22.13+且低于23，并需要适合平台的原生依赖构建工具。模型服务与渠道仍需凭据和相应费用；工作区隔离不自动等同操作系统安全沙箱。

### 开始使用

选择对应桌面发行或README的源码安装路径，配置模型后建立工作区。 参阅[官方 README](https://github.com/OpenBMB/PilotDeck/blob/main/README.md)。

### 收录与来源

具备运行后端、记忆管理和多端界面，有可安装发行包。 最近维护：[v2026.11.12](https://github.com/OpenBMB/PilotDeck/releases/tag/v2026.11.12)（2026-11-12T01:00:50Z）。正式版修复新建工作区的首次进入，以及macOS窗口拖动区域。

通过逛逛GitHub的第三方文章索引发现。索引记录了下列文章；本次未读取微信原文，不据此声称已阅读全文。

- 2026-10-15：[清华在 GitHub 上开源的 Agent 工作台，最近更新了 2.0 版本。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537716&idx=1&sn=b88d7aec28cf8cc8bbb217813d392f91)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。


补充核对作者在公开平台发布或授权发布的文章，确认署名、日期与仓库关联：

- 2026-10-16：[清华在 GitHub 上开源的 Agent 工作台，最近更新了 2.0 版本。](https://www.woshipm.com/ai/6478827.html)

## English

Organizes agent tasks, memory, skills and long-running work around separate workspaces.

### Uses and features

- Manage multiple agent projects
- Inspect and edit project memory

Provides workspace-scoped files and memory, inspectable memory processing, task routing, MCP and Web, CLI and messaging entry points.

### Requirements and limits

Supports Linux, macOS and Windows. Source use requires Node 22.13+ below 23 and suitable native build tools. Model providers and channels require credentials and may incur charges; workspace separation is not automatically an OS security sandbox.

### Getting started

Choose a desktop release or the documented source path, configure a model and create a workspace. See the [official README](https://github.com/OpenBMB/PilotDeck/blob/main/README.md).

### Review and provenance

Provides a runtime backend, memory management, multiple interfaces and installable releases. Recent maintenance: [v2026.11.12](https://github.com/OpenBMB/PilotDeck/releases/tag/v2026.11.12) (2026-11-12T01:00:50Z). The formal release fixes opening newly created onboarding workspaces and macOS window drag regions.

Discovered through a third-party index of 逛逛GitHub articles. The index records the articles below; the original WeChat pages were not read in this review. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.


Public articles published or authorized by the author were also checked for attribution, date and repository links. See the additional links in the Chinese section.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:34:39.859Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "pilotdeck",
    "name": "PilotDeck",
    "repository": "OpenBMB/PilotDeck",
    "repo_node_id": "R_kgDOSkqLzQ",
    "category": "ai",
    "tags": [],
    "forms": [
      "desktop",
      "service",
      "cli"
    ],
    "platforms": [
      "linux",
      "macos",
      "windows"
    ],
    "aliases": {
      "zh-CN": [
        "PilotDeck"
      ],
      "en": [
        "PilotDeck"
      ]
    },
    "summary": {
      "zh-CN": "围绕独立工作区组织智能体任务、记忆、技能和长期运行。",
      "en": "Organizes agent tasks, memory, skills and long-running work around separate workspaces."
    },
    "use_cases": {
      "zh-CN": [
        "管理多个智能体项目",
        "检查和编辑项目记忆"
      ],
      "en": [
        "Manage multiple agent projects",
        "Inspect and edit project memory"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:34:39.859Z",
        "en": "2026-11-16T14:34:39.859Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "AGPL-3.0",
      "osi_approved": true,
      "license_sha256": "0d96a4ff68ad6d4b6f1f30f713b18d5184912ba8dd389f86aa7710db079abcb0",
      "source_url": "https://github.com/OpenBMB/PilotDeck/blob/9e6f889832f921745089a794988321075c6a6166/LICENSE",
      "reviewed_at": "2026-11-16T14:34:39.859Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "9e6f889832f921745089a794988321075c6a6166"
    },
    "activity_evidence": [
      {
        "type": "release",
        "url": "https://github.com/OpenBMB/PilotDeck/releases/tag/v2026.11.12",
        "occurred_at": "2026-11-12T01:00:50Z",
        "reason": {
          "zh-CN": "正式版修复新建工作区的首次进入，以及macOS窗口拖动区域。",
          "en": "The formal release fixes opening newly created onboarding workspaces and macOS window drag regions."
        },
        "reviewed_at": "2026-11-16T14:34:39.859Z",
        "qualifies": true
      }
    ],
    "sources": [
      {
        "url": "https://github.com/OpenBMB/PilotDeck/blob/main/README.md",
        "accessed_at": "2026-11-16T14:34:39.859Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/OpenBMB/PilotDeck/blob/9e6f889832f921745089a794988321075c6a6166/LICENSE",
        "accessed_at": "2026-11-16T14:34:39.859Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.noking.tech/github-radar/data/library.json",
        "accessed_at": "2026-11-16T14:34:39.859Z",
        "supports": {
          "zh-CN": "第三方索引中的公众号文章归属、时间与项目发现线索；非原文阅读证据。",
          "en": "Third-party account attribution, article dates and discovery leads; not proof of reading the originals."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537716&idx=1&sn=b88d7aec28cf8cc8bbb217813d392f91",
        "accessed_at": "2026-11-16T14:34:39.859Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-10-15 清华在 GitHub 上开源的 Agent 工作台，最近更新了 2.0 版本。；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-10-15; not directly read in this review."
        }
      },
      {
        "url": "https://www.woshipm.com/ai/6478827.html",
        "accessed_at": "2026-11-16T14:26:01.125950+00:00",
        "published_date": "2026-10-16",
        "author": "逛逛GitHub",
        "supports": {
          "zh-CN": "作者公开发表或授权的文章；已核对署名、日期与仓库链接。",
          "en": "Author-published or authorized public article; attribution, date and repository links checked."
        }
      }
    ],
    "quality_review": {
      "basis": {
        "zh-CN": "具备运行后端、记忆管理和多端界面，有可安装发行包。",
        "en": "Provides a runtime backend, memory management, multiple interfaces and installable releases."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOSkqLzQ",
    "full_name": "OpenBMB/PilotDeck",
    "stargazers_count": 4998,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "AGPL-3.0",
    "license_sha256": "0d96a4ff68ad6d4b6f1f30f713b18d5184912ba8dd389f86aa7710db079abcb0",
    "last_success_at": "2026-11-16T14:19:21.792Z"
  }
}
```

</details>

