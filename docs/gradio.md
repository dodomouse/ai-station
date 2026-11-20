# Gradio

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[gradio-app/gradio](https://github.com/gradio-app/gradio)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 已收录 / Included |
| Star | 44073 |
| 评估时间 / Evaluated at | 2026-11-17T14:28:37.557556Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:26.034Z |

## 中文

用 Python 为模型、API 或函数构建可交互的网页界面。

将 AI 推理封装成可操作的演示或应用，便于测试输入、比较输出并共享结果。

### 主要功能

- 用 `Interface` 为函数配置输入和输出组件。
- 用 `Blocks` 组合布局，用 `ChatInterface` 构建聊天界面。
- 支持本地运行、开发重载和共享链接。

### 环境要求

- 需要 Python 3.10 或更高版本，建议使用虚拟环境。
- 模型及其计算资源由应用另行提供。

### 使用限制

- 共享链接仍依赖运行应用的计算环境，不等于持久化部署。
- 公开共享会让其他人访问应用，应按实际用途配置访问方式。

### 开始使用

1. 运行 `pip install --upgrade gradio`。
2. 将官方首个示例保存为 `app.py`，按需要替换处理函数。
3. 运行 `python app.py`，在浏览器中检查输入、输出和错误反馈。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:26.034Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-13 · commit](https://github.com/gradio-app/gradio/commit/ec06278ed72e5eb73494a9d171ca851d553dc82a)。更新工作流中的嵌入式推理配置。

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://raw.githubusercontent.com/gradio-app/gradio/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/gradio-app/gradio)

## English

Build interactive web interfaces for models, APIs, or functions using Python.

It turns AI inference into an interactive demo or application for testing inputs, comparing outputs, and sharing results.

### Features

- Configure function inputs and outputs with `Interface`.
- Compose layouts with `Blocks` and build chat interfaces with `ChatInterface`.
- Support local execution, development reloads, and share links.

### Requirements

- Requires Python 3.10 or later; a virtual environment is recommended.
- The application must provide its model and computing resources separately.

### Limitations

- A share link still depends on the environment running the application; it is not a persistent deployment.
- Public sharing exposes the application to other users, so access should be configured for the intended use.

### Getting started

1. Run `pip install --upgrade gradio`.
2. Save the official first-demo example as `app.py` and replace its processing function as needed.
3. Run `python app.py` and inspect inputs, outputs, and error feedback in the browser.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:26.034Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-13 · commit](https://github.com/gradio-app/gradio/commit/ec06278ed72e5eb73494a9d171ca851d553dc82a).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://raw.githubusercontent.com/gradio-app/gradio/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/gradio-app/gradio)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:28:37.557556Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "gradio",
    "name": "Gradio",
    "repository": "gradio-app/gradio",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkxNjI0MDU5NjM=",
    "category": "development",
    "summary": {
      "zh-CN": "用 Python 为模型、API 或函数构建可交互的网页界面。",
      "en": "Build interactive web interfaces for models, APIs, or functions using Python."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:28:37.557556Z",
        "en": "2026-11-17T14:28:37.557556Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "将 AI 推理封装成可操作的演示或应用，便于测试输入、比较输出并共享结果。",
        "en": "It turns AI inference into an interactive demo or application for testing inputs, comparing outputs, and sharing results."
      },
      "source_url": "https://raw.githubusercontent.com/gradio-app/gradio/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/gradio-app/gradio/commit/ec06278ed72e5eb73494a9d171ca851d553dc82a",
        "occurred_at": "2026-11-13T18:01:54Z",
        "reviewed_at": "2026-11-17T14:28:37.557556Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "更新工作流中的嵌入式推理配置。 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://raw.githubusercontent.com/gradio-app/gradio/main/README.md"
      },
      {
        "title": "GitHub 仓库元数据 / Repository metadata",
        "url": "https://api.github.com/repos/gradio-app/gradio"
      }
    ]
  },
  "snapshot": {
    "full_name": "gradio-app/gradio",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkxNjI0MDU5NjM=",
    "stargazers_count": 44073,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:26.034Z",
    "source_url": "https://api.github.com/repos/gradio-app/gradio"
  }
}
```

</details>
