# Deskworlds

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[chaseleantj/deskworlds](https://github.com/chaseleantj/deskworlds)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 468 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:50:00.494Z |

## 中文

在Mac桌面运行可交互的本地3D场景，也可在浏览器中体验。

### 用途与功能

- 使用可交互动态壁纸
- 研究程序化3D场景

提供水景、自然场景、光照和生物互动。菜单栏可切换场景、暂停和投喂。程序按桌面可见性与电源状态降低负载。

### 环境与限制

桌面模式需macOS13+及Xcode命令行工具，安装器会添加登录项；浏览器模式需WebGL2，启动服务需Node20+。持续渲染消耗GPU资源，场景物理不作为科学模拟结果。

### 开始使用

按README构建桌面应用，或先通过浏览器运行；使用菜单栏控制，并保留卸载入口。 参阅[官方 README](https://github.com/chaseleantj/deskworlds/blob/main/README.md)。

### 收录与来源

低Star项目已有桌面宿主、多场景管理、安装卸载和节能逻辑，具备可使用的应用形态。 最近维护：[实现提交](https://github.com/chaseleantj/deskworlds/commit/d3e507cd444e5bbb1bfe6d0969b9a161350b8e5c)（2026-10-18T13:05:19Z）。已核对合并实现：更新珊瑚礁几何、鱼模型、焦散与后处理质量策略。

通过逛逛GitHub的第三方文章索引发现。索引记录了下列文章；本次未读取微信原文，不据此声称已阅读全文。

- 2026-10-12：[5 个 GitHub 上开源的稀奇古怪小玩意儿，这一届网友真天才。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537707&idx=1&sn=1331f4af944d2e655349efed37bab588)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。


补充核对作者在公开平台发布或授权发布的文章，确认署名、日期与仓库关联：

- 2026-10-13：[5 个 GitHub 上开源的稀奇古怪小玩意儿，这一届网友真天才。](https://www.woshipm.com/share/6477077.html)

## English

Runs interactive local 3D scenes on the Mac desktop and in a browser.

### Uses and features

- Use interactive live wallpaper
- Explore procedural 3D scenes

Includes aquatic and nature scenes, lighting and creature interaction, with menu-bar switching, pause and feeding and load reduction based on desktop visibility and power state.

### Requirements and limits

Desktop mode requires macOS 13+ and Xcode command-line tools, and installation adds a login item. Browser mode needs WebGL2 and Node 20+ to start its server. Continuous rendering uses GPU resources; scene behavior is not a scientific simulation result.

### Getting started

Build the desktop app or try the browser version first, then use menu-bar controls and retain the uninstall instructions. See the [official README](https://github.com/chaseleantj/deskworlds/blob/main/README.md).

### Review and provenance

This low-star project has a desktop host, scene management, installation/removal and power-aware behavior, forming a usable application. Recent maintenance: [implementation commit](https://github.com/chaseleantj/deskworlds/commit/d3e507cd444e5bbb1bfe6d0969b9a161350b8e5c) (2026-10-18T13:05:19Z). Reviewed merged implementation updating reef geometry, fish models, caustics and post-processing quality profiles.

Discovered through a third-party index of 逛逛GitHub articles. The index records the articles below; the original WeChat pages were not read in this review. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.


Public articles published or authorized by the author were also checked for attribution, date and repository links. See the additional links in the Chinese section.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:50:00.494Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "deskworlds",
    "name": "Deskworlds",
    "repository": "chaseleantj/deskworlds",
    "repo_node_id": "R_kgDOUf3pQg",
    "category": "media",
    "tags": [],
    "forms": [
      "desktop",
      "web"
    ],
    "platforms": [
      "macos"
    ],
    "aliases": {
      "zh-CN": [
        "Deskworlds"
      ],
      "en": [
        "Deskworlds"
      ]
    },
    "summary": {
      "zh-CN": "在Mac桌面运行可交互的本地3D场景，也可在浏览器中体验。",
      "en": "Runs interactive local 3D scenes on the Mac desktop and in a browser."
    },
    "use_cases": {
      "zh-CN": [
        "使用可交互动态壁纸",
        "研究程序化3D场景"
      ],
      "en": [
        "Use interactive live wallpaper",
        "Explore procedural 3D scenes"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:50:00.494Z",
        "en": "2026-11-16T14:50:00.494Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "b660528234fa02f2c865e920aff83cf4bfc0f0650e6b7f85de91149dad7e3f78",
      "source_url": "https://github.com/chaseleantj/deskworlds/blob/b0642e7c7db1bb16408f4cc1adbd3aab30c5418b/LICENSE",
      "reviewed_at": "2026-11-16T14:50:00.494Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "b0642e7c7db1bb16408f4cc1adbd3aab30c5418b"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/chaseleantj/deskworlds/commit/d3e507cd444e5bbb1bfe6d0969b9a161350b8e5c",
        "occurred_at": "2026-10-18T13:05:19Z",
        "reason": {
          "zh-CN": "已核对合并实现：更新珊瑚礁几何、鱼模型、焦散与后处理质量策略。",
          "en": "Reviewed merged implementation updating reef geometry, fish models, caustics and post-processing quality profiles."
        },
        "reviewed_at": "2026-11-16T14:50:00.494Z",
        "qualifies": true
      }
    ],
    "sources": [
      {
        "url": "https://github.com/chaseleantj/deskworlds/blob/main/README.md",
        "accessed_at": "2026-11-16T14:50:00.494Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/chaseleantj/deskworlds/blob/b0642e7c7db1bb16408f4cc1adbd3aab30c5418b/LICENSE",
        "accessed_at": "2026-11-16T14:50:00.494Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.noking.tech/github-radar/data/library.json",
        "accessed_at": "2026-11-16T14:50:00.494Z",
        "supports": {
          "zh-CN": "第三方索引中的公众号文章归属、时间与项目发现线索；非原文阅读证据。",
          "en": "Third-party account attribution, article dates and discovery leads; not proof of reading the originals."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537707&idx=1&sn=1331f4af944d2e655349efed37bab588",
        "accessed_at": "2026-11-16T14:50:00.494Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-10-12 5 个 GitHub 上开源的稀奇古怪小玩意儿，这一届网友真天才。；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-10-12; not directly read in this review."
        }
      },
      {
        "url": "https://www.woshipm.com/share/6477077.html",
        "accessed_at": "2026-11-16T14:26:01.652964+00:00",
        "published_date": "2026-10-13",
        "author": "逛逛GitHub",
        "supports": {
          "zh-CN": "作者公开发表或授权的文章；已核对署名、日期与仓库链接。",
          "en": "Author-published or authorized public article; attribution, date and repository links checked."
        }
      }
    ],
    "quality_review": {
      "basis": {
        "zh-CN": "低Star项目已有桌面宿主、多场景管理、安装卸载和节能逻辑，具备可使用的应用形态。",
        "en": "This low-star project has a desktop host, scene management, installation/removal and power-aware behavior, forming a usable application."
      },
      "low_star": true
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOUf3pQg",
    "full_name": "chaseleantj/deskworlds",
    "stargazers_count": 468,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "b660528234fa02f2c865e920aff83cf4bfc0f0650e6b7f85de91149dad7e3f78",
    "last_success_at": "2026-11-16T14:19:21.906Z"
  }
}
```

</details>

