# TOOL-dDeclaredLoop-43 — acceptance ledger

**Serves:** journal TOOL-dDeclaredLoop-43

No merge bar, no self-test suite and no gate leg ran in this pass, and `guard.py --selftest` was not
run. The criteria were observed on node `d` (win32) by probes of the unit's own code, each by direct
CLI with the host temp directory pointed at the session's scratch: the new plant
`write-guarded-rollback`; the `raise-admitted`, `set-run-live` and `proof-signed-fallback` plants,
which write through the loop kit's copy; the instruction command's `record` plant; the overlay's
`write-then-render` plant; the `awk` cut AC5 spells; and the naming lexicon's suggest verb for every
function this pass wrote, the block's nested helper renamed for it (deviation 433).

Owed to the close: every leg the spec's section 7 names; the RED-first observation of the spec's one
`New arm:` line, the `write-guarded-rollback` plant run over the in-place write at this pass's base,
where the spy sees no rename; and the `loop guard fixtures` budget row in
`tools/run-gates/selftest-budgets.txt` read against the leg's own timing, since the plant adds one
scratch repository to that leg.

The close's RED-first observation, made by the main loop on 2026-11-17 at `a48272d09` in scratch
worktrees outside the repository: each staged break applied, the arm run, the break restored and the
arm run again, the green half also read off every loop leg run whole at that commit.
`python tools/loop/guard.py --fixture --plant write-guarded-rollback` with every function the unit's pass
changed in `tools/loop/guard.py` swapped back to its pre-pass source exited 0, and 0 once restored: not
reddened by this break, so not observed.
`python tools/loop/guard.py --fixture --plant write-guarded-rollback` with every function the unit's pass
changed in `tools/lib/guarded_write.py` and `tools/loop/policy_edit.py` swapped back to its pre-pass source
exited 3, and 0 once restored: RED observed.

**Evidences:** TOOL-dDeclaredLoop-43
- AC1 — `record refused over a prior file` — `python tools/loop/guard.py --fixture --plant write-guarded-rollback` printed `held` for the record's error reaching the caller, the policy file's bytes equal to the committed bytes, two renames onto it and no temp sibling, then `bytes held`; the scenario held.
- AC2 — `record refused, no prior file` — the same run printed `held` for the error reaching the caller, the path not existing, one rename onto it and no temp sibling; the scenario held.
- AC3 — `interrupted at the rename` — the spy raised `KeyboardInterrupt` on its first call; `held` for the interrupt reaching the caller, the policy file holding its committed bytes and no temp sibling; the scenario held.
- AC4 — `a callable over its prior bytes` — `held` for the policy file being the committed bytes plus the appended line, the handed path a sibling and not the target, `record()`'s value returned and no temp sibling; the plant printed `all held` and exited 0.
- AC5 — `os.replace` — the `awk` cut over `tools/lib/guarded_write.py`, `tools/loop/policy_edit.py` and `tools/playbook/instructions_edit.py`, carriage returns dropped, gave three outputs with one md5 digest, each holding `os.replace`.
- AC6 — `python tools/playbook/overlay.py --fixture --plant write-then-render` — printed `the write's render holds the new overlay row in the same command` and `overlay: fixture · green`, exit 0.
