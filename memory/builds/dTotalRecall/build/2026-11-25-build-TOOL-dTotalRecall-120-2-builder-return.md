**Serves:** journal TOOL-dTotalRecall-120
**Caused-by:** TOOL-dTotalRecall-120

# TOOL-dTotalRecall-120 build pass 2 — the builder's return

The gov-builder return for the pass dispatched at `3c1a90c1e` from [2026-11-25-prompt-TOOL-dTotalRecall-120-build-2-brief](../prompts/2026-11-25-prompt-TOOL-dTotalRecall-120-build-2-brief.md), recorded whole, each number's line tagged by the recorder; the pass tip is `392fd752d`.

## Why

TOOL-dTotalRecall-120 is built as spec rev-2 states and committed in one commit, with no divergence. An armed legacy home whose causes rows are drained now answers the empty set, so every record is graded. AC1 to AC4 were observed by fixture, probe and grep. The suite arm's run and its RED-first observation are owed to the close.

## Summary

Built from the first pass's draft, with `{}` in the plant and the long boolean rewrapped.
- S1 and S2 are in C:/projects/coding-governance/.claude/worktrees/unattended-dtotalrecall-ae256e/tools/memory-tree/record_causes.py (`read_legacy_paths` and its docstrings).
- S3 is the plant `legacy-drained`, its check `check_drained_plant`, and its arm in tools/memory-tree/check-memory-hygiene.test.sh.
- S4: FLOOR_ASSERTIONS 837 -> 842; the shell-role row 3751 -> 3752, through widen record 31 (DERIVED 2026-11-25).
- The spec is CLOSED, and the acceptance ledger is 2026-11-25-build-TOOL-dTotalRecall-120-2-acceptance-ledger.md. The generators also moved symbols.json, LIVE.md, the build README and the spec's generated records block. No deviation is owed.

Checks run, standing in for the `record causes` leg and the hygiene suite's plant arms:
- AC1: `python record_causes.py --fixture --plant legacy-drained` printed the new record and the two former legacy ones under causes, the cause-writer count lines, 3 backfilled and PASS, exit 0 (DERIVED 2026-11-25). It ran from the repository root, not from tools/memory-tree/.
- AC2: plants legacy, causeless and none were byte-identical to acbb74bb in C:/Temp/rf, exits 0, 1, 0; `read_legacy_paths` over a scratch tree with no registration answered None (DERIVED 2026-11-25).
- AC3: the grep printed no line (DERIVED 2026-11-25).
- AC4: the arm, floor and row are in place; the floor is counted by reading. The suite file passed `bash -n` only.
- Break probe: with the old reader put back in memory, the check printed `unarmed` at exit 0, the backfill wrote nothing, and the plant printed FAIL, exit 1 (DERIVED 2026-11-25).
- `lexicon.py --suggest` admits `check_drained_plant`. The pre-commit hook's staged checks passed.

Owed to the close: §7's legs, the hygiene suite's own run (floor 842, PINNED by this commit), and the `New arm:` RED-first observation of `legacy-drained` in tools/memory-tree/check-memory-hygiene.test.sh.

`gotchas.py --for-diff HEAD~1..HEAD` was run over the commit; I read its selection and nothing needed a change. The nearest classes were fixture-plants-a-state-no-writer-makes (the fixture drains through `legacy_ledger.write_rows`) and vacuous-selector-empty-population (the class this unit closes here).

Still red outside this unit: `record_causes.py --cause-writers` names tools/memory-tree/build_records.py@14341c75:1289, unit 121 S14 per the brief. So the `record causes` leg stays red until that lands. Nothing timed out. One early read-only multi-command call was refused by the worktree guard and rerun split. The `--brief` verb answered already recorded, unchanged, rc 0. (DERIVED 2026-11-25, the pass)
