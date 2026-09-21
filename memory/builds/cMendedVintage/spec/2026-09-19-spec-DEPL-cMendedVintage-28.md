# DEPL-cMendedVintage-28 — a receipt path that escapes is answered before an operator's untracked file

**Status:** CLOSED · rev-2 · 2026-09-19 · node c · Tier-2 · base 859daa67 · streams deployer · order 40

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-19-build-DEPL-cMendedVintage-28-acceptance-ledger.md](../build/2026-09-19-build-DEPL-cMendedVintage-28-acceptance-ledger.md) | journal | — |
| [2026-09-19-prompt-DEPL-cMendedVintage-28-2-build-brief.md](../prompts/2026-09-19-prompt-DEPL-cMendedVintage-28-2-build-brief.md) | journal | — |
| [2026-09-21-review-DEPL-cMendedVintage-1-diff-review-round2.md](../reviews/2026-09-21-review-DEPL-cMendedVintage-1-diff-review-round2.md) | diff-review | DEPL-cMendedVintage-1 DEPL-cMendedVintage-2 DEPL-cMendedVintage-3 DEPL-cMendedVintage-4 DEPL-cMendedVintage-5 DEPL-cMendedVintage-6 DEPL-cMendedVintage-7 DEPL-cMendedVintage-8 DEPL-cMendedVintage-9 DEPL-cMendedVintage-10 DEPL-cMendedVintage-11 DEPL-cMendedVintage-12 DEPL-cMendedVintage-13 DEPL-cMendedVintage-14 DEPL-cMendedVintage-15 DEPL-cMendedVintage-16 DEPL-cMendedVintage-17 DEPL-cMendedVintage-18 DEPL-cMendedVintage-19 DEPL-cMendedVintage-20 DEPL-cMendedVintage-21 DEPL-cMendedVintage-22 DEPL-cMendedVintage-23 DEPL-cMendedVintage-24 DEPL-cMendedVintage-25 DEPL-cMendedVintage-26 DEPL-cMendedVintage-27 DEPL-cMendedVintage-29 TOOL-cMendedVintage-1 TOOL-cMendedVintage-2 TOOL-cMendedVintage-3 TOOL-cMendedVintage-4 TOOL-cMendedVintage-5 TOOL-cMendedVintage-6 TOOL-cMendedVintage-7 TOOL-cMendedVintage-8 TOOL-cMendedVintage-9 TOOL-cMendedVintage-10 TOOL-cMendedVintage-11 TOOL-cMendedVintage-12 TOOL-cMendedVintage-13 TOOL-cMendedVintage-14 TOOL-cMendedVintage-15 TOOL-cMendedVintage-16 TOOL-cMendedVintage-17 TOOL-cMendedVintage-18 TOOL-cMendedVintage-19 |

<!-- /gen:spec-records -->

## 1. Goal

`update`'s preamble refuses a receipt-claimed path that is present in the worktree and absent from
the index. `DEPL-cMendedVintage-24` widened that refusal's population to every writing disposition,
which put the `attributes` row into it for the first time. A path that ESCAPES the target root is
present in no index by construction, so the shadow refusal now answers first and tells the operator
to `git add` a path git refuses as outside the repository. The containment guard still holds — that
was measured on bytes — but it is unreachable on this branch and its arm can no longer see it. Grade
containment before shadowing.

## 2. Scope (IN)

- **S1** Every receipt path the preamble is about to grade is checked for CONTAINMENT first, and an
  escaping path takes the containment refusal naming the row that supplied it. A receipt defect is
  answered as a receipt defect. Observed by AC1.
- **S2** The untracked-shadow refusal keeps its widened population and its wording, unchanged, for
  every path that is inside the target. `DEPL-cMendedVintage-24` exists because gov was staging an
  operator's uncommitted `.gitattributes` on every run, and nothing here narrows that. Observed by
  AC2.
- **S3** The sibling arm asserting the outside file still holds gov's marker pair stops being
  satisfied by a refusal for an unrelated reason. It is green today over a run that never reached
  the branch it grades, which is a skip wearing a pass. Observed by AC3.
