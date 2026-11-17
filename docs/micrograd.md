# micrograd

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[karpathy/micrograd](https://github.com/karpathy/micrograd)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 候选 / Candidate |
| Star | 18968 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T04:00:03.487232+00:00 |

## 中文

用于学习反向自动微分的微型标量引擎，并附带简单神经网络模块。

候选原因：尚无三个月内的实质维护证据；最近提交只是 README 链接更新。

### 用途与功能

- 动态建立计算图并计算标量梯度。
- 提供二分类 MLP 示例及 Graphviz 计算图演示。

### 环境与限制

核心为 Python 标量运算，不适合大规模张量训练；笔记本与可视化需相应依赖，梯度对照测试使用 PyTorch。

### 开始使用

安装 micrograd，从 Value 运算和 backward() 示例开始，再阅读 demo.ipynb。

参阅[官方 README](https://github.com/karpathy/micrograd/blob/7bc720e951fe422b8f8814aa5aa1b64121d26b4c/README.md)。

### 收录与来源

实现紧凑，便于逐步理解计算图与梯度传播；当前缺少目录要求的近期实质维护证据。

维护证据：[最近提交仅在 README 增加外部 microgpt 教程链接，未修改自动微分实现，且已超出三个月窗口。](https://github.com/karpathy/micrograd/commit/7bc720e951fe422b8f8814aa5aa1b64121d26b4c)（2026-08-03）。

发现于 [GitHub 月榜](https://github.com/trending/jupyter-notebook?since=monthly)。2026-11-17 的榜单记录新增 1,065 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

A small scalar reverse-mode autodifferentiation engine with a basic neural-network module for learning.

Candidate reason: No substantive maintenance evidence within three months; the latest commit only updates a README link.

### Uses and features

- Builds dynamic computation graphs and computes scalar gradients.
- Includes an MLP classification example and Graphviz graph demonstrations.

### Requirements and limits

The Python core uses scalar operations and is unsuitable for large tensor training. Notebooks and visualization need additional dependencies; gradient comparison tests use PyTorch.

### Getting started

Install micrograd, begin with Value operations and backward(), then read demo.ipynb.

See the [official README](https://github.com/karpathy/micrograd/blob/7bc720e951fe422b8f8814aa5aa1b64121d26b4c/README.md).

### Review and provenance

The compact implementation helps explain computation graphs and gradient propagation, but lacks the recent substantive maintenance required by this catalog.

Maintenance evidence: [The latest commit only adds an external microgpt tutorial link to the README, changes no autodiff implementation and falls outside the three-month window.](https://github.com/karpathy/micrograd/commit/7bc720e951fe422b8f8814aa5aa1b64121d26b4c) (2026-08-03).

Discovered in [GitHub monthly Trending](https://github.com/trending/jupyter-notebook?since=monthly), which recorded 1,065 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:00:03.487232+00:00",
  "eligibility": {
    "status": "needs_review",
    "reasons": [
      "no_recent_substantive_activity"
    ],
    "pending_actions": {
      "zh-CN": [
        "发现三个月窗口内的实质实现变更后重新核对。"
      ],
      "en": [
        "Recheck when a substantive implementation change appears within the three-month window."
      ]
    }
  },
  "metadata": {
    "schema_version": 1,
    "id": "micrograd",
    "name": "micrograd",
    "repository": "karpathy/micrograd",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkyNTUyMzEyOTM=",
    "category": "ai",
    "summary": {
      "zh-CN": "用于学习反向自动微分的微型标量引擎，并附带简单神经网络模块。",
      "en": "A small scalar reverse-mode autodifferentiation engine with a basic neural-network module for learning."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:00:03.487232+00:00",
        "en": "2026-11-17T04:00:03.487232+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "实现紧凑，便于逐步理解计算图与梯度传播；当前缺少目录要求的近期实质维护证据。",
      "en": "The compact implementation helps explain computation graphs and gradient propagation, but lacks the recent substantive maintenance required by this catalog.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/karpathy/micrograd/blob/7bc720e951fe422b8f8814aa5aa1b64121d26b4c/LICENSE",
      "license_sha256": "f372f582c99dc5b0e8dcf5ca5542183a735365468857ec6416af628490187cc1",
      "source_commit": "7bc720e951fe422b8f8814aa5aa1b64121d26b4c",
      "reviewed_at": "2026-11-17T04:00:03.487232+00:00",
      "evidence_pinned_at": "2026-11-17T04:00:03.487232+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "Root license applies to repository software code; models, data, assets and external services have separate terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-08-03T04:04:01Z",
        "reviewed_at": "2026-11-17T04:00:03.487232+00:00",
        "url": "https://github.com/karpathy/micrograd/commit/7bc720e951fe422b8f8814aa5aa1b64121d26b4c",
        "qualifies": false,
        "reason": {
          "zh-CN": "最近提交仅在 README 增加外部 microgpt 教程链接，未修改自动微分实现，且已超出三个月窗口。",
          "en": "The latest commit only adds an external microgpt tutorial link to the README, changes no autodiff implementation and falls outside the three-month window."
        },
        "reviewed_files": [
          "README.md"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/karpathy/micrograd",
        "accessed_at": "2026-11-17T04:00:03.487232+00:00"
      },
      {
        "url": "https://github.com/karpathy/micrograd/blob/7bc720e951fe422b8f8814aa5aa1b64121d26b4c/README.md",
        "accessed_at": "2026-11-17T04:00:03.487232+00:00"
      },
      {
        "url": "https://github.com/karpathy/micrograd/blob/7bc720e951fe422b8f8814aa5aa1b64121d26b4c/LICENSE",
        "accessed_at": "2026-11-17T04:00:03.487232+00:00"
      },
      {
        "url": "https://github.com/karpathy/micrograd/commit/7bc720e951fe422b8f8814aa5aa1b64121d26b4c",
        "accessed_at": "2026-11-17T04:00:03.487232+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 1065,
      "source_url": "https://github.com/trending/jupyter-notebook?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkyNTUyMzEyOTM=",
    "full_name": "karpathy/micrograd",
    "stargazers_count": 18968,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "f372f582c99dc5b0e8dcf5ca5542183a735365468857ec6416af628490187cc1",
    "last_success_at": "2026-11-17T03:54:54.265448+00:00"
  }
}
```

</details>
