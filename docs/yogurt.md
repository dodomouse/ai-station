# Yogurt

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[FrigadeHQ/yogurt](https://github.com/FrigadeHQ/yogurt)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 1788 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:30:19.931551Z |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:27:09.959Z |

## 中文

### 用途与功能

在本机记录会议语音、生成转写和纪要，并从历史会议中回答问题、附上出处。

通过麦克风与系统音频录制通话，提供文件夹、搜索、Markdown 导出及可选本地 MCP 读取入口。

### 环境与限制

需要至少 8 GB 内存。支持 Apple Silicon 与 macOS 14.4+、Windows 10 2004+ x64、Ubuntu 22.04+ x64 等环境。首次需下载数 GB 模型；日历和发言人识别部分功能仅限 Mac。启用 MCP 后，接入的助手可能把读取内容发给自己的模型。

### 入门与收录判断

从[官方 README](https://github.com/FrigadeHQ/yogurt/blob/main/README.md)查阅安装和使用步骤。本地转写和纪要功能完整，提供桌面发行、导出与来源追溯。

本轮为文档复核，未安装、运行或测试上游项目。正式发行 v0.3.33，附前一版本的变更比较。详见[维护记录](https://github.com/FrigadeHQ/yogurt/releases/tag/v0.3.33)。

### 文章来源

发现于“逛逛GitHub”在 2026-11-16 发布的[《8 个开源工具速览》](https://www.woshipm.com/ai/6494405.html)。已读取作者署名正文，功能和限制另按当前上游复核。

## English

### Purpose and features

Records meetings locally, creates transcripts and notes, and answers questions across meetings with source references.

Captures microphone and system audio, with folders, search, Markdown export and optional local MCP read access.

### Requirements and limits

Requires at least 8 GB RAM and a supported Mac, Windows or Linux system. Initial models require several GB of downloads. Some calendar and speaker features are Mac-only. An external MCP client may send retrieved notes to its own model.

### Getting started and review

Use the [official README](https://github.com/FrigadeHQ/yogurt/blob/main/README.md) for installation and usage. This is a documentation review; the software was not installed or tested. Stable v0.3.33 was published with a changelog comparison. See the [activity evidence](https://github.com/FrigadeHQ/yogurt/releases/tag/v0.3.33).

The project appears in the account's [author-published article dated 2026-11-16](https://www.woshipm.com/ai/6494405.html). Current upstream documentation supports the feature descriptions.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:30:19.931551Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "yogurt",
    "name": "Yogurt",
    "repository": "FrigadeHQ/yogurt",
    "repo_node_id": "R_kgDOVp0Log",
    "category": "productivity",
    "summary": {
      "zh-CN": "在本机记录会议语音、生成转写和纪要，并从历史会议中回答问题、附上出处。",
      "en": "Records meetings locally, creates transcripts and notes, and answers questions across meetings with source references."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:30:19.931551Z",
        "en": "2026-11-16T14:30:19.931551Z"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "basis": "本地转写和纪要功能完整，提供桌面发行、导出与来源追溯。",
      "rationale": "本地转写和纪要功能完整，提供桌面发行、导出与来源追溯。",
      "stars_are_advisory": true,
      "reviewed_at": "2026-11-16T14:30:19.931551Z"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "5c7f0de8bbe8ee8a29540939bfdd83adf000e8c2817587d618c9637347dd34ec",
      "source_url": "https://github.com/FrigadeHQ/yogurt/blob/dcafd6694cc4210befb0664c3222f63756d2b824/LICENSE",
      "reviewed_at": "2026-11-16T14:30:19.931551Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "dcafd6694cc4210befb0664c3222f63756d2b824"
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-11-16T14:05:13Z",
        "reviewed_at": "2026-11-16T14:30:19.931551Z",
        "url": "https://github.com/FrigadeHQ/yogurt/releases/tag/v0.3.33",
        "qualifies": true,
        "reason": {
          "zh-CN": "正式发行 v0.3.33，附前一版本的变更比较。",
          "en": "Stable v0.3.33 was published with a changelog comparison."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/FrigadeHQ/yogurt",
        "accessed_at": "2026-11-16T14:27:09.959Z",
        "supports": "Repository identity, Stars and public state."
      },
      {
        "url": "https://github.com/FrigadeHQ/yogurt/blob/main/README.md",
        "accessed_at": "2026-11-16T14:30:19.931551Z",
        "supports": "Capabilities, requirements and limits."
      },
      {
        "url": "https://www.woshipm.com/ai/6494405.html",
        "published_date": "2026-11-16",
        "accessed_at": "2026-11-16T14:30:19.931551Z",
        "supports": "Author-published article body and account attribution."
      }
    ],
    "discovery": {
      "account": "逛逛GitHub",
      "article_url": "https://www.woshipm.com/ai/6494405.html",
      "published_date": "2026-11-16",
      "body_verification": "author_published_article"
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVp0Log",
    "full_name": "FrigadeHQ/yogurt",
    "stargazers_count": 1788,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "5c7f0de8bbe8ee8a29540939bfdd83adf000e8c2817587d618c9637347dd34ec",
    "last_success_at": "2026-11-16T14:27:09.959Z"
  }
}
```

</details>
