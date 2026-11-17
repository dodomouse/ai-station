# agent-browser

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[vercel-labs/agent-browser](https://github.com/vercel-labs/agent-browser)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 52076 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-17T04:07:37.953819+00:00 |

## 中文

为 AI 智能体提供网页快照、元素操作和浏览器会话管理命令。

### 用途与功能

- 将页面无障碍树转换为带元素引用的文本快照。
- 通过 CLI 执行导航、点击、输入、截图和下载。
- 支持独立会话、CDP 连接和 MCP 接口。

### 环境与限制

需要受支持平台上的浏览器；默认安装 Chrome for Testing，Linux 可能需要系统库。模型由调用方提供，页面变化后须刷新引用；云浏览器服务的账号和费用独立适用。

### 开始使用

按 README 安装 CLI 和浏览器，依次打开页面、获取 snapshot，再操作元素并检查结果。

参阅[官方 README](https://github.com/vercel-labs/agent-browser/blob/b06e2533ba9b3823b8a96c859d455cb55f4d7893/README.md)。

### 收录与来源

适合把浏览、操作和结果检查拆成智能体可调用的小步骤。

维护证据：[统一 CDP 会话匹配逻辑。正确处理直接页面连接中缺少 sessionId 的事件，并拒绝未连接浏览器消费这些事件。](https://github.com/vercel-labs/agent-browser/commit/53384771fbafc261ba67608ac806dd5aa70b84f0)（2026-11-15）。

发现于 [GitHub 月榜](https://github.com/trending?since=monthly)。2026-11-17 的榜单记录新增 7,943 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Provides web snapshots, element actions and browser-session commands for AI agents.

### Uses and features

- Converts page accessibility trees into text snapshots with element references.
- Exposes navigation, clicking, input, screenshots and downloads through a CLI.
- Supports isolated sessions, CDP connections and MCP.

### Requirements and limits

Requires a browser on a supported platform; Chrome for Testing is the default, and Linux may need system libraries. The caller supplies the model, references need refreshing after page changes, and cloud-browser accounts and fees apply separately.

### Getting started

Install the CLI and browser from the README, open a page, request a snapshot, act on an element and inspect the result.

See the [official README](https://github.com/vercel-labs/agent-browser/blob/b06e2533ba9b3823b8a96c859d455cb55f4d7893/README.md).

### Review and provenance

Useful for exposing browsing, interaction and verification as small agent-callable steps.

Maintenance evidence: [Unifies CDP session matching to accept events without sessionId for direct-page connections while rejecting them for unattached browsers.](https://github.com/vercel-labs/agent-browser/commit/53384771fbafc261ba67608ac806dd5aa70b84f0) (2026-11-15).

Discovered in [GitHub monthly Trending](https://github.com/trending?since=monthly), which recorded 7,943 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:07:37.953819+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "agent-browser",
    "name": "agent-browser",
    "repository": "vercel-labs/agent-browser",
    "repo_node_id": "R_kgDOQ3j5Tg",
    "category": "development",
    "summary": {
      "zh-CN": "为 AI 智能体提供网页快照、元素操作和浏览器会话管理命令。",
      "en": "Provides web snapshots, element actions and browser-session commands for AI agents."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:07:37.953819+00:00",
        "en": "2026-11-17T04:07:37.953819+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合把浏览、操作和结果检查拆成智能体可调用的小步骤。",
      "en": "Useful for exposing browsing, interaction and verification as small agent-callable steps.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "source_url": "https://github.com/vercel-labs/agent-browser/blob/b06e2533ba9b3823b8a96c859d455cb55f4d7893/LICENSE",
      "license_sha256": "014bb31e83d5c2e76aea1cc6e82217346ab41362f32cb355ad0f5c10aa0aeaff",
      "source_commit": "b06e2533ba9b3823b8a96c859d455cb55f4d7893",
      "reviewed_at": "2026-11-17T04:07:37.953819+00:00",
      "evidence_pinned_at": "2026-11-17T04:07:37.953819+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "Applies to repository code and documentation; external models, services, data and assets retain their own terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-15T08:16:52Z",
        "reviewed_at": "2026-11-17T04:07:37.953819+00:00",
        "url": "https://github.com/vercel-labs/agent-browser/commit/53384771fbafc261ba67608ac806dd5aa70b84f0",
        "qualifies": true,
        "reason": {
          "zh-CN": "统一 CDP 会话匹配逻辑。正确处理直接页面连接中缺少 sessionId 的事件，并拒绝未连接浏览器消费这些事件。",
          "en": "Unifies CDP session matching to accept events without sessionId for direct-page connections while rejecting them for unattached browsers."
        },
        "reviewed_files": [
          "cli/src/native/cdp/types.rs",
          "cli/src/native/actions.rs",
          "cli/src/native/tracing.rs"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/vercel-labs/agent-browser",
        "accessed_at": "2026-11-17T04:07:37.953819+00:00"
      },
      {
        "url": "https://github.com/vercel-labs/agent-browser/blob/b06e2533ba9b3823b8a96c859d455cb55f4d7893/README.md",
        "accessed_at": "2026-11-17T04:07:37.953819+00:00"
      },
      {
        "url": "https://github.com/vercel-labs/agent-browser/blob/b06e2533ba9b3823b8a96c859d455cb55f4d7893/LICENSE",
        "accessed_at": "2026-11-17T04:07:37.953819+00:00"
      },
      {
        "url": "https://github.com/vercel-labs/agent-browser/commit/53384771fbafc261ba67608ac806dd5aa70b84f0",
        "accessed_at": "2026-11-17T04:07:37.953819+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 7943,
      "source_url": "https://github.com/trending?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOQ3j5Tg",
    "full_name": "vercel-labs/agent-browser",
    "stargazers_count": 52076,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "014bb31e83d5c2e76aea1cc6e82217346ab41362f32cb355ad0f5c10aa0aeaff",
    "last_success_at": "2026-11-17T03:56:41.863891+00:00"
  }
}
```

</details>
