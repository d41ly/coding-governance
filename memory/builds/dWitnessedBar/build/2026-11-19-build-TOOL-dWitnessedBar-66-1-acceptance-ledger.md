# TOOL-dWitnessedBar-66 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-66

No merge bar, no self-test suite and no gate leg ran in this pass. The criteria were observed on node d,
2026-11-21 (GNU bash 5.3.9 `x86_64-pc-cygwin`, GNU grep 3.0, git 2.54.0.windows.1), through a scratch
probe that writes S1's record with the arm's own `printf`, cuts `read_green_file` from a hook by the arm's
awk range, sources it, and runs the arm's compare and failure line, over HEAD's `.githooks/pre-push` and
two scratch copies of it under `%TEMP%/u66p`; and through the arm's `read_tag_lines` call run as written.
The suite file passed `bash -n`, and its code-line count, measured by
`tools/gate-lint/sh_hygiene.py#measure_code_lines`, stays 611, its `memory/project/shell-role.txt` row.
No `a=$((a+1))` was added or removed. The `New arm:` line of §7 owes its RED-first observation, which the
main loop makes at the close, and so does every leg §7 names.

**Evidences:** TOOL-dWitnessedBar-66
- AC1 — `rec_sha` — over S1's record HEAD's cut set `rec_sha` to forty `b`, and `printf %s "$rec_sha" | wc -c` printed 40; the compare held. The record holds two CR-LF pairs (lines 1 and 3), counted 2 by a Python byte read and by `grep -c -U $'\r$'`; plain `grep -c $'\r$'` on this node's Git for Windows grep reads in text mode and printed 0 at a prompt and 3 inside `$(...)`, so the figure 2 is observed with `-U` here. `grep -n 'rec_sha'` names the arm's comment, its sourced call and its failure line.
- AC2 — `$1=="sha"{print $2}` — against a copy whose `sha` read is `awk -F'\t' '$1=="sha"{print $2}'` (one `diff` line opening `>`), `rec_sha` was 81 bytes and the arm failed with `gov-canary: the hook's read_green_file set rec_sha to 'a…a|b…b' …`, naming `rec_sha` and joining the two values with `|`. Against a copy whose `sha` read lacks ` sub(/\r$/, "", v);` (one `diff` line opening `>`), `rec_sha` was 40 bytes and the arm stayed green on this Git for Windows node, as §4 Evidence and §8 F3 state: that half is OWED to a node whose awk and bash `$(...)` keep the CR, or to `TOOL-dWitnessedBar-70` S3 after unit 69 S1. The failure line's CR rendering was probed on a value `b…b<CR>`, printing `'b…b\r'`.
- AC3 — `repr(r.get("sha"))` — the arm's `read_tag_lines` call over S1's record, opened with `newline=""`, printed `'GREEN' '` + forty `b` + `'`, and the compare `[ "$rgf_py" = "'GREEN' '$rgf_b'" ]` held; the `sha` value is the one AC1's hook cut reads. `grep -n 'repr(r.get("sha"))'` names the arm's Python line.
