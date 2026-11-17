# Anthropic Sandbox Runtime

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[anthropics/sandbox-runtime](https://github.com/anthropics/sandbox-runtime)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 部署与运维 / Deployment and operations |
| 状态 / Status | 已收录 / Included |
| Star | 7155 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-17T04:00:03.484710+00:00 |

## 中文

为智能体、MCP 服务和命令提供操作系统级文件与网络访问限制的运行时。

### 用途与功能

- 用 CLI 包装命令，或通过库接口嵌入智能体运行器。
- 配置读写路径、域名规则和违规监测。

### 环境与限制

仍为研究预览；macOS 使用 sandbox-exec，Linux 使用 bubblewrap 等依赖，Windows 需单独设置后端。默认读取并非全面禁止；Windows 网络过滤存在已知绕过限制，不应据此声称能隔离恶意代码。

### 开始使用

安装 @anthropic-ai/sandbox-runtime，按平台文档准备依赖，配置 ~/.srt-settings.json 后用 srt 包装测试命令。

参阅[官方 README](https://github.com/anthropics/sandbox-runtime/blob/0bbebed0aa9a8e628dc4df8bc30293550a1988eb/README.md)。

### 收录与来源

可将权限配置和命令执行集成到智能体运行流程，且文档说明了不同平台的限制。

维护证据：[将调用方环境变量传入 Windows MXC 子进程，并按 Windows 规则合并代理和 Git 环境。](https://github.com/anthropics/sandbox-runtime/commit/41501a60b27deb89484b718acb76a04e2a37aa75)（2026-11-11）。

发现于 [GitHub 月榜](https://github.com/trending/typescript?since=monthly)。2026-11-17 的榜单记录新增 1,609 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

A runtime applying operating-system file and network restrictions to agents, MCP servers and commands.

### Uses and features

- Wrap commands with a CLI or embed the library in an agent runner.
- Configure read/write paths, domain rules and violation monitoring.

### Requirements and limits

A research preview using sandbox-exec on macOS, bubblewrap and other dependencies on Linux, and separately configured Windows backends. Reads are not universally denied by default; known Windows network-filter bypasses prevent treating it as isolation for malicious code.

### Getting started

Install @anthropic-ai/sandbox-runtime, prepare platform dependencies, configure ~/.srt-settings.json and wrap a test command with srt.

See the [official README](https://github.com/anthropics/sandbox-runtime/blob/0bbebed0aa9a8e628dc4df8bc30293550a1988eb/README.md).

### Review and provenance

Integrates permission configuration with agent command execution and documents platform-specific limitations.

Maintenance evidence: [Passes caller environment variables to Windows MXC children and merges proxy and Git environment layers using Windows rules.](https://github.com/anthropics/sandbox-runtime/commit/41501a60b27deb89484b718acb76a04e2a37aa75) (2026-11-11).

Discovered in [GitHub monthly Trending](https://github.com/trending/typescript?since=monthly), which recorded 1,609 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:00:03.484710+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "anthropic-sandbox-runtime",
    "name": "Anthropic Sandbox Runtime",
    "repository": "anthropics/sandbox-runtime",
    "repo_node_id": "R_kgDOQFjJqA",
    "category": "operations",
    "summary": {
      "zh-CN": "为智能体、MCP 服务和命令提供操作系统级文件与网络访问限制的运行时。",
      "en": "A runtime applying operating-system file and network restrictions to agents, MCP servers and commands."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:00:03.484710+00:00",
        "en": "2026-11-17T04:00:03.484710+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "可将权限配置和命令执行集成到智能体运行流程，且文档说明了不同平台的限制。",
      "en": "Integrates permission configuration with agent command execution and documents platform-specific limitations.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "source_url": "https://github.com/anthropics/sandbox-runtime/blob/0bbebed0aa9a8e628dc4df8bc30293550a1988eb/LICENSE",
      "license_sha256": "1210bc93eb85dd786c33192d5bcb7153a93922fa99fbc1512af6a7199cb41080",
      "source_commit": "0bbebed0aa9a8e628dc4df8bc30293550a1988eb",
      "reviewed_at": "2026-11-17T04:00:03.484710+00:00",
      "evidence_pinned_at": "2026-11-17T04:00:03.484710+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "Root license applies to repository software code; models, data, assets and external services have separate terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-11T19:41:37Z",
        "reviewed_at": "2026-11-17T04:00:03.484710+00:00",
        "url": "https://github.com/anthropics/sandbox-runtime/commit/41501a60b27deb89484b718acb76a04e2a37aa75",
        "qualifies": true,
        "reason": {
          "zh-CN": "将调用方环境变量传入 Windows MXC 子进程，并按 Windows 规则合并代理和 Git 环境。",
          "en": "Passes caller environment variables to Windows MXC children and merges proxy and Git environment layers using Windows rules."
        },
        "reviewed_files": [
          "src/sandbox/mxc-sandbox-utils.ts",
          "src/sandbox/sandbox-manager.ts"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/anthropics/sandbox-runtime",
        "accessed_at": "2026-11-17T04:00:03.484710+00:00"
      },
      {
        "url": "https://github.com/anthropics/sandbox-runtime/blob/0bbebed0aa9a8e628dc4df8bc30293550a1988eb/README.md",
        "accessed_at": "2026-11-17T04:00:03.484710+00:00"
      },
      {
        "url": "https://github.com/anthropics/sandbox-runtime/blob/0bbebed0aa9a8e628dc4df8bc30293550a1988eb/LICENSE",
        "accessed_at": "2026-11-17T04:00:03.484710+00:00"
      },
      {
        "url": "https://github.com/anthropics/sandbox-runtime/commit/41501a60b27deb89484b718acb76a04e2a37aa75",
        "accessed_at": "2026-11-17T04:00:03.484710+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 1609,
      "source_url": "https://github.com/trending/typescript?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOQFjJqA",
    "full_name": "anthropics/sandbox-runtime",
    "stargazers_count": 7155,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "1210bc93eb85dd786c33192d5bcb7153a93922fa99fbc1512af6a7199cb41080",
    "last_success_at": "2026-11-17T03:54:52.381287+00:00"
  }
}
```

</details>
