# Claude Cage

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[Lee-xeo/Claude-Cage](https://github.com/Lee-xeo/Claude-Cage)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 部署与运维 / Deployment and operations |
| 状态 / Status | 已收录 / Included |
| Star | 6137 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T06:06:21.872784+00:00 |

## 中文

用于运行 Claude Code 和相关开发工具的桌面工作台，管理本地虚拟机、项目共享与独立网络配置，也可连接自有 Linux 服务器。

### 用途与功能

- 在同一工作台使用客机终端、浏览器、编辑器和可选的 Claude Desktop。
- 管理网络代理、时区和语言配置，检查出口与环境状态，并在检查不通过时暂停业务外网。
- 按需共享项目目录并保留环境磁盘；可通过 SSH 使用云端环境，或配对手机接续会话和审批。

### 环境与限制

发行版支持 macOS 14+ Apple Silicon、Windows 10 22H2/11 x64，以及指定 Debian/Ubuntu x86_64。Linux 主机运行本地客机需 KVM；Windows 11 客机需启用 Hyper-V 的 Windows 11 专业版、企业版或教育版主机。需自备代理、Claude 账户及适用的系统授权。共享目录修改直接影响主机，同一配置内的项目不相互隔离；云端使用 rootless 容器，并非虚拟机。默认公网出站限 IPv4 TCP，DNS 经代理。系统镜像下载使用主机网络；联网检查不是完整安全审计，也不保证账户不受平台限制。

### 开始使用

从 Releases 选择匹配平台的安装包，配置自己的代理并验证出口，再选择客机系统与存储位置。完成安装和联网检查后打开项目，在客机终端运行 `claude` 并用自己的账户授权。

参阅[官方 README](https://github.com/Lee-xeo/Claude-Cage/blob/6b39225bcf1670595d421bc63d729883032dc0c8/README.md)。

### 收录与来源

把 Claude 开发环境、共享目录授权和网络状态放在同一工作台，便于集中管理持久环境。已核对出口转发代码与项目操作并发修复；未安装运行，也未验证虚拟化或网络隔离的完整性。

维护证据：[让打开、保存项目和目录操作等待正在执行的网络巡检，在固定期限内重试取锁，并在请求取消或账户锁定时终止，避免操作跨解锁周期获得权限](https://github.com/Lee-xeo/Claude-Cage/commit/2efa16c78d0c29544280c786f044cccdca7df2dc)（2026-11-17）。

用户于 2026-11-17 提供仓库链接。本条按工程通用标准复核，不设 Star 门槛。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

A desktop workbench for Claude Code and related development tools, managing local VMs, project sharing and separate network configuration, with connections to self-hosted Linux servers.

### Uses and features

- Use a guest terminal, browser, editor and optional Claude Desktop in one workbench.
- Manage network proxies, timezone and language, check egress and environment state, and pause workload internet access when checks fail.
- Share selected project directories and persist environment disks; connect over SSH to a server environment or pair a phone for sessions and approvals.

### Requirements and limits

Releases support macOS 14+ on Apple Silicon, Windows 10 22H2/11 x64 and specified Debian/Ubuntu x86_64 hosts. Linux hosts need KVM for local guests; Windows 11 guests require a Windows 11 Pro, Enterprise or Education host with Hyper-V enabled. Supply your own proxy, Claude account and applicable OS licenses. Shared-directory edits affect host files, projects in one configuration are not isolated from each other, and cloud mode uses rootless containers rather than VMs. Default public egress is IPv4 TCP with proxied DNS; OS-image downloads use the host network. Network checks are neither a full security audit nor a guarantee against account restrictions.

### Getting started

Choose the platform installer from Releases, configure your proxy and verify egress, then select the guest OS and storage location. After installation and network checks, open a project, run `claude` in the guest terminal and authenticate with your own account.

See the [official README](https://github.com/Lee-xeo/Claude-Cage/blob/6b39225bcf1670595d421bc63d729883032dc0c8/README.md).

### Review and provenance

Combines Claude development tools, directory-sharing grants and network status for managing persistent environments. Egress forwarding code and a project-operation concurrency fix were reviewed; the software was not run and isolation completeness was not verified.

Maintenance evidence: [Makes project open/save and directory operations wait for an active network check, retry lock acquisition within a fixed deadline, and abort on cancellation or account lock so work cannot gain authority from a later unlock](https://github.com/Lee-xeo/Claude-Cage/commit/2efa16c78d0c29544280c786f044cccdca7df2dc) (2026-11-17).

Submitted by the user on 2026-11-17 and reviewed against the general catalog criteria, with no star threshold.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T06:06:21.872784+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "claude-cage",
    "name": "Claude Cage",
    "repository": "Lee-xeo/Claude-Cage",
    "repo_node_id": "R_kgDOVeN7AA",
    "category": "operations",
    "summary": {
      "zh-CN": "用于运行 Claude Code 和相关开发工具的桌面工作台，管理本地虚拟机、项目共享与独立网络配置，也可连接自有 Linux 服务器。",
      "en": "A desktop workbench for Claude Code and related development tools, managing local VMs, project sharing and separate network configuration, with connections to self-hosted Linux servers."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T06:06:21.872784+00:00",
        "en": "2026-11-17T06:06:21.872784+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "把 Claude 开发环境、共享目录授权和网络状态放在同一工作台，便于集中管理持久环境。已核对出口转发代码与项目操作并发修复；未安装运行，也未验证虚拟化或网络隔离的完整性。",
      "en": "Combines Claude development tools, directory-sharing grants and network status for managing persistent environments. Egress forwarding code and a project-operation concurrency fix were reviewed; the software was not run and isolation completeness was not verified.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/Lee-xeo/Claude-Cage/blob/6b39225bcf1670595d421bc63d729883032dc0c8/LICENSE",
      "license_sha256": "65354d4222cc95d61aeeb46c3dcd544de53be7ab282c13ca7bad0d3275c4f323",
      "source_commit": "6b39225bcf1670595d421bc63d729883032dc0c8",
      "reviewed_at": "2026-11-17T06:06:21.872784+00:00",
      "evidence_pinned_at": "2026-11-17T06:06:21.872784+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "The root LICENSE grants MIT for Cage and its agent-vm-derived core. It does not replace bundled-component licenses: NOTICE identifies separately executed Mihomo as GPL-3.0, modified noVNC as MPL-2.0, macOS guest SSHFS as GPL-2.0 and linked GLib/gettext as LGPL-2.1-or-later, plus other third-party terms. OS images, Claude products/accounts and proxy services retain their own terms. GitHub license API returned NOASSERTION; MIT is a manual classification from the pinned root license text."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-17T04:29:55Z",
        "reviewed_at": "2026-11-17T06:06:21.872784+00:00",
        "url": "https://github.com/Lee-xeo/Claude-Cage/commit/2efa16c78d0c29544280c786f044cccdca7df2dc",
        "qualifies": true,
        "reason": {
          "zh-CN": "让打开、保存项目和目录操作等待正在执行的网络巡检，在固定期限内重试取锁，并在请求取消或账户锁定时终止，避免操作跨解锁周期获得权限",
          "en": "Makes project open/save and directory operations wait for an active network check, retry lock acquisition within a fixed deadline, and abort on cancellation or account lock so work cannot gain authority from a later unlock"
        },
        "reviewed_files": [
          "internal/workbench/project_operation.go",
          "internal/workbench/runtime.go",
          "internal/workbench/projects.go",
          "internal/workbench/project_groups.go",
          "internal/workbench/server.go",
          "internal/workbench/account_epoch.go"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/Lee-xeo/Claude-Cage",
        "accessed_at": "2026-11-17T06:06:21.872784+00:00"
      },
      {
        "url": "https://github.com/Lee-xeo/Claude-Cage/blob/6b39225bcf1670595d421bc63d729883032dc0c8/README.md",
        "accessed_at": "2026-11-17T06:06:21.872784+00:00"
      },
      {
        "url": "https://github.com/Lee-xeo/Claude-Cage/blob/6b39225bcf1670595d421bc63d729883032dc0c8/LICENSE",
        "accessed_at": "2026-11-17T06:06:21.872784+00:00"
      },
      {
        "url": "https://github.com/Lee-xeo/Claude-Cage/commit/2efa16c78d0c29544280c786f044cccdca7df2dc",
        "accessed_at": "2026-11-17T06:06:21.872784+00:00"
      },
      {
        "url": "https://github.com/Lee-xeo/Claude-Cage/blob/6b39225bcf1670595d421bc63d729883032dc0c8/go.mod",
        "accessed_at": "2026-11-17T06:06:21.872784+00:00"
      },
      {
        "url": "https://github.com/Lee-xeo/Claude-Cage/blob/6b39225bcf1670595d421bc63d729883032dc0c8/NOTICE",
        "accessed_at": "2026-11-17T06:06:21.872784+00:00"
      },
      {
        "url": "https://github.com/Lee-xeo/Claude-Cage/blob/6b39225bcf1670595d421bc63d729883032dc0c8/THIRD_PARTY_LICENSES",
        "accessed_at": "2026-11-17T06:06:21.872784+00:00"
      },
      {
        "url": "https://github.com/Lee-xeo/Claude-Cage/blob/6b39225bcf1670595d421bc63d729883032dc0c8/docs/getting-started.md",
        "accessed_at": "2026-11-17T06:06:21.872784+00:00"
      },
      {
        "url": "https://github.com/Lee-xeo/Claude-Cage/blob/6b39225bcf1670595d421bc63d729883032dc0c8/docs/guide/guest-systems.md",
        "accessed_at": "2026-11-17T06:06:21.872784+00:00"
      },
      {
        "url": "https://github.com/Lee-xeo/Claude-Cage/blob/6b39225bcf1670595d421bc63d729883032dc0c8/docs/guide/network.md",
        "accessed_at": "2026-11-17T06:06:21.872784+00:00"
      },
      {
        "url": "https://github.com/Lee-xeo/Claude-Cage/blob/6b39225bcf1670595d421bc63d729883032dc0c8/docs/guide/cloud.md",
        "accessed_at": "2026-11-17T06:06:21.872784+00:00"
      },
      {
        "url": "https://github.com/Lee-xeo/Claude-Cage/blob/6b39225bcf1670595d421bc63d729883032dc0c8/internal/cage/egress.go",
        "accessed_at": "2026-11-17T06:06:21.872784+00:00"
      },
      {
        "url": "https://github.com/Lee-xeo/Claude-Cage/blob/6b39225bcf1670595d421bc63d729883032dc0c8/internal/workbench/runtime.go",
        "accessed_at": "2026-11-17T06:06:21.872784+00:00"
      }
    ],
    "discovery": {
      "kind": "user_submission",
      "submitted_date": "2026-11-17",
      "source_url": "https://github.com/Lee-xeo/Claude-Cage",
      "repository_url": "https://github.com/Lee-xeo/Claude-Cage"
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVeN7AA",
    "full_name": "Lee-xeo/Claude-Cage",
    "stargazers_count": 6137,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "api_license_spdx": "MIT",
    "license_sha256": "65354d4222cc95d61aeeb46c3dcd544de53be7ab282c13ca7bad0d3275c4f323",
    "last_success_at": "2026-11-17T05:32:14.036450+00:00"
  }
}
```

</details>
