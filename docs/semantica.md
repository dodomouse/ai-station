# Semantica

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[semantica-agi/semantica](https://github.com/semantica-agi/semantica)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 14627 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:20:20.508Z |

## 中文

把多来源资料组织为知识图谱与上下文图，并记录数据来源和推理过程。

### 主要功能

- 提供资料导入、实体关系处理、图存储与查询组件。
- 支持本体、规则和图分析，可按需接入模型。

### 环境与限制

- Python 包按功能选择可选依赖，数据库和模型服务另行配置。
- 生产部署需要持久化存储与访问控制，来源记录不等于数据正确性保证。

### 开始使用

从[官方说明](https://github.com/semantica-agi/semantica/blob/main/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/semantica-agi/semantica/releases)可用于确认版本。

### 收录复核

把多来源资料组织为知识图谱与上下文图，并记录数据来源和推理过程。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。

有效维护证据：[v0.7.0](https://github.com/semantica-agi/semantica/releases/tag/v0.7.0)，2026-09-22T11:18:03Z。修复知识图谱导出按扩展名选择格式和保留导出器默认参数的行为，并跳过空集合。 2026-11-17 已读取[实现提交](https://github.com/semantica-agi/semantica/commit/04409b31d0093194602750725bc7470e3f6a3985)的差异；未运行上游测试。

发现线索：[公开索引](https://www.noking.tech/github-radar/)记录的[微信文章](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536122&idx=1&sn=b7a284d06296707235d8dde07c6f6d4e)，索引日期 2026-08-23。仅核对公开索引，未直接读取该篇微信全文；功能与限制以上游资料为依据。

本次为文档与实现证据复核，未安装或运行上游项目。

## English

A library for organizing data into knowledge and context graphs with provenance and reasoning records.

### Features

- Provides ingestion, entity and relation processing, graph storage and queries.
- Supports ontologies, rules and graph analysis, with optional model integration.

### Requirements and limits

- Select optional dependencies for the Python package and configure databases or models separately.
- Production deployments need persistent storage and access control
- provenance does not guarantee correct data.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/semantica-agi/semantica/blob/main/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/semantica-agi/semantica/releases) for versions.

### Review and provenance

A library for organizing data into knowledge and context graphs with provenance and reasoning records. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.

Activity: [v0.7.0](https://github.com/semantica-agi/semantica/releases/tag/v0.7.0), 2026-09-22T11:18:03Z. Fixes extension-based knowledge-graph export routing, preserves exporter defaults and skips empty collections. On 2026-11-17, the [implementation diff](https://github.com/semantica-agi/semantica/commit/04409b31d0093194602750725bc7470e3f6a3985) was inspected; upstream tests were not run.

Discovery: [an indexed WeChat article](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536122&idx=1&sn=b7a284d06296707235d8dde07c6f6d4e). This is a secondary discovery record; the WeChat article body was not read. Features and limits come from upstream documentation.

This review covers documentation and implementation evidence. The upstream project was not installed or run.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:58:29.135174Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "semantica",
    "name": "Semantica",
    "repository": "semantica-agi/semantica",
    "repo_node_id": "R_kgDOPBmB5g",
    "category": "development",
    "summary": {
      "zh-CN": "把多来源资料组织为知识图谱与上下文图，并记录数据来源和推理过程。",
      "en": "A library for organizing data into knowledge and context graphs with provenance and reasoning records."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:58:29.135174Z",
        "en": "2026-11-16T14:58:29.135174Z"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "把多来源资料组织为知识图谱与上下文图，并记录数据来源和推理过程。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。",
      "en": "A library for organizing data into knowledge and context graphs with provenance and reasoning records. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "7650ef0576603b337c310b9ad9dc051819257213abc44b720d9e678f8e4f4c40",
      "source_url": "https://github.com/semantica-agi/semantica/blob/066505cf7bf80a7944e1efe729b88f8a2878fd41/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "Root license reviewed. External dependencies and assets retain their individual licenses.",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "066505cf7bf80a7944e1efe729b88f8a2878fd41"
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-09-22T11:18:03Z",
        "reviewed_at": "2026-11-17T03:15:51.892548+00:00",
        "url": "https://github.com/semantica-agi/semantica/releases/tag/v0.7.0",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复知识图谱导出按扩展名选择格式和保留导出器默认参数的行为，并跳过空集合。",
          "en": "Fixes extension-based knowledge-graph export routing, preserves exporter defaults and skips empty collections."
        },
        "draft": false,
        "prerelease": false,
        "implementation_evidence": {
          "type": "commit",
          "url": "https://github.com/semantica-agi/semantica/commit/04409b31d0093194602750725bc7470e3f6a3985",
          "sha": "04409b31d0093194602750725bc7470e3f6a3985",
          "occurred_at": "2026-09-22T09:38:09Z",
          "reviewed_at": "2026-11-17T03:15:51.892548+00:00",
          "reviewed_files": [
            "semantica/export/methods.py",
            "semantica/export/csv_exporter.py",
            "semantica/export/parquet_exporter.py"
          ],
          "verification_level": "source_review",
          "upstream_tests_run": false
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/semantica-agi/semantica",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/semantica-agi/semantica/blob/main/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/semantica-agi/semantica/blob/066505cf7bf80a7944e1efe729b88f8a2878fd41/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/semantica-agi/semantica/releases/tag/v0.7.0",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536122&idx=1&sn=b7a284d06296707235d8dde07c6f6d4e",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      }
    ],
    "article_source": {
      "article_id": "2247536122_1",
      "title": "一周没逛 GitHub 不要紧，这 TOP 10 的热门开源项目整理好了。",
      "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536122&idx=1&sn=b7a284d06296707235d8dde07c6f6d4e",
      "published_date": "2026-08-23",
      "account": "逛逛GitHub",
      "content_review_url": null,
      "content_review_kind": "secondary article index only",
      "wechat_direct_body_read": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOPBmB5g",
    "full_name": "semantica-agi/semantica",
    "stargazers_count": 14627,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "7650ef0576603b337c310b9ad9dc051819257213abc44b720d9e678f8e4f4c40",
    "last_success_at": "2026-11-16T14:20:20.508Z"
  }
}
```

</details>
