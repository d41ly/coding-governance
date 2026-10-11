# TOOL-aPairedSlots-8 — the process-monitor adopter self-test stamps a fixture's common dir, not the real one

**Status:** CLOSED · rev-2 · 2026-10-11 · node a · Tier-1 · base b6cd02bc · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aPairedSlots-1-1-acceptance-ledger.md](../build/2026-10-11-build-TOOL-aPairedSlots-1-1-acceptance-ledger.md) | journal | TOOL-aPairedSlots-1 TOOL-aPairedSlots-6 |
| [2026-10-11-build-TOOL-aPairedSlots-5-shared-path-audit.md](../build/2026-10-11-build-TOOL-aPairedSlots-5-shared-path-audit.md) | journal | TOOL-aPairedSlots-5 TOOL-aPairedSlots-7 |
| [2026-10-11-prompt-TOOL-aPairedSlots-1-1-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aPairedSlots-1-1-build-brief.md) | journal | TOOL-aPairedSlots-1 TOOL-aPairedSlots-2 TOOL-aPairedSlots-3 TOOL-aPairedSlots-4 TOOL-aPairedSlots-5 TOOL-aPairedSlots-6 TOOL-aPairedSlots-7 TOOL-aPairedSlots-9 |

<!-- /gen:spec-records -->

## 1. Goal

The shared-path audit found one leg fixture that writes a fixed name in the REAL repository's common
dir: `tools/process-monitor/adopt-process-monitor.test.sh` runs the session hook against `$ROOT` and
removes and writes `procmon-stamp` there, so two bars running that self-test at once, or one bar
beside a live session whose hook stamps the same file, can flip its broken-monitor and throttle
arms. Those arms move to a fixture root, as its clean arm already did.

## 2. Scope (IN)

- **S1 — the stamp-touching arms run against a fixture.** Every arm that clears, writes or reads
  `$GD/procmon-stamp`, with `GD` the real common dir, runs its hook with `CLAUDE_PROJECT_DIR` at a
  scratch repository built the way the clean arm builds `_cleandir`, and reads that repository's
  stamp. Observed by AC1.
- **S2 — the real common dir is not touched.** The suite no longer resolves the real common dir for
  a stamp. Observed by AC2.

## 3. Non-goals (OUT)

- The hook itself, `procmon-hook.js`, and where it keeps its stamp.
- The arms that do not touch the stamp.

## 4. Design

The clean arm already moved to a fixture for a related reason: over the real root the census reads
the host, so a long session made "clean is silent" red. The stamp arms have the same dependence on
what else runs on the machine, through the stamp instead of the census, and take the same fix.

### Files touched (estimate)

- `tools/process-monitor/adopt-process-monitor.test.sh`

## 5. Acceptance criteria

- **AC1** — When the throttle arm and the broken-monitor arm run while a second process writes and
  removes `procmon-stamp` in the REAL common dir in a loop, both arms pass.
  Red when: the arms still read the real stamp, and the loop flips one of them.
- **AC2** — When `grep -nF '"$GD/procmon-stamp"'` runs over the suite, it prints nothing.
  Red when: an arm still names the real common dir's stamp.

## 6. Gates

`process-monitor adopter selftest`

New arm: tools/process-monitor/adopt-process-monitor.test.sh · covers AC1 · a loop toggling the real stamp beside the sliced arms · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-10-11 · initial draft.
- rev-2 · 2026-10-11 · AC2 · the grep names the quoted real-dir path exactly: the fixture's own
  `CLEAN_GD/procmon-stamp` carries the bare substring, so the rev-1 command could never print nothing.
