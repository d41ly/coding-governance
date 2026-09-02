# Build brief — TOOL-dRetiredFork-5

**Serves:** journal TOOL-dRetiredFork-5

## What the unit is

`check(name, fn)` prints `ok   {name}` whenever `fn` raises nothing. A guarded arm prints an honest
`SKIP ... NOT a pass.` and then RETURNS — so `check` sees no exception and stamps `ok` on the next
line. The suite reports coverage it does not have, inside the kit's own proof. inCMS found it and
filed `ABL-aFerriedToolkit-4`; gov has not taken it.

## What this pass does

1. S1 — a `Skipped` sentinel the arms RAISE instead of returning. `check` catches it, prints the arm
   as `skipped` with the guard named, and stamps no `ok`.
2. S2 — the summary reports executed and skipped separately, and REFUSES when both GUARDED arms
   skipped. Keyed on the guarded pair, never on "all arms": 24 of 26 are unconditional, so an
   all-skipped predicate is unreachable and would be dead the moment it landed — the could-not-fail
   shape this unit exists to close.
3. S3 — `encoding="utf-8"` on the corpus-recall `subprocess.run`. VERIFIED before editing, as S3
   demands: gov HEAD has `text=True` with no `encoding=`, so the row is live, not stale.
4. S4 — bump `KIT_CODEBASE_MAP_VERSION` with its paired markers AND regenerate the map, because the
   version rides `inventories.json`, `MAP.md` and `symbols.json` and the freshness gate
   byte-compares them.

## A count in the spec that has already rotted

§3's non-goal says "the four guard EXITS". There are FIVE: `selftest.py` prints a guarded SKIP at
five sites across the two arms. The ARM count — two — is what S1, S2 and AC2 key on and it is
correct. The non-goal's figure is amended to carry no count, per this repo's own rule that a number
in prose beside the thing that owns it is wrong on the next commit.

## Acceptance

AC1-AC4, run rather than asserted, with AC2's RED observed by unsetting both guards.

## And the thing I missed four units ago

Run `python3 tools/memory-tree/gen_build_index.py --check-format` before committing. It is in this
unit's neighbours' gate lists and I omitted it from hand-picked subsets for four units.
