# MiniMind

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[jingyaogong/minimind](https://github.com/jingyaogong/minimind)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 65498 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:50:00.739Z |

## 中文

用较小语言模型学习从预训练、微调到推理服务的完整实现。

### 用途与功能

- 学习语言模型训练流程
- 在有限资源上做训练实验

提供原生PyTorch模型、数据处理、预训练、SFT、LoRA、偏好训练、工具调用和服务示例。

### 环境与限制

README使用Python3.10.16及其依赖栈；GPU、显存和训练时长取决于任务。宣传的两小时指特定3090上SFT单轮，不能当作从零全流程承诺。训练数据与权重应另核许可，教学模型能力有限。

### 开始使用

按README安装依赖，先运行预训练模型推理，再选择小数据与匹配硬件复现一个训练阶段。 参阅[官方 README](https://github.com/jingyaogong/minimind/blob/master/README.md)。

### 收录与来源

公开完整模型与训练实现，并有可运行推理服务及回归测试。 最近维护：[实现提交](https://github.com/jingyaogong/minimind/commit/d80c69254309c4dc457e9ab926d6987725e1cf2b)（2026-10-27T06:52:51Z）。已核对合并实现：修复OpenAI兼容流式服务中工具调用与普通内容分段，并新增测试。

来源为2026-09-05公开转载文章，文末明确署名逛逛GitHub；已从公开正文提取仓库链接。

- 2026-09-05：[GitHub 周报：科研、语音、SEO，一个清单看懂 14 个 AI 项目](https://www.woshipm.com/ai/6460165.html)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。

## English

Teaches language-model implementation from pretraining and fine-tuning to inference serving using small models.

### Uses and features

- Learn language-model training workflows
- Run training experiments with limited resources

Provides native PyTorch models, data processing, pretraining, SFT, LoRA, preference training, tool use and serving examples.

### Requirements and limits

The README uses Python 3.10.16 and its dependency stack. GPU memory and duration depend on the task. The advertised two hours refers to one SFT epoch on a specific 3090 setup, not an end-to-end training promise. Check data and checkpoint terms separately; educational model capabilities are limited.

### Getting started

Install documented dependencies, first run checkpoint inference, then reproduce one training stage with a small dataset and suitable hardware. See the [official README](https://github.com/jingyaogong/minimind/blob/master/README.md).

### Review and provenance

Publishes model and training implementation with runnable inference services and regression tests. Recent maintenance: [implementation commit](https://github.com/jingyaogong/minimind/commit/d80c69254309c4dc457e9ab926d6987725e1cf2b) (2026-10-27T06:52:51Z). Reviewed merged implementation fixing tool-call and text segmentation in OpenAI-compatible streaming, with new tests.

The source is a public republication dated 2026-09-05 with explicit attribution to 逛逛GitHub; repository links were extracted from its public body. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:50:00.739Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "minimind",
    "name": "MiniMind",
    "repository": "jingyaogong/minimind",
    "repo_node_id": "R_kgDOMbt5gA",
    "category": "ai",
    "tags": [],
    "forms": [
      "library",
      "cli",
      "service"
    ],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "MiniMind"
      ],
      "en": [
        "MiniMind"
      ]
    },
    "summary": {
      "zh-CN": "用较小语言模型学习从预训练、微调到推理服务的完整实现。",
      "en": "Teaches language-model implementation from pretraining and fine-tuning to inference serving using small models."
    },
    "use_cases": {
      "zh-CN": [
        "学习语言模型训练流程",
        "在有限资源上做训练实验"
      ],
      "en": [
        "Learn language-model training workflows",
        "Run training experiments with limited resources"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:50:00.739Z",
        "en": "2026-11-16T14:50:00.739Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4",
      "source_url": "https://github.com/jingyaogong/minimind/blob/233d00fa068ec2b8c0d4f07b703934d6391a5a73/LICENSE",
      "reviewed_at": "2026-11-16T14:50:00.739Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "233d00fa068ec2b8c0d4f07b703934d6391a5a73"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/jingyaogong/minimind/commit/d80c69254309c4dc457e9ab926d6987725e1cf2b",
        "occurred_at": "2026-10-27T06:52:51Z",
        "reason": {
          "zh-CN": "已核对合并实现：修复OpenAI兼容流式服务中工具调用与普通内容分段，并新增测试。",
          "en": "Reviewed merged implementation fixing tool-call and text segmentation in OpenAI-compatible streaming, with new tests."
        },
        "reviewed_at": "2026-11-16T14:50:00.739Z",
        "qualifies": true
      }
    ],
    "sources": [
      {
        "url": "https://github.com/jingyaogong/minimind/blob/master/README.md",
        "accessed_at": "2026-11-16T14:50:00.739Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/jingyaogong/minimind/blob/233d00fa068ec2b8c0d4f07b703934d6391a5a73/LICENSE",
        "accessed_at": "2026-11-16T14:50:00.739Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.woshipm.com/ai/6460165.html",
        "accessed_at": "2026-11-16T14:50:00.307Z",
        "supports": {
          "zh-CN": "已核对作者署名、日期与正文仓库链接。",
          "en": "Verified author attribution, date and repository links in the public article body."
        }
      }
    ],
    "quality_review": {
      "basis": {
        "zh-CN": "公开完整模型与训练实现，并有可运行推理服务及回归测试。",
        "en": "Publishes model and training implementation with runnable inference services and regression tests."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOMbt5gA",
    "full_name": "jingyaogong/minimind",
    "stargazers_count": 65498,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4",
    "last_success_at": "2026-11-16T14:35:03.066Z"
  }
}
```

</details>