- **S4** `tools/govkit/selftest.py` gains the ORDERING arm the collision hid: with the containment
  call staged out, the escaping path is answered by the shadow refusal, and the arm reds naming
  which guard spoke. A guard that is merely first today is first by accident until something asserts
  it. Observed by AC4.

## 3. Non-goals (OUT)

- No change to `demand_contained_dest` itself, nor to where the `pins` arm calls it. That call is
  correctly placed above the join, above the read and above the withdrawal exit; the defect is that
  the run dies before the loop starts.
- No narrowing of the shadow refusal's population back to a role literal. That is the change
  `DEPL-cMendedVintage-24` made deliberately and `DEPL-cMendedVintage-26` scoped correctly; undoing
  it reopens a destroyed-work blocker to fix a diagnostic.
- No repair of the fixture in place of the engine. Contorting the fixture so the shadow guard has
  nothing to catch would restore the arm and leave the operator with the impossible remedy.
- No new refusal text. The containment message already names the row, the destination and the
  source; it simply never gets to speak on this branch.

### Edges

- **consumes-from** `DEPL-cMendedVintage-23` — that unit's containment guard is what this makes
  reachable, and its two arms are what this returns to green.
- **consumes-from** `DEPL-cMendedVintage-24` — that unit's widening created the collision, and its
  own subject must survive this repair untouched.
- **hands-off** external — an operator holding a receipt whose path escapes is told so, rather than
  told to stage a file git cannot stage.

## 4. Design

Two guards answer two different questions about the same row. An ESCAPING path is a defect in the
receipt, which is committed, hand-editable and text-merged. An UNTRACKED SHADOW is a state of the
operator's worktree. The first is about the data gov was handed; the second is about the tree gov is
writing into. Answering the second first is what produces the impossible remedy, because a path
outside the repository can never be staged.

Ordering them is therefore not a preference. It is which question is answerable: a path that escapes
has no index membership to report, so the shadow predicate's own inputs are undefined for it.

THE MEASUREMENT THIS RESTS ON, so a later reader does not re-derive it. Three engine variants against
one fixture: shipped, the outside file is unchanged and the run refuses with the shadow message; with
the shadow refusal staged out the run refuses with the containment message and the file is still
unchanged; with both staged out the run exits 0 and mutates the file. The third variant is what makes
the second meaningful — it proves the fixture reaches the splice rather than passing by never getting
there.

rev-2. THE PRECONDITION THAT TABLE OMITS, and it decides which arms are red. The shadow predicate
tests index membership AND presence on disk, so the collision needs the escaping path to exist in the
worktree. It does on the WITHDRAWAL fixture, which writes real bytes there to prove the splice
destroys them, and it does not on the creation fixture, whose whole assertion is that nothing
appears. So the shipped engine already answered the creation branch with the containment refusal, and
both red arms are the withdrawal branch's: the one asserting its refusal names containment, and the
liveness arm beside it — which could no longer reach the splice at all, because staging the
containment call out left the shadow refusal answering in its place. That second one is the sharper
finding: the liveness helper has to defuse the shadow refusal as well, or the arm that reproduces the
defect is reproducing a different refusal.

## 5. Production-readiness checklist

- security — this changes which refusal an escaping path receives, never whether it is refused. The
  byte measurement above is the evidence, and `AC1` re-takes it.
- perf / scale — one containment test per graded row in the preamble, over a list already in memory,
  against a loop that already stats each path.
- error / empty / loading states — a row that is neither escaping nor shadowed takes neither
  refusal, unchanged; a row that is both takes containment, which is the point.
- observability — the operator gets a message naming the receipt row rather than a remedy that
  cannot be run, and `AC4` makes the ordering itself observable instead of incidental.
- risks — the real risk is narrowing the shadow refusal while reordering it and reopening
  `DEPL-cMendedVintage-24`'s destroyed-work blocker. `AC2` is written against exactly that and is the
  criterion this unit would most plausibly fail.
- testing — `AC1` to `AC4` run the real verb against scratch fixture targets, with the failing case
  staged for each. The permanent arms are declared in section 7.
