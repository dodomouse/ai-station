# 百智办公 MonkeyAI（MonkeyCode）

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[chaitin/MonkeyCode](https://github.com/chaitin/MonkeyCode)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 5244 |
| 许可证 / License | AGPL-3.0-only |
| 评估时间 / Evaluated at | 2026-11-17T07:03:12.282893+00:00 |

## 中文

面向团队 AI 办公的服务端与管理后台，统一配置模型、知识库、技能和 MCP 连接器，供兼容客户端执行办公、编程与设计任务。

### 用途与功能

- 共享模型、知识库、技能、专家和规则，按团队与成员管理资源访问权限。
- 提供模型代理与 MCP 工具接口，并记录资源使用、审计和本地计费信息。
- 支持自有服务器部署和可选远程执行中转；设备端须启用远程访问并批准权限。

### 环境与限制

需配置模型及工具服务。官方免费版当前最多 10 个席位；服务端源码采用 Docker Compose、PostgreSQL/pgvector 和 RustFS。公开源码的默认启动入口缺少成员写入实现，初始化管理员及正常密码登录需另行补齐，不能视为开箱即用。调用外部模型或工具时，相关内容会发送到所配置的服务。

### 开始使用

先从官方 README 进入在线体验或选择客户端，了解工作台的资源配置与任务流程。源码部署参阅 monkeyai/README.md，并先补齐上述成员接口；本条未验证完整部署流程。

参阅[官方 README](https://github.com/chaitin/MonkeyCode/blob/a7589284e39e71c76fc11e1cea4167ba456430b9/README.md)。

### 收录与来源

按用户要求收录，供查找团队 AI 办公工具和研究源码使用。已核对主仓 AGPL 许可及近期 MCP 兼容修复；本条确认的开源范围为 monkeyai 服务端与管理后台代码。agent 与官方插件子模块未完成许可核验，字体和其他素材另有条款。已知部署限制保留在环境说明中，未运行上游。

维护证据：[修复独立认证 MCP 工具的启停配置兼容，保留既有工具 ID，并兼容省略工具名称的旧配置请求。](https://github.com/chaitin/MonkeyCode/commit/3f7820a0ad0983449792d9953eda9ee2e332a872)（2026-11-16）。

用户于 2026-11-17 提供仓库链接。本条按工程通用标准复核，不设 Star 门槛。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Server and administration console for team AI work, managing models, knowledge bases, skills and MCP connectors for compatible clients handling office, coding and design tasks.

### Uses and features

- Share models, knowledge bases, skills, experts and rules, with resource access managed for teams and members.
- Provide model proxy and MCP tool interfaces, with usage records, auditing and local billing.
- Support self-hosted deployment and an optional remote-execution relay; devices must enable remote access and approve permissions.

### Requirements and limits

Requires configured model and tool services. The current official free edition supports up to ten seats; the server source uses Docker Compose, PostgreSQL/pgvector and RustFS. The default public-source entry point lacks a member-writer implementation, so initial administrator creation and normal password login require additional integration. External model or tool calls send relevant content to the configured services.

### Getting started

Start with the online demo or clients linked in the official README to explore resource configuration and task workflows. For source deployment, consult monkeyai/README.md and supply the member implementation noted above. The complete deployment process was not tested.

See the [official README](https://github.com/chaitin/MonkeyCode/blob/a7589284e39e71c76fc11e1cea4167ba456430b9/README.md).

### Review and provenance

Included at the user’s request as a reference for team AI office tools and source study. The root AGPL license and recent MCP compatibility fixes were reviewed. The verified open-source scope covers the monkeyai server and admin-console code; the agent and official plugin submodules have not completed license verification, and fonts and other assets have separate terms. Known deployment limits are retained above; upstream software was not run.

Maintenance evidence: [Restores compatibility for independently authenticated MCP tool toggles, preserves existing tool IDs and supports older configuration requests omitting the tool name.](https://github.com/chaitin/MonkeyCode/commit/3f7820a0ad0983449792d9953eda9ee2e332a872) (2026-11-16).

Submitted by the user on 2026-11-17 and reviewed against the general catalog criteria, with no star threshold.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T07:03:12.282893+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "monkeycode",
    "name": "百智办公 MonkeyAI（MonkeyCode）",
    "repository": "chaitin/MonkeyCode",
    "repo_node_id": "R_kgDOPBePpg",
    "category": "productivity",
    "summary": {
      "zh-CN": "面向团队 AI 办公的服务端与管理后台，统一配置模型、知识库、技能和 MCP 连接器，供兼容客户端执行办公、编程与设计任务。",
      "en": "Server and administration console for team AI work, managing models, knowledge bases, skills and MCP connectors for compatible clients handling office, coding and design tasks."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T07:03:12.282893+00:00",
        "en": "2026-11-17T07:03:12.282893+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "按用户要求收录，供查找团队 AI 办公工具和研究源码使用。已核对主仓 AGPL 许可及近期 MCP 兼容修复；本条确认的开源范围为 monkeyai 服务端与管理后台代码。agent 与官方插件子模块未完成许可核验，字体和其他素材另有条款。已知部署限制保留在环境说明中，未运行上游。",
      "en": "Included at the user’s request as a reference for team AI office tools and source study. The root AGPL license and recent MCP compatibility fixes were reviewed. The verified open-source scope covers the monkeyai server and admin-console code; the agent and official plugin submodules have not completed license verification, and fonts and other assets have separate terms. Known deployment limits are retained above; upstream software was not run.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "AGPL-3.0-only",
      "osi_approved": true,
      "source_url": "https://github.com/chaitin/MonkeyCode/blob/a7589284e39e71c76fc11e1cea4167ba456430b9/LICENSE",
      "license_sha256": "0d96a4ff68ad6d4b6f1f30f713b18d5184912ba8dd389f86aa7710db079abcb0",
      "source_commit": "a7589284e39e71c76fc11e1cea4167ba456430b9",
      "reviewed_at": "2026-11-17T07:03:12.282893+00:00",
      "evidence_pinned_at": "2026-11-17T07:03:12.282893+00:00",
      "evidence_status": "hash_matched",
      "scope_note": {
        "zh-CN": "根 AGPL v3 原文覆盖本条收录的 monkeyai 服务端与管理后台代码。agent、plugins 子模块以及官网字体、素材、模型权重和外部服务不因此获得同一许可；仅确认主仓代码范围。",
        "en": "The root AGPL v3 text covers the monkeyai server and admin-console code included here. It does not establish the same license for the agent or plugins submodules, website fonts/assets, model weights or external services; this review confirms only the main-repository code scope."
      }
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "为团队 AI 办公提供模型代理、知识库、技能和 MCP 工具接口，支持兼容客户端执行办公、编程与设计任务。",
        "en": "Provides model proxies, knowledge bases, skills and MCP tool interfaces for team AI work, supporting compatible clients performing office, coding and design tasks."
      },
      "source_url": "https://github.com/chaitin/MonkeyCode/blob/a7589284e39e71c76fc11e1cea4167ba456430b9/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-16T12:35:41Z",
        "reviewed_at": "2026-11-17T07:03:12.282893+00:00",
        "url": "https://github.com/chaitin/MonkeyCode/commit/3f7820a0ad0983449792d9953eda9ee2e332a872",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复独立认证 MCP 工具的启停配置兼容，保留既有工具 ID，并兼容省略工具名称的旧配置请求。",
          "en": "Restores compatibility for independently authenticated MCP tool toggles, preserves existing tool IDs and supports older configuration requests omitting the tool name."
        },
        "reviewed_files": [
          "monkeyai/backend/internal/mcp/service.go",
          "monkeyai/backend/internal/mcp/tools.go",
          "monkeyai/backend/internal/mcp/query.sql"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/chaitin/MonkeyCode",
        "accessed_at": "2026-11-17T07:03:12.282893+00:00"
      },
      {
        "url": "https://github.com/chaitin/MonkeyCode/blob/a7589284e39e71c76fc11e1cea4167ba456430b9/README.md",
        "accessed_at": "2026-11-17T07:03:12.282893+00:00"
      },
      {
        "url": "https://github.com/chaitin/MonkeyCode/blob/a7589284e39e71c76fc11e1cea4167ba456430b9/LICENSE",
        "accessed_at": "2026-11-17T07:03:12.282893+00:00"
      },
      {
        "url": "https://github.com/chaitin/MonkeyCode/commit/3f7820a0ad0983449792d9953eda9ee2e332a872",
        "accessed_at": "2026-11-17T07:03:12.282893+00:00"
      },
      {
        "url": "https://github.com/chaitin/MonkeyCode/blob/a7589284e39e71c76fc11e1cea4167ba456430b9/monkeyai/README.md",
        "accessed_at": "2026-11-17T07:03:12.282893+00:00"
      },
      {
        "url": "https://github.com/chaitin/MonkeyCode/blob/a7589284e39e71c76fc11e1cea4167ba456430b9/monkeyai/docker-compose.yml",
        "accessed_at": "2026-11-17T07:03:12.282893+00:00"
      },
      {
        "url": "https://github.com/chaitin/MonkeyCode/blob/a7589284e39e71c76fc11e1cea4167ba456430b9/monkeyai/backend/Dockerfile",
        "accessed_at": "2026-11-17T07:03:12.282893+00:00"
      },
      {
        "url": "https://github.com/chaitin/MonkeyCode/blob/a7589284e39e71c76fc11e1cea4167ba456430b9/monkeyai/admin/Dockerfile",
        "accessed_at": "2026-11-17T07:03:12.282893+00:00"
      },
      {
        "url": "https://github.com/chaitin/MonkeyCode/blob/a7589284e39e71c76fc11e1cea4167ba456430b9/monkeyai/backend/go.mod",
        "accessed_at": "2026-11-17T07:03:12.282893+00:00"
      },
      {
        "url": "https://github.com/chaitin/MonkeyCode/blob/a7589284e39e71c76fc11e1cea4167ba456430b9/.gitmodules",
        "accessed_at": "2026-11-17T07:03:12.282893+00:00"
      },
      {
        "url": "https://github.com/chaitin/MonkeyCode/blob/a7589284e39e71c76fc11e1cea4167ba456430b9/monkeyai/backend/internal/app/app.go",
        "accessed_at": "2026-11-17T07:03:12.282893+00:00"
      },
      {
        "url": "https://github.com/chaitin/MonkeyCode/blob/a7589284e39e71c76fc11e1cea4167ba456430b9/monkeyai/backend/member/empty.go",
        "accessed_at": "2026-11-17T07:03:12.282893+00:00"
      },
      {
        "url": "https://github.com/chaitin/MonkeyCode/blob/a7589284e39e71c76fc11e1cea4167ba456430b9/monkeyai/backend/internal/identity/password.go",
        "accessed_at": "2026-11-17T07:03:12.282893+00:00"
      }
    ],
    "discovery": {
      "kind": "user_submission",
      "submitted_date": "2026-11-17",
      "source_url": "https://github.com/chaitin/MonkeyCode",
      "repository_url": "https://github.com/chaitin/MonkeyCode"
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOPBePpg",
    "full_name": "chaitin/MonkeyCode",
    "stargazers_count": 5244,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "AGPL-3.0-only",
    "api_license_spdx": "AGPL-3.0",
    "license_sha256": "0d96a4ff68ad6d4b6f1f30f713b18d5184912ba8dd389f86aa7710db079abcb0",
    "last_success_at": "2026-11-17T06:55:40.135267+00:00"
  }
}
```

</details>
