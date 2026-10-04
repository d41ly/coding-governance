# TOOL-aGraftedHelix-17 — check 27's engine arm asserts its branch run prints no check 28 line, observed once check 28 exists

**Status:** SPECCED · rev-3 · 2026-10-04 · node a · Tier-1 · base 5266d22e · streams tooling · order 7

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-review-TOOL-aGraftedHelix-16-spec-audit-round1.md](../reviews/2026-10-04-review-TOOL-aGraftedHelix-16-spec-audit-round1.md) | spec-audit | TOOL-aGraftedHelix-16 TOOL-aGraftedHelix-18 TOOL-aGraftedHelix-19 |

<!-- /gen:spec-records -->

## 1. Goal

`TOOL-aGraftedHelix-14`'s engine arm reds the hygiene engine over a branch that adds a decision row
near a base row, and observes check 27 by a non-zero exit plus a `check 27:` line.
`TOOL-aGraftedHelix-6` adds check 28 at the same build step. Check 28 is always on and grades the
added set, so a branch row whose content key equals the base row's would red it too. Unit 14 rev-2
pins its branch row as a paraphrase whose content key differs, so check 28 does not fire on the
fixture as written, and unit 14's AC1 already asserts that no other line opens `check <n>:`, which
reds on a `check 28:` line once check 28 exists. What unit 14's pass cannot do is be OBSERVED to red
against check 28, because it is built at the step unit 6 shares. This unit, built after both,
observes that red with check 28 present, and gives the arm a diagnosis of its own: a named assertion
whose failure text says the exit is check 28's because the branch row is a content duplicate. That
text is what it adds over unit 14's only-offending-check assertion, which reds on the same run with a
message about the offending check and not about the fixture. It closes finding 16 (HIGH) of the
round-1 spec audit of units 10 to 15.

## 2. Scope (IN)

- **S1** — Unit 14's engine arm in `tools/memory-tree/check-memory-hygiene.test.sh` asserts, on its
  branch run, that no output line opens `check 28:`, as a named assertion of its own beside unit
  14's only-offending-check assertion and with its own FAIL text. It keeps the non-zero exit
  assertion, which is the only observation of check 27's `status=1`, and the `check 27:` line.
  Observed by AC1.
- **S2** — S1's failure text names which half failed: a `check 28:` line present means the
  fixture's branch row is a content duplicate of its base row, and the exit belongs to check 28.
  Observed by AC1, which runs the arm and reads that text.
- **S3** — The memory-tree kit version moves once after this unit's last move if its shipped bytes
  moved, in every carrier `tools/check-kit-versions.sh` pairs. Observed by AC2.

## 3. Non-goals (OUT)

- **The fixture's wording.** Unit 14 pins its branch row as a paraphrase whose content key differs
  from the base row's and that still clears the near-match floor (its rev-2). This unit asserts the
  consequence and does not re-pin the row. Unit 14's assertion that 27 is the only offending check
  already reds on a `check 28:` line once check 28 exists; what it cannot do in its own pass is be
  observed to move against check 28, which is this unit's AC1, together with S1's own text.
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
- Unit 14 rev-2 §4 pins its branch row as "a paraphrase, never a verbatim restatement", so its
  content key differs from the base row's and check 28 is silent on the fixture as written.
- On the fixture's `main` the added set is empty, so check 28 cannot fire there. Unit 14's AC2 clean
  run therefore separates nothing about check 28.
- `tools/memory-tree/row_grammar.py:53` sets `CHECK = 20`, and `:677-681` reds an id appearing twice
  within one row document. Unit 6 grades only keys held by two or more distinct identities, so a row
  copied whole, id included, prints a `check 20:` line and no `check 28:` line.

### The staged break

The break is made in the scratch fixture, never in a tracked file: the branch row KEEPS its own new
id, and only its body becomes the base row's body, verbatim. The branch run then prints a `check 28:`
line and no `check 20:` line, and the arm reds with S1's own failure text beside unit 14's. A second
break, made in a scratch copy of the arm, deletes S1's assertion: the same verbatim run still reds,
through unit 14's assertion, and S1's text is absent from the output. That observes S1 can move on
its own, which a break that only makes the row verbatim cannot tell from unit 14's red. With the row
and the assertion restored, the arm is green.

