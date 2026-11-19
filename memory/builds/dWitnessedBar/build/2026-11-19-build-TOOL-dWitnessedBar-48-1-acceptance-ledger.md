# TOOL-dWitnessedBar-48 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-48

No merge bar, no self-test suite and no gate leg ran in this pass, the naming lexicon excepted. The
criteria were observed through probes of the unit's own code on node d, 2026-11-19: the two greps
AC1 spells, the nested `resolve_shell_ere` cut out of `cmd_selftest` with `ast` and run alone, and
`scan_bare_bash` imported from `tools/run-gates` and called over fixture repos under `%TEMP%`. The
`New arm:` of spec section 7 still owes its RED-first observation, which the main loop makes at the
close, and so does every suite the section names.

**Evidences:** TOOL-dWitnessedBar-48
- AC1 — `^# >>> resolve_bash_py` — `grep -c` over `tools/memory-tree/row_grammar.py` printed 1, and
  `git grep -nE 'GOV_BASH.{0,30}"bash",'` over the same file printed nothing and exited 1. The new
  block, cut between its two markers, compared equal to the canonical's in `tools/lib/resolve_bash.py`.
  The adapter, cut out of `cmd_selftest` and run against `check-memory-hygiene.sh`, returned the
  hygiene check's ERE and kept Git's own bash in `shell_used`; with `scan_bash` replaced by a refusal
  it returned None, `shell_used` stayed empty and `shell_refused` held the refusal text.
- AC2 — `GOV_BASH` — over a fixture repo tracking `const x = 1;` in a `.js` and a `.py` holding the
  list of a `GOV_BASH` read, the constant `bash` and Git's own bash.exe path, `scan_bare_bash` named
  that `.py` file's list line as `shape 2`; over the same `.js` beside a `.py` holding
  `if argv[0] not in ("bash", "bash.exe"): pass` it returned `[]`. The scanner at `a30a26466`, run on
  the same two fixtures, returned `[]` for the first and named the membership line as `shape 2` for
  the second, each criterion's red. Three more
  literals were probed: `("bash", "/bin/bash")` and `["bash", "bash.exe"]` matched shape 2, and
  `["bash", "sh"]` and a `/bin/bash` membership test did not. Over this worktree the scan returned
  `[]`.
