# TOOL-dSettledStage-4 — acceptance ledger

**Serves:** journal TOOL-dSettledStage-4

No merge bar, no self-test suite, no `--selftest` and no leg argv ran in this pass. The pass started
at ea1efc18f. `<p4>` is the product commit, the one that adds this ledger and closes the spec. Each
probe ran from the worktree root: the scanner's functions imported by `python -I` scripts under the
session scratchpad, and arm 43's extract run by hand over fixture repositories under `%TEMP%`. The
base scanner is `tools/gate-lint/sh_hygiene.py` at blob `19e87517`, the blob at 41e57fca5 and at
ea1efc18f, read before the first edit; the base suite is `git show 41e57fca5:tools/push-main.test.sh`.

**Evidences:** TOOL-dSettledStage-4
- AC1 — `(0, 0, 0, 1)` — `scan_stage_file` of the built scanner read the `--allow-empty` fixture as
  (0, 0, 0, 1) and the `--cached` fixture as (0, 1, 0, 0); the base scanner read both as
  (1, 0, 0, 0), PINNED at blob `19e87517`. An unquoted `$(date)` and a `$((1+2))` before
  `--allow-empty` read (0, 0, 0, 1) on the built scanner, and
  `n=$(git diff --cached --name-only | wc -l)` still reads admitted.
- AC2 — `(1, 0, 0, 0)` — the built scanner read each of the eight option fixtures as (1, 0, 0, 0), and
  `--exec-path=/x` too; the base read each as (0, 0, 0, 0), PINNED at blob `19e87517`.
  `git $GIT_OPTS commit` and `git "--no-pager" commit` read (0, 0, 0, 0) on the built scanner.
- AC3 — `(0, 0, 1, 0)` — the built scanner read the two-hop unchecked fixture as
  (1, 0, 0, 0), the two-hop checked one as (0, 1, 0, 0) and the call cycle as (0, 0, 1, 0), each
  under a millisecond; the base read the two-hop unchecked one as (0, 0, 1, 0), PINNED at blob
  `19e87517`.
- AC4 — `FLOOR_ASSERTIONS` — `stage_cases` holds the 13 rows of section 4's table and
  `STAGE_BOUNDARY` its new row, 14 executed assertions, PINNED by section 4's table; the floor is
  165, counted off the arms over the 151 of blob `19e87517`, DERIVED at observation, and its
  `RAISED` line names TOOL-dSettledStage-4. A copy of `read_stage_helpers` making one pass read the
  two-hop unchecked fixture as (0, 0, 1, 0). The `--selftest` run, its printed count and its RED
  are the close's.
- AC5 — `a git global option behind an expansion or in quotes` — an import of the built scanner
  found the label in `run_stage_scan.__doc__` and in the README section under the
  `--stage-commits` heading, `--git-dir` in the module docstring, and the label in
  `STAGE_BOUNDARY` with the class `unread`. Every boundary row read its class and had its label in
  both, squeezed as the selftest reads them, 11 rows, DERIVED at observation.
- AC6 — `memory/project/stage-commit-sites.txt` — `scan_stage_tree` of the built scanner over
  `. :!*.test.sh :!memory/` read 75 sources and 3 unchecked, 4 admitted, 2 unpaired and 0 empty-ok
  sites, DERIVED at observation, and `build_stage_measured` equalled the registry's rows, 3 sites in
  3 rows, DERIVED at observation, so no row moved and the registry is unedited. The leg-argv run and
  its empty-registry and lowered-row cases are the close's.
- AC7 — `l43=0` — the criterion's `<a43>` over this worktree's lander printed `l43=0` with
  `eol-empty=1` and `eol-dirty=1` in `$out43`; with `GIT_CONFIG_VALUE_0=false` it printed `l43=1`,
  no `eol-dirty=1`. The extract from 41e57fca5 with the same rewrite printed `l43=0`, the vacuous
  pass. The arm's stage carries `2>/dev/null`, arm 42's spelling, so git's line-ending warning does
  not reach the suite's output.
- AC8 — `read_stage_calls` — `gen_map.py --write` re-rendered `memory/map/generated/symbols.json`
  with the function, and `gen_map.py --check` then exited 0. This commit changes no spec under the
  spec folder but this one, its status cell and its generated records region. This ledger carries `**Serves:** journal TOOL-dSettledStage-4`.
- AC9 — `shell hygiene (a stage committed with no staged-diff test)` — the spec's section 7 leg
  line names the leg and its section 9 rev-1 entry names the review's item 6, as written by the
  spec author; this pass did not edit either.

**Also probed:** `bash -n` passed over `tools/push-main.test.sh`. The naming lexicon answered OK for
`read_stage_calls` as `py.function`.

**The bug-class checklist over the product commit** selected `failed-stage-reads-as-nothing-staged`
on arm 43's new liveness stage. Its line,
`git add -A 2>/dev/null; git diff --cached --quiet && echo eol-empty=1`,
the spec's spelling and arm 42's, prints the marker over a stage that failed. Joining the two with
`&&` closes it in both arms; the scratch-guard refused the edit once the spec was CLOSED, so it is
left to the close or a follow-up. A cause that persists to the fold still reds the arm, through the
fold's own stage refusal and `eol-rc`.

**Owed to the close (the main loop, after every unit is terminal):**
- New arm `tools/gate-lint/sh_hygiene.py --selftest`, covering AC1 to AC4: RED over a copy with the
  walk, the widened git word and the closure each taken out, GREEN once restored, and its printed
  count against `FLOOR_ASSERTIONS`.
- New arm `tools/push-main.test.sh` 43, covering AC7: RED with `GIT_CONFIG_VALUE_0=false` in place
  of `true`, GREEN once restored.
- AC6's leg-argv run, and the gates section 7 names.
