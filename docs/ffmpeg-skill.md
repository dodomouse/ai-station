# ffmpeg-skill

[中文目录](../README.md) · [English index](../README.en.md) · [中文](#中文) · [English](#english)

GitHub：[kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill)

| 项目 / Item | 记录 / Record |
| --- | --- |
| 分类 / Category | 图像与音视频 / Images, audio and video |
| 状态 / Status | 已收录 / Included |
| Star | 10542 |
| 评估时间 / Evaluated at | 2026-11-24T16:01:11.576187Z |

## 中文

ffmpeg-skill 给编程智能体配一个本地视频编辑器。它是面向 Claude Code、Cursor、Codex 以及任何能读取 SKILL.md 的智能体的 Agent Skill，让智能体用本机 FFmpeg 剪辑素材并自行校验成片；素材不上传，不需要 API 密钥，核心只用 Python 标准库。

它帮助 AI 完成任务：智能体按固定流程（先探测、尽量无损编辑、检查、验证）执行剪辑，把自然语言需求翻译成带类型的工具调用，并在报告完成前复核输出参数。

### 主要功能

- 内置 42 个基于 ffmpeg / ffprobe 的工具：剪切拼接、静音删除、按时长与画幅适配、字幕与卡拉 OK、叠加与动态图形、HDR→SDR 与 LUT、音频清理与响度、漂移校正同步、多机位、交付检查、整段项目渲染与文件夹批处理。
- 每个工具也可作为 MCP 工具调用（默认列出核心 12 个，`FFMPEG_SKILL_MCP_FULL=1` 列出全部 42 个），并由机器可读契约描述。
- 工具的输入 schema 在运行时由同一个 argparse 解析器派生，CI 在漂移时失败（SPEC）。
- 剪辑后生成 HTML 复核页，展示素材、每步检查、成片与时间线，可在页面上写修改意见并复制回智能体；页面支持英语、日语、韩语和中文。

### 环境要求

- PATH 中需要 `ffmpeg` 与 `python3`；全部本地运行，无云端、无 API 密钥、无 Python 第三方依赖。
- `npx ffmpeg-skill setup` 需要 Node 16+ 与 Python 3.10+；setup 会为发现的智能体安装技能，必要时安装 FFmpeg，并以 doctor 收尾。
- CI 已测试 FFmpeg 6.1、7.1、8、9。语音转字幕（`caption.py --transcribe`）需另装本地语音引擎（如 `pip install faster-whisper`），首次运行下载权重，音频不上传。

### 使用限制

- 该项目是「手」而不是「脑」：它不决定剪哪里、是否可交付、什么是亮点或字幕写什么（用户给的字幕按原样烧录）。
- `doctor` 的整体 `ok` 与单个工具的 `usable` 不同：只要某工具所需组件缺失，`ok` 就为 false，即使多数工具仍可用。
- 源文件保护：目标与已声明输入相同会被拒绝；直接编辑已有输出需 `--overwrite`。

### 开始使用

1. 运行 `npx ffmpeg-skill setup` 安装技能并检查环境（`npx ffmpeg-skill doctor`）。
2. 用自然语言向智能体提需求，例如取 interview.mp4、保留指定片段并做一条 60 秒 Reel。
3. 向智能体索取复核页（`npx ffmpeg-skill review project.json --result run.json`），查看每步检查与成片后再定稿。

### 收录与来源

AI 任务用途已依据官方 README 核对：该项目作为编程智能体的本地视频编辑技能，帮助 AI 完成剪辑任务。Star 为 2026-11-24T16:01:11.576187Z 的快照，达到总量 ≥1,000 条件，eligibility=true。近期活动：[2026-11-24 · commit](https://github.com/kajisho5/ffmpeg-skill/commit/c7dad34c846099e7cf606ef943abe5e12d1ab0f9)。本次为文档复核，未安装或运行上游项目。

- [Official README](https://github.com/kajisho5/ffmpeg-skill/blob/main/README.md)
- [Website](https://kajisho5.github.io/ffmpeg-skill/)
- [Demos](https://github.com/kajisho5/ffmpeg-skill/blob/main/docs/demos.md)

## English

ffmpeg-skill gives a coding agent a local video editor. It is an Agent Skill for Claude Code, Cursor, Codex, and any agent that reads SKILL.md, letting the agent edit footage with local FFmpeg and check its own output. Nothing is uploaded, no API key is needed, and the core uses only the Python standard library.

It helps AI complete tasks: the agent follows a fixed workflow (probe, edit losslessly where possible, check, verify), turns natural-language requests into typed tool calls, and verifies output parameters before reporting success.

### Features

- 42 tools built on ffmpeg / ffprobe: cut and join, silence removal, fit to duration and aspect, captions and karaoke, overlays and motion graphics, HDR→SDR and LUTs, audio clean-up and loudness, drift-correction sync, multicam, delivery checks, whole-edit project rendering, and batch folders.
- Every tool is also callable as an MCP tool (12 core tools advertised by default; `FFMPEG_SKILL_MCP_FULL=1` lists all 42) and described by a machine-readable contract.
- Each tool's input schema is derived at runtime from the same argparse parser that defines the CLI; CI fails the build on drift (SPEC).
- After an edit, an HTML review page shows the sources, each step with its checks, the result, and a timeline; you can write what should change and copy the instruction back to the agent. The page speaks English, Japanese, Korean, and Chinese.

### Requirements

- `ffmpeg` and `python3` on PATH; everything runs locally with no cloud, no API key, and no Python third-party dependencies.
- `npx ffmpeg-skill setup` needs Node 16+ and Python 3.10+; it installs the skill for agents it finds, installs FFmpeg when missing, and ends with doctor.
- FFmpeg 6.1, 7.1, 8 and 9 are tested in CI. Captioning from speech (`caption.py --transcribe`) needs a separate local speech engine such as `pip install faster-whisper`; weights download on first run and audio never leaves the machine.

### Limitations

- This repo is the hands, not the brain: it does not decide what to cut, whether a deliverable is approvable, what makes a highlight, or what a caption should say (the user's cue text is burned as written).
- `doctor`'s overall `ok` differs from a single tool's `usable`: `ok` is false when anything some tool requires is missing, even though most tools still run.
- Source protection: a destination matching a declared input is refused, and direct edits require `--overwrite`.

### Getting started

1. Run `npx ffmpeg-skill setup` to install the skill and check the machine with `npx ffmpeg-skill doctor`.
2. Ask your agent in natural language, for example to keep two segments of interview.mp4 and make a 60-second Reel.
3. Ask the agent for the review page (`npx ffmpeg-skill review project.json --result run.json`) and inspect the checks and result before shipping.

### Review and sources

The documented AI task use was reviewed: the repo is a local video editing skill for coding agents and helps AI complete editing tasks. The Star snapshot at 2026-11-24T16:01:11.576187Z meets the 1,000 total-Star threshold; eligibility=true. Recent activity: [2026-11-24 · commit](https://github.com/kajisho5/ffmpeg-skill/commit/c7dad34c846099e7cf606ef943abe5e12d1ab0f9). This is a documentation review; the upstream software was not installed or run.

- [Official README](https://github.com/kajisho5/ffmpeg-skill/blob/main/README.md)
- [Website](https://kajisho5.github.io/ffmpeg-skill/)
- [Demos](https://github.com/kajisho5/ffmpeg-skill/blob/main/docs/demos.md)

## Review evidence

本次依据公开文章和 GitHub 官方文档复核，未安装或运行上游项目。

Reviewed against public articles and official GitHub documentation; upstream software was not installed or run.

- [GitHub activity](https://github.com/kajisho5/ffmpeg-skill/commit/c7dad34c846099e7cf606ef943abe5e12d1ab0f9) (2026-11-24T09:13:54Z)
- [Discovery article](https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA==&mid=2247538734&idx=1&sn=663aff51de396b45a5d7825f27439e6c&chksm=f9a28be7ced502f1d2d79aee06cdc63c341d4aef6baba8f94daeef6405661ea49ce76ea67c3c)

<details>
<summary>收录依据与来源 / Review evidence and sources</summary>

```json
{
  "evaluated_at": "2026-11-24T16:01:11.576187Z",
  "eligibility": {
    "status": "eligible",
    "reasons": [],
    "policy_id": "ai-activity-stars-2026-11-17",
    "admission_basis": "total_stars"
  },
  "metadata": {
    "schema_version": 1,
    "id": "ffmpeg-skill",
    "name": "ffmpeg-skill",
    "repository": "kajisho5/ffmpeg-skill",
    "repo_node_id": "R_kgDOUNQZzA",
    "category": "media",
    "summary": {
      "zh-CN": "给编程智能体使用的本地视频编辑技能，用 FFmpeg 剪辑并自动校验成片。",
      "en": "A local video editing skill for coding agents that edits footage with FFmpeg and verifies its own output."
    },
    "editorial": {
      "status": "reviewed",
      "reviewed_at": {
        "zh-CN": "2026-11-24T16:01:11.576187Z",
        "en": "2026-11-24T16:01:11.576187Z"
      },
      "verification_level": "docs"
    },
    "ai_task_relevance": {
      "supports_ai_tasks": true,
      "reason": {
        "zh-CN": "给编程智能体使用的本地视频编辑技能，用 FFmpeg 剪辑并自动校验成片。",
        "en": "A local video editing skill for coding agents that edits footage with FFmpeg and verifies its own output."
      },
      "source_url": "https://github.com/kajisho5/ffmpeg-skill/blob/main/README.md"
    },
    "activity_evidence": [
      {
        "type": "commit",
        "url": "https://github.com/kajisho5/ffmpeg-skill/commit/c7dad34c846099e7cf606ef943abe5e12d1ab0f9",
        "occurred_at": "2026-11-24T09:13:54Z",
        "reviewed_at": "2026-11-24T16:01:11.576187Z",
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
        "url": "https://github.com/kajisho5/ffmpeg-skill/blob/main/README.md"
      },
      {
        "title": "Discovery article",
        "url": "https://mp.weixin.qq.com/s?__biz=MzUxNjg4NDEzNA==&mid=2247538734&idx=1&sn=663aff51de396b45a5d7825f27439e6c&chksm=f9a28be7ced502f1d2d79aee06cdc63c341d4aef6baba8f94daeef6405661ea49ce76ea67c3c"
      }
    ]
  },
  "snapshot": {
    "full_name": "kajisho5/ffmpeg-skill",
    "repo_node_id": "R_kgDOUNQZzA",
    "stargazers_count": 10542,
    "archived": false,
    "disabled": false,
    "visibility": "public",
    "last_success_at": "2026-11-24T16:01:11.576187Z",
    "source_url": "https://api.github.com/repos/kajisho5/ffmpeg-skill"
  }
}
```

</details>
