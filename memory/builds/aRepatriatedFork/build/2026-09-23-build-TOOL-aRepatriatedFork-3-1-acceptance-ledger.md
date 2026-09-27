# TOOL-aRepatriatedFork-3 — acceptance ledger

**Serves:** journal TOOL-aRepatriatedFork-3

One unit pass under the mandate. It ran no merge bar and no self-test suite. Every criterion below
was observed by a direct run of a scanner, a `--selftest` flag or the probe itself. No adopter tree
was written: inCMS's scanner was READ from `C:/projects/incms/main` at `10c15529c` and pointed at
gov's files by absolute path. The a7c78ad2 observations ran in `git clone --local --shared` of gov
under `%TEMP%/r3`, checked out at `a7c78ad2`.

## The fixtures

- **Red-first clone**: `%TEMP%/r3` at `a7c78ad2`, graded by the new scanner with an EMPTY registry
  file and the leg's pathspecs `tools skills`.
- **Selftest breaks**: two copies of the scanner in the scratchpad, one with the `subprocess` arm's
  append removed and one with the `open()` predicate forced false. Each ran `--selftest`, observed
  RED naming only its own arm's fixtures, and was discarded.
- **Probe records**: two scratch files, one whose body says it has no machine gate and one plain.

**Evidences:** TOOL-aRepatriatedFork-3
- AC1 — `check_encoding_posture.py` — inCMS's scanner over the 14 landable files printed `OK: 14 files declare an explicit encoding on every text-IO call.`, exit 0; `grep -c 'encoding=' tools/memory-tree/row_grammar.py` went 5 → 8
- AC2 — `python3 encoding_posture.py --selftest` — `PASS (26 assertions)` from `tools/gate-lint`; each break copy printed `RED (26 assertions)` naming the offending fixtures of the arm it disabled and no other
- AC3 — `encoding_posture.py <empty> <clone> tools skills` — exit 1 at a7c78ad2 over 67 tracked files, 180 sites in 33 findings, naming `tools/memory-tree/row_grammar.py:653:25` and `tools/run-gates/check-receipt.py:151:63`
- AC4 — `python3 tools/gate-lint/encoding_posture.py memory/project/encoding-posture-sites.txt . tools skills` — exit 0, 67 files graded, 153 declared sites in 18 rows; `govkit shipped` gives every registry file a role outside engine, seed, rendered and merged, and none of the 14 is a row
- AC5 — `python3 tools/memory-tree/gotchas.py --declares` — printed `declares: yes` with exit 0 on the gated record, and `declares: no` with exit 1 on the plain one

The leg's first run at a7c78ad2 is AC3's run: red on all 29 landable sites plus the 151 carried
ones. The registry was measured at `85fcb90f`, where govkit's self-test carries two more
`subprocess` sites than at a7c78ad2, which the same scanner over the clone with the seeded registry
names as the only row that differs.
