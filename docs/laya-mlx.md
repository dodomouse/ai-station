# Laya-MLX

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[mizorewww/laya-mlx](https://github.com/mizorewww/laya-mlx)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 7107 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:47:41.417Z |

## 中文

在Apple Silicon上用MLX运行结构化选择、评分和真假判断模型。

### 用途与功能

- 本地执行受约束分类与决策

用一次双向前向计算输出类型化结果和概率，提供路由、校准和批处理接口。

### 环境与限制

需Apple Silicon、macOS14+与Python3.11+。这是独立移植，训练、CUDA、ONNX、PyTorch后端和vegaml引擎不在范围内。权重另取自上游，性能数字未在本机复测。

### 开始使用

安装laya-mlx后，按README下载适合的权重并先运行一个受约束问题示例。 参阅[官方 README](https://github.com/mizorewww/laya-mlx/blob/main/README.md)。

### 收录与来源

有原生MLX编码器、决策头和上游接口对齐实现，适合特定本地推理需求。 最近维护：[实现提交](https://github.com/mizorewww/laya-mlx/commit/c8a7aa92b4a2ce2502aada08071c81943d1b9299)（2026-11-16T09:21:25Z）。已核对移植提交中的校准、batch大小和置信度校验实现及测试。

通过逛逛GitHub的第三方文章索引发现。索引记录了下列文章；本次未读取微信原文，不据此声称已阅读全文。

- 2026-09-26：[一周就收割 2 万 Star，这个 GitHub 项目把近期爆火的 Jev 模型开源了。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537349&idx=1&sn=bfedd504e5736caa5c5e3ce449cc15b7)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。

## English

Runs structured selection, scoring and boolean decisions through MLX on Apple Silicon.

### Uses and features

- Run local constrained classification and decisions

Produces typed results and probabilities from a bidirectional forward pass, with routing, calibration and batching interfaces.

### Requirements and limits

Requires Apple Silicon, macOS 14+ and Python 3.11+. This independent port excludes training, CUDA, ONNX, PyTorch backends and the vegaml engine. Weights come from upstream; performance figures were not reproduced locally.

### Getting started

Install laya-mlx, load an appropriate checkpoint and start with a constrained-question example. See the [official README](https://github.com/mizorewww/laya-mlx/blob/main/README.md).

### Review and provenance

Implements a native MLX encoder, decision heads and upstream API compatibility for local inference. Recent maintenance: [implementation commit](https://github.com/mizorewww/laya-mlx/commit/c8a7aa92b4a2ce2502aada08071c81943d1b9299) (2026-11-16T09:21:25Z). Reviewed the port's calibration, batch-size and confidence validation implementation and tests.

Discovered through a third-party index of 逛逛GitHub articles. The index records the articles below; the original WeChat pages were not read in this review. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:47:41.417Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "laya-mlx",
    "name": "Laya-MLX",
    "repository": "mizorewww/laya-mlx",
    "repo_node_id": "R_kgDOUhaUgA",
    "category": "ai",
    "tags": [],
    "forms": [
      "library",
      "cli"
    ],
    "platforms": [
      "macos"
    ],
    "aliases": {
      "zh-CN": [
        "Laya-MLX"
      ],
      "en": [
        "Laya-MLX"
      ]
    },
    "summary": {
      "zh-CN": "在Apple Silicon上用MLX运行结构化选择、评分和真假判断模型。",
      "en": "Runs structured selection, scoring and boolean decisions through MLX on Apple Silicon."
    },
    "use_cases": {
      "zh-CN": [
        "本地执行受约束分类与决策"
      ],
      "en": [
        "Run local constrained classification and decisions"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:47:41.417Z",
        "en": "2026-11-16T14:47:41.417Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "a6cba85bc92e0cff7a450b1d873c0eaa2e9fc96bf472df0247a26bec77bf3ff9",
      "source_url": "https://github.com/mizorewww/laya-mlx/blob/main/LICENSE",
      "reviewed_at": "2026-11-16T14:47:41.417Z"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/mizorewww/laya-mlx/commit/c8a7aa92b4a2ce2502aada08071c81943d1b9299",
        "occurred_at": "2026-11-16T09:21:25Z",
        "reason": {
          "zh-CN": "已核对移植提交中的校准、batch大小和置信度校验实现及测试。",
          "en": "Reviewed the port's calibration, batch-size and confidence validation implementation and tests."
        },
        "reviewed_at": "2026-11-16T14:47:41.417Z",
        "qualifies": true
      }
    ],
    "sources": [
      {
        "url": "https://github.com/mizorewww/laya-mlx/blob/main/README.md",
        "accessed_at": "2026-11-16T14:47:41.417Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/mizorewww/laya-mlx/blob/main/LICENSE",
        "accessed_at": "2026-11-16T14:47:41.417Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.noking.tech/github-radar/data/library.json",
        "accessed_at": "2026-11-16T14:47:41.417Z",
        "supports": {
          "zh-CN": "第三方索引中的公众号文章归属、时间与项目发现线索；非原文阅读证据。",
          "en": "Third-party account attribution, article dates and discovery leads; not proof of reading the originals."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537349&idx=1&sn=bfedd504e5736caa5c5e3ce449cc15b7",
        "accessed_at": "2026-11-16T14:47:41.417Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-09-26 一周就收割 2 万 Star，这个 GitHub 项目把近期爆火的 Jev 模型开源了。；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-09-26; not directly read in this review."
        }
      }
    ],
    "quality_review": {
      "basis": {
        "zh-CN": "有原生MLX编码器、决策头和上游接口对齐实现，适合特定本地推理需求。",
        "en": "Implements a native MLX encoder, decision heads and upstream API compatibility for local inference."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOUhaUgA",
    "full_name": "mizorewww/laya-mlx",
    "stargazers_count": 7107,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "a6cba85bc92e0cff7a450b1d873c0eaa2e9fc96bf472df0247a26bec77bf3ff9",
    "last_success_at": "2026-11-16T14:20:00.235Z"
  }
}
```

</details>

