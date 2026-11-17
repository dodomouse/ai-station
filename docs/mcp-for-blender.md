# MCP for Blender

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[ahujasid/mcp-for-blender](https://github.com/ahujasid/mcp-for-blender)

| 项目 / Field | 内容 / Value |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 34616 |
| 许可证 / License | MIT |
| 评估时间 / Evaluated at | 2026-11-16T14:50:50.290410+00:00 |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:21:49.729Z |

## 中文

通过 MCP 把 Agent 连接到 Blender，用自然语言组织场景、模型、材质和渲染，并接入可选素材服务。

**环境与限制：** 需要 Blender、Python 3.10+、uv 和支持 MCP 的客户端，安装插件并运行本地服务。工具能执行 Blender 代码，应只连接可信客户端；第三方素材/API 可能收费，本项目不是 Blender 官方插件。

**入门：** 从[官方说明](https://raw.githubusercontent.com/ahujasid/mcp-for-blender/main/README.md)确认安装与配置步骤，再查看[发布版本](https://github.com/ahujasid/mcp-for-blender/releases)。本次为文档、许可原文与维护证据审查，未安装运行。

**近期维护：** [提交修复默认渲染选择，使其渲染场景而非视口。](https://github.com/ahujasid/mcp-for-blender/commit/b6a2ce30c14636a562b5549684d9db6fc01f29ab)（2026-11-15）

## English

Connects agents to Blender through MCP for scenes, models, materials and rendering, with optional asset-service integrations.

**Requirements and limitations:** Requires Blender, Python 3.10+, uv and an MCP client, plus an installed add-on and local service. Tools can execute Blender code, so connect trusted clients. Third-party assets or APIs may charge fees; this is not an official Blender add-on.

**Getting started:** Follow the [official documentation](https://raw.githubusercontent.com/ahujasid/mcp-for-blender/main/README.md) for setup, then check [releases](https://github.com/ahujasid/mcp-for-blender/releases). This review examined documentation, license text and maintenance evidence; the software was not installed or run.

**Recent maintenance:** [The inspected commit makes the default render target the scene rather than the viewport.](https://github.com/ahujasid/mcp-for-blender/commit/b6a2ce30c14636a562b5549684d9db6fc01f29ab) (2026-11-15)

## Review evidence

发现线索来自第三方公众号文章索引，原始微信正文未完整读取；用途、环境、许可与维护状态依据仓库当前资料复核。

Discovery uses a third-party WeChat article index; the original article body was not fully read. Current repository sources were reviewed for function, requirements, licensing and maintenance.

- 公众号索引原文 / Indexed WeChat source：[最近火出圈的 GPT-6 Astra + 3D 玩法，很多都基于这个神级开源 MCP。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536724&idx=1&sn=f31a6e255ca663a00167fba0e83dd64a)（2026-09-07）

<details>
<summary>可核验快照 / Verifiable snapshot</summary>

```json
{
  "evaluated_at": "2026-11-16T14:50:50.290410+00:00",
  "eligibility": {
    "status": "eligible",
    "reasons": []
  },
  "metadata": {
    "schema_version": 1,
    "id": "mcp-for-blender",
    "name": "MCP for Blender",
    "repository": "ahujasid/mcp-for-blender",
    "repo_node_id": "R_kgDOOEqgHw",
    "category": "media",
    "summary": {
      "zh-CN": "通过 MCP 把 Agent 连接到 Blender，用自然语言组织场景、模型、材质和渲染，并接入可选素材服务。",
      "en": "Connects agents to Blender through MCP for scenes, models, materials and rendering, with optional asset-service integrations."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-16T14:50:50.290410+00:00",
        "en": "2026-11-16T14:50:50.290410+00:00"
      },
      "verification_level": "docs"
    },
    "license_review": {
      "spdx": "MIT",
      "osi_approved": true,
      "license_sha256": "049501fd54d27852507853a5b88094ca1c6ff97404418a5032f3310eecc9cde6",
      "source_url": "https://github.com/ahujasid/mcp-for-blender/blob/b6a2ce30c14636a562b5549684d9db6fc01f29ab/LICENSE",
      "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
      "files": [
        {
          "path": "LICENSE",
          "source_url": "https://github.com/ahujasid/mcp-for-blender/blob/b6a2ce30c14636a562b5549684d9db6fc01f29ab/LICENSE",
          "fetched_at": "2026-11-16T14:23:40.518Z",
          "sha256": "049501fd54d27852507853a5b88094ca1c6ff97404418a5032f3310eecc9cde6",
          "source_commit": "b6a2ce30c14636a562b5549684d9db6fc01f29ab"
        }
      ],
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "b6a2ce30c14636a562b5549684d9db6fc01f29ab"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-15T13:56:12Z",
        "url": "https://github.com/ahujasid/mcp-for-blender/commit/b6a2ce30c14636a562b5549684d9db6fc01f29ab",
        "sha": "b6a2ce30c14636a562b5549684d9db6fc01f29ab",
        "summary": "fix: make render default to see the scene instead of viewport",
        "files": [
          "pyproject.toml",
          "src/blender_mcp/blender_scripts.py",
          "src/blender_mcp/server.py",
          "tests/test_look_telemetry.py",
          "uv.lock"
        ],
        "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
        "qualifies": true,
        "reason": {
          "zh-CN": "提交修复默认渲染选择，使其渲染场景而非视口。",
          "en": "The inspected commit makes the default render target the scene rather than the viewport."
        }
      }
    ],
    "sources": [
      {
        "article_id": "2247536724_1",
        "title": "最近火出圈的 GPT-6 Astra + 3D 玩法，很多都基于这个神级开源 MCP。",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536724&idx=1&sn=f31a6e255ca663a00167fba0e83dd64a",
        "published_date": "2026-09-07",
        "account": "逛逛GitHub",
        "source_strength": "third_party_index",
        "index_url": "https://www.noking.tech/github-radar/data/library.json",
        "original_article_body_read": false
      }
    ],
    "discovery": {
      "account": "逛逛GitHub",
      "window_start": "2026-08-16",
      "window_end": "2026-11-16",
      "original_article_body_read": false,
      "repository_review_sources": [
        "https://api.github.com/repos/ahujasid/mcp-for-blender",
        "https://raw.githubusercontent.com/ahujasid/mcp-for-blender/main/README.md",
        "https://github.com/ahujasid/mcp-for-blender/commit/b6a2ce30c14636a562b5549684d9db6fc01f29ab",
        "https://github.com/ahujasid/mcp-for-blender/blob/b6a2ce30c14636a562b5549684d9db6fc01f29ab/LICENSE"
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOOEqgHw",
    "full_name": "ahujasid/mcp-for-blender",
    "stargazers_count": 34616,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "MIT",
    "license_sha256": "049501fd54d27852507853a5b88094ca1c6ff97404418a5032f3310eecc9cde6",
    "last_success_at": "2026-11-16T14:21:49.729Z"
  }
}
```

</details>
