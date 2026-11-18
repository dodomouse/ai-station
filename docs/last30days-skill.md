# Last30Days Skill

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 69671 |
| 评估时间 / Evaluated at | 2026-11-18T14:33:57.649647Z |

## 中文

Last30Days 是一个由 AI 智能体主导的搜索引擎，按点赞、喜欢和真实资金（而非编辑）评分。它并行搜索 Reddit、X、YouTube、TikTok、Hacker News、Polymarket 等平台，按真实互动打分，再由 AI 裁判综合成一份简报。

它帮助智能体在会议前、调研公司或追踪话题时，汇总近 30 天内人们真正关注的内容，而不是依赖搜索引擎的编辑结果。

### 主要功能

- 多平台检索：覆盖 Reddit、X、YouTube、TikTok、HN、Polymarket、GitHub、Digg、arXiv、Techmeme、Yahoo Finance、LinkedIn、招聘页与专利等来源。
- 按互动评分：以点赞、评论、观看量与预测市场赔率等真实信号排序，而非 SEO 权重。
- AI 综合：由智能体裁判把多源结果合成为带引用与引语行的简报。
- 发现模式：扫描分类榜单与热门故事，输出带跨源数据、热度标签与后续查询命令的话题。
- 多宿主安装：支持 Claude Code 插件、npx skills、claude.ai 上传、Claude Desktop、OpenClaw 与 Grok 等 50 多种 Agent Skills 宿主。

### 环境要求

- 推荐 Claude Code 插件安装；也支持 `npx skills add -g` 安装到任意 Agent Skills 宿主。
- Reddit、HN、Polymarket、GitHub 等开箱即用；X、YouTube、TikTok、arXiv 等需在设置向导中配置自有密钥或浏览器会话。
- 部分来源需单独安装 CLI（如 digg-pp-cli、arxiv-pp-cli、techmeme-pp-cli）或提供 API 令牌。
- 可用 `--preflight` 在不读 Cookie、不写文件、不运行研究的情况下查看配置计划。

### 使用限制

- 搜索能力取决于凭据、已安装工具、话题类型与显式选择；许多平台是需登录的围墙花园，需自带密钥与会话。
- 同一机器不要混用插件与 npx skills 安装，否则 `/last30days` 会出现重复条目。
- README 中的示例输出为演示性质；实际结果取决于平台可用性与模型。
- 本次为文档复核，未安装或运行上游项目。

### 开始使用

1. 在 Claude Code 中执行 `/plugin marketplace add mvanhorn/last30days-skill`，再执行 `/plugin install last30days`。
2. 或其他宿主执行 `npx skills add mvanhorn/last30days-skill -g`。
3. 运行 `/last30days <话题或人物>`，按首次向导提示解锁所需来源。

### 收录与来源

AI 任务用途已依据官方 README 核对。Star 为 2026-11-18T14:33:57.649647Z 的快照，达到总量 ≥1,000 条件；月净增无基线，未作为依据。

