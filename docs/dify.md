# Dify

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[langgenius/dify](https://github.com/langgenius/dify)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 161353 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:53.148204Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:38.781Z |

## 中文

通过可视化工作区构建 AI 流程、RAG 管线和 Agent 应用。

为 AI 连接模型、知识库与工具，并管理应用的部署和运行记录。

### 主要功能

- 在可视化工作区编排模型和工具。
- 构建检索增强生成管线和知识库。
- 让智能体在沙箱中处理文件和运行命令。

### 环境要求

- 官方最低要求为 2 核 CPU 和 4 GiB 内存。
- Docker 部署需 Docker、Compose v2.35.0 或更新版本，以及 OpenSSL。
- 需要配置模型供应商及沙箱认证。

### 使用限制

- 升级时需保留现有 .env 并核对配置。
- 智能体的命令与文件操作受沙箱和工具权限影响。

### 开始使用

1. 按[Docker 部署指南](https://github.com/langgenius/dify/blob/main/docker/README.md)准备服务。
2. 完成初始化并配置模型供应商。
3. 按[README](https://github.com/langgenius/dify/blob/main/README.md)创建并测试一个工作流。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:38.781Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/langgenius/dify/commit/39addda308deb3f24885bc1e5ebaa6f160f2f492)。test: fix specs that fail the merge queue (#46617)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [README / README](https://github.com/langgenius/dify/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/langgenius/dify)
- [Docker 部署指南 / Docker deployment guide](https://github.com/langgenius/dify/blob/main/docker/README.md)

## English

Builds AI workflows, retrieval pipelines and agents in a visual workspace.

Connects AI to models, knowledge bases and tools while managing application deployment and run records.

### Features

- Orchestrate models and tools in a visual workspace.
- Build retrieval-augmented generation pipelines and knowledge bases.
- Let agents process files and run commands in a sandbox.

### Requirements

- The documented minimum is a 2-core CPU and 4 GiB of memory.
- Docker deployment requires Docker, Compose v2.35.0 or later, and OpenSSL.
- Model-provider access and sandbox authentication must be configured.

### Limitations

- Preserve the existing .env and review configuration during upgrades.
- Agent command and file operations depend on sandbox and tool permissions.

### Getting started

1. Prepare services using the [Docker deployment guide](https://github.com/langgenius/dify/blob/main/docker/README.md).
2. Complete initialization and configure a model provider.
3. Create and test a workflow using the [README](https://github.com/langgenius/dify/blob/main/README.md).

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:38.781Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/langgenius/dify/commit/39addda308deb3f24885bc1e5ebaa6f160f2f492).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [README / README](https://github.com/langgenius/dify/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/langgenius/dify)
- [Docker 部署指南 / Docker deployment guide](https://github.com/langgenius/dify/blob/main/docker/README.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:53.148204Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "dify",
    "name": "Dify",
    "repository": "langgenius/dify",
    "repo_node_id": "R_kgDOJVxJug",
    "category": "ai",
    "summary": {
      "zh-CN": "通过可视化工作区构建 AI 流程、RAG 管线和 Agent 应用。",
      "en": "Builds AI workflows, retrieval pipelines and agents in a visual workspace."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:53.148204Z",
        "en": "2026-11-17T14:24:53.148204Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "为 AI 连接模型、知识库与工具，并管理应用的部署和运行记录。",
        "en": "Connects AI to models, knowledge bases and tools while managing application deployment and run records."
      },
      "source_url": "https://github.com/langgenius/dify/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/langgenius/dify/commit/39addda308deb3f24885bc1e5ebaa6f160f2f492",
        "occurred_at": "2026-11-17T13:09:39Z",
        "reviewed_at": "2026-11-17T14:24:53.148204Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "test: fix specs that fail the merge queue (#46617) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "README / README",
        "url": "https://github.com/langgenius/dify/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / GitHub metadata",
        "url": "https://api.github.com/repos/langgenius/dify"
      },
      {
        "title": "Docker 部署指南 / Docker deployment guide",
        "url": "https://github.com/langgenius/dify/blob/main/docker/README.md"
      }
    ]
  },
  "snapshot": {
    "full_name": "langgenius/dify",
    "repo_node_id": "R_kgDOJVxJug",
    "stargazers_count": 161353,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:38.781Z",
    "source_url": "https://api.github.com/repos/langgenius/dify"
  }
}
```

</details>
