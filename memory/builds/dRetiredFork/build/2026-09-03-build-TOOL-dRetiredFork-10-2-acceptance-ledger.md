# Acceptance ledger — TOOL-dRetiredFork-10

**Serves:** journal TOOL-dRetiredFork-10

Tier-2 · node d · 2026-09-03

Three workflow gates stopped spelling `tools/` in their population filter and their predicate path.
Those literals were the cause of `nc carve-out 10/20`, `11/20` and `12/20` and inCMS rows 16, 17
and 18 — six hand-maintained divergence records across two adopters for a path each script can
derive from where it stands.

## The mechanism changed, and the pre-wiring run is why

S4 exists because §7 says to run a candidate predicate over the real tree before wiring it. It was
run, and it refuted S2's prescribed mechanism: a `workflows/` basename anchor NARROWS review-join's
population from 7 files to 5, while AC5 requires 7. §5 had named the risk as widening and this run
was built to catch that; it caught the reverse. The full run, with both near-miss directions, is
record 1 beside this one.

Built on a DERIVED prefix instead — `git rev-parse --show-prefix` from the script's own directory —
which spells no literal and reproduces the population exactly. **Parked**, because the owner
ratified S2 as written and a run does not overrule a ratified pick on its own authority.

Basename anchoring was kept where it is the right form: the two `SELF_EXCLUDE` patterns, which name
individual FILES. A subtree cannot be named by a basename when the subtree's name is the variable.

## Acceptance criteria

**Evidences:** TOOL-dRetiredFork-10

- AC1 — MET — `diff` reports all three gates byte-identical: their pre-change output was captured
  BEFORE any edit and compared after. The `--explain` diagnostic §5 asks for is behind the flag
  precisely so the default run's bytes stay pinned
- AC2 — MET — `bash tools/workflows/check-verifier-fanout.test.sh`, arm *AC2*: a fixture installed
  at `scripts/` with its hook a directory up resolves and exits 0, and its population is non-empty.
  The pre-change gate found nothing there
- AC3 — MET — same suite, arm *AC3*: a fixture whose ONLY hook copy is at `.claude/hooks/` resolves
  via rung 3. This is the inCMS shape, and a two-rung chain strands it
- AC4 — MET — same suite, arm *AC4*: with no `agent-cap.js` anywhere the gate exits 2 and the
  refusal names all three probes it tried. A fifth arm pins that fixtures A and C differ ONLY by
  the hook, so the refusal cannot be passing for an unrelated reason
- AC5 — MET — record 1, `2026-09-03-build-TOOL-dRetiredFork-10-1-predicate-run.md`, carries the run
  with hits and both near-miss directions. `bash tools/workflows/check-review-join.sh` still reports
  a 7-file population, verified against the shipped derivation
- AC6 — MET — `bash tools/check-kit-versions.sh` exits 0 after the bump, and with
  `gov:kit review-harness@` alone reverted to 1.5 it exits 1 naming that carrier by path. Both
  directions observed; the bare green could not have failed

## Where this deviates from the spec, and why

**S5 said bump review-harness AND agent-cap. Only review-harness was bumped.** `git status` over
`tools/hooks/` is empty — no agent-cap kit file changed in this unit. A version bump asserts that a
kit's bytes moved, and bumping one whose bytes did not move records something untrue in every
adopter's receipt. The three gates DELEGATE to agent-cap; they do not ship with it.

**§5's observability item is partly met, and the part that is not is named.** It asks each script to
print its resolved hook path and population size. AC1 forbids new output in the default run, and the
two criteria cannot both be satisfied unconditionally. `check-review-join.sh` reports both under
`--explain`; `check-verifier-fanout.sh` and `check-workflow-syntax.js` already print their population
size in their clean line and do not report the hook path at all. Adding it to either would fail AC1.

## What the test fixtures were hiding

Four arms across the two suites broke on the change, and every one of them broke for the same
reason: the fixtures copied the gate to the **bare repository root** and let it find its hook through
the hard-coded `$ROOT/tools/hooks/`. No kit installs a workflow gate at a repository root. Those
fixtures described a layout that has never existed in any adopter, and because they resolved through
the literal, they would have gone on passing while every real adopter stayed broken.

They now place the gate at `tools/workflows/` — an actual install shape — and the arms hold. This is
the more useful finding of the unit: the literal had propagated into the tests that were supposed to
be able to detect it.

## One incidental measurement: the install-prefix ratchet grades itself

The new `tools/workflows/README.md` carries four `tools/<kit>/` spellings — its invocation examples,
which is what every other kit README does and why each of them has a ratchet row. Recording that row
raised `tools/install-prefix-carried.txt`'s OWN count from 92 to 93, because the ratchet file is
itself a carrying file: its rows name the very paths it grades.

So `--write-ratchet` needs TWO passes to converge on any commit that adds a carrying file. The first
records the new file from the pre-write state and leaves its own row one behind; the second settles
it. Not a defect, and cheap once known — but a session that runs it once, sees `ROSE`, and assumes
its edit was rejected will go looking in the wrong place.
