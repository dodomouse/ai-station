# Superpowers

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[obra/superpowers](https://github.com/obra/superpowers)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 318748 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T04:07:37.947199+00:00 |

## 中文

为编码智能体提供需求澄清、任务规划、测试和代码审查技能。

### 用途与功能

- 把设计讨论、实现计划和验证组织成可组合技能。
- 提供子智能体协作、系统化调试和完成前验证流程。

### 环境与限制

需要受支持的编码智能体；技能本身不含模型。不同宿主须分别安装。开发流程仍应遵守项目授权，包括工作树和提交操作。可选可视化工具的遥测可关闭。

### 开始使用

选择 README 中对应宿主的安装入口，启动新会话，以一个小型开发任务检查技能是否加载。

参阅[官方 README](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/README.md)。

### 收录与来源

适合希望复用规划、测试和审查步骤的编码智能体用户。

维护证据：[修复 Hermes 子智能体继承控制器启动指令的问题，仅在非子智能体的首轮注入启动上下文。](https://github.com/obra/superpowers/commit/22f0b463e7a5e579904dd6211a520321035526f7)（2026-11-03）。

发现于 [GitHub 月榜](https://github.com/trending/shell?since=monthly)。2026-11-17 的榜单记录新增 19,285 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Provides coding agents with skills for requirements, planning, testing and code review.

### Uses and features

- Organizes design discussion, implementation planning and verification into composable skills.
- Includes subagent collaboration, systematic debugging and completion checks.

### Requirements and limits

Requires a supported coding agent; the skills do not include a model. Install separately for each host, apply project authorization to worktree and commit workflows, and configure optional visual-companion telemetry as needed.

### Getting started

Use the README installation path for your host, start a new session and check skill loading with a small development task.

See the [official README](https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/README.md).

### Review and provenance

Useful for coding-agent users who want reusable planning, testing and review procedures.

Maintenance evidence: [Prevents Hermes task subagents from receiving controller bootstrap instructions by limiting first-turn injection to non-subagent sessions.](https://github.com/obra/superpowers/commit/22f0b463e7a5e579904dd6211a520321035526f7) (2026-11-03).

Discovered in [GitHub monthly Trending](https://github.com/trending/shell?since=monthly), which recorded 19,285 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:07:37.947199+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "superpowers",
    "name": "Superpowers",
    "repository": "obra/superpowers",
    "repo_node_id": "R_kgDOP_gcWw",
    "category": "development",
    "summary": {
      "zh-CN": "为编码智能体提供需求澄清、任务规划、测试和代码审查技能。",
      "en": "Provides coding agents with skills for requirements, planning, testing and code review."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:07:37.947199+00:00",
        "en": "2026-11-17T04:07:37.947199+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合希望复用规划、测试和审查步骤的编码智能体用户。",
      "en": "Useful for coding-agent users who want reusable planning, testing and review procedures.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/LICENSE",
      "license_sha256": "a37e0e9697144819e1d965176ac4ae5bc3fa02d11e7812036bbcadf6dafe2400",
      "source_commit": "22f0b463e7a5e579904dd6211a520321035526f7",
      "reviewed_at": "2026-11-17T04:07:37.947199+00:00",
      "evidence_pinned_at": "2026-11-17T04:07:37.947199+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "Applies to repository code and documentation; external models, services, data and assets retain their own terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-03T22:17:07Z",
        "reviewed_at": "2026-11-17T04:07:37.947199+00:00",
        "url": "https://github.com/obra/superpowers/commit/22f0b463e7a5e579904dd6211a520321035526f7",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复 Hermes 子智能体继承控制器启动指令的问题，仅在非子智能体的首轮注入启动上下文。",
          "en": "Prevents Hermes task subagents from receiving controller bootstrap instructions by limiting first-turn injection to non-subagent sessions."
        },
        "reviewed_files": [
          ".hermes-plugin/__init__.py"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/obra/superpowers",
        "accessed_at": "2026-11-17T04:07:37.947199+00:00"
      },
      {
        "url": "https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/README.md",
        "accessed_at": "2026-11-17T04:07:37.947199+00:00"
      },
      {
        "url": "https://github.com/obra/superpowers/blob/22f0b463e7a5e579904dd6211a520321035526f7/LICENSE",
        "accessed_at": "2026-11-17T04:07:37.947199+00:00"
      },
      {
        "url": "https://github.com/obra/superpowers/commit/22f0b463e7a5e579904dd6211a520321035526f7",
        "accessed_at": "2026-11-17T04:07:37.947199+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 19285,
      "source_url": "https://github.com/trending/shell?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOP_gcWw",
    "full_name": "obra/superpowers",
    "stargazers_count": 318748,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "a37e0e9697144819e1d965176ac4ae5bc3fa02d11e7812036bbcadf6dafe2400",
    "last_success_at": "2026-11-17T03:53:17.095588+00:00"
  }
}
```

</details>
