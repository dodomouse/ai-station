# Gemini CLI

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[google-gemini/gemini-cli](https://github.com/google-gemini/gemini-cli)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 108884 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-17T04:00:03.483009+00:00 |

## 中文

面向企业 Gemini Code Assist 工作流的终端 AI 智能体，可读取代码、编辑文件和运行工具。

### 用途与功能

- 通过 MCP 扩展工具，并用 GEMINI.md 提供项目说明。
- 支持交互会话与用于脚本的非交互输出。

### 环境与限制

当前 README 主要支持企业 Code Assist；个人免费及 Google AI Pro/Ultra 入口已迁至 Antigravity CLI。需相应组织授权或受支持 API/Vertex 凭据；项目未针对 Gemini 4+ 优化。

### 开始使用

按 README 安装 @google/gemini-cli，运行 gemini 并选择组织账户或 API 认证，再从只读代码查询开始。

参阅[官方 README](https://github.com/google-gemini/gemini-cli/blob/4fa64e71b9b4e1bb65a86cc2863574f561b82340/README.md)。

### 收录与来源

提供企业认证、工具配置和脚本入口，适合已采用 Gemini Code Assist 的开发团队。

维护证据：[列出模型前初始化认证能力、检查强制认证类型，并对手动模型选项去重。](https://github.com/google-gemini/gemini-cli/commit/4ed06ed0ddc523a6d356a4ad35ddfea331041888)（2026-11-13）。

发现于 [GitHub 月榜](https://github.com/trending/typescript?since=monthly)。2026-11-17 的榜单记录新增 2,021 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

A terminal AI agent maintained for enterprise Gemini Code Assist workflows, with code inspection, file editing and tool execution.

### Uses and features

- Extends tools through MCP and takes project instructions from GEMINI.md.
- Supports interactive sessions and noninteractive output for scripts.

### Requirements and limits

The current README focuses on enterprise Code Assist; individual free and Google AI Pro/Ultra access moved to Antigravity CLI. Requires organizational access or supported API/Vertex credentials; it is not optimized for Gemini 4+.

### Getting started

Install @google/gemini-cli using the README, run gemini, configure organizational or API authentication, and begin with a read-only code query.

See the [official README](https://github.com/google-gemini/gemini-cli/blob/4fa64e71b9b4e1bb65a86cc2863574f561b82340/README.md).

### Review and provenance

Offers enterprise authentication, tool configuration and scripting entry points for teams using Gemini Code Assist.

Maintenance evidence: [Initializes authentication capabilities and checks enforced auth before listing models, while deduplicating manual model options.](https://github.com/google-gemini/gemini-cli/commit/4ed06ed0ddc523a6d356a4ad35ddfea331041888) (2026-11-13).

Discovered in [GitHub monthly Trending](https://github.com/trending/typescript?since=monthly), which recorded 2,021 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:00:03.483009+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "gemini-cli",
    "name": "Gemini CLI",
    "repository": "google-gemini/gemini-cli",
    "repo_node_id": "R_kgDOObWEYA",
    "category": "ai",
    "summary": {
      "zh-CN": "面向企业 Gemini Code Assist 工作流的终端 AI 智能体，可读取代码、编辑文件和运行工具。",
      "en": "A terminal AI agent maintained for enterprise Gemini Code Assist workflows, with code inspection, file editing and tool execution."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:00:03.483009+00:00",
        "en": "2026-11-17T04:00:03.483009+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "提供企业认证、工具配置和脚本入口，适合已采用 Gemini Code Assist 的开发团队。",
      "en": "Offers enterprise authentication, tool configuration and scripting entry points for teams using Gemini Code Assist.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "source_url": "https://github.com/google-gemini/gemini-cli/blob/4fa64e71b9b4e1bb65a86cc2863574f561b82340/LICENSE",
      "license_sha256": "58d1e17ffe5109a7ae296caafcadfdbe6a7d176f0bc4ab01e12a689b0499d8bd",
      "source_commit": "4fa64e71b9b4e1bb65a86cc2863574f561b82340",
      "reviewed_at": "2026-11-17T04:00:03.483009+00:00",
      "evidence_pinned_at": "2026-11-17T04:00:03.483009+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "Root license applies to repository software code; models, data, assets and external services have separate terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-13T19:49:40Z",
        "reviewed_at": "2026-11-17T04:00:03.483009+00:00",
        "url": "https://github.com/google-gemini/gemini-cli/commit/4ed06ed0ddc523a6d356a4ad35ddfea331041888",
        "qualifies": true,
        "reason": {
          "zh-CN": "列出模型前初始化认证能力、检查强制认证类型，并对手动模型选项去重。",
          "en": "Initializes authentication capabilities and checks enforced auth before listing models, while deduplicating manual model options."
        },
        "reviewed_files": [
          "packages/cli/src/acp/acpUtils.ts",
          "packages/cli/src/commands/models/list.ts"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/google-gemini/gemini-cli",
        "accessed_at": "2026-11-17T04:00:03.483009+00:00"
      },
      {
        "url": "https://github.com/google-gemini/gemini-cli/blob/4fa64e71b9b4e1bb65a86cc2863574f561b82340/README.md",
        "accessed_at": "2026-11-17T04:00:03.483009+00:00"
      },
      {
        "url": "https://github.com/google-gemini/gemini-cli/blob/4fa64e71b9b4e1bb65a86cc2863574f561b82340/LICENSE",
        "accessed_at": "2026-11-17T04:00:03.483009+00:00"
      },
      {
        "url": "https://github.com/google-gemini/gemini-cli/commit/4ed06ed0ddc523a6d356a4ad35ddfea331041888",
        "accessed_at": "2026-11-17T04:00:03.483009+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 2021,
      "source_url": "https://github.com/trending/typescript?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOObWEYA",
    "full_name": "google-gemini/gemini-cli",
    "stargazers_count": 108884,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "58d1e17ffe5109a7ae296caafcadfdbe6a7d176f0bc4ab01e12a689b0499d8bd",
    "last_success_at": "2026-11-17T03:51:13.058439+00:00"
  }
}
```

</details>
