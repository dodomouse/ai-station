# Netdata Agent

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[netdata/netdata](https://github.com/netdata/netdata)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 部署与运维 / Deployment and operations |
| 状态 / Status | 已收录 / Included |
| Star | 81435 |
| 许可证 / License | GPL-3.0-or-later |
| 评估时间 / Evaluated at | 2026-11-16T14:29:18.179Z |

## 中文

采集主机、容器与应用指标，并在本地存储、检测异常和触发告警。

### 用途与功能

- 定位主机与服务性能变化
- 汇集多节点监控指标

提供自动发现、秒级采样、多种采集器、指标流转与告警规则。可将指标导出到其他系统，或选择连接 Netdata Cloud。

### 环境与限制

本词条仅收录 GPL 开源的 Agent 核心。当前 Web 界面采用 NCUL1 专有许可，Cloud 也非开源，且包含付费功能。支持 Linux、macOS、Windows 和 FreeBSD；采集能力和安装步骤因平台而异。监控数据与配置需按部署环境管理。

### 开始使用

按官方安装页选择系统，安装 Agent 后检查采集器、数据保留和告警配置。 参阅[官方 README](https://github.com/netdata/netdata/blob/master/README.md)。

### 收录与来源

具备实际采集器、存储与告警实现，并提供平台安装文档和持续维护。 最近维护：[v2.12.3](https://github.com/netdata/netdata/releases/tag/v2.12.3)（2026-11-04T16:43:10Z）。正式版修复连接检测、内存访问和 SQLite 运行故障。

由 Frontier Now 二级索引发现，其页面记录 AI开源求索于 2026-10-01 介绍 Netdata；本次未取得该公众号原文。

- 2026-10-01：[Frontier Now 的 Netdata 条目](https://frontiernow.dev/zh/github/netdata/)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。

## English

Collects host, container and application metrics, with local storage, anomaly detection and alerts.

### Uses and features

- Investigate host and service performance
- Collect metrics across multiple nodes

Includes auto-discovery, per-second sampling, collectors, metric streaming and alert rules. Metrics can be exported to other systems or connected to optional Netdata Cloud.

### Requirements and limits

This entry covers the GPL-licensed Agent core. The current Web UI uses the proprietary NCUL1 license; Cloud is also proprietary and includes paid features. Linux, macOS, Windows and FreeBSD have different collectors and setup paths. Manage monitoring data and configuration for the deployment environment.

### Getting started

Choose the installation guide for your OS, install the Agent, then review collectors, retention and alerts. See the [official README](https://github.com/netdata/netdata/blob/master/README.md).

### Review and provenance

Includes implemented collectors, storage and alerting, with platform installation guides and ongoing maintenance. Recent maintenance: [v2.12.3](https://github.com/netdata/netdata/releases/tag/v2.12.3) (2026-11-04T16:43:10Z). The formal release fixes connection detection, memory-access and SQLite runtime issues.

Discovered through Frontier Now, which attributes a Netdata article to AI开源求索 on 2026-10-01. The original account article was not obtained. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:29:18.179Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "netdata",
    "name": "Netdata Agent",
    "repository": "netdata/netdata",
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkxMDc0NDE4Mw==",
    "category": "operations",
    "tags": [],
    "forms": [
      "service"
    ],
    "platforms": [
      "linux",
      "macos",
      "windows",
      "freebsd"
    ],
    "aliases": {
      "zh-CN": [
        "Netdata Agent"
      ],
      "en": [
        "Netdata Agent"
      ]
    },
    "summary": {
      "zh-CN": "采集主机、容器与应用指标，并在本地存储、检测异常和触发告警。",
      "en": "Collects host, container and application metrics, with local storage, anomaly detection and alerts."
    },
    "use_cases": {
      "zh-CN": [
        "定位主机与服务性能变化",
        "汇集多节点监控指标"
      ],
      "en": [
        "Investigate host and service performance",
        "Collect metrics across multiple nodes"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:29:18.179Z",
        "en": "2026-11-16T14:29:18.179Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "GPL-3.0-or-later",
      "osi_approved": true,
      "license_sha256": "0e5fd9d833efe9b79f784d1903281554af82d1b4261af67d35455728e5572aa6",
      "source_url": "https://github.com/netdata/netdata/blob/c7eeb0b732abfe5b95e16a33fa3b721a0b3b06e6/LICENSE",
      "reviewed_at": "2026-11-16T14:29:18.179Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "c7eeb0b732abfe5b95e16a33fa3b721a0b3b06e6"
    },
    "activity_evidence": [
      {
        "type": "release",
        "url": "https://github.com/netdata/netdata/releases/tag/v2.12.3",
        "occurred_at": "2026-11-04T16:43:10Z",
        "reason": {
          "zh-CN": "正式版修复连接检测、内存访问和 SQLite 运行故障。",
          "en": "The formal release fixes connection detection, memory-access and SQLite runtime issues."
        },
        "reviewed_at": "2026-11-16T14:29:18.179Z",
        "qualifies": true
      }
    ],
    "sources": [
      {
        "url": "https://github.com/netdata/netdata/blob/master/README.md",
        "accessed_at": "2026-11-16T14:29:18.179Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/netdata/netdata/blob/c7eeb0b732abfe5b95e16a33fa3b721a0b3b06e6/LICENSE",
        "accessed_at": "2026-11-16T14:29:18.179Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://frontiernow.dev/zh/github/netdata/",
        "accessed_at": "2026-11-16T14:29:18.153Z",
        "supports": {
          "zh-CN": "二级索引中 AI开源求索的归属、日期和发现线索。",
          "en": "Secondary attribution to AI开源求索, date and discovery lead."
        }
      }
    ],
    "quality_review": {
      "basis": {
        "zh-CN": "具备实际采集器、存储与告警实现，并提供平台安装文档和持续维护。",
        "en": "Includes implemented collectors, storage and alerting, with platform installation guides and ongoing maintenance."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "MDEwOlJlcG9zaXRvcnkxMDc0NDE4Mw==",
    "full_name": "netdata/netdata",
    "stargazers_count": 81435,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "GPL-3.0-or-later",
    "license_sha256": "0e5fd9d833efe9b79f784d1903281554af82d1b4261af67d35455728e5572aa6",
    "last_success_at": "2026-11-16T14:21:01Z"
  }
}
```

</details>

