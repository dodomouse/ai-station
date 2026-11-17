# OpenDots

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[CopilotKit/OpenDots](https://github.com/CopilotKit/OpenDots)

| 项目 / Field | 内容 / Value |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 6624 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:50:50.290410+00:00 |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:19:44.350Z |

## 中文

持久化 AI 同事的社区模板，通过网页、手机和消息渠道与 Agent 交互，并提供各自的电脑工作区。

**环境与限制：** MIT 覆盖应用模板。运行需要 Node.js 24、npm 和 CopilotKit Intelligence 后端。后端有托管、评估或商业自托管条款，不在本仓库开源授权范围内。模型、浏览器基础设施及账号另配。

**入门：** 从[官方说明](https://raw.githubusercontent.com/CopilotKit/OpenDots/main/README.md)确认安装与配置步骤，再查看[发布版本](https://github.com/CopilotKit/OpenDots/releases)。本次为文档、许可原文与维护证据审查，未安装运行。

**近期维护：** [提交修复工作区主人刷新画面时产生多余活动日志的问题，并添加测试。](https://github.com/CopilotKit/OpenDots/commit/3e10a7b5fb546aa760111fffba492c0fec1628a7)（2026-11-03）

## English

A community starter for persistent AI coworkers, with web, mobile and messaging interactions and per-agent computer workspaces.

**Requirements and limitations:** MIT covers the application template. Running it requires Node.js 24, npm and the CopilotKit Intelligence backend, which has hosted, evaluation or commercial self-hosting terms outside this repository's open-source grant. Models, browser infrastructure and accounts are separate.

**Getting started:** Follow the [official documentation](https://raw.githubusercontent.com/CopilotKit/OpenDots/main/README.md) for setup, then check [releases](https://github.com/CopilotKit/OpenDots/releases). This review examined documentation, license text and maintenance evidence; the software was not installed or run.

**Recent maintenance:** [The inspected commit prevents owner screen refreshes from polluting computer activity logs and adds tests.](https://github.com/CopilotKit/OpenDots/commit/3e10a7b5fb546aa760111fffba492c0fec1628a7) (2026-11-03)

## Review evidence

发现线索来自第三方公众号文章索引，原始微信正文未完整读取；用途、环境、许可与维护状态依据仓库当前资料复核。

Discovery uses a third-party WeChat article index; the original article body was not fully read. Current repository sources were reviewed for function, requirements, licensing and maintenance.

- 公众号索引原文 / Indexed WeChat source：[3 个最近爆火的 Personal Agent ，在 GitHub 上有开源平替了。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537624&idx=1&sn=10eccfc7b58a97b27b2144654b7ddd35)（2026-10-08）
- 作者署名转载 / Author-attributed repost：[3 个最近爆火的 Personal Agent ，在 GitHub 上有开源平替了。](https://www.woshipm.com/ai/6475152.html)（2026-10-09）；仓库链接映射已交叉核对 / repository mapping corroborated.

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-16T14:50:50.290410+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "opendots",
    "name": "OpenDots",
    "repository": "CopilotKit/OpenDots",
    "repo_node_id": "R_kgDOUzcQzw",
    "category": "ai",
    "summary": {
      "zh-CN": "持久化 AI 同事的社区模板，通过网页、手机和消息渠道与 Agent 交互，并提供各自的电脑工作区。",
      "en": "A community starter for persistent AI coworkers, with web, mobile and messaging interactions and per-agent computer workspaces."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:50:50.290410+00:00",
        "en": "2026-11-16T14:50:50.290410+00:00"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "15a0e5343aea872c0573ad72feb6044b336f162d724cc1673c608e6b37ea071b",
      "source_url": "https://github.com/CopilotKit/OpenDots/blob/0e706ab3686fee50e9f26befc6df2aac2c2b1422/LICENSE",
      "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
      "files": [
        {
          "path": "LICENSE",
          "source_url": "https://github.com/CopilotKit/OpenDots/blob/0e706ab3686fee50e9f26befc6df2aac2c2b1422/LICENSE",
          "fetched_at": "2026-11-16T14:23:27.845Z",
          "sha256": "15a0e5343aea872c0573ad72feb6044b336f162d724cc1673c608e6b37ea071b",
          "source_commit": "0e706ab3686fee50e9f26befc6df2aac2c2b1422"
        }
      ],
      "scope": "MIT application template only. Required CopilotKit Intelligence backend has separate hosted/evaluation/commercial terms.",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "0e706ab3686fee50e9f26befc6df2aac2c2b1422"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-03T09:17:11Z",
        "url": "https://github.com/CopilotKit/OpenDots/commit/3e10a7b5fb546aa760111fffba492c0fec1628a7",
        "sha": "3e10a7b5fb546aa760111fffba492c0fec1628a7",
        "summary": "fix: keep the owner screen refresh out of the Computer activity log (#94)",
        "files": [
          "src/server/computer-service.ts",
          "src/server/computer-store.ts",
          "tests/computer.test.ts"
        ],
        "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
        "qualifies": true,
        "reason": {
          "zh-CN": "提交修复工作区主人刷新画面时产生多余活动日志的问题，并添加测试。",
          "en": "The inspected commit prevents owner screen refreshes from polluting computer activity logs and adds tests."
        }
      }
    ],
    "sources": [
      {
        "article_id": "2247537624_1",
        "title": "3 个最近爆火的 Personal Agent ，在 GitHub 上有开源平替了。",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537624&idx=1&sn=10eccfc7b58a97b27b2144654b7ddd35",
        "published_date": "2026-10-08",
        "account": "逛逛GitHub",
        "source_strength": "third_party_index",
        "index_url": "https://www.noking.tech/github-radar/data/library.json",
        "original_article_body_read": false
      },
      {
        "url": "https://www.woshipm.com/ai/6475152.html",
        "title": "3 个最近爆火的 Personal Agent ，在 GitHub 上有开源平替了。",
        "published_date": "2026-10-09",
        "account": "逛逛GitHub",
        "source_strength": "author_attributed_repost_repository_mapping",
        "author_attribution_confirmed": true,
        "body_read_method": "public_html_repository_links_and_attribution_extraction",
        "full_text_archived": false
      }
    ],
    "discovery": {
      "account": "逛逛GitHub",
      "window_start": "2026-08-16",
      "window_end": "2026-11-16",
      "original_article_body_read": false,
      "repository_review_sources": [
        "https://api.github.com/repos/copilotkit/opendots",
        "https://raw.githubusercontent.com/CopilotKit/OpenDots/main/README.md",
        "https://github.com/CopilotKit/OpenDots/commit/3e10a7b5fb546aa760111fffba492c0fec1628a7",
        "https://github.com/CopilotKit/OpenDots/blob/0e706ab3686fee50e9f26befc6df2aac2c2b1422/LICENSE"
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOUzcQzw",
    "full_name": "CopilotKit/OpenDots",
    "stargazers_count": 6624,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "15a0e5343aea872c0573ad72feb6044b336f162d724cc1673c608e6b37ea071b",
    "last_success_at": "2026-11-16T14:19:44.350Z"
  }
}
```

</details>
