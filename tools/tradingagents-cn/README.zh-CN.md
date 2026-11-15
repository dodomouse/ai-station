# TradingAgents-CN

简体中文 | [English](README.en.md)

TradingAgents-CN 是面向 A 股的多智能体研究辅助系统。当前默认分支 `v3.0` 为社区版，提供单股研究、主题研究、自然语言筛选、学习课程和模拟交易。它通过多个模型角色组织分析与讨论。

当前保留为参考候选：项目采用混合许可。部分目录为 Apache-2.0，应用层为专有的源码可见组件，不能将整个社区版视为完整开源软件。GitHub 的许可字段为 `NOASSERTION`，现有字典将资格记为 `unknown`。具体限制见下文。

## 适用场景

- 研究多智能体如何组织 A 股分析与观点讨论。
- 通过单股、主题及筛选入口整理研究问题。
- 使用社区版的学习课程、技能管理和纸面交易功能。

## 社区版能力

| 方向 | 官方 README 中的范围 |
| --- | --- |
| 单股研究 | 多角色辩论与五级分析深度，呈现多种情景观点。 |
| 通用研究和筛选 | 自然语言提问、条件筛选和候选股票池。 |
| 智能助手 | 联网搜索、工具调用及项目级记忆。 |
| Skill 中心 | 创建和管理自定义数据获取技能。 |
| 学习与模拟 | 社区课程、学习指南、纸面交易和复盘。 |

官方将自定义 Agent 工作坊、策略系统、定时或批量分析、专业 Word/PDF 导出和高级课程列为 Pro 能力。本词条不把这些能力算作社区版已包含功能。范围以[当前 README](https://github.com/hsliuping/TradingAgents-CN/blob/51060a7682cf51810b4bc3a704829438d18cd8dc/README.md)为准。

## 环境、费用与限制

- README 的部署基线是 Python 3.11、Node.js 18+、MongoDB 7.0+ 和 Redis 6+。数据库需自行准备。
- 后端使用 FastAPI，前端使用 Vue 3。需要配置数据库连接、认证参数和模型服务。
- `pyproject.toml` 的 Python 下限为 `>=3.10`，与 README 的 3.11 基线不同。本次未验证较低版本兼容性，入门步骤沿用 README。
- 模型 API、行情数据访问、服务器和数据库可能产生费用。社区版源码可见不代表外部服务免费。
- 当前 README 将市场范围限定为 A 股。不能根据旧版本介绍或依赖列表推定其他市场已受支持。
- 模拟交易不等于券商实盘执行。上游将输出定位为学习和研究参考，不提供目标价或买卖时机指令。
- 本次未验证行情质量、报告准确性、研究效果或投资收益。

## 许可范围

按[根 LICENSE 的分层声明](https://github.com/hsliuping/TradingAgents-CN/blob/51060a7682cf51810b4bc3a704829438d18cd8dc/LICENSE)：

| 范围 | 许可说明 |
| --- | --- |
| `tradingagents/`、`cli/`、`docs/`、`tests/`、`web/`及根配置 | 适用 Apache-2.0。 |
| `app/`、`frontend/`、`core/` | 专有、源码可见；允许个人使用、评估和教育用途，限制再分发及商业使用。 |

商业许可需按上游说明另行取得。此处整理许可证声明，不替任何具体使用场景作授权判断。

## 开始使用

1. 阅读社区版 [README](https://github.com/hsliuping/TradingAgents-CN/tree/v3.0#readme)和[许可范围](https://github.com/hsliuping/TradingAgents-CN/blob/v3.0/LICENSE)，确认版本与用途。
2. 按文档准备 Python、Node.js、MongoDB 和 Redis。
3. 在自己的环境中填写 `.env` 配置，再按官方步骤启动前后端。
4. 登录后配置模型服务及所需数据源，从一个研究问题开始检查输出。

本次未克隆运行应用、配置凭据、调用模型或执行模拟交易。

## 相关选择

- [Vibe Research](../vibe-research/README.zh-CN.md)侧重自选、持仓、报告库及研究工作台，可按工作流需求比较。
- [AI Berkshire](../ai-berkshire/README.zh-CN.md)是依托编码助手运行的研究技能，部署方式不同。
- [easyquotation](../easyquotation/README.zh-CN.md)是行情读取库，适合程序接入，不提供上述完整研究界面。

以上不代表功能等价或已验证集成。

## 复核说明

2026-11-15 核对默认分支、README、分层许可证、Python 包声明和 2026-09-22 的社区版首发提交。该提交包含应用启动和模型能力配置代码，属于窗口内的功能发布。仓库较新的推送时间未替代这条证据。

验证级别为 `docs`。本次只阅读文档与选定源码，候选原因是许可范围。来源和指纹见 [tool.json](tool.json)，Star 与仓库状态见 [GitHub 快照](../../data/github/tradingagents-cn.json)。
