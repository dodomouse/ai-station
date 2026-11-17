# OpenCode

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[anomalyco/opencode](https://github.com/anomalyco/opencode)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 227359 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T04:07:37.950012+00:00 |

## 中文

在终端或桌面界面中调用模型，完成代码探索、规划和修改。

### 用途与功能

- 提供可切换的 build 和 plan 智能体。
- plan 默认拒绝编辑，并在执行 shell 命令前请求权限。
- 支持通用子智能体处理搜索和多步骤任务。

### 环境与限制

需要配置可用的模型访问方式，模型服务的费用与条款独立适用。build 可修改文件和执行开发操作；桌面应用仍标为 Beta。

### 开始使用

按 README 安装 CLI 或桌面应用，配置模型，在项目目录先用 plan 模式探索任务。

参阅[官方 README](https://github.com/anomalyco/opencode/blob/32974e0c5743cd70def6f013fe2bcb48e7e44792/README.md)。

### 收录与来源

适合在同一开发入口中切换代码分析与实施任务。

维护证据：[修复单个 well-known 配置源不可达时丢弃全部来源的问题。对失败来源记录警告，并保留其余来源。](https://github.com/anomalyco/opencode/commit/5cdf288a8cabf718e7590f6ed556cd333f9a7812)（2026-11-17）。

发现于 [GitHub 月榜](https://github.com/trending/typescript?since=monthly)。2026-11-17 的榜单记录新增 14,552 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Uses models in terminal or desktop interfaces to explore, plan and modify code.

### Uses and features

- Offers switchable build and plan agents.
- The plan agent denies edits by default and requests permission for shell commands.
- Provides a general subagent for searches and multistep tasks.

### Requirements and limits

Requires configured model access, with provider costs and terms applying separately. The build agent can modify files and perform development operations; the desktop app is labeled beta.

### Getting started

Install the CLI or desktop app from the README, configure a model, and explore a project task with the plan agent.

See the [official README](https://github.com/anomalyco/opencode/blob/32974e0c5743cd70def6f013fe2bcb48e7e44792/README.md).

### Review and provenance

Useful for switching between code analysis and implementation in one development interface.

Maintenance evidence: [Keeps reachable well-known configuration sources when one fails, logging and skipping individual failures.](https://github.com/anomalyco/opencode/commit/5cdf288a8cabf718e7590f6ed556cd333f9a7812) (2026-11-17).

Discovered in [GitHub monthly Trending](https://github.com/trending/typescript?since=monthly), which recorded 14,552 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:07:37.950012+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "opencode",
    "name": "OpenCode",
    "repository": "anomalyco/opencode",
    "repo_node_id": "R_kgDOOiiGLw",
    "category": "ai",
    "summary": {
      "zh-CN": "在终端或桌面界面中调用模型，完成代码探索、规划和修改。",
      "en": "Uses models in terminal or desktop interfaces to explore, plan and modify code."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:07:37.950012+00:00",
        "en": "2026-11-17T04:07:37.950012+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合在同一开发入口中切换代码分析与实施任务。",
      "en": "Useful for switching between code analysis and implementation in one development interface.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/anomalyco/opencode/blob/32974e0c5743cd70def6f013fe2bcb48e7e44792/LICENSE",
      "license_sha256": "625f0f619133f89bbbb2abe37369613dfa1885eba1e50d02170deb62bb42cb6b",
      "source_commit": "32974e0c5743cd70def6f013fe2bcb48e7e44792",
      "reviewed_at": "2026-11-17T04:07:37.950012+00:00",
      "evidence_pinned_at": "2026-11-17T04:07:37.950012+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "Applies to repository code and documentation; external models, services, data and assets retain their own terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-17T03:01:46Z",
        "reviewed_at": "2026-11-17T04:07:37.950012+00:00",
        "url": "https://github.com/anomalyco/opencode/commit/5cdf288a8cabf718e7590f6ed556cd333f9a7812",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复单个 well-known 配置源不可达时丢弃全部来源的问题。对失败来源记录警告，并保留其余来源。",
          "en": "Keeps reachable well-known configuration sources when one fails, logging and skipping individual failures."
        },
        "reviewed_files": [
          "packages/core/src/wellknown.ts",
          "packages/core/test/wellknown.test.ts"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/anomalyco/opencode",
        "accessed_at": "2026-11-17T04:07:37.950012+00:00"
      },
      {
        "url": "https://github.com/anomalyco/opencode/blob/32974e0c5743cd70def6f013fe2bcb48e7e44792/README.md",
        "accessed_at": "2026-11-17T04:07:37.950012+00:00"
      },
      {
        "url": "https://github.com/anomalyco/opencode/blob/32974e0c5743cd70def6f013fe2bcb48e7e44792/LICENSE",
        "accessed_at": "2026-11-17T04:07:37.950012+00:00"
      },
      {
        "url": "https://github.com/anomalyco/opencode/commit/5cdf288a8cabf718e7590f6ed556cd333f9a7812",
        "accessed_at": "2026-11-17T04:07:37.950012+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 14552,
      "source_url": "https://github.com/trending/typescript?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOOiiGLw",
    "full_name": "anomalyco/opencode",
    "stargazers_count": 227359,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "625f0f619133f89bbbb2abe37369613dfa1885eba1e50d02170deb62bb42cb6b",
    "last_success_at": "2026-11-17T03:53:17.276973+00:00"
  }
}
```

</details>
