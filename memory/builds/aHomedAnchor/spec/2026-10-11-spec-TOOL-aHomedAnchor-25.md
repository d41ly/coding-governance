# TOOL-aHomedAnchor-25 — two suite fixtures follow the carriers other builds changed

**Status:** INPROGRESS · rev-1 · 2026-10-11 · node a · Tier-1 · base b726385f · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-prompt-TOOL-aHomedAnchor-22-0-held-reds-brief.md](../prompts/2026-10-11-prompt-TOOL-aHomedAnchor-22-0-held-reds-brief.md) | journal | TOOL-aHomedAnchor-22 TOOL-aHomedAnchor-23 TOOL-aHomedAnchor-24 |

<!-- /gen:spec-records -->

## 1. Goal

Gate shard 6/8 keys a fixture on "One `AskUserQuestion`", which another build lowercased, so the fixture no-ops and its arm reds. The cross-component suite's prompt-mode README carries no prompt record, and this repo's conf now arms the two brief cutoffs, so its preflight is refused at check 115, later 117.

## 2. Scope (IN)

- S1. The fixture in `tools/unattended/check-unattended.test.sh` matches either case. Observed by AC1.
- S2. `tools/unattended/cross-component.test.sh` blanks `PROMPT_BRIEF_CUTOFF` and `PROMPT_BRIEF_SKELETON_CUTOFF` in its fixture conf, beside the keys it already blanks. Observed by AC2.

## 3. Non-goals (OUT)

Any other suite's red; running the unattended shard suites (owner, 2026-10-11).

### Edges

none

## 4. Design

The brief is `memory/builds/aHomedAnchor/prompts/2026-10-11-prompt-TOOL-aHomedAnchor-22-0-held-reds-brief.md`. The red was read from the daily held job's run 38045767386 at `d006cfc5`.

### Files touched (estimate)

- `tools/unattended/check-unattended.test.sh`
- `tools/unattended/cross-component.test.sh`

## 6. Acceptance criteria

- **AC1** — When the fixture's `sed` runs over `tools/unattended/SKILL.template.md`, the output differs from the input. Red when: it no-ops.
- **AC2** — When the cross-component suite is sliced through its arm 2, its second `--preflight` prints `preflight OK`. Red when: a brief check still refuses it.

## 7. Gates

`unattended kit gate`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.

## 10. Reuse audit

No existing seam fits beyond the site named in §2. Recall terms used: `--terms "held job red suite daily remote-ci PYTHONUTF8 cp1252 reconfigure fixture stale launcher overlaps"`.
