# ArtCraft

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[storytold/artcraft](https://github.com/storytold/artcraft)

| 项目 / Field | 内容 / Value |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 41207 |
| 许可证 / License | MIT OR Apache-2.0 |
| 评估时间 / Evaluated at | 2026-11-16T14:50:50.290410+00:00 |
| 快照时间 / Snapshot fetched at | 2026-11-16T14:19:22.186Z |

## 中文

桌面 AI 创作工作台，结合二维画面编排、三维场景和图像/视频模型，组织生成素材与创作流程。

**环境与限制：** 提供 macOS、Windows、Linux 工作流，具体安装包以 Releases 为准。模型端点、账号和费用另行配置，第三方素材与模型受各自许可约束。

**入门：** 从[官方说明](https://raw.githubusercontent.com/storytold/artcraft/main/README.md)确认安装与配置步骤，再查看[发布版本](https://github.com/storytold/artcraft/releases)。本次为文档、许可原文与维护证据审查，未安装运行。

**近期维护：** [提交统一图像、音频、视频和 3D 文件签名识别，包含实际 Rust 实现变更。](https://github.com/storytold/artcraft/commit/69f53c2f0358a91a5e35e5a7b3a91677320c3112)（2026-11-16）

## English

A desktop AI creation workspace combining 2D composition, 3D scenes and image/video models to organize generative media workflows.

**Requirements and limitations:** Provides macOS, Windows and Linux workflows; consult Releases for available installers. Model endpoints, accounts and costs are separate, and third-party assets and models retain their own licenses.

**Getting started:** Follow the [official documentation](https://raw.githubusercontent.com/storytold/artcraft/main/README.md) for setup, then check [releases](https://github.com/storytold/artcraft/releases). This review examined documentation, license text and maintenance evidence; the software was not installed or run.

**Recent maintenance:** [The inspected commit unifies image, audio, video and 3D file-signature detection in Rust.](https://github.com/storytold/artcraft/commit/69f53c2f0358a91a5e35e5a7b3a91677320c3112) (2026-11-16)

## Review evidence

发现线索来自第三方公众号文章索引，原始微信正文未完整读取；用途、环境、许可与维护状态依据仓库当前资料复核。

Discovery uses a third-party WeChat article index; the original article body was not fully read. Current repository sources were reviewed for function, requirements, licensing and maintenance.

- 公众号索引原文 / Indexed WeChat source：[盘点本周 11 个 Star 攀升最多的 GitHub 开源项目。](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537903&idx=1&sn=69b07453177c4c06c464245954d7e217)（2026-10-21）
- 作者署名转载 / Author-attributed repost：[盘点本周 11 个 Star 攀升最多的 GitHub 开源项目。](https://www.woshipm.com/ai/6482138.html)（2026-10-22）；仓库链接映射已交叉核对 / repository mapping corroborated.

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
    "id": "artcraft",
    "name": "ArtCraft",
    "repository": "storytold/artcraft",
    "repo_node_id": "R_kgDOHGbvPA",
    "category": "media",
    "summary": {
      "zh-CN": "桌面 AI 创作工作台，结合二维画面编排、三维场景和图像/视频模型，组织生成素材与创作流程。",
      "en": "A desktop AI creation workspace combining 2D composition, 3D scenes and image/video models to organize generative media workflows."
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
      "spdx": "MIT OR Apache-2.0",
      "osi_approved": true,
      "license_sha256": "0d542e0c8804e39aa7f37eb00da5a762149dc682d7829451287e11b938e94594",
      "source_url": "https://raw.githubusercontent.com/storytold/artcraft/main/LICENSE-APACHE",
      "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
      "files": [
        {
          "path": "LICENSE-APACHE",
          "source_url": "https://raw.githubusercontent.com/storytold/artcraft/main/LICENSE-APACHE",
          "fetched_at": "2026-11-16T14:23:16.939Z",
          "sha256": "0d542e0c8804e39aa7f37eb00da5a762149dc682d7829451287e11b938e94594"
        },
        {
          "path": "LICENSE-MIT",
          "source_url": "https://raw.githubusercontent.com/storytold/artcraft/main/LICENSE-MIT",
          "fetched_at": "2026-11-16T14:23:17.090Z",
          "sha256": "8ce608753585920ec5b61e8f324b0b205ca345e663a92850f4ef0b4240c3f49c"
        }
      ],
      "scope": "Original code is offered under MIT OR Apache-2.0; third-party assets and model services retain separate terms."
    },
    "activity_evidence": [
      {
        "type": "commit",
        "occurred_at": "2026-11-16T13:20:58Z",
        "url": "https://github.com/storytold/artcraft/commit/69f53c2f0358a91a5e35e5a7b3a91677320c3112",
        "sha": "69f53c2f0358a91a5e35e5a7b3a91677320c3112",
        "summary": "Detect image, audio, video and 3D file types with the shared craft-sniff table (#2862)",
        "files": [
          "Cargo.lock",
          "crates/lib/files/mimetypes/Cargo.toml",
          "crates/lib/files/mimetypes/src/custom/custom_infer.rs",
          "crates/lib/files/mimetypes/src/custom/mod.rs",
          "crates/lib/files/mimetypes/src/lib.rs",
          "crates/lib/files/mimetypes/src/mimetype_for_bytes.rs",
          "crates/lib/files/mimetypes/src/mimetype_for_file.rs",
          "crates/lib/files/mimetypes/src/mimetype_info/mimetype_info.rs"
        ],
        "reviewed_at": "2026-11-16T14:50:50.290410+00:00",
        "qualifies": true,
        "reason": {
          "zh-CN": "提交统一图像、音频、视频和 3D 文件签名识别，包含实际 Rust 实现变更。",
          "en": "The inspected commit unifies image, audio, video and 3D file-signature detection in Rust."
        }
      }
    ],
    "sources": [
      {
        "article_id": "2247537903_1",
        "title": "盘点本周 11 个 Star 攀升最多的 GitHub 开源项目。",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA%3D%3D&mid=2247537903&idx=1&sn=69b07453177c4c06c464245954d7e217",
        "published_date": "2026-10-21",
        "account": "逛逛GitHub",
        "source_strength": "third_party_index",
        "index_url": "https://www.noking.tech/github-radar/data/library.json",
        "original_article_body_read": false
      },
      {
        "url": "https://www.woshipm.com/ai/6482138.html",
        "title": "盘点本周 11 个 Star 攀升最多的 GitHub 开源项目。",
        "published_date": "2026-10-22",
        "account": "逛逛GitHub",
        "source_strength": "author_attributed_repost_repository_mapping",
        "author_attribution_confirmed": true,
        "body_read_method": "public_html_repository_links_and_attribution_extraction",
        "full_text_archived": false
      }
    ],
    "discovery": {
      "account": "逛逛GitHub",
      "window_start": "2026-08-16",
      "window_end": "2026-11-16",
      "original_article_body_read": false,
      "repository_review_sources": [
        "https://api.github.com/repos/storytold/artcraft",
        "https://raw.githubusercontent.com/storytold/artcraft/main/README.md",
        "https://github.com/storytold/artcraft/commit/69f53c2f0358a91a5e35e5a7b3a91677320c3112",
        "https://raw.githubusercontent.com/storytold/artcraft/main/LICENSE-APACHE"
      ]
    }
  },
  "snapshot": {
    "schema_version": 1,
    "repo_node_id": "R_kgDOHGbvPA",
    "full_name": "storytold/artcraft",
    "stargazers_count": 41207,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "license_spdx": "Apache-2.0",
    "license_sha256": "0d542e0c8804e39aa7f37eb00da5a762149dc682d7829451287e11b938e94594",
    "last_success_at": "2026-11-16T14:19:22.186Z"
  }
}
```

</details>
