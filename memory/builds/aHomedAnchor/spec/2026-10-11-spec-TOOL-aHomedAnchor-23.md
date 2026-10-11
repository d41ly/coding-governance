# TOOL-aHomedAnchor-23 — the launcher arm reads an invocation, not a declaration, a string or a file extension

**Status:** INPROGRESS · rev-1 · 2026-10-11 · node a · Tier-1 · base b726385f · streams tooling · order 6 · closes TOOL-aHomedAnchor-18

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-prompt-TOOL-aHomedAnchor-22-0-held-reds-brief.md](../prompts/2026-10-11-prompt-TOOL-aHomedAnchor-22-0-held-reds-brief.md) | journal | TOOL-aHomedAnchor-22 TOOL-aHomedAnchor-24 TOOL-aHomedAnchor-25 |

<!-- /gen:spec-records -->

## 1. Goal

Driver shard 2/8 is red on its own arm: the source-level launcher check flags `local base py d`, echo prose saying "no python launcher", and `drift_report.py `, none of which runs a launcher.

## 2. Scope (IN)

- S1. The arm in `tools/unattended/unattended.test.sh` skips `local` declarations, blanks double-quoted strings, and adds `.` to the excluded neighbours. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

Any other suite's red; running the unattended shard suites (owner, 2026-10-11).

### Edges

none

## 4. Design

The brief is `memory/builds/aHomedAnchor/prompts/2026-10-11-prompt-TOOL-aHomedAnchor-22-0-held-reds-brief.md`. The red was read from the daily held job's run 38045767386 at `d006cfc5`.

### Files touched (estimate)

- `tools/unattended/unattended.test.sh`

## 6. Acceptance criteria

- **AC1** — When the arm's predicate runs over `tools/unattended/unattended.sh` at the base, it prints nothing. Red when: a false positive remains.
- **AC2** — When a line `python3 bare_call.py` or `py -3 bare.py` is staged into a copy, the predicate names it. Red when: the tightening hid a real launcher.

## 7. Gates

`unattended kit gate`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.

## 10. Reuse audit

No existing seam fits beyond the site named in §2. Recall terms used: `--terms "held job red suite daily remote-ci PYTHONUTF8 cp1252 reconfigure fixture stale launcher overlaps"`.
