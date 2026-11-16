# Codex with ChatGPT

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[XiaoDuoYa/codex-with-chatgpt](https://github.com/XiaoDuoYa/codex-with-chatgpt)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 7718 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:20:00.540Z |

## 中文

用只读 MCP 连接将 ChatGPT 网页的规划与审查接入 Codex 工作区。

### 主要功能

- 按需提供工作区文件读取、搜索和执行记录。
- 由 Codex 保留文件修改与命令执行职责。

### 环境与限制

- 需要 Git、Node.js 20+、cloudflared 及支持连接的 ChatGPT/Codex 环境。
- 被读取的代码会发送给模型服务，只读并不表示内容留在本机。

### 开始使用

从[官方说明](https://github.com/XiaoDuoYa/codex-with-chatgpt/blob/main/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/XiaoDuoYa/codex-with-chatgpt/releases)可用于确认版本。

### 收录复核

用只读 MCP 连接将 ChatGPT 网页的规划与审查接入 Codex 工作区。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。

有效维护证据：[v0.1.4](https://github.com/XiaoDuoYa/codex-with-chatgpt/releases/tag/v0.1.4)，2026-10-01T05:19:24Z。已核对正式发行 v0.1.4 的发布状态与时间。

发现线索：[公开索引](https://www.noking.tech/github-radar/)记录的[微信文章](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536916&idx=1&sn=deaea310ec94f838f6484f580da1acc2)，索引日期 2026-09-14。仅核对公开索引，未直接读取该篇微信全文；功能与限制以上游资料为依据。

本次为文档与实现证据复核，未安装或运行上游项目。

## English

Connects ChatGPT web planning and review to a Codex workspace through a read-only MCP bridge.

### Features

- Provides on-demand file reading, search and execution records.
- Keeps file changes and command execution with Codex.

### Requirements and limits

- Requires Git, Node.js 20+, cloudflared and compatible ChatGPT/Codex environments.
- Read code is sent to the model service
- read-only access does not mean data stays on the machine.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/XiaoDuoYa/codex-with-chatgpt/blob/main/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/XiaoDuoYa/codex-with-chatgpt/releases) for versions.

### Review and provenance

Connects ChatGPT web planning and review to a Codex workspace through a read-only MCP bridge. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.

Activity: [v0.1.4](https://github.com/XiaoDuoYa/codex-with-chatgpt/releases/tag/v0.1.4), 2026-10-01T05:19:24Z. Checked the non-draft, non-prerelease publication v0.1.4 and its date.

Discovery: [an indexed WeChat article](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536916&idx=1&sn=deaea310ec94f838f6484f580da1acc2). This is a secondary discovery record; the WeChat article body was not read. Features and limits come from upstream documentation.

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
    "id": "codex-with-chatgpt",
    "name": "Codex with ChatGPT",
    "repository": "XiaoDuoYa/codex-with-chatgpt",
    "repo_node_id": "R_kgDOUHFJRw",
    "category": "development",
    "summary": {
      "zh-CN": "用只读 MCP 连接将 ChatGPT 网页的规划与审查接入 Codex 工作区。",
      "en": "Connects ChatGPT web planning and review to a Codex workspace through a read-only MCP bridge."
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
      "zh-CN": "用只读 MCP 连接将 ChatGPT 网页的规划与审查接入 Codex 工作区。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。",
      "en": "Connects ChatGPT web planning and review to a Codex workspace through a read-only MCP bridge. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "4b18c7291304dc84d601a6305053e9a68b3f39877f27434556f30e184eb834b5",
      "source_url": "https://github.com/XiaoDuoYa/codex-with-chatgpt/blob/main/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "Root license reviewed. External dependencies and assets retain their individual licenses."
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-10-01T05:19:24Z",
        "reviewed_at": "2026-11-16T14:58:29.135174Z",
        "url": "https://github.com/XiaoDuoYa/codex-with-chatgpt/releases/tag/v0.1.4",
        "qualifies": true,
        "reason": {
          "zh-CN": "已核对正式发行 v0.1.4 的发布状态与时间。",
          "en": "Checked the non-draft, non-prerelease publication v0.1.4 and its date."
        },
        "draft": false,
        "prerelease": false
      }
    ],
    "sources": [
      {
        "url": "https://github.com/XiaoDuoYa/codex-with-chatgpt",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/XiaoDuoYa/codex-with-chatgpt/blob/main/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/XiaoDuoYa/codex-with-chatgpt/blob/main/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/XiaoDuoYa/codex-with-chatgpt/releases/tag/v0.1.4",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536916&idx=1&sn=deaea310ec94f838f6484f580da1acc2",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      }
    ],
    "article_source": {
      "article_id": "2247536916_1",
      "title": "2 个让你的 Codex 狠狠省 Token 的开源项目，有点意思啊。",
      "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536916&idx=1&sn=deaea310ec94f838f6484f580da1acc2",
      "published_date": "2026-09-14",
      "account": "逛逛GitHub",
      "content_review_url": null,
      "content_review_kind": "secondary article index only",
      "wechat_direct_body_read": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOUHFJRw",
    "full_name": "XiaoDuoYa/codex-with-chatgpt",
    "stargazers_count": 7718,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "4b18c7291304dc84d601a6305053e9a68b3f39877f27434556f30e184eb834b5",
    "last_success_at": "2026-11-16T14:20:00.540Z"
  }
}
```
