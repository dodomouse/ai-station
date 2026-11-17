# Many PPT Skills

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[brycewang-stanford/many-ppt-skills](https://github.com/brycewang-stanford/many-ppt-skills)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 知识与学习 / Knowledge and learning |
| 状态 / Status | 已收录 / Included |
| Star | 81 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T06:06:21.881310+00:00 |

## 中文

面向智能体的 AI 幻灯片工具登记册和查询脚本，按可编辑性、备注、模板与交付格式筛选技能及视觉样式。

### 用途与功能

- 比较 HTML 与 PPTX 路线，查询工具能力、安装方式和样式标识。
- 维护带来源的能力说明和固定提交的上游示例图片链接，供选型参考。
- 提供统计刷新、双语目录生成和基准测试工具；该项目本身不生成演示文稿。

### 环境与限制

查询脚本需要 Python 3 和仓库 data 目录；刷新数据需要 GitHub 网络访问，受 API 限流影响。实际制作仍需另行安装目标技能及其运行环境。多数能力来自项目文档，样例来自上游展示；横评样本不足，热度和图库不能作为质量排名。收录范围是 MIT 代码，登记册与研究内容另为 CC BY 4.0。

### 开始使用

克隆仓库后先阅读路线比较，使用 `python scripts/pick.py route` 或按需求执行 list、compare、styles 子命令。根据输出到目标仓库核对安装、能力和许可，再制作演示文稿。

参阅[官方 README](https://github.com/brycewang-stanford/many-ppt-skills/blob/3d56ba677126e81d9cf855d5ec232001ebfd3a48/README.md)。

### 收录与来源

提供可查询的选型资料和独立维护脚本，帮助智能体缩小工具范围；不把文档声明当作已验证性能。已读查询实现与失败刷新保值回归补丁，未运行基准测试。

维护证据：[统计刷新在写检查点前读取旧快照，使本次请求失败的仓库保留此前数据并标记 stale；新增覆盖检查点写入后的失败恢复用例](https://github.com/brycewang-stanford/many-ppt-skills/commit/62d40768a8cc5dd3cbd309da257e1350dc6f5380)（2026-09-05）。

仓库来自用户于 2026-11-17 提供的办公技能 PDF，已另行核对上游。本条按工程通用标准复核，不设 Star 门槛。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

An AI slide-tool registry and query toolkit for agents, filtering skills and visual styles by editability, notes, templates and delivery format.

### Uses and features

- Compares HTML and PPTX routes and queries capabilities, installation methods and style identifiers.
- Maintains sourced capability descriptions and commit-pinned links to upstream sample images for tool selection.
- Provides statistics refresh, bilingual catalog generation and benchmark tooling; it does not generate decks itself.

### Requirements and limits

Queries need Python 3 and the repository data directory; refreshes need GitHub access and are subject to API limits. Actual deck creation requires installing the selected skill and its runtime. Most capabilities are documentation claims and samples are upstream showcases; limited benchmark data, stars and galleries do not establish a quality ranking. The included code is MIT; registry and research content is separately CC BY 4.0.

### Getting started

Clone the repository and use `python scripts/pick.py route`, or its list, compare and styles commands. Verify installation, capabilities and licensing in the chosen upstream repository before creating a deck.

See the [official README](https://github.com/brycewang-stanford/many-ppt-skills/blob/3d56ba677126e81d9cf855d5ec232001ebfd3a48/README.md).

### Review and provenance

Provides queryable selection evidence and maintenance scripts to narrow tool choices without treating documentation claims as measured performance. The query implementation and failed-refresh regression patch were reviewed; benchmarks were not run.

Maintenance evidence: [Loads the previous statistics snapshot before checkpoint writes so failed repository requests retain their earlier data with a stale flag, and adds regression coverage across checkpoint writes](https://github.com/brycewang-stanford/many-ppt-skills/commit/62d40768a8cc5dd3cbd309da257e1350dc6f5380) (2026-09-05).

Identified in an office-skills PDF supplied by the user on 2026-11-17, independently checked against upstream sources and reviewed against the general catalog criteria, with no star threshold.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T06:06:21.881310+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "many-ppt-skills",
    "name": "Many PPT Skills",
    "repository": "brycewang-stanford/many-ppt-skills",
    "repo_node_id": "R_kgDOTmBScw",
    "category": "knowledge",
    "summary": {
      "zh-CN": "面向智能体的 AI 幻灯片工具登记册和查询脚本，按可编辑性、备注、模板与交付格式筛选技能及视觉样式。",
      "en": "An AI slide-tool registry and query toolkit for agents, filtering skills and visual styles by editability, notes, templates and delivery format."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T06:06:21.881310+00:00",
        "en": "2026-11-17T06:06:21.881310+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "提供可查询的选型资料和独立维护脚本，帮助智能体缩小工具范围；不把文档声明当作已验证性能。已读查询实现与失败刷新保值回归补丁，未运行基准测试。",
      "en": "Provides queryable selection evidence and maintenance scripts to narrow tool choices without treating documentation claims as measured performance. The query implementation and failed-refresh regression patch were reviewed; benchmarks were not run.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/brycewang-stanford/many-ppt-skills/blob/3d56ba677126e81d9cf855d5ec232001ebfd3a48/LICENSE-CODE",
      "license_sha256": "85cec0bdefb216ab287f422f54eddd21ca3880105a9802a084c365d1f497b929",
      "source_commit": "3d56ba677126e81d9cf855d5ec232001ebfd3a48",
      "reviewed_at": "2026-11-17T06:06:21.881310+00:00",
      "evidence_pinned_at": "2026-11-17T06:06:21.881310+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "MIT applies only to scripts/, benchmark/runner/ and .github/ under LICENSE-CODE. Registry data, README, benchmark corpus/rubric, principles and research notes are separately CC BY 4.0 under root LICENSE and are not labeled OSI-approved software. Linked skills, sample images and third-party projects retain their own terms; the skill wrapper is not part of the explicit MIT directory grant.",
      "files": [
        {
          "spdx": "MIT",
          "osi_approved": true,
          "source_url": "https://github.com/brycewang-stanford/many-ppt-skills/blob/3d56ba677126e81d9cf855d5ec232001ebfd3a48/LICENSE-CODE",
          "license_sha256": "85cec0bdefb216ab287f422f54eddd21ca3880105a9802a084c365d1f497b929",
          "source_commit": "3d56ba677126e81d9cf855d5ec232001ebfd3a48",
          "reviewed_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_pinned_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_status": "hash_matched",
          "scope": "MIT applies only to scripts/, benchmark/runner/ and .github/ under LICENSE-CODE. Registry data, README, benchmark corpus/rubric, principles and research notes are separately CC BY 4.0 under root LICENSE and are not labeled OSI-approved software. Linked skills, sample images and third-party projects retain their own terms; the skill wrapper is not part of the explicit MIT directory grant."
        },
        {
          "scope": "Registry, research and benchmark content, not software-code approval",
          "spdx": "CC-BY-4.0",
          "osi_approved": false,
          "source_url": "https://github.com/brycewang-stanford/many-ppt-skills/blob/3d56ba677126e81d9cf855d5ec232001ebfd3a48/LICENSE",
          "license_sha256": "fafee6ec04d48cdefce98ddd375dc3de4cbb17f7658dfd7fb4de100f5e80d9f1",
          "source_commit": "3d56ba677126e81d9cf855d5ec232001ebfd3a48",
          "reviewed_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_pinned_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_status": "hash_matched"
        }
      ],
      "components": [
        {
          "scope": "Registry, research and benchmark content, not software-code approval",
          "spdx": "CC-BY-4.0",
          "osi_approved": false,
          "source_url": "https://github.com/brycewang-stanford/many-ppt-skills/blob/3d56ba677126e81d9cf855d5ec232001ebfd3a48/LICENSE",
          "license_sha256": "fafee6ec04d48cdefce98ddd375dc3de4cbb17f7658dfd7fb4de100f5e80d9f1",
          "source_commit": "3d56ba677126e81d9cf855d5ec232001ebfd3a48",
          "reviewed_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_pinned_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_status": "hash_matched"
        }
      ]
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-09-05T06:27:44Z",
        "reviewed_at": "2026-11-17T06:06:21.881310+00:00",
        "url": "https://github.com/brycewang-stanford/many-ppt-skills/commit/62d40768a8cc5dd3cbd309da257e1350dc6f5380",
        "qualifies": true,
        "reason": {
          "zh-CN": "统计刷新在写检查点前读取旧快照，使本次请求失败的仓库保留此前数据并标记 stale；新增覆盖检查点写入后的失败恢复用例",
          "en": "Loads the previous statistics snapshot before checkpoint writes so failed repository requests retain their earlier data with a stale flag, and adds regression coverage across checkpoint writes"
        },
        "reviewed_files": [
          "scripts/fetch_stats.py",
          "scripts/test_fetch_stats.py"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/brycewang-stanford/many-ppt-skills",
        "accessed_at": "2026-11-17T06:06:21.881310+00:00"
      },
      {
        "url": "https://github.com/brycewang-stanford/many-ppt-skills/blob/3d56ba677126e81d9cf855d5ec232001ebfd3a48/README.md",
        "accessed_at": "2026-11-17T06:06:21.881310+00:00"
      },
      {
        "url": "https://github.com/brycewang-stanford/many-ppt-skills/blob/3d56ba677126e81d9cf855d5ec232001ebfd3a48/LICENSE-CODE",
        "accessed_at": "2026-11-17T06:06:21.881310+00:00"
      },
      {
        "url": "https://github.com/brycewang-stanford/many-ppt-skills/commit/62d40768a8cc5dd3cbd309da257e1350dc6f5380",
        "accessed_at": "2026-11-17T06:06:21.881310+00:00"
      },
      {
        "url": "https://github.com/brycewang-stanford/many-ppt-skills/blob/3d56ba677126e81d9cf855d5ec232001ebfd3a48/LICENSE",
        "accessed_at": "2026-11-17T06:06:21.881310+00:00"
      },
      {
        "url": "https://github.com/brycewang-stanford/many-ppt-skills/blob/3d56ba677126e81d9cf855d5ec232001ebfd3a48/SKILL.md",
        "accessed_at": "2026-11-17T06:06:21.881310+00:00"
      },
      {
        "url": "https://github.com/brycewang-stanford/many-ppt-skills/blob/3d56ba677126e81d9cf855d5ec232001ebfd3a48/scripts/pick.py",
        "accessed_at": "2026-11-17T06:06:21.881310+00:00"
      }
    ],
    "discovery": {
      "kind": "user_pdf",
      "submitted_date": "2026-11-17",
      "source_url": "https://github.com/brycewang-stanford/many-ppt-skills",
      "repository_url": "https://github.com/brycewang-stanford/many-ppt-skills",
      "source_title": "办公室 Skill 从夯到拉(纯主观)",
      "source_pages": [
        2
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOTmBScw",
    "full_name": "brycewang-stanford/many-ppt-skills",
    "stargazers_count": 81,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "api_license_spdx": "NOASSERTION",
    "license_sha256": "85cec0bdefb216ab287f422f54eddd21ca3880105a9802a084c365d1f497b929",
    "last_success_at": "2026-11-17T05:44:55.713208+00:00"
  }
}
```

</details>
