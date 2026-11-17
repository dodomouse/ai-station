# Mobile MCP

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[mobile-next/mobile-mcp](https://github.com/mobile-next/mobile-mcp)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 自动化 / Automation |
| 状态 / Status | 已收录 / Included |
| Star | 10616 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:20:00.045Z |

## 中文

通过 MCP 让智能体操作 Android 与 iOS 应用、模拟器及真实设备。

### 主要功能

- 读取无障碍结构或截图，可执行的操作包括点击和输入。
- 向不同 MCP 客户端提供统一设备接口。

### 环境与限制

- 需要 Node.js 20+、MCP 客户端及相应平台设备工具。
- 真实设备需先按指南完成连接，云设备属于独立服务。

### 开始使用

从[官方说明](https://github.com/mobile-next/mobile-mcp/blob/main/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/mobile-next/mobile-mcp/releases)可用于确认版本。

### 收录复核

通过 MCP 让智能体操作 Android 与 iOS 应用、模拟器及真实设备。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。

有效维护证据：[1.0.17](https://github.com/mobile-next/mobile-mcp/releases/tag/1.0.17)，2026-11-11T14:44:51Z。按截图方向调整屏幕尺寸映射，修复横屏应用仍使用竖屏尺寸生成点击提示的问题。 2026-11-17 已读取[实现提交](https://github.com/mobile-next/mobile-mcp/commit/3b51952bcd83955f3a743f731f5a9beaebecdab7)的差异；未运行上游测试。

文章来源：[逛逛GitHub署名文章](https://www.woshipm.com/share/6470286.html)，平台日期 2026-09-26。已通过公开正文核对仓库链接与作者归属；微信正文未直接读取。

本次为文档与实现证据复核，未安装或运行上游项目。

## English

An MCP server for agent interaction with Android and iOS apps, simulators and real devices.

### Features

- Reads accessibility snapshots or screenshots and performs taps and text input.
- Offers a shared device interface to different MCP clients.

### Requirements and limits

- Requires Node.js 20+, an MCP client and platform-specific device tools.
- Real devices need the documented connection setup
- cloud devices are a separate service.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/mobile-next/mobile-mcp/blob/main/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/mobile-next/mobile-mcp/releases) for versions.

### Review and provenance

An MCP server for agent interaction with Android and iOS apps, simulators and real devices. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.

Activity: [1.0.17](https://github.com/mobile-next/mobile-mcp/releases/tag/1.0.17), 2026-11-11T14:44:51Z. Aligns reported screen dimensions with screenshot orientation so landscape apps receive correct tap-coordinate guidance. On 2026-11-17, the [implementation diff](https://github.com/mobile-next/mobile-mcp/commit/3b51952bcd83955f3a743f731f5a9beaebecdab7) was inspected; upstream tests were not run.

Discovery: [an author-attributed 逛逛GitHub article](https://www.woshipm.com/share/6470286.html), dated 2026-09-26 on the public platform. Repository links and attribution were checked in its public body; the WeChat body was not read directly.

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
    "id": "mobile-mcp",
    "name": "Mobile MCP",
    "repository": "mobile-next/mobile-mcp",
    "repo_node_id": "R_kgDOOQVw5Q",
    "category": "automation",
    "summary": {
      "zh-CN": "通过 MCP 让智能体操作 Android 与 iOS 应用、模拟器及真实设备。",
      "en": "An MCP server for agent interaction with Android and iOS apps, simulators and real devices."
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
      "zh-CN": "通过 MCP 让智能体操作 Android 与 iOS 应用、模拟器及真实设备。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。",
      "en": "An MCP server for agent interaction with Android and iOS apps, simulators and real devices. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4",
      "source_url": "https://github.com/mobile-next/mobile-mcp/blob/ad3b42336d89717313af45176c48538bea6ec363/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "Root license reviewed. External dependencies and assets retain their individual licenses.",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "ad3b42336d89717313af45176c48538bea6ec363"
    },
    "activity_evidence": [
      {
        "type": "release",
        "occurred_at": "2026-11-11T14:44:51Z",
        "reviewed_at": "2026-11-17T03:15:51.892548+00:00",
        "url": "https://github.com/mobile-next/mobile-mcp/releases/tag/1.0.17",
        "qualifies": true,
        "reason": {
          "zh-CN": "按截图方向调整屏幕尺寸映射，修复横屏应用仍使用竖屏尺寸生成点击提示的问题。",
          "en": "Aligns reported screen dimensions with screenshot orientation so landscape apps receive correct tap-coordinate guidance."
        },
        "draft": false,
        "prerelease": false,
        "implementation_evidence": {
          "type": "commit",
          "url": "https://github.com/mobile-next/mobile-mcp/commit/3b51952bcd83955f3a743f731f5a9beaebecdab7",
          "sha": "3b51952bcd83955f3a743f731f5a9beaebecdab7",
          "occurred_at": "2026-11-07T08:39:19Z",
          "reviewed_at": "2026-11-17T03:15:51.892548+00:00",
          "reviewed_files": [
            "src/coordinate-mapping.ts",
            "test/coordinate-mapping.ts"
          ],
          "verification_level": "source_review",
          "upstream_tests_run": false
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/mobile-next/mobile-mcp",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/mobile-next/mobile-mcp/blob/main/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/mobile-next/mobile-mcp/blob/ad3b42336d89717313af45176c48538bea6ec363/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/mobile-next/mobile-mcp/releases/tag/1.0.17",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://www.woshipm.com/share/6470286.html",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      }
    ],
    "article_source": {
      "article_id": "2247537318_1",
      "title": "让 AI 帮你操作手机，这个 GitHub 开源项目支持安卓和 iPhone。",
      "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537318&idx=1&sn=c968c54a4558a9a05087a3892296f698",
      "published_date": "2026-09-25",
      "account": "逛逛GitHub",
      "content_review_url": "https://www.woshipm.com/share/6470286.html",
      "content_review_kind": "author-attributed public article",
      "wechat_direct_body_read": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOOQVw5Q",
    "full_name": "mobile-next/mobile-mcp",
    "stargazers_count": 10616,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "c71d239df91726fc519c6eb72d318ec65820627232b2f796219e87dcf35d0ab4",
    "last_success_at": "2026-11-16T14:20:00.045Z"
  }
}
```

</details>
