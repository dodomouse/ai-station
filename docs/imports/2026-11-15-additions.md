# 2026-11-15 新增与复核

[English](2026-11-15-additions.en.md)

处理用户指定的 7 个仓库：新增 3 个，复用并刷新 4 个。当前共 62 个唯一项目、124 篇双语介绍和 62 份 GitHub 快照。本次评估时，35 个进入默认目录，27 个保留为候选。

评估时间：2026-11-15T11:54:08.129868Z

| 项目 | 处理 | Star | 状态 | 说明 |
| --- | --- | ---: | --- | --- |
| [Eynnzerr/TelemetryCleaner](../../tools/telemetrycleaner/README.zh-CN.md) | 新增 | 807 | ineligible | Star 未达到 1000；MIT 与窗口内功能维护已核对。 |
| [shidenggui/easyquotation](../../tools/easyquotation/README.zh-CN.md) | 新增 | 5478 | needs_review | 默认分支最近更新为 2026-02-28，且属于文档更新。 |
| [hsliuping/TradingAgents-CN](../../tools/tradingagents-cn/README.zh-CN.md) | 新增 | 32957 | unknown | 应用层采用专有许可，整库不满足完整开源口径。 |
| [KKKKhazix/agent-autoloop](../../tools/agent-autoloop/README.zh-CN.md) | 刷新 | 5427 | eligible | 已有词条；仓库身份与许可指纹一致，刷新快照，保留有效维护证据。 |
| [yetone/magpie](../../tools/magpie/README.zh-CN.md) | 刷新 | 36740 | eligible | 已有词条；仓库身份与许可指纹一致，刷新快照，保留有效维护证据。 |
| [debpalash/VoiceStudio](../../tools/voicestudio/README.zh-CN.md) | 刷新 | 110994 | eligible | 已有词条；仓库身份与许可指纹一致，刷新快照，保留有效维护证据。 |
| [simonlin1212/Vibe-Research](../../tools/vibe-research/README.zh-CN.md) | 刷新 | 3720 | eligible | 已有词条；仓库身份与许可指纹一致，刷新快照，保留有效维护证据。 |

## 判定说明

三项新词条都提供完整的双语介绍与来源。TelemetryCleaner 的 Star 门槛、easyquotation 的维护窗口、TradingAgents-CN 的混合许可分别影响默认收录。候选仍可查询，收录规则没有放宽。

`unknown` 是现有资格计算首先遇到许可证据限制时的状态。TradingAgents-CN 的专有应用层来自 LICENSE 明文说明，不是由 NOASSERTION 标签直接推断。easyquotation 的根 MIT 许可与打包脚本 BSD 标记差异已写入词条。

本次核对新词条的官方说明、许可与选定源码。四个已有词条的身份、Star、仓库状态及许可文件再次核对；未重写其历史中文记录。未安装项目、操作手机组件、请求行情、调用模型或执行交易。

[结构化记录](../../data/imports/2026-11-15-additions.json) · [首批 59 项导入](2026-11-15.md)

快照会在 7 天后过期。历史评估需结合当时的 Git 版本与快照阅读，不能将新的快照当成过去时点的数据。

```bash
python3 scripts/catalog.py search telemetrycleaner --all
python3 scripts/catalog.py search easyquotation --all
python3 scripts/catalog.py search tradingagents-cn --all --lang en
python3 scripts/catalog.py search --all --json
```
