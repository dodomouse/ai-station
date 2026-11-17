# 2010 Rust Rewrite Mashup

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[chasmlol/2010-rust-rewrite-mashup](https://github.com/chasmlol/2010-rust-rewrite-mashup)

| 项目 / Field | 内容 / Value |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 951 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:50:50.290410+00:00 |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:19:06.368Z |

## 中文

以 Rust 实现的游戏混搭实验，把 MW2 风格场景、滑板和体素地图组合起来。可用于学习游戏重实现与资源兼容。

**环境与限制：** 需要用户自有 MW2 Steam 游戏文件。部分模式还需 Skate 3 文件，仓库不授予商业游戏资源使用权。优先按 Windows Releases 安装，其他平台按构建文档核对。不能视为独立免费游戏包。

**入门：** 从[官方说明](https://raw.githubusercontent.com/chasmlol/2010-rust-rewrite-mashup/main/README.md)确认安装与配置步骤，再查看[发布版本](https://github.com/chasmlol/2010-rust-rewrite-mashup/releases)。本次为文档、许可原文与维护证据审查，未安装运行。

**近期维护：** [v0.4.0 修复物理卡顿与攻击阻挡相关行为。](https://github.com/chasmlol/2010-rust-rewrite-mashup/releases/tag/v0.4.0)（2026-10-02）

## English

A Rust game-mashup experiment combining MW2-style environments, skating and voxel maps for studying game reimplementation and asset compatibility.

**Requirements and limitations:** Requires user-owned MW2 Steam files; some modes also need Skate 3 files. The repository does not grant rights to commercial game assets. Start with Windows releases and consult build docs for other platforms; it is not a standalone free game bundle.

**Getting started:** Follow the [official documentation](https://raw.githubusercontent.com/chasmlol/2010-rust-rewrite-mashup/main/README.md) for setup, then check [releases](https://github.com/chasmlol/2010-rust-rewrite-mashup/releases). This review examined documentation, license text and maintenance evidence; the software was not installed or run.

**Recent maintenance:** [v0.4.0 fixes physics stutter and attack-blocking behavior.](https://github.com/chasmlol/2010-rust-rewrite-mashup/releases/tag/v0.4.0) (2026-10-02)

## Review evidence

发现线索来自第三方公众号文章索引，原始微信正文未完整读取；用途、环境、许可与维护状态依据仓库当前资料复核。

Discovery uses a third-party WeChat article index; the original article body was not fully read. Current repository sources were reviewed for function, requirements, licensing and maintenance.

- 公众号索引原文 / Indexed WeChat source：[看这 11 个外网爆火的案例，AI 做游戏真的越来越顶了。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538126&idx=1&sn=adf428f2a574155f3cfd0fb2adb1f5d4)（2026-10-28）
- 作者署名转载 / Author-attributed repost：[看这 11 个外网爆火的案例，AI 做游戏真的越来越顶了。](https://www.woshipm.com/ai/6485839.html)（2026-10-29）；仓库链接映射已交叉核对 / repository mapping corroborated.

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
    "id": "2010-rust-rewrite-mashup",
    "name": "2010 Rust Rewrite Mashup",
    "repository": "chasmlol/2010-rust-rewrite-mashup",
    "repo_node_id": "R_kgDOUvC1gg",
    "category": "development",
    "summary": {
      "zh-CN": "以 Rust 实现的游戏混搭实验，把 MW2 风格场景、滑板和体素地图组合起来，可用于学习游戏重实现与资源兼容。",
      "en": "A Rust game-mashup experiment combining MW2-style environments, skating and voxel maps for studying game reimplementation and asset compatibility."
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
      "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
      "source_url": "https://github.com/chasmlol/2010-rust-rewrite-mashup/blob/f608f85e407ff1b7689d54a9aafdd16e95711ac4/LICENSE",
      "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
      "files": [
        {
          "path": "LICENSE",
          "source_url": "https://github.com/chasmlol/2010-rust-rewrite-mashup/blob/f608f85e407ff1b7689d54a9aafdd16e95711ac4/LICENSE",
          "fetched_at": "2026-11-16T14:26:56.770Z",
          "sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
          "source_commit": "f608f85e407ff1b7689d54a9aafdd16e95711ac4"
        }
      ],
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "f608f85e407ff1b7689d54a9aafdd16e95711ac4"
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-10-02T02:28:19Z",
        "url": "https://github.com/chasmlol/2010-rust-rewrite-mashup/releases/tag/v0.4.0",
        "tag": "v0.4.0",
        "summary": "2010 Rust Rewrite Mashup v0.4.0",
        "draft": false,
        "prerelease": false,
        "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
        "qualifies": true,
        "reason": {
          "zh-CN": "v0.4.0 修复物理卡顿与攻击阻挡相关行为。",
          "en": "v0.4.0 fixes physics stutter and attack-blocking behavior."
        }
      }
    ],
    "sources": [
      {
        "article_id": "2247538126_1",
        "title": "看这 11 个外网爆火的案例，AI 做游戏真的越来越顶了。",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538126&idx=1&sn=adf428f2a574155f3cfd0fb2adb1f5d4",
        "published_date": "2026-10-28",
        "account": "逛逛GitHub",
        "source_strength": "third_party_index",
        "index_url": "https://www.noking.tech/github-radar/data/library.json",
        "original_article_body_read": false
      },
      {
        "url": "https://www.woshipm.com/ai/6485839.html",
        "title": "看这 11 个外网爆火的案例，AI 做游戏真的越来越顶了。",
        "published_date": "2026-10-29",
        "account": "逛逛GitHub",
        "source_strength": "author_attributed_repost_repository_mapping",
        "author_attribution_confirmed": true,
        "body_read_method": "public_html_repository_links_and_attribution_extraction",
        "full_text_archived": false
      }
    ],
    "quality_review": {
      "zh-CN": "包含实际 Rust 游戏重实现和连续功能发布，适合兼容层与游戏开发研究；明确自有商业素材要求，未验证实际运行。",
      "en": "Contains substantive Rust game-reimplementation code and functional releases, useful for compatibility and game-development study. User-owned commercial assets are required; runtime behavior was not tested."
    },
    "discovery": {
      "account": "逛逛GitHub",
      "window_start": "2026-08-16",
      "window_end": "2026-11-16",
      "original_article_body_read": false,
      "repository_review_sources": [
        "https://api.github.com/repos/chasmlol/2010-rust-rewrite-mashup",
        "https://raw.githubusercontent.com/chasmlol/2010-rust-rewrite-mashup/main/README.md",
        "https://github.com/chasmlol/2010-rust-rewrite-mashup/releases/tag/v0.4.0",
        "https://github.com/chasmlol/2010-rust-rewrite-mashup/blob/f608f85e407ff1b7689d54a9aafdd16e95711ac4/LICENSE"
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOUvC1gg",
    "full_name": "chasmlol/2010-rust-rewrite-mashup",
    "stargazers_count": 951,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
    "last_success_at": "2026-11-16T14:19:06.368Z"
  }
}
```

</details>
