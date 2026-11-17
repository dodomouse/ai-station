# Plannotator

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[backnotprop/plannotator](https://github.com/backnotprop/plannotator)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 12679 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-17T04:07:37.961386+00:00 |

## 中文

为 AI 智能体提供本地浏览器审阅界面。支持批注计划、文档、网页产物和代码差异，并把反馈送回会话。

### 用途与功能

- 批注文档和 HTML 产物，提出修改意见。
- 审阅本地差异或远程 PR，并向智能体返回行级反馈。
- 通过 Inbox 汇集多个智能体的问题、文件和待审阅内容。

### 环境与限制

需要本地浏览器和受支持的智能体集成；源码开发使用 Bun。远程模式需转发端口并限制网络访问，分享功能可能上传加密内容。README 提供 Apache-2.0 或 MIT 二选一许可，本条目固定核对 Apache 选项；外部 AI 服务和集成另有条款。

### 开始使用

按 README 安装对应平台版本并配置智能体，然后运行 `plannotator review` 审阅差异，或 `plannotator inbox` 打开待办界面。

参阅[官方 README](https://github.com/backnotprop/plannotator/blob/d3e72f346d93d16c7046d71ce97207de5441129c/README.md)。

### 收录与来源

适合需要在智能体继续实施前集中审阅计划、代码和产物，并保留可操作反馈的工作流。

维护证据：[区分差异加载失败类型，并在服务器不可达或会话不明时禁止提交审阅决定](https://github.com/backnotprop/plannotator/commit/c1ea7d68b960ec99d21e9f53489a4d5622bff87f)（2026-11-17）。

发现于 [GitHub 月榜](https://github.com/trending?since=monthly)。2026-11-17 的榜单记录新增 2,848 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Provide a local browser review interface for AI agents, annotating plans, documents, web artifacts and code diffs and returning feedback to the session.

### Uses and features

- Annotate documents and HTML artifacts with requested changes.
- Review local diffs or remote PRs and return line-level feedback to an agent.
- Collect questions, files and review requests from multiple agents in an Inbox.

### Requirements and limits

Requires a local browser and supported agent integration; source development uses Bun. Remote mode requires port forwarding and network access controls, while sharing may upload encrypted content. The README offers Apache-2.0 or MIT at your option; this entry pins the Apache option. External AI services and integrations have separate terms.

### Getting started

Install the platform version and configure your agent following the README, then run `plannotator review` for diffs or `plannotator inbox` for incoming review work.

See the [official README](https://github.com/backnotprop/plannotator/blob/d3e72f346d93d16c7046d71ce97207de5441129c/README.md).

### Review and provenance

Useful for workflows that review agent plans, code and artifacts while returning actionable feedback.

Maintenance evidence: [Distinguishes diff-loading failures and disables review decisions when the server is unreachable or the session is uncertain](https://github.com/backnotprop/plannotator/commit/c1ea7d68b960ec99d21e9f53489a4d5622bff87f) (2026-11-17).

Discovered in [GitHub monthly Trending](https://github.com/trending?since=monthly), which recorded 2,848 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:07:37.961386+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "plannotator",
    "name": "Plannotator",
    "repository": "backnotprop/plannotator",
    "repo_node_id": "R_kgDOQv43sg",
    "category": "development",
    "summary": {
      "zh-CN": "为 AI 智能体提供本地浏览器审阅界面。支持批注计划、文档、网页产物和代码差异，并把反馈送回会话。",
      "en": "Provide a local browser review interface for AI agents, annotating plans, documents, web artifacts and code diffs and returning feedback to the session."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:07:37.961386+00:00",
        "en": "2026-11-17T04:07:37.961386+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合需要在智能体继续实施前集中审阅计划、代码和产物，并保留可操作反馈的工作流。",
      "en": "Useful for workflows that review agent plans, code and artifacts while returning actionable feedback.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "source_url": "https://github.com/backnotprop/plannotator/blob/d3e72f346d93d16c7046d71ce97207de5441129c/LICENSE-APACHE",
      "license_sha256": "b96752709405e4b4eefda5514d01941a25d78230bddd891523279fed63eed5e0",
      "source_commit": "d3e72f346d93d16c7046d71ce97207de5441129c",
      "reviewed_at": "2026-11-17T04:07:37.961386+00:00",
      "evidence_pinned_at": "2026-11-17T04:07:37.961386+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "The pinned README offers Apache-2.0 OR MIT. This record selects and hashes LICENSE-APACHE; external AI providers and integrations are outside that license."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-17T03:06:06Z",
        "reviewed_at": "2026-11-17T04:07:37.961386+00:00",
        "url": "https://github.com/backnotprop/plannotator/commit/c1ea7d68b960ec99d21e9f53489a4d5622bff87f",
        "qualifies": true,
        "reason": {
          "zh-CN": "区分差异加载失败类型，并在服务器不可达或会话不明时禁止提交审阅决定",
          "en": "Distinguishes diff-loading failures and disables review decisions when the server is unreachable or the session is uncertain"
        },
        "reviewed_files": [
          "packages/review-editor/utils/diffLoadFailure.ts"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/backnotprop/plannotator",
        "accessed_at": "2026-11-17T04:07:37.961386+00:00"
      },
      {
        "url": "https://github.com/backnotprop/plannotator/blob/d3e72f346d93d16c7046d71ce97207de5441129c/README.md",
        "accessed_at": "2026-11-17T04:07:37.961386+00:00"
      },
      {
        "url": "https://github.com/backnotprop/plannotator/blob/d3e72f346d93d16c7046d71ce97207de5441129c/LICENSE-APACHE",
        "accessed_at": "2026-11-17T04:07:37.961386+00:00"
      },
      {
        "url": "https://github.com/backnotprop/plannotator/commit/c1ea7d68b960ec99d21e9f53489a4d5622bff87f",
        "accessed_at": "2026-11-17T04:07:37.961386+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 2848,
      "source_url": "https://github.com/trending?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOQv43sg",
    "full_name": "backnotprop/plannotator",
    "stargazers_count": 12679,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "b96752709405e4b4eefda5514d01941a25d78230bddd891523279fed63eed5e0",
    "last_success_at": "2026-11-17T03:52:42.455263+00:00"
  }
}
```

</details>
