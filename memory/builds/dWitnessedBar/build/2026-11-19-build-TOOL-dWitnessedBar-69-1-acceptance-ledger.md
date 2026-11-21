# TOOL-dWitnessedBar-69 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-69

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node d,
2026-11-21 (GNU bash 5.3.9 `x86_64-pc-cygwin`, git 2.54.0.windows.1), through a scratch probe that writes
AC1's record under `%TEMP%/wb69`, cuts `read_green_file` from the built `.githooks/pre-push` by its awk
range, sources it and calls it, and through a Python probe that builds AC4's scratch `git init`
repository and a stripped copy of `verdict_backends.py` under `%TEMP%/wb69py`. The hook passed `bash -n`.
Its shell-role count, measured by the gate-lint kit's seed through `ratchet.py widen shell-role`, is 1720
past the 1719 row, widened under `2026-11-21-build-TOOL-dWitnessedBar-69-widen-9`. §7 names no new arm;
every leg §7 names, and the two staged breaks it records, are the main loop's at the close.

**Evidences:** TOOL-dWitnessedBar-69
- AC1 — `rec_sha` — the sourced cut over the record (`sha` forty `a` LF, `sha` forty `b` CR-LF, `manifest<TAB>x<TAB>`, `fingerprint` forty `c`, a bare `fingerprint`, an unterminated `selftests<TAB>on`) set `rec_sha` to forty `b`, `printf %s "$rec_man" | od -c` showed `x  \t`, `rec_fp` stayed forty `c` past the bare line, and `rec_st` read `on`. An absent path and a directory path each left `rec_sha` empty.
- AC2 — `wc -c` — after `sed 's/%[$].[\]r.}/}/'` the `diff` of the two cuts counted one changed line, `printf %s "$rec_sha" | wc -c` printed 41 and `tail -c1 | od -c` showed `\r`, so the CR reaches the strip on this Windows node.
- AC3 — `IFS= read -r` — the cut piped to `grep -c 'awk'` printed 0 and to `grep -c 'IFS= read -r'` printed 1; the cut holds one column-0 `}`.
- AC4 — `newline=""` — over the CR-LF record for tree forty `c`, `read_local_verdict({}, <forty a>, <t>, repo=<repo>)` with `tools/run-gates` first on `sys.path` answered `GREEN`, and its why's `repr` held `run r\r1,`. With the copy whose `read_tag_lines` strip `v[:-1] if v.endswith("\r") else v` reads `v` first on `sys.path` (one changed line by `difflib`), the call answered `DEAD PROBE`. `grep -n 'newline=""' tools/run-gates/verdict_backends.py` names the `with open(slot, ...)` line in `tools/run-gates/verdict_backends.py#read_local_verdict`.
