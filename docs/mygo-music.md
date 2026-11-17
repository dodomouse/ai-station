# MyGo Music

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[egoist/mygo-music](https://github.com/egoist/mygo-music)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 1408 |
| 许可证 / License | AGPL-3.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:21:24.299979Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:21:24.299979Z |

## 中文

原生桌面音乐播放器，支持本地音乐、歌词、播放列表和插件。插件可接入音乐目录、播客和电台。

### 主要功能

- 播放本地 MP3、FLAC、Ogg Vorbis、WAV、M4A 和 AAC 文件。
- 显示专辑封面和歌词，管理播放列表、收藏和播放队列。
- 通过插件扩展账号、音乐目录、播客、电台和页面。
- 按需下载 sherpa-onnx 与 Qwen3-ASR，在本机生成播客字幕。

### 环境与限制

- 桌面版本覆盖 macOS、Windows 和 Linux。源码构建使用 Go 和 MyGo。
- 第三方音乐来源需要对应插件。服务账号、内容许可与费用取决于来源。
- 插件密码控件只遮蔽界面显示，设置仍以明文 JSON 保存。
- 插件申请进程权限后可以运行本机程序。安装前需检查插件来源与权限。

### 开始使用

从官方 Releases 选择系统对应的安装包。导入本地音乐后，再按需要配置插件。

[官方说明](https://github.com/egoist/mygo-music/blob/main/README.md) · [正式发行](https://github.com/egoist/mygo-music/releases)

### 收录复核

2026-11-16 文档复核：已读取官方说明、许可证和提交差异。本次未安装运行，也未测试上游功能。

项目用途明确，提供可检查实现与使用文档，公开且未归档、未禁用。已确认近 3 个日历月内的功能变更。

有效维护证据：[93b7ceab2c](https://github.com/egoist/mygo-music/commit/93b7ceab2c97c94ea4dd8d60f1c1fed569b1d67b)，时间为 2026-11-14T10:58:26Z。增加黑胶唱机和磁带播放页。已检查 internal/app/ui_retro.go、retro_render.go 与设置代码差异。

文章线索来自逛逛GitHub于2026-11-14发布的[五项目介绍](https://www.woshipm.com/ai/6493951.html)。本次读取作者在人人都是产品经理的署名文章。[微信链接](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538466&idx=1&sn=8ce06fbf66930fa6d90e80f5be10fa3f)用于追溯，微信正文未直接读取。功能和环境以上游说明为准。

## English

A native desktop music player for local files, lyrics and playlists, with plugins for catalogs, podcasts and radio.

### Features

- Play local MP3, FLAC, Ogg Vorbis, WAV, M4A and AAC files.
- Show cover art and lyrics; manage playlists, favorites and the play queue.
- Extend accounts, catalogs, podcasts, radio and pages through plugins.
- Download sherpa-onnx and Qwen3-ASR on request for on-device podcast captions.

### Requirements and limits

- Desktop builds target macOS, Windows and Linux. Building from source uses Go and MyGo.
- External catalogs require plugins; accounts, content rights and charges depend on the provider.
- Password controls mask the display, but settings remain plaintext JSON.
- A plugin granted process access can run local programs; review its origin and requested permissions.

### Getting started

Choose a matching build from official Releases, add local music, then configure any plugins you need.

[Official documentation](https://github.com/egoist/mygo-music/blob/main/README.md) · [Releases](https://github.com/egoist/mygo-music/releases)

### Review and provenance

Documentation review on 2026-11-16: official docs, the license and implementation changes were read. The project was not installed or tested.

The project has a clear purpose, inspectable implementation and usage documentation. It is public, unarchived and enabled, with a verified functional change within the last three calendar months.

Activity: [93b7ceab2c](https://github.com/egoist/mygo-music/commit/93b7ceab2c97c94ea4dd8d60f1c1fed569b1d67b) at 2026-11-14T10:58:26Z. Adds vinyl and cassette player views. Reviewed changes in internal/app/ui_retro.go, retro_render.go and settings code.

Discovery source: [the author-attributed five-project article](https://www.woshipm.com/ai/6493951.html), published by 逛逛GitHub on 2026-11-14. The WeChat URL is retained for provenance; its body was not read directly. Feature and requirement statements come from upstream documentation.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:21:24.299979Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "mygo-music",
    "name": "MyGo Music",
    "repository": "egoist/mygo-music",
    "repo_node_id": "R_kgDOViuR6A",
    "category": "media",
    "summary": {
      "zh-CN": "原生桌面音乐播放器，支持本地音乐、歌词、播放列表和插件。插件可接入音乐目录、播客和电台。",
      "en": "A native desktop music player for local files, lyrics and playlists, with plugins for catalogs, podcasts and radio."
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
      "spdx": "AGPL-3.0",
      "osi_approved": true,
      "license_sha256": "0d96a4ff68ad6d4b6f1f30f713b18d5184912ba8dd389f86aa7710db079abcb0",
      "source_url": "https://github.com/egoist/mygo-music/blob/298c88a03407844ac1c4eb76e3590edfe4577121/LICENSE",
      "reviewed_at": "2026-11-16T14:21:24.299979Z",
      "scope_note": "项目主许可证已读取；外部依赖与素材仍保留各自许可。",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "298c88a03407844ac1c4eb76e3590edfe4577121"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-14T10:58:26Z",
        "reviewed_at": "2026-11-16T14:21:24.299979Z",
        "url": "https://github.com/egoist/mygo-music/commit/93b7ceab2c97c94ea4dd8d60f1c1fed569b1d67b",
        "qualifies": true,
        "reason": {
          "zh-CN": "增加黑胶唱机和磁带播放页。已检查 internal/app/ui_retro.go、retro_render.go 与设置代码差异。",
          "en": "Adds vinyl and cassette player views. Reviewed changes in internal/app/ui_retro.go, retro_render.go and settings code."
        },
        "reviewed_files": [
          "internal/app/ui_retro.go",
          "internal/app/retro_render.go",
          "internal/app/settings.go"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/egoist/mygo-music",
        "accessed_at": "2026-11-16T14:21:24.299979Z"
      },
      {
        "url": "https://github.com/egoist/mygo-music/blob/main/README.md",
        "accessed_at": "2026-11-16T14:21:24.299979Z"
      },
      {
        "url": "https://github.com/egoist/mygo-music/blob/298c88a03407844ac1c4eb76e3590edfe4577121/LICENSE",
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
      "zh-CN": "原生桌面音乐播放器，支持本地音乐、歌词、播放列表和插件。插件可接入音乐目录、播客和电台。 官方说明、使用入口和实现差异可复核。",
      "en": "A native desktop music player for local files, lyrics and playlists, with plugins for catalogs, podcasts and radio. Official documentation, usage entry points and implementation changes are inspectable.",
      "verification_level": "docs"
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOViuR6A",
    "full_name": "egoist/mygo-music",
    "stargazers_count": 1408,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "AGPL-3.0",
    "license_sha256": "0d96a4ff68ad6d4b6f1f30f713b18d5184912ba8dd389f86aa7710db079abcb0",
    "last_success_at": "2026-11-16T14:21:24.299979Z"
  }
}
```

</details>
