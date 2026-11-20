# App Store Compliance Playbook

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[mjmirza/app-store-compliance](https://github.com/mjmirza/app-store-compliance)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 1965 |
| 评估时间 / Evaluated at | 2026-11-20T04:00:17.568982Z |

## 中文

App Store Compliance Playbook 将 iOS 与 Android 应用被 App Store 和 Google Play 拒绝的常见原因整理为参考手册，并提供提交前自动检查的 guard 脚本。它可以作为 skill 安装进多种 AI 编码工具，让 AI 智能体在每次提交前运行检查，并在发现严重拒绝风险时阻断命令。

它能帮助 AI 完成具体任务：AI 编码代理在向 App Store Connect 或 Google Play 提交前，按统一规则审计应用代码与清单，定位可能导致拒绝的风险并给出修复指引。

### 主要功能

- 提供可阅读的拒绝模式手册与提交前检查清单，每条规则都指向 Apple 或 Google 的真实来源。
- guard 脚本扫描项目并列出风险，严重项排在前面，尽量给出触发的文件与行号；末行给出 BLOCKED.、CLEAR. 或 NOT CHECKED. 结论。
- install.sh 可将 guard、skill 与 hook 安装进 Claude Code、Codex CLI、Gemini CLI、OpenCode、Cursor、GitHub Copilot、Grok、Qwen Code、Kimi Code、Factory Droid、Augment Auggie、Windsurf 等工具；除 Claude Code 外均需 python3。
- 安装后可用 /app-store-audit 斜杠命令审计；hook 会在任何提交命令前运行 guard，遇到严重风险即阻断。
- 覆盖导致多数拒绝的两类检查：带可用后端与演示账号的审核准备，以及与运行时行为（含每个 SDK）一致的隐私声明；文档还跟踪 EU AI Act、DSA、COPPA 等监管期限。
- verify-citations.py 可联网核对规则引用是否真实。

### 环境要求

- 必需依赖：一次性扫描只需 git 与 bash；脚本不安装任何东西，也不改动应用。
- 安装进 AI 编码工具需要 git 与 bash；除 Claude Code 外的工具还需要 python3。
- Windows 上通过 Git Bash 安装，安装器会同时注册 Bash 与 PowerShell 的 hook。
- 扫描需要临时目录可写；受管 Expo 应用若无原生目录，只会读取 app.json 或 app.config，需先运行 npx expo prebuild 才能覆盖原生代码。
- 可选：verify-citations.py 需要网络访问，用于核对引用，不属于基础扫描。

### 使用限制

- 代码扫描无法查看账号与上架状态，例如开发者账号是否有效、协议是否已接受、Play 账号与包名是否已注册，这些都可能在上架前造成阻塞。
- 审核备注与 App Store Connect 中声明的数据用途无法自行核实，因此会被列为待确认项，而非判定为正常。
- 部分工具未自动接入：Kiro CLI 尚未在真实环境测试，Cline 仅在 macOS 与 Linux 上通过可执行文件运行，Amp、Goose、Crush、Roo Code、Continue、Aider、Copilot for Xcode 需要手动配置或手动运行 guard。
- 扫描耗时随项目规模变化，小项目约一秒，大项目最长约一分钟；找不到 iOS/Android 项目或无法写入扫描文件时会输出 NOT CHECKED.。
- 这是提交前检查与参考手册，不能保证审核通过；README 仅给出个别开发者一次通过的例子。

### 开始使用

1. 必需：克隆仓库，git clone https://github.com/mjmirza/app-store-compliance ~/repositories/app-store-compliance 。
2. 一次性扫描：运行 bash ~/repositories/app-store-compliance/agent-os/hooks/app-store-compliance-guard.sh /path/to/your/app （目录含空格时保留引号），按 BLOCKED.、CLEAR.、NOT CHECKED. 结论处理并阅读提交前清单。
3. 可选：要让 AI 代理每次提交前自动检查，运行 bash ~/repositories/app-store-compliance/scripts/install.sh --tool all （或指定工具名），按提示重启工具或在 Codex 中批准新 hook。
4. 之后可用 /app-store-audit 审计，并在提交前按 docs/PRE-SUBMISSION-CHECKLIST.md 走查账号与上架准备。

### 收录与来源

AI 任务用途已依据官方 README 核对。Star 为 2026-11-20 快照 1965，达到总量≥1000 条件；月度净增基线缺失未核验，因总量条件已满足无需另行核对。

近期活动：2026-11-15 提交 d2156bab9d7189835631c0a99adcc2479d32138d，发布 2.4.0 并加入 11 月缺口扫描检查。

本次为文档复核，未安装或运行上游项目。提交证明窗口内活动，不代表运行验证。许可不作为准入条件。

- Official README：https://github.com/mjmirza/app-store-compliance/blob/main/README.md
- Project website：https://mjmirza.github.io/app-store-compliance/
- Pre-submission checklist：https://github.com/mjmirza/app-store-compliance/blob/main/docs/PRE-SUBMISSION-CHECKLIST.md
- Mistake patterns and appeal playbook：https://github.com/mjmirza/app-store-compliance/blob/main/docs/MISTAKE-PATTERNS.md

## English

App Store Compliance Playbook collects the common reasons iOS and Android apps get rejected by the App Store and Google Play into a reference, and provides a pre-submission guard script. It installs as a skill into multiple AI coding tools so an AI agent runs the check before every submit and blocks the command when it finds a critical rejection risk.

It helps AI complete a concrete task: before an agent submits to App Store Connect or Google Play, it audits the app's code and manifest against one set of rules, locates rejection risks, and points to concrete fixes.

### Features

- A readable rejection-pattern playbook and a pre-submission checklist; each rule traces to a real Apple or Google source.
- A guard script that scans a project and ranks findings, critical first, with the triggering file and line when available; the last line reports BLOCKED., CLEAR., or NOT CHECKED.
- install.sh wires the guard, skill, and hook into Claude Code, Codex CLI, Gemini CLI, OpenCode, Cursor, GitHub Copilot, Grok, Qwen Code, Kimi Code, Factory Droid, Augment Auggie, Windsurf, and more; every tool except Claude Code also needs python3.
- After install, the /app-store-audit slash command runs the audit; the hook runs the guard before any submit command and blocks it when a critical risk stands.
- Covers the two checks behind most rejections: a working demo account with a live backend, and a privacy declaration that matches runtime behavior including every SDK; it also tracks regulatory deadlines such as the EU AI Act, DSA, and COPPA.
- verify-citations.py checks over the network that cited rules are real.

### Requirements

- Required for a one-time scan: git and bash; the script installs nothing and changes nothing in the app.
- Installing into an AI coding tool needs git and bash; every tool except Claude Code also needs python3.
- On Windows, install from Git Bash; the installer registers hooks for both Bash and PowerShell.
- The scan needs a writable temp folder; a managed Expo app with no native folders only has app.json or app.config read, so run npx expo prebuild to cover native code.
- Optional: verify-citations.py needs network access to check citations and is not part of the basic scan.

### Limitations

- The code scan cannot see account or listing state, such as whether the developer account is active, whether agreements are accepted, or whether the Play account and package names are registered; these can block a first launch before review starts.
- Review notes and data usage declared in App Store Connect cannot be verified by the tool, so they are surfaced as items to confirm rather than assumed clean.
- Some tools are not wired automatically: Kiro CLI is not yet tested against a live instance, Cline runs hooks on macOS and Linux only via an executable file, and Amp, Goose, Crush, Roo Code, Continue, Aider, and Copilot for Xcode need manual setup or a manual guard run.
- Scan time scales with project size, about a second for a small project and up to a minute for a large one; NOT CHECKED. is printed when no iOS/Android project is found or scan files cannot be written.
- This is a pre-submission check and reference, not a guarantee of approval; the README gives only individual reports of first-try approval.

### Getting started

1. Required: clone with git clone https://github.com/mjmirza/app-store-compliance ~/repositories/app-store-compliance .
2. For a one-time scan, run bash ~/repositories/app-store-compliance/agent-os/hooks/app-store-compliance-guard.sh /path/to/your/app (keep quotes when the path has spaces), act on the BLOCKED., CLEAR., NOT CHECKED. verdict, and read the pre-submission checklist.
3. Optional: to have the agent check before every submit, run bash ~/repositories/app-store-compliance/scripts/install.sh --tool all (or a specific tool name), then restart the tool or approve the new hook in Codex as prompted.
4. Afterwards use /app-store-audit for audits, and walk through the account and program readiness section of docs/PRE-SUBMISSION-CHECKLIST.md before submitting.

### Review and sources

The documented AI task use was reviewed. The Star snapshot on 2026-11-20 is 1965, meeting the total-Star threshold of 1,000; monthly net growth was not assessed because the total-Star condition is already satisfied.

Recent activity: commit d2156bab9d7189835631c0a99adcc2479d32138d on 2026-11-15, releasing 2.4.0 with November gap sweep checks.

This is a documentation review; the upstream software was not installed or run. The commit establishes activity within the review window, not runtime validation. Licensing is not an admission criterion.

- Official README: https://github.com/mjmirza/app-store-compliance/blob/main/README.md
- Project website: https://mjmirza.github.io/app-store-compliance/
- Pre-submission checklist: https://github.com/mjmirza/app-store-compliance/blob/main/docs/PRE-SUBMISSION-CHECKLIST.md
- Mistake patterns and appeal playbook: https://github.com/mjmirza/app-store-compliance/blob/main/docs/MISTAKE-PATTERNS.md

## Review evidence

本次从 GitHub Trending 日榜发现项目，并依据 GitHub 官方文档复核，未安装或运行上游项目。榜单显示的今日新增 Star 仅用于挑选复核对象，不作为近一个月净增证据。

Discovered on GitHub Trending daily and reviewed against official GitHub documentation; upstream software was not installed or run. Today's stars select review candidates, not evidence of net growth over a calendar month.

- [GitHub activity](https://github.com/mjmirza/app-store-compliance/commit/d2156bab9d7189835631c0a99adcc2479d32138d) (2026-11-15T20:08:31Z)
- [GitHub Trending daily](https://github.com/trending?since=daily)

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-20T04:00:17.568982Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "app-store-compliance",
    "name": "App Store Compliance Playbook",
    "repository": "mjmirza/app-store-compliance",
    "repo_node_id": "R_kgDOSyx1Zg",
    "category": "development",
    "summary": {
      "zh-CN": "将 iOS/Android 应用被 App Store 与 Google Play 拒绝的原因整理为参考手册与提交前 guard，可作为 skill 安装进 AI 编码工具，让代理在提交前审计应用并阻断高风险提交。",
      "en": "A reference and pre-submission guard for App Store and Google Play rejections, installable as a skill into AI coding tools so agents audit apps and block risky submits."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-20T04:00:17.568982Z",
        "en": "2026-11-20T04:00:17.568982Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "将 iOS/Android 应用被 App Store 与 Google Play 拒绝的原因整理为参考手册与提交前 guard，可作为 skill 安装进 AI 编码工具，让代理在提交前审计应用并阻断高风险提交。",
        "en": "A reference and pre-submission guard for App Store and Google Play rejections, installable as a skill into AI coding tools so agents audit apps and block risky submits."
      },
      "source_url": "https://github.com/mjmirza/app-store-compliance/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/mjmirza/app-store-compliance/commit/d2156bab9d7189835631c0a99adcc2479d32138d",
        "occurred_at": "2026-11-15T20:08:31Z",
        "reviewed_at": "2026-11-20T04:00:17.568982Z",
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
        "url": "https://github.com/mjmirza/app-store-compliance/blob/main/README.md"
      },
      {
        "title": "GitHub Trending daily",
        "url": "https://github.com/trending?since=daily"
      }
    ]
  },
  "snapshot": {
    "full_name": "mjmirza/app-store-compliance",
    "repo_node_id": "R_kgDOSyx1Zg",
    "stargazers_count": 1965,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-20T04:00:17.568982Z",
    "source_url": "https://api.github.com/repos/mjmirza/app-store-compliance"
  }
}
```

</details>
