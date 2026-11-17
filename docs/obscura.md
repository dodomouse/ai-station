# Obscura

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[h4ckf0r0day/obscura](https://github.com/h4ckf0r0day/obscura)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 36016 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-17T06:06:21.870826+00:00 |

## 中文

面向 AI 智能体和网页采集的 Rust 无头浏览器，通过 V8 执行 JavaScript，并提供 CDP 与 MCP 接口。

### 用途与功能

- 用 MCP 获取页面快照与元素引用，执行点击、表单填写和 JavaScript。
- 通过 CDP 连接 Puppeteer 或 Playwright，并用 CLI 导出 HTML、文本、链接和 Markdown。
- 启用渲染的构建可直接生成截图、屏幕流和栅格 PDF；批量采集使用独立工作进程。

### 环境与限制

可使用 Linux、macOS 或 Windows x86_64 发布包；Linux 包要求 glibc 2.35+，Windows 需保留附带 DLL。源码构建需稳定版 Rust，stealth 构建另需 CMake、Clang 和 LLVM/libclang。独立引擎的 CSS、Web API 和字体显示可能与 Chromium 不同；截图及 PDF 需渲染构建，内网地址访问需显式启用。附带字体遵循 SIL OFL，第三方依赖和云服务许可另行适用。

### 开始使用

下载对应平台发布包并保留 obscura 与 obscura-worker，先运行 `obscura fetch https://example.com --dump text`。智能体可将 `obscura mcp` 配为本地 stdio 工具；CDP 客户端通过 `obscura serve --port 9222` 接入。

参阅[官方 README](https://github.com/h4ckf0r0day/obscura/blob/0d9a2f764ffdb097269da048002c593865e83a9e/README.md)。

### 收录与来源

把页面读取、元素操作和可选渲染集中到同一浏览器引擎，便于为智能体提供浏览工具，也可接入已有 CDP 脚本。已核对 MCP 实现及历史导航修复，未运行上游或验证性能。

维护证据：[同步 JavaScript 与浏览器历史条目，并让 CDP 的同文档历史跳转保留运行时和 history.state，避免重新加载页面丢失状态](https://github.com/h4ckf0r0day/obscura/commit/0ecc41770da5c5300227dd83a15bfa1e5100d5d4)（2026-11-13）。

用户于 2026-11-17 提供仓库链接。本条按工程通用标准复核，不设 Star 门槛。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

A Rust headless browser for AI agents and web extraction, with V8 JavaScript execution and CDP and MCP interfaces.

### Uses and features

- Use MCP to obtain page snapshots and element references, click controls, fill forms and execute JavaScript.
- Connect Puppeteer or Playwright over CDP, or export HTML, text, links and Markdown through the CLI.
- Render-enabled builds produce screenshots, screencasts and raster PDFs; batch extraction uses worker processes.

### Requirements and limits

Release archives cover Linux, macOS and Windows x86_64; Linux requires glibc 2.35+, and Windows needs the bundled DLLs. Source builds need stable Rust; stealth builds additionally need CMake, Clang and LLVM/libclang. CSS, Web APIs and font output may differ from Chromium. Screenshots and PDFs require rendering, and private-network access requires explicit opt-in. Bundled fonts use SIL OFL; dependencies and hosted services retain separate terms.

### Getting started

Download the platform archive and keep obscura and obscura-worker together. Start with `obscura fetch https://example.com --dump text`. Agents can launch `obscura mcp` over local stdio; CDP clients connect through `obscura serve --port 9222`.

See the [official README](https://github.com/h4ckf0r0day/obscura/blob/0d9a2f764ffdb097269da048002c593865e83a9e/README.md).

### Review and provenance

Combines page extraction, element interaction and optional rendering in one engine for agent browsing tools and existing CDP scripts. MCP implementation and a history-navigation fix were reviewed; upstream execution and performance were not tested.

Maintenance evidence: [Synchronizes JavaScript and browser history entries and preserves the runtime and history.state during CDP same-document history traversal instead of reloading the document](https://github.com/h4ckf0r0day/obscura/commit/0ecc41770da5c5300227dd83a15bfa1e5100d5d4) (2026-11-13).

Submitted by the user on 2026-11-17 and reviewed against the general catalog criteria, with no star threshold.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T06:06:21.870826+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "obscura",
    "name": "Obscura",
    "repository": "h4ckf0r0day/obscura",
    "repo_node_id": "R_kgDOSBUdsQ",
    "category": "development",
    "summary": {
      "zh-CN": "面向 AI 智能体和网页采集的 Rust 无头浏览器，通过 V8 执行 JavaScript，并提供 CDP 与 MCP 接口。",
      "en": "A Rust headless browser for AI agents and web extraction, with V8 JavaScript execution and CDP and MCP interfaces."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T06:06:21.870826+00:00",
        "en": "2026-11-17T06:06:21.870826+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "把页面读取、元素操作和可选渲染集中到同一浏览器引擎，便于为智能体提供浏览工具，也可接入已有 CDP 脚本。已核对 MCP 实现及历史导航修复，未运行上游或验证性能。",
      "en": "Combines page extraction, element interaction and optional rendering in one engine for agent browsing tools and existing CDP scripts. MCP implementation and a history-navigation fix were reviewed; upstream execution and performance were not tested.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "source_url": "https://github.com/h4ckf0r0day/obscura/blob/0d9a2f764ffdb097269da048002c593865e83a9e/LICENSE",
      "license_sha256": "50e6751797c50dedd75ef1b8a0d9e42f5f8472e9fbce91f34718e9f97b0c780a",
      "source_commit": "0d9a2f764ffdb097269da048002c593865e83a9e",
      "reviewed_at": "2026-11-17T06:06:21.870826+00:00",
      "evidence_pinned_at": "2026-11-17T06:06:21.870826+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "Apache-2.0 covers the project browser software, confirmed by the root LICENSE and workspace Cargo metadata. Vendored dependencies retain their own licenses (reviewed examples: Taffy MIT and wreq-util Apache-2.0); bundled Noto Color Emoji font uses SIL OFL-1.1. The root license does not relicense fetched website content, third-party fonts or hosted services."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-13T20:02:53Z",
        "reviewed_at": "2026-11-17T06:06:21.870826+00:00",
        "url": "https://github.com/h4ckf0r0day/obscura/commit/0ecc41770da5c5300227dd83a15bfa1e5100d5d4",
        "qualifies": true,
        "reason": {
          "zh-CN": "同步 JavaScript 与浏览器历史条目，并让 CDP 的同文档历史跳转保留运行时和 history.state，避免重新加载页面丢失状态",
          "en": "Synchronizes JavaScript and browser history entries and preserves the runtime and history.state during CDP same-document history traversal instead of reloading the document"
        },
        "reviewed_files": [
          "crates/obscura-browser/src/fork_virtual_url.rs",
          "crates/obscura-browser/src/page.rs",
          "crates/obscura-cdp/src/domains/page.rs",
          "crates/obscura-js/js/bootstrap.js",
          "crates/obscura-js/src/runtime.rs"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/h4ckf0r0day/obscura",
        "accessed_at": "2026-11-17T06:06:21.870826+00:00"
      },
      {
        "url": "https://github.com/h4ckf0r0day/obscura/blob/0d9a2f764ffdb097269da048002c593865e83a9e/README.md",
        "accessed_at": "2026-11-17T06:06:21.870826+00:00"
      },
      {
        "url": "https://github.com/h4ckf0r0day/obscura/blob/0d9a2f764ffdb097269da048002c593865e83a9e/LICENSE",
        "accessed_at": "2026-11-17T06:06:21.870826+00:00"
      },
      {
        "url": "https://github.com/h4ckf0r0day/obscura/commit/0ecc41770da5c5300227dd83a15bfa1e5100d5d4",
        "accessed_at": "2026-11-17T06:06:21.870826+00:00"
      },
      {
        "url": "https://github.com/h4ckf0r0day/obscura/blob/0d9a2f764ffdb097269da048002c593865e83a9e/Cargo.toml",
        "accessed_at": "2026-11-17T06:06:21.870826+00:00"
      },
      {
        "url": "https://github.com/h4ckf0r0day/obscura/blob/0d9a2f764ffdb097269da048002c593865e83a9e/crates/obscura-cli/Cargo.toml",
        "accessed_at": "2026-11-17T06:06:21.870826+00:00"
      },
      {
        "url": "https://github.com/h4ckf0r0day/obscura/blob/0d9a2f764ffdb097269da048002c593865e83a9e/docs/Use-the-MCP-server.md",
        "accessed_at": "2026-11-17T06:06:21.870826+00:00"
      },
      {
        "url": "https://github.com/h4ckf0r0day/obscura/blob/0d9a2f764ffdb097269da048002c593865e83a9e/crates/obscura-mcp/src/lib.rs",
        "accessed_at": "2026-11-17T06:06:21.870826+00:00"
      },
      {
        "url": "https://github.com/h4ckf0r0day/obscura/blob/0d9a2f764ffdb097269da048002c593865e83a9e/crates/obscura-render/assets/LICENSE-NOTO-COLOR-EMOJI.txt",
        "accessed_at": "2026-11-17T06:06:21.870826+00:00"
      },
      {
        "url": "https://github.com/h4ckf0r0day/obscura/blob/0d9a2f764ffdb097269da048002c593865e83a9e/vendor/taffy/LICENSE",
        "accessed_at": "2026-11-17T06:06:21.870826+00:00"
      },
      {
        "url": "https://github.com/h4ckf0r0day/obscura/blob/0d9a2f764ffdb097269da048002c593865e83a9e/vendor/wreq-util/LICENSE",
        "accessed_at": "2026-11-17T06:06:21.870826+00:00"
      }
    ],
    "discovery": {
      "kind": "user_submission",
      "submitted_date": "2026-11-17",
      "source_url": "git@github.com:h4ckf0r0day/obscura.git",
      "repository_url": "https://github.com/h4ckf0r0day/obscura"
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOSBUdsQ",
    "full_name": "h4ckf0r0day/obscura",
    "stargazers_count": 36016,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "api_license_spdx": "Apache-2.0",
    "license_sha256": "50e6751797c50dedd75ef1b8a0d9e42f5f8472e9fbce91f34718e9f97b0c780a",
    "last_success_at": "2026-11-17T05:22:01.983551+00:00"
  }
}
```

</details>
