# Ponytail

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 191880 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:32:13.500Z |

## 中文

帮助编码智能体复用已有实现、审查变更，并记录任务成本与测试状态。

### 用途与功能

- 审查修改或全仓代码
- 跟踪编码会话的成本和执行情况

核心技能提供问题分析和复用规则；配套 review、audit、状态栏和本地任务面板可记录会话、token 与测试信息。

### 环境与限制

需要支持的编码智能体。Claude Code 状态栏需 2.1.290+，显示能力因入口而异，包括终端、桌面与 VS Code。各工具适配并非功能完全相同，节省比例属于上游基准而非本次验证。

### 开始使用

从 README 选择 Claude Code、Codex 或其他工具的安装路径，然后在一个项目中使用 review 或 audit。 参阅[官方 README](https://github.com/DietrichGebert/ponytail/blob/main/README.md)。

### 收录与来源

配套本地状态栏、任务记录与代码地图实现，使技能有可观察的运行支持。 最近维护：[v5.3.3](https://github.com/DietrichGebert/ponytail/releases/tag/v5.3.3)（2026-10-29T03:11:08Z）。正式版修复状态栏信息、跨插件命令归属和大型仓库文件读取。

通过逛逛GitHub的第三方文章索引发现。索引记录了下列文章；本次未读取微信原文，不据此声称已阅读全文。

- 2026-11-02：[盘点 10 月份 19 个 Star 蹭蹭涨的 GitHub 项目，第一个很有用。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538256&idx=1&sn=3b97e48392e47b295968f5c66a4ce5f0)
- 2026-10-05：[盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537550&idx=1&sn=29715a80ebde4036ab57651905d6bc3f)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。


补充核对作者在公开平台发布或授权发布的文章，确认署名、日期与仓库关联：

- 2026-11-02：[盘点 10 月份 19 个 Star 蹭蹭涨的 GitHub 项目，第一个很有用。](https://www.woshipm.com/ai/6487701.html)
- 2026-10-06：[盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。](https://www.woshipm.com/share/6473850.html)

## English

Helps coding agents reuse existing implementation, review changes and record task cost and test status.

### Uses and features

- Review changes or a whole repository
- Track coding-session cost and execution

The core skill guides problem analysis and reuse. Review, audit, a status band and a local board record sessions, tokens and test information.

### Requirements and limits

Requires a supported coding agent. The Claude Code band requires 2.1.290+; terminal, desktop and VS Code surfaces differ. Agent adapters do not have full feature parity, and advertised savings are upstream benchmarks rather than this review's results.

### Getting started

Choose the README installation path for Claude Code, Codex or another supported tool, then try review or audit in a project. See the [official README](https://github.com/DietrichGebert/ponytail/blob/main/README.md).

### Review and provenance

Includes implemented local status, task recording and code mapping around the skill. Recent maintenance: [v5.3.3](https://github.com/DietrichGebert/ponytail/releases/tag/v5.3.3) (2026-10-29T03:11:08Z). The formal release fixes status-band data, cross-plugin command attribution and large-repository file reads.

Discovered through a third-party index of 逛逛GitHub articles. The index records the articles below; the original WeChat pages were not read in this review. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.


Public articles published or authorized by the author were also checked for attribution, date and repository links. See the additional links in the Chinese section.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:32:13.500Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "ponytail",
    "name": "Ponytail",
    "repository": "DietrichGebert/ponytail",
    "repo_node_id": "R_kgDOS4HNrw",
    "category": "development",
    "tags": [],
    "forms": [
      "skill",
      "plugin"
    ],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "Ponytail"
      ],
      "en": [
        "Ponytail"
      ]
    },
    "summary": {
      "zh-CN": "帮助编码智能体复用已有实现、审查变更，并记录任务成本与测试状态。",
      "en": "Helps coding agents reuse existing implementation, review changes and record task cost and test status."
    },
    "use_cases": {
      "zh-CN": [
        "审查修改或全仓代码",
        "跟踪编码会话的成本和执行情况"
      ],
      "en": [
        "Review changes or a whole repository",
        "Track coding-session cost and execution"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:32:13.500Z",
        "en": "2026-11-16T14:32:13.500Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "fb1bc6909ac3ef82d5c22106e32ef682b0cff66788fa915fb9b53b15c9d2f3ab",
      "source_url": "https://github.com/DietrichGebert/ponytail/blob/main/LICENSE",
      "reviewed_at": "2026-11-16T14:32:13.500Z"
    },
    "activity_evidence": [
      {
        "type": "release",
        "reason": {
          "zh-CN": "正式版修复状态栏信息、跨插件命令归属和大型仓库文件读取。",
          "en": "The formal release fixes status-band data, cross-plugin command attribution and large-repository file reads."
        },
        "reviewed_at": "2026-11-16T14:32:13.500Z",
        "qualifies": true,
        "url": "https://github.com/DietrichGebert/ponytail/releases/tag/v5.3.3",
        "occurred_at": "2026-10-29T03:11:08Z"
      }
    ],
    "sources": [
      {
        "url": "https://github.com/DietrichGebert/ponytail/blob/main/README.md",
        "accessed_at": "2026-11-16T14:32:13.500Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/DietrichGebert/ponytail/blob/main/LICENSE",
        "accessed_at": "2026-11-16T14:32:13.500Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.noking.tech/github-radar/data/library.json",
        "accessed_at": "2026-11-16T14:32:13.500Z",
        "supports": {
          "zh-CN": "第三方索引中的公众号文章归属、时间与项目发现线索；非原文阅读证据。",
          "en": "Third-party account attribution, article dates and discovery leads; not proof of reading the originals."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538256&idx=1&sn=3b97e48392e47b295968f5c66a4ce5f0",
        "accessed_at": "2026-11-16T14:32:13.500Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-11-02 盘点 10 月份 19 个 Star 蹭蹭涨的 GitHub 项目，第一个很有用。；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-11-02; not directly read in this review."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537550&idx=1&sn=29715a80ebde4036ab57651905d6bc3f",
        "accessed_at": "2026-11-16T14:32:13.500Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-10-05 盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-10-05; not directly read in this review."
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
        "url": "https://www.woshipm.com/share/6473850.html",
        "accessed_at": "2026-11-16T14:26:02.487400+00:00",
        "published_date": "2026-10-06",
        "author": "逛逛GitHub",
        "supports": {
          "zh-CN": "作者公开发表或授权的文章；已核对署名、日期与仓库链接。",
          "en": "Author-published or authorized public article; attribution, date and repository links checked."
        }
      }
    ],
    "quality_review": {
      "basis": {
        "zh-CN": "配套本地状态栏、任务记录与代码地图实现，使技能有可观察的运行支持。",
        "en": "Includes implemented local status, task recording and code mapping around the skill."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOS4HNrw",
    "full_name": "DietrichGebert/ponytail",
    "stargazers_count": 191880,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "fb1bc6909ac3ef82d5c22106e32ef682b0cff66788fa915fb9b53b15c9d2f3ab",
    "last_success_at": "2026-11-16T14:18:44.116Z"
  }
}
```

</details>

