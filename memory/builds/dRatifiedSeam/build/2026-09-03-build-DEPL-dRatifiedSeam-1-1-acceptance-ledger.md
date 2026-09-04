# Acceptance ledger — DEPL-dRatifiedSeam-1

**Serves:** journal DEPL-dRatifiedSeam-1

Tier-2 · node d · 2026-09-03

## The headline: S3 shipped green and did nothing, and only writing the arm found it

The suite was green at 1065 arms with the unclaimed-source landing reached by NOTHING. Every
destination the `[-11]` fixture offered was one the walk had already decided about, so the block
skipped them all and reported zero. **Zero landings and a broken landing produce the identical
green.** Writing AC4's arm is what exposed the cause: I passed `target` as `resolve_entry`'s first
argument, and that parameter is GOV's root — its rule walk reads gov's tree to expand the globs. So
it expanded the ADOPTER's files against gov's descriptor, declared nothing new, and found zero on
every run. `_cmd_apply` spells it `resolve_entry(root, ...)` at its own call site; that is the line
I should have copied.

Had I trusted the green and written this ledger one step earlier, S3 would have landed as a feature
that does nothing, in the build whose subject is checks that cannot fail.

## Acceptance criteria

**Evidences:** DEPL-dRatifiedSeam-1

- AC1 — MET — `python tools/govkit/selftest.py` exits 0 with the `[-RS1]` arms landing a tracked
  file, and the standing predicate no longer fails on the rise. Its antecedent is a real arm now:
  rev-3 corrected this criterion precisely because no fixture ADDED a file, so the relaxed
  direction was never taken.
- AC2 — MET, OBSERVED BY MUTATION — mutating `count_never_falls` to `return True` reds
  `[-11] S4 count_never_falls(5, 4) is False` and `(5, 0) is False` by name; restoring goes green.
  The removal direction is bound by a subject that can actually break.
- AC3 — MET — `grep -nE "tracked-file count|_files_before|_files_after|count_never_falls"` over
  `tools/govkit/selftest.py` reports the comment, the two snapshots, the check and the extracted
  call. Every comparison now routes through `count_never_falls`; there is no second operator to
  audit, because there is no second comparison.
- AC4 — MET, OBSERVED — `python tools/govkit/selftest.py` runs six `[-RS1] AC4` arms: the run
  exits 0 and prints `unclaimed sources: 1 landed`, the file is in the worktree, it is TRACKED,
  the receipt carries a row, that row carries `commit`/`gov_oid`/`source`/`sha256`, and a liveness
  arm asserts the count really rose by one.
- AC5 — MET, OBSERVED — three `[-RS1] AC5` arms: a destination the target already holds is
  REFUSED by name, the adopter's bytes are byte-identical afterwards, and no receipt row is minted.
- AC6 — MET — `python tools/govkit/selftest.py` exits 0 with ZERO arms failing, at 1074 arms. The
  nineteen-arm cascade the spec anticipated never materialised as fixture updates: it materialised
  as four defects in my own code, listed below.
- AC7 — MET — `python tools/govkit/selftest.py` and `python tools/govkit/govkit.py selfcheck` both
  exit 0.
- AC8 — pending — `bash tools/run-gates/run-gates.sh` has not run since this unit's last edit; 
  recorded here when the closing bar does, with the legs it ran.

## S5's disposition: the cascade was four defects, not nineteen fixtures

The spec asked for each cascade arm to be dispositioned rather than counted. The answer is that
none of them was a fixture needing an update. Each was S3 being wrong:

1. **It landed destinations the walk had just REFUSED.** `twin-a.txt` and `twin-b.txt` are the two
   ends of a rename declined as ambiguous — *one row cannot move to several, and picking one would
   be a guess*. Landing both manufactures exactly the ambiguity that refusal preserves. A
   destination the walk decided about is not unclaimed; it is decided. Now excluded via the walk's
   own `rename_dests` map and its withdrawn rows.
2. **The receipt row carried five fields where a real row carries nine.** Without `commit` and
   `gov_oid` a row cannot be attributed to a gov vintage, so the NEXT run failed
   `DEPL-dCarriedReceipt-7`'s integrity preamble. Row shape taken from `_cmd_apply`'s producer.
3. **`staged.append()` named a variable that does not exist in `_cmd_update`.** That function
   stages through `checkout-index`/`update-index`, not a list. It raised `NameError` on the WRITE
   path only, so every read-only run passed and only the fixture's second write run caught it.
4. **The `resolve_entry(target, …)` argument**, above.

Four defects, four different shapes, and every one caught by running something rather than reading
it. Three were invisible to a read-only run.

## What S4 nearly was

My first cut of the removal-direction arm compared `len(_fell) >= len(_files_before)` in the TEST.
One fewer than a number is never at least that number, so it passed whatever the engine did — a
tautology over a copy of the predicate, which is the re-implements-the-gate-instead-of-invoking-it
defect the closing review of `dRetiredFork` found in that build's BAN arms. Repeated one build
later, inside the unit whose job is to stop a relaxed predicate grading nothing.

Fixed the way that one was: `count_never_falls` is a pure function in `govkit.py`, the suite CALLS
it, and a six-row truth table grades it. That is now the second time this shape has been the right
answer, which is worth more than either instance.

## The cold pass is still owed

`dRatifiedSeam`'s M4 audit was SELF-review — five cold reviewers died on server 529s across two
workflow fans and three direct agents. Eight findings were folded into the specs, four of them
acceptance criteria that could not fail. This unit's own build then found four more defects that no
spec audit would have caught, because they only exist in code. Neither fact substitutes for the
other, and the cold pass on the specs remains unpaid.
