# Wakaru

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[pionxzh/wakaru](https://github.com/pionxzh/wakaru)

| 项目 / Field | 内容 / Value |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 1090 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:50:50.290410+00:00 |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:19:22.394Z |

## 中文

JavaScript 反编译工具，可拆分打包文件、展开压缩代码并恢复部分转译结构，提供 CLI 和网页试用。

**环境与限制：** 命令行工具需要 Node.js/npm。恢复结果受打包器和代码变换影响，无法保证还原原始变量名或精确源码。

**入门：** 从[官方说明](https://raw.githubusercontent.com/pionxzh/wakaru/main/README.md)确认安装与配置步骤，再查看[发布版本](https://github.com/pionxzh/wakaru/releases)。本次为文档、许可原文与维护证据审查，未安装运行。

**近期维护：** [v1.16.0 修复路径遍历并更新打包模块提取。](https://github.com/pionxzh/wakaru/releases/tag/v1.16.0)（2026-11-02）

## English

A JavaScript decompiler that unbundles packages, expands minified code and restores some transpiled structures through a CLI or playground.

**Requirements and limitations:** The CLI needs Node.js/npm. Results depend on the bundler and transformations; original names and exact source cannot always be reconstructed.

**Getting started:** Follow the [official documentation](https://raw.githubusercontent.com/pionxzh/wakaru/main/README.md) for setup, then check [releases](https://github.com/pionxzh/wakaru/releases). This review examined documentation, license text and maintenance evidence; the software was not installed or run.

**Recent maintenance:** [v1.16.0 fixes path traversal and updates bundle extraction.](https://github.com/pionxzh/wakaru/releases/tag/v1.16.0) (2026-11-02)

## Review evidence

发现线索来自第三方公众号文章索引，原始微信正文未完整读取；用途、环境、许可与维护状态依据仓库当前资料复核。

Discovery uses a third-party WeChat article index; the original article body was not fully read. Current repository sources were reviewed for function, requirements, licensing and maintenance.

- 公众号索引原文 / Indexed WeChat source：[火了两周的 30 万 Star 逆向 GitHub 开源神器，网友都用它来干啥？](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537852&idx=1&sn=641d50231c757ac9c628f8657e3024c5)（2026-10-18）
- 作者署名转载 / Author-attributed repost：[火了两周的 30 万 Star 逆向 GitHub 开源神器，网友都用它来干啥？](https://www.woshipm.com/ai/6480438.html)（2026-10-19）；仓库链接映射已交叉核对 / repository mapping corroborated.

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
    "id": "wakaru",
    "name": "Wakaru",
    "repository": "pionxzh/wakaru",
    "repo_node_id": "R_kgDOI2v4zQ",
    "category": "development",
    "summary": {
      "zh-CN": "JavaScript 反编译工具，可拆分打包文件、展开压缩代码并恢复部分转译结构，提供 CLI 和网页试用。",
      "en": "A JavaScript decompiler that unbundles packages, expands minified code and restores some transpiled structures through a CLI or playground."
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
      "license_sha256": "c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4",
      "source_url": "https://raw.githubusercontent.com/pionxzh/wakaru/main/LICENSE",
      "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
      "files": [
        {
          "path": "LICENSE",
          "source_url": "https://raw.githubusercontent.com/pionxzh/wakaru/main/LICENSE",
          "fetched_at": "2026-11-16T14:23:28.293Z",
          "sha256": "c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4"
        }
      ]
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-11-02T19:04:27Z",
        "url": "https://github.com/pionxzh/wakaru/releases/tag/v1.16.0",
        "tag": "v1.16.0",
        "summary": "v1.16.0",
        "draft": false,
        "prerelease": false,
        "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
        "qualifies": true,
        "reason": {
          "zh-CN": "v1.16.0 修复路径遍历并更新打包模块提取。",
          "en": "v1.16.0 fixes path traversal and updates bundle extraction."
        }
      }
    ],
    "sources": [
      {
        "article_id": "2247537852_1",
        "title": "火了两周的 30 万 Star 逆向 GitHub 开源神器，网友都用它来干啥？",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537852&idx=1&sn=641d50231c757ac9c628f8657e3024c5",
        "published_date": "2026-10-18",
        "account": "逛逛GitHub",
        "source_strength": "third_party_index",
        "index_url": "https://www.noking.tech/github-radar/data/library.json",
        "original_article_body_read": false
      },
      {
        "url": "https://www.woshipm.com/ai/6480438.html",
        "title": "火了两周的 30 万 Star 逆向 GitHub 开源神器，网友都用它来干啥？",
        "published_date": "2026-10-19",
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
        "https://api.github.com/repos/pionxzh/wakaru",
        "https://raw.githubusercontent.com/pionxzh/wakaru/main/README.md",
        "https://github.com/pionxzh/wakaru/releases/tag/v1.16.0",
        "https://raw.githubusercontent.com/pionxzh/wakaru/main/LICENSE"
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOI2v4zQ",
    "full_name": "pionxzh/wakaru",
    "stargazers_count": 1090,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4",
    "last_success_at": "2026-11-16T14:19:22.394Z"
  }
}
```

</details>
