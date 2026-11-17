# T3 Code

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[pingdotgg/t3code](https://github.com/pingdotgg/t3code)

| 项目 / Field | 内容 / Value |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 62317 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:50:50.290410+00:00 |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:18:43.844Z |

## 中文

统一管理多个编码 Agent 的会话、变更差异和远程连接，可从桌面、网页或手机继续开发任务。

**环境与限制：** 支持 macOS、Windows、Linux；需自行安装并登录所选 Agent，模型订阅或 API 用量另计。具体提供商与远程功能以当前文档为准。

**入门：** 从[官方说明](https://raw.githubusercontent.com/pingdotgg/t3code/main/README.md)确认安装与配置步骤，再查看[发布版本](https://github.com/pingdotgg/t3code/releases)。本次为文档、许可原文与维护证据审查，未安装运行。

**近期维护：** [提交把 Pi 健康检查放入专用目录，避免在服务端工作目录加载扩展，并补充测试。](https://github.com/pingdotgg/t3code/commit/222288b00f9ed392e1e7352ad929c9ae9ac10cef)（2026-11-16）

## English

Manages coding-agent sessions, diffs and remote connections in one interface, with desktop, web and phone access.

**Requirements and limitations:** Supports macOS, Windows and Linux. Install and authenticate the selected agents separately; model subscriptions and API usage are separate. Provider and remote capabilities depend on the current integration.

**Getting started:** Follow the [official documentation](https://raw.githubusercontent.com/pingdotgg/t3code/main/README.md) for setup, then check [releases](https://github.com/pingdotgg/t3code/releases). This review examined documentation, license text and maintenance evidence; the software was not installed or run.

**Recent maintenance:** [The inspected commit isolates Pi health checks in a dedicated directory and tests extension-loading behavior.](https://github.com/pingdotgg/t3code/commit/222288b00f9ed392e1e7352ad929c9ae9ac10cef) (2026-11-16)

## Review evidence

发现线索来自第三方公众号文章索引，原始微信正文未完整读取；用途、环境、许可与维护状态依据仓库当前资料复核。

Discovery uses a third-party WeChat article index; the original article body was not fully read. Current repository sources were reviewed for function, requirements, licensing and maintenance.

- 公众号索引原文 / Indexed WeChat source：[盘点 10 月份 19 个 Star 蹭蹭涨的 GitHub 项目，第一个很有用。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538256&idx=1&sn=3b97e48392e47b295968f5c66a4ce5f0)（2026-11-02）
- 作者署名转载 / Author-attributed repost：[盘点 10 月份 19 个 Star 蹭蹭涨的 GitHub 项目，第一个很有用。](https://www.woshipm.com/ai/6487701.html)（2026-11-02）；仓库链接映射已交叉核对 / repository mapping corroborated.

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
    "id": "t3code",
    "name": "T3 Code",
    "repository": "pingdotgg/t3code",
    "repo_node_id": "R_kgDORLtfbQ",
    "category": "development",
    "summary": {
      "zh-CN": "统一管理多个编码 Agent 的会话、变更差异和远程连接，可从桌面、网页或手机继续开发任务。",
      "en": "Manages coding-agent sessions, diffs and remote connections in one interface, with desktop, web and phone access."
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
      "license_sha256": "935d8f2af0c703f9c39517ee57cc4930b19d02d533be930b63f0e82f93614b43",
      "source_url": "https://github.com/pingdotgg/t3code/blob/222288b00f9ed392e1e7352ad929c9ae9ac10cef/LICENSE",
      "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
      "files": [
        {
          "path": "LICENSE",
          "source_url": "https://github.com/pingdotgg/t3code/blob/222288b00f9ed392e1e7352ad929c9ae9ac10cef/LICENSE",
          "fetched_at": "2026-11-16T14:23:16.623Z",
          "sha256": "935d8f2af0c703f9c39517ee57cc4930b19d02d533be930b63f0e82f93614b43",
          "source_commit": "222288b00f9ed392e1e7352ad929c9ae9ac10cef"
        }
      ],
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "222288b00f9ed392e1e7352ad929c9ae9ac10cef"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-16T14:19:22Z",
        "url": "https://github.com/pingdotgg/t3code/commit/222288b00f9ed392e1e7352ad929c9ae9ac10cef",
        "sha": "222288b00f9ed392e1e7352ad929c9ae9ac10cef",
        "summary": "fix(pi): health checks no longer run Pi extensions in the server's folder (#37654)",
        "files": [
          "packages/provider-pi/src/server/driver.test.ts",
          "packages/provider-pi/src/server/driver.ts"
        ],
        "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
        "qualifies": true,
        "reason": {
          "zh-CN": "提交把 Pi 健康检查放入专用目录，避免在服务端工作目录加载扩展，并补充测试。",
          "en": "The inspected commit isolates Pi health checks in a dedicated directory and tests extension-loading behavior."
        }
      }
    ],
    "sources": [
      {
        "article_id": "2247538256_1",
        "title": "盘点 10 月份 19 个 Star 蹭蹭涨的 GitHub 项目，第一个很有用。",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538256&idx=1&sn=3b97e48392e47b295968f5c66a4ce5f0",
        "published_date": "2026-11-02",
        "account": "逛逛GitHub",
        "source_strength": "third_party_index",
        "index_url": "https://www.noking.tech/github-radar/data/library.json",
        "original_article_body_read": false
      },
      {
        "url": "https://www.woshipm.com/ai/6487701.html",
        "title": "盘点 10 月份 19 个 Star 蹭蹭涨的 GitHub 项目，第一个很有用。",
        "published_date": "2026-11-02",
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
        "https://api.github.com/repos/pingdotgg/t3code",
        "https://raw.githubusercontent.com/pingdotgg/t3code/main/README.md",
        "https://github.com/pingdotgg/t3code/commit/222288b00f9ed392e1e7352ad929c9ae9ac10cef",
        "https://github.com/pingdotgg/t3code/blob/222288b00f9ed392e1e7352ad929c9ae9ac10cef/LICENSE"
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDORLtfbQ",
    "full_name": "pingdotgg/t3code",
    "stargazers_count": 62317,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "935d8f2af0c703f9c39517ee57cc4930b19d02d533be930b63f0e82f93614b43",
    "last_success_at": "2026-11-16T14:18:43.844Z"
  }
}
```

</details>
