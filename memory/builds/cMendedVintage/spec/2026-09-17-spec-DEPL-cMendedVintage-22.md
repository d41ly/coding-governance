# DEPL-cMendedVintage-22 — the gate-leg drift guard compares the target, not gov against itself

**Status:** CLOSED · rev-2 · 2026-09-17 · node c · Tier-2 · base 859daa67 · streams deployer · order 32

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-17-build-DEPL-cMendedVintage-22-acceptance-ledger.md](../build/2026-09-17-build-DEPL-cMendedVintage-22-acceptance-ledger.md) | journal | — |
| [2026-09-17-prompt-DEPL-cMendedVintage-22-2-build-brief.md](../prompts/2026-09-17-prompt-DEPL-cMendedVintage-22-2-build-brief.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

The drift guard in `write_gate_legs` compares `receipt["gate_runner"]["emitted"]` against this run's
fresh resolution of gov's OWN descriptor. Both sides are gov's. The target's actual manifest row is
assigned and never read, so a target that hand-edits a row gov owns is never detected, and any
gov-side `argv` change reds an adopter whose manifest is byte-identical to what gov wrote. The
refusal withholds the whole manifest, the withheld path re-stamps the old rows, and the next run
compares identically. Compare the row the message names.

## 2. Scope (IN)

- **S1** The guard reads the TARGET's manifest row and compares it against the receipt's recorded
  row. A row gov owns whose `argv` or `guard` the target changed is the drift, and it is what the
  existing message already claims to report. Observed by AC1.
- **S2** A gov-side descriptor change — a different `argv` for a leg the receipt records — is NOT
  drift and does not refuse. It is a new vintage, which is the thing `update` exists to deliver.
  Observed by AC2.
- **S3** The refusal keeps withholding the whole manifest, unchanged. A target that really did edit
  a gov-owned row still stops the emission for every leg in the run, because a manifest half-written
  against a tampered file is worse than one not written. Observed by AC3.
- **S4** `tools/govkit/selftest.py` gains the arm the existing fixture comment says it cannot have:
  tampering the RUNNER row is asserted to REFUSE, beside a gov-side `argv` change asserted to
  proceed. Observed by AC1 and AC2.

## 3. Non-goals (OUT)

- No change to what the withheld path writes. `emitted = list(prior)` is correct for a run that
  emitted nothing, and changing it is a separate question from which runs reach it.
- No recovery verb for an adopter already wedged by the shipped predicate. The fix stops the state
  being created; an adopter who reached it before this lands edits their own receipt, and the
  release note is where that belongs, not a new flag.
- No change to the gate-lint descriptor's own argv. Its third element left in this build for reasons
  that unit recorded, and reverting it would trade this defect for that one rather than closing it.
- No widening to the non-manifest order path. That path writes a document, not rows a target edits,
  and the review files its own finding against it separately.

### Edges

- **consumes-from** `DEPL-cMendedVintage-13` — that unit made `update` a second caller of this
  function, which is what turned a latent apply-only defect into one two verbs reach.
- **hands-off** external — an adopter stops being wedged by a gov-side descriptor edit; nothing else
  in this build reads the guard.

## 4. Design

The comparison has three values available and uses the wrong two. `prior` is gov's record of what
gov last wrote. The fresh `argv` and guards are gov's current resolution. The target's current row,
read from the target's own manifest, is only ever assigned.

Drift is a statement about the TARGET, so the comparison is the target's row against the receipt's
recorded row. Gov's fresh resolution is then what gets WRITTEN, which is what a new vintage means.

Two consequences fall out and both are load bearing. A target that never touched the row compares
equal however far gov's descriptor has moved, so the wedge cannot form. And a target that edited the
row is caught for the first time, which is a behaviour change on arrival: an adopter carrying a
hand-edit they have been getting away with will red, truthfully, with the message that already
exists.

Why not compare all three: a run that refuses whenever any pair disagrees cannot tell a new vintage
from a tampered row, which is the defect one level up rather than a stricter version of the fix.

## 5. Production-readiness checklist

- security — the guard decides whether gov overwrites a row in a file the target owns. Reading the
  target's row is what makes the decision about the target at all, so this strictly narrows what gov
  will silently overwrite.
- perf / scale — one dict lookup per owned leg, over a list already in memory. No new read.
- error / empty / loading states — a leg the receipt records and the target no longer carries takes
  the existing absent-row path unchanged; a receipt with no `gate_runner` block takes the existing
  empty-prior path and every row is new.
- observability — the existing refusal message is already written for this comparison and needs no
  change, which is itself the evidence that the comparison was the half that drifted.
- risks — the real risk is the behaviour change on arrival: a target carrying a hand-edited gov row
  reds where it used to pass silently. That is the guard working, and `AC1` is written to observe it
  rather than to avoid it.
- testing — `AC1` to `AC3` run the real verbs against scratch fixture targets. The permanent arms
  are declared in section 7.
- migration — none for a healthy target. An adopter already wedged edits their receipt once; the
  non-goal above states why no verb is added for it.
- user docs — `WIRE-INTO-PROJECT.md` gains one sentence saying a gov-side leg change is delivered
  rather than refused, because the shipped text currently tells an adopter to answer the red by
  editing their own argv.

## 6. Acceptance criteria

- **AC1** — When a fixture target's manifest row for a gov-owned leg is hand-edited and
  `python tools/govkit/govkit.py update --target <fixture> --write`
  runs, the run REFUSES naming that leg. Red when: the guard still compares the receipt against
  gov's fresh resolution, in which case the tamper is invisible and the row is silently overwritten.
- **AC2** — When gov's descriptor changes a leg's `argv` and the target's manifest still carries
  what gov last wrote,
  `python tools/govkit/govkit.py update --target <fixture> --write`
  emits the new row and does not refuse. Red when: a gov-side change is read as drift, which is the
  shipped defect and is reproducible at BASE before the change.
- **AC3** — When the refusal of AC1 fires, no leg in that run is written to the target's manifest and
  `install.json`
  carries the previous emitted rows. Red when: the fix narrows the refusal into a per-leg skip, which
  writes a manifest half-graded against a file the target tampered with.

## 7. Gates

`govkit selftest` · `govkit selfcheck` · `govkit refusal join` · `govkit acceptance matrix`

New arm: `tools/govkit/selftest.py` · a fixture whose manifest row is tampered, asserted to refuse,
beside a fixture whose gov-side argv moved, asserted to emit · the `BRANCH_PIN` floor in
`tools/govkit/refusal_join.py` is re-derived only if the branch count moves. Nothing here adds or
removes a refusal branch, so that floor does not move.

Two fixture constructions are load bearing and were found by building them wrong first. The new
vintage must come out of the SAME scratch gov checkout: applying from one and updating from a second
refuses upstream of this step, because the receipt's recorded gov commit does not resolve in another
clone, and every arm then grades a run that never reached the legs step — measured, three of them
passing vacuously and the rest red for a reason with nothing to do with gate legs. And the tamper fixture
must also DELETE a sibling row the receipt still claims and re-serialise the file at an indent the
emitter never produces — without both, a per-leg skip and a whole-manifest withhold leave identical
bytes and AC3 grades nothing.

## 8. Open questions

- **Q1 — should the tamper refusal name a remedy?** RESOLVED (agent, 2026-09-17, delegated): not in
  this unit. The existing message names the leg and the file, which is what an operator needs to find
  the edit; a remedy sentence that recommends a verb is the shape that wedged adopters in the first
  place, and it belongs with whoever writes the release note.

## 9. Revision log

- rev-1 · 2026-09-17 · initial draft, authored mid-build by the main loop after the closing review
  adjudicated finding B1 a BLOCKER. Adopted under the protocol's discovery rule as a blocker between
  this run and its own landing.
- rev-2 · 2026-09-17 · §7 §8 · closed by the build pass. No criterion changed and none was amended.
  §7 gains the two fixture constructions the arms turned out to need, both found by writing them
  wrong and measuring the result: the new vintage must come out of the SAME scratch gov checkout, and
  the tamper fixture must delete a sibling row and re-serialise at a foreign indent or AC3 cannot
  tell a per-leg skip from a withhold.
  §8's Q1 mark is re-spelled to the resolver form the template's closed pair allows. The decision is
  untouched; `main loop` is not one of the two resolvers, and this run is delegated by a standing
  mandate rather than owner-signed, so `agent … delegated` is the truthful one.
  §5's user-docs line is discharged as a short subsection rather than the single sentence it named —
  same content, plus the remedy an adopter needs, in the runbook rather than in the refusal message
  Q1 rules on.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "compare a target manifest row against the receipt row gov recorded for it"`
returns no seam: the map holds `write_gate_legs` as the only writer of a target's gate manifest and
`cmd_check`'s block-drift loop as the only other reader of a gov-owned region's drift, and that loop
already compares the TARGET's bytes against a recorded digest rather than gov against itself. NO
EXISTING SEAM FITS, and the evidence is that the one correct comparator in the tree is in a different
verb over a different artifact.

The correct shape is therefore already demonstrated one file over: `cmd_check` reads the target,
hashes it, and compares against the receipt. S1 makes the gate-leg guard ask its question the same
way, which is why this is a comparison change and not a new mechanism.

Recall terms used: govkit gate leg manifest emitted receipt drift guard argv tamper vintage withheld
target-owned row install.json.
