# OpenMausBot

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[milind-soni/OpenMausBot](https://github.com/milind-soni/OpenMausBot)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 23982 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:24:08.700270Z |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:18:52.133Z |

## 中文

### 用途与功能

以联系人和群聊组织多个编码智能体。可为各机器人配置模型、工作目录、连接应用和执行环境。

提供本地会话记录、审批卡片、定时任务和 MCP 控制入口。适合集中管理已有命令行助手，包括 Claude 和 Codex。

### 环境与限制

桌面发行覆盖 macOS、Windows 和 Ubuntu。需要可用的智能体账号或模型服务。云桌面与应用连接各有配置和费用；本地保存会话不等于模型推理离线。Ubuntu Wayland 主机控制仍有限制。

### 入门与收录判断

从[官方 README](https://github.com/milind-soni/OpenMausBot/blob/main/README.md)查阅安装和配置步骤。把已有编码助手、执行环境和人工审批放在同一会话中，入口和发行包完整。

本轮为文档复核，未安装、运行或测试上游软件。正式 v0.1.161 调整自动任务失败后的重试，并补充跳过运行的记录。详见[维护记录](https://github.com/milind-soni/OpenMausBot/releases/tag/v0.1.161)。

### 文章来源

公众号“逛逛GitHub”的[微信原文](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538420&idx=1&sn=9769127e763c53057c449032da509279)，索引日期为 2026-11-09。本次读取了作者在[人人都是产品经理发布的正文](https://www.woshipm.com/share/6491406.html)，该页日期为 2026-11-10。功能和限制另按当前上游复核。


补充核对作者在公开平台发布或授权发布的文章，确认署名、日期与仓库关联：

- 2026-10-09：[3 个最近爆火的 Personal Agent ，在 GitHub 上有开源平替了。](https://www.woshipm.com/ai/6475152.html)

## English

### Purpose and features

A desktop chat interface for coordinating agents with separate models, workspaces and connected applications.

Combines local transcripts, approval cards, scheduled work and an MCP control interface for existing coding agents.

### Requirements and limits

Requires a supported desktop and agent account or model service. Cloud computers and app connectors have separate requirements and costs. Local transcript storage does not make inference offline; host control has platform limits.

### Getting started and review

Use the [official README](https://github.com/milind-soni/OpenMausBot/blob/main/README.md) for installation and configuration. This is a documentation review; the software was not installed or tested. Stable v0.1.161 changes automation retry behavior and records skipped runs. See the [release](https://github.com/milind-soni/OpenMausBot/releases/tag/v0.1.161).

The original WeChat article is dated 2026-11-09 in the public index. Its author-published mirror is dated 2026-11-10. The mirror establishes the article association; current upstream documentation supports the feature descriptions.


Public articles published or authorized by the author were also checked for attribution, date and repository links. See the additional links in the Chinese section.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:24:08.700270Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "openmausbot",
    "name": "OpenMausBot",
    "repository": "milind-soni/OpenMausBot",
    "repo_node_id": "R_kgDOT1lw9w",
    "category": "ai",
    "summary": {
      "zh-CN": "以联系人和群聊组织多个编码智能体。可为各机器人配置模型、工作目录、连接应用和执行环境。",
      "en": "A desktop chat interface for coordinating agents with separate models, workspaces and connected applications."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:24:08.700270Z",
        "en": "2026-11-16T14:24:08.700270Z"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "basis": "把已有编码助手、执行环境和人工审批放在同一会话中，入口和发行包完整。",
      "stars_are_advisory": true,
      "reviewed_at": "2026-11-16T14:24:08.700270Z"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
      "source_url": "https://github.com/milind-soni/OpenMausBot/blob/12c07fb5fff3faa755233a71d25f034bbed7ae0f/LICENSE",
      "reviewed_at": "2026-11-16T14:24:08.700270Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "12c07fb5fff3faa755233a71d25f034bbed7ae0f"
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-11-15T21:43:29Z",
        "reviewed_at": "2026-11-16T14:24:08.700270Z",
        "url": "https://github.com/milind-soni/OpenMausBot/releases/tag/v0.1.161",
        "qualifies": true,
        "reason": {
          "zh-CN": "正式 v0.1.161 调整自动任务失败后的重试，并补充跳过运行的记录。",
          "en": "Stable v0.1.161 changes automation retry behavior and records skipped runs."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/milind-soni/OpenMausBot",
        "accessed_at": "2026-11-16T14:18:52.133Z",
        "supports": "Repository identity, Stars and public state."
      },
      {
        "url": "https://github.com/milind-soni/OpenMausBot/blob/main/README.md",
        "accessed_at": "2026-11-16T14:24:08.700270Z",
        "supports": "Capabilities, requirements and limits."
      },
      {
        "url": "https://www.woshipm.com/share/6491406.html",
        "published_date": "2026-11-10",
        "accessed_at": "2026-11-16T14:24:08.700270Z",
        "supports": "Article body and account attribution verified on the author-published mirror."
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538420&idx=1&sn=9769127e763c53057c449032da509279",
        "published_date": "2026-11-09",
        "supports": "Original WeChat URL and date from the public article index; original body unavailable."
      },
      {
        "url": "https://www.woshipm.com/ai/6475152.html",
        "accessed_at": "2026-11-16T14:26:02.216777+00:00",
        "published_date": "2026-10-09",
        "author": "逛逛GitHub",
        "supports": {
          "zh-CN": "作者公开发表或授权的文章；已核对署名、日期与仓库链接。",
          "en": "Author-published or authorized public article; attribution, date and repository links checked."
        }
      }
    ],
    "discovery": {
      "account": "逛逛GitHub",
      "article": {
        "article_id": "2247538420_1",
        "title": "7 个近期 GitHub 上贼火火的开源项目，又是质量很高的一波。",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538420&idx=1&sn=9769127e763c53057c449032da509279",
        "published_date": "2026-11-09"
      },
      "index_url": "https://www.noking.tech/github-radar/",
      "body_verification": "author_published_mirror"
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOT1lw9w",
    "full_name": "milind-soni/OpenMausBot",
    "stargazers_count": 23982,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
    "last_success_at": "2026-11-16T14:18:52.133Z"
  }
}
```

</details>
