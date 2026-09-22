**Serves:** journal TOOL-dFramedEntrypoint-1

# Closing review: three rounds, and the one mistake I kept making

*Node d, 2026-08-25. Blocker trend 3 -> 1 -> 0, so the loop CONVERGED. This record carries the fold
and the correction the round-3 review asked for.*

## Rounds

| Round | Base | Raw | Confirmed | Precision | Distinct defects | Verdict |
|---|---|---|---|---|---|---|
| 1 | 470bb09b | 25 | 24 | 0.96 | 3 BLOCKER, 6 HIGH, 10 MEDIUM, 5 LOW | BLOCKED |
| 2 | beb5fce4 | 14 | 12 | 0.86 | 1 BLOCKER, 1 HIGH, 3 MEDIUM | BLOCKED |
| 3 | 747ab929 | 5 | 3 | 0.60 | 0 BLOCKER, 1 HIGH, 2 MEDIUM | BLOCKED |

## The through-line, stated plainly

Every round found the same class in a different place: **a check that could not fail.** Round 1 found
a ceiling file whose five values had been blanked in a landed commit while the bar printed
`slot contract clean`, because a blank ceiling is the legal unarmed state. Round 2 found that the
guard I wrote to fix that never matched, and that the arm I wrote to cover the other fix was a closed
boolean over four literals. Round 3 found that my replacement for THAT arm still did not call
`do_bump` — it restated the filter inline, and the copy had already drifted.

**The root cause was structural, and round 3 is where I found it.** Every reader of the two slot
declaration files resolved them from `__file__`, so nothing could point them at a fixture. An arm that
called `do_bump` would have rewritten this repository's own high-water file. So each attempt at
coverage copied the subject instead of running it — three times, each time looking like a fix. The
repair is one seam, `slot_data_dir()`, overridable only by the selftest. With it, the arm calls the
real verb twice and asserts the row count is stable; with D4 reinstated it reports `expected 5, got 10`.

That is the lesson worth keeping from this build: **when an arm keeps coming out as a restatement, the
subject is untestable and that is the defect.** Writing a better restatement is not the fix.

## What round 3 raised, and its disposition

- HIGH, the `do_bump` arms that never called it — FIXED, with the seam above, and both breaks
  reinstated and observed.
- MEDIUM, M3's canon scoping shipping with no arm — FIXED. Two arms now reach that guard; deleting
  `h in canon_heads and` fails both.
- MEDIUM, round 2's M2 absent from every catalog — CORRECTED HERE, which is the only place it can be:
  the round-1 record is a ratified review record and is not rewritten. Its still-open fixes cite
  `assert_contract_registry`, `_canon_violations`, `budget_findings` and a bare `slot_sizes`, none of
  which exist at HEAD — they were renamed onto declared verbs at 2b6b2e62 (`check_contract_registry`,
  `scan_canon`, `scan_slot_budget`, `measure_slot_sizes`). A later pass routing on those names finds
  nothing. The same record's line 23 says the rename was uncommitted; it landed in that same commit.

## Two range corrections from the round-3 report

The BASE passed to round 3 was a 40-character sha that does not resolve; the unambiguous prefix
`747ab929` resolves to `747ab9293b611624ec0b47db11c5b280afc40053`, which is what the report measured
against. And that BASE is the fix commit itself, so the round-3 window held one commit and did not
contain the code its HIGH and first MEDIUM are about — both were raised against the cumulative
landing set, which is the review's stated subject. A round-4 base of `54bb6276` would put the fixes
back inside the window.

## Still standing, unfolded

Round 1's 2 remaining HIGH, 10 MEDIUM and 5 LOW, and round 2's 2 remaining MEDIUM, are enumerated
with `file:line` in their own records. They are not fixed and this record does not claim otherwise.
