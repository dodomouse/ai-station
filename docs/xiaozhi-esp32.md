# XiaoZhi ESP32

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[78/xiaozhi-esp32](https://github.com/78/xiaozhi-esp32)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 自动化 / Automation |
| 状态 / Status | 已收录 / Included |
| Star | 33330 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T04:00:03.482525+00:00 |

## 中文

面向 ESP32 设备的语音交互固件，将语音模型和 MCP 设备控制接到硬件上。

### 用途与功能

- 提供离线唤醒、Opus 音频传输和支持板卡上的摄像头输入。
- 通过 WebSocket 或 MQTT/UDP 通信，并用 MCP 控制扬声器、灯和 GPIO。

### 环境与限制

需要受支持板卡及音频硬件；源码构建要求 ESP-IDF 6.0.1+，推荐 release/v6.1。默认连接官方服务，也可配置兼容后端；硬件、模型和服务分别受限。

### 开始使用

按官方板卡教程选择固件并烧录，完成联网和设备激活；自定义硬件参阅 Custom Board Guide。

参阅[官方 README](https://github.com/78/xiaozhi-esp32/blob/aaf1eb7798cabee87a0c6a0649aabf4d17e9e383/README.md)。

### 收录与来源

将语音链路、板卡适配和设备工具放在同一固件中，适合验证语音助手硬件原型。

维护证据：[修正 CST3530 触摸依赖条件的 OR 嵌套，使组件管理器能处理 ESP32-C6 板卡分支。](https://github.com/78/xiaozhi-esp32/commit/4de00aed740595a8713b01f8332b9b2cf30685bc)（2026-11-13）。

发现于 [GitHub 月榜](https://github.com/trending/c%2B%2B?since=monthly)。2026-11-17 的榜单记录新增 2,146 Star，用于本批筛选，不代表全站增速排名。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Voice-interaction firmware that connects ESP32 hardware to voice models and MCP device control.

### Uses and features

- Provides offline wake words, Opus audio transport and camera input on supported boards.
- Communicates through WebSocket or MQTT/UDP and controls speakers, lights and GPIO through MCP.

### Requirements and limits

Requires supported boards and audio hardware. Source builds need ESP-IDF 6.0.1+; release/v6.1 is recommended. Firmware defaults to the hosted service but can use compatible backends; hardware, model and service constraints apply separately.

### Getting started

Choose and flash firmware using the board guide, configure networking and activate the device; consult the Custom Board Guide for custom hardware.

See the [official README](https://github.com/78/xiaozhi-esp32/blob/aaf1eb7798cabee87a0c6a0649aabf4d17e9e383/README.md).

### Review and provenance

Combines voice transport, board integration and device tools for prototyping physical voice assistants.

Maintenance evidence: [Corrects OR nesting in the CST3530 dependency condition so the component manager evaluates the ESP32-C6 board branch.](https://github.com/78/xiaozhi-esp32/commit/4de00aed740595a8713b01f8332b9b2cf30685bc) (2026-11-13).

Discovered in [GitHub monthly Trending](https://github.com/trending/c%2B%2B?since=monthly), which recorded 2,146 added stars on 2026-11-17. This selects the batch; it is not a global growth ranking.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T04:00:03.482525+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "xiaozhi-esp32",
    "name": "XiaoZhi ESP32",
    "repository": "78/xiaozhi-esp32",
    "repo_node_id": "R_kgDOMq4NxA",
    "category": "automation",
    "summary": {
      "zh-CN": "面向 ESP32 设备的语音交互固件，将语音模型和 MCP 设备控制接到硬件上。",
      "en": "Voice-interaction firmware that connects ESP32 hardware to voice models and MCP device control."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T04:00:03.482525+00:00",
        "en": "2026-11-17T04:00:03.482525+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "将语音链路、板卡适配和设备工具放在同一固件中，适合验证语音助手硬件原型。",
      "en": "Combines voice transport, board integration and device tools for prototyping physical voice assistants.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/78/xiaozhi-esp32/blob/aaf1eb7798cabee87a0c6a0649aabf4d17e9e383/LICENSE",
      "license_sha256": "0a5a839033bfe18fe75d32b50d9d028912cf876f69ef59c2791aeb2971335d05",
      "source_commit": "aaf1eb7798cabee87a0c6a0649aabf4d17e9e383",
      "reviewed_at": "2026-11-17T04:00:03.482525+00:00",
      "evidence_pinned_at": "2026-11-17T04:00:03.482525+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "Root license applies to repository software code; models, data, assets and external services have separate terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-13T19:11:08Z",
        "reviewed_at": "2026-11-17T04:00:03.482525+00:00",
        "url": "https://github.com/78/xiaozhi-esp32/commit/4de00aed740595a8713b01f8332b9b2cf30685bc",
        "qualifies": true,
        "reason": {
          "zh-CN": "修正 CST3530 触摸依赖条件的 OR 嵌套，使组件管理器能处理 ESP32-C6 板卡分支。",
          "en": "Corrects OR nesting in the CST3530 dependency condition so the component manager evaluates the ESP32-C6 board branch."
        },
        "reviewed_files": [
          "main/idf_component.yml"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/78/xiaozhi-esp32",
        "accessed_at": "2026-11-17T04:00:03.482525+00:00"
      },
      {
        "url": "https://github.com/78/xiaozhi-esp32/blob/aaf1eb7798cabee87a0c6a0649aabf4d17e9e383/README.md",
        "accessed_at": "2026-11-17T04:00:03.482525+00:00"
      },
      {
        "url": "https://github.com/78/xiaozhi-esp32/blob/aaf1eb7798cabee87a0c6a0649aabf4d17e9e383/LICENSE",
        "accessed_at": "2026-11-17T04:00:03.482525+00:00"
      },
      {
        "url": "https://github.com/78/xiaozhi-esp32/commit/4de00aed740595a8713b01f8332b9b2cf30685bc",
        "accessed_at": "2026-11-17T04:00:03.482525+00:00"
      }
    ],
    "discovery": {
      "kind": "github_trending",
      "period": "monthly",
      "observed_date": "2026-11-17",
      "stars_gained": 2146,
      "source_url": "https://github.com/trending/c%2B%2B?since=monthly",
      "selection_threshold": 1000,
      "ranking_scope": "Selected GitHub Trending language and overall charts; not a global growth ranking."
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOMq4NxA",
    "full_name": "78/xiaozhi-esp32",
    "stargazers_count": 33330,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "0a5a839033bfe18fe75d32b50d9d028912cf876f69ef59c2791aeb2971335d05",
    "last_success_at": "2026-11-17T03:53:28.241476+00:00"
  }
}
```

</details>
