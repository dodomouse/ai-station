# InvokeAI

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[invoke-ai/InvokeAI](https://github.com/invoke-ai/InvokeAI)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 29105 |
| 评估时间 / Evaluated at | 2026-11-17T14:28:37.558215Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:26.080Z |

## 中文

面向图像创作的本地 AI 应用，结合画布编辑、节点工作流和模型管理。

把生成、局部修改和后处理放在同一工作区，便于反复调整 AI 图像并复用流程。

### 主要功能

- 统一画布支持局部重绘、扩图和笔刷工具。
- 节点工作流可组合、保存和分享生成流程。
- 图库保存图像及生成参数，并提供模型管理、放大和对象选择工具。

### 环境要求

- 官方 Launcher 提供 Windows、macOS 和 Linux 安装入口。
- 应按所选模型核对硬件要求，并准备模型存储空间。

### 使用限制

- 不同模型的设备和内存要求不同，安装应用不代表能运行全部模型。
- README 中部分模型仅通过 API 提供，需要外部服务连接。

### 开始使用

1. 按[官方安装指南](https://invoke.ai/start-here/installation/)下载适合系统的 Launcher。
2. 启动 Launcher，选择 Install，并完成应用安装。
3. 启动工作区，配置一个支持的模型，在画布中生成并修改一张测试图像。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:26.080Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/invoke-ai/InvokeAI/commit/471bb0f4de2d09efcdfe5d4e0326c1c1ee593f87)。优化 GGUF 文件探测的内存回收行为，并清理无效测试。

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://raw.githubusercontent.com/invoke-ai/InvokeAI/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/invoke-ai/InvokeAI)
- [官方安装指南 / Official installation guide](https://invoke.ai/start-here/installation/)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## English

A local AI application for image creation, combining canvas editing, node workflows, and model management.

It brings generation, local edits, and post-processing into one workspace for iterative image work and reusable AI workflows.

### Features

- The unified canvas supports inpainting, outpainting, and brush tools.
- Node workflows can compose, save, and share generation processes.
- The gallery retains images and generation settings, alongside model management, upscaling, and object selection tools.

### Requirements

- The official Launcher provides installation routes for Windows, macOS, and Linux.
- Check hardware requirements for the selected models and provide storage for their files.

### Limitations

- Device and memory requirements differ by model; installing the app does not make every model runnable.
- Some models listed in the README are API-only and require external service connections.

### Getting started

1. Download the Launcher for your system using the [official installation guide](https://invoke.ai/start-here/installation/).
2. Open the Launcher, select Install, and complete the application installation.
3. Launch the workspace, configure a supported model, and generate and edit a test image on the canvas.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:26.080Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/invoke-ai/InvokeAI/commit/471bb0f4de2d09efcdfe5d4e0326c1c1ee593f87).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://raw.githubusercontent.com/invoke-ai/InvokeAI/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/invoke-ai/InvokeAI)
- [官方安装指南 / Official installation guide](https://invoke.ai/start-here/installation/)

[筛选记录 / Discovery record](../reviews/2026-11-17-ai-repository-shortlist.md)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:28:37.558215Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "invokeai",
    "name": "InvokeAI",
    "repository": "invoke-ai/InvokeAI",
    "repo_node_id": "R_kgDOH1Ppow",
    "category": "media",
    "summary": {
      "zh-CN": "面向图像创作的本地 AI 应用，结合画布编辑、节点工作流和模型管理。",
      "en": "A local AI application for image creation, combining canvas editing, node workflows, and model management."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:28:37.558215Z",
        "en": "2026-11-17T14:28:37.558215Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "把生成、局部修改和后处理放在同一工作区，便于反复调整 AI 图像并复用流程。",
        "en": "It brings generation, local edits, and post-processing into one workspace for iterative image work and reusable AI workflows."
      },
      "source_url": "https://raw.githubusercontent.com/invoke-ai/InvokeAI/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/invoke-ai/InvokeAI/commit/471bb0f4de2d09efcdfe5d4e0326c1c1ee593f87",
        "occurred_at": "2026-11-17T04:05:27Z",
        "reviewed_at": "2026-11-17T14:28:37.558215Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "优化 GGUF 文件探测的内存回收行为，并清理无效测试。 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://raw.githubusercontent.com/invoke-ai/InvokeAI/main/README.md"
      },
      {
        "title": "GitHub 仓库元数据 / Repository metadata",
        "url": "https://api.github.com/repos/invoke-ai/InvokeAI"
      },
      {
        "title": "官方安装指南 / Official installation guide",
        "url": "https://invoke.ai/start-here/installation/"
      }
    ]
  },
  "snapshot": {
    "full_name": "invoke-ai/InvokeAI",
    "repo_node_id": "R_kgDOH1Ppow",
    "stargazers_count": 29105,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:26.080Z",
    "source_url": "https://api.github.com/repos/invoke-ai/InvokeAI"
  }
}
```

</details>
