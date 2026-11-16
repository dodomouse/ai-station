# Open Interpreter

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[openinterpreter/openinterpreter](https://github.com/openinterpreter/openinterpreter)

| 项目 / Field | 内容 / Value |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 68895 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:50:50.290410+00:00 |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:21:49.680Z |

## 中文

当前主线是基于 Rust 的终端编码 Agent，连接模型提供商，提供工具调用、MCP/ACP、技能和原生沙箱。

**环境与限制：** 支持 macOS、Windows、Linux，需自行配置模型或登录服务。当前 Rust 主线与历史 Python 解释器产品不同，旧教程可能不适用；按当前 README 与 Releases 入门。

**入门：** 从[官方说明](https://raw.githubusercontent.com/openinterpreter/openinterpreter/main/README.md)确认安装与配置步骤，再查看[发布版本](https://github.com/openinterpreter/openinterpreter/releases)。本次为文档、许可原文与维护证据审查，未安装运行。

**近期维护：** [提交修复多处编辑始终匹配原始文件，避免前次替换影响后续匹配。](https://github.com/openinterpreter/openinterpreter/commit/382f615b907279be1b6518156ac2754d3c235ff4)（2026-11-15）

## English

The current mainline is a Rust terminal coding agent with model-provider integration, tool use, MCP/ACP, skills and native sandboxing.

**Requirements and limitations:** Supports macOS, Windows and Linux with separately configured model access. The Rust mainline differs from the historical Python interpreter, so older tutorials may not apply. Follow the current README and releases.

**Getting started:** Follow the [official documentation](https://raw.githubusercontent.com/openinterpreter/openinterpreter/main/README.md) for setup, then check [releases](https://github.com/openinterpreter/openinterpreter/releases). This review examined documentation, license text and maintenance evidence; the software was not installed or run.

**Recent maintenance:** [The inspected commit matches multiple edits against the original file so earlier replacements cannot corrupt later matching.](https://github.com/openinterpreter/openinterpreter/commit/382f615b907279be1b6518156ac2754d3c235ff4) (2026-11-15)

## Review evidence

发现线索来自第三方公众号文章索引，原始微信正文未完整读取；用途、环境、许可与维护状态依据仓库当前资料复核。

Discovery uses a third-party WeChat article index; the original article body was not fully read. Current repository sources were reviewed for function, requirements, licensing and maintenance.

- 公众号索引原文 / Indexed WeChat source：[GitHub 定律：今天有个 xxx 刷屏，明天就有个 Openxxx 登上开源热榜。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537495&idx=1&sn=803c312533d9b69a993cfa4e89cc5ee2)（2026-10-03）

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
    "id": "open-interpreter",
    "name": "Open Interpreter",
    "repository": "openinterpreter/openinterpreter",
    "repo_node_id": "R_kgDOJ7brVg",
    "category": "ai",
    "summary": {
      "zh-CN": "当前主线是基于 Rust 的终端编码 Agent，连接模型提供商，提供工具调用、MCP/ACP、技能和原生沙箱。",
      "en": "The current mainline is a Rust terminal coding agent with model-provider integration, tool use, MCP/ACP, skills and native sandboxing."
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
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "d17f227e4df5da1600391338865ce0f3055211760a36688f816941d58232d8dc",
      "source_url": "https://raw.githubusercontent.com/openinterpreter/openinterpreter/main/LICENSE",
      "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
      "files": [
        {
          "path": "LICENSE",
          "source_url": "https://raw.githubusercontent.com/openinterpreter/openinterpreter/main/LICENSE",
          "fetched_at": "2026-11-16T14:23:28.368Z",
          "sha256": "d17f227e4df5da1600391338865ce0f3055211760a36688f816941d58232d8dc"
        }
      ]
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-15T12:12:47Z",
        "url": "https://github.com/openinterpreter/openinterpreter/commit/382f615b907279be1b6518156ac2754d3c235ff4",
        "sha": "382f615b907279be1b6518156ac2754d3c235ff4",
        "summary": "Merge pull request #1958 from Dev-next-gen/fix/pi-edit-original-file-matching",
        "files": [
          "codex-rs/core/src/tools/handlers/harness_aliases.rs"
        ],
        "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
        "qualifies": true,
        "reason": {
          "zh-CN": "提交修复多处编辑始终匹配原始文件，避免前次替换影响后续匹配。",
          "en": "The inspected commit matches multiple edits against the original file so earlier replacements cannot corrupt later matching."
        }
      }
    ],
    "sources": [
      {
        "article_id": "2247537495_1",
        "title": "GitHub 定律：今天有个 xxx 刷屏，明天就有个 Openxxx 登上开源热榜。",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537495&idx=1&sn=803c312533d9b69a993cfa4e89cc5ee2",
        "published_date": "2026-10-03",
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
        "https://api.github.com/repos/openinterpreter/openinterpreter",
        "https://raw.githubusercontent.com/openinterpreter/openinterpreter/main/README.md",
        "https://github.com/openinterpreter/openinterpreter/commit/382f615b907279be1b6518156ac2754d3c235ff4",
        "https://raw.githubusercontent.com/openinterpreter/openinterpreter/main/LICENSE"
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOJ7brVg",
    "full_name": "openinterpreter/openinterpreter",
    "stargazers_count": 68895,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "d17f227e4df5da1600391338865ce0f3055211760a36688f816941d58232d8dc",
    "last_success_at": "2026-11-16T14:21:49.680Z"
  }
}
```

</details>
