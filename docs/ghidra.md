# Ghidra

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[NationalSecurityAgency/ghidra](https://github.com/NationalSecurityAgency/ghidra)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 100277 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:32:13.622Z |

## 中文

用于分析编译后程序的逆向工程框架，提供反汇编、反编译与脚本扩展。

### 用途与功能

- 理解二进制程序结构
- 自动化程序分析任务

支持多种指令集与可执行格式，提供图形分析、交互和自动化模式，以及 Java、Python 扩展入口。

### 环境与限制

可运行于 Windows、macOS、Linux；当前 README 要求 64位 JDK 25。源码构建还需 Gradle、Python 与平台编译工具。反编译结果不等于原始源码，格式支持和分析质量需按目标验证。

### 开始使用

按 README 下载正式二进制发行并配置 JDK，再运行 ghidraRun；源码构建使用独立开发指南。 参阅[官方 README](https://github.com/NationalSecurityAgency/ghidra/blob/master/README.md)。

### 收录与来源

有完整二进制分析实现、扩展机制、发行包与使用文档。 最近维护：[Ghidra_12.2_build](https://github.com/NationalSecurityAgency/ghidra/releases/tag/Ghidra_12.2_build)（2026-10-22T08:31:12Z）。已核对窗口内的非预发行版本及其更新说明入口。

通过逛逛GitHub的第三方文章索引发现。索引记录了下列文章；本次未读取微信原文，不据此声称已阅读全文。

- 2026-11-02：[盘点 10 月份 19 个 Star 蹭蹭涨的 GitHub 项目，第一个很有用。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538256&idx=1&sn=3b97e48392e47b295968f5c66a4ce5f0)
- 2026-10-21：[盘点本周 11 个 Star 攀升最多的 GitHub 开源项目。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537903&idx=1&sn=69b07453177c4c06c464245954d7e217)
- 2026-10-18：[火了两周的 30 万 Star 逆向 GitHub 开源神器，网友都用它来干啥？](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537852&idx=1&sn=641d50231c757ac9c628f8657e3024c5)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。


补充核对作者在公开平台发布或授权发布的文章，确认署名、日期与仓库关联：

- 2026-11-02：[盘点 10 月份 19 个 Star 蹭蹭涨的 GitHub 项目，第一个很有用。](https://www.woshipm.com/ai/6487701.html)
- 2026-10-22：[盘点本周 11 个 Star 攀升最多的 GitHub 开源项目。](https://www.woshipm.com/ai/6482138.html)

## English

A reverse-engineering framework for compiled programs with disassembly, decompilation and scripting.

### Uses and features

- Understand binary program structure
- Automate program analysis

Supports multiple instruction sets and executable formats, graphical analysis, interactive and automated modes, and Java/Python extensions.

### Requirements and limits

Runs on Windows, macOS and Linux; the current README requires a 64-bit JDK 25. Source builds also need Gradle, Python and platform build tools. Decompiled output is not the original source; validate format support and analysis on the target.

### Getting started

Download a formal binary release, configure the JDK and run ghidraRun; use the separate development guide for source builds. See the [official README](https://github.com/NationalSecurityAgency/ghidra/blob/master/README.md).

### Review and provenance

Provides implemented binary analysis, extensibility, release packages and documentation. Recent maintenance: [Ghidra_12.2_build](https://github.com/NationalSecurityAgency/ghidra/releases/tag/Ghidra_12.2_build) (2026-10-22T08:31:12Z). Verified a non-prerelease version within the review window and its release-note links.

Discovered through a third-party index of 逛逛GitHub articles. The index records the articles below; the original WeChat pages were not read in this review. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.


Public articles published or authorized by the author were also checked for attribution, date and repository links. See the additional links in the Chinese section.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:32:13.622Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "ghidra",
    "name": "Ghidra",
    "repository": "NationalSecurityAgency/ghidra",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkxNzMyMjg0MzY=",
    "category": "development",
    "tags": [],
    "forms": [
      "desktop",
      "cli"
    ],
    "platforms": [
      "linux",
      "macos",
      "windows"
    ],
    "aliases": {
      "zh-CN": [
        "Ghidra"
      ],
      "en": [
        "Ghidra"
      ]
    },
    "summary": {
      "zh-CN": "用于分析编译后程序的逆向工程框架，提供反汇编、反编译与脚本扩展。",
      "en": "A reverse-engineering framework for compiled programs with disassembly, decompilation and scripting."
    },
    "use_cases": {
      "zh-CN": [
        "理解二进制程序结构",
        "自动化程序分析任务"
      ],
      "en": [
        "Understand binary program structure",
        "Automate program analysis"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:32:13.622Z",
        "en": "2026-11-16T14:32:13.622Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4",
      "source_url": "https://github.com/NationalSecurityAgency/ghidra/blob/master/LICENSE",
      "reviewed_at": "2026-11-16T14:32:13.622Z"
    },
    "activity_evidence": [
      {
        "type": "release",
        "reason": {
          "zh-CN": "已核对窗口内的非预发行版本及其更新说明入口。",
          "en": "Verified a non-prerelease version within the review window and its release-note links."
        },
        "reviewed_at": "2026-11-16T14:32:13.622Z",
        "qualifies": true,
        "url": "https://github.com/NationalSecurityAgency/ghidra/releases/tag/Ghidra_12.2_build",
        "occurred_at": "2026-10-22T08:31:12Z"
      }
    ],
    "sources": [
      {
        "url": "https://github.com/NationalSecurityAgency/ghidra/blob/master/README.md",
        "accessed_at": "2026-11-16T14:32:13.622Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/NationalSecurityAgency/ghidra/blob/master/LICENSE",
        "accessed_at": "2026-11-16T14:32:13.622Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.noking.tech/github-radar/data/library.json",
        "accessed_at": "2026-11-16T14:32:13.622Z",
        "supports": {
          "zh-CN": "第三方索引中的公众号文章归属、时间与项目发现线索；非原文阅读证据。",
          "en": "Third-party account attribution, article dates and discovery leads; not proof of reading the originals."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538256&idx=1&sn=3b97e48392e47b295968f5c66a4ce5f0",
        "accessed_at": "2026-11-16T14:32:13.622Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-11-02 盘点 10 月份 19 个 Star 蹭蹭涨的 GitHub 项目，第一个很有用。；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-11-02; not directly read in this review."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537903&idx=1&sn=69b07453177c4c06c464245954d7e217",
        "accessed_at": "2026-11-16T14:32:13.622Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-10-21 盘点本周 11 个 Star 攀升最多的 GitHub 开源项目。；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-10-21; not directly read in this review."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537852&idx=1&sn=641d50231c757ac9c628f8657e3024c5",
        "accessed_at": "2026-11-16T14:32:13.622Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-10-18 火了两周的 30 万 Star 逆向 GitHub 开源神器，网友都用它来干啥？；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-10-18; not directly read in this review."
        }
      },
      {
        "url": "https://www.woshipm.com/ai/6487701.html",
        "accessed_at": "2026-11-16T14:26:00.440875+00:00",
        "published_date": "2026-11-02",
        "author": "逛逛GitHub",
        "supports": {
          "zh-CN": "作者公开发表或授权的文章；已核对署名、日期与仓库链接。",
          "en": "Author-published or authorized public article; attribution, date and repository links checked."
        }
      },
      {
        "url": "https://www.woshipm.com/ai/6482138.html",
        "accessed_at": "2026-11-16T14:26:00.452739+00:00",
        "published_date": "2026-10-22",
        "author": "逛逛GitHub",
        "supports": {
          "zh-CN": "作者公开发表或授权的文章；已核对署名、日期与仓库链接。",
          "en": "Author-published or authorized public article; attribution, date and repository links checked."
        }
      }
    ],
    "quality_review": {
      "basis": {
        "zh-CN": "有完整二进制分析实现、扩展机制、发行包与使用文档。",
        "en": "Provides implemented binary analysis, extensibility, release packages and documentation."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkxNzMyMjg0MzY=",
    "full_name": "NationalSecurityAgency/ghidra",
    "stargazers_count": 100277,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4",
    "last_success_at": "2026-11-16T14:18:44.014Z"
  }
}
```

</details>

