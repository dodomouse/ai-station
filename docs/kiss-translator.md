# KISS Translator

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[fishjar/kiss-translator](https://github.com/fishjar/kiss-translator)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 13389 |
| 许可证 / License | GPL-3.0 |
| 评估时间 / Evaluated at | 2026-11-17T06:06:21.869942+00:00 |

## 中文

支持网页双语阅读、划词和字幕翻译的浏览器扩展与用户脚本，可选择传统翻译引擎、云端大模型或本地 AI。

### 用途与功能

- 翻译网页、选中文字和输入框内容，并可对比多个服务的译文。
- 为兼容 AI 服务配置提示词和术语；可选用所在段落增强划词翻译上下文。
- 处理 YouTube 双语字幕，并可使用 AI 断句和基于字幕的视频总结。
- 桌面扩展的当前代码提供文件与图片翻译、本地模型管理和接口插件。

### 环境与限制

支持 Chrome、Edge 和 Firefox 扩展；用户脚本需 Tampermonkey、Violentmonkey 或相应平台的脚本管理器。文件翻译、本地 AI 和接口插件等高级入口主要面向桌面扩展，用户脚本不具备同等功能；商店版本可能落后于当前源码。云模型通常需接口地址、密钥和模型配置，服务费用另计；本地 AI 需下载模型并满足浏览器、WebGPU/WASM 和硬件要求。

使用远程服务时，待翻译文本、字幕或文件处理内容会按所选功能发送到配置的翻译、OCR 或模型接口。AI 提示词还可能带入页面标题、描述和摘要；启用划词上下文后会额外传入符合条件的所在段落。选择本地模型只使相应推理阶段在本机运行，其他云服务或同步仍可能联网。GPL-3.0 覆盖项目代码，模型、外部插件和服务另有许可或条款。

### 开始使用

从 README 选择浏览器扩展或用户脚本入口。在服务配置中添加并测试翻译接口，再为网页、划词或字幕场景选择服务；用 Alt+Q 启动网页翻译。本地 AI 用户先在模型中心检测环境并下载所需模型。

参阅[官方 README](https://github.com/fishjar/kiss-translator/blob/381ab009928922390e73892193b00ddc76f02679/README.md)。

### 收录与来源

适合需要双语网页阅读、多个翻译服务对比和可配置 AI 辅助的用户。AI 用途有具体实现，但属于可选服务能力；普通翻译引擎可独立使用，项目本身不提供所有模型或保证译文准确。

维护证据：[新增默认关闭的划词上下文增强：把符合条件的当前段落传给兼容 AI 服务，同时保持选中文字为翻译目标；编辑原文、跨页或段落超长时取消该上下文](https://github.com/fishjar/kiss-translator/commit/e6400758cab42efbd7111799b5bca896f75491cc)（2026-11-15）。

用户于 2026-11-17 提供仓库链接。本条按工程通用标准复核，不设 Star 门槛。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

A browser extension and userscript for bilingual web reading, selection and subtitle translation, with a choice of conventional translation engines, cloud LLMs or local AI.

### Uses and features

- Translate pages, selections and input fields, and compare results from multiple services.
- Configure prompts and terminology for compatible AI services, with optional paragraph context for selection translation.
- Process bilingual YouTube subtitles, with optional AI segmentation and transcript-based video summaries.
- Current desktop-extension code provides document and image translation, local model management and service plugins.

### Requirements and limits

Supports Chrome, Edge and Firefox extensions; userscripts require Tampermonkey, Violentmonkey or a platform-specific script manager. Advanced features such as file translation, local AI and service plugins primarily target desktop extensions and are not equivalent in userscripts; store releases may lag current source. Cloud models generally require an endpoint, key and model configuration, with separate service charges. Local AI requires downloaded models and suitable browser, WebGPU/WASM and hardware support.

Remote services receive translation text, subtitles or file-processing content according to the selected feature. AI prompts may also include page titles, descriptions and summaries; enabling selection context additionally supplies an eligible surrounding paragraph. Selecting a local model keeps that inference stage on the device, while other cloud services or synchronization may still use the network. GPL-3.0 covers project code; models, external plugins and services have separate licenses or terms.

### Getting started

Choose an extension or userscript installation from the README. Add and test a translation service, assign it to page, selection or subtitle scenarios, then use Alt+Q for page translation. For local AI, check the environment and download the required model in the model center first.

See the [official README](https://github.com/fishjar/kiss-translator/blob/381ab009928922390e73892193b00ddc76f02679/README.md).

### Review and provenance

Useful for bilingual web reading, comparing translation services and configuring AI assistance. AI features have inspectable implementations but depend on optional service capabilities; conventional engines work independently. The project does not supply every model or guarantee translation accuracy.

Maintenance evidence: [Adds opt-in contextual selection translation, passing an eligible current paragraph to compatible AI services while keeping the selection as the translation target; edited source, changed pages or oversized paragraphs invalidate that context](https://github.com/fishjar/kiss-translator/commit/e6400758cab42efbd7111799b5bca896f75491cc) (2026-11-15).

Submitted by the user on 2026-11-17 and reviewed against the general catalog criteria, with no star threshold.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T06:06:21.869942+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "kiss-translator",
    "name": "KISS Translator",
    "repository": "fishjar/kiss-translator",
    "repo_node_id": "R_kgDOJ8zHyg",
    "category": "productivity",
    "summary": {
      "zh-CN": "支持网页双语阅读、划词和字幕翻译的浏览器扩展与用户脚本，可选择传统翻译引擎、云端大模型或本地 AI。",
      "en": "A browser extension and userscript for bilingual web reading, selection and subtitle translation, with a choice of conventional translation engines, cloud LLMs or local AI."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T06:06:21.869942+00:00",
        "en": "2026-11-17T06:06:21.869942+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合需要双语网页阅读、多个翻译服务对比和可配置 AI 辅助的用户。AI 用途有具体实现，但属于可选服务能力；普通翻译引擎可独立使用，项目本身不提供所有模型或保证译文准确。",
      "en": "Useful for bilingual web reading, comparing translation services and configuring AI assistance. AI features have inspectable implementations but depend on optional service capabilities; conventional engines work independently. The project does not supply every model or guarantee translation accuracy.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "GPL-3.0",
      "osi_approved": true,
      "source_url": "https://github.com/fishjar/kiss-translator/blob/381ab009928922390e73892193b00ddc76f02679/LICENSE",
      "license_sha256": "3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986",
      "source_commit": "381ab009928922390e73892193b00ddc76f02679",
      "reviewed_at": "2026-11-17T06:06:21.869942+00:00",
      "evidence_pinned_at": "2026-11-17T06:06:21.869942+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "GPL-3.0 covers the KISS Translator repository software. Downloaded models, separately distributed plugins, dictionaries/content and remote translation or model services retain their own licenses and terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-15T10:17:47Z",
        "reviewed_at": "2026-11-17T06:06:21.869942+00:00",
        "url": "https://github.com/fishjar/kiss-translator/commit/e6400758cab42efbd7111799b5bca896f75491cc",
        "qualifies": true,
        "reason": {
          "zh-CN": "新增默认关闭的划词上下文增强：把符合条件的当前段落传给兼容 AI 服务，同时保持选中文字为翻译目标；编辑原文、跨页或段落超长时取消该上下文",
          "en": "Adds opt-in contextual selection translation, passing an eligible current paragraph to compatible AI services while keeping the selection as the translation target; edited source, changed pages or oversized paragraphs invalidate that context"
        },
        "reviewed_files": [
          "src/config/api.js",
          "src/config/setting.js",
          "src/hooks/useSelectionController.js",
          "src/views/Options/Tranbox.js",
          "src/views/Selection/TranCont.js",
          "src/views/Selection/TranForm.js"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/fishjar/kiss-translator",
        "accessed_at": "2026-11-17T06:06:21.869942+00:00"
      },
      {
        "url": "https://github.com/fishjar/kiss-translator/blob/381ab009928922390e73892193b00ddc76f02679/README.md",
        "accessed_at": "2026-11-17T06:06:21.869942+00:00"
      },
      {
        "url": "https://github.com/fishjar/kiss-translator/blob/381ab009928922390e73892193b00ddc76f02679/LICENSE",
        "accessed_at": "2026-11-17T06:06:21.869942+00:00"
      },
      {
        "url": "https://github.com/fishjar/kiss-translator/commit/e6400758cab42efbd7111799b5bca896f75491cc",
        "accessed_at": "2026-11-17T06:06:21.869942+00:00"
      }
    ],
    "discovery": {
      "kind": "user_submission",
      "submitted_date": "2026-11-17",
      "source_url": "https://github.com/fishjar/kiss-translator",
      "repository_url": "https://github.com/fishjar/kiss-translator"
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOJ8zHyg",
    "full_name": "fishjar/kiss-translator",
    "stargazers_count": 13389,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "GPL-3.0",
    "api_license_spdx": "GPL-3.0",
    "license_sha256": "3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986",
    "last_success_at": "2026-11-17T05:21:56.784295+00:00"
  }
}
```

</details>
