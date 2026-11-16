# Worktrunk

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 12565 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:34:39.906Z |

## 中文

简化 Git worktree 的切换、查看和清理，支持并行编码任务。

### 用途与功能

- 管理多个已有工作目录
- 查看并行任务与分支状态

提供worktree列表、切换、hooks和任务状态接入；强制删除前可创建有限范围的恢复备份。

### 环境与限制

依赖Git及Shell集成；Windows的wt命令可能与Windows Terminal冲突，可用git-wt。强制删除备份不包含忽略文件、子模块内部变化或独立暂存版本。分支与目录操作应遵循工程授权。上游提供MIT或Apache双许可，本次核对Apache文本。

### 开始使用

按系统安装CLI并配置Shell集成，先用list查看现有worktree。 参阅[官方 README](https://github.com/max-sixty/worktrunk/blob/main/README.md)。

### 收录与来源

实现worktree状态、生命周期与恢复操作，适合多任务开发。 最近维护：[v0.82.0](https://github.com/max-sixty/worktrunk/releases/tag/v0.82.0)（2026-11-14T21:20:53Z）。正式版加入强制移除前的备份，并修复平台和hook处理。

通过逛逛GitHub的第三方文章索引发现。索引记录了下列文章；本次未读取微信原文，不据此声称已阅读全文。

- 2026-10-05：[盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537550&idx=1&sn=29715a80ebde4036ab57651905d6bc3f)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。


补充核对作者在公开平台发布或授权发布的文章，确认署名、日期与仓库关联：

- 2026-10-06：[盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。](https://www.woshipm.com/share/6473850.html)

## English

Simplifies switching, inspecting and removing Git worktrees for parallel coding tasks.

### Uses and features

- Manage multiple working directories
- Inspect parallel task and branch state

Provides worktree listing, switching, hooks and task-status integration, with scoped recovery backups before forced removal.

### Requirements and limits

Depends on Git and shell integration. On Windows, wt may conflict with Windows Terminal; git-wt is available. Forced-removal backups exclude ignored files, changes inside submodules and separate staged versions. Follow project authorization for branch and directory operations. Upstream offers MIT or Apache; this review checks the Apache text.

### Getting started

Install the CLI and shell integration for your system, then inspect existing worktrees with list. See the [official README](https://github.com/max-sixty/worktrunk/blob/main/README.md).

### Review and provenance

Implements worktree status, lifecycle and recovery operations for concurrent development. Recent maintenance: [v0.82.0](https://github.com/max-sixty/worktrunk/releases/tag/v0.82.0) (2026-11-14T21:20:53Z). The formal release adds backups before forced removal and improves platform and hook handling.

Discovered through a third-party index of 逛逛GitHub articles. The index records the articles below; the original WeChat pages were not read in this review. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.


Public articles published or authorized by the author were also checked for attribution, date and repository links. See the additional links in the Chinese section.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:34:39.906Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "worktrunk",
    "name": "Worktrunk",
    "repository": "max-sixty/worktrunk",
    "repo_node_id": "R_kgDOQEkLnw",
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
        "Worktrunk"
      ],
      "en": [
        "Worktrunk"
      ]
    },
    "summary": {
      "zh-CN": "简化 Git worktree 的切换、查看和清理，支持并行编码任务。",
      "en": "Simplifies switching, inspecting and removing Git worktrees for parallel coding tasks."
    },
    "use_cases": {
      "zh-CN": [
        "管理多个已有工作目录",
        "查看并行任务与分支状态"
      ],
      "en": [
        "Manage multiple working directories",
        "Inspect parallel task and branch state"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:34:39.906Z",
        "en": "2026-11-16T14:34:39.906Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "e1e07ba86c3e6d2760efbbfbaec4ebeaac590f7d3fd885d622e1cdc2f92c20fc",
      "source_url": "https://github.com/max-sixty/worktrunk/blob/main/LICENSE-APACHE",
      "reviewed_at": "2026-11-16T14:34:39.906Z"
    },
    "activity_evidence": [
      {
        "type": "release",
        "url": "https://github.com/max-sixty/worktrunk/releases/tag/v0.82.0",
        "occurred_at": "2026-11-14T21:20:53Z",
        "reason": {
          "zh-CN": "正式版加入强制移除前的备份，并修复平台和hook处理。",
          "en": "The formal release adds backups before forced removal and improves platform and hook handling."
        },
        "reviewed_at": "2026-11-16T14:34:39.906Z",
        "qualifies": true
      }
    ],
    "sources": [
      {
        "url": "https://github.com/max-sixty/worktrunk/blob/main/README.md",
        "accessed_at": "2026-11-16T14:34:39.906Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/max-sixty/worktrunk/blob/main/LICENSE-APACHE",
        "accessed_at": "2026-11-16T14:34:39.906Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.noking.tech/github-radar/data/library.json",
        "accessed_at": "2026-11-16T14:34:39.906Z",
        "supports": {
          "zh-CN": "第三方索引中的公众号文章归属、时间与项目发现线索；非原文阅读证据。",
          "en": "Third-party account attribution, article dates and discovery leads; not proof of reading the originals."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537550&idx=1&sn=29715a80ebde4036ab57651905d6bc3f",
        "accessed_at": "2026-11-16T14:34:39.906Z",
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
        "zh-CN": "实现worktree状态、生命周期与恢复操作，适合多任务开发。",
        "en": "Implements worktree status, lifecycle and recovery operations for concurrent development."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOQEkLnw",
    "full_name": "max-sixty/worktrunk",
    "stargazers_count": 12565,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "e1e07ba86c3e6d2760efbbfbaec4ebeaac590f7d3fd885d622e1cdc2f92c20fc",
    "last_success_at": "2026-11-16T14:19:44.212Z"
  }
}
```

</details>

