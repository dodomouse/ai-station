# TelemetryCleaner（遥测清理）

简体中文 | [English](README.en.md)

TelemetryCleaner 是 Android 运营商预装组件管理工具。它通过 Shizuku 检查已知组件在不同用户空间中的状态，提供权限查看、按空间卸载、恢复和停用操作。适合希望了解手机预装包、并评估是否调整组件状态的用户。

当前保留为候选：本次核对时未达到字典的 1000 Star 门槛。数据见 [GitHub 快照](../../data/github/telemetrycleaner.json)，可用 `search telemetrycleaner --all` 查询。

## 适用场景

- 检查设备是否安装内置清单中的运营商组件。
- 查看主空间、分身或其他用户空间的安装状态与权限记录。
- 在确认影响后，管理指定空间中的组件，并查看操作结果。

## 主要功能

| 功能 | 范围与行为 |
| --- | --- |
| 已知组件检测 | 按内置包名清单检查 SystemHelper、RegService 及部分厂商组件；不是扫描所有应用的行为分析器。 |
| 权限查看 | 读取 Android 包管理器中的声明和授权记录；这些记录本身不能证明组件实际读取或上传了数据。 |
| 按空间卸载 | 对选定空间执行操作，并重新读取包状态核对结果。卸载会清除该空间的组件数据。 |
| 失败后停用 | v1.3 新增手动卸载失败后的停用兜底，设置默认启用。停用保留已有数据和缓存。 |
| 恢复 | 对手动停用的组件尝试重新启用。重新安装已卸载组件需要设备上仍有 APK 副本。 |
| 自动清理 | 默认关闭；启用后按周期检查所选空间，只处理自动清理名单中的组件。 |
| 诊断日志 | 卸载与停用都失败时，可复制拒绝日志供排查。 |

以上范围来自[官方 README](https://github.com/Eynnzerr/TelemetryCleaner/blob/47d7f733ecb821bae154ead8f8bfcb945a170db7/README.md)、[v1.3 说明](https://github.com/Eynnzerr/TelemetryCleaner/releases/tag/v1.3)及[功能提交](https://github.com/Eynnzerr/TelemetryCleaner/commit/e8dd7786628f368907f0d1d31ec2829cc373639a)。

## 环境与限制

- Android 10 或以上，且 Shizuku 已启动并获得授权。Android 11 或以上可按上游指引使用无线调试启动 Shizuku。
- 免 Root 路径借助 shell 权限请求包管理服务。厂商 ROM 仍可拒绝操作，不能保证所有设备都能卸载。
- v1.3 仍未解决部分 vivo 电信、移动组件无法卸载的问题。作者记录过卸载 Device Management 后通话录音失效的用户反馈；这不是本字典的实机验证结果。
- 恢复组件不等于找回卸载时删除的数据。设备未保留 APK 时，也不能保证重新安装。
- 检测范围受清单覆盖限制。未检出已知组件不能证明设备没有其他遥测行为。运营商组件也可能承担正常的入网或运维功能。
- 根目录为 [MIT 许可证](https://github.com/Eynnzerr/TelemetryCleaner/blob/47d7f733ecb821bae154ead8f8bfcb945a170db7/LICENSE)。作者在 README 中将项目定位为 Android 包管理机制的学习工具。

## 开始使用

1. 阅读[官方 README](https://github.com/Eynnzerr/TelemetryCleaner#readme)中的环境要求、组件清单和设备反馈。
2. 从[官方发行页](https://github.com/Eynnzerr/TelemetryCleaner/releases)选择版本，并按上游指南启动 Shizuku。
3. 先检查目标空间、包名和权限记录，再决定是否授权具体操作。
4. 根据结果区分已卸载、已停用和失败。需要恢复时，先确认 APK 副本与数据恢复的区别。

本次收录未下载或安装 APK，也未在手机上执行卸载、停用或恢复。

## 替代选择

现有字典没有经过核对的同用途替代项。选择其他包管理工具时，可比较操作范围、状态核验和恢复条件。

## 复核说明

2026-11-15 核对官方说明、MIT 文件、v1.3 发行记录及部分 Kotlin 实现。源码确认最低 SDK 为 29、自动清理默认关闭、手动卸载失败后的停用兜底默认启用。维护证据为 2026-11-13 的功能提交，最新的许可文件提交未单独用作有效维护证明。

验证级别为 `docs`。源码阅读只能支持实现说明，不能证明各机型上的兼容性或隐私效果。来源、时间和许可指纹见 [tool.json](tool.json)。
