# MiniMax Skills

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[MiniMax-AI/skills](https://github.com/MiniMax-AI/skills)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 开发辅助 / Development tools |
| 状态 / Status | 已收录 / Included |
| Star | 13846 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-17T06:06:21.880337+00:00 |

## 中文

为编程智能体提供前端、全栈和移动开发技能，并附带文档处理及 MiniMax 多模态素材生成流程。

### 用途与功能

- 用技能指令组织设计、动效、代码实现和质量检查，覆盖多种前端及移动技术栈。
- 附带演示文稿、Word、PDF 和表格工作流，以及图像、视频、语音与音乐相关技能。
- 多模态脚本可通过 MiniMax API 生成素材；已核对图像生成与参考图编辑的请求实现。

### 环境与限制

需要支持本地技能的编程智能体；依赖随技能变化，可能涉及 Python、Node.js、.NET、FFmpeg 或办公工具。多模态功能需 API 凭据及服务额度，会将提示词和参考素材发送到对应服务。项目标为 Beta，配置和接口可能变化；技能指令不保证生成代码可直接投产，仍需测试和审查。

### 开始使用

按 README 在所用智能体中安装 MiniMax Skills，先选定一项开发或文档技能，再按该技能说明补齐依赖。使用素材生成前配置 API 凭据，并检查生成文件和费用。

参阅[官方 README](https://github.com/MiniMax-AI/skills/blob/02853d885acb1abc157477ce00c4d98a8ed14a71/README.md)。

### 收录与来源

把开发方法、参考资料和可调用脚本集中提供给智能体，适合需要结合界面实现与素材制作的任务。已核对前端技能及图像 API 迁移补丁，未运行 API 或验证各技能产出。

维护证据：[图像脚本改用 H3 图像接口，分别构造生成和编辑请求，增加参考图转 data URL、尺寸互斥检查和新版响应解析](https://github.com/MiniMax-AI/skills/commit/3584c0a6f26fc004f3be299c02e134cb9f43e84e)（2026-11-10）。

仓库来自用户于 2026-11-17 提供的办公技能 PDF，已另行核对上游。本条按工程通用标准复核，不设 Star 门槛。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

Provides frontend, full-stack and mobile-development skills for coding agents, alongside document workflows and MiniMax multimodal asset generation.

### Uses and features

- Organizes design, motion, implementation and quality checks through skills for multiple frontend and mobile stacks.
- Includes presentation, Word, PDF and spreadsheet workflows, plus image, video, speech and music skills.
- Multimodal scripts generate assets through MiniMax APIs; image-generation and reference-image editing requests were inspected.

### Requirements and limits

Requires a coding agent that supports local skills. Dependencies vary by skill and may include Python, Node.js, .NET, FFmpeg or office tooling. Multimodal functions require API credentials and quota, and send prompts and reference media to the configured provider. The project is Beta and interfaces may change; skill instructions do not guarantee production-ready generated code, which still requires testing and review.

### Getting started

Install MiniMax Skills for your agent following the README, select a development or document skill and install its dependencies. Configure API credentials before media generation, then review the output and usage charges.

See the [official README](https://github.com/MiniMax-AI/skills/blob/02853d885acb1abc157477ce00c4d98a8ed14a71/README.md).

### Review and provenance

Combines development guidance, references and callable scripts for agents, including tasks that join UI implementation with media creation. The frontend skill and image API migration patch were reviewed; APIs and individual skill outputs were not tested.

Maintenance evidence: [Migrates the image script to H3 generation/edit endpoints, adds reference-image data URLs and mutually exclusive size controls, and parses the new response format](https://github.com/MiniMax-AI/skills/commit/3584c0a6f26fc004f3be299c02e134cb9f43e84e) (2026-11-10).

Identified in an office-skills PDF supplied by the user on 2026-11-17, independently checked against upstream sources and reviewed against the general catalog criteria, with no star threshold.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T06:06:21.880337+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "minimax-skills",
    "name": "MiniMax Skills",
    "repository": "MiniMax-AI/skills",
    "repo_node_id": "R_kgDORpLePg",
    "category": "development",
    "summary": {
      "zh-CN": "为编程智能体提供前端、全栈和移动开发技能，并附带文档处理及 MiniMax 多模态素材生成流程。",
      "en": "Provides frontend, full-stack and mobile-development skills for coding agents, alongside document workflows and MiniMax multimodal asset generation."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T06:06:21.880337+00:00",
        "en": "2026-11-17T06:06:21.880337+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "把开发方法、参考资料和可调用脚本集中提供给智能体，适合需要结合界面实现与素材制作的任务。已核对前端技能及图像 API 迁移补丁，未运行 API 或验证各技能产出。",
      "en": "Combines development guidance, references and callable scripts for agents, including tasks that join UI implementation with media creation. The frontend skill and image API migration patch were reviewed; APIs and individual skill outputs were not tested.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "source_url": "https://github.com/MiniMax-AI/skills/blob/02853d885acb1abc157477ce00c4d98a8ed14a71/LICENSE",
      "license_sha256": "eed4ccce37c2d24822da3bd9d5bee7bc12d494741de56ada513d0b97f537fcd0",
      "source_commit": "02853d885acb1abc157477ce00c4d98a8ed14a71",
      "reviewed_at": "2026-11-17T06:06:21.880337+00:00",
      "evidence_pinned_at": "2026-11-17T06:06:21.880337+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "MIT covers MiniMax-authored repository software and skills. CREDITS.md identifies Apache-2.0 Anthropic-derived visual-art material and MIT-derived community material; these retain their notices. The minimax-docx component has its own MIT notice. External model APIs, dependencies and media retain separate terms.",
      "files": [
        {
          "spdx": "MIT",
          "osi_approved": true,
          "source_url": "https://github.com/MiniMax-AI/skills/blob/02853d885acb1abc157477ce00c4d98a8ed14a71/LICENSE",
          "license_sha256": "eed4ccce37c2d24822da3bd9d5bee7bc12d494741de56ada513d0b97f537fcd0",
          "source_commit": "02853d885acb1abc157477ce00c4d98a8ed14a71",
          "reviewed_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_pinned_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_status": "hash_matched",
          "scope": "MIT covers MiniMax-authored repository software and skills. CREDITS.md identifies Apache-2.0 Anthropic-derived visual-art material and MIT-derived community material; these retain their notices. The minimax-docx component has its own MIT notice. External model APIs, dependencies and media retain separate terms."
        },
        {
          "scope": "Anthropic-derived visual-art content identified by CREDITS.md",
          "spdx": "Apache-2.0",
          "osi_approved": true,
          "source_url": "https://github.com/MiniMax-AI/skills/blob/02853d885acb1abc157477ce00c4d98a8ed14a71/LICENSES/Apache-2.0.txt",
          "license_sha256": "58d1e17ffe5109a7ae296caafcadfdbe6a7d176f0bc4ab01e12a689b0499d8bd",
          "source_commit": "02853d885acb1abc157477ce00c4d98a8ed14a71",
          "reviewed_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_pinned_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_status": "hash_matched"
        },
        {
          "scope": "minimax-docx software",
          "spdx": "MIT",
          "osi_approved": true,
          "source_url": "https://github.com/MiniMax-AI/skills/blob/02853d885acb1abc157477ce00c4d98a8ed14a71/skills/minimax-docx/LICENSE",
          "license_sha256": "8288840186d6d3d6a0b74395e17448c06160b38e796963c7745f579631b47b01",
          "source_commit": "02853d885acb1abc157477ce00c4d98a8ed14a71",
          "reviewed_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_pinned_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_status": "hash_matched"
        }
      ],
      "components": [
        {
          "scope": "Anthropic-derived visual-art content identified by CREDITS.md",
          "spdx": "Apache-2.0",
          "osi_approved": true,
          "source_url": "https://github.com/MiniMax-AI/skills/blob/02853d885acb1abc157477ce00c4d98a8ed14a71/LICENSES/Apache-2.0.txt",
          "license_sha256": "58d1e17ffe5109a7ae296caafcadfdbe6a7d176f0bc4ab01e12a689b0499d8bd",
          "source_commit": "02853d885acb1abc157477ce00c4d98a8ed14a71",
          "reviewed_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_pinned_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_status": "hash_matched"
        },
        {
          "scope": "minimax-docx software",
          "spdx": "MIT",
          "osi_approved": true,
          "source_url": "https://github.com/MiniMax-AI/skills/blob/02853d885acb1abc157477ce00c4d98a8ed14a71/skills/minimax-docx/LICENSE",
          "license_sha256": "8288840186d6d3d6a0b74395e17448c06160b38e796963c7745f579631b47b01",
          "source_commit": "02853d885acb1abc157477ce00c4d98a8ed14a71",
          "reviewed_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_pinned_at": "2026-11-17T05:50:30.044989+00:00",
          "evidence_status": "hash_matched"
        }
      ]
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-10T15:22:16Z",
        "reviewed_at": "2026-11-17T06:06:21.880337+00:00",
        "url": "https://github.com/MiniMax-AI/skills/commit/3584c0a6f26fc004f3be299c02e134cb9f43e84e",
        "qualifies": true,
        "reason": {
          "zh-CN": "图像脚本改用 H3 图像接口，分别构造生成和编辑请求，增加参考图转 data URL、尺寸互斥检查和新版响应解析",
          "en": "Migrates the image script to H3 generation/edit endpoints, adds reference-image data URLs and mutually exclusive size controls, and parses the new response format"
        },
        "reviewed_files": [
          "skills/frontend-dev/scripts/minimax_image.py"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/MiniMax-AI/skills",
        "accessed_at": "2026-11-17T06:06:21.880337+00:00"
      },
      {
        "url": "https://github.com/MiniMax-AI/skills/blob/02853d885acb1abc157477ce00c4d98a8ed14a71/README.md",
        "accessed_at": "2026-11-17T06:06:21.880337+00:00"
      },
      {
        "url": "https://github.com/MiniMax-AI/skills/blob/02853d885acb1abc157477ce00c4d98a8ed14a71/LICENSE",
        "accessed_at": "2026-11-17T06:06:21.880337+00:00"
      },
      {
        "url": "https://github.com/MiniMax-AI/skills/commit/3584c0a6f26fc004f3be299c02e134cb9f43e84e",
        "accessed_at": "2026-11-17T06:06:21.880337+00:00"
      },
      {
        "url": "https://github.com/MiniMax-AI/skills/blob/02853d885acb1abc157477ce00c4d98a8ed14a71/skills/frontend-dev/SKILL.md",
        "accessed_at": "2026-11-17T06:06:21.880337+00:00"
      },
      {
        "url": "https://github.com/MiniMax-AI/skills/blob/02853d885acb1abc157477ce00c4d98a8ed14a71/skills/minimax-docx/LICENSE",
        "accessed_at": "2026-11-17T06:06:21.880337+00:00"
      },
      {
        "url": "https://github.com/MiniMax-AI/skills/blob/02853d885acb1abc157477ce00c4d98a8ed14a71/CREDITS.md",
        "accessed_at": "2026-11-17T06:06:21.880337+00:00"
      },
      {
        "url": "https://github.com/MiniMax-AI/skills/blob/02853d885acb1abc157477ce00c4d98a8ed14a71/LICENSES/Apache-2.0.txt",
        "accessed_at": "2026-11-17T06:06:21.880337+00:00"
      }
    ],
    "discovery": {
      "kind": "user_pdf",
      "submitted_date": "2026-11-17",
      "source_url": "https://github.com/MiniMax-AI/skills",
      "repository_url": "https://github.com/MiniMax-AI/skills",
      "source_title": "办公室 Skill 从夯到拉(纯主观)",
      "source_pages": [
        2
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDORpLePg",
    "full_name": "MiniMax-AI/skills",
    "stargazers_count": 13846,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "api_license_spdx": "MIT",
    "license_sha256": "eed4ccce37c2d24822da3bd9d5bee7bc12d494741de56ada513d0b97f537fcd0",
    "last_success_at": "2026-11-17T05:44:43.140045+00:00"
  }
}
```

</details>
