# Text to CAD

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 26417 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:18:44.110Z |

## 中文

把自然语言设计需求转成参数化 CAD 脚本和制造文件的智能体工具。

### 主要功能

- 使用 build123d 与 OpenCASCADE 建模，导出格式包括 STEP 和 STL。
- 包含图纸、PCB、装配和制造检查流程。

### 环境与限制

- 按官方安装指南准备 uv 和支持技能的编码智能体。
- 部分检查依赖外部求解器，结果需要工程复核，不能作为制造合格保证。

### 开始使用

从[官方说明](https://github.com/earthtojake/text-to-cad/blob/main/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/earthtojake/text-to-cad/releases)可用于确认版本。

### 收录复核

把自然语言设计需求转成参数化 CAD 脚本和制造文件的智能体工具。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。

有效维护证据：[v0.11.10](https://github.com/earthtojake/text-to-cad/releases/tag/v0.11.10)，2026-11-13T11:35:12Z。修复板件轮廓拐角处倒圆或倒角在展平时丢失的问题，并增加尺寸与面积回归检查。 2026-11-17 已读取[实现提交](https://github.com/earthtojake/text-to-cad/commit/8ea243463968e81b682d678ace010ad835f162b1)的差异；未运行上游测试。

文章来源：[逛逛GitHub署名文章](https://www.woshipm.com/ai/6487701.html)，平台日期 2026-11-02。已通过公开正文核对仓库链接与作者归属；微信正文未直接读取。

本次为文档与实现证据复核，未安装或运行上游项目。


补充核对作者在公开平台发布或授权发布的文章，确认署名、日期与仓库关联：

- 2026-10-22：[盘点本周 11 个 Star 攀升最多的 GitHub 开源项目。](https://www.woshipm.com/ai/6482138.html)

## English

Agent tools for turning design requests into parametric CAD scripts and manufacturing files.

### Features

- Models parts with build123d and OpenCASCADE and exports STEP, STL and other formats.
- Includes drawings, PCB, assembly and manufacturing checks.

### Requirements and limits

- Follow the installation guide for uv and a skill-capable coding agent.
- Some checks need external solvers
- their results require engineering review and do not certify a design for manufacture.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/earthtojake/text-to-cad/blob/main/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/earthtojake/text-to-cad/releases) for versions.

### Review and provenance

Agent tools for turning design requests into parametric CAD scripts and manufacturing files. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.

Activity: [v0.11.10](https://github.com/earthtojake/text-to-cad/releases/tag/v0.11.10), 2026-11-13T11:35:12Z. Fixes rounded or chamfered outline corners being lost in sheet flattening, with dimension and area regression checks. On 2026-11-17, the [implementation diff](https://github.com/earthtojake/text-to-cad/commit/8ea243463968e81b682d678ace010ad835f162b1) was inspected; upstream tests were not run.

Discovery: [an author-attributed 逛逛GitHub article](https://www.woshipm.com/ai/6487701.html), dated 2026-11-02 on the public platform. Repository links and attribution were checked in its public body; the WeChat body was not read directly.

This review covers documentation and implementation evidence. The upstream project was not installed or run.


Public articles published or authorized by the author were also checked for attribution, date and repository links. See the additional links in the Chinese section.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:58:29.135174Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "text-to-cad",
    "name": "Text to CAD",
    "repository": "earthtojake/text-to-cad",
    "repo_node_id": "R_kgDOSJHpkw",
    "category": "development",
    "summary": {
      "zh-CN": "把自然语言设计需求转成参数化 CAD 脚本和制造文件的智能体工具。",
      "en": "Agent tools for turning design requests into parametric CAD scripts and manufacturing files."
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
      "zh-CN": "把自然语言设计需求转成参数化 CAD 脚本和制造文件的智能体工具。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。",
      "en": "Agent tools for turning design requests into parametric CAD scripts and manufacturing files. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "c11168234f932c4a39bb640571079e73b178b4459682a5507e5944ad723058b3",
      "source_url": "https://github.com/earthtojake/text-to-cad/blob/2738524be8b30ec3d025d73b499fd2a6028af336/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "Root license reviewed. External dependencies and assets retain their individual licenses.",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "2738524be8b30ec3d025d73b499fd2a6028af336"
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-11-13T11:35:12Z",
        "reviewed_at": "2026-11-17T03:15:51.892548+00:00",
        "url": "https://github.com/earthtojake/text-to-cad/releases/tag/v0.11.10",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复板件轮廓拐角处倒圆或倒角在展平时丢失的问题，并增加尺寸与面积回归检查。",
          "en": "Fixes rounded or chamfered outline corners being lost in sheet flattening, with dimension and area regression checks."
        },
        "draft": false,
        "prerelease": false,
        "implementation_evidence": {
          "type": "commit",
          "url": "https://github.com/earthtojake/text-to-cad/commit/8ea243463968e81b682d678ace010ad835f162b1",
          "sha": "8ea243463968e81b682d678ace010ad835f162b1",
          "occurred_at": "2026-11-11T19:16:42Z",
          "reviewed_at": "2026-11-17T03:15:51.892548+00:00",
          "reviewed_files": [
            "packages/cad/src/cad/build123d/_dfm_sheet.py",
            "tests/python/packages/cad/test_dfm_sheet.py"
          ],
          "verification_level": "source_review",
          "upstream_tests_run": false
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/earthtojake/text-to-cad",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/earthtojake/text-to-cad/blob/main/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/earthtojake/text-to-cad/blob/2738524be8b30ec3d025d73b499fd2a6028af336/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/earthtojake/text-to-cad/releases/tag/v0.11.10",
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
    "repo_node_id": "R_kgDOSJHpkw",
    "full_name": "earthtojake/text-to-cad",
    "stargazers_count": 26417,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "c11168234f932c4a39bb640571079e73b178b4459682a5507e5944ad723058b3",
    "last_success_at": "2026-11-16T14:18:44.110Z"
  }
}
```

</details>
