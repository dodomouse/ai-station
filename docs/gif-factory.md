# GIF 工厂 / GIF Factory

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[WoYun520/gif-factory](https://github.com/WoYun520/gif-factory)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 1940 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:21:24.299979Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:21:24.299979Z |

## 中文

面向编码智能体的图像与动画技能集合。提供表情包、动态海报、签名、绘本和知识短片的制作说明与脚本。

### 主要功能

- 从角色图和文字制作循环 GIF，提供批量导出脚本。
- 制作动态海报、签名、片名字形和逐页绘本。
- 按主题选择知识短片流程，并检查视频与旁白文件。
- 按文章选择封面配色；封面制作需另用图像工具。

### 环境与限制

- 安装技能只添加说明和脚本，不会提供图像模型或服务额度。
- GIF 导出需要 Python 3 和 Pillow。MP4 预览另需 FFmpeg。
- 动态签名需要 NumPy、FFmpeg 和 ffprobe。其他流程按各自说明配置。
- 外部立体剖面分支另需 lemo-opuscar；外部工具与素材遵循各自许可。

### 开始使用

阅读官方使用指南，选择要制作的类型。按对应流程准备依赖，再向支持技能的智能体提供素材与要求。

[官方说明](https://github.com/WoYun520/gif-factory/blob/main/README.md) · [正式发行](https://github.com/WoYun520/gif-factory/releases)

### 收录复核

2026-11-16 文档复核：已读取官方说明、许可证和提交差异。本次未安装运行，也未测试上游功能。

项目用途明确，提供可检查实现与使用文档，公开且未归档、未禁用。已确认近 3 个日历月内的功能变更。

有效维护证据：[58031a82bc](https://github.com/WoYun520/gif-factory/commit/58031a82bc71c123605e65099b293095115cdb30)，时间为 2026-11-14T06:34:51Z。新增旁白缓存脚本 voiceover_cache.py。已检查输入校验、音频哈希、完整解码和缓存写入实现。

文章线索来自逛逛GitHub于2026-11-14发布的[五项目介绍](https://www.woshipm.com/ai/6493951.html)。本次读取作者在人人都是产品经理的署名文章。[微信链接](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538466&idx=1&sn=8ce06fbf66930fa6d90e80f5be10fa3f)用于追溯，微信正文未直接读取。功能和环境以上游说明为准。

## English

A collection of agent skills, examples and scripts for stickers, animated posters, signatures, storybooks and explanatory videos.

### Features

- Build looping GIFs from character images and text, with scripts for exporting packs.
- Create animated posters, signatures, title lettering and page-based storybooks.
- Choose explanatory-video workflows and inspect video and narration files.
- Suggest article-cover palettes; producing the cover requires separate image tools.

### Requirements and limits

- Installing the skill adds instructions and scripts, not image models or service quotas.
- GIF export needs Python 3 and Pillow; MP4 previews additionally need FFmpeg.
- Animated signatures require NumPy, FFmpeg and ffprobe. Other workflows have separate requirements.
- The external cutaway workflow requires lemo-opuscar; external tools and assets retain their own licenses.

### Getting started

Read the guide, select a workflow and prepare its dependencies, then provide assets and requirements to an agent that supports skills.

[Official documentation](https://github.com/WoYun520/gif-factory/blob/main/README.md) · [Releases](https://github.com/WoYun520/gif-factory/releases)

### Review and provenance

Documentation review on 2026-11-16: official docs, the license and implementation changes were read. The project was not installed or tested.

The project has a clear purpose, inspectable implementation and usage documentation. It is public, unarchived and enabled, with a verified functional change within the last three calendar months.

Activity: [58031a82bc](https://github.com/WoYun520/gif-factory/commit/58031a82bc71c123605e65099b293095115cdb30) at 2026-11-14T06:34:51Z. Adds voiceover_cache.py. Reviewed request validation, audio hashes, full-decode checks and cache writes.

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
    "id": "gif-factory",
    "name": "GIF 工厂 / GIF Factory",
    "repository": "WoYun520/gif-factory",
    "repo_node_id": "R_kgDOVjgRrQ",
    "category": "media",
    "summary": {
      "zh-CN": "面向编码智能体的图像与动画技能集合。提供表情包、动态海报、签名、绘本和知识短片的制作说明与脚本。",
      "en": "A collection of agent skills, examples and scripts for stickers, animated posters, signatures, storybooks and explanatory videos."
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
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "7330cdef16d47a3a9d84e8b9689c5a1aec08720477dcd096d0921efacaffd332",
      "source_url": "https://github.com/WoYun520/gif-factory/blob/e89003a4a6ca4fd0e9e39c8859851b58c82bc368/LICENSE",
      "reviewed_at": "2026-11-16T14:21:24.299979Z",
      "scope_note": "项目主许可证已读取；外部依赖与素材仍保留各自许可。",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "e89003a4a6ca4fd0e9e39c8859851b58c82bc368"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-14T06:34:51Z",
        "reviewed_at": "2026-11-16T14:21:24.299979Z",
        "url": "https://github.com/WoYun520/gif-factory/commit/58031a82bc71c123605e65099b293095115cdb30",
        "qualifies": true,
        "reason": {
          "zh-CN": "新增旁白缓存脚本 voiceover_cache.py。已检查输入校验、音频哈希、完整解码和缓存写入实现。",
          "en": "Adds voiceover_cache.py. Reviewed request validation, audio hashes, full-decode checks and cache writes."
        },
        "reviewed_files": [
          "skills/paper-mechanism-explainer/scripts/voiceover_cache.py"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/WoYun520/gif-factory",
        "accessed_at": "2026-11-16T14:21:24.299979Z"
      },
      {
        "url": "https://github.com/WoYun520/gif-factory/blob/main/README.md",
        "accessed_at": "2026-11-16T14:21:24.299979Z"
      },
      {
        "url": "https://github.com/WoYun520/gif-factory/blob/e89003a4a6ca4fd0e9e39c8859851b58c82bc368/LICENSE",
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
      "zh-CN": "面向编码智能体的图像与动画技能集合。提供表情包、动态海报、签名、绘本和知识短片的制作说明与脚本。 官方说明、使用入口和实现差异可复核。",
      "en": "A collection of agent skills, examples and scripts for stickers, animated posters, signatures, storybooks and explanatory videos. Official documentation, usage entry points and implementation changes are inspectable.",
      "verification_level": "docs"
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVjgRrQ",
    "full_name": "WoYun520/gif-factory",
    "stargazers_count": 1940,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "7330cdef16d47a3a9d84e8b9689c5a1aec08720477dcd096d0921efacaffd332",
    "last_success_at": "2026-11-16T14:21:24.299979Z"
  }
}
```

</details>
