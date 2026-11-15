# ai-station

**中英文开源工具字典，按用途查找、按证据收录。**

简体中文 | [English](README.en.md)

ai-station 整理 GitHub 上有明确用途的开源工具。每个词条提供中文和英文介绍，说明适用场景、主要功能、使用限制、入门方法和替代选择。收录范围覆盖通用工具，AI 是其中一个分类。

[浏览中文目录](indexes/README.md) · [Browse in English](indexes/README.en.md) · [贡献指南](CONTRIBUTING.md) · [设计说明](docs/catalog-design.md)

## 当前状态

已导入 59 个项目，提供 118 篇中英文介绍和 59 份 GitHub 快照。2026-11-15 导入评估时，35 个符合默认目录条件，其余保留为可查询候选。见[全部条目与检查报告](docs/imports/2026-11-15.md)。GitHub 自动采集、定时同步和网页搜索尚未实现。

## 收录标准

默认目录只展示同时满足以下条件的工具：

- 至少 **1000 个 Star**。
- 最近 **3 个日历月**内有人工确认的有效维护活动。
- GitHub 仓库公开、未归档、未禁用。
- 开源许可证已复核，中英文内容均已复核。
- GitHub 数据快照距评估时刻不超过 **7 天**。

功能或缺陷修复、已合并 PR、正式发行版可作为维护证据。纯文档修改或机器人机械更新不能单独证明有效维护。Star 和活跃度是筛选条件，不能代替工具质量判断。

未达标或证据过期的词条保留在仓库中，通过 `search --all` 查询。每次本地查询重新评估资格；Markdown 目录显示构建时的结果及评估时间。

## 分类

| 分类 | 收录方向 |
| --- | --- |
| AI 工具 | 本地推理、辅助编程、知识检索 |
| 开发辅助 | API 调试、代码导航、开发环境 |
| 终端与 Shell | 命令行搜索、终端交互、Shell 效率 |
| 数据处理 | 清洗、转换、查询、可视化 |
| 自动化 | 批处理、任务编排、系统集成 |
| 部署与运维 | 部署、监控、日志、备份 |
| 文档与效率 | 笔记、知识管理、文件整理 |
| 图像与音视频 | 编辑、转换、压缩、录制 |

## 本地使用

需要 Python 3.10 或更新版本，无第三方依赖。在仓库根目录运行：

```bash
python3 scripts/catalog.py validate
python3 -m unittest discover -s tests -v
python3 scripts/catalog.py build
python3 scripts/catalog.py search "终端"
python3 scripts/catalog.py search "terminal" --lang en
```

中文和英文查询都会检索两种语言的内容。`--lang` 控制结果的摘要语言和词条链接。

```bash
python3 scripts/catalog.py search --category ai --platform linux
python3 scripts/catalog.py search --all --lang en --json
```

使用 `search --all` 可查看尚未正式收录的候选。`build` 生成两份 Markdown 目录和 `dist/catalog.json`。固定评估时间可复现构建结果：

```bash
python3 scripts/catalog.py build --as-of 2026-11-15T11:03:50.120930Z
```

## 新增工具

以下命令创建草稿。将 `example-tool` 和 `owner/repository` 替换为实际值：

```bash
python3 scripts/catalog.py new example-tool --repository owner/repository
```

随后填写共享元数据和两篇介绍。按[贡献指南](CONTRIBUTING.md)补充来源、许可证、活动证据及仓库快照。校验允许保留草稿；进入默认目录前必须完成双语复核和资格检查。

## 仓库结构

```text
config/                   收录策略与双语分类
tools/<id>/              每个工具的独立目录
   tool.json              两种语言共用的结构化元数据
   README.zh-CN.md         中文介绍
   README.en.md            英文介绍
data/github/<id>.json    GitHub 数据快照
templates/               词条和快照模板
scripts/catalog.py       创建、校验、构建、查询
indexes/                 自动生成的中英文目录
tests/                   行为与边界测试
docs/                    设计与数据格式说明
```

元数据和介绍由编辑者维护，目录由脚本生成。Star 数量只写在快照中，避免两种语言各自维护一份。

## 参与维护

阅读[中文贡献指南](CONTRIBUTING.md)或[English contribution guide](CONTRIBUTING.en.md)。数据字段见[中文格式说明](docs/data-format.md)和[English format reference](docs/data-format.en.md)。

可优先完善真实词条、中英文译文、维护证据和替代工具比较。只依据文档撰写的介绍应标记为文档复核。

## 许可证

本仓库采用 [Apache License 2.0](LICENSE)。收录工具各自保留原有许可证。
