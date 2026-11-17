# Octop

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[TencentCloud/Octop](https://github.com/TencentCloud/Octop)

| 项目 / Field | 内容 / Value |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 12113 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:50:50.290410+00:00 |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:19:44.234Z |

## 中文

可自托管的多用户、多 Agent 助手，提供专家库、网页/CLI/消息渠道、定时任务、知识库及 MCP/ACP 接口。

**环境与限制：** 需要 Python 3.12，uv 安装器可准备环境；前端开发需 Node.js 18+。需配置模型和消息渠道凭据，团队相关功能仍在演进。

**入门：** 从[官方说明](https://raw.githubusercontent.com/TencentCloud/Octop/main/README.md)确认安装与配置步骤，再查看[发布版本](https://github.com/TencentCloud/Octop/releases)。本次为文档、许可原文与维护证据审查，未安装运行。

**近期维护：** [v1.0.3b6 新增 Helm、存储后端和知识图谱功能；版本仍带 beta 标识。](https://github.com/TencentCloud/Octop/releases/tag/v1.0.3b6)（2026-11-15）

## English

A self-hosted multi-user, multi-agent assistant with expert libraries, web/CLI/messaging access, scheduled tasks, knowledge bases and MCP/ACP interfaces.

**Requirements and limitations:** Requires Python 3.12, which the uv installer can provision; frontend development needs Node.js 18+. Configure models and messaging credentials separately. Team features are still evolving.

**Getting started:** Follow the [official documentation](https://raw.githubusercontent.com/TencentCloud/Octop/main/README.md) for setup, then check [releases](https://github.com/TencentCloud/Octop/releases). This review examined documentation, license text and maintenance evidence; the software was not installed or run.

**Recent maintenance:** [v1.0.3b6 adds Helm, storage backends and knowledge-graph functionality; the version retains a beta label.](https://github.com/TencentCloud/Octop/releases/tag/v1.0.3b6) (2026-11-15)

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
    "id": "octop",
    "name": "Octop",
    "repository": "TencentCloud/Octop",
    "repo_node_id": "R_kgDOTRrGxQ",
    "category": "ai",
    "summary": {
      "zh-CN": "可自托管的多用户、多 Agent 助手，提供专家库、网页/CLI/消息渠道、定时任务、知识库及 MCP/ACP 接口。",
      "en": "A self-hosted multi-user, multi-agent assistant with expert libraries, web/CLI/messaging access, scheduled tasks, knowledge bases and MCP/ACP interfaces."
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
      "license_sha256": "5f2089cdcc57d00c6b70c0fb83368cbf3a86bb57839385fc6ac9086878d606e8",
      "source_url": "https://github.com/TencentCloud/Octop/blob/bf134dbd379036ce7545c7df1a1da7e381ece9ff/LICENSE",
      "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
      "files": [
        {
          "path": "LICENSE",
          "source_url": "https://github.com/TencentCloud/Octop/blob/bf134dbd379036ce7545c7df1a1da7e381ece9ff/LICENSE",
          "fetched_at": "2026-11-16T14:23:28.986Z",
          "sha256": "5f2089cdcc57d00c6b70c0fb83368cbf3a86bb57839385fc6ac9086878d606e8",
          "source_commit": "bf134dbd379036ce7545c7df1a1da7e381ece9ff"
        }
      ],
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "bf134dbd379036ce7545c7df1a1da7e381ece9ff"
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-11-15T16:00:57Z",
        "url": "https://github.com/TencentCloud/Octop/releases/tag/v1.0.3b6",
        "tag": "v1.0.3b6",
        "summary": "v1.0.3b6",
        "draft": false,
        "prerelease": false,
        "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
        "qualifies": true,
        "reason": {
          "zh-CN": "v1.0.3b6 新增 Helm、存储后端和知识图谱功能；版本仍带 beta 标识。",
          "en": "v1.0.3b6 adds Helm, storage backends and knowledge-graph functionality; the version retains a beta label."
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
        "https://api.github.com/repos/tencentcloud/octop",
        "https://raw.githubusercontent.com/TencentCloud/Octop/main/README.md",
        "https://github.com/TencentCloud/Octop/releases/tag/v1.0.3b6",
        "https://github.com/TencentCloud/Octop/blob/bf134dbd379036ce7545c7df1a1da7e381ece9ff/LICENSE"
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOTRrGxQ",
    "full_name": "TencentCloud/Octop",
    "stargazers_count": 12113,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "5f2089cdcc57d00c6b70c0fb83368cbf3a86bb57839385fc6ac9086878d606e8",
    "last_success_at": "2026-11-16T14:19:44.234Z"
  }
}
```

</details>
