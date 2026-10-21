---
slug: dPlacedRequest
node: d
opened: 2026-10-21
streams: tooling
roster: TOOL
ids: TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-22
status: OPEN
spec-audit: 2026-10-21
parents: dDeclaredLoop
may: PLAY-dClosedLoop-3
---

# dPlacedRequest — the Entry build of the dClosedLoop chain

## The problem this build exists to solve

dPlacedRequest owns 18 gaps at the baseline `59ff8f2ac`, as its row of v2's `[chain]` names them: gap-flow-07,
gap-conc-01, gap-conc-02, gap-orient-01, gap-orient-02, gap-orient-04, gap-orient-11, gap-flow-18, gap-orient-20,
gap-conc-06, gap-conc-07, gap-conc-08, gap-conc-12, gap-conc-13, gap-conc-14, gap-conc-17, gap-conc-18, gap-conc-19.
Closing every one is this build's goal bound.

## Expected improvements

- Each of the 21 clauses of its row in v2's `[chain]` carried by a spec pinned to its hash, one roster unit per
  clause.
- Each unit built and landed, so the 18 owned gaps above close.

## Detriments if this is not built

- Its 18 owned gaps stay open.
- Its 3 child builds wait on it: dKeptSession, dBoundRoles, dTotalRecall.

## Build-level rules

- Phase, from the tree: a run whose `BACKLOG.md` at its baseline holds an open ask and whose starting roster has a
  unit `MISSING` is the spec run; it specs, audits and defers every unit, each it added a departure, and closes by
  carry-forward. Any other run is the build run: it builds every carried unit, deferring none again.
- Read in the packet's order, `packet.py --check dPlacedRequest` green before the first pass; a moved instrument blob
  is a stop, never re-rendered away.
- Push the run branch after every pass commit, hold and hand-off.
- Close on the prepared merge after `--phase VERIFYING` and the last `push-main.sh --prepare`:
  `deviations.py --report dPlacedRequest`, a record per member "recorded by nobody", the same with `--write` (commit
  it as `…-departures-spec.md` or `-build.md`) and `--check`, then `--authorization` and `--close`; again after a
  re-prepare.
- Deviation values: `report` and `author-recorded`.
- Forks by the plan's rungs: a rung 5 or 6 choice's §8 mark and `Decided:` trailer cite its ruling (ER:240, ER:388,
  ER:328 or P0.8 row 5) and carry `widens:` and `relaxes:`, a value or `none`; a `relaxes:` value joins a record with
  `**Bound:**`, `**Tier:**`, `**Reason:**`, a `widens:` value one with `**Surface:**`, `**Reason:**`; a grant-lifted
  choice carries `grants: <id> <change>`.
- Writes stay in this build's folder and a build run's `--dispatch --writes` paths; outside, only an ask row in
  another build's `BACKLOG.md` and the shared renders. The departures report lists the rest.
- The unattended kit's own self-test suites are WAIVED for this build's landing (owner, 2026-10-20, walk answer 5). A
  criterion they would observe is amended citing this rule; their clean reading is owed with PLAY-dClosedLoop-14.

## Parked decisions

none

<!-- roster:units -->

