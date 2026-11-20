# SwarmUI

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[mcmonkeyprojects/SwarmUI](https://github.com/mcmonkeyprojects/SwarmUI)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 4791 |
| 评估时间 / Evaluated at | 2026-11-17T14:28:37.558368Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:26.614Z |

## 中文

为图像、视频及部分音频生成模型提供可扩展的网页界面。

通过生成面板或 Comfy 工作流运行模型，组织批量对比和图像编辑任务。

### 主要功能

- Generate 面板集中管理生成参数和输出。
- Comfy Workflow 面板可编辑节点图。
- 提供图像编辑、自动工作流生成和参数网格对比工具。

### 环境要求

- Windows、Linux 和 Apple Silicon Mac 有对应安装流程。
- 依平台准备 Git、Python 和 .NET；Linux 推荐 Python 3.11 或 3.12。

### 使用限制

- 当前 README 标为 Beta，部分功能仍在开发。
- macOS 仅支持 Apple Silicon；README 要求不要使用 Python 3.14 或更高版本。
- 原生 LLM 辅助提示词仍列为计划功能，已有扩展不能等同于内置支持。

### 开始使用

1. 按 README 选择系统对应的安装入口。
2. 启动安装程序或脚本，在浏览器中完成后端和模型配置。
3. 按[基础使用指南](https://github.com/mcmonkeyprojects/SwarmUI/blob/master/docs/Basic%20Usage.md)运行一次生成，再用网格工具比较参数。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:26.614Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-12 · commit](https://github.com/mcmonkeyprojects/SwarmUI/commit/d347f3061ce9aa19e0d3950e5189415022de6659)。移除 DirectML 引用。

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://raw.githubusercontent.com/mcmonkeyprojects/SwarmUI/master/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/mcmonkeyprojects/SwarmUI)

## English

An extensible web interface for image, video, and selected audio generation models.

It runs models through a generation panel or Comfy workflows for batch comparisons and image editing tasks.

### Features

- The Generate panel organizes generation settings and outputs.
- The Comfy Workflow panel exposes the node graph.
- Provide image editing, automatic workflow generation, and parameter-grid comparisons.

### Requirements

- Separate installation flows are available for Windows, Linux, and Apple Silicon Macs.
- Prepare Git, Python, and .NET as required by the platform; Linux instructions recommend Python 3.11 or 3.12.

### Limitations

- The current README labels the project as Beta, with some features still under development.
- macOS requires Apple Silicon; the README says not to use Python 3.14 or later.
- Native LLM-assisted prompting remains planned; an available extension is not equivalent to built-in support.

### Getting started

1. Choose the installation route for your operating system in the README.
2. Run its installer or script, then complete backend and model setup in the browser.
3. Run a generation using the [basic usage guide](https://github.com/mcmonkeyprojects/SwarmUI/blob/master/docs/Basic%20Usage.md), then compare settings with the grid tools.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:26.614Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-12 · commit](https://github.com/mcmonkeyprojects/SwarmUI/commit/d347f3061ce9aa19e0d3950e5189415022de6659).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://raw.githubusercontent.com/mcmonkeyprojects/SwarmUI/master/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/mcmonkeyprojects/SwarmUI)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:28:37.558368Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "swarmui",
    "name": "SwarmUI",
    "repository": "mcmonkeyprojects/SwarmUI",
    "repo_node_id": "R_kgDOMMOABQ",
    "category": "media",
    "summary": {
      "zh-CN": "为图像、视频及部分音频生成模型提供可扩展的网页界面。",
      "en": "An extensible web interface for image, video, and selected audio generation models."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:28:37.558368Z",
        "en": "2026-11-17T14:28:37.558368Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "通过生成面板或 Comfy 工作流运行模型，组织批量对比和图像编辑任务。",
        "en": "It runs models through a generation panel or Comfy workflows for batch comparisons and image editing tasks."
      },
      "source_url": "https://raw.githubusercontent.com/mcmonkeyprojects/SwarmUI/master/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/mcmonkeyprojects/SwarmUI/commit/d347f3061ce9aa19e0d3950e5189415022de6659",
        "occurred_at": "2026-11-12T18:08:36Z",
        "reviewed_at": "2026-11-17T14:28:37.558368Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "移除 DirectML 引用。 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://raw.githubusercontent.com/mcmonkeyprojects/SwarmUI/master/README.md"
      },
      {
        "title": "GitHub 仓库元数据 / Repository metadata",
        "url": "https://api.github.com/repos/mcmonkeyprojects/SwarmUI"
      }
    ]
  },
  "snapshot": {
    "full_name": "mcmonkeyprojects/SwarmUI",
    "repo_node_id": "R_kgDOMMOABQ",
    "stargazers_count": 4791,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:26.614Z",
    "source_url": "https://api.github.com/repos/mcmonkeyprojects/SwarmUI"
  }
}
```

</details>
