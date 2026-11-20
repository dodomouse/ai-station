# Supermemory

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[supermemoryai/supermemory](https://github.com/supermemoryai/supermemory)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 31641 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:53.148914Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:38.449Z |

## 中文

提供记忆与上下文接口、助手插件和 MCP 接入，用于提取事实和检索历史。

让编码助手与应用在不同会话中检索项目背景、偏好和已完成的讨论。

### 主要功能

- 从对话中提取事实并构建用户资料。
- 通过插件、MCP 或 API 提供记忆检索。
- 支持本地服务及本地嵌入模型。

### 环境要求

- 本地部署可使用官方 Docker Compose 方案。
- 配置语言模型供应商，或按文档连接 Ollama。

### 使用限制

- 本地 API 也要求认证。升级时需保留数据卷和密钥。
- 本地版本与企业版本的能力范围需分别核对。

### 开始使用

1. 按[自托管快速入门](https://supermemory.ai/docs/self-hosting/quickstart)启动服务。
2. 按[配置指南](https://supermemory.ai/docs/self-hosting/configuration)连接模型。
3. 写入测试记忆并通过客户端检索。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:38.449Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-16 · commit](https://github.com/supermemoryai/supermemory/commit/fb105722a4a86b0e4010c09851c83fb93655b121)。docs: link the Convex component (#1896)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/supermemoryai/supermemory/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/supermemoryai/supermemory)
- [自托管快速入门 / self-hosting quickstart](https://supermemory.ai/docs/self-hosting/quickstart)
- [配置指南 / configuration guide](https://supermemory.ai/docs/self-hosting/configuration)

## English

Provides memory and context APIs, assistant plugins and MCP access for extracting facts and retrieving history.

Lets coding assistants and applications retrieve project context, preferences and prior discussions across sessions.

### Features

- Extract conversation facts and build user profiles.
- Expose memory retrieval through plugins, MCP or APIs.
- Support a local service and local embedding models.

### Requirements

- Local deployment can use the official Docker Compose setup.
- Configure a language-model provider or connect Ollama as documented.

### Limitations

- The local API also requires authentication. Preserve the data volume and keys during upgrades.
- Check the feature scope of local and enterprise editions separately.

### Getting started

1. Start the service using the [self-hosting quickstart](https://supermemory.ai/docs/self-hosting/quickstart).
2. Connect a model using the [configuration guide](https://supermemory.ai/docs/self-hosting/configuration).
3. Write a test memory and retrieve it through a client.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:38.449Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-16 · commit](https://github.com/supermemoryai/supermemory/commit/fb105722a4a86b0e4010c09851c83fb93655b121).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/supermemoryai/supermemory/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/supermemoryai/supermemory)
- [自托管快速入门 / self-hosting quickstart](https://supermemory.ai/docs/self-hosting/quickstart)
- [配置指南 / configuration guide](https://supermemory.ai/docs/self-hosting/configuration)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:53.148914Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "supermemory",
    "name": "Supermemory",
    "repository": "supermemoryai/supermemory",
    "repo_node_id": "R_kgDOLY4afw",
    "category": "ai",
    "summary": {
      "zh-CN": "提供记忆与上下文接口、助手插件和 MCP 接入，用于提取事实和检索历史。",
      "en": "Provides memory and context APIs, assistant plugins and MCP access for extracting facts and retrieving history."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:53.148914Z",
        "en": "2026-11-17T14:24:53.148914Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "让编码助手与应用在不同会话中检索项目背景、偏好和已完成的讨论。",
        "en": "Lets coding assistants and applications retrieve project context, preferences and prior discussions across sessions."
      },
      "source_url": "https://github.com/supermemoryai/supermemory/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/supermemoryai/supermemory/commit/fb105722a4a86b0e4010c09851c83fb93655b121",
        "occurred_at": "2026-11-16T01:35:34Z",
        "reviewed_at": "2026-11-17T14:24:53.148914Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "docs: link the Convex component (#1896) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/supermemoryai/supermemory/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / GitHub metadata",
        "url": "https://api.github.com/repos/supermemoryai/supermemory"
      },
      {
        "title": "自托管快速入门 / self-hosting quickstart",
        "url": "https://supermemory.ai/docs/self-hosting/quickstart"
      },
      {
        "title": "配置指南 / configuration guide",
        "url": "https://supermemory.ai/docs/self-hosting/configuration"
      }
    ]
  },
  "snapshot": {
    "full_name": "supermemoryai/supermemory",
    "repo_node_id": "R_kgDOLY4afw",
    "stargazers_count": 31641,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:38.449Z",
    "source_url": "https://api.github.com/repos/supermemoryai/supermemory"
  }
}
```

</details>
