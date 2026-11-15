# TelemetryCleaner

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[Eynnzerr/TelemetryCleaner](https://github.com/Eynnzerr/TelemetryCleaner)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 部署与运维 / Operations |
| 状态 / Status | 候选 / Candidate |
| Star | 807 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T11:45:04.617Z |

候选原因：Star 未满 1000。
Candidate reason: Below 1000 Stars.

以上为历史核对结果，使用前请复核上游状态。 / This is a dated review; check the current upstream state before use.

## 中文

TelemetryCleaner 是 Android 运营商预装组件管理工具。它通过 Shizuku 检查已知组件在不同用户空间中的状态，提供权限查看、按空间卸载、恢复和停用操作。适合希望了解手机预装包、并评估是否调整组件状态的用户。

当前保留为候选：本次核对时未达到字典的 1000 Star 门槛。数据见 [GitHub 快照](#review-evidence)。该项目列在目录的候选部分。

### 适用场景

- 检查设备是否安装内置清单中的运营商组件。
- 查看主空间、分身或其他用户空间的安装状态与权限记录。
- 在确认影响后，管理指定空间中的组件，并查看操作结果。

### 主要功能

| 功能 | 范围与行为 |
| --- | --- |
| 已知组件检测 | 按内置包名清单检查 SystemHelper、RegService 及部分厂商组件；不是扫描所有应用的行为分析器。 |
| 权限查看 | 读取 Android 包管理器中的声明和授权记录；这些记录本身不能证明组件实际读取或上传了数据。 |
| 按空间卸载 | 对选定空间执行操作，并重新读取包状态核对结果。卸载会清除该空间的组件数据。 |
| 失败后停用 | v1.3 新增手动卸载失败后的停用兜底，设置默认启用。停用保留已有数据和缓存。 |
| 恢复 | 对手动停用的组件尝试重新启用。重新安装已卸载组件需要设备上仍有 APK 副本。 |
| 自动清理 | 默认关闭；启用后按周期检查所选空间，只处理自动清理名单中的组件。 |
| 诊断日志 | 卸载与停用都失败时，可复制拒绝日志供排查。 |

以上范围来自[官方 README](https://github.com/Eynnzerr/TelemetryCleaner/blob/47d7f733ecb821bae154ead8f8bfcb945a170db7/README.md)、[v1.3 说明](https://github.com/Eynnzerr/TelemetryCleaner/releases/tag/v1.3)及[功能提交](https://github.com/Eynnzerr/TelemetryCleaner/commit/e8dd7786628f368907f0d1d31ec2829cc373639a)。

### 环境与限制

- Android 10 或以上，且 Shizuku 已启动并获得授权。Android 11 或以上可按上游指引使用无线调试启动 Shizuku。
- 免 Root 路径借助 shell 权限请求包管理服务。厂商 ROM 仍可拒绝操作，不能保证所有设备都能卸载。
- v1.3 仍未解决部分 vivo 电信、移动组件无法卸载的问题。作者记录过卸载 Device Management 后通话录音失效的用户反馈；这不是本字典的实机验证结果。
- 恢复组件不等于找回卸载时删除的数据。设备未保留 APK 时，也不能保证重新安装。
- 检测范围受清单覆盖限制。未检出已知组件不能证明设备没有其他遥测行为。运营商组件也可能承担正常的入网或运维功能。
- 根目录为 [MIT 许可证](https://github.com/Eynnzerr/TelemetryCleaner/blob/47d7f733ecb821bae154ead8f8bfcb945a170db7/LICENSE)。作者在 README 中将项目定位为 Android 包管理机制的学习工具。

### 开始使用

1. 阅读[官方 README](https://github.com/Eynnzerr/TelemetryCleaner#readme)中的环境要求、组件清单和设备反馈。
2. 从[官方发行页](https://github.com/Eynnzerr/TelemetryCleaner/releases)选择版本，并按上游指南启动 Shizuku。
3. 先检查目标空间、包名和权限记录，再决定是否授权具体操作。
4. 根据结果区分已卸载、已停用和失败。需要恢复时，先确认 APK 副本与数据恢复的区别。

本次收录未下载或安装 APK，也未在手机上执行卸载、停用或恢复。

### 替代选择

现有字典没有经过核对的同用途替代项。选择其他包管理工具时，可比较操作范围、状态核验和恢复条件。

### 复核说明

2026-11-15 核对官方说明、MIT 文件、v1.3 发行记录及部分 Kotlin 实现。源码确认最低 SDK 为 29、自动清理默认关闭、手动卸载失败后的停用兜底默认启用。维护证据为 2026-11-13 的功能提交，最新的许可文件提交未单独用作有效维护证明。

验证级别为 `docs`。源码阅读只能支持实现说明，不能证明各机型上的兼容性或隐私效果。来源、时间和许可指纹见 [收录依据](#review-evidence)。

## English

TelemetryCleaner manages known carrier components preinstalled on Android devices. Through Shizuku, it inspects package states across user spaces and provides permission inspection, per-space removal, restoration and disabling controls. It is intended for users investigating preinstalled packages and deciding whether to change their state.

This entry remains a candidate because it was below the catalog's 1000-Star threshold when reviewed. See the [GitHub snapshot](#review-evidence). The candidate is listed in the main index.

### Use cases

- Check whether a device contains carrier packages in the bundled directory.
- Inspect installation states and permission records across Android user spaces.
- Manage selected components after assessing their role, then inspect the reported outcome.

### Features

| Feature | Scope and behavior |
| --- | --- |
| Known-package detection | Checks a bundled package-name list, including SystemHelper, RegService and selected vendor components. It does not analyze every app's behavior. |
| Permission inspection | Reads Android package-manager declarations and grant records. These do not prove that a package actually accessed or transmitted data. |
| Per-space removal | Operates on selected spaces and rereads package state to confirm the result. Removal clears component data in those spaces. |
| Disable fallback | v1.3 adds an option, enabled by default, to try disabling after a manual uninstall fails. Disabling retains existing data and caches. |
| Restoration | Can re-enable manually disabled components. Reinstalling a removed package requires an APK copy still available on the device. |
| Automatic cleanup | Off by default. When enabled, periodically checks selected spaces and processes only the automatic-cleanup list. |
| Diagnostics | Provides copyable denial logs when both removal and disabling fail. |

Sources: [official README](https://github.com/Eynnzerr/TelemetryCleaner/blob/47d7f733ecb821bae154ead8f8bfcb945a170db7/README.md), [v1.3 notes](https://github.com/Eynnzerr/TelemetryCleaner/releases/tag/v1.3) and the [implementation commit](https://github.com/Eynnzerr/TelemetryCleaner/commit/e8dd7786628f368907f0d1d31ec2829cc373639a).

### Requirements and limits

- Requires Android 10 or later and a running, authorized Shizuku service. The upstream instructions support wireless-debugging startup on Android 11 or later.
- The non-root path uses shell privileges to request package-manager operations. Vendor ROMs can still reject them; removal is not guaranteed on every device.
- v1.3 does not resolve removal failures for some vivo carrier components. The maintainer records user reports of lost call-recording functionality after removing Device Management. This catalog did not reproduce those reports.
- Restoring a package does not recover data deleted during removal. Reinstallation also depends on a retained APK.
- Detection is limited to known packages. An empty result does not establish the absence of other telemetry, and carrier components can have legitimate functions.
- The root [license is MIT](https://github.com/Eynnzerr/TelemetryCleaner/blob/47d7f733ecb821bae154ead8f8bfcb945a170db7/LICENSE). The README describes the project as an educational tool for Android package management.

### Getting started

1. Read the [official README](https://github.com/Eynnzerr/TelemetryCleaner#readme), including requirements, package coverage and device feedback.
2. Choose a version from [official releases](https://github.com/Eynnzerr/TelemetryCleaner/releases), then follow the upstream Shizuku setup instructions.
3. Inspect the target space, package name and permission records before authorizing an operation.
4. Distinguish removed, disabled and failed outcomes. Before restoration, check whether an APK remains and remember that deleted data is separate.

This import did not download or install the APK, or remove, disable or restore any device package.

### Alternatives

The catalog has no reviewed equivalent yet. When comparing package managers, consider operation scope, result verification and restoration conditions.

### Review

Reviewed on 2026-11-15 using official documentation, the MIT file, v1.3 notes and selected Kotlin code. The code specifies SDK 29 as the minimum, automatic cleanup off by default and the manual-uninstall disable fallback on by default. The 2026-11-13 functional commit provides maintenance evidence; the later license-only commit is not used for that purpose.

Verification level: `docs`. Source inspection supports implementation descriptions, not device compatibility or privacy guarantees. See [shared metadata](#review-evidence) for sources, timestamps and the license fingerprint.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

保留原始核对数据，便于追溯来源、许可和维护证据。 / Original review data preserves source, license and maintenance evidence.

```json
{
  "evaluated_at": "2026-11-15T11:54:08.129868Z",
  "eligibility": {
    "status": "ineligible",
    "reasons": [
      "below_star_threshold"
    ]
  },
  "metadata": {
    "schema_version": 1,
    "id": "telemetrycleaner",
    "name": "TelemetryCleaner",
    "repository": "Eynnzerr/TelemetryCleaner",
    "repo_node_id": "R_kgDOVqQ_bw",
    "category": "operations",
    "tags": [
      "android",
      "privacy",
      "shizuku",
      "system-apps"
    ],
    "forms": [],
    "platforms": [
      "android"
    ],
    "aliases": {
      "zh-CN": [
        "遥测清理",
        "安卓运营商组件管理"
      ],
      "en": [
        "Telemetry Cleaner",
        "Android carrier component manager"
      ]
    },
    "summary": {
      "zh-CN": "通过 Shizuku 检查 Android 预装运营商组件，查看各空间状态与权限，并管理卸载、恢复及失败后的停用。",
      "en": "Uses Shizuku to inspect Android carrier packages across user spaces and manage removal, restoration and disabling after failed uninstalls."
    },
    "use_cases": {
      "zh-CN": [
        "检测已知运营商预装组件",
        "查看各用户空间的安装状态和权限记录",
        "评估影响后管理指定空间的组件状态"
      ],
      "en": [
        "Detect known preinstalled carrier components",
        "Inspect package states and permission records across user spaces",
        "Manage selected package states after assessing their effects"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-15T11:54:08.129868Z",
        "en": "2026-11-15T11:54:08.129868Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "c93b8f273ef009de6e57fa5d920d328aa5197e40f8e1f739e9d1f70a46315f23",
      "source_url": "https://github.com/Eynnzerr/TelemetryCleaner/blob/47d7f733ecb821bae154ead8f8bfcb945a170db7/LICENSE",
      "reviewed_at": "2026-11-15T11:54:08.129868Z"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-13T09:31:46Z",
        "reviewed_at": "2026-11-15T11:54:08.129868Z",
        "url": "https://github.com/Eynnzerr/TelemetryCleaner/commit/e8dd7786628f368907f0d1d31ec2829cc373639a",
        "qualifies": true,
        "reason": {
          "zh-CN": "该提交实现手动卸载失败后的停用选项、结果状态及恢复处理。已阅读设置与包操作差异，属于功能变更，未运行手机测试。",
          "en": "Implements the disable fallback, result states and restoration handling for failed manual uninstalls. Settings and package-operation diffs were inspected; no device test was run."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/Eynnzerr/TelemetryCleaner/blob/47d7f733ecb821bae154ead8f8bfcb945a170db7/README.md",
        "accessed_at": "2026-11-15T11:54:08.129868Z",
        "supports": {
          "zh-CN": "官方用途、功能范围、入门和限制。",
          "en": "Official purpose, feature scope, setup and limitations."
        }
      },
      {
        "url": "https://github.com/Eynnzerr/TelemetryCleaner/blob/47d7f733ecb821bae154ead8f8bfcb945a170db7/LICENSE",
        "accessed_at": "2026-11-15T11:54:08.129868Z",
        "supports": {
          "zh-CN": "当前根许可证及适用范围。",
          "en": "Current root license and its scope."
        }
      },
      {
        "url": "https://api.github.com/repos/Eynnzerr/TelemetryCleaner",
        "accessed_at": "2026-11-15T11:45:04.617Z",
        "supports": {
          "zh-CN": "本次仓库身份、Star 和公开状态。",
          "en": "Repository identity, Stars and public state at review time."
        }
      },
      {
        "url": "https://opensource.org/license/mit",
        "accessed_at": "2026-11-15T11:54:08.129868Z",
        "supports": {
          "zh-CN": "MIT 为 OSI 批准的许可证；与根文件许可条款对照。",
          "en": "MIT is OSI-approved; its permission terms were compared with the root file."
        }
      },
      {
        "url": "https://github.com/Eynnzerr/TelemetryCleaner/blob/47d7f733ecb821bae154ead8f8bfcb945a170db7/app/build.gradle.kts",
        "accessed_at": "2026-11-15T11:54:08.129868Z",
        "supports": {
          "zh-CN": "最低 SDK 29，对应 Android 10。",
          "en": "Minimum SDK 29, corresponding to Android 10."
        }
      },
      {
        "url": "https://github.com/Eynnzerr/TelemetryCleaner/blob/47d7f733ecb821bae154ead8f8bfcb945a170db7/app/src/main/java/com/eynnzerr/telemetrycleaner/data/CleanerSettings.kt",
        "accessed_at": "2026-11-15T11:54:08.129868Z",
        "supports": {
          "zh-CN": "自动清理及停用兜底的默认值。",
          "en": "Defaults for automatic cleanup and disable fallback."
        }
      },
      {
        "url": "https://github.com/Eynnzerr/TelemetryCleaner/blob/47d7f733ecb821bae154ead8f8bfcb945a170db7/app/src/main/java/com/eynnzerr/telemetrycleaner/data/PackagePermissions.kt",
        "accessed_at": "2026-11-15T11:54:08.129868Z",
        "supports": {
          "zh-CN": "按用户空间解析权限记录。",
          "en": "Permission records parsed per user space."
        }
      },
      {
        "url": "https://github.com/Eynnzerr/TelemetryCleaner/releases/tag/v1.3",
        "accessed_at": "2026-11-15T11:45:04.913Z",
        "supports": {
          "zh-CN": "v1.3 停用兜底及 vivo 限制说明。",
          "en": "v1.3 disable fallback and documented vivo limitations."
        }
      }
    ],
    "catalog_review": {
      "reviewed_at": "2026-11-15T11:54:08.129868Z",
      "notes": {
        "zh-CN": "Star 未达门槛。已核对 MIT 与近期功能提交；只做文档和源码复核，未操作设备。",
        "en": "Below the Star threshold. MIT and recent functional activity were checked; documentation and source review only, with no device operations."
      }
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVqQ_bw",
    "full_name": "Eynnzerr/TelemetryCleaner",
    "stargazers_count": 807,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "c93b8f273ef009de6e57fa5d920d328aa5197e40f8e1f739e9d1f70a46315f23",
    "last_success_at": "2026-11-15T11:45:04.617Z"
  }
}
```

</details>
