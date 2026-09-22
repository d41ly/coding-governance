# Acceptance ledger — DEPL-dCarriedReceipt-11, rename detection and `withdrawn`

**Serves:** journal DEPL-dCarriedReceipt-11

**Evidences:** DEPL-dCarriedReceipt-11
- AC1 — `python tools/govkit/govkit.py update --write` — the most destructive RED in this build, and
  it was observed against the engine with `-1`..`-10` landed and this unit not. The run exited **0**,
  unlinked EIGHT tracked files, `git rm`-ed them, dropped all eight rows from `install.json` and
  landed nothing at any new path: 18 tracked files before, 10 after. SEVEN of the eight were rows
  whose gov source gov had merely RENAMED and still ships. GREEN: 18 to 18, four rows moved, five
  reported.
- AC2 — `tools/govkit/selftest.py` — GREEN: prints `renamed`, `git status --porcelain` shows the
  `R` pair, and the row's `path` AND `source` both carry the new spelling.
- AC3 — `tools/govkit/selftest.py` — the fixture is AUTHORED to sit between the two thresholds, and
  an arm proves git pairs it at 10% and not at 50%, so `RENAME_SIMILARITY_PERCENT` is what decides
  rather than the fixture being trivially one side or the other.
- AC4 — `tools/govkit/selftest.py` — RED with `--write-withdrawals` removed: the run exits 2 on an
  unknown argument. GREEN: the row is deleted only with the flag, and an order is written either way.
- AC5 — `tools/govkit/selftest.py` — GREEN: the delta row is moved AND merged; `git show :<new>` is
  NOT gov's blob there, the adopter's edit survives beside gov's change, and the two identities split.
- AC6 — `tools/govkit/selftest.py` — the standing predicate, measured ACROSS the write run: tracked
  count unchanged without the flag, RED under the break that drops the guard (18 to 13). Its
  LIVENESS half asserts the count DID fall on the run allowed to delete, so it cannot pass over an
  inert fixture.
- AC7 — `python tools/govkit/refusal_join.py` — exit 0 at 185. Four of the five new refusal branches
  are reached by a named arm, each seen RED. The fifth is NOT armed and says so in its own branch —
  see below. AC7's letter is met 4/5, stated rather than rounded up.
- AC8 — `tools/govkit/selftest.py` — RED with the byte decision deferred: the file lands at
  pre-rename content while the row stamps forward. GREEN: the index blob at the new path is gov's
  blob at `--to` for the NEW source.
- AC9 — `tools/govkit/selftest.py` — GREEN: the verdict is `renamed` and `patched` appears NOWHERE
  in the run's output.
- AC10 — `tools/govkit/selftest.py` — RED OBSERVED TWICE: at the pre-unit engine, and again with
  S0c's exemption removed from the landed engine. Both times a `seed` row printed `current` while its
  gov source no longer existed — a silent green over a file that is gone.
- AC11 — `tools/govkit/selftest.py` — RED with `renamed` absent from the reported-only tuple: the
  `rendered` row falls through to a bare `continue` and only its verdict line prints.

## One refusal branch has NO arm, and it says so itself

`land_through_index` failing AFTER a successful `git mv`. Reaching it needs the TARGET's own git to
refuse a blob write, a mode or a worktree replacement, and this suite manufactures none of those —
the two older call sites of the same helper are in exactly the same position. The gap is written
into the branch, and its message states what state it leaves behind.

## A judgement the spec does not cover

A row the TARGET deleted whose gov source was renamed stays `converged`, not `renamed`. There is
nothing to move; calling it renamed would `git mv` a file that is not there, fail, and freeze the
receipt re-stamp for that run. It has its own fixture row and its own arm.

## What landed outside the unit's own build

The `codebase-map` regen (one function, five lines of `symbols.json`) and the `BRANCH_PIN` raise
180 -> 185 are in this same commit. Both are under paths the builder's file set forbade, and both
are required by the unit — the map leg reds without the first, and that file's own convention
demands the second at each landing, with both values named.

## §5's user-docs item names a section that does not exist

It asks for `WIRE-INTO-PROJECT.md`'s update section. That runbook has no update-verb section at all.
The two dispositions and the flag landed in `skills/deploy-governance/SKILL.md`. Recorded at rev-7.
This is the second spec in a row whose user-docs item pointed at a place in that runbook that is not
there.
