# ASCII

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[bas3line/ascii](https://github.com/bas3line/ascii)

| 项目 / Field | 内容 / Value |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 1232 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:50:50.290410+00:00 |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:19:21.679Z |

## 中文

可嵌入网页的 TypeScript ASCII 动画组件，支持 React、Next.js、Astro、Web Components 和普通 HTML，也可生成 SVG。

**环境与限制：** 面向现代浏览器；包集成通常需要 JavaScript/TypeScript 构建环境。使用所附字体、品牌或外部素材时仍需遵守对应条款。

**入门：** 从[官方说明](https://raw.githubusercontent.com/bas3line/ascii/main/README.md)确认安装与配置步骤，再查看[发布版本](https://github.com/bas3line/ascii/releases)。本次为文档、许可原文与维护证据审查，未安装运行。

**近期维护：** [提交修复篮球 SVG 动画循环参数覆盖，并添加测试。](https://github.com/bas3line/ascii/commit/8c6eefbb55b0944f999358e2adf81178f763da87)（2026-11-13）

## English

A TypeScript ASCII-animation library for React, Next.js, Astro, Web Components and plain HTML, with SVG output.

**Requirements and limitations:** Targets modern browsers; package integration typically needs a JavaScript or TypeScript toolchain. Fonts, brands and external assets retain their applicable terms.

**Getting started:** Follow the [official documentation](https://raw.githubusercontent.com/bas3line/ascii/main/README.md) for setup, then check [releases](https://github.com/bas3line/ascii/releases). This review examined documentation, license text and maintenance evidence; the software was not installed or run.

**Recent maintenance:** [The inspected commit fixes basketball SVG animation loop overrides and adds tests.](https://github.com/bas3line/ascii/commit/8c6eefbb55b0944f999358e2adf81178f763da87) (2026-11-13)

## Review evidence

发现线索来自第三方公众号文章索引，原始微信正文未完整读取；用途、环境、许可与维护状态依据仓库当前资料复核。

Discovery uses a third-party WeChat article index; the original article body was not fully read. Current repository sources were reviewed for function, requirements, licensing and maintenance.

- 公众号索引原文 / Indexed WeChat source：[又盘点了 4 个稀奇古怪的 GitHub 项目，第一个很抽象。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537904&idx=1&sn=f91d24d988863606f9abb5445ef79296)（2026-10-22）

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
    "id": "ascii",
    "name": "ASCII",
    "repository": "bas3line/ascii",
    "repo_node_id": "R_kgDOU_IMGw",
    "category": "media",
    "summary": {
      "zh-CN": "可嵌入网页的 TypeScript ASCII 动画组件，支持 React、Next.js、Astro、Web Components 和普通 HTML，也可生成 SVG。",
      "en": "A TypeScript ASCII-animation library for React, Next.js, Astro, Web Components and plain HTML, with SVG output."
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
      "license_sha256": "d5af6735a633d3cb73496e62dee74bd490120345660a88be68752e03f00a75a6",
      "source_url": "https://github.com/bas3line/ascii/blob/9ba5ab14a1946dc1ab875d5c456203079854bdcf/LICENSE",
      "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
      "files": [
        {
          "path": "LICENSE",
          "source_url": "https://github.com/bas3line/ascii/blob/9ba5ab14a1946dc1ab875d5c456203079854bdcf/LICENSE",
          "fetched_at": "2026-11-16T14:23:16.879Z",
          "sha256": "d5af6735a633d3cb73496e62dee74bd490120345660a88be68752e03f00a75a6",
          "source_commit": "9ba5ab14a1946dc1ab875d5c456203079854bdcf"
        }
      ],
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "9ba5ab14a1946dc1ab875d5c456203079854bdcf"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-13T09:18:03Z",
        "url": "https://github.com/bas3line/ascii/commit/8c6eefbb55b0944f999358e2adf81178f763da87",
        "sha": "8c6eefbb55b0944f999358e2adf81178f763da87",
        "summary": "pieces: honor basketball SVG loop overrides",
        "files": [
          "src/basketball.test.ts",
          "src/pieces/basketball.ts",
          "src/svg.ts",
          "src/types.ts"
        ],
        "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
        "qualifies": true,
        "reason": {
          "zh-CN": "提交修复篮球 SVG 动画循环参数覆盖，并添加测试。",
          "en": "The inspected commit fixes basketball SVG animation loop overrides and adds tests."
        }
      }
    ],
    "sources": [
      {
        "article_id": "2247537904_1",
        "title": "又盘点了 4 个稀奇古怪的 GitHub 项目，第一个很抽象。",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537904&idx=1&sn=f91d24d988863606f9abb5445ef79296",
        "published_date": "2026-10-22",
        "account": "逛逛GitHub",
        "source_strength": "third_party_index",
        "index_url": "https://www.noking.tech/github-radar/data/library.json",
        "original_article_body_read": false
      }
    ],
    "discovery": {
      "account": "逛逛GitHub",
      "window_start": "2026-08-16",
      "window_end": "2026-11-16",
      "original_article_body_read": false,
      "repository_review_sources": [
        "https://api.github.com/repos/bas3line/ascii",
        "https://raw.githubusercontent.com/bas3line/ascii/main/README.md",
        "https://github.com/bas3line/ascii/commit/8c6eefbb55b0944f999358e2adf81178f763da87",
        "https://github.com/bas3line/ascii/blob/9ba5ab14a1946dc1ab875d5c456203079854bdcf/LICENSE"
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOU_IMGw",
    "full_name": "bas3line/ascii",
    "stargazers_count": 1232,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "d5af6735a633d3cb73496e62dee74bd490120345660a88be68752e03f00a75a6",
    "last_success_at": "2026-11-16T14:19:21.679Z"
  }
}
```

</details>