- migration — none. No recorded data changes and no receipt field moves.
- user docs — `WIRE-INTO-PROJECT.md` gains one sentence saying an escaping receipt path is reported
  as a receipt defect, because the shipped text currently implies the operator can stage their way
  out of it.

## 6. Acceptance criteria

- **AC1** — When a fixture's receipt claims a path outside the target root AND real bytes exist
  there, `update --write` refuses naming `leaves the target repository` and those bytes are
  byte-identical afterwards. Red when: the run refuses with the untracked-shadow wording instead,
  which is the shipped behaviour and is reproducible before the change. rev-2 adds the
  bytes-exist precondition: without it the shadow predicate does not match, the shipped engine
  answers with containment already, and the criterion grades nothing.
- **AC2** — When a fixture's receipt claims an INSIDE path absent from the index, `update --write`
  still refuses with the untracked-shadow wording, and the operator's bytes are untouched. Red when: the reorder narrowed the shadow population, reopening
  the blocker `DEPL-cMendedVintage-24` closed.
- **AC3** — The sibling arm asserts the escaping file's `govkit:lf-pins` marker pair survives a run
  that REACHED the containment guard, not merely a run that refused. Red when: the arm stays satisfiable
  by any refusal, which is what makes it green today.
- **AC4** — With `demand_contained_dest` staged out of the preamble, the ordering arm REDS naming
  the guard that answered. Red when: no arm asserts the order, leaving a guard that is first by
  accident.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix`

New arm: `tools/govkit/selftest.py` · the ordering arm S4 names, beside the repaired `[-23]` AC3 and
its sibling · the `BRANCH_PIN` floor in `tools/govkit/refusal_join.py` is re-derived only if the
branch count moves — rev-2: it does not move, because this unit adds a CALL to an existing
containment helper and no new `raise` of its own.

rev-2. THE LIVENESS HELPER CHANGES WITH THE ARMS, and that was not foreseen. It staged out one
containment call by line; it now takes the guard lines to stage as a parameter and defuses the
untracked-shadow refusal alongside them, because an escaping path present on disk is caught by that
refusal whatever the containment calls do — so the arm that reproduces the defect could not reach the
splice. The ordering arm is the same helper with only the preamble call staged out.

## 8. Open questions

- **Q1 — should the preamble grade containment for every row or only for writing dispositions?**
  RESOLVED (agent, 2026-09-19, delegated): every row it grades. The preamble's population is already
  the graded set, and a read-only row whose receipt path escapes is still a receipt defect worth
  naming; scoping it to writers would make the message depend on a disposition the operator did not
  choose.

## 9. Revision log

- rev-1 · 2026-09-19 · initial draft, authored mid-build by the main loop after a read-only
  attribution measured the containment guard holding on bytes and traced the two red arms to a
  guard-ordering collision introduced at `d2de6795`. Adopted because the arms are this build's own
  and the diagnostic regression reaches every adopter.
- rev-2 · 2026-09-19 · built. Three corrections, each measured against both engines on scratch
  fixtures. Section 4's variant table omitted the precondition that decides which arms are red: the
  shadow predicate also tests presence on disk, so the collision reaches the withdrawal fixture and
  not the creation one, and AC1 gains that precondition rather than claiming a red-when its own
  fixture cannot produce. Section 7 records that the liveness helper had to change with the arms —
  staging the containment call out is no longer enough to reach the splice, because the shadow
  refusal answers in its place, so the helper now takes the guard lines to stage and defuses that
  refusal too. The `BRANCH_PIN` clause is answered rather than left open: the unit adds a call and
  no new refusal, so the count does not move.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "grade a receipt path for containment before testing its index membership"`
returns `demand_contained_dest` and nothing else: it is the one containment predicate in the engine,
called at four sites, and this unit adds a fifth rather than writing a second. AN EXISTING SEAM FITS,
and the evidence is that the call this unit adds is the same function with the same arguments the
`pins` arm already passes it.

What is NOT reusable is the ordering itself, which is a property of the preamble and is asserted
nowhere; S4 is the first arm over it.

Recall terms used: govkit update preamble untracked shadow index membership containment escaping
receipt path attributes row refusal ordering guard.
