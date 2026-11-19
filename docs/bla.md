# BLA (Blind LLM Agents)

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[qybaihe/bla](https://github.com/qybaihe/bla)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 6188 |
| 评估时间 / Evaluated at | 2026-11-19T16:00:58.096476Z |

## 中文

BLA（Blind LLM Agents，包名 bla-agents）是一套开源蓝队防御工具，以 MCP 服务与 CLI 形式帮助软件作者保护自己的发布产物，对抗 REA 等 AI 逆向工程 Agent。它通过投毒、耗尽与致幻等手段抬高 AI 自动逆向的算力与 Token 成本，同时保持产物运行等价、普通用户无感知。它可以作为 MCP 工具由 AI 编程智能体直接调用，完成审计、加固与校验这一具体任务。

### 主要功能

- 提供 MCP 服务（31 个防御工具）与 CLI，可被 Claude Code、Cursor、Codex、Windsurf、Gemini CLI、GitHub Copilot CLI 等编程智能体编排，按 `bla_weave_plan` → `bla_encrypt_strings` → `bla_bind_scope` → `bla_verify_weave` → `bla_harden` → `bla_verify` 流程完成源码与产物加固。
- 核心流程为审计 → 保护 → 校验：`npx bla-agents harden .` 生成加固镜像，`--apply` 替换构建产物，`--restore` 还原；另有 `audit`、`lint`、`defend` 子命令。
- 内置 26 种格式防护，覆盖 JS/TS、Electron ASAR、WASM、Python、原生 ELF/Mach-O/PE、SQLite、GGUF/Safetensors、Android DEX、Go buildinfo、Erlang BEAM、EVM、PCAP 等格式，不依赖外部加壳工具。
- 采用投毒（合法诱饵元数据与影子逻辑）、耗尽（触发分析器资源上限）、自封与运行时诱骗等机制；官方以真实 REA 对 14 个样本做了红队验证并附录报告。
- 提供 Vite/Rollup/Webpack/esbuild 打包插件，可在打包阶段自动加固；MIT 许可。

### 环境要求

- 推荐 Node.js ^22.23.4 或 >=24.0.0，通过 `npx bla-agents` 运行 CLI。
- 若由 AI 编程智能体调用，需要支持 MCP 的客户端（Claude Code、Cursor、Codex、Windsurf、Gemini CLI、GitHub Copilot CLI、VS Code、OpenCode 等）。
- 复现红队测试还需本地原生工具（Wabt、tshark 等），缺失时相关探针会被跳过。

### 使用限制

- 官方明确声明仅用于防御自己的知识产权；不防 Ghidra、IDA、Frida 等人工交互式逆向。
- 防护有保质期：REA 可调高默认预算（如 `asar.max_header_bytes` 最高 256 MiB），对应耗尽策略可能失效；加固会带来包体积膨胀与冷启动解析开销。
- 固件、CUDA、SPIR-V、完整 APK 动态脱壳等场景官方标注未验证。
- `--llm-directives` 默认关闭，属高风险红队功能，业务保护不要开启；默认最高强度档位为 `bankrupt`。
- 本次为文档复核，未安装或运行上游项目。

### 开始使用

1. 按官方 README 安装并注册 MCP 技能：`npx bla-agents setup`，随后在编程智能体中提示「Harden my software against REA」。
2. 先构建项目，再执行 `npx bla-agents harden .` 查看加固镜像，确认后用 `--apply` 替换构建产物，并以自身测试验证。
3. 需要 CI 门禁时使用 `npx bla-agents lint .`，或在 Vite 配置中加入 `blaVitePlugin({ intensity: "bankrupt", enableHoneySourceMaps: true })`。

### 收录与来源

AI 任务用途已依据官方 README 核对：BLA 以 MCP 工具与 CLI 形式被 AI 编程智能体调用，完成软件审计与加固这一具体任务。Star 为 2026-11-19T16:00:58.096476Z 的快照（6188），达到总量 ≥1,000 条件。近期活动：[2026-11-19 · commit](https://github.com/qybaihe/bla/commit/1d4d490f4d98f384f50a11622759cd7d6f8fd357)。本次为文档复核，未安装或运行上游项目；该提交只证明窗口内活动，不代表运行验证。许可不作为准入条件。

- [Official README](https://github.com/qybaihe/bla/blob/main/README.md)
- [中文 README](https://github.com/qybaihe/bla/blob/main/docs/readme/README_zh.md)
- [GitHub API](https://api.github.com/repos/qybaihe/bla)
- [官方网站](https://bla.tools)

## English

BLA (Blind LLM Agents, package `bla-agents`) is an open-source blue-team defense tool that helps software authors protect their own release artifacts against AI reverse-engineering agents such as REA. It uses poison, exhaustion and hallucination techniques to raise the compute and token cost of automated AI reverse engineering while keeping artifacts runtime-equivalent and transparent to normal users. It can be invoked directly by AI coding agents as an MCP tool to audit, harden and verify software — a concrete AI task.

### Features

- Provides an MCP server (31 defense tools) and a CLI that can be orchestrated by coding agents (Claude Code, Cursor, Codex, Windsurf, Gemini CLI, GitHub Copilot CLI, etc.) through the flow `bla_weave_plan` → `bla_encrypt_strings` → `bla_bind_scope` → `bla_verify_weave` → `bla_harden` → `bla_verify`.
- Core workflow is audit → protect → verify: `npx bla-agents harden .` writes a partial mirror, `--apply` replaces build output, `--restore` reverts; `audit`, `lint` and `defend` subcommands are also available.
- Ships 26 format shields with no external packer dependency, covering JS/TS, Electron ASAR, WASM, Python, native ELF/Mach-O/PE, SQLite, GGUF/Safetensors, Android DEX, Go buildinfo, Erlang BEAM, EVM, PCAP and more.
- Uses poisoning (format-valid decoys and shadow logic), budget exhaustion, self-sealing and runtime deception; the maintainers ran a red-team validation against real REA on 14 samples with a published report.
- Offers Vite/Rollup/Webpack/esbuild bundler plugins for build-time hardening; MIT licensed.

### Requirements

- Node.js ^22.23.4 or >=24.0.0 is recommended; run the CLI via `npx bla-agents`.
- Agent-driven use requires an MCP-capable client (Claude Code, Cursor, Codex, Windsurf, Gemini CLI, GitHub Copilot CLI, VS Code, OpenCode, etc.).
- Reproducing the red-team suite additionally needs local native tools (Wabt, tshark, etc.); missing tools cause the related probes to be skipped.

### Limitations

- The project states defensive use only, protecting your own intellectual property; it does not stop human interactive reverse engineering with Ghidra, IDA or Frida.
- Protection has a shelf life: REA can raise default budgets (e.g. `asar.max_header_bytes` up to 256 MiB), so the matching exhaustion strategy may stop working; hardening also increases artifact size and cold-start parsing overhead.
- Firmware, CUDA, SPIR-V and full APK dynamic unpacking are explicitly marked unverified by the maintainers.
- `--llm-directives` is off by default and is a high-risk red-team feature not meant for business protection; the default highest intensity is `bankrupt`.
- This is a documentation review; the upstream software was not installed or run.

### Getting started

1. Install and register the MCP skill per the official README: `npx bla-agents setup`, then prompt your coding agent「Harden my software against REA」.
2. Build your project first, run `npx bla-agents harden .` to inspect the mirror, then use `--apply` to replace build output and validate with your own tests.
3. For CI gates use `npx bla-agents lint .`, or add `blaVitePlugin({ intensity: "bankrupt", enableHoneySourceMaps: true })` to a Vite config.

### Review and sources

AI task use was reviewed from the official README: BLA is invoked by AI coding agents as an MCP tool/CLI to perform the concrete task of software auditing and hardening. The Star snapshot at 2026-11-19T16:00:58.096476Z is 6188, meeting the total-Star threshold of 1,000. Recent activity: [2026-11-19 · commit](https://github.com/qybaihe/bla/commit/1d4d490f4d98f384f50a11622759cd7d6f8fd357). This is a documentation review; the upstream software was not installed or run, and the cited commit only establishes activity within the window. Licensing is not an admission criterion.

- [Official README](https://github.com/qybaihe/bla/blob/main/README.md)
- [中文 README](https://github.com/qybaihe/bla/blob/main/docs/readme/README_zh.md)
- [GitHub API](https://api.github.com/repos/qybaihe/bla)
- [官方网站](https://bla.tools)

## Review evidence

本次依据公开文章和 GitHub 官方文档复核，未安装或运行上游项目。

Reviewed against public articles and official GitHub documentation; upstream software was not installed or run.

- [GitHub activity](https://github.com/qybaihe/bla/commit/1d4d490f4d98f384f50a11622759cd7d6f8fd357) (2026-11-19T06:41:33Z)
- [Discovery article](https://mp.weixin.qq.com/s?__biz=MzIyOTY1ODAzNQ==&mid=2247489303&idx=1&sn=8176e6a08d9243722b78d8d4e710a7a9&chksm=e8be0bcbdfc982dd09ead72e76c1e0901ff56dd5d0ed831db09e4c16232817b862028373c71a)

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-19T16:00:58.096476Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "bla",
    "name": "BLA (Blind LLM Agents)",
    "repository": "qybaihe/bla",
    "repo_node_id": "R_kgDOVWezCw",
    "category": "development",
    "summary": {
      "zh-CN": "以 MCP 服务与 CLI 形式供 AI 编程智能体调用，加固软件发布产物以抵御 REA 等 AI 逆向工程 Agent。",
      "en": "MCP server and CLI that lets AI coding agents harden software releases against AI reverse-engineering agents."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-19T16:00:58.096476Z",
        "en": "2026-11-19T16:00:58.096476Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "以 MCP 服务与 CLI 形式供 AI 编程智能体调用，加固软件发布产物以抵御 REA 等 AI 逆向工程 Agent。",
        "en": "MCP server and CLI that lets AI coding agents harden software releases against AI reverse-engineering agents."
      },
      "source_url": "https://github.com/qybaihe/bla/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/qybaihe/bla/commit/1d4d490f4d98f384f50a11622759cd7d6f8fd357",
        "occurred_at": "2026-11-19T06:41:33Z",
        "reviewed_at": "2026-11-19T16:00:58.096476Z",
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
        "url": "https://github.com/qybaihe/bla/blob/main/README.md"
      },
      {
        "title": "Discovery article",
        "url": "https://mp.weixin.qq.com/s?__biz=MzIyOTY1ODAzNQ==&mid=2247489303&idx=1&sn=8176e6a08d9243722b78d8d4e710a7a9&chksm=e8be0bcbdfc982dd09ead72e76c1e0901ff56dd5d0ed831db09e4c16232817b862028373c71a"
      }
    ]
  },
  "snapshot": {
    "full_name": "qybaihe/bla",
    "repo_node_id": "R_kgDOVWezCw",
    "stargazers_count": 6188,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-19T16:00:58.096476Z",
    "source_url": "https://api.github.com/repos/qybaihe/bla"
  }
}
```

</details>
