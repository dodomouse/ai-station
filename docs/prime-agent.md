# Prime Agent

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[PrimeIntellect-ai/prime-agent](https://github.com/PrimeIntellect-ai/prime-agent)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 22746 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:47:41.714Z |

## 中文

以持久Python环境、子智能体和后台会话执行编码与研究任务。

### 用途与功能

- 组织长期编码或研究任务

通过程序调用工具和子智能体，保存会话、记忆与可回滚的流程改进；提供daemon重连和状态命令。

### 环境与限制

需要可用模型提供商与当前目录权限。模型生成的Python和Shell按用户权限执行，worker隔离不是安全沙箱。平台和MCP服务依赖各自环境；后台任务会继续消耗资源。

### 开始使用

按README安装，选择可检查和恢复的项目目录，再配置提供商启动会话。 参阅[官方 README](https://github.com/PrimeIntellect-ai/prime-agent/blob/main/README.md)。

### 收录与来源

具备持久执行、后台生命周期和子智能体实现，适合需要程序化编排的任务。 最近维护：[实现提交](https://github.com/PrimeIntellect-ai/prime-agent/commit/ad1613303dff0c642b9a95706678559356086107)（2026-11-13T19:31:26Z）。已核对Rust实现：把仍在运行或待通知的后台bash任务计入静止状态，防止过早结束环境。

通过逛逛GitHub的第三方文章索引发现。索引记录了下列文章；本次未读取微信原文，不据此声称已阅读全文。

- 2026-08-22：[推荐关注一下这个刚开源的自进化 Agent ，登上 GitHub 热榜了都。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536098&idx=1&sn=f5d705af93475ffc2faa1d42915a7d61)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。

## English

Executes coding and research tasks through a persistent Python environment, subagents and background sessions.

### Uses and features

- Coordinate long-running coding or research

Calls tools and subagents programmatically, stores sessions, memory and reversible workflow refinements, and provides daemon reconnection and status commands.

### Requirements and limits

Needs a usable model provider and access to the working directory. Generated Python and shell commands run with user privileges; worker isolation is not a security sandbox. Platforms and MCP services have separate requirements, and background jobs continue consuming resources.

### Getting started

Install as documented, choose a project directory whose changes can be inspected and restored, then configure a provider and start a session. See the [official README](https://github.com/PrimeIntellect-ai/prime-agent/blob/main/README.md).

### Review and provenance

Implements persistent execution, background lifecycle and subagents for programmatic orchestration. Recent maintenance: [implementation commit](https://github.com/PrimeIntellect-ai/prime-agent/commit/ad1613303dff0c642b9a95706678559356086107) (2026-11-13T19:31:26Z). Reviewed Rust changes that count running or pending-notification background bash jobs in quiescence, preventing premature teardown.

Discovered through a third-party index of 逛逛GitHub articles. The index records the articles below; the original WeChat pages were not read in this review. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:47:41.714Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "prime-agent",
    "name": "Prime Agent",
    "repository": "PrimeIntellect-ai/prime-agent",
    "repo_node_id": "R_kgDOSXZbXg",
    "category": "ai",
    "tags": [],
    "forms": [
      "cli",
      "service"
    ],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "Prime Agent"
      ],
      "en": [
        "Prime Agent"
      ]
    },
    "summary": {
      "zh-CN": "以持久Python环境、子智能体和后台会话执行编码与研究任务。",
      "en": "Executes coding and research tasks through a persistent Python environment, subagents and background sessions."
    },
    "use_cases": {
      "zh-CN": [
        "组织长期编码或研究任务"
      ],
      "en": [
        "Coordinate long-running coding or research"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:47:41.714Z",
        "en": "2026-11-16T14:47:41.714Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "e0d1bf8d137e6d56e98ee968402b0b7f324c5c85ea505e4fd7b6b78615bc4e7a",
      "source_url": "https://github.com/PrimeIntellect-ai/prime-agent/blob/ad1613303dff0c642b9a95706678559356086107/LICENSE",
      "reviewed_at": "2026-11-16T14:47:41.714Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "ad1613303dff0c642b9a95706678559356086107"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/PrimeIntellect-ai/prime-agent/commit/ad1613303dff0c642b9a95706678559356086107",
        "occurred_at": "2026-11-13T19:31:26Z",
        "reason": {
          "zh-CN": "已核对Rust实现：把仍在运行或待通知的后台bash任务计入静止状态，防止过早结束环境。",
          "en": "Reviewed Rust changes that count running or pending-notification background bash jobs in quiescence, preventing premature teardown."
        },
        "reviewed_at": "2026-11-16T14:47:41.714Z",
        "qualifies": true
      }
    ],
    "sources": [
      {
        "url": "https://github.com/PrimeIntellect-ai/prime-agent/blob/main/README.md",
        "accessed_at": "2026-11-16T14:47:41.714Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/PrimeIntellect-ai/prime-agent/blob/ad1613303dff0c642b9a95706678559356086107/LICENSE",
        "accessed_at": "2026-11-16T14:47:41.714Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.noking.tech/github-radar/data/library.json",
        "accessed_at": "2026-11-16T14:47:41.714Z",
        "supports": {
          "zh-CN": "第三方索引中的公众号文章归属、时间与项目发现线索；非原文阅读证据。",
          "en": "Third-party account attribution, article dates and discovery leads; not proof of reading the originals."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536098&idx=1&sn=f5d705af93475ffc2faa1d42915a7d61",
        "accessed_at": "2026-11-16T14:47:41.714Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-08-22 推荐关注一下这个刚开源的自进化 Agent ，登上 GitHub 热榜了都。；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-08-22; not directly read in this review."
        }
      }
    ],
    "quality_review": {
      "basis": {
        "zh-CN": "具备持久执行、后台生命周期和子智能体实现，适合需要程序化编排的任务。",
        "en": "Implements persistent execution, background lifecycle and subagents for programmatic orchestration."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOSXZbXg",
    "full_name": "PrimeIntellect-ai/prime-agent",
    "stargazers_count": 22746,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "e0d1bf8d137e6d56e98ee968402b0b7f324c5c85ea505e4fd7b6b78615bc4e7a",
    "last_success_at": "2026-11-16T14:20:19.446Z"
  }
}
```

</details>

