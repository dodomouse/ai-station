# agent-desktop

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[vercel-labs/agent-desktop](https://github.com/vercel-labs/agent-desktop)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 自动化 / Automation |
| 状态 / Status | 已收录 / Included |
| Star | 24668 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-17T04:07:37.945382+00:00 |

## 中文

通过操作系统无障碍接口，为 AI 智能体提供桌面快照和界面操作。

### 用途与功能

- 将窗口和控件树输出为带引用的 JSON 快照。
- 通过控件引用执行界面操作，包括点击和输入。提供截图和 MCP 接口。

### 环境与限制

需要支持的 macOS、Windows 或 Linux 环境及相应无障碍权限；模型由调用方提供。界面变化后应重新获取快照，截图和剪贴板可能包含敏感内容。

### 开始使用

按系统安装官方 CLI，完成权限配置，再获取窗口快照并验证一次控件操作。

参阅[官方 README](https://github.com/vercel-labs/agent-desktop/blob/8ffecc1d3d088727f8d84baf4dde0224aab2e8ad/README.md)。

### 收录与来源

适合需要读取控件结构、再执行桌面操作的智能体工具链。

维护证据：[修复 tmux 下权限引导定位错误应用的问题，优先查询 macOS 责任进程并保留父进程回退。](https://github.com/vercel-labs/agent-desktop/commit/8ffecc1d3d088727f8d84baf4dde0224aab2e8ad)（2026-11-15）。

发现于 [GitHub 月榜](https://github.com/trending/rust?since=monthly)。2026-11-17 的榜单记录新增 22,859 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Provides desktop snapshots and UI actions for AI agents through operating-system accessibility APIs.

### Uses and features

- Exports window and control trees as JSON snapshots with references.
- Acts on referenced controls and exposes screenshots and an MCP interface.

### Requirements and limits

Requires a supported macOS, Windows or Linux environment and accessibility permissions; the caller supplies the model. Refresh snapshots after UI changes, and account for private content in screenshots and clipboard data.

### Getting started

Install the official CLI for your platform, configure permissions, then obtain a window snapshot and verify a control action.

See the [official README](https://github.com/vercel-labs/agent-desktop/blob/8ffecc1d3d088727f8d84baf4dde0224aab2e8ad/README.md).

### Review and provenance

Useful for agent toolchains that inspect structured controls before acting on a desktop.

Maintenance evidence: [Fixes the wrong app being named in macOS permission guidance under tmux by checking the responsible process before the ancestor chain.](https://github.com/vercel-labs/agent-desktop/commit/8ffecc1d3d088727f8d84baf4dde0224aab2e8ad) (2026-11-15).

Discovered in [GitHub monthly Trending](https://github.com/trending/rust?since=monthly), which recorded 22,859 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:07:37.945382+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "agent-desktop",
    "name": "agent-desktop",
    "repository": "vercel-labs/agent-desktop",
    "repo_node_id": "R_kgDORUIU8w",
    "category": "automation",
    "summary": {
      "zh-CN": "通过操作系统无障碍接口，为 AI 智能体提供桌面快照和界面操作。",
      "en": "Provides desktop snapshots and UI actions for AI agents through operating-system accessibility APIs."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:07:37.945382+00:00",
        "en": "2026-11-17T04:07:37.945382+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合需要读取控件结构、再执行桌面操作的智能体工具链。",
      "en": "Useful for agent toolchains that inspect structured controls before acting on a desktop.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "source_url": "https://github.com/vercel-labs/agent-desktop/blob/8ffecc1d3d088727f8d84baf4dde0224aab2e8ad/LICENSE",
      "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
      "source_commit": "8ffecc1d3d088727f8d84baf4dde0224aab2e8ad",
      "reviewed_at": "2026-11-17T04:07:37.945382+00:00",
      "evidence_pinned_at": "2026-11-17T04:07:37.945382+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "Applies to repository code and documentation; external models, services, data and assets retain their own terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-15T00:11:14Z",
        "reviewed_at": "2026-11-17T04:07:37.945382+00:00",
        "url": "https://github.com/vercel-labs/agent-desktop/commit/8ffecc1d3d088727f8d84baf4dde0224aab2e8ad",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复 tmux 下权限引导定位错误应用的问题，优先查询 macOS 责任进程并保留父进程回退。",
          "en": "Fixes the wrong app being named in macOS permission guidance under tmux by checking the responsible process before the ancestor chain."
        },
        "reviewed_files": [
          "crates/macos/src/system/permissions/permission_guide.rs"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/vercel-labs/agent-desktop",
        "accessed_at": "2026-11-17T04:07:37.945382+00:00"
      },
      {
        "url": "https://github.com/vercel-labs/agent-desktop/blob/8ffecc1d3d088727f8d84baf4dde0224aab2e8ad/README.md",
        "accessed_at": "2026-11-17T04:07:37.945382+00:00"
      },
      {
        "url": "https://github.com/vercel-labs/agent-desktop/blob/8ffecc1d3d088727f8d84baf4dde0224aab2e8ad/LICENSE",
        "accessed_at": "2026-11-17T04:07:37.945382+00:00"
      },
      {
        "url": "https://github.com/vercel-labs/agent-desktop/commit/8ffecc1d3d088727f8d84baf4dde0224aab2e8ad",
        "accessed_at": "2026-11-17T04:07:37.945382+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 22859,
      "source_url": "https://github.com/trending/rust?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDORUIU8w",
    "full_name": "vercel-labs/agent-desktop",
    "stargazers_count": 24668,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
    "last_success_at": "2026-11-17T03:50:48.068975+00:00"
  }
}
```

</details>
