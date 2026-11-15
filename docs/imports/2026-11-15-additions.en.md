# Additions and refresh: 2026-11-15

[简体中文](2026-11-15-additions.md)

Processed seven requested repositories: three added and four existing entries refreshed. The catalog now has 62 unique projects, 124 language documents and 62 GitHub snapshots. At this evaluation, 35 qualify for the default catalog and 27 remain candidates.

Evaluated at: 2026-11-15T11:54:08.129868Z

| Project | Action | Stars | Status | Notes |
| --- | --- | ---: | --- | --- |
| [Eynnzerr/TelemetryCleaner](../../tools/telemetrycleaner/README.en.md) | added | 807 | ineligible | Below 1000 Stars; MIT and functional activity in the window verified. |
| [shidenggui/easyquotation](../../tools/easyquotation/README.en.md) | added | 5478 | needs_review | Latest default-branch change is documentation dated 2026-02-28. |
| [hsliuping/TradingAgents-CN](../../tools/tradingagents-cn/README.en.md) | added | 32957 | unknown | The application layer is proprietary; the complete app is not wholly open source. |
| [KKKKhazix/agent-autoloop](../../tools/agent-autoloop/README.en.md) | refreshed | 5427 | eligible | Existing entry; identity and license fingerprint match. Snapshot refreshed; valid maintenance evidence retained. |
| [yetone/magpie](../../tools/magpie/README.en.md) | refreshed | 36740 | eligible | Existing entry; identity and license fingerprint match. Snapshot refreshed; valid maintenance evidence retained. |
| [debpalash/VoiceStudio](../../tools/voicestudio/README.en.md) | refreshed | 110994 | eligible | Existing entry; identity and license fingerprint match. Snapshot refreshed; valid maintenance evidence retained. |
| [simonlin1212/Vibe-Research](../../tools/vibe-research/README.en.md) | refreshed | 3720 | eligible | Existing entry; identity and license fingerprint match. Snapshot refreshed; valid maintenance evidence retained. |

## Interpretation

All three new entries have bilingual descriptions and sources. TelemetryCleaner misses the Star threshold, easyquotation lacks recent maintenance, and TradingAgents-CN has mixed licensing. Candidates remain searchable; inclusion rules are unchanged.

`unknown` is the existing evaluator’s result when it first encounters unsupported license evidence. TradingAgents-CN’s proprietary application layer is explicit in LICENSE, not inferred from NOASSERTION. easyquotation’s MIT/BSD packaging discrepancy is documented in its entry.

New entries were reviewed against official documentation, licenses and selected code. The four existing entries had identity, Stars, state and license files rechecked; their historical Chinese cards were preserved. No project was installed, device package changed, quote requested, model called or trade executed.

[Structured record](../../data/imports/2026-11-15-additions.json) · [Initial 59-entry import](2026-11-15.en.md)

Snapshots expire after seven days. Historical evaluations need the matching Git revision and snapshots; refreshed data does not describe an earlier instant.

```bash
python3 scripts/catalog.py search telemetrycleaner --all
python3 scripts/catalog.py search easyquotation --all
python3 scripts/catalog.py search tradingagents-cn --all --lang en
python3 scripts/catalog.py search --all --json
```
