# AI Berkshire

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 数据处理 / Data processing |
| 状态 / Status | 已收录 / Included |
| Star | 17140 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T10:48:17.763Z |

以上为历史核对结果，使用前请复核上游状态。 / This is a dated review; check the current upstream state before use.

## 中文

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

### 原始中文记录（历史快照）

### 028 AI Berkshire

仓库：[xbtlin/ai-berkshire](https://github.com/xbtlin/ai-berkshire)

#### 1. 简介

基于 Claude Code 与 Codex 的价值投资研究技能。通过多个分析视角组织公司研究、财报、估值、组合复盘和论点跟踪。

#### 2. 适用场景

组织上市公司深度研究。精读财报与复核估值。并行比较多个分析视角。跟踪投资论点和组合变化。

#### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 公司与估值研究 | 提供公司深研、内在价值、现金流、SOTP和反向估值等入口。 | Skills 一览 / 深度研究类 |
| 多视角并行研究 | 团队型技能调度多个投资方法视角独立研究并互相挑战。 | 整体架构 / 多Agent并行 |
| 财报精读 | earnings-review强调阅读原始财报，团队入口可组织多视角精读。 | 财报分析类 |
| 行业与初筛 | 提供行业研究、漏斗筛选、质量筛选及买入前检查表。 | 行业筛选类 |
| 组合与论点跟踪 | 覆盖组合复盘、投资论点持续跟踪和两份报告的漂移检查。 | 持仓管理类 |
| 数据核对规范 | 提供财务数据获取、独立来源交叉核对和精确计算规范。 | 金融数据的精确性 / 思维工具类 |
| Claude Code和Codex入口 | 同一工作流提供Claude Code commands与Codex skills。 | 快速开始 |

官方来源入口：[官方 README](https://github.com/xbtlin/ai-berkshire/blob/main/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

**平台与环境**

- 取决于Claude Code/Codex运行环境；README含macOS、Linux、Windows安装指引

- MIT开源；需要用户自己的AI客户端及模型服务。
- README明确深度投研多轮、多Agent流程token消耗较高。
- 较强模型与更完整研究可能增加成本，不是免费投研算力。

- 多视角是提示与工作流设计，不能当成大师本人背书。
- README展示的历史收益、质量宣传和部分客户端能力未独立核实。
- 未运行任何研究或投资评估，报告不是确定性收益保证。

**容易找错的需求（不属于本项目能力）**

- 照着输出交易就能复制作者宣传的收益率。
- 无需数据或模型额度就能免费自动理财。

#### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/xbtlin/ai-berkshire/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- Claude Code commands
- Codex skills
- 计算、检索、报告抽检工具

#### 6. 替代选择

- [simonlin1212/Vibe-Research](vibe-research.md#中文)：本项目以多个分析视角组织公司研究；后者另含自选、持仓、研报库和历史回测。

#### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/xbtlin/ai-berkshire/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/028_xbtlin-ai-berkshire.md`。

## English

Agent skills for company research, financial statements, valuation and tracking investment theses from multiple perspectives.

### Use cases

- Structure company research
- Keep a portfolio thesis and evidence record

### Requirements and limits

Needs the user's coding assistant and model services. Multi-agent research can consume substantial tokens. Named investor perspectives are workflow prompts, not endorsements. Historical returns and quality claims were not independently checked, and outputs do not guarantee investment results.

### Getting started

Read the [official documentation](https://github.com/xbtlin/ai-berkshire/blob/main/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [Vibe Research](vibe-research.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:17.763Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

保留原始核对数据，便于追溯来源、许可和维护证据。 / Original review data preserves source, license and maintenance evidence.

```json
{
  "evaluated_at": "2026-11-15T11:54:08.129868Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "ai-berkshire",
    "name": "AI Berkshire",
    "repository": "xbtlin/ai-berkshire",
    "repo_node_id": "R_kgDOR8AxgA",
    "category": "data",
    "tags": [
      "agent-skill",
      "finance",
      "research"
    ],
    "forms": [],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "AI Berkshire"
      ],
      "en": [
        "AI Berkshire"
      ]
    },
    "summary": {
      "zh-CN": "基于 Claude Code 与 Codex 的价值投资研究技能。通过多个分析视角组织公司研究、财报、估值、组合复盘和论点跟踪。",
      "en": "Agent skills for company research, financial statements, valuation and tracking investment theses from multiple perspectives."
    },
    "use_cases": {
      "zh-CN": [
        "组织上市公司深度研究。精读财报与复核估值。并行比较多个分析视角。跟踪投资论点和组合变化。"
      ],
      "en": [
        "Structure company research",
        "Keep a portfolio thesis and evidence record"
      ]
    },
    "alternatives": [
      "vibe-research"
    ],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-15T11:03:50.120930Z",
        "en": "2026-11-15T11:03:50.120930Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "81b843bec8a087f4c20e5be8ad744cfe1a169dc0b4f0147cbe61e6cd3da39981",
      "source_url": "https://github.com/xbtlin/ai-berkshire/blob/bea57d5e72aad7def1c34ed5b2b1598039de41cf/LICENSE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "bea57d5e72aad7def1c34ed5b2b1598039de41cf"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-14T16:44:18Z",
        "reviewed_at": "2026-11-15T11:03:50.120930Z",
        "url": "https://github.com/xbtlin/ai-berkshire/commit/bea57d5e72aad7def1c34ed5b2b1598039de41cf",
        "qualifies": true,
        "reason": {
          "zh-CN": "新增交互课程和测验程序。已核对提交中的实现文件与差异；未运行上游测试。",
          "en": "Adds interactive course and quiz code. Reviewed implementation changes; upstream tests were not run."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/xbtlin/ai-berkshire",
        "accessed_at": "2026-11-15T10:48:17.763Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/xbtlin/ai-berkshire/blob/main/README.md",
        "accessed_at": "2026-11-15T10:54:03.147Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      },
      {
        "url": "https://github.com/xbtlin/ai-berkshire/blob/bea57d5e72aad7def1c34ed5b2b1598039de41cf/LICENSE",
        "accessed_at": "2026-11-15T10:53:12.039Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "028",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "238f145bb8450f0e79ba036e3b8d4bea0885af6cb257f9d9e5db3555a2374b31",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "agent-skill",
      "pending_reasons": [],
      "english_scope": "editorial_digest",
      "source_card_preserved": true
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOR8AxgA",
    "full_name": "xbtlin/ai-berkshire",
    "stargazers_count": 17140,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "81b843bec8a087f4c20e5be8ad744cfe1a169dc0b4f0147cbe61e6cd3da39981",
    "last_success_at": "2026-11-15T10:48:17.763Z"
  }
}
```

</details>
