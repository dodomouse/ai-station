# Ruflo

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[ruvnet/ruflo](https://github.com/ruvnet/ruflo)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 81892 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T04:07:37.955235+00:00 |

## 中文

为编码智能体提供任务编排、共享记忆和 MCP 工具集成。

### 用途与功能

- 通过角色与任务配置组织多个智能体协作。
- 使用向量记忆保存和检索任务上下文。
- 提供 CLI、控制台及 Claude Code 插件或 MCP 接入。

### 环境与限制

需要 Node.js/npm 运行环境和相应智能体或模型服务。项目初始化会添加配置、钩子和记忆文件；插件按账号权限运行，应按实际需要配置。外部模型及相关商业服务不由代码许可覆盖。

### 开始使用

按 README 选择项目初始化、插件或仅 MCP 接入方式，从一个边界明确的任务检查编排和记忆输出。

参阅[官方 README](https://github.com/ruvnet/ruflo/blob/8cb2fbc7a1e9e08f20fc5fc6a45e1046ad0369b9/README.md)。

### 收录与来源

适合在已有编码智能体上补充任务协调和持久上下文。

维护证据：[将配置的嵌入模型和向量维度传入 AgentDB。校验生成维度，并避免把默认模型错误标为自定义模型。](https://github.com/ruvnet/ruflo/commit/8971ebad35fe2b37888f66bfd266ee1128f458a7)（2026-11-13）。

发现于 [GitHub 月榜](https://github.com/trending/typescript?since=monthly)。2026-11-17 的榜单记录新增 6,780 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Provides task orchestration, shared memory and MCP tool integration for coding agents.

### Uses and features

- Coordinates multiple agents through role and task configuration.
- Stores and retrieves task context with vector memory.
- Offers a CLI, console, Claude Code plugins and MCP integration.

### Requirements and limits

Requires a Node.js/npm environment and relevant agents or model services. Project initialization adds configuration, hooks and memory files; plugins run with account permissions and should be configured for the intended task. External models and related commercial services are outside the code license.

### Getting started

Choose project initialization, plugins or MCP-only setup in the README, then inspect orchestration and memory outputs on a bounded task.

See the [official README](https://github.com/ruvnet/ruflo/blob/8cb2fbc7a1e9e08f20fc5fc6a45e1046ad0369b9/README.md).

### Review and provenance

Useful for adding task coordination and persistent context to existing coding agents.

Maintenance evidence: [Passes configured embedding models and vector dimensions into AgentDB, validates generated dimensions and avoids labeling default embeddings as a custom model.](https://github.com/ruvnet/ruflo/commit/8971ebad35fe2b37888f66bfd266ee1128f458a7) (2026-11-13).

Discovered in [GitHub monthly Trending](https://github.com/trending/typescript?since=monthly), which recorded 6,780 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:07:37.955235+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "ruflo",
    "name": "Ruflo",
    "repository": "ruvnet/ruflo",
    "repo_node_id": "R_kgDOO07yiQ",
    "category": "ai",
    "summary": {
      "zh-CN": "为编码智能体提供任务编排、共享记忆和 MCP 工具集成。",
      "en": "Provides task orchestration, shared memory and MCP tool integration for coding agents."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:07:37.955235+00:00",
        "en": "2026-11-17T04:07:37.955235+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合在已有编码智能体上补充任务协调和持久上下文。",
      "en": "Useful for adding task coordination and persistent context to existing coding agents.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/ruvnet/ruflo/blob/8cb2fbc7a1e9e08f20fc5fc6a45e1046ad0369b9/LICENSE",
      "license_sha256": "a45ba66fa502c49ad108440536d8aa91dfe9c04575a32a01287839bee336199c",
      "source_commit": "8cb2fbc7a1e9e08f20fc5fc6a45e1046ad0369b9",
      "reviewed_at": "2026-11-17T04:07:37.955235+00:00",
      "evidence_pinned_at": "2026-11-17T04:07:37.955235+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "Applies to repository code and documentation; external models, services, data and assets retain their own terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-13T20:34:37Z",
        "reviewed_at": "2026-11-17T04:07:37.955235+00:00",
        "url": "https://github.com/ruvnet/ruflo/commit/8971ebad35fe2b37888f66bfd266ee1128f458a7",
        "qualifies": true,
        "reason": {
          "zh-CN": "将配置的嵌入模型和向量维度传入 AgentDB。校验生成维度，并避免把默认模型错误标为自定义模型。",
          "en": "Passes configured embedding models and vector dimensions into AgentDB, validates generated dimensions and avoids labeling default embeddings as a custom model."
        },
        "reviewed_files": [
          "v3/@claude-flow/cli/src/memory/memory-bridge.ts",
          "v3/@claude-flow/memory/src/controller-registry.ts"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/ruvnet/ruflo",
        "accessed_at": "2026-11-17T04:07:37.955235+00:00"
      },
      {
        "url": "https://github.com/ruvnet/ruflo/blob/8cb2fbc7a1e9e08f20fc5fc6a45e1046ad0369b9/README.md",
        "accessed_at": "2026-11-17T04:07:37.955235+00:00"
      },
      {
        "url": "https://github.com/ruvnet/ruflo/blob/8cb2fbc7a1e9e08f20fc5fc6a45e1046ad0369b9/LICENSE",
        "accessed_at": "2026-11-17T04:07:37.955235+00:00"
      },
      {
        "url": "https://github.com/ruvnet/ruflo/commit/8971ebad35fe2b37888f66bfd266ee1128f458a7",
        "accessed_at": "2026-11-17T04:07:37.955235+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 6780,
      "source_url": "https://github.com/trending/typescript?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOO07yiQ",
    "full_name": "ruvnet/ruflo",
    "stargazers_count": 81892,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "a45ba66fa502c49ad108440536d8aa91dfe9c04575a32a01287839bee336199c",
    "last_success_at": "2026-11-17T03:54:57.547917+00:00"
  }
}
```

</details>
