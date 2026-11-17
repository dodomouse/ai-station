# Unsloth

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[unslothai/unsloth](https://github.com/unslothai/unsloth)

| 项目 / Field | 内容 / Value |
| --- | --- |
| 分类 / Category | AI 工具 / AI tools |
| 状态 / Status | 已收录 / Included |
| Star | 79601 |
| 许可证 / License | Apache-2.0 AND AGPL-3.0-only |
| 评估时间 / Evaluated at | 2026-11-16T14:50:50.290410+00:00 |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:20:19.542Z |

## 中文

模型运行与微调工具，覆盖语言、扩散、语音和嵌入模型，并提供本地桌面/Studio 工作流。

**环境与限制：** 支持环境取决于模型与硬件。按 Windows、macOS 或 Linux 对应安装说明配置。内存、显存和加速器要求需逐模型核对。核心代码 Apache-2.0，Studio 为 AGPL-3.0，模型权重另有条款。性能宣传未在本次审查实测。

**入门：** 从[官方说明](https://raw.githubusercontent.com/unslothai/unsloth/main/README.md)确认安装与配置步骤，再查看[发布版本](https://github.com/unslothai/unsloth/releases)。本次为文档、许可原文与维护证据审查，未安装运行。

**近期维护：** [核验 Studio 提交修复 FLUX.1 LoRA 的渲染崩溃与单块更新丢失，并增加回归测试。](https://github.com/unslothai/unsloth/commit/c08bbec4a3e1ba7566bb37d677b0a8853804a1c8)（2026-11-16）

## English

Tools for running and fine-tuning language, diffusion, speech and embedding models, including local desktop/Studio workflows.

**Requirements and limitations:** Follow platform-specific Windows, macOS or Linux setup and check each model's memory and accelerator requirements. Core code is Apache-2.0 and Studio is AGPL-3.0; model weights have separate terms. Performance claims were not benchmarked in this review.

**Getting started:** Follow the [official documentation](https://raw.githubusercontent.com/unslothai/unsloth/main/README.md) for setup, then check [releases](https://github.com/unslothai/unsloth/releases). This review examined documentation, license text and maintenance evidence; the software was not installed or run.

**Recent maintenance:** [An inspected Studio commit fixes FLUX.1 LoRA render crashes and lost single-block updates, with regression tests.](https://github.com/unslothai/unsloth/commit/c08bbec4a3e1ba7566bb37d677b0a8853804a1c8) (2026-11-16)

## Review evidence

发现线索来自第三方公众号文章索引，原始微信正文未完整读取；用途、环境、许可与维护状态依据仓库当前资料复核。

Discovery uses a third-party WeChat article index; the original article body was not fully read. Current repository sources were reviewed for function, requirements, licensing and maintenance.

- 公众号索引原文 / Indexed WeChat source：[一周没逛 GitHub 不要紧，这 TOP 10 的热门开源项目整理好了。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536122&idx=1&sn=b7a284d06296707235d8dde07c6f6d4e)（2026-08-23）

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
    "id": "unsloth",
    "name": "Unsloth",
    "repository": "unslothai/unsloth",
    "repo_node_id": "R_kgDOKznBOA",
    "category": "ai",
    "summary": {
      "zh-CN": "模型运行与微调工具，覆盖语言、扩散、语音和嵌入模型，并提供本地桌面/Studio 工作流。",
      "en": "Tools for running and fine-tuning language, diffusion, speech and embedding models, including local desktop/Studio workflows."
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
      "spdx": "Apache-2.0 AND AGPL-3.0-only",
      "osi_approved": true,
      "license_sha256": "40e0b458a68b557560def38b106a1a0da1aac57685536dcb882f1c78c647e4d3",
      "source_url": "https://github.com/unslothai/unsloth/blob/7cd8ff4126f704a5af2f6b0423b37758b491ff9d/LICENSE",
      "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
      "files": [
        {
          "path": "LICENSE",
          "source_url": "https://github.com/unslothai/unsloth/blob/7cd8ff4126f704a5af2f6b0423b37758b491ff9d/LICENSE",
          "fetched_at": "2026-11-16T14:23:40.519Z",
          "sha256": "40e0b458a68b557560def38b106a1a0da1aac57685536dcb882f1c78c647e4d3",
          "source_commit": "7cd8ff4126f704a5af2f6b0423b37758b491ff9d"
        },
        {
          "path": "COPYING",
          "source_url": "https://github.com/unslothai/unsloth/blob/d2d8823325aad4353221acaa9f8ecc4c3dd26c9f/COPYING",
          "fetched_at": "2026-11-16T14:23:40.632Z",
          "sha256": "4c5cff5c6011f8773f358bd083148fec38aa55b58d553c06e3e22f9fadd64403",
          "source_commit": "d2d8823325aad4353221acaa9f8ecc4c3dd26c9f"
        }
      ],
      "scope": "Apache-2.0 core and AGPL-3.0-only Studio software. Downloaded model weights retain their own licenses.",
      "evidence_pinned_at": "2026-11-17T03:18:39.545644+00:00",
      "evidence_status": "hash_matched",
      "source_commit": "7cd8ff4126f704a5af2f6b0423b37758b491ff9d"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-16T14:01:31Z",
        "url": "https://github.com/unslothai/unsloth/commit/c08bbec4a3e1ba7566bb37d677b0a8853804a1c8",
        "sha": "c08bbec4a3e1ba7566bb37d677b0a8853804a1c8",
        "summary": "Studio sd.cpp: FLUX.1 LoRAs no longer crash sd-server or drop single-block updates (#17962)",
        "files": [
          "studio/backend/core/inference/diffusion_lora.py",
          "studio/backend/core/inference/sd_cpp_backend.py",
          "studio/backend/core/inference/sd_cpp_server.py",
          "studio/backend/tests/test_sd_cpp_backend.py",
          "studio/backend/tests/test_sd_cpp_flux1_lora.py"
        ],
        "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
        "qualifies": true,
        "reason": {
          "zh-CN": "核验 Studio 提交修复 FLUX.1 LoRA 的渲染崩溃与单块更新丢失，并增加回归测试。",
          "en": "An inspected Studio commit fixes FLUX.1 LoRA render crashes and lost single-block updates, with regression tests."
        }
      }
    ],
    "sources": [
      {
        "article_id": "2247536122_1",
        "title": "一周没逛 GitHub 不要紧，这 TOP 10 的热门开源项目整理好了。",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247536122&idx=1&sn=b7a284d06296707235d8dde07c6f6d4e",
        "published_date": "2026-08-23",
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
        "https://api.github.com/repos/unslothai/unsloth",
        "https://raw.githubusercontent.com/unslothai/unsloth/main/README.md",
        "https://github.com/unslothai/unsloth/commit/c08bbec4a3e1ba7566bb37d677b0a8853804a1c8",
        "https://github.com/unslothai/unsloth/blob/7cd8ff4126f704a5af2f6b0423b37758b491ff9d/LICENSE"
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOKznBOA",
    "full_name": "unslothai/unsloth",
    "stargazers_count": 79601,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "40e0b458a68b557560def38b106a1a0da1aac57685536dcb882f1c78c647e4d3",
    "last_success_at": "2026-11-16T14:20:19.542Z"
  }
}
```

</details>
