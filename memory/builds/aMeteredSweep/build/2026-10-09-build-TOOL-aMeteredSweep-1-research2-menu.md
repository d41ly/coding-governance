# Research — where the bar's hours go, and the units that remove them

**Serves:** research TOOL-aMeteredSweep-1

Node `a`, 2026-10-09. Two rounds. Round one is aMeteredSweep's
`2026-10-08-build-TOOL-aMeteredSweep-1-speed-research.md` and its five appendices: the levers per
leg and for the runner, ranked by seconds on a profiled bar. Round two is the five `-research2-*.md`
appendices beside this record, on the questions round one left open. Every figure there is an
estimate from static counts or one-line timings unless it says measured; none ran a suite.

## The cost model, measured

| | MSYS, node `a` | WSL2, same machine |
|---|---:|---:|
| spawn of `true` | 21 ms quiet, 632 to 818 ms loaded | 1.07 to 1.2 ms |
| `$(:)` subshell fork | 89 to 315 ms | 1.15 ms |
| scratch-repo cycle | 4052 ms | 23 ms |
| `git rev-parse` | ~225 ms | 45 to 91 ms on `/mnt/c`, native on ext4 |

The suites' cost is arms times processes per arm times that price. The unattended driver suite makes
about 1,450 calls of a 13,310-line driver, each paying a preamble of about 17 avoidable spawns; the
gate suite runs the whole 50-check gate about 449 times. Refusal sites went 168 to 367 in the driver
and 154 to 264 in the gate between 2026-08-23 and 2026-10-09, and `ARMS_FLOORS` has only ever risen.

## What round two found

- **WSL2.** Feasible from a separate clone on WSL's own disk; Linux git cannot open a Windows
  worktree and a WSL prune against the primary would delete its 18 worktrees, so WSL only ever
  fetches from it. CI is `windows-latest` on purpose. One default-bar leg is sure to red under
  Linux and about 15 suites have Windows-only arms. Estimated 10 to 30x for bash and git-fixture
  legs; the 13,324 s bar would land near 15 to 45 minutes.
- **In-process driver.** No verb body calls `exit`; only the conf preamble and the dispatch tail
  block sourcing. Wrap them as `load_driver_conf` and `main`, guard on `BASH_SOURCE`, and the suite
  sources the driver once per shard and runs each arm in a subshell, keeping exit codes, file
  writes, git effects and traps. About 5 percent of calls stay real processes, plus a parity table.
  `check-unattended.sh` already has `--only 28`; extend it to `--only core` and `--only N`.
- **Retirement.** About 93 percent of driver sites and 92 percent of gate sites have no real-run
  evidence of firing, and half of the checks that did fire were wedges or false positives. 12
  driver and gate pairs test one condition. The proposed review retires a site only if it never
  fired, cites no incident, its condition survives elsewhere and it is not security-shaped; the
  owner decides each batch; a growth budget sits beside the floors.
- **Reuse.** A soundness bug today: `run-gates.sh:2140-2150` keys a dirty guarded file by its
  status line, not its content, so `GATE_REUSE=1` reuses a stale green on a second unstaged edit
  (dev runs only; the pre-push scrubs it). Selecting held suites by the kit whose shipped bytes
  moved would have run 13 percent of their seconds over the last 30 commits on `main`, and nothing
  on 23 of them.
- **Spawns.** 722 sites call a shell function through `$(...)` whose body starts no process, 290 of
  them in the driver. Three patterns can be banned outright; a `PS4` trace count gives a fork-count
  arm with no clock, so it cannot flake.

## The menu — units the owner selects from

Each line is one proposed unit. The estimate is on node `a` and is the research's, not measured.

| # | Unit | Saves (est.) | Risk | Needs the owner |
|---:|---|---|---|---|
| A1 | Fix the reuse key: content, not status line, of a dirty guarded file | correctness | low | — |
| A2 | Measure width 4, 6 and 8 quiet and loaded; derive width from a spawn calibration | 2-5 ks a bar, if it saturates near 4 | med | — |
| A3 | Retry a ceiling-killed leg in the drain tail; dispatch by declared ceiling with no ledger | ~3.3 ks + ~1.9 ks | low-med | — |
| A4 | The runner's own spawns: 45-65 per leg to ~6, one `rev-parse` per bar | ~1.3 ks + ~0.9 ks in the canary family | low-med | — |
| B1 | Run the self-test tier in WSL2 from an ext4 clone, verdicts combined, paired bars until they agree | most of the tier: hours to tens of minutes | med | yes: a Linux host for kit suites |
| B2 | The driver as a library: `load_driver_conf` and `main`, suites source it once per shard | ~1.9-8.1 ks pool | med | — |
| B3 | `check-unattended.sh --only core / N` and `check-memory-hygiene.sh --only N`, each naming what ran | ~4.3-6.5 ks + ~1.5 ks | med | — |
| B4 | Fork-free readers for the 722 function-call sites, a lint leg banning three patterns, a fork-count arm with a ceiling | ~2-4 ks pool, and it stops regrowth | low | — |
| B5 | Fixture templates and environment git identity across suites | 10-30 % of each small suite | low | — |
| B6 | `foreign-prefix parity` probes one shard per sharded suite and runs whole rows in the pool | ~2.4 ks | low | — |
| B7 | Per-suite levers: agent-cap property in one `node`, drift-audit per signal, hook destinations scratch once, `build_commit` memoised, `AI_AGENT` unset in manifest-check | ~4-5 ks pool together | low-med | — |
| C1 | Run a held suite only when its kit's shipped bytes or the suite moved | 87 % of held seconds over 30 commits | med | yes: what binds at the push |
| C2 | Reuse keyed on declared read classes, sampled for soundness; the impure legs keyed on the remote tip at push | ~25 ks against a green parent | high | yes: push-time reuse |
| D1 | A refusal retirement review, owner-decided batches, and a refusal growth budget | ~6-13 ks across the two suites | med | yes: each batch |
| D2 | Calibrate the remaining clock-bound arms on the flake list | removes load reds | low | — |

**Not a unit, and the largest single factor:** a Windows Defender exclusion for the repository, its
worktrees and `%TEMP%` on node `a`. It is a security setting and the owner's to make.

## The order, if all are taken

A1 first (it is a correctness fix). Then A2, because width decides how much A3 is worth and
longest-first dispatch alone packed the heaviest suites together in aMeteredSweep's second bar.
B4 and B2 before B3, so the gate's `--only` lands on a driver that is cheap to call. B1 runs in
parallel as its own track, paired bars first. C1, C2 and D1 wait on the owner's rulings.
