---
slug: dSafePassage
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-14
spec-audit: 2026-10-21
parents: dGroundRules
may: PLAY-dClosedLoop-3
---

# dSafePassage — the Supersession build of the dClosedLoop chain

## The problem this build exists to solve

dSafePassage owns 13 gaps at the baseline `59ff8f2ac`, as its row of v2's `[chain]` names them: gap-deploy-15,
gap-deploy-16, gap-deploy-17, gap-deploy-24, gap-tool-10, gap-tool-22, gap-tool-12, gap-tool-23, gap-deploy-18,
gap-deploy-19, gap-deploy-20, gap-deploy-25, gap-found-35. Closing every one is this build's goal bound.

## Expected improvements

- Each of the 13 clauses of its row in v2's `[chain]` carried by a spec pinned to its hash, one roster unit per
  clause.
- Each unit built and landed, so the 13 owned gaps above close.

## Detriments if this is not built

- Its 13 owned gaps stay open.
- Its 2 child builds wait on it: dOrderedCharter, dFairHearing.

## Build-level rules

- Phase, from the tree: a run whose `BACKLOG.md` at its baseline holds an open ask and whose starting roster has a
  unit `MISSING` is the spec run; it specs, audits and defers every unit, each it added a departure, and closes by
  carry-forward. Any other run is the build run: it builds every carried unit, deferring none again.
- Read in the packet's order, `packet.py --check dSafePassage` green before the first pass; a moved instrument blob is
  a stop, never re-rendered away.
- Push the run branch after every pass commit, hold and hand-off.
- Close on the prepared merge after `--phase VERIFYING` and the last `push-main.sh --prepare`:
  `deviations.py --report dSafePassage`, a record per member "recorded by nobody", the same with `--write` (commit it
  as `…-departures-spec.md` or `-build.md`) and `--check`, then `--authorization` and `--close`; again after a
  re-prepare.
- Deviation values: `report` and `author-recorded`.
- Forks by the plan's rungs: a rung 5 or 6 choice's §8 mark and `Decided:` trailer cite its ruling (ER:240, ER:388,
  ER:328 or P0.8 row 5) and carry `widens:` and `relaxes:`, a value or `none`; a `relaxes:` value joins a record with
  `**Bound:**`, `**Tier:**`, `**Reason:**`, a `widens:` value one with `**Surface:**`, `**Reason:**`; a grant-lifted
  choice carries `grants: <id> <change>`.
- Writes stay in this build's folder and a build run's `--dispatch --writes` paths; outside, only an ask row in
  another build's `BACKLOG.md` and the shared renders. The departures report lists the rest.

## Parked decisions

none

<!-- roster:units -->

