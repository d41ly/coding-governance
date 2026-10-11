# PLAY-aFrugalTurnstile-1 — acceptance ledger

**Serves:** journal PLAY-aFrugalTurnstile-1

No merge bar, no runner and no self-test suite ran in this pass. The checks were the commands each
criterion names, run directly. RED at base `bef97330`: the AC1 grep counted 0 in both files, the
template's high-water read 48597, and `check-template-size.sh AGENTS.md` printed a WARN (54377 ->
54472, the 95 bytes the spec pinned). AC2's RED was a staged break: with the new line deleted from
`AGENTS.md` alone, `adopt-playbook.sh --check` printed `DRIFT`; restored, it printed OK. GREEN
against the edit is below. The close still owes every §7 leg, among them playbook parity, the
agent-cap restatement, memory hygiene and spec tokens.

**Evidences:** PLAY-aFrugalTurnstile-1
- AC1 — `grep -c 'DECLARED to run after the merge'` — 1 in the Landing range of each file, the
  line before it being the "After each merge run" bullet, outside the `kit:unattended` block.
- AC2 — `render-playbook OK` — printed by `adopt-playbook.sh --target . --check` after the render.
- AC3 — `bash tools/check-template-size.sh` — exit 0, 48866 / 49152, 269 above 48597, no `WARN`;
  the high-water row reads 48866.
- AC4 — `bash tools/check-template-size.sh AGENTS.md` — exit 0, 54741 / 64512, no `WARN`; the
  `AGENTS.md` high-water row reads 54741 (95 found at base plus 269 from this line).
- AC5 — `bash tools/check-line-length.sh` — 0 over 450 for both files, exit 0.
- AC6 — `grep -cE 'GATE_POST_MERGE|refs/gov|post-merge.sh'` — prints 0 over the new template line.
