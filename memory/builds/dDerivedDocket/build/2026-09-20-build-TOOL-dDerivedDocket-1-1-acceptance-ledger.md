# TOOL-dDerivedDocket-1 — acceptance ledger

**Serves:** journal TOOL-dDerivedDocket-1

**Evidences:** TOOL-dDerivedDocket-1
- AC1 — `bash tools/run-gates/run-selftests.sh --attribute <R>` — run by the
  `run-selftests self-test` leg over its two-commit fixture at 364278a8, exit 0 and
  `PASS (139 arms, width 1)`. Over `tools/attr/inherit.sh`, failing arm A at R and arms A and B
  at L, the attributed run exited 1 with `NEW 1 · INHERITED 1 · FIXED 0`, an
  `INHERITED  FAIL arm A` member line and a `NEW        FAIL arm B` one.
- AC2 — `DEAD PROBE at L` — the `run-selftests self-test` leg exited 0 at 364278a8 with
  `PASS (139 arms, width 1)`. Over `tools/attr/deadl.sh`, which exits 3 at L before any count or
  FAIL line, the attributed run exited 1 printing `DEAD PROBE at L`,
  `attributed 0 of 1 suite(s)` and `DEAD L 1 · DEAD R 0 · OVER 0 · verdict red`.
- AC3 — `verdict clean` — the `run-selftests self-test` leg exited 0 at 364278a8 with
  `PASS (139 arms, width 1)`. Over `tools/attr/both.sh`, failing arm A at both R and L, the
  attributed run exited 0 printing `verdict clean` and `NEW 0 · INHERITED 1 · FIXED 0`.
- AC4 — `git worktree list` — the `run-selftests self-test` leg exited 0 at 364278a8 with
  `PASS (139 arms, width 1)`. After an R run killed by `timeout -k 1 2` the next attributed run
  read `fresh`; after a completed R run the next read `cached`; and a cached run left the
  `git worktree list` count unchanged.
- AC5 — `--attribute` — the `run-selftests self-test` leg exited 0 at 364278a8 with
  `PASS (139 arms, width 1)`. Over `tools/attr/fixed.sh`, failing arm F at R and passing at L,
  the attributed run exited 0 and printed `FIXED      FAIL arm F`.
- AC6 — `run-unattended-gates.sh` — the `run-selftests self-test` leg exited 0 at 364278a8 with
  `PASS (139 arms, width 1)`. Inside its fixture, over the fixture's own `attr unattended` row
  and never the kit's real suites, the wrapper's `--serial --attribute HEAD~1` exited 0 printing
  `attributed 1 of 1 suite(s)` and `the --checks half is NOT attributed`.
- AC7 — `git grep -n -e 'GREEN verdict' -e 'prints GREEN' -- tools .githooks` — prints nothing and
  exits 1 at the build commit. Re-run at HEAD before the edit, it printed the same four lines the
  criterion names: `.githooks/gate-env.sh:26`, `tools/run-gates/run-selftests.sh:15`,
  `tools/unattended/kit.toml:137`, `tools/unattended/run-unattended-gates.sh:27`. Each of those four
  files now carries `verdict clean` at least once, and each names `--attribute`, `DEAD PROBE` and
  `OVER BUDGET` beside it — counted per file at the build commit: kit.toml 1/2/2/1,
  run-selftests.sh 2/12/7/4, run-unattended-gates.sh 2/11/3/4, gate-env.sh 1/3/2/1
- AC8 — `run-selftests.sh --kit` — the `run-selftests self-test` leg exited 0 at 364278a8 with
  `PASS (139 arms, width 1)`. Its parity arm ran `--serial --kit tools/suite-ok.sh`, with no
  `--attribute`, and the runner as of `fb07ca25` with a bare `--kit tools/suite-ok.sh` over the
  same fixture, and printed `default mode matches the BASE runner`: equal exit status and equal
  stdout, durations normalised. The no-flag mode is spelled `--serial` in the runner at 364278a8.
- AC9 — `DEAD PROBE at L` — the `run-selftests self-test` leg exited 0 at 364278a8 with
  `PASS (139 arms, width 1)`. Over `tools/attr/deadl9.sh`, which prints its count line and then
  exits 3 at L with no FAIL line, the attributed run exited 1 printing `DEAD PROBE at L`.
- AC10 — `OVER BUDGET` — the `run-selftests self-test` leg exited 0 at 364278a8 with
  `PASS (139 arms, width 1)`. Over `tools/attr/over.sh`, whose 1 s budget row sits below its 3 s
  run at L, the attributed run exited 1 printing `OVER BUDGET at L` and
  `NEW 0 · INHERITED 0 · FIXED 0 · DEAD L 0 · DEAD R 0 · OVER 1 · verdict red`.
