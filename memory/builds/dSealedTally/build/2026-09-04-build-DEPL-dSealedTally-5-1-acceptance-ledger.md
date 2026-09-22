# Acceptance ledger — DEPL-dSealedTally-5

**Serves:** journal DEPL-dSealedTally-5

Tier-2 · node d · 2026-09-04

## The headline: the bar can now run where the merge protocol asks for it

The suite's real-root `update` invocations defaulted to `--to HEAD`, and `demand_published_vintage`
refuses a commit no ref contains. A `--no-ff` merge on a detached head is exactly that commit — and
it is what the merge protocol asks a run to produce, at the moment it asks for a gate. The suite was
grading THE SHAPE OF THE HEAD rather than the tree it was handed.

**Observed, not argued.** A merge commit was made on a detached head from this build's branch,
verified to be reachable from no ref and to carry a tree identical to the branch tip's, and the
suite run there exits 0 at 1116 arms. At base `0f19429a` that same head shape red 46.

## Tree identity, and why ref-reachability alone is the wrong rule

Measured on a scratch repository holding a detached merge: `parent^1` was ref-reachable and carried
the WRONG tree; `parent^2` carried the right one. `HEAD^` picks the first, so a "nearest
ref-reachable ancestor" rule — which is what rev-1 of this spec said — grades the pre-merge tree and
reports on something nobody asked about. The pin therefore requires BOTH conditions.

## The criteria

**Evidences:** DEPL-dSealedTally-5

- AC1 — MET, OBSERVED — `python tools/govkit/selftest.py` exits 0 at 1116 arms from a `--no-ff`
  merge commit made on a detached head, `14de2baa`, confirmed reachable from no ref and carrying the
  branch tip's tree. This is the state that produced `DEPL-dRatifiedSeam-6`.
- AC2 — MET, OBSERVED — `python tools/govkit/selftest.py` on that same tree checked out as a
  branch also exits 0 at 1116 arms, so the fix does not trade one head shape for another.
- AC3 — MET, OBSERVED — `[-ST5]` arms assert BOTH pin conditions: its tree equals the working
  tree's, and some ref contains it. Either alone is satisfied by a silently-defaulted HEAD.
  Independently, the suite PRINTS which branch it took — `(HEAD)` on a branch,
  `(a ref-reachable ancestor with this tree)` on the detached run — so the two are distinguishable
  without reading code.
- AC4 — MET, OBSERVED — `resolve_gov_pin` is driven against a scratch repository holding a detached
  commit no ref contains and REFUSES by name, then the same commit is given a branch and it
  RESOLVES. The second half is what shows the refusal grades ref-reachability rather than scratch
  repositories in general.
- AC5 — MET, OBSERVED — an arm in `tools/govkit/selftest.py` counts the invocations carrying their
  own inline `--to` and asserts 4, by an ANCHORED match. The unanchored form counts `gov_run(` too
  and returns 9, which is the miscount rev-3 of this spec shipped as a fact.
- AC6 — MET BY AC1's `python tools/govkit/selftest.py` RUN, not by a dedicated arm. That run
  exercises every apply-then-update
  fixture in the suite with the pin an ANCESTOR of HEAD, which is precisely the state
  `demand_forward_vintage` refuses as a downgrade. It exits 0, so the receipt re-stamp works. No arm
  isolates the property; it is covered as a consequence.
- AC7 — MET, OBSERVED BY STAGED BREAK — reverting the `gov_commit` comparison from the pin back to
  `HEAD`, on the detached head where the two differ, reds EXACTLY ONE arm: *and re-stamps the
  receipt at the new commit*, with the detail showing it received `629cf067` where it expected the
  merge. One mutation, one failure, the right one.
- AC8 — MET — 1116 arms, six more than the 1110 at the head of `order 4`, against a spec floor of
  four.

## Why the staged break had to happen there

Reverting an arm to `HEAD` is a NO-OP whenever the pin equals HEAD, which is every run on a branch.
On a branch that mutation passes and proves nothing. The detached merge is the only state where the
two values differ, so it is the only place AC7 is a real observation rather than a ritual.

## What went wrong while building this, and what it cost

The arms were inserted twice. The first attempt's repair script excised from a verified START anchor
to a POSITIONAL end marker, and the `[-RS1]` block happened to sit between them — nine arms from a
previous build, deleted. Caught by counting every block's arms afterwards rather than trusting the
script's own success message, and reverted to the last commit.

The rule that would have prevented it: **an insertion needs one verified anchor; an excision needs
two.** The generator had asserted anchor UNIQUENESS for several units by then, but uniqueness of the
start says nothing about where the end lands. The second attempt inserts only.

## Residue

None specific to this unit. The `apply` verb still has no vintage argument, which is deliberate —
giving it one adds public surface to a product verb and is an owner turn this run could not take —
so the fixture re-stamp stands in for it, and AC6 is covered by consequence rather than by an arm
that isolates it.
