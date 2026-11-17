# Filee

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[KnifeLemon/Filee](https://github.com/KnifeLemon/Filee)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 28180 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T06:06:21.873739+00:00 |

## 中文

本地文件转换器，提供可选的 Ollama 文档翻译、Whisper 音视频转写和 AI 图像放大模块。

### 用途与功能

- 通过本机 Ollama 翻译 DOCX、EPUB、Markdown 等文档和电子书，读写文档结构，并支持配置目标语言及本地模型。
- 可选 whisper.cpp 模块把音视频转为 SRT 或纯文本；可选 Upscayl/NCNN 引擎通过本地图像模型执行放大。
- 提供拖放格式选择、批量转换、监控文件夹和 CLI，可将文档、图片、表格及音视频转换组合进本地处理流程。

### 环境与限制

桌面版支持 Windows 10/11、Linux x64/ARM64（Ubuntu 22.04+）和 macOS 13+ 预览版；Linux 拖动手势需要 X11，Wayland 使用放置区或右键菜单，macOS 构建尚未公证。源码构建需要 .NET 10 SDK。AI 翻译需要本机 Ollama 和适配硬件的模型；代码只接受回环地址，并拒绝识别到的云端模型。当前 Whisper 转写模块仅支持 Windows x64，macOS/Linux 不可用，另需 FFmpeg 和模型；图像放大需 Vulkan 设备及对应引擎/模型，平台引擎供应并不一致。部分格式需要另装 LibreOffice、Pandoc、Ghostscript、calibre 或 FFmpeg。转换和模型推理在本机执行，但更新检查、引擎/模型下载、预设库及用户主动下载文件会联网。转换格式与 AI 输出需自行核验，不能保证版式完全一致或翻译、转写准确。

### 开始使用

下载适配平台的 Release 并完成安装；需要翻译时，先准备本机 Ollama 模型，在 Settings → Engines → Manage Ollama 检查模型，再在 Settings → Presets 配置 Translate 目标语言。拖入支持的文档后选择该预设。转写或放大需先安装对应可选引擎。普通转换也可使用 `filee convert photo.heic --to jpg`。

参阅[官方 README](https://github.com/KnifeLemon/Filee/blob/aee96c3d04f452ccbd5ba4192f579b08c34d9e20/README.md)。

### 收录与来源

收录价值来自已实现的本地模型调用：文档翻译通过 Ollama 的模型检查和生成接口，Whisper 与图像放大通过本地引擎执行。它的主要形态仍是通用文件转换器；此处明确记录其可选 AI 模块，不把一般格式转换本身称为 AI，也不宣称提供 MCP 或智能体服务。适合在同一桌面工具中处理本地文档翻译、语音转写和素材转换。

维护证据：[在读取相机 RAW 时将 LibRaw 的 BT.709 色调转换为 sRGB，修复中暗部偏暗，并增加色调表及像素转换测试](https://github.com/KnifeLemon/Filee/commit/0e5c702ec51e860498a13762d73127313ad2fb2a)（2026-11-15）。

用户于 2026-11-17 提供仓库链接。本条按工程通用标准复核，不设 Star 门槛。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

A local file converter with optional Ollama document translation, Whisper audio/video transcription and AI image upscaling.

### Uses and features

- Translate documents and e-books such as DOCX, EPUB and Markdown through local Ollama, retaining a document structure during conversion and allowing target-language and local-model selection.
- Optional whisper.cpp converts audio/video into SRT or plain text; an optional Upscayl/NCNN engine performs image upscaling with local models.
- Drag-and-drop format selection, batch conversion, watched folders and a CLI support local document, image, spreadsheet and media workflows.

### Requirements and limits

Desktop releases support Windows 10/11, Linux x64/ARM64 (Ubuntu 22.04+) and a macOS 13+ preview. Linux drag gestures require X11; Wayland uses the drop zone or context menu, and macOS builds are not notarized. Building requires .NET 10 SDK. AI translation needs local Ollama and a model suited to the available hardware; the code accepts only loopback endpoints and rejects detected cloud models. The current Whisper transcription module supports Windows x64 only and is unavailable on macOS/Linux; it also requires FFmpeg and a model. Upscaling needs a Vulkan-capable device and the appropriate engine/models; engine availability varies by platform. Some formats require optional LibreOffice, Pandoc, Ghostscript, calibre or FFmpeg. Conversion and inference run locally, while update checks, engine/model downloads, the preset gallery and user-initiated file downloads use the network. Check conversion and AI output: exact layout preservation and translation or transcription accuracy are not guaranteed.

### Getting started

Install the release for your platform. For translation, prepare a local Ollama model, check it under Settings → Engines → Manage Ollama, and configure the Translate preset target language in Settings → Presets. Drop a supported document and select that preset. Install the appropriate optional engine before transcription or upscaling. Ordinary conversion also supports `filee convert photo.heic --to jpg`.

See the [official README](https://github.com/KnifeLemon/Filee/blob/aee96c3d04f452ccbd5ba4192f579b08c34d9e20/README.md).

### Review and provenance

Its AI value comes from implemented local-model calls: document translation uses Ollama model checks and generation, while Whisper transcription and image upscaling invoke local engines. Its primary form remains a general file converter; this entry identifies its optional AI modules without labeling ordinary conversion as AI or claiming an MCP or agent service. It suits local document translation, transcription and asset conversion in one desktop tool.

Maintenance evidence: [Converts LibRaw BT.709 tones to sRGB when reading camera RAW files to correct dark midtones and shadows, with tone-table and pixel-conversion tests](https://github.com/KnifeLemon/Filee/commit/0e5c702ec51e860498a13762d73127313ad2fb2a) (2026-11-15).

Submitted by the user on 2026-11-17 and reviewed against the general catalog criteria, with no star threshold.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T06:06:21.873739+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "filee",
    "name": "Filee",
    "repository": "KnifeLemon/Filee",
    "repo_node_id": "R_kgDOUz1Obg",
    "category": "productivity",
    "summary": {
      "zh-CN": "本地文件转换器，提供可选的 Ollama 文档翻译、Whisper 音视频转写和 AI 图像放大模块。",
      "en": "A local file converter with optional Ollama document translation, Whisper audio/video transcription and AI image upscaling."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T06:06:21.873739+00:00",
        "en": "2026-11-17T06:06:21.873739+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "收录价值来自已实现的本地模型调用：文档翻译通过 Ollama 的模型检查和生成接口，Whisper 与图像放大通过本地引擎执行。它的主要形态仍是通用文件转换器；此处明确记录其可选 AI 模块，不把一般格式转换本身称为 AI，也不宣称提供 MCP 或智能体服务。适合在同一桌面工具中处理本地文档翻译、语音转写和素材转换。",
      "en": "Its AI value comes from implemented local-model calls: document translation uses Ollama model checks and generation, while Whisper transcription and image upscaling invoke local engines. Its primary form remains a general file converter; this entry identifies its optional AI modules without labeling ordinary conversion as AI or claiming an MCP or agent service. It suits local document translation, transcription and asset conversion in one desktop tool.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/KnifeLemon/Filee/blob/aee96c3d04f452ccbd5ba4192f579b08c34d9e20/LICENSE",
      "license_sha256": "34209d059d78056e9a68c861aebee328c0651c909467479c49b3e2dd1bd9cece",
      "source_commit": "aee96c3d04f452ccbd5ba4192f579b08c34d9e20",
      "reviewed_at": "2026-11-17T06:06:21.873739+00:00",
      "evidence_pinned_at": "2026-11-17T06:06:21.873739+00:00",
      "evidence_status": "hash_matched",
      "scope_note": {
        "zh-CN": "Filee 自有源码根 LICENSE 为 MIT。第三方库、字体、捆绑及可选外部程序各自保留许可证，包括 Upscayl 的 AGPL-3.0、不同 FFmpeg 构建条款及 7-Zip 的 unRAR 限制；Ollama 和放大模型权重也应逐项核对。MIT 不覆盖整个下载包、所有引擎或全部模型。",
        "en": "The root LICENSE covers Filee-owned source under MIT. Third-party libraries, fonts, bundled components and optional external programs retain their own licenses, including Upscayl AGPL-3.0, build-specific FFmpeg terms and the 7-Zip unRAR restriction. Check Ollama and upscaling model licenses separately. MIT does not cover the entire download, every engine or every model."
      }
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-15T18:29:52Z",
        "reviewed_at": "2026-11-17T06:06:21.873739+00:00",
        "url": "https://github.com/KnifeLemon/Filee/commit/0e5c702ec51e860498a13762d73127313ad2fb2a",
        "qualifies": true,
        "reason": {
          "zh-CN": "在读取相机 RAW 时将 LibRaw 的 BT.709 色调转换为 sRGB，修复中暗部偏暗，并增加色调表及像素转换测试",
          "en": "Converts LibRaw BT.709 tones to sRGB when reading camera RAW files to correct dark midtones and shadows, with tone-table and pixel-conversion tests"
        },
        "reviewed_files": [
          "src/Filee.Engines/Magick/ImageReader.cs",
          "src/Filee.Engines/Magick/RawTone.cs",
          "tests/Filee.Engines.Tests/GraphicsTests.cs"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/KnifeLemon/Filee",
        "accessed_at": "2026-11-17T06:06:21.873739+00:00"
      },
      {
        "url": "https://github.com/KnifeLemon/Filee/blob/aee96c3d04f452ccbd5ba4192f579b08c34d9e20/README.md",
        "accessed_at": "2026-11-17T06:06:21.873739+00:00"
      },
      {
        "url": "https://github.com/KnifeLemon/Filee/blob/aee96c3d04f452ccbd5ba4192f579b08c34d9e20/LICENSE",
        "accessed_at": "2026-11-17T06:06:21.873739+00:00"
      },
      {
        "url": "https://github.com/KnifeLemon/Filee/commit/0e5c702ec51e860498a13762d73127313ad2fb2a",
        "accessed_at": "2026-11-17T06:06:21.873739+00:00"
      },
      {
        "url": "https://github.com/KnifeLemon/Filee/blob/aee96c3d04f452ccbd5ba4192f579b08c34d9e20/docs/ENGINES.md",
        "accessed_at": "2026-11-17T06:06:21.873739+00:00"
      },
      {
        "url": "https://github.com/KnifeLemon/Filee/blob/aee96c3d04f452ccbd5ba4192f579b08c34d9e20/THIRD-PARTY-NOTICES.md",
        "accessed_at": "2026-11-17T06:06:21.873739+00:00"
      },
      {
        "url": "https://github.com/KnifeLemon/Filee/blob/aee96c3d04f452ccbd5ba4192f579b08c34d9e20/src/Filee.Engines/Translation/OllamaEndpoint.cs",
        "accessed_at": "2026-11-17T06:06:21.873739+00:00"
      },
      {
        "url": "https://github.com/KnifeLemon/Filee/blob/aee96c3d04f452ccbd5ba4192f579b08c34d9e20/src/Filee.Engines/Translation/TranslationService.cs",
        "accessed_at": "2026-11-17T06:06:21.873739+00:00"
      },
      {
        "url": "https://github.com/KnifeLemon/Filee/blob/aee96c3d04f452ccbd5ba4192f579b08c34d9e20/src/Filee.Engines/Translation/TranslatorConverter.cs",
        "accessed_at": "2026-11-17T06:06:21.873739+00:00"
      },
      {
        "url": "https://github.com/KnifeLemon/Filee/blob/aee96c3d04f452ccbd5ba4192f579b08c34d9e20/src/Filee.Engines/Media/WhisperConverter.cs",
        "accessed_at": "2026-11-17T06:06:21.873739+00:00"
      },
      {
        "url": "https://github.com/KnifeLemon/Filee/blob/aee96c3d04f452ccbd5ba4192f579b08c34d9e20/src/Filee.Engines/Upscale/UpscalerConverter.cs",
        "accessed_at": "2026-11-17T06:06:21.873739+00:00"
      }
    ],
    "discovery": {
      "kind": "user_submission",
      "submitted_date": "2026-11-17",
      "source_url": "https://github.com/KnifeLemon/Filee",
      "repository_url": "https://github.com/KnifeLemon/Filee"
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOUz1Obg",
    "full_name": "KnifeLemon/Filee",
    "stargazers_count": 28180,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "api_license_spdx": "MIT",
    "license_sha256": "34209d059d78056e9a68c861aebee328c0651c909467479c49b3e2dd1bd9cece",
    "last_success_at": "2026-11-17T05:32:23.351991+00:00"
  }
}
```

</details>
