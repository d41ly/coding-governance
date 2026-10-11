# TOOL-aHomedAnchor-27 — govkit reads the paths it guards as UTF-8

**Status:** CLOSED · rev-1 · 2026-10-11 · node a · Tier-1 · base b726385f · streams tooling · order 6 · closes TOOL-aHomedAnchor-12

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

govkit selftest's `[-25] AC2` is red on the held job: `apply` over a pinned path named
`memory/café.md` refuses, but names `memory/cafÃ©.md`, because `eol_population` decodes `git ls-files
-z` and `git check-attr -z` with the platform default. The mis-decoded name does not exist on disk, so
the refusal is reached through `missing_wt` with the wrong path. `TOOL-aHomedAnchor-22` stops the
selftest crashing on the print; this unit makes the arm pass.

## 2. Scope (IN)

- S1. `eol_population` in `tools/govkit/govkit.py` passes `encoding="utf-8"` to both reads, and the
  dirty-path read in `_cmd_apply` does too. Observed by AC1.
- S2. `memory/project/encoding-posture-sites.txt` declares govkit's unencoded subprocess sites as 36,
  down from 39, the count the posture leg measures. Observed by AC2.

## 3. Non-goals (OUT)

govkit's other 36 declared sites, which the registry carries and nothing red names.

### Edges

none

## 4. Design

The brief is `memory/builds/aHomedAnchor/prompts/2026-10-11-prompt-TOOL-aHomedAnchor-22-0-held-reds-brief.md`.
The arm is inside the selftest's `main()`, which cannot be sliced, so it is replayed through the
module's own `make_target`, `settle` and `run` helpers.

### Files touched (estimate)

- `tools/govkit/govkit.py`
- `memory/project/encoding-posture-sites.txt`

## 6. Acceptance criteria

- **AC1** — When the `[-25] AC2` replay runs with `PYTHONUTF8=0`, the `apply` refusal names the
  non-ASCII pinned path in full. Red when: either read decodes with the platform default.
- **AC2** — When `encoding_posture.py` runs with the leg's arguments, it prints `OK`. Red when: the
  registry row and the measured count disagree.

## 7. Gates

`govkit selftest` · `encoding posture (text IO names its encoding)` · `govkit acceptance matrix` · `govkit refusal join` · `recall floor` · `recall floor arms`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft.

## 10. Reuse audit

No existing seam fits beyond the `encoding="utf-8"` keyword the posture leg prescribes. Recall terms
used: `--terms "govkit eol_population ls-files check-attr encoding cp1252 pinned population non-ASCII path"`.
