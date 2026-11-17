# Handy

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[cjpais/Handy](https://github.com/cjpais/Handy)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 38948 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:24:08.700270Z |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:18:51.825Z |

## 中文

### 用途与功能

通过快捷键录音，在本地识别语音，再把文字粘贴到当前输入位置。可选择 Whisper 或 Parakeet 等模型。

适合日常听写和辅助输入。提供语音活动检测、转写历史及命令行控制。macOS 和 Linux 还支持转写后处理脚本。

### 环境与限制

支持 Windows、macOS 和 Linux。需要麦克风及相应系统权限，首次需下载模型。Linux 粘贴依赖显示协议和输入工具；蓝牙麦克风、管理员应用和快捷键存在平台限制。可选模型后处理须单独确认联网行为。

### 入门与收录判断

从[官方 README](https://github.com/cjpais/Handy/blob/main/README.md)查阅安装和配置步骤。用单一快捷键完成录音到输入，文档明确列出平台差异和已知限制。

本轮为文档复核，未安装、运行或测试上游软件。正式 v0.10.1 修复 Linux 终端粘贴、录音覆盖层和依赖问题。详见[维护记录](https://github.com/cjpais/Handy/releases/tag/v0.10.1)。

### 文章来源

公众号“逛逛GitHub”的[微信原文](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538420&idx=1&sn=9769127e763c53057c449032da509279)，索引日期为 2026-11-09。本次读取了作者在[人人都是产品经理发布的正文](https://www.woshipm.com/share/6491406.html)，该页日期为 2026-11-10。功能和限制另按当前上游复核。

## English

### Purpose and features

Shortcut-driven local speech recognition that pastes text into the current field, with model choices including Whisper and Parakeet.

Includes voice activity detection, transcript history and CLI controls. macOS and Linux support a transcription hook.

### Requirements and limits

Requires a microphone, system permissions and a downloaded model. Linux paste behavior depends on the display server and input utilities. Bluetooth microphones, elevated apps and shortcuts have platform-specific limits; optional model post-processing needs a separate privacy review.

### Getting started and review

Use the [official README](https://github.com/cjpais/Handy/blob/main/README.md) for installation and configuration. This is a documentation review; the software was not installed or tested. Stable v0.10.1 fixes Linux terminal pasting, the recording overlay and dependencies. See the [release](https://github.com/cjpais/Handy/releases/tag/v0.10.1).

The original WeChat article is dated 2026-11-09 in the public index. Its author-published mirror is dated 2026-11-10. The mirror establishes the article association; current upstream documentation supports the feature descriptions.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:24:08.700270Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "handy",
    "name": "Handy",
    "repository": "cjpais/Handy",
    "repo_node_id": "R_kgDON4t-Ng",
    "category": "media",
    "summary": {
      "zh-CN": "通过快捷键录音，在本地识别语音，再把文字粘贴到当前输入位置。可选择 Whisper 或 Parakeet 等模型。",
      "en": "Shortcut-driven local speech recognition that pastes text into the current field, with model choices including Whisper and Parakeet."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:24:08.700270Z",
        "en": "2026-11-16T14:24:08.700270Z"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "basis": "用单一快捷键完成录音到输入，文档明确列出平台差异和已知限制。",
      "stars_are_advisory": true,
      "reviewed_at": "2026-11-16T14:24:08.700270Z"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "3564e8ec14055ed54f896e8660a62627ea4fc3a1b64f72b798593df00e1f4edc",
      "source_url": "https://github.com/cjpais/Handy/blob/aca8985190c3ad7f361d8a80cb30f179513ed690/LICENSE",
      "reviewed_at": "2026-11-16T14:24:08.700270Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "aca8985190c3ad7f361d8a80cb30f179513ed690"
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-11-14T08:50:18Z",
        "reviewed_at": "2026-11-16T14:24:08.700270Z",
        "url": "https://github.com/cjpais/Handy/releases/tag/v0.10.1",
        "qualifies": true,
        "reason": {
          "zh-CN": "正式 v0.10.1 修复 Linux 终端粘贴、录音覆盖层和依赖问题。",
          "en": "Stable v0.10.1 fixes Linux terminal pasting, the recording overlay and dependencies."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/cjpais/Handy",
        "accessed_at": "2026-11-16T14:18:51.825Z",
        "supports": "Repository identity, Stars and public state."
      },
      {
        "url": "https://github.com/cjpais/Handy/blob/main/README.md",
        "accessed_at": "2026-11-16T14:24:08.700270Z",
        "supports": "Capabilities, requirements and limits."
      },
      {
        "url": "https://www.woshipm.com/share/6491406.html",
        "published_date": "2026-11-10",
        "accessed_at": "2026-11-16T14:24:08.700270Z",
        "supports": "Article body and account attribution verified on the author-published mirror."
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538420&idx=1&sn=9769127e763c53057c449032da509279",
        "published_date": "2026-11-09",
        "supports": "Original WeChat URL and date from the public article index; original body unavailable."
      }
    ],
    "discovery": {
      "account": "逛逛GitHub",
      "article": {
        "article_id": "2247538420_1",
        "title": "7 个近期 GitHub 上贼火火的开源项目，又是质量很高的一波。",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538420&idx=1&sn=9769127e763c53057c449032da509279",
        "published_date": "2026-11-09"
      },
      "index_url": "https://www.noking.tech/github-radar/",
      "body_verification": "author_published_mirror"
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDON4t-Ng",
    "full_name": "cjpais/Handy",
    "stargazers_count": 38948,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "3564e8ec14055ed54f896e8660a62627ea4fc3a1b64f72b798593df00e1f4edc",
    "last_success_at": "2026-11-16T14:18:51.825Z"
  }
}
```

</details>
