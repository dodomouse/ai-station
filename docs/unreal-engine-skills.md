# Unreal Engine Skills for Claude Code

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[EpicGames/unreal-engine-skills-for-claude-code-plugin](https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 1980 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T04:07:37.965977+00:00 |

## 中文

指导 Claude Code 通过 MCP 操作 Unreal Editor 的技能和会话钩子。

### 用途与功能

- 提供场景、蓝图、材质、动画和测试相关操作指引。
- 注入 Unreal 项目上下文，并指导按需发现工具集。

### 环境与限制

需 Claude Code、启用 ModelContextProtocol 与 AllToolsets 的 Unreal Editor，以及可用 bash。编辑器操作会修改实际资源；MIT 仅覆盖本插件，不授予 Unreal Engine 或素材的许可。

### 开始使用

安装 unreal-engine-skills-for-claude-code 插件，在编辑器启动 MCP 服务并生成客户端配置，先列出当前关卡的 actor。

参阅[官方 README](https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin/blob/0e27bde2b55c5d3f6948532f4296aaa3654d8f4b/README.md)。

### 收录与来源

将编辑器工具发现、状态检查和操作顺序整理成智能体可加载的工作流。

维护证据：[更新执行规则，允许支持安全重叠的独立工具并发。要求依赖调用及共享资源修改保持串行。](https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin/commit/a6aa73ada02a9fb1f5415bec491f9942c519b297)（2026-09-17）。

发现于 [GitHub 月榜](https://github.com/trending/shell?since=monthly)。2026-11-17 的榜单记录新增 1,439 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Skills and session hooks that guide Claude Code in operating Unreal Editor through MCP.

### Uses and features

- Provides workflows for scenes, blueprints, materials, animation and tests.
- Injects Unreal project context and guides on-demand toolset discovery.

### Requirements and limits

Requires Claude Code, Unreal Editor with ModelContextProtocol and AllToolsets, and bash. Editor operations mutate real assets. MIT covers this plugin, not Unreal Engine or assets.

### Getting started

Install the unreal-engine-skills-for-claude-code plugin, start the editor MCP server, generate client configuration and first list actors in the current level.

See the [official README](https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin/blob/0e27bde2b55c5d3f6948532f4296aaa3654d8f4b/README.md).

### Review and provenance

Packages editor tool discovery, state checks and operation ordering into agent-loadable workflows.

Maintenance evidence: [Updates execution rules to permit independent tools with safe overlap while serializing dependent calls and mutations of shared editor state.](https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin/commit/a6aa73ada02a9fb1f5415bec491f9942c519b297) (2026-09-17).

Discovered in [GitHub monthly Trending](https://github.com/trending/shell?since=monthly), which recorded 1,439 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:07:37.965977+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "unreal-engine-skills",
    "name": "Unreal Engine Skills for Claude Code",
    "repository": "EpicGames/unreal-engine-skills-for-claude-code-plugin",
    "repo_node_id": "R_kgDOS0wqzw",
    "category": "development",
    "summary": {
      "zh-CN": "指导 Claude Code 通过 MCP 操作 Unreal Editor 的技能和会话钩子。",
      "en": "Skills and session hooks that guide Claude Code in operating Unreal Editor through MCP."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:07:37.965977+00:00",
        "en": "2026-11-17T04:07:37.965977+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "将编辑器工具发现、状态检查和操作顺序整理成智能体可加载的工作流。",
      "en": "Packages editor tool discovery, state checks and operation ordering into agent-loadable workflows.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin/blob/0e27bde2b55c5d3f6948532f4296aaa3654d8f4b/LICENSE",
      "license_sha256": "5b337be051359edcdec510103aee15f5f870efb38b6d42eecd685dc3582314a6",
      "source_commit": "0e27bde2b55c5d3f6948532f4296aaa3654d8f4b",
      "reviewed_at": "2026-11-17T04:07:37.965977+00:00",
      "evidence_pinned_at": "2026-11-17T04:07:37.965977+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "MIT covers this skill/plugin repository only; Unreal Engine, its plugins and project assets remain subject to their own licenses."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-09-17T01:28:32Z",
        "reviewed_at": "2026-11-17T04:07:37.965977+00:00",
        "url": "https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin/commit/a6aa73ada02a9fb1f5415bec491f9942c519b297",
        "qualifies": true,
        "reason": {
          "zh-CN": "更新执行规则，允许支持安全重叠的独立工具并发。要求依赖调用及共享资源修改保持串行。",
          "en": "Updates execution rules to permit independent tools with safe overlap while serializing dependent calls and mutations of shared editor state."
        },
        "reviewed_files": [
          "skills/unreal-mcp/SKILL.md",
          "skills/unreal-mcp/references/operations.md"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin",
        "accessed_at": "2026-11-17T04:07:37.965977+00:00"
      },
      {
        "url": "https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin/blob/0e27bde2b55c5d3f6948532f4296aaa3654d8f4b/README.md",
        "accessed_at": "2026-11-17T04:07:37.965977+00:00"
      },
      {
        "url": "https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin/blob/0e27bde2b55c5d3f6948532f4296aaa3654d8f4b/LICENSE",
        "accessed_at": "2026-11-17T04:07:37.965977+00:00"
      },
      {
        "url": "https://github.com/EpicGames/unreal-engine-skills-for-claude-code-plugin/commit/a6aa73ada02a9fb1f5415bec491f9942c519b297",
        "accessed_at": "2026-11-17T04:07:37.965977+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 1439,
      "source_url": "https://github.com/trending/shell?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOS0wqzw",
    "full_name": "EpicGames/unreal-engine-skills-for-claude-code-plugin",
    "stargazers_count": 1980,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "5b337be051359edcdec510103aee15f5f870efb38b6d42eecd685dc3582314a6",
    "last_success_at": "2026-11-17T03:54:05.665242+00:00"
  }
}
```

</details>
