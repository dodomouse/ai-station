# Subvox

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[joeblau/subvox](https://github.com/joeblau/subvox)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 838 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:58:29.135174Z |

## 中文

研究 AirPods 头部运动数据能否识别无声口型的小词汇量实验原型。

### 主要功能

- 录制模板，并使用动态时间规整匹配。
- 提供留一评估、置换检验和混淆矩阵，便于检查是否优于随机结果。

### 环境与限制

- 需要 macOS 14+、支持头部追踪的耳机、Xcode 与运动权限。
- 不是通用语音识别产品，现有证据只支持实验价值，长期维护仍待观察。

### 开始使用

从[官方说明](https://github.com/joeblau/subvox/blob/main/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/joeblau/subvox/releases)可用于确认版本。

### 收录复核

研究 AirPods 头部运动数据能否识别无声口型的小词汇量实验原型。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。 Star 较少，依据具体用途、实现和可复核文档收录；未据此推断成熟度或持续维护能力。

有效维护证据：[591d028385](https://github.com/joeblau/subvox/commit/591d02838521c3d33107bc9fde1a6fd620f96d58)，2026-10-31T01:49:43Z。首次加入采集、训练和解码应用实现；已检查应用状态与入口代码。

文章来源：[逛逛GitHub署名文章](https://www.woshipm.com/share/6491690.html)，平台日期 2026-11-10。已通过公开正文核对仓库链接与作者归属；微信正文未直接读取。

本次为文档与实现证据复核，未安装或运行上游项目。

## English

A small-vocabulary prototype testing whether AirPods head-motion data can identify silently mouthed words.

### Features

- Records templates and matches them with dynamic time warping.
- Provides leave-one-out evaluation, permutation testing and confusion matrices to assess performance against chance.

### Requirements and limits

- Requires macOS 14+, head-tracking headphones, Xcode and Motion permission.
- It is not general speech recognition
- current evidence supports experimental value, while long-term maintenance remains unproven.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/joeblau/subvox/blob/main/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/joeblau/subvox/releases) for versions.

### Review and provenance

A small-vocabulary prototype testing whether AirPods head-motion data can identify silently mouthed words. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable. Included despite limited Stars because the use case, implementation and documentation are inspectable; popularity is not treated as evidence of maturity or sustained maintenance.

Activity: [591d028385](https://github.com/joeblau/subvox/commit/591d02838521c3d33107bc9fde1a6fd620f96d58), 2026-10-31T01:49:43Z. Initial capture, training and decoding application; reviewed application state and entry-point code.

Discovery: [an author-attributed 逛逛GitHub article](https://www.woshipm.com/share/6491690.html), dated 2026-11-10 on the public platform. Repository links and attribution were checked in its public body; the WeChat body was not read directly.

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
    "id": "subvox",
    "name": "Subvox",
    "repository": "joeblau/subvox",
    "repo_node_id": "R_kgDOVdrchw",
    "category": "media",
    "summary": {
      "zh-CN": "研究 AirPods 头部运动数据能否识别无声口型的小词汇量实验原型。",
      "en": "A small-vocabulary prototype testing whether AirPods head-motion data can identify silently mouthed words."
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
      "zh-CN": "研究 AirPods 头部运动数据能否识别无声口型的小词汇量实验原型。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。 Star 较少，依据具体用途、实现和可复核文档收录；未据此推断成熟度或持续维护能力。",
      "en": "A small-vocabulary prototype testing whether AirPods head-motion data can identify silently mouthed words. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable. Included despite limited Stars because the use case, implementation and documentation are inspectable; popularity is not treated as evidence of maturity or sustained maintenance.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "38bcdd63b567dabb0d6c8f5e2b68bbe120d40c405ac8026981557d944d6cd2b4",
      "source_url": "https://github.com/joeblau/subvox/blob/591d02838521c3d33107bc9fde1a6fd620f96d58/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "Root license reviewed. External dependencies and assets retain their individual licenses.",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "591d02838521c3d33107bc9fde1a6fd620f96d58"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-10-31T01:49:43Z",
        "reviewed_at": "2026-11-16T14:58:29.135174Z",
        "url": "https://github.com/joeblau/subvox/commit/591d02838521c3d33107bc9fde1a6fd620f96d58",
        "qualifies": true,
        "reason": {
          "zh-CN": "首次加入采集、训练和解码应用实现；已检查应用状态与入口代码。",
          "en": "Initial capture, training and decoding application; reviewed application state and entry-point code."
        },
        "reviewed_files": [
          "Subvox/App/AppModel.swift",
          "Subvox/App/SubvoxApp.swift"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/joeblau/subvox",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/joeblau/subvox/blob/main/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/joeblau/subvox/blob/591d02838521c3d33107bc9fde1a6fd620f96d58/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/joeblau/subvox/commit/591d02838521c3d33107bc9fde1a6fd620f96d58",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://www.woshipm.com/share/6491690.html",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      }
    ],
    "article_source": {
      "article_id": "2247538431_1",
      "title": "把你的 AirPods 当鼠标用，这 3 个黑科技 GitHub 开源项目有趣。",
      "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538431&idx=1&sn=74a9f0be88c711205e42507b6b8e2b92",
      "published_date": "2026-11-10",
      "account": "逛逛GitHub",
      "content_review_url": "https://www.woshipm.com/share/6491690.html",
      "content_review_kind": "author-attributed public article",
      "wechat_direct_body_read": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVdrchw",
    "full_name": "joeblau/subvox",
    "stargazers_count": 838,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "38bcdd63b567dabb0d6c8f5e2b68bbe120d40c405ac8026981557d944d6cd2b4",
    "last_success_at": "2026-11-16T14:58:29.135174Z"
  }
}
```

</details>
