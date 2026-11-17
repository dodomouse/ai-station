# OpenWhispr

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[OpenWhispr/openwhispr](https://github.com/OpenWhispr/openwhispr)

| 项目 / Field | 内容 / Value |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 11669 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:50:50.290410+00:00 |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:47:50.665Z |

## 中文

跨平台语音输入与会议转写应用，通过快捷键把语音转换为当前光标处的文本。提供笔记、说话人区分和可选 AI 助手。

**环境与限制：** 提供 macOS、Windows、Linux 安装包，源码开发需要 Node.js 24+。本地模型需下载且能力受硬件限制。Intel Mac 的实时说话人识别不可用，云端模型、团队服务和订阅另行配置。

**入门：** 从[官方说明](https://raw.githubusercontent.com/OpenWhispr/openwhispr/main/README.md)确认安装与配置步骤，再查看[发布版本](https://github.com/OpenWhispr/openwhispr/releases)。本次为文档、许可原文与维护证据审查，未安装运行。

**近期维护：** [v1.11.0 增加技能支持并修复 Whisper GPU 回退、粘贴和会议转写问题。](https://github.com/OpenWhispr/openwhispr/releases/tag/v1.11.0)（2026-10-29）

## English

A cross-platform dictation and meeting-transcription app that inserts recognized speech at the cursor, with notes, speaker labeling and optional AI assistance.

**Requirements and limitations:** Provides macOS, Windows and Linux installers; source development requires Node.js 24+. Local models require downloads and suitable hardware; live speaker identification is unavailable on Intel Macs. Cloud models, team services and subscriptions are separate.

**Getting started:** Follow the [official documentation](https://raw.githubusercontent.com/OpenWhispr/openwhispr/main/README.md) for setup, then check [releases](https://github.com/OpenWhispr/openwhispr/releases). This review examined documentation, license text and maintenance evidence; the software was not installed or run.

**Recent maintenance:** [v1.11.0 adds skill support and fixes Whisper GPU fallback, pasting and meeting transcription.](https://github.com/OpenWhispr/openwhispr/releases/tag/v1.11.0) (2026-10-29)

## Review evidence

发现线索来自作者署名转载的公开正文；仓库链接与作者归属已交叉核对，微信正文未直接读取。用途、环境、许可与维护状态依据仓库当前资料复核。

Discovery uses an author-attributed public repost with corroborated repository links and attribution; the WeChat body was not read directly. Current repository sources were reviewed for function, requirements, licensing and maintenance.

- 作者署名转载 / Author-attributed repost：[GitHub 周报：科研、语音、SEO，一个清单看懂 14 个 AI 项目](https://www.woshipm.com/ai/6460165.html)（2026-09-05）；仓库链接映射已交叉核对 / repository mapping corroborated.

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
    "id": "openwhispr",
    "name": "OpenWhispr",
    "repository": "OpenWhispr/openwhispr",
    "repo_node_id": "R_kgDOO-G1sQ",
    "category": "productivity",
    "summary": {
      "zh-CN": "跨平台语音输入与会议转写应用，通过快捷键把语音转换为当前光标处的文本，提供笔记、说话人区分和可选 AI 助手。",
      "en": "A cross-platform dictation and meeting-transcription app that inserts recognized speech at the cursor, with notes, speaker labeling and optional AI assistance."
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
      "license_sha256": "ecf1a12d3dc51085d2f3a720dc177c7da3cd075ea3fadcc6a1b719fb44ed30e0",
      "source_url": "https://github.com/OpenWhispr/openwhispr/blob/2eb67aa55bc7b5a8e778fe2719cbdf7bef07cd04/LICENSE",
      "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
      "files": [
        {
          "path": "LICENSE",
          "source_url": "https://github.com/OpenWhispr/openwhispr/blob/2eb67aa55bc7b5a8e778fe2719cbdf7bef07cd04/LICENSE",
          "fetched_at": "2026-11-16T14:48:18.686Z",
          "sha256": "ecf1a12d3dc51085d2f3a720dc177c7da3cd075ea3fadcc6a1b719fb44ed30e0",
          "source_commit": "2eb67aa55bc7b5a8e778fe2719cbdf7bef07cd04"
        }
      ],
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "2eb67aa55bc7b5a8e778fe2719cbdf7bef07cd04"
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-10-29T11:43:27Z",
        "url": "https://github.com/OpenWhispr/openwhispr/releases/tag/v1.11.0",
        "tag": "v1.11.0",
        "summary": "1.11.0",
        "draft": false,
        "prerelease": false,
        "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
        "qualifies": true,
        "reason": {
          "zh-CN": "v1.11.0 增加技能支持并修复 Whisper GPU 回退、粘贴和会议转写问题。",
          "en": "v1.11.0 adds skill support and fixes Whisper GPU fallback, pasting and meeting transcription."
        }
      }
    ],
    "sources": [
      {
        "url": "https://www.woshipm.com/ai/6460165.html",
        "title": "GitHub 周报：科研、语音、SEO，一个清单看懂 14 个 AI 项目",
        "published_date": "2026-09-05",
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
        "https://api.github.com/repos/OpenWhispr/openwhispr",
        "https://raw.githubusercontent.com/OpenWhispr/openwhispr/main/README.md",
        "https://github.com/OpenWhispr/openwhispr/releases/tag/v1.11.0",
        "https://github.com/OpenWhispr/openwhispr/blob/2eb67aa55bc7b5a8e778fe2719cbdf7bef07cd04/LICENSE"
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOO-G1sQ",
    "full_name": "OpenWhispr/openwhispr",
    "stargazers_count": 11669,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "ecf1a12d3dc51085d2f3a720dc177c7da3cd075ea3fadcc6a1b719fb44ed30e0",
    "last_success_at": "2026-11-16T14:47:50.665Z"
  }
}
```

</details>
