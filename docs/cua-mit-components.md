# Cua（MIT 桌面自动化组件）

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[trycua/cua](https://github.com/trycua/cua)

| 项目 / Field | 内容 / Value |
| --- | --- |
| 分类 / Category | 自动化 / Automation |
| 状态 / Status | 已收录 / Included |
| Star | 32442 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:50:50.290410+00:00 |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:19:44.539Z |

## 中文

收录 Cua 的 MIT 许可 SDK、CLI、Driver 和 Lume，用于 Agent 截图、输入控制及本地虚拟电脑管理。

**环境与限制：** Driver 支持 macOS、Windows、Linux，Lume 的本地 macOS 虚拟化需要 Apple Silicon；需配置权限、运行环境与模型。Spaces 和 DriverBench 使用 FSL，不属于本词条收录范围，不能把整库视为 MIT。

**入门：** 从[官方说明](https://raw.githubusercontent.com/trycua/cua/main/README.md)确认安装与配置步骤，再查看[发布版本](https://github.com/trycua/cua/releases)。本次为文档、许可原文与维护证据审查，未安装运行。

**近期维护：** [核验 MIT Linux Driver 提交，修复嵌套合成器中的点击与滚动事件；未使用 FSL Spaces 活动作为准入证据。](https://github.com/trycua/cua/commit/d88757e613c6a5f60508533bd3bb71fb383140cf)（2026-11-16）

## English

Covers Cua's MIT-licensed SDK, CLI, Driver and Lume components for agent screenshots, input control and local virtual-computer management.

**Requirements and limitations:** Driver supports macOS, Windows and Linux; Lume's local macOS virtualization requires Apple Silicon. Configure permissions, runtimes and models. Spaces and DriverBench use FSL and are excluded from this entry; the entire monorepo is not MIT.

**Getting started:** Follow the [official documentation](https://raw.githubusercontent.com/trycua/cua/main/README.md) for setup, then check [releases](https://github.com/trycua/cua/releases). This review examined documentation, license text and maintenance evidence; the software was not installed or run.

**Recent maintenance:** [An inspected MIT Linux Driver commit fixes click and scroll delivery in the nested compositor; eligibility does not rely on FSL Spaces activity.](https://github.com/trycua/cua/commit/d88757e613c6a5f60508533bd3bb71fb383140cf) (2026-11-16)

## Review evidence

发现线索来自第三方公众号文章索引，原始微信正文未完整读取；用途、环境、许可与维护状态依据仓库当前资料复核。

Discovery uses a third-party WeChat article index; the original article body was not fully read. Current repository sources were reviewed for function, requirements, licensing and maintenance.

- 公众号索引原文 / Indexed WeChat source：[盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537550&idx=1&sn=29715a80ebde4036ab57651905d6bc3f)（2026-10-05）
- 作者署名转载 / Author-attributed repost：[盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。](https://www.woshipm.com/share/6473850.html)（2026-10-06）；仓库链接映射已交叉核对 / repository mapping corroborated.

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
    "id": "cua-mit-components",
    "name": "Cua（MIT 桌面自动化组件）",
    "repository": "trycua/cua",
    "repo_node_id": "R_kgDONyaAvQ",
    "category": "automation",
    "summary": {
      "zh-CN": "收录 Cua 的 MIT 许可 SDK、CLI、Driver 和 Lume，用于 Agent 截图、输入控制及本地虚拟电脑管理。",
      "en": "Covers Cua's MIT-licensed SDK, CLI, Driver and Lume components for agent screenshots, input control and local virtual-computer management."
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
      "license_sha256": "c0779290c1d4783169aa3dbfb55feb505e563ef8a004bbf55298ceffcfbda8d9",
      "source_url": "https://github.com/trycua/cua/blob/72273ef7da372ddb0477151cd9e2ae3772593110/LICENSE.md",
      "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
      "files": [
        {
          "path": "LICENSE.md",
          "source_url": "https://github.com/trycua/cua/blob/72273ef7da372ddb0477151cd9e2ae3772593110/LICENSE.md",
          "fetched_at": "2026-11-16T14:23:28.051Z",
          "sha256": "c0779290c1d4783169aa3dbfb55feb505e563ef8a004bbf55298ceffcfbda8d9",
          "source_commit": "72273ef7da372ddb0477151cd9e2ae3772593110"
        }
      ],
      "scope": "Only MIT SDK, CLI, Driver and Lume components. FSL Spaces and DriverBench are excluded.",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "72273ef7da372ddb0477151cd9e2ae3772593110"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-16T10:49:43Z",
        "url": "https://github.com/trycua/cua/commit/d88757e613c6a5f60508533bd3bb71fb383140cf",
        "sha": "d88757e613c6a5f60508533bd3bb71fb383140cf",
        "summary": "fix(cua-driver): deliver desktop click and scroll on the nested cua-compositor (#7926)",
        "files": [
          "libs/cua-driver/rust/crates/platform-linux/src/atspi/native.rs",
          "libs/cua-driver/rust/crates/platform-linux/src/wayland/mod.rs",
          "nix/cua-driver/compositor/cua_compositor_patch.py"
        ],
        "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
        "qualifies": true,
        "reason": {
          "zh-CN": "核验 MIT Linux Driver 提交，修复嵌套合成器中的点击与滚动事件；未使用 FSL Spaces 活动作为准入证据。",
          "en": "An inspected MIT Linux Driver commit fixes click and scroll delivery in the nested compositor; eligibility does not rely on FSL Spaces activity."
        }
      }
    ],
    "sources": [
      {
        "article_id": "2247537550_1",
        "title": "盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537550&idx=1&sn=29715a80ebde4036ab57651905d6bc3f",
        "published_date": "2026-10-05",
        "account": "逛逛GitHub",
        "source_strength": "third_party_index",
        "index_url": "https://www.noking.tech/github-radar/data/library.json",
        "original_article_body_read": false
      },
      {
        "url": "https://www.woshipm.com/share/6473850.html",
        "title": "盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。",
        "published_date": "2026-10-06",
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
        "https://api.github.com/repos/trycua/cua",
        "https://raw.githubusercontent.com/trycua/cua/main/README.md",
        "https://github.com/trycua/cua/commit/d88757e613c6a5f60508533bd3bb71fb383140cf",
        "https://github.com/trycua/cua/blob/72273ef7da372ddb0477151cd9e2ae3772593110/LICENSE.md"
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDONyaAvQ",
    "full_name": "trycua/cua",
    "stargazers_count": 32442,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "c0779290c1d4783169aa3dbfb55feb505e563ef8a004bbf55298ceffcfbda8d9",
    "last_success_at": "2026-11-16T14:19:44.539Z"
  }
}
```

</details>
