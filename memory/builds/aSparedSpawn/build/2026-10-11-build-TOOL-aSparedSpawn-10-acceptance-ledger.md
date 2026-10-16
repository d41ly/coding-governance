# Acceptance ledger — TOOL-aSparedSpawn-10

**Serves:** journal TOOL-aSparedSpawn-10

Node `a`, 2026-10-11, bash 5.3 under MSYS. The pass ran no bar, no suite, no held leg and no slice
of a suite. The unattended kit's gate-guard refused a `--plan` run of the leg's own file before
VERIFYING, so every criterion worded as a run of that file is owed there, and the pass observed the
classifier through the fixture committed beside this ledger,
`2026-10-11-build-TOOL-aSparedSpawn-10-plan-fixture.sh` (spec rev-3). It extracts the leg's lines from
`SELF_ROW=` to the `--plan` branch verbatim and runs that branch's five calls over a hand-built git
repository holding the real unattended `kit.toml` and driver, against one `run-selftests.sh --list`
captured from this tree (92 selected rows; that listing took 77 s). `bash -n` passed on the leg, the
unattended driver's suite and the fixture.

**Evidences:** TOOL-aSparedSpawn-10
- AC1 — `plan-fixture.sh` over the leg's classifier block — at a commit that leaves the kit marker
  alone, exactly one shard row per family was `probe` and the other fourteen printed `represented ·
  by shard 4/8`; dispatched plus represented equalled the 92 selected rows. The plan branch exits
  before the leg's `mktemp -d`, read in the diff. The `--plan` run of the leg itself, with an empty
  `TMPDIR` checked afterwards, is owed at VERIFYING.
- AC2 — `foreign-prefix.gov.test.sh --kit unattended` — OWED at VERIFYING. A filtered run clones and
  moves the tree three times and runs suites, so the represented lines at each prefix and the
  summary's separate count were not observed in the pass.
- AC3 — `plan-fixture.sh`, four plans at successive commits — each family printed `rule input HEAD
  <40-hex sha> as an integer mod 8 = <r>`; the representative matched `int(sha, 16) % 8 + 1`
  computed independently in python; a later commit moved it (shard 3/8 to shard 5/8 on the last
  run); a root commit printed "has no first parent" and probed every shard; a commit moving
  `KIT_UNATTENDED_VERSION` printed both marker lines and probed every shard of both families. The
  same observation through the leg's own `--plan` is owed at VERIFYING.
- AC4 — `git grep -n 'runs/whole' -- tools/run-gates/foreign-prefix.gov.test.sh` printed nothing
  (exit 1); `plan-fixture.sh` read the plan's order and found all eleven whole rows ahead of every
  probe row in descending budget, 1080 s first. The leg's own `--plan` is owed at VERIFYING.
- AC5 — `foreign-prefix.gov.test.sh --kit <whole row>` with a 1 s budget staged — OWED at VERIFYING.
  It runs that row at three prefixes, so the scaled hang verdict inside the pool was not observed in
  the pass. `run_row` itself is unchanged; the whole row now reaches it through the pool's dispatch,
  read in the diff.
- AC6 — `plan-fixture.sh` with a stale `WHOLE_RUN` entry staged — the plan printed `FAIL  a
  whole-run declaration names no row in the population: no such row anywhere` and counted one
  failure; with a second probe row forced into one family it printed that the family "has 2 probe
  row(s) where the rule answers 1" and counted one failure. The leg's own `--plan` exiting 1 on a
  scratch copy is owed at VERIFYING.
- AC7 — `foreign-prefix.gov.test.sh` timed at base `22efab65` and after, on a frozen clone — OWED at
  VERIFYING. Two whole runs of the leg are a held run, the owner's by the 2026-10-06 ruling, and
  neither wall time exists yet.
- AC8 — `python tools/gate-lint/sh_hygiene.py memory/project/substitution-fed-loops.txt` — before the
  pass it exited 1 naming the unattended driver's suite, "the registry declares 1 site(s) at `<<<`
  and the scan measures 2"; after it exited 0, "58 declared site(s) in 43 row(s), no undeclared loop
  fed by a command substitution", with the registry untouched. The changed arm itself runs in the
  driver suite's shard 1 at VERIFYING.
- AC9 — `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt . --only run-gates-2leg`
  — calibrated on its 5-fork specimen, then "ok run-gates-2leg · measured 95 · ceiling 99 · base
  97"; the row's reason names the stated margin, the readings it sits over and the stale
  direction's bound at 95.

Checked as well, none of them a bar leg run: `sh_hygiene.py --spawn-idioms` with the leg's pathspecs
exited 0 with every registered count unchanged; `sh_hygiene.py --location-probes` exited 0;
`lexicon.py` exited 0 over the six new shell function names; `check-spec-tokens.py` exited 0 with no
hit on this spec; `gen_map.py --check` exited 0 after `--write`.
