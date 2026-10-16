# Acceptance ledger — TOOL-aSparedSpawn-16

**Serves:** journal TOOL-aSparedSpawn-16

Node `a`, 2026-10-12, bash 5.3 under MSYS. The pass ran no bar, no suite, no held leg and no slice of
a suite. Its runtime observations come from the instrument committed beside this ledger,
`2026-10-12-build-TOOL-aSparedSpawn-16-direct-checks.sh`, run once over the changed tree and once over
`git show f53211e6c:` copies of the same files, the unit's base; the declaration checkers ran
directly with their own argv. `bash -n` passed on the runner, the hook and every changed suite. S10
and its AC11 moved to the build's exit at rev-3 and are not observed here.

**Evidences:** TOOL-aSparedSpawn-16
- AC1 — `python tools/govkit/govkit.py selfcheck` — exit 0 after `selfcheck --write` added the `held-halves selftest` row; before it, the same command exited 1 naming that leg.
- AC2 — `python tools/gate-lint/sh_hygiene.py --spawn-idioms memory/project/spawn-idiom-sites.txt . ':!*.test.sh' ':!memory/'` — exit 0, every registered site matching the scan, run after every other code edit; this build's `cat-file` and `printf-subst` sites were rewritten first, and the canary's `var-pipe` row was set to its measured count.
- AC3 — `bash tools/gate-lint/fork-count.sh memory/project/fork-ceilings.txt . --only run-gates-1leg` — `ok`, measured 51 against ceiling 51; with `--only run-gates-2leg`, `ok`, measured 53 against ceiling 55. Both rows read STALE before the edit.
- AC4 — `python tools/memory-tree/check-arms.py --check` — exit 0 and no `HYGIENE check-arms: tools/run-gates/run-gates.sh` line; at the unit's base it named the six sites. The canary arms 12a2 and 9d3 that arm them are OWED at VERIFYING; the two refusals 12a2 asserts were observed by running `--calibrate-width` directly in a scratch repo, each exiting 1 with its whole text.
- AC6 — `direct-checks.sh push` — changed hook: `pre-push: not honoured from the environment by this bar: GATE_REUSE_SAMPLE GATE_REUSE_DAY`, and the stub bar saw `unset|unset`; base hook: no such line, and the stub bar saw `0|1`. The suite arm `RP S6` is OWED at VERIFYING.
- AC10 — `grep -n 'by TOOL-aSparedSpawn-13 and -16' tools/run-gates/run-gates.evidence.test.sh` — one `RAISED 163 -> 208` line, and `FLOOR_ASSERTIONS` is 208. Whether the executed count reaches 208 is OWED at VERIFYING.
- AC11 — amended rev-3, the spec's entry that moved S10 with this criterion to the build's exit as a named ask —
  `--dispatch` — MOVED to the build's exit with S10 at rev-3, so no check observes it in this unit; it is an ask, not a discharge. The spec's rev-4 entry names that ask, `TOOL-aSparedSpawn-25`.
- AC12 — `direct-checks.sh reuse` — changed runner: with K1's count at 9, a K2 execution on a dirty tree, then a K1 reuse, the next K1 run printed `GATE ok    pa  (executed: reused on 10 runs in a row)` and the age line; base runner: counting in its per-name `age.*` file (`age.${heldkeys[$i]}` at f53211e6c) that run printed `GATE reuse pa`. The evidence arm `16-AC12` is OWED at VERIFYING.
- AC13 — `grep -n 'sleep 1[25]' tools/run-gates/run-gates.test.sh` — finds neither the 9k nor the 9m sleeper, each now polling for its signal file. The fork-loaded run of both arms is OWED at VERIFYING.
- AC14 — `direct-checks.sh contended` — shipped runner: the contended leg's key holds no cache entry and the spinner's does; a copy whose cache writer reads `.retry.rc` wrote the contended entry, which the new 9f assertion reds on. The arm itself is OWED at VERIFYING.
- AC15 — `python tools/run-gates/held_halves.py --selftest` — 34/34 arms; with `load_half`'s `newline=""` removed it printed `FAIL held-halves selftest: S14 a CR in a failing leg's output splits off no verdict row` and 33/34.
- AC16 — `git grep -n 'ts_now' -- tools/` — prints nothing; `grep -c 'EPOCHSECONDS:-' tools/run-gates/run-gates.sh` prints 0.
- AC17 — `direct-checks.sh reuse` — changed runner: the nondeterministic red's `log:` file opens `# run-gates | leg pa | exit 1`; base runner: `exit 0`, the sample's second look. The evidence arm `16-AC17` is OWED at VERIFYING.
- AC18 — `direct-checks.sh reuse` — changed runner: `GATE ok    pa  (sampled against a cached ok)` (an instance of `GATE ok    <leg>  (sampled against a cached ok)`) on a drawn leg, the aged tail on a count of 10, and `GATE FAIL  pa  (exit 1) (sampled against a cached ok)` on a drawn red; base runner: the plain lines. The canary arm 9d2 is OWED at VERIFYING.
- AC19 — `direct-checks.sh reuse` — changed runner, with a `git` that fails `hash-object` first on PATH: a reusing bar and a clean plain bar each printed `the input keys could not be measured (the toolchain digest)` once, a dirty plain bar none; base runner: silent on all three. The canary arm 9d3 is OWED at VERIFYING.
- AC20 — `grep -n 'print_env_failure' memory/builds/aSparedSpawn/spec/2026-10-09-spec-TOOL-aSparedSpawn-14.md` — prints AC11's line, S10's, the §7 arm line and the rev-4 and rev-5 log lines; AC11 names the five checks 27, 29, 56, 69 and 88.
