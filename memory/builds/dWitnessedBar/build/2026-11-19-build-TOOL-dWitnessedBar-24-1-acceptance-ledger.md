# TOOL-dWitnessedBar-24 — acceptance ledger, pass 1

**Serves:** journal TOOL-dWitnessedBar-24

One pass, the second builder, at base `63fda85259e62e81300be901589470dde43d916b` over the rev-6 spec, starting from
the first builder's saved rev-5 work re-checked against rev-6: the PowerShell self-test's guard narrowed to
`{kit}/ps-hygiene.py` (§8 F12), and the shell-role scan graded `shrink-only`, a fall red as `count fell` (§8 F11).
The pass ran no merge bar, no self-test suite and no gate leg. It ran the naming lexicon's `--suggest`, the
generators `leg_factory.py --write`, `govkit.py selfcheck --write` (for `subject-pins.tsv`), `gen_map.py --write`
and `gen_build_index.py --write`, `owed_rows.py --base HEAD`, the canonical `legacy_ledger.py read`, and `python`
probes calling each changed scanner over scratch repositories under `%TEMP%/w24`, plus in-process calls of each
seed's `--measure` and of `eol_class.check_eol` on the tree. Each criterion below was checked on node d on
2026-11-20. Owed to the close: every leg section 7 names, the nine new legs of §4 and the four `New arm:` RED-first
observations.

**Evidences:** TOOL-dWitnessedBar-24
- AC1 — `* text=auto` — over a scratch repository tracking `a.py` with only that line, `eol_class.py <repo>` exits 1
  naming `a.py`; with `*.py text eol=lf` added it exits 0.
- AC2 — `graded count` — `eol_class.check_eol` on the built tree returns no finding over the class population
  (DERIVED from the builder's probe); the `eol_class.py .` leg itself is owed to the close.
- AC3 — `encoding posture (text IO names its encoding)` — `grep -c` under `tools/govkit/` over `registry.toml`
  prints 0, and `grep -n 'encoding_posture.py' kit.toml` under `tools/gate-lint/` names the `[[gate_leg]]` whose
  argv is `["python3", "{kit}/encoding_posture.py"]`, no registry.
- AC4 — `stdout` — `encoding_posture.py --stdout <empty> <repo>` over an entry point printing `"é"` exits 1 naming
  the path and `stdout`; with `sys.stdout.reconfigure(encoding="utf-8")` before the print it exits 0.
- AC5 — `js-io` — `encoding_posture.py --js <empty> <repo>` over `fs.readFileSync(` split across two lines exits 1
  naming `js-io`; with `'utf8'` added it exits 0.
- AC6 — `backslash-path` — `sh_hygiene.py --path-literals <empty> <repo>` over `cd C:\Users\x` in `a.sh` exits 1
  naming it; `cd /c/Users/x` exits 0, and the backslashed text in a comment exits 0.
- AC7 — `fixed-temp` — `sh_hygiene.py --temp-names <empty> <repo>` over a write to `"$f.tmp"` renamed over `"$f"`
  exits 1 naming it, and the leg's row in `tools/gate-legs.json` carries `pack` `portability`.
- AC8 — `heredoc-source` — `sh_hygiene.py --quoting <empty> <repo>` over `cat > gen.sh <<EOF` and
  `IFS=$'\t' read -r a b` exits 1 naming `heredoc-source` and `tab-ifs-read`; a quoted heredoc writing
  `notes.txt` exits 0.
- AC9 — `--bare-bash` — `measure_legs.py --bare-bash <repo>` over `subprocess.run(["bash", "x.sh"])` in `a.py`
  beside a tracked `b.js` exits 1 naming `a.py`; `run_bare_bash` over a guarded launch inside a
  `resolve_bash_py` block beside a tracked `b.js` that launches nothing returns 0, and 1 once `b.js` is untracked.
- AC10 — `census` — in a scratch repository holding a copy of `python_floor.py`, a `python-floor.txt` reading
  `3.99` exits 1 naming `3.99` and `uv python install 3.99`; at the declared floor a tracked `b.py` holding a
  syntax error exits 1 naming `b.py`; `from locale import getdefaultlocale` in a tracked `c.py` exits 1 naming
  `removal 3.15`; the clean repository exits 0.
- AC11 — `count fell` — `sh_hygiene.py --shell-role <ledger> <repo>` with `a.sh` at its row of 10 code lines
  exits 0; at 11 (a comment line added beside it) exits 1; a new `b.sh` exits 1 naming it; at 9 exits 1 naming
  `count fell`; with the row lowered to 9 exits 0.
- AC12 — `portability` — the criterion's `python -c` under `tools/` prints the fifteen pack legs, every rule tag
  and none on the two self-test legs (DERIVED from the builder's probe); under `tools/playbook/`
  `grep -c 'practice.portable.'` prints 0, `grep -c 'powershell hygiene selftest'` prints 1 and
  `grep -c 'shell hygiene ('` prints 0 over `core-pending.txt`.
- AC13 — `legacy_ledger.py read` — run from `tools/lib/` for each of the five populations it exits 0, each seed's
  `--measure` output equal row for row to its seeded home (DERIVED from the builder's probe), and
  `grep -c 'shell-role.txt' .memory-tree.conf` prints 1.
