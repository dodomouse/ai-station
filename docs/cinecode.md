# cinecode

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[sarpstar/cinecode](https://github.com/sarpstar/cinecode)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 2593 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:21:24.299979Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:21:24.299979Z |

## 中文

面向编码智能体的影片制作技能。用网页画布或 Three.js 编排画面与声音，通过浏览器和 FFmpeg 输出 MP4。

### 主要功能

- 用 Canvas 或 Three.js 创建画面、镜头、文字和转场。
- 按快速模式或影片模式组织脚本、预览、修改和成片。
- 制作短片、讲解视频、广告、产品影片与音乐视频。
- 提供逐帧采集、混音、响度处理和质量检查脚本。

### 环境与限制

- 需要能运行本机工具的编码智能体。官方推荐 Claude Code，也说明了其他智能体入口。
- 需要 Node.js 22+、Python 3.9+、FFmpeg 和 Chrome 兼容浏览器。
- 浏览器需要可用的图形处理器。影片模式渲染通常占用数 GB 临时空间。
- 配音服务和素材另有条件。Claude Code 专用守卫钩子不适用于所有智能体。

### 开始使用

阅读官方中文或英文说明。准备独立影片目录，在支持的智能体中提供主题、时长、画幅和声音要求。

[官方说明](https://github.com/sarpstar/cinecode/blob/main/README.en.md) · [正式发行](https://github.com/sarpstar/cinecode/releases)

### 收录复核

2026-11-16 文档复核：已读取官方说明、许可证和提交差异。本次未安装运行，也未测试上游功能。

项目用途明确，提供可检查实现与使用文档，公开且未归档、未禁用。已确认近 3 个日历月内的功能变更。

有效维护证据：[6fcbcf7845](https://github.com/sarpstar/cinecode/commit/6fcbcf7845053200c704ade1982ae599e5742855)，时间为 2026-11-03T10:23:17Z。修复 Windows 下影片记忆锁的并发删除问题。已检查 scripts/dice.py 对 PermissionError 和锁删除重试的处理。

文章线索来自逛逛GitHub于2026-11-14发布的[五项目介绍](https://www.woshipm.com/ai/6493951.html)。本次读取作者在人人都是产品经理的署名文章。[微信链接](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538466&idx=1&sn=8ce06fbf66930fa6d90e80f5be10fa3f)用于追溯，微信正文未直接读取。功能和环境以上游说明为准。

## English

An agent skill for making films with code, using browser scenes, sound design and FFmpeg to produce MP4 files.

### Features

- Build scenes, cameras, text and transitions with Canvas or Three.js.
- Organize scripts, previews, revisions and rendering through Quick or Film mode.
- Produce short films, explainers, ads, product videos and music videos.
- Use helpers for frame capture, mixing, loudness processing and quality checks.

### Requirements and limits

- Requires an agent that can run local tools. Claude Code is the recommended setup, with other agent entry points documented.
- Requires Node.js 22+, Python 3.9+, FFmpeg and a Chrome-compatible browser.
- The browser needs a working GPU; Film mode uses several GB of temporary space.
- Narration providers and assets have separate conditions. Claude Code guard hooks do not apply to every agent.

### Getting started

Read the official Chinese or English guide, prepare a separate film folder and give the agent a subject, duration, format and sound requirements.

[Official documentation](https://github.com/sarpstar/cinecode/blob/main/README.en.md) · [Releases](https://github.com/sarpstar/cinecode/releases)

### Review and provenance

Documentation review on 2026-11-16: official docs, the license and implementation changes were read. The project was not installed or tested.

The project has a clear purpose, inspectable implementation and usage documentation. It is public, unarchived and enabled, with a verified functional change within the last three calendar months.

Activity: [6fcbcf7845](https://github.com/sarpstar/cinecode/commit/6fcbcf7845053200c704ade1982ae599e5742855) at 2026-11-03T10:23:17Z. Fixes concurrent film-memory lock deletion on Windows. Reviewed PermissionError handling and lock-removal retries in scripts/dice.py.

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
    "id": "cinecode",
    "name": "cinecode",
    "repository": "sarpstar/cinecode",
    "repo_node_id": "R_kgDOVhNo0Q",
    "category": "media",
    "summary": {
      "zh-CN": "面向编码智能体的影片制作技能。用网页画布或 Three.js 编排画面与声音，通过浏览器和 FFmpeg 输出 MP4。",
      "en": "An agent skill for making films with code, using browser scenes, sound design and FFmpeg to produce MP4 files."
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
      "license_sha256": "a27dda60518acb8211ccc3181914539556117cd00930d1adbae504ef63b793c9",
      "source_url": "https://github.com/sarpstar/cinecode/blob/c8a3e7552699360a2b0142c9620882af2069eedb/LICENSE",
      "reviewed_at": "2026-11-16T14:21:24.299979Z",
      "scope_note": "项目主许可证已读取；外部依赖与素材仍保留各自许可。",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "c8a3e7552699360a2b0142c9620882af2069eedb"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-03T10:23:17Z",
        "reviewed_at": "2026-11-16T14:21:24.299979Z",
        "url": "https://github.com/sarpstar/cinecode/commit/6fcbcf7845053200c704ade1982ae599e5742855",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复 Windows 下影片记忆锁的并发删除问题。已检查 scripts/dice.py 对 PermissionError 和锁删除重试的处理。",
          "en": "Fixes concurrent film-memory lock deletion on Windows. Reviewed PermissionError handling and lock-removal retries in scripts/dice.py."
        },
        "reviewed_files": [
          "scripts/dice.py"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/sarpstar/cinecode",
        "accessed_at": "2026-11-16T14:21:24.299979Z"
      },
      {
        "url": "https://github.com/sarpstar/cinecode/blob/main/README.en.md",
        "accessed_at": "2026-11-16T14:21:24.299979Z"
      },
      {
        "url": "https://github.com/sarpstar/cinecode/blob/c8a3e7552699360a2b0142c9620882af2069eedb/LICENSE",
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
      "zh-CN": "面向编码智能体的影片制作技能。用网页画布或 Three.js 编排画面与声音，通过浏览器和 FFmpeg 输出 MP4。 官方说明、使用入口和实现差异可复核。",
      "en": "An agent skill for making films with code, using browser scenes, sound design and FFmpeg to produce MP4 files. Official documentation, usage entry points and implementation changes are inspectable.",
      "verification_level": "docs"
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVhNo0Q",
    "full_name": "sarpstar/cinecode",
    "stargazers_count": 2593,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "a27dda60518acb8211ccc3181914539556117cd00930d1adbae504ef63b793c9",
    "last_success_at": "2026-11-16T14:21:24.299979Z"
  }
}
```

</details>
