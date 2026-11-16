# Codex ChatGPT Web Bridge

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[miuuyy/codex-chatgpt-web](https://github.com/miuuyy/codex-chatgpt-web)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 15746 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:47:41.565Z |

## 中文

通过本机登录的ChatGPT网页会话，为Codex提供第三方模型桥接。

### 用途与功能

- 研究网页会话与编码工具之间的集成

提供桌面启动器、内置浏览器、模型选择与流式对话；可通过MCP接入当前任务文件、工具与审批。

### 环境与限制

第三方项目，不是OpenAI官方集成。需要有效ChatGPT账户及相应模型权限，仍受账户限制；网页或Codex更新可能破坏兼容。桌面包提供各主流系统；完整工具模式会访问当前项目，应核对权限与服务条款。

### 开始使用

阅读兼容说明，使用对应桌面包完成自己的登录和Codex接入配置。 参阅[官方 README](https://github.com/miuuyy/codex-chatgpt-web/blob/main/README.md)。

### 收录与来源

有实际浏览器桥接、会话管理与桌面发行，维护记录包含续接修复。 最近维护：[v6.1.18](https://github.com/miuuyy/codex-chatgpt-web/releases/tag/v6.1.18)（2026-11-08T23:56:55Z）。正式版修复长任务续接、目标变更保留和macOS通行密钥会话导入。

通过逛逛GitHub的第三方文章索引发现。索引记录了下列文章；本次未读取微信原文，不据此声称已阅读全文。

- 2026-09-14：[2 个让你的 Codex 狠狠省 Token 的开源项目，有点意思啊。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536916&idx=1&sn=deaea310ec94f838f6484f580da1acc2)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。

## English

Provides a third-party bridge from a signed-in local ChatGPT Web session to Codex.

### Uses and features

- Explore integration between Web sessions and coding tools

Provides a desktop launcher, embedded browser, model selection and streaming, with optional MCP access to task files, tools and approvals.

### Requirements and limits

This is a third-party project, not an official OpenAI integration. It needs a valid ChatGPT account and model access and remains subject to account limits. Web or Codex changes can break compatibility. Desktop packages target major systems; full tool mode accesses the project, so review permissions and service terms.

### Getting started

Read compatibility guidance and use the matching desktop package to configure your own login and Codex integration. See the [official README](https://github.com/miuuyy/codex-chatgpt-web/blob/main/README.md).

### Review and provenance

Implements browser bridging and session management with desktop releases and continuation fixes. Recent maintenance: [v6.1.18](https://github.com/miuuyy/codex-chatgpt-web/releases/tag/v6.1.18) (2026-11-08T23:56:55Z). The formal release fixes long-task continuation, retained goal changes and macOS passkey-session import.

Discovered through a third-party index of 逛逛GitHub articles. The index records the articles below; the original WeChat pages were not read in this review. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:47:41.565Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "codex-chatgpt-web",
    "name": "Codex ChatGPT Web Bridge",
    "repository": "miuuyy/codex-chatgpt-web",
    "repo_node_id": "R_kgDOTj_alw",
    "category": "ai",
    "tags": [],
    "forms": [
      "desktop",
      "plugin"
    ],
    "platforms": [
      "linux",
      "macos",
      "windows"
    ],
    "aliases": {
      "zh-CN": [
        "Codex ChatGPT Web Bridge"
      ],
      "en": [
        "Codex ChatGPT Web Bridge"
      ]
    },
    "summary": {
      "zh-CN": "通过本机登录的ChatGPT网页会话，为Codex提供第三方模型桥接。",
      "en": "Provides a third-party bridge from a signed-in local ChatGPT Web session to Codex."
    },
    "use_cases": {
      "zh-CN": [
        "研究网页会话与编码工具之间的集成"
      ],
      "en": [
        "Explore integration between Web sessions and coding tools"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:47:41.565Z",
        "en": "2026-11-16T14:47:41.565Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "d8b06e8d802722749b8f09e4ed1f2439fde0995a09b7e47c65dca3cc54d43d6e",
      "source_url": "https://github.com/miuuyy/codex-chatgpt-web/blob/main/LICENSE",
      "reviewed_at": "2026-11-16T14:47:41.565Z"
    },
    "activity_evidence": [
      {
        "type": "release",
        "url": "https://github.com/miuuyy/codex-chatgpt-web/releases/tag/v6.1.18",
        "occurred_at": "2026-11-08T23:56:55Z",
        "reason": {
          "zh-CN": "正式版修复长任务续接、目标变更保留和macOS通行密钥会话导入。",
          "en": "The formal release fixes long-task continuation, retained goal changes and macOS passkey-session import."
        },
        "reviewed_at": "2026-11-16T14:47:41.565Z",
        "qualifies": true
      }
    ],
    "sources": [
      {
        "url": "https://github.com/miuuyy/codex-chatgpt-web/blob/main/README.md",
        "accessed_at": "2026-11-16T14:47:41.565Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/miuuyy/codex-chatgpt-web/blob/main/LICENSE",
        "accessed_at": "2026-11-16T14:47:41.565Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.noking.tech/github-radar/data/library.json",
        "accessed_at": "2026-11-16T14:47:41.565Z",
        "supports": {
          "zh-CN": "第三方索引中的公众号文章归属、时间与项目发现线索；非原文阅读证据。",
          "en": "Third-party account attribution, article dates and discovery leads; not proof of reading the originals."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536916&idx=1&sn=deaea310ec94f838f6484f580da1acc2",
        "accessed_at": "2026-11-16T14:47:41.565Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-09-14 2 个让你的 Codex 狠狠省 Token 的开源项目，有点意思啊。；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-09-14; not directly read in this review."
        }
      }
    ],
    "quality_review": {
      "basis": {
        "zh-CN": "有实际浏览器桥接、会话管理与桌面发行，维护记录包含续接修复。",
        "en": "Implements browser bridging and session management with desktop releases and continuation fixes."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOTj_alw",
    "full_name": "miuuyy/codex-chatgpt-web",
    "stargazers_count": 15746,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "d8b06e8d802722749b8f09e4ed1f2439fde0995a09b7e47c65dca3cc54d43d6e",
    "last_success_at": "2026-11-16T14:20:00.044Z"
  }
}
```

</details>

