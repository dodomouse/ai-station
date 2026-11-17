# Public APIs

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[public-apis/public-apis](https://github.com/public-apis/public-apis)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development |
| 状态 / Status | 候选 / Candidate |
| Star | 499152 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T10:48:16.339Z |

候选原因：双语内容与维护证据待复核。
Candidate reason: Bilingual content and activity evidence require review.

状态整理：2026-11-17，依据已有证据区分当前待办与历史结论；未重新完成全部准入复核，Star 与快照日期保持原值。
Status clarified on 2026-11-17 from existing evidence; this is not a complete new eligibility review. Stars and snapshot dates retain their original values.

下一步：核对中英文说明并补充窗口内的实质活动证据。
Next step: Review both language versions and add substantive activity evidence within the review window.

历史资格见[收录依据](#review-evidence)中的 `eligibility_history`。 / Earlier decisions are retained in `eligibility_history` in the [review evidence](#review-evidence).

## 中文

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

### 原始中文记录（历史快照）

### 021 Public APIs

仓库：[public-apis/public-apis](https://github.com/public-apis/public-apis)

#### 1. 简介

按领域收集公开 API，列出认证、HTTPS 和 CORS 信息。当前也包含供智能体使用的 MCP 服务目录。

#### 2. 适用场景

为原型寻找外部数据接口。按领域查找 API。筛选认证与跨域条件。

#### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 按领域寻找 API | 领域索引覆盖天气、地理、金融、新闻、开发、开放数据等，可跳转到具体接口条目。 | Index / 各领域分类 |
| 接口基本条件对照 | API 表列出说明、Auth、HTTPS、CORS，帮助初步筛选认证、传输和跨域条件。 | 各领域 API 表 |
| MCP 服务导航 | MCP Servers 单列可供智能体调用的服务，并提供认证、传输和安装入口等信息。 | MCP Servers |
| 服务文档与接入入口 | 接口条目链接到各自的服务或文档。APILayer 部分另列产品及 Postman 等接入入口。 | APILayer APIs / 各领域 API 表 |

官方来源入口：[官方 README](https://github.com/public-apis/public-apis/blob/master/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

**平台与环境**

- 通过浏览器或 GitHub 阅读，目录无独立运行平台要求
- 具体 API 或 MCP 的客户端兼容范围由各服务决定

- 仓库元数据标示 MIT。被收录 API、MCP 与 APILayer 产品分别定价，可能有免费额度、认证或付费套餐；目录许可不替代服务合同，也不意味着全部免费。

- 条目是发现线索，不代表对外部服务的可用性和数据准确性作验证。
- Auth、HTTPS 和 CORS 字段需按服务当前文档复核。
- README 含商业推广，推广内容与社区目录需区分。

**容易找错的需求（不属于本项目能力）**

- 不匹配“一个接口或一个 key 就能免费调用目录全部服务”的需求。
- 不是自带所有数据、可完全离线运行的 API 服务器。

#### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/public-apis/public-apis/blob/master/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- GitHub README 分类目录
- 外部 API 文档链接
- MCP 服务导航；本仓本身不是统一网关

可先阅读 README 与目录，按具体主题进入资料。若要使用附带程序或技能，再按其说明准备环境。

#### 6. 替代选择

- [1c7/chinese-independent-developer](chinese-independent-developer.md#中文)：本项目帮助寻找 API 和认证条件；后者帮助寻找已经上线的网站、App 与开发者。

#### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/public-apis/public-apis/blob/master/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/021_public-apis-public-apis.md`。

## English

A categorized directory of APIs and MCP-related services, with indicators such as authentication, HTTPS and CORS.

### Use cases

- Discover services by topic
- Find service documentation

### Requirements and limits

The directory does not host all listed data or grant one credential for every API. Service availability, terms, quotas and prices differ. Listing metadata was not checked service by service. Promotional material is separate from community curation.

### Getting started

Read the [official documentation](https://github.com/public-apis/public-apis/blob/master/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [Chinese Independent Developer Projects](chinese-independent-developer.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:16.339Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

保留原始核对数据，便于追溯来源、许可和维护证据。 / Original review data preserves source, license and maintenance evidence.

```json
{
  "evaluated_at": "2026-11-15T11:54:08.129868Z",
  "eligibility": {
    "status": "needs_review",
    "reasons": [
      "bilingual_content_needs_review"
    ],
    "reviewed_at": "2026-11-17T03:11:46.178386+00:00",
    "review_basis": "existing_evidence_status_clarification",
    "pending_actions": {
      "zh-CN": [
        "核对中英文说明并补充窗口内的实质活动证据。"
      ],
      "en": [
        "Review both language versions and add substantive activity evidence within the review window."
      ]
    }
  },
  "metadata": {
    "schema_version": 1,
    "id": "public-apis",
    "name": "Public APIs",
    "repository": "public-apis/public-apis",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnk1NDM0Njc5OQ==",
    "category": "development",
    "tags": [
      "resource-list",
      "api",
      "discovery"
    ],
    "forms": [],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "Public APIs"
      ],
      "en": [
        "Public APIs"
      ]
    },
    "summary": {
      "zh-CN": "按领域收集公开 API，列出认证、HTTPS 和 CORS 信息。当前也包含供智能体使用的 MCP 服务目录。",
      "en": "A categorized directory of APIs and MCP-related services, with indicators such as authentication, HTTPS and CORS."
    },
    "use_cases": {
      "zh-CN": [
        "为原型寻找外部数据接口。按领域查找 API。筛选认证与跨域条件。"
      ],
      "en": [
        "Discover services by topic",
        "Find service documentation"
      ]
    },
    "alternatives": [
      "chinese-independent-developer"
    ],
    "editorial": {
      "status": "draft",
      "reviewed_at": {
        "zh-CN": "2026-11-15T11:03:50.120930Z",
        "en": "2026-11-15T11:03:50.120930Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "07704fa08e479d81930b0ad53c7c1d634c766736d27f725044949f982c1c9447",
      "source_url": "https://github.com/public-apis/public-apis/blob/51bc64abb499c7c532619d89c3f3a083899d3c61/LICENSE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "51bc64abb499c7c532619d89c3f3a083899d3c61"
    },
    "activity_evidence": [],
    "sources": [
      {
        "url": "https://github.com/public-apis/public-apis",
        "accessed_at": "2026-11-15T10:48:16.339Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/public-apis/public-apis/blob/master/README.md",
        "accessed_at": "2026-11-03T00:00:00+08:00",
        "supports": {
          "zh-CN": "用户原卡记录的官方说明来源；本次未逐项刷新资料目录。",
          "en": "Official source recorded in the user’s historical card; directory contents were not individually refreshed."
        }
      },
      {
        "url": "https://github.com/public-apis/public-apis/blob/51bc64abb499c7c532619d89c3f3a083899d3c61/LICENSE",
        "accessed_at": "2026-11-15T10:53:10.779Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "021",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "f0accb07e7bca0dd5b81a0057ae34c4f9915a6e0170bc817e744aff5b04e8bab",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "reference",
      "pending_reasons": [
        "reference_resource"
      ],
      "english_scope": "editorial_digest",
      "source_card_preserved": true,
      "historical": true
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "MDEwOlJlcG9zaXRvcnk1NDM0Njc5OQ==",
    "full_name": "public-apis/public-apis",
    "stargazers_count": 499152,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "07704fa08e479d81930b0ad53c7c1d634c766736d27f725044949f982c1c9447",
    "last_success_at": "2026-11-15T10:48:16.339Z"
  },
  "eligibility_history": [
    {
      "evaluated_at": "2026-11-15T11:54:08.129868Z",
      "status": "needs_review",
      "reasons": [
        "bilingual_content_needs_review"
      ]
    }
  ]
}
```

</details>
