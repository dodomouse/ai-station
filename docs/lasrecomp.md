# LASRecomp

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[peiikai/LASRecomp](https://github.com/peiikai/LASRecomp)

| 项目 / Field | 内容 / Value |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 2451 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:50:50.290410+00:00 |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:19:06.505Z |

## 中文

将《塞尔达传说：织梦岛》Switch 版本重编译为桌面或移动端原生程序，提供图形、输入和平台兼容代码。

**环境与限制：** 仅项目自有代码适用 MIT。Nintendo 游戏和第三方资源不包含在授权内，必须自备受支持版本游戏文件。Windows/Linux 需要 x64 AVX2 与 Vulkan 1.3，macOS 需要 Apple Silicon。移动端安装及性能限制见官方文档。

**入门：** 从[官方说明](https://raw.githubusercontent.com/peiikai/LASRecomp/main/README.md)确认安装与配置步骤，再查看[发布版本](https://github.com/peiikai/LASRecomp/releases)。本次为文档、许可原文与维护证据审查，未安装运行。

**近期维护：** [Beta 6 发布加入 Android、iOS 与触控支持；GitHub release 标记非 prerelease，软件仍自称 Beta。](https://github.com/peiikai/LASRecomp/releases/tag/beta_6)（2026-11-15）

## English

Recompiles the Switch edition of Link's Awakening into native desktop or mobile programs with graphics, input and platform compatibility code.

**Requirements and limitations:** MIT covers the project's own code, not Nintendo games or third-party assets. Supply supported game files yourself. Windows/Linux require x64 AVX2 and Vulkan 1.3; macOS requires Apple Silicon. Consult the documentation for mobile installation and performance constraints.

**Getting started:** Follow the [official documentation](https://raw.githubusercontent.com/peiikai/LASRecomp/main/README.md) for setup, then check [releases](https://github.com/peiikai/LASRecomp/releases). This review examined documentation, license text and maintenance evidence; the software was not installed or run.

**Recent maintenance:** [Beta 6 adds Android, iOS and touch support; GitHub marks the release non-prerelease, while the software remains labeled beta.](https://github.com/peiikai/LASRecomp/releases/tag/beta_6) (2026-11-15)

## Review evidence

发现线索来自第三方公众号文章索引，原始微信正文未完整读取；用途、环境、许可与维护状态依据仓库当前资料复核。

Discovery uses a third-party WeChat article index; the original article body was not fully read. Current repository sources were reviewed for function, requirements, licensing and maintenance.

- 公众号索引原文 / Indexed WeChat source：[在电脑和手机上玩 Switch 游戏？这 5 个GitHub 项目值得看看。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538101&idx=1&sn=9586777b5d22d5b3dbfbc0693fda1098)（2026-10-27）

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
    "id": "lasrecomp",
    "name": "LASRecomp",
    "repository": "peiikai/LASRecomp",
    "repo_node_id": "R_kgDOVBqNYQ",
    "category": "development",
    "summary": {
      "zh-CN": "将《塞尔达传说：织梦岛》Switch 版本重编译为桌面或移动端原生程序，提供图形、输入和平台兼容代码。",
      "en": "Recompiles the Switch edition of Link's Awakening into native desktop or mobile programs with graphics, input and platform compatibility code."
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
      "license_sha256": "31e2e8c10f4461ff75bd2f95e26125f6126ee88828bf29233f4d9f14e90630d6",
      "source_url": "https://github.com/peiikai/LASRecomp/blob/33784c2ad6ce7f802eb4b78139fb578633e60aa4/LICENSE",
      "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
      "files": [
        {
          "path": "LICENSE",
          "source_url": "https://github.com/peiikai/LASRecomp/blob/33784c2ad6ce7f802eb4b78139fb578633e60aa4/LICENSE",
          "fetched_at": "2026-11-16T14:23:16.634Z",
          "sha256": "31e2e8c10f4461ff75bd2f95e26125f6126ee88828bf29233f4d9f14e90630d6",
          "source_commit": "33784c2ad6ce7f802eb4b78139fb578633e60aa4"
        }
      ],
      "scope": "MIT applies to original project code only; Nintendo game files and third-party materials are excluded.",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "33784c2ad6ce7f802eb4b78139fb578633e60aa4"
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-11-15T06:35:20Z",
        "url": "https://github.com/peiikai/LASRecomp/releases/tag/beta_6",
        "tag": "beta_6",
        "summary": "Beta 6",
        "draft": false,
        "prerelease": false,
        "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
        "qualifies": true,
        "reason": {
          "zh-CN": "Beta 6 发布加入 Android、iOS 与触控支持；GitHub release 标记非 prerelease，软件仍自称 Beta。",
          "en": "Beta 6 adds Android, iOS and touch support; GitHub marks the release non-prerelease, while the software remains labeled beta."
        }
      }
    ],
    "sources": [
      {
        "article_id": "2247538101_1",
        "title": "在电脑和手机上玩 Switch 游戏？这 5 个GitHub 项目值得看看。",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538101&idx=1&sn=9586777b5d22d5b3dbfbc0693fda1098",
        "published_date": "2026-10-27",
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
        "https://api.github.com/repos/peiikai/lasrecomp",
        "https://raw.githubusercontent.com/peiikai/LASRecomp/main/README.md",
        "https://github.com/peiikai/LASRecomp/releases/tag/beta_6",
        "https://github.com/peiikai/LASRecomp/blob/33784c2ad6ce7f802eb4b78139fb578633e60aa4/LICENSE"
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVBqNYQ",
    "full_name": "peiikai/LASRecomp",
    "stargazers_count": 2451,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "NOASSERTION",
    "license_sha256": "31e2e8c10f4461ff75bd2f95e26125f6126ee88828bf29233f4d9f14e90630d6",
    "last_success_at": "2026-11-16T14:19:06.505Z"
  }
}
```

</details>
