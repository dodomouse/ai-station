# S2Arm

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[jhaizhou-ops/S2Arm](https://github.com/jhaizhou-ops/S2Arm)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 3346 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:30:19.931551Z |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:27:09.966Z |

## 中文

### 用途与功能

将用户自备的部分 Switch 游戏代码转换为苹果设备的 ARM64 程序，并提供图形化打包与游戏库管理。

提供 Mac 与 Windows 启动器，以及脚本控制和诊断入口。适合兼容性和图形转换技术研究。

### 环境与限制

需自备合法取得的游戏与密钥。目标为 iOS/iPadOS 18+ 或 Apple Silicon/macOS 15+；签名和安装另有平台要求。仅支持特定 64 位游戏，不保证兼容全部作品。v0.4.4 已撤回，本轮维护依据采用正式 v0.4.3。

### 入门与收录判断

从[官方 README](https://github.com/jhaizhou-ops/S2Arm/blob/main/README.md)查阅安装和使用步骤。有明确平台边界、可检查的转换实现和持续缺陷修复，作为兼容性工具收录。

本轮为文档复核，未安装、运行或测试上游项目。正式 v0.4.3 修复游戏崩溃、颜色格式和音频中断。详见[维护记录](https://github.com/jhaizhou-ops/S2Arm/releases/tag/v0.4.3)。

### 文章来源

发现于“逛逛GitHub”在 2026-11-16 发布的[《8 个开源工具速览》](https://www.woshipm.com/ai/6494405.html)。已读取作者署名正文，功能和限制另按当前上游复核。

## English

### Purpose and features

Translates supported, user-supplied Switch games into ARM64 programs for Apple devices, with graphical packaging and library management.

Offers Mac and Windows launchers plus scripting and diagnostics interfaces for compatibility and graphics-translation work.

### Requirements and limits

Requires legitimately obtained games and keys. Targets iOS/iPadOS 18+ or Apple Silicon/macOS 15+, with separate signing requirements. Support is limited to compatible 64-bit games. Version 0.4.4 was withdrawn; this review uses stable v0.4.3 as activity evidence.

### Getting started and review

Use the [official README](https://github.com/jhaizhou-ops/S2Arm/blob/main/README.md) for installation and usage. This is a documentation review; the software was not installed or tested. Stable v0.4.3 fixes game crashes, a color format and audio loss. See the [activity evidence](https://github.com/jhaizhou-ops/S2Arm/releases/tag/v0.4.3).

The project appears in the account's [author-published article dated 2026-11-16](https://www.woshipm.com/ai/6494405.html). Current upstream documentation supports the feature descriptions.

## Review evidence

```json
{
  "evaluated_at": "2026-11-16T14:30:19.931551Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "s2arm",
    "name": "S2Arm",
    "repository": "jhaizhou-ops/S2Arm",
    "repo_node_id": "R_kgDOVm1wdg",
    "category": "development",
    "summary": {
      "zh-CN": "将用户自备的部分 Switch 游戏代码转换为苹果设备的 ARM64 程序，并提供图形化打包与游戏库管理。",
      "en": "Translates supported, user-supplied Switch games into ARM64 programs for Apple devices, with graphical packaging and library management."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:30:19.931551Z",
        "en": "2026-11-16T14:30:19.931551Z"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "basis": "有明确平台边界、可检查的转换实现和持续缺陷修复，作为兼容性工具收录。",
      "rationale": "有明确平台边界、可检查的转换实现和持续缺陷修复，作为兼容性工具收录。",
      "stars_are_advisory": true,
      "reviewed_at": "2026-11-16T14:30:19.931551Z"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
      "source_url": "https://github.com/jhaizhou-ops/S2Arm/blob/main/LICENSE",
      "reviewed_at": "2026-11-16T14:30:19.931551Z"
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-11-16T00:18:07Z",
        "reviewed_at": "2026-11-16T14:30:19.931551Z",
        "url": "https://github.com/jhaizhou-ops/S2Arm/releases/tag/v0.4.3",
        "qualifies": true,
        "reason": {
          "zh-CN": "正式 v0.4.3 修复游戏崩溃、颜色格式和音频中断。",
          "en": "Stable v0.4.3 fixes game crashes, a color format and audio loss."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/jhaizhou-ops/S2Arm",
        "accessed_at": "2026-11-16T14:27:09.966Z",
        "supports": "Repository identity, Stars and public state."
      },
      {
        "url": "https://github.com/jhaizhou-ops/S2Arm/blob/main/README.md",
        "accessed_at": "2026-11-16T14:30:19.931551Z",
        "supports": "Capabilities, requirements and limits."
      },
      {
        "url": "https://www.woshipm.com/ai/6494405.html",
        "published_date": "2026-11-16",
        "accessed_at": "2026-11-16T14:30:19.931551Z",
        "supports": "Author-published article body and account attribution."
      }
    ],
    "discovery": {
      "account": "逛逛GitHub",
      "article_url": "https://www.woshipm.com/ai/6494405.html",
      "published_date": "2026-11-16",
      "body_verification": "author_published_article"
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVm1wdg",
    "full_name": "jhaizhou-ops/S2Arm",
    "stargazers_count": 3346,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
    "last_success_at": "2026-11-16T14:27:09.966Z"
  }
}
```
