# rust-anything

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[erkamyaman/rust-anything](https://github.com/erkamyaman/rust-anything)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 9104 |
| 评估时间 / Evaluated at | 2026-11-24T16:01:04.864732Z |

## 中文

rust-anything 把整个应用分块改写成 Rust，并在每一步用原版录制的行为逐条校验。把项目交给它后，它先记录原版做了什么，由编程智能体（Claude Code、Codex、Cursor、Gemini CLI、OpenCode 等）一块一块写 Rust，每块在通过录制回放比对与 gate 之前不会启用。它不翻译代码，而是证明改写没有改坏。

它帮助 AI 完成任务：为智能体提供热点定位、桥接层、必须对齐的行为标尺、安全启用方式与收口门禁，使智能体能在约束下改写生产级老项目。

### 主要功能

- 四步流程：Record（录制原版在生成用例与自身输入下的输出与异常）、Port（`bridge` 生成 Rust crate 与包装层并保留原 API，Rust 由智能体编写）、Check（`diff` 回放所有录制用例，全部一致且 `gate` 通过才发布）、Lift（回放无回退且各单元过 gate 后，`app lift` 产出纯 Rust 应用）。
- `rust-anything go --agent claude -- python3 app.py` 只迁最慢的一段：分析性能、挑选值得迁移的最外层循环、录制，并把 `src/port.rs` 交给智能体。
- 以 napi-rs、PyO3、wasm-bindgen 承载跨语言调用，由 rust-anything 决定迁移对象并核对行为。
- 支持 TypeScript/JavaScript、Python、C、Go、Ruby、Java、Kotlin（单元迁移）；PHP、C# 为预览；Swift 暂不支持。整应用录制可用 `--effects` 记录 HTTP、SMTP 等副作用并在回放时比对顺序与内容。

### 环境要求

- `cargo install rust-anything` 后执行 `rust-anything setup`，向发现的智能体注册 MCP server 并安装工作流技能；无 Rust 工具链可用各 Release 的预编译二进制，JS 项目可 `npm install -g rust-anything`。
- Claude Code 用 `/plugin install rust-anything --marketplace erkamyaman/rust-anything`；Codex 用 `codex plugin marketplace add erkamyaman/rust-anything` 与 `codex plugin add rust-anything@rust-anything`。
- 迁移时需要本机既能编译 Rust，也能运行原项目以对比两版。

### 使用限制

- 只能保证录制覆盖到的输入表现一致；未录到的边界、畸形请求、并发时序、消息队列与系统信号不会自动覆盖。
- `record` 与 `app record` 会真实运行原代码（`app record` 每个用例跑两次），`diff`、`gate`、`app replay` 会再次运行；有文件、数据库或网络副作用的用例每次都会执行。务必在副本、测试库且无生产密钥的环境执行。
- Rust 常用正则库不支持环视与反向引用，部分 JS / Python 正则行为会不一致；时间戳、随机数、并发顺序等非确定性输出需归一化或隔离。
- 小函数逐条跨语言调用通常更慢，收益来自批量迁移热点循环；纯闭源、无源码的程序无法做源码级迁移。

### 开始使用

1. 安装并执行 `rust-anything setup`，重启智能体后打开目标项目。
2. 让智能体执行例如「用 rust-anything 分析这个项目里最慢的操作，先把最耗时的一个模块迁到 Rust，并用同一批输入比较新旧版本的结果和性能」。
3. 进阶按 profile → bridge（建议 `--batch`）→ record → build → diff → bench → gate 推进，全量迁移完成后用 `app lift` 剥离旧运行时。

### 收录与来源

AI 任务用途已依据官方 README 核对：该项目为编程智能体提供录制比对与迁移门禁，帮助 AI 完成老项目改写任务。Star 为 2026-11-24T16:01:04.864732Z 的快照，达到总量 ≥1,000 条件，eligibility=true。近期活动：[2026-11-24 · commit](https://github.com/erkamyaman/rust-anything/commit/2e82dccdc63739f5fa9dc9d97c20706112f4d308)。本次为文档复核，未安装或运行上游项目。

- [Official README](https://github.com/erkamyaman/rust-anything/blob/main/README.md)
- [Documentation](https://rust-anything.com/)
- [Real-world ports](https://github.com/erkamyaman/rust-anything/blob/main/docs/real-world.md)

## English

rust-anything ports a whole app to Rust one piece at a time, checking each piece against the original's recorded behavior. It records what the original does, your coding agent (Claude Code, Codex, Cursor, Gemini CLI, OpenCode, and others) writes the Rust, and nothing ships until replay matches and `gate` passes. It does not translate code; it proves the rewrite.

It helps AI complete tasks by giving the agent hot-spot profiling, a bridge, the exact behavior to match, a safe way to switch a port on, and a gate that says when a port is done, so agents can rewrite production-grade legacy code under constraints.

### Features

- Four steps: Record (run the original on generated edge cases and your own inputs, saving returns and throws), Port (`bridge` generates a Rust crate and wrapper that preserve the original API while the agent writes the Rust), Check (`diff` replays every recorded case; nothing ships until all match and `gate` passes), and Lift (`app lift` produces a pure Rust app once replay passes with no fallback and every unit passes gate).
- `rust-anything go --agent claude -- python3 app.py` ports only the slowest part: it profiles the run, picks the outermost function worth moving, records it, and hands `src/port.rs` to the agent.
- Cross-language calls ride on napi-rs, PyO3, and wasm-bindgen; rust-anything decides what to move and proves it matches.
- Supports TypeScript/JavaScript, Python, C, Go, Ruby, Java, and Kotlin at unit level; PHP and C# are in preview; Swift is not supported. Whole-app recording can capture side effects such as HTTP and SMTP with `--effects` and compare their order and content on replay.

### Requirements

- `cargo install rust-anything` then `rust-anything setup`, which registers an MCP server and installs the workflow skill with agents it finds; prebuilt binaries are attached to each GitHub release, and JS projects can use `npm install -g rust-anything`.
- Claude Code: `/plugin install rust-anything --marketplace erkamyaman/rust-anything`. Codex: `codex plugin marketplace add erkamyaman/rust-anything` then `codex plugin add rust-anything@rust-anything`.
- Migration needs a machine that can both compile Rust and run the original project to compare the two versions.

### Limitations

- It only catches what the recording covers; unrecorded edge cases, malformed requests, concurrency timing, message queues, and system signals are not automatically covered.
- `record` and `app record` really run the original code (`app record` runs each case twice), and `diff`, `gate`, and `app replay` run the cases again; code with file, database, or network side effects executes once per case. Work on a copy, with a test database and no production credentials.
- Rust's common regex libraries lack lookaround and backreferences, so some JS / Python regex behavior differs; non-deterministic output such as timestamps, randomness, and concurrency order needs normalization or isolation.
- Calling Rust once per small function is usually slower than a JIT; the win comes from batching a hot loop. Closed-source programs without source cannot be ported at source level.

### Getting started

1. Install and run `rust-anything setup`, restart your agent, and open the target project.
2. Ask the agent, for example, to analyze the slowest operation with rust-anything, port the most expensive module to Rust, and compare results and timing on the same inputs.
3. For deeper work, follow profile → bridge (prefer `--batch`) → record → build → diff → bench → gate, then use `app lift` after a full migration.

### Review and sources

The documented AI task use was reviewed: the project gives coding agents recorded replay comparison and migration gates to help AI rewrite legacy projects. The Star snapshot at 2026-11-24T16:01:04.864732Z meets the 1,000 total-Star threshold; eligibility=true. Recent activity: [2026-11-24 · commit](https://github.com/erkamyaman/rust-anything/commit/2e82dccdc63739f5fa9dc9d97c20706112f4d308). This is a documentation review; the upstream software was not installed or run.

- [Official README](https://github.com/erkamyaman/rust-anything/blob/main/README.md)
- [Documentation](https://rust-anything.com/)
- [Real-world ports](https://github.com/erkamyaman/rust-anything/blob/main/docs/real-world.md)

## Review evidence

本次依据公开文章和 GitHub 官方文档复核，未安装或运行上游项目。

Reviewed against public articles and official GitHub documentation; upstream software was not installed or run.

- [GitHub activity](https://github.com/erkamyaman/rust-anything/commit/2e82dccdc63739f5fa9dc9d97c20706112f4d308) (2026-11-24T14:24:31Z)
- [Discovery article](https://mp.weixin.qq.com/s?__biz=MzIyOTY1ODAzNQ==&mid=2247489445&idx=1&sn=f25d5b6fd88a3fce202892be0536d2cb&chksm=e8be0b79dfc9826f20e5201797bd7c38fcccbe91d319cf64385a7a886fe2c1075a43e62cb5b5)

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-24T16:01:04.864732Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "rust-anything",
    "name": "rust-anything",
    "repository": "erkamyaman/rust-anything",
    "repo_node_id": "R_kgDOVwVmZA",
    "category": "development",
    "summary": {
      "zh-CN": "让编程智能体分块把老项目改写为 Rust，并用录制回放比对与门禁证明行为未变。",
      "en": "Lets coding agents port legacy apps to Rust piece by piece, proving behavior is unchanged with recorded replay and gates."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-24T16:01:04.864732Z",
        "en": "2026-11-24T16:01:04.864732Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "让编程智能体分块把老项目改写为 Rust，并用录制回放比对与门禁证明行为未变。",
        "en": "Lets coding agents port legacy apps to Rust piece by piece, proving behavior is unchanged with recorded replay and gates."
      },
      "source_url": "https://github.com/erkamyaman/rust-anything/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/erkamyaman/rust-anything/commit/2e82dccdc63739f5fa9dc9d97c20706112f4d308",
        "occurred_at": "2026-11-24T14:24:31Z",
        "reviewed_at": "2026-11-24T16:01:04.864732Z",
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
        "url": "https://github.com/erkamyaman/rust-anything/blob/main/README.md"
      },
      {
        "title": "Discovery article",
        "url": "https://mp.weixin.qq.com/s?__biz=MzIyOTY1ODAzNQ==&mid=2247489445&idx=1&sn=f25d5b6fd88a3fce202892be0536d2cb&chksm=e8be0b79dfc9826f20e5201797bd7c38fcccbe91d319cf64385a7a886fe2c1075a43e62cb5b5"
      }
    ]
  },
  "snapshot": {
    "full_name": "erkamyaman/rust-anything",
    "repo_node_id": "R_kgDOVwVmZA",
    "stargazers_count": 9104,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-24T16:01:04.864732Z",
    "source_url": "https://api.github.com/repos/erkamyaman/rust-anything"
  }
}
```

</details>
