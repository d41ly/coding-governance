# TOOL-aGraftedHelix-17 — check 27's engine arm asserts its branch run prints no check 28 line, observed once check 28 exists

**Status:** SPECCED · rev-1 · 2026-10-04 · node a · Tier-1 · base 5266d22e · streams tooling · order 7

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aGraftedHelix-14`'s engine arm reds the hygiene engine over a branch that adds a decision row
near a base row, and observes check 27 by a non-zero exit plus a `check 27:` line.
`TOOL-aGraftedHelix-6` adds check 28 at the same build step. Check 28 is always on and grades the
added set, so a branch row whose content key equals the base row's reds it too. Once unit 6 has
landed, that arm stays green with check 27's `status=1` deleted, because check 28 still sets the exit.
It is an arm that cannot fail, the shape unit 14 exists to close. Unit 14 is built at the step unit 6
shares, so whatever it asserts about check 28 cannot be seen to move during its own pass. This unit,
built after both, gives the arm an explicit assertion that the branch run prints no `check 28:`
line, and observes that assertion red with check 28 present. It closes finding 16 (HIGH) of the
round-1 spec audit of units 10 to 15.

## 2. Scope (IN)

- **S1** — Unit 14's engine arm in `tools/memory-tree/check-memory-hygiene.test.sh` asserts, on its
  branch run, that no output line opens `check 28:`, as a named assertion of its own beside unit
  14's only-offending-check assertion. It keeps the non-zero exit assertion, which is the only
  observation of check 27's `status=1`, and the `check 27:` line. Observed by AC1.
- **S2** — The arm's failure message names which half failed: a `check 28:` line present means the
  fixture's branch row is a content duplicate of its base row, and the exit belongs to check 28.
  Observed by AC1.
- **S3** — The memory-tree kit version moves once after this unit's last move if its shipped bytes
  moved, in every carrier `tools/check-kit-versions.sh` pairs. Observed by AC2.

## 3. Non-goals (OUT)

- **The fixture's wording.** Unit 14 pins its branch row as a paraphrase whose content key differs
  from the base row's and that still clears the near-match floor (its rev-2). This unit asserts the
  consequence and does not re-pin the row. Unit 14's assertion that 27 is the only offending check
  already reads a `check 28:` line once check 28 exists; what it cannot do in its own pass is be
  observed to move against check 28, which is this unit's AC1.
- **Unit 13's arm.** Check 28's own engine arm is unit 13's, and it asserts its own only-offending
  check there.
- **A shared helper across the suite's engine arms.** Two arms in this build need the assertion,
  and each states it in one line. A helper would be a third copy of the `_b1` precedent's shape for
  two callers.

### Edges

- **consumes-from** `TOOL-aGraftedHelix-14` — the check 27 engine arm, its copy-install fixture and
  the paraphrased branch row its rev-2 pins; without them there is no arm to strengthen.
- **consumes-from** `TOOL-aGraftedHelix-6` — check 28 in the hygiene engine, its `CONTENT_CHECK`
  key and its `check 28:` line; without it the absence S1 asserts is vacuous, because nothing could
  print the line.

## 4. Design

### Evidence

- Unit 6's AC10 calls a same-text third row "a third row restating them" and expects check 28 to
  red it. Check 28 grades keys held by a record added since the mainline merge-base, and it has no
  arming key.
- Unit 14's §4 fixture adds a row restating a base row under a new id. Read as this build reads
  "restating", that is a content duplicate.
- On the fixture's `main` the added set is empty, so check 28 cannot fire there. Unit 14's AC2 clean
  run therefore separates nothing about check 28.

### The staged break

The break is made in the scratch fixture, never in a tracked file: the branch row is replaced by a
verbatim copy of the base row's text. The branch run then prints a `check 28:` line, and the arm reds
naming it. With the row restored, the arm is green. That observes the assertion can move, which a
break deleting check 27's `status=1` alone could not, once check 28 holds the exit.

### Files touched (estimate)

- `tools/memory-tree/check-memory-hygiene.test.sh`

## 5. Production-readiness checklist

- security — N/A: a test arm.
- perf / scale — No new engine run. The assertion reads the branch run unit 14's arm already makes.
- error / empty / loading states — N/A.
- observability — S2's message names the check that took the exit.
- risks — A future check that also fires on the fixture would take the exit too. The arm names only
  check 28, because that is the check this build adds beside check 27.
- testing — S1's assertion, observed RED with the branch row made verbatim.
- migration — None.
- user docs — N/A.

## 6. Acceptance criteria

The fixture is unit 14's copy-install fixture, built after unit 6 has landed, so the engine copied
into it carries check 28.

- **AC1** — When the fixture's copy of the hygiene engine runs at the root of its branch, it exits
  non-zero, prints a `check 27:` line, and prints no line opening `check 28:`. With the branch row
  replaced by a verbatim copy of the base row in the fixture, the same run prints a `check 28:` line;
  that red is observed once, then the row is restored.
  Red when: the branch row is a content duplicate, so the exit is check 28's and check 27's
  `status=1` is unobserved.
- **AC2** — When `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` runs at the
  pass's commit, it names no memory-tree carrier left behind.
  Red when: the kit's shipped bytes moved without its version.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · the check 27 engine arm asserts no check 28 line on its branch run; stage the branch row as a verbatim copy of the base row · the suite's floor rises by its new arm count

The close runs the legs and the suite; a pass runs the fixture's engine as its check.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, promoted from finding 16 of the round-1 spec audit of units 10
  to 15.

## 10. Reuse audit

The seam is unit 14's own arm and fixture, and the `_b1` precedent in
`tools/memory-tree/check-memory-hygiene.test.sh`, which asserts an otherwise-clean tree before it
reads one check's output. No existing seam fits beyond them: no arm in the hygiene suite asserts the
absence of a sibling check's line. The recall probe returned `TOOL-cSpliceWarden-6` and
`TOOL-aCollapsedScan-10`, as for units 13 and 14.

Recall terms used: hygiene engine dispatch delegated row_grammar check-rotation status offender green-run summary arm staged break
