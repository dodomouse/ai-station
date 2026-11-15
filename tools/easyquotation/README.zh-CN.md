# easyquotation

简体中文 | [English](README.en.md)

easyquotation 是读取股票行情的 Python 库。它封装新浪、腾讯和集思录的部分数据接口，向脚本返回行情字典。适合已有 Python 程序、只需要增加行情读取能力的用户。

当前保留为候选：默认分支最近提交为 2026-02-28 的文档更新，本次未发现三个月内的有效维护证据。Star 已达到门槛，具体数据见 [GitHub 快照](../../data/github/easyquotation.json)。

## 适用场景

- 在 Python 脚本中读取单只、多只或全市场的行情快照。
- 获取文档列出的腾讯港股行情和日 K 线。
- 按数据源的访问条件读取集思录指数 ETF 数据。

## 主要功能

| 接口 | 官方文档描述的用途 |
| --- | --- |
| `easyquotation.use()` | 选择新浪、腾讯、港股、日 K 线或集思录适配器。 |
| `market_snapshot(prefix=True)` | 读取市场快照，并保留股票代码的市场前缀。 |
| `real()` | 请求一个或多个代码；指数和股票代码重合时需注意市场前缀。 |
| `update_stock_codes()` | 更新本地使用的全市场股票代码。 |
| `etfindex()` | 通过集思录适配器查询指数 ETF；文档注明不含黄金和货币 ETF。 |

接口范围来自[官方 README](https://github.com/shidenggui/easyquotation/blob/7778c1b9f93afb2ce2cf431de393fe690d4ec07c/README.md)。本次没有请求实际行情，不能据此保证各适配器目前均可用。

## 环境与限制

- 仓库的 `setup.py` 声明 Python `>=3.6`，主要运行依赖为 `requests`。这是包声明，不代表已验证所有 Python 版本组合。
- 数据来自外部服务，可能受到接口变化、登录、限流和网络条件影响。代码许可证不授予数据的再分发权。
- 集思录文档说明，未设置 Cookie 时可获取的数据受限。不要把账号 Cookie 写入公开代码或提交到仓库。
- “实时”和耗时描述属于上游接口定位及作者说明。本次未测量延迟、数据完整性或准确率。
- 本项目提供数据读取接口。券商下单、策略执行和回测不能由这些接口推导出来。
- 根目录 [LICENSE](https://github.com/shidenggui/easyquotation/blob/7778c1b9f93afb2ce2cf431de393fe690d4ec07c/LICENSE) 和 README 为 MIT，但 `setup.py` 仍写 BSD。元数据存在不一致，本词条按当前根许可证记录；采用某个发行包时还需核对包内许可。

## 开始使用

在自己的 Python 环境中按[官方安装说明](https://github.com/shidenggui/easyquotation#安装)安装包。以下是使用方式示例，本次未执行：

```bash
python -m pip install easyquotation
```

```python
import easyquotation

quotation = easyquotation.use("sina")
quotes = quotation.real(["sh000001", "sz000001"], prefix=True)
```

先核对结果中的时间、代码前缀和字段含义，再把数据接入自己的程序。

## 相关选择

- [Vibe Research](../vibe-research/README.zh-CN.md)提供研究工作台、报告和自选管理；easyquotation 侧重程序中的行情读取。
- [TradingAgents-CN](../tradingagents-cn/README.zh-CN.md)提供多智能体研究流程，且有独立的模型、数据库和许可要求。

以上为用途比较，未验证它们与 easyquotation 的直接集成。

## 复核说明

2026-11-15 核对默认分支、最近提交、发行列表、README、`setup.py` 与 MIT 文件。最近提交只新增项目协作说明，且早于活动窗口；发行列表为空。不把这些观察扩大为项目永远不可用的判断。

验证级别为 `docs`，未安装或请求行情。可用 `search easyquotation --all` 查询候选。证据见 [tool.json](tool.json)。
