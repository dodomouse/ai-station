# WeKnora

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[Tencent/WeKnora](https://github.com/Tencent/WeKnora)

| 项目 / Field | 内容 / Value |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 37540 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:50:50.290410+00:00 |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:19:44.600Z |

## 中文

企业文档知识库与 RAG 问答服务，整合文档解析、检索、Agent 和 Wiki 工作流。

**环境与限制：** 通常使用 Docker Compose 或 Kubernetes，并配置存储与模型服务；Lite 模式支持 SQLite。桌面部分需按文档构建。自有代码 MIT，打包依赖保留各自许可；外部模型会收到所发送的内容。

**入门：** 从[官方说明](https://raw.githubusercontent.com/Tencent/WeKnora/main/README.md)确认安装与配置步骤，再查看[发布版本](https://github.com/Tencent/WeKnora/releases)。本次为文档、许可原文与维护证据审查，未安装运行。

**近期维护：** [v0.9.0 增加人工交互持久化与 RRF 检索控制等功能。](https://github.com/Tencent/WeKnora/releases/tag/v0.9.0)（2026-10-29）

## English

An enterprise-document knowledge base and RAG service combining parsing, retrieval, agents and wiki workflows.

**Requirements and limitations:** Typically deployed with Docker Compose or Kubernetes and configured storage and models; Lite mode supports SQLite. Desktop components require documented build steps. Project code is MIT while bundled dependencies retain their licenses; external models receive submitted content.

**Getting started:** Follow the [official documentation](https://raw.githubusercontent.com/Tencent/WeKnora/main/README.md) for setup, then check [releases](https://github.com/Tencent/WeKnora/releases). This review examined documentation, license text and maintenance evidence; the software was not installed or run.

**Recent maintenance:** [v0.9.0 adds persistent human interactions and RRF retrieval controls.](https://github.com/Tencent/WeKnora/releases/tag/v0.9.0) (2026-10-29)

## Review evidence

发现线索来自第三方公众号文章索引，原始微信正文未完整读取；用途、环境、许可与维护状态依据仓库当前资料复核。

Discovery uses a third-party WeChat article index; the original article body was not fully read. Current repository sources were reviewed for function, requirements, licensing and maintenance.

- 公众号索引原文 / Indexed WeChat source：[盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537550&idx=1&sn=29715a80ebde4036ab57651905d6bc3f)（2026-10-05）
- 作者署名转载 / Author-attributed repost：[盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。](https://www.woshipm.com/share/6473850.html)（2026-10-06）；仓库链接映射已交叉核对 / repository mapping corroborated.

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
    "id": "weknora",
    "name": "WeKnora",
    "repository": "Tencent/WeKnora",
    "repo_node_id": "R_kgDOPQrONg",
    "category": "ai",
    "summary": {
      "zh-CN": "企业文档知识库与 RAG 问答服务，整合文档解析、检索、Agent 和 Wiki 工作流。",
      "en": "An enterprise-document knowledge base and RAG service combining parsing, retrieval, agents and wiki workflows."
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
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "5935f49975d7daf97857d7053b6fe45500a3b2ec31cc92a42a89a5fd98a86cea",
      "source_url": "https://raw.githubusercontent.com/Tencent/WeKnora/main/LICENSE",
      "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
      "files": [
        {
          "path": "LICENSE",
          "source_url": "https://raw.githubusercontent.com/Tencent/WeKnora/main/LICENSE",
          "fetched_at": "2026-11-16T14:23:27.918Z",
          "sha256": "5935f49975d7daf97857d7053b6fe45500a3b2ec31cc92a42a89a5fd98a86cea"
        }
      ],
      "scope": "MIT original project code; bundled dependencies retain their respective licenses, including Apache-2.0 notices."
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-10-29T06:59:12Z",
        "url": "https://github.com/Tencent/WeKnora/releases/tag/v0.9.0",
        "tag": "v0.9.0",
        "summary": "v0.9.0",
        "draft": false,
        "prerelease": false,
        "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
        "qualifies": true,
        "reason": {
          "zh-CN": "v0.9.0 增加人工交互持久化与 RRF 检索控制等功能。",
          "en": "v0.9.0 adds persistent human interactions and RRF retrieval controls."
        }
      }
    ],
    "sources": [
      {
        "article_id": "2247537550_1",
        "title": "盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537550&idx=1&sn=29715a80ebde4036ab57651905d6bc3f",
        "published_date": "2026-10-05",
        "account": "逛逛GitHub",
        "source_strength": "third_party_index",
        "index_url": "https://www.noking.tech/github-radar/data/library.json",
        "original_article_body_read": false
      },
      {
        "url": "https://www.woshipm.com/share/6473850.html",
        "title": "盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。",
        "published_date": "2026-10-06",
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
        "https://api.github.com/repos/tencent/weknora",
        "https://raw.githubusercontent.com/Tencent/WeKnora/main/README.md",
        "https://github.com/Tencent/WeKnora/releases/tag/v0.9.0",
        "https://raw.githubusercontent.com/Tencent/WeKnora/main/LICENSE"
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOPQrONg",
    "full_name": "Tencent/WeKnora",
    "stargazers_count": 37540,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "NOASSERTION",
    "license_sha256": "5935f49975d7daf97857d7053b6fe45500a3b2ec31cc92a42a89a5fd98a86cea",
    "last_success_at": "2026-11-16T14:19:44.600Z"
  }
}
```

</details>
