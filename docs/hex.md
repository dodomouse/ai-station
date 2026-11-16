# Hex

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[anomalyco/hex](https://github.com/anomalyco/hex)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 7045 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:24:08.700270Z |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:18:51.558Z |

## 中文

### 用途与功能

在本机把语音转成文字并输入当前应用。支持词汇表、转写历史、文本处理步骤和录音文件转写。

适合日常语音输入和录音整理。提供命令行、本地认证 API 和 TypeScript SDK。部分录屏和会议功能仍在实验区。

### 环境与限制

支持 macOS、Windows 和 Linux，首次使用需下载语音模型。识别速度和语言支持取决于模型。可选 OpenCode 改写需要另查其服务与数据流，不能等同基础离线听写。

### 入门与收录判断

从[官方 README](https://github.com/anomalyco/hex/blob/dev/README.md)查阅安装和配置步骤。离线听写之外提供可配置输出管道，适合对术语和应用文本格式有固定要求的用户。

本轮为文档复核，未安装、运行或测试上游软件。正式 v3.4.0 发布包含安装升级及使用行为改进。详见[维护记录](https://github.com/anomalyco/hex/releases/tag/v3.4.0)。

### 文章来源

公众号“逛逛GitHub”的[微信原文](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538420&idx=1&sn=9769127e763c53057c449032da509279)，索引日期为 2026-11-09。本次读取了作者在[人人都是产品经理发布的正文](https://www.woshipm.com/share/6491406.html)，该页日期为 2026-11-10。功能和限制另按当前上游复核。

## English

### Purpose and features

On-device dictation that pastes into the active application, with vocabulary, history, processing steps and file transcription.

Offers a CLI, authenticated local API and TypeScript SDK. Some meeting and annotation features remain experimental.

### Requirements and limits

Supports macOS, Windows and Linux and downloads a speech model first. Language coverage and performance depend on the model. Optional OpenCode rewriting has separate service and data-flow requirements.

### Getting started and review

Use the [official README](https://github.com/anomalyco/hex/blob/dev/README.md) for installation and configuration. This is a documentation review; the software was not installed or tested. Stable v3.4.0 includes installation, update and user-facing improvements. See the [release](https://github.com/anomalyco/hex/releases/tag/v3.4.0).

The original WeChat article is dated 2026-11-09 in the public index. Its author-published mirror is dated 2026-11-10. The mirror establishes the article association; current upstream documentation supports the feature descriptions.

## Review evidence

```json
{
  "evaluated_at": "2026-11-16T14:24:08.700270Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "hex",
    "name": "Hex",
    "repository": "anomalyco/hex",
    "repo_node_id": "R_kgDOTcCg9w",
    "category": "media",
    "summary": {
      "zh-CN": "在本机把语音转成文字并输入当前应用。支持词汇表、转写历史、文本处理步骤和录音文件转写。",
      "en": "On-device dictation that pastes into the active application, with vocabulary, history, processing steps and file transcription."
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
      "basis": "离线听写之外提供可配置输出管道，适合对术语和应用文本格式有固定要求的用户。",
      "stars_are_advisory": true,
      "reviewed_at": "2026-11-16T14:24:08.700270Z"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "0c267f186f600c6f4d9d229d1792861361f2c433cfb23054fece61f227006344",
      "source_url": "https://github.com/anomalyco/hex/blob/dev/LICENSE",
      "reviewed_at": "2026-11-16T14:24:08.700270Z"
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-11-11T04:30:30Z",
        "reviewed_at": "2026-11-16T14:24:08.700270Z",
        "url": "https://github.com/anomalyco/hex/releases/tag/v3.4.0",
        "qualifies": true,
        "reason": {
          "zh-CN": "正式 v3.4.0 发布包含安装升级及使用行为改进。",
          "en": "Stable v3.4.0 includes installation, update and user-facing improvements."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/anomalyco/hex",
        "accessed_at": "2026-11-16T14:18:51.558Z",
        "supports": "Repository identity, Stars and public state."
      },
      {
        "url": "https://github.com/anomalyco/hex/blob/dev/README.md",
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
    "repo_node_id": "R_kgDOTcCg9w",
    "full_name": "anomalyco/hex",
    "stargazers_count": 7045,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "0c267f186f600c6f4d9d229d1792861361f2c433cfb23054fece61f227006344",
    "last_success_at": "2026-11-16T14:18:51.558Z"
  }
}
```
