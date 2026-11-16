# OpenHands

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[OpenHands/OpenHands](https://github.com/OpenHands/OpenHands)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 93582 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:58:29.135174Z |

## 中文

用于软件开发任务的智能体工作台，提供会话、工具执行与变更审查。

### 主要功能

- 支持配置模型和开发工作区。
- 提供自托管界面、自动化入口及执行环境集成。

### 环境与限制

- 按官方部署指南准备运行环境与模型账号。
- 智能体可修改文件或执行工具，需要为工作区设置合适权限和资源限制。

### 开始使用

从[官方说明](https://github.com/OpenHands/OpenHands/blob/main/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/OpenHands/OpenHands/releases)可用于确认版本。

### 收录复核

用于软件开发任务的智能体工作台，提供会话、工具执行与变更审查。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。

有效维护证据：[v1.40.0](https://github.com/OpenHands/OpenHands/releases/tag/v1.40.0)，2026-11-12T14:22:00Z。已核对正式发行 v1.40.0 的发布状态与时间。

发现线索：[公开索引](https://www.noking.tech/github-radar/)记录的[微信文章](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537495&idx=1&sn=803c312533d9b69a993cfa4e89cc5ee2)，索引日期 2026-10-03。仅核对公开索引，未直接读取该篇微信全文；功能与限制以上游资料为依据。

本次为文档与实现证据复核，未安装或运行上游项目。

## English

An agent workspace for software development with conversations, tool execution and change review.

### Features

- Supports configurable models and development workspaces.
- Provides a self-hosted interface, automation entry points and execution-environment integrations.

### Requirements and limits

- Prepare the runtime and model account using the official deployment guide.
- Agents can modify files and execute tools, so configure workspace permissions and resource limits.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/OpenHands/OpenHands/blob/main/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/OpenHands/OpenHands/releases) for versions.

### Review and provenance

An agent workspace for software development with conversations, tool execution and change review. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.

Activity: [v1.40.0](https://github.com/OpenHands/OpenHands/releases/tag/v1.40.0), 2026-11-12T14:22:00Z. Checked the non-draft, non-prerelease publication v1.40.0 and its date.

Discovery: [an indexed WeChat article](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537495&idx=1&sn=803c312533d9b69a993cfa4e89cc5ee2). This is a secondary discovery record; the WeChat article body was not read. Features and limits come from upstream documentation.

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
    "id": "openhands",
    "name": "OpenHands",
    "repository": "OpenHands/OpenHands",
    "repo_node_id": "R_kgDOLfkiww",
    "category": "ai",
    "summary": {
      "zh-CN": "用于软件开发任务的智能体工作台，提供会话、工具执行与变更审查。",
      "en": "An agent workspace for software development with conversations, tool execution and change review."
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
      "zh-CN": "用于软件开发任务的智能体工作台，提供会话、工具执行与变更审查。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。",
      "en": "An agent workspace for software development with conversations, tool execution and change review. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "e1d1fa9f3a8d7bef24449d488fcd8f00f8f272cac297bb9bed161eb6175b876a",
      "source_url": "https://github.com/OpenHands/OpenHands/blob/main/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "Root license reviewed. External dependencies and assets retain their individual licenses."
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-11-12T14:22:00Z",
        "reviewed_at": "2026-11-16T14:58:29.135174Z",
        "url": "https://github.com/OpenHands/OpenHands/releases/tag/v1.40.0",
        "qualifies": true,
        "reason": {
          "zh-CN": "已核对正式发行 v1.40.0 的发布状态与时间。",
          "en": "Checked the non-draft, non-prerelease publication v1.40.0 and its date."
        },
        "draft": false,
        "prerelease": false
      }
    ],
    "sources": [
      {
        "url": "https://github.com/OpenHands/OpenHands",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/OpenHands/OpenHands/blob/main/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/OpenHands/OpenHands/blob/main/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/OpenHands/OpenHands/releases/tag/v1.40.0",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537495&idx=1&sn=803c312533d9b69a993cfa4e89cc5ee2",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      }
    ],
    "article_source": {
      "article_id": "2247537495_1",
      "title": "GitHub 定律：今天有个 xxx 刷屏，明天就有个 Openxxx 登上开源热榜。",
      "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537495&idx=1&sn=803c312533d9b69a993cfa4e89cc5ee2",
      "published_date": "2026-10-03",
      "account": "逛逛GitHub",
      "content_review_url": null,
      "content_review_kind": "secondary article index only",
      "wechat_direct_body_read": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOLfkiww",
    "full_name": "OpenHands/OpenHands",
    "stargazers_count": 93582,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "e1d1fa9f3a8d7bef24449d488fcd8f00f8f272cac297bb9bed161eb6175b876a",
    "last_success_at": "2026-11-16T14:58:29.135174Z"
  }
}
```
