# PaperOrchestra

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[google-research/paper-orchestra](https://github.com/google-research/paper-orchestra)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Documents and productivity |
| 状态 / Status | 已收录 / Included |
| Star | 3837 |
| 评估时间 / Evaluated at | 2026-11-18T14:33:53.118470Z |

## 中文

PaperOrchestra 是 Google Cloud AI Research 推出的多智能体框架，用于自动化撰写 AI 研究论文。它把无结构的写作材料（想法与实验日志）转换为可提交的 LaTeX 稿件，包含文献综合与图表生成。

它像一支由专业智能体组成的团队，负责大纲、文献综述、章节写作、内容润色和绘图，弥合原始研究材料与成稿之间的差距。

### 主要功能

- 多智能体流水线：编排大纲、文献综述、章节写作、内容润色与绘图智能体，端到端生成论文。
- 文献综合：自动检索、排序并整合相关文献到稿件中。
- 图表生成：生成数据图并支持插入概念图。
- LaTeX 自动化：按目标会议模板产出可提交的 LaTeX 稿件。

### 环境要求

- README 示例使用名为 paper_orchestra 的 Conda 环境与 Python 3.11；通过 `pip install -r requirements.txt` 安装依赖。
- 在根目录 .env 中按启用的模型和功能填写相关配置：OpenAI 模型使用 OPENAI_API_KEY；Gemini 模型使用 VERTEX_AI_PROJECT/VERTEX_AI_LOCATION 或 GEMINI_API_KEY。SEMANTIC_SCHOLAR_API_KEY 和可选 SMTP_EMAIL/SMTP_PASSWORD 按所用功能配置，未使用的项可留空。
- 论文生成所用数据集未包含在代码仓库中，需另行下载并放到 datasets/ 目录。

### 使用限制

- 数据集不随仓库发布，需等待单独放出后手动放置。
- 输入材料需为想法与实验日志等预写作素材；输出质量取决于所选模型与模板。
- 写作与文献智能体需要可用的模型服务及相应认证配置，具体凭据取决于所选模型。
- 官方声明这不是 Google 官方支持的产品。
- 本次为文档复核，未安装或运行上游项目。

### 开始使用

1. 按 README 创建并激活 Conda 环境：`conda create -n paper_orchestra python=3.11`，然后 `pip install -r requirements.txt`。
2. 在根目录创建 .env 并填入所需 API 密钥；将数据集放到 datasets/。
3. 运行 `./paper_writing_cli.sh`，或执行 `python paper_writing_cli.py` 并指定 `--raw_materials_dir`、`--latex_template_dir`、`--output_dir` 与 `--use_plotting`。

### 收录与来源

AI 任务用途已依据官方 README 核对。Star 为 2026-11-18T14:33:53.118470Z 的快照，达到总量 ≥1,000 条件；月净增无基线，未作为依据。

近期活动：[2026-11-15 · commit](https://github.com/google-research/paper-orchestra/commit/d9bae997e793a015ed38bb1605be9eb58c00284f)，合并修复无效转义序列的 PR。该提交证明窗口内活动，不代表运行验证。许可不作为准入条件。

- [Official README](https://github.com/google-research/paper-orchestra/blob/main/README.md)

## English

PaperOrchestra is a multi-agent framework from Google Cloud AI Research for automated AI research paper writing. It transforms unconstrained pre-writing materials (ideas and experimental logs) into submission-ready LaTeX manuscripts, including literature synthesis and generated visuals.

Acting like an orchestrated team of specialized agents, it handles outline generation, literature review, section writing, content refinement, and plotting to close the gap between raw research materials and finished papers.

### Features

- Multi-agent pipeline: orchestrates Outline, Literature Review, Section Writing, Content Refinement, and Plotting agents for end-to-end generation.
- Comprehensive literature synthesis: automatically searches, prioritizes, and integrates relevant literature into the manuscript.
- Visuals generation: creates plots and supports inclusion of conceptual diagrams.
- LaTeX automation: produces submission-ready manuscripts following target conference templates.

### Requirements

- The README examples use a Conda environment named paper_orchestra and Python 3.11, with dependencies via `pip install -r requirements.txt`.
- Configure the root .env for the models and features you enable: OPENAI_API_KEY for OpenAI models; VERTEX_AI_PROJECT/VERTEX_AI_LOCATION or GEMINI_API_KEY for Gemini. Configure SEMANTIC_SCHOLAR_API_KEY and optional SMTP_EMAIL/SMTP_PASSWORD as needed for the selected features; unused entries can remain empty.
- The dataset used for paper generation is not included; download it separately and place it under datasets/.

### Limitations

- The dataset is not shipped with the repository and must be placed manually once released.
- Input must be pre-writing material such as ideas and experiment logs; output quality depends on the chosen models and template.
- Writing and literature agents need a usable model service and its authentication configuration; required credentials depend on the selected model.
- The authors state this is not an officially supported Google product.
- This is a documentation review; the upstream software was not installed or run.

### Getting started

1. Create and activate the Conda environment: `conda create -n paper_orchestra python=3.11`, then `pip install -r requirements.txt`.
2. Create a root .env with the required API keys; place the dataset under datasets/.
3. Run `./paper_writing_cli.sh`, or run `python paper_writing_cli.py` with `--raw_materials_dir`, `--latex_template_dir`, `--output_dir`, and `--use_plotting`.

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-18T14:33:53.118470Z meets the total-Star threshold of 1,000; no monthly-growth baseline was available and was not used.

Recent activity: [2026-11-15 · commit](https://github.com/google-research/paper-orchestra/commit/d9bae997e793a015ed38bb1605be9eb58c00284f). The cited commit establishes activity within the review window, not runtime validation. Licensing is not an admission criterion.

- [Official README](https://github.com/google-research/paper-orchestra/blob/main/README.md)

## Review evidence

本次从 GitHub Trending 日榜发现项目，并依据 GitHub 官方文档复核，未安装或运行上游项目。榜单显示的今日新增 Star 仅用于挑选复核对象，不作为近一个月净增证据。

Discovered on GitHub Trending daily and reviewed against official GitHub documentation; upstream software was not installed or run. Today's stars select review candidates, not evidence of net growth over a calendar month.

- [GitHub activity](https://github.com/google-research/paper-orchestra/commit/d9bae997e793a015ed38bb1605be9eb58c00284f) (2026-11-15T18:08:07Z)
- [GitHub Trending daily](https://github.com/trending?since=daily)

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-18T14:33:53.118470Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "paper-orchestra",
    "name": "PaperOrchestra",
    "repository": "google-research/paper-orchestra",
    "repo_node_id": "R_kgDOSR3Uuw",
    "category": "productivity",
    "summary": {
      "zh-CN": "多智能体框架，将想法与实验日志自动写成可提交的 LaTeX 论文并完成文献综述与图表。",
      "en": "A multi-agent framework that turns ideas and experiment logs into submission-ready LaTeX papers with literature synthesis and figures."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-18T14:33:53.118470Z",
        "en": "2026-11-18T14:33:53.118470Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "多智能体框架，将想法与实验日志自动写成可提交的 LaTeX 论文并完成文献综述与图表。",
        "en": "A multi-agent framework that turns ideas and experiment logs into submission-ready LaTeX papers with literature synthesis and figures."
      },
      "source_url": "https://github.com/google-research/paper-orchestra/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/google-research/paper-orchestra/commit/d9bae997e793a015ed38bb1605be9eb58c00284f",
        "occurred_at": "2026-11-15T18:08:07Z",
        "reviewed_at": "2026-11-18T14:33:53.118470Z",
        "qualifies": true,
        "reason": {
          "zh-CN": "GitHub API 记录的具体活动，证明复核窗口内有活动；不代表运行验证。",
          "en": "A specific GitHub API activity establishes activity in the review window, not runtime validation."
        }
      }
    ],
    "sources": [
      {
        "title": "Official README",
        "url": "https://github.com/google-research/paper-orchestra/blob/main/README.md"
      },
      {
        "title": "GitHub Trending daily",
        "url": "https://github.com/trending?since=daily"
      }
    ]
  },
  "snapshot": {
    "full_name": "google-research/paper-orchestra",
    "repo_node_id": "R_kgDOSR3Uuw",
    "stargazers_count": 3837,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-18T14:33:53.118470Z",
    "source_url": "https://api.github.com/repos/google-research/paper-orchestra"
  }
}
```

</details>
