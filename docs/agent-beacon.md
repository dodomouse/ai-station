# Agent Beacon

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[Asymptote-Labs/agent-beacon](https://github.com/Asymptote-Labs/agent-beacon)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 3543 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T04:07:37.964448+00:00 |

## 中文

收集多个编程智能体的会话轨迹，将经过审阅的工作经验提供给后续智能体复用。

### 用途与功能

- 汇总提示、响应、工具调用和文件操作为本地 JSONL 轨迹。
- 提供轨迹浏览、MCP 和 Skills 记忆访问，并可配置外部日志目的地。

### 环境与限制

需要受支持的智能体与对应系统安装包。轨迹可能包含代码和提示。交互安装预选 Beacon Cloud。选择 Local 才保持该路径的本地存储，确认云选项会开始转发。

### 开始使用

按系统安装 Beacon，运行 beacon endpoint install 并确认存储目的地；用 beacon traces 查看收集结果。

参阅[官方 README](https://github.com/Asymptote-Labs/agent-beacon/blob/a3e0bbfa8a65450877bf8477db272e3dd3b8e662/README.md)。

### 收录与来源

统一不同智能体的事件记录，便于追查开发过程并整理经审核的项目经验。

维护证据：[启动命令时识别已存储的有效登录，仅在匿名状态下持久化身份，避免重复遥测识别。](https://github.com/Asymptote-Labs/agent-beacon/commit/a3e0bbfa8a65450877bf8477db272e3dd3b8e662)（2026-11-17）。

发现于 [GitHub 月榜](https://github.com/trending/go?since=monthly)。2026-11-17 的榜单记录新增 1,704 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Collects coding-agent session traces and makes reviewed working knowledge reusable by later agents.

### Uses and features

- Collects prompts, responses, tool calls and file operations in local JSONL traces.
- Provides trace browsing and memory access through MCP and Skills, with configurable external log destinations.

### Requirements and limits

Requires a supported agent and platform package. Traces may contain code and prompts. Interactive setup preselects Beacon Cloud; choose Local for local storage, while confirming Cloud starts forwarding.

### Getting started

Install Beacon for your platform, run beacon endpoint install and confirm the destination, then inspect captured results with beacon traces.

See the [official README](https://github.com/Asymptote-Labs/agent-beacon/blob/a3e0bbfa8a65450877bf8477db272e3dd3b8e662/README.md).

### Review and provenance

Unifies events across agents to inspect development history and curate reviewed project knowledge.

Maintenance evidence: [Identifies a valid stored sign-in at command startup, persists identity only for anonymous state and avoids duplicate telemetry identification.](https://github.com/Asymptote-Labs/agent-beacon/commit/a3e0bbfa8a65450877bf8477db272e3dd3b8e662) (2026-11-17).

Discovered in [GitHub monthly Trending](https://github.com/trending/go?since=monthly), which recorded 1,704 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:07:37.964448+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "agent-beacon",
    "name": "Agent Beacon",
    "repository": "Asymptote-Labs/agent-beacon",
    "repo_node_id": "R_kgDOSa6n_g",
    "category": "ai",
    "summary": {
      "zh-CN": "收集多个编程智能体的会话轨迹，将经过审阅的工作经验提供给后续智能体复用。",
      "en": "Collects coding-agent session traces and makes reviewed working knowledge reusable by later agents."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:07:37.964448+00:00",
        "en": "2026-11-17T04:07:37.964448+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "统一不同智能体的事件记录，便于追查开发过程并整理经审核的项目经验。",
      "en": "Unifies events across agents to inspect development history and curate reviewed project knowledge.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/Asymptote-Labs/agent-beacon/blob/a3e0bbfa8a65450877bf8477db272e3dd3b8e662/LICENSE",
      "license_sha256": "083b5d7f980521a76359c5bf9892ae051e3b6c31838a86e197e20f7879100457",
      "source_commit": "a3e0bbfa8a65450877bf8477db272e3dd3b8e662",
      "reviewed_at": "2026-11-17T04:07:37.964448+00:00",
      "evidence_pinned_at": "2026-11-17T04:07:37.964448+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "Root license applies to repository software code; models, data, assets and external services have separate terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-17T03:10:06Z",
        "reviewed_at": "2026-11-17T04:07:37.964448+00:00",
        "url": "https://github.com/Asymptote-Labs/agent-beacon/commit/a3e0bbfa8a65450877bf8477db272e3dd3b8e662",
        "qualifies": true,
        "reason": {
          "zh-CN": "启动命令时识别已存储的有效登录，仅在匿名状态下持久化身份，避免重复遥测识别。",
          "en": "Identifies a valid stored sign-in at command startup, persists identity only for anonymous state and avoids duplicate telemetry identification."
        },
        "reviewed_files": [
          "cli/beacon/cmd/telemetry.go",
          "cli/beacon/internal/telemetry/telemetry.go"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/Asymptote-Labs/agent-beacon",
        "accessed_at": "2026-11-17T04:07:37.964448+00:00"
      },
      {
        "url": "https://github.com/Asymptote-Labs/agent-beacon/blob/a3e0bbfa8a65450877bf8477db272e3dd3b8e662/README.md",
        "accessed_at": "2026-11-17T04:07:37.964448+00:00"
      },
      {
        "url": "https://github.com/Asymptote-Labs/agent-beacon/blob/a3e0bbfa8a65450877bf8477db272e3dd3b8e662/LICENSE",
        "accessed_at": "2026-11-17T04:07:37.964448+00:00"
      },
      {
        "url": "https://github.com/Asymptote-Labs/agent-beacon/commit/a3e0bbfa8a65450877bf8477db272e3dd3b8e662",
        "accessed_at": "2026-11-17T04:07:37.964448+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 1704,
      "source_url": "https://github.com/trending/go?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOSa6n_g",
    "full_name": "Asymptote-Labs/agent-beacon",
    "stargazers_count": 3543,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "083b5d7f980521a76359c5bf9892ae051e3b6c31838a86e197e20f7879100457",
    "last_success_at": "2026-11-17T03:53:41.757727+00:00"
  }
}
```

</details>
