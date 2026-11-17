# PR-Agent

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[The-PR-Agent/pr-agent](https://github.com/The-PR-Agent/pr-agent)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 16305 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T04:07:37.960878+00:00 |

## 中文

用大模型分析拉取请求，生成变更说明、代码审查意见和针对差异的问答。

### 用途与功能

- 提供多种拉取请求命令，包括 describe、review 和 ask。
- 支持 CLI、GitHub Actions、Docker 和 webhook 部署方式。
- 可配置模型、提示词和代码托管平台集成。

### 环境与限制

需要相应 Git 平台凭据和模型服务，Python 安装需选择对应平台的可选依赖。发送给云模型的差异受服务商数据条款约束。MIT 覆盖社区 PR-Agent 代码；Qodo 商业产品是独立服务，自动审查结果仍需人工判断。

### 开始使用

按 README 选择 CLI 或 GitHub Actions 路径，配置平台令牌和模型，再对测试 PR 运行 review。

参阅[官方 README](https://github.com/The-PR-Agent/pr-agent/blob/a7749abad3d2805da2638a0dc44990e91b528661/README.md)。

### 收录与来源

适合把变更摘要和初步审查接入现有 PR 流程，并保留自托管与配置能力。

维护证据：[写入结构化审查前先序列化 JSON，避免序列化失败时截断已有文件](https://github.com/The-PR-Agent/pr-agent/commit/a7749abad3d2805da2638a0dc44990e91b528661)（2026-11-16）。

发现于 [GitHub 月榜](https://github.com/trending/python?since=monthly)。2026-11-17 的榜单记录新增 2,921 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Use LLMs to analyze pull requests, generate change descriptions and reviews, and answer questions about diffs.

### Uses and features

- Handle pull requests through commands such as describe, review and ask.
- Support CLI, GitHub Actions, Docker and webhook deployment.
- Configure models, prompts and code-hosting integrations.

### Requirements and limits

Requires Git-provider credentials and a model service; Python installations need the appropriate provider extras. Diffs sent to cloud models are subject to provider data terms. MIT covers the community PR-Agent code; the Qodo commercial offering is a separate service. Automated reviews still require human judgment.

### Getting started

Choose the CLI or GitHub Actions path in the README, configure provider credentials and a model, then run review on a test PR.

See the [official README](https://github.com/The-PR-Agent/pr-agent/blob/a7749abad3d2805da2638a0dc44990e91b528661/README.md).

### Review and provenance

Useful for integrating change summaries and initial reviews into an existing PR workflow with self-hosting and configuration control.

Maintenance evidence: [Serializes structured reviews before opening the output file, avoiding truncation when JSON serialization fails](https://github.com/The-PR-Agent/pr-agent/commit/a7749abad3d2805da2638a0dc44990e91b528661) (2026-11-16).

Discovered in [GitHub monthly Trending](https://github.com/trending/python?since=monthly), which recorded 2,921 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:07:37.960878+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "pr-agent",
    "name": "PR-Agent",
    "repository": "The-PR-Agent/pr-agent",
    "repo_node_id": "R_kgDOJ4EDkg",
    "category": "development",
    "summary": {
      "zh-CN": "用大模型分析拉取请求，生成变更说明、代码审查意见和针对差异的问答。",
      "en": "Use LLMs to analyze pull requests, generate change descriptions and reviews, and answer questions about diffs."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:07:37.960878+00:00",
        "en": "2026-11-17T04:07:37.960878+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合把变更摘要和初步审查接入现有 PR 流程，并保留自托管与配置能力。",
      "en": "Useful for integrating change summaries and initial reviews into an existing PR workflow with self-hosting and configuration control.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/The-PR-Agent/pr-agent/blob/a7749abad3d2805da2638a0dc44990e91b528661/LICENSE",
      "license_sha256": "ea19f3b6bfd70ce0bf8d60fc5b15cdb789fcf86a63c0d6542977f888519f5788",
      "source_commit": "a7749abad3d2805da2638a0dc44990e91b528661",
      "reviewed_at": "2026-11-17T04:07:37.960878+00:00",
      "evidence_pinned_at": "2026-11-17T04:07:37.960878+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "MIT covers the community PR-Agent project, not Qodo commercial services or external model and Git hosting services."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-16T21:52:41Z",
        "reviewed_at": "2026-11-17T04:07:37.960878+00:00",
        "url": "https://github.com/The-PR-Agent/pr-agent/commit/a7749abad3d2805da2638a0dc44990e91b528661",
        "qualifies": true,
        "reason": {
          "zh-CN": "写入结构化审查前先序列化 JSON，避免序列化失败时截断已有文件",
          "en": "Serializes structured reviews before opening the output file, avoiding truncation when JSON serialization fails"
        },
        "reviewed_files": [
          "pr_agent/algo/review_json_output.py"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/The-PR-Agent/pr-agent",
        "accessed_at": "2026-11-17T04:07:37.960878+00:00"
      },
      {
        "url": "https://github.com/The-PR-Agent/pr-agent/blob/a7749abad3d2805da2638a0dc44990e91b528661/README.md",
        "accessed_at": "2026-11-17T04:07:37.960878+00:00"
      },
      {
        "url": "https://github.com/The-PR-Agent/pr-agent/blob/a7749abad3d2805da2638a0dc44990e91b528661/LICENSE",
        "accessed_at": "2026-11-17T04:07:37.960878+00:00"
      },
      {
        "url": "https://github.com/The-PR-Agent/pr-agent/commit/a7749abad3d2805da2638a0dc44990e91b528661",
        "accessed_at": "2026-11-17T04:07:37.960878+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 2921,
      "source_url": "https://github.com/trending/python?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOJ4EDkg",
    "full_name": "The-PR-Agent/pr-agent",
    "stargazers_count": 16305,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "ea19f3b6bfd70ce0bf8d60fc5b15cdb789fcf86a63c0d6542977f888519f5788",
    "last_success_at": "2026-11-17T03:52:40.035089+00:00"
  }
}
```

</details>
