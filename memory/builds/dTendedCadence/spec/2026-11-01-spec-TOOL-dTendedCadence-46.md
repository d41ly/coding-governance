# TOOL-dTendedCadence-46 — `defer dormant` probes the disposal in a scratch tree and lands it through a records-only patch intake, so the walk leaves no tracked write

**Status:** DEFERRED · rev-2 · 2026-11-01 · node a · Tier-2 · base f4597719 · streams tooling · order 10 · advances TOOL-dTendedCadence-19

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md](../build/2026-11-01-build-TOOL-dTendedCadence-1-agent-ledger.md) | journal | TOOL-dTendedCadence-1 TOOL-dTendedCadence-2 TOOL-dTendedCadence-3 TOOL-dTendedCadence-4 TOOL-dTendedCadence-5 TOOL-dTendedCadence-6 TOOL-dTendedCadence-7 TOOL-dTendedCadence-8 TOOL-dTendedCadence-9 TOOL-dTendedCadence-10 TOOL-dTendedCadence-11 TOOL-dTendedCadence-12 TOOL-dTendedCadence-13 TOOL-dTendedCadence-14 TOOL-dTendedCadence-15 TOOL-dTendedCadence-16 TOOL-dTendedCadence-17 TOOL-dTendedCadence-18 TOOL-dTendedCadence-35 TOOL-dTendedCadence-36 TOOL-dTendedCadence-37 TOOL-dTendedCadence-38 TOOL-dTendedCadence-39 TOOL-dTendedCadence-40 TOOL-dTendedCadence-41 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-47 TOOL-dTendedCadence-48 TOOL-dTendedCadence-49 TOOL-dTendedCadence-50 TOOL-dTendedCadence-51 TOOL-dTendedCadence-52 TOOL-dTendedCadence-53 TOOL-dTendedCadence-54 TOOL-dTendedCadence-55 TOOL-dTendedCadence-56 TOOL-dTendedCadence-57 TOOL-dTendedCadence-58 TOOL-dTendedCadence-59 TOOL-dTendedCadence-60 TOOL-dTendedCadence-61 TOOL-dTendedCadence-62 TOOL-dTendedCadence-63 TOOL-dTendedCadence-64 TOOL-dTendedCadence-65 TOOL-dTendedCadence-66 TOOL-dTendedCadence-67 TOOL-dTendedCadence-68 TOOL-dTendedCadence-69 TOOL-dTendedCadence-70 TOOL-dTendedCadence-71 TOOL-dTendedCadence-72 TOOL-dTendedCadence-73 TOOL-dTendedCadence-74 |
| [2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md](../reviews/2026-11-01-review-TOOL-dTendedCadence-35-to-48-spec-audit-round1.md) | spec-audit | TOOL-dTendedCadence-35 TOOL-dTendedCadence-37 TOOL-dTendedCadence-42 TOOL-dTendedCadence-43 TOOL-dTendedCadence-47 TOOL-dTendedCadence-36 TOOL-dTendedCadence-40 TOOL-dTendedCadence-38 TOOL-dTendedCadence-44 TOOL-dTendedCadence-45 TOOL-dTendedCadence-39 TOOL-dTendedCadence-41 TOOL-dTendedCadence-48 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 43 of `reviews/2026-11-01-review-TOOL-dTendedCadence-1-to-18-spec-audit-round1.md`,
HIGH, item H11. Unit 3's `item.maintain.direct` runs `loop_transition.py dispose --build <slug>` in
the checkout the cadence runs in (spec-3 S6, :91-96), and dispose records the move through
`write_transition`, a tracked record (TOOL-dRankedPlan-4 S3). The walk commits nothing (spec-1:98)
and only the maintenance record has a landing intake (spec-1 S6, §8 F4). Unit 3 itself says "the one
tracked write is dispose's" (:196) and that tracked content belongs to `maintain.patch` (:190). The
move stays uncommitted on one node, the default branch never sees it, and the next clean-base reading
re-proposes and re-applies it each period over a dirty checkout. This unit routes the disposal's write
through `maintain.patch`, keeping the owner-gated read.

## 2. Scope (IN)

- **S1** — The probe. `run_dormant_fix(root, key, dry_run)` (unit 3 S6) runs `loop_transition.py
  dispose --build <slug>` only inside a detached scratch worktree of `HEAD`, yielded by
  `resolve_reading_tree(root, <HEAD sha>, "clean-base")` (TOOL-dTendedCadence-18 S7) and taken down
  on exit, so its write lands in a tree that is discarded. Its exit is read as unit 3 S6 reads it: 1 is
  `held`, proposed to the owner through `run_breach_route`; 2 is `survived` with the refusal.
  Observed by AC1 and AC2.
- **S2** — The landing. Exit 0 in the probe is a move the owner recorded: the walk files it as one
  records-only patch intake, `write_patch_intake(root, reading, key)` (TOOL-dTendedCadence-8 S7) for
  the reading `live_builds_without_activity` and that build's offender key, whose patch build runs
  `dispose` in its own tree and lands the transition. The outcome is the filing's, `filed` or `seen`,
  and `item.maintain.direct`'s row gains both, each routed to `item.maintain.record`. Observed by AC1.
