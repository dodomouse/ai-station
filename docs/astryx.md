# Astryx

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[meta/astryx](https://github.com/meta/astryx)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 32787 |
| 评估时间 / Evaluated at | 2026-11-24T16:01:13.906268Z |

## 中文

Astryx 是一套完全可定制的开源设计系统，既供人使用，也供并肩工作的智能体使用，目前处于 Beta，基于 React 19+ 与 StyleX。它在 Meta 内部发展八年，支撑 13,000+ 应用，提供 150+ 无障碍组件、品牌级主题、暗色模式、现成模板与 CLI；只需导入预编译 CSS 并使用类型化 React 组件，无需构建插件或采用样式库。

它帮助 AI 完成任务：API、文档与 CLI 为人和智能体协同设计，`astryx init` 会把 Astryx 指南写入 AGENTS.md / CLAUDE.md，让智能体按项目既有组件与规范写界面，而不是靠猜测。

### 主要功能

- 150+ 可组合组件、主题系统与工具类；内部结构开放，可任意层级组合，必要时 swizzle 弹出组件源码自行掌控。
- 无样式锁定：用 `className` 配合 Tailwind、CSS modules 或原生 CSS 覆盖，消费者无需感知 StyleX。
- 主题是一组 CSS 自定义属性覆盖，可在不 fork 或包装组件源码的前提下定制。
- CLI 提供组件文档、模板、脚手架、主题与 codemod；文档、Storybook、Sandbox 同时面向人和智能体。

### 环境要求

- 消费项目需要 React 19+（`react` 与 `react-dom` 是 `@astryxdesign/core` 的 peer 依赖）。
- 安装：`npm install @astryxdesign/core @astryxdesign/theme-neutral @stylexjs/stylex` 并 `-D @astryxdesign/cli`，随后 `npx @astryxdesign/cli init`；CLI 也可 `npm i -g @astryxdesign/cli` 全局安装。
- CLI 包在消费项目支持 Node.js 22.13.0+；仓库本地开发使用 `.nvmrc` 指定的 Node 与 pnpm 11。

### 使用限制

- 目前为 Beta；`@astryxdesign/lab` 实验组件不发布到 npm，`@astryxdesign/vega` 与 `@astryxdesign/charts` 仅以 `@canary` 标签发布，尚无稳定版本。
- 组件给的是能力而非强制护栏：传入什么值就渲染什么值，设计约定写在文档与示例中，需团队自行遵守。
- 需要 React 19 或更高版本，旧项目升级成本需自行评估。

### 开始使用

1. 安装核心包、主题、StyleX 与 CLI（见上）。
2. 运行 `npx @astryxdesign/cli init`，它会写入样式与主题入门步骤，并把 Astryx 指南保存到 AGENTS.md / CLAUDE.md，供智能体读取。
3. 按 [core README](https://github.com/meta/astryx/blob/main/packages/core/README.md#quick-start) 完成 CSS 导入与主题 Provider；用 `npm run astryx -- component --list` 列出组件。

### 收录与来源

AI 任务用途已依据官方 README 核对：该设计系统的 CLI 会向 AGENTS.md / CLAUDE.md 写入指南，帮助智能体按统一组件与约定构建界面。Star 为 2026-11-24T16:01:13.906268Z 的快照，达到总量 ≥1,000 条件，eligibility=true。近期活动：[2026-11-24 · commit](https://github.com/meta/astryx/commit/d63c24970f9ab1dc5e3024a7123ec7edee2a0f11)。本次为文档复核，未安装或运行上游项目。

- [Official README](https://github.com/meta/astryx/blob/main/README.md)
- [Docs](https://astryx.atmeta.com)
- [Storybook](https://astryx.atmeta.com/storybook/)

## English

Astryx is a fully customizable open source design system built for people and the agents working alongside them. Currently in Beta and built on React 19+ with StyleX, it grew inside Meta over eight years, powers 13,000+ apps, and ships 150+ accessible components, brand-level theming, dark mode, ready-to-ship templates, and a CLI. You import pre-built CSS and use typed React components, with no build plugin or styling library to adopt.

It helps AI complete tasks: the API, docs, and CLI are designed together for humans and agents, and `astryx init` saves the Astryx guide into AGENTS.md / CLAUDE.md so agents build with the project's existing components and conventions instead of guessing.

### Features

- 150+ composable components, a theme system, and utilities; internals are open for composition at any level, with swizzle to eject a component's full source when needed.
- No styling lock-in: override with `className` using Tailwind, CSS modules, or plain CSS; consumers need not adopt StyleX.
- A theme is a set of CSS custom property overrides, so it can be customized without forking or wrapping component source.
- The CLI provides component docs, templates, scaffolding, themes, and codemods; docs, Storybook, and Sandbox serve both people and agents.

### Requirements

- Consumer projects need React 19+ (`react` and `react-dom` are peer dependencies of `@astryxdesign/core`).
- Install `npm install @astryxdesign/core @astryxdesign/theme-neutral @stylexjs/stylex` plus `-D @astryxdesign/cli`, then run `npx @astryxdesign/cli init`; the CLI can also be installed globally with `npm i -g @astryxdesign/cli`.
- The CLI package supports Node.js 22.13.0+ in consumer projects; local development uses the Node version pinned in `.nvmrc` and pnpm 11.

### Limitations

- Currently Beta; `@astryxdesign/lab` experimental components are not published to npm, and `@astryxdesign/vega` and `@astryxdesign/charts` ship only under the `@canary` tag with no stable release.
- Components provide capability rather than guardrails: any value passed is rendered, and conventions live in docs and examples, so teams must follow them.
- React 19 or later is required; upgrading legacy projects needs its own evaluation.

### Getting started

1. Install the core package, theme, StyleX, and CLI (see above).
2. Run `npx @astryxdesign/cli init`, which prints the styles and theme steps and saves the Astryx guide into AGENTS.md / CLAUDE.md for agents to read.
3. Complete CSS imports and the theme provider using the [core README](https://github.com/meta/astryx/blob/main/packages/core/README.md#quick-start); list components with `npm run astryx -- component --list`.

### Review and sources

The documented AI task use was reviewed: the design system's CLI writes guidance into AGENTS.md / CLAUDE.md to help agents build UIs with consistent components and conventions. The Star snapshot at 2026-11-24T16:01:13.906268Z meets the 1,000 total-Star threshold; eligibility=true. Recent activity: [2026-11-24 · commit](https://github.com/meta/astryx/commit/d63c24970f9ab1dc5e3024a7123ec7edee2a0f11). This is a documentation review; the upstream software was not installed or run.

- [Official README](https://github.com/meta/astryx/blob/main/README.md)
- [Docs](https://astryx.atmeta.com)
- [Storybook](https://astryx.atmeta.com/storybook/)

## Review evidence

本次依据公开文章和 GitHub 官方文档复核，未安装或运行上游项目。

Reviewed against public articles and official GitHub documentation; upstream software was not installed or run.

- [GitHub activity](https://github.com/meta/astryx/commit/d63c24970f9ab1dc5e3024a7123ec7edee2a0f11) (2026-11-24T15:15:54Z)
- [Discovery article](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA==&mid=2247538734&idx=1&sn=663aff51de396b45a5d7825f27439e6c&chksm=f9a28be7ced502f1d2d79aee06cdc63c341d4aef6baba8f94daeef6405661ea49ce76ea67c3c)

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-24T16:01:13.906268Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "astryx",
    "name": "Astryx",
    "repository": "meta/astryx",
    "repo_node_id": "R_kgDOQ2zHeg",
    "category": "development",
    "summary": {
      "zh-CN": "面向人与智能体的开源设计系统，CLI 写入 AGENTS.md/CLAUDE.md 指南帮助智能体按统一组件构建界面。",
      "en": "An open source design system for people and agents whose CLI writes guidance into AGENTS.md/CLAUDE.md for consistent agent-built UIs."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-24T16:01:13.906268Z",
        "en": "2026-11-24T16:01:13.906268Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "面向人与智能体的开源设计系统，CLI 写入 AGENTS.md/CLAUDE.md 指南帮助智能体按统一组件构建界面。",
        "en": "An open source design system for people and agents whose CLI writes guidance into AGENTS.md/CLAUDE.md for consistent agent-built UIs."
      },
      "source_url": "https://github.com/meta/astryx/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/meta/astryx/commit/d63c24970f9ab1dc5e3024a7123ec7edee2a0f11",
        "occurred_at": "2026-11-24T15:15:54Z",
        "reviewed_at": "2026-11-24T16:01:13.906268Z",
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
        "url": "https://github.com/meta/astryx/blob/main/README.md"
      },
      {
        "title": "Discovery article",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA==&mid=2247538734&idx=1&sn=663aff51de396b45a5d7825f27439e6c&chksm=f9a28be7ced502f1d2d79aee06cdc63c341d4aef6baba8f94daeef6405661ea49ce76ea67c3c"
      }
    ]
  },
  "snapshot": {
    "full_name": "meta/astryx",
    "repo_node_id": "R_kgDOQ2zHeg",
    "stargazers_count": 32787,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-24T16:01:13.906268Z",
    "source_url": "https://api.github.com/repos/meta/astryx"
  }
}
```

</details>
