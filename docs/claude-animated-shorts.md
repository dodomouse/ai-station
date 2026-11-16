# Claude Animated Shorts

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[mromidev/claude-animated-shorts](https://github.com/mromidev/claude-animated-shorts)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 3658 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:21:24.299979Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:21:24.299979Z |

## 中文

面向 Claude Code 的竖屏动画短片技能。用 Three.js 与 Remotion 渲染角色、场景和声音，附带桥梁故事示例。

### 主要功能

- 提供 55 至 70 秒竖屏故事的制作流程。
- 用二维角色、三维场景、镜头和声音组成动画。
- 附带场景模板、声音脚本、抽帧和逐帧检查工具。

### 环境与限制

- 需要 Claude Code、Node.js、Python 3、FFmpeg、Remotion 和 @remotion/three。
- Remotion 打包会复制素材，官方示例提示预留临时空间。
- 代码与文档采用 MIT；参考帧只供风格学习，不能据此认定可商用或再分发。
- 收录范围为 MIT 代码与文档，不包含参考帧的商用或再分发授权。

Remotion 采用独立许可，商业使用须另行核对其条款；本技能的 MIT 许可不覆盖渲染器的所有使用方式。

### 开始使用

先阅读官方 README 与许可说明。确认参考素材使用范围后，再按官方步骤安装技能和渲染依赖。

[官方说明](https://github.com/mromidev/claude-animated-shorts/blob/main/README.md) · [正式发行](https://github.com/mromidev/claude-animated-shorts/releases)

### 收录复核

2026-11-16 文档复核：已读取官方说明、许可证和提交差异。本次未安装运行，也未测试上游功能。

已确认 MIT 覆盖代码和文档，按此范围收录。参考帧的使用限制独立保留。

有效维护证据：[744b75fbba](https://github.com/mromidev/claude-animated-shorts/commit/744b75fbbaee6e57838bcfa899634462434302c0)，时间为 2026-11-01T05:50:37Z。2026-11-01 的初始功能提交包含动画模板和质量检查脚本。已检查 templates/scripts/short_qa.py 的视频解码与逐帧分析实现。

文章线索来自逛逛GitHub于2026-11-14发布的[五项目介绍](https://www.woshipm.com/ai/6493951.html)。本次读取作者在人人都是产品经理的署名文章。[微信链接](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538466&idx=1&sn=8ce06fbf66930fa6d90e80f5be10fa3f)用于追溯，微信正文未直接读取。功能和环境以上游说明为准。

## English

A Claude Code skill for vertical animated shorts, with Three.js and Remotion scenes, sound helpers and a bridge-story example.

### Features

- Provides a workflow for vertical stories lasting 55–70 seconds.
- Combines 2D characters, 3D scenes, camera work and sound.
- Includes scene templates, sound scripts, frame capture and frame-by-frame checks.

### Requirements and limits

- Requires Claude Code, Node.js, Python 3, FFmpeg, Remotion and @remotion/three.
- Remotion bundles copy assets, so temporary disk space is needed.
- Code and docs are MIT; reference frames are for style study only, which does not establish commercial-use or redistribution rights.
- Inclusion covers MIT code and documentation, not commercial-use or redistribution rights for reference frames.

Remotion has independent licensing and commercial-use terms; this skill’s MIT license does not authorize every use of the renderer.

### Getting started

Read the README and license scope first. Confirm reference-asset rights before following the skill and renderer setup.

[Official documentation](https://github.com/mromidev/claude-animated-shorts/blob/main/README.md) · [Releases](https://github.com/mromidev/claude-animated-shorts/releases)

### Review and provenance

Documentation review on 2026-11-16: official docs, the license and implementation changes were read. The project was not installed or tested.

MIT coverage of the code and documentation is verified. Inclusion is limited to that scope; restrictions on reference frames remain separate.

Activity: [744b75fbba](https://github.com/mromidev/claude-animated-shorts/commit/744b75fbbaee6e57838bcfa899634462434302c0) at 2026-11-01T05:50:37Z. The initial feature commit on 2026-11-01 adds animation templates and QA scripts. Reviewed video decoding and per-frame analysis in templates/scripts/short_qa.py.

Discovery source: [the author-attributed five-project article](https://www.woshipm.com/ai/6493951.html), published by 逛逛GitHub on 2026-11-14. The WeChat URL is retained for provenance; its body was not read directly. Feature and requirement statements come from upstream documentation.

## Review evidence

```json
{
  "evaluated_at": "2026-11-16T14:21:24.299979Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "claude-animated-shorts",
    "name": "Claude Animated Shorts",
    "repository": "mromidev/claude-animated-shorts",
    "repo_node_id": "R_kgDOVevxrA",
    "category": "media",
    "summary": {
      "zh-CN": "面向 Claude Code 的竖屏动画短片技能。用 Three.js 与 Remotion 渲染角色、场景和声音，附带桥梁故事示例。",
      "en": "A Claude Code skill for vertical animated shorts, with Three.js and Remotion scenes, sound helpers and a bridge-story example."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:21:24.299979Z",
        "en": "2026-11-16T14:21:24.299979Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "0c88b6c1afe23ba94a2326eb289868fa4bb24edfd6994ad0c6bb7f2f2ed517e2",
      "source_url": "https://github.com/mromidev/claude-animated-shorts/blob/main/LICENSE",
      "reviewed_at": "2026-11-16T14:21:24.299979Z",
      "scope_note": "MIT covers code and documentation. Reference frames are limited to style study and excluded from the approved software-license scope."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-01T05:50:37Z",
        "reviewed_at": "2026-11-16T14:21:24.299979Z",
        "url": "https://github.com/mromidev/claude-animated-shorts/commit/744b75fbbaee6e57838bcfa899634462434302c0",
        "qualifies": true,
        "reason": {
          "zh-CN": "2026-11-01 的初始功能提交包含动画模板和质量检查脚本。已检查 templates/scripts/short_qa.py 的视频解码与逐帧分析实现。",
          "en": "The initial feature commit on 2026-11-01 adds animation templates and QA scripts. Reviewed video decoding and per-frame analysis in templates/scripts/short_qa.py."
        },
        "reviewed_files": [
          "templates/scripts/short_qa.py"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/mromidev/claude-animated-shorts",
        "accessed_at": "2026-11-16T14:21:24.299979Z"
      },
      {
        "url": "https://github.com/mromidev/claude-animated-shorts/blob/main/README.md",
        "accessed_at": "2026-11-16T14:21:24.299979Z"
      },
      {
        "url": "https://github.com/mromidev/claude-animated-shorts/blob/main/LICENSE",
        "accessed_at": "2026-11-16T14:21:24.299979Z"
      },
      {
        "url": "https://www.woshipm.com/ai/6493951.html",
        "accessed_at": "2026-11-16T14:21:24.299979Z",
        "supports": "2026-11-14 作者署名原创文章，明确列出仓库 URL。"
      },
      {
        "url": "https://www.remotion.dev/docs/license",
        "accessed_at": "2026-11-16T14:54:34.388Z",
        "supports": {
          "zh-CN": "交叉复核用途、实现或许可范围。",
          "en": "Cross-review of purpose, implementation or license scope."
        }
      }
    ],
    "article_source": {
      "article_id": "2247538466_1",
      "title": "搜罗了 5 个刚开源的 GitHub 项目，可以看看自己能不能用到。",
      "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538466&idx=1&sn=8ce06fbf66930fa6d90e80f5be10fa3f",
      "published_date": "2026-11-14",
      "account": "逛逛GitHub",
      "content_review_url": "https://www.woshipm.com/ai/6493951.html",
      "content_review_kind": "author-attributed original publication on Woshipm",
      "wechat_direct_body_read": false
    },
    "quality_review": {
      "zh-CN": "面向 Claude Code 的竖屏动画短片技能。用 Three.js 与 Remotion 渲染角色、场景和声音，附带桥梁故事示例。 官方说明、使用入口和实现差异可复核。",
      "en": "A Claude Code skill for vertical animated shorts, with Three.js and Remotion scenes, sound helpers and a bridge-story example. Official documentation, usage entry points and implementation changes are inspectable.",
      "verification_level": "docs"
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVevxrA",
    "full_name": "mromidev/claude-animated-shorts",
    "stargazers_count": 3658,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "0c88b6c1afe23ba94a2326eb289868fa4bb24edfd6994ad0c6bb7f2f2ed517e2",
    "last_success_at": "2026-11-16T14:21:24.299979Z"
  }
}
```
