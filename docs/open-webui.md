# Open WebUI

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[open-webui/open-webui](https://github.com/open-webui/open-webui)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 158918 |
| 评估时间 / Evaluated at | 2026-11-17T14:28:37.557894Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:26.634Z |

## 中文

可自行部署的 AI 网页界面，连接本地模型和兼容 API 的模型服务。

提供统一的模型交互入口，便于把对话、资料和相关工具用于 AI 任务。

### 主要功能

- 连接 Ollama 与 OpenAI 兼容接口。
- 提供 Python、Docker 和独立桌面应用入口。
- 通过配套项目扩展终端操作、知识库同步和计算机交互。

### 环境要求

- README 的 pip 安装方式使用 Python 3.12；也可使用 Docker。
- 需要配置可访问的模型服务；本地推理还需相应模型与计算资源。

### 使用限制

- 离线使用取决于模型、依赖和服务是否已在本地准备好。
- 终端操作和计算机交互来自配套项目，需要单独部署或配置。

### 开始使用

1. 在 Python 3.12 环境中运行 `pip install open-webui`。
2. 运行 `open-webui serve`，打开 `http://localhost:8080`。
3. 按[官方文档](https://docs.openwebui.com/getting-started/)连接 Ollama 或兼容接口，并测试对话。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:26.634Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-08 · commit](https://github.com/open-webui/open-webui/commit/b0e6098e940942281d9c83f3529ea117287a3a22)。将开发分支的 PR 合并到主分支。

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://raw.githubusercontent.com/open-webui/open-webui/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/open-webui/open-webui)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

A self-hosted AI web interface for local models and services with compatible APIs.

It provides a common interface for model interaction, bringing conversations, documents, and related tools into AI tasks.

### Features

- Connect Ollama and OpenAI-compatible endpoints.
- Offer Python, Docker, and a separate desktop application as entry points.
- Extend terminal actions, knowledge-base synchronization, and computer interaction through companion projects.

### Requirements

- The README's pip installation uses Python 3.12; Docker is another option.
- Requires an accessible model service; local inference also needs model files and computing resources.

### Limitations

- Offline use depends on preparing models, dependencies, and services locally.
- Terminal actions and computer interaction come from companion projects and require separate deployment or configuration.

### Getting started

1. Run `pip install open-webui` in a Python 3.12 environment.
2. Run `open-webui serve` and open `http://localhost:8080`.
3. Connect Ollama or a compatible endpoint using the [official documentation](https://docs.openwebui.com/getting-started/) and test a conversation.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:26.634Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-08 · commit](https://github.com/open-webui/open-webui/commit/b0e6098e940942281d9c83f3529ea117287a3a22).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://raw.githubusercontent.com/open-webui/open-webui/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/open-webui/open-webui)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:28:37.557894Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "open-webui",
    "name": "Open WebUI",
    "repository": "open-webui/open-webui",
    "repo_node_id": "R_kgDOKdDCcw",
    "category": "ai",
    "summary": {
      "zh-CN": "可自行部署的 AI 网页界面，连接本地模型和兼容 API 的模型服务。",
      "en": "A self-hosted AI web interface for local models and services with compatible APIs."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:28:37.557894Z",
        "en": "2026-11-17T14:28:37.557894Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "提供统一的模型交互入口，便于把对话、资料和相关工具用于 AI 任务。",
        "en": "It provides a common interface for model interaction, bringing conversations, documents, and related tools into AI tasks."
      },
      "source_url": "https://raw.githubusercontent.com/open-webui/open-webui/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/open-webui/open-webui/commit/b0e6098e940942281d9c83f3529ea117287a3a22",
        "occurred_at": "2026-11-08T23:48:12Z",
        "reviewed_at": "2026-11-17T14:28:37.557894Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "将开发分支的 PR 合并到主分支。 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://raw.githubusercontent.com/open-webui/open-webui/main/README.md"
      },
      {
        "title": "GitHub 仓库元数据 / Repository metadata",
        "url": "https://api.github.com/repos/open-webui/open-webui"
      }
    ]
  },
  "snapshot": {
    "full_name": "open-webui/open-webui",
    "repo_node_id": "R_kgDOKdDCcw",
    "stargazers_count": 158918,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:26.634Z",
    "source_url": "https://api.github.com/repos/open-webui/open-webui"
  }
}
```

</details>
