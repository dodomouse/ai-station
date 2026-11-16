# The Well

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[PolymathicAI/the_well](https://github.com/PolymathicAI/the_well)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 数据处理 / Data processing |
| 状态 / Status | 已收录 / Included |
| Star | 4577 |
| 许可证 / License | BSD-3-Clause |
| 评估时间 / Evaluated at | 2026-11-16T14:32:13.801Z |

## 中文

提供物理时空模拟数据的统一读取、下载和模型基准工具。

### 用途与功能

- 训练物理模拟代理模型
- 比较模型的多步预测表现

Python 数据接口兼容 PyTorch DataLoader；提供数据下载、Hugging Face 流式读取、参考模型、训练配置和评估指标。

### 环境与限制

建议 Python 3.10+ 与匹配硬件的 PyTorch。单个数据集可达数 GB 至 TB。完整数据约 15 TB，应按需求下载。代码BSD许可不替代数据集各自条款，训练算力和存储自备。

### 开始使用

安装 the_well 包后，先下载一个数据集及拆分，再按教程构造 WellDataset。 参阅[官方 README](https://github.com/PolymathicAI/the_well/blob/master/README.md)。

### 收录与来源

具备统一数据接口、参考训练实现和评估代码，可直接嵌入科研流程。 最近维护：[实现提交](https://github.com/PolymathicAI/the_well/commit/e63dec8ded515be864755eaf595d39fea409e335)（2026-10-12T21:49:06Z）。已核对合并提交：长期预测指标改为跨验证batch求平均，并新增针对回归的测试。

通过逛逛GitHub的第三方文章索引发现。索引记录了下列文章；本次未读取微信原文，不据此声称已阅读全文。

- 2026-10-31：[我在 GitHub 上搜罗了 6 个高质量数据集，看看哪些会用到。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538180&idx=1&sn=f8f37078438b90a2815051c5012a8acc)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。


补充核对作者在公开平台发布或授权发布的文章，确认署名、日期与仓库关联：

- 2026-10-31：[我在 GitHub 上搜罗了 6 个高质量数据集，看看哪些会用到。](https://www.woshipm.com/share/6487219.html)

## English

Provides unified loading, download and model benchmarks for spatiotemporal physics simulations.

### Uses and features

- Train surrogate physics models
- Compare multi-step prediction performance

Python data interfaces work with PyTorch DataLoader, alongside downloads, Hugging Face streaming, reference models, training configurations and metrics.

### Requirements and limits

Python 3.10+ and a hardware-appropriate PyTorch build are recommended. Individual datasets range from GB to TB, with roughly 15 TB in total; download selectively. The code's BSD license does not replace dataset-specific terms, and compute and storage are required.

### Getting started

Install the_well, download one dataset and split, then create a WellDataset following the tutorial. See the [official README](https://github.com/PolymathicAI/the_well/blob/master/README.md).

### Review and provenance

Includes unified data access, reference training and evaluation code for research workflows. Recent maintenance: [implementation commit](https://github.com/PolymathicAI/the_well/commit/e63dec8ded515be864755eaf595d39fea409e335) (2026-10-12T21:49:06Z). Reviewed the merged implementation: long-horizon metrics now average across validation batches, with regression tests.

Discovered through a third-party index of 逛逛GitHub articles. The index records the articles below; the original WeChat pages were not read in this review. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.


Public articles published or authorized by the author were also checked for attribution, date and repository links. See the additional links in the Chinese section.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:32:13.801Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "the-well",
    "name": "The Well",
    "repository": "PolymathicAI/the_well",
    "repo_node_id": "R_kgDONXvPsg",
    "category": "data",
    "tags": [],
    "forms": [
      "library",
      "cli"
    ],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "The Well"
      ],
      "en": [
        "The Well"
      ]
    },
    "summary": {
      "zh-CN": "提供物理时空模拟数据的统一读取、下载和模型基准工具。",
      "en": "Provides unified loading, download and model benchmarks for spatiotemporal physics simulations."
    },
    "use_cases": {
      "zh-CN": [
        "训练物理模拟代理模型",
        "比较模型的多步预测表现"
      ],
      "en": [
        "Train surrogate physics models",
        "Compare multi-step prediction performance"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:32:13.801Z",
        "en": "2026-11-16T14:32:13.801Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "BSD-3-Clause",
      "osi_approved": true,
      "license_sha256": "714e789efb1453e42fafd50d4f02e6f73d516e345a93b4c9238cf8f203f34caf",
      "source_url": "https://github.com/PolymathicAI/the_well/blob/master/LICENSE",
      "reviewed_at": "2026-11-16T14:32:13.801Z"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/PolymathicAI/the_well/commit/e63dec8ded515be864755eaf595d39fea409e335",
        "occurred_at": "2026-10-12T21:49:06Z",
        "reason": {
          "zh-CN": "已核对合并提交：长期预测指标改为跨验证batch求平均，并新增针对回归的测试。",
          "en": "Reviewed the merged implementation: long-horizon metrics now average across validation batches, with regression tests."
        },
        "reviewed_at": "2026-11-16T14:32:13.801Z",
        "qualifies": true
      }
    ],
    "sources": [
      {
        "url": "https://github.com/PolymathicAI/the_well/blob/master/README.md",
        "accessed_at": "2026-11-16T14:32:13.801Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/PolymathicAI/the_well/blob/master/LICENSE",
        "accessed_at": "2026-11-16T14:32:13.801Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.noking.tech/github-radar/data/library.json",
        "accessed_at": "2026-11-16T14:32:13.801Z",
        "supports": {
          "zh-CN": "第三方索引中的公众号文章归属、时间与项目发现线索；非原文阅读证据。",
          "en": "Third-party account attribution, article dates and discovery leads; not proof of reading the originals."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538180&idx=1&sn=f8f37078438b90a2815051c5012a8acc",
        "accessed_at": "2026-11-16T14:32:13.801Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-10-31 我在 GitHub 上搜罗了 6 个高质量数据集，看看哪些会用到。；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-10-31; not directly read in this review."
        }
      },
      {
        "url": "https://www.woshipm.com/share/6487219.html",
        "accessed_at": "2026-11-16T14:26:00.427448+00:00",
        "published_date": "2026-10-31",
        "author": "逛逛GitHub",
        "supports": {
          "zh-CN": "作者公开发表或授权的文章；已核对署名、日期与仓库链接。",
          "en": "Author-published or authorized public article; attribution, date and repository links checked."
        }
      }
    ],
    "quality_review": {
      "basis": {
        "zh-CN": "具备统一数据接口、参考训练实现和评估代码，可直接嵌入科研流程。",
        "en": "Includes unified data access, reference training and evaluation code for research workflows."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDONXvPsg",
    "full_name": "PolymathicAI/the_well",
    "stargazers_count": 4577,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "BSD-3-Clause",
    "license_sha256": "714e789efb1453e42fafd50d4f02e6f73d516e345a93b4c9238cf8f203f34caf",
    "last_success_at": "2026-11-16T14:19:05.891Z"
  }
}
```

</details>

