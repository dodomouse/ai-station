# MiroFish

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[666ghj/MiroFish](https://github.com/666ghj/MiroFish)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 85784 |
| 许可证 / License | AGPL-3.0 |
| 评估时间 / Evaluated at | 2026-11-17T04:07:37.955887+00:00 |

## 中文

### 当前收录状态

2026-11-17 按用户要求转为正式收录。本次是目录状态迁移，未重新核实全部新准入条件。原有 Star、活动与功能记录保留原核对日期，许可不再决定收录状态。

### 先前介绍与复核记录（历史）

根据输入资料构建多智能体模拟环境，探索群体互动和不同情景。


### 用途与功能

- 从种子资料抽取实体、关系和角色设定。
- 运行智能体互动并保存模拟过程中的记忆。
- 生成模拟报告，并支持与模拟角色继续对话。

### 环境与限制

源码部署要求 Node.js 18+、Python 3.11–3.12 和 uv，需配置 LLM 与 Zep Cloud API Key，也可用 Docker。多轮模拟会消耗模型额度；模拟结果不等于经过验证的现实预测。

### 开始使用

阅读 README 并配置环境变量，按源码或 Docker 方式启动，从少轮次的小型情景检查图谱、模拟记录和报告。

参阅[官方 README](https://github.com/666ghj/MiroFish/blob/7657031ac01184afe2cb220f5ee3545573b5e843/README.md)。

### 收录与来源

适合探索多智能体社会模拟的工作流程。先前评估因近期实质维护证据不足而保留为候选；该结论已由 2026-11-17 转正取代，不是当前状态。

维护证据：[该提交仅更新 Star History 数据与图像，不能作为功能或缺陷修复证据。近三个月未核到实质维护。](https://github.com/666ghj/MiroFish/commit/7657031ac01184afe2cb220f5ee3545573b5e843)（2026-10-01）。

发现于 [GitHub 月榜](https://github.com/trending/python?since=monthly)。2026-11-17 的榜单记录新增 6,391 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

### Current catalog status

Promoted to an included entry on 2026-11-17 at the user’s request. This is a catalog transition, not a new verification of every admission criterion. Stars, activity and feature records retain their original review dates; licensing no longer determines admission.

### Earlier description and review (historical)

Builds multi-agent simulation environments from input materials to explore group interactions and scenarios.


### Uses and features

- Extracts entities, relationships and personas from seed material.
- Runs agent interactions and retains simulation memory.
- Generates simulation reports and supports follow-up conversations with simulated agents.

### Requirements and limits

Source deployment requires Node.js 18+, Python 3.11–3.12 and uv, plus LLM and Zep Cloud API keys; Docker is also documented. Multiround simulations consume model usage, and simulated outcomes are not validated real-world forecasts.

### Getting started

Read the README, configure environment variables and start from source or Docker, then inspect graphs, simulation records and reports on a small scenario with few rounds.

See the [official README](https://github.com/666ghj/MiroFish/blob/7657031ac01184afe2cb220f5ee3545573b5e843/README.md).

### Review and provenance

Useful for exploring multi-agent social-simulation workflows. The earlier assessment retained it as a candidate because recent substantive maintenance evidence was insufficient. That decision was superseded by the 2026-11-17 promotion and is not the current status.

Maintenance evidence: [This commit only updates Star History data and images, providing no feature or bug-fix evidence; no substantive maintenance was verified in the three-month window.](https://github.com/666ghj/MiroFish/commit/7657031ac01184afe2cb220f5ee3545573b5e843) (2026-10-01).

Discovered in [GitHub monthly Trending](https://github.com/trending/python?since=monthly), which recorded 6,391 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:07:37.955887+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "admission_basis": "user_directed_transition",
    "policy_id": "ai-activity-stars-2026-11-17",
    "admitted_at": "2026-11-17T13:33:30.547820+00:00"
  },
  "metadata": {
    "schema_version": 1,
    "id": "mirofish",
    "name": "MiroFish",
    "repository": "666ghj/MiroFish",
    "repo_node_id": "R_kgDOQdLIuw",
    "category": "ai",
    "summary": {
      "zh-CN": "根据输入资料构建多智能体模拟环境，探索群体互动和不同情景。",
      "en": "Builds multi-agent simulation environments from input materials to explore group interactions and scenarios."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:07:37.955887+00:00",
        "en": "2026-11-17T04:07:37.955887+00:00"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "AGPL-3.0",
      "osi_approved": true,
      "source_url": "https://github.com/666ghj/MiroFish/blob/7657031ac01184afe2cb220f5ee3545573b5e843/LICENSE",
      "license_sha256": "8486a10c4393cee1c25392769ddd3b2d6c242d6ec7928e1414efff7dfb2f07ef",
      "source_commit": "7657031ac01184afe2cb220f5ee3545573b5e843",
      "reviewed_at": "2026-11-17T04:07:37.955887+00:00",
      "evidence_pinned_at": "2026-11-17T04:07:37.955887+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "Root code license is AGPL-3.0; model services, Zep Cloud, input materials and dependencies retain their own terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-10-01T18:20:36Z",
        "reviewed_at": "2026-11-17T04:07:37.955887+00:00",
        "url": "https://github.com/666ghj/MiroFish/commit/7657031ac01184afe2cb220f5ee3545573b5e843",
        "qualifies": false,
        "reason": {
          "zh-CN": "该提交仅更新 Star History 数据与图像，不能作为功能或缺陷修复证据。近三个月未核到实质维护。",
          "en": "This commit only updates Star History data and images, providing no feature or bug-fix evidence; no substantive maintenance was verified in the three-month window."
        },
        "reviewed_files": [
          ".github/star-history/history.json",
          "static/image/star-history-dark.svg",
          "static/image/star-history-light.svg"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/666ghj/MiroFish",
        "accessed_at": "2026-11-17T04:07:37.955887+00:00"
      },
      {
        "url": "https://github.com/666ghj/MiroFish/blob/7657031ac01184afe2cb220f5ee3545573b5e843/README.md",
        "accessed_at": "2026-11-17T04:07:37.955887+00:00"
      },
      {
        "url": "https://github.com/666ghj/MiroFish/blob/7657031ac01184afe2cb220f5ee3545573b5e843/LICENSE",
        "accessed_at": "2026-11-17T04:07:37.955887+00:00"
      },
      {
        "url": "https://github.com/666ghj/MiroFish/commit/7657031ac01184afe2cb220f5ee3545573b5e843",
        "accessed_at": "2026-11-17T04:07:37.955887+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 6391,
      "source_url": "https://github.com/trending/python?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOQdLIuw",
    "full_name": "666ghj/MiroFish",
    "stargazers_count": 85784,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "AGPL-3.0",
    "license_sha256": "8486a10c4393cee1c25392769ddd3b2d6c242d6ec7928e1414efff7dfb2f07ef",
    "last_success_at": "2026-11-17T03:55:05.704236+00:00"
  },
  "eligibility_history": [
    {
      "status": "needs_review",
      "reasons": [
        "recent_substantive_activity_unverified"
      ],
      "evaluated_at": "2026-11-17T04:07:37.955887+00:00",
      "superseded_at": "2026-11-17T13:33:30.547820+00:00",
      "superseded_by": "user_directed_transition_2026_11_17",
      "pending_actions": {
        "zh-CN": [
          "补充近三个月功能或缺陷修复提交，并核对具体实现差异。"
        ],
        "en": [
          "Provide a feature or bug-fix commit within the last three months and review its implementation diff."
        ]
      },
      "quality_review": {
        "zh-CN": "适合探索多智能体社会模拟的工作流程；近期实质维护证据不足，保留为候选。",
        "en": "Useful for exploring multi-agent social-simulation workflows; retained as a candidate because recent substantive maintenance evidence is insufficient.",
        "verification_level": "docs"
      }
    }
  ]
}
```

</details>
