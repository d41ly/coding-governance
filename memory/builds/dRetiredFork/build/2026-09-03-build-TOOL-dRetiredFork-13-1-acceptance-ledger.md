# Acceptance ledger — TOOL-dRetiredFork-13

**Serves:** journal TOOL-dRetiredFork-13

Tier-1 · node d · 2026-09-03

The `KIT_REL` idiom, already proven in two sibling suites, applied across the shipped test and
selftest surface. Every touched file carries its own equivalence proof.

## Acceptance criteria

**Evidences:** TOOL-dRetiredFork-13

- AC0 — MET — re-derived from `tools/install-prefix-carried.txt`: **33 test/selftest rows summing to
  259**, out of 112 rows and 652 occurrences. The spec's own AC0 said the ratchet holds 33 and rev-1
  said 32; the ratchet says 33, so rev-1 was wrong. `.githooks/pre-push.test.sh` (2) belongs to THIS
  unit — `TOOL-dRetiredFork-11` added an arm to that file but swept no literals from it, and moved
  only `.githooks/pre-push`'s own row
- AC0b — MET — the per-file residue is listed below rather than a total, so a partial sweep could
  not have passed by moving one large row. `check-playbook.test.sh` went 37 to 3 and
  `run-gates.test.sh` 33 to 2
- AC1 — MET, mechanically and for every file — the sweep refuses to write a file whose expansion
  does not reproduce its pre-change bytes. Not a sample: `EQUIVALENCE FAILED` reverts that file and
  it never lands. Two files were refused by that check during the pass and are named below
- AC2 — MET at `scripts/<kit>`, SHORT BY ONE at the repo root, and both halves are reported. Three
  suites ran green at `scripts/<kit>` with assertion counts EQUAL to their default-prefix run:
  `scratch-guard.test.sh` 70, `tier2-review.test.sh` 20, `unattended-build.test.sh` 21. At a
  repo-root prefix only TWO were equal — `scratch-guard.test.sh` 70 and `tier2-review.test.sh` 20;
  `unattended-build.test.sh` reported 20 arms against 21, so it is not counted
- AC3 — MET — the unexercised set is named below with a reason each
- AC4 — MET — `bash tools/check-install-prefix.sh` exits 0 with the total at **470**, down from 652
  and far below the spec-era 656. The test surface fell **259 to 83** and seven rows vanished
  entirely. Re-baselined in this commit
- AC5 — MET — `bash tools/check-testsuite-counts.sh` exits 0, every touched suite still printing its
  executed count

## AC3 — what was NOT run, and why

**The unattended kit's own self-tests, all of them.** `check-playbook.test.sh` (34 sites),
`check-pass-order.test.sh` (13), `unattended.test.sh`, `cross-component.test.sh`. A standing owner
instruction says this node does not run that kit's self-tests. They are covered by AC1's
byte-equivalence proof, which establishes regression and says nothing about the new capability —
exactly the gap this criterion exists to stop being silent about.

**Both Python selftests were not swept at all.** `lexicon/selftest.py` keeps 15 and
`codebase-map/selftest.py` 5, together 20 of the 83 remaining. `lexicon` needs an `import os` added
before the idiom fits, and five of its literals are **fixture data for the glob matcher** — rows
whose exact spelling is the thing under test, where rewriting the path would leave the suite green
while testing nothing. `codebase-map` was refused by AC1's own equivalence check, twice, and the
second refusal was a defect in my checker rather than in the edit. Filed as `TOOL-dRetiredFork-26`
rather than forced.

**Three suites do not pass at a foreign prefix even after sweeping**:
`memory-tree/check-method-carriers.test.sh`, `codebase-map/adopt-codebase-map.test.sh` and
`workflows/check-review-join.test.sh`. They carry residual resolution beyond the literals this unit
retired. Named here so a green default-prefix row is never read as foreign-prefix coverage.

## The defect the first cut shipped, and what caught it

The sweep initially rewrote literals **inside single-quoted shell strings**, where `$KIT_REL` does
not expand. `check-review-join.test.sh` broke on `H='tools/workflows/tier2-review.js'` becoming a
string containing the characters `$KIT_REL`, and an arm failed for a reason having nothing to do
with what it tests.

AC1's equivalence proof did **not** catch it, and that is worth recording: expanding `$KIT_REL` back
to its default reproduces the original bytes whether or not the shell would have expanded it. The
proof is textual, so it is blind to quoting. What caught it was RUNNING the suite — which is the
whole reason AC2 and AC3 exist beside AC1 rather than after it.

The sweep now tracks single-quoted spans and skips them: 214 candidate sites became 196, and the 18
difference is exactly the set that would have been silently broken.

## Per-file residue, after the sweep

Comments and usage headers keep their literal deliberately — `bash tools/<kit>/x.sh` in a header is
what a human types, and the proven idiom left those alone. A cross-kit reference inside an assertion
string is also left, because `KIT_REL` does not point at that kit.

```
lexicon/selftest.py 15 · merge-rows.test.sh 7 · codebase-map/selftest.py 5
kit-dogfood-parity.test.sh 5 · check-memory-hygiene.test.sh 4 · run-gates.gov.test.sh 4
check-install-prefix.test.sh 3 · adopt-codebase-map.test.sh 3 · agent-cap.test.sh 3
pytest-parallel-guardrails.test.sh 3 · check-playbook.test.sh 3 · check-unattended.test.sh 3
unattended.test.sh 3 · check-protocol-parity.test.sh 3 · check-review-join.test.sh 3
check-wiring.test.sh 2 · scratch-guard.test.sh 2 · hygiene-parity.test.sh 2
run-gates.test.sh 2 · adopt-unattended.test.sh 2 · and six files at 1
```

## One latent failure found, not caused

`check-memory-hygiene.test.sh` fails two arms on a freshly scaffolded tree — check 9 and check 2.
Measured **before** this unit touched the file, so it is pre-existing. It surfaced only because
touching `tools/memory-tree/` arms that leg's guard; it is `chunk = selftests` and therefore held
off the ordinary bar. Filed as `TOOL-dRetiredFork-25` rather than absorbed.

## A control that was green when verified and red when committed

`.githooks/pre-push.test.sh` failed here on an arm **this build wrote two units ago**. Unit 11's
red-first control read `HEAD:.githooks/pre-push` to obtain "the pre-change hook". That worked while
the fix was uncommitted and stopped working the instant it landed: HEAD then held the FIXED hook, so
the control reported that the pre-change hook "already forced — this arm proves nothing".

It was verified green before the commit and was red immediately after, which is the worst possible
timing for a control nobody re-runs. Nothing caught it for two units, because that suite's guard
only arms when its own paths move — and this sweep is what moved them.

Pinned to `05455c45`, the last commit that touched the hook before unit 11. **A control anchored on
a moving ref is a control with an expiry date**, and the expiry is the moment the thing it guards
gets fixed.
