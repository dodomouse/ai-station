# 数据格式

简体中文 | [English](data-format.en.md)

一个工具对应 `tools/<id>/`。目录包含 `tool.json`、`README.zh-CN.md` 和 `README.en.md`。动态仓库数据存入 `data/github/<id>.json`。JSON 使用 UTF-8，禁止重复键。

## 共享元数据

完整结构见[模板](../templates/tool/tool.json)。以下字段均需保留；允许未知值的字段在草稿中使用 `null`。

| 字段 | 类型与用途 |
| --- | --- |
| `schema_version` | 整数，当前为 `1` |
| `id` | 小写英文或数字，可用连字符连接；必须等于目录名 |
| `name` | 产品正式名称，通常不翻译 |
| `repository` | GitHub 的 `owner/repository` |
| `repo_node_id` | GitHub 返回的仓库 `node_id`；未核对时为 `null` |
| `category` | `config/taxonomy.json` 中的一个分类 ID |
| `tags` | 不重复的小写标签 ID，例如 `backup` |
| `forms`、`platforms` | 不重复的数组，取值来自分类配置 |
| `summary` | `zh-CN` 和 `en` 两个字符串 |
| `aliases`、`use_cases` | `zh-CN` 和 `en` 两个字符串数组 |
| `alternatives` | 已有工具 ID 数组，不能引用自身 |
| `editorial` | 内容状态、双语复核时间和复核方式 |
| `license_review` | 许可证人工核对结果 |
| `activity_evidence` | 维护活动证据数组 |
| `sources` | 功能、限制和其他描述的来源数组 |

`editorial.status` 为 `draft` 或 `reviewed`。`reviewed_at` 包含两种语言的时间戳。`verification_level` 为 `docs` 或 `tested`。

草稿允许空摘要、空场景、空证据和未知仓库身份。两篇正文仍必须存在。已复核词条必须具有双语摘要、场景、复核日期和至少一个来源，正文不能留有 `{{...}}` 模板占位。

校验器检查结构和已记录的证据。事实是否真实、译文是否表达同一含义、活动是否有意义，仍由编辑者复核。

## 许可证复核

`license_review` 包含 `spdx`、`osi_approved`、`license_sha256`、`source_url` 和 `reviewed_at`。许可证的 SPDX 标识及文件指纹须与快照一致。`license_sha256` 使用上游许可证文件原始字节的 SHA-256，写为 64 位小写十六进制字符串。

未知许可证标识、缺少复核或指纹变化都会阻止默认收录。`osi_approved` 是人工判断记录，程序不会自动判定许可证法律含义。

## 维护证据

以下是字段示例，时间和链接需替换为已核对的实际值：

```json
{
  "type": "merged_pr",
  "occurred_at": "2026-11-01T10:00:00Z",
  "reviewed_at": "2026-11-02T10:00:00Z",
  "url": "https://github.com/owner/repository/pull/123",
  "reason": {
    "zh-CN": "修复文件同步时的重复写入问题。",
    "en": "Fixes duplicate writes during file synchronization."
  },
  "qualifies": true
}
```

`type` 支持 `commit`、`merged_pr`、`release`。`occurred_at` 使用事件实际发生时间，不能填成目录录入时间。`reviewed_at` 不能早于事件时间。

功能与缺陷修复需进入默认分支或明确维护的版本分支。发行版需为正式版本。`qualifies=false` 的证据保留，但不会使工具达标。

## 内容来源

每项来源包含 HTTPS `url`、带时区的 `accessed_at`，以及双语 `supports` 对象：

```json
{
  "url": "https://github.com/owner/repository",
  "accessed_at": "2026-11-02T10:00:00Z",
  "supports": {
    "zh-CN": "安装方法与平台支持。",
    "en": "Installation and supported platforms."
  }
}
```

## GitHub 快照

完整字段见[快照模板](../templates/github-snapshot.json)。

- `repo_node_id` 对应 GitHub 仓库 `node_id`，与词条绑定。
- `full_name` 对应 `owner/repository`，比较时忽略大小写。
- `stargazers_count` 为非负整数，未知时为 `null`。
- `archived`、`disabled` 为布尔值，未知时为 `null`。
- `visibility` 为 `public`、`private`、`internal` 或 `null`。
- `license_spdx`、`license_sha256` 记录许可证标识与文件指纹。
- `last_success_at` 记录这份数据成功核对的时间。

快照模板可以保留未知值并通过结构检查，但工具会显示为 `unknown`。孤立快照、重复仓库路径和重复仓库身份会使校验失败。

## 资格与时间

| 状态 | 判定顺序与含义 |
| --- | --- |
| `unknown` | 快照缺失、不完整、超期或来自未来；仓库身份或许可证需要复核 |
| `ineligible` | 数据可用，但 Star、公开状态、归档状态或开源条件不满足 |
| `needs_review` | 双语内容未复核，或缺少窗口内有效维护证据 |
| `eligible` | 所有条件满足，进入默认查询与目录 |

时间戳必须包含时区。程序统一转为 UTC。活动窗口按评估时刻倒推 3 个日历月，月末取目标月份的最后一天，起止时刻均包含。快照恰好 7 天仍有效，超过 7 天则过期。

阈值来自 `config/policy.json`。查询使用当前时间；测试和构建可以通过 `--as-of` 固定评估时刻。未来活动或未来复核时间不能使词条达标。

## 查询与生成结果

搜索匹配两种语言的名称、别名、摘要、场景、分类名称、标签和正文。英文忽略大小写，并规范化全角字符。空格分隔的词同时匹配，中文连续短语按子串匹配。别名需要人工维护，不自动翻译查询词。

精确名称或别名匹配优先，其次是精确场景或标签，其余按稳定 ID 排序。支持 `--category` 和 `--platform` 筛选。`--lang` 只控制显示语言。

`build` 在校验全部输入后生成两份 Markdown 目录与 `dist/catalog.json`。JSON 保留所有词条及其资格原因；Markdown 只展示 `eligible` 词条。输入校验失败时保留已有输出。每个输出文件单独原子替换，多个文件之间不提供事务保证。

`dist/catalog.json` 是导出数据，尚不是网页全文搜索索引。网站、自动联网采集和定时任务留待后续实现。
