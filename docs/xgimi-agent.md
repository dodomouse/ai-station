# XGIMI Agent

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[Wechat-ggGitHub/xgimi-agent](https://github.com/Wechat-ggGitHub/xgimi-agent)

| 项目 / Field | 内容 / Value |
| --- | --- |
| 分类 / Category | 自动化 / Automation |
| 状态 / Status | 已收录 / Included |
| Star | 7 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:50:50.290410+00:00 |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:19:21.682Z |

## 中文

macOS 菜单栏与 Agent 技能，通过局域网控制用户自己的极米投影仪，提供遥控、截图与实验性蓝牙唤醒。

**环境与限制：** 需要 Apple Silicon、macOS 13+、Python 3.10 和 Xcode 命令行工具。蓝牙唤醒还需权限，并需从自有官方手机应用学习信号。作者仅确认 Z7X，其他型号未保证兼容。控制协议适用于可信局域网。

**入门：** 从[官方说明](https://raw.githubusercontent.com/Wechat-ggGitHub/xgimi-agent/main/README.md)确认安装与配置步骤，再查看[发布版本](https://github.com/Wechat-ggGitHub/xgimi-agent/releases)。本次为文档、许可原文与维护证据审查，未安装运行。

**近期维护：** [核验首次公开提交包含 Swift 菜单栏、Python 控制协议和测试的完整实现。](https://github.com/Wechat-ggGitHub/xgimi-agent/commit/903b0b4a63f50d29c1f94eaeba15a74579dfe083)（2026-10-18）

## English

A macOS menu-bar app and agent skill for LAN control of the user's XGIMI projector, with remote input, screenshots and experimental Bluetooth wake.

**Requirements and limitations:** Requires Apple Silicon, macOS 13+, Python 3.10 and Xcode command-line tools. Bluetooth wake also needs permission and signal learning from the user's official phone app. Only Z7X is author-confirmed; other models are unverified. Use on a trusted LAN.

**Getting started:** Follow the [official documentation](https://raw.githubusercontent.com/Wechat-ggGitHub/xgimi-agent/main/README.md) for setup, then check [releases](https://github.com/Wechat-ggGitHub/xgimi-agent/releases). This review examined documentation, license text and maintenance evidence; the software was not installed or run.

**Recent maintenance:** [The inspected initial public commit includes functional Swift menu-bar code, Python control protocols and tests.](https://github.com/Wechat-ggGitHub/xgimi-agent/commit/903b0b4a63f50d29c1f94eaeba15a74579dfe083) (2026-10-18)

## Review evidence

发现线索来自第三方公众号文章索引，原始微信正文未完整读取；用途、环境、许可与维护状态依据仓库当前资料复核。

Discovery uses a third-party WeChat article index; the original article body was not fully read. Current repository sources were reviewed for function, requirements, licensing and maintenance.

- 公众号索引原文 / Indexed WeChat source：[我用 Codex 破解了家里这个设备，还能语音遥控。。。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537902&idx=1&sn=bab85f388e137fed4534ec70fc77f18b)（2026-10-20）
- 作者署名转载 / Author-attributed repost：[我用 Codex 破解了家里这个设备，还能语音遥控。。。](https://www.woshipm.com/ai/6481266.html)（2026-10-20）；仓库链接映射已交叉核对 / repository mapping corroborated.

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
    "id": "xgimi-agent",
    "name": "XGIMI Agent",
    "repository": "Wechat-ggGitHub/xgimi-agent",
    "repo_node_id": "R_kgDOVOjvdw",
    "category": "automation",
    "summary": {
      "zh-CN": "macOS 菜单栏与 Agent 技能，通过局域网控制用户自己的极米投影仪，提供遥控、截图与实验性蓝牙唤醒。",
      "en": "A macOS menu-bar app and agent skill for LAN control of the user's XGIMI projector, with remote input, screenshots and experimental Bluetooth wake."
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
      "license_sha256": "24caa63d04c523975b506ff57ba4abe677f4968a67a1206fe2c6c79e4b048f36",
      "source_url": "https://github.com/Wechat-ggGitHub/xgimi-agent/blob/903b0b4a63f50d29c1f94eaeba15a74579dfe083/LICENSE",
      "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
      "files": [
        {
          "path": "LICENSE",
          "source_url": "https://github.com/Wechat-ggGitHub/xgimi-agent/blob/903b0b4a63f50d29c1f94eaeba15a74579dfe083/LICENSE",
          "fetched_at": "2026-11-16T14:26:56.616Z",
          "sha256": "24caa63d04c523975b506ff57ba4abe677f4968a67a1206fe2c6c79e4b048f36",
          "source_commit": "903b0b4a63f50d29c1f94eaeba15a74579dfe083"
        }
      ],
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "903b0b4a63f50d29c1f94eaeba15a74579dfe083"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-10-18T15:58:23Z",
        "url": "https://github.com/Wechat-ggGitHub/xgimi-agent/commit/903b0b4a63f50d29c1f94eaeba15a74579dfe083",
        "sha": "903b0b4a63f50d29c1f94eaeba15a74579dfe083",
        "summary": "Open source XGIMI menu bar remote and visual Agent skill",
        "files": [
          ".gitignore",
          "AGENTS.md",
          "LICENSE",
          "README.md",
          "SECURITY.md",
          "app/App.swift",
          "app/BeaconSignal.swift",
          "app/BeaconWake.swift",
          "app/MakeIcon.swift",
          "app/RemoteCore.swift",
          "app/WakeHelper.swift",
          "app/WakeIPC.swift",
          "build.py",
          "skills/xgimi-remote/SKILL.md",
          "skills/xgimi-remote/agents/openai.yaml",
          "skills/xgimi-remote/references/device-protocol.md",
          "skills/xgimi-remote/scripts/app_use.py",
          "skills/xgimi-remote/scripts/capture.py",
          "skills/xgimi-remote/scripts/control.py",
          "tests/test_app_use.py",
          "tests/test_skill_control.py"
        ],
        "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
        "qualifies": true,
        "reason": {
          "zh-CN": "核验首次公开提交包含 Swift 菜单栏、Python 控制协议和测试的完整实现。",
          "en": "The inspected initial public commit includes functional Swift menu-bar code, Python control protocols and tests."
        }
      }
    ],
    "sources": [
      {
        "article_id": "2247537902_1",
        "title": "我用 Codex 破解了家里这个设备，还能语音遥控。。。",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537902&idx=1&sn=bab85f388e137fed4534ec70fc77f18b",
        "published_date": "2026-10-20",
        "account": "逛逛GitHub",
        "source_strength": "third_party_index",
        "index_url": "https://www.noking.tech/github-radar/data/library.json",
        "original_article_body_read": false
      },
      {
        "url": "https://www.woshipm.com/ai/6481266.html",
        "title": "我用 Codex 破解了家里这个设备，还能语音遥控。。。",
        "published_date": "2026-10-20",
        "account": "逛逛GitHub",
        "source_strength": "author_attributed_repost_repository_mapping",
        "author_attribution_confirmed": true,
        "body_read_method": "public_html_repository_links_and_attribution_extraction",
        "full_text_archived": false
      }
    ],
    "quality_review": {
      "zh-CN": "解决特定投影仪本地控制需求，公开 Swift 应用、Python 协议实现和测试，并明确单型号验证边界；低 Star 不替代质量判断，本次未连接真实设备。",
      "en": "Addresses a concrete local-projector-control need with Swift application code, Python protocols and tests, while documenting single-model verification. Low stars do not determine quality; no physical device was tested."
    },
    "discovery": {
      "account": "逛逛GitHub",
      "window_start": "2026-08-16",
      "window_end": "2026-11-16",
      "original_article_body_read": false,
      "repository_review_sources": [
        "https://api.github.com/repos/wechat-gggithub/xgimi-agent",
        "https://raw.githubusercontent.com/Wechat-ggGitHub/xgimi-agent/main/README.md",
        "https://github.com/Wechat-ggGitHub/xgimi-agent/commit/903b0b4a63f50d29c1f94eaeba15a74579dfe083",
        "https://github.com/Wechat-ggGitHub/xgimi-agent/blob/903b0b4a63f50d29c1f94eaeba15a74579dfe083/LICENSE"
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVOjvdw",
    "full_name": "Wechat-ggGitHub/xgimi-agent",
    "stargazers_count": 7,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "24caa63d04c523975b506ff57ba4abe677f4968a67a1206fe2c6c79e4b048f36",
    "last_success_at": "2026-11-16T14:19:21.682Z"
  }
}
```

</details>
