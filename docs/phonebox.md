# PhoneBox

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[ersinkoc/phonebox](https://github.com/ersinkoc/phonebox)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 自动化 / Automation |
| 状态 / Status | 已收录 / Included |
| Star | 2004 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T06:06:21.868390+00:00 |

## 中文

把 Android 手机用作电脑的桌面面板和触控控制台，提供系统指标、AI 编程会话、配额及可选权限响应模块。

### 用途与功能

- 在手机查看 Claude Code、Codex 本地会话状态，以及可用的模型、计时和 Token 详情。
- 显示 Claude、Codex 等服务的配额与重置时间；可选择安装钩子，在手机允许或拒绝 Claude Code 权限请求。
- 通过浏览器编辑多页面布局，组合系统指标、快捷操作、媒体控制及自动化组件。

### 环境与限制

需要 Android 7+ 手机与受支持的 Windows、Linux 或 macOS 电脑。USB 方式需要数据线、adb 和 USB 调试授权；Wi-Fi 方式需安装 APK 并完成证书与配对码核对。发行版内置 .NET，源码构建使用 .NET 10；Android 构建另需 JDK 17 和 Android SDK Platform 35。

AI 模块需要本机已有相应工具的登录状态或会话记录。Claude 配额依赖未公开的服务接口，接口变化或限流可能影响显示；配额、GitHub、天气等可选模块仍会访问外部服务。触控功能依平台和权限而异，随前台应用切换的 App console 当前仅支持 Windows。

### 开始使用

从官方发行版选择电脑端程序和 Android APK，完成 USB 或 Wi-Fi 配对。打开电脑的本地设置页，选择 Sessions 或 AI quotas 模板；需要手机审批时，再显式启用 Claude Code permission prompts 并安装钩子。

参阅[官方 README](https://github.com/ersinkoc/phonebox/blob/5d5cafd850f7ac367202538975efa576b93d19c9/README.md)。

### 收录与来源

适合用闲置手机持续查看 AI 编程任务是否运行或等待输入，并在启用后处理权限请求，减少在多个终端之间切换。它同时是通用设备面板，不运行模型或代替编码智能体。

维护证据：[新增 Windows App console，根据前台应用选择按键与旋钮配置，并在发送每组按键前复查组件授权和前台窗口](https://github.com/ersinkoc/phonebox/commit/5d5cafd850f7ac367202538975efa576b93d19c9)（2026-11-16）。

用户于 2026-11-17 提供仓库链接。本条按工程通用标准复核，不设 Star 门槛。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Turns an Android phone into a desktop panel and touch console for a computer, with system metrics, AI coding sessions, quotas and optional permission responses.

### Uses and features

- View local Claude Code and Codex session status on the phone, including available model, timing and token details.
- Display quota and reset information for services such as Claude and Codex; optionally install a hook to allow or deny Claude Code permission requests from the phone.
- Edit multipage layouts in a browser, combining system metrics, shortcuts, media controls and automation widgets.

### Requirements and limits

Requires an Android 7+ phone and a supported Windows, Linux or macOS computer. USB requires a data cable, adb and authorized USB debugging; Wi-Fi requires the APK and certificate/check-code pairing. Releases bundle .NET; source builds use .NET 10, with JDK 17 and Android SDK Platform 35 additionally required for Android builds.

AI modules require the relevant tools’ local sign-in state or session records. Claude quota reading depends on an undocumented service endpoint and may be affected by changes or rate limits; optional quota, GitHub and weather modules still contact external services. Touch controls depend on platform and permissions, and the foreground-app-aware App console currently supports Windows only.

### Getting started

Choose the desktop agent and Android APK from an official release, then pair over USB or Wi-Fi. Open the computer’s local settings page and select a Sessions or AI quotas template; explicitly enable Claude Code permission prompts and install the hook if phone-based approval is needed.

See the [official README](https://github.com/ersinkoc/phonebox/blob/5d5cafd850f7ac367202538975efa576b93d19c9/README.md).

### Review and provenance

Useful for keeping AI coding task progress and waiting states visible on a spare phone, and handling permission requests when enabled, with less switching between terminals. It is also a general device panel and neither runs a model nor replaces a coding agent.

Maintenance evidence: [Adds the Windows App console, selecting key and dial profiles by foreground app and rechecking widget permission and the foreground window before each key combination](https://github.com/ersinkoc/phonebox/commit/5d5cafd850f7ac367202538975efa576b93d19c9) (2026-11-16).

Submitted by the user on 2026-11-17 and reviewed against the general catalog criteria, with no star threshold.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T06:06:21.868390+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "phonebox",
    "name": "PhoneBox",
    "repository": "ersinkoc/phonebox",
    "repo_node_id": "R_kgDOVmZZOQ",
    "category": "automation",
    "summary": {
      "zh-CN": "把 Android 手机用作电脑的桌面面板和触控控制台，提供系统指标、AI 编程会话、配额及可选权限响应模块。",
      "en": "Turns an Android phone into a desktop panel and touch console for a computer, with system metrics, AI coding sessions, quotas and optional permission responses."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T06:06:21.868390+00:00",
        "en": "2026-11-17T06:06:21.868390+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "适合用闲置手机持续查看 AI 编程任务是否运行或等待输入，并在启用后处理权限请求，减少在多个终端之间切换。它同时是通用设备面板，不运行模型或代替编码智能体。",
      "en": "Useful for keeping AI coding task progress and waiting states visible on a spare phone, and handling permission requests when enabled, with less switching between terminals. It is also a general device panel and neither runs a model nor replaces a coding agent.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/ersinkoc/phonebox/blob/5d5cafd850f7ac367202538975efa576b93d19c9/LICENSE",
      "license_sha256": "e3cfb97b744f8391177244cd991b126875adac85d13b76d526a5fd603fcb548b",
      "source_commit": "5d5cafd850f7ac367202538975efa576b93d19c9",
      "reviewed_at": "2026-11-17T06:06:21.868390+00:00",
      "evidence_pinned_at": "2026-11-17T06:06:21.868390+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "MIT covers PhoneBox repository software and documentation, subject to bundled third-party notices. Connected AI services, desktop applications, hardware and external data sources retain their own terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-16T23:47:25Z",
        "reviewed_at": "2026-11-17T06:06:21.868390+00:00",
        "url": "https://github.com/ersinkoc/phonebox/commit/5d5cafd850f7ac367202538975efa576b93d19c9",
        "qualifies": true,
        "reason": {
          "zh-CN": "新增 Windows App console，根据前台应用选择按键与旋钮配置，并在发送每组按键前复查组件授权和前台窗口",
          "en": "Adds the Windows App console, selecting key and dial profiles by foreground app and rechecking widget permission and the foreground window before each key combination"
        },
        "reviewed_files": [
          "agent/PhoneBox.Agent/AppConsole.cs",
          "agent/PhoneBox.Agent/KeySender.cs",
          "android/app/src/main/assets/www/widgets/console.js"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/ersinkoc/phonebox",
        "accessed_at": "2026-11-17T06:06:21.868390+00:00"
      },
      {
        "url": "https://github.com/ersinkoc/phonebox/blob/5d5cafd850f7ac367202538975efa576b93d19c9/README.md",
        "accessed_at": "2026-11-17T06:06:21.868390+00:00"
      },
      {
        "url": "https://github.com/ersinkoc/phonebox/blob/5d5cafd850f7ac367202538975efa576b93d19c9/LICENSE",
        "accessed_at": "2026-11-17T06:06:21.868390+00:00"
      },
      {
        "url": "https://github.com/ersinkoc/phonebox/commit/5d5cafd850f7ac367202538975efa576b93d19c9",
        "accessed_at": "2026-11-17T06:06:21.868390+00:00"
      },
      {
        "url": "https://github.com/ersinkoc/phonebox/blob/5d5cafd850f7ac367202538975efa576b93d19c9/docs/GUIDE.md",
        "accessed_at": "2026-11-17T06:06:21.868390+00:00"
      },
      {
        "url": "https://github.com/ersinkoc/phonebox/blob/5d5cafd850f7ac367202538975efa576b93d19c9/docs/SETUP.md",
        "accessed_at": "2026-11-17T06:06:21.868390+00:00"
      },
      {
        "url": "https://github.com/ersinkoc/phonebox/blob/5d5cafd850f7ac367202538975efa576b93d19c9/docs/DEVELOPMENT.md",
        "accessed_at": "2026-11-17T06:06:21.868390+00:00"
      },
      {
        "url": "https://github.com/ersinkoc/phonebox/blob/5d5cafd850f7ac367202538975efa576b93d19c9/agent/PhoneBox.Agent/SessionMonitor.cs",
        "accessed_at": "2026-11-17T06:06:21.868390+00:00"
      },
      {
        "url": "https://github.com/ersinkoc/phonebox/blob/5d5cafd850f7ac367202538975efa576b93d19c9/agent/PhoneBox.Agent/ClaudeHook.cs",
        "accessed_at": "2026-11-17T06:06:21.868390+00:00"
      },
      {
        "url": "https://github.com/ersinkoc/phonebox/blob/5d5cafd850f7ac367202538975efa576b93d19c9/agent/PhoneBox.Agent/THIRD-PARTY-NOTICES.txt",
        "accessed_at": "2026-11-17T06:06:21.868390+00:00"
      }
    ],
    "discovery": {
      "kind": "user_submission",
      "submitted_date": "2026-11-17",
      "source_url": "https://github.com/ersinkoc/phonebox",
      "repository_url": "https://github.com/ersinkoc/phonebox"
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVmZZOQ",
    "full_name": "ersinkoc/phonebox",
    "stargazers_count": 2004,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "api_license_spdx": "MIT",
    "license_sha256": "e3cfb97b744f8391177244cd991b126875adac85d13b76d526a5fd603fcb548b",
    "last_success_at": "2026-11-17T05:21:47.266226+00:00"
  }
}
```

</details>
