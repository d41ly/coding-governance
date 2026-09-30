# TOOL-aRepatriatedFork-50 — check 24's add baseline is this run's, on a build that ran before

**Status:** SPECCED · rev-1 · 2026-10-01 · node a · Tier-1 · base 6e7cb0df · streams tooling · order 22

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-01-prompt-TOOL-aRepatriatedFork-50-build-brief.md](../prompts/2026-10-01-prompt-TOOL-aRepatriatedFork-50-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The full bar at `6e7cb0df` redded the `unattended kit gate` leg's check 24 on this build's own run
record. It named 19 units as added mid-run with no rescope row, and every one of them was specced or
closed before this run's preflight. The roster a run "entered BUILDING with" is read from the first
live-phase commit on the run-state path, and on a build whose earlier run landed that commit is the
earlier run's. This unit makes that walk read only the current run's commits.

## 2. Scope (IN)

- **S1** — `baseline_units` in `tools/unattended/lib-unattended.sh` skips every commit whose record
  pins a `base:` other than the working record's. A working record with no `base:` filters nothing.
  Observed by AC1 and AC2.
- **S2** — Every run-fact read the change adds keeps the `| extract_run_facts | grep -m1 ` spelling,
  so check 36's two staged breaks still reach every read in the library. Observed by AC3.

## 3. Non-goals (OUT)

- The RETIRE arm. It reads `pinned_units` at the pinned BASE and was never affected.
- A run re-preflighted at the SAME base after an abort. Its walk still starts at the earlier run's
  first live commit. That roster is a subset of the later one, so the ceiling is a row owed, never a
  row skipped.
- Recording rescope rows for the 19 units. The scope did not move, so such rows would be false.

### Edges

none

## 4. Design

### Evidence

Read at `6e7cb0df`. `git log --reverse -- memory/builds/aRepatriatedFork/RUN.md` starts at
`0e284ca8`, which reads `phase: RUNNING` and `base: f8fdd873…`, the run that landed on 2026-09-24.
This run's first commit on that path is `a73fe338`, pinning `base: d6e1749c…`. `baseline_units` breaks
on the first live phase it meets, so it returned the roster at `0e284ca8`. The driver's `--rescope add`
reads the same function, so the same baseline decided whether an `add` row was a late record.

### Mechanism

`baseline_units` reads the working record's `base:` line once. For each commit on the path it reads
the blob once, compares that blob's `base:` line, and continues on a mismatch before the phase test.
The one derivation both callers share is the one fixed, so the checker and the driver stay one answer.

### Files touched (estimate)

- `tools/unattended/lib-unattended.sh`
- `tools/unattended/check-unattended.test.sh`

### Alternatives rejected

- Resetting the walk at every terminal phase. The current run may itself read `LANDED`, and then the
  walk would find no live commit after it.
- Rescope rows for the 19 units. They record a transition that did not happen.

## 5. Production-readiness checklist

- security — none. The check can only get stricter or equal for a first run, whose commits all pin
  one base.
- perf / scale — one extra pipeline per commit on the run-state path, over a blob already read. No
  extra git spawn.
- error / empty / loading states — a record with no `base:` keeps the unfiltered walk.
- observability — the existing check 24 message is unchanged.
- risks — the ceiling in §3.
- testing — AC1 to AC3.
- migration — none. The unattended kit's version is already moved on this branch.
- user docs — none. No `help/` page describes check 24.

## 6. Acceptance criteria

- **AC1** — When the §7 new arm runs as a slice, the prologue plus the check 24 block, a fixture whose first run
  landed, whose unit `ARCH-tRos-7` was specced between the runs, and whose second run pinned a new
  BASE draws no check 24 failure naming `ARCH-tRos-7`.
  Red when: the `6e7cb0df` library names `ARCH-tRos-7`.
- **AC2** — When the same slice runs, unit `ARCH-tRos-9`, added after the second run went live with no
  row, still draws the check 24 failure.
  Red when: the arm grades nothing and `ARCH-tRos-9` is not named.
- **AC3** — When the check 36 block runs as a slice, both staged breaks on `lib-unattended.sh` still
  red, and the unmutated kit is green.
  Red when: a new read escapes the `| extract_run_facts | grep -m1 ` spelling and a staged break
  stops reaching it.
- **AC4** — When `bash tools/unattended/check-unattended.sh` runs over this tree, it names no
  `aRepatriatedFork` unit under check 24.
  Red when: any of the 19 units is still named.
  cost: about nine minutes on node a.

## 7. Gates

`unattended kit gate` · `lexicon naming predicates` · `kit epoch (shipped bytes move, the version moves)` · `kit version markers`

New arm: `tools/unattended/check-unattended.test.sh` · a two-run fixture whose second run pins a new BASE · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-01 · initial draft, promoted by the VERIFYING repair pass R1 from the full bar's
  check 24 red at `6e7cb0df`.

## 10. Reuse audit

No existing seam fits beyond the one this changes: `baseline_units` is the single derivation both the
checker and the driver call, found by reading `tools/unattended/lib-unattended.sh`, which
`reuse_lookup.py` cannot see because it reports `.sh` as an unscanned layer.

Recall terms used: `check 24 rescope add baseline_units BUILDING roster retired run re-run preflight base`.
