# Claude-Mem

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 117552 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:32:13.743Z |

## 中文

记录编码智能体的工作观察，在后续会话中检索和恢复相关记忆。

### 用途与功能

- 保留跨会话项目背景
- 搜索既有决策、修复和工作记录

通过宿主hooks、本地worker、观察器与搜索界面组织记忆；部分工具仅支持检索，不能记录会话。

### 环境与限制

需 Node.js 20.19+（20.x）或22.12+及支持的宿主。观察器可使用自己的模型提供商，也有收费服务；记录和摘要可能向所选服务发送代码或活动。安装器选择与各适配器能力需核对。

### 开始使用

按 README 使用安装器选择宿主与记忆提供商，完成后重新启动会话；全局 npm 安装SDK不等于配置插件。 参阅[官方 README](https://github.com/thedotmack/claude-mem/blob/main/README.md)。

### 收录与来源

有实际会话采集、存储、检索和恢复实现，安装与服务边界有明确说明。 最近维护：[v15.19.0](https://github.com/thedotmack/claude-mem/releases/tag/v15.19.0)（2026-11-16T02:04:44Z）。正式版允许从 My Work 继续 Claude Code 或 Codex 对话，并记录回复和停止状态。

通过逛逛GitHub的第三方文章索引发现。索引记录了下列文章；本次未读取微信原文，不据此声称已阅读全文。

- 2026-11-02：[盘点 10 月份 19 个 Star 蹭蹭涨的 GitHub 项目，第一个很有用。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538256&idx=1&sn=3b97e48392e47b295968f5c66a4ce5f0)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。


补充核对作者在公开平台发布或授权发布的文章，确认署名、日期与仓库关联：

- 2026-11-02：[盘点 10 月份 19 个 Star 蹭蹭涨的 GitHub 项目，第一个很有用。](https://www.woshipm.com/ai/6487701.html)

## English

Records coding-agent observations and retrieves relevant memory in later sessions.

### Uses and features

- Preserve project context across sessions
- Search prior decisions, fixes and work records

Combines host hooks, a local worker, an observer and search UI; some hosts support retrieval only, without recording sessions.

### Requirements and limits

Requires Node.js 20.19+ in the 20.x line or 22.12+ and a supported host. The observer can use a configured model provider or a paid service; recording and summarization may send code or activity to that provider. Review installer choices and adapter capabilities.

### Getting started

Use the documented installer to choose a host and memory provider, then restart sessions; globally installing the SDK does not configure plugin hooks. See the [official README](https://github.com/thedotmack/claude-mem/blob/main/README.md).

### Review and provenance

Implements session capture, storage, retrieval and resumption, with documented installation and service boundaries. Recent maintenance: [v15.19.0](https://github.com/thedotmack/claude-mem/releases/tag/v15.19.0) (2026-11-16T02:04:44Z). The formal release can continue Claude Code or Codex conversations from My Work and record replies and stop status.

Discovered through a third-party index of 逛逛GitHub articles. The index records the articles below; the original WeChat pages were not read in this review. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.


Public articles published or authorized by the author were also checked for attribution, date and repository links. See the additional links in the Chinese section.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:32:13.743Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "claude-mem",
    "name": "Claude-Mem",
    "repository": "thedotmack/claude-mem",
    "repo_node_id": "R_kgDOPng1Jw",
    "category": "ai",
    "tags": [],
    "forms": [
      "plugin",
      "service"
    ],
    "platforms": [
      "linux",
      "macos",
      "windows"
    ],
    "aliases": {
      "zh-CN": [
        "Claude-Mem"
      ],
      "en": [
        "Claude-Mem"
      ]
    },
    "summary": {
      "zh-CN": "记录编码智能体的工作观察，在后续会话中检索和恢复相关记忆。",
      "en": "Records coding-agent observations and retrieves relevant memory in later sessions."
    },
    "use_cases": {
      "zh-CN": [
        "保留跨会话项目背景",
        "搜索既有决策、修复和工作记录"
      ],
      "en": [
        "Preserve project context across sessions",
        "Search prior decisions, fixes and work records"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:32:13.743Z",
        "en": "2026-11-16T14:32:13.743Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
      "source_url": "https://github.com/thedotmack/claude-mem/blob/82d3602e2e43503ffd39c180b2af5f7521fc457b/LICENSE",
      "reviewed_at": "2026-11-16T14:32:13.743Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "82d3602e2e43503ffd39c180b2af5f7521fc457b"
    },
    "activity_evidence": [
      {
        "type": "release",
        "reason": {
          "zh-CN": "正式版允许从 My Work 继续 Claude Code 或 Codex 对话，并记录回复和停止状态。",
          "en": "The formal release can continue Claude Code or Codex conversations from My Work and record replies and stop status."
        },
        "reviewed_at": "2026-11-16T14:32:13.743Z",
        "qualifies": true,
        "url": "https://github.com/thedotmack/claude-mem/releases/tag/v15.19.0",
        "occurred_at": "2026-11-16T02:04:44Z"
      }
    ],
    "sources": [
      {
        "url": "https://github.com/thedotmack/claude-mem/blob/main/README.md",
        "accessed_at": "2026-11-16T14:32:13.743Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/thedotmack/claude-mem/blob/82d3602e2e43503ffd39c180b2af5f7521fc457b/LICENSE",
        "accessed_at": "2026-11-16T14:32:13.743Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.noking.tech/github-radar/data/library.json",
        "accessed_at": "2026-11-16T14:32:13.743Z",
        "supports": {
          "zh-CN": "第三方索引中的公众号文章归属、时间与项目发现线索；非原文阅读证据。",
          "en": "Third-party account attribution, article dates and discovery leads; not proof of reading the originals."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538256&idx=1&sn=3b97e48392e47b295968f5c66a4ce5f0",
        "accessed_at": "2026-11-16T14:32:13.743Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-11-02 盘点 10 月份 19 个 Star 蹭蹭涨的 GitHub 项目，第一个很有用。；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-11-02; not directly read in this review."
        }
      },
      {
        "url": "https://www.woshipm.com/ai/6487701.html",
        "accessed_at": "2026-11-16T14:26:00.440875+00:00",
        "published_date": "2026-11-02",
        "author": "逛逛GitHub",
        "supports": {
          "zh-CN": "作者公开发表或授权的文章；已核对署名、日期与仓库链接。",
          "en": "Author-published or authorized public article; attribution, date and repository links checked."
        }
      }
    ],
    "quality_review": {
      "basis": {
        "zh-CN": "有实际会话采集、存储、检索和恢复实现，安装与服务边界有明确说明。",
        "en": "Implements session capture, storage, retrieval and resumption, with documented installation and service boundaries."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOPng1Jw",
    "full_name": "thedotmack/claude-mem",
    "stargazers_count": 117552,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
    "last_success_at": "2026-11-16T14:19:05.888Z"
  }
}
```

</details>

