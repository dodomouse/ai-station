# Modern Web Guidance (Source)

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[GoogleChrome/modern-web-guidance-src](https://github.com/GoogleChrome/modern-web-guidance-src)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 9681 |
| 评估时间 / Evaluated at | 2026-11-21T11:29:01.055867Z |

## 中文

Modern Web Guidance 是一组技能（skills），把 Web 平台专业知识、最佳实践和浏览器兼容性数据直接注入编码智能体。它由 Google Chrome、Microsoft Edge、Mozilla Firefox 和 MDN 团队与 Web 开发社区共同维护，目标是引导智能体放弃过时写法，改用现代 Web 平台能力。

本仓库是 GoogleChrome/modern-web-guidance 的源码仓库，包含用于编写、校准和评估其内容的代码与文档；实际可分发的技能通过 npm 包 modern-web-guidance 提供。

它能帮助 AI 完成具体任务：编码智能体（如 Codex、Claude Code）在处理网页开发任务时，可先检索专家审核过的指南，再按现代、可兼顾兼容性的写法生成代码，避免因为训练数据偏旧而产出臃肿或过时的实现。

### 主要功能

- 提供按场景整理的指南，覆盖现代浏览器 API、性能与可访问性、以及稳妥的降级方案（Responsible Fallbacks）。
- CLI 支持按关键词或自然语言描述搜索指南（search）、按 ID 获取某篇指南（retrieve），以及扫描本地代码库中的过时写法（legacy-scan）。
- 指南强调 token 效率，并通过评估（evals）剔除模型已掌握的内容，聚焦于模型知识盲区。
- 覆盖多个方向：用户体验（View Transitions、动画）、CSS 布局（容器查询、subgrid、oklch 等）、性能（预加载、INP 诊断、scheduler.yield）、表单与 UI（Popover、dialog、:user-invalid 等）、可访问性、以及内置 AI（本地翻译、摘要、语言检测 API）。
- README 列出 262 项现代 Web 特性，其中 CSS 与布局 140 项。

### 环境要求

- 安装需要 Node.js 22 或更高版本。
- 通过 npx modern-web-guidance@latest install 运行交互式向导完成安装；README 也列出了其他安装方式。
- 可不安装直接试用 npx modern-web-guidance@latest 的 search、retrieve、legacy-scan 子命令。

### 使用限制

- 本仓库是源码仓库，用于编写、校准和评估内容；终端用户安装和使用的技能来自 npm 包 modern-web-guidance 及 GoogleChrome/modern-web-guidance 内容仓库。
- 它向智能体的上下文窗口提供经过专家整理的指南，并不直接修改代码；实际改动由编码智能体完成。
- 指南聚焦现代 Web 特性并经过裁剪以保持 token 效率，不是完整 Web API 文档；更早的遗留写法不在覆盖重点内。
- 特定写法的浏览器兼容性需按项目目标浏览器核对；指南提供的是通用最佳实践与兼容提示。

### 开始使用

1. 确认已安装 Node.js 22+，运行 npx modern-web-guidance@latest install，按交互式向导完成安装。
2. 不安装先试用：运行 npx modern-web-guidance@latest search "animate a dialog modal backdrop" 检索指南，或用 npx modern-web-guidance@latest retrieve "animate-to-from-top-layer" 按 ID 获取。
3. 用 npx modern-web-guidance@latest legacy-scan . 扫描现有代码库中的过时写法；在编码智能体的需求中可要求「先用 Modern Web Guidance 查推荐写法，再改代码」。

### 收录与来源

AI 任务用途已依据官方 README 核对，eligibility=true。Star 为 2026-11-21T11:29:01.055867Z 的快照，共 9681，达到总量 ≥1,000 条件。

近期活动：[2026-11-20 · commit](https://github.com/GoogleChrome/modern-web-guidance-src/commit/634d0f83bb41092832797411d148350196b8258d)：legacy-scan 增加 --max-files 参数并报告部分覆盖（#3666）。

本次为文档复核，未安装或运行上游项目。上述提交仅证明窗口内活动，不代表运行验证。许可不作为准入条件。

- [Official README](https://github.com/GoogleChrome/modern-web-guidance-src/blob/main/README.md)
- [Documentation](https://developer.chrome.com/docs/modern-web-guidance)
- [Eval Dashboard](https://googlechrome.github.io/modern-web-guidance-src/)

## English

Modern Web Guidance is a set of skills that embed web platform expertise, best practices, and browser compatibility data directly into coding agents. It is stewarded by the Google Chrome, Microsoft Edge, Mozilla Firefox, and MDN teams alongside the web development community, aiming to steer agents away from legacy patterns toward modern web platform capabilities.

This repository is the source repository for GoogleChrome/modern-web-guidance, containing the code and documentation for authoring, calibrating, and evaluating its content; the distributable skill is delivered through the npm package modern-web-guidance.

It helps AI with concrete tasks: when coding agents such as Codex and Claude Code work on web development, they can first retrieve expert-reviewed guides and then produce modern, compatibility-aware code, avoiding bloated or outdated output caused by older training data.

### Features

- Provides scenario-organized guides covering modern browser APIs, performance and accessibility, and responsible fallbacks.
- CLI supports searching guides by keyword or natural-language description (search), retrieving a guide by ID (retrieve), and scanning a local codebase for legacy patterns (legacy-scan).
- Guides are designed to be token-efficient; evals prune content that models already know, focusing on knowledge gaps.
- Covers multiple disciplines: user experience (View Transitions, animations), CSS layout (container queries, subgrid, oklch), performance (preloading, INP diagnostics, scheduler.yield), forms and UI (Popover, dialog, :user-invalid), accessibility, and built-in AI (local translation, summarization, language detection APIs).
- The README lists 262 modern web features, including 140 in CSS & Layout.

### Requirements

- Installation requires Node.js 22 or later.
- Run npx modern-web-guidance@latest install for the interactive installation wizard; the README also documents alternative installation methods.
- You can try the CLI without installing using the search, retrieve, and legacy-scan subcommands via npx modern-web-guidance@latest.

### Limitations

- This is the source repository for authoring/calibrating/evaluating content; the skill end users install comes from the npm package modern-web-guidance and the GoogleChrome/modern-web-guidance content repository.
- It supplies curated guidelines into the agent's context window rather than editing code itself; the actual changes are made by the coding agent.
- Guides focus on modern web features and are pruned for token efficiency; they are not exhaustive Web API documentation, and legacy patterns are not the coverage focus.
- Compatibility of a specific technique should be checked against the project's target browsers; the guides provide general best practices and compatibility notes.

### Getting started

1. Ensure Node.js 22+ is installed, then run npx modern-web-guidance@latest install and follow the interactive wizard.
2. Try without installing: run npx modern-web-guidance@latest search "animate a dialog modal backdrop" to find guides, or npx modern-web-guidance@latest retrieve "animate-to-from-top-layer" to fetch one by ID.
3. Use npx modern-web-guidance@latest legacy-scan . to scan an existing codebase for legacy patterns; in an agent prompt you can ask to "check the recommended approach with Modern Web Guidance first, then change the code."

### Review and sources

The documented AI task use was reviewed and eligibility=true. The Star snapshot at 2026-11-21T11:29:01.055867Z is 9681, meeting the total-Star threshold of 1,000.

Recent activity: [2026-11-20 · commit](https://github.com/GoogleChrome/modern-web-guidance-src/commit/634d0f83bb41092832797411d148350196b8258d) — legacy-scan adds a --max-files flag and reports partial coverage (#3666).

This is a documentation review; the upstream software was not installed or run. The cited commit only establishes activity within the review window, not runtime validation. Licensing is not an admission criterion.

- [Official README](https://github.com/GoogleChrome/modern-web-guidance-src/blob/main/README.md)
- [Documentation](https://developer.chrome.com/docs/modern-web-guidance)
- [Eval Dashboard](https://googlechrome.github.io/modern-web-guidance-src/)

## Review evidence

本次依据公开文章和 GitHub 官方文档复核，未安装或运行上游项目。

Reviewed against public articles and official GitHub documentation; upstream software was not installed or run.

- [GitHub activity](https://github.com/GoogleChrome/modern-web-guidance-src/commit/634d0f83bb41092832797411d148350196b8258d) (2026-11-20T21:17:42Z)
- [Discovery article](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA==&mid=2247538609&idx=1&sn=4f14737e2c3c5e739567c1406c764fa0&chksm=f9a28478ced50d6e93eb66cea14d1af7b1e61e5c0562dddfa2667f9782312be32cd7a073dcff)

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-21T11:29:01.055867Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "modern-web-guidance-src",
    "name": "Modern Web Guidance (Source)",
    "repository": "GoogleChrome/modern-web-guidance-src",
    "repo_node_id": "R_kgDORCp1Rw",
    "category": "development",
    "summary": {
      "zh-CN": "把现代 Web 平台知识与浏览器兼容最佳实践以 Skill/CLI 形式注入 Codex、Claude Code 等编码智能体，引导其避免过时写法。",
      "en": "Embeds modern web platform expertise and browser compatibility best practices as a skill/CLI into coding agents such as Codex and Claude Code, steering them away from legacy patterns."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-21T11:29:01.055867Z",
        "en": "2026-11-21T11:29:01.055867Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "把现代 Web 平台知识与浏览器兼容最佳实践以 Skill/CLI 形式注入 Codex、Claude Code 等编码智能体，引导其避免过时写法。",
        "en": "Embeds modern web platform expertise and browser compatibility best practices as a skill/CLI into coding agents such as Codex and Claude Code, steering them away from legacy patterns."
      },
      "source_url": "https://github.com/GoogleChrome/modern-web-guidance-src/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/GoogleChrome/modern-web-guidance-src/commit/634d0f83bb41092832797411d148350196b8258d",
        "occurred_at": "2026-11-20T21:17:42Z",
        "reviewed_at": "2026-11-21T11:29:01.055867Z",
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
        "url": "https://github.com/GoogleChrome/modern-web-guidance-src/blob/main/README.md"
      },
      {
        "title": "Discovery article",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA==&mid=2247538609&idx=1&sn=4f14737e2c3c5e739567c1406c764fa0&chksm=f9a28478ced50d6e93eb66cea14d1af7b1e61e5c0562dddfa2667f9782312be32cd7a073dcff"
      }
    ]
  },
  "snapshot": {
    "full_name": "GoogleChrome/modern-web-guidance-src",
    "repo_node_id": "R_kgDORCp1Rw",
    "stargazers_count": 9681,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-21T11:29:01.055867Z",
    "source_url": "https://api.github.com/repos/GoogleChrome/modern-web-guidance-src"
  }
}
```

</details>
