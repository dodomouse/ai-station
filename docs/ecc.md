# ECC

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[affaan-m/ECC](https://github.com/affaan-m/ECC)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 304243 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:32:13.687Z |

## 中文

为编码智能体组合规划、审查、记忆、上下文管理和工程检查。

### 用途与功能

- 复用团队的编码流程
- 管理智能体会话上下文与验证步骤

提供技能、角色、hooks、规则和 AgentShield 扫描工具；支持 Claude Code、Codex 及能力不同的其他适配器。

### 环境与限制

通用包需要 Node.js 18+；Claude 插件安装还需 Git 与 Claude Code 2.1+。各宿主能力不同，必须查看支持矩阵。MIT 仓库与收费 ECC Pro 托管应用应分别理解。

### 开始使用

按 README 选择一个安装路径和作用范围，避免叠加同一工具的插件与完整手工安装。 参阅[官方 README](https://github.com/affaan-m/ECC/blob/main/README.md)。

### 收录与来源

具备可执行hooks、上下文处理和回归测试，超出提示词集合。 最近维护：[实现提交](https://github.com/affaan-m/ECC/commit/fafdfb5de6e1ae75c6c0a413132c6a34b2141a5d)（2026-10-30T02:42:36Z）。已核对实现差异：严格校验上下文预算，并修复压缩提醒阈值；附回归测试。

通过逛逛GitHub的第三方文章索引发现。索引记录了下列文章；本次未读取微信原文，不据此声称已阅读全文。

- 2026-11-02：[盘点 10 月份 19 个 Star 蹭蹭涨的 GitHub 项目，第一个很有用。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538256&idx=1&sn=3b97e48392e47b295968f5c66a4ce5f0)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。


补充核对作者在公开平台发布或授权发布的文章，确认署名、日期与仓库关联：

- 2026-11-02：[盘点 10 月份 19 个 Star 蹭蹭涨的 GitHub 项目，第一个很有用。](https://www.woshipm.com/ai/6487701.html)

## English

Combines planning, review, memory, context management and engineering checks for coding agents.

### Uses and features

- Reuse engineering workflows
- Manage agent context and verification steps

Includes skills, roles, hooks, rules and AgentShield scanning, with Claude Code, Codex and other adapters of varying capability.

### Requirements and limits

The universal package requires Node.js 18+; Claude plugin setup also needs Git and Claude Code 2.1+. Host capabilities vary, so check the support matrix. The MIT repository and paid ECC Pro hosted app are separate offerings.

### Getting started

Choose one installation path and scope from the README; avoid stacking a plugin with a full manual install for the same tool. See the [official README](https://github.com/affaan-m/ECC/blob/main/README.md).

### Review and provenance

Includes executable hooks, context processing and regression tests beyond prompt collections. Recent maintenance: [implementation commit](https://github.com/affaan-m/ECC/commit/fafdfb5de6e1ae75c6c0a413132c6a34b2141a5d) (2026-10-30T02:42:36Z). Reviewed implementation changes that validate context budgets and repair compaction reminder thresholds, with regression tests.

Discovered through a third-party index of 逛逛GitHub articles. The index records the articles below; the original WeChat pages were not read in this review. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.


Public articles published or authorized by the author were also checked for attribution, date and repository links. See the additional links in the Chinese section.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:32:13.687Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "ecc",
    "name": "ECC",
    "repository": "affaan-m/ECC",
    "repo_node_id": "R_kgDOQ77-1A",
    "category": "development",
    "tags": [],
    "forms": [
      "plugin",
      "skill",
      "cli"
    ],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "ECC"
      ],
      "en": [
        "ECC"
      ]
    },
    "summary": {
      "zh-CN": "为编码智能体组合规划、审查、记忆、上下文管理和工程检查。",
      "en": "Combines planning, review, memory, context management and engineering checks for coding agents."
    },
    "use_cases": {
      "zh-CN": [
        "复用团队的编码流程",
        "管理智能体会话上下文与验证步骤"
      ],
      "en": [
        "Reuse engineering workflows",
        "Manage agent context and verification steps"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:32:13.687Z",
        "en": "2026-11-16T14:32:13.687Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "326146379f01bb137c0a5d3c54770c1aa31076705c8b88a7f6b26a460f6221b2",
      "source_url": "https://github.com/affaan-m/ECC/blob/main/LICENSE",
      "reviewed_at": "2026-11-16T14:32:13.687Z"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/affaan-m/ECC/commit/fafdfb5de6e1ae75c6c0a413132c6a34b2141a5d",
        "occurred_at": "2026-10-30T02:42:36Z",
        "reason": {
          "zh-CN": "已核对实现差异：严格校验上下文预算，并修复压缩提醒阈值；附回归测试。",
          "en": "Reviewed implementation changes that validate context budgets and repair compaction reminder thresholds, with regression tests."
        },
        "reviewed_at": "2026-11-16T14:32:13.687Z",
        "qualifies": true
      }
    ],
    "sources": [
      {
        "url": "https://github.com/affaan-m/ECC/blob/main/README.md",
        "accessed_at": "2026-11-16T14:32:13.687Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/affaan-m/ECC/blob/main/LICENSE",
        "accessed_at": "2026-11-16T14:32:13.687Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.noking.tech/github-radar/data/library.json",
        "accessed_at": "2026-11-16T14:32:13.687Z",
        "supports": {
          "zh-CN": "第三方索引中的公众号文章归属、时间与项目发现线索；非原文阅读证据。",
          "en": "Third-party account attribution, article dates and discovery leads; not proof of reading the originals."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538256&idx=1&sn=3b97e48392e47b295968f5c66a4ce5f0",
        "accessed_at": "2026-11-16T14:32:13.687Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-11-02 盘点 10 月份 19 个 Star 蹭蹭涨的 GitHub 项目，第一个很有用。；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-11-02; not directly read in this review."
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
      }
    ],
    "quality_review": {
      "basis": {
        "zh-CN": "具备可执行hooks、上下文处理和回归测试，超出提示词集合。",
        "en": "Includes executable hooks, context processing and regression tests beyond prompt collections."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOQ77-1A",
    "full_name": "affaan-m/ECC",
    "stargazers_count": 304243,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "326146379f01bb137c0a5d3c54770c1aa31076705c8b88a7f6b26a460f6221b2",
    "last_success_at": "2026-11-16T14:19:05.909Z"
  }
}
```

</details>

