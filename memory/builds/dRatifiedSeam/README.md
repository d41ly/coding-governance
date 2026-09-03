---
slug: dRatifiedSeam
node: d
opened: 2026-09-03
streams: tooling+deployer
roster: TOOL+DEPL
ids: DEPL-dRatifiedSeam-1 TOOL-dRatifiedSeam-1
---

# dRatifiedSeam — build the two owner rulings dRetiredFork parked

## The problem this build exists to solve

`dRetiredFork` closed with four parked questions and the owner answered all four on 2026-09-03.
Two were records and are done. Two are work, and neither is optional: each names a mechanism that
is currently broken or blocked, and each was chosen over the run's own recommendation or in spite
of the run declining to act.

**`DEPL-dRetiredFork-13`** — `update` may not land a gov source that has no receipt row, because a
standing predicate asserts the target's tracked-file count never rises. The capability is built and
was measured working against a live adopter (9 landable, 8 correctly reported-not-landed). The
ruling supersedes the invariant rather than routing around it.

**`TOOL-dRetiredFork-41`** — the `passes-harnessed` directive routes M6's pass sequence through
`unattended-build.js`, whose AUDIT stage orders a sidechain agent to invoke the Workflow tool. A
sidechain holds neither Workflow nor Agent; the capability is absent, not policed. The stage agent
was right to refuse, and the route has never completed. The ruling is to fix the harness.

## Start here

Both units are Tier-2 and both are BLOCKED on nothing — the rulings are their authorization, and
each is recorded in `memory/DECISIONS.md` with its trade-off. Read the ruling before the spec: the
`DEPL` one was decided AGAINST the run's recommendation and the reasoning for the road not taken is
part of what the unit must respect.

Next action: the M4 spec audit, then build in order 1 then 2.

<!-- gen:build-index -->
**Build status:** OPEN · 2 unit(s) · node d · opened 2026-09-03 · streams tooling+deployer
ids DEPL-dRatifiedSeam-1 TOOL-dRatifiedSeam-1

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [DEPL-dRatifiedSeam-1 — the tracked-count invariant admits additions, and `update` lands a new source](spec/2026-09-03-spec-DEPL-dRatifiedSeam-1.md) | 1 | 2 | OPEN | rev-3 | 2026-09-03 |
| [TOOL-dRatifiedSeam-1 — the harness AUDIT stage runs where Workflow exists](spec/2026-09-03-spec-TOOL-dRatifiedSeam-1.md) | 2 | 2 | OPEN | rev-2 | 2026-09-03 |
<!-- /gen:build-units -->

Records: 0 bound to this build, across 1 record folder(s).

Ids no record names: DEPL-dRatifiedSeam-1 TOOL-dRatifiedSeam-1.

Ids no `spec-audit` record has ever named: DEPL-dRatifiedSeam-1 TOOL-dRatifiedSeam-1.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `DEPL-dRatifiedSeam-1` | no |
| 2 | `TOOL-dRatifiedSeam-1` | no |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->

## What grounding already established

Run before either spec was authored, and both findings changed the scope:

- **The `DEPL` unit is far smaller than the ruling assumed.** The ruling says nineteen arms;
  `grep` for `[-11]` returns eighty lines, and both figures are wrong for the same reason. `[-11]`
  is the UNIT tag of `DEPL-dCarriedReceipt-11` and covers renames, refusals, seed rows and two
  other ACs. Only **four** places in `tools/govkit/selftest.py` assert a tracked-file count, and
  exactly ONE is the standing predicate. The nineteen were a CASCADE: one write run that added
  files, nineteen downstream arms in the same fixture failing as a consequence.
- **The `TOOL` unit is more tractable than its own prior record suggests.** `TOOL-dBriefedPass-4`
  records that a Workflow harness buys pass ORDER and never ENFORCEMENT, and that two of its shapes
  were forced by `agent-cap.js` denying `agent()` in any loop. That denial is SUPERSEDED: the hook
  carries a third marker, `gov:sequential-agents(5)`, spelling ratified by the owner 2026-09-01,
  and it is the only marker that admits a loop. It exists precisely because the old gap made a
  unit-iterating harness unwritable.
