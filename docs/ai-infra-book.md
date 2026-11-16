# AI Infra Book

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[bojieli/ai-infra-book](https://github.com/bojieli/ai-infra-book)

| 项目 / Field | 内容 / Value |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 7897 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:50:50.290410+00:00 |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:19:21.983Z |

## 中文

AI 基础设施教材与计算工具，覆盖硬件、模型架构、推理和训练，并提供在线版、PDF/EPUB 及容量估算脚本。

**环境与限制：** 示例计算器使用 Python 3.10 和标准库，无需 GPU；估算依赖假设，需结合实际负载验证。这是教材和辅助工具，并非可直接部署的推理服务。

**入门：** 从[官方说明](https://raw.githubusercontent.com/bojieli/ai-infra-book/main/README.md)确认安装与配置步骤，再查看[发布版本](https://github.com/bojieli/ai-infra-book/releases)。本次为文档、许可原文与维护证据审查，未安装运行。

**近期维护：** [提交修复 PDF 构建器的符号与章节链接，并增加测试，属于有效构建功能修复。](https://github.com/bojieli/ai-infra-book/commit/bee1aad9690ee6aa2923b797c680cc3aebb4ce0e)（2026-10-01）

## English

An AI infrastructure textbook and calculation toolkit covering hardware, model architecture, inference and training, with web, PDF/EPUB and capacity-planning scripts.

**Requirements and limitations:** Example calculators use Python 3.10 and its standard library without requiring a GPU. Estimates depend on assumptions and need workload validation. This is educational material and tooling rather than a deployable inference server.

**Getting started:** Follow the [official documentation](https://raw.githubusercontent.com/bojieli/ai-infra-book/main/README.md) for setup, then check [releases](https://github.com/bojieli/ai-infra-book/releases). This review examined documentation, license text and maintenance evidence; the software was not installed or run.

**Recent maintenance:** [The inspected commit fixes symbols and section links in the PDF builder and adds tests, establishing a substantive build-tool fix.](https://github.com/bojieli/ai-infra-book/commit/bee1aad9690ee6aa2923b797c680cc3aebb4ce0e) (2026-10-01)

## Review evidence

发现线索来自第三方公众号文章索引，原始微信正文未完整读取；用途、环境、许可与维护状态依据仓库当前资料复核。

Discovery uses a third-party WeChat article index; the original article body was not fully read. Current repository sources were reviewed for function, requirements, licensing and maintenance.

- 公众号索引原文 / Indexed WeChat source：[这 6 本 GitHub 上的开源 AI 宝典，那是相当有真东西。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537712&idx=1&sn=0a65b2d17e6b825013c0a4630baa3bc2)（2026-10-13）
- 作者署名转载 / Author-attributed repost：[这 6 本 GitHub 上的开源 AI 宝典，那是相当有真东西。](https://www.woshipm.com/ai/6477469.html)（2026-10-13）；仓库链接映射已交叉核对 / repository mapping corroborated.

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
    "id": "ai-infra-book",
    "name": "AI Infra Book",
    "repository": "bojieli/ai-infra-book",
    "repo_node_id": "R_kgDOUAuQJg",
    "category": "development",
    "summary": {
      "zh-CN": "AI 基础设施教材与计算工具，覆盖硬件、模型架构、推理和训练，并提供在线版、PDF/EPUB 及容量估算脚本。",
      "en": "An AI infrastructure textbook and calculation toolkit covering hardware, model architecture, inference and training, with web, PDF/EPUB and capacity-planning scripts."
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
      "license_sha256": "c1b6a99661affda21c759da02976e76cc6694c23ef564c0f1267cdf8d803ca19",
      "source_url": "https://raw.githubusercontent.com/bojieli/ai-infra-book/main/LICENSE",
      "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
      "files": [
        {
          "path": "LICENSE",
          "source_url": "https://raw.githubusercontent.com/bojieli/ai-infra-book/main/LICENSE",
          "fetched_at": "2026-11-16T14:23:27.862Z",
          "sha256": "c1b6a99661affda21c759da02976e76cc6694c23ef564c0f1267cdf8d803ca19"
        }
      ]
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-10-01T07:44:35Z",
        "url": "https://github.com/bojieli/ai-infra-book/commit/bee1aad9690ee6aa2923b797c680cc3aebb4ce0e",
        "sha": "bee1aad9690ee6aa2923b797c680cc3aebb4ce0e",
        "summary": "Preserve PDF symbols and Russian section links",
        "files": [
          "book-ru/scripts/build_pdf.py",
          "book-ru/tests/test_pdf_build.py",
          "book-zh-tw/preamble.tex",
          "book/preamble.tex",
          "manuscripts/05-算子与运行时.md"
        ],
        "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
        "qualifies": true,
        "reason": {
          "zh-CN": "提交修复 PDF 构建器的符号与章节链接，并增加测试，属于有效构建功能修复。",
          "en": "The inspected commit fixes symbols and section links in the PDF builder and adds tests, establishing a substantive build-tool fix."
        }
      }
    ],
    "sources": [
      {
        "article_id": "2247537712_1",
        "title": "这 6 本 GitHub 上的开源 AI 宝典，那是相当有真东西。",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537712&idx=1&sn=0a65b2d17e6b825013c0a4630baa3bc2",
        "published_date": "2026-10-13",
        "account": "逛逛GitHub",
        "source_strength": "third_party_index",
        "index_url": "https://www.noking.tech/github-radar/data/library.json",
        "original_article_body_read": false
      },
      {
        "url": "https://www.woshipm.com/ai/6477469.html",
        "title": "这 6 本 GitHub 上的开源 AI 宝典，那是相当有真东西。",
        "published_date": "2026-10-13",
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
        "https://api.github.com/repos/bojieli/ai-infra-book",
        "https://raw.githubusercontent.com/bojieli/ai-infra-book/main/README.md",
        "https://github.com/bojieli/ai-infra-book/commit/bee1aad9690ee6aa2923b797c680cc3aebb4ce0e",
        "https://raw.githubusercontent.com/bojieli/ai-infra-book/main/LICENSE"
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOUAuQJg",
    "full_name": "bojieli/ai-infra-book",
    "stargazers_count": 7897,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "c1b6a99661affda21c759da02976e76cc6694c23ef564c0f1267cdf8d803ca19",
    "last_success_at": "2026-11-16T14:19:21.983Z"
  }
}
```

</details>
