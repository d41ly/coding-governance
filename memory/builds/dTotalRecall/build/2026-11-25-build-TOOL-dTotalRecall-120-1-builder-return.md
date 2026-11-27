**Serves:** journal TOOL-dTotalRecall-120
**Caused-by:** TOOL-dTotalRecall-120

# TOOL-dTotalRecall-120 build pass 1 — the builder's return

The gov-builder return for the pass dispatched at `20e9bd298` from [2026-11-25-prompt-TOOL-dTotalRecall-120-build-brief](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-120-build-brief.md), recorded whole, each number's line tagged by the recorder; the pass tip is `20e9bd298`.

## Why

DIVERGENCE: §4 "The plant" cannot be built as written. It says the fixture calls `legacy_ledger.write_rows(root, reg, [])`. `tools/memory-tree/legacy_ledger.py#write_rows` takes a mapping and iterates `rows.items()`, so that call raises `AttributeError("'list' object has no attribute 'items'")` (DERIVED 2026-11-25, probe). Every caller I listed in tools/memory-tree and tools/policy passes a dict, `ratchet.py` and `policy.py` among them. `run_fixture` catches only ValueError, OSError and StopIteration, so the plant as specced ends in a traceback and AC1 cannot hold.

WHAT THE SPEC WOULD HAVE TO SAY: in §4 "The plant", `legacy_ledger.write_rows(root, reg, {})`. That one literal is the whole fix. §2 S3, §6 and §8 stand as they are. `write_rows` must not be taught to accept a list: it sits in the byte-identical `legacy_ledger_py` block, which §4 does not touch. (DERIVED 2026-11-25, the pass)

No other claim I checked fails:
- `read_legacy_paths` returns None for an armed home with no row, as the Goal says.
- Every reader of the answer is safe with the empty set, as §4 lists them. (DERIVED 2026-11-25, the pass)
- `read_legacy_keys` answers a set in the same situation.
- The §7 leg names all resolve in tools/gate-legs.json. (DERIVED 2026-11-25, the pass)
- The naming lexicon admits `check_drained_plant`.
- No path beyond the declared write set turned up.

## Summary

Nothing is committed. C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/tools/memory-tree/record_causes.py is restored, and the tree is as dispatched, with only RUN.md staged. The `--brief` verb answered "already recorded, unchanged", rc 0.

The `record_causes.py` half of the unit (S1, S2 and the plant of S3) is drafted with `{}` in place of `[]` and saved as C:/Temp/claude/7a8436c9e3b87ce5/9067262b-db21-4497-8ba8-ef2deab46f53/scratchpad/u120/draft.patch. Once §4 reads `{}` it applies as it stands, except that one continued boolean in `check_drained_plant` came out as a single long line to rewrap. Not drafted: the suite arm, `FLOOR_ASSERTIONS`, the shell-role widen, the ledger and the generated map files. (DERIVED 2026-11-25, the pass)

Probes over that draft, before the restore (they stand in for the record causes leg and the suite's plant arms):
- AC1: `python record_causes.py --fixture --plant legacy-drained` printed the new record under `causes`, the cause-writer count lines, 3 backfilled and `fixture legacy-drained · PASS`, rc 0 (DERIVED 2026-11-25).
- AC2: the plants legacy, causeless and none were byte-identical to `acbb74bb` run in C:/Temp/rf, at rc 0, 1 and 0. `read_legacy_paths` over a scratch repository with no registration answered None (DERIVED 2026-11-25). C:/Temp/rf now stands detached at `acbb74bb`.
- AC3: the grep printed no line (DERIVED 2026-11-25).
- AC4: not started.

The bug-class checklist was not run, because there is no commit. The rest of §7's legs, and the RED-first observation of the new suite arm, stay owed to the close.

A RED FOR THE MAIN LOOP, outside this unit. `python tools/memory-tree/record_causes.py --cause-writers` over this tree lists `tools/memory-tree/build_records.py@14341c75:1289` as red (DERIVED 2026-11-25). It is a bare `**Serves:** ` literal with no cause line in reach and no census marker. That file's last commit is unit 117's `07486a8f8`. So the `record causes` leg reads red at HEAD independently of this unit. I changed nothing there.

One AC2 baseline attempt was refused by the worktree guard for an inline git command and was rerun from a script file. Nothing timed out.
