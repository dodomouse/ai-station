# Garden Skills

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[ConardLi/garden-skills](https://github.com/ConardLi/garden-skills)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 15316 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T04:07:37.962114+00:00 |

## 中文

为 AI 编程智能体提供可复用的技能、脚本和模板。覆盖网页设计、演示内容、图像创作与本地知识检索。

### 用途与功能

- 提供网页设计、文章排版和演示文稿制作的分步工作流。
- 包含代码视频、图像生成及配套脚本和参考模板。
- 通过 kb-retriever 逐步检索本地知识文件并保留来源。

### 环境与限制

需要支持 Skill 的智能体；各技能还可能依赖 Node.js、浏览器、媒体工具或图像/TTS 服务。模型调用和素材许可需单独确认。MIT 覆盖仓库自身代码与技能，外部引用资料和第三方素材保留各自权利。

### 开始使用

先阅读技能自身依赖和操作步骤。按 README 用 skills CLI 或插件入口安装所需技能，也可从发行版选择固定版本。

参阅[官方 README](https://github.com/ConardLi/garden-skills/blob/9578a34edf3c359da23d8a632b72790834961d11/README.md)。

### 收录与来源

适合把重复的内容制作与设计步骤交给已有智能体，并复用模板和检查流程。

维护证据：[修复演示模板的自动播放启动按键同时推进页面、跳过首步的问题](https://github.com/ConardLi/garden-skills/commit/4112001f4b6fb3c8011fae0637977a37b590519f)（2026-11-14）。

发现于 [GitHub 月榜](https://github.com/trending/javascript?since=monthly)。2026-11-17 的榜单记录新增 2,426 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Reusable skills, scripts and templates for AI coding agents, covering web design, presentations, image creation and local knowledge retrieval.

### Uses and features

- Provide staged workflows for web design, article layout and presentations.
- Include code-rendered video and image-generation workflows with scripts and reference templates.
- Use kb-retriever to search local knowledge files progressively with source references.

### Requirements and limits

Requires a skill-capable agent. Individual skills may also need Node.js, a browser, media tools, or image/TTS services. Model usage and asset licenses need separate review. MIT covers the repository’s own code and skills; external reference material and third-party assets retain their own rights.

### Getting started

Install selected skills through the skills CLI or plugin instructions, or choose a pinned release. Read each skill’s dependencies and workflow before use.

See the [official README](https://github.com/ConardLi/garden-skills/blob/9578a34edf3c359da23d8a632b72790834961d11/README.md).

### Review and provenance

Useful for reusing templates and review steps when an existing agent handles recurring design and content-production work.

Maintenance evidence: [Fixes the presentation template’s autoplay start key also advancing the cursor and skipping the first step](https://github.com/ConardLi/garden-skills/commit/4112001f4b6fb3c8011fae0637977a37b590519f) (2026-11-14).

Discovered in [GitHub monthly Trending](https://github.com/trending/javascript?since=monthly), which recorded 2,426 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:07:37.962114+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "garden-skills",
    "name": "Garden Skills",
    "repository": "ConardLi/garden-skills",
    "repo_node_id": "R_kgDOSIk_Sw",
    "category": "development",
    "summary": {
      "zh-CN": "为 AI 编程智能体提供可复用的技能、脚本和模板。覆盖网页设计、演示内容、图像创作与本地知识检索。",
      "en": "Reusable skills, scripts and templates for AI coding agents, covering web design, presentations, image creation and local knowledge retrieval."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:07:37.962114+00:00",
        "en": "2026-11-17T04:07:37.962114+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合把重复的内容制作与设计步骤交给已有智能体，并复用模板和检查流程。",
      "en": "Useful for reusing templates and review steps when an existing agent handles recurring design and content-production work.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/ConardLi/garden-skills/blob/9578a34edf3c359da23d8a632b72790834961d11/LICENSE",
      "license_sha256": "1126322e2cc8d165adc4c792eeb195717de2bcc7b39be1ce77959d78e87ef685",
      "source_commit": "9578a34edf3c359da23d8a632b72790834961d11",
      "reviewed_at": "2026-11-17T04:07:37.962114+00:00",
      "evidence_pinned_at": "2026-11-17T04:07:37.962114+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "MIT covers original repository code and skills. Referenced external prompts, assets, model services and generated content require their own rights review."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-14T15:06:47Z",
        "reviewed_at": "2026-11-17T04:07:37.962114+00:00",
        "url": "https://github.com/ConardLi/garden-skills/commit/4112001f4b6fb3c8011fae0637977a37b590519f",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复演示模板的自动播放启动按键同时推进页面、跳过首步的问题",
          "en": "Fixes the presentation template’s autoplay start key also advancing the cursor and skipping the first step"
        },
        "reviewed_files": [
          "skills/web-video-presentation/templates/src/App.tsx",
          "skills/web-video-presentation/templates/src/hooks/useStepper.ts"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/ConardLi/garden-skills",
        "accessed_at": "2026-11-17T04:07:37.962114+00:00"
      },
      {
        "url": "https://github.com/ConardLi/garden-skills/blob/9578a34edf3c359da23d8a632b72790834961d11/README.md",
        "accessed_at": "2026-11-17T04:07:37.962114+00:00"
      },
      {
        "url": "https://github.com/ConardLi/garden-skills/blob/9578a34edf3c359da23d8a632b72790834961d11/LICENSE",
        "accessed_at": "2026-11-17T04:07:37.962114+00:00"
      },
      {
        "url": "https://github.com/ConardLi/garden-skills/commit/4112001f4b6fb3c8011fae0637977a37b590519f",
        "accessed_at": "2026-11-17T04:07:37.962114+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 2426,
      "source_url": "https://github.com/trending/javascript?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOSIk_Sw",
    "full_name": "ConardLi/garden-skills",
    "stargazers_count": 15316,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "1126322e2cc8d165adc4c792eeb195717de2bcc7b39be1ce77959d78e87ef685",
    "last_success_at": "2026-11-17T03:53:42.595693+00:00"
  }
}
```

</details>
