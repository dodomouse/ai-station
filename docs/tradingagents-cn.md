# TradingAgents-CN

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[hsliuping/TradingAgents-CN](https://github.com/hsliuping/TradingAgents-CN)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 数据处理 / Data processing |
| 状态 / Status | 候选 / Candidate |
| Star | 32957 |
| 许可证 / License | 混合许可，含专有组件 / Mixed, includes proprietary components |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T11:46:22.824Z |

候选原因：应用层采用专有许可。
Candidate reason: Proprietary application layer.

状态整理：2026-11-17，依据已有证据区分当前待办与历史结论；未重新完成全部准入复核，Star 与快照日期保持原值。
Status clarified on 2026-11-17 from existing evidence; this is not a complete new eligibility review. Stars and snapshot dates retain their original values.

下一步：仅作参考线索保留；许可改变或可独立收录的开放组件明确后再评估。
Next step: Retain as a reference lead; reassess if the license changes or a separately includable open component is established.

历史资格见[收录依据](#review-evidence)中的 `eligibility_history`。 / Earlier decisions are retained in `eligibility_history` in the [review evidence](#review-evidence).

## 中文

TradingAgents-CN 是面向 A 股的多智能体研究辅助系统。当前默认分支 `v3.0` 为社区版，提供单股研究、主题研究、自然语言筛选、学习课程和模拟交易。它通过多个模型角色组织分析与讨论。

当前保留为参考候选：项目采用混合许可。部分目录为 Apache-2.0，应用层为专有的源码可见组件，不能将整个社区版视为完整开源软件。GitHub 的许可字段为 `NOASSERTION`；本词条依据已记录的专有应用层范围，将整体资格记为 `ineligible`，仅作参考线索保留。具体限制见下文。

### 适用场景

- 研究多智能体如何组织 A 股分析与观点讨论。
- 通过单股、主题及筛选入口整理研究问题。
- 使用社区版的学习课程、技能管理和纸面交易功能。

### 社区版能力

| 方向 | 官方 README 中的范围 |
| --- | --- |
| 单股研究 | 多角色辩论与五级分析深度，呈现多种情景观点。 |
| 通用研究和筛选 | 自然语言提问、条件筛选和候选股票池。 |
| 智能助手 | 联网搜索、工具调用及项目级记忆。 |
| Skill 中心 | 创建和管理自定义数据获取技能。 |
| 学习与模拟 | 社区课程、学习指南、纸面交易和复盘。 |

官方将自定义 Agent 工作坊、策略系统、定时或批量分析、专业 Word/PDF 导出和高级课程列为 Pro 能力。本词条不把这些能力算作社区版已包含功能。范围以[当前 README](https://github.com/hsliuping/TradingAgents-CN/blob/51060a7682cf51810b4bc3a704829438d18cd8dc/README.md)为准。

### 环境、费用与限制

- README 的部署基线是 Python 3.11、Node.js 18+、MongoDB 7.0+ 和 Redis 6+。数据库需自行准备。
- 后端使用 FastAPI，前端使用 Vue 3。需要配置数据库连接、认证参数和模型服务。
- `pyproject.toml` 的 Python 下限为 `>=3.10`，与 README 的 3.11 基线不同。本次未验证较低版本兼容性，入门步骤沿用 README。
- 模型 API、行情数据访问、服务器和数据库可能产生费用。社区版源码可见不代表外部服务免费。
- 当前 README 将市场范围限定为 A 股。不能根据旧版本介绍或依赖列表推定其他市场已受支持。
- 模拟交易不等于券商实盘执行。上游将输出定位为学习和研究参考，不提供目标价或买卖时机指令。
- 本次未验证行情质量、报告准确性、研究效果或投资收益。

### 许可范围

按[根 LICENSE 的分层声明](https://github.com/hsliuping/TradingAgents-CN/blob/51060a7682cf51810b4bc3a704829438d18cd8dc/LICENSE)：

| 范围 | 许可说明 |
| --- | --- |
| `tradingagents/`、`cli/`、`docs/`、`tests/`、`web/`及根配置 | 适用 Apache-2.0。 |
| `app/`、`frontend/`、`core/` | 专有、源码可见；允许个人使用、评估和教育用途，限制再分发及商业使用。 |

商业许可需按上游说明另行取得。此处整理许可证声明，不替任何具体使用场景作授权判断。

### 开始使用

1. 阅读社区版 [README](https://github.com/hsliuping/TradingAgents-CN/tree/v3.0#readme)和[许可范围](https://github.com/hsliuping/TradingAgents-CN/blob/v3.0/LICENSE)，确认版本与用途。
2. 按文档准备 Python、Node.js、MongoDB 和 Redis。
3. 在自己的环境中填写 `.env` 配置，再按官方步骤启动前后端。
4. 登录后配置模型服务及所需数据源，从一个研究问题开始检查输出。

本次未克隆运行应用、配置凭据、调用模型或执行模拟交易。

### 相关选择

- [Vibe Research](vibe-research.md#中文)侧重自选、持仓、报告库及研究工作台，可按工作流需求比较。
- [AI Berkshire](ai-berkshire.md#中文)是依托编码助手运行的研究技能，部署方式不同。
- [easyquotation](easyquotation.md#中文)是行情读取库，适合程序接入，不提供上述完整研究界面。

以上不代表功能等价或已验证集成。

### 复核说明

2026-11-15 核对默认分支、README、分层许可证、Python 包声明和 2026-09-22 的社区版首发提交。该提交包含应用启动和模型能力配置代码，属于窗口内的功能发布。仓库较新的推送时间未替代这条证据。

验证级别为 `docs`。本次只阅读文档与选定源码，候选原因是许可范围。来源和指纹见 [收录依据](#review-evidence)，Star 与仓库状态见 [GitHub 快照](#review-evidence)。

## English

TradingAgents-CN is a multi-agent research assistant for Chinese A-shares. Its current default branch, `v3.0`, is the Community Edition, with single-stock research, topic research, natural-language screening, learning material and paper trading. Several model roles organize analysis and discussion.

This entry remains a reference candidate because licensing differs by component. Some directories use Apache-2.0, while the application layer is proprietary source-available code. The complete Community Edition therefore cannot be described as wholly open-source software. GitHub reports `NOASSERTION`; the documented proprietary application scope makes the complete application `ineligible`, retained only as a reference lead.

### Use cases

- Study how multiple agents organize A-share analysis and debate.
- Structure research questions through stock, topic and screening workflows.
- Explore the Community Edition's courses, skill management and paper trading.

### Community features

| Area | Scope described by the official README |
| --- | --- |
| Single-stock research | Multiple analyst roles, debate, five analysis-depth levels and scenario-based views. |
| General research and screening | Natural-language questions, condition-based screening and candidate stock pools. |
| Assistant | Web search, tool calls and project-level memory. |
| Skill center | Creation and management of custom data-retrieval skills. |
| Learning and simulation | Community courses, guides, paper trading and review. |

The project lists the custom Agent workshop, strategy system, scheduled or batch analysis, professional Word/PDF exports and advanced courses as Pro features. They are not counted as Community features here. See the [current README](https://github.com/hsliuping/TradingAgents-CN/blob/51060a7682cf51810b4bc3a704829438d18cd8dc/README.md).

### Requirements, costs and limits

- The README specifies Python 3.11, Node.js 18+, MongoDB 7.0+ and Redis 6+. Databases must be installed separately.
- The backend uses FastAPI and the frontend Vue 3. Database connections, authentication settings and model services require configuration.
- `pyproject.toml` declares Python `>=3.10`, which differs from the README's 3.11 baseline. Lower-version compatibility was not tested; the starting instructions here follow the README.
- Model APIs, data access, hosting and databases can incur separate costs. Source availability does not make those services free.
- The current README limits the supported research market to A-shares. Older descriptions or installed dependencies do not establish support for other markets.
- Paper trading does not establish live brokerage execution. The project frames output as learning and research material and excludes target-price or trade-timing instructions.
- Data quality, report accuracy, research effectiveness and investment returns were not validated here.

### License scope

The [root license](https://github.com/hsliuping/TradingAgents-CN/blob/51060a7682cf51810b4bc3a704829438d18cd8dc/LICENSE) separates two groups:

| Scope | Stated terms |
| --- | --- |
| `tradingagents/`, `cli/`, `docs/`, `tests/`, `web/` and root configuration | Apache-2.0. |
| `app/`, `frontend/` and `core/` | Proprietary source-available components allowing personal use, evaluation and education, with redistribution and commercial-use restrictions. |

Commercial permission must be obtained separately under the upstream terms. This is a summary of the project's statements, not authorization for a particular use.

### Getting started

1. Read the Community [README](https://github.com/hsliuping/TradingAgents-CN/tree/v3.0#readme) and [license scope](https://github.com/hsliuping/TradingAgents-CN/blob/v3.0/LICENSE) for the intended version and use.
2. Prepare Python, Node.js, MongoDB and Redis as documented.
3. Configure `.env` in your own environment and follow the upstream frontend/backend startup steps.
4. After login, configure model access and required data sources, then inspect the output from one research question.

This import did not run the application, configure credentials, call models or execute paper trades.

### Related choices

- [Vibe Research](vibe-research.md#english) focuses on watchlists, holdings, report storage and research workflows.
- [AI Berkshire](ai-berkshire.md#english) supplies research skills for coding assistants and has a different setup model.
- [easyquotation](easyquotation.md#english) retrieves market data inside Python programs without the full research interface described above.

These comparisons do not establish feature parity or tested integration.

### Review

On 2026-11-15, this review checked the default branch, README, component licenses, Python package declaration and the Community Edition's 2026-09-22 initial commit. That commit includes application startup and model-capability configuration code, providing functional activity within the window. A newer repository push date is not used as a substitute.

Verification level: `docs`. Only documentation and selected code were inspected; license scope keeps the entry outside the default catalog. See [shared metadata](#review-evidence) and the [GitHub snapshot](#review-evidence).

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
      "license_not_approved"
    ],
    "reviewed_at": "2026-11-17T03:11:46.178386+00:00",
    "review_basis": "existing_evidence_status_clarification",
    "pending_actions": {
      "zh-CN": [
        "仅作参考线索保留；许可改变或可独立收录的开放组件明确后再评估。"
      ],
      "en": [
        "Retain as a reference lead; reassess if the license changes or a separately includable open component is established."
      ]
    }
  },
  "metadata": {
    "schema_version": 1,
    "id": "tradingagents-cn",
    "name": "TradingAgents-CN",
    "repository": "hsliuping/TradingAgents-CN",
    "repo_node_id": "R_kgDOPCHzDw",
    "category": "data",
    "tags": [
      "agents",
      "finance",
      "research",
      "source-available"
    ],
    "forms": [
      "web"
    ],
    "platforms": [
      "linux",
      "macos",
      "windows"
    ],
    "aliases": {
      "zh-CN": [
        "TradingAgents 中文社区版",
        "多智能体 A 股研究"
      ],
      "en": [
        "TradingAgents-CN Community Edition"
      ]
    },
    "summary": {
      "zh-CN": "面向 A 股的多智能体研究辅助系统，社区版提供研究、筛选、课程和模拟交易；应用层采用专有许可。",
      "en": "A multi-agent A-share research assistant with screening, courses and paper trading; its Community Edition includes a proprietary application layer."
    },
    "use_cases": {
      "zh-CN": [
        "研究多智能体组织 A 股分析与讨论的流程",
        "通过单股、主题及筛选入口整理研究问题",
        "探索社区版学习课程、技能管理和模拟交易"
      ],
      "en": [
        "Study multi-agent A-share research workflows",
        "Structure questions through stock, topic and screening tools",
        "Explore community courses, skill management and paper trading"
      ]
    },
    "alternatives": [
      "vibe-research",
      "ai-berkshire",
      "easyquotation"
    ],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-15T11:54:08.129868Z",
        "en": "2026-11-15T11:54:08.129868Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": null,
      "osi_approved": false,
      "license_sha256": "c14aadbd32d79d1cb3d8a8d720bc319f2d5020e9c56a2ddaa794e75d0f7e2164",
      "source_url": "https://github.com/hsliuping/TradingAgents-CN/blob/51060a7682cf51810b4bc3a704829438d18cd8dc/LICENSE",
      "reviewed_at": "2026-11-15T11:54:08.129868Z",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "51060a7682cf51810b4bc3a704829438d18cd8dc"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-09-22T12:10:31Z",
        "reviewed_at": "2026-11-15T11:54:08.129868Z",
        "url": "https://github.com/hsliuping/TradingAgents-CN/commit/51060a7682cf51810b4bc3a704829438d18cd8dc",
        "qualifies": true,
        "reason": {
          "zh-CN": "社区版首发提交新增应用启动和模型能力配置代码。已抽查提交中的实现差异，属于窗口内功能发布；未运行研究或交易。",
          "en": "The Community Edition initial commit adds application startup and model-capability code. Selected implementation diffs confirm a functional introduction in the window; research and trading were not executed."
        }
      }
    ],
    "sources": [
      {
        "url": "https://github.com/hsliuping/TradingAgents-CN/blob/51060a7682cf51810b4bc3a704829438d18cd8dc/README.md",
        "accessed_at": "2026-11-15T11:54:08.129868Z",
        "supports": {
          "zh-CN": "官方用途、功能范围、入门和限制。",
          "en": "Official purpose, feature scope, setup and limitations."
        }
      },
      {
        "url": "https://github.com/hsliuping/TradingAgents-CN/blob/51060a7682cf51810b4bc3a704829438d18cd8dc/LICENSE",
        "accessed_at": "2026-11-15T11:54:08.129868Z",
        "supports": {
          "zh-CN": "当前根许可证及适用范围。",
          "en": "Current root license and its scope."
        }
      },
      {
        "url": "https://api.github.com/repos/hsliuping/TradingAgents-CN",
        "accessed_at": "2026-11-15T11:46:22.824Z",
        "supports": {
          "zh-CN": "本次仓库身份、Star 和公开状态。",
          "en": "Repository identity, Stars and public state at review time."
        }
      },
      {
        "url": "https://github.com/hsliuping/TradingAgents-CN/blob/51060a7682cf51810b4bc3a704829438d18cd8dc/pyproject.toml",
        "accessed_at": "2026-11-15T11:54:08.129868Z",
        "supports": {
          "zh-CN": "Python 包声明与 README 部署基线的区别。",
          "en": "Difference between the package Python declaration and README deployment baseline."
        }
      }
    ],
    "catalog_review": {
      "reviewed_at": "2026-11-15T11:54:08.129868Z",
      "notes": {
        "zh-CN": "v3.0 社区版为 Apache-2.0 与专有应用层混合许可，整库不满足完整开源口径。API 返回 NOASSERTION，现有资格计算为 unknown；限制来自明确许可声明，而非仅由 API 标签推断。",
        "en": "v3.0 combines Apache-2.0 components with a proprietary application layer. API NOASSERTION yields unknown under the current gate; restrictions are established by the license text, not inferred from the API label alone."
      },
      "historical": true
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOPCHzDw",
    "full_name": "hsliuping/TradingAgents-CN",
    "stargazers_count": 32957,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "NOASSERTION",
    "license_sha256": "c14aadbd32d79d1cb3d8a8d720bc319f2d5020e9c56a2ddaa794e75d0f7e2164",
    "last_success_at": "2026-11-15T11:46:22.824Z"
  },
  "eligibility_history": [
    {
      "evaluated_at": "2026-11-15T11:54:08.129868Z",
      "status": "unknown",
      "reasons": [
        "license_needs_review"
      ]
    }
  ]
}
```

</details>
