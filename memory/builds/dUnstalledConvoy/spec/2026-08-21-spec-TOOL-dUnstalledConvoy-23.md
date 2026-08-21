# TOOL-dUnstalledConvoy-23 — the dispatch write-set grading, redesigned against four rounds of evidence, and turned back on

**Status:** SPECCED · rev-1 · 2026-08-21 · node d · Tier-2 · base d9728f89 · streams tooling

## 1. Goal

Make check 23's grading of a dispatch declaration against what the pass committed correct enough to
ship ON, and then ship it ON by flipping `DISPATCH_GRADING`'s default. Today it is inert: the
declarations are recorded, the grading is dark, and the leg announces that on every run carrying
dispatch rows. That is a holding position, not an answer.

## 2. Scope (IN)

- **S1 — check 23's window is bounded above.** Each dispatch row is graded against the commits between
  its own anchor and the NEXT anchor for the same unit, not `anchor..HEAD`. This is what makes a
  multi-pass unit gradeable at all and every other change here assumes it.
- **S2 — the two openness questions are split.** Condition 1 keeps the intersection-filtered set it has
  today; the re-declaration lookup keys on raw `pass_commit` openness. `pass_commit` itself is not
  touched.
- **S3 — `cur` is selected by best match, not `tail -1`**, and the case where two open rows both
  overlap the new declaration is REFUSED as undecidable rather than resolved by position.
- **S4 — a scan-forward openness helper** in `lib-unattended.sh`, the one change here that adds a
  library function, so S1 and S2 read the same history the same way.
- **S5 — four one-liners with their own arms:** the narrowing test compares normalised paths against
  the normalised record; `normpath` collapses an interior `/./`; the empty-proof announcement measures
  condition 1's actual population rather than `sibrows`; and the re-declaration gate drops its
  `curgrp != grp` nesting.
- **S6 — `DISPATCH_GRADING` defaults ON** once S1–S5 land with their arms, in the same unit and not a
  follow-up. A fix nobody turns on is the state this unit exists to leave.
- **S7 — the discipline is part of the scope, not a note about it.** Every change lands with its arm in
  the same commit, and every arm is observed RED before the fix goes in.

## 3. Non-goals (OUT)

- The declaration grammar, the recording verb, and condition 1 and condition 3's refusals. They work
  and no round found a defect in them.
- `pass_commit`'s permissiveness. Round 3 established that pushing an intersection filter into it makes
  check 23 report an out-of-lane pass as "a pass that produced no change" — the check going green on
  the exact defect it exists to catch. Round 4 confirmed it. Reversing this is a regression, not a fix.
- `normpath`'s ordering, B2's overlap gate, and cross-component arm 3b. Round 4 named all three as
  correct and warned the next round not to undo them.
- The two KNOWN boundaries: a commit writing inside a pass's declared lane closes that pass, and a new
  pass partly overlapping its predecessor is refused as a narrowing. Both are documented and pinned.
- Any change to the acceptance ledger, the landing anchors, or the rescope verbs.

## 4. Design

The spine is S2, and the reason four rounds failed is that it was not done. One predicate served three
callers whose edges disagree: condition 1 wants strict openness, the re-declaration lookup wants strict
openness for THIS pass kind, and check 23 wants a permissive attribution oracle. Rounds 1–3 each tried
to satisfy all three with one answer and each produced a defect in the direction the other two pulled.

S1 is what makes S2 safe. With the window bounded above by the next anchor for the same unit, a row is
graded against its own pass's commits and nothing else, so the multi-pass shape M6 sanctions stops
being a source of cross-attribution. D2's reproduction is the proof: with an unbounded window, row 1 of
a unit whose first pass produced no change is graded against pass 2's commit.

S3 removes the last positional guess. `tail -1` picked an open row by order of appearance; where two
open rows both overlap the incoming declaration there is no correct pick, and refusing is the only
answer that does not silently choose one. That refusal is reachable in-band — the run declares
narrower, or commits the pass it already has.

S4 exists so S1 and S2 cannot drift. The helper answers "which commits belong to this row" once, and
both the driver and the leg call it. This is the same argument that produced `lib-unattended.sh`, and
the argument survived round 4: what failed was not the library, it was giving one function three
questions.

