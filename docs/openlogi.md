# OpenLogi

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[AprilNEA/OpenLogi](https://github.com/AprilNEA/OpenLogi)

| 项目 / Field | 内容 / Value |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 25783 |
| 许可证 / License | MIT OR Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:50:50.290410+00:00 |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:20:19.330Z |

## 中文

Rust 原生 Logitech 设备工具，通过 HID++/UVC 配置鼠标、键盘与摄像头。功能包括按钮、DPI、滚轮配置和跨电脑 Flow。

**环境与限制：** 支持 Windows、macOS、Linux。可用功能取决于具体设备和系统权限。项目仍在快速开发，配置格式与兼容性需查看当前版本说明。

**入门：** 从[官方说明](https://raw.githubusercontent.com/AprilNEA/OpenLogi/master/README.md)确认安装与配置步骤，再查看[发布版本](https://github.com/AprilNEA/OpenLogi/releases)。本次为文档、许可原文与维护证据审查，未安装运行。

**近期维护：** [v0.9.0 发布跨电脑 Flow 功能。](https://github.com/AprilNEA/OpenLogi/releases/tag/v0.9.0)（2026-11-03）

## English

A native Rust Logitech-device tool using HID++/UVC for mouse, keyboard and webcam settings, including buttons, DPI, scrolling and cross-computer Flow.

**Requirements and limitations:** Supports Windows, macOS and Linux, with capabilities depending on hardware and OS permissions. Development is active; check current release notes for configuration and compatibility changes.

**Getting started:** Follow the [official documentation](https://raw.githubusercontent.com/AprilNEA/OpenLogi/master/README.md) for setup, then check [releases](https://github.com/AprilNEA/OpenLogi/releases). This review examined documentation, license text and maintenance evidence; the software was not installed or run.

**Recent maintenance:** [v0.9.0 releases cross-computer Flow.](https://github.com/AprilNEA/OpenLogi/releases/tag/v0.9.0) (2026-11-03)

## Review evidence

发现线索来自第三方公众号文章索引，原始微信正文未完整读取；用途、环境、许可与维护状态依据仓库当前资料复核。

Discovery uses a third-party WeChat article index; the original article body was not fully read. Current repository sources were reviewed for function, requirements, licensing and maintenance.

- 公众号索引原文 / Indexed WeChat source：[一周没逛 GitHub 不要紧，这 TOP 10 的热门开源项目整理好了。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536122&idx=1&sn=b7a284d06296707235d8dde07c6f6d4e)（2026-08-23）

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
    "id": "openlogi",
    "name": "OpenLogi",
    "repository": "AprilNEA/OpenLogi",
    "repo_node_id": "R_kgDOSmXwow",
    "category": "productivity",
    "summary": {
      "zh-CN": "Rust 原生 Logitech 设备工具，通过 HID++/UVC 配置鼠标、键盘与摄像头，提供按钮、DPI、滚轮和跨电脑 Flow 等能力。",
      "en": "A native Rust Logitech-device tool using HID++/UVC for mouse, keyboard and webcam settings, including buttons, DPI, scrolling and cross-computer Flow."
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
      "spdx": "MIT OR Apache-2.0",
      "osi_approved": true,
      "license_sha256": "bf94bc462c2d978803800ee4287629a79756ceb47f1eab26a04cb65d8aa62f2e",
      "source_url": "https://github.com/AprilNEA/OpenLogi/blob/9ca7ef0cbd1f4577ffdc338f8288f8c3a410f013/LICENSE-APACHE",
      "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
      "files": [
        {
          "path": "LICENSE-APACHE",
          "source_url": "https://github.com/AprilNEA/OpenLogi/blob/9ca7ef0cbd1f4577ffdc338f8288f8c3a410f013/LICENSE-APACHE",
          "fetched_at": "2026-11-16T14:23:40.992Z",
          "sha256": "bf94bc462c2d978803800ee4287629a79756ceb47f1eab26a04cb65d8aa62f2e",
          "source_commit": "9ca7ef0cbd1f4577ffdc338f8288f8c3a410f013"
        },
        {
          "path": "LICENSE-MIT",
          "source_url": "https://github.com/AprilNEA/OpenLogi/blob/9ca7ef0cbd1f4577ffdc338f8288f8c3a410f013/LICENSE-MIT",
          "fetched_at": "2026-11-16T14:23:40.671Z",
          "sha256": "ab94bd99807f525cb149219a0fda80eac91d6003689c010405698500867dc1b0",
          "source_commit": "9ca7ef0cbd1f4577ffdc338f8288f8c3a410f013"
        }
      ],
      "scope": "Original project code offered under MIT OR Apache-2.0.",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "9ca7ef0cbd1f4577ffdc338f8288f8c3a410f013"
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-11-03T23:47:35Z",
        "url": "https://github.com/AprilNEA/OpenLogi/releases/tag/v0.9.0",
        "tag": "v0.9.0",
        "summary": "v0.9.0",
        "draft": false,
        "prerelease": false,
        "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
        "qualifies": true,
        "reason": {
          "zh-CN": "v0.9.0 发布跨电脑 Flow 功能。",
          "en": "v0.9.0 releases cross-computer Flow."
        }
      }
    ],
    "sources": [
      {
        "article_id": "2247536122_1",
        "title": "一周没逛 GitHub 不要紧，这 TOP 10 的热门开源项目整理好了。",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536122&idx=1&sn=b7a284d06296707235d8dde07c6f6d4e",
        "published_date": "2026-08-23",
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
        "https://api.github.com/repos/aprilnea/openlogi",
        "https://raw.githubusercontent.com/AprilNEA/OpenLogi/master/README.md",
        "https://github.com/AprilNEA/OpenLogi/releases/tag/v0.9.0",
        "https://github.com/AprilNEA/OpenLogi/blob/9ca7ef0cbd1f4577ffdc338f8288f8c3a410f013/LICENSE-APACHE"
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOSmXwow",
    "full_name": "AprilNEA/OpenLogi",
    "stargazers_count": 25783,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "bf94bc462c2d978803800ee4287629a79756ceb47f1eab26a04cb65d8aa62f2e",
    "last_success_at": "2026-11-16T14:20:19.330Z"
  }
}
```

</details>
