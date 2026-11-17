# Univer

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[dream-num/univer](https://github.com/dream-num/univer)

| 项目 / Field | 内容 / Value |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 27511 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:50:50.290410+00:00 |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:20:00.102Z |

## 中文

用于嵌入网页的电子表格与文档 SDK，提供公式计算、渲染、编辑和程序接口，也支持无界面处理。

**环境与限制：** 通常通过 JavaScript/TypeScript 包在浏览器或 Node.js 中集成。收录 Apache-2.0 开源核心；商业插件、Server SDK 和部分 AI 扩展另有授权，部署时需区分。

**入门：** 从[官方说明](https://raw.githubusercontent.com/dream-num/univer/dev/README.md)确认安装与配置步骤，再查看[发布版本](https://github.com/dream-num/univer/releases)。本次为文档、许可原文与维护证据审查，未安装运行。

**近期维护：** [提交修复条件格式中重复值与唯一值文本比较的大小写处理，并补充测试。](https://github.com/dream-num/univer/commit/8a301b94fdc1fb7f398181bfd9af33e320c95d42)（2026-11-16）

## English

An embeddable spreadsheet and document SDK with formulas, rendering, editing and programmatic APIs, including headless processing.

**Requirements and limitations:** Typically integrated through JavaScript/TypeScript packages in browsers or Node.js. This entry covers the Apache-2.0 core; commercial plugins, Server SDK and some AI extensions have separate licensing.

**Getting started:** Follow the [official documentation](https://raw.githubusercontent.com/dream-num/univer/dev/README.md) for setup, then check [releases](https://github.com/dream-num/univer/releases). This review examined documentation, license text and maintenance evidence; the software was not installed or run.

**Recent maintenance:** [The inspected commit fixes case-insensitive text comparison in duplicate/unique conditional formatting and adds tests.](https://github.com/dream-num/univer/commit/8a301b94fdc1fb7f398181bfd9af33e320c95d42) (2026-11-16)

## Review evidence

发现线索来自第三方公众号文章索引，原始微信正文未完整读取；用途、环境、许可与维护状态依据仓库当前资料复核。

Discovery uses a third-party WeChat article index; the original article body was not fully read. Current repository sources were reviewed for function, requirements, licensing and maintenance.

- 公众号索引原文 / Indexed WeChat source：[推荐 8 个最近火火火火的开源项目，登上 GitHub 今日热榜。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537385&idx=1&sn=6f57abbd0554d6288c4aa1b3566ef704)（2026-09-27）
- 作者署名转载 / Author-attributed repost：[推荐 8 个最近火火火火的开源项目，登上 GitHub 今日热榜。](https://www.woshipm.com/share/6470709.html)（2026-09-28）；仓库链接映射已交叉核对 / repository mapping corroborated.

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-16T14:50:50.290410+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "univer",
    "name": "Univer",
    "repository": "dream-num/univer",
    "repo_node_id": "R_kgDOIF8T9Q",
    "category": "development",
    "summary": {
      "zh-CN": "用于嵌入网页的电子表格与文档 SDK，提供公式计算、渲染、编辑和程序接口，也支持无界面处理。",
      "en": "An embeddable spreadsheet and document SDK with formulas, rendering, editing and programmatic APIs, including headless processing."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:50:50.290410+00:00",
        "en": "2026-11-16T14:50:50.290410+00:00"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "a6cba85bc92e0cff7a450b1d873c0eaa2e9fc96bf472df0247a26bec77bf3ff9",
      "source_url": "https://github.com/dream-num/univer/blob/8a301b94fdc1fb7f398181bfd9af33e320c95d42/LICENSE",
      "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
      "files": [
        {
          "path": "LICENSE",
          "source_url": "https://github.com/dream-num/univer/blob/8a301b94fdc1fb7f398181bfd9af33e320c95d42/LICENSE",
          "fetched_at": "2026-11-16T14:23:29.017Z",
          "sha256": "a6cba85bc92e0cff7a450b1d873c0eaa2e9fc96bf472df0247a26bec77bf3ff9",
          "source_commit": "8a301b94fdc1fb7f398181bfd9af33e320c95d42"
        }
      ],
      "scope": "Apache-2.0 open core only; commercial plugins, Server SDK and separately licensed AI extensions are excluded.",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "8a301b94fdc1fb7f398181bfd9af33e320c95d42"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-16T13:08:04Z",
        "url": "https://github.com/dream-num/univer/commit/8a301b94fdc1fb7f398181bfd9af33e320c95d42",
        "sha": "8a301b94fdc1fb7f398181bfd9af33e320c95d42",
        "summary": "fix(sheets-conditional-formatting): compare text case-insensitively in duplicate and unique value rules (#8217)",
        "files": [
          "packages/sheets-conditional-formatting/src/models/calculate-unit-v2/__tests__/calculate.highlight.spec.ts",
          "packages/sheets-conditional-formatting/src/models/calculate-unit-v2/highlight-cell-calculate-unit.ts"
        ],
        "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
        "qualifies": true,
        "reason": {
          "zh-CN": "提交修复条件格式中重复值与唯一值文本比较的大小写处理，并补充测试。",
          "en": "The inspected commit fixes case-insensitive text comparison in duplicate/unique conditional formatting and adds tests."
        }
      }
    ],
    "sources": [
      {
        "article_id": "2247537385_1",
        "title": "推荐 8 个最近火火火火的开源项目，登上 GitHub 今日热榜。",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537385&idx=1&sn=6f57abbd0554d6288c4aa1b3566ef704",
        "published_date": "2026-09-27",
        "account": "逛逛GitHub",
        "source_strength": "third_party_index",
        "index_url": "https://www.noking.tech/github-radar/data/library.json",
        "original_article_body_read": false
      },
      {
        "url": "https://www.woshipm.com/share/6470709.html",
        "title": "推荐 8 个最近火火火火的开源项目，登上 GitHub 今日热榜。",
        "published_date": "2026-09-28",
        "account": "逛逛GitHub",
        "source_strength": "author_attributed_repost_repository_mapping",
        "author_attribution_confirmed": true,
        "body_read_method": "public_html_repository_links_and_attribution_extraction",
        "full_text_archived": false
      }
    ],
    "discovery": {
      "account": "逛逛GitHub",
      "window_start": "2026-08-16",
      "window_end": "2026-11-16",
      "original_article_body_read": false,
      "repository_review_sources": [
        "https://api.github.com/repos/dream-num/univer",
        "https://raw.githubusercontent.com/dream-num/univer/dev/README.md",
        "https://github.com/dream-num/univer/commit/8a301b94fdc1fb7f398181bfd9af33e320c95d42",
        "https://github.com/dream-num/univer/blob/8a301b94fdc1fb7f398181bfd9af33e320c95d42/LICENSE"
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOIF8T9Q",
    "full_name": "dream-num/univer",
    "stargazers_count": 27511,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "a6cba85bc92e0cff7a450b1d873c0eaa2e9fc96bf472df0247a26bec77bf3ff9",
    "last_success_at": "2026-11-16T14:20:00.102Z"
  }
}
```

</details>
