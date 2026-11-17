# Not Sandboxed（Cybersecurity Projects 子项目）

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[CarterPerez-dev/Cybersecurity-Projects](https://github.com/CarterPerez-dev/Cybersecurity-Projects)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 9554 |
| 许可证 / License | AGPL-3.0-or-later |
| 评估时间 / Evaluated at | 2026-11-17T06:06:21.894839+00:00 |

## 中文

Cybersecurity Projects 中的 LLM 提示注入防护子项目，提供来源标记、工具权限策略和输出检查的 Python 库、CLI 及实验代理。

### 用途与功能

- 区分系统、用户和不可信数据来源，检查规范化文本，并为不可信数据添加每次请求独立的边界标记。
- 提供工具调用权限、参数约束、注册秘密及 URL 输出检查，用于在应用侧约束模型可产生的影响。
- 包含本地 CLI、OpenAI 兼容的实验接口和分级演示环境，帮助观察各层策略的作用。

### 环境与限制

需要 Python 3.14+，源码依赖通过 uv 管理；完整演示界面使用 Docker。核心检查和默认脚本化 MockAgent 可离线运行，不需模型密钥；代理默认也使用 MockAgent，并非自动转发到真实模型的成品网关。接入真实推理需适配 Agent 上游，输入和输出的数据流、费用由实际模型部署决定。代理仅根据消息角色推断来源，检索内容若拼进用户消息可能绕过相应入口检查；直接库接口需由宿主正确标记来源、注册工具和策略。项目为 beta，不能承诺识别所有注入或防止所有泄露。

### 开始使用

进入仓库的 PROJECTS/beginner/prompt-injection-firewall 子目录，按该目录 README 配置 Python 环境；先用 CLI 和无真实秘密的本地演示检查策略，再通过库接口接入自己的应用。目录条目只覆盖该防护子项目，整仓其他安全练习不作为本条功能。

参阅[官方 README](https://github.com/CarterPerez-dev/Cybersecurity-Projects/blob/f34a6c17ac84bca8cb515e979d7080bc8851e565/PROJECTS/beginner/prompt-injection-firewall/README.md)。

### 收录与来源

已核对组件 README、pyproject.toml、AGPL 原文、代理默认后端及 2026-10-06 实际修复：将安全响应头配置显式加入设置缓存头的 nginx 路由，并打包进镜像，避免继承规则导致页面缺少响应头。未运行上游或验证检测率；README 的百分比不作为可靠性保证。

维护证据：[修复 nginx 子路由自设缓存头后丢失安全响应头的问题，显式引入共享响应头片段并加入生产镜像](https://github.com/CarterPerez-dev/Cybersecurity-Projects/commit/2b702064e0bbb879c7b10ac09b601b1d143fe22b)（2026-10-06）。

用户于 2026-11-17 提供仓库链接。本条按工程通用标准复核，不设 Star 门槛。

本次核对了官方文档、许可原文和维护变更，未安装或运行上游项目。代码许可不自动覆盖模型权重、数据、素材和外部服务。

## English

The LLM prompt-injection defense component of Cybersecurity Projects, offering a Python library, CLI and experimental proxy for provenance, tool policies and output checks.

### Uses and features

- Track system, user and untrusted-data provenance, inspect normalized text and fence data using per-request markers.
- Provide tool authorization, argument constraints and registered-secret/URL output checks to constrain model effects at the application boundary.
- Includes a local CLI, an experimental OpenAI-compatible interface and a staged demo environment for examining policy layers.

### Requirements and limits

Requires Python 3.14+ with uv-managed source dependencies; the full demo UI uses Docker. Core checks and the default scripted MockAgent run offline without model credentials. The proxy also defaults to MockAgent rather than forwarding automatically to a real model. Real inference requires an upstream Agent integration, with data flows and costs depending on that deployment. Proxy provenance is inferred from message roles, so retrieved content pasted into a user message may bypass relevant ingress checks. Library users must correctly declare provenance, register tools and configure policies. This beta project does not guarantee complete injection detection or leak prevention.

### Getting started

Open PROJECTS/beginner/prompt-injection-firewall and follow its README to configure Python. Start with CLI checks and the local demo without real secrets, then integrate the library into your application. This entry covers only this defense component, not the repository’s other security exercises.

See the [official README](https://github.com/CarterPerez-dev/Cybersecurity-Projects/blob/f34a6c17ac84bca8cb515e979d7080bc8851e565/PROJECTS/beginner/prompt-injection-firewall/README.md).

### Review and provenance

Reviewed the component README, pyproject.toml, AGPL text, default proxy backend and the 2026-10-06 fix that explicitly includes security headers in nginx locations setting cache headers and packages the snippet in the image, preventing inheritance from dropping those headers. Upstream code and detection-rate benchmarks were not run; advertised percentages are not treated as reliability guarantees.

Maintenance evidence: [Fixes security headers lost when nginx locations set cache headers by including a shared header snippet and shipping it in the production image](https://github.com/CarterPerez-dev/Cybersecurity-Projects/commit/2b702064e0bbb879c7b10ac09b601b1d143fe22b) (2026-10-06).

Submitted by the user on 2026-11-17 and reviewed against the general catalog criteria, with no star threshold.

This review checked official documentation, license text and maintenance changes; the upstream software was not installed or run. The code license does not automatically cover model weights, data, assets or external services.

## Review evidence

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-17T06:06:21.894839+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "cybersecurity-projects",
    "name": "Not Sandboxed（Cybersecurity Projects 子项目）",
    "repository": "CarterPerez-dev/Cybersecurity-Projects",
    "repo_node_id": "R_kgDOQRgy4w",
    "category": "ai",
    "summary": {
      "zh-CN": "Cybersecurity Projects 中的 LLM 提示注入防护子项目，提供来源标记、工具权限策略和输出检查的 Python 库、CLI 及实验代理。",
      "en": "The LLM prompt-injection defense component of Cybersecurity Projects, offering a Python library, CLI and experimental proxy for provenance, tool policies and output checks."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-17T06:06:21.894839+00:00",
        "en": "2026-11-17T06:06:21.894839+00:00"
      },
      "verification_level": "docs"
    },
    "quality_review": {
      "zh-CN": "已核对组件 README、pyproject.toml、AGPL 原文、代理默认后端及 2026-10-06 实际修复：将安全响应头配置显式加入设置缓存头的 nginx 路由，并打包进镜像，避免继承规则导致页面缺少响应头。未运行上游或验证检测率；README 的百分比不作为可靠性保证。",
      "en": "Reviewed the component README, pyproject.toml, AGPL text, default proxy backend and the 2026-10-06 fix that explicitly includes security headers in nginx locations setting cache headers and packages the snippet in the image, preventing inheritance from dropping those headers. Upstream code and detection-rate benchmarks were not run; advertised percentages are not treated as reliability guarantees.",
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "AGPL-3.0-or-later",
      "osi_approved": true,
      "source_url": "https://github.com/CarterPerez-dev/Cybersecurity-Projects/blob/f34a6c17ac84bca8cb515e979d7080bc8851e565/PROJECTS/beginner/prompt-injection-firewall/LICENSE",
      "license_sha256": "8486a10c4393cee1c25392769ddd3b2d6c242d6ec7928e1414efff7dfb2f07ef",
      "source_commit": "f34a6c17ac84bca8cb515e979d7080bc8851e565",
      "reviewed_at": "2026-11-17T06:06:21.894839+00:00",
      "evidence_pinned_at": "2026-11-17T06:06:21.894839+00:00",
      "evidence_status": "hash_matched",
      "scope_note": "AGPL-3.0-or-later applies to the reviewed Not Sandboxed component at PROJECTS/beginner/prompt-injection-firewall, as stated in its README and pyproject.toml and backed by its LICENSE. This catalog scope does not certify the other security projects, externally supplied model services, datasets or assets."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-10-06T00:29:49Z",
        "reviewed_at": "2026-11-17T06:06:21.894839+00:00",
        "url": "https://github.com/CarterPerez-dev/Cybersecurity-Projects/commit/2b702064e0bbb879c7b10ac09b601b1d143fe22b",
        "qualifies": true,
        "reason": {
          "zh-CN": "修复 nginx 子路由自设缓存头后丢失安全响应头的问题，显式引入共享响应头片段并加入生产镜像",
          "en": "Fixes security headers lost when nginx locations set cache headers by including a shared header snippet and shipping it in the production image"
        },
        "reviewed_files": [
          "PROJECTS/beginner/prompt-injection-firewall/infra/nginx/prod.nginx",
          "PROJECTS/beginner/prompt-injection-firewall/infra/nginx/security-headers.conf",
          "PROJECTS/beginner/prompt-injection-firewall/infra/docker/vite.prod"
        ]
      }
    ],
    "sources": [
      {
        "url": "https://github.com/CarterPerez-dev/Cybersecurity-Projects",
        "accessed_at": "2026-11-17T06:06:21.894839+00:00"
      },
      {
        "url": "https://github.com/CarterPerez-dev/Cybersecurity-Projects/blob/f34a6c17ac84bca8cb515e979d7080bc8851e565/PROJECTS/beginner/prompt-injection-firewall/README.md",
        "accessed_at": "2026-11-17T06:06:21.894839+00:00"
      },
      {
        "url": "https://github.com/CarterPerez-dev/Cybersecurity-Projects/blob/f34a6c17ac84bca8cb515e979d7080bc8851e565/PROJECTS/beginner/prompt-injection-firewall/LICENSE",
        "accessed_at": "2026-11-17T06:06:21.894839+00:00"
      },
      {
        "url": "https://github.com/CarterPerez-dev/Cybersecurity-Projects/commit/2b702064e0bbb879c7b10ac09b601b1d143fe22b",
        "accessed_at": "2026-11-17T06:06:21.894839+00:00"
      },
      {
        "url": "https://github.com/CarterPerez-dev/Cybersecurity-Projects/blob/f34a6c17ac84bca8cb515e979d7080bc8851e565/PROJECTS/beginner/prompt-injection-firewall/pyproject.toml",
        "accessed_at": "2026-11-17T06:06:21.894839+00:00"
      },
      {
        "url": "https://github.com/CarterPerez-dev/Cybersecurity-Projects/blob/f34a6c17ac84bca8cb515e979d7080bc8851e565/PROJECTS/beginner/prompt-injection-firewall/src/not_sandboxed/proxy/app.py",
        "accessed_at": "2026-11-17T06:06:21.894839+00:00"
      }
    ],
    "discovery": {
      "kind": "user_submission",
      "submitted_date": "2026-11-17",
      "source_url": "https://github.com/CarterPerez-dev/Cybersecurity-Projects",
      "repository_url": "https://github.com/CarterPerez-dev/Cybersecurity-Projects"
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOQRgy4w",
    "full_name": "CarterPerez-dev/Cybersecurity-Projects",
    "stargazers_count": 9554,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "AGPL-3.0-or-later",
    "api_license_spdx": "AGPL-3.0",
    "license_sha256": "8486a10c4393cee1c25392769ddd3b2d6c242d6ec7928e1414efff7dfb2f07ef",
    "last_success_at": "2026-11-17T05:56:56.376156+00:00"
  }
}
```

</details>
