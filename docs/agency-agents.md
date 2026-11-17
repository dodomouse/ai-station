# Agency Agents

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 168864 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T04:07:37.953119+00:00 |

## 中文

提供按专业角色组织的 AI 智能体指令、工作步骤和交付模板。

### 用途与功能

- 按多个领域组织角色文件，包括工程、设计和测试。
- 为角色定义任务流程、输出要求和参考示例。
- 提供转换和安装脚本，适配不同智能体宿主。

### 环境与限制

这是一组角色指令与配套脚本，需要模型及智能体宿主执行；不同宿主的工具能力有差异。角色描述中的专业能力和成功指标不代表经过验证的结果，输出仍需审查。

### 开始使用

先阅读一个目标领域的角色文件，按 README 安装到所用宿主，或将其作为可调整的参考模板。

参阅[官方 README](https://github.com/msitarzewski/agency-agents/blob/8ae6164602c95ca78828b148b9052460ee426885/README.md)。

### 收录与来源

适合为常见任务复用角色分工和交付结构，减少重复编写提示。

维护证据：[修正实验跟踪角色的执行规则。要求预先设定显著性、功效和停止规则，并将无显著结果记录为有效发现。](https://github.com/msitarzewski/agency-agents/commit/0f3c87babdbfb5762190ab87a6da424321ffe9ae)（2026-11-07）。

发现于 [GitHub 月榜](https://github.com/trending/shell?since=monthly)。2026-11-17 的榜单记录新增 8,817 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Provides AI-agent instructions, workflows and deliverable templates organized by professional role.

### Uses and features

- Organizes role files across engineering, design, testing and other domains.
- Defines workflows, output requirements and examples for each role.
- Includes conversion and installation scripts for different agent hosts.

### Requirements and limits

This collection contains role instructions and supporting scripts, requiring a model and agent host to execute them. Tool capabilities vary by host. Claimed expertise and success metrics are not validated outcomes, and outputs need review.

### Getting started

Read one role file for your domain, then install it into your host as documented or adapt it as a reference template.

See the [official README](https://github.com/msitarzewski/agency-agents/blob/8ae6164602c95ca78828b148b9052460ee426885/README.md).

### Review and provenance

Useful for reusing role responsibilities and deliverable structures across recurring tasks.

Maintenance evidence: [Revises the experiment-tracker workflow to prespecify significance, power and stopping rules and retain null or inconclusive findings as valid results.](https://github.com/msitarzewski/agency-agents/commit/0f3c87babdbfb5762190ab87a6da424321ffe9ae) (2026-11-07).

Discovered in [GitHub monthly Trending](https://github.com/trending/shell?since=monthly), which recorded 8,817 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:07:37.953119+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "agency-agents",
    "name": "Agency Agents",
    "repository": "msitarzewski/agency-agents",
    "repo_node_id": "R_kgDOQBjiAQ",
    "category": "ai",
    "summary": {
      "zh-CN": "提供按专业角色组织的 AI 智能体指令、工作步骤和交付模板。",
      "en": "Provides AI-agent instructions, workflows and deliverable templates organized by professional role."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:07:37.953119+00:00",
        "en": "2026-11-17T04:07:37.953119+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合为常见任务复用角色分工和交付结构，减少重复编写提示。",
      "en": "Useful for reusing role responsibilities and deliverable structures across recurring tasks.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/msitarzewski/agency-agents/blob/8ae6164602c95ca78828b148b9052460ee426885/LICENSE",
      "license_sha256": "9a45258434d5cedf0af73c9ad4771373701225038d246c49219026c33677f66f",
      "source_commit": "8ae6164602c95ca78828b148b9052460ee426885",
      "reviewed_at": "2026-11-17T04:07:37.953119+00:00",
      "evidence_pinned_at": "2026-11-17T04:07:37.953119+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "Applies to repository code and documentation; external models, services, data and assets retain their own terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-07T00:45:06Z",
        "reviewed_at": "2026-11-17T04:07:37.953119+00:00",
        "url": "https://github.com/msitarzewski/agency-agents/commit/0f3c87babdbfb5762190ab87a6da424321ffe9ae",
        "qualifies": true,
        "reason": {
          "zh-CN": "修正实验跟踪角色的执行规则。要求预先设定显著性、功效和停止规则，并将无显著结果记录为有效发现。",
          "en": "Revises the experiment-tracker workflow to prespecify significance, power and stopping rules and retain null or inconclusive findings as valid results."
        },
        "reviewed_files": [
          "project-management/project-management-experiment-tracker.md"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/msitarzewski/agency-agents",
        "accessed_at": "2026-11-17T04:07:37.953119+00:00"
      },
      {
        "url": "https://github.com/msitarzewski/agency-agents/blob/8ae6164602c95ca78828b148b9052460ee426885/README.md",
        "accessed_at": "2026-11-17T04:07:37.953119+00:00"
      },
      {
        "url": "https://github.com/msitarzewski/agency-agents/blob/8ae6164602c95ca78828b148b9052460ee426885/LICENSE",
        "accessed_at": "2026-11-17T04:07:37.953119+00:00"
      },
      {
        "url": "https://github.com/msitarzewski/agency-agents/commit/0f3c87babdbfb5762190ab87a6da424321ffe9ae",
        "accessed_at": "2026-11-17T04:07:37.953119+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 8817,
      "source_url": "https://github.com/trending/shell?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOQBjiAQ",
    "full_name": "msitarzewski/agency-agents",
    "stargazers_count": 168864,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "9a45258434d5cedf0af73c9ad4771373701225038d246c49219026c33677f66f",
    "last_success_at": "2026-11-17T03:53:58.221758+00:00"
  }
}
```

</details>
