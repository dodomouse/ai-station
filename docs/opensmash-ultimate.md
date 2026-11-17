# OpenSmash-Ultimate

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[OpenSmash-Ultimate/OpenSmash-Ultimate](https://github.com/OpenSmash-Ultimate/OpenSmash-Ultimate)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 188 |
| 许可证 / License | GPL-3.0-or-later |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:58:29.135174Z |

## 中文

通过静态重编译研究让用户自备的特定 Switch 游戏在桌面平台运行。

### 主要功能

- 合并 WindowSmash 与 ssbu-recomp，提供转换工具、运行时和图形启动器。
- 包含构建诊断、控制器输入和可选联机组件。

### 环境与限制

- 主要需要 64 位 Windows 10/11 与约 60 GB 可用空间，Linux 和 Apple 芯片 Mac 支持仍属实验性。
- 用户需自备有权使用的游戏与密钥，GPL-3.0-or-later 仅覆盖项目源码，不授权游戏数据，外部组件另有许可。

### 开始使用

从[官方说明](https://github.com/OpenSmash-Ultimate/OpenSmash-Ultimate/blob/main/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/OpenSmash-Ultimate/OpenSmash-Ultimate/releases)可用于确认版本。

### 收录复核

公众号文章提及旧仓 ssbu-recomp。旧仓和本仓 README 均确认合并迁移，本文收录当前后继仓。

通过静态重编译研究让用户自备的特定 Switch 游戏在桌面平台运行。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。 Star 较少，依据具体用途、实现和可复核文档收录；未据此推断成熟度或持续维护能力。

有效维护证据：[8539f9bf02](https://github.com/OpenSmash-Ultimate/OpenSmash-Ultimate/commit/8539f9bf02065e0f250c97aef294bf38e74e795e)，2026-11-16T14:39:36Z。修复启动器点击播放后的重建流程与进度反馈，已检查 LauncherForm.cs 的具体实现。

发现线索：[公开索引](https://www.noking.tech/github-radar/)记录的[微信文章](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538101&idx=1&sn=9586777b5d22d5b3dbfbc0693fda1098)，索引日期 2026-10-27。仅核对公开索引，未直接读取该篇微信全文；功能与限制以上游资料为依据。

本次为文档与实现证据复核，未安装或运行上游项目。

## English

A static-recompilation project for running a specific, user-supplied Switch game on desktop platforms.

### Features

- Merges WindowSmash and ssbu-recomp and provides conversion tools, a runtime and a graphical launcher.
- Includes build diagnostics, controller input and optional networking components.

### Requirements and limits

- Primarily requires 64-bit Windows 10/11 and about 60 GB of free space
- Linux and Apple-silicon Mac support is experimental.
- Users must supply game files and keys they are entitled to use
- GPL-3.0-or-later covers project source, not game data, and external components have separate licenses.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/OpenSmash-Ultimate/OpenSmash-Ultimate/blob/main/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/OpenSmash-Ultimate/OpenSmash-Ultimate/releases) for versions.

### Review and provenance

The article names the predecessor ssbu-recomp. Both READMEs confirm the merger; this entry covers the current successor.

Both repositories confirm the merger. The successor provides conversion tools, a runtime, a launcher and an installation guide. Recent code fixes support its compatibility-research value.

Low Stars do not establish maturity. The upstream project was not run.

Activity: [8539f9bf02](https://github.com/OpenSmash-Ultimate/OpenSmash-Ultimate/commit/8539f9bf02065e0f250c97aef294bf38e74e795e), 2026-11-16T14:39:36Z. Fixes rebuild-on-play behavior and progress reporting; reviewed the implementation in LauncherForm.cs.

Discovery: [an indexed WeChat article](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538101&idx=1&sn=9586777b5d22d5b3dbfbc0693fda1098). This is a secondary discovery record; the WeChat article body was not read. Features and limits come from upstream documentation.

This review covers documentation and implementation evidence. The upstream project was not installed or run.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:58:29.135174Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "opensmash-ultimate",
    "name": "OpenSmash-Ultimate",
    "repository": "OpenSmash-Ultimate/OpenSmash-Ultimate",
    "repo_node_id": "R_kgDOVStUSQ",
    "category": "development",
    "summary": {
      "zh-CN": "通过静态重编译研究让用户自备的特定 Switch 游戏在桌面平台运行。",
      "en": "A static-recompilation project for running a specific, user-supplied Switch game on desktop platforms."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:58:29.135174Z",
        "en": "2026-11-16T14:58:29.135174Z"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "虽然仅 188 Star，但迁移关系由前后两个仓库相互确认，后继仓提供转换工具、运行时、启动器、安装指南和近期代码修复，具有明确兼容性研究价值。未运行上游项目，实验性平台与游戏数据许可单独说明。",
      "en": "Despite 188 Stars, both repositories confirm the migration. The successor provides conversion tools, a runtime, launcher, installation guide and recent code fixes, giving it a clear compatibility-research use. The upstream project was not run; experimental platforms and game-data rights are documented separately.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "GPL-3.0-or-later",
      "osi_approved": true,
      "license_sha256": "3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986",
      "source_url": "https://github.com/OpenSmash-Ultimate/OpenSmash-Ultimate/blob/199e1ed4508a6b6349d92ba1209c0cfd5ffe0cef/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "GPL-3.0-or-later covers the project source, including merged WindowSmash and ssbu-recomp. Game code, assets, keys and firmware are excluded. External libraries and optional Epic Online Services retain their own licenses.",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "199e1ed4508a6b6349d92ba1209c0cfd5ffe0cef"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-16T14:39:36Z",
        "reviewed_at": "2026-11-16T14:58:29.135174Z",
        "url": "https://github.com/OpenSmash-Ultimate/OpenSmash-Ultimate/commit/8539f9bf02065e0f250c97aef294bf38e74e795e",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复启动器点击播放后的重建流程与进度反馈，已检查 LauncherForm.cs 的具体实现。",
          "en": "Fixes rebuild-on-play behavior and progress reporting; reviewed the implementation in LauncherForm.cs."
        },
        "reviewed_files": [
          "OpenSmash.Launcher/LauncherForm.cs"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/OpenSmash-Ultimate/OpenSmash-Ultimate",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/OpenSmash-Ultimate/OpenSmash-Ultimate/blob/main/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/OpenSmash-Ultimate/OpenSmash-Ultimate/blob/199e1ed4508a6b6349d92ba1209c0cfd5ffe0cef/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/OpenSmash-Ultimate/OpenSmash-Ultimate/commit/8539f9bf02065e0f250c97aef294bf38e74e795e",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538101&idx=1&sn=9586777b5d22d5b3dbfbc0693fda1098",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/OpenSmash-Ultimate/ssbu-recomp/blob/main/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/OpenSmash-Ultimate/OpenSmash-Ultimate/blob/main/NOTICE.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      }
    ],
    "article_source": {
      "article_id": "2247538101_1",
      "title": "在电脑和手机上玩 Switch 游戏？这 5 个GitHub 项目值得看看。",
      "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538101&idx=1&sn=9586777b5d22d5b3dbfbc0693fda1098",
      "published_date": "2026-10-27",
      "account": "逛逛GitHub",
      "content_review_url": null,
      "content_review_kind": "secondary article index only",
      "wechat_direct_body_read": false,
      "migration_note": "The article names OpenSmash-Ultimate/ssbu-recomp. Its README explicitly redirects ongoing work to this merged successor, whose README and NOTICE confirm both predecessor projects and their licensing."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVStUSQ",
    "full_name": "OpenSmash-Ultimate/OpenSmash-Ultimate",
    "stargazers_count": 188,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "GPL-3.0",
    "license_sha256": "3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986",
    "last_success_at": "2026-11-16T14:58:29.135174Z"
  }
}
```

</details>
