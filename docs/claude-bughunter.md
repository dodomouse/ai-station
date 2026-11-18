# Claude-BugHunter

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 10641 |
| 评估时间 / Evaluated at | 2026-11-18T14:33:50.589597Z |

## 中文

Claude-BugHunter 是一套自包含的 Claude Code 技能包，用于授权范围内的漏洞赏金与外部红队工作。它包含 83 个技能、15 个斜杠命令、681 个已披露报告模式（覆盖 24 类核心漏洞），以及企业身份与基础设施攻击矩阵、任务文件夹脚手架和 Burp MCP 集成。

它让编码智能体按资深安全研究员的方式工作：先建立方法论与思维框架，再按主题自动加载对应的检测技能，最后完成验证与报告。适合在自有资产、已获书面授权的赏金项目范围或 CTF 中使用。

### 主要功能

- 方法论层：bb-methodology 与 redteam-mindset 提供五阶段非线性工作流、批判性思考框架与红队纪律。
- Web 应用狩猎：58 个 hunt-* 技能按漏洞类别给出检测模式、载荷、绕过表与利用链模板。
- 边界攻击：面向 M365/Entra、Okta、vCenter、SSL VPN、SharePoint、云 IAM 的企业平台链，含 2024–2026 年 CVE 链与凭据后升级。
- 交付与验证：triage-validation、报告编写与 evidence-hygiene，提供 7-Question Gate、VRT 严重级别与 PII 脱敏。
- 多智能体宿主：技能为通用 Agent Skills（SKILL.md），可安装到 Claude Code、OpenCode、OpenAI Codex CLI、Hermes Agent 与 Google AntiGravity。

### 环境要求

- 推荐 Claude Code 通过插件市场安装；也支持复制安装（git clone）与 pipx 安装 cbh CLI。
- 复制安装需 git；终端运行器需 Python 与 pipx；Burp MCP 集成为可选项。
- 支持 macOS、Windows（PowerShell）与 Linux。

### 使用限制

- 仅覆盖外部攻击面；内部 AD、C2、后渗透、持久化、规避、iOS/硬件/RF/ICS 与二进制利用明确不在范围内。
- 技能按主题自动加载，无需按名称调用；`/hunt` 引擎与斜杠命令仅 Claude Code 可用。
- 仅面向自有或已获书面授权的资产；内置范围校验门，明确排除对未授权目标使用 0day、后渗透工具、恶意软件与大规模目标。
- Anthropic 运行时网络安全保障默认可能拦截相关请求，即使授权工作也可能需要申请 CVP。
- 本次为文档复核，未安装或运行上游项目。

### 开始使用

1. 在 Claude Code 中执行 `/plugin marketplace add elementalsouls/Claude-BugHunter`，再执行 `/plugin install claude-bughunter@elementalsouls`。
2. 或克隆仓库后按平台运行 `bash scripts/install.sh`（macOS/Linux）或 `pwsh ./scripts/install.ps1`（Windows）。
3. 打开 Claude Code，用自然语言描述授权范围内的测试目标，相关技能会自动加载。详见 INSTALL.md 与 USAGE.md。

### 收录与来源

AI 任务用途已依据官方 README 核对。Star 为 2026-11-18T14:33:50.589597Z 的快照，达到总量 ≥1,000 条件；月净增无基线，未作为依据。