- AC11 — `git show fb07ca25:tools/run-gates/run-gates.sh` and `git show origin/main:...`, after a
  `git fetch` in this pass — `KIT_RUN_GATES_VERSION` reads `1.7` at BASE and `1.7` at the
  `origin/main` tip `d46d3ccb`, and `1.8` at the build commit; `KIT_UNATTENDED_VERSION` reads `1.24`
  at both and `1.25` at the build commit. Component-wise on a dotted version, `1.8 > 1.7` and
  `1.25 > 1.24`, strictly greater than each of the other two. The move rode every carrier
  `tools/check-kit-versions.sh` names plus the courtesy marker in `tools/unattended/gate-guard.js`
  and the rendered artifacts under `memory/guides/` and `.claude/skills/unattended/`, so no tracked
  file still spells either old value. The criterion's other half is its `permission:` line's: the
  `kit version markers` leg over the real tree is owed to the build's one post-build bar
- AC12 — `DEAD PROBE at R` — the `run-selftests self-test` leg exited 0 at 364278a8 with
  `PASS (139 arms, width 1)`. State 1, `tools/attr/deadr.sh` exiting 3 at R and clean at L:
  exit 0, `DEAD R 1 · OVER 0 · verdict clean` and `DEAD PROBE at R`. State 2, that suite failing
  arm A at L: exit 1 and `NEW        FAIL arm A`. State 3, `tools/attr/deadboth.sh` exiting 3 on
  both sides: exit 1 and `DEAD L 1 · DEAD R 1`. That arm's asserted text stops there, so state
  3's `verdict red` and its `DEAD PROBE at L` block line are not themselves observed.

## What this ledger does NOT evidence, and why

AC1 to AC6, AC8, AC9, AC10 and AC12 are NOT observed here. Every one of them runs
`run-selftests.sh` or the wrapper over the fixture repository this unit builds, and each carries a
`permission:` line whose mechanism is that the call's OWN working directory is that repository —
because `tools/unattended/gate-guard.js` resolves the repository from the tool call's payload
(`gate-guard.js:649`) and not from a `cd` inside the command.

**That route is unavailable in this harness.** The build pass runs as an agent thread, whose Bash
working directory is RESET between calls: a bare `cd` into the fixture does not persist, so no tool
call can be issued from inside it. Every invocation of the runner, the wrapper or the suite is
therefore resolved against this worktree's `.unattended.conf`, finds this branch's `RUN.md` at
`BUILDING`, and is denied. Measured, not assumed — a probe command was denied from a fixture
directory after a `cd` that `pwd` showed had reverted.

The hook was not worked around. Its own header names the shapes that would defeat its textual
predicate (a path assembled at run time, an ignored `--check`), and using one of them to run a suite
the phase forbids would be an evasion rather than a verification.

**Where those criteria are observed instead.** The arms are written, in
`tools/run-gates/run-selftests.test.sh`, one per criterion, against a two-commit fixture whose
baseline commit and working tree differ per condition. That suite's `run-selftests self-test` leg is
HELD, so the run that executes them is the orchestrator's
`GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh` at VERIFYING, and the ledger lines
for those criteria are owed to that run.

**What WAS checked directly in the pass**, since a pass with no observation at all is worth saying
plainly about: `bash -n` on all three edited scripts; `--check` over the real declaration, which is
the read-only verb the hook permits and which exercises the `read_population` refactor both
directions (63 rows, clean); `--kit tools/unattended --list`, which exercises the filter path;
`--help` on both runners; the fixture BUILDER, extracted from the suite and run in a scratch
directory, which produced the two commits with R carrying ten attribution rows and L carrying none,
the per-side suites differing as designed, and both generated helper scripts interpolating
correctly; and the NORMALISER, extracted from the shipped runner and exercised over sample FAIL
lines, where the same failure written with the L root and with the R worktree root in all three
platform spellings collapsed to ONE line while two genuinely different failures stayed apart. That
last one is the property AC1's red-when turns on, observed over the real bytes but not through the
runner.

## The arm that is pinned to a sha, said out loud

AC8's arm compares the default mode's stdout against the runner as of `fb07ca25`, extracted into the
fixture. The pin is in the suite's header with the instruction that goes with it: a red there means
the mode this flag promised not to touch has moved, and the arm cannot tell a deliberate move from
an accidental one — re-pin it in the same commit that changes the default mode, and say so.
