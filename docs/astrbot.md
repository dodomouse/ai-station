# AstrBot

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[AstrBotDevs/AstrBot](https://github.com/AstrBotDevs/AstrBot)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 47065 |
| 许可证 / License | AGPL-3.0 |
| 评估时间 / Evaluated at | 2026-11-17T04:07:37.958040+00:00 |

## 中文

将大模型对话和智能体接入多种即时通讯平台，提供插件、知识库及网页管理界面。

### 用途与功能

- 接入多种消息平台，包括 Telegram、飞书和企业微信。
- 配置模型提供商、多模态对话、角色与上下文压缩。
- 通过插件、MCP 和 Skills 扩展工具，并可配置智能体沙箱。

### 环境与限制

可使用 Python 3.12 与 uv，或按文档部署 Docker。需要对应平台的机器人凭据和模型服务；本地模型还需匹配硬件。AGPL-3.0 适用于项目代码，平台接口、模型与第三方插件另有条款。

### 开始使用

按 README 的 uv 或 Docker 路径部署，打开 WebUI 配置模型和消息平台，再选择所需插件。

参阅[官方 README](https://github.com/AstrBotDevs/AstrBot/blob/6ff0b0830314d553a9734ec735a073543bdd0476/README.md)。

### 收录与来源

适合把同一套 AI 对话、知识检索和工具能力接入已有聊天渠道。

维护证据：[优化上下文截断中的增量 token 计数，并为 ASCII 文本加入估算捷径](https://github.com/AstrBotDevs/AstrBot/commit/6ff0b0830314d553a9734ec735a073543bdd0476)（2026-11-16）。

发现于 [GitHub 月榜](https://github.com/trending/python?since=monthly)。2026-11-17 的榜单记录新增 5,303 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Connect LLM conversations and agents to messaging platforms, with plugins, knowledge bases and a web administration interface.

### Uses and features

- Connect messaging platforms such as Telegram, Lark and WeCom.
- Configure model providers, multimodal conversations, personas and context compression.
- Extend tools through plugins, MCP and skills, with an optional agent sandbox.

### Requirements and limits

Use Python 3.12 with uv, or Docker as documented. Requires messaging-platform bot credentials and a model service; local models also need suitable hardware. AGPL-3.0 covers project code, while platform APIs, models and third-party plugins have separate terms.

### Getting started

Deploy through the README’s uv or Docker instructions, configure a model and messaging platform in WebUI, then select plugins.

See the [official README](https://github.com/AstrBotDevs/AstrBot/blob/6ff0b0830314d553a9734ec735a073543bdd0476/README.md).

### Review and provenance

Useful for bringing shared AI conversation, knowledge retrieval and tool capabilities into existing chat channels.

Maintenance evidence: [Optimizes incremental token counting during context truncation and adds an ASCII estimation fast path](https://github.com/AstrBotDevs/AstrBot/commit/6ff0b0830314d553a9734ec735a073543bdd0476) (2026-11-16).

Discovered in [GitHub monthly Trending](https://github.com/trending/python?since=monthly), which recorded 5,303 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:07:37.958040+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "astrbot",
    "name": "AstrBot",
    "repository": "AstrBotDevs/AstrBot",
    "repo_node_id": "R_kgDOIlMBmA",
    "category": "ai",
    "summary": {
      "zh-CN": "将大模型对话和智能体接入多种即时通讯平台，提供插件、知识库及网页管理界面。",
      "en": "Connect LLM conversations and agents to messaging platforms, with plugins, knowledge bases and a web administration interface."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:07:37.958040+00:00",
        "en": "2026-11-17T04:07:37.958040+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合把同一套 AI 对话、知识检索和工具能力接入已有聊天渠道。",
      "en": "Useful for bringing shared AI conversation, knowledge retrieval and tool capabilities into existing chat channels.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "AGPL-3.0",
      "osi_approved": true,
      "source_url": "https://github.com/AstrBotDevs/AstrBot/blob/6ff0b0830314d553a9734ec735a073543bdd0476/LICENSE",
      "license_sha256": "ccf7d08f932af3e813848881731113afbb7c80d0fd6d958e8d319002bf344d02",
      "source_commit": "6ff0b0830314d553a9734ec735a073543bdd0476",
      "reviewed_at": "2026-11-17T04:07:37.958040+00:00",
      "evidence_pinned_at": "2026-11-17T04:07:37.958040+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "AGPL-3.0 covers repository code; model weights, messaging platform services and independently licensed plugins are outside this grant."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-16T15:03:19Z",
        "reviewed_at": "2026-11-17T04:07:37.958040+00:00",
        "url": "https://github.com/AstrBotDevs/AstrBot/commit/6ff0b0830314d553a9734ec735a073543bdd0476",
        "qualifies": true,
        "reason": {
          "zh-CN": "优化上下文截断中的增量 token 计数，并为 ASCII 文本加入估算捷径",
          "en": "Optimizes incremental token counting during context truncation and adds an ASCII estimation fast path"
        },
        "reviewed_files": [
          "astrbot/core/agent/context/manager.py",
          "astrbot/core/agent/context/token_counter.py"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/AstrBotDevs/AstrBot",
        "accessed_at": "2026-11-17T04:07:37.958040+00:00"
      },
      {
        "url": "https://github.com/AstrBotDevs/AstrBot/blob/6ff0b0830314d553a9734ec735a073543bdd0476/README.md",
        "accessed_at": "2026-11-17T04:07:37.958040+00:00"
      },
      {
        "url": "https://github.com/AstrBotDevs/AstrBot/blob/6ff0b0830314d553a9734ec735a073543bdd0476/LICENSE",
        "accessed_at": "2026-11-17T04:07:37.958040+00:00"
      },
      {
        "url": "https://github.com/AstrBotDevs/AstrBot/commit/6ff0b0830314d553a9734ec735a073543bdd0476",
        "accessed_at": "2026-11-17T04:07:37.958040+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 5303,
      "source_url": "https://github.com/trending/python?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOIlMBmA",
    "full_name": "AstrBotDevs/AstrBot",
    "stargazers_count": 47065,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "AGPL-3.0",
    "license_sha256": "ccf7d08f932af3e813848881731113afbb7c80d0fd6d958e8d319002bf344d02",
    "last_success_at": "2026-11-17T03:51:55.054326+00:00"
  }
}
```

</details>
