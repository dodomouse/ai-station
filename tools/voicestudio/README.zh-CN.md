# VoiceStudio

简体中文 | [English](README.en.md) | [全部导入记录](../../docs/imports/2026-11-15.md)

## 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

当前资格请运行 `python3 scripts/catalog.py search voicestudio --all`（仓库根目录）。Star 和时间数据见 [GitHub 快照](../../data/github/voicestudio.json)，核对依据见 [元数据](tool.json)。

## 原始中文记录（历史快照）

## 009 VoiceStudio

仓库：[debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio)

### 1. 简介

在本地运行语音克隆、声音设计、转录和视频配音。另提供听写、有声书、批量任务及本地 API 与 MCP 接口。

### 2. 适用场景

把文字转成语音或有声书。本地语音转录与听写。翻译并重新配音视频。

### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 参考声音克隆 | 用清晰参考录音生成相近音色的语音。效果依赖参考质量和所选引擎。 | What you can do / Get started |
| 文字设计音色 | 用文字描述声音特征，在声音设计工作区生成声音。 | What you can do |
| 视频翻译与配音 | 为视频翻译并生成配音，使语音时序匹配原视频。提供多说话人配音等相关指南。 | What you can do / Documentation |
| 听写与转录 | 提供浮动听写组件和本地转录，将语音内容转为文字。 | What you can do |
| 旁白、有声书与队列 | 支持故事、有声书和批量排队任务，适合重复生成语音。 | What you can do |
| 本地模型管理 | 按需选择引擎并下载所需模型，下载前询问用户。可使用 CPU，硬件加速按引擎和平台变化。 | What you can do / Platforms / Get started |
| 自动化接入 | 提供本地 API、MCP、可复用配方及监控文件夹，供其他流程调用语音能力。 | What you can do / Documentation |

官方来源入口：[官方 README](https://github.com/debpalash/VoiceStudio/blob/main/README.md)。 能力按原卡核对日期理解。

### 4. 使用限制

**平台与环境**

- macOS 13.3+ Apple Silicon 为稳定本地路径；Intel Mac UI 需连接远程后端，标为 Limited
- Windows 10/11 x64；Windows ARM 为实验性
- Linux 与 Docker
- Android 10+、iOS/iPadOS 17+ 为 Preview，模型下载后可本地离线运行

- 应用为 AGPL-3.0。模型权重、声音与生成输出各有许可，不能用应用开源推断所有音色都可自由商用。本地生成消耗本机算力、存储和电力，CPU/GPU 成本自理。

- 语言覆盖与功能随所选引擎而变，不沿用宣传中的语言总数。
- 克隆声音需所有者许可，清晰参考录音不等于保证完美复刻。
- 本地运行路径依平台而变；Intel Mac、Windows ARM 和手机版本需注意上述状态。
- 本轮没有验证生成质量、翻译准确率或设备速度。

**容易找错的需求（不属于本项目能力）**

- 不能据此满足“无参考、百分之百复刻任意人的声音”。
- 不能承诺给视频人物自动改口型；README 的配音时序对齐不等同唇形重建。

### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/debpalash/VoiceStudio/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- 桌面工作区与浮动听写组件
- 本地 API
- MCP
- 配方、队列及监控文件夹

### 6. 替代选择

- [threerocks/sweety-handdraw-video](../sweety-handdraw-video/README.zh-CN.md)：本项目提供语音克隆、转录和配音；后者围绕手绘视频组织口播、画面和声音对齐。后者只覆盖部分制作需求。

### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/debpalash/VoiceStudio/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/009_debpalash-VoiceStudio.md`。
