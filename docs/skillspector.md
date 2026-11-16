# SkillSpector

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 26363 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:34:39.953Z |

## 中文

扫描智能体技能中的可疑指令、代码行为和安全问题。

### 用途与功能

- 安装技能前检查内容
- 把技能检查接入审核流程

解析技能包与嵌套内容，结合规则和可配置模型分析。输出来源、发现项和检查覆盖信息。提供 CLI 及可选 MCP。

### 环境与限制

需要Python3.12+或Docker。模型辅助路径需要可用服务；扫描受支持语法、资源限额和分析器能力约束。报告不构成安全保证。

### 开始使用

从README选择CLI或Docker安装，再对一个本地技能运行扫描并阅读覆盖诊断。 参阅[官方 README](https://github.com/NVIDIA/SkillSpector/blob/main/README.md)。

### 收录与来源

包含实际解析器、报告与边界控制，并持续修复分析遗漏。 最近维护：[v2.13.5](https://github.com/NVIDIA/SkillSpector/releases/tag/v2.13.5)（2026-11-16T10:10:49Z）。正式版改进大型结构输入、嵌套制品、来源重建与覆盖诊断。

通过逛逛GitHub的第三方文章索引发现。索引记录了下列文章；本次未读取微信原文，不据此声称已阅读全文。

- 2026-10-05：[盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537550&idx=1&sn=29715a80ebde4036ab57651905d6bc3f)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。


补充核对作者在公开平台发布或授权发布的文章，确认署名、日期与仓库关联：

- 2026-10-06：[盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。](https://www.woshipm.com/share/6473850.html)

## English

Scans agent skills for suspicious instructions, code behavior and security issues.

### Uses and features

- Inspect skills before installation
- Integrate skill checks into review workflows

Parses skill bundles and nested content, combines rules with configurable model analysis, and reports provenance, findings and coverage through a CLI and optional MCP.

### Requirements and limits

Requires Python 3.12+ or Docker. Model-assisted paths need a usable provider. Coverage is limited by supported syntax, resource bounds and analyzer capability; reports are not a security guarantee.

### Getting started

Choose CLI or Docker setup, scan a local skill and review coverage diagnostics. See the [official README](https://github.com/NVIDIA/SkillSpector/blob/main/README.md).

### Review and provenance

Includes implemented parsers, reports and resource bounds, with ongoing fixes for analysis gaps. Recent maintenance: [v2.13.5](https://github.com/NVIDIA/SkillSpector/releases/tag/v2.13.5) (2026-11-16T10:10:49Z). The formal release improves large structured inputs, nested artifacts, provenance reconstruction and coverage diagnostics.

Discovered through a third-party index of 逛逛GitHub articles. The index records the articles below; the original WeChat pages were not read in this review. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.


Public articles published or authorized by the author were also checked for attribution, date and repository links. See the additional links in the Chinese section.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:34:39.953Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "skillspector",
    "name": "SkillSpector",
    "repository": "NVIDIA/SkillSpector",
    "repo_node_id": "R_kgDORsnMJw",
    "category": "development",
    "tags": [],
    "forms": [
      "cli",
      "service"
    ],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "SkillSpector"
      ],
      "en": [
        "SkillSpector"
      ]
    },
    "summary": {
      "zh-CN": "扫描智能体技能中的可疑指令、代码行为和安全问题。",
      "en": "Scans agent skills for suspicious instructions, code behavior and security issues."
    },
    "use_cases": {
      "zh-CN": [
        "安装技能前检查内容",
        "把技能检查接入审核流程"
      ],
      "en": [
        "Inspect skills before installation",
        "Integrate skill checks into review workflows"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:34:39.953Z",
        "en": "2026-11-16T14:34:39.953Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "9f8785b47596b2993a17a3fa8d747ae63126a2c5e80a9e77195a907273d71839",
      "source_url": "https://github.com/NVIDIA/SkillSpector/blob/main/LICENSE",
      "reviewed_at": "2026-11-16T14:34:39.953Z"
    },
    "activity_evidence": [
      {
        "type": "release",
        "url": "https://github.com/NVIDIA/SkillSpector/releases/tag/v2.13.5",
        "occurred_at": "2026-11-16T10:10:49Z",
        "reason": {
          "zh-CN": "正式版改进大型结构输入、嵌套制品、来源重建与覆盖诊断。",
          "en": "The formal release improves large structured inputs, nested artifacts, provenance reconstruction and coverage diagnostics."
        },
        "reviewed_at": "2026-11-16T14:34:39.953Z",
        "qualifies": true
      }
    ],
    "sources": [
      {
        "url": "https://github.com/NVIDIA/SkillSpector/blob/main/README.md",
        "accessed_at": "2026-11-16T14:34:39.953Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/NVIDIA/SkillSpector/blob/main/LICENSE",
        "accessed_at": "2026-11-16T14:34:39.953Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.noking.tech/github-radar/data/library.json",
        "accessed_at": "2026-11-16T14:34:39.953Z",
        "supports": {
          "zh-CN": "第三方索引中的公众号文章归属、时间与项目发现线索；非原文阅读证据。",
          "en": "Third-party account attribution, article dates and discovery leads; not proof of reading the originals."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537550&idx=1&sn=29715a80ebde4036ab57651905d6bc3f",
        "accessed_at": "2026-11-16T14:34:39.953Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-10-05 盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-10-05; not directly read in this review."
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
        "zh-CN": "包含实际解析器、报告与边界控制，并持续修复分析遗漏。",
        "en": "Includes implemented parsers, reports and resource bounds, with ongoing fixes for analysis gaps."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDORsnMJw",
    "full_name": "NVIDIA/SkillSpector",
    "stargazers_count": 26363,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "9f8785b47596b2993a17a3fa8d747ae63126a2c5e80a9e77195a907273d71839",
    "last_success_at": "2026-11-16T14:19:44.415Z"
  }
}
```

</details>

