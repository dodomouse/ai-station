# Claude Community Plugins：目录与校验器

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[anthropics/claude-plugins-community](https://github.com/anthropics/claude-plugins-community)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 4903 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T15:06:51.866Z |

## 中文

提供Claude社区插件目录，以及可复用的插件市场CI校验器。

### 用途与功能

- 发现社区插件并查看安装入口
- 为插件市场增加自动校验

社区目录按审核流程同步。独立GitHub Action可检查清单结构、重复名称、固定提交和来源字段。它还检查变更插件的清单，以及辅助JSON文件。支持完整目录检查和外部来源漂移检查。详见[校验器文档](https://github.com/anthropics/claude-plugins-community/blob/main/.github/actions/validate-plugins/README.md)。

### 环境与限制

目录是只读镜像，提交插件需使用官方提交通道。外部插件有各自许可、依赖与权限。校验器示例使用Ubuntu运行器，并安装Node20、jq和Claude CLI。应固定Action提交与CLI版本。它执行静态清单校验，不能证明插件行为安全。命令来源白名单不审查命令输出。

### 开始使用

用户可按根目录README添加市场，再选择单个插件。市场维护者可按校验器文档配置只读CI任务，并固定版本。 参阅[官方 README](https://github.com/anthropics/claude-plugins-community/blob/main/README.md)。

### 收录与来源

校验器是可直接复用的组合Action，包含多层清单检查与回归测试。本次以这些可执行能力确认工具价值。 最近维护：[实现提交](https://github.com/anthropics/claude-plugins-community/commit/163301d1904c0a994539f5226ce0fcd65b8652bf)（2026-11-06T00:52:06Z）。已核对11月6日实现差异：增加命令来源白名单、严格字符校验和跳过克隆逻辑。测试覆盖未授权来源、命令分隔符和名称拼接。

通过逛逛GitHub的第三方文章索引发现。索引记录了下列文章；本次未读取微信原文，不据此声称已阅读全文。

- 2026-08-25：[用下这 3 个 GitHub 上的超精简 Skill，内容只有几句话，却很好用。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536168&idx=1&sn=3b28f7bc3a53dc9183ff4d8940a12761)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。

## English

Provides a Claude community plugin directory and a reusable marketplace CI validator.

### Uses and features

- Discover community plugins and installation paths
- Add automated validation to plugin marketplaces

The community directory syncs through a review pipeline. A reusable GitHub Action checks manifest structure, duplicate names, pinned revisions and source fields. It also validates changed plugin manifests and auxiliary JSON files, with full-directory and external-source drift checks. See the [validator documentation](https://github.com/anthropics/claude-plugins-community/blob/main/.github/actions/validate-plugins/README.md).

### Requirements and limits

The directory is a read-only mirror; submit plugins through the official channel. External plugins have separate licenses, dependencies and permissions. The validator example uses an Ubuntu runner and installs Node 20, jq and Claude CLI. Pin the action revision and CLI version. Static manifest validation does not establish runtime safety, and command-source exemptions do not inspect command output.

### Getting started

Users can add the marketplace and select a plugin as documented. Marketplace maintainers can configure a read-only CI job from the validator guide and pin its versions. See the [official README](https://github.com/anthropics/claude-plugins-community/blob/main/README.md).

### Review and provenance

The validator is a reusable composite action with layered manifest checks and regression tests. These executable capabilities establish its tool value in this review. Recent maintenance: [implementation commit](https://github.com/anthropics/claude-plugins-community/commit/163301d1904c0a994539f5226ce0fcd65b8652bf) (2026-11-06T00:52:06Z). Reviewed the November 6 implementation adding command-source exemptions, strict character validation and clone skipping. Tests cover unauthorized sources, command separators and name-splicing cases.

Discovered through a third-party index of 逛逛GitHub articles. The index records the articles below; the original WeChat pages were not read in this review. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T15:06:51.866Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "claude-plugins-community",
    "name": "Claude Community Plugins：目录与校验器",
    "repository": "anthropics/claude-plugins-community",
    "repo_node_id": "R_kgDORr03Lg",
    "category": "development",
    "tags": [],
    "forms": [
      "plugin",
      "ci"
    ],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "Claude Community Plugins：目录与校验器"
      ],
      "en": [
        "Claude Community Plugins：目录与校验器"
      ]
    },
    "summary": {
      "zh-CN": "提供Claude社区插件目录，以及可复用的插件市场CI校验器。",
      "en": "Provides a Claude community plugin directory and a reusable marketplace CI validator."
    },
    "use_cases": {
      "zh-CN": [
        "发现社区插件并查看安装入口",
        "为插件市场增加自动校验"
      ],
      "en": [
        "Discover community plugins and installation paths",
        "Add automated validation to plugin marketplaces"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T15:06:51.866Z",
        "en": "2026-11-16T15:06:51.866Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
      "source_url": "https://github.com/anthropics/claude-plugins-community/blob/main/LICENSE",
      "reviewed_at": "2026-11-16T15:06:51.866Z"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/anthropics/claude-plugins-community/commit/163301d1904c0a994539f5226ce0fcd65b8652bf",
        "occurred_at": "2026-11-06T00:52:06Z",
        "reason": {
          "zh-CN": "已核对11月6日实现差异：增加命令来源白名单、严格字符校验和跳过克隆逻辑。测试覆盖未授权来源、命令分隔符和名称拼接。",
          "en": "Reviewed the November 6 implementation adding command-source exemptions, strict character validation and clone skipping. Tests cover unauthorized sources, command separators and name-splicing cases."
        },
        "reviewed_at": "2026-11-16T15:06:51.866Z",
        "qualifies": true
      }
    ],
    "sources": [
      {
        "url": "https://github.com/anthropics/claude-plugins-community/blob/main/README.md",
        "accessed_at": "2026-11-16T15:06:51.866Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/anthropics/claude-plugins-community/blob/main/LICENSE",
        "accessed_at": "2026-11-16T15:06:51.866Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.noking.tech/github-radar/data/library.json",
        "accessed_at": "2026-11-16T15:06:51.852Z",
        "supports": {
          "zh-CN": "第三方索引中的2026-08-25公众号文章与仓库发现线索；未直接阅读微信原文。",
          "en": "Third-party index linking the 2026-08-25 account article to this repository; the original WeChat page was not directly read."
        }
      },
      {
        "url": "https://github.com/anthropics/claude-plugins-community/blob/main/.github/actions/validate-plugins/README.md",
        "accessed_at": "2026-11-16T15:06:51.852Z",
        "supports": {
          "zh-CN": "可复用Action的用途、检查范围、环境、固定版本要求和安全边界。",
          "en": "Reusable action purpose, checks, requirements, version pinning and security boundaries."
        }
      },
      {
        "url": "https://github.com/anthropics/claude-plugins-community/blob/main/.github/actions/validate-plugins/action.yml",
        "accessed_at": "2026-11-16T15:06:51.852Z",
        "supports": {
          "zh-CN": "组合Action入口、输入与依赖安装实现。",
          "en": "Composite-action entry point, inputs and dependency setup implementation."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536168&idx=1&sn=3b28f7bc3a53dc9183ff4d8940a12761",
        "accessed_at": "2026-11-16T15:06:51.866Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-08-25 用下这 3 个 GitHub 上的超精简 Skill，内容只有几句话，却很好用。；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-08-25; not directly read in this review."
        }
      }
    ],
    "quality_review": {
      "basis": {
        "zh-CN": "校验器是可直接复用的组合Action，包含多层清单检查与回归测试。本次以这些可执行能力确认工具价值。",
        "en": "The validator is a reusable composite action with layered manifest checks and regression tests. These executable capabilities establish its tool value in this review."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDORr03Lg",
    "full_name": "anthropics/claude-plugins-community",
    "stargazers_count": 4903,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
    "last_success_at": "2026-11-16T15:06:51.821Z"
  }
}
```

</details>

