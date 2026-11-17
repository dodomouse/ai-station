# Claude Code Templates

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 33885 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T06:06:21.884334+00:00 |

## 中文

提供 Claude Code 组件目录和命令行安装工具，用于选择技能、子智能体、命令、Hooks、MCP 配置及插件。

### 用途与功能

- 通过目录搜索和预览组件，再用 CLI 安装到相应配置位置。
- 涵盖开发审查与工作流组件；API 安全审查智能体要求整理端点、认证授权关系和可复核问题证据。
- invoice-organizer 技能指导提取票据信息、统一文件名、分类保存副本并生成 CSV 汇总，缺失信息交由人工核实。

### 环境与限制

需要 Node.js/npm 和兼容的 Claude Code；组件可能另外要求 Python、浏览器、MCP 服务或 API 凭据。安装会写入本地配置，Hooks 和组件可触发脚本，应先阅读实际文件及权限。目录包含第三方组件，根 MIT 不替代其原许可。票据提取和安全审查都是智能体工作流，不保证识别准确、税务合规或发现所有漏洞。

### 开始使用

先在目录中查看目标组件文件，再运行 `npx claude-code-templates@latest` 交互安装，或使用组件页给出的精确命令。检查配置差异，按需连接外部服务，并用样例项目验证。

参阅[官方 README](https://github.com/davila7/claude-code-templates/blob/ce1cbd39fc3abfdcbfc49bddd1009fd8236b1268/README.md)。

### 收录与来源

把可组合的智能体配置集中成可检索目录，降低寻找和安装组件的重复工作。已核对票据整理指令与 API 审查流程改写，未安装 CLI 或执行组件。

维护证据：[重写 API 审查智能体的产品指令：先建立端点与认证授权清单，逐项追踪输入和危险操作，要求反证候选问题并提供请求、源码位置和修复建议，同时限定本地验证及只读报告](https://github.com/davila7/claude-code-templates/commit/291762626caaaa180186dcc387211b9e1f3d2bba)（2026-11-17）。

仓库来自用户于 2026-11-17 提供的办公技能 PDF，已另行核对上游。本条按工程通用标准复核，不设 Star 门槛。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Provides a component catalog and CLI installer for Claude Code skills, subagents, commands, hooks, MCP configurations and plugins.

### Uses and features

- Searches and previews catalog components and installs them into the corresponding configuration locations.
- Includes development-review workflows; the API security agent specifies endpoint inventories, authentication/authorization mapping and reviewable finding evidence.
- The invoice-organizer skill guides extraction, consistent filenames, categorized copies and CSV summaries, with unclear information flagged for review.

### Requirements and limits

Requires Node.js/npm and compatible Claude Code. Components may additionally require Python, a browser, MCP services or API credentials. Installation writes local configuration, and hooks/components can trigger scripts, so inspect their files and permissions first. Third-party components retain their original licenses rather than inheriting the root MIT grant. Invoice extraction and security review are agent workflows, not guarantees of accuracy, tax compliance or complete vulnerability detection.

### Getting started

Preview the target component files, then run `npx claude-code-templates@latest` interactively or use the exact command from its catalog page. Inspect configuration changes, connect external services as needed and verify behavior on a sample project.

See the [official README](https://github.com/davila7/claude-code-templates/blob/ce1cbd39fc3abfdcbfc49bddd1009fd8236b1268/README.md).

### Review and provenance

Collects composable agent configurations in a searchable catalog to reduce repetitive discovery and installation work. Invoice-organization instructions and the API-review workflow rewrite were reviewed; neither the CLI nor its components were executed.

Maintenance evidence: [Rewrites the API-review agent instructions to inventory endpoints and auth checks, trace input to sensitive operations, refute candidate findings and report concrete requests, source locations and fixes, with local-only validation and read-only reporting](https://github.com/davila7/claude-code-templates/commit/291762626caaaa180186dcc387211b9e1f3d2bba) (2026-11-17).

Identified in an office-skills PDF supplied by the user on 2026-11-17, independently checked against upstream sources and reviewed against the general catalog criteria, with no star threshold.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T06:06:21.884334+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "claude-code-templates",
    "name": "Claude Code Templates",
    "repository": "davila7/claude-code-templates",
    "repo_node_id": "R_kgDOPGh7XA",
    "category": "development",
    "summary": {
      "zh-CN": "提供 Claude Code 组件目录和命令行安装工具，用于选择技能、子智能体、命令、Hooks、MCP 配置及插件。",
      "en": "Provides a component catalog and CLI installer for Claude Code skills, subagents, commands, hooks, MCP configurations and plugins."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T06:06:21.884334+00:00",
        "en": "2026-11-17T06:06:21.884334+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "把可组合的智能体配置集中成可检索目录，降低寻找和安装组件的重复工作。已核对票据整理指令与 API 审查流程改写，未安装 CLI 或执行组件。",
      "en": "Collects composable agent configurations in a searchable catalog to reduce repetitive discovery and installation work. Invoice-organization instructions and the API-review workflow rewrite were reviewed; neither the CLI nor its components were executed.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/davila7/claude-code-templates/blob/ce1cbd39fc3abfdcbfc49bddd1009fd8236b1268/LICENSE",
      "license_sha256": "15cc073ffa3a01bb7da145aeae2a842b473860d142c92485536ee9c91195a705",
      "source_commit": "ce1cbd39fc3abfdcbfc49bddd1009fd8236b1268",
      "reviewed_at": "2026-11-17T06:06:21.884334+00:00",
      "evidence_pinned_at": "2026-11-17T06:06:21.884334+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "MIT approval covers the repository-authored CLI, catalog tooling and original components. README Attribution explicitly preserves each imported component’s original license, including external Anthropic and community material; this is not a blanket MIT approval of the whole component catalog. External MCP servers, dependencies, services and input documents are outside that grant.",
      "files": [
        {
          "spdx": "MIT",
          "osi_approved": true,
          "source_url": "https://github.com/davila7/claude-code-templates/blob/ce1cbd39fc3abfdcbfc49bddd1009fd8236b1268/LICENSE",
          "license_sha256": "15cc073ffa3a01bb7da145aeae2a842b473860d142c92485536ee9c91195a705",
          "source_commit": "ce1cbd39fc3abfdcbfc49bddd1009fd8236b1268",
          "reviewed_at": "2026-11-17T05:54:50.206488+00:00",
          "evidence_pinned_at": "2026-11-17T05:54:50.206488+00:00",
          "evidence_status": "hash_matched",
          "scope": "MIT approval covers the repository-authored CLI, catalog tooling and original components. README Attribution explicitly preserves each imported component’s original license, including external Anthropic and community material; this is not a blanket MIT approval of the whole component catalog. External MCP servers, dependencies, services and input documents are outside that grant."
        }
      ]
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-17T04:44:31Z",
        "reviewed_at": "2026-11-17T06:06:21.884334+00:00",
        "url": "https://github.com/davila7/claude-code-templates/commit/291762626caaaa180186dcc387211b9e1f3d2bba",
        "qualifies": true,
        "reason": {
          "zh-CN": "重写 API 审查智能体的产品指令：先建立端点与认证授权清单，逐项追踪输入和危险操作，要求反证候选问题并提供请求、源码位置和修复建议，同时限定本地验证及只读报告",
          "en": "Rewrites the API-review agent instructions to inventory endpoints and auth checks, trace input to sensitive operations, refute candidate findings and report concrete requests, source locations and fixes, with local-only validation and read-only reporting"
        },
        "reviewed_files": [
          "cli-tool/components/agents/security/api-security-audit.md"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/davila7/claude-code-templates",
        "accessed_at": "2026-11-17T06:06:21.884334+00:00"
      },
      {
        "url": "https://github.com/davila7/claude-code-templates/blob/ce1cbd39fc3abfdcbfc49bddd1009fd8236b1268/README.md",
        "accessed_at": "2026-11-17T06:06:21.884334+00:00"
      },
      {
        "url": "https://github.com/davila7/claude-code-templates/blob/ce1cbd39fc3abfdcbfc49bddd1009fd8236b1268/LICENSE",
        "accessed_at": "2026-11-17T06:06:21.884334+00:00"
      },
      {
        "url": "https://github.com/davila7/claude-code-templates/commit/291762626caaaa180186dcc387211b9e1f3d2bba",
        "accessed_at": "2026-11-17T06:06:21.884334+00:00"
      },
      {
        "url": "https://github.com/davila7/claude-code-templates/blob/ce1cbd39fc3abfdcbfc49bddd1009fd8236b1268/cli-tool/components/skills/productivity/invoice-organizer/SKILL.md",
        "accessed_at": "2026-11-17T06:06:21.884334+00:00"
      },
      {
        "url": "https://github.com/davila7/claude-code-templates/blob/ce1cbd39fc3abfdcbfc49bddd1009fd8236b1268/cli-tool/package.json",
        "accessed_at": "2026-11-17T06:06:21.884334+00:00"
      }
    ],
    "discovery": {
      "kind": "user_pdf",
      "submitted_date": "2026-11-17",
      "source_url": "https://github.com/davila7/claude-code-templates",
      "repository_url": "https://github.com/davila7/claude-code-templates",
      "source_title": "办公室 Skill 从夯到拉(纯主观)",
      "source_pages": [
        4
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOPGh7XA",
    "full_name": "davila7/claude-code-templates",
    "stargazers_count": 33885,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "api_license_spdx": "MIT",
    "license_sha256": "15cc073ffa3a01bb7da145aeae2a842b473860d142c92485536ee9c91195a705",
    "last_success_at": "2026-11-17T05:45:50.908709+00:00"
  }
}
```

</details>