近期活动：[2026-11-17 · commit](https://github.com/mvanhorn/last30days-skill/commit/a854f3bcb2c4344d7498426d653378510f8b253a)，升级 trufflesecurity/trufflehog 依赖。该提交证明窗口内活动，不代表运行验证。许可不作为准入条件。

- [Official README](https://github.com/mvanhorn/last30days-skill/blob/main/README.md)

## English

Last30Days is an AI agent-led search engine scored by upvotes, likes, and real money rather than editors. It searches Reddit, X, YouTube, TikTok, Hacker News, Polymarket and more in parallel, scores them by real engagement, and an AI judge synthesizes the results into one brief.

It helps an agent build a grounded picture of the last 30 days before a meeting, during company research, or while tracking a topic, instead of relying on editor-aggregated search results.

### Features

- Multi-source search: Reddit, X, YouTube, TikTok, HN, Polymarket, GitHub, Digg, arXiv, Techmeme, Yahoo Finance, LinkedIn, careers pages, patents, and more.
- Engagement scoring: ranks by real signals such as upvotes, comments, views, and prediction-market odds rather than SEO relevance.
- AI synthesis: an agent judge combines multiple sources into a brief with inline quotes and attribution.
- Discovery mode: sweeps category listings and front-page stories, returning velocity-ranked topics with cross-source numbers and follow-up commands.
- Multi-harness install: Claude Code plugin, npx skills, claude.ai upload, Claude Desktop, OpenClaw, Grok, and 50+ Agent Skills hosts.

### Requirements

- Claude Code plugin install is recommended; `npx skills add -g` works for any Agent Skills host.
- Reddit, HN, Polymarket, and GitHub work immediately; X, YouTube, TikTok, and arXiv require your own keys or browser sessions via the setup wizard.
- Some sources need extra CLIs (for example digg-pp-cli, arxiv-pp-cli, techmeme-pp-cli) or API tokens.
- Use `--preflight` to inspect config, cookie plans, and writes without running research.

### Limitations

- Availability depends on credentials, installed tools, topic, and explicit opt-ins; many platforms are walled gardens requiring your own keys and sessions.
- Do not mix plugin and npx skills installs on one machine, or `/last30days` will show duplicate entries.
- Example outputs in the README are illustrative; real results depend on platform availability and models.
- This is a documentation review; the upstream software was not installed or run.

### Getting started

1. In Claude Code run `/plugin marketplace add mvanhorn/last30days-skill`, then `/plugin install last30days`.
2. Or, for other hosts, run `npx skills add mvanhorn/last30days-skill -g`.
3. Run `/last30days <topic or person>` and follow the first-run wizard to unlock the sources you need.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-18T14:33:57.649647Z meets the total-Star threshold of 1,000; no monthly-growth baseline was available and was not used.

Recent activity: [2026-11-17 · commit](https://github.com/mvanhorn/last30days-skill/commit/a854f3bcb2c4344d7498426d653378510f8b253a). The cited commit establishes activity within the review window, not runtime validation. Licensing is not an admission criterion.

- [Official README](https://github.com/mvanhorn/last30days-skill/blob/main/README.md)

## Review evidence

本次从 GitHub Trending 日榜发现项目，并依据 GitHub 官方文档复核，未安装或运行上游项目。榜单显示的今日新增 Star 仅用于挑选复核对象，不作为近一个月净增证据。

Discovered on GitHub Trending daily and reviewed against official GitHub documentation; upstream software was not installed or run. Today's stars select review candidates, not evidence of net growth over a calendar month.

- [GitHub activity](https://github.com/mvanhorn/last30days-skill/commit/a854f3bcb2c4344d7498426d653378510f8b253a) (2026-11-17T22:37:08Z)
- [GitHub Trending daily](https://github.com/trending?since=daily)

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-18T14:33:57.649647Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "last30days-skill",
    "name": "Last30Days Skill",
    "repository": "mvanhorn/last30days-skill",
    "repo_node_id": "R_kgDOQ__jdA",
    "category": "ai",
    "summary": {
      "zh-CN": "AI 智能体主导的搜索引擎，跨多平台检索并按真实互动评分综合成简报，帮助 AI 完成调研任务。",
      "en": "An AI agent-led search engine that scores multiple platforms by real engagement and synthesizes a grounded brief for research tasks."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-18T14:33:57.649647Z",
        "en": "2026-11-18T14:33:57.649647Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "AI 智能体主导的搜索引擎，跨多平台检索并按真实互动评分综合成简报，帮助 AI 完成调研任务。",
        "en": "An AI agent-led search engine that scores multiple platforms by real engagement and synthesizes a grounded brief for research tasks."
      },
      "source_url": "https://github.com/mvanhorn/last30days-skill/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/mvanhorn/last30days-skill/commit/a854f3bcb2c4344d7498426d653378510f8b253a",
        "occurred_at": "2026-11-17T22:37:08Z",
        "reviewed_at": "2026-11-18T14:33:57.649647Z",
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
        "url": "https://github.com/mvanhorn/last30days-skill/blob/main/README.md"
      },
      {
        "title": "GitHub Trending daily",
        "url": "https://github.com/trending?since=daily"
      }
    ]
  },
  "snapshot": {
    "full_name": "mvanhorn/last30days-skill",
    "repo_node_id": "R_kgDOQ__jdA",
    "stargazers_count": 69671,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-18T14:33:57.649647Z",
    "source_url": "https://api.github.com/repos/mvanhorn/last30days-skill"
  }
}
```

</details>
