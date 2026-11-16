# Holo Card Studio

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[EverettFish/holo-card-studio](https://github.com/EverettFish/holo-card-studio)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 2106 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:47:41.468Z |

## 中文

把分层图片制作成可旋转的全息卡网页和可编辑Blender工程。

### 用途与功能

- 制作人物或产品展示卡
- 研究全息材质与视差

使用主体、背景、线稿和文字层，生成Three.js浏览器展示、Blender场景和渲染输出；配置可复用。

### 环境与限制

需要Python3与Pillow、Node.js与npm，以及Blender；素材生成路径还依赖相应智能体或图像服务。输入图片版权、渲染资源和第三方工具许可另计。效果随浏览器和GPU变化。

### 开始使用

按README准备四层素材与card-config，再运行生成流程并在浏览器和Blender中检查。 参阅[官方 README](https://github.com/EverettFish/holo-card-studio/blob/main/README.md)。

### 收录与来源

提供可重复的材质与网页生成脚本，输出可编辑工程，超出单个展示页面。 最近维护：[实现提交](https://github.com/EverettFish/holo-card-studio/commit/6103d539a74e16bcd644758eb5747111aa30ca7a)（2026-09-11T10:48:39Z）。已核对实现：恢复流程调度、修复卡背UV方向，并兼容Blender合成节点与macOS Metal。

通过逛逛GitHub的第三方文章索引发现。索引记录了下列文章；本次未读取微信原文，不据此声称已阅读全文。

- 2026-09-18：[推荐 4 个夯夯夯夯的 GitHub 开源项目，特别是第 2 个。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537034&idx=1&sn=a81b159785dac2887c1145f48825dd72)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。


补充核对作者在公开平台发布或授权发布的文章，确认署名、日期与仓库关联：

- 2026-09-18：[推荐 4 个夯夯夯夯的 GitHub 开源项目，特别是第 2 个。](https://www.woshipm.com/ai/6466407.html)

## English

Builds layered images into interactive holographic-card pages and editable Blender projects.

### Uses and features

- Create character or product cards
- Explore holographic materials and parallax

Uses subject, background, line-art and text layers to generate Three.js viewers, Blender scenes and rendered outputs with reusable configuration.

### Requirements and limits

Requires Python 3 with Pillow, Node.js/npm and Blender; image generation also needs an agent or image service. Input rights, rendering resources and third-party tool terms are separate. Effects vary with browser and GPU.

### Getting started

Prepare four image layers and card-config, run the build workflow and inspect the browser and Blender outputs. See the [official README](https://github.com/EverettFish/holo-card-studio/blob/main/README.md).

### Review and provenance

Provides repeatable material and page generation scripts with editable project outputs beyond a single demo. Recent maintenance: [implementation commit](https://github.com/EverettFish/holo-card-studio/commit/6103d539a74e16bcd644758eb5747111aa30ca7a) (2026-09-11T10:48:39Z). Reviewed implementation restoring workflow dispatch, fixing rear UV orientation and supporting Blender compositor versions and macOS Metal.

Discovered through a third-party index of 逛逛GitHub articles. The index records the articles below; the original WeChat pages were not read in this review. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.


Public articles published or authorized by the author were also checked for attribution, date and repository links. See the additional links in the Chinese section.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:47:41.468Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "holo-card-studio",
    "name": "Holo Card Studio",
    "repository": "EverettFish/holo-card-studio",
    "repo_node_id": "R_kgDOUQoDJQ",
    "category": "media",
    "tags": [],
    "forms": [
      "skill",
      "cli"
    ],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "Holo Card Studio"
      ],
      "en": [
        "Holo Card Studio"
      ]
    },
    "summary": {
      "zh-CN": "把分层图片制作成可旋转的全息卡网页和可编辑Blender工程。",
      "en": "Builds layered images into interactive holographic-card pages and editable Blender projects."
    },
    "use_cases": {
      "zh-CN": [
        "制作人物或产品展示卡",
        "研究全息材质与视差"
      ],
      "en": [
        "Create character or product cards",
        "Explore holographic materials and parallax"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:47:41.468Z",
        "en": "2026-11-16T14:47:41.468Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "8fb0edc794206c5d9b5b46717803a07c21c2411b0ee73a966df2a7e71eb74069",
      "source_url": "https://github.com/EverettFish/holo-card-studio/blob/main/LICENSE",
      "reviewed_at": "2026-11-16T14:47:41.468Z"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/EverettFish/holo-card-studio/commit/6103d539a74e16bcd644758eb5747111aa30ca7a",
        "occurred_at": "2026-09-11T10:48:39Z",
        "reason": {
          "zh-CN": "已核对实现：恢复流程调度、修复卡背UV方向，并兼容Blender合成节点与macOS Metal。",
          "en": "Reviewed implementation restoring workflow dispatch, fixing rear UV orientation and supporting Blender compositor versions and macOS Metal."
        },
        "reviewed_at": "2026-11-16T14:47:41.468Z",
        "qualifies": true
      }
    ],
    "sources": [
      {
        "url": "https://github.com/EverettFish/holo-card-studio/blob/main/README.md",
        "accessed_at": "2026-11-16T14:47:41.468Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/EverettFish/holo-card-studio/blob/main/LICENSE",
        "accessed_at": "2026-11-16T14:47:41.468Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.noking.tech/github-radar/data/library.json",
        "accessed_at": "2026-11-16T14:47:41.468Z",
        "supports": {
          "zh-CN": "第三方索引中的公众号文章归属、时间与项目发现线索；非原文阅读证据。",
          "en": "Third-party account attribution, article dates and discovery leads; not proof of reading the originals."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537034&idx=1&sn=a81b159785dac2887c1145f48825dd72",
        "accessed_at": "2026-11-16T14:47:41.468Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-09-18 推荐 4 个夯夯夯夯的 GitHub 开源项目，特别是第 2 个。；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-09-18; not directly read in this review."
        }
      },
      {
        "url": "https://www.woshipm.com/ai/6466407.html",
        "accessed_at": "2026-11-16T14:26:03.445387+00:00",
        "published_date": "2026-09-18",
        "author": "逛逛GitHub",
        "supports": {
          "zh-CN": "作者公开发表或授权的文章；已核对署名、日期与仓库链接。",
          "en": "Author-published or authorized public article; attribution, date and repository links checked."
        }
      }
    ],
    "quality_review": {
      "basis": {
        "zh-CN": "提供可重复的材质与网页生成脚本，输出可编辑工程，超出单个展示页面。",
        "en": "Provides repeatable material and page generation scripts with editable project outputs beyond a single demo."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOUQoDJQ",
    "full_name": "EverettFish/holo-card-studio",
    "stargazers_count": 2106,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "8fb0edc794206c5d9b5b46717803a07c21c2411b0ee73a966df2a7e71eb74069",
    "last_success_at": "2026-11-16T14:20:00.152Z"
  }
}
```

</details>

