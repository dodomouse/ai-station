# 知了 Cicada

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[wquguru/cicada](https://github.com/wquguru/cicada)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 2347 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:21:24.299979Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:21:24.299979Z |

## 中文

为会议和直播提供双语字幕、同声传译与会议纪要。直接读取系统声音，支持转写搜索和记录导出。

### 主要功能

- 从系统声音生成双语字幕，整理讨论重点与待办事项。
- 在通话中播放翻译后的语音，并按平台配置音频通道。
- 搜索和修正转写内容，导出会议记录与字幕。
- 在支持的 Mac 上使用本机识别，其他平台按配置连接语音服务。

### 环境与限制

- 要求 macOS 14.4+、Windows 10 2004+、Ubuntu 22.04/24.04 或 Android 10+。
- Apple 芯片 Mac 可在本机识别语音。Intel Mac 与其他平台需要配置模型服务。
- 翻译、纪要和语音克隆的服务条件不同；服务可能接收音频或文本。
- Android 通话应用会限制内部音频采集。面对面模式需要通过扬声器收音。
- 项目代码采用 Apache-2.0。可选 BlackHole 驱动和附带声纹模型使用独立许可。

### 开始使用

从官方 Releases 阅读系统要求和安装说明。配置字幕语言与模型服务，再用示例会议检查收音和输出。

[官方说明](https://github.com/wquguru/cicada/blob/main/README.md) · [正式发行](https://github.com/wquguru/cicada/releases)

### 收录复核

2026-11-16 文档复核：已读取官方说明、许可证和提交差异。本次未安装运行，也未测试上游功能。

项目用途明确，提供可检查实现与使用文档，公开且未归档、未禁用。已确认近 3 个日历月内的功能变更。

有效维护证据：[663ef932ab](https://github.com/wquguru/cicada/commit/663ef932ab1ffc247ed4c3809beaaa03286a1614)，时间为 2026-11-14T15:01:44Z。修复 Windows 将未使用麦克风的应用判为通话的问题。已检查 windows/src/Cicada/Platform.cs 的注册表时间判断。

文章线索来自逛逛GitHub于2026-11-14发布的[五项目介绍](https://www.woshipm.com/ai/6493951.html)。本次读取作者在人人都是产品经理的署名文章。[微信链接](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538466&idx=1&sn=8ce06fbf66930fa6d90e80f5be10fa3f)用于追溯，微信正文未直接读取。功能和环境以上游说明为准。

## English

Live bilingual captions, interpreting and meeting notes for calls and streams, with transcript search and exports.

### Features

- Generate bilingual captions from system audio and organize topics and action items.
- Play translated speech into a call through the platform-specific audio setup.
- Search and edit transcripts; export meeting records and subtitles.
- Use on-device recognition on supported Macs, or configured speech services on other platforms.

### Requirements and limits

- Requires macOS 14.4+, Windows 10 2004+, Ubuntu 22.04/24.04 or Android 10+.
- Apple-silicon Macs support on-device recognition; Intel Macs and other platforms require a configured model service.
- Translation, notes and voice cloning have different service requirements; providers may receive audio or text.
- Android call apps restrict internal audio capture; in-person mode uses speaker audio.
- Project code is Apache-2.0. The optional BlackHole driver and bundled voiceprint model have separate licenses.

### Getting started

Read the platform requirements and installation guide in official Releases, configure languages and services, then test audio capture with the sample meeting.

[Official documentation](https://github.com/wquguru/cicada/blob/main/README.md) · [Releases](https://github.com/wquguru/cicada/releases)

### Review and provenance

Documentation review on 2026-11-16: official docs, the license and implementation changes were read. The project was not installed or tested.

The project has a clear purpose, inspectable implementation and usage documentation. It is public, unarchived and enabled, with a verified functional change within the last three calendar months.

Activity: [663ef932ab](https://github.com/wquguru/cicada/commit/663ef932ab1ffc247ed4c3809beaaa03286a1614) at 2026-11-14T15:01:44Z. Fixes Windows treating apps that never used the microphone as active calls. Reviewed registry timestamp checks in windows/src/Cicada/Platform.cs.

Discovery source: [the author-attributed five-project article](https://www.woshipm.com/ai/6493951.html), published by 逛逛GitHub on 2026-11-14. The WeChat URL is retained for provenance; its body was not read directly. Feature and requirement statements come from upstream documentation.

## Review evidence

```json
{
  "evaluated_at": "2026-11-16T14:21:24.299979Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "cicada",
    "name": "知了 Cicada",
    "repository": "wquguru/cicada",
    "repo_node_id": "R_kgDOVeveRQ",
    "category": "productivity",
    "summary": {
      "zh-CN": "为会议和直播提供双语字幕、同声传译与会议纪要。直接读取系统声音，支持转写搜索和记录导出。",
      "en": "Live bilingual captions, interpreting and meeting notes for calls and streams, with transcript search and exports."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:21:24.299979Z",
        "en": "2026-11-16T14:21:24.299979Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
      "source_url": "https://github.com/wquguru/cicada/blob/main/LICENSE",
      "reviewed_at": "2026-11-16T14:21:24.299979Z",
      "scope_note": "项目主许可证已读取；外部依赖与素材仍保留各自许可。"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-14T15:01:44Z",
        "reviewed_at": "2026-11-16T14:21:24.299979Z",
        "url": "https://github.com/wquguru/cicada/commit/663ef932ab1ffc247ed4c3809beaaa03286a1614",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复 Windows 将未使用麦克风的应用判为通话的问题。已检查 windows/src/Cicada/Platform.cs 的注册表时间判断。",
          "en": "Fixes Windows treating apps that never used the microphone as active calls. Reviewed registry timestamp checks in windows/src/Cicada/Platform.cs."
        },
        "reviewed_files": [
          "windows/src/Cicada/Platform.cs"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/wquguru/cicada",
        "accessed_at": "2026-11-16T14:21:24.299979Z"
      },
      {
        "url": "https://github.com/wquguru/cicada/blob/main/README.md",
        "accessed_at": "2026-11-16T14:21:24.299979Z"
      },
      {
        "url": "https://github.com/wquguru/cicada/blob/main/LICENSE",
        "accessed_at": "2026-11-16T14:21:24.299979Z"
      },
      {
        "url": "https://www.woshipm.com/ai/6493951.html",
        "accessed_at": "2026-11-16T14:21:24.299979Z",
        "supports": "2026-11-14 作者署名原创文章，明确列出仓库 URL。"
      }
    ],
    "article_source": {
      "article_id": "2247538466_1",
      "title": "搜罗了 5 个刚开源的 GitHub 项目，可以看看自己能不能用到。",
      "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538466&idx=1&sn=8ce06fbf66930fa6d90e80f5be10fa3f",
      "published_date": "2026-11-14",
      "account": "逛逛GitHub",
      "content_review_url": "https://www.woshipm.com/ai/6493951.html",
      "content_review_kind": "author-attributed original publication on Woshipm",
      "wechat_direct_body_read": false
    },
    "quality_review": {
      "zh-CN": "为会议和直播提供双语字幕、同声传译与会议纪要。直接读取系统声音，支持转写搜索和记录导出。 官方说明、使用入口和实现差异可复核。",
      "en": "Live bilingual captions, interpreting and meeting notes for calls and streams, with transcript search and exports. Official documentation, usage entry points and implementation changes are inspectable.",
      "verification_level": "docs"
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVeveRQ",
    "full_name": "wquguru/cicada",
    "stargazers_count": 2347,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
    "last_success_at": "2026-11-16T14:21:24.299979Z"
  }
}
```
