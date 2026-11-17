# Screenshot to Code

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[abi/screenshot-to-code](https://github.com/abi/screenshot-to-code)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 81243 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:58:29.135174Z |

## 中文

根据截图、设计图或录屏生成网页界面代码，并迭代调整。

### 主要功能

- 支持多种输出路径，包括 HTML、React 和 Vue。
- 可配置模型，并通过可选浏览器预览检查生成结果。

### 环境与限制

- 本机运行包含 React/Vite 前端与 FastAPI 后端，需要模型服务凭据。
- 输入图片会发送至配置的服务，生成代码仍需审查与测试。

### 开始使用

从[官方说明](https://github.com/abi/screenshot-to-code/blob/main/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/abi/screenshot-to-code/releases)可用于确认版本。

### 收录复核

根据截图、设计图或录屏生成网页界面代码，并迭代调整。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。

有效维护证据：[a8139779f7](https://github.com/abi/screenshot-to-code/commit/a8139779f7c5ae231b7f2a86fa7f83ddc5f7badc)，2026-10-09T19:42:15Z。修改后端编辑模式的模型选择并同步回归测试。

文章来源：[逛逛GitHub署名文章](https://www.woshipm.com/ai/6460165.html)，平台日期 2026-09-05。已通过公开正文核对仓库链接与作者归属；微信正文未直接读取。

本次为文档与实现证据复核，未安装或运行上游项目。

## English

Generates and iterates on web-interface code from screenshots, designs or screen recordings.

### Features

- Supports HTML, React, Vue and other output paths.
- Uses configurable models and optional browser previews to inspect generated pages.

### Requirements and limits

- Local setup uses a React/Vite frontend and FastAPI backend and requires model-provider credentials.
- Input images go to the configured services, and generated code still requires review and testing.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/abi/screenshot-to-code/blob/main/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/abi/screenshot-to-code/releases) for versions.

### Review and provenance

Generates and iterates on web-interface code from screenshots, designs or screen recordings. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.

Activity: [a8139779f7](https://github.com/abi/screenshot-to-code/commit/a8139779f7c5ae231b7f2a86fa7f83ddc5f7badc), 2026-10-09T19:42:15Z. Updates backend model selection for the editing variant and its regression tests.

Discovery: [an author-attributed 逛逛GitHub article](https://www.woshipm.com/ai/6460165.html), dated 2026-09-05 on the public platform. Repository links and attribution were checked in its public body; the WeChat body was not read directly.

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
    "id": "screenshot-to-code",
    "name": "Screenshot to Code",
    "repository": "abi/screenshot-to-code",
    "repo_node_id": "R_kgDOKtchNQ",
    "category": "development",
    "summary": {
      "zh-CN": "根据截图、设计图或录屏生成网页界面代码，并迭代调整。",
      "en": "Generates and iterates on web-interface code from screenshots, designs or screen recordings."
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
      "zh-CN": "根据截图、设计图或录屏生成网页界面代码，并迭代调整。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。",
      "en": "Generates and iterates on web-interface code from screenshots, designs or screen recordings. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "a264aef6acfaf75d9dcf0600a984f0f0ad0a36c2961013f530e2367d66201fd7",
      "source_url": "https://github.com/abi/screenshot-to-code/blob/f2e5bbdd1dd5d93c259548d9bccf54e2a5f06a30/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "Root license reviewed. External dependencies and assets retain their individual licenses.",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "f2e5bbdd1dd5d93c259548d9bccf54e2a5f06a30"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-10-09T19:42:15Z",
        "reviewed_at": "2026-11-16T14:58:29.135174Z",
        "url": "https://github.com/abi/screenshot-to-code/commit/a8139779f7c5ae231b7f2a86fa7f83ddc5f7badc",
        "qualifies": true,
        "reason": {
          "zh-CN": "修改后端编辑模式的模型选择并同步回归测试。",
          "en": "Updates backend model selection for the editing variant and its regression tests."
        },
        "reviewed_files": [
          "backend/routes/model_choice_sets.py",
          "backend/tests/test_model_selection.py"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/abi/screenshot-to-code",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/abi/screenshot-to-code/blob/main/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/abi/screenshot-to-code/blob/f2e5bbdd1dd5d93c259548d9bccf54e2a5f06a30/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/abi/screenshot-to-code/commit/a8139779f7c5ae231b7f2a86fa7f83ddc5f7badc",
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
    "repo_node_id": "R_kgDOKtchNQ",
    "full_name": "abi/screenshot-to-code",
    "stargazers_count": 81243,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "a264aef6acfaf75d9dcf0600a984f0f0ad0a36c2961013f530e2367d66201fd7",
    "last_success_at": "2026-11-16T14:58:29.135174Z"
  }
}
```

</details>
