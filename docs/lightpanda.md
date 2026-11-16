# Lightpanda Browser

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[lightpanda-io/browser](https://github.com/lightpanda-io/browser)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 42129 |
| 许可证 / License | AGPL-3.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:24:08.700270Z |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:18:52.098Z |

## 中文

### 用途与功能

面向自动化和智能体的无头浏览器。执行网页脚本、操作页面并提取 HTML、Markdown 或结构化内容。

提供 Chrome DevTools Protocol（CDP）、WebDriver Bidi、命令行和 MCP 接口。适合网页采集和无需图形渲染的自动化任务。

### 环境与限制

提供 Linux、macOS 和 Docker 入口。Windows 通过 WSL 使用；Linux 二进制有 glibc 版本要求。网页 API 兼容性需按目标网站验证。默认采集使用遥测，可用 LIGHTPANDA_DISABLE_TELEMETRY=true 关闭。性能比较仅为上游自述。

### 入门与收录判断

从[官方 README](https://github.com/lightpanda-io/browser/blob/main/README.md)查阅安装和配置步骤。为程序化网页读取提供独立浏览器实现及多种自动化协议，补充现有浏览器工具条目。

本轮为文档复核，未安装、运行或测试上游软件。正式 1.0.4 包含多项修复，涉及请求端口、postMessage 目标域和跨站 Cookie。详见[维护记录](https://github.com/lightpanda-io/browser/releases/tag/1.0.4)。

### 文章来源

公众号“逛逛GitHub”的[微信原文](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538420&idx=1&sn=9769127e763c53057c449032da509279)，索引日期为 2026-11-09。本次读取了作者在[人人都是产品经理发布的正文](https://www.woshipm.com/share/6491406.html)，该页日期为 2026-11-10。功能和限制另按当前上游复核。

## English

### Purpose and features

A headless browser for automation and agents, with JavaScript execution, page interaction and HTML, Markdown or structured extraction.

Offers CDP, WebDriver Bidi, CLI and MCP interfaces for extraction and automation without a conventional graphical rendering engine.

### Requirements and limits

Available for Linux, macOS and Docker; Windows uses WSL. Linux binaries require suitable glibc versions. Web API compatibility needs site-specific testing. Usage telemetry is enabled by default and can be disabled with LIGHTPANDA_DISABLE_TELEMETRY=true. Benchmark claims remain upstream claims.

### Getting started and review

Use the [official README](https://github.com/lightpanda-io/browser/blob/main/README.md) for installation and configuration. This is a documentation review; the software was not installed or tested. Stable 1.0.4 fixes request-port restrictions, postMessage target origins and cross-site cookie behavior. See the [release](https://github.com/lightpanda-io/browser/releases/tag/1.0.4).

The original WeChat article is dated 2026-11-09 in the public index. Its author-published mirror is dated 2026-11-10. The mirror establishes the article association; current upstream documentation supports the feature descriptions.

## Review evidence

```json
{
  "evaluated_at": "2026-11-16T14:24:08.700270Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "lightpanda",
    "name": "Lightpanda Browser",
    "repository": "lightpanda-io/browser",
    "repo_node_id": "R_kgDOI67vwg",
    "category": "development",
    "summary": {
      "zh-CN": "面向自动化和智能体的无头浏览器。执行网页脚本、操作页面并提取 HTML、Markdown 或结构化内容。",
      "en": "A headless browser for automation and agents, with JavaScript execution, page interaction and HTML, Markdown or structured extraction."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:24:08.700270Z",
        "en": "2026-11-16T14:24:08.700270Z"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "basis": "为程序化网页读取提供独立浏览器实现及多种自动化协议，补充现有浏览器工具条目。",
      "stars_are_advisory": true,
      "reviewed_at": "2026-11-16T14:24:08.700270Z"
    },
    "license_review": {
      "spdx": "AGPL-3.0",
      "osi_approved": true,
      "license_sha256": "8486a10c4393cee1c25392769ddd3b2d6c242d6ec7928e1414efff7dfb2f07ef",
      "source_url": "https://github.com/lightpanda-io/browser/blob/main/LICENSE",
      "reviewed_at": "2026-11-16T14:24:08.700270Z"
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-11-13T11:51:36Z",
        "reviewed_at": "2026-11-16T14:24:08.700270Z",
        "url": "https://github.com/lightpanda-io/browser/releases/tag/1.0.4",
        "qualifies": true,
        "reason": {
          "zh-CN": "正式 1.0.4 修复请求端口、postMessage 目标域和跨站 Cookie 等行为。",
          "en": "Stable 1.0.4 fixes request-port restrictions, postMessage target origins and cross-site cookie behavior."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/lightpanda-io/browser",
        "accessed_at": "2026-11-16T14:18:52.098Z",
        "supports": "Repository identity, Stars and public state."
      },
      {
        "url": "https://github.com/lightpanda-io/browser/blob/main/README.md",
        "accessed_at": "2026-11-16T14:24:08.700270Z",
        "supports": "Capabilities, requirements and limits."
      },
      {
        "url": "https://www.woshipm.com/share/6491406.html",
        "published_date": "2026-11-10",
        "accessed_at": "2026-11-16T14:24:08.700270Z",
        "supports": "Article body and account attribution verified on the author-published mirror."
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538420&idx=1&sn=9769127e763c53057c449032da509279",
        "published_date": "2026-11-09",
        "supports": "Original WeChat URL and date from the public article index; original body unavailable."
      }
    ],
    "discovery": {
      "account": "逛逛GitHub",
      "article": {
        "article_id": "2247538420_1",
        "title": "7 个近期 GitHub 上贼火火的开源项目，又是质量很高的一波。",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538420&idx=1&sn=9769127e763c53057c449032da509279",
        "published_date": "2026-11-09"
      },
      "index_url": "https://www.noking.tech/github-radar/",
      "body_verification": "author_published_mirror"
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOI67vwg",
    "full_name": "lightpanda-io/browser",
    "stargazers_count": 42129,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "AGPL-3.0",
    "license_sha256": "8486a10c4393cee1c25392769ddd3b2d6c242d6ec7928e1414efff7dfb2f07ef",
    "last_success_at": "2026-11-16T14:18:52.098Z"
  }
}
```