近期活动：[2026-11-18 · commit](https://github.com/elementalsouls/Claude-BugHunter/commit/b63ae349afad88772e6d854a277ae9965fd4c369)，刷新 star history 图表。该提交证明窗口内活动，不代表运行验证。许可不作为准入条件。

- [Official README](https://github.com/elementalsouls/Claude-BugHunter/blob/main/README.md)
- [Installation guide](https://github.com/elementalsouls/Claude-BugHunter/blob/main/INSTALL.md)
- [Usage guide](https://github.com/elementalsouls/Claude-BugHunter/blob/main/USAGE.md)

## English

Claude-BugHunter is a self-contained Claude Code skill bundle for authorized bug hunting and external red-team work. It ships 83 skills, 15 slash commands, 681 disclosed-report patterns across 24 core vulnerability classes, enterprise identity and infrastructure attack matrices, engagement-folder scaffolding, and Burp MCP integration.

It makes a coding agent work like a senior security researcher: establish methodology and mindset, auto-load the right per-topic detection skills, then validate and report. Intended for assets you own, bug-bounty in-scope targets, or CTF challenges.

### Features

- Methodology layer: bb-methodology and redteam-mindset provide a five-phase non-linear workflow, critical-thinking framework, and red-team discipline.
- Web app hunting: 58 hunt-* skills with per-class detection patterns, payloads, bypass tables, and chain templates.
- Perimeter: enterprise platform chains (M365/Entra, Okta, vCenter, SSL VPN, SharePoint, cloud IAM) with 2024–2026 CVE chains and post-credential escalation.
- Delivery: triage-validation, reporting, and evidence-hygiene with a 7-Question Gate, VRT-aware severity, and PII redaction.
- Multi-harness: skills use the generic Agent Skills (SKILL.md) format and install to Claude Code, OpenCode, OpenAI Codex CLI, Hermes Agent, and Google AntiGravity.

### Requirements

- Claude Code is recommended via the plugin marketplace; copy install (git clone) and a pipx-installed `cbh` runner are also supported.
- Copy install needs git; the terminal runner needs Python and pipx; Burp MCP integration is optional.
- Supports macOS, Windows (PowerShell), and Linux.

### Limitations

- Covers only the external attack surface; internal AD, C2, post-exploitation, persistence, evasion, iOS/hardware/RF/ICS, and binary exploitation are explicitly out of scope.
- Skills load automatically by topic; the `/hunt` engine and slash commands are Claude-Code-only.
- Intended for owned or written-authorized assets; scope gates are included and weaponizing 0-days, post-exploitation tools, malware, and mass targeting are excluded.
- Anthropic runtime cyber safeguards may block even authorized work; the CVP program is the supported route.
- This is a documentation review; the upstream software was not installed or run.

### Getting started

1. In Claude Code run `/plugin marketplace add elementalsouls/Claude-BugHunter`, then `/plugin install claude-bughunter@elementalsouls`.
2. Or clone the repository and run `bash scripts/install.sh` (macOS/Linux) or `pwsh ./scripts/install.ps1` (Windows).
3. Describe an in-scope target in plain English; relevant skills load automatically. See INSTALL.md and USAGE.md.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-18T14:33:50.589597Z meets the total-Star threshold of 1,000; no monthly-growth baseline was available and was not used.

Recent activity: [2026-11-18 · commit](https://github.com/elementalsouls/Claude-BugHunter/commit/b63ae349afad88772e6d854a277ae9965fd4c369). The cited commit establishes activity within the review window, not runtime validation. Licensing is not an admission criterion.

- [Official README](https://github.com/elementalsouls/Claude-BugHunter/blob/main/README.md)
- [Installation guide](https://github.com/elementalsouls/Claude-BugHunter/blob/main/INSTALL.md)
- [Usage guide](https://github.com/elementalsouls/Claude-BugHunter/blob/main/USAGE.md)

## Review evidence

本次从 GitHub Trending 日榜发现项目，并依据 GitHub 官方文档复核，未安装或运行上游项目。榜单显示的今日新增 Star 仅用于挑选复核对象，不作为近一个月净增证据。

Discovered on GitHub Trending daily and reviewed against official GitHub documentation; upstream software was not installed or run. Today's stars select review candidates, not evidence of net growth over a calendar month.

- [GitHub activity](https://github.com/elementalsouls/Claude-BugHunter/commit/b63ae349afad88772e6d854a277ae9965fd4c369) (2026-11-18T13:09:41Z)
- [GitHub Trending daily](https://github.com/trending?since=daily)

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-18T14:33:50.589597Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "claude-bughunter",
    "name": "Claude-BugHunter",
    "repository": "elementalsouls/Claude-BugHunter",
    "repo_node_id": "R_kgDOSUzdDA",
    "category": "development",
    "summary": {
      "zh-CN": "用于授权范围内漏洞赏金与外部红队工作的 Claude Code 技能包，帮助 AI 完成安全测试与报告。",
      "en": "A Claude Code skill bundle for authorized bug hunting and external red-team work that helps AI run security tests and reporting."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-18T14:33:50.589597Z",
        "en": "2026-11-18T14:33:50.589597Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "用于授权范围内漏洞赏金与外部红队工作的 Claude Code 技能包，帮助 AI 完成安全测试与报告。",
        "en": "A Claude Code skill bundle for authorized bug hunting and external red-team work that helps AI run security tests and reporting."
      },
      "source_url": "https://github.com/elementalsouls/Claude-BugHunter/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/elementalsouls/Claude-BugHunter/commit/b63ae349afad88772e6d854a277ae9965fd4c369",
        "occurred_at": "2026-11-18T13:09:41Z",
        "reviewed_at": "2026-11-18T14:33:50.589597Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "GitHub API 记录的具体活动，证明复核窗口内有活动；不代表运行验证。",
          "en": "A specific GitHub API activity establishes activity in the review window, not runtime validation."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/elementalsouls/Claude-BugHunter/blob/main/README.md"
      },
      {
        "title": "GitHub Trending daily",
        "url": "https://github.com/trending?since=daily"
      }
    ]
  },
  "snapshot": {
    "full_name": "elementalsouls/Claude-BugHunter",
    "repo_node_id": "R_kgDOSUzdDA",
    "stargazers_count": 10641,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-18T14:33:50.589597Z",
    "source_url": "https://api.github.com/repos/elementalsouls/Claude-BugHunter"
  }
}
```

</details>
