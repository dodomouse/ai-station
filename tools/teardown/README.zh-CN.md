# Teardown：交互式机械拆解与3D演示

简体中文 | [English](README.en.md) | [全部导入记录](../../docs/imports/2026-11-15.md)

## 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

当前资格请运行 `python3 scripts/catalog.py search teardown --all`（仓库根目录）。Star 和时间数据见 [GitHub 快照](../../data/github/teardown.json)，核对依据见 [元数据](tool.json)。

## 原始中文记录（历史快照）

## 051 Teardown：交互式机械拆解与3D演示

仓库：[elvarofficial/teardown](https://github.com/elvarofficial/teardown)

### 1. 简介

面向 Claude Code 的 3D 机械原理演示技能。支持部件拆解、剖视、联动、自动演示与人工交互，可构建离线 HTML 并录制 MP4。

### 2. 适用场景

制作发动机、起落架和连杆机构等机械教学页面、产品结构说明或原理动画。

### 3. 主要功能

| 能力 | 具体作用 | 核对来源 |
| --- | --- | --- |
| 机械运动与联动 | 用统一状态驱动零件姿态和面板读数；运动学模型与 Three.js 绘制分开。 | SKILL.md、V8 运动学源码 |
| 拆解与剖视 | 按子系统查看部件，提供实体、透明、剖切显示方式和观察视角。 | README、SKILL.md |
| 自动讲解与人工探索 | 空闲时按路线演示；点击、拖动、滚轮或键盘操作后交给观众控制，空闲后恢复。 | SKILL.md |
| 离线页面 | 构建脚本将 Three.js、字体和样式嵌入 HTML；也支持配置外部大资源。 | sims/build.mjs |
| 视频与截图 | Playwright 控制 Chromium 逐帧采集，支持 MP4、静帧和联系表；视频默认 60 fps。 | sims/capture.mjs |

官方来源入口：[当前 README](https://github.com/elvarofficial/teardown/blob/main/README.md)。 能力按原卡核对日期理解。

### 4. 使用限制

- **制作环境**：官方面向 Claude Code；Node.js 要求 20 或以上，依赖 Three.js、esbuild 和 Playwright。采集需安装 Playwright Chromium；视频编码需 FFmpeg，程序化音效生成另需 Python 3。观看已打包页面与制作、录制的依赖不同。
- **输入资料**：技能要求查找参考尺寸、图片或手册，再建立几何和运动关系。复杂机器的准确结构不能仅靠一句描述保证。
- **精度**：源码包含运动学和压力等演示模型。本轮只核对文档与静态代码。机械精度、物理计算和工程适用性未经验证。工程计算须另核对参数、假设和结果。
- **设备**：技能采用 1600 × 900 的固定逻辑画布，并考虑集成显卡的绘制负担。本轮未验证 iPad、触摸操作和小屏排版，也未验证 Codex 直接接入。
- **许可**：仓库为 MIT。使用外部模型、图片或音频时，还需分别核对素材许可。

知识卡未提供完整部署费用或付费服务价格；未记录的费用项目需要另行核对。

### 5. 开始使用

安装与入门文档：[当前 README](https://github.com/elvarofficial/teardown/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

其他入口：[当前技能说明](https://github.com/elvarofficial/teardown/blob/main/SKILL.md)。

### 6. 替代选择

- [wheresryan22/anatomy](../anatomy/README.zh-CN.md)：本项目侧重 3D 机械运动、拆解与剖视；后者偏向等轴测结构和机制说明。

### 7. 复核说明

- 知识库记录日期：2026-11-06；卡片最后确认日期：2026-11-06。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：核对官方 README、SKILL.md、依赖清单和关键源码，未安装运行。问法、分类和匹配理由为检索整理判断。

**来源与版本记录**

- [当前 README](https://github.com/elvarofficial/teardown/blob/main/README.md)、[当前技能说明](https://github.com/elvarofficial/teardown/blob/main/SKILL.md)、[提交历史](https://github.com/elvarofficial/teardown/commits/main/)用于后续更新。
- 本次核验提交：[`a91262ac1109051e014662d42ecb0b7bc1f113b1`](https://github.com/elvarofficial/teardown/commit/a91262ac1109051e014662d42ecb0b7bc1f113b1)。
- 固定版本：[README](https://github.com/elvarofficial/teardown/blob/a91262ac1109051e014662d42ecb0b7bc1f113b1/README.md)、[SKILL.md](https://github.com/elvarofficial/teardown/blob/a91262ac1109051e014662d42ecb0b7bc1f113b1/SKILL.md)、[依赖与 Node 要求](https://github.com/elvarofficial/teardown/blob/a91262ac1109051e014662d42ecb0b7bc1f113b1/package.json)。
- 实现核对：[页面构建](https://github.com/elvarofficial/teardown/blob/a91262ac1109051e014662d42ecb0b7bc1f113b1/sims/build.mjs)、[录制工具](https://github.com/elvarofficial/teardown/blob/a91262ac1109051e014662d42ecb0b7bc1f113b1/sims/capture.mjs)、[V8 运动学模型](https://github.com/elvarofficial/teardown/blob/a91262ac1109051e014662d42ecb0b7bc1f113b1/sims/v8-shared/kin.js)。
- README Git blob SHA：`ba138fb0f6cfd3cd62ac5ed021e2c16374dad645`；SKILL.md Git blob SHA：`9505e4aa15caa097260cd982d1a91312dd45859a`。
- 更新时按仓库 ID `1439522537` 去重，复核默认分支、提交、能力与依赖，同步本卡和用途索引，更新最后确认日期。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/051_elvarofficial-teardown.md`。
