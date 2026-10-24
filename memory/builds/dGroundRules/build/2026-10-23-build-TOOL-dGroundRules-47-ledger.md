# TOOL-dGroundRules-47 — acceptance ledger

**Serves:** journal TOOL-dGroundRules-47

No merge bar, no gate leg and no self-test suite ran in this pass. Each criterion's command ran as
spelled from the repository root of this worktree, on the built record and on the same file at
commit 9bcca652. S3 is observed by a probe that stands in for the `memory hygiene` leg's index
check: a scratch call imported `tools/memory-tree/gotchas.py`, built the records with `records`
and compared `render` with the tracked index byte for byte; it read identical, and the record's
anchors stayed the three the unit before it left. Owed at the close: the `gotchas selftest`,
`memory hygiene`, `recall floor` and `recall floor arms` legs over the built tree. This unit
declares no `New arm:` line.

**Evidences:** TOOL-dGroundRules-47
- AC1 — `grep -c "verbatim from the repository root"` over "The fix" — printed `1` on the built record and `0` at commit 9bcca652; with `grep -c "never copied"` in place of the last stage it printed `1` and `0`.
- AC2 — `grep -c "TOOL-dGroundRules-40"` over "Where it bit" — printed `1` on the built record and `0` at commit 9bcca652.
