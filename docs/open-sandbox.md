# OpenSandbox

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[opensandbox-group/OpenSandbox](https://github.com/opensandbox-group/OpenSandbox)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 部署与运维 / Deployment and operations |
| 状态 / Status | 已收录 / Included |
| Star | 17391 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-17T04:00:03.485220+00:00 |

## 中文

在自有 Docker 或 Kubernetes 基础设施上管理 AI 智能体的隔离执行环境。

### 用途与功能

- 提供沙箱生命周期、命令执行、文件操作及浏览器集成示例。
- 提供多语言 SDK、CLI、MCP 和网络访问策略。

### 环境与限制

本地快速开始需要 Docker 和 Python 3.10+；集群部署另需 Kubernetes 运维配置。隔离强度取决于后端与配置；生产镜像需单独核对摘要和发布签名覆盖。

### 开始使用

用 uvx opensandbox-server 初始化 Docker 配置并启动服务，再用 opensandbox SDK 创建沙箱、执行命令并销毁。

参阅[官方 README](https://github.com/opensandbox-group/OpenSandbox/blob/75b2570b4bbfbd619a77ff5e1cffe9219912bea5/README.md)。

### 收录与来源

统一生命周期与执行接口，适合在本地开发和集群智能体任务间复用集成代码。

维护证据：[为 Kubernetes informer 的资源缺失 404 增加单次告警和静默重试，并在恢复后重置告警状态。](https://github.com/opensandbox-group/OpenSandbox/commit/b32ad0b4007d9022f0fd730df3f9f728677a85bc)（2026-11-16）。

发现于 [GitHub 月榜](https://github.com/trending/go?since=monthly)。2026-11-17 的榜单记录新增 1,483 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Manages isolated execution environments for AI agents on self-hosted Docker or Kubernetes infrastructure.

### Uses and features

- Provides sandbox lifecycle, command execution, file operations and browser integration examples.
- Provides multilingual SDKs, CLI, MCP and network-access policies.

### Requirements and limits

The local quick start needs Docker and Python 3.10+; cluster deployment needs Kubernetes configuration. Isolation depends on backend and policy; production image digests and signing coverage require separate verification.

### Getting started

Initialize Docker configuration with uvx opensandbox-server, start the service, then use the opensandbox SDK to create, execute in and destroy a sandbox.

See the [official README](https://github.com/opensandbox-group/OpenSandbox/blob/75b2570b4bbfbd619a77ff5e1cffe9219912bea5/README.md).

### Review and provenance

A common lifecycle and execution API supports reusing integrations between local development and cluster agent workloads.

Maintenance evidence: [Adds one warning per missing-resource 404 outage and quiet retries to Kubernetes informers, resetting warning state after recovery.](https://github.com/opensandbox-group/OpenSandbox/commit/b32ad0b4007d9022f0fd730df3f9f728677a85bc) (2026-11-16).

Discovered in [GitHub monthly Trending](https://github.com/trending/go?since=monthly), which recorded 1,483 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:00:03.485220+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "open-sandbox",
    "name": "OpenSandbox",
    "repository": "opensandbox-group/OpenSandbox",
    "repo_node_id": "R_kgDOQqSjUg",
    "category": "operations",
    "summary": {
      "zh-CN": "在自有 Docker 或 Kubernetes 基础设施上管理 AI 智能体的隔离执行环境。",
      "en": "Manages isolated execution environments for AI agents on self-hosted Docker or Kubernetes infrastructure."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:00:03.485220+00:00",
        "en": "2026-11-17T04:00:03.485220+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "统一生命周期与执行接口，适合在本地开发和集群智能体任务间复用集成代码。",
      "en": "A common lifecycle and execution API supports reusing integrations between local development and cluster agent workloads.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "source_url": "https://github.com/opensandbox-group/OpenSandbox/blob/75b2570b4bbfbd619a77ff5e1cffe9219912bea5/LICENSE",
      "license_sha256": "50e6751797c50dedd75ef1b8a0d9e42f5f8472e9fbce91f34718e9f97b0c780a",
      "source_commit": "75b2570b4bbfbd619a77ff5e1cffe9219912bea5",
      "reviewed_at": "2026-11-17T04:00:03.485220+00:00",
      "evidence_pinned_at": "2026-11-17T04:00:03.485220+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "Root license applies to repository software code; models, data, assets and external services have separate terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-16T06:16:00Z",
        "reviewed_at": "2026-11-17T04:00:03.485220+00:00",
        "url": "https://github.com/opensandbox-group/OpenSandbox/commit/b32ad0b4007d9022f0fd730df3f9f728677a85bc",
        "qualifies": true,
        "reason": {
          "zh-CN": "为 Kubernetes informer 的资源缺失 404 增加单次告警和静默重试，并在恢复后重置告警状态。",
          "en": "Adds one warning per missing-resource 404 outage and quiet retries to Kubernetes informers, resetting warning state after recovery."
        },
        "reviewed_files": [
          "server/opensandbox_server/services/k8s/informer.py",
          "server/opensandbox_server/services/k8s/client.py"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/opensandbox-group/OpenSandbox",
        "accessed_at": "2026-11-17T04:00:03.485220+00:00"
      },
      {
        "url": "https://github.com/opensandbox-group/OpenSandbox/blob/75b2570b4bbfbd619a77ff5e1cffe9219912bea5/README.md",
        "accessed_at": "2026-11-17T04:00:03.485220+00:00"
      },
      {
        "url": "https://github.com/opensandbox-group/OpenSandbox/blob/75b2570b4bbfbd619a77ff5e1cffe9219912bea5/LICENSE",
        "accessed_at": "2026-11-17T04:00:03.485220+00:00"
      },
      {
        "url": "https://github.com/opensandbox-group/OpenSandbox/commit/b32ad0b4007d9022f0fd730df3f9f728677a85bc",
        "accessed_at": "2026-11-17T04:00:03.485220+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 1483,
      "source_url": "https://github.com/trending/go?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOQqSjUg",
    "full_name": "opensandbox-group/OpenSandbox",
    "stargazers_count": 17391,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "50e6751797c50dedd75ef1b8a0d9e42f5f8472e9fbce91f34718e9f97b0c780a",
    "last_success_at": "2026-11-17T03:53:57.631305+00:00"
  }
}
```

</details>
