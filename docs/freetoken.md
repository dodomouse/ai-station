# FreeToken

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 17244 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:24:08.700270Z |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:18:51.712Z |

## 中文

### 用途与功能

在本地运行混合专家模型的推理引擎。组合 GPU、CPU 和系统内存，提供专家缓存和模型服务接口。

适合已有合适硬件、需要自建模型服务的开发者。提供命令行和桌面入口，并兼容部分 OpenAI、Anthropic 接口。

### 环境与限制

CLI 安装文档要求 Linux x86_64、NVIDIA GPU、r580+ 驱动、CUDA 13 和 Python 3.10+。首次编译内核需要 nvcc。桌面另有 Windows/Linux 发行。模型权重、内存和磁盘仍需满足对应模型要求；宣传速度未在本轮实测。

### 入门与收录判断

从[官方 README](https://github.com/FlashML-org/FreeToken/blob/main/README.md)查阅安装和配置步骤。针对显存不足时的混合专家推理提供可检查实现和安装说明，适合本地推理选型。

本轮为文档复核，未安装、运行或测试上游软件。正式 v0.2.2 增加推测解码和 Ripple 模型支持，并优化 CPU 专家执行。详见[维护记录](https://github.com/FlashML-org/FreeToken/releases/tag/v0.2.2)。

### 文章来源

公众号“逛逛GitHub”的[微信原文](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538420&idx=1&sn=9769127e763c53057c449032da509279)，索引日期为 2026-11-09。本次读取了作者在[人人都是产品经理发布的正文](https://www.woshipm.com/share/6491406.html)，该页日期为 2026-11-10。功能和限制另按当前上游复核。

## English

### Purpose and features

A local mixture-of-experts inference engine that combines GPU, CPU and system memory with expert caching and serving APIs.

Provides CLI and desktop entry points and compatible OpenAI and Anthropic interfaces for supported models.

### Requirements and limits

The CLI guide requires Linux x86_64, an NVIDIA GPU, r580+ drivers, CUDA 13 and Python 3.10+; first-use kernel compilation needs nvcc. Desktop builds also cover Windows. Model weights, RAM and disk requirements remain model-specific; performance claims were not benchmarked.

### Getting started and review

Use the [official README](https://github.com/FlashML-org/FreeToken/blob/main/README.md) for installation and configuration. This is a documentation review; the software was not installed or tested. Stable v0.2.2 adds speculative decoding and Ripple model support and improves CPU expert execution. See the [release](https://github.com/FlashML-org/FreeToken/releases/tag/v0.2.2).

The original WeChat article is dated 2026-11-09 in the public index. Its author-published mirror is dated 2026-11-10. The mirror establishes the article association; current upstream documentation supports the feature descriptions.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:24:08.700270Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "freetoken",
    "name": "FreeToken",
    "repository": "FlashML-org/FreeToken",
    "repo_node_id": "R_kgDOTedDYg",
    "category": "ai",
    "summary": {
      "zh-CN": "在本地运行混合专家模型的推理引擎。组合 GPU、CPU 和系统内存，提供专家缓存和模型服务接口。",
      "en": "A local mixture-of-experts inference engine that combines GPU, CPU and system memory with expert caching and serving APIs."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:24:08.700270Z",
        "en": "2026-11-16T14:24:08.700270Z"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "basis": "针对显存不足时的混合专家推理提供可检查实现和安装说明，适合本地推理选型。",
      "stars_are_advisory": true,
      "reviewed_at": "2026-11-16T14:24:08.700270Z"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "1d28009bf66a66c90fa9c5561d9a73b7460ab611eeb3e90169d22a3b5a2a2326",
      "source_url": "https://github.com/FlashML-org/FreeToken/blob/548f97f51e434367f9fe4575d8aac45f68e92ca5/LICENSE",
      "reviewed_at": "2026-11-16T14:24:08.700270Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "548f97f51e434367f9fe4575d8aac45f68e92ca5"
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-11-09T04:10:58Z",
        "reviewed_at": "2026-11-16T14:24:08.700270Z",
        "url": "https://github.com/FlashML-org/FreeToken/releases/tag/v0.2.2",
        "qualifies": true,
        "reason": {
          "zh-CN": "正式 v0.2.2 增加推测解码和 Ripple 模型支持，并优化 CPU 专家执行。",
          "en": "Stable v0.2.2 adds speculative decoding and Ripple model support and improves CPU expert execution."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/FlashML-org/FreeToken",
        "accessed_at": "2026-11-16T14:18:51.712Z",
        "supports": "Repository identity, Stars and public state."
      },
      {
        "url": "https://github.com/FlashML-org/FreeToken/blob/main/README.md",
        "accessed_at": "2026-11-16T14:24:08.700270Z",
        "supports": "Capabilities, requirements and limits."
      },
      {
        "url": "https://www.woshipm.com/share/6491406.html",
        "published_date": "2026-11-10",
        "accessed_at": "2026-11-16T14:24:08.700270Z",
        "supports": "Article body and account attribution verified on the author-published mirror."
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538420&idx=1&sn=9769127e763c53057c449032da509279",
        "published_date": "2026-11-09",
        "supports": "Original WeChat URL and date from the public article index; original body unavailable."
      }
    ],
    "discovery": {
      "account": "逛逛GitHub",
      "article": {
        "article_id": "2247538420_1",
        "title": "7 个近期 GitHub 上贼火火的开源项目，又是质量很高的一波。",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538420&idx=1&sn=9769127e763c53057c449032da509279",
        "published_date": "2026-11-09"
      },
      "index_url": "https://www.noking.tech/github-radar/",
      "body_verification": "author_published_mirror"
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOTedDYg",
    "full_name": "FlashML-org/FreeToken",
    "stargazers_count": 17244,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "1d28009bf66a66c90fa9c5561d9a73b7460ab611eeb3e90169d22a3b5a2a2326",
    "last_success_at": "2026-11-16T14:18:51.712Z"
  }
}
```

</details>
