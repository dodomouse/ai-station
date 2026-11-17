# Promptfoo

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[promptfoo/promptfoo](https://github.com/promptfoo/promptfoo)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 27370 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:53.150038Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:39.234Z |

## 中文

用配置和命令行比较提示与模型，执行评测、红队测试和 CI 检查。

验证 AI 的回答与工具流程是否达到预期，把回归用例和安全测试纳入开发流程。

### 主要功能

- 批量比较提示、模型和输出结果。
- 执行红队测试与漏洞扫描。
- 在 CI/CD 中自动运行评测。

### 环境要求

- 按官方安装方式准备 CLI；可使用 npm、Homebrew 或 pip 入口。
- 多数模型供应商需要访问凭据；本地模型需运行相应服务。

### 使用限制

- 调用远程供应商时，评测输入仍会发送给该服务。
- 红队与自动评分只覆盖配置的场景，不能证明应用没有其他问题。

### 开始使用

1. 按[入门指南](https://www.promptfoo.dev/docs/getting-started/)安装并创建评测。
2. 配置模型、提示、测试输入和断言。
3. 运行评测；需要安全测试时阅读[红队指南](https://www.promptfoo.dev/docs/red-team/)。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:39.234Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/promptfoo/promptfoo/commit/9a7187a33b53277295151cc20d24cf96fa0d5cfb)。fix(redteam): isolate live config files for concurrent runs (#12457)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://github.com/promptfoo/promptfoo/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/promptfoo/promptfoo)
- [入门指南 / getting-started guide](https://www.promptfoo.dev/docs/getting-started/)
- [红队指南 / red-team guide](https://www.promptfoo.dev/docs/red-team/)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

Compares prompts and models through configuration-driven evaluations, red-team tests and CI checks.

Checks whether AI responses and tool workflows meet expectations and adds regression tests to development.

### Features

- Compare prompts, models and outputs in batches.
- Run red-team tests and vulnerability scans.
- Run evaluations automatically in CI/CD.

### Requirements

- Prepare the CLI using an official installation route: npm, Homebrew or pip.
- Most model providers require credentials; local models need their corresponding service.

### Limitations

- Evaluation inputs still go to the provider when using a remote model service.
- Red-team tests and automated scores cover configured scenarios; they do not prove the absence of other issues.

### Getting started

1. Install and create an evaluation using the [getting-started guide](https://www.promptfoo.dev/docs/getting-started/).
2. Configure models, prompts, test inputs and assertions.
3. Run evaluations; use the [red-team guide](https://www.promptfoo.dev/docs/red-team/) for security tests.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:39.234Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/promptfoo/promptfoo/commit/9a7187a33b53277295151cc20d24cf96fa0d5cfb).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://github.com/promptfoo/promptfoo/blob/main/README.md)
- [GitHub 元数据 / GitHub metadata](https://api.github.com/repos/promptfoo/promptfoo)
- [入门指南 / getting-started guide](https://www.promptfoo.dev/docs/getting-started/)
- [红队指南 / red-team guide](https://www.promptfoo.dev/docs/red-team/)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:53.150038Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "promptfoo",
    "name": "Promptfoo",
    "repository": "promptfoo/promptfoo",
    "repo_node_id": "R_kgDOJcj3uQ",
    "category": "development",
    "summary": {
      "zh-CN": "用配置和命令行比较提示与模型，执行评测、红队测试和 CI 检查。",
      "en": "Compares prompts and models through configuration-driven evaluations, red-team tests and CI checks."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:53.150038Z",
        "en": "2026-11-17T14:24:53.150038Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "验证 AI 的回答与工具流程是否达到预期，把回归用例和安全测试纳入开发流程。",
        "en": "Checks whether AI responses and tool workflows meet expectations and adds regression tests to development."
      },
      "source_url": "https://github.com/promptfoo/promptfoo/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/promptfoo/promptfoo/commit/9a7187a33b53277295151cc20d24cf96fa0d5cfb",
        "occurred_at": "2026-11-17T00:21:31Z",
        "reviewed_at": "2026-11-17T14:24:53.150038Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "fix(redteam): isolate live config files for concurrent runs (#12457) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://github.com/promptfoo/promptfoo/blob/main/README.md"
      },
      {
        "title": "GitHub 元数据 / GitHub metadata",
        "url": "https://api.github.com/repos/promptfoo/promptfoo"
      },
      {
        "title": "入门指南 / getting-started guide",
        "url": "https://www.promptfoo.dev/docs/getting-started/"
      },
      {
        "title": "红队指南 / red-team guide",
        "url": "https://www.promptfoo.dev/docs/red-team/"
      }
    ]
  },
  "snapshot": {
    "full_name": "promptfoo/promptfoo",
    "repo_node_id": "R_kgDOJcj3uQ",
    "stargazers_count": 27370,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:39.234Z",
    "source_url": "https://api.github.com/repos/promptfoo/promptfoo"
  }
}
```

</details>
