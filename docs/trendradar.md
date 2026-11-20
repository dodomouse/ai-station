# TrendRadar

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[sansan0/TrendRadar](https://github.com/sansan0/TrendRadar)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 63753 |
| 评估时间 / Evaluated at | 2026-11-20T14:20:07Z |
| 快照时间 / Snapshot recorded at | 2026-11-20T14:19:16Z |

## 中文

TrendRadar 聚合新闻热榜和自选 RSS/Atom 订阅，适合持续跟踪同一议题。它记录新闻何时上榜、出现多少次、排名怎样变化，还可以让 AI 检索采集记录、翻译外语条目或生成简报。

### 跟踪国内外时事

| 信息来源 | 怎样使用 |
| --- | --- |
| 国内热榜 | 默认从 NewsNow 获取澎湃新闻、财联社、凤凰网、今日头条等平台的榜单。可以对照同一话题在各个平台的排名和出现时间。 |
| 海外订阅 | 默认订阅包含雅虎财经和 Hacker News。要跟踪综合时事，可以在 `config/config.yaml` 的 `rss.feeds` 中添加媒体的订阅地址。 |
| 自选订阅示例 | 给每个源设置唯一的 `id`、显示名称 `name` 和订阅地址 `url`。本次直接读取并确认有新闻条目的两个源是[中新网时政](https://www.chinanews.com.cn/rss/china.xml)和 [BBC World](https://feeds.bbci.co.uk/news/world/rss.xml)。 |

### 搜索、分析与推送

- 在 `config/frequency_words.txt` 设置关注词，可以按当前榜单、当日汇总或新增条目查看结果。启用 AI 筛选后，可用自然语言描述兴趣。报告可推送到飞书、Telegram 或邮箱等渠道。
- 接入项目的 MCP 服务后，可以让 AI 助手搜索已采集的新闻和 RSS，分析话题在指定时段的热度。要比较一周的走向，先持续采集并保留这一周的数据。热榜衡量的是所选平台的关注度，RSS 条目按发布时间跟踪。[MCP 工具与查询示例](https://github.com/sansan0/TrendRadar/blob/86584f5544c66d4e22132f9b87c44a7ea3a32fea/README-MCP-FAQ.md)

### 开始使用与限制

1. 克隆上游仓库，进入 `TrendRadar` 目录，运行 `uv sync`。项目要求 Python 3.12 或以上，uv 可管理 Python 环境，另有 Docker 部署入口。
2. 编辑 `config/config.yaml`，选择热榜和 RSS 源，运行 `uv run python -m trendradar` 采集一次。跟踪中英文报道时，可分别设置两种语言的关键词。阅读外语条目时可启用 AI 翻译。
3. 关键词筛选可独立运行。使用 AI 筛选、翻译或分析时需要配置模型服务，使用云模型可能产生费用。启用通知时需要配置相应渠道的凭据。新闻覆盖取决于订阅源、热榜接口的可用性和采集频率。[上游使用说明](https://github.com/sansan0/TrendRadar/blob/86584f5544c66d4e22132f9b87c44a7ea3a32fea/README.md) · [配置文件](https://github.com/sansan0/TrendRadar/blob/86584f5544c66d4e22132f9b87c44a7ea3a32fea/config/config.yaml) · [Python 依赖](https://github.com/sansan0/TrendRadar/blob/86584f5544c66d4e22132f9b87c44a7ea3a32fea/pyproject.toml)

### 收录依据

2026-11-20 核对时有 63,753 Star。2026-10-29 的提交修复了没有关键词匹配时报告丢失 RSS 总数的问题。此次核对覆盖上游文档、配置、提交及上述两个订阅地址，项目运行和推送效果未经实测。[GitHub 仓库 API](https://api.github.com/repos/sansan0/TrendRadar) · [RSS 计数修复](https://github.com/sansan0/TrendRadar/commit/946f52aa0704883f666c322888b8cd9af4cbcfff)

## English

TrendRadar monitors news rankings and RSS/Atom feeds. It records when a headline first and last appears on a chart, how often it appears and how its rank changes. An AI assistant can search these records, translate items or produce a briefing.

### Following Chinese and international news

The default charts include The Paper, Cailian Press, Phoenix and Toutiao via NewsNow. The default feeds include Yahoo Finance and Hacker News. To follow general current affairs, add a unique `id`, a display `name` and a feed `url` to `rss.feeds` in `config/config.yaml`. Two optional feeds returned news items during this review. [China News Service politics (Chinese)](https://www.chinanews.com.cn/rss/china.xml) · [BBC World (English)](https://feeds.bbci.co.uk/news/world/rss.xml)

Set topics in `config/frequency_words.txt` and choose a current chart, daily digest or newly collected items. The MCP server lets an assistant search stored news and RSS items and compare a topic across dates. A week-long comparison needs a week of retained observations. Chart positions reflect attention on the selected platforms. RSS feeds track stories by publication time. Reports can be delivered through Feishu, Telegram or email. [MCP tools and query examples](https://github.com/sansan0/TrendRadar/blob/86584f5544c66d4e22132f9b87c44a7ea3a32fea/README-MCP-FAQ.md)

### Getting started and limitations

1. Clone the upstream repository, enter the `TrendRadar` directory and run `uv sync`. The project requires Python 3.12 or later. uv can manage the interpreter. Docker is also supported.
2. Choose platforms and feeds in `config/config.yaml`, then run `uv run python -m trendradar` to collect a snapshot. Configure keywords in both languages to match Chinese and English coverage. Enable AI translation to read foreign-language items.
3. Keyword filtering runs on its own. AI filtering, translation and analysis require a configured model service. Hosted models may incur charges. Notifications require channel credentials. Coverage depends on feed and chart availability and the collection interval. [Upstream guide](https://github.com/sansan0/TrendRadar/blob/86584f5544c66d4e22132f9b87c44a7ea3a32fea/README.md) · [Source configuration](https://github.com/sansan0/TrendRadar/blob/86584f5544c66d4e22132f9b87c44a7ea3a32fea/config/config.yaml) · [Python requirements](https://github.com/sansan0/TrendRadar/blob/86584f5544c66d4e22132f9b87c44a7ea3a32fea/pyproject.toml)

### Admission evidence

The repository had 63,753 stars on 2026-11-20. A 2026-10-29 commit preserves the RSS item count when no keywords match. This review checked documentation, configuration, the commit and the two optional feeds. Collection and notification delivery were not tested through TrendRadar. [GitHub repository API](https://api.github.com/repos/sansan0/TrendRadar) · [RSS count fix](https://github.com/sansan0/TrendRadar/commit/946f52aa0704883f666c322888b8cd9af4cbcfff)

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-20T14:20:07Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "trendradar",
    "name": "TrendRadar",
    "repository": "sansan0/TrendRadar",
    "repo_node_id": "R_kgDOOhDnFA",
    "category": "productivity",
    "summary": {
      "zh-CN": "聚合国内新闻热榜与国内外 RSS 订阅，跟踪话题排名变化，支持 AI 检索、翻译和简报推送。",
      "en": "Tracks Chinese news rankings and RSS feeds from China and abroad, with AI-assisted search, translation and briefing delivery."
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "MCP 服务提供新闻及 RSS 检索与话题趋势分析工具，供 AI 助手查询已采集的数据。",
        "en": "The MCP server lets AI assistants search collected news and RSS items and analyze topic trends."
      },
      "source_url": "https://github.com/sansan0/TrendRadar/blob/86584f5544c66d4e22132f9b87c44a7ea3a32fea/README-MCP-FAQ.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "qualifies": true,
        "url": "https://github.com/sansan0/TrendRadar/commit/946f52aa0704883f666c322888b8cd9af4cbcfff",
        "occurred_at": "2026-10-29T11:37:47Z",
        "reviewed_at": "2026-11-20T14:20:07Z",
        "reason": {
          "zh-CN": "修复关键词没有匹配项时的 RSS 总数统计，并补充对应的边界测试。",
          "en": "Preserves the RSS count when no keywords match and adds regression coverage for edge cases."
        }
      }
    ],
    "sources": [
      {"url": "https://api.github.com/repos/sansan0/TrendRadar", "accessed_at": "2026-11-20T14:19:16Z"},
      {"url": "https://github.com/sansan0/TrendRadar/blob/86584f5544c66d4e22132f9b87c44a7ea3a32fea/README.md", "accessed_at": "2026-11-20T14:20:07Z"},
      {"url": "https://github.com/sansan0/TrendRadar/blob/86584f5544c66d4e22132f9b87c44a7ea3a32fea/config/config.yaml", "accessed_at": "2026-11-20T14:20:07Z"},
      {"url": "https://github.com/sansan0/TrendRadar/blob/86584f5544c66d4e22132f9b87c44a7ea3a32fea/README-MCP-FAQ.md", "accessed_at": "2026-11-20T14:20:07Z"},
      {"url": "https://github.com/sansan0/TrendRadar/blob/86584f5544c66d4e22132f9b87c44a7ea3a32fea/pyproject.toml", "accessed_at": "2026-11-20T14:20:07Z"}
    ]
  },
  "snapshot": {
    "schema_version": 1,
    "repository_id": 974186260,
    "repo_node_id": "R_kgDOOhDnFA",
    "full_name": "sansan0/TrendRadar",
    "stargazers_count": 63753,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-20T14:19:16Z",
    "head_sha": "86584f5544c66d4e22132f9b87c44a7ea3a32fea"
  }
}
```

</details>
