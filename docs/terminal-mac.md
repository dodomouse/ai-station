# terminal-mac

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[govijr/terminal-mac](https://github.com/govijr/terminal-mac)

| 项目 / Field | 内容 / Value |
| --- | --- |
| 分类 / Category | 终端与 Shell / Terminal and shell |
| 状态 / Status | 已收录 / Included |
| Star | 2795 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:50:50.290410+00:00 |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:18:43.846Z |

## 中文

为电脑操作 Agent 启动独立 macOS 虚拟机，把画面流式显示在终端，并提供输入控制接口。

**环境与限制：** 需要 Apple Silicon、macOS 14+。从源码构建需 Xcode 16 / Swift 6，终端需支持 Kitty 或 iTerm2 图像协议。首次运行下载系统镜像，客机独立登录。屏幕录制和辅助功能权限需在客机配置，当前仍为早期版本。

**入门：** 从[官方说明](https://raw.githubusercontent.com/govijr/terminal-mac/main/README.md)确认安装与配置步骤，再查看[发布版本](https://github.com/govijr/terminal-mac/releases)。本次为文档、许可原文与维护证据审查，未安装运行。

**近期维护：** [提交修复 Unicode 输入事件边界处的空白上下文，并增加回归测试。](https://github.com/govijr/terminal-mac/commit/66458219780a710b683af7fdd6e59be872a29939)（2026-11-09）

## English

Runs an isolated macOS virtual machine for computer-use agents, streaming its display into a terminal and exposing input controls.

**Requirements and limitations:** Requires Apple Silicon and macOS 14+; source builds need Xcode 16 / Swift 6 and a Kitty- or iTerm2-compatible image terminal. Initial setup downloads a system image. Guest accounts and screen-recording/accessibility permissions require separate setup; this is early-stage software.

**Getting started:** Follow the [official documentation](https://raw.githubusercontent.com/govijr/terminal-mac/main/README.md) for setup, then check [releases](https://github.com/govijr/terminal-mac/releases). This review examined documentation, license text and maintenance evidence; the software was not installed or run.

**Recent maintenance:** [The inspected commit preserves whitespace at Unicode input boundaries and adds regression tests.](https://github.com/govijr/terminal-mac/commit/66458219780a710b683af7fdd6e59be872a29939) (2026-11-09)

## Review evidence

发现线索来自第三方公众号文章索引，原始微信正文未完整读取；用途、环境、许可与维护状态依据仓库当前资料复核。

Discovery uses a third-party WeChat article index; the original article body was not fully read. Current repository sources were reviewed for function, requirements, licensing and maintenance.

- 公众号索引原文 / Indexed WeChat source：[有个刚开源的 GitHub 项目贼有说法，竟然能在终端里再跑一台 Mac。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538388&idx=1&sn=76b1287f4a12472c0ea4c90697d47571)（2026-11-08）

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
    "id": "terminal-mac",
    "name": "terminal-mac",
    "repository": "govijr/terminal-mac",
    "repo_node_id": "R_kgDOVg4HSg",
    "category": "terminal",
    "summary": {
      "zh-CN": "为电脑操作 Agent 启动独立 macOS 虚拟机，把画面流式显示在终端，并提供输入控制接口。",
      "en": "Runs an isolated macOS virtual machine for computer-use agents, streaming its display into a terminal and exposing input controls."
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
      "license_sha256": "97a617246303da2c1ec23133cbbe1dc6c99705948dd763a0845b1d508fb94a39",
      "source_url": "https://raw.githubusercontent.com/govijr/terminal-mac/main/LICENSE",
      "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
      "files": [
        {
          "path": "LICENSE",
          "source_url": "https://raw.githubusercontent.com/govijr/terminal-mac/main/LICENSE",
          "fetched_at": "2026-11-16T14:23:16.438Z",
          "sha256": "97a617246303da2c1ec23133cbbe1dc6c99705948dd763a0845b1d508fb94a39"
        }
      ]
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-09T21:47:36Z",
        "url": "https://github.com/govijr/terminal-mac/commit/66458219780a710b683af7fdd6e59be872a29939",
        "sha": "66458219780a710b683af7fdd6e59be872a29939",
        "summary": "Preserve whitespace context at Unicode event boundaries",
        "files": [
          "Sources/TerminalMacCore/UnicodeText.swift",
          "Tests/TerminalMacCoreTests/UnicodeTextTests.swift"
        ],
        "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
        "qualifies": true,
        "reason": {
          "zh-CN": "提交修复 Unicode 输入事件边界处的空白上下文，并增加回归测试。",
          "en": "The inspected commit preserves whitespace at Unicode input boundaries and adds regression tests."
        }
      }
    ],
    "sources": [
      {
        "article_id": "2247538388_1",
        "title": "有个刚开源的 GitHub 项目贼有说法，竟然能在终端里再跑一台 Mac。",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538388&idx=1&sn=76b1287f4a12472c0ea4c90697d47571",
        "published_date": "2026-11-08",
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
        "https://api.github.com/repos/govijr/terminal-mac",
        "https://raw.githubusercontent.com/govijr/terminal-mac/main/README.md",
        "https://github.com/govijr/terminal-mac/commit/66458219780a710b683af7fdd6e59be872a29939",
        "https://raw.githubusercontent.com/govijr/terminal-mac/main/LICENSE"
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVg4HSg",
    "full_name": "govijr/terminal-mac",
    "stargazers_count": 2795,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "97a617246303da2c1ec23133cbbe1dc6c99705948dd763a0845b1d508fb94a39",
    "last_success_at": "2026-11-16T14:18:43.846Z"
  }
}
```

</details>
