# DeepTutor

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[HKUDS/DeepTutor](https://github.com/HKUDS/DeepTutor)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 59827 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-17T04:07:37.948814+00:00 |

## 中文

将学习资料、辅导对话、练习和学习记录组织到同一 AI 学习工作区。

### 用途与功能

- 支持基于知识库检索和来源引用的辅导对话。
- 提供多种学习模式，包括阅读、测验、学习路径和笔记。
- 通过 CLI、技能和 MCP 扩展工作区。

### 环境与限制

需要配置模型服务；检索、解析和生成能力依赖所选模块。PyPI 完整版要求 Python 3.11–3.14 和 Node.js 20.9+，也可使用 Docker 或桌面预览版。生成内容需结合原始资料核对。

### 开始使用

按 README 选择部署方式，在设置中配置模型，然后导入一份学习资料并开始带来源引用的对话。

参阅[官方 README](https://github.com/HKUDS/DeepTutor/blob/4c1e000d8563c5ac3b231baaaf149dc4dc4d2406/README.md)。

### 收录与来源

适合希望将资料、提问和复习记录保存在同一工作区的学习者。

维护证据：[修复工作区会话迁移的冲突查询，对旧数据库含双引号的唯一列名正确转义。](https://github.com/HKUDS/DeepTutor/commit/4c1e000d8563c5ac3b231baaaf149dc4dc4d2406)（2026-11-15）。

发现于 [GitHub 月榜](https://github.com/trending?since=monthly)。2026-11-17 的榜单记录新增 18,533 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Combines learning materials, tutoring conversations, practice and study records in an AI learning workspace.

### Uses and features

- Grounds tutoring conversations in knowledge-base retrieval and source citations.
- Provides reading, quizzes, learning paths and notebooks.
- Extends the workspace through a CLI, skills and MCP.

### Requirements and limits

Requires a model provider; retrieval, parsing and generation depend on installed modules. The full PyPI app requires Python 3.11–3.14 and Node.js 20.9+, with Docker and desktop-preview alternatives. Check generated content against source materials.

### Getting started

Choose a deployment path in the README, configure a model in Settings, then import learning material and start a source-grounded conversation.

See the [official README](https://github.com/HKUDS/DeepTutor/blob/4c1e000d8563c5ac3b231baaaf149dc4dc4d2406/README.md).

### Review and provenance

Useful for learners keeping materials, questions and review records in one workspace.

Maintenance evidence: [Fixes workspace session-transfer conflict queries by escaping quoted unique-column names in legacy databases.](https://github.com/HKUDS/DeepTutor/commit/4c1e000d8563c5ac3b231baaaf149dc4dc4d2406) (2026-11-15).

Discovered in [GitHub monthly Trending](https://github.com/trending?since=monthly), which recorded 18,533 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:07:37.948814+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "deeptutor",
    "name": "DeepTutor",
    "repository": "HKUDS/DeepTutor",
    "repo_node_id": "R_kgDOQwI8Aw",
    "category": "ai",
    "summary": {
      "zh-CN": "将学习资料、辅导对话、练习和学习记录组织到同一 AI 学习工作区。",
      "en": "Combines learning materials, tutoring conversations, practice and study records in an AI learning workspace."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:07:37.948814+00:00",
        "en": "2026-11-17T04:07:37.948814+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合希望将资料、提问和复习记录保存在同一工作区的学习者。",
      "en": "Useful for learners keeping materials, questions and review records in one workspace.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "source_url": "https://github.com/HKUDS/DeepTutor/blob/4c1e000d8563c5ac3b231baaaf149dc4dc4d2406/LICENSE",
      "license_sha256": "cd2f54e1e5066644023203dcbd956776a9f4ef6eb8b6225afe1ffa2d380fede4",
      "source_commit": "4c1e000d8563c5ac3b231baaaf149dc4dc4d2406",
      "reviewed_at": "2026-11-17T04:07:37.948814+00:00",
      "evidence_pinned_at": "2026-11-17T04:07:37.948814+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "Applies to repository code and documentation; external models, services, data and assets retain their own terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-15T18:17:36Z",
        "reviewed_at": "2026-11-17T04:07:37.948814+00:00",
        "url": "https://github.com/HKUDS/DeepTutor/commit/4c1e000d8563c5ac3b231baaaf149dc4dc4d2406",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复工作区会话迁移的冲突查询，对旧数据库含双引号的唯一列名正确转义。",
          "en": "Fixes workspace session-transfer conflict queries by escaping quoted unique-column names in legacy databases."
        },
        "reviewed_files": [
          "deeptutor/services/workspace/session_transfer.py"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/HKUDS/DeepTutor",
        "accessed_at": "2026-11-17T04:07:37.948814+00:00"
      },
      {
        "url": "https://github.com/HKUDS/DeepTutor/blob/4c1e000d8563c5ac3b231baaaf149dc4dc4d2406/README.md",
        "accessed_at": "2026-11-17T04:07:37.948814+00:00"
      },
      {
        "url": "https://github.com/HKUDS/DeepTutor/blob/4c1e000d8563c5ac3b231baaaf149dc4dc4d2406/LICENSE",
        "accessed_at": "2026-11-17T04:07:37.948814+00:00"
      },
      {
        "url": "https://github.com/HKUDS/DeepTutor/commit/4c1e000d8563c5ac3b231baaaf149dc4dc4d2406",
        "accessed_at": "2026-11-17T04:07:37.948814+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 18533,
      "source_url": "https://github.com/trending?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOQwI8Aw",
    "full_name": "HKUDS/DeepTutor",
    "stargazers_count": 59827,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "cd2f54e1e5066644023203dcbd956776a9f4ef6eb8b6225afe1ffa2d380fede4",
    "last_success_at": "2026-11-17T03:53:04.798696+00:00"
  }
}
```

</details>
