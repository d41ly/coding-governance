# Acceptance ledger — TOOL-aSparedSpawn-12

**Serves:** journal TOOL-aSparedSpawn-12

Node `a`, 2026-10-12, bash under MSYS, Python 3.14. The pass ran no bar, no suite, no held leg and
no slice of a suite. The observations below come from the two instruments committed beside this
ledger. `2026-10-12-build-TOOL-aSparedSpawn-12-direct-checks.sh` runs the changed runner directly over
a hand-built repository in a scratch root, with a stub govkit and a four-leg manifest of bash legs:
`repo ok`, kit `kx`'s suite, kit `ky`'s suite, and `uz`, a selftests-chunk suite no kit ships. Each
bar cost about 35 s here. The first run, bounded at 580 s, stopped inside AC5 with no failure; the
second ran whole and printed 39 PASS and one FAIL. The FAIL was the instrument's own AC7 diff line,
which compared `.githooks/` against the spec's base `22efab65` although units 1 to 5, 9 and 15 of
this build had moved it first. The corrected line compares against `76578ece`, the commit that
opened this unit, and was run directly: `git diff --name-only 76578ece -- .githooks/` printed only
`.githooks/pre-push.test.sh`. `2026-10-12-build-TOOL-aSparedSpawn-12-select-sim.py` replays the rule
as built, and its output is the `.out` file beside it.

`bash -n` passed on `tools/run-gates/run-gates.sh`, `tools/run-gates/run-gates.test.sh`,
`.githooks/pre-push.test.sh` and the direct-checks instrument, and an `ast.parse` passed on the
selection program lifted out of the runner. The new suite arms are owed at VERIFYING, each checked
here only by reading it against the direct check that observed the same behaviour: section 13 of
`tools/run-gates/run-gates.test.sh` (25 assertions over AC1 to AC6 and the stamp, floor 356 to 381),
arms 23b and 23c of `.githooks/pre-push.test.sh` (AC7), and the two `[aSS-12 AC8]` checks in
`tools/govkit/selftest.py`.

**Evidences:** TOOL-aSparedSpawn-12
- AC1 — `direct-checks.sh` — after a `GATE_SELFTESTS=1` run seeded three records, a `changed` bar
  with nothing moved held kx and ky as `GATE held  <name>  (self-test, unchanged since <sha8>)`.
  After a commit moving only `kx/engine.sh`, kx printed its selection line naming
  `kx/engine.sh moved since <sha8>` and `GATE ok`, and ky was held and printed no `GATE ok`. A
  commit moving only kx's `project-owned` row held kx, so a non-epoch role selects nothing. The suite
  arm is owed at VERIFYING.
- AC2 — `direct-checks.sh` — a commit moving only `ky/y.test.sh` executed ky; one moving only
  `uz/guarded.txt` executed uz, naming that path. Every `changed` bar printed the fallback line
  naming `uz suite` exactly once. The suite arm is owed at VERIFYING.
- AC3 — `direct-checks.sh` — one bar with kx's record deleted, ky's record naming a dangling
  `commit-tree` sha and uz's manifest row given a `ceiling` printed `runs (no last-run record)`,
  `runs (recorded <sha8> is not an ancestor of HEAD)` and
  `runs (its manifest row changed since its record)`. A record holding `not-a-sha` printed
  `runs (its last-run record is unreadable)`. The
  suite arm is owed at VERIFYING.
- AC4 — `direct-checks.sh` — after eleven empty commits, a bar with `GATE_SELFTESTS_MAX_LAG=20` held
  ky, and under the default bound ky ran with the reason
  `recorded <sha8> is 11 first-parent commits behind HEAD, beyond the bound 10`. The suite arm is
  owed at VERIFYING.
- AC5 — `direct-checks.sh` — with a kx record present, a bar where kx moved and `KX_RED=1` printed
  `GATE FAIL  kx suite` and left no kx record. With ky's record removed and a tracked file dirtied,
  ky executed green and no ky record was written. The suite arm is owed at VERIFYING.
- AC6 — `direct-checks.sh` — after a commit adding `ky/extra.sh`, which no kit ships, ky was held
  while the stub govkit answered. With `GOVKIT_STUB_OFF=1` the bar printed `govkit is not reachable`
  exactly once, ky ran naming `ky/extra.sh moved since <sha8>`, and kx was held unchanged on its
  diff. In the default mode a held leg still printed `set GATE_SELFTESTS=1 to run` and no selection
  line appeared. The suite arm is owed at VERIFYING.
- AC7 — `direct-checks.sh` — the `gate-full-green` of a `changed` run read `selftests changed`, a
  `GATE_SELFTESTS=1` run's read `selftests 1`, and the run header carried `selftests changed`.
  `check_green_record`, lifted unedited from `.githooks/pre-push`, forced a switch-on push over a
  `changed` record with the predicate 8 reason and accepted a switch-off push. Only
  `.githooks/pre-push.test.sh` moved under `.githooks/` since `76578ece`. Arms 23b and 23c are owed
  at VERIFYING.
- AC8 — `govkit.py shipped --epoch` on this tree — 242 rows, all in `engine`, `seed`, `rendered` or
  `merged`, and identical to the plain verb's rows filtered to those roles; no `project-owned` or
  `generated` row. Over a hand-built one-entry registry in `direct-checks.sh`, `--epoch` printed only
  the engine row while the plain verb printed the generated one. `shipped --all` and the flag given
  twice each exited 2 naming `--epoch`. The selftest arms are owed at VERIFYING.
- AC9 — `select-sim.py` over the last 30 first-parent commits of `main` at `76c924e7` — 13.3% of
  36221 held leg-seconds selected, under the 23% of rule B, against the pinned 13%. Commits selecting
  nothing: 0 of 30, against the pinned 23 of 30. The whole difference is one leg,
  `template size gate selftest`. No kit ships its suite and it declares no guard, so the rule as built selects it on
  every commit, which is what an unguarded leg means to the runner. With it set aside, 17 of 30
  commits select nothing, inside the ±2x band. An owner or a guard for that one leg would restore the
  zero-run figure, and that is a follow-up.
