# Skid Homework

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[cubewhy/skid-homework](https://github.com/cubewhy/skid-homework)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 1947 |
| 许可证 / License | GPL-3.0 |
| 评估时间 / Evaluated at | 2026-11-17T06:06:21.874484+00:00 |

## 中文

在浏览器中调用多模态模型分析题目图片、PDF 和文本，辅助理解解题过程。

### 用途与功能

- 通过拍照或文件导入题目，按题查看 AI 解析并继续提问。
- 可连接 Gemini 或 OpenAI 兼容接口，调整提示词和回答风格。
- 支持公式、图形和图表展示；提供快捷键及实验性的 WebUSB/ADB 截图入口。

### 环境与限制

在电脑、平板或手机浏览器中使用，需自行配置 Gemini 或 OpenAI 兼容服务的 API 密钥及支持相应输入的模型；服务费用、配额和网络限制由供应方决定。OpenAI 模式处理 PDF 或使用联网搜索需要启用 Responses API，并要求接口支持对应能力。题目图片、文件内容、提示词及用于追问的对话会发送到所配置的模型服务；本地截图或保存解析不等于本地推理。ADB 截图还依赖支持 WebUSB 的浏览器和设备授权。AI 解答及图形可能出错，需人工核对。

### 开始使用

打开 README 提供的在线实例或按部署说明自托管，配置模型服务、API 密钥及模型，再用一道不含个人信息的题目图片检查解析和追问。源码开发使用 Node.js 与 pnpm；README 也提供 Docker 部署方法。

参阅[官方 README](https://github.com/cubewhy/skid-homework/blob/8580e3fe6be0f68208b71b6b5df600103a3e2787/README.md)。

### 收录与来源

已核对固定版本 README、GPL-3.0 原文、模型调用实现和近期提交。2026-09-09 的变更修正 Responses API 图片字段及文件 data URL 格式，属于近三个月的实质功能修复。项目适合作为 AI 学习辅助工具收录；未实测模型准确率、浏览器兼容性或部署流程。

维护证据：[修正 Responses API 的 input_image.image_url 字符串结构，为图片和文件统一补齐 data URL 并避免重复前缀](https://github.com/cubewhy/skid-homework/commit/f480330c0155e670795f2238575a6e872c672f08)（2026-09-09）。

用户于 2026-11-17 提供仓库链接。本条按工程通用标准复核，不设 Star 门槛。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

A browser-based study assistant that uses multimodal models to analyze question images, PDFs and text and explain solutions.

### Uses and features

- Import questions from camera captures or files, review AI explanations and ask follow-up questions.
- Connect Gemini or an OpenAI-compatible endpoint and customize prompts and answer style.
- Render mathematical notation, diagrams and plots, with keyboard shortcuts and experimental WebUSB/ADB screenshot capture.

### Requirements and limits

Use a desktop, tablet or phone browser with your own Gemini or OpenAI-compatible API credentials and a model that supports the input format. Provider pricing, quotas and network restrictions apply. In OpenAI mode, PDF input and web search require Responses API mode and a compatible endpoint. Question images, file content, prompts and follow-up conversation are sent to the configured model service; local screenshots or saved explanations do not imply local inference. ADB capture additionally requires a WebUSB-capable browser and device authorization. Review generated answers and diagrams for errors.

### Getting started

Open the hosted instance linked in the README or follow its self-hosting instructions, configure your provider, API key and model, then try analysis and follow-up questions on an image without personal information. Source development uses Node.js and pnpm; the README also documents Docker deployment.

See the [official README](https://github.com/cubewhy/skid-homework/blob/8580e3fe6be0f68208b71b6b5df600103a3e2787/README.md).

### Review and provenance

Reviewed the pinned README, GPL-3.0 text, model clients and recent changes. The 2026-09-09 patch corrects Responses API image fields and file data URLs, providing substantive maintenance within three months. The project fits the catalog as an AI study assistant. Model accuracy, browser compatibility and deployment were not tested.

Maintenance evidence: [Corrects the Responses API input_image.image_url string format and normalizes image/file data URLs without duplicating existing prefixes](https://github.com/cubewhy/skid-homework/commit/f480330c0155e670795f2238575a6e872c672f08) (2026-09-09).

Submitted by the user on 2026-11-17 and reviewed against the general catalog criteria, with no star threshold.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T06:06:21.874484+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "skid-homework",
    "name": "Skid Homework",
    "repository": "cubewhy/skid-homework",
    "repo_node_id": "R_kgDOP3tWeg",
    "category": "ai",
    "summary": {
      "zh-CN": "在浏览器中调用多模态模型分析题目图片、PDF 和文本，辅助理解解题过程。",
      "en": "A browser-based study assistant that uses multimodal models to analyze question images, PDFs and text and explain solutions."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T06:06:21.874484+00:00",
        "en": "2026-11-17T06:06:21.874484+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "已核对固定版本 README、GPL-3.0 原文、模型调用实现和近期提交。2026-09-09 的变更修正 Responses API 图片字段及文件 data URL 格式，属于近三个月的实质功能修复。项目适合作为 AI 学习辅助工具收录；未实测模型准确率、浏览器兼容性或部署流程。",
      "en": "Reviewed the pinned README, GPL-3.0 text, model clients and recent changes. The 2026-09-09 patch corrects Responses API image fields and file data URLs, providing substantive maintenance within three months. The project fits the catalog as an AI study assistant. Model accuracy, browser compatibility and deployment were not tested.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "GPL-3.0",
      "osi_approved": true,
      "source_url": "https://github.com/cubewhy/skid-homework/blob/8580e3fe6be0f68208b71b6b5df600103a3e2787/LICENSE",
      "license_sha256": "4a03dc6eb67c255f17154376ec3b99af63c21820d3ad36703db4eb76acf9d3ce",
      "source_commit": "8580e3fe6be0f68208b71b6b5df600103a3e2787",
      "reviewed_at": "2026-11-17T06:06:21.874484+00:00",
      "evidence_pinned_at": "2026-11-17T06:06:21.874484+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "GPL-3.0 covers the repository software under its root LICENSE; external model services, provider API terms, submitted materials and generated content are not automatically covered by this code license."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-09-09T15:31:05Z",
        "reviewed_at": "2026-11-17T06:06:21.874484+00:00",
        "url": "https://github.com/cubewhy/skid-homework/commit/f480330c0155e670795f2238575a6e872c672f08",
        "qualifies": true,
        "reason": {
          "zh-CN": "修正 Responses API 的 input_image.image_url 字符串结构，为图片和文件统一补齐 data URL 并避免重复前缀",
          "en": "Corrects the Responses API input_image.image_url string format and normalizes image/file data URLs without duplicating existing prefixes"
        },
        "reviewed_files": [
          "src/ai/openai.ts"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/cubewhy/skid-homework",
        "accessed_at": "2026-11-17T06:06:21.874484+00:00"
      },
      {
        "url": "https://github.com/cubewhy/skid-homework/blob/8580e3fe6be0f68208b71b6b5df600103a3e2787/README.md",
        "accessed_at": "2026-11-17T06:06:21.874484+00:00"
      },
      {
        "url": "https://github.com/cubewhy/skid-homework/blob/8580e3fe6be0f68208b71b6b5df600103a3e2787/LICENSE",
        "accessed_at": "2026-11-17T06:06:21.874484+00:00"
      },
      {
        "url": "https://github.com/cubewhy/skid-homework/commit/f480330c0155e670795f2238575a6e872c672f08",
        "accessed_at": "2026-11-17T06:06:21.874484+00:00"
      },
      {
        "url": "https://github.com/cubewhy/skid-homework/blob/8580e3fe6be0f68208b71b6b5df600103a3e2787/src/ai/openai.ts",
        "accessed_at": "2026-11-17T06:06:21.874484+00:00"
      },
      {
        "url": "https://github.com/cubewhy/skid-homework/blob/8580e3fe6be0f68208b71b6b5df600103a3e2787/src/ai/gemini.ts",
        "accessed_at": "2026-11-17T06:06:21.874484+00:00"
      },
      {
        "url": "https://github.com/cubewhy/skid-homework/blob/8580e3fe6be0f68208b71b6b5df600103a3e2787/package.json",
        "accessed_at": "2026-11-17T06:06:21.874484+00:00"
      }
    ],
    "discovery": {
      "kind": "user_submission",
      "submitted_date": "2026-11-17",
      "source_url": "https://github.com/cubewhy/skid-homework",
      "repository_url": "https://github.com/cubewhy/skid-homework"
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOP3tWeg",
    "full_name": "cubewhy/skid-homework",
    "stargazers_count": 1947,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "GPL-3.0",
    "api_license_spdx": "GPL-3.0",
    "license_sha256": "4a03dc6eb67c255f17154376ec3b99af63c21820d3ad36703db4eb76acf9d3ce",
    "last_success_at": "2026-11-17T05:33:14.696956+00:00"
  }
}
```

</details>
