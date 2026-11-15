# TelemetryCleaner

[简体中文](README.zh-CN.md) | English

TelemetryCleaner manages known carrier components preinstalled on Android devices. Through Shizuku, it inspects package states across user spaces and provides permission inspection, per-space removal, restoration and disabling controls. It is intended for users investigating preinstalled packages and deciding whether to change their state.

This entry remains a candidate because it was below the catalog's 1000-Star threshold when reviewed. See the [GitHub snapshot](../../data/github/telemetrycleaner.json) and use `search telemetrycleaner --all` to find it.

## Use cases

- Check whether a device contains carrier packages in the bundled directory.
- Inspect installation states and permission records across Android user spaces.
- Manage selected components after assessing their role, then inspect the reported outcome.

## Features

| Feature | Scope and behavior |
| --- | --- |
| Known-package detection | Checks a bundled package-name list, including SystemHelper, RegService and selected vendor components. It does not analyze every app's behavior. |
| Permission inspection | Reads Android package-manager declarations and grant records. These do not prove that a package actually accessed or transmitted data. |
| Per-space removal | Operates on selected spaces and rereads package state to confirm the result. Removal clears component data in those spaces. |
| Disable fallback | v1.3 adds an option, enabled by default, to try disabling after a manual uninstall fails. Disabling retains existing data and caches. |
| Restoration | Can re-enable manually disabled components. Reinstalling a removed package requires an APK copy still available on the device. |
| Automatic cleanup | Off by default. When enabled, periodically checks selected spaces and processes only the automatic-cleanup list. |
| Diagnostics | Provides copyable denial logs when both removal and disabling fail. |

Sources: [official README](https://github.com/Eynnzerr/TelemetryCleaner/blob/47d7f733ecb821bae154ead8f8bfcb945a170db7/README.md), [v1.3 notes](https://github.com/Eynnzerr/TelemetryCleaner/releases/tag/v1.3) and the [implementation commit](https://github.com/Eynnzerr/TelemetryCleaner/commit/e8dd7786628f368907f0d1d31ec2829cc373639a).

## Requirements and limits

- Requires Android 10 or later and a running, authorized Shizuku service. The upstream instructions support wireless-debugging startup on Android 11 or later.
- The non-root path uses shell privileges to request package-manager operations. Vendor ROMs can still reject them; removal is not guaranteed on every device.
- v1.3 does not resolve removal failures for some vivo carrier components. The maintainer records user reports of lost call-recording functionality after removing Device Management. This catalog did not reproduce those reports.
- Restoring a package does not recover data deleted during removal. Reinstallation also depends on a retained APK.
- Detection is limited to known packages. An empty result does not establish the absence of other telemetry, and carrier components can have legitimate functions.
- The root [license is MIT](https://github.com/Eynnzerr/TelemetryCleaner/blob/47d7f733ecb821bae154ead8f8bfcb945a170db7/LICENSE). The README describes the project as an educational tool for Android package management.

## Getting started

1. Read the [official README](https://github.com/Eynnzerr/TelemetryCleaner#readme), including requirements, package coverage and device feedback.
2. Choose a version from [official releases](https://github.com/Eynnzerr/TelemetryCleaner/releases), then follow the upstream Shizuku setup instructions.
3. Inspect the target space, package name and permission records before authorizing an operation.
4. Distinguish removed, disabled and failed outcomes. Before restoration, check whether an APK remains and remember that deleted data is separate.

This import did not download or install the APK, or remove, disable or restore any device package.

## Alternatives

The catalog has no reviewed equivalent yet. When comparing package managers, consider operation scope, result verification and restoration conditions.

## Review

Reviewed on 2026-11-15 using official documentation, the MIT file, v1.3 notes and selected Kotlin code. The code specifies SDK 29 as the minimum, automatic cleanup off by default and the manual-uninstall disable fallback on by default. The 2026-11-13 functional commit provides maintenance evidence; the later license-only commit is not used for that purpose.

Verification level: `docs`. Source inspection supports implementation descriptions, not device compatibility or privacy guarantees. See [shared metadata](tool.json) for sources, timestamps and the license fingerprint.
