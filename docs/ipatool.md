# ipatool

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[majd/ipatool](https://github.com/majd/ipatool)

| 项目 / Field | 内容 / Value |
| --- | --- |
| 分类 / Category | 终端与 Shell / Terminal and shell |
| 状态 / Status | 已收录 / Included |
| Star | 12352 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:50:50.290410+00:00 |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:47:50.559Z |

## 中文

通过命令行搜索 App Store 应用，查看已购项目和版本。可下载账号有权取得的 IPA 或 macOS PKG 文件，并提供 MCP 接口。

**环境与限制：** 支持 macOS、Linux、Windows 和 iOS，需要已开通 App Store 的 Apple 账号；源码构建使用 Go。下载和版本可用性受账号、地区和商店服务限制，工具不提供应用付费授权或 DRM 绕过。

**入门：** 从[官方说明](https://raw.githubusercontent.com/majd/ipatool/main/README.md)确认安装与配置步骤，再查看[发布版本](https://github.com/majd/ipatool/releases)。本次为文档、许可原文与维护证据审查，未安装运行。

**近期维护：** [v2.8.1 增加并行下载和动态商店区域发现，并改进认证与已购下架应用恢复。](https://github.com/majd/ipatool/releases/tag/v2.8.1)（2026-11-11）

## English

A CLI for App Store search, purchases and versions, downloading IPA or macOS PKG packages the account is entitled to obtain; it also exposes an MCP interface.

**Requirements and limitations:** Supports macOS, Linux, Windows and iOS and requires an Apple account configured for the App Store; source builds use Go. Downloads and versions depend on account, region and store availability. The tool does not grant paid-app rights or bypass DRM.

**Getting started:** Follow the [official documentation](https://raw.githubusercontent.com/majd/ipatool/main/README.md) for setup, then check [releases](https://github.com/majd/ipatool/releases). This review examined documentation, license text and maintenance evidence; the software was not installed or run.

**Recent maintenance:** [v2.8.1 adds parallel downloads and dynamic storefront discovery, improving authentication and recovery of previously acquired delisted apps.](https://github.com/majd/ipatool/releases/tag/v2.8.1) (2026-11-11)

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
    "id": "ipatool",
    "name": "ipatool",
    "repository": "majd/ipatool",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkzNjk3NTU4NTY=",
    "category": "terminal",
    "summary": {
      "zh-CN": "通过命令行搜索 App Store 应用、查看已购项目和版本，并下载账号有权取得的 IPA 或 macOS PKG 文件；提供 MCP 接口。",
      "en": "A CLI for App Store search, purchases and versions, downloading IPA or macOS PKG packages the account is entitled to obtain; it also exposes an MCP interface."
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
      "license_sha256": "3466fcf0483597283e184031a9f1f0d142d7f41004452cf7714182742a503a95",
      "source_url": "https://github.com/majd/ipatool/blob/b352566155a667d8aaeabaa7ecec4966080f92ab/LICENSE",
      "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
      "files": [
        {
          "path": "LICENSE",
          "source_url": "https://github.com/majd/ipatool/blob/b352566155a667d8aaeabaa7ecec4966080f92ab/LICENSE",
          "fetched_at": "2026-11-16T14:48:19.969Z",
          "sha256": "3466fcf0483597283e184031a9f1f0d142d7f41004452cf7714182742a503a95",
          "source_commit": "b352566155a667d8aaeabaa7ecec4966080f92ab"
        }
      ],
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "b352566155a667d8aaeabaa7ecec4966080f92ab"
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-11-11T23:37:55Z",
        "url": "https://github.com/majd/ipatool/releases/tag/v2.8.1",
        "tag": "v2.8.1",
        "summary": "v2.8.1",
        "draft": false,
        "prerelease": false,
        "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
        "qualifies": true,
        "reason": {
          "zh-CN": "v2.8.1 增加并行下载和动态商店区域发现，并改进认证与已购下架应用恢复。",
          "en": "v2.8.1 adds parallel downloads and dynamic storefront discovery, improving authentication and recovery of previously acquired delisted apps."
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
        "https://api.github.com/repos/majd/ipatool",
        "https://raw.githubusercontent.com/majd/ipatool/main/README.md",
        "https://github.com/majd/ipatool/releases/tag/v2.8.1",
        "https://github.com/majd/ipatool/blob/b352566155a667d8aaeabaa7ecec4966080f92ab/LICENSE"
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkzNjk3NTU4NTY=",
    "full_name": "majd/ipatool",
    "stargazers_count": 12352,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "3466fcf0483597283e184031a9f1f0d142d7f41004452cf7714182742a503a95",
    "last_success_at": "2026-11-16T14:47:50.559Z"
  }
}
```

</details>