| # | Unit | Carries | Clause |
|---|---|---|---|
| 1 | `TOOL-dSafePassage-1` | `cl-dClosedLoop-0018@ed08a364` | the upgrade-step kind: a kit descriptor's `[[upgrade]]` row (id |
| 2 | `TOOL-dSafePassage-2` | `cl-dClosedLoop-0019@6e0cd313` | `update` walking every step between a receipt's vintage and its target |
| 3 | `TOOL-dSafePassage-3` | `cl-dClosedLoop-0020@42c7d579` | the receipt's schema 4 gaining `steps` |
| 4 | `TOOL-dSafePassage-4` | `cl-dClosedLoop-0021@ad0db541` | down steps run in reverse |
| 5 | `TOOL-dSafePassage-5` | `cl-dClosedLoop-0022@4bc8eba9` | the release-0 fixture tree and the `upgrade-walk` leg: up |
| 6 | `TOOL-dSafePassage-6` | `cl-dClosedLoop-0023@6e1e2e99` | a forwarding shim for a moved command |
| 7 | `TOOL-dSafePassage-7` | `cl-dClosedLoop-0024@7817c7d0` | the step kind's isolation contract |
| 8 | `TOOL-dSafePassage-8` | `cl-dClosedLoop-0025@4e486ab9` | gov first for every step: each step run on gov's own tree in the lander's prepared merge before any adopter meets it |
| 9 | `TOOL-dSafePassage-9` | `cl-dClosedLoop-0026@97d3c99b` | withdrawn hook fragments unwired |
| 10 | `TOOL-dSafePassage-10` | `cl-dClosedLoop-0027@46290183` | the step gate: a leg that diffs the adopter-visible surface population between a landing's base and its tip |
| 11 | `TOOL-dSafePassage-11` | `cl-dClosedLoop-0028@032ca791` | the interpreter floor raised to Python 3.15 as the step kind's first step after the receipt's schema-4 step |
| 12 | `TOOL-dSafePassage-12` | `cl-dClosedLoop-0029@4aeb7648` | gov's own executors at the floor in the landing that raises it: every job of `.github/workflows/remote-ci.yml` that runs Python setting it up at the floor |
| 13 | `TOOL-dSafePassage-13` | `cl-dClosedLoop-0030@274077d4` | the docs leg |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 13 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dSafePassage-1 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8 TOOL-dSafePassage-9 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-14

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-dSafePassage-1 — the upgrade-step kind: the step row, succession rows, their one reader, and frozen landed rows](spec/2026-10-23-spec-TOOL-dSafePassage-1.md) | 1 | 2 | OPEN | rev-2 | 2026-10-23 |
| [TOOL-dSafePassage-3 — the receipt's schema 4: the `steps` field, its one writer, and the step that ships it](spec/2026-10-23-spec-TOOL-dSafePassage-3.md) | 1 | 2 | OPEN | rev-1 | 2026-10-23 |
| [TOOL-dSafePassage-2 — `update` walks the upgrade steps oldest first, and recovers what a killed run left](spec/2026-10-23-spec-TOOL-dSafePassage-2.md) | 2 | 2 | OPEN | rev-1 | 2026-10-23 |
| [TOOL-dSafePassage-4 — down steps in reverse, and the recorded rollback that lifts the downgrade refusal](spec/2026-10-23-spec-TOOL-dSafePassage-4.md) | 2 | 2 | OPEN | rev-1 | 2026-10-23 |
| [TOOL-dSafePassage-7 — the step kind's isolation contract, and the check of its needs-target field](spec/2026-10-23-spec-TOOL-dSafePassage-7.md) | 2 | 2 | OPEN | rev-1 | 2026-10-23 |
| [TOOL-dSafePassage-11 — the interpreter floor at Python 3.15, declared once, refused below by the resolver, and raised as the second upgrade step](spec/2026-10-23-spec-TOOL-dSafePassage-11.md) | 3 | 2 | OPEN | rev-1 | 2026-10-23 |
| [TOOL-dSafePassage-12 — gov's remote CI at the interpreter floor, read from its one declaration, with the floor's preflight as the bar's first step](spec/2026-10-23-spec-TOOL-dSafePassage-12.md) | 3 | 2 | OPEN | rev-1 | 2026-10-23 |
| [TOOL-dSafePassage-8 — gov first for every step: the lander walks each new step on gov's own tree, recorded in gov's source-mode receipt](spec/2026-10-23-spec-TOOL-dSafePassage-8.md) | 3 | 2 | OPEN | rev-1 | 2026-10-23 |
| [TOOL-dSafePassage-10 — the step gate: the adopter-visible surface population diffed between a landing's base and its tip](spec/2026-10-23-spec-TOOL-dSafePassage-10.md) | 4 | 2 | OPEN | rev-1 | 2026-10-23 |
| [TOOL-dSafePassage-6 — forwarding shims for a moved command, hook path or module import, held for their deprecation window](spec/2026-10-23-spec-TOOL-dSafePassage-6.md) | 4 | 2 | OPEN | rev-1 | 2026-10-23 |
| [TOOL-dSafePassage-9 — withdrawn hook fragments unwired, and an edited file gov stopped shipping kept as `retired-edited` and ordered](spec/2026-10-23-spec-TOOL-dSafePassage-9.md) | 4 | 2 | OPEN | rev-1 | 2026-10-23 |
| [TOOL-dSafePassage-13 — the docs leg: each user-facing member's declared usage fingerprinted against its help page, under help.enforce](spec/2026-10-23-spec-TOOL-dSafePassage-13.md) | 5 | 2 | OPEN | rev-1 | 2026-10-23 |
| [TOOL-dSafePassage-5 — the release-0 fixture tree and the upgrade-walk leg: every declared step walked up, down and up again over today's install](spec/2026-10-23-spec-TOOL-dSafePassage-5.md) | 5 | 2 | OPEN | rev-1 | 2026-10-23 |
<!-- /gen:build-units -->

Records: 11 bound to this build, across 3 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: TOOL-dSafePassage-1 TOOL-dSafePassage-10 TOOL-dSafePassage-11 TOOL-dSafePassage-12 TOOL-dSafePassage-13 TOOL-dSafePassage-2 TOOL-dSafePassage-3 TOOL-dSafePassage-4 TOOL-dSafePassage-5 TOOL-dSafePassage-6 TOOL-dSafePassage-7 TOOL-dSafePassage-8
TOOL-dSafePassage-9.

Ids whose spec moved past its audited revision: none — 0 of 13 unit id(s) carry a pin.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dSafePassage's 13 clause(s) and 5 owned node(s), over 13 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 13
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 0 (none)
- stale: 3 (cl-dClosedLoop-0018, cl-dClosedLoop-0028, cl-dClosedLoop-0030)
- ambiguous: 0 (none)
- owned nodes no spec names: none
- specs derived from no clause: none
- clauses the token arm cannot see: cl-dClosedLoop-0021
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-dSafePassage-1`, `TOOL-dSafePassage-3` | yes |
| 2 | `TOOL-dSafePassage-2`, `TOOL-dSafePassage-4`, `TOOL-dSafePassage-7` | yes |
| 3 | `TOOL-dSafePassage-11`, `TOOL-dSafePassage-12`, `TOOL-dSafePassage-8` | yes |
| 4 | `TOOL-dSafePassage-10`, `TOOL-dSafePassage-6`, `TOOL-dSafePassage-9` | yes |
| 5 | `TOOL-dSafePassage-13`, `TOOL-dSafePassage-5` | yes |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dGroundRules](../dGroundRules/README.md)
- **Child builds:** [dFairHearing](../dFairHearing/README.md), [dOrderedCharter](../dOrderedCharter/README.md)
<!-- /gen:build-edges -->
