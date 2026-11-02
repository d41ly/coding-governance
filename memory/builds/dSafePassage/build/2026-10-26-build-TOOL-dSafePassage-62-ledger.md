**Serves:** journal TOOL-dSafePassage-62

# TOOL-dSafePassage-62 — acceptance ledger

The unit as built, at spec rev-1. `tools/govkit/govkit.py`: `write_install_receipt(target,
receipt_path, doc)` writes `.governance/install.sums` from every `doc["files"]` row carrying
`sha256`, then the receipt, each through `write_atomic`; `apply`, `update`'s findings, unattributed
and stamp paths and `adopt` call it in place of their own pair, and `_cmd_update`'s walking branch
calls it before `upgrade_steps.run_step_walk`, `gov_commit` unmoved. The comment over
`ADOPTER_BAR_PATHS` names the one writer. `tools/govkit/upgrade_steps.py`: the `rollback-update`
family gains the plant `schema-up-kill`. `tools/govkit/selftest.py`: `check_step_rollback` gains its
`[dSP-62]` row. `help/upgrade-steps.md`'s "After a kill" paragraph says what the receipt holds after
a kill.

HOW EACH CRITERION WAS OBSERVED. No gate, suite or bar ran in this pass. AC1 and AC2 were observed by
the unit's own CLI, `python3 tools/govkit/upgrade_steps.py fixture rollback-update --plant
schema-up-kill`, over its scratch fixture under `%TEMP%` on node d (Windows, Git Bash); AC3 and the
first half of AC4 by `git grep`. They stand in for the `govkit selftest` leg's `[dSP-62]` row for
this unit only.

Owed at the close: `govkit selftest`, `govkit refusal join`, `govkit acceptance matrix`,
`govkit selfcheck`, `recall floor arms`, `policy fixtures`, `encoding posture`, `lexicon naming
predicates`, `docs` (AC4's `python tools/govkit/docs_leg.py` exits 0, which the role hook refused
in this pass), `memory hygiene`, `spec tokens`; and the new arm's RED-first observation (§7): the
`[dSP-62]` row with the write before the walk taken out of a working copy.

**Evidences:** TOOL-dSafePassage-62
- AC1 — the plant exited 0 printing `rollback-update: the rollback exits 0 · tools/demo/one.txt b'v1\n' · schema 3 · no steps · gov_commit A`, the rollback's own line `wrote 1, moved 0, deleted 0`, and no `FAILED`. Red: with the `write_install_receipt` call before the walk taken out of a working copy, it exited 1 printing `tools/demo/one.txt b'v2\n'`, `wrote 0`, and `rollback-update: FAILED · the rollback did not exit 0 with one.txt at v1, schema 3, no `steps` and gov_commit A`; the copy was restored.
- AC2 — the same run printed `rollback-update: after the kill · gov_commit A · tools/demo/one.txt row at B`. Red: the same broken copy printed `... tools/demo/one.txt row at A` and `rollback-update: FAILED · the killed receipt does not name gov_commit A with the one.txt row at B's vintage`.
- AC3 — `git grep -n -F 'write_atomic(target / ".governance" / "install.sums"' -- tools/govkit/govkit.py` printed one line, `tools/govkit/govkit.py:4338`, inside `write_install_receipt`; five at `41062397`.
- AC4 — `git grep -n -e "before its first step" -- help/upgrade-steps.md` printed line 173 of the "After a kill" paragraph. `python tools/govkit/docs_leg.py` is a gate leg the role hook refuses here: owed at the close.

The `New arm:` lines of this unit were observed at the close, each RED on its staged break and GREEN restored; a line counts observed when its break reds at least one of its arms. Observed by a researcher in scratch clones of `83817478f` (batch c, `2026-10-28-prompt-TOOL-dSafePassage-37-close-arms-c-researcher.md`), each break staged alone and restored: The `New arm:` line was observed at the close, RED on its staged break and GREEN restored, in a scratch clone of `83817478f`. Under tools/govkit/selftest.py (`check_step_rollback` row `schema-up-kill`), the break was the pre-walk `write_install_receipt` taken out: `FAIL [dSP-62] fixture rollback-update schema-up-kill exits 0 …`, where the fixture prints `rollback-update: FAILED · the killed receipt does not name gov_commit A with the one.txt row at B's vintage`. Restored, GREEN: 1 of 1 `ok`.
