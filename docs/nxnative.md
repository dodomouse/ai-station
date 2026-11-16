# nxnative

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[seedds/nxnative](https://github.com/seedds/nxnative)

| 项目 / Field | 内容 / Value |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 15844 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:50:50.290410+00:00 |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:19:06.291Z |

## 中文

将用户自有 Switch 游戏程序转换为原生 Apple 平台应用。提供 Horizon 系统调用和图形接口的兼容层，适合研究静态重编译。

**环境与限制：** 需要合法取得的游戏转储，仓库不提供游戏资源。当前文档要求 Apple Silicon、macOS 26.6+、Xcode 27.2、Python 3.12；移动端要求更高版本设备与系统。仅部分游戏兼容，不是通用运行保证。

**入门：** 从[官方说明](https://raw.githubusercontent.com/seedds/nxnative/main/README.md)确认安装与配置步骤，再查看[发布版本](https://github.com/seedds/nxnative/releases)。本次为文档、许可原文与维护证据审查，未安装运行。

**近期维护：** [提交修复 GLSL 保留名称的着色器转换，并包含测试。](https://github.com/seedds/nxnative/commit/ba9ce21258c90bcf2b90be5555ba5333c227e752)（2026-11-16）

## English

Translates user-owned Switch game programs into native Apple applications, with Horizon and graphics compatibility layers for static-recompilation research.

**Requirements and limitations:** Requires legally obtained game dumps; no game assets are included. Current documentation specifies Apple Silicon, macOS 26.6+, Xcode 27.2 and Python 3.12, with additional mobile hardware and OS requirements. Compatibility is game-specific.

**Getting started:** Follow the [official documentation](https://raw.githubusercontent.com/seedds/nxnative/main/README.md) for setup, then check [releases](https://github.com/seedds/nxnative/releases). This review examined documentation, license text and maintenance evidence; the software was not installed or run.

**Recent maintenance:** [The inspected commit fixes reserved GLSL names during shader translation and includes tests.](https://github.com/seedds/nxnative/commit/ba9ce21258c90bcf2b90be5555ba5333c227e752) (2026-11-16)

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
    "id": "nxnative",
    "name": "nxnative",
    "repository": "seedds/nxnative",
    "repo_node_id": "R_kgDOVG4bQg",
    "category": "development",
    "summary": {
      "zh-CN": "将用户自有 Switch 游戏程序转换为原生 Apple 平台应用，提供 Horizon 系统调用和图形接口的兼容层，适合研究静态重编译。",
      "en": "Translates user-owned Switch game programs into native Apple applications, with Horizon and graphics compatibility layers for static-recompilation research."
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
      "license_sha256": "a65554a74de59bf4d2210f3d4381c67d6fc6fa78f237f83c85543773319efa7b",
      "source_url": "https://raw.githubusercontent.com/seedds/nxnative/main/LICENSE",
      "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
      "files": [
        {
          "path": "LICENSE",
          "source_url": "https://raw.githubusercontent.com/seedds/nxnative/main/LICENSE",
          "fetched_at": "2026-11-16T14:23:16.545Z",
          "sha256": "a65554a74de59bf4d2210f3d4381c67d6fc6fa78f237f83c85543773319efa7b"
        }
      ]
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-16T13:46:48Z",
        "url": "https://github.com/seedds/nxnative/commit/ba9ce21258c90bcf2b90be5555ba5333c227e752",
        "sha": "ba9ce21258c90bcf2b90be5555ba5333c227e752",
        "summary": "gl/shaders: a GLSL ES 1.00 name that later GLSL takes is renamed for the compile and given back in the table rows (#2818, PR #2819)",
        "files": [
          "dm/gfx/tools/gl_shaders.py",
          "dm/tools/tests/test_gl_shaders.py",
          "docs/agents/symptoms.md",
          "docs/reference/rendering.md"
        ],
        "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
        "qualifies": true,
        "reason": {
          "zh-CN": "提交修复 GLSL 保留名称的着色器转换，并包含测试。",
          "en": "The inspected commit fixes reserved GLSL names during shader translation and includes tests."
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
        "https://api.github.com/repos/seedds/nxnative",
        "https://raw.githubusercontent.com/seedds/nxnative/main/README.md",
        "https://github.com/seedds/nxnative/commit/ba9ce21258c90bcf2b90be5555ba5333c227e752",
        "https://raw.githubusercontent.com/seedds/nxnative/main/LICENSE"
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVG4bQg",
    "full_name": "seedds/nxnative",
    "stargazers_count": 15844,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "a65554a74de59bf4d2210f3d4381c67d6fc6fa78f237f83c85543773319efa7b",
    "last_success_at": "2026-11-16T14:19:06.291Z"
  }
}
```

</details>
