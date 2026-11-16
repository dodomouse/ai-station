# OpenFuse（原OpenMuse）

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[CopilotKit/openfuse](https://github.com/CopilotKit/openfuse)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 6496 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:50:00.542Z |

## 中文

提供带浏览器、终端和文件工作区的个人智能体应用模板。

### 用途与功能

- 构建可接管和查看过程的个人智能体

包含服务端、任务worker、持久浏览器和可选Linux工作区；提供Web及React Native界面、邮件与日历适配。

### 环境与限制

处于Alpha，需Node24 LTS、pnpm11.19.0及CopilotKit Intelligence项目凭据；真实模型和Google连接另配。移动开发还需Xcode或Android工具。样例可运行不证明所有真实账户流程已验证。

### 开始使用

按README先运行本地样例，再按验证范围配置实际模型、浏览器和账号连接。 参阅[官方 README](https://github.com/CopilotKit/openfuse/blob/main/README.md)。

### 收录与来源

具有服务端、任务执行和跨端界面实现，并明确标注Alpha验证边界。 最近维护：[实现提交](https://github.com/CopilotKit/openfuse/commit/a4944f4c471d3dc93b8bfc060b5da309b5216ab2)（2026-10-26T15:38:10Z）。已核对邮件解析实现及测试：处理无效代理区数值字符引用，避免邮件列表整体失败。

通过逛逛GitHub的第三方文章索引发现。索引记录了下列文章；本次未读取微信原文，不据此声称已阅读全文。

- 2026-10-08：[3 个最近爆火的 Personal Agent ，在 GitHub 上有开源平替了。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537624&idx=1&sn=10eccfc7b58a97b27b2144654b7ddd35)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。

## English

Provides a personal-agent application template with a browser, terminal and file workspace.

### Uses and features

- Build personal agents with visible work and user takeover

Includes an API, task worker, persistent browser and optional Linux workspace, with Web/React Native interfaces and mail/calendar adapters.

### Requirements and limits

An alpha requiring Node 24 LTS, pnpm 11.19.0 and a CopilotKit Intelligence project credential, with separate model and Google configuration. Mobile builds need Xcode or Android tools. A working sample does not validate every live-account workflow.

### Getting started

Start with the documented local sample, then configure real models, browser and account connections within the stated verification scope. See the [official README](https://github.com/CopilotKit/openfuse/blob/main/README.md).

### Review and provenance

Implements backend execution and cross-platform UI with explicit alpha verification boundaries. Recent maintenance: [implementation commit](https://github.com/CopilotKit/openfuse/commit/a4944f4c471d3dc93b8bfc060b5da309b5216ab2) (2026-10-26T15:38:10Z). Reviewed mail parsing and tests handling invalid surrogate numeric references to keep message lists from failing.

Discovered through a third-party index of 逛逛GitHub articles. The index records the articles below; the original WeChat pages were not read in this review. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:50:00.542Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "openfuse",
    "name": "OpenFuse（原OpenMuse）",
    "repository": "CopilotKit/openfuse",
    "repo_node_id": "R_kgDOUcNbCg",
    "category": "ai",
    "tags": [],
    "forms": [
      "service",
      "web",
      "mobile"
    ],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "OpenFuse（原OpenMuse）"
      ],
      "en": [
        "OpenFuse（原OpenMuse）"
      ]
    },
    "summary": {
      "zh-CN": "提供带浏览器、终端和文件工作区的个人智能体应用模板。",
      "en": "Provides a personal-agent application template with a browser, terminal and file workspace."
    },
    "use_cases": {
      "zh-CN": [
        "构建可接管和查看过程的个人智能体"
      ],
      "en": [
        "Build personal agents with visible work and user takeover"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:50:00.542Z",
        "en": "2026-11-16T14:50:00.542Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "7fdc5583ed6735e5659ccc4fb05c5c8c36838b23b37934b0f72d101dfe0daf2a",
      "source_url": "https://github.com/CopilotKit/openfuse/blob/main/LICENSE",
      "reviewed_at": "2026-11-16T14:50:00.542Z"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/CopilotKit/openfuse/commit/a4944f4c471d3dc93b8bfc060b5da309b5216ab2",
        "occurred_at": "2026-10-26T15:38:10Z",
        "reason": {
          "zh-CN": "已核对邮件解析实现及测试：处理无效代理区数值字符引用，避免邮件列表整体失败。",
          "en": "Reviewed mail parsing and tests handling invalid surrogate numeric references to keep message lists from failing."
        },
        "reviewed_at": "2026-11-16T14:50:00.542Z",
        "qualifies": true
      }
    ],
    "sources": [
      {
        "url": "https://github.com/CopilotKit/openfuse/blob/main/README.md",
        "accessed_at": "2026-11-16T14:50:00.542Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/CopilotKit/openfuse/blob/main/LICENSE",
        "accessed_at": "2026-11-16T14:50:00.542Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.noking.tech/github-radar/data/library.json",
        "accessed_at": "2026-11-16T14:50:00.542Z",
        "supports": {
          "zh-CN": "第三方索引中的公众号文章归属、时间与项目发现线索；非原文阅读证据。",
          "en": "Third-party account attribution, article dates and discovery leads; not proof of reading the originals."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537624&idx=1&sn=10eccfc7b58a97b27b2144654b7ddd35",
        "accessed_at": "2026-11-16T14:50:00.542Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-10-08 3 个最近爆火的 Personal Agent ，在 GitHub 上有开源平替了。；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-10-08; not directly read in this review."
        }
      }
    ],
    "quality_review": {
      "basis": {
        "zh-CN": "具有服务端、任务执行和跨端界面实现，并明确标注Alpha验证边界。",
        "en": "Implements backend execution and cross-platform UI with explicit alpha verification boundaries."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOUcNbCg",
    "full_name": "CopilotKit/openfuse",
    "stargazers_count": 6496,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "7fdc5583ed6735e5659ccc4fb05c5c8c36838b23b37934b0f72d101dfe0daf2a",
    "last_success_at": "2026-11-16T14:21:49.873Z"
  }
}
```

</details>

