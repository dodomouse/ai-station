# ego-browser for ego lite

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[citrolabs/ego-lite](https://github.com/citrolabs/ego-lite)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 23215 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T04:07:37.957469+00:00 |

## 中文

为 AI 智能体连接 ego lite 浏览器的开源 Skill 与工具层，通过 JavaScript 操作页面并使用独立任务工作区。

### 用途与功能

- 向智能体提供页面快照、导航、点击、填写与截图工具。
- 用任务 Space 管理标签页，并支持人工接管。
- 可通过 Skill 接入支持技能的工具，包括 Codex 和 Claude Code。

### 环境与限制

需要单独安装 ego lite 浏览器和支持 Skill 的智能体。README 列出 macOS、Windows，Linux 尚在路线图。MIT 覆盖本仓库连接层和技能，不等于浏览器本体采用 MIT；访问已有登录状态需要用户授权。模型服务费用和数据处理取决于所接智能体。

### 开始使用

按 README 安装浏览器，或用 `npx skills add citrolabs/ego-lite` 安装连接技能，然后在智能体中调用 ego-browser。

参阅[官方 README](https://github.com/citrolabs/ego-lite/blob/f499162d1b911ba9b320ed31b741dba7ebc2e4d6/README.md)。

### 收录与来源

适合让已有编程智能体操作网页，并把任务标签页与日常浏览分开管理。

维护证据：[修改执行技能的任务结束协议。先观察完成结果，再在独立脚本中调用 finish，避免过早关闭工作区](https://github.com/citrolabs/ego-lite/commit/fad68b972ede76ee608e3fdb8d4b76e9d5465e40)（2026-11-10）。

发现于 [GitHub 月榜](https://github.com/trending/javascript?since=monthly)。2026-11-17 的榜单记录新增 5,737 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

An open-source skill and tool layer connecting AI agents to the ego lite browser, with JavaScript page actions and separate task workspaces.

### Uses and features

- Expose page snapshots, navigation, clicks, form filling and capture to agents.
- Manage tabs in task Spaces and allow human takeover.
- Integrate through a skill with tools such as Codex and Claude Code.

### Requirements and limits

Requires the separately downloaded ego lite browser and a skill-capable agent. The README lists macOS and Windows, with Linux on the roadmap. MIT covers this repository’s integration layer and skills, not an asserted MIT license for the browser itself. Access to existing sessions requires user authorization; model costs and data handling depend on the connected agent.

### Getting started

Install the browser following the README, or install the integration skill with `npx skills add citrolabs/ego-lite`, then invoke ego-browser in your agent.

See the [official README](https://github.com/citrolabs/ego-lite/blob/f499162d1b911ba9b320ed31b741dba7ebc2e4d6/README.md).

### Review and provenance

Useful for giving an existing coding agent web interaction while managing task tabs separately from everyday browsing.

Maintenance evidence: [Changes the executable skill completion protocol to observe the outcome before calling finish in a separate script, avoiding premature workspace closure](https://github.com/citrolabs/ego-lite/commit/fad68b972ede76ee608e3fdb8d4b76e9d5465e40) (2026-11-10).

Discovered in [GitHub monthly Trending](https://github.com/trending/javascript?since=monthly), which recorded 5,737 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:07:37.957469+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "ego-lite",
    "name": "ego-browser for ego lite",
    "repository": "citrolabs/ego-lite",
    "repo_node_id": "R_kgDOSEVU0g",
    "category": "development",
    "summary": {
      "zh-CN": "为 AI 智能体连接 ego lite 浏览器的开源 Skill 与工具层，通过 JavaScript 操作页面并使用独立任务工作区。",
      "en": "An open-source skill and tool layer connecting AI agents to the ego lite browser, with JavaScript page actions and separate task workspaces."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:07:37.957469+00:00",
        "en": "2026-11-17T04:07:37.957469+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合让已有编程智能体操作网页，并把任务标签页与日常浏览分开管理。",
      "en": "Useful for giving an existing coding agent web interaction while managing task tabs separately from everyday browsing.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/citrolabs/ego-lite/blob/f499162d1b911ba9b320ed31b741dba7ebc2e4d6/LICENSE",
      "license_sha256": "325b6f26ca9452fcfb81cc6f52e3889573a7c141e9d07ab35f678b7d95d48e52",
      "source_commit": "f499162d1b911ba9b320ed31b741dba7ebc2e4d6",
      "reviewed_at": "2026-11-17T04:07:37.957469+00:00",
      "evidence_pinned_at": "2026-11-17T04:07:37.957469+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "MIT covers repository contents, including the ego-browser integration and skill. The ego lite browser is a separate download; its license is not established by this repository MIT grant."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-10T14:11:05Z",
        "reviewed_at": "2026-11-17T04:07:37.957469+00:00",
        "url": "https://github.com/citrolabs/ego-lite/commit/fad68b972ede76ee608e3fdb8d4b76e9d5465e40",
        "qualifies": true,
        "reason": {
          "zh-CN": "修改执行技能的任务结束协议。先观察完成结果，再在独立脚本中调用 finish，避免过早关闭工作区",
          "en": "Changes the executable skill completion protocol to observe the outcome before calling finish in a separate script, avoiding premature workspace closure"
        },
        "reviewed_files": [
          "package/ego-browser/skill-body/SKILL.md",
          "plugins/ego/tests/claude-plugin-mode-isolation.test.mjs"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/citrolabs/ego-lite",
        "accessed_at": "2026-11-17T04:07:37.957469+00:00"
      },
      {
        "url": "https://github.com/citrolabs/ego-lite/blob/f499162d1b911ba9b320ed31b741dba7ebc2e4d6/README.md",
        "accessed_at": "2026-11-17T04:07:37.957469+00:00"
      },
      {
        "url": "https://github.com/citrolabs/ego-lite/blob/f499162d1b911ba9b320ed31b741dba7ebc2e4d6/LICENSE",
        "accessed_at": "2026-11-17T04:07:37.957469+00:00"
      },
      {
        "url": "https://github.com/citrolabs/ego-lite/commit/fad68b972ede76ee608e3fdb8d4b76e9d5465e40",
        "accessed_at": "2026-11-17T04:07:37.957469+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 5737,
      "source_url": "https://github.com/trending/javascript?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOSEVU0g",
    "full_name": "citrolabs/ego-lite",
    "stargazers_count": 23215,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "325b6f26ca9452fcfb81cc6f52e3889573a7c141e9d07ab35f678b7d95d48e52",
    "last_success_at": "2026-11-17T03:51:51.030511+00:00"
  }
}
```

</details>
