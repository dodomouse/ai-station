# DeepInfer

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[deepseek-ai/DeepInfer](https://github.com/deepseek-ai/DeepInfer)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 26102 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:19:06.299Z |

## 中文

面向 DeepSeek 模型的推理实现，提供高性能计算与分布式执行组件。

### 主要功能

- 公开模型执行与设备相关实现。
- 支持当前说明列出的 NVIDIA 和昇腾硬件路径。

### 环境与限制

- 当前支持范围聚焦 DeepSeek V4.1 Flash，要求特定 Linux、编译器、Python 与 CUDA/CANN 组合。
- 面向离线推理核心，不能直接视为完整在线服务系统。

### 开始使用

从[官方说明](https://github.com/deepseek-ai/DeepInfer/blob/main/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/deepseek-ai/DeepInfer/releases)可用于确认版本。

### 收录复核

面向 DeepSeek 模型的推理实现，提供高性能计算与分布式执行组件。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。

有效维护证据：[553741557a](https://github.com/deepseek-ai/DeepInfer/commit/553741557a57df44a46fb3ab72b6aafeaf945337)，2026-10-25T11:59:27Z。修复布尔环境变量解析，对无效值明确返回错误。

文章来源：[逛逛GitHub署名文章](https://www.woshipm.com/ai/6486928.html)，平台日期 2026-10-30。已通过公开正文核对仓库链接与作者归属；微信正文未直接读取。

本次为文档与实现证据复核，未安装或运行上游项目。

## English

An inference implementation for DeepSeek models with optimized compute and distributed execution components.

### Features

- Publishes model execution and device-specific implementations.
- Supports the NVIDIA and Ascend paths listed in the current documentation.

### Requirements and limits

- Current support focuses on DeepSeek V4.1 Flash and specific Linux, compiler, Python and CUDA/CANN combinations.
- It is an offline inference core, not a complete online serving system.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/deepseek-ai/DeepInfer/blob/main/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/deepseek-ai/DeepInfer/releases) for versions.

### Review and provenance

An inference implementation for DeepSeek models with optimized compute and distributed execution components. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.

Activity: [553741557a](https://github.com/deepseek-ai/DeepInfer/commit/553741557a57df44a46fb3ab72b6aafeaf945337), 2026-10-25T11:59:27Z. Fixes boolean environment parsing and rejects invalid values.

Discovery: [an author-attributed 逛逛GitHub article](https://www.woshipm.com/ai/6486928.html), dated 2026-10-30 on the public platform. Repository links and attribution were checked in its public body; the WeChat body was not read directly.

This review covers documentation and implementation evidence. The upstream project was not installed or run.

## Review evidence

```json
{
  "evaluated_at": "2026-11-16T14:58:29.135174Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "deepinfer",
    "name": "DeepInfer",
    "repository": "deepseek-ai/DeepInfer",
    "repo_node_id": "R_kgDOVL9UxQ",
    "category": "ai",
    "summary": {
      "zh-CN": "面向 DeepSeek 模型的推理实现，提供高性能计算与分布式执行组件。",
      "en": "An inference implementation for DeepSeek models with optimized compute and distributed execution components."
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
      "zh-CN": "面向 DeepSeek 模型的推理实现，提供高性能计算与分布式执行组件。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。",
      "en": "An inference implementation for DeepSeek models with optimized compute and distributed execution components. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4",
      "source_url": "https://github.com/deepseek-ai/DeepInfer/blob/main/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "Root license reviewed. External dependencies and assets retain their individual licenses."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-10-25T11:59:27Z",
        "reviewed_at": "2026-11-16T14:58:29.135174Z",
        "url": "https://github.com/deepseek-ai/DeepInfer/commit/553741557a57df44a46fb3ab72b6aafeaf945337",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复布尔环境变量解析，对无效值明确报错。",
          "en": "Fixes boolean environment parsing and rejects invalid values."
        },
        "reviewed_files": [
          "deepinfer/environ.py"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/deepseek-ai/DeepInfer",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/deepseek-ai/DeepInfer/blob/main/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/deepseek-ai/DeepInfer/blob/main/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/deepseek-ai/DeepInfer/commit/553741557a57df44a46fb3ab72b6aafeaf945337",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://www.woshipm.com/ai/6486928.html",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      }
    ],
    "article_source": {
      "article_id": "2247538171_1",
      "title": "这 6 个 GitHub 项目是刚开源，但是 Star 攀升很快的几个。",
      "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538171&idx=1&sn=cd8f63d5332497b649d72590298e1a05",
      "published_date": "2026-10-30",
      "account": "逛逛GitHub",
      "content_review_url": "https://www.woshipm.com/ai/6486928.html",
      "content_review_kind": "author-attributed public article",
      "wechat_direct_body_read": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVL9UxQ",
    "full_name": "deepseek-ai/DeepInfer",
    "stargazers_count": 26102,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4",
    "last_success_at": "2026-11-16T14:19:06.299Z"
  }
}
```
