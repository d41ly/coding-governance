# TOOL-aWokenSentinel-21 — acceptance ledger

**Serves:** journal TOOL-aWokenSentinel-21

Every leg-shaped half below reads `observed at --close`: this pass ran no gate leg, no bar and no
suite, and `unattended-build.test.sh` itself was not run — the pin is authored from the static count
and the first green under `GATE_SELFTESTS=1` or `run-selftests.sh --kit tools/workflows` is its
named observer, as spec 21 §3 says. The pass verified with the direct checks the spec's section 6
names: one `python3 -c` over `tools/gate-legs.json` and `tools/run-gates/selftest-budgets.txt` at
the tip and over the manifest at `1d8530e7` for AC1; the greps of AC2, AC3 and AC4 over the tip and
over the files at `1d8530e7`; the floor block extracted with `sed -n` and evaluated by `bash -c` on
both sides of the pin for AC5; the self-read line extracted the same way and run by
`bash -c '<line>' <path>` over the tip, over a scratchpad copy with `true` appended after its
`exit $st`, and over a near-miss copy with a blank and a comment appended; `bash -n` over the suite;
and a `cat -A` probe over the diff for CR bytes. Those stand in for the `every held leg is budgeted,
every budget row resolves`, `leg ceilings clear their evidenced maximum`, `govkit selfcheck`,
`memory hygiene`, `spec tokens (a spec's own names resolve)` and `install-prefix (shipped surface)`
legs, which run once at the close. The budget's one measured invocation came from a scratchpad
script holding the suite's preamble (lines 1 to 116, `HERE` pinned to the kit dir) and timing
`run_wf "$UNITS" "$(returns CONVERGED 0)"` three times: 183, 186 and 182 ms, `RESULT` each time.
One fold was owed and taken as the spec's rev-3: §4's lower-bound sentence had the `PV-AC12` branch
masking grep-counted sites on an adopter-less tree, and that branch holds zero `same`/`has`/`hasnt_`
sites (it counts through inline `n=$((n+1))` only), so the static count is a lower bound on every
tree; and AC5's fixture copy lives under the session scratchpad rather than `%TEMP%`, because the
harness reserves the short path for a clone and a one-file copy is not one. The kickoff manifest's
`last-audit` is re-stamped in this commit because `tools/gate-legs.json` is on its `watch` line.

**Evidences:** TOOL-aWokenSentinel-21
- AC1 — `python3 -c` over `tools/gate-legs.json` at the tip printed the leg `{'name': 'unattended-build self-test', 'argv': ['bash', 'tools/workflows/unattended-build.test.sh'], 'guard': ['tools/workflows/'], 'chunk': 'selftests', 'subject': 'kit', 'ceiling': 120}`, and the same read over `tools/run-gates/selftest-budgets.txt` printed `budget 60 factor 2 product 120 ceiling==product: True`; over `git show 1d8530e7:tools/gate-legs.json` the read printed `[]` for that name. OBSERVED; the declaration leg and the ceilings leg are observed at --close.
- AC2 — `grep -c '^unattended-build self-test	' tools/run-gates/selftest-budgets.txt` printed `1` at the tip and `0` over the file at `1d8530e7`; the row's second field is `60` and its reading column opens `sized from one run_wf invocation measured alone on node a 2026-09-21 from the suite's sourced preamble: 186 ms worst of three, times the 103 run_wf sites the suite carried at 1d8530e7 by grep -c, 19 s, x1.5 floored at 60`. Derivation: `grep -c 'run_wf ' tools/workflows/unattended-build.test.sh` printed `103`; 103 x 0.186 s x 1.5 = 28.7 s, under the file's 60 s floor. OBSERVED.
- AC3 — `grep -c 'name = "unattended-build self-test"' tools/govkit/registry.toml` printed `1` at the tip and `0` over the file at `1d8530e7`; `grep -c 'unattended-build.test.sh.*tools/workflows/kit.toml' tools/govkit/registry.toml` printed `1`, the row being the `tier2-review self-test` row's text with the suite filename substituted and nothing else changed. OBSERVED; `govkit selfcheck` is observed at --close.
- AC4 — `grep -cE '^\s*(same|has|hasnt_) ' tools/workflows/unattended-build.test.sh` printed `326` at the tip and `sed -n 's/^FLOOR_ASSERTIONS=//p'` over the same file printed `293`, which is `326 * 9 / 10` rounded down exactly (2934 / 10) and above `326 * 8 / 10 = 260`; the pin sits at line 1287, the `--- $n arms` summary at 1295 and `exit $st` at 1296; over `git show 1d8530e7:tools/workflows/unattended-build.test.sh` the sed printed nothing and the grep printed `326`, up from the 317 the spec pinned at its own base, moved by unit 15 as the spec expected. OBSERVED.
- AC5 — the floor block extracted with `sed -n '/^FLOOR_ASSERTIONS=/,/^\[ "\$n" -ge "\$FLOOR_ASSERTIONS" \]/p'` (two lines) and run by `bash -c` with `n=292` and `st=0` printed `FAIL executed 292 assertions against a floor of 293 — arms are UNREACHABLE rather than absent` and left `st=1`; with `n=293` it printed nothing and `st` stayed `0`. The self-read line, extracted by `grep -F '[ "$(sed -n'` and run by `bash -c "st=0; $line; echo st=\$st" <path>`, printed `FAIL a line follows the terminal exit and can never run` and `st=1` with `$0` bound to a scratchpad `cp` of the suite with `true` appended by `printf` after its `exit $st`, and printed `st=0` with `$0` bound to the unmodified suite; a near-miss copy with a blank line and `# a comment` appended read `st=0`; `sed -n '/^exit \$st$/,$p' tools/workflows/unattended-build.test.sh | grep -cvE '^\s*(#|$)'` printed exactly `1` at the tip. OBSERVED; the suite's own green under the pin is observed at --close.
- checkers — `bash -n tools/workflows/unattended-build.test.sh` exited 0; `git diff | cat -A | grep -c '\^M'` printed `0` over every touched file; `python3 -c` parsed `tools/gate-legs.json` whole after the insertion. OBSERVED; the legs are observed at --close.
