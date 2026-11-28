# 麦田（Maitian）

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[CzzzzzzJ/mdldm-maitian](https://github.com/CzzzzzzJ/mdldm-maitian)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 自动化 / Automation |
| 状态 / Status | 已收录 / Included |
| Star | 2398 |
| 评估时间 / Evaluated at | 2026-11-28T16:00:27.380537Z |

## 中文

麦田是给自媒体创作者的开源工作台，由 Agent 驱动：你对 AI 说一句「整理发布」，发布 skill 让 Claude Code / Codex 看片、写各平台文案、生成发布工程并校验。它把成片、封面、文案和定时放进同一份分发计划，在专用 Chrome 里逐平台填写上传页、定时发布，并把各平台播放、互动、粉丝和转化数据汇总到网页看板。

它帮助 AI 完成的具体任务是：发布 skill 让 AI 助手读取一期视频，生成各平台文案与 `publish.json` 发布工程，再交给中控执行分发、取链接、采数据与复盘。

### 主要功能

- 发布 skill（`skills/maitian-publish`）：让 Claude Code / Codex 看片、写 B站/抖音/小红书/视频号/YouTube/X/Instagram 文案、生成并校验发布工程；快手需在 `batches` 中显式启用。
- 麦田发布助手（Chrome 插件）：各平台适配器，打开上传页、上传视频与封面、填文案、设定时。
- 中控（`hub.mjs`）：分发计划、调度、防重、到点取链接、每日采集播放互动与粉丝、网页大屏、飞书卡片通知，以及第 1/3/7 天复盘和周报。
- 转化：接入自有站点后，按 `utm_campaign` 归因注册、会员、订单和收入；可选接入小鹅通销售看板。
- 平台管理：网页查看登录态、按需打开单个平台登录页、停用不用的平台。

### 环境要求

- 一台常开的 macOS 或 Windows 10/11 电脑；Node.js ≥ 22.5（用到内置 `node:sqlite`）；Google Chrome，并用专用 Chrome 登录各平台。不存任何平台密码。
- 可选：NAS（放成片）、飞书群机器人、cloudflared 隧道。Windows 安装脚本在缺 Git 或 Node 时用 winget 补装。

### 使用限制

- B站、抖音、小红书、视频号只填写不发布，最后一下由用户自己点以降低风控风险；启用快手后同样只填写。YouTube、X、Instagram 可自动提交。
- 同一平台一份登录态放在专用 Chrome 的 profile 里，做不到同一平台多账号同时登录或在网页内嵌扫码。
- 成片必须 faststart（moov 在文件头），否则小红书报「无视频流信息」、抖音不出表单。
- 视频号的定时可能被平台改动，`sync` 会比对计划并在不一致时发提醒。
- 接入站点做转化属于二次开发：需按 `src/site.mjs` 提供两个只读接口。

### 开始使用

1. 按[安装指南](https://github.com/CzzzzzzJ/mdldm-maitian)选择方式：Agent 自动安装（把 `agent-install.md` 的指引交给 AI 助手）、一行安装脚本，或手动 `git clone` 后 `node src/init.mjs` 运行安装向导。
2. 用 `node src/demo.mjs` 先看假数据大屏；在专用 Chrome 里从应用商店添加「麦田发布助手」并登录各平台。
3. 用 `node src/hub.mjs doctor` 检查登录态；按发布 skill 生成一期发布工程后 `hub plan` 登记、`hub run` 分批填写。

### 收录与来源

AI 任务用途已依据官方 README 核对：发布 skill 明确面向 Claude Code / Codex 等 AI 助手，用于写文案、生成与校验发布工程。Star 为 2026-11-28T16:00:27.380537Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-28 · commit](https://github.com/CzzzzzzJ/mdldm-maitian/commit/d25b7f2f9e8af153fb45ed442270a6ea5d63e4d2)，合并 PR #65（国内媒体平台功能）。

本次为文档复核，未安装或运行上游项目。上述提交证明窗口内活动，不代表软件运行验证。许可不作为准入条件。

- [Official README](https://github.com/CzzzzzzJ/mdldm-maitian/blob/main/README.md)
- [Agent install guide](https://github.com/CzzzzzzJ/mdldm-maitian/blob/main/agent-install.md)
- [Publish skill](https://github.com/CzzzzzzJ/mdldm-maitian/tree/main/skills/maitian-publish)

## English

Maitian is an open-source publishing workstation for self-media creators, driven by Agents: tell the AI "organize and publish" and the publish skill has Claude Code / Codex watch the video, draft copy for each platform, and build and validate a publishing project. It puts the finished video, cover, copy and schedule into one distribution plan, fills in each platform's upload page in a dedicated Chrome, schedules posts, and aggregates plays, interactions, followers and conversion data into a web dashboard.

The concrete AI task it supports: the publish skill lets an AI assistant read an episode, produce platform-specific copy and a `publish.json` project, then hands it to the controller for distribution, link retrieval, data collection and review.

### Features

- Publish skill (`skills/maitian-publish`): lets Claude Code / Codex watch a video, write copy for Bilibili / Douyin / Xiaohongshu / WeChat Channels / YouTube / X / Instagram, and build and validate a publishing project; Kuaishou must be enabled explicitly in `batches`.
- Maitian publish assistant (Chrome extension): platform adapters that open upload pages, upload video and cover, fill in copy and set the schedule.
- Controller (`hub.mjs`): distribution plan, scheduling, deduplication, scheduled link retrieval, daily collection of plays/interactions and followers, web dashboard, Feishu card notifications, plus day-1/3/7 reviews and weekly reports.
- Conversion: with your own site connected, attribute registrations, memberships, orders and revenue via `utm_campaign`; optional Xiaoe-tong sales dashboard.
- Platform management: check login state in the web UI, open a single platform's login page on demand, and disable unused platforms.

### Requirements

- An always-on macOS or Windows 10/11 machine; Node.js ≥ 22.5 (uses built-in `node:sqlite`); Google Chrome, with a dedicated Chrome for platform logins. No platform passwords are stored.
- Optional: NAS (finished videos), Feishu group bot, cloudflared tunnel. The Windows installer uses winget to add Git or Node if missing.

### Limitations

- Bilibili, Douyin, Xiaohongshu and WeChat Channels are filled in but not published — the final click is the user's, to reduce risk; Kuaishou behaves the same when enabled. YouTube, X and Instagram can be auto-submitted.
- Each platform has one login state in the dedicated Chrome profile; simultaneous multi-account login on one platform or embedded QR login in the web UI is not supported.
- The finished video must be faststart (moov at file head), otherwise Xiaohongshu reports "no video stream" and Douyin shows no form.
- WeChat Channels scheduled times can be changed by the platform; `sync` compares against the plan and alerts on mismatch.
- Connecting a site for conversion is a secondary development task: provide two read-only endpoints per `src/site.mjs`.

### Getting started

1. Choose an install method per the [repository README](https://github.com/CzzzzzzJ/mdldm-maitian): Agent auto-install (hand `agent-install.md` to your AI assistant), the one-line install script, or manual `git clone` followed by `node src/init.mjs` for the setup wizard.
2. Run `node src/demo.mjs` to preview the dashboard with sample data; add the "Maitian publish assistant" from the Chrome Web Store in the dedicated Chrome and log in to each platform.
3. Run `node src/hub.mjs doctor` to check login state; after the publish skill produces an episode's publishing project, use `hub plan` to register it and `hub run` to fill platforms in batches.

### Review and sources

The documented AI task use was reviewed: the publish skill explicitly targets AI assistants such as Claude Code / Codex for writing copy and building/validating publishing projects. The Star snapshot at 2026-11-28T16:00:27.380537Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-28 · commit](https://github.com/CzzzzzzJ/mdldm-maitian/commit/d25b7f2f9e8af153fb45ed442270a6ea5d63e4d2), merging PR #65 (domestic media platform feature).

This is a documentation review; the upstream software was not installed or run. The cited commit establishes activity within the review window, not runtime validation. Licensing is not an admission criterion.

- [Official README](https://github.com/CzzzzzzJ/mdldm-maitian/blob/main/README.md)
- [Agent install guide](https://github.com/CzzzzzzJ/mdldm-maitian/blob/main/agent-install.md)
- [Publish skill](https://github.com/CzzzzzzJ/mdldm-maitian/tree/main/skills/maitian-publish)

## Review evidence

本次依据公开文章和 GitHub 官方文档复核，未安装或运行上游项目。

Reviewed against public articles and official GitHub documentation; upstream software was not installed or run.

- [GitHub activity](https://github.com/CzzzzzzJ/mdldm-maitian/commit/d25b7f2f9e8af153fb45ed442270a6ea5d63e4d2) (2026-11-28T14:40:01Z)
- [Discovery article](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA==&mid=2247538736&idx=1&sn=36e970efb8b69b95f8b66a102b628a62&chksm=f9a28bf9ced502efdef49a8ff57a21c4e68439e40de0a3164def6c16c66e89fa0dd22087163d)

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-28T16:00:27.380537Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "mdldm-maitian",
    "name": "麦田（Maitian）",
    "repository": "CzzzzzzJ/mdldm-maitian",
    "repo_node_id": "R_kgDOVt2VFA",
    "category": "automation",
    "summary": {
      "zh-CN": "给自媒体创作者的 Agent 驱动多平台发布工作台：发布 skill 让 Claude Code / Codex 看片、写各平台文案、生成并校验发布工程，中控自动填写上传页、定时发布并汇总各平台数据与转化。",
      "en": "An Agent-driven publishing workstation for self-media creators: a publish skill lets Claude Code / Codex watch videos, draft platform-specific copy and build/validate publishing projects, while the controller auto-fills upload pages, schedules posts and aggregates traffic and conversion data."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-28T16:00:27.380537Z",
        "en": "2026-11-28T16:00:27.380537Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "给自媒体创作者的 Agent 驱动多平台发布工作台：发布 skill 让 Claude Code / Codex 看片、写各平台文案、生成并校验发布工程，中控自动填写上传页、定时发布并汇总各平台数据与转化。",
        "en": "An Agent-driven publishing workstation for self-media creators: a publish skill lets Claude Code / Codex watch videos, draft platform-specific copy and build/validate publishing projects, while the controller auto-fills upload pages, schedules posts and aggregates traffic and conversion data."
      },
      "source_url": "https://github.com/CzzzzzzJ/mdldm-maitian/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/CzzzzzzJ/mdldm-maitian/commit/d25b7f2f9e8af153fb45ed442270a6ea5d63e4d2",
        "occurred_at": "2026-11-28T14:40:01Z",
        "reviewed_at": "2026-11-28T16:00:27.380537Z",
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
        "url": "https://github.com/CzzzzzzJ/mdldm-maitian/blob/main/README.md"
      },
      {
        "title": "Discovery article",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA==&mid=2247538736&idx=1&sn=36e970efb8b69b95f8b66a102b628a62&chksm=f9a28bf9ced502efdef49a8ff57a21c4e68439e40de0a3164def6c16c66e89fa0dd22087163d"
      }
    ]
  },
  "snapshot": {
    "full_name": "CzzzzzzJ/mdldm-maitian",
    "repo_node_id": "R_kgDOVt2VFA",
    "stargazers_count": 2398,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-28T16:00:27.380537Z",
    "source_url": "https://api.github.com/repos/CzzzzzzJ/mdldm-maitian"
  }
}
```

</details>
