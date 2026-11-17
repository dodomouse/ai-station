# TimesFM（开源代码与 ≤2.5 权重）

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[google-research/timesfm](https://github.com/google-research/timesfm)

| 项目 / Field | 内容 / Value |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 35602 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:50:50.290410+00:00 |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:47:50.765Z |

## 中文

Google Research 的时间序列预测代码库。提供预训练模型调用、分位数预测和协变量支持。本词条收录 Apache-2.0 源代码及 2.5 或更早的开源权重。

**环境与限制：** 使用 Python 环境及所选 PyTorch、Flax 或 MLX 后端，资源要求取决于模型和批量大小。3.0 权重另受非商业、非生产许可约束，不属于本词条开源权重范围；Google Cloud 商业服务另有条款。开源版不是 Google 正式支持的产品。

**入门：** 从[官方说明](https://raw.githubusercontent.com/google-research/timesfm/master/README.md)确认安装与配置步骤，再查看[发布版本](https://github.com/google-research/timesfm/releases)。本次为文档、许可原文与维护证据审查，未安装运行。

**近期维护：** [核验 2.5 代码路径的提交，修复可选后端缺失时的属性探测，并增加回归测试。](https://github.com/google-research/timesfm/commit/c22c05b60a9dac9e46d629f618fdbe259fd522dd)（2026-11-10）

## English

Google Research's time-series forecasting codebase provides pretrained-model inference, quantile forecasts and covariate support. This entry covers Apache-2.0 source code and open weights through version 2.5.

**Requirements and limitations:** Requires Python and the selected PyTorch, Flax or MLX backend, with resources depending on model and batch size. Version 3.0 weights have separate non-commercial, non-production terms and are excluded from the open-weight scope; Google Cloud services have separate terms. The open version is not an officially supported Google product.

**Getting started:** Follow the [official documentation](https://raw.githubusercontent.com/google-research/timesfm/master/README.md) for setup, then check [releases](https://github.com/google-research/timesfm/releases). This review examined documentation, license text and maintenance evidence; the software was not installed or run.

**Recent maintenance:** [An inspected commit on the 2.5 code path fixes optional-backend attribute probing and adds regression tests.](https://github.com/google-research/timesfm/commit/c22c05b60a9dac9e46d629f618fdbe259fd522dd) (2026-11-10)

## Review evidence

发现线索来自作者署名转载的公开正文；仓库链接与作者归属已交叉核对，微信正文未直接读取。用途、环境、许可与维护状态依据仓库当前资料复核。

Discovery uses an author-attributed public repost with corroborated repository links and attribution; the WeChat body was not read directly. Current repository sources were reviewed for function, requirements, licensing and maintenance.

- 作者署名转载 / Author-attributed repost：[GitHub 周报：科研、语音、SEO，一个清单看懂 14 个 AI 项目](https://www.woshipm.com/ai/6460165.html)（2026-09-05）；仓库链接映射已交叉核对 / repository mapping corroborated.

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-16T14:50:50.290410+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "timesfm",
    "name": "TimesFM（开源代码与 ≤2.5 权重）",
    "repository": "google-research/timesfm",
    "repo_node_id": "R_kgDOL1Au9w",
    "category": "ai",
    "summary": {
      "zh-CN": "Google Research 的时间序列预测代码库，提供预训练模型调用、分位数预测和协变量支持；本词条收录 Apache-2.0 源代码及 2.5 或更早的开源权重。",
      "en": "Google Research's time-series forecasting codebase provides pretrained-model inference, quantile forecasts and covariate support. This entry covers Apache-2.0 source code and open weights through version 2.5."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:50:50.290410+00:00",
        "en": "2026-11-16T14:50:50.290410+00:00"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
      "source_url": "https://github.com/google-research/timesfm/blob/918df02c9d366b2145bc5876135fa2131d3ed2a6/LICENSE",
      "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
      "files": [
        {
          "path": "LICENSE",
          "source_url": "https://github.com/google-research/timesfm/blob/918df02c9d366b2145bc5876135fa2131d3ed2a6/LICENSE",
          "fetched_at": "2026-11-16T14:48:18.547Z",
          "sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
          "source_commit": "918df02c9d366b2145bc5876135fa2131d3ed2a6"
        }
      ],
      "scope": "Apache-2.0 source code and model weights through 2.5 only. TimesFM 3.0 weights are non-commercial/non-production and excluded; cloud offerings have separate terms.",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "918df02c9d366b2145bc5876135fa2131d3ed2a6"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-10T17:38:06Z",
        "url": "https://github.com/google-research/timesfm/commit/c22c05b60a9dac9e46d629f618fdbe259fd522dd",
        "sha": "c22c05b60a9dac9e46d629f618fdbe259fd522dd",
        "summary": "fix(timesfm): keep the optional-backend error an AttributeError",
        "files": [
          "src/timesfm/__init__.py",
          "tests/test_optional_backend_errors.py"
        ],
        "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
        "qualifies": true,
        "reason": {
          "zh-CN": "核验 2.5 代码路径的提交，修复可选后端缺失时的属性探测，并增加回归测试。",
          "en": "An inspected commit on the 2.5 code path fixes optional-backend attribute probing and adds regression tests."
        }
      }
    ],
    "sources": [
      {
        "url": "https://www.woshipm.com/ai/6460165.html",
        "title": "GitHub 周报：科研、语音、SEO，一个清单看懂 14 个 AI 项目",
        "published_date": "2026-09-05",
        "account": "逛逛GitHub",
        "source_strength": "author_attributed_repost_repository_mapping",
        "author_attribution_confirmed": true,
        "body_read_method": "public_html_repository_links_and_attribution_extraction",
        "full_text_archived": false
      }
    ],
    "discovery": {
      "account": "逛逛GitHub",
      "window_start": "2026-08-16",
      "window_end": "2026-11-16",
      "original_article_body_read": false,
      "repository_review_sources": [
        "https://api.github.com/repos/google-research/timesfm",
        "https://raw.githubusercontent.com/google-research/timesfm/master/README.md",
        "https://github.com/google-research/timesfm/commit/c22c05b60a9dac9e46d629f618fdbe259fd522dd",
        "https://github.com/google-research/timesfm/blob/918df02c9d366b2145bc5876135fa2131d3ed2a6/LICENSE"
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOL1Au9w",
    "full_name": "google-research/timesfm",
    "stargazers_count": 35602,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
    "last_success_at": "2026-11-16T14:47:50.765Z"
  }
}
```

</details>