| # | Unit | Carries | Clause |
|---|---|---|---|
| 1 | `TOOL-dPlacedRequest-1` | `cl-dClosedLoop-0120@5d655f07` | the coordination feature: one lease grammar for builds |
| 2 | `TOOL-dPlacedRequest-2` | `cl-dClosedLoop-0121@2f58beed` | the build's orientation card at level 1 |
| 3 | `TOOL-dPlacedRequest-3` | `cl-dClosedLoop-0122@938c9643` | the entry step's items: the card's orientation |
| 4 | `TOOL-dPlacedRequest-4` | `cl-dClosedLoop-0123@626c316e` | the placement predicate and its check |
| 5 | `TOOL-dPlacedRequest-5` | `cl-dClosedLoop-0503@65f19d46` | the `breakpoint` disposition in the placement set: an owner's request for a review on a live build |
| 6 | `TOOL-dPlacedRequest-6` | `cl-dClosedLoop-0124@b8ada8e4` | the items' declarations of the `map` slot and their unfolds |
| 7 | `TOOL-dPlacedRequest-7` | `cl-dClosedLoop-0125@4e0727e5` | the probe program (`probe.trigger` |
| 8 | `TOOL-dPlacedRequest-8` | `cl-dClosedLoop-0126@b35ab44f` | each item's declared code seed: its write set |
| 9 | `TOOL-dPlacedRequest-9` | `cl-dClosedLoop-0127@4f0c1452` | the kickoff manifest's facts as level-2 instruction units the card reads (the memory plan's `[pockets]`) |
| 10 | `TOOL-dPlacedRequest-10` | `cl-dClosedLoop-0128@e0109d47` | a build's scenarios chosen at `entry.place`: the orientation scout's return naming each scenario whose admission predicate holds over the request's facts |
| 11 | `TOOL-dPlacedRequest-11` | `cl-dClosedLoop-0129@30a0ceda` | each lease and claim written as a commit whose parent is its ref's previous tip |
| 12 | `TOOL-dPlacedRequest-12` | `cl-dClosedLoop-0130@57d242df` | create-only registers on the remote |
| 13 | `TOOL-dPlacedRequest-13` | `cl-dClosedLoop-0131@3532cbe6` | the change feed: an ordered |
| 14 | `TOOL-dPlacedRequest-14` | `cl-dClosedLoop-0132@6096ecb9` | the pre-claim budget: placement loops before `entry.claim` drawing on a budget keyed to the request's content key |
| 15 | `TOOL-dPlacedRequest-15` | `cl-dClosedLoop-0133@231564d8` | the fenced effect push: every effect push carrying the holder's new lease beat in one atomic push under a compare-and-swap on the lease tip it read |
| 16 | `TOOL-dPlacedRequest-16` | `cl-dClosedLoop-0134@bacb3ef7` | a lease never deleted: each release a hand-over |
| 17 | `TOOL-dPlacedRequest-17` | `cl-dClosedLoop-0135@55365bfa` | a lease's expiry |
| 18 | `TOOL-dPlacedRequest-18` | `cl-dClosedLoop-0136@c9686488` | the cadence segment of the lease grammar taking any name the tag grammar admits |
| 19 | `TOOL-dPlacedRequest-19` | `cl-dClosedLoop-0137@39b3ef9d` | a request that is not yet a build written as a project-level record any node may claim by lease |
| 20 | `TOOL-dPlacedRequest-20` | `cl-dClosedLoop-0138@b6141505` | lease acquisition taking an optional offer |
| 21 | `TOOL-dPlacedRequest-21` | `cl-dClosedLoop-0501@e1101a14` | `entry.claim` writing a patch or repeat build's derived plan record |
<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node d · opened 2026-10-21 · streams tooling
ids TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13
ids TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-22

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-coverage -->

Coverage of dPlacedRequest's 21 clause(s) and 37 owned node(s), over 0 spec(s) at or after SPEC_CARRIES_CUTOFF 2026-10-21:

- carried whole: 0
- carried in parts: 0 (none)
- moved, retired or deferred: none
- uncarried: 21 (cl-dClosedLoop-0120, cl-dClosedLoop-0121, cl-dClosedLoop-0122, cl-dClosedLoop-0123, cl-dClosedLoop-0503, cl-dClosedLoop-0124, cl-dClosedLoop-0125, cl-dClosedLoop-0126, cl-dClosedLoop-0127, cl-dClosedLoop-0128, cl-dClosedLoop-0129, cl-dClosedLoop-0130, cl-dClosedLoop-0131,
  cl-dClosedLoop-0132, cl-dClosedLoop-0133, cl-dClosedLoop-0134, cl-dClosedLoop-0135, cl-dClosedLoop-0136, cl-dClosedLoop-0137, cl-dClosedLoop-0138, cl-dClosedLoop-0501)
- stale: 0 (none)
- ambiguous: 0 (none)
- owned nodes no spec names: item.entry.claim, item.entry.orient, item.entry.place, item.entry.place-check, item.entry.place-owner, item.probe.design, item.probe.experiment, item.probe.judge, item.probe.judge-claimed, item.probe.pin, item.probe.return, item.probe.run, item.probe.trigger,
  policy-key.card.follows, policy-key.card.snapshot, policy-key.card.store, policy-key.leases, policy-key.leases.expiry-hours, policy-key.leases.granularity, policy-key.leases.offer-seconds, policy-key.leases.offline, policy-key.leases.overlap, policy-key.leases.queued-claim-days,
  policy-key.leases.renewal, policy-key.patch.ratify, policy-key.placement, policy-key.placement.check, policy-key.probe.experiment.authority, policy-key.probe.observations, policy-key.probe.points, policy-key.probe.raise, policy-key.resume.context, policy-key.resume.partial, record-kind.card,
  record-kind.lease, record-kind.probe, record-kind.probe-trigger
- specs derived from no clause: none
- clauses the token arm cannot see: cl-dClosedLoop-0122, cl-dClosedLoop-0126, cl-dClosedLoop-0129, cl-dClosedLoop-0133, cl-dClosedLoop-0136, cl-dClosedLoop-0137
<!-- /gen:build-coverage -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

- **Parent builds:** [dDeclaredLoop](../dDeclaredLoop/README.md)
- **Child builds:** [dBoundRoles](../dBoundRoles/README.md), [dKeptSession](../dKeptSession/README.md), [dTotalRecall](../dTotalRecall/README.md)
<!-- /gen:build-edges -->
