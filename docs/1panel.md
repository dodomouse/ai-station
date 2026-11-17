# 1Panel

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[1Panel-dev/1Panel](https://github.com/1Panel-dev/1Panel)

| 项目 / Field | 内容 / Value |
| --- | --- |
| 分类 / Category | 部署与运维 / Deployment and operations |
| 状态 / Status | 已收录 / Included |
| Star | 37458 |
| 许可证 / License | GPL-3.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:50:50.290410+00:00 |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:20:00.371Z |

## 中文

Linux 服务器的网页管理面板，管理容器、数据库、文件、站点与证书，并提供部分模型和 GPU 管理能力。

**环境与限制：** 需要受支持的 Linux 服务器与管理员权限；安装和服务资源要求以官方说明为准。面板管理权限较高，应按部署文档配置访问控制；扩展服务仍有自身依赖。

**入门：** 从[官方说明](https://raw.githubusercontent.com/1Panel-dev/1Panel/dev-v2/README.md)确认安装与配置步骤，再查看[发布版本](https://github.com/1Panel-dev/1Panel/releases)。本次为文档、许可原文与维护证据审查，未安装运行。

**近期维护：** [v2.5.0 增加 GPU 统计与 vLLM 管理。](https://github.com/1Panel-dev/1Panel/releases/tag/v2.5.0)（2026-11-11）

## English

A web-based Linux server panel for containers, databases, files, websites and certificates, with model and GPU management features.

**Requirements and limitations:** Requires a supported Linux server and administrator privileges. Follow the official installation and resource requirements. The panel has broad management privileges, so configure access controls as documented; integrated services retain their own dependencies.

**Getting started:** Follow the [official documentation](https://raw.githubusercontent.com/1Panel-dev/1Panel/dev-v2/README.md) for setup, then check [releases](https://github.com/1Panel-dev/1Panel/releases). This review examined documentation, license text and maintenance evidence; the software was not installed or run.

**Recent maintenance:** [v2.5.0 adds GPU statistics and vLLM management.](https://github.com/1Panel-dev/1Panel/releases/tag/v2.5.0) (2026-11-11)

## Review evidence

发现线索来自第三方公众号文章索引，原始微信正文未完整读取；用途、环境、许可与维护状态依据仓库当前资料复核。

Discovery uses a third-party WeChat article index; the original article body was not fully read. Current repository sources were reviewed for function, requirements, licensing and maintenance.

- 公众号索引原文 / Indexed WeChat source：[37K Star 的 GitHub 开源项目开放 AI 网关，10 人团队免费用。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537027&idx=1&sn=75cff48e39e64266715ab74062af08d6)（2026-09-16）
- 作者署名转载 / Author-attributed repost：[37K Star 的 GitHub 开源项目开放 AI 网关，10 人团队免费用](https://www.woshipm.com/share/6466411.html)（2026-09-18）；仓库链接映射已交叉核对 / repository mapping corroborated.

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
    "id": "1panel",
    "name": "1Panel",
    "repository": "1Panel-dev/1Panel",
    "repo_node_id": "R_kgDOHrwnHA",
    "category": "operations",
    "summary": {
      "zh-CN": "Linux 服务器的网页管理面板，管理容器、数据库、文件、站点与证书，并提供部分模型和 GPU 管理能力。",
      "en": "A web-based Linux server panel for containers, databases, files, websites and certificates, with model and GPU management features."
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
      "spdx": "GPL-3.0",
      "osi_approved": true,
      "license_sha256": "3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986",
      "source_url": "https://github.com/1Panel-dev/1Panel/blob/b00478c312443b88ad8cc7610bd3d3c8343a4a37/LICENSE",
      "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
      "files": [
        {
          "path": "LICENSE",
          "source_url": "https://github.com/1Panel-dev/1Panel/blob/b00478c312443b88ad8cc7610bd3d3c8343a4a37/LICENSE",
          "fetched_at": "2026-11-16T14:23:42.069Z",
          "sha256": "3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986",
          "source_commit": "b00478c312443b88ad8cc7610bd3d3c8343a4a37"
        }
      ],
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "b00478c312443b88ad8cc7610bd3d3c8343a4a37"
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-11-11T08:51:39Z",
        "url": "https://github.com/1Panel-dev/1Panel/releases/tag/v2.5.0",
        "tag": "v2.5.0",
        "summary": "v2.5.0",
        "draft": false,
        "prerelease": false,
        "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
        "qualifies": true,
        "reason": {
          "zh-CN": "v2.5.0 增加 GPU 统计与 vLLM 管理。",
          "en": "v2.5.0 adds GPU statistics and vLLM management."
        }
      }
    ],
    "sources": [
      {
        "article_id": "2247537027_1",
        "title": "37K Star 的 GitHub 开源项目开放 AI 网关，10 人团队免费用。",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537027&idx=1&sn=75cff48e39e64266715ab74062af08d6",
        "published_date": "2026-09-16",
        "account": "逛逛GitHub",
        "source_strength": "third_party_index",
        "index_url": "https://www.noking.tech/github-radar/data/library.json",
        "original_article_body_read": false
      },
      {
        "url": "https://www.woshipm.com/share/6466411.html",
        "title": "37K Star 的 GitHub 开源项目开放 AI 网关，10 人团队免费用",
        "published_date": "2026-09-18",
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
        "https://api.github.com/repos/1panel-dev/1panel",
        "https://raw.githubusercontent.com/1Panel-dev/1Panel/dev-v2/README.md",
        "https://github.com/1Panel-dev/1Panel/releases/tag/v2.5.0",
        "https://github.com/1Panel-dev/1Panel/blob/b00478c312443b88ad8cc7610bd3d3c8343a4a37/LICENSE"
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOHrwnHA",
    "full_name": "1Panel-dev/1Panel",
    "stargazers_count": 37458,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "GPL-3.0",
    "license_sha256": "3972dc9744f6499f0f9b2dbf76696f2ae7ad8af9b23dde66d6af86c9dfb36986",
    "last_success_at": "2026-11-16T14:20:00.371Z"
  }
}
```

</details>
