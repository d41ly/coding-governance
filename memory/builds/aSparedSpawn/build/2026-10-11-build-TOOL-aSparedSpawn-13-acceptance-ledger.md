# Acceptance ledger — TOOL-aSparedSpawn-13

**Serves:** journal TOOL-aSparedSpawn-13

Node `a`, 2026-10-12, bash under MSYS. The pass ran no bar, no suite, no held leg and no slice of a
suite. The observations below come from `2026-10-12-build-TOOL-aSparedSpawn-13-direct-checks.sh`,
committed beside this ledger with its output in the `.out` file. It runs the changed runner directly
over a hand-built repository with its own local bare remote and a nine-leg manifest of `bash -c` legs,
one per class plus a legacy `impure` leg, a leg reading `FLIP`, a toggling leg and a leg reading
`RED`, none of which any key holds. Every guarded leg runs because the base is an empty tree. It
then pushes through a copy of the changed `.githooks/pre-push` to a local bare remote with a stub bar
that prints the knob it received. Its first run printed 62 ok and 6 FAIL. Each FAIL was the
instrument's own setup, all fixed before the second run: an expected entry count of 7 that should
have been 8, a toggling leg's flag left set before its arm, an age check reading files joined
without newlines, a stale `gate-full-green` from an earlier fixture run, and a PATH shim for
`timeout` that git's hook environment put behind its own directories. The second run printed 68 ok
and 0 failed, against the runner and the hook as committed here.

`bash -n` passed on `tools/run-gates/run-gates.sh`, `.githooks/pre-push`,
`tools/run-gates/run-gates.evidence.test.sh`, `tools/run-gates/run-gates.test.sh`,
`.githooks/pre-push.test.sh` and the instrument. `tomllib` parsed both changed `kit.toml` files, and
each of the four descriptors' `reads` equals its manifest row's. `fork-count.sh --only` read the
one-leg and two-leg runner rows at 51 and 53 forks both with this change and at its parent, so the
spawn budget does not move. Both rows were already STALE against their ceilings of 72 and 74 before
this unit.

The changed and new suite arms are owed at VERIFYING, each checked here only by reading it against
the direct check that observed the same behaviour. They are the reuse section of
`tools/run-gates/run-gates.evidence.test.sh`, rewritten for the cache with no `GATE_FULL` and planted
entries where a dirty tree writes none; its 13-leg precomputed-keys arm; the `reads` key-set pair and
section 9d of `tools/run-gates/run-gates.test.sh`; and the `RP` arms of `.githooks/pre-push.test.sh`.

**Evidences:** TOOL-aSparedSpawn-13
- AC1 — `direct-checks.sh` — after an earning bar at an empty-tree base, a `GATE_REUSE` bar at a
  second base executed `based` and printed `GATE reuse` for `pure` and `hist`. The suite arm is owed
  at VERIFYING.
- AC2 — `direct-checks.sh` — after a commit that touched only a file outside every guard, `hist`
  executed and `pure` was reused; a second bar at that HEAD reused `hist`. The suite arm is owed at
  VERIFYING.
- AC3 — `direct-checks.sh` — with `GATE_REUSE_DAY=1` against an earning bar on today's day, `clk`
  (which reads `clock`) executed and `pure` was reused. The suite arm is owed at VERIFYING.
- AC4 — `direct-checks.sh` — a `GATE_REUSE` bar in a worktree added after the earning bar printed
  `GATE reuse` for `pure` and `clk`. The suite arm is owed at VERIFYING.
- AC5 — `direct-checks.sh` — on a cleared cache a bar with `RED=1` left no entry under the red leg's
  key and wrote its green sibling's. A bar on a tree holding an untracked guarded file (under which
  the runner's `TREE_CLEAN` reads `no`) left the entry count at 7. A reused leg's entry bytes were
  unchanged after the reusing bar. The suite arm is owed at VERIFYING.
- AC6 — `direct-checks.sh` — at `GATE_REUSE_SAMPLE=1` with `FLIP=1` the bar exited 1, printed
  `cache disagreement · flip · <key>` with the key the record holds and `nondeterministic · nd`,
  erased flip's entry and wrote two quarantine files. After a clean bar earned flip's key again, a
  `GATE_REUSE` bar executed flip and reused `pure`. The suite arm is owed at VERIFYING.
- AC7 — `direct-checks.sh` — with every age counter set to 10, the next `GATE_REUSE` bar executed
  `pure`, printed `pure was reused on 10 runs in a row, so it executes`, and left every counter at 0.
  The suite arm is owed at VERIFYING.
- AC8 — `direct-checks.sh` — `GATE_FULL=1` with `GATE_REUSE=1` printed no `GATE reuse` line and
  `GATE_FULL is set, so nothing is reused`; a reusing bar left no `gate-full-green`, and the earning
  bar's stamp read `reused 0`. The suite arm is owed at VERIFYING.
- AC9 — `direct-checks.sh` — a `GATE_REUSE` bar erased an entry touched 31 days back and kept one
  touched 29 days back. The suite arm is owed at VERIFYING.
- AC10 — `direct-checks.sh` — the legacy `impure` leg executed on the bar that reused every other
  leg. After a push of a new branch to the fixture remote, its key moved with the `remote` leg's while
  `pure`'s did not. The suite arm is owed at VERIFYING.
- AC11 — amended rev-6, the spec's entry recording that this criterion was never observed —
  NOT OBSERVED — not run — it needs two whole bars with the self-test tier on a frozen clone, hours
  on node `a`, which no pass may run. It is owed at VERIFYING as the reused count and seconds a
  second bar in a fresh worktree reports.
- AC12 — `direct-checks.sh` — under `GATE_REUSE_PUSH` naming HEAD, the probed tip and the
  advertisement digest, `rem` and `hist` were reused and `pure` and `based` executed. A moved tip,
  another advertisement digest, another pushed sha and a commit moving a guarded file each executed
  `rem`. At the hook, a first push to an empty remote, whose probe has no tip to answer with, printed
  `reuse not offered: the ls-remote probe did not answer with the main tip` and handed the bar no
  knob. A probe that fails outright takes that same branch and was not staged, because a PATH shim
  cannot reach the hook. The suite arms are owed at VERIFYING.
- AC13 — `direct-checks.sh` — the reusing push bar's record read `reuse push`, an empty `full` and a
  `reused` count above 0, and the hook's scoped decision line read
  `reuse offered to remote and history legs at <sha8>, tip <sha8>`, with the bar receiving
  `<pushed sha> <the remote's pre-push main> <digest>`. The suite arms are owed at VERIFYING.
- AC14 — `direct-checks.sh` — the reusing push bar wrote no `gate-full-green`. A planted full green
  whose `reused` read 1 made the hook print `FULL gate on main push` naming
  `says its run reused 1 leg(s)`, and the same record reading 0 scoped. The suite arms are owed at
  VERIFYING.
- AC15 — `direct-checks.sh` — a push carrying `GATE_REUSE_PUSH=planted` was told
  `not honoured from the environment by this bar:` naming `GATE_REUSE_PUSH`, and the bar never received
  `planted`; under a FULL decision it received no knob. `git grep -n 'never sets it'` over
  `tools/run-gates/README.md` printed nothing, exit 1. The H49 arm, which still sees an environment
  `GATE_REUSE` ignored, is owed at VERIFYING with the new arms.
