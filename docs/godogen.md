# Godogen

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[htdt/godogen](https://github.com/htdt/godogen)

| 项目 / Field | 内容 / Value |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 7354 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:50:50.290410+00:00 |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:20:00.522Z |

## 中文

通过编码 Agent 生成独立游戏工程与素材。支持多种目标，包括 Godot、Bevy、Babylon.js 和 Three.js，并提供运行验证流程。

**环境与限制：** 需要 Claude Code 或 Codex，按目标准备 Godot 4、Rust 或 Node.js 22.12+，素材脚本需要 Python 3，推荐 Blender。可选本地 GPU 或付费生成服务；它是开发工具而非即用成品游戏。

**入门：** 从[官方说明](https://raw.githubusercontent.com/htdt/godogen/master/README.md)确认安装与配置步骤，再查看[发布版本](https://github.com/htdt/godogen/releases)。本次为文档、许可原文与维护证据审查，未安装运行。

**近期维护：** [提交加入音频工具、GDScript/Three.js 支持和本地素材流程，包含功能脚本变更。](https://github.com/htdt/godogen/commit/40542b6c8efbdc40112c2b004fbaa6d67141846d)（2026-10-16）

## English

Uses coding agents to generate standalone game projects and assets for targets including Godot, Bevy, Babylon.js and Three.js, with runtime verification workflows.

**Requirements and limitations:** Requires Claude Code or Codex and target-specific Godot 4, Rust or Node.js 22.12+, plus Python 3 for asset scripts; Blender is recommended. Local GPU or paid generation services are optional. This is development tooling, not a finished game.

**Getting started:** Follow the [official documentation](https://raw.githubusercontent.com/htdt/godogen/master/README.md) for setup, then check [releases](https://github.com/htdt/godogen/releases). This review examined documentation, license text and maintenance evidence; the software was not installed or run.

**Recent maintenance:** [The inspected commit adds audio tooling, GDScript/Three.js support and local asset workflows with functional script changes.](https://github.com/htdt/godogen/commit/40542b6c8efbdc40112c2b004fbaa6d67141846d) (2026-10-16)

## Review evidence

发现线索来自第三方公众号文章索引，原始微信正文未完整读取；用途、环境、许可与维护状态依据仓库当前资料复核。

Discovery uses a third-party WeChat article index; the original article body was not fully read. Current repository sources were reviewed for function, requirements, licensing and maintenance.

- 公众号索引原文 / Indexed WeChat source：[发现 GitHub 上两个教 Agent 做 3D 游戏的 Skills，收藏起来。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536792&idx=1&sn=3bede56b586fdb91b2039089f48ae20c)（2026-09-12）

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
    "id": "godogen",
    "name": "Godogen",
    "repository": "htdt/godogen",
    "repo_node_id": "R_kgDORKUN8g",
    "category": "development",
    "summary": {
      "zh-CN": "通过编码 Agent 生成独立游戏工程与素材，支持 Godot、Bevy、Babylon.js 和 Three.js 等目标，并提供运行验证流程。",
      "en": "Uses coding agents to generate standalone game projects and assets for targets including Godot, Bevy, Babylon.js and Three.js, with runtime verification workflows."
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
      "license_sha256": "9994c50a3e043728bcf59106d5941c21b06e53dc64977e6bcafe9580a8a5e5d6",
      "source_url": "https://github.com/htdt/godogen/blob/40542b6c8efbdc40112c2b004fbaa6d67141846d/LICENSE.md",
      "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
      "files": [
        {
          "path": "LICENSE.md",
          "source_url": "https://github.com/htdt/godogen/blob/40542b6c8efbdc40112c2b004fbaa6d67141846d/LICENSE.md",
          "fetched_at": "2026-11-16T14:23:40.243Z",
          "sha256": "9994c50a3e043728bcf59106d5941c21b06e53dc64977e6bcafe9580a8a5e5d6",
          "source_commit": "40542b6c8efbdc40112c2b004fbaa6d67141846d"
        }
      ],
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "40542b6c8efbdc40112c2b004fbaa6d67141846d"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-10-16T14:53:57Z",
        "url": "https://github.com/htdt/godogen/commit/40542b6c8efbdc40112c2b004fbaa6d67141846d",
        "sha": "40542b6c8efbdc40112c2b004fbaa6d67141846d",
        "summary": "Local assets by default; audio; GDScript and three.js (#54)",
        "files": [
          ".gitignore",
          "AGENTS.md",
          "CHANGELOG.md",
          "CONTRIBUTING.md",
          "README.md",
          "asset-gen/SKILL.md",
          "asset-gen/api.md",
          "asset-gen/motion.md",
          "asset-gen/rembg.md",
          "asset-gen/tools/asset_gen.py",
          "asset-gen/tools/loop_audio.py",
          "asset-gen/tools/requirements.txt",
          "docs/PROJECT.md",
          "engines/godot-gdscript.md",
          "engines/threejs.md",
          "prompts/runtime.md",
          "publish.sh",
          "setup.md"
        ],
        "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
        "qualifies": true,
        "reason": {
          "zh-CN": "提交加入音频工具、GDScript/Three.js 支持和本地素材流程，包含功能脚本变更。",
          "en": "The inspected commit adds audio tooling, GDScript/Three.js support and local asset workflows with functional script changes."
        }
      }
    ],
    "sources": [
      {
        "article_id": "2247536792_1",
        "title": "发现 GitHub 上两个教 Agent 做 3D 游戏的 Skills，收藏起来。",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536792&idx=1&sn=3bede56b586fdb91b2039089f48ae20c",
        "published_date": "2026-09-12",
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
        "https://api.github.com/repos/htdt/godogen",
        "https://raw.githubusercontent.com/htdt/godogen/master/README.md",
        "https://github.com/htdt/godogen/commit/40542b6c8efbdc40112c2b004fbaa6d67141846d",
        "https://github.com/htdt/godogen/blob/40542b6c8efbdc40112c2b004fbaa6d67141846d/LICENSE.md"
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDORKUN8g",
    "full_name": "htdt/godogen",
    "stargazers_count": 7354,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "9994c50a3e043728bcf59106d5941c21b06e53dc64977e6bcafe9580a8a5e5d6",
    "last_success_at": "2026-11-16T14:20:00.522Z"
  }
}
```

</details>
