# ComfyUI

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[Comfy-Org/ComfyUI](https://github.com/Comfy-Org/ComfyUI)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 147310 |
| 评估时间 / Evaluated at | 2026-11-17T14:28:37.558063Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:25.898Z |

## 中文

用节点图构建和复用图像、视频、音频及其他生成式 AI 工作流。

将模型加载、生成和后处理组织成可重复执行的流程，也可通过本地 API 接入应用。

### 主要功能

- 可视化连接节点，保存模板并复用子图。
- 提供执行队列、局部重算和模型卸载。
- 支持多种生成模型，以及 App Mode 和本地 API。

### 环境要求

- 桌面版支持 Windows 和 macOS；其他安装方式按硬件选择依赖。
- 需要工作流指定的模型文件；手动安装还需匹配 Python、PyTorch 和设备环境。

### 使用限制

- 应按工作流核对模型所需的内存和计算资源。
- 第三方节点有各自依赖；云端或外部模型服务可能需要账号和付费。

### 开始使用

1. 从[官方下载页](https://www.comfy.org/download)安装桌面版，或按 README 选择手动安装。
2. 从[工作流库](https://comfy.org/workflows)选择模板，并准备其模型和节点。
3. 填写输入后加入执行队列，检查输出，再保存工作流供重复使用。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:25.898Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/Comfy-Org/ComfyUI/commit/ee34406f56f84f6bc89996b8b77a4bedec98a2b9)。合并对前一个 PR 的清理提交。

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://raw.githubusercontent.com/Comfy-Org/ComfyUI/master/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/Comfy-Org/ComfyUI)

## English

Build and reuse generative AI workflows for images, video, audio, and other media through node graphs.

It organizes model loading, generation, and post-processing into repeatable workflows that applications can call through a local API.

### Features

- Connect nodes visually, save templates, and reuse subgraphs.
- Provide execution queues, partial recomputation, and model offloading.
- Support multiple generative models, App Mode, and a local API.

### Requirements

- The desktop app supports Windows and macOS; other installation routes require hardware-specific dependencies.
- Requires the model files referenced by a workflow; manual installation also needs compatible Python, PyTorch, and device support.

### Limitations

- Check the memory and computing resources required by the models in each workflow.
- Third-party nodes have their own dependencies; cloud or external model services may require accounts and payment.

### Getting started

1. Install the desktop app from the [official download page](https://www.comfy.org/download), or choose manual installation in the README.
2. Select a template from the [workflow library](https://comfy.org/workflows) and prepare its models and nodes.
3. Supply the inputs, queue execution, inspect the outputs, and save the workflow for reuse.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:25.898Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/Comfy-Org/ComfyUI/commit/ee34406f56f84f6bc89996b8b77a4bedec98a2b9).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://raw.githubusercontent.com/Comfy-Org/ComfyUI/master/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/Comfy-Org/ComfyUI)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:28:37.558063Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "comfyui",
    "name": "ComfyUI",
    "repository": "Comfy-Org/ComfyUI",
    "repo_node_id": "R_kgDOIygeJg",
    "category": "media",
    "summary": {
      "zh-CN": "用节点图构建和复用图像、视频、音频及其他生成式 AI 工作流。",
      "en": "Build and reuse generative AI workflows for images, video, audio, and other media through node graphs."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:28:37.558063Z",
        "en": "2026-11-17T14:28:37.558063Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "将模型加载、生成和后处理组织成可重复执行的流程，也可通过本地 API 接入应用。",
        "en": "It organizes model loading, generation, and post-processing into repeatable workflows that applications can call through a local API."
      },
      "source_url": "https://raw.githubusercontent.com/Comfy-Org/ComfyUI/master/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/Comfy-Org/ComfyUI/commit/ee34406f56f84f6bc89996b8b77a4bedec98a2b9",
        "occurred_at": "2026-11-17T05:22:29Z",
        "reviewed_at": "2026-11-17T14:28:37.558063Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "合并对前一个 PR 的清理提交。 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://raw.githubusercontent.com/Comfy-Org/ComfyUI/master/README.md"
      },
      {
        "title": "GitHub 仓库元数据 / Repository metadata",
        "url": "https://api.github.com/repos/Comfy-Org/ComfyUI"
      }
    ]
  },
  "snapshot": {
    "full_name": "Comfy-Org/ComfyUI",
    "repo_node_id": "R_kgDOIygeJg",
    "stargazers_count": 147310,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:25.898Z",
    "source_url": "https://api.github.com/repos/Comfy-Org/ComfyUI"
  }
}
```

</details>
