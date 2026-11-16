# Claude for Financial Services

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[anthropics/financial-services](https://github.com/anthropics/financial-services)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 数据处理 / Data processing |
| 状态 / Status | 已收录 / Included |
| Star | 41340 |
| 许可证 / License | Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:47:41.248Z |

## 中文

为金融研究与运营提供智能体模板、技能、数据连接器和部署脚本。

### 用途与功能

- 起草研究、估值与对账材料

覆盖研究、建模、会议准备与运营流程，支持Cowork插件和Managed Agents部署；附Office插件管理工具。

### 环境与限制

需要兼容Claude产品、相关API或数据服务权限。数据连接器可能付费，部署涉及租户配置。产出供专业人员复核，不代表投资建议、交易执行或财务审批。不同插件与预览功能的边界需单独核对。

### 开始使用

按README选取单个业务插件，配置必要数据连接，并先用样例验证输出。 参阅[官方 README](https://github.com/anthropics/financial-services/blob/main/README.md)。

### 收录与来源

除业务技能外提供可执行部署、清单生成与Office安装维护脚本。 最近维护：[实现提交](https://github.com/anthropics/financial-services/commit/3e32c2287dcb637c184c01cc0ad82d6af7e9bb0f)（2026-11-12T19:13:44Z）。已核对实现提交：修复Office安装清单对Outlook的Bedrock配置处理，并更新导出边界说明。

通过逛逛GitHub的第三方文章索引发现。索引记录了下列文章；本次未读取微信原文，不据此声称已阅读全文。

- 2026-10-05：[盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537550&idx=1&sn=29715a80ebde4036ab57651905d6bc3f)

本次为文档复核，未安装或运行上游项目。Star、许可和维护状态为核对时的快照。


补充核对作者在公开平台发布或授权发布的文章，确认署名、日期与仓库关联：

- 2026-10-06：[盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。](https://www.woshipm.com/share/6473850.html)

## English

Provides agent templates, skills, data connectors and deployment scripts for financial research and operations.

### Uses and features

- Draft research, valuation and reconciliation material

Covers research, modeling, meeting preparation and operations through Cowork plugins and Managed Agents deployment, with Office add-in administration tools.

### Requirements and limits

Requires compatible Claude products and relevant API or data-service access. Connectors may be paid and deployment involves tenant configuration. Outputs are for professional review, not investment advice, transaction execution or financial approval. Check each plugin and preview feature separately.

### Getting started

Choose one workflow plugin, configure required data connections and validate outputs on a sample. See the [official README](https://github.com/anthropics/financial-services/blob/main/README.md).

### Review and provenance

Includes executable deployment, manifest generation and Office administration scripts alongside domain skills. Recent maintenance: [implementation commit](https://github.com/anthropics/financial-services/commit/3e32c2287dcb637c184c01cc0ad82d6af7e9bb0f) (2026-11-12T19:13:44Z). Reviewed an implementation commit fixing Office manifest handling for Outlook Bedrock configuration and updating export-boundary documentation.

Discovered through a third-party index of 逛逛GitHub articles. The index records the articles below; the original WeChat pages were not read in this review. The article links and dates are listed in the Chinese section. This was a documentation review; the upstream project was not installed or run. Stars, licensing and activity are dated snapshots.


Public articles published or authorized by the author were also checked for attribution, date and repository links. See the additional links in the Chinese section.

## Review evidence

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-16T14:47:41.248Z",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "financial-services",
    "name": "Claude for Financial Services",
    "repository": "anthropics/financial-services",
    "repo_node_id": "R_kgDORXFZgQ",
    "category": "data",
    "tags": [],
    "forms": [
      "plugin",
      "skill"
    ],
    "platforms": [],
    "aliases": {
      "zh-CN": [
        "Claude for Financial Services"
      ],
      "en": [
        "Claude for Financial Services"
      ]
    },
    "summary": {
      "zh-CN": "为金融研究与运营提供智能体模板、技能、数据连接器和部署脚本。",
      "en": "Provides agent templates, skills, data connectors and deployment scripts for financial research and operations."
    },
    "use_cases": {
      "zh-CN": [
        "起草研究、估值与对账材料"
      ],
      "en": [
        "Draft research, valuation and reconciliation material"
      ]
    },
    "alternatives": [],
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:47:41.248Z",
        "en": "2026-11-16T14:47:41.248Z"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "Apache-2.0",
      "osi_approved": true,
      "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
      "source_url": "https://github.com/anthropics/financial-services/blob/main/LICENSE",
      "reviewed_at": "2026-11-16T14:47:41.248Z"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/anthropics/financial-services/commit/3e32c2287dcb637c184c01cc0ad82d6af7e9bb0f",
        "occurred_at": "2026-11-12T19:13:44Z",
        "reason": {
          "zh-CN": "已核对实现提交：修复Office安装清单对Outlook的Bedrock配置处理，并更新导出边界说明。",
          "en": "Reviewed an implementation commit fixing Office manifest handling for Outlook Bedrock configuration and updating export-boundary documentation."
        },
        "reviewed_at": "2026-11-16T14:47:41.248Z",
        "qualifies": true
      }
    ],
    "sources": [
      {
        "url": "https://github.com/anthropics/financial-services/blob/main/README.md",
        "accessed_at": "2026-11-16T14:47:41.248Z",
        "supports": {
          "zh-CN": "用途、功能、环境、限制和入门；文档复核，未安装试用。",
          "en": "Uses, features, requirements, limits and setup; documentation review, not a hands-on test."
        }
      },
      {
        "url": "https://github.com/anthropics/financial-services/blob/main/LICENSE",
        "accessed_at": "2026-11-16T14:47:41.248Z",
        "supports": {
          "zh-CN": "许可正文与文件摘要。",
          "en": "License text and file digest."
        }
      },
      {
        "url": "https://www.noking.tech/github-radar/data/library.json",
        "accessed_at": "2026-11-16T14:47:41.248Z",
        "supports": {
          "zh-CN": "第三方索引中的公众号文章归属、时间与项目发现线索；非原文阅读证据。",
          "en": "Third-party account attribution, article dates and discovery leads; not proof of reading the originals."
        }
      },
      {
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537550&idx=1&sn=29715a80ebde4036ab57651905d6bc3f",
        "accessed_at": "2026-11-16T14:47:41.248Z",
        "supports": {
          "zh-CN": "索引记录的文章链接：2026-10-05 盘点 20 个 9 月份 GitHub 上顶顶顶的开源项目。；本次未直接读取。",
          "en": "Article link recorded in the index: 2026-10-05; not directly read in this review."
        }
      },
      {
        "url": "https://www.woshipm.com/share/6473850.html",
        "accessed_at": "2026-11-16T14:26:02.487400+00:00",
        "published_date": "2026-10-06",
        "author": "逛逛GitHub",
        "supports": {
          "zh-CN": "作者公开发表或授权的文章；已核对署名、日期与仓库链接。",
          "en": "Author-published or authorized public article; attribution, date and repository links checked."
        }
      }
    ],
    "quality_review": {
      "basis": {
        "zh-CN": "除业务技能外提供可执行部署、清单生成与Office安装维护脚本。",
        "en": "Includes executable deployment, manifest generation and Office administration scripts alongside domain skills."
      },
      "low_star": false
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDORXFZgQ",
    "full_name": "anthropics/financial-services",
    "stargazers_count": 41340,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30",
    "last_success_at": "2026-11-16T14:19:44.520Z"
  }
}
```

</details>

