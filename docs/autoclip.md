# AutoClip

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[zhouxiaoka/autoclip](https://github.com/zhouxiaoka/autoclip)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 15521 |
| 评估时间 / Evaluated at | 2026-11-25T04:00:16.782403Z |

## 中文

AutoClip 是一款本地优先的开源 AI 视频剪辑工具：输入视频链接、本地文件或直播回放，自动找出精彩片段、跟踪说话人、烧录字幕、生成封面与标题，并导出适配抖音、小红书、TikTok、Reels、YouTube Shorts 等平台的成片。

它把播客、访谈、课程和游戏直播的长视频转成可发布的短视频，适合需要批量制作字幕、封面和发布文案的 AI 内容工作流。

### 主要功能

- 自动挑选片段、跟踪说话人、烧录字幕、生成封面，并一键切换目标平台重新导出，不丢失之前的导出结果。
- 支持链接、本地文件与直播回放；v1.6 提供 OBS Studio、Twitch、YouTube、Kick、Discord 和本地录像六种回放来源，可通过 OBS WebSocket（4455）自动截取并在直播结束后无损裁剪入队。
- 游戏高光检测支持 8 秒以上的独立片段，并收紧视觉/OCR 预算；提供 CLI 与 MCP（`io.github.zhouxiaoka/autoclip-mcp`），可用于 Claude Code、Codex、OpenCode 等智能体。
- 可配自有 API 密钥使用云分析，也可完全离线运行 Ollama / LM Studio 加 Whisper / SenseVoice；桌面界面与文档支持 13 种语言。

### 环境要求

- 桌面应用：从 Releases 下载 `.dmg` 或 `-setup.exe`，适用于 Apple Silicon macOS 或 Windows 10/11 x64，已内置 Python 与 FFmpeg。
- CLI / MCP：`uvx autoclip-mcp` 或 `npx skills add zhouxiaoka/autoclip`，需要 Python 3.10+（推荐 3.11）与 FFmpeg。自托管/Linux/Intel Mac 需要 Docker 与 Compose v2。
- 云分析、转写与 AI 封面按所选服务提供方配置自己的 API 密钥并按量计费；基础示例无需密钥，Ollama / LM Studio 本地模型也不需要云端密钥。直接发布使用用户自己的 Bilibili 或 Upload-Post 账号。

### 使用限制

- 剪辑与渲染在本地完成，但云分析只发送转写文本、视觉模型只接收抽帧、云 ASR 会上传音频；只有使用本地 LLM 加 Whisper / SenseVoice 才能完全离线。
- 无字幕视频可改用本地 Whisper / SenseVoice 或云 ASR；游戏或低对话直播需要启用视觉模型。生成失败需依次检查字幕/转写、模型连接、FFmpeg、磁盘空间与平台时长限制。
- 桌面安装包的代码签名与 Apple 公证仍在 issue #119 跟进；素材版权归原作者所有。

### 开始使用

1. 桌面应用：从 [GitHub Releases](https://github.com/zhouxiaoka/autoclip/releases/latest) 下载安装包，在设置中选择云提供方或启动 Ollama / LM Studio，测试连接后保存；也可点击内置示例免密钥试用。粘贴链接、拖入文件或切换到直播回放，选择平台后点击生成。
2. CLI / MCP：运行 `uvx autoclip-mcp` 与 `npx skills add zhouxiaoka/autoclip`，用 `autoclip produce talk.mp4 --srt talk.srt --platform tiktok --portrait-style podcast --json` 生成，再用 `autoclip outputs PROJECT_ID --export-kits` 导出。
3. 自托管：克隆仓库，执行 `cp env.example .env`、`mkdir -p data logs uploads` 与 `docker compose up -d --build`，打开 `http://localhost:3000`（API 文档在 `http://localhost:8000/docs`）。

### 收录与来源

AI 任务用途已依据官方 README 核对。Star 为 2026-11-25T04:00:16.782403Z 的快照，达到总量 ≥1,000 条件。

近期活动：[2026-11-24 · commit](https://github.com/zhouxiaoka/autoclip/commit/9e62c07c5770b1206bbd5ecea8304e82e8bb1c5c)，自定义模型请求头、推理力度与请求参数（#643）。

本次为文档复核，未安装或运行上游项目。上述提交证明窗口内活动，不代表软件运行验证。许可不作为本次准入条件。

- [Official README](https://github.com/zhouxiaoka/autoclip/blob/main/README.md)
- [GitHub API snapshot](https://api.github.com/repos/zhouxiaoka/autoclip)
- [Recent commit](https://github.com/zhouxiaoka/autoclip/commit/9e62c07c5770b1206bbd5ecea8304e82e8bb1c5c)

## English

AutoClip is an open-source, local-first AI video clipping tool. Give it a link, a local file, or a live-stream replay and it finds the best moments, tracks the speaker, burns in captions, generates covers and titles, and exports ready-to-post clips for Douyin, Xiaohongshu, TikTok, Reels, and YouTube Shorts.

It turns long podcasts, interviews, courses, and game streams into short videos, supporting AI content workflows that need captions, covers, and post copy at scale.

### Features

- Automatically picks clips, tracks the speaker, burns in captions, and generates covers; one-click repurposing switches target platforms without losing earlier exports.
- Accepts links, local files, and live replays; v1.6 adds six replay sources (OBS Studio, Twitch, YouTube, Kick, Discord, local recordings), OBS WebSocket (4455) auto-capture with lossless `-c copy` trimming, and auto-queuing after a stream ends.
- Game highlight detection handles standalone plays of 8s or more with tighter vision/OCR budgets; a CLI and MCP server (`io.github.zhouxiaoka/autoclip-mcp`) work with Claude Code, Codex, OpenCode, and other agents.
- Cloud analysis works with your own API keys, or run fully offline with Ollama / LM Studio plus Whisper / SenseVoice; the desktop UI and docs cover 13 languages.

### Requirements

- Desktop app: download `.dmg` or `-setup.exe` from Releases for Apple Silicon macOS or Windows 10/11 x64; Python and FFmpeg are bundled.
- CLI / MCP: `uvx autoclip-mcp` or `npx skills add zhouxiaoka/autoclip` requires Python 3.10+ (3.11 recommended) and FFmpeg. Self-hosting on Linux or Intel Mac requires Docker with Compose v2.
- Cloud analysis, transcription, and AI covers require an API key for the provider you choose and are billed by that provider; the built-in example needs no key, and local Ollama / LM Studio models need no cloud key. Direct publishing uses your own Bilibili or Upload-Post account.

### Limitations

- Cutting and rendering run locally, but cloud analysis sends only transcript text, vision models receive sampled frames, and cloud ASR uploads audio; full offline operation requires local LLMs plus Whisper / SenseVoice.
- Videos without subtitles need local Whisper / SenseVoice or cloud ASR; game or low-dialogue streams need a vision-capable model. Empty output requires checking subtitles/transcription, model connection, FFmpeg, disk space, and platform length limits in order.
- Installer code signing and Apple notarization are tracked in issue #119; source copyrights remain with the original creators.

### Getting started

1. Desktop: download the installer from [GitHub Releases](https://github.com/zhouxiaoka/autoclip/releases/latest), pick a cloud provider or start Ollama / LM Studio in Settings, test and save — or try the built-in example with no API key. Paste a link, drop a file, or open Live Replay, choose platforms, and click Generate.
2. CLI / MCP: run `uvx autoclip-mcp` and `npx skills add zhouxiaoka/autoclip`, then use `autoclip produce talk.mp4 --srt talk.srt --platform tiktok --portrait-style podcast --json` and `autoclip outputs PROJECT_ID --export-kits`.
3. Self-hosting: clone the repo, run `cp env.example .env`, `mkdir -p data logs uploads`, and `docker compose up -d --build`, then open `http://localhost:3000` (API docs at `http://localhost:8000/docs`).

### Review and sources

The documented AI task use was reviewed. The Star snapshot at 2026-11-25T04:00:16.782403Z meets the total-Star threshold of 1,000.

Recent activity: [2026-11-24 · commit](https://github.com/zhouxiaoka/autoclip/commit/9e62c07c5770b1206bbd5ecea8304e82e8bb1c5c), covering custom model headers, reasoning effort, and request parameters (#643).

This is a documentation review; the upstream software was not installed or run. The cited commit establishes activity within the review window, not runtime validation. Licensing is not an admission criterion.

- [Official README](https://github.com/zhouxiaoka/autoclip/blob/main/README.md)
- [GitHub API snapshot](https://api.github.com/repos/zhouxiaoka/autoclip)
- [Recent commit](https://github.com/zhouxiaoka/autoclip/commit/9e62c07c5770b1206bbd5ecea8304e82e8bb1c5c)

## Review evidence

本次从 GitHub Trending 日榜发现项目，并依据 GitHub 官方文档复核，未安装或运行上游项目。榜单显示的今日新增 Star 仅用于挑选复核对象，不作为近一个月净增证据。

Discovered on GitHub Trending daily and reviewed against official GitHub documentation; upstream software was not installed or run. Today's stars select review candidates, not evidence of net growth over a calendar month.

- [GitHub activity](https://github.com/zhouxiaoka/autoclip/commit/9e62c07c5770b1206bbd5ecea8304e82e8bb1c5c) (2026-11-24T13:47:06Z)
- [GitHub Trending daily](https://github.com/trending?since=daily)

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-25T04:00:16.782403Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "autoclip",
    "name": "AutoClip",
    "repository": "zhouxiaoka/autoclip",
    "repo_node_id": "R_kgDOPIwfLw",
    "category": "media",
    "summary": {
      "zh-CN": "AutoClip 把播客、访谈、直播等长视频自动剪成带字幕、封面与标题的短视频，导出到抖音、小红书、TikTok、Reels 与 YouTube Shorts。",
      "en": "AutoClip turns podcasts, interviews, and stream replays into ready-to-post short videos with captions, covers, and titles for Douyin, Xiaohongshu, TikTok, Reels, and YouTube Shorts."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-25T04:00:16.782403Z",
        "en": "2026-11-25T04:00:16.782403Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "AutoClip 把播客、访谈、直播等长视频自动剪成带字幕、封面与标题的短视频，导出到抖音、小红书、TikTok、Reels 与 YouTube Shorts。",
        "en": "AutoClip turns podcasts, interviews, and stream replays into ready-to-post short videos with captions, covers, and titles for Douyin, Xiaohongshu, TikTok, Reels, and YouTube Shorts."
      },
      "source_url": "https://github.com/zhouxiaoka/autoclip/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/zhouxiaoka/autoclip/commit/9e62c07c5770b1206bbd5ecea8304e82e8bb1c5c",
        "occurred_at": "2026-11-24T13:47:06Z",
        "reviewed_at": "2026-11-25T04:00:16.782403Z",
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
        "url": "https://github.com/zhouxiaoka/autoclip/blob/main/README.md"
      },
      {
        "title": "GitHub Trending daily",
        "url": "https://github.com/trending?since=daily"
      }
    ]
  },
  "snapshot": {
    "full_name": "zhouxiaoka/autoclip",
    "repo_node_id": "R_kgDOPIwfLw",
    "stargazers_count": 15521,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-25T04:00:16.782403Z",
    "source_url": "https://api.github.com/repos/zhouxiaoka/autoclip"
  }
}
```

</details>
