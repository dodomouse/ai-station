# OpenViking

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[volcengine/OpenViking](https://github.com/volcengine/OpenViking)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 42305 |
| 许可证 / License | AGPL-3.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:47:41.664Z |

## 中文

用可浏览的虚拟文件系统组织智能体知识、记忆和技能。

### 用途与功能

- 建立可检查的智能体上下文库

提供目录摘要、分层读取、按子树检索、会话管理和快照；可通过SDK、API或Studio使用。

### 环境与限制

自部署需uv、Python3.10+以及embedding和视觉语言模型提供商；Docker路径可同时启动附带组件。模型、存储和多节点部署需配置，推理费用另计。AGPL网络服务义务应按部署核对。

### 开始使用

先按快速入门启动服务，配置模型，再导入小规模资料测试检索。 参阅[官方 README](https://github.com/volcengine/OpenViking/blob/main/README.md)。

### 收录与来源

实现上下文存储、检索和版本管理，近期维护覆盖多节点一致性与存储。 最近维护：[v0.5.5](https://github.com/volcengine/OpenViking/releases/tag/v0.5.5)（2026-11-13T13:13:11Z）。正式版增加pgvector、PostgreSQL路径锁和多节点协调。

通过逛逛GitHub的第三方文章索引发现。索引记录了下列文章；本次未读取微信原文，不据此声称已阅读全文。

- 2026-08-23：[一周没逛 GitHub 不要紧，这 TOP 10 的热门开源项目整理好了。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536122&idx=1&sn=b7a284d06296707235d8dde07c6f6d4e)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。

## English

Organizes agent knowledge, memory and skills in a browsable virtual filesystem.

### Uses and features

- Build inspectable agent context stores

Provides directory summaries, layered reading, subtree-scoped retrieval, sessions and snapshots through SDKs, APIs or Studio.

### Requirements and limits

Self-hosting requires uv, Python 3.10+ and embedding/VLM providers; Docker may also start bundled components. Models, storage and multi-node operation need configuration and incur separate inference costs. Review AGPL obligations for network deployments.

### Getting started

Start a server from the quick-start guide, configure models and test retrieval on a small document set. See the [official README](https://github.com/volcengine/OpenViking/blob/main/README.md).

### Review and provenance

Implements context storage, retrieval and versioning with recent multi-node and storage maintenance. Recent maintenance: [v0.5.5](https://github.com/volcengine/OpenViking/releases/tag/v0.5.5) (2026-11-13T13:13:11Z). The formal release adds pgvector, PostgreSQL path locks and multi-node coordination.

Discovered through a third-party index of 逛逛GitHub articles. The index records the articles below; the original WeChat pages were not read in this review. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:47:41.664Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "openviking",
    "name": "OpenViking",
    "repository": "volcengine/OpenViking",
    "repo_node_id": "R_kgDOQz3Myg",
    "category": "ai",
    "tags": [],
    "forms": [
      "service",
      "library",
      "cli"
    ],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "OpenViking"
      ],
      "en": [
        "OpenViking"
      ]
    },
    "summary": {
      "zh-CN": "用可浏览的虚拟文件系统组织智能体知识、记忆和技能。",
      "en": "Organizes agent knowledge, memory and skills in a browsable virtual filesystem."
    },
    "use_cases": {
      "zh-CN": [
        "建立可检查的智能体上下文库"
      ],
      "en": [
        "Build inspectable agent context stores"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:47:41.664Z",
        "en": "2026-11-16T14:47:41.664Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "AGPL-3.0",
      "osi_approved": true,
      "license_sha256": "1bd87fa6d9a5c79daf0c2af042b6725c9773bf095cc3d1bdf3656e66d1c3e5b1",
      "source_url": "https://github.com/volcengine/OpenViking/blob/main/LICENSE",
      "reviewed_at": "2026-11-16T14:47:41.664Z"
    },
    "activity_evidence": [
      {
        "type": "release",
        "url": "https://github.com/volcengine/OpenViking/releases/tag/v0.5.5",
        "occurred_at": "2026-11-13T13:13:11Z",
        "reason": {
          "zh-CN": "正式版增加pgvector、PostgreSQL路径锁和多节点协调。",
          "en": "The formal release adds pgvector, PostgreSQL path locks and multi-node coordination."
        },
        "reviewed_at": "2026-11-16T14:47:41.664Z",
        "qualifies": true
      }
    ],
    "sources": [
      {
        "url": "https://github.com/volcengine/OpenViking/blob/main/README.md",
        "accessed_at": "2026-11-16T14:47:41.664Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/volcengine/OpenViking/blob/main/LICENSE",
        "accessed_at": "2026-11-16T14:47:41.664Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.noking.tech/github-radar/data/library.json",
        "accessed_at": "2026-11-16T14:47:41.664Z",
        "supports": {
          "zh-CN": "第三方索引中的公众号文章归属、时间与项目发现线索；非原文阅读证据。",
          "en": "Third-party account attribution, article dates and discovery leads; not proof of reading the originals."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536122&idx=1&sn=b7a284d06296707235d8dde07c6f6d4e",
        "accessed_at": "2026-11-16T14:47:41.664Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-08-23 一周没逛 GitHub 不要紧，这 TOP 10 的热门开源项目整理好了。；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-08-23; not directly read in this review."
        }
      }
    ],
    "quality_review": {
      "basis": {
        "zh-CN": "实现上下文存储、检索和版本管理，近期维护覆盖多节点一致性与存储。",
        "en": "Implements context storage, retrieval and versioning with recent multi-node and storage maintenance."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOQz3Myg",
    "full_name": "volcengine/OpenViking",
    "stargazers_count": 42305,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "AGPL-3.0",
    "license_sha256": "1bd87fa6d9a5c79daf0c2af042b6725c9773bf095cc3d1bdf3656e66d1c3e5b1",
    "last_success_at": "2026-11-16T14:20:19.331Z"
  }
}
```

</details>

