# Heretic

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[p-e-w/heretic](https://github.com/p-e-w/heretic)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 40743 |
| 许可证 / License | AGPL-3.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:58:29.135174Z |

## 中文

通过免训练的参数修改研究语言模型的回答风格、拒答与迎合行为。

### 主要功能

- 根据对照提示与评分器搜索行为修改参数。
- 支持配置、模型导出与可复现的修改记录。

### 环境与限制

- 需要 Python 3.10+、PyTorch 2.6+ 及足够运行目标模型的硬件。
- 代码采用 AGPL-3.0，模型权重另有许可，修改后能力与行为需要重新评估。

### 开始使用

从[官方说明](https://github.com/p-e-w/heretic/blob/master/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/p-e-w/heretic/releases)可用于确认版本。

### 收录复核

通过免训练的参数修改研究语言模型的回答风格、拒答与迎合行为。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。

有效维护证据：[v2.1.0](https://github.com/p-e-w/heretic/releases/tag/v2.1.0)，2026-11-08T07:14:03Z。已核对正式发行 v2.1.0 的发布状态与时间。

文章来源：[逛逛GitHub署名文章](https://www.woshipm.com/ai/6460165.html)，平台日期 2026-09-05。已通过公开正文核对仓库链接与作者归属；微信正文未直接读取。

本次为文档与实现证据复核，未安装或运行上游项目。

## English

A tool for studying language-model style, refusal and sycophancy through training-free parameter modification.

### Features

- Searches behavior-modification parameters using contrasting prompts and scorers.
- Supports configuration, model export and reproducible modification records.

### Requirements and limits

- Requires Python 3.10+, PyTorch 2.6+ and hardware capable of running the target model.
- Code is AGPL-3.0 and weights have separate licenses
- capabilities and behavior need reevaluation after modification.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/p-e-w/heretic/blob/master/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/p-e-w/heretic/releases) for versions.

### Review and provenance

A tool for studying language-model style, refusal and sycophancy through training-free parameter modification. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.

Activity: [v2.1.0](https://github.com/p-e-w/heretic/releases/tag/v2.1.0), 2026-11-08T07:14:03Z. Checked the non-draft, non-prerelease publication v2.1.0 and its date.

Discovery: [an author-attributed 逛逛GitHub article](https://www.woshipm.com/ai/6460165.html), dated 2026-09-05 on the public platform. Repository links and attribution were checked in its public body; the WeChat body was not read directly.

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
    "id": "heretic",
    "name": "Heretic",
    "repository": "p-e-w/heretic",
    "repo_node_id": "R_kgDOPz41qA",
    "category": "ai",
    "summary": {
      "zh-CN": "通过免训练的参数修改研究语言模型的回答风格、拒答与迎合行为。",
      "en": "A tool for studying language-model style, refusal and sycophancy through training-free parameter modification."
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
      "zh-CN": "通过免训练的参数修改研究语言模型的回答风格、拒答与迎合行为。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。",
      "en": "A tool for studying language-model style, refusal and sycophancy through training-free parameter modification. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "AGPL-3.0",
      "osi_approved": true,
      "license_sha256": "0d96a4ff68ad6d4b6f1f30f713b18d5184912ba8dd389f86aa7710db079abcb0",
      "source_url": "https://github.com/p-e-w/heretic/blob/master/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "Root license reviewed. External dependencies and assets retain their individual licenses."
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-11-08T07:14:03Z",
        "reviewed_at": "2026-11-16T14:58:29.135174Z",
        "url": "https://github.com/p-e-w/heretic/releases/tag/v2.1.0",
        "qualifies": true,
        "reason": {
          "zh-CN": "已核对正式发行 v2.1.0 的发布状态与时间。",
          "en": "Checked the non-draft, non-prerelease publication v2.1.0 and its date."
        },
        "draft": false,
        "prerelease": false
      }
    ],
    "sources": [
      {
        "url": "https://github.com/p-e-w/heretic",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/p-e-w/heretic/blob/master/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/p-e-w/heretic/blob/master/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/p-e-w/heretic/releases/tag/v2.1.0",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://www.woshipm.com/ai/6460165.html",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      }
    ],
    "article_source": {
      "account": "逛逛GitHub",
      "content_review_url": "https://www.woshipm.com/ai/6460165.html",
      "content_review_kind": "author-attributed public article",
      "wechat_direct_body_read": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOPz41qA",
    "full_name": "p-e-w/heretic",
    "stargazers_count": 40743,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "AGPL-3.0",
    "license_sha256": "0d96a4ff68ad6d4b6f1f30f713b18d5184912ba8dd389f86aa7710db079abcb0",
    "last_success_at": "2026-11-16T14:58:29.135174Z"
  }
}
```