### Files touched (estimate)

- `tools/memory-tree/check-memory-hygiene.test.sh`

## 5. Production-readiness checklist

- security — N/A: a test arm.
- perf / scale — No new engine run. The assertion reads the branch run unit 14's arm already makes.
- error / empty / loading states — N/A.
- observability — S2's message names the check that took the exit.
- risks — A future check that also fires on the fixture would take the exit too. The arm names only
  check 28, because that is the check this build adds beside check 27.
- testing — S1's assertion, observed RED with the branch row's body made verbatim, and observed to
  vanish with S1 deleted while unit 14's assertion still reds.
- migration — None.
- user docs — N/A.

## 6. Acceptance criteria

The fixture is unit 14's copy-install fixture, built after unit 6 has landed, so the engine copied
into it carries check 28. AC1 runs a SLICE of the hygiene suite, its prologue plus the check 27
engine arm, written as a scratch script under the session scratchpad with the prologue's kit
directory pointed at `tools/memory-tree`; it runs one arm, not the suite.

- **AC1** — When the slice runs over the fixture as written, it passes, and the branch run prints a
  `check 27:` line and no line opening `check 28:`. With the branch row's body replaced by the base
  row's body verbatim in the fixture, its own id kept, the slice reds, its output carries S1's own
  FAIL text naming check 28 and the duplicate row, and the branch run prints a `check 28:` line and no
  `check 20:` line. With S1's assertion deleted from a scratch copy of the slice, the same verbatim
  run still reds and S1's text is absent from the output. Both reds are observed once, then the row
  and the assertion are restored.
  Red when: S1's text never appears, so its assertion cannot red alone, or the red carries a
  `check 20:` line and belongs to the copied id rather than to check 28.
- **AC2** — When `python tools/govkit/govkit.py epoch --base <the pass's parent sha>` runs at the
  pass's commit, it names no memory-tree carrier left behind.
  Red when: the kit's shipped bytes moved without its version.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `kit version markers` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · the check 27 engine arm asserts no check 28 line on its branch run, with its own FAIL text; stage the branch row's body as the base row's body verbatim, its id kept, and assert no check 20 line · the suite's floor rises by its new arm count

The close runs the legs and the suite; a pass runs AC1's slice as its check.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, promoted from finding 16 of the round-1 spec audit of units 10
  to 15.
- rev-2 · 2026-10-04 · S2 · relabelled NOT OBSERVED: the bug-class checklist over the promoting
  commit selected `observed-by-claim-no-arm-discharges`, and AC1 runs the engine, never the arm
  whose message S2 states.
- rev-3 · 2026-10-04 · §1 §3 §4 §5 §6 §7 · S1 S2 · AC1 · folded the round-1 spec audit of units 16
  to 19 on this unit. Finding 10: §1 and §4 restate the premise against unit 14 rev-2, whose
  paraphrased row check 28 does not fire on and whose AC1 already reds on a `check 28:` line; S1's
  addition is its own failure text. Finding 1: AC1 runs a slice holding the arm, so it observes S1
  and S2, and a staged deletion of S1 shows its text vanish while unit 14's assertion still reds.
  Finding 19: the verbatim break keeps the branch row's own id, and AC1 asserts no `check 20:` line.

## 10. Reuse audit

The seam is unit 14's own arm and fixture, and the `_b1` precedent in
`tools/memory-tree/check-memory-hygiene.test.sh`, which asserts an otherwise-clean tree before it
reads one check's output. No existing seam fits beyond them: no arm in the hygiene suite asserts the
absence of a sibling check's line. The recall probe returned `TOOL-cSpliceWarden-6` and
`TOOL-aCollapsedScan-10`, as for units 13 and 14.

Recall terms used: hygiene engine dispatch delegated row_grammar check-rotation status offender green-run summary arm staged break
