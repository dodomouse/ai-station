# AX

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[google/ax](https://github.com/google/ax)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 自动化 / Automation |
| 状态 / Status | 已收录 / Included |
| Star | 14733 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:20:00.109Z |

## 中文

用声明式配置调度沙箱中的智能体任务和工作区。

### 主要功能

- 定义任务、模型配置与代码工作区。
- 提供任务状态查询和运行环境调试入口。

### 环境与限制

- 需要 Kubernetes、可用的 Agent Substrate 和容器镜像工具。
- 项目仍在快速开发，协议和 API 可能发生不兼容变化。

### 开始使用

从[官方说明](https://github.com/google/ax/blob/main/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/google/ax/releases)可用于确认版本。

### 收录复核

用声明式配置调度沙箱中的智能体任务和工作区。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。

有效维护证据：[v0.3.1](https://github.com/google/ax/releases/tag/v0.3.1)，2026-09-25T13:25:21Z。修复 CLI 使用复数资源名时忽略指定名称、错误列出全部资源的问题，并增加别名测试。 2026-11-17 已读取[实现提交](https://github.com/google/ax/commit/6015f79106589f979ff5162242d4dfdead8dd77c)的差异；未运行上游测试。

文章来源：[逛逛GitHub署名文章](https://www.woshipm.com/share/6470709.html)，平台日期 2026-09-28。已通过公开正文核对仓库链接与作者归属；微信正文未直接读取。

本次为文档与实现证据复核，未安装或运行上游项目。

## English

A declarative orchestrator for sandboxed agent tasks and workspaces.

### Features

- Defines tasks, model profiles and code workspaces.
- Provides task inspection and debugging access to execution environments.

### Requirements and limits

- Requires Kubernetes, a working Agent Substrate and container-image tools.
- The project remains under active development, and protocols and APIs may change incompatibly.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/google/ax/blob/main/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/google/ax/releases) for versions.

### Review and provenance

A declarative orchestrator for sandboxed agent tasks and workspaces. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.

Activity: [v0.3.1](https://github.com/google/ax/releases/tag/v0.3.1), 2026-09-25T13:25:21Z. Fixes plural CLI resource aliases ignoring the requested name and listing all resources, with alias tests. On 2026-11-17, the [implementation diff](https://github.com/google/ax/commit/6015f79106589f979ff5162242d4dfdead8dd77c) was inspected; upstream tests were not run.

Discovery: [an author-attributed 逛逛GitHub article](https://www.woshipm.com/share/6470709.html), dated 2026-09-28 on the public platform. Repository links and attribution were checked in its public body; the WeChat body was not read directly.

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
    "id": "google-ax",
    "name": "AX",
    "repository": "google/ax",
    "repo_node_id": "R_kgDOR1BXBQ",
    "category": "automation",
    "summary": {
      "zh-CN": "用声明式配置调度沙箱中的智能体任务和工作区。",
      "en": "A declarative orchestrator for sandboxed agent tasks and workspaces."
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
      "zh-CN": "用声明式配置调度沙箱中的智能体任务和工作区。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。",
      "en": "A declarative orchestrator for sandboxed agent tasks and workspaces. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
      "source_url": "https://github.com/google/ax/blob/8b1c2e915426da5128dc6c592c738c604214ba29/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "Root license reviewed. External dependencies and assets retain their individual licenses.",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "8b1c2e915426da5128dc6c592c738c604214ba29"
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-09-25T13:25:21Z",
        "reviewed_at": "2026-11-17T03:15:51.892548+00:00",
        "url": "https://github.com/google/ax/releases/tag/v0.3.1",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复 CLI 使用复数资源名时忽略指定名称、错误列出全部资源的问题，并增加别名测试。",
          "en": "Fixes plural CLI resource aliases ignoring the requested name and listing all resources, with alias tests."
        },
        "draft": false,
        "prerelease": false,
        "implementation_evidence": {
          "type": "commit",
          "url": "https://github.com/google/ax/commit/6015f79106589f979ff5162242d4dfdead8dd77c",
          "sha": "6015f79106589f979ff5162242d4dfdead8dd77c",
          "occurred_at": "2026-09-25T13:10:24Z",
          "reviewed_at": "2026-11-17T03:15:51.892548+00:00",
          "reviewed_files": [
            "cmd/ax/main.go",
            "cmd/ax/main_test.go"
          ],
          "verification_level": "source_review",
          "upstream_tests_run": false
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/google/ax",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/google/ax/blob/main/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/google/ax/blob/8b1c2e915426da5128dc6c592c738c604214ba29/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/google/ax/releases/tag/v0.3.1",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://www.woshipm.com/share/6470709.html",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      }
    ],
    "article_source": {
      "article_id": "2247537385_1",
      "title": "推荐 8 个最近火火火火的开源项目，登上 GitHub 今日热榜。",
      "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537385&idx=1&sn=6f57abbd0554d6288c4aa1b3566ef704",
      "published_date": "2026-09-27",
      "account": "逛逛GitHub",
      "content_review_url": "https://www.woshipm.com/share/6470709.html",
      "content_review_kind": "author-attributed public article",
      "wechat_direct_body_read": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOR1BXBQ",
    "full_name": "google/ax",
    "stargazers_count": 14733,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
    "last_success_at": "2026-11-16T14:20:00.109Z"
  }
}
```

</details>
