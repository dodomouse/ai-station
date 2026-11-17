# TokenEconomizer

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[microsoft/TokenEconomizer](https://github.com/microsoft/TokenEconomizer)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 7272 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T06:06:21.893655+00:00 |

## 中文

为编程智能体复用仓库经验、裁剪少用工具并识别失败循环，记录包含插件自身模型调用的会话成本。

### 用途与功能

- 可选微技能从反复失败与会话摘要中学习仓库事实，经后续会话验证后注入上下文；该功能默认关闭，envfacts 模式无需额外模型调用。
- 根据使用记录裁剪工具定义，减少后续请求携带的工具上下文；Claude Code、Codex 和 Copilot CLI 的裁剪粒度分别为工具、能力包和 MCP 服务器，可查看提案并恢复。
- 循环守卫结合成功回合基线、重复失败信号和模型判断给出改换思路的提示，同时记录自身开销；它不会强制停止智能体。

### 环境与限制

需要 Python 3.10+、已配置的兼容编程智能体及其登录或模型服务；各宿主能力不同，Pi 不支持工具裁剪，其他多项适配仍为实验性。状态保存在本地 ~/.tokeneconomizer，但默认循环判断和重定向、可选事实提议会通过宿主 CLI 调用模型并占用其配额或产生费用，传入的摘要可含命令片段、文件名和错误信息，因此不能视为完全离线。可选 macOS 本地模型路由失败时仍会回退到宿主模型。

### 开始使用

按官方 plugin/README.md 中对应宿主的步骤安装，保留插件所引用的源码目录，再通过 status 与 doctor 检查连接、状态和成本。Claude Code 与 Copilot CLI 先刷新工具目录；若希望逐项审阅裁剪，可把 toolprune 设为 propose。先积累真实会话，再按需启用 microskills，并对比任务完成情况与包含插件开销的成本。

参阅[官方 README](https://github.com/microsoft/TokenEconomizer/blob/fb853981ef439db813bf96ec42eaa82822962e1e/README.md)。

### 收录与来源

具体价值是把编程会话经验和工具使用记录用于减少后续上下文与重复尝试，不需要训练模型。已核对配置默认值、工具裁剪与模型调用源码，以及错误类型返回值的实际修复补丁；未安装或执行上游。节省幅度和任务准确性取决于仓库、模型、缓存与工作负载，裁剪或错误经验可能影响结果，额外判断也可能增加成本，不能把作者基准等同于普遍效果保证。

维护证据：[为微技能提议返回值增加字段类型校验，丢弃无效 extractor、fact、detector 和 cite 数据，避免提炼过程因异常模型输出崩溃，并新增相应回归测试](https://github.com/microsoft/TokenEconomizer/commit/edde289e3017e1643d71fa84714ed55981cb7b8f)（2026-11-16）。

用户于 2026-11-17 提供仓库链接。本条按工程通用标准复核，不设 Star 门槛。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Reuses repository experience, prunes unused tools and detects failure loops for coding agents, with session accounting that includes the plugin’s own model calls.

### Uses and features

- Optional micro-skills learn repository facts from repeated failures and session digests, validate them against later sessions and inject them into context. They are off by default; envfacts mode needs no additional model calls.
- Usage-based pruning reduces tool definitions carried into later requests. Its granularity is individual tools in Claude Code, capability packages in Codex and MCP servers in Copilot CLI, with proposals and restoration available.
- The loop guard combines successful-turn baselines, repeated-failure signals and model judgments to suggest a different approach, while recording its own overhead. It never forcibly stops the agent.

### Requirements and limits

Requires Python 3.10+, a configured compatible coding agent and its login or model service. Capabilities vary by host: Pi has no tool pruning, and several other adapters remain experimental. State is stored locally under ~/.tokeneconomizer, but default loop judgments and redirects, plus optional fact proposals, call models through the host CLI and consume its quota or incur fees. Digests can contain command fragments, file names and errors, so this is not a fully offline workflow. The optional macOS on-device route falls back to the host model if it fails.

### Getting started

Install using the host-specific instructions in plugin/README.md, retain the source directory referenced by the installation, and use status and doctor to inspect connectivity, state and cost. Refresh the tool catalog first for Claude Code and Copilot CLI. Set toolprune to propose to review pruning before applying it. Accumulate real sessions, enable microskills if needed, and compare task completion and costs including plugin overhead.

See the [official README](https://github.com/microsoft/TokenEconomizer/blob/fb853981ef439db813bf96ec42eaa82822962e1e/README.md).

### Review and provenance

Its concrete value is using coding-session experience and tool-usage records to reduce later context and repeated attempts without training a model. This review inspected defaults, pruning and model-call source and an actual fix for wrongly typed model responses; it did not install or execute upstream code. Savings and task accuracy depend on the repository, model, caching and workload. Pruning or incorrect learned facts can affect results, and extra judgments can increase cost; the authors’ benchmarks are not a universal guarantee.

Maintenance evidence: [Adds type checks for micro-skill proposer responses, dropping invalid extractor, fact, detector and cite data to prevent malformed model output from crashing distillation, with regression tests](https://github.com/microsoft/TokenEconomizer/commit/edde289e3017e1643d71fa84714ed55981cb7b8f) (2026-11-16).

Submitted by the user on 2026-11-17 and reviewed against the general catalog criteria, with no star threshold.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T06:06:21.893655+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "token-economizer",
    "name": "TokenEconomizer",
    "repository": "microsoft/TokenEconomizer",
    "repo_node_id": "R_kgDOVG0zYA",
    "category": "development",
    "summary": {
      "zh-CN": "为编程智能体复用仓库经验、裁剪少用工具并识别失败循环，记录包含插件自身模型调用的会话成本。",
      "en": "Reuses repository experience, prunes unused tools and detects failure loops for coding agents, with session accounting that includes the plugin’s own model calls."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T06:06:21.893655+00:00",
        "en": "2026-11-17T06:06:21.893655+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "具体价值是把编程会话经验和工具使用记录用于减少后续上下文与重复尝试，不需要训练模型。已核对配置默认值、工具裁剪与模型调用源码，以及错误类型返回值的实际修复补丁；未安装或执行上游。节省幅度和任务准确性取决于仓库、模型、缓存与工作负载，裁剪或错误经验可能影响结果，额外判断也可能增加成本，不能把作者基准等同于普遍效果保证。",
      "en": "Its concrete value is using coding-session experience and tool-usage records to reduce later context and repeated attempts without training a model. This review inspected defaults, pruning and model-call source and an actual fix for wrongly typed model responses; it did not install or execute upstream code. Savings and task accuracy depend on the repository, model, caching and workload. Pruning or incorrect learned facts can affect results, and extra judgments can increase cost; the authors’ benchmarks are not a universal guarantee.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/microsoft/TokenEconomizer/blob/fb853981ef439db813bf96ec42eaa82822962e1e/LICENSE",
      "license_sha256": "275b4dd619de4e16a017b10d0beec72abbbbf14ee8a2fc68f8bdb398e821f623",
      "source_commit": "fb853981ef439db813bf96ec42eaa82822962e1e",
      "reviewed_at": "2026-11-17T06:06:21.893655+00:00",
      "evidence_pinned_at": "2026-11-17T06:06:21.893655+00:00",
      "evidence_status": "hash_matched",
      "scope_note": {
        "zh-CN": "固定版本根 LICENSE 为 MIT，覆盖仓库源码；README 顶部遗留 Apache-2.0 徽章与当前许可原文不一致，应以已核对的 MIT 原文为准。许可不包含宿主智能体、模型订阅或外部服务。",
        "en": "The pinned root LICENSE is MIT and covers repository source. The README’s remaining Apache-2.0 badge disagrees with the current license text; this assessment follows the verified MIT text. Host agents, model subscriptions and external services have separate terms."
      }
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-16T04:23:12Z",
        "reviewed_at": "2026-11-17T06:06:21.893655+00:00",
        "url": "https://github.com/microsoft/TokenEconomizer/commit/edde289e3017e1643d71fa84714ed55981cb7b8f",
        "qualifies": true,
        "reason": {
          "zh-CN": "为微技能提议返回值增加字段类型校验，丢弃无效 extractor、fact、detector 和 cite 数据，避免提炼过程因异常模型输出崩溃，并新增相应回归测试",
          "en": "Adds type checks for micro-skill proposer responses, dropping invalid extractor, fact, detector and cite data to prevent malformed model output from crashing distillation, with regression tests"
        },
        "reviewed_files": [
          "tokeneconomizer/microskills/distiller.py",
          "tests/test_distiller_payload_types.py"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/microsoft/TokenEconomizer",
        "accessed_at": "2026-11-17T06:06:21.893655+00:00"
      },
      {
        "url": "https://github.com/microsoft/TokenEconomizer/blob/fb853981ef439db813bf96ec42eaa82822962e1e/README.md",
        "accessed_at": "2026-11-17T06:06:21.893655+00:00"
      },
      {
        "url": "https://github.com/microsoft/TokenEconomizer/blob/fb853981ef439db813bf96ec42eaa82822962e1e/LICENSE",
        "accessed_at": "2026-11-17T06:06:21.893655+00:00"
      },
      {
        "url": "https://github.com/microsoft/TokenEconomizer/commit/edde289e3017e1643d71fa84714ed55981cb7b8f",
        "accessed_at": "2026-11-17T06:06:21.893655+00:00"
      }
    ],
    "discovery": {
      "kind": "user_submission",
      "submitted_date": "2026-11-17",
      "source_url": "https://github.com/microsoft/TokenEconomizer",
      "repository_url": "https://github.com/microsoft/TokenEconomizer"
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVG0zYA",
    "full_name": "microsoft/TokenEconomizer",
    "stargazers_count": 7272,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "api_license_spdx": "MIT",
    "license_sha256": "275b4dd619de4e16a017b10d0beec72abbbbf14ee8a2fc68f8bdb398e821f623",
    "last_success_at": "2026-11-17T05:53:15.917762+00:00"
  }
}
```

</details>
