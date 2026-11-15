# 贡献指南

简体中文 | [English](CONTRIBUTING.en.md)

每个工具使用一个稳定 ID，共享一份元数据，并提供中文和英文介绍。新增前检查现有词条，避免为仓库改名、镜像或不同语言重复建档。

## 创建草稿

在仓库根目录运行，替换示例参数：

```bash
python3 scripts/catalog.py new example-tool --repository owner/repository
```

脚本创建 `tools/example-tool/`，初始状态为 `draft`。重复 ID 或重复仓库会返回错误，已有词条不会被覆盖。

## 编写两种语言

编辑 `tool.json` 中的名称、摘要、别名、场景、分类和标签。分别编辑 `README.zh-CN.md` 与 `README.en.md`。两篇正文应表达相同的功能、限制和确定程度，无须逐句直译。

正文说明用途、场景、功能、限制、入门方法和替代选择。保留产品正式名称、命令、链接和许可证标识。删除模板占位文字。不要将尚未实测的能力写成测试结论。

`summary`、`aliases`、`use_cases` 使用 `zh-CN` 和 `en` 两个键。稳定标签使用英文小写 ID；需要中文同义词时，写入中文别名或场景。

## 记录证据

填写[格式说明](docs/data-format.md)中的来源、许可证和维护活动字段。

复制 `templates/github-snapshot.json` 到 `data/github/<id>.json`。从 GitHub 核对仓库身份、Star、归档状态和许可证，填写快照。当前工具不会联网采集数据。

许可证指纹采用上游许可证文件原始字节的 SHA-256。词条与快照中的指纹必须一致。通过 [OSI 许可证清单](https://opensource.org/licenses)核对后，才将 `osi_approved` 设为 `true`。

维护证据需包含实际发生时间、来源 URL、中英文判断理由和复核时间。确认活动属于有效维护后，将 `qualifies` 设为 `true`。纯文档或机器人机械更新保持 `false`。

## 完成复核

两种语言均完成复核后，填写各自的 `editorial.reviewed_at`。随后将 `editorial.status` 改为 `reviewed`。

`verification_level` 使用 `docs` 或 `tested`。实际试用时，在两篇正文中记录版本、环境、操作和结果。

内容复核与收录资格是两件事。已复核词条仍可能因快照过期、活动证据过期或 Star 不足而退出默认目录。

## 验证变更

```bash
python3 scripts/catalog.py validate
python3 -m unittest discover -s tests -v
python3 scripts/catalog.py build
python3 scripts/catalog.py search --all --lang en --json
```

检查两份目录的链接和摘要。提交内容变更时一并更新 `indexes/`；`dist/` 是忽略的构建产物。不要手改生成的目录。

## 更新已有工具

仓库改名或转移时保留工具 ID，核对 `repo_node_id` 后更新仓库路径。新仓库使用不同身份时重新复核。Star、归档状态和许可证识别结果只更新在快照中。

快照记录最后一次成功核对的数据。联网失败不能覆盖成功数据，也不能把 `last_success_at` 改为失败时刻。手动维护时同样遵循这条规则。
