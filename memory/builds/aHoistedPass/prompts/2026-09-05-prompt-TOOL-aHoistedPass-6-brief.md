**Serves:** journal TOOL-aHoistedPass-6

# Brief — TOOL-aHoistedPass-6, the hoist itself

*The pass that builds the unit the previous stretch of this run deliberately refused. Read this,
then read the spec whole. The spec is the design; this says what the spec cannot: why the last pass
stopped, what has changed, and what verification is actually owed.*

## Why this unit was not built the first time, and what is different now

The round-2 BUILD stage built seven units and stopped at this one. Its recorded reason is in the
run-state file under `aHoistedPass-build-stopped-at-order-5`: it priced the unit as restructuring an
835-line workflow script, adding a `--paths` mode to a 4936-line driver, arms in two suites, a
verb-carrier render, a kit bump and three backlog rows — **and then verifying all of it through a
kit gate costing 10 to 45 minutes per invocation and a self-test suite it had watched run for over
an hour without finishing.** It judged that it could not complete that verification honestly inside
its remaining span, refused a reduced version outright, and handed the unit over with its spec
folded and READY. That was the right call and this brief does not second-guess it.

**Two things are different, and only one of them is time.**

The first is that the previous pass over-scoped what a build pass owes. **M6 is explicit: run the
diff-scoped gates for what the pass touched; the FULL BAR runs ONCE, at the push boundary.** A pass
that treats the whole kit gate and the whole self-test suite as its own per-invocation admission
price has invented a cost the method does not charge it. Section 7 of the spec already names the
legs that matter and — importantly — states that the two `*.test.sh` suites this unit adds arms to
are **on no bar at all**, so no gate is waiting on them either way. What is owed is the HAND-RUN of
those two suites with their exit codes reported, which section 7 names as the compensating check.

The second is that the unit's spec has been through two adversarial audit rounds and is at rev-6.
Every `unattended-build.js` address in it was re-derived at BASE `e828f778` by opening the file, and
S2 now names its deletions BY IDENTIFIER rather than by span — which matters, because at the old
spans the deletion set covered the AUDIT stage. You are starting from a correct design.

## What to do about the cost, stated as instructions rather than as sympathy

- **Do not run the full bar.** `bash tools/run-gates/run-gates.sh` is the push boundary's job. Run
  the legs section 7 names, individually, over what you touched.
- **The kit gate has a narrow form.** `bash tools/unattended/check-unattended.sh --only 26` runs the
  one check section 7 actually needs from it. Paying for the whole subject per arm is a gate that
  cannot fail, spent in wall clock.
- **Hand-run the two suites, and report the exit codes**, because nothing standing re-checks them:
  `bash tools/workflows/unattended-build.test.sh` and `bash tools/unattended/unattended.test.sh`.
  If one of them genuinely cannot finish, say so with what you observed rather than reporting a
  green you did not see. A skip that looks like a pass is indistinguishable from coverage.
- **If a leg or a suite exceeds what you can pay, that is a finding to record, not a reason to
  claim.** Write it into the acceptance ledger against the criterion it defeats.

## The bounds

- **The write set is declared before you touch anything**, with
  `--dispatch aHoistedPass --pass TOOL-aHoistedPass-6 --writes <path>`, one `--writes` per path.
  Widen it before the commit if you discover another file; narrowing after the fact is refused.
- **S13's three backlog rows mint ids under THIS session's slug.** Do not reuse another session's.
- **S11's verb carrier is REGENERATED**, never hand-edited:
  `bash tools/unattended/adopt-unattended.sh`, then `--check` to prove the byte-compare.
- **S12 takes the `review-harness` 1.6 to 1.7 bump.** The sibling `TOOL-aHoistedPass-5` declines it
  and its rev-4 says so explicitly, so this is the only unit that may move it.
- **The `unattended` kit version is NOT yours.** `DEPL-aHoistedPass-1` took 1.17 to 1.18 at order 2.
  Assert `bash tools/check-kit-versions.sh` exit 0 and move it no further.
- **Flip this unit's spec status header to `CLOSED` in the SAME COMMIT as the code**, and write the
  acceptance ledger the manifest requires of a closed Tier-2 unit — one line per numbered criterion,
  `**Serves:** journal`, under `memory/builds/aHoistedPass/build/`.
- **Run the bug-class checklist after the commit**, `python tools/memory-tree/gotchas.py --for-diff
  HEAD~1..HEAD`, and act on what it names before you stop. It takes a COMMITTED range, so it runs
  after the commit and never before it.
- Commit; do not merge and do not push. The landing is the parent run's act.

## One correction the spec carries that is easy to read past

Attended mode landed INSIDE the BUILD stage after this spec's original base, so S2's deletion set has
a keep/delete boundary rather than a clean cut: the attended `planState` refusal and `skippedDone`
grade which units may be dispatched, so they move AHEAD of the roster hand-out instead of leaving
with the deleted agent. And there is a FOURTH exit — attended mode's every-unit-terminal return —
that needs `roster: []` for the same reason the `CONVERGING` exit does. Section 4's boundary table is
the authority; do not reconstruct it from the header.
