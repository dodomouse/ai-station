# Voice Control Agent

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[Wechat-ggGitHub/voice-control-agent](https://github.com/Wechat-ggGitHub/voice-control-agent)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 自动化 / Automation |
| 状态 / Status | 已收录 / Included |
| Star | 5 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:58:29.135174Z |
| 快照时间 / Snapshot recorded at | 2026-11-16T14:58:29.135174Z |

## 中文

为 Mac 上的 Codex 桌面会话提供本机唤醒、语音输入和回复朗读入口。

### 主要功能

- 将识别结果发送到固定会话，并监听最终回复。
- 提供菜单栏控制、暂停和避免自我唤醒的朗读处理。

### 环境与限制

- 要求 Apple 芯片、macOS 14+、Python 3.12+、构建工具及兼容的 Codex 桌面 CLI。
- 识别依赖用户配置的火山服务，命令能力取决于会话授权，第三方模型和库各有许可。

### 开始使用

从[官方说明](https://github.com/Wechat-ggGitHub/voice-control-agent/blob/main/README.md)选择对应平台或集成方式，核对依赖与权限后按入门步骤操作。[发行记录](https://github.com/Wechat-ggGitHub/voice-control-agent/releases)可用于确认版本。

### 收录复核

为 Mac 上的 Codex 桌面会话提供本机唤醒、语音输入和回复朗读入口。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。 Star 较少，依据具体用途、实现和可复核文档收录；未据此推断成熟度或持续维护能力。

有效维护证据：[45f6ca93b7](https://github.com/Wechat-ggGitHub/voice-control-agent/commit/45f6ca93b715ad90101c504aa6e180fea62b0bc4)，2026-10-18T15:58:36Z。首次公开语音路由实现；已检查音频采集、应用状态和朗读助手接口。

文章来源：[逛逛GitHub署名文章](https://www.woshipm.com/ai/6481266.html)，平台日期 2026-10-20。已通过公开正文核对仓库链接与作者归属；微信正文未直接读取。

本次为文档与实现证据复核，未安装或运行上游项目。

## English

A Mac voice entry point for a Codex desktop conversation, with local wake-word detection and spoken replies.

### Features

- Routes recognized text to one fixed conversation and monitors final replies.
- Provides menu-bar controls, pause and speech handling that suppresses self-triggered wakeups.

### Requirements and limits

- Requires Apple silicon, macOS 14+, Python 3.12+, build tools and a compatible Codex desktop CLI.
- Recognition uses a configured Volcengine service
- actions depend on conversation authorization, and third-party models and libraries retain separate licenses.

### Getting started

Choose the platform or integration in the [official documentation](https://github.com/Wechat-ggGitHub/voice-control-agent/blob/main/README.md), review its dependencies and permissions, and follow its quickstart. Check [release records](https://github.com/Wechat-ggGitHub/voice-control-agent/releases) for versions.

### Review and provenance

A Mac voice entry point for a Codex desktop conversation, with local wake-word detection and spoken replies. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable. Included despite limited Stars because the use case, implementation and documentation are inspectable; popularity is not treated as evidence of maturity or sustained maintenance.

Activity: [45f6ca93b7](https://github.com/Wechat-ggGitHub/voice-control-agent/commit/45f6ca93b715ad90101c504aa6e180fea62b0bc4), 2026-10-18T15:58:36Z. Initial public voice-routing implementation; reviewed audio capture, application state and the speech-helper interface.

Discovery: [an author-attributed 逛逛GitHub article](https://www.woshipm.com/ai/6481266.html), dated 2026-10-20 on the public platform. Repository links and attribution were checked in its public body; the WeChat body was not read directly.

This review covers documentation and implementation evidence. The upstream project was not installed or run.

## Review evidence

```json
{
  "evaluated_at": "2026-11-16T14:58:29.135174Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "voice-control-agent",
    "name": "Voice Control Agent",
    "repository": "Wechat-ggGitHub/voice-control-agent",
    "repo_node_id": "R_kgDOVOjwMA",
    "category": "automation",
    "summary": {
      "zh-CN": "为 Mac 上的 Codex 桌面会话提供本机唤醒、语音输入和回复朗读入口。",
      "en": "A Mac voice entry point for a Codex desktop conversation, with local wake-word detection and spoken replies."
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
      "zh-CN": "为 Mac 上的 Codex 桌面会话提供本机唤醒、语音输入和回复朗读入口。 已检查官方说明、使用入口、许可证和近期功能证据；用途明确，提供可检查实现。 Star 较少，依据具体用途、实现和可复核文档收录；未据此推断成熟度或持续维护能力。",
      "en": "A Mac voice entry point for a Codex desktop conversation, with local wake-word detection and spoken replies. Official docs, a usage entry point, the license and recent functional evidence were reviewed; the purpose and implementation are inspectable. Included despite limited Stars because the use case, implementation and documentation are inspectable; popularity is not treated as evidence of maturity or sustained maintenance.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "24caa63d04c523975b506ff57ba4abe677f4968a67a1206fe2c6c79e4b048f36",
      "source_url": "https://github.com/Wechat-ggGitHub/voice-control-agent/blob/main/LICENSE",
      "reviewed_at": "2026-11-16T14:58:29.135174Z",
      "scope_note": "MIT covers original code only. Speech libraries, model files and packaged third-party components keep their individual licenses."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-10-18T15:58:36Z",
        "reviewed_at": "2026-11-16T14:58:29.135174Z",
        "url": "https://github.com/Wechat-ggGitHub/voice-control-agent/commit/45f6ca93b715ad90101c504aa6e180fea62b0bc4",
        "qualifies": true,
        "reason": {
          "zh-CN": "首次公开语音路由实现；已检查音频采集、应用状态和朗读助手接口。",
          "en": "Initial public voice-routing implementation; reviewed audio capture, application state and the speech-helper interface."
        },
        "reviewed_files": [
          "src/AppState.swift",
          "src/Audio.swift",
          "src/EdgeSpeech.swift"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/Wechat-ggGitHub/voice-control-agent",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/Wechat-ggGitHub/voice-control-agent/blob/main/README.md",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/Wechat-ggGitHub/voice-control-agent/blob/main/LICENSE",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://github.com/Wechat-ggGitHub/voice-control-agent/commit/45f6ca93b715ad90101c504aa6e180fea62b0bc4",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      },
      {
        "url": "https://www.woshipm.com/ai/6481266.html",
        "accessed_at": "2026-11-16T14:58:29.135174Z"
      }
    ],
    "article_source": {
      "article_id": "2247537902_1",
      "title": "我用 Codex 破解了家里这个设备，还能语音遥控。。。",
      "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537902&idx=1&sn=bab85f388e137fed4534ec70fc77f18b",
      "published_date": "2026-10-20",
      "account": "逛逛GitHub",
      "content_review_url": "https://www.woshipm.com/ai/6481266.html",
      "content_review_kind": "author-attributed public article",
      "wechat_direct_body_read": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVOjwMA",
    "full_name": "Wechat-ggGitHub/voice-control-agent",
    "stargazers_count": 5,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "24caa63d04c523975b506ff57ba4abe677f4968a67a1206fe2c6c79e4b048f36",
    "last_success_at": "2026-11-16T14:58:29.135174Z"
  }
}
```
