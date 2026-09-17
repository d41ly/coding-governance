# cMendedVintage — the acceptance ledger for unit 20

**Serves:** journal DEPL-cMendedVintage-20

*Node `c`, 2026-09-17, written by the pass that built the unit. Every line below was taken by driving
the committed arm directly, from a small runner under this run's scratch root that loads
`tools/govkit/selftest.py` and calls the arm with a path. No merge bar and no `*.test.sh` suite ran
in this pass.*

## The one thing worth reading twice

**The defect and its fix were observed side by side, on the same bytes.** Case C below is a copy of
this tip's engine with one `ALLOW_UNGRADED = False` line added. The new arm reds on it and names the
line. The shipped criterion's own pattern, `grep -c 'allow_ungraded'`, run over that same copy,
returns **0** — it would have reported the re-introduction clean. That is the whole argument for this
unit, reproduced rather than asserted.

**The break never touched the worktree.** `tools/govkit/govkit.py` is not in this unit's write set,
`DEPL-cMendedVintage-19` landed in it minutes before this pass, and the closing review follows
immediately. Every red below was staged on a copy under the scratch root, which is why the arm takes
its target as a parameter — recorded as a rev-2 amendment to S1 and AC1.

**Green on arrival, and that is the sequencing rather than a pass.** `DEPL-cMendedVintage-4` drained
the flag at `81ce02a4`, so both figures measure 0 on this tree before this unit wrote a line. An arm
nobody has seen fail is an assertion about nothing, which is what cases B, C, E and F are for.

**Evidences:** DEPL-cMendedVintage-20

- AC1 — `check_retired_flags` driven directly, twice. POSITIVE, against its own default derived path
  on this tree: the arm prints the derived pattern `/allow[_-]ungraded/i` beside
  `0 matching line(s) of 9946`, and every row is `ok`. RED, against a scratch copy of that file with
  `ALLOW_UNGRADED = False` inserted above `def main(`: `1 matching line(s) of 9949` and the failure
  detail reads `9894:ALLOW_UNGRADED = False`, so the red names the surviving line and not only the
  flag. Re-measured rather than quoted: `grep -c 'allow_ungraded'` and
  `grep -cE 'allow[_-]ungraded|ALLOW_UNGRADED'` both return 0 over the tracked file on this tree.
  CONTROL, because a red against a copy proves nothing if the copy is what reds: a second copy of the
  same file carrying an unrelated `UNRELATED_SENTINEL = 1` in the same position stays GREEN at 0
  matching lines. AMENDED at rev-2, section 9 line 1: the re-introduction is staged on a COPY and
  never on the tracked module, and the arm's target became a parameter defaulting to the derived path
  for that reason. The parameter is also what gives the checker a negative case at all — one that can
  only ever read a single hard-coded file cannot be tested.
- AC2 — `check_retired_flags` against `859daa67:tools/govkit/govkit.py`, extracted with `git show`
  into the scratch root. RED, reporting `14 matching line(s) of 9005`, and the failure detail names
  the first six sites — the two parameter defaults, the `if ungraded and not allow_ungraded:` guard,
  the remedy sentence, the usage line and the `over` clause. The narrow criterion's pattern over that
  same blob returns 8, so the six lines it cannot see are the gap this arm closes, measured and not
  inherited from the spec. AMENDED at rev-2, section 9 line 2: the figure's UNIT was wrong. Rev-1
  wrote "14 occurrences" where both numbers came from `grep -c`, which counts lines; measured here,
  the widened pattern has 15 occurrences on those 14 lines, because `allow_ungraded=ALLOW_UNGRADED`
  carries the name twice. The arm counts lines, the unit the criterion it grades was measured in, and
  the section 4 table now states its unit in the header.
- AC3 — `RETIRED_FLAGS` read back from the committed source: one row,
  `("allow-ungraded", "2026-09-16", "DEPL-cMendedVintage-4")`. The arm grades the provenance rather
  than trusting it: the date must match `\d{4}-\d{2}-\d{2}` and the unit id `[A-Z]+-[A-Za-z]+-\d+`.
  Case F drove a deliberately bad row, `("ghost-flag", "yesterday", "somebody")`, which reds naming
  both values, so a bare-name row cannot reach a green.
- AC4 — `check_retired_flags` docstring, read back from the committed source by the runner and
  printed whole. It names the single module it is handed and says a flag re-introduced in this
  harness, in a rendered document or in a sibling tool is invisible to it; it says it grades SPELLING
  and never BEHAVIOUR, and that the argv-refusal arm owns the behavioural half; and it says a green
  row means only that no operator can read the name in that module's text. It is written as what the
  arm does NOT reach, not as a description of what it catches.

## Two more arms, observed and answering no numbered criterion

Both come from the section 5 readiness rows rather than section 6, and both were driven in the same
runner.

- The DEAD PROBE branch. With the declaration monkeypatched to `()`, the arm reds on its own liveness
  row rather than reporting a clean pass over nothing. Without it an empty list would print no
  failures and read exactly like a drained tree.
- The unspellable-name branch. A row named `allow ungraded!` reds naming the row, and the arm then
  makes NO absence assertion for it — a green there would be a skip wearing coverage's clothes. This
  one moved during the build: the first cut refused the name and still printed an `ok` absence row
  for it, which is the same could-not-fail shape one level in, so the loop now continues past a
  refused row.

## What did not run, and why — the OWED half

The arm is wired into `main()` and nothing in this pass ran `main()`. `govkit selftest`,
`govkit selfcheck` and the acceptance matrix — the three gates section 7 names — are all suite or bar
shaped and are banned in this pass by its own mandate. What that leaves unobserved is precisely the
WIRING: that `check_retired_flags()` is reached when the suite runs, in the order and the process the
suite runs it in. Every assertion the arm makes was observed here by calling it directly, and the bar
the run owes covers the wiring once every unit is terminal.

`tools/codebase-map/test_codebase_map.py` is a gate leg and did not run either; the generated symbol
inventory was regenerated in this commit so the two new keys are claimed, and the leg is owed with
the rest of the bar.
