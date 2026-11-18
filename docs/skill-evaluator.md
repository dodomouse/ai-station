# SkillEvaluator

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[NVIDIA/SkillEvaluator](https://github.com/NVIDIA/SkillEvaluator)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 3513 |
| 评估时间 / Evaluated at | 2026-11-18T14:34:02.253297Z |

## 中文

SkillEvaluator 是 NVIDIA 推出的多层框架，用于评估和改进 AI 智能体技能与插件：检查质量、安全、重叠、兼容性，并衡量技能对任务结果的真实影响。

它先做质量检查，再对比启用与不启用某技能的运行效果；也可用 CI 模板在合并前设置自动化质量与安全门禁，无需自行编写评估代码。

### 主要功能

- 三层评估：Tier 1 校验（500+ 静态规则、Harness Check、安全扫描）、Tier 2 去重（语义重叠检测）、Tier 3 实时智能体评估（技能带来的效果提升）。
- 无需密钥的快速检查：quality-check 与 harness-check 不需要 API 密钥、GPU 或 Docker。
- 安全扫描：集成 SkillSpector、Gitleaks、Bandit 与可选 Semgrep，检查提示、钩子、MCP 配置、权限与密钥。
- CI 集成：提供 GitHub 与 GitLab 模板，含 11 项 CI 检查与可下载报告。
- 多宿主：可作为技能安装到 Claude Code、Codex 等智能体，并检查技能是否能被目标宿主加载。

### 环境要求

- 在 Python 3.12–3.14 环境中执行 `pip install skillevaluator`，或用 `uv tool install --python 3.13 skillevaluator`。
- 完整静态覆盖需安装外部扫描器；Tier 2 需嵌入与聊天模型；Tier 3 需模型提供方、受支持的智能体与运行中的沙箱（默认 Docker，基于 Harbor）。
- 合资格的 NVIDIA Developer Program 成员可用免费 NVIDIA Build 端点做原型验证，但受访问条款与速率限制约束。

### 使用限制

- 支持级别为 Experimental，社区支持、尽力而为，无 SLA 或企业支持权益。
- 完整三层评估需配置提供方、扫描器与沙箱；模型与托管沙箱可能产生费用。
- `--no-llm` 不会移除扫描器要求；无法运行的扫描器会报告 INCOMPLETE 并非零退出。
- 安装会下载安装额外第三方开源软件，使用前需审查其许可条款。
- 本次为文档复核，未安装或运行上游项目。

### 开始使用

1. 在 Python 3.12–3.14 环境执行 `pip install skillevaluator`。
2. 运行 `skillevaluator quality-check ./my-skill` 做无密钥静态质量检查，或 `skillevaluator harness-check ./my-skill` 检查宿主兼容性。
3. 运行 `skillevaluator validate ./my-skill --tiers 1` 执行 Tier 1。运行全部层级前，按官方说明执行 `pip install "skillevaluator[all]"`（或对应的全层级安装），配置所选模型提供方及扫描器，准备已审查的数据集并启动 Docker 沙箱，再去掉 `--tiers 1`。

### 收录与来源

AI 任务用途已依据官方 README 核对。Star 为 2026-11-18T14:34:02.253297Z 的快照，达到总量 ≥1,000 条件；月净增无基线，未作为依据。

近期活动：[2026-11-18 · commit](https://github.com/NVIDIA/SkillEvaluator/commit/affe1acc3d0a24877c5d508d96ac69663a7fd92a)，澄清无密钥校验与仓库 CI 设置。该提交证明窗口内活动，不代表运行验证。许可不作为准入条件。

- [Official README](https://github.com/NVIDIA/SkillEvaluator/blob/main/README.md)

## English

SkillEvaluator is a multi-tier framework from NVIDIA for evaluating and improving AI agent skills and plugins: quality, security, overlap, compatibility, and real impact on task results.

It starts with quality checks, then compares runs with and without a skill to measure lift. A CI template adds automated quality and security gates before merge, without writing evaluation code yourself.

### Features

- Three tiers: Tier 1 validation (500+ static rules, Harness Check, security scanning), Tier 2 deduplication (semantic overlap), and Tier 3 live agent evaluation (measured skill lift).
- Keyless checks: quality-check and harness-check need no API key, GPU, or Docker.
- Security scanning: SkillSpector, Gitleaks, Bandit, and optional Semgrep check prompts, hooks, MCP config, permissions, and secrets.
- CI integration: GitHub and GitLab templates with 11 CI checks and downloadable reports.
- Multi-harness: install as a skill into Claude Code, Codex, and other agents, and check whether a skill loads in a target harness.

### Requirements

- Install with `pip install skillevaluator` in a Python 3.12–3.14 environment, or `uv tool install --python 3.13 skillevaluator`.
- Full static coverage needs external scanners; Tier 2 needs embedding and chat models; Tier 3 needs a provider, a supported agent, and a running sandbox (Docker by default, powered by Harbor).
- Eligible NVIDIA Developer Program members can use hosted endpoints for free prototyping, subject to access terms and rate limits.

### Limitations

- Support level is Experimental, community-supported, best-effort, with no SLA or NVIDIA enterprise support entitlement.
- All three tiers require configured providers, scanners, and sandbox; model and managed-sandbox usage can incur charges.
- `--no-llm` does not remove scanner requirements; a scanner that cannot run is reported as INCOMPLETE and exits nonzero.
- Installation downloads additional third-party open source software; review their license terms before use.
- This is a documentation review; the upstream software was not installed or run.

### Getting started

1. Run `pip install skillevaluator` in a Python 3.12–3.14 environment.
2. Run `skillevaluator quality-check ./my-skill` for a keyless static check, or `skillevaluator harness-check ./my-skill` for harness compatibility.
3. Run `skillevaluator validate ./my-skill --tiers 1` for Tier 1. Before running all tiers, follow the official setup for `pip install "skillevaluator[all]"` (or an equivalent all-tier installation), configure the selected provider and scanners, prepare a reviewed dataset, and start the Docker sandbox; then omit `--tiers 1`.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-18T14:34:02.253297Z meets the total-Star threshold of 1,000; no monthly-growth baseline was available and was not used.

Recent activity: [2026-11-18 · commit](https://github.com/NVIDIA/SkillEvaluator/commit/affe1acc3d0a24877c5d508d96ac69663a7fd92a). The cited commit establishes activity within the review window, not runtime validation. Licensing is not an admission criterion.

- [Official README](https://github.com/NVIDIA/SkillEvaluator/blob/main/README.md)

## Review evidence

本次从 GitHub Trending 日榜发现项目，并依据 GitHub 官方文档复核，未安装或运行上游项目。榜单显示的今日新增 Star 仅用于挑选复核对象，不作为近一个月净增证据。

Discovered on GitHub Trending daily and reviewed against official GitHub documentation; upstream software was not installed or run. Today's stars select review candidates, not evidence of net growth over a calendar month.

- [GitHub activity](https://github.com/NVIDIA/SkillEvaluator/commit/affe1acc3d0a24877c5d508d96ac69663a7fd92a) (2026-11-18T09:12:56Z)
- [GitHub Trending daily](https://github.com/trending?since=daily)

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-18T14:34:02.253297Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "skill-evaluator",
    "name": "SkillEvaluator",
    "repository": "NVIDIA/SkillEvaluator",
    "repo_node_id": "R_kgDOTDcPlA",
    "category": "development",
    "summary": {
      "zh-CN": "多层框架，用于评估 AI 智能体技能与插件的质量、安全、重叠、兼容性及真实效果。",
      "en": "A multi-tier framework for evaluating AI agent skills and plugins on quality, security, overlap, compatibility, and real impact."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-18T14:34:02.253297Z",
        "en": "2026-11-18T14:34:02.253297Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "多层框架，用于评估 AI 智能体技能与插件的质量、安全、重叠、兼容性及真实效果。",
        "en": "A multi-tier framework for evaluating AI agent skills and plugins on quality, security, overlap, compatibility, and real impact."
      },
      "source_url": "https://github.com/NVIDIA/SkillEvaluator/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/NVIDIA/SkillEvaluator/commit/affe1acc3d0a24877c5d508d96ac69663a7fd92a",
        "occurred_at": "2026-11-18T09:12:56Z",
        "reviewed_at": "2026-11-18T14:34:02.253297Z",
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
        "url": "https://github.com/NVIDIA/SkillEvaluator/blob/main/README.md"
      },
      {
        "title": "GitHub Trending daily",
        "url": "https://github.com/trending?since=daily"
      }
    ]
  },
  "snapshot": {
    "full_name": "NVIDIA/SkillEvaluator",
    "repo_node_id": "R_kgDOTDcPlA",
    "stargazers_count": 3513,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-18T14:34:02.253297Z",
    "source_url": "https://api.github.com/repos/NVIDIA/SkillEvaluator"
  }
}
```

</details>
