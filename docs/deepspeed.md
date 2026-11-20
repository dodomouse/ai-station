# DeepSpeed

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[deepspeedai/DeepSpeed](https://github.com/deepspeedai/DeepSpeed)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 43332 |
| 评估时间 / Evaluated at | 2026-11-17T14:24:07.604213Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:27.780Z |

## 中文

用于模型训练与推理的分布式优化库。

通过状态分片、卸载和并行执行，调整大模型任务的资源需求。

### 主要功能

- 提供多种内存优化机制，包括 ZeRO 和 ZeRO-Infinity。
- 支持多种并行训练方式，包括数据、流水线和序列并行。
- 提供环境报告，用于检查本机扩展和算子兼容性。

### 环境要求

- 先安装 PyTorch，再安装 DeepSpeed；加速器和编译环境需匹配所用扩展。
- 分布式任务还需配置多设备通信和训练启动环境。

### 使用限制

- 并非所有功能都支持每个平台。README 明确 Windows 不支持 AIO 和 GDS。
- 扩展可即时编译，安装成功不代表所有优化算子均可用。

### 开始使用

1. 按[官方入门](https://www.deepspeed.ai/)准备 PyTorch 和 DeepSpeed。
2. 运行 README 中的环境报告，核对所需扩展。
3. 参考[高级安装](https://www.deepspeed.ai/tutorials/advanced-install/)和训练示例配置首个任务。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:27.780Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-17 · commit](https://github.com/deepspeedai/DeepSpeed/commit/fd8be8161176d0359060cc44faa98383382b70d3)。Exit spawned test workers with os._exit to avoid gloo abort at shutdown (#9100)

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [Official README](https://github.com/deepspeedai/DeepSpeed/blob/master/README.md)
- [Documentation](https://www.deepspeed.ai/)
- [Advanced installation](https://www.deepspeed.ai/tutorials/advanced-install/)

## English

A distributed optimization library for model training and inference.

Adjusts resource requirements for large-model workloads through state sharding, offloading, and parallel execution.

### Features

- Provides memory optimization mechanisms such as ZeRO and ZeRO-Infinity.
- Supports parallel training strategies including data, pipeline, and sequence parallelism.
- Provides an environment report for checking extension and operator compatibility.

### Requirements

- Install PyTorch before DeepSpeed; accelerator and compiler environments must match the required extensions.
- Distributed workloads also require inter-device communication and launch configuration.

### Limitations

- Not every feature supports every platform; the README states that AIO and GDS are unavailable on Windows.
- Extensions may compile just in time; successful installation does not mean every optimized operator is available.

### Getting started

1. Prepare PyTorch and DeepSpeed using the [official project documentation](https://www.deepspeed.ai/).
2. Run the README's environment report and check required extensions.
3. Configure the first workload using the [advanced installation guide](https://www.deepspeed.ai/tutorials/advanced-install/) and training examples.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:27.780Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-17 · commit](https://github.com/deepspeedai/DeepSpeed/commit/fd8be8161176d0359060cc44faa98383382b70d3).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [Official README](https://github.com/deepspeedai/DeepSpeed/blob/master/README.md)
- [Documentation](https://www.deepspeed.ai/)
- [Advanced installation](https://www.deepspeed.ai/tutorials/advanced-install/)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:24:07.604213Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "deepspeed",
    "name": "DeepSpeed",
    "repository": "deepspeedai/DeepSpeed",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkyMzU4NjAyMDQ=",
    "category": "ai",
    "summary": {
      "zh-CN": "用于模型训练与推理的分布式优化库。",
      "en": "A distributed optimization library for model training and inference."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:24:07.604213Z",
        "en": "2026-11-17T14:24:07.604213Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "通过状态分片、卸载和并行执行，调整大模型任务的资源需求。",
        "en": "Adjusts resource requirements for large-model workloads through state sharding, offloading, and parallel execution."
      },
      "source_url": "https://github.com/deepspeedai/DeepSpeed/blob/master/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/deepspeedai/DeepSpeed/commit/fd8be8161176d0359060cc44faa98383382b70d3",
        "occurred_at": "2026-11-17T11:16:21Z",
        "reviewed_at": "2026-11-17T14:24:07.604213Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "Exit spawned test workers with os._exit to avoid gloo abort at shutdown (#9100) 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/deepspeedai/DeepSpeed/blob/master/README.md"
      },
      {
        "title": "Documentation",
        "url": "https://www.deepspeed.ai/"
      },
      {
        "title": "Advanced installation",
        "url": "https://www.deepspeed.ai/tutorials/advanced-install/"
      }
    ]
  },
  "snapshot": {
    "full_name": "deepspeedai/DeepSpeed",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkyMzU4NjAyMDQ=",
    "stargazers_count": 43332,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:27.780Z",
    "source_url": "https://api.github.com/repos/deepspeedai/DeepSpeed"
  }
}
```

</details>
