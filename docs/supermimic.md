# SuperMimic

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[HybridRobotics/supermimic](https://github.com/HybridRobotics/supermimic)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 1646 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:30:19.931551Z |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:27:09.986Z |

## 中文

### 用途与功能

面向人形机器人的动作跟踪研究实现。使用可微世界模型训练全身动作控制策略。

提供宇树 G1 的两种坐标表示任务、训练和回放入口。适合机器人学习方法研究。

### 环境与限制

需要 Python/uv 环境、配套 mjlab_research 仓库及适合训练的 GPU 和数据。开源训练代码不等于可直接部署到真实机器人。论文和演示效果未在本轮复现。

### 入门与收录判断

从[官方 README](https://github.com/HybridRobotics/supermimic/blob/main/README.md)查阅安装和使用步骤。公开训练与回放实现，并明确任务类型，适合研究者复核方法。

本轮为文档复核，未安装、运行或测试上游项目。2026-11-16 删除数据采集中的动作噪声，修改训练配置和运行器实现。详见[维护记录](https://github.com/HybridRobotics/supermimic/commit/5f69628350940d7eb1968184eda449b3d8d18b8d)。

### 文章来源

发现于“逛逛GitHub”在 2026-11-16 发布的[《8 个开源工具速览》](https://www.woshipm.com/ai/6494405.html)。已读取作者署名正文，功能和限制另按当前上游复核。

## English

### Purpose and features

A humanoid motion-tracking research implementation that trains whole-body control with a differentiable world model.

Provides two coordinate-representation tasks for Unitree G1, with training and playback entry points.

### Requirements and limits

Requires Python/uv, the companion mjlab_research repository, suitable GPU resources and data. The training code does not establish readiness for deployment on physical robots. Paper results were not reproduced.

### Getting started and review

Use the [official README](https://github.com/HybridRobotics/supermimic/blob/main/README.md) for installation and usage. This is a documentation review; the software was not installed or tested. The 2026-11-16 change removes action noise from data collection in the learner configuration and runner. See the [activity evidence](https://github.com/HybridRobotics/supermimic/commit/5f69628350940d7eb1968184eda449b3d8d18b8d).

The project appears in the account's [author-published article dated 2026-11-16](https://www.woshipm.com/ai/6494405.html). Current upstream documentation supports the feature descriptions.

## Review evidence

```json
{
  "evaluated_at": "2026-11-16T14:30:19.931551Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "supermimic",
    "name": "SuperMimic",
    "repository": "HybridRobotics/supermimic",
    "repo_node_id": "R_kgDOVpPffg",
    "category": "ai",
    "summary": {
      "zh-CN": "面向人形机器人的动作跟踪研究实现。使用可微世界模型训练全身动作控制策略。",
      "en": "A humanoid motion-tracking research implementation that trains whole-body control with a differentiable world model."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:30:19.931551Z",
        "en": "2026-11-16T14:30:19.931551Z"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "basis": "公开训练与回放实现，并明确任务类型，适合研究者复核方法。",
      "rationale": "公开训练与回放实现，并明确任务类型，适合研究者复核方法。",
      "stars_are_advisory": true,
      "reviewed_at": "2026-11-16T14:30:19.931551Z"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
      "source_url": "https://github.com/HybridRobotics/supermimic/blob/main/LICENSE",
      "reviewed_at": "2026-11-16T14:30:19.931551Z"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-16T11:37:59Z",
        "reviewed_at": "2026-11-16T14:30:19.931551Z",
        "url": "https://github.com/HybridRobotics/supermimic/commit/5f69628350940d7eb1968184eda449b3d8d18b8d",
        "qualifies": true,
        "reason": {
          "zh-CN": "2026-11-16 删除数据采集中的动作噪声，修改训练配置和运行器实现。",
          "en": "The 2026-11-16 change removes action noise from data collection in the learner configuration and runner."
        },
        "reviewed_files": [
          "src/supermimic/learners/policy_learner.py",
          "src/supermimic/runners/supermimic_runner.py"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/HybridRobotics/supermimic",
        "accessed_at": "2026-11-16T14:27:09.986Z",
        "supports": "Repository identity, Stars and public state."
      },
      {
        "url": "https://github.com/HybridRobotics/supermimic/blob/main/README.md",
        "accessed_at": "2026-11-16T14:30:19.931551Z",
        "supports": "Capabilities, requirements and limits."
      },
      {
        "url": "https://www.woshipm.com/ai/6494405.html",
        "published_date": "2026-11-16",
        "accessed_at": "2026-11-16T14:30:19.931551Z",
        "supports": "Author-published article body and account attribution."
      }
    ],
    "discovery": {
      "account": "逛逛GitHub",
      "article_url": "https://www.woshipm.com/ai/6494405.html",
      "published_date": "2026-11-16",
      "body_verification": "author_published_article"
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVpPffg",
    "full_name": "HybridRobotics/supermimic",
    "stargazers_count": 1646,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
    "last_success_at": "2026-11-16T14:27:09.986Z"
  }
}
```
