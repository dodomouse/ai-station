# Jev Chat Jarvis

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[jev-chat/jev-chat-jarvis](https://github.com/jev-chat/jev-chat-jarvis)

| 项目 / Field | 内容 / Value |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 8409 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:50:50.290410+00:00 |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:19:44.294Z |

## 中文

Android 聊天辅助浮层，使用无障碍与 OCR 获取当前聊天上下文，生成分析和回复草稿，由用户选择插入。

**环境与限制：** 需要 Android 设备、无障碍授权和模型服务配置；适配范围有限。截图 OCR 在本地处理，但文本上下文可能发送给所配模型提供商；草稿并非自动代发消息。

**入门：** 从[官方说明](https://github.com/jev-chat/jev-chat-jarvis/blob/main/cn/README.md)确认安装与配置步骤，再查看[发布版本](https://github.com/jev-chat/jev-chat-jarvis/releases)。本次为文档、许可原文与维护证据审查，未安装运行。

**近期维护：** [v1.7 增加 WhatsApp 支持并调整分析结果与候选回复交互。](https://github.com/jev-chat/jev-chat-jarvis/releases/tag/v1.7)（2026-10-05）

## English

An Android chat-assistance overlay that uses accessibility and OCR to read current conversation context, analyze it and draft replies for user-selected insertion.

**Requirements and limitations:** Requires Android, accessibility access and a configured model service; app compatibility is limited. Screenshot OCR is local, but text context can be sent to the selected model provider. Drafts are not automatically sent as messages.

**Getting started:** Follow the [official documentation](https://github.com/jev-chat/jev-chat-jarvis/blob/main/cn/README.md) for setup, then check [releases](https://github.com/jev-chat/jev-chat-jarvis/releases). This review examined documentation, license text and maintenance evidence; the software was not installed or run.

**Recent maintenance:** [v1.7 adds WhatsApp support and updates analysis cards and reply interactions.](https://github.com/jev-chat/jev-chat-jarvis/releases/tag/v1.7) (2026-10-05)

## Review evidence

发现线索来自第三方公众号文章索引，原始微信正文未完整读取；用途、环境、许可与维护状态依据仓库当前资料复核。

Discovery uses a third-party WeChat article index; the original article body was not fully read. Current repository sources were reviewed for function, requirements, licensing and maintenance.

- 公众号索引原文 / Indexed WeChat source：[最近逛 GitHub ，挖到 3 个给力的开源项目，第一个比较硬核。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537705&idx=1&sn=33d14b64d048e4941f677c6800ea90f3)（2026-10-11）

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
    "id": "jev-chat-jarvis",
    "name": "Jev Chat Jarvis",
    "repository": "jev-chat/jev-chat-jarvis",
    "repo_node_id": "R_kgDOUjqjyA",
    "category": "ai",
    "summary": {
      "zh-CN": "Android 聊天辅助浮层，使用无障碍与 OCR 获取当前聊天上下文，生成分析和回复草稿，由用户选择插入。",
      "en": "An Android chat-assistance overlay that uses accessibility and OCR to read current conversation context, analyze it and draft replies for user-selected insertion."
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
      "license_sha256": "a708e87c86bd01c2e161ea58961932e612ad7f2e96feb17ef601d505f7576092",
      "source_url": "https://raw.githubusercontent.com/jev-chat/jev-chat-jarvis/main/LICENSE",
      "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
      "files": [
        {
          "path": "LICENSE",
          "source_url": "https://raw.githubusercontent.com/jev-chat/jev-chat-jarvis/main/LICENSE",
          "fetched_at": "2026-11-16T14:23:27.933Z",
          "sha256": "a708e87c86bd01c2e161ea58961932e612ad7f2e96feb17ef601d505f7576092"
        }
      ]
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-10-05T16:12:03Z",
        "url": "https://github.com/jev-chat/jev-chat-jarvis/releases/tag/v1.7",
        "tag": "v1.7",
        "summary": "v1.7 — 支持 WhatsApp，分析结果改为常驻卡片",
        "draft": false,
        "prerelease": false,
        "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
        "qualifies": true,
        "reason": {
          "zh-CN": "v1.7 增加 WhatsApp 支持并调整分析结果与候选回复交互。",
          "en": "v1.7 adds WhatsApp support and updates analysis cards and reply interactions."
        }
      }
    ],
    "sources": [
      {
        "article_id": "2247537705_1",
        "title": "最近逛 GitHub ，挖到 3 个给力的开源项目，第一个比较硬核。",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537705&idx=1&sn=33d14b64d048e4941f677c6800ea90f3",
        "published_date": "2026-10-11",
        "account": "逛逛GitHub",
        "source_strength": "third_party_index",
        "index_url": "https://www.noking.tech/github-radar/data/library.json",
        "original_article_body_read": false
      }
    ],
    "discovery": {
      "account": "逛逛GitHub",
      "window_start": "2026-08-16",
      "window_end": "2026-11-16",
      "original_article_body_read": false,
      "repository_review_sources": [
        "https://api.github.com/repos/jev-chat/jev-chat-jarvis",
        "https://github.com/jev-chat/jev-chat-jarvis/blob/main/cn/README.md",
        "https://github.com/jev-chat/jev-chat-jarvis/releases/tag/v1.7",
        "https://raw.githubusercontent.com/jev-chat/jev-chat-jarvis/main/LICENSE"
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOUjqjyA",
    "full_name": "jev-chat/jev-chat-jarvis",
    "stargazers_count": 8409,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "a708e87c86bd01c2e161ea58961932e612ad7f2e96feb17ef601d505f7576092",
    "last_success_at": "2026-11-16T14:19:44.294Z"
  }
}
```

</details>
