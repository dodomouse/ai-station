# Resource Radar (Freebie Radar)

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[ZiChuanLan/freebie-radar](https://github.com/ZiChuanLan/freebie-radar)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 数据处理 / Data processing |
| 状态 / Status | 已收录 / Included |
| Star | 1214 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T06:06:21.876287+00:00 |

## 中文

自托管的信息聚合与筛选工具，从社区、RSS 和资源站采集条目，用规则和可选 AI 审核分类、评分，再供网页浏览或 Telegram 推送。

### 用途与功能

- 汇总社区动态、软件和游戏优惠、开源项目及行业资讯，按内容形态、类别和获取方式组织条目。
- 通过 OpenAI 兼容接口批量审核标题与内容摘录，返回保留建议、分类、获取条件、质量评分和原因；可自定义提示词及送审来源。
- 结合关键词拦截、收藏与忽略样本调整筛选偏好，并按频道、关键词和评分配置 Telegram 即时或批量推送。

### 环境与限制

可用 Docker 部署；源码运行要求 Node.js 22.5+ 与 pnpm 10，数据保存在本地 SQLite，需持久化数据目录。ADMIN_TOKEN 默认空：非生产 selfhost 模式下管理接口开放，public 模式或 NODE_ENV=production 下则锁定管理区；对外部署前应设置令牌并配置访问边界。AI 需兼容接口和模型，云服务可能收费，并会接收条目标题、正文或摘要摘录、自定义提示词，以及启用偏好学习时抽取的收藏和忽略样本标题。采集依赖来源可达性、限流及部分站点登录状态；Telegram 推送需机器人配置。规则和模型可能误分类，优惠条件与有效期仍需到原站核实。

### 开始使用

克隆仓库后将 .env.example 复制为 .env，先设置 ADMIN_TOKEN 和数据目录，再运行 `docker compose up -d --build`。默认从本机 8788 端口打开页面，选择采集来源；需要 AI 时在管理页配置端点、模型和密钥并测试连通性，再按需启用 Telegram 路由。

参阅[官方 README](https://github.com/ZiChuanLan/freebie-radar/blob/9de586d4c4461ec9b756baf98036d6e97c84b5d6/README.md)。

### 收录与来源

把采集、规则筛选、模型审核和推送串成可配置流程，适合整理多来源信息流。已核对 AI 请求实现及分类维护补丁；偏好学习是将样本加入提示词，不是训练模型。本次未安装运行，也未验证分类准确率或推送可靠性。

维护证据：[调整实物福利分类：有领取动作且包含实物或生活福利线索的免费条目可进入 offline；测评和选购标题改归 tech，有价或促销条目保留 goods，并同步类别说明](https://github.com/ZiChuanLan/freebie-radar/commit/88ceab7705b20c1f29f5dda980742cbe78bbb2df)（2026-11-16）。

用户于 2026-11-17 提供仓库链接。本条按工程通用标准复核，不设 Star 门槛。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

A self-hosted information aggregator that collects community, RSS and resource-site entries, classifies and scores them with rules and optional AI review, then serves them on the web or through Telegram.

### Uses and features

- Aggregates community posts, software and game deals, open-source projects and industry information, organized by content kind, category and acquisition conditions.
- Reviews titles and text excerpts in batches through an OpenAI-compatible endpoint, returning keep decisions, classifications, acquisition conditions, quality scores and reasons; prompts and source selection are configurable.
- Combines keyword blocking with favorite/ignored examples and configures immediate or batched Telegram delivery by channel, keywords and score.

### Requirements and limits

Deploy with Docker, or run the source with Node.js 22.5+ and pnpm 10. Data uses local SQLite and requires a persistent data directory. ADMIN_TOKEN is empty by default: management is open in non-production selfhost mode, while public mode or NODE_ENV=production locks administration; set a token and configure access boundaries before public deployment. AI requires a compatible endpoint and model. Cloud services may charge and receive entry titles, body or summary excerpts, custom prompts, and sampled favorite/ignored titles when preference learning is enabled. Collection depends on source availability, rate limits and login state for some sites; Telegram delivery requires bot configuration. Rules and models can misclassify entries, and offers and expiry dates require verification at the original source.

### Getting started

Clone the repository, copy .env.example to .env, set ADMIN_TOKEN and persistent storage, then run `docker compose up -d --build`. Open the local site on port 8788 and select sources. For AI review, configure an endpoint, model and key in the admin interface and test connectivity; enable Telegram routes as needed.

See the [official README](https://github.com/ZiChuanLan/freebie-radar/blob/9de586d4c4461ec9b756baf98036d6e97c84b5d6/README.md).

### Review and provenance

Connects collection, rule filtering, model review and delivery in a configurable workflow for organizing multi-source feeds. AI request construction and a classification maintenance patch were reviewed. Preference learning adds examples to prompts rather than training a model. The software was not installed or run, and classification accuracy and delivery reliability were not measured.

Maintenance evidence: [Updates physical-benefit classification: free entries with claim actions and physical or everyday-benefit signals can enter offline; review and buying-guide titles move to tech, priced or promotional entries stay in goods, and category descriptions are updated](https://github.com/ZiChuanLan/freebie-radar/commit/88ceab7705b20c1f29f5dda980742cbe78bbb2df) (2026-11-16).

Submitted by the user on 2026-11-17 and reviewed against the general catalog criteria, with no star threshold.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T06:06:21.876287+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "freebie-radar",
    "name": "Resource Radar (Freebie Radar)",
    "repository": "ZiChuanLan/freebie-radar",
    "repo_node_id": "R_kgDOVrqNtQ",
    "category": "data",
    "summary": {
      "zh-CN": "自托管的信息聚合与筛选工具，从社区、RSS 和资源站采集条目，用规则和可选 AI 审核分类、评分，再供网页浏览或 Telegram 推送。",
      "en": "A self-hosted information aggregator that collects community, RSS and resource-site entries, classifies and scores them with rules and optional AI review, then serves them on the web or through Telegram."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T06:06:21.876287+00:00",
        "en": "2026-11-17T06:06:21.876287+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "把采集、规则筛选、模型审核和推送串成可配置流程，适合整理多来源信息流。已核对 AI 请求实现及分类维护补丁；偏好学习是将样本加入提示词，不是训练模型。本次未安装运行，也未验证分类准确率或推送可靠性。",
      "en": "Connects collection, rule filtering, model review and delivery in a configurable workflow for organizing multi-source feeds. AI request construction and a classification maintenance patch were reviewed. Preference learning adds examples to prompts rather than training a model. The software was not installed or run, and classification accuracy and delivery reliability were not measured.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/ZiChuanLan/freebie-radar/blob/9de586d4c4461ec9b756baf98036d6e97c84b5d6/LICENSE",
      "license_sha256": "b32f2a249e149a652cf298e65d30e30067ac0c32ff8088b130394878fbcd220f",
      "source_commit": "9de586d4c4461ec9b756baf98036d6e97c84b5d6",
      "reviewed_at": "2026-11-17T06:06:21.876287+00:00",
      "evidence_pinned_at": "2026-11-17T06:06:21.876287+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "MIT covers the repository software under the pinned root LICENSE. Collected posts, images and other source content, third-party dependencies, model services and optional browser/FlareSolverr components retain their own licenses and service terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-16T17:33:32Z",
        "reviewed_at": "2026-11-17T06:06:21.876287+00:00",
        "url": "https://github.com/ZiChuanLan/freebie-radar/commit/88ceab7705b20c1f29f5dda980742cbe78bbb2df",
        "qualifies": true,
        "reason": {
          "zh-CN": "调整实物福利分类：有领取动作且包含实物或生活福利线索的免费条目可进入 offline；测评和选购标题改归 tech，有价或促销条目保留 goods，并同步类别说明",
          "en": "Updates physical-benefit classification: free entries with claim actions and physical or everyday-benefit signals can enter offline; review and buying-guide titles move to tech, priced or promotional entries stay in goods, and category descriptions are updated"
        },
        "reviewed_files": [
          "src/server/enrich/index.ts",
          "src/shared/taxonomy.ts"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/ZiChuanLan/freebie-radar",
        "accessed_at": "2026-11-17T06:06:21.876287+00:00"
      },
      {
        "url": "https://github.com/ZiChuanLan/freebie-radar/blob/9de586d4c4461ec9b756baf98036d6e97c84b5d6/README.md",
        "accessed_at": "2026-11-17T06:06:21.876287+00:00"
      },
      {
        "url": "https://github.com/ZiChuanLan/freebie-radar/blob/9de586d4c4461ec9b756baf98036d6e97c84b5d6/LICENSE",
        "accessed_at": "2026-11-17T06:06:21.876287+00:00"
      },
      {
        "url": "https://github.com/ZiChuanLan/freebie-radar/commit/88ceab7705b20c1f29f5dda980742cbe78bbb2df",
        "accessed_at": "2026-11-17T06:06:21.876287+00:00"
      },
      {
        "url": "https://github.com/ZiChuanLan/freebie-radar/blob/9de586d4c4461ec9b756baf98036d6e97c84b5d6/docs/ai.md",
        "accessed_at": "2026-11-17T06:06:21.876287+00:00"
      },
      {
        "url": "https://github.com/ZiChuanLan/freebie-radar/blob/9de586d4c4461ec9b756baf98036d6e97c84b5d6/package.json",
        "accessed_at": "2026-11-17T06:06:21.876287+00:00"
      },
      {
        "url": "https://github.com/ZiChuanLan/freebie-radar/blob/9de586d4c4461ec9b756baf98036d6e97c84b5d6/src/server/enrich/ai.ts",
        "accessed_at": "2026-11-17T06:06:21.876287+00:00"
      },
      {
        "url": "https://github.com/ZiChuanLan/freebie-radar/blob/9de586d4c4461ec9b756baf98036d6e97c84b5d6/src/server/enrich/ai-settings.ts",
        "accessed_at": "2026-11-17T06:06:21.876287+00:00"
      },
      {
        "url": "https://github.com/ZiChuanLan/freebie-radar/blob/9de586d4c4461ec9b756baf98036d6e97c84b5d6/src/server/config.ts",
        "accessed_at": "2026-11-17T06:06:21.876287+00:00"
      },
      {
        "url": "https://github.com/ZiChuanLan/freebie-radar/blob/9de586d4c4461ec9b756baf98036d6e97c84b5d6/src/server/routes.ts",
        "accessed_at": "2026-11-17T06:06:21.876287+00:00"
      },
      {
        "url": "https://github.com/ZiChuanLan/freebie-radar/blob/9de586d4c4461ec9b756baf98036d6e97c84b5d6/src/server/index.ts",
        "accessed_at": "2026-11-17T06:06:21.876287+00:00"
      }
    ],
    "discovery": {
      "kind": "user_submission",
      "submitted_date": "2026-11-17",
      "source_url": "https://github.com/ZiChuanLan/freebie-radar",
      "repository_url": "https://github.com/ZiChuanLan/freebie-radar"
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVrqNtQ",
    "full_name": "ZiChuanLan/freebie-radar",
    "stargazers_count": 1214,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "api_license_spdx": "MIT",
    "license_sha256": "b32f2a249e149a652cf298e65d30e30067ac0c32ff8088b130394878fbcd220f",
    "last_success_at": "2026-11-17T05:36:49.556952+00:00"
  }
}
```

</details>
