# Universal Modder

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[rehan-remade/universal-modder](https://github.com/rehan-remade/universal-modder)

| 项目 / Field | 内容 / Value |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 9725 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:50:50.290410+00:00 |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:19:21.684Z |

## 中文

提供游戏模组制作的 Agent 技能、um 命令行工具和知识库，覆盖引擎识别、资源处理与游戏内验证。

**环境与限制：** 需要 Git、Python 3.10、FFmpeg 和本地游戏；3D 工作流另需 Blender，部分素材生成使用付费 API。游戏兼容性和资源使用权需按具体游戏核对。

**入门：** 从[官方说明](https://raw.githubusercontent.com/rehan-remade/universal-modder/main/README.md)确认安装与配置步骤，再查看[发布版本](https://github.com/rehan-remade/universal-modder/releases)。本次为文档、许可原文与维护证据审查，未安装运行。

**近期维护：** [提交限制知识库同步范围，并保留失败更新时的旧缓存，包含实际代码和测试。](https://github.com/rehan-remade/universal-modder/commit/0d65ff96d3d519263355366adf0899acd5cb76bf)（2026-11-06）

## English

Combines agent skills, the um CLI and a knowledge base for engine discovery, asset processing and in-game validation during mod development.

**Requirements and limitations:** Requires Git, Python 3.10, FFmpeg and local games. 3D workflows also need Blender; some asset generation uses paid APIs. Compatibility and asset permissions remain game-specific.

**Getting started:** Follow the [official documentation](https://raw.githubusercontent.com/rehan-remade/universal-modder/main/README.md) for setup, then check [releases](https://github.com/rehan-remade/universal-modder/releases). This review examined documentation, license text and maintenance evidence; the software was not installed or run.

**Recent maintenance:** [The inspected commit bounds knowledge synchronization and preserves a stale cache on failure, with code and tests.](https://github.com/rehan-remade/universal-modder/commit/0d65ff96d3d519263355366adf0899acd5cb76bf) (2026-11-06)

## Review evidence

发现线索来自第三方公众号文章索引，原始微信正文未完整读取；用途、环境、许可与维护状态依据仓库当前资料复核。

Discovery uses a third-party WeChat article index; the original article body was not fully read. Current repository sources were reviewed for function, requirements, licensing and maintenance.

- 公众号索引原文 / Indexed WeChat source：[又盘点了 4 个稀奇古怪的 GitHub 项目，第一个很抽象。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537904&idx=1&sn=f91d24d988863606f9abb5445ef79296)（2026-10-22）

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
    "id": "universal-modder",
    "name": "Universal Modder",
    "repository": "rehan-remade/universal-modder",
    "repo_node_id": "R_kgDOU0THuw",
    "category": "development",
    "summary": {
      "zh-CN": "提供游戏模组制作的 Agent 技能、um 命令行工具和知识库，覆盖引擎识别、资源处理与游戏内验证。",
      "en": "Combines agent skills, the um CLI and a knowledge base for engine discovery, asset processing and in-game validation during mod development."
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
      "license_sha256": "db6cfa2ad2c44f73080440c866c4a3a078749d84ba40b4dfa27d50f18a525543",
      "source_url": "https://github.com/rehan-remade/universal-modder/blob/3c4ac6c38e411b8c543bce217eae197039516bfc/LICENSE",
      "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
      "files": [
        {
          "path": "LICENSE",
          "source_url": "https://github.com/rehan-remade/universal-modder/blob/3c4ac6c38e411b8c543bce217eae197039516bfc/LICENSE",
          "fetched_at": "2026-11-16T14:23:16.872Z",
          "sha256": "db6cfa2ad2c44f73080440c866c4a3a078749d84ba40b4dfa27d50f18a525543",
          "source_commit": "3c4ac6c38e411b8c543bce217eae197039516bfc"
        }
      ],
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "3c4ac6c38e411b8c543bce217eae197039516bfc"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-06T08:20:23Z",
        "url": "https://github.com/rehan-remade/universal-modder/commit/0d65ff96d3d519263355366adf0899acd5cb76bf",
        "sha": "0d65ff96d3d519263355366adf0899acd5cb76bf",
        "summary": "Bound knowledge sync and preserve a stale cache (#468)",
        "files": [
          "tests/test_kb_sync.py",
          "um/kb.py"
        ],
        "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
        "qualifies": true,
        "reason": {
          "zh-CN": "提交限制知识库同步范围，并保留失败更新时的旧缓存，包含实际代码和测试。",
          "en": "The inspected commit bounds knowledge synchronization and preserves a stale cache on failure, with code and tests."
        }
      }
    ],
    "sources": [
      {
        "article_id": "2247537904_1",
        "title": "又盘点了 4 个稀奇古怪的 GitHub 项目，第一个很抽象。",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537904&idx=1&sn=f91d24d988863606f9abb5445ef79296",
        "published_date": "2026-10-22",
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
        "https://api.github.com/repos/rehan-remade/universal-modder",
        "https://raw.githubusercontent.com/rehan-remade/universal-modder/main/README.md",
        "https://github.com/rehan-remade/universal-modder/commit/0d65ff96d3d519263355366adf0899acd5cb76bf",
        "https://github.com/rehan-remade/universal-modder/blob/3c4ac6c38e411b8c543bce217eae197039516bfc/LICENSE"
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOU0THuw",
    "full_name": "rehan-remade/universal-modder",
    "stargazers_count": 9725,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "db6cfa2ad2c44f73080440c866c4a3a078749d84ba40b4dfa27d50f18a525543",
    "last_success_at": "2026-11-16T14:19:21.684Z"
  }
}
```

</details>