- **S3** — Unit 3 §5's security line reads with S1 and S2: the walk writes nothing tracked; the one
  tracked write, dispose's, is the patch build's. Observed by AC2.

## 3. Non-goals (OUT)

- `dispose` and `--dormant`: TOOL-dRankedPlan-4, unchanged.
- The other five fixes: unit 3 S2, unchanged.
- A walk-level arm asserting a clean `git status --porcelain` after every full `maintain.py` run: the
  report's left-shift gate, which also catches id 44 (TOOL-dTendedCadence-48); not built here.

### Edges

- **consumes-from** `TOOL-dTendedCadence-3` — `run_dormant_fix`, `item.maintain.direct` and its outcomes, which this unit re-routes
- **consumes-from** `TOOL-dTendedCadence-8` — `write_patch_intake`, the records-only filing the disposal lands through
- **consumes-from** `TOOL-dTendedCadence-18` — `resolve_reading_tree`, the scratch tree the probe runs in
- **hands-off** `TOOL-dTendedCadence-59` — `item.maintain.direct`'s `survivor` route and the Files touched, which the minors batch repairs (review ids 38, 48)

## 4. Design

### Evidence

- Spec-3 S6 reads dispose's three exits, `fixed`, `held` and `survived`; spec-3 §4 "Alternatives
  rejected" gives tracked content to `maintain.patch`.
- Spec-18 S7 adds a detached worktree of a sha under `clean-base` and removes it on exit; its `mode`
  is a parameter, so a caller may pass `clean-base` whatever `maintain.reading-tree` says.
- Spec-8 S7 renders the patch intake from the reading's name, offender key, fix and layer, so the
  disposal needs no new text.

### Inventory

Minted: nothing; `filed` and `seen` join `item.maintain.direct`'s outcomes from unit 8 S7's.

### Files touched (estimate)

- `tools/drift-audit/maintain_fixes.py`: S1, S2
- `tools/drift-audit/kit.toml`: S2's two outcomes on `item.maintain.direct`
- `tools/drift-audit/selftest.py`: the cases of §6

### Alternatives rejected

- **The walk commits the transition and lands it.** A landing from a tick with no owner turn, the
  write surface unit 1 §8 F4 refused for the record (veto 3).
- **File every dormant build as a patch intake with no probe.** The patch build would then hold the
  owner proposal for a build with no disposition, a decision the walk makes today from dispose's exit.

## 5. Production-readiness checklist

- security — the walk's write set loses its one tracked path; the scratch tree sits under the git
  common dir and is removed on exit.
- perf / scale — one scratch worktree per run that has a dormant build, reused for every slug.
- error / empty / loading states — a scratch tree that cannot be added makes every slug `survived`
  with the git error.
- observability — each slug prints `direct — defer dormant · <slug> · <outcome>`.
- risks — a scratch tree left by a killed run is id 47's case (TOOL-dTendedCadence-48).
- testing — the criteria of §6.
- migration — N/A — the fix is new in this build.
- user docs — `help/maintain.md`'s section "The safe fixes" says the disposal lands through a patch
  build.

## 6. Acceptance criteria

- **AC1** — When `GOV_CADENCE_KEY=2026-11-01 python maintain.py` runs over a fixture holding one
  dormant build with an owner disposition and one without, with a recording filer and a stub
  `loop_transition.py`, it files one patch intake naming the first build and proposes the second
  through `run_breach_route` as `held`.
  Red when: a recorded move is applied in the checkout, or is not filed.
- **AC2** — When the same run ends, `git status --porcelain` in the fixture prints what it printed
  before the run, and `git worktree list` lists no `maintain-read` tree.
  Red when: the walk leaves a tracked file dirty, or the scratch tree behind.

## 7. Gates

`drift-audit selftest` · `policy fixtures` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/drift-audit/selftest.py · covers AC1 AC2 · two dormant builds with a stub dispose that writes a tracked file, staged against dispose run in the checkout · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-01 · initial draft, promoted from review id 43 (HIGH, item H11) of the round-1 spec
  audit.
- rev-2 · 2026-11-01 · §3 · the Edges gain the mirror of each edge the promoted units of the round-1 spec audit of units 35 to 48 declare toward this unit (unit 59); no scope, design or criterion moved.

## 10. Reuse audit

The seams reused are unit 18's `resolve_reading_tree` for the scratch tree, unit 8's
`write_patch_intake` for the landing, and unit 3's `run_dormant_fix` for the exit reading. `python
tools/codebase-map/reuse_lookup.py "add a detached scratch worktree and remove it on exit"` ranked
`add_scratch_worktree` (`tools/run-gates/lib-attribute.sh`, fan-in 3, a SEAM), the shell helper whose
argv unit 18 S7 already reuses, so this unit calls unit 18's Python seam and writes no third copy.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit placed after the unit it repairs" --terms "spec audit promoted repair unit order hands-off
consumes-from minors batch maintenance record key grammar over-pin"`
