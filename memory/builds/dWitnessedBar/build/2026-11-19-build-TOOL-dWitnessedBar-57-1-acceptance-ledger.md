# TOOL-dWitnessedBar-57 — acceptance ledger

**Serves:** journal TOOL-dWitnessedBar-57

This pass ran no merge bar, no gate leg and no self-test suite. Every criterion below was checked on node
d on 2026-11-20 by probing the unit's own code: `refuse-wrong-shell.sh --coverage` over the built tree and
over a scratch fixture repository under `%TEMP%` built as the resolver suite's order fixture is;
`scan_bare_bash` and `regen.run_command` called in process; `ratchet.py --fixture --plant`;
`legacy_ledger.py seed --home` over a scratch repository under `%TEMP%`; `inherited_red.py up` over two
`build_target` fixtures; `drift_report.py --gate-health --fixture`; `verdict_flow.py --fixture
flakes-record`; and greps and `git log` over the tree. The close owes every leg of section 7, the RED-first
observation of its six `New arm:` lines, and AC14 and AC18, which only the close can observe.

**Evidences:** TOOL-dWitnessedBar-57
- AC1 — `derived from` — `bash tools/lib/refuse-wrong-shell.sh --coverage` printed `derived from 96 files`,
  and the §4 probe printed `86 10 96` on the built tree; in the scratch fixture, `tools/x/indent.sh`, whose
  only call is `resolve_python >/dev/null` indented under `if`, was named `BREAK tools/x/indent.sh never
  calls refuse_wrong_shell || exit 2`. The resolver suite's order fixture carries the case (owed at close).
- AC2 — `resolve_python() { echo bash; }` — the same fixture's `tools/x/stub.sh`, holding the indented stub
  alone, was not listed by `--coverage`.
- AC3 — `grep -c 'refuse_wrong_shell || exit 2' tools/lib/resolve-python.sh` — printed 0, and `--coverage`
  printed `dropped: tools/lib/resolve-python.sh (TOOL-dWitnessedBar-27's listed member the predicate
  excludes: ...)` on the tree and in the fixture.
- AC4 — `scan_bare_bash` — over a fixture repository whose `x.py` holds
  `x = (B if a == "bash" else "") or shutil.which(a)` and `y = shutil.which(b)` it returned
  the one shape-4 hit on the planted `x.py`'s first line, and over the gov tree `[]`; `regen.run_command(['bash', '-c', 'exit 0'], '.', 30)`
  with `regen.BASH` empty returned status 127.
- AC5 — `shell_used.append(found)` — the `sed -n` range shows it the line before `return out[-1]`, and
  `shell_refused.append(refusal)` the line before the first `return None`; present at HEAD.
- AC6 — `grep -c '^# >>> resolve_bash_py'` — printed 1, 0 and 0 for `tree_lib.py`, `row_grammar.py` and
  `corpus_ids.py`; both modules carry `from tree_lib import scan_bash`, and in process
  `corpus_ids.scan_bash is tree_lib.scan_bash` and `row_grammar.scan_bash is tree_lib.scan_bash` read True;
  the tree_lib block equals `tools/lib/resolve_bash.py`'s byte for byte.
- AC7 — `prints 8` — the §4 shape-2 probe over blobs at `cdfbd1cf` printed 8.
- AC8 — `empty seed conf-scalar-pins` — `python ratchet.py --fixture --plant empty-seed` passed: the armed
  empty home beside `ROW_DUPLICATE_PIN="0"` exited 1 printing `empty seed conf-scalar-pins` and
  `re-seed it: remove pop/rows.txt, then run python ...`, and no `unheld` line.
- AC9 — `LL.read_home_state` — `grep -c '# unarmed' ratchet.py` printed 0, the grep names line 379 in
  `run_unarmed` and line 605 in `run_keys_not_scalar`, and `--fixture --plant unarmed-home` passed: a home
  opening the unarmed line exited 1 printing `unarmed conf-scalar-pins`.
- AC10 — `outside the tree` — `legacy_ledger.py seed --home <home> --copy <template>` over a scratch
  repository printed `outside the tree` for `../outside/x`, an absolute path outside the tree and
  `.git/x.txt`, `ignored ign/x.txt` under an ignored `ign/`, each exiting 1 and writing nothing; an
  absolute in-tree home printed `armed nodir/abs.txt`. The resolver suite's part 2o carries the cases.
- AC11 — `affordance-exempt\.toml` — the `git grep` printed nothing; arms 7 and 8 read the basename
  `affordance-exempt.txt` from the adopter's seed call by `sed`, and red when none is found (owed at close).
- AC12 — `inherited_red.py up` — over an LF and a CRLF `.githooks/gate-env.sh` it exited 0 and left
  `A=1`, `B=2  # kept`, a tab-led `C='3'` and an unended `D=4` byte for byte, each file's line ends kept.
- AC13 — `EXCLUDED_KINDS_BEFORE_FIX_OF` — the grep names the definition (line 123), the
  `EXCLUDED_KINDS_BEFORE_REFUSAL` derivation (124) and the `excluded rows` template (293); the committed
  records' validity is the `runlog record schema` leg's, owed at close.
- AC14 — `push-main.sh --prepare` — not observable in a pass: the close runs the shell-role derivation on
  that merge. This pass's own growth is settled in `2026-11-20-build-TOOL-dWitnessedBar-57-widen-2`, each
  row set to its measured count (353, 116, 1167).
- AC15 — `fe49c7d2a` — the §4 pass-commit rule printed nothing for `TOOL-dWitnessedBar-28`, `fe49c7d2a`'s
  SHA for `TOOL-dWitnessedBar-24` and `aecf1c95a`'s for `TOOL-dWitnessedBar-6`, never `ad002a024`.
- AC16 — `--fixture held` — `drift_report.py --gate-health --fixture held --selection <empty file>` printed
  `gate-health fixture held ok`: with its quarantine row appended the bar read `legs 1/1`, and with no
  `--selection` the mode exited 2 naming the flag; the bare `--gate-health --fixture held` exited 2.
- AC17 — `^# >>> acceptance_reader` — the grep printed 2, and every path outside `memory/` that
  `git show --name-only --format= 7b649d671` lists is spelled in unit 51's spec.
- AC18 — `_check_exists_refused` — the `sed -n` range prints the `not w` refusal; the scratch-copy
  `govkit.py selfcheck` half is a gate leg's command, owed at close.
- AC19 — `grants: PLAY-dClosedLoop-3` — the grep printed §8 F3's grant naming `memory/HYGIENE.md` and
  `memory/guides/BUILD-METHOD.md`, and `git show --name-only --format= 28edeaa0b` lists both.
- AC20 — `git log --merges --oneline cc35bb62c^..ef33493d7` — printed nothing, and the `--format=%h` log
  named `94e566d88` and `cc35bb62c`, neither `75a15d9ce` nor `ef33493d7`.
- AC21 — `.memory-tree.conf` — the grep over its uncommented lines printed 0.
- AC22 — `mismatch []` — §4's pack probe printed `portability 15`, `product-tests 1` and `mismatch []`,
  exit 0; over a scratch copy of the manifest with every `pack` key removed it printed
  `mismatch ['portability']` and exited 1.
