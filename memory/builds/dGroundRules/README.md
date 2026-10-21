---
slug: dGroundRules
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-12
status: OPEN
spec-audit: 2026-10-21
parents: dTrueNorth
may: PLAY-dClosedLoop-3
---

# dGroundRules — the Policy build of the dClosedLoop chain

## The problem this build exists to solve

dGroundRules owns 3 gaps at the baseline `59ff8f2ac`, as its row of v2's `[chain]` names them: gap-spine-06,
gap-tool-24, gap-rt-34. Closing every one is this build's goal bound.

## Expected improvements

- Each of the 11 clauses of its row in v2's `[chain]` carried by a spec pinned to its hash, one roster unit per
  clause.
- Each unit built and landed, so the 3 owned gaps above close.

## Detriments if this is not built

- Its 3 owned gaps stay open.
- Its 1 child build waits on it: dSafePassage.

## Build-level rules

- Phase, from the tree: a run whose `BACKLOG.md` at its baseline holds an open ask and whose starting roster has a
  unit `MISSING` is the spec run; it specs, audits and defers every unit, each it added a departure, and closes by
  carry-forward. Any other run is the build run: it builds every carried unit, deferring none again.
- Read in the packet's order, `packet.py --check dGroundRules` green before the first pass; a moved instrument blob is
  a stop, never re-rendered away.
- Push the run branch after every pass commit, hold and hand-off.
- Close on the prepared merge after `--phase VERIFYING` and the last `push-main.sh --prepare`:
  `deviations.py --report dGroundRules`, a record per member "recorded by nobody", the same with `--write` (commit it
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
| 1 | `TOOL-dGroundRules-1` | `cl-dClosedLoop-0007@b0458b78` | `.governance/policy.toml` |
| 2 | `TOOL-dGroundRules-2` | `cl-dClosedLoop-0008@6598846f` | the reader extending `read_policy_key`'s contract |
| 3 | `TOOL-dGroundRules-3` | `cl-dClosedLoop-0009@7d93fce9` | each key resolved in one order: an override in the file |
| 4 | `TOOL-dGroundRules-4` | `cl-dClosedLoop-0010@cd629be7` | a malformed file or an out-of-set value read as `policy-file.on-invalid` says |
| 5 | `TOOL-dGroundRules-5` | `cl-dClosedLoop-0011@8312590d` | the JSON mirror regenerated at each landing and pinned to the landed revision |
| 6 | `TOOL-dGroundRules-6` | `cl-dClosedLoop-0012@937c308e` | the minimal guard |
| 7 | `TOOL-dGroundRules-7` | `cl-dClosedLoop-0013@8ae02ac2` | the legacy homes on a shrink-only list derived by query from the files they guard |
| 8 | `TOOL-dGroundRules-8` | `cl-dClosedLoop-0014@28a178b1` | an arm red when a key whose Owner build has landed has no reader |
| 9 | `TOOL-dGroundRules-9` | `cl-dClosedLoop-0015@8ce57bfb` | `budgets.enforce` |
| 10 | `TOOL-dGroundRules-10` | `cl-dClosedLoop-0016@df63b6eb` | `runtime.agents-in-flight` |
| 11 | `TOOL-dGroundRules-11` | `cl-dClosedLoop-0017@c5b54ae9` | each loop bound and deadline key declaring that raising it is a loosening |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dGroundRules-1 TOOL-dGroundRules-2 TOOL-dGroundRules-3 TOOL-dGroundRules-4 TOOL-dGroundRules-5 TOOL-dGroundRules-6 TOOL-dGroundRules-7 TOOL-dGroundRules-8 TOOL-dGroundRules-9 TOOL-dGroundRules-10 TOOL-dGroundRules-11 TOOL-dGroundRules-12

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dGroundRules's 11 clause(s) and 5 owned node(s), over 0 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 0
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 11 (cl-dClosedLoop-0007, cl-dClosedLoop-0008, cl-dClosedLoop-0009, cl-dClosedLoop-0010, cl-dClosedLoop-0011, cl-dClosedLoop-0012, cl-dClosedLoop-0013, cl-dClosedLoop-0014, cl-dClosedLoop-0015, cl-dClosedLoop-0016, cl-dClosedLoop-0017)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: policy-key.budgets.*, policy-key.budgets.enforce, policy-key.budgets.pinned, policy-key.policy-file.on-invalid, policy-key.runtime.agents-in-flight
- specs derived from no clause: none
- clauses the token arm cannot see: cl-dClosedLoop-0009, cl-dClosedLoop-0014, cl-dClosedLoop-0017
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dTrueNorth](../dTrueNorth/README.md)
- **Child builds:** [dSafePassage](../dSafePassage/README.md)
<!-- /gen:build-edges -->
