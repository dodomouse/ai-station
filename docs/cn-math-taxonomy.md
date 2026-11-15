# 中小学·高中知识图谱（cn-math-taxonomy）

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[xiaoyang111222/cn-math-taxonomy](https://github.com/xiaoyang111222/cn-math-taxonomy)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 文档与效率 / Productivity |
| 状态 / Status | 候选 / Candidate |
| Star | 8095 |
| 许可证 / License | 待复核 / Review needed |
| 评估时间 / Evaluated at | 2026-11-15T11:54:08.129868Z |
| 快照时间 / Snapshot fetched at | 2026-11-15T10:48:17.864Z |

候选原因：许可证待复核。
Candidate reason: License requires review.

以上为历史核对结果，使用前请复核上游状态。 / This is a dated review; check the current upstream state before use.

## 中文

### 导入复核（2026-11-15）

本次核对 GitHub 状态、可取得的许可证及维护提交。以下原卡保留原来的日期、功能说明和限制；原卡中“未重新联网”指当时的导出过程。本次仍未安装或试用项目。

本次收录状态和数据见文首，来源及许可核对记录见[收录依据](#review-evidence)。

当前 LICENSE 与 README 说明数据、题库、诊断代码和文档采用 CC BY-NC 4.0。按非商业许可候选保留。

### 原始中文记录（历史快照）

### 029 中小学·高中知识图谱（cn-math-taxonomy）

仓库：[xiaoyang111222/cn-math-taxonomy](https://github.com/xiaoyang111222/cn-math-taxonomy)

#### 1. 简介

按知识点和先修关系组织中小学至高中多学科资料。提供图谱浏览、题库和自适应前置诊断，追溯基础知识薄弱点。

#### 2. 适用场景

浏览学科知识点及先修关系。按答题结果回溯基础知识。研究教育知识图谱和静态诊断工具。

#### 3. 主要功能

| 能力 | 具体作用 | README 核对位置 |
| --- | --- | --- |
| 学科知识点与先修图 | 以节点和 hard/soft 先修边表示多学科知识，提供局部关系图浏览。 | 项目概述 / 数据来源与对齐依据 |
| 教材和课程标准映射 | 记录教材章节与课标条目，区分已核与待核信息。 | 数据来源与对齐依据 / 课标对齐 |
| 自适应前置诊断 | 从目标知识点或章节开始出题；依答题情况继续确认或回溯先修，并输出薄弱、不稳线索。 | 诊断小工具 |
| 题目、答案与解析 | 提供各知识点的练习题和参考答案，作答后可看解析。 | 题库 / 诊断小工具 |
| 学习路径与结果导出 | 按先修和年级组织建议路径，支持本机进度、JSON 导出、打印与分享图。 | 诊断小工具 |
| 本机盲区与历史 | 把薄弱和不稳线索存入本地浏览器，可关联孩子档案并一键再测。 | 诊断小工具 / 文件 |
| 静态网页与离线使用 | 图谱和诊断页由静态资源组成，PWA 与本地资源支持离线使用场景。 | 文件 / 诊断小工具 / 打开网页 |

官方来源入口：[官方 README](https://github.com/xiaoyang111222/cn-math-taxonomy/blob/main/README.md)。 能力按原卡核对日期理解。

#### 4. 使用限制

**平台与环境**

- 现代浏览器
- 线上静态站点或本地静态服务器
- 支持 PWA 与 localStorage 的离线浏览环境

- 采用 CC BY-NC 4.0，个人学习、教学与研究可免费使用；商业使用需单独授权。
- 诊断网页使用已提供的静态题库，README 没有要求每次答题调用付费大模型。
- 自行托管资源与后续改造成本另计。

- 先修关系、题目难度和区分度未经教师或学生数据检验。
- 题目和答案由 AI 生成，部分有自动复核，但不是全部经独立盲解或教师审核。
- 每个知识点测试题数有限，诊断输出只是线索，不代替完整测评。
- 覆盖教材、学科、课标版次和页码有待核项。

**容易找错的需求（不属于本项目能力）**

- 不是经过教育测量验证、能准确判定孩子能力的正式测评系统。
- 不是无限生成新题、提供完整在线课程或英语口语听力训练的平台。

#### 5. 开始使用

安装与入门文档：[官方 README](https://github.com/xiaoyang111222/cn-math-taxonomy/blob/main/README.md)。安装、依赖配置及示例以该入口指向的项目文档为准。

**接入方式**

- 静态浏览器网页：首页、explore、diagnose、children
- PWA / 本机缓存
- 公开 JSON 数据与实现源码

#### 6. 替代选择

- [byoungd/up](up.md#中文)：本项目提供学科知识点、先修关系和题库；后者讨论学习方法。后者不能代替知识图谱和题库。

#### 7. 复核说明

- 知识库记录日期：2026-11-03；卡片最后确认日期：2026-11-03。

- 本次导出（2026-11-15）：整理知识库既有材料，未重新联网核验，也未安装或实际试用。

**既有记录的核验范围**

- 信息口径：能力来自项目文档。口语问法和匹配理由是检索整理判断，未经安装实测。

**来源与版本记录**

- [官方 README](https://github.com/xiaoyang111222/cn-math-taxonomy/blob/main/README.md)：能力、输入输出、接入和使用条件的核对来源。确认日期：2026-11-03。
- README 会更新。采用工具前复核平台、接口、额度、收费和许可。
- 问法匹配属于用途归纳，不证明用户已使用项目，也不证明项目效果。

知识库原卡：`004_技术学习/005_GitHub收藏/005_项目详解/029_xiaoyang111222-cn-math-taxonomy.md`。

## English

A Chinese school-subject knowledge graph with prerequisites, question banks and diagnostic learning paths.

### Use cases

- Explore subject prerequisites
- Use question-based study diagnostics

### Requirements and limits

Data, questions, diagnostic code and documentation use CC BY-NC 4.0, so this is not admitted as an OSI-approved software entry. Questions and difficulty estimates have not all received independent educational validation. Diagnosis is a study aid, not a validated assessment or complete course platform.

### Getting started

Read the [official documentation](https://github.com/xiaoyang111222/cn-math-taxonomy/blob/main/README.md) for the current installation or reading entry point. This import did not install the project, invoke its workflows or test its output.

### Related entries

- [Up](up.md#english)

Related entries can serve different needs; this list does not claim feature parity.

### Review and provenance

This English digest condenses the user’s Chinese card and adds import findings. The [preserved Chinese record](#中文) contains the full historical feature table, limitations and original source dates. Capability statements are documentation-based, not hands-on test results.

GitHub metadata was fetched at 2026-11-15T10:48:17.864Z. [Shared metadata](#review-evidence) contains license and commit evidence; the [snapshot](#review-evidence) contains Stars and repository state. This is a dated review; repository state requires manual rechecking.

Current licensing applies CC BY-NC 4.0 to the data, question bank, diagnostic code and docs. Retained as a non-commercial candidate.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

保留原始核对数据，便于追溯来源、许可和维护证据。 / Original review data preserves source, license and maintenance evidence.

```json
{
  "evaluated_at": "2026-11-15T11:54:08.129868Z",
  "eligibility": {
    "status": "unknown",
    "reasons": [
      "license_needs_review"
    ]
  },
  "metadata": {
    "schema_version": 1,
    "id": "cn-math-taxonomy",
    "name": "中小学·高中知识图谱（cn-math-taxonomy）",
    "repository": "xiaoyang111222/cn-math-taxonomy",
    "repo_node_id": "R_kgDOVONPVA",
    "category": "productivity",
    "tags": [
      "education",
      "knowledge-graph",
      "noncommercial"
    ],
    "forms": [
      "web"
    ],
    "platforms": [
      "web"
    ],
    "aliases": {
      "zh-CN": [
        "中小学·高中知识图谱（cn-math-taxonomy）"
      ],
      "en": [
        "CN Math Taxonomy"
      ]
    },
    "summary": {
      "zh-CN": "按知识点和先修关系组织中小学至高中多学科资料。提供图谱浏览、题库和自适应前置诊断，追溯基础知识薄弱点。",
      "en": "A Chinese school-subject knowledge graph with prerequisites, question banks and diagnostic learning paths."
    },
    "use_cases": {
      "zh-CN": [
        "浏览学科知识点及先修关系。按答题结果回溯基础知识。研究教育知识图谱和静态诊断工具。"
      ],
      "en": [
        "Explore subject prerequisites",
        "Use question-based study diagnostics"
      ]
    },
    "alternatives": [
      "up"
    ],
    "editorial": {
      "status": "draft",
      "reviewed_at": {
        "zh-CN": "2026-11-15T11:03:50.120930Z",
        "en": "2026-11-15T11:03:50.120930Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": null,
      "osi_approved": false,
      "license_sha256": "41003d4a74749c0220e33dd415042164b5a1093ed401f36277234f772d22d3d0",
      "source_url": "https://github.com/xiaoyang111222/cn-math-taxonomy/blob/main/LICENSE",
      "reviewed_at": "2026-11-15T11:03:50.120930Z"
    },
    "activity_evidence": [],
    "sources": [
      {
        "url": "https://github.com/xiaoyang111222/cn-math-taxonomy",
        "accessed_at": "2026-11-15T10:48:17.864Z",
        "supports": {
          "zh-CN": "本次联网核对仓库身份、Star 与公开状态。",
          "en": "Repository identity, Stars and visibility checked during import."
        }
      },
      {
        "url": "https://github.com/xiaoyang111222/cn-math-taxonomy/blob/main/README.md",
        "accessed_at": "2026-11-15T10:54:04.825Z",
        "supports": {
          "zh-CN": "官方说明；能力整理沿用原卡，导入补注另列。",
          "en": "Official documentation; source-card descriptions are retained with separate import notes."
        }
      },
      {
        "url": "https://github.com/xiaoyang111222/cn-math-taxonomy/blob/main/LICENSE",
        "accessed_at": "2026-11-15T10:53:12.924Z",
        "supports": {
          "zh-CN": "本次读取的许可文件；不代表已完成复杂许可范围复核。",
          "en": "License file retrieved during import; complex scope may still require review."
        }
      }
    ],
    "import_review": {
      "batch": "2026-11-15",
      "source_number": "029",
      "source_file": "001_GitHub仓库介绍汇总_2026-11-15.md",
      "source_sha256": "d86b47077ac82d5559dd3f2fd56fd35738add0f5fa2b3efae33a72396323d1f7",
      "original_card_sha256": "c198b0cdb1c8d2432b3f996a99225ec3284d1888b1546ed3b07488ef91384726",
      "reviewed_at": "2026-11-15T11:03:50.120930Z",
      "content_kind": "tool",
      "pending_reasons": [
        "license_review_pending"
      ],
      "english_scope": "editorial_digest",
      "source_card_preserved": true,
      "notes": {
        "zh-CN": "当前 LICENSE 与 README 说明数据、题库、诊断代码和文档采用 CC BY-NC 4.0。按非商业许可候选保留。",
        "en": "Current licensing applies CC BY-NC 4.0 to the data, question bank, diagnostic code and docs. Retained as a non-commercial candidate."
      }
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOVONPVA",
    "full_name": "xiaoyang111222/cn-math-taxonomy",
    "stargazers_count": 8095,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "NOASSERTION",
    "license_sha256": "41003d4a74749c0220e33dd415042164b5a1093ed401f36277234f772d22d3d0",
    "last_success_at": "2026-11-15T10:48:17.864Z"
  }
}
```

</details>
