# FiftyOne

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[voxel51/fiftyone](https://github.com/voxel51/fiftyone)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 数据处理 / Data processing |
| 状态 / Status | 已收录 / Included |
| Star | 11315 |
| 评估时间 / Evaluated at | 2026-11-17T15:22:59Z |
| 快照时间 / Snapshot recorded at | 2026-11-17T15:22:59Z |

## 中文

FiftyOne 将本地图片和视频整理为可筛选的数据集。它提供 Python 接口与可视化应用，用于检索、标注和模型评估。

它帮助视觉 AI 项目筛选素材、检查标注和模型结果。配置嵌入模型后，还能检索相似图片和视频帧。

### 主要功能

- 递归导入本地图片或视频目录，在 App 中浏览、筛选和标记样本。
- 为图片或对象区域建立向量索引。使用 CLIP 兼容索引时，可通过文字或示例图片搜索。
- 将视频转换为帧视图，保留原视频 ID 和帧号。根据已有时间范围或逐帧标签建立片段视图。
- 导出选中的媒体、标签或视频片段，供后续处理使用。
- 可视化嵌入、检查数据质量，并评估分类与检测模型的结果。

### 环境要求

- 支持 macOS、Windows 和 Linux。官方文档要求 Python 3.10–3.13，建议使用虚拟环境。视频处理还需 FFmpeg。
- 向量检索需模型或预先计算的嵌入。CLIP 示例使用 PyTorch。额外依赖和计算设备要求取决于所选模型。

### 使用限制

- 导入视频不会自动生成动作标签或镜头边界。片段视图依赖已有标签、帧范围或筛选表达式。图像向量检索不能直接等同于时序动作理解。
- 抽帧会生成磁盘图片。视频库的处理时间和存储需求受采样频率与索引范围影响。
- 文字搜索需要支持文本查询的模型和索引。按模型名称建立索引后，App 和后续 Python 会话才能重新加载模型。
- 官方片段导出流程生成媒体和数据集文件。接入剪映或 Premiere 工程格式需另外处理。

### 开始使用

1. 按[安装指南](https://docs.voxel51.com/installation/index.html)在虚拟环境中安装 `fiftyone`。
2. 按[目录导入指南](https://docs.voxel51.com/user_guide/import_datasets.html)导入一组代表性图片或视频。用 `fo.launch_app()` 检查导入结果。
3. 视频检索先按[帧视图说明](https://docs.voxel51.com/user_guide/using_views.html#frame-views)配置抽帧。按[相似度检索指南](https://docs.voxel51.com/user_guide/similarity.html)创建 CLIP 索引。用文字或示例图片查询。

### 收录与来源

AI 任务用途已依据官方文档核对。Star 为 2026-11-17T15:22:59Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-13 · commit](https://github.com/voxel51/fiftyone/commit/1b61a94988fcab55c10378f5fdd2f087b42ff1c9)。合并 MCP operator 文档更新。

本次为文档复核，未安装或运行上游项目。上述提交证明窗口内活动，不代表软件运行验证。许可不作为本次准入条件。

- [Official README](https://github.com/voxel51/fiftyone/blob/main/README.md)
- [Similarity Search](https://docs.voxel51.com/user_guide/similarity.html)
- [Video frame and clip views](https://docs.voxel51.com/user_guide/using_views.html#clip-views)
- [Exporting video clips](https://docs.voxel51.com/user_guide/export_datasets.html#video-clips)

## English

FiftyOne organizes local images and videos into datasets that you can filter and explore. Its Python API and visual application support search, annotation, and model evaluation.

It helps visual AI projects select data and inspect annotations and model results. With an embedding model configured, it can also retrieve similar images and video frames.

### Features

- Recursively import local image or video directories, then browse, filter, and tag samples in the App.
- Build embedding indexes for images or object patches. CLIP-compatible indexes support queries by text or example images.
- Create frame views that retain source video IDs and frame numbers. Build clip views from existing temporal ranges or frame labels.
- Export selected media, labels, or video clips for downstream workflows.
- Visualize embeddings, inspect data quality, and evaluate classification and detection results.

### Requirements

- Supports macOS, Windows, and Linux. Official documentation requires Python 3.10–3.13 and recommends a virtual environment. Video workflows also require FFmpeg.
- Similarity search requires a model or precomputed embeddings. The CLIP examples use PyTorch. Additional dependencies and compute requirements depend on the selected model.

### Limitations

- Importing videos does not automatically generate action labels or shot boundaries. Clip views require existing labels, frame ranges, or filtering expressions. Image embedding search is not equivalent to temporal action understanding.
- Frame sampling creates images on disk. Processing time and storage requirements depend on the sampling rate and indexing scope.
- Text search requires a model and index that support text queries. Register the model by name so that the App and later Python sessions can reload it.
- The documented clip export workflow produces media and dataset files. Integration with Jianying or Premiere project formats requires additional work.

### Getting started

1. Follow the [installation guide](https://docs.voxel51.com/installation/index.html) to install `fiftyone` in a virtual environment.
2. Import a representative collection of images or videos using the [directory import guide](https://docs.voxel51.com/user_guide/import_datasets.html). Inspect the result with `fo.launch_app()`.
3. For video search, configure sampling using the [frame views guide](https://docs.voxel51.com/user_guide/using_views.html#frame-views). Create a CLIP index using the [similarity search guide](https://docs.voxel51.com/user_guide/similarity.html). Query it with text or example images.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-17T15:22:59Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-13 · commit](https://github.com/voxel51/fiftyone/commit/1b61a94988fcab55c10378f5fdd2f087b42ff1c9).

This is a documentation review; the upstream software was not installed or run. The cited commit establishes activity within the review window, not runtime validation. Licensing is not an admission criterion.

- [Official README](https://github.com/voxel51/fiftyone/blob/main/README.md)
- [Similarity Search](https://docs.voxel51.com/user_guide/similarity.html)
- [Video frame and clip views](https://docs.voxel51.com/user_guide/using_views.html#clip-views)
- [Exporting video clips](https://docs.voxel51.com/user_guide/export_datasets.html#video-clips)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-17T15:22:59Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "fiftyone",
    "name": "FiftyOne",
    "repository": "voxel51/fiftyone",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkyNTc5MTM1OTU=",
    "category": "data",
    "summary": {
      "zh-CN": "FiftyOne 将本地图片和视频整理为可筛选的数据集。它提供 Python 接口与可视化应用，用于检索、标注和模型评估。",
      "en": "FiftyOne organizes local images and videos into datasets that you can filter and explore. Its Python API and visual application support search, annotation, and model evaluation."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T15:22:59Z",
        "en": "2026-11-17T15:22:59Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "它帮助视觉 AI 项目筛选素材、检查标注和模型结果。配置嵌入模型后，还能检索相似图片和视频帧。",
        "en": "It helps visual AI projects select data and inspect annotations and model results. With an embedding model configured, it can also retrieve similar images and video frames."
      },
      "source_url": "https://github.com/voxel51/fiftyone/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/voxel51/fiftyone/commit/1b61a94988fcab55c10378f5fdd2f087b42ff1c9",
        "occurred_at": "2026-11-13T20:39:36Z",
        "reviewed_at": "2026-11-17T15:22:59Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "合并 MCP operator 文档更新。 此记录用于证明窗口内活动。",
          "en": "The recorded commit establishes repository activity within the review window; it does not establish runtime behavior."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/voxel51/fiftyone/blob/main/README.md"
      },
      {
        "title": "Similarity Search",
        "url": "https://docs.voxel51.com/user_guide/similarity.html"
      },
      {
        "title": "Video frame and clip views",
        "url": "https://docs.voxel51.com/user_guide/using_views.html#clip-views"
      },
      {
        "title": "Exporting video clips",
        "url": "https://docs.voxel51.com/user_guide/export_datasets.html#video-clips"
      }
    ]
  },
  "snapshot": {
    "full_name": "voxel51/fiftyone",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkyNTc5MTM1OTU=",
    "stargazers_count": 11315,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-17T15:22:59Z",
    "source_url": "https://api.github.com/repos/voxel51/fiftyone"
  }
}
```

</details>