S6 is the point of the unit. The grading is dark today because it could not be trusted, and the only
thing that changes that is the arms — which is why S7 is in scope rather than in a comment.

## 5. Production-readiness checklist

- **security** — the mechanism is a disjointness proof for concurrent passes inside one run. Every check
  still runs under the run's own uid and a determined run can still declare a wide set up front; the
  protocol says so and this unit does not claim to change it. What it restores is catching a run that
  is WRONG.
- **perf/scale** — S1 narrows each row's commit window, so the leg does strictly less `git log` work per
  row than the unbounded form. S4 adds one helper call per row.
- **a11y / i18n** — N/A, a shell gate with no user surface.
- **error/empty/loading states** — the empty-proof announcement is S5's third item: condition 1 over an
  empty population must say so, and today it measures the wrong set.
- **observability** — the dark announcement is removed by S6 and replaced by ordinary grading output.
- **testing/gates** — the full bar; the driver, leg and cross-component suites; every new arm RED-first.
- **migration/rollback** — `DISPATCH_GRADING` stays a declared key, so a project that hits trouble sets
  it blank and is back to today's behaviour without a code change. That is the rollback.
- **help/ docs** — `PROTOCOL.template.md`'s conf table and the key's own comment both describe a default
  that S6 changes; both are updated in the same commit.

## 6. Acceptance criteria

- **AC1** — a row whose unit has a LATER dispatch row is graded only against commits before that later
  anchor, observed in `tools/unattended/check-unattended.test.sh`.
- **AC2** — a unit whose first pass produced no change does not have row 1 graded against pass 2's
  commit; the no-change branch reports instead, observed in `tools/unattended/check-unattended.test.sh`.
- **AC3** — condition 1 and the re-declaration lookup read DIFFERENT openness sets, and an arm
  distinguishes them: a pass that committed entirely outside its lane is open to condition 1 and closed
  to the re-declaration lookup, observed in `tools/unattended/unattended.test.sh`.
- **AC4** — the D1 sequence no longer retracts a finding: declare narrow, commit out of lane, re-declare
  wide, and the leg still reds, observed in `tools/unattended/check-unattended.test.sh`.
- **AC5** — two open rows both overlapping a new declaration is a REFUSAL naming both, observed in
  `tools/unattended/unattended.test.sh`.
- **AC6** — `normpath` collapses an interior `/./`, observed in `tools/unattended/unattended.test.sh`.
- **AC7** — the narrowing test compares normalised paths, so a re-declaration spelled `work/one/` is
  judged against a record holding `work/one`, observed in `tools/unattended/unattended.test.sh`.
- **AC8** — the empty-proof announcement fires exactly when condition 1's own population is empty,
  observed in `tools/unattended/unattended.test.sh`.
- **AC9** — `DISPATCH_GRADING` is unset in the shipped example and the project conf and the grading
  RUNS; the dark announcement is gone, observed by `bash tools/unattended/check-unattended.sh`.
- **AC10** — every arm added by this unit was observed RED against the pre-fix code, observed in
  `2026-08-21-build-TOOL-dUnstalledConvoy-23-1-red-first.md`, which names the staged break per arm.
- **AC11** — the full bar is green, observed by `bash tools/run-gates/run-gates.sh`.

## 7. Gates

`bash tools/run-gates/run-gates.sh`, with the unattended driver, leg, cross-component and adopter
self-tests as the legs that actually exercise this. `GATE_FULL=1` for the Definition of Done.

## 8. Open questions

**F1 — does S6 flip the default, or does the owner flip it?** RESOLVED: this unit flips it. A fix
shipped dark is the state the unit exists to leave, and leaving the flip to a later decision reproduces
the holding position under a different name. The rollback is one conf key, which is what makes flipping
it the reversible choice rather than the brave one.

## 9. Revision log

- rev-1 · 2026-08-21 · initial draft, written against the four review records under `../reviews/` rather
  than against the code, because the code is the thing those records found wrong.

## 10. Reuse audit

`lib-unattended.sh` already exists and is the right home for S4 — this unit adds one function to it
rather than a second library. `covers`/`overlaps`/`normpath`/`id_in` are all reused unchanged. No new
file, no new kit, no new conf key beyond the one already declared.
