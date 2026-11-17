# Mac Duo

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[sumimakito/Mac-Duo](https://github.com/sumimakito/Mac-Duo)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 1236 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:19:59.961Z |

## 中文

根据 MacBook 屏幕开合角度，为实时桌面画面添加倾斜、模糊和渐暗效果。

### 主要功能

- 使用 ScreenCaptureKit 捕获画面并以 Metal 渲染。
- 在菜单栏调节透视和效果参数。

### 环境与限制

- 要求 macOS 14+、兼容的内置开合角传感器及屏幕录制权限。
- 合盖导致系统睡眠后效果停止，源码构建需要 Swift 6 与 Xcode。

### 开始使用

从[官方说明](https://github.com/sumimakito/Mac-Duo/blob/main/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/sumimakito/Mac-Duo/releases)可用于确认版本。

### 收录复核

根据 MacBook 屏幕开合角度，为实时桌面画面添加倾斜、模糊和渐暗效果。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。

有效维护证据：[4568442f4c](https://github.com/sumimakito/Mac-Duo/commit/4568442f4c76facae894b9fd63aa428eddeae3fc)，2026-09-14T14:53:12Z。增加开盖最小位移条件，避免传感器抖动反复开关效果。

文章来源：[逛逛GitHub署名文章](https://www.woshipm.com/ai/6466407.html)，平台日期 2026-09-18。已通过公开正文核对仓库链接与作者归属；微信正文未直接读取。

本次为文档与实现证据复核，未安装或运行上游项目。

## English

Applies tilt, blur and dimming to live desktop content as a MacBook lid moves.

### Features

- Captures content with ScreenCaptureKit and renders with Metal.
- Offers perspective and effect controls in the menu bar.

### Requirements and limits

- Requires macOS 14+, a compatible built-in lid-angle sensor and Screen Recording permission.
- The effect stops when the machine sleeps
- source builds require Swift 6 and Xcode.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/sumimakito/Mac-Duo/blob/main/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/sumimakito/Mac-Duo/releases) for versions.

### Review and provenance

Applies tilt, blur and dimming to live desktop content as a MacBook lid moves. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.

Activity: [4568442f4c](https://github.com/sumimakito/Mac-Duo/commit/4568442f4c76facae894b9fd63aa428eddeae3fc), 2026-09-14T14:53:12Z. Adds a minimum opening movement to prevent sensor jitter from toggling the effect.

Discovery: [an author-attributed 逛逛GitHub article](https://www.woshipm.com/ai/6466407.html), dated 2026-09-18 on the public platform. Repository links and attribution were checked in its public body; the WeChat body was not read directly.

This review covers documentation and implementation evidence. The upstream project was not installed or run.

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
    "id": "mac-duo",
    "name": "Mac Duo",
    "repository": "sumimakito/Mac-Duo",
    "repo_node_id": "R_kgDOUViyVQ",
    "category": "media",
    "summary": {
      "zh-CN": "根据 MacBook 屏幕开合角度，为实时桌面画面添加倾斜、模糊和渐暗效果。",
      "en": "Applies tilt, blur and dimming to live desktop content as a MacBook lid moves."
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
      "zh-CN": "根据 MacBook 屏幕开合角度，为实时桌面画面添加倾斜、模糊和渐暗效果。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。",
      "en": "Applies tilt, blur and dimming to live desktop content as a MacBook lid moves. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
      "source_url": "https://github.com/sumimakito/Mac-Duo/blob/2a9fa18bea0e92293bf59227b539fe3de0e91328/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "Root license reviewed. External dependencies and assets retain their individual licenses.",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "2a9fa18bea0e92293bf59227b539fe3de0e91328"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-09-14T14:53:12Z",
        "reviewed_at": "2026-11-16T14:58:29.135174Z",
        "url": "https://github.com/sumimakito/Mac-Duo/commit/4568442f4c76facae894b9fd63aa428eddeae3fc",
        "qualifies": true,
        "reason": {
          "zh-CN": "增加开盖最小位移条件，避免传感器抖动反复开关效果。",
          "en": "Adds a minimum opening movement to prevent sensor jitter from toggling the effect."
        },
        "reviewed_files": [
          "Sources/MacDuo/LidController.swift",
          "Sources/MacDuo/LidEffectPolicy.swift",
          "Tests/MacDuoTests/LidEffectPolicyTests.swift"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/sumimakito/Mac-Duo",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/sumimakito/Mac-Duo/blob/main/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/sumimakito/Mac-Duo/blob/2a9fa18bea0e92293bf59227b539fe3de0e91328/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/sumimakito/Mac-Duo/commit/4568442f4c76facae894b9fd63aa428eddeae3fc",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://www.woshipm.com/ai/6466407.html",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      }
    ],
    "article_source": {
      "article_id": "2247537034_1",
      "title": "推荐 4 个夯夯夯夯的 GitHub 开源项目，特别是第 2 个。",
      "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537034&idx=1&sn=a81b159785dac2887c1145f48825dd72",
      "published_date": "2026-09-18",
      "account": "逛逛GitHub",
      "content_review_url": "https://www.woshipm.com/ai/6466407.html",
      "content_review_kind": "author-attributed public article",
      "wechat_direct_body_read": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOUViyVQ",
    "full_name": "sumimakito/Mac-Duo",
    "stargazers_count": 1236,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
    "last_success_at": "2026-11-16T14:19:59.961Z"
  }
}
```

</details>
