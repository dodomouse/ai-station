# Hunyuan3D 2

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[Tencent-Hunyuan/Hunyuan3D-2](https://github.com/Tencent-Hunyuan/Hunyuan3D-2)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 15462 |
| 评估时间 / Evaluated at | 2026-11-17T14:28:37.558447Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T14:14:26.871Z |

## 中文

通过形状生成和纹理合成两个阶段，把图像转换为带纹理的 3D 资产。

为 AI 生成的网格添加纹理，并通过代码、网页或 Blender 接入 3D 制作流程。

### 主要功能

- Hunyuan3D-DiT 从输入图像生成网格。
- Hunyuan3D-Paint 为网格合成纹理。
- 提供 Gradio、API Server 和 Blender 插件入口。网格可导出为 GLB、OBJ 或其他支持的格式。

### 环境要求

- 需要 PyTorch、仓库依赖和选定模型的权重。
- 纹理功能还需安装 custom_rasterizer 和 differentiable_renderer 扩展。

### 使用限制

- 形状和纹理是分开的阶段；只运行形状流水线不会自动生成纹理。
- 运行资源取决于模型和阶段，应按官方说明选择配置。

### 开始使用

1. 按 Install Requirements 安装 PyTorch，并运行 `pip install -r requirements.txt` 和 `pip install -e .`。
2. 按 Code Usage 加载预训练流水线，用 `assets/demo.png` 生成测试网格。
3. 若要生成纹理，先安装纹理扩展，再按 Hunyuan3D-Paint 示例处理网格并导出。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T14:14:26.871Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-08 · pr](https://github.com/Tencent-Hunyuan/Hunyuan3D-2/pull/385)。新建 PR，建议修复层次解码中的整数截断；作为 PR 活动记录，不据此声称已合并。

本次为文档复核，未安装或运行上游项目。PR 或 issue 仅作为活动证据，不代表变更已合并或问题已修复。许可不作为本次准入条件。

- [官方 README / Official README](https://raw.githubusercontent.com/Tencent-Hunyuan/Hunyuan3D-2/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/Tencent-Hunyuan/Hunyuan3D-2)

## English

Convert images into textured 3D assets through separate shape-generation and texture-synthesis stages.

It adds textures to generated meshes and connects AI generation to 3D workflows through code, a web interface, or Blender.

### Features

- Hunyuan3D-DiT generates a mesh from an input image.
- Hunyuan3D-Paint synthesizes mesh textures.
- Provide Gradio, API Server, and Blender add-on entry points, with mesh export to formats such as GLB/OBJ.

### Requirements

- Requires PyTorch, repository dependencies, and weights for the selected model.
- Texture generation also requires the custom_rasterizer and differentiable_renderer extensions.

### Limitations

- Shape and texture generation are separate stages; running the shape pipeline alone does not add textures.
- Resource needs depend on the model and stage, so use the configuration described by the project.

### Getting started

1. Install PyTorch following Install Requirements, then run `pip install -r requirements.txt` and `pip install -e .`.
2. Load the pretrained pipeline from Code Usage and generate a test mesh from `assets/demo.png`.
3. For textures, install the texture extensions, follow the Hunyuan3D-Paint example, and export the mesh.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T14:14:26.871Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-08 · pr](https://github.com/Tencent-Hunyuan/Hunyuan3D-2/pull/385).

This is a documentation review; the upstream software was not installed or run. A PR or issue establishes activity only, not a merged change or resolved issue. Licensing is not an admission criterion.

- [官方 README / Official README](https://raw.githubusercontent.com/Tencent-Hunyuan/Hunyuan3D-2/main/README.md)
- [GitHub 仓库元数据 / Repository metadata](https://api.github.com/repos/Tencent-Hunyuan/Hunyuan3D-2)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T14:28:37.558447Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "hunyuan3d-2",
    "name": "Hunyuan3D 2",
    "repository": "Tencent-Hunyuan/Hunyuan3D-2",
    "repo_node_id": "R_kgDONtOTwg",
    "category": "media",
    "summary": {
      "zh-CN": "通过形状生成和纹理合成两个阶段，把图像转换为带纹理的 3D 资产。",
      "en": "Convert images into textured 3D assets through separate shape-generation and texture-synthesis stages."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T14:28:37.558447Z",
        "en": "2026-11-17T14:28:37.558447Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "为 AI 生成的网格添加纹理，并通过代码、网页或 Blender 接入 3D 制作流程。",
        "en": "It adds textures to generated meshes and connects AI generation to 3D workflows through code, a web interface, or Blender."
      },
      "source_url": "https://raw.githubusercontent.com/Tencent-Hunyuan/Hunyuan3D-2/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "pr",
        "url": "https://github.com/Tencent-Hunyuan/Hunyuan3D-2/pull/385",
        "occurred_at": "2026-11-08T08:38:39Z",
        "reviewed_at": "2026-11-17T14:28:37.558447Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "新建 PR，建议修复层次解码中的整数截断；作为 PR 活动记录，不据此声称已合并。 此记录用于证明窗口内活动。",
          "en": "The recorded pr establishes repository activity within the review window; it is not runtime validation or proof that a proposed change was merged."
        }
      }
    ],
    "sources": [
      {
        "title": "官方 README / Official README",
        "url": "https://raw.githubusercontent.com/Tencent-Hunyuan/Hunyuan3D-2/main/README.md"
      },
      {
        "title": "GitHub 仓库元数据 / Repository metadata",
        "url": "https://api.github.com/repos/Tencent-Hunyuan/Hunyuan3D-2"
      }
    ]
  },
  "snapshot": {
    "full_name": "Tencent-Hunyuan/Hunyuan3D-2",
    "repo_node_id": "R_kgDONtOTwg",
    "stargazers_count": 15462,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T14:14:26.871Z",
    "source_url": "https://api.github.com/repos/Tencent-Hunyuan/Hunyuan3D-2"
  }
}
```

</details>
