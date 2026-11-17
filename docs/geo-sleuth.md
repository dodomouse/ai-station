# Geo Sleuth

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[Oldcircle/geo-sleuth](https://github.com/Oldcircle/geo-sleuth)

| 项目 / Field | 内容 / Value |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 7109 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:50:50.290410+00:00 |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:19:06.595Z |

## 中文

为 Agent 提供照片地理定位流程，综合地形、天际线、道路和地图检索，输出候选位置、观察方向与证据。

**环境与限制：** 需要 Python 3.10、uv、curl；反向图片搜索需要浏览器，部分模型需下载且可选 GPU。仅分析有权使用的图片；结果是可复核推断，不能作为已核实位置或身份。

**入门：** 从[官方说明](https://raw.githubusercontent.com/Oldcircle/geo-sleuth/main/README.md)确认安装与配置步骤，再查看[发布版本](https://github.com/Oldcircle/geo-sleuth/releases)。本次为文档、许可原文与维护证据审查，未安装运行。

**近期维护：** [提交修复行政区名称、ISO 国家代码与国界查询逻辑，并添加测试。](https://github.com/Oldcircle/geo-sleuth/commit/8245bf551b6b2469cbcedb021a980ff40c7530c2)（2026-11-16）

## English

Provides an agent workflow for locating photos from terrain, skylines, roads and map searches, returning candidate locations, viewing directions and evidence.

**Requirements and limitations:** Requires Python 3.10, uv and curl; reverse-image search uses a browser, while some models require downloads and optionally a GPU. Use images you are authorized to analyze. Results are hypotheses requiring verification.

**Getting started:** Follow the [official documentation](https://raw.githubusercontent.com/Oldcircle/geo-sleuth/main/README.md) for setup, then check [releases](https://github.com/Oldcircle/geo-sleuth/releases). This review examined documentation, license text and maintenance evidence; the software was not installed or run.

**Recent maintenance:** [The inspected commit fixes administrative-region, country-code and boundary lookup logic with tests.](https://github.com/Oldcircle/geo-sleuth/commit/8245bf551b6b2469cbcedb021a980ff40c7530c2) (2026-11-16)

## Review evidence

发现线索来自第三方公众号文章索引，原始微信正文未完整读取；用途、环境、许可与维护状态依据仓库当前资料复核。

Discovery uses a third-party WeChat article index; the original article body was not fully read. Current repository sources were reviewed for function, requirements, licensing and maintenance.

- 公众号索引原文 / Indexed WeChat source：[最近又刷到 4 个黑科技 GitHub 项目，第 3 个重点看看。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537991&idx=1&sn=69fafc227ed7436bf409e5cd3dd1a43d)（2026-10-24）

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
    "id": "geo-sleuth",
    "name": "Geo Sleuth",
    "repository": "Oldcircle/geo-sleuth",
    "repo_node_id": "R_kgDOUf44tQ",
    "category": "ai",
    "summary": {
      "zh-CN": "为 Agent 提供照片地理定位流程，综合地形、天际线、道路和地图检索，输出候选位置、观察方向与证据。",
      "en": "Provides an agent workflow for locating photos from terrain, skylines, roads and map searches, returning candidate locations, viewing directions and evidence."
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
      "license_sha256": "bd374c9fb4dcb3273b0e1098445ce62355aaa66f45df18971a84a037ed89e4b0",
      "source_url": "https://github.com/Oldcircle/geo-sleuth/blob/8245bf551b6b2469cbcedb021a980ff40c7530c2/LICENSE",
      "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
      "files": [
        {
          "path": "LICENSE",
          "source_url": "https://github.com/Oldcircle/geo-sleuth/blob/8245bf551b6b2469cbcedb021a980ff40c7530c2/LICENSE",
          "fetched_at": "2026-11-16T14:23:16.697Z",
          "sha256": "bd374c9fb4dcb3273b0e1098445ce62355aaa66f45df18971a84a037ed89e4b0",
          "source_commit": "8245bf551b6b2469cbcedb021a980ff40c7530c2"
        }
      ],
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "8245bf551b6b2469cbcedb021a980ff40c7530c2"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-16T07:05:13Z",
        "url": "https://github.com/Oldcircle/geo-sleuth/commit/8245bf551b6b2469cbcedb021a980ff40c7530c2",
        "sha": "8245bf551b6b2469cbcedb021a980ff40c7530c2",
        "summary": "regions: correct administrative lookup and country boundaries (#82)",
        "files": [
          "skills/geo-sleuth/regions/README.md",
          "skills/geo-sleuth/scripts/board.py",
          "skills/geo-sleuth/scripts/clues.py",
          "skills/geo-sleuth/scripts/gazetteer.py",
          "skills/geo-sleuth/scripts/regions.py",
          "skills/geo-sleuth/tests/test_gazetteer.py",
          "skills/geo-sleuth/tests/test_regions.py"
        ],
        "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
        "qualifies": true,
        "reason": {
          "zh-CN": "提交修复行政区名称、ISO 国家代码与国界查询逻辑，并添加测试。",
          "en": "The inspected commit fixes administrative-region, country-code and boundary lookup logic with tests."
        }
      }
    ],
    "sources": [
      {
        "article_id": "2247537991_1",
        "title": "最近又刷到 4 个黑科技 GitHub 项目，第 3 个重点看看。",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537991&idx=1&sn=69fafc227ed7436bf409e5cd3dd1a43d",
        "published_date": "2026-10-24",
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
        "https://api.github.com/repos/oldcircle/geo-sleuth",
        "https://raw.githubusercontent.com/Oldcircle/geo-sleuth/main/README.md",
        "https://github.com/Oldcircle/geo-sleuth/commit/8245bf551b6b2469cbcedb021a980ff40c7530c2",
        "https://github.com/Oldcircle/geo-sleuth/blob/8245bf551b6b2469cbcedb021a980ff40c7530c2/LICENSE"
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOUf44tQ",
    "full_name": "Oldcircle/geo-sleuth",
    "stargazers_count": 7109,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "bd374c9fb4dcb3273b0e1098445ce62355aaa66f45df18971a84a037ed89e4b0",
    "last_success_at": "2026-11-16T14:19:06.595Z"
  }
}
```

</details>
