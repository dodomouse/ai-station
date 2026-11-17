# DeepSeek chat-demo

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[deepseek-ai/chat-demo](https://github.com/deepseek-ai/chat-demo)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 3890 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:30:19.931551Z |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:27:09.950Z |

## 中文

### 用途与功能

通过 DeepSeek API 提供聊天界面的静态网页示例。支持流式回答、会话分支、附件和历史导入导出。

提供中英文界面、语音输入和内容渲染。适合研究或自建浏览器端模型界面。

### 环境与限制

使用需要 API 服务与凭据，调用费用另计。浏览器直接发送消息与附件；密钥存于 localStorage，会话存于 IndexedDB。开发构建需要 Node.js 22.12+ 和 pnpm。直接打开本地页面还取决于浏览器存储和接口跨域支持。

### 入门与收录判断

从[官方 README](https://github.com/deepseek-ai/chat-demo/blob/main/README.md)查阅安装和使用步骤。官方示例说明数据流、持久化和导出边界，具有明确学习及定制价值。

本轮为文档复核，未安装、运行或测试上游项目。正式 v0.1.1 修复会话历史导入失败的提示。详见[维护记录](https://github.com/deepseek-ai/chat-demo/releases/tag/v0.1.1)。

### 文章来源

发现于“逛逛GitHub”在 2026-11-16 发布的[《8 个开源工具速览》](https://www.woshipm.com/ai/6494405.html)。已读取作者署名正文，功能和限制另按当前上游复核。

## English

### Purpose and features

A static chat interface for the DeepSeek API, with streaming replies, conversation branches, attachments and history import/export.

Provides bilingual UI, speech input and rich-content rendering for studying or hosting a browser-based model interface.

### Requirements and limits

Requires an API service and credentials with separate usage costs. Messages and attachments go directly from the browser to the service. Keys use localStorage and conversations use IndexedDB. Development requires Node.js 22.12+ and pnpm; local-file use depends on storage and CORS support.

### Getting started and review

Use the [official README](https://github.com/deepseek-ai/chat-demo/blob/main/README.md) for installation and usage. This is a documentation review; the software was not installed or tested. Stable v0.1.1 fixes history-import failure messages. See the [activity evidence](https://github.com/deepseek-ai/chat-demo/releases/tag/v0.1.1).

The project appears in the account's [author-published article dated 2026-11-16](https://www.woshipm.com/ai/6494405.html). Current upstream documentation supports the feature descriptions.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:30:19.931551Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "deepseek-chat-demo",
    "name": "DeepSeek chat-demo",
    "repository": "deepseek-ai/chat-demo",
    "repo_node_id": "R_kgDOVrmjdg",
    "category": "ai",
    "summary": {
      "zh-CN": "通过 DeepSeek API 提供聊天界面的静态网页示例。支持流式回答、会话分支、附件和历史导入导出。",
      "en": "A static chat interface for the DeepSeek API, with streaming replies, conversation branches, attachments and history import/export."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:30:19.931551Z",
        "en": "2026-11-16T14:30:19.931551Z"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "basis": "官方示例说明数据流、持久化和导出边界，具有明确学习及定制价值。",
      "rationale": "官方示例说明数据流、持久化和导出边界，具有明确学习及定制价值。",
      "stars_are_advisory": true,
      "reviewed_at": "2026-11-16T14:30:19.931551Z"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "18895f3c654f34440e66b920a8815e43d38abaa77bd54d8da0e89c4f7fb987e4",
      "source_url": "https://github.com/deepseek-ai/chat-demo/blob/5d5dd754ebc1948e977ddb880a9eb5aa25f37b4c/LICENSE",
      "reviewed_at": "2026-11-16T14:30:19.931551Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "5d5dd754ebc1948e977ddb880a9eb5aa25f37b4c"
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-11-13T14:33:18Z",
        "reviewed_at": "2026-11-16T14:30:19.931551Z",
        "url": "https://github.com/deepseek-ai/chat-demo/releases/tag/v0.1.1",
        "qualifies": true,
        "reason": {
          "zh-CN": "正式 v0.1.1 修复会话历史导入失败的提示。",
          "en": "Stable v0.1.1 fixes history-import failure messages."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/deepseek-ai/chat-demo",
        "accessed_at": "2026-11-16T14:27:09.950Z",
        "supports": "Repository identity, Stars and public state."
      },
      {
        "url": "https://github.com/deepseek-ai/chat-demo/blob/main/README.md",
        "accessed_at": "2026-11-16T14:30:19.931551Z",
        "supports": "Capabilities, requirements and limits."
      },
      {
        "url": "https://www.woshipm.com/ai/6494405.html",
        "published_date": "2026-11-16",
        "accessed_at": "2026-11-16T14:30:19.931551Z",
        "supports": "Author-published article body and account attribution."
      }
    ],
    "discovery": {
      "account": "逛逛GitHub",
      "article_url": "https://www.woshipm.com/ai/6494405.html",
      "published_date": "2026-11-16",
      "body_verification": "author_published_article"
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVrmjdg",
    "full_name": "deepseek-ai/chat-demo",
    "stargazers_count": 3890,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "18895f3c654f34440e66b920a8815e43d38abaa77bd54d8da0e89c4f7fb987e4",
    "last_success_at": "2026-11-16T14:27:09.950Z"
  }
}
```

</details>
