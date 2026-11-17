# Answer me with HTML

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[QingYunA/answer-me-with-html](https://github.com/QingYunA/answer-me-with-html)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 6390 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T06:06:21.877612+00:00 |

## 中文

供 AI Agent 使用的技能和本地渲染 CLI，将 Markdown 回答转换为包含图表、代码和交互反馈的单页 HTML。

### 用途与功能

- 由 Agent 编写 Markdown 草稿，CLI 负责布局、主题及流程图、时序图、表格等组件。
- 生成可离线打开的 HTML，保留草稿来源，并将读者评论或选项整理为可复制给 Agent 的回复。
- 可按需生成带旁白的讲解播放器；支持图片及视频导出，但受浏览器和额外依赖限制。

### 环境与限制

基本渲染需要 Node.js 20+ 和能够执行本地命令的 AI Agent；CLI 已打包依赖。回答内容由所用 Agent/模型生成，其费用和数据处理条款仍适用。HTML 可离线阅读，但草稿生成不保证离线；更新检查会访问 GitHub，旁白可使用系统语音、本地服务或第三方服务，使用在线语音时会发送旁白文本。MP4/WebM 命令行导出需 Chrome 与 Node.js 22+，MP4 还需 ffmpeg；页面复制为图片仅支持 Chromium。仓库代码为 MIT，嵌入的 Bangers 字体另遵守 SIL OFL 1.1。

### 开始使用

按 README 为自己的 Agent 安装技能或插件，确认 Node.js 版本，再让 Agent 将一个解释或对比问题输出为 HTML；从生成的本地文件检查图表和事实。也可直接使用随技能提供的 CLI 渲染 Markdown。

参阅[官方 README](https://github.com/QingYunA/answer-me-with-html/blob/c4919922ad2f323e33c33ee8d0c3f85bfd84f60e/README.md)。

### 收录与来源

已核对固定版本 README、MIT 和字体许可、视频说明及实际代码差异。2026-11-17 的修复让支持页面绘制的嵌入式 Chromium 显示图片导出按钮，并在剪贴板不可用时下载 PNG，属于实质维护。适合作为 AI 回答的可视化交付工具收录；未运行渲染或导出，也未验证上游节省 token 和提速的基准结论。

维护证据：[调整图片导出能力检测，兼容缺少 userAgentData 的 Chromium 容器，并在非安全上下文或无剪贴板 API 时改为下载 PNG](https://github.com/QingYunA/answer-me-with-html/commit/c4919922ad2f323e33c33ee8d0c3f85bfd84f60e)（2026-11-17）。

用户于 2026-11-17 提供仓库链接。本条按工程通用标准复核，不设 Star 门槛。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

An AI agent skill and local rendering CLI that turn Markdown answers into single-page HTML with diagrams, code and reader feedback.

### Uses and features

- The agent writes a Markdown draft while the CLI handles layouts, themes and components such as flow diagrams, sequences and tables.
- Produce offline HTML with embedded source and collect reader comments or choices into a reply to paste back to the agent.
- Optionally create narrated explainer players and export images or videos, subject to browser support and additional dependencies.

### Requirements and limits

Basic rendering needs Node.js 20+ and an AI agent able to run local commands; CLI dependencies are bundled. The agent/model generates the answer, with its own costs and data-processing terms. HTML is readable offline, but drafting is not necessarily offline. Update checks contact GitHub; narration can use system voices, a local service or a third party, with narration text sent to online voice providers when selected. CLI MP4/WebM export needs Chrome and Node.js 22+; MP4 also needs ffmpeg. Copy-as-image support is limited to Chromium. Repository code is MIT; the embedded Bangers font separately uses SIL OFL 1.1.

### Getting started

Follow the README to install the skill or plugin for your agent, check the Node.js version, and ask for an explanation or comparison in HTML. Open the generated local file and check its diagrams and facts. The bundled CLI can also render Markdown directly.

See the [official README](https://github.com/QingYunA/answer-me-with-html/blob/c4919922ad2f323e33c33ee8d0c3f85bfd84f60e/README.md).

### Review and provenance

Reviewed the pinned README, MIT and font licenses, video documentation and implementation diff. A 2026-11-17 fix exposes image export in capable embedded Chromium hosts and downloads PNGs when clipboard access is unavailable, providing substantive maintenance. It fits as a visual delivery tool for AI answers. Rendering/export and upstream token-saving or speed benchmarks were not tested.

Maintenance evidence: [Updates image-export detection for Chromium hosts without userAgentData and falls back to PNG download in insecure contexts or without the Clipboard API](https://github.com/QingYunA/answer-me-with-html/commit/c4919922ad2f323e33c33ee8d0c3f85bfd84f60e) (2026-11-17).

Submitted by the user on 2026-11-17 and reviewed against the general catalog criteria, with no star threshold.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T06:06:21.877612+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "answer-me-with-html",
    "name": "Answer me with HTML",
    "repository": "QingYunA/answer-me-with-html",
    "repo_node_id": "R_kgDOU4jVlA",
    "category": "productivity",
    "summary": {
      "zh-CN": "供 AI Agent 使用的技能和本地渲染 CLI，将 Markdown 回答转换为包含图表、代码和交互反馈的单页 HTML。",
      "en": "An AI agent skill and local rendering CLI that turn Markdown answers into single-page HTML with diagrams, code and reader feedback."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T06:06:21.877612+00:00",
        "en": "2026-11-17T06:06:21.877612+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "已核对固定版本 README、MIT 和字体许可、视频说明及实际代码差异。2026-11-17 的修复让支持页面绘制的嵌入式 Chromium 显示图片导出按钮，并在剪贴板不可用时下载 PNG，属于实质维护。适合作为 AI 回答的可视化交付工具收录；未运行渲染或导出，也未验证上游节省 token 和提速的基准结论。",
      "en": "Reviewed the pinned README, MIT and font licenses, video documentation and implementation diff. A 2026-11-17 fix exposes image export in capable embedded Chromium hosts and downloads PNGs when clipboard access is unavailable, providing substantive maintenance. It fits as a visual delivery tool for AI answers. Rendering/export and upstream token-saving or speed benchmarks were not tested.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/QingYunA/answer-me-with-html/blob/c4919922ad2f323e33c33ee8d0c3f85bfd84f60e/LICENSE",
      "license_sha256": "752a1a34b40ae8e64e86f546ec699a691aff573179e1f96997e82757b2ee5d3f",
      "source_commit": "c4919922ad2f323e33c33ee8d0c3f85bfd84f60e",
      "reviewed_at": "2026-11-17T06:06:21.877612+00:00",
      "evidence_pinned_at": "2026-11-17T06:06:21.877612+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "MIT applies to the repository software and associated documentation under the root LICENSE. The Bangers font is separately licensed under SIL OFL-1.1; bundled dependencies retain their notices. External agents, models, TTS services and user-supplied content are outside this MIT scope."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-17T04:02:29Z",
        "reviewed_at": "2026-11-17T06:06:21.877612+00:00",
        "url": "https://github.com/QingYunA/answer-me-with-html/commit/c4919922ad2f323e33c33ee8d0c3f85bfd84f60e",
        "qualifies": true,
        "reason": {
          "zh-CN": "调整图片导出能力检测，兼容缺少 userAgentData 的 Chromium 容器，并在非安全上下文或无剪贴板 API 时改为下载 PNG",
          "en": "Updates image-export detection for Chromium hosts without userAgentData and falls back to PNG download in insecure contexts or without the Clipboard API"
        },
        "reviewed_files": [
          "src/runtime/copy-image.js",
          "test/copy-image-browser.test.js"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/QingYunA/answer-me-with-html",
        "accessed_at": "2026-11-17T06:06:21.877612+00:00"
      },
      {
        "url": "https://github.com/QingYunA/answer-me-with-html/blob/c4919922ad2f323e33c33ee8d0c3f85bfd84f60e/README.md",
        "accessed_at": "2026-11-17T06:06:21.877612+00:00"
      },
      {
        "url": "https://github.com/QingYunA/answer-me-with-html/blob/c4919922ad2f323e33c33ee8d0c3f85bfd84f60e/LICENSE",
        "accessed_at": "2026-11-17T06:06:21.877612+00:00"
      },
      {
        "url": "https://github.com/QingYunA/answer-me-with-html/commit/c4919922ad2f323e33c33ee8d0c3f85bfd84f60e",
        "accessed_at": "2026-11-17T06:06:21.877612+00:00"
      },
      {
        "url": "https://github.com/QingYunA/answer-me-with-html/blob/c4919922ad2f323e33c33ee8d0c3f85bfd84f60e/docs/video.md",
        "accessed_at": "2026-11-17T06:06:21.877612+00:00"
      },
      {
        "url": "https://github.com/QingYunA/answer-me-with-html/blob/c4919922ad2f323e33c33ee8d0c3f85bfd84f60e/skills/answer-me-with-html/SKILL.md",
        "accessed_at": "2026-11-17T06:06:21.877612+00:00"
      },
      {
        "url": "https://github.com/QingYunA/answer-me-with-html/blob/c4919922ad2f323e33c33ee8d0c3f85bfd84f60e/skills/answer-me-with-html/licenses/OFL-Bangers.txt",
        "accessed_at": "2026-11-17T06:06:21.877612+00:00"
      }
    ],
    "discovery": {
      "kind": "user_submission",
      "submitted_date": "2026-11-17",
      "source_url": "https://github.com/QingYunA/answer-me-with-html",
      "repository_url": "https://github.com/QingYunA/answer-me-with-html"
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOU4jVlA",
    "full_name": "QingYunA/answer-me-with-html",
    "stargazers_count": 6390,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "api_license_spdx": "MIT",
    "license_sha256": "752a1a34b40ae8e64e86f546ec699a691aff573179e1f96997e82757b2ee5d3f",
    "last_success_at": "2026-11-17T05:38:10.666863+00:00"
  }
}
```

</details>
