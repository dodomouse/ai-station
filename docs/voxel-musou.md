# Voxel Musou

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[mike007jd/voxel-musou](https://github.com/mike007jd/voxel-musou)

| 项目 / Field | 内容 / Value |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 178 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:50:50.290410+00:00 |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:19:05.858Z |

## 中文

浏览器 Three.js 体素动作游戏示例，包含多角色、章节与试炼。适合研究轻量游戏逻辑、渲染和本地进度管理。

**环境与限制：** 通过静态 HTTP 服务加载 ES Modules，无需打包；使用现代浏览器。进度存于当前站点的 localStorage，不包含战斗中途恢复；字体和 Three.js 依赖保留自身许可。

**入门：** 从[官方说明](https://raw.githubusercontent.com/mike007jd/voxel-musou/main/README.md)确认安装与配置步骤，再查看[发布版本](https://github.com/mike007jd/voxel-musou/releases)。本次为文档、许可原文与维护证据审查，未安装运行。

**近期维护：** [提交修复存档缺少记录时的校验，并更新检查脚本。](https://github.com/mike007jd/voxel-musou/commit/3e6d5501d0c103c4869a6f6ae15bac0126f7d788)（2026-10-01）

## English

A browser Three.js voxel-action game with multiple characters, chapters and trials, useful for studying lightweight gameplay, rendering and local progress management.

**Requirements and limitations:** Serve ES modules over static HTTP in a modern browser; no bundling is required. Progress uses the site's localStorage and does not resume mid-battle. Fonts and Three.js retain their licenses.

**Getting started:** Follow the [official documentation](https://raw.githubusercontent.com/mike007jd/voxel-musou/main/README.md) for setup, then check [releases](https://github.com/mike007jd/voxel-musou/releases). This review examined documentation, license text and maintenance evidence; the software was not installed or run.

**Recent maintenance:** [The inspected commit rejects saves without records and updates validation scripts.](https://github.com/mike007jd/voxel-musou/commit/3e6d5501d0c103c4869a6f6ae15bac0126f7d788) (2026-10-01)

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
    "id": "voxel-musou",
    "name": "Voxel Musou",
    "repository": "mike007jd/voxel-musou",
    "repo_node_id": "R_kgDOUoevwQ",
    "category": "development",
    "summary": {
      "zh-CN": "浏览器 Three.js 体素动作游戏示例，包含多角色、章节与试炼，适合研究轻量游戏逻辑、渲染和本地进度管理。",
      "en": "A browser Three.js voxel-action game with multiple characters, chapters and trials, useful for studying lightweight gameplay, rendering and local progress management."
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
      "license_sha256": "a2ffa96dae312e6977ac9cb2914dfbab8d920bd3989304a72d8c73eb256f178d",
      "source_url": "https://github.com/mike007jd/voxel-musou/blob/aba5fb8f43b713e88e8ac3a3105e48f01941dc7f/LICENSE",
      "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
      "files": [
        {
          "path": "LICENSE",
          "source_url": "https://github.com/mike007jd/voxel-musou/blob/aba5fb8f43b713e88e8ac3a3105e48f01941dc7f/LICENSE",
          "fetched_at": "2026-11-16T14:26:57.125Z",
          "sha256": "a2ffa96dae312e6977ac9cb2914dfbab8d920bd3989304a72d8c73eb256f178d",
          "source_commit": "aba5fb8f43b713e88e8ac3a3105e48f01941dc7f"
        }
      ],
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "aba5fb8f43b713e88e8ac3a3105e48f01941dc7f"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-10-01T06:59:05Z",
        "url": "https://github.com/mike007jd/voxel-musou/commit/3e6d5501d0c103c4869a6f6ae15bac0126f7d788",
        "sha": "3e6d5501d0c103c4869a6f6ae15bac0126f7d788",
        "summary": "Reject a save without records; fix a stale check log line",
        "files": [
          "checks/trials.mjs",
          "src/core/progress.js"
        ],
        "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
        "qualifies": true,
        "reason": {
          "zh-CN": "提交修复存档缺少记录时的校验，并更新检查脚本。",
          "en": "The inspected commit rejects saves without records and updates validation scripts."
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
      "zh-CN": "具有可阅读的游戏实现、渲染与进度模块及检查脚本，适合作为小型浏览器游戏学习样例；近期修复真实存档校验问题，未实机试玩。",
      "en": "Provides readable gameplay, rendering and progress modules with checks, making a useful small browser-game example. Recent work fixes real save validation; no hands-on gameplay test was performed."
    },
    "discovery": {
      "account": "逛逛GitHub",
      "window_start": "2026-08-16",
      "window_end": "2026-11-16",
      "original_article_body_read": false,
      "repository_review_sources": [
        "https://api.github.com/repos/mike007jd/voxel-musou",
        "https://raw.githubusercontent.com/mike007jd/voxel-musou/main/README.md",
        "https://github.com/mike007jd/voxel-musou/commit/3e6d5501d0c103c4869a6f6ae15bac0126f7d788",
        "https://github.com/mike007jd/voxel-musou/blob/aba5fb8f43b713e88e8ac3a3105e48f01941dc7f/LICENSE"
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOUoevwQ",
    "full_name": "mike007jd/voxel-musou",
    "stargazers_count": 178,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "a2ffa96dae312e6977ac9cb2914dfbab8d920bd3989304a72d8c73eb256f178d",
    "last_success_at": "2026-11-16T14:19:05.858Z"
  }
}
```

</details>
