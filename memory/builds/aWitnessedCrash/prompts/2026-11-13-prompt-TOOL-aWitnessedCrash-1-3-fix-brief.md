**Serves:** research TOOL-aWitnessedCrash-1

# Fix brief — TOOL-aWitnessedCrash-1, the close bar's three own reds

The close's bar (`GATE_FULL=1 bash tools/run-gates/run-gates.sh` at 4f779dc0c) redded three legs, each this unit's own.
Clear them, changing nothing else. The spec stays at rev-2; none of these moves a criterion.

## 1. `spawn budget (forks per hot entrypoint)`

`fork-count: RED memory-hygiene · measured 192 · ceiling 190 · delta +2`. The witness added two command substitutions:
`_CRASH_LOG=$(mktemp)` and `_crash=$(grep -E '^.+: line [0-9]+: ' "$_CRASH_LOG" || true)`.

- Replace the `grep` substitution with a builtin read loop over `$_CRASH_LOG` matching the same shape with `[[ =~ ]]`,
  so the verdict block forks nothing. Keep the matched lines and their order exactly as the grep printed them.
- The `mktemp` is the one fork the witness cannot avoid. Raise the `memory-hygiene` row of
  `memory/project/fork-ceilings.txt` by exactly the count `bash tools/gate-lint/fork-count.sh` then measures above 190,
  and append to that row's reason, in the house form of the rows beside it: raised 190 -> <n> by TOOL-aWitnessedCrash-1,
  the crash witness's one `mktemp`, measured three times on node a under bash 5.3, 2026-11-13. Measure with that tool,
  three runs; if the count is 190 the row stays.

## 2. `harness arms (fail branches armed or pinned)`

`check-arms: tools/memory-tree/check-memory-hygiene.sh:3677 status site (reasoned) has no POSITIVE assertion naming its own
failure text ("HYGIENE FAILED — bash reported a runtime error on this engine's stderr, so a check may have stopped
part-way and its silence is not a pass")`. The arm in `tools/memory-tree/check-memory-hygiene.test.sh` greps only the
prefix. Make that assertion grep the whole failure text. The assertion count does not change, so `FLOOR_ASSERTIONS` stays 696.
Confirm with `python tools/run-gates/check-arms.py` or whichever command the leg's argv in `tools/gate-legs.json` names.

## 3. `writing practice (records and units)` — pinned facts

`pinned-facts: red · memory/builds/aWitnessedCrash/build/2026-11-13-build-TOOL-aWitnessedCrash-1-acceptance-ledger.md ·
unpinned fact `0 lines`` and `` `5 s` ``. Pin each on its line (PINNED) or drop the figure; keep every AC's backticked token.
Run the leg's own argv from `tools/gate-legs.json` to confirm.

## Order

Code first (items 1 and 2, then the fork-ceiling row), then the ledger, then the CLOSED header commit last. The kit
version stays 2.159: these edits land before the unit closes again, so no second bump is owed — confirm with
`python tools/govkit/govkit.py epoch --base f9a87e782`.
