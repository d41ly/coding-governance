# TOOL-aFrugalTurnstile-10 — acceptance ledger

**Serves:** journal TOOL-aFrugalTurnstile-10

No merge bar, no runner and no self-test suite ran in this pass. The checks were the commands each
criterion names, run directly. RED at base `bef97330`, against `git show bef97330:` of the protocol
in a scratch fixture: each AC2 token counted 0 in the §6 range, the AC3 greps found neither
`post-merge bar` in the `gates-green` row nor `GATE_POST_MERGE` in the `GATE_POLICY_FILE` row, and
the file measured 65692 CR-stripped bytes. GREEN against the edit is below. The growth is 1020
bytes, 13 above the rev-1 measurement of 1007 that rev-2 said would move by a handful, and inside
the 1100 ceiling; the template high-water row was re-recorded with `--bump` to match. The close
still owes every §7 leg, among them `unattended protocol size`, `unattended kit gate` (checks 10,
16 and 22), memory hygiene and spec tokens.

**Evidences:** TOOL-aFrugalTurnstile-10
- AC1 — `cmp tools/unattended/PROTOCOL.template.md memory/guides/UNATTENDED-PROTOCOL.md` — exit 0.
- AC2 — `grep -F` — each of `GATE_POST_MERGE`, `--decide`, `record commit alone`,
  `refs/gov/bar-red`, `relaxes` and `under the boundary's decision` counted 1 in the §6 range.
- AC3 — `post-merge bar` — 1 in the `gates-green` row, and the `GATE_POLICY_FILE` row carries
  `GATE_POST_MERGE`.
- AC4 — `bash tools/check-template-size.sh memory/guides/UNATTENDED-PROTOCOL.md` — exit 0,
  `66712 / 66712 bytes (0 under, 100.0%)`, 1020 above 65692, no `WARN` after the high-water bump.
- AC5 — `grep -n 'TOOL-aFrugalTurnstile-10' tools/template-size-limits.txt` — line 115, the comment
  directly above the protocol row on line 116.
- AC6 — `grep -c '^| .GATE_POST_MERGE. |'` — prints 0.
