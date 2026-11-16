# Claude Plugins Official

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 47430 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:19:05.928Z |

## 中文

Anthropic 维护的 Claude 插件目录，提供开发与工作流程扩展。

### 主要功能

- 按插件安装技能、命令、钩子和工具连接。
- 包含官方实现及独立第三方扩展入口。

### 环境与限制

- 需要兼容插件的 Claude 客户端及其账号。
- 根许可证不自动覆盖外部插件，应逐个检查来源和权限。

### 开始使用

从[官方说明](https://github.com/anthropics/claude-plugins-official/blob/main/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/anthropics/claude-plugins-official/releases)可用于确认版本。

### 收录复核

Anthropic 维护的 Claude 插件目录，提供开发与工作流程扩展。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。

有效维护证据：[893173fb82](https://github.com/anthropics/claude-plugins-official/commit/893173fb82a7184fcf3f08ae55930016d84fd588)，2026-11-13T19:25:14Z。新增主题插件与烟花钩子的实现。

文章来源：[逛逛GitHub署名文章](https://www.woshipm.com/ai/6487701.html)，平台日期 2026-11-02。已通过公开正文核对仓库链接与作者归属；微信正文未直接读取。

本次为文档与实现证据复核，未安装或运行上游项目。


补充核对作者在公开平台发布或授权发布的文章，确认署名、日期与仓库关联：

- 2026-10-22：[盘点本周 11 个 Star 攀升最多的 GitHub 开源项目。](https://www.woshipm.com/ai/6482138.html)

## English

Anthropic's plugin directory for extending Claude development and work workflows.

### Features

- Installs skills, commands, hooks and tool connections by plugin.
- Contains official implementations and entries for independent third-party extensions.

### Requirements and limits

- Requires a compatible Claude client and account.
- The root license does not automatically cover external plugins
- review their sources and permissions individually.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/anthropics/claude-plugins-official/blob/main/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/anthropics/claude-plugins-official/releases) for versions.

### Review and provenance

Anthropic's plugin directory for extending Claude development and work workflows. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.

Activity: [893173fb82](https://github.com/anthropics/claude-plugins-official/commit/893173fb82a7184fcf3f08ae55930016d84fd588), 2026-11-13T19:25:14Z. Adds a theme plugin and its fireworks hook implementation.

Discovery: [an author-attributed 逛逛GitHub article](https://www.woshipm.com/ai/6487701.html), dated 2026-11-02 on the public platform. Repository links and attribution were checked in its public body; the WeChat body was not read directly.

This review covers documentation and implementation evidence. The upstream project was not installed or run.


Public articles published or authorized by the author were also checked for attribution, date and repository links. See the additional links in the Chinese section.

## Review evidence

```json
{
  "evaluated_at": "2026-11-16T14:58:29.135174Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "claude-plugins-official",
    "name": "Claude Plugins Official",
    "repository": "anthropics/claude-plugins-official",
    "repo_node_id": "R_kgDOQZyFQA",
    "category": "development",
    "summary": {
      "zh-CN": "Anthropic 维护的 Claude 插件目录，提供开发与工作流程扩展。",
      "en": "Anthropic's plugin directory for extending Claude development and work workflows."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:58:29.135174Z",
        "en": "2026-11-16T14:58:29.135174Z"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "Anthropic 维护的 Claude 插件目录，提供开发与工作流程扩展。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。",
      "en": "Anthropic's plugin directory for extending Claude development and work workflows. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
      "source_url": "https://github.com/anthropics/claude-plugins-official/blob/main/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "Root license reviewed. External dependencies and assets retain their individual licenses."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-13T19:25:14Z",
        "reviewed_at": "2026-11-16T14:58:29.135174Z",
        "url": "https://github.com/anthropics/claude-plugins-official/commit/893173fb82a7184fcf3f08ae55930016d84fd588",
        "qualifies": true,
        "reason": {
          "zh-CN": "新增主题插件与烟花钩子的实现。",
          "en": "Adds a theme plugin and its fireworks hook implementation."
        },
        "reviewed_files": [
          "plugins/theme-examples/LICENSE",
          "plugins/theme-examples/hooks/fireworks.ts",
          "plugins/theme-examples/hooks/project-key.ts"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/anthropics/claude-plugins-official",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/anthropics/claude-plugins-official/blob/main/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/anthropics/claude-plugins-official/blob/main/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/anthropics/claude-plugins-official/commit/893173fb82a7184fcf3f08ae55930016d84fd588",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://www.woshipm.com/ai/6487701.html",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
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
    "article_source": {
      "article_id": "2247538256_1",
      "title": "盘点 10 月份 19 个 Star 蹭蹭涨的 GitHub 项目，第一个很有用。",
      "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538256&idx=1&sn=3b97e48392e47b295968f5c66a4ce5f0",
      "published_date": "2026-11-02",
      "account": "逛逛GitHub",
      "content_review_url": "https://www.woshipm.com/ai/6487701.html",
      "content_review_kind": "author-attributed public article",
      "wechat_direct_body_read": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOQZyFQA",
    "full_name": "anthropics/claude-plugins-official",
    "stargazers_count": 47430,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
    "last_success_at": "2026-11-16T14:19:05.928Z"
  }
}
```
