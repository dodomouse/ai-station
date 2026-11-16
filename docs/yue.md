# YuE2 推理代码 / YuE2 inference code

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[multimodal-art-projection/YuE](https://github.com/multimodal-art-projection/YuE)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 13534 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:34:39.811Z |

## 中文

通过可编辑旋律与和弦计划生成包含人声和伴奏的歌曲。

### 用途与功能

- 实验歌曲生成与乐谱编辑

提供计划、语义生成、合成与解码的 Python 阶段接口。技能用于编排创作流程。

### 环境与限制

仅收录当前Apache-2.0代码。YuE2权重采用CC BY-NC4.0及额外创作者许可，企业商业用途另需授权；旧发行包许可也需单独核对。标准路径需Linux、Python3.12、支持BF16的NVIDIA GPU与24GB显存；其他平台为实验性。

### 开始使用

先阅读当前代码与MODEL_LICENSE，再按硬件指南安装源码和合适权重。 参阅[官方 README](https://github.com/multimodal-art-projection/YuE/blob/main/README.md)。

### 收录与来源

提供分阶段推理、可编辑音乐计划和硬件适配实现；权重限制单独列明。 最近维护：[实现提交](https://github.com/multimodal-art-projection/YuE/commit/d2427d03db38e0054a1b96019f9add4e409bb08f)（2026-11-01T05:38:47Z）。已核对实现：Intel XPU图执行同时检查用户开关与运行时API，并报告实际设备；含回归测试。

通过逛逛GitHub的第三方文章索引发现。索引记录了下列文章；本次未读取微信原文，不据此声称已阅读全文。

- 2026-10-19：[玩了一天 1.2 万人收藏的开源音乐模型，真的惊艳到我了。。。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537876&idx=1&sn=8ba02c7b1a619f84c1bb1f5ea34c1856)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。


补充核对作者在公开平台发布或授权发布的文章，确认署名、日期与仓库关联：

- 2026-10-20：[玩了一天 1.2 万人收藏的开源音乐模型，真的惊艳到我了。。。](https://www.woshipm.com/ai/6480800.html)

## English

Generates vocals and accompaniment from editable melody and chord plans.

### Uses and features

- Experiment with song generation and composition editing

Provides Python stages for planning, semantic generation, synthesis and decoding, with a skill for creative workflow orchestration.

### Requirements and limits

This entry covers current Apache-2.0 code only. YuE2 weights use CC BY-NC 4.0 with additional creator permission; company commercial use requires separate authorization, and older release licensing must be checked separately. The standard path needs Linux, Python 3.12 and a BF16-capable NVIDIA GPU with 24 GB VRAM; other platforms are experimental.

### Getting started

Read the current code license and MODEL_LICENSE, then follow hardware guidance to install source and appropriate weights. See the [official README](https://github.com/multimodal-art-projection/YuE/blob/main/README.md).

### Review and provenance

Provides staged inference, editable music plans and hardware adaptation, with weight restrictions stated separately. Recent maintenance: [implementation commit](https://github.com/multimodal-art-projection/YuE/commit/d2427d03db38e0054a1b96019f9add4e409bb08f) (2026-11-01T05:38:47Z). Reviewed implementation gating Intel XPU graphs on opt-in and runtime APIs and reporting the actual device, with regression tests.

Discovered through a third-party index of 逛逛GitHub articles. The index records the articles below; the original WeChat pages were not read in this review. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.


Public articles published or authorized by the author were also checked for attribution, date and repository links. See the additional links in the Chinese section.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:34:39.811Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "yue",
    "name": "YuE2 推理代码 / YuE2 inference code",
    "repository": "multimodal-art-projection/YuE",
    "repo_node_id": "R_kgDONuVFoA",
    "category": "media",
    "tags": [],
    "forms": [
      "library",
      "cli",
      "skill"
    ],
    "platforms": [
      "linux"
    ],
    "aliases": {
      "zh-CN": [
        "YuE2 推理代码 / YuE2 inference code"
      ],
      "en": [
        "YuE2 推理代码 / YuE2 inference code"
      ]
    },
    "summary": {
      "zh-CN": "通过可编辑旋律与和弦计划生成包含人声和伴奏的歌曲。",
      "en": "Generates vocals and accompaniment from editable melody and chord plans."
    },
    "use_cases": {
      "zh-CN": [
        "实验歌曲生成与乐谱编辑"
      ],
      "en": [
        "Experiment with song generation and composition editing"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:34:39.811Z",
        "en": "2026-11-16T14:34:39.811Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
      "source_url": "https://github.com/multimodal-art-projection/YuE/blob/main/LICENSE",
      "reviewed_at": "2026-11-16T14:34:39.811Z"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/multimodal-art-projection/YuE/commit/d2427d03db38e0054a1b96019f9add4e409bb08f",
        "occurred_at": "2026-11-01T05:38:47Z",
        "reason": {
          "zh-CN": "已核对实现：Intel XPU图执行同时检查用户开关与运行时API，并报告实际设备；含回归测试。",
          "en": "Reviewed implementation gating Intel XPU graphs on opt-in and runtime APIs and reporting the actual device, with regression tests."
        },
        "reviewed_at": "2026-11-16T14:34:39.811Z",
        "qualifies": true
      }
    ],
    "sources": [
      {
        "url": "https://github.com/multimodal-art-projection/YuE/blob/main/README.md",
        "accessed_at": "2026-11-16T14:34:39.811Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/multimodal-art-projection/YuE/blob/main/LICENSE",
        "accessed_at": "2026-11-16T14:34:39.811Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.noking.tech/github-radar/data/library.json",
        "accessed_at": "2026-11-16T14:34:39.811Z",
        "supports": {
          "zh-CN": "第三方索引中的公众号文章归属、时间与项目发现线索；非原文阅读证据。",
          "en": "Third-party account attribution, article dates and discovery leads; not proof of reading the originals."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537876&idx=1&sn=8ba02c7b1a619f84c1bb1f5ea34c1856",
        "accessed_at": "2026-11-16T14:34:39.811Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-10-19 玩了一天 1.2 万人收藏的开源音乐模型，真的惊艳到我了。。。；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-10-19; not directly read in this review."
        }
      },
      {
        "url": "https://www.woshipm.com/ai/6480800.html",
        "accessed_at": "2026-11-16T14:26:01.272867+00:00",
        "published_date": "2026-10-20",
        "author": "逛逛GitHub",
        "supports": {
          "zh-CN": "作者公开发表或授权的文章；已核对署名、日期与仓库链接。",
          "en": "Author-published or authorized public article; attribution, date and repository links checked."
        }
      }
    ],
    "quality_review": {
      "basis": {
        "zh-CN": "提供分阶段推理、可编辑音乐计划和硬件适配实现；权重限制单独列明。",
        "en": "Provides staged inference, editable music plans and hardware adaptation, with weight restrictions stated separately."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDONuVFoA",
    "full_name": "multimodal-art-projection/YuE",
    "stargazers_count": 13534,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
    "last_success_at": "2026-11-16T14:19:22.087Z"
  }
}
```

</details>

