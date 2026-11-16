# AirCursor

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[m-afham/AirCursor](https://github.com/m-afham/AirCursor)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 226 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:50:00.444Z |

## 中文

把支持头部追踪的耳机动作转换为Mac鼠标移动与点击。

### 用途与功能

- 在不使用手部鼠标时控制Mac

支持头动指针、停留点击、点头动作、自定义手势、校准和菜单栏控制；本地运行，无需摄像头或账户。

### 环境与限制

需macOS15+和兼容传感器耳机，如AirPods Pro、Max、第三代以后AirPods或Beats Fit Pro；支持Intel与Apple Silicon。需要相应辅助功能和动作访问权限，精度与舒适度需实际设备验证。

### 开始使用

安装发行包，连接兼容耳机，完成权限引导与个人动作校准。 参阅[官方 README](https://github.com/m-afham/AirCursor/blob/main/README.md)。

### 收录与来源

虽Star较低，但实现原生输入控制、停留点击、引导校准和更新流程，解决明确的免手动操作需求。 最近维护：[实现提交](https://github.com/m-afham/AirCursor/commit/b1ac85182a27b1d766ac487df22a6a908a4188f7)（2026-11-10T22:20:09Z）。已核对Swift实现：识别临时签名并调整更新权限引导，使稳定证书更新保留权限。

通过逛逛GitHub的第三方文章索引发现。索引记录了下列文章；本次未读取微信原文，不据此声称已阅读全文。

- 2026-11-10：[把你的 AirPods 当鼠标用，这 3 个黑科技 GitHub 开源项目有趣。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538431&idx=1&sn=74a9f0be88c711205e42507b6b8e2b92)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。


补充核对作者在公开平台发布或授权发布的文章，确认署名、日期与仓库关联：

- 2026-11-10：[把你的 AirPods 当鼠标用，这 3 个黑科技 GitHub 开源项目有趣。](https://www.woshipm.com/share/6491690.html)

## English

Turns motion from head-tracking headphones into Mac pointer movement and clicks.

### Uses and features

- Control a Mac without a hand-operated mouse

Provides head-driven pointing, dwell clicks, nod actions, remappable gestures, calibration and menu-bar control, running locally without a camera or account.

### Requirements and limits

Requires macOS 15+ and compatible sensor-equipped headphones such as AirPods Pro, Max, third-generation-or-newer AirPods or Beats Fit Pro, on Intel or Apple Silicon. Accessibility and motion access are required; precision and comfort need device testing.

### Getting started

Install a release, connect compatible headphones and complete permission setup and personal motion calibration. See the [official README](https://github.com/m-afham/AirCursor/blob/main/README.md).

### Review and provenance

Despite a low star count, it implements native input control, dwell clicks, onboarding calibration and updates for a clear hands-free use case. Recent maintenance: [implementation commit](https://github.com/m-afham/AirCursor/commit/b1ac85182a27b1d766ac487df22a6a908a4188f7) (2026-11-10T22:20:09Z). Reviewed Swift changes detecting ad-hoc signatures and adapting update guidance so stable-certificate updates preserve permissions.

Discovered through a third-party index of 逛逛GitHub articles. The index records the articles below; the original WeChat pages were not read in this review. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.


Public articles published or authorized by the author were also checked for attribution, date and repository links. See the additional links in the Chinese section.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:50:00.444Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "aircursor",
    "name": "AirCursor",
    "repository": "m-afham/AirCursor",
    "repo_node_id": "R_kgDOVjSCdQ",
    "category": "productivity",
    "tags": [],
    "forms": [
      "desktop"
    ],
    "platforms": [
      "macos"
    ],
    "aliases": {
      "zh-CN": [
        "AirCursor"
      ],
      "en": [
        "AirCursor"
      ]
    },
    "summary": {
      "zh-CN": "把支持头部追踪的耳机动作转换为Mac鼠标移动与点击。",
      "en": "Turns motion from head-tracking headphones into Mac pointer movement and clicks."
    },
    "use_cases": {
      "zh-CN": [
        "在不使用手部鼠标时控制Mac"
      ],
      "en": [
        "Control a Mac without a hand-operated mouse"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:50:00.444Z",
        "en": "2026-11-16T14:50:00.444Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "ac5569da19be1ab3d4581d246b98aeb7e278262dc0c8eff52cf19d5967c1180b",
      "source_url": "https://github.com/m-afham/AirCursor/blob/main/LICENSE",
      "reviewed_at": "2026-11-16T14:50:00.444Z"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/m-afham/AirCursor/commit/b1ac85182a27b1d766ac487df22a6a908a4188f7",
        "occurred_at": "2026-11-10T22:20:09Z",
        "reason": {
          "zh-CN": "已核对Swift实现：识别临时签名并调整更新权限引导，使稳定证书更新保留权限。",
          "en": "Reviewed Swift changes detecting ad-hoc signatures and adapting update guidance so stable-certificate updates preserve permissions."
        },
        "reviewed_at": "2026-11-16T14:50:00.444Z",
        "qualifies": true
      }
    ],
    "sources": [
      {
        "url": "https://github.com/m-afham/AirCursor/blob/main/README.md",
        "accessed_at": "2026-11-16T14:50:00.444Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/m-afham/AirCursor/blob/main/LICENSE",
        "accessed_at": "2026-11-16T14:50:00.444Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.noking.tech/github-radar/data/library.json",
        "accessed_at": "2026-11-16T14:50:00.444Z",
        "supports": {
          "zh-CN": "第三方索引中的公众号文章归属、时间与项目发现线索；非原文阅读证据。",
          "en": "Third-party account attribution, article dates and discovery leads; not proof of reading the originals."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247538431&idx=1&sn=74a9f0be88c711205e42507b6b8e2b92",
        "accessed_at": "2026-11-16T14:50:00.444Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-11-10 把你的 AirPods 当鼠标用，这 3 个黑科技 GitHub 开源项目有趣。；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-11-10; not directly read in this review."
        }
      },
      {
        "url": "https://www.woshipm.com/share/6491690.html",
        "accessed_at": "2026-11-16T14:25:59.576915+00:00",
        "published_date": "2026-11-10",
        "author": "逛逛GitHub",
        "supports": {
          "zh-CN": "作者公开发表或授权的文章；已核对署名、日期与仓库链接。",
          "en": "Author-published or authorized public article; attribution, date and repository links checked."
        }
      }
    ],
    "quality_review": {
      "basis": {
        "zh-CN": "虽Star较低，但实现原生输入控制、停留点击、引导校准和更新流程，解决明确的免手动操作需求。",
        "en": "Despite a low star count, it implements native input control, dwell clicks, onboarding calibration and updates for a clear hands-free use case."
      },
      "low_star": true
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVjSCdQ",
    "full_name": "m-afham/AirCursor",
    "stargazers_count": 226,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "ac5569da19be1ab3d4581d246b98aeb7e278262dc0c8eff52cf19d5967c1180b",
    "last_success_at": "2026-11-16T14:18:44.440Z"
  }
}
```

</details>

