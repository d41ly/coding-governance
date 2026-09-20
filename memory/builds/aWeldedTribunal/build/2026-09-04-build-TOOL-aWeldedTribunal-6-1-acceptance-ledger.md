# TOOL-aWeldedTribunal-6 — acceptance ledger

**Serves:** journal TOOL-aWeldedTribunal-6

## What changed

One pass in `_cmd_update`, after every refusal the verb already makes and before its three summary
exits. It computes the gap set with `coverage_rows`, grades it through `decline_findings` against a
THROWAWAY `Report`, prints undeclined gaps and declined rows separately, and closes with a coverage
line that prints at zero.

## Each criterion, answered

- **AC1 / AC2** — an undeclined gap prints its own `GAP` line naming kit, destination and source, and
  the coverage line then says the install is INCOMPLETE. Exercised through the govkit self-test's
  fixtures, which drive `update` end to end.
- **AC3** — `gap 0` prints. The coverage line is unconditional, inheriting `plan --coverage`'s own
  stated rule that a clean run printing nothing is indistinguishable from a join that did not run.
- **AC4** — `--kits` narrows `_gap_selection` before the join, so a gap in an unnamed kit is not
  reported.
- **AC6** — a declined gap prints as a `declined` row and does NOT count toward INCOMPLETE. This is
  the presence half of S2, and without it the cheapest build filters declined rows out entirely and
  commits the exclusion-list failure `DEPL-dCarriedReceipt-5` exists to prevent.
- **AC7** — `python tools/govkit/selftest.py`: **all arms held**, exit 0.

## The measured correction, and it is the reason this ledger is worth reading

Rev-3 specified the pass "after `--kits` scoping and before the classification loop". The self-test
refuted it: `coverage_rows` reaches `planned_writes`, which RAISES on the `-11` escape fixture's
out-of-tree prefix, so that fixture's GRADED refusal became a hard abort and its arm went from pass
to FAIL — `[-11] a rename destination OUTSIDE the target repository is refused by name`.

**Confirmed as mine, not pre-existing**, by running the same suite against the stashed-clean tree,
where all arms held. That check is the difference between fixing a defect and inheriting one.

`index_read`'s own header in this same file already documents that class: an out-of-tree path is an
ANSWER, not a probe failure, and raising on it changes the verb's exit code. The file warned about it
and the first cut walked in anyway. The pass now runs last and is wrapped so it cannot raise; on any
exception it prints `coverage: UNAVAILABLE` with the exception type, which is a different fact from
zero gaps and says so.

## What this does NOT do, stated plainly

It does not LAND the bytes. `TOOL-aFlaggedScaffold-3` therefore stays OPEN and keeps tracking the
landing verb, and `TOOL-aWeldedTribunal-8` closes `TOOL-aScouredKit-25` as a duplicate of that row
rather than against this unit. An operator who reads `1 undeclined gap` and does nothing is in the
same state as before; what changed is that the state is legible when the verb runs instead of at the
next ImportError.

## Evidence

**Evidences:** TOOL-aWeldedTribunal-6
- AC1 — `python tools/govkit/selftest.py` — the gap pass prints a `GAP` line naming kit, destination and source
- AC2 — `tools/govkit/govkit.py` — an undeclined gap makes the coverage line say INCOMPLETE
- AC3 — `tools/govkit/govkit.py` — the coverage line is unconditional, so a zero-gap run prints its zero
- AC4 — `tools/govkit/govkit.py` — `--kits` narrows the gap selection before the join
- AC5 — `python tools/govkit/selftest.py` — all arms held, including the escape fixture whose graded refusal an earlier placement turned into a hard abort
- AC6 — `tools/govkit/govkit.py` — a declined row prints as `declined` and is excluded from the INCOMPLETE count
- AC6b — `tools/govkit/govkit.py` — the declined row PRINTS rather than vanishing, which is the exclusion-list shape the decline contract exists to prevent
- AC6c — amended rev-4 — the fork resolved the Report question to a THROWAWAY so decline hygiene cannot fail this verb; the closing review found the same hazard on the coverage call and it was hoisted, logged in section 9
- AC7 — `python tools/govkit/selftest.py` — all arms held, exit 0
