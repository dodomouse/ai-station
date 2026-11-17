# oMLX

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[jundot/omlx](https://github.com/jundot/omlx)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 23663 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:20:19.260Z |

## 中文

为 Apple 芯片 Mac 提供本地模型推理服务和菜单栏管理界面。

### 主要功能

- 使用连续批处理及内存、SSD 分层 KV 缓存。
- 按需加载模型，并向兼容客户端提供推理接口。

### 环境与限制

- 要求 macOS 15+ 与 Apple 芯片，源码路径使用 Python 3.11–3.13。
- 模型内存需求和许可各异，RC 版本应与稳定发行区分。

### 开始使用

从[官方说明](https://github.com/jundot/omlx/blob/main/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/jundot/omlx/releases)可用于确认版本。

### 收录复核

为 Apple 芯片 Mac 提供本地模型推理服务和菜单栏管理界面。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。

有效维护证据：[8bfb13be42](https://github.com/jundot/omlx/commit/8bfb13be42bbc3db78ec1bcf59b2f47902642ade)，2026-11-16T09:43:27Z。修复 CUDA 辅助端量化矩阵计算的批次索引与缓存问题。

发现线索：[公开索引](https://www.noking.tech/github-radar/)记录的[微信文章](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536122&idx=1&sn=b7a284d06296707235d8dde07c6f6d4e)，索引日期 2026-08-23。仅核对公开索引，未直接读取该篇微信全文；功能与限制以上游资料为依据。

本次为文档与实现证据复核，未安装或运行上游项目。

## English

A local model-serving system with menu-bar management for Apple-silicon Macs.

### Features

- Uses continuous batching and tiered memory/SSD KV caching.
- Loads models on demand and exposes inference endpoints to compatible clients.

### Requirements and limits

- Requires macOS 15+ and Apple silicon
- source setup uses Python 3.11–3.13.
- Models have different memory and license requirements
- distinguish release candidates from stable builds.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/jundot/omlx/blob/main/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/jundot/omlx/releases) for versions.

### Review and provenance

A local model-serving system with menu-bar management for Apple-silicon Macs. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.

Activity: [8bfb13be42](https://github.com/jundot/omlx/commit/8bfb13be42bbc3db78ec1bcf59b2f47902642ade), 2026-11-16T09:43:27Z. Fixes quantized-matrix batch indexing and cache issues in the CUDA helper.

Discovery: [an indexed WeChat article](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536122&idx=1&sn=b7a284d06296707235d8dde07c6f6d4e). This is a secondary discovery record; the WeChat article body was not read. Features and limits come from upstream documentation.

This review covers documentation and implementation evidence. The upstream project was not installed or run.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:58:29.135174Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "omlx",
    "name": "oMLX",
    "repository": "jundot/omlx",
    "repo_node_id": "R_kgDORPkI2g",
    "category": "ai",
    "summary": {
      "zh-CN": "为 Apple 芯片 Mac 提供本地模型推理服务和菜单栏管理界面。",
      "en": "A local model-serving system with menu-bar management for Apple-silicon Macs."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:58:29.135174Z",
        "en": "2026-11-16T14:58:29.135174Z"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "为 Apple 芯片 Mac 提供本地模型推理服务和菜单栏管理界面。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。",
      "en": "A local model-serving system with menu-bar management for Apple-silicon Macs. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "de69b4352c9952cd5f0f4b8cb4584782a07f02c9ba82aeb5d496aa2b7fe5457d",
      "source_url": "https://github.com/jundot/omlx/blob/bf28cd6c43541ececeec01ba797377c913da5f8f/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "Root license reviewed. External dependencies and assets retain their individual licenses.",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "bf28cd6c43541ececeec01ba797377c913da5f8f"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-16T09:43:27Z",
        "reviewed_at": "2026-11-16T14:58:29.135174Z",
        "url": "https://github.com/jundot/omlx/commit/8bfb13be42bbc3db78ec1bcf59b2f47902642ade",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复 CUDA 辅助端量化矩阵计算的批次索引与缓存问题。",
          "en": "Fixes quantized-matrix batch indexing and cache issues in the CUDA helper."
        },
        "reviewed_files": [
          "apps/omlx-cuda-helper/mlx-build/patches/0008-omlx-cuda-qmm-naive-batch-on-grid-x.patch",
          "apps/omlx-cuda-helper/mlx-build/series",
          "apps/omlx-cuda-helper/omlx_cuda_helper/__init__.py"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/jundot/omlx",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/jundot/omlx/blob/main/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/jundot/omlx/blob/bf28cd6c43541ececeec01ba797377c913da5f8f/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/jundot/omlx/commit/8bfb13be42bbc3db78ec1bcf59b2f47902642ade",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536122&idx=1&sn=b7a284d06296707235d8dde07c6f6d4e",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      }
    ],
    "article_source": {
      "article_id": "2247536122_1",
      "title": "一周没逛 GitHub 不要紧，这 TOP 10 的热门开源项目整理好了。",
      "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536122&idx=1&sn=b7a284d06296707235d8dde07c6f6d4e",
      "published_date": "2026-08-23",
      "account": "逛逛GitHub",
      "content_review_url": null,
      "content_review_kind": "secondary article index only",
      "wechat_direct_body_read": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDORPkI2g",
    "full_name": "jundot/omlx",
    "stargazers_count": 23663,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "de69b4352c9952cd5f0f4b8cb4584782a07f02c9ba82aeb5d496aa2b7fe5457d",
    "last_success_at": "2026-11-16T14:20:19.260Z"
  }
}
```

</details>
