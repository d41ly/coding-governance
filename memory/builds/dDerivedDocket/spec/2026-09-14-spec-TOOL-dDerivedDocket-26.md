# TOOL-dDerivedDocket-26 — honest verdicts under contention

**Status:** SPECCED · rev-6 · 2026-09-20 · node d · Tier-2 · base fb07ca25 · streams tooling · order 26

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-build-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 TOOL-dDerivedDocket-37 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-review-TOOL-dDerivedDocket-21-spec-audit-g4-round1.md](../reviews/2026-09-14-review-TOOL-dDerivedDocket-21-spec-audit-g4-round1.md) | spec-audit | TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 |
| [2026-09-20-review-TOOL-dDerivedDocket-21-spec-audit-g4-round2.md](../reviews/2026-09-20-review-TOOL-dDerivedDocket-21-spec-audit-g4-round2.md) | spec-audit | TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 |

<!-- /gen:spec-records -->

## 1. Goal

A leg killed by its ceiling on a loaded host reports FAIL exactly as a real hang does, so a full bar
under its own concurrency is not reproducible on its ceiling kills (TOOL-aSurfacedLexicon-22 records
`pass-order history` killed at 5400 s under fleet load after a 267 s standalone run), and one push
to the default branch has proceeded with no bar run while the hook said it was forcing one
(TOOL-aSurfacedLexicon-25). This unit makes the runner retry, once and alone, a leg whose ceiling
fired, count a pass on that retry as green (D12-i6), name the neighbours beside every timeout,
print when it acquired the repository, say HOST when a calibrated measurement shows the host rather
than the subject is at fault, and never exit 0 without a verdict the push boundary can read. It
removes i70, i91 and i152's timeout half, and i97 together with the gate-wall unit (DR 21.4 U24).
It answers the timeout class only. TOOL-dSpentCeiling-8 records two ASSERTION reds on a saturated bar, the
`run-gates turnstile` TERM arm and the `row-keyed merge driver replay` nesting arm, and no timeout;
that row stays OPEN.

## 2. Scope (IN)

- **S1** — the serial retry. A leg whose ceiling FIRED is deferred rather than failed: rc 124 with a
  positive bound in its `.bound` file, or rc 137 under a positive bound whose `.sec` is at or above
  it, which is `timeout -k`'s kill after an ignored TERM. Every other rc 137 — a self-kill, an OOM
  kill, an operator's or a CI cancel, under a bound or with none — stays a FAIL with today's tail:
  `(killed after <s>s, ceiling <n>s)` under a positive bound, and `(killed after <s>s)` with a bound
  of 0 (`tools/run-gates/run-gates.sh:1494` and `:1499`). The red attribution unit reads CONTENDED
  by this same predicate. The reader prints
  `GATE retry  <leg>  (timed out after <n>s beside <k> neighbours; one serial retry after the pool
  drains)` in its manifest position. After the pool drains, and while the run's wall is still armed,
  each deferred leg runs once more alone under its own ceiling. A pass prints
  `GATE ok    <leg>  (retried after timeout)`; a second timeout prints
  `GATE FAIL  <leg>  (timed out after <n>s, again on its serial retry)`; any other failure prints its
  exit status the same way. Observed by AC1 and AC9.
- **S2** — the records. A chunk holding a deferred leg closes `pending`, never `green`, and one
  `---- retry: <verdict>  (<n> retried, <m> failed)` line follows the retries. The first attempt keeps
  its `<i>.leg` row with status `timeout`; the retry writes `<i>.retry.leg`. The verdict file gains
  `retried <n>`. The ledger row takes the retry's seconds and the status `retried`, which the reuse
  predicate (`tools/run-gates/run-gates.sh:1355`, `_st = ok`) never accepts, so a contended pass is
  never copied forward. Observed by AC1, AC2 and AC6.
- **S3** — the neighbour count. `measure_neighbours` counts the other legs whose run-record interval
  contains the timed-out leg's end time, plus legs still holding a `.pid` and no `.rc` when the reader
  reaches it. The figure rides the S1 tails. Observed by AC1.
- **S4** — the acquire line. Right after `gate queue: waited <n>s`
  (`tools/run-gates/run-gates.sh:977`) the runner prints `gate queue: acquired <iso-utc> from <state>`,
  where state is the existing `QUEUED_FROM` word, and writes the same pair into the run record
  header. Observed by AC3.
- **S5** — calibration and HOST. `measure_spawn_cost` times ten spawns of an external binary. Each
  bar reads the recorded floor, then measures once at start and folds that figure into the minimum
  kept in `<git-common-dir>/gate-spawn-floor`, written tmp-then-rename. A retry compares against the
  floor AS READ before this bar measured, so a bar never calibrates against itself and a clone's
  first bar has no floor (§8 F4). Before a deferred leg's retry, and again before the second
  spawn-cost measurement, the timed-out attempt's process tree must already be gone. WHICH mechanism
  buys that is F5, parked for the orchestrator, because three properties measured at HEAD rule out
  every mechanism this runner already carries, and the spec names none until that fork is resolved.
  First, `run_leg_reap` (`tools/run-gates/run-gates.sh:1001`) MAY NOT be rooted at the walker's own
  pid: `scan_descendants` seeds its accumulator with the ROOT (`out=$1`,
  `tools/run-gates/run-gates.sh:429`) and `remove_descendants` iterates that list and `kill -9`s the
  seed first (`:445-452`), so a `runleg` calling it on its own `$BASHPID`, the pid it records in
  `$WORK/<i>.pid` (`:1367`), would SIGKILL the worker before it writes `.sec` and `.rc`; the leg's
  completion signal would never appear and both of its readers would take the leg for one still
  running (`:1033`, `:1621`). Second, neither of that function's two arms survives a DEAD root, so
  it cannot simply be moved after the pool drains: `remove_descendants` walks `scan_descendants`
  over a `ps -ef` snapshot from the root and an exited root yields the seed alone (`:445-473`, whose
  own comment records that exact failure shape from TOOL-aQuenchedHarness-1), and the monitor arm
  resolves the msys pid through `tools/process-monitor/reap.py:311`, which REFUSES when the id
  resolves to no census row and kills nothing. Third, a ppid walk may not reach the residue from
  EITHER root: on the timeout path `timeout`'s own child is already dead, and the comment at
  `tools/run-gates/run-gates.sh:419-421` records that killing a parent REPARENTS its children off
  the chain about to be walked, so a surviving grandchild is no longer a ppid-descendant of the
  worker either. The monitor's orphan sweep is no route either: it flags by age against
  `PROCMON_AGE_CEILING`, 14400 seconds as this repository declares it, so a grandchild orphaned
  seconds ago grades `OK` (`tools/process-monitor/classify.py:38-48`). At BASE `runleg` writes `.rc`
  after a timeout without reaping at all. Whatever F5 settles, two things hold: the worker still
  writes `.sec` and `.rc` on the timeout path, and after the pool drains the runner VERIFIES rather
  than reaps: each deferred leg's recorded `<i>.pid` is dead, and any
  descendant `remove_descendants` still names is printed with its pid instead of being assumed gone.
  That is also why the two existing callers skip a leg holding an `.rc` (`:1033`, `:1621`) — the
  skip's precondition is that same dead root, not a judgement that the tree is clean. When a deferred leg times out again on its retry, the runner measures once more, and the
  leg is HOST when that figure exceeds `GATE_HOST_RATIO` times the floor. The ratio is a source
  constant of 4 (§8 F1). The bar exits 4, printing `gates HOST — <n> leg(s) timed out twice while a
  spawn cost <x>x this clone's floor; the verdict is about the host, not the subject`, only when
  every failed leg is HOST. A bar with any other failure stays RED and names its HOST legs. With no
  floor recorded, HOST is unavailable and the leg is FAIL with a note saying so. The run record's
  verdict reads `HOST` and no full-green stamp is written. Exit precedence, first match wins, stated
  here because this is the later of the two units that add runner exits: 2 REFUSED (S6); 1 RED, when
  any failed leg is not HOST, its RED line naming a moved tree and any HOST legs; 4 HOST, when every
  failed leg is HOST, its line naming the moved tree when `tree_moved yes`; 3 TREE MOVED, when no leg
  failed and the tree moved; 0 GREEN. The scratch-hygiene unit's 'a bar that failed AND moved stays
  RED' reads 'failed on a leg that is not HOST' from this unit on (§8 F3). Observed by AC4, AC10 and
  AC11.
- **S6** — no silent pass. The runner refuses exit 0 unless at least one leg line was reported and
  the run record's verdict file was written; otherwise it exits 2 as REFUSED, naming which half was
  missing. `.githooks/pre-push` pins `GATE_RUN_ID` to a fresh unpredictable id, removes any directory
  of that name first, and after an exit 0 requires `verdict GREEN` in that run's record. A missing or
  different verdict blocks the push as RED. With `GOV_GATE_CMD` set, the hook announces that the
  record check is skipped for an override command. Observed by AC5, AC12 and, for the pin and its
  pre-removal, AC15.
- **S7** — the drift signal. `tools/drift-audit/drift_report.py` gains `legs_retried_after_timeout`,
  the sum of `retried` over the run records it can read, report-only. Zero readable verdict files is
  a DEAD PROBE, never a reassuring 0. Observed by AC7.
- **S8** — carriers. `tools/run-gates/README.md` states exit 4, the exit precedence S5 fixes, the
  `GATE retry` tail and the `pending` chunk verdict. Observed by AC8. NOT OBSERVED for versions: this
  unit moves no version constant; drift-audit moves once in this build's landing range in
  `TOOL-dDerivedDocket-13` and run-gates in `TOOL-dDerivedDocket-1`, and this unit's bytes ride those
  moves — `kit version markers` grades only the final tree's agreement.
- **S9** — the kickoff manifest. `memory/guides/SESSION-KICKOFF.md`'s command-block line that a leg
  outliving its `ceiling` is killed 'RED naming the leg and the number' (`:134` at BASE) is
  rewritten: a leg whose ceiling fired gets one serial retry, a pass on it counts green and is
  counted in `retried`, and a bar whose only failures are HOST exits 4. `last-audit` is re-stamped in
  the same commit with a delta line, because `tools/run-gates/run-gates.sh` is in the manifest's
  `watch:` list. The rewrite LANDS NET ZERO on that carrier. The passage is the single command-block
  ceiling line at `memory/guides/SESSION-KICKOFF.md:134`, and its replacement is written no longer
  than the line it replaces. What will not fit in one line — the retry's own tail, the `pending`
  chunk verdict and where exit 4 sits in the precedence — goes to `tools/run-gates/README.md`,
  which S8 already has this unit writing and which owns the runner's exit codes. Observed by AC13
  and AC14.

## 3. Non-goals (OUT)

- **Attributing a timeout.** The red-attribution unit classifies a timed-out leg CONTENDED from the
  FIRST attempt's record; this unit does not read that verdict, and its retry records keep that
  first record intact (S2), which the edge below declares.
- **The root cause of TOOL-aSurfacedLexicon-25.** Reading the source at BASE finds no main-shell
  `exit 0` other than the green line and `--print-profile`, so the failing path is UNVERIFIED. S6 is
  the envelope that turns any such path into RED at the boundary, whatever it turns out to be.
- **The beacon reap race** of TOOL-aReapedTicket-4.
- **The driver's reaction to HOST and to a kill before `acquired`.** Both are the gate-wall unit's.
- **Retrying a leg more than once, or retrying a non-timeout failure.** One retry, timeouts only.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-25` — the TREE MOVED verdict and exit 3, which S6 must accept as a written verdict rather than a missing one, and whose precedence against exit 4 S5 states
- **consumes-from** `TOOL-dDerivedDocket-23` — the CONTENDED reading of a leg's first attempt record and the fired-ceiling predicate S1 shares with it; S2's `.retry` files must leave that record readable as written
- **hands-off** `TOOL-dDerivedDocket-27` — exit 4 and the `gate queue: acquired` line, which the driver's bound stack reads to choose a hold

## 4. Design

### Data model

```
stdout      GATE retry  <leg>  (timed out after <n>s beside <k> neighbours; ...)
            GATE ok    <leg>  (retried after timeout)
            ---- chunk <c>: pending  (...)
            ---- retry: <green|RED|HOST>  (<n> retried, <m> failed)
            gate queue: acquired <iso-utc> from <held|expired|unticketed|off|unresolved>
            gates HOST — ...                         # exit 4
<git-dir>/gate-run/<id>/verdict   gains  retried <n>  and the value HOST
<git-dir>/gate-run/<id>/header    gains  acquired <iso-utc> / acquired_from <state>
<git-common-dir>/gate-spawn-floor  one line: <per-spawn-ms><TAB><iso-utc measured>
```

Every new tail keeps the two-space tail contract (`tools/run-gates/run-gates.sh:1439-1445`), so
`read_gate_verdicts` in `tools/govkit/govkit.py` still splits the bare leg name. It ignores the
unknown `GATE retry` prefix and keeps the FIRST line per leg under each declared prefix
(`tools/govkit/govkit.py:3578`); a deferred leg prints exactly one `ok` or `FAIL` line, after its
retry, so that first line is the retry's verdict.

### The retry pass

The reader's walk is unchanged except for the deferral. After the terminal `wait`
(`tools/run-gates/run-gates.sh:1677`) and before `remove_wall_watcher`, a loop runs each deferred
leg through the existing `runleg` into fresh `.retry` files, one at a time. Keeping the wall armed
is the bound on the retry: a retry cannot extend the run past its declared wall. Each deferred leg's
first attempt is reaped before its retry starts.

### Calibration

The floor is per CLONE, because node `a` pays roughly 251 ms per process against node `d`'s 19-39 ms
(DR 21.7), so an absolute figure would call one node permanently degraded. The measurement at the
second timeout happens after the pool drained AND after the timed-out attempts' trees were reaped,
so the bar's own concurrency, grandchildren included, is gone and a high figure means another
tenant; the runner's own comment records a grandchild outliving `timeout` by 51 s on these nodes
(`:1376-1381`). That precondition is bought by the mechanism F5 settles, and S5 states the bounds
rather than the mechanism. Rooting a live-tree reap at the walker's own pid is REFUSED, because
`remove_descendants` kills its seed and would take the worker with it before `.sec` and `.rc` are
written. Moving `run_leg_reap` after the pool drains is refused too, because by then that pid has
exited and both of its arms die on a dead root — the walk returns its seed, the monitor refuses the
msys id — so a reap placed there would leave exactly the residue this paragraph asserts is gone, and
the bar would exit 4 as HOST over its own leftovers while calling them another tenant. Nor may the
mechanism assume a ppid chain: the timed-out child is already dead and its own children have been
reparented off it. What the post-drain step contributes is the ASSERTION: the recorded pid is dead and no descendant is still named. If either fails the
figure is not attributable and the runner says so, rather than reporting a ratio about a tree it
never cleared. `GATE_SPAWN_CMD` is a seam for the arm, naming the binary timed, exactly as
`GATE_RUN_ID` is seamed for an arm (`tools/run-gates/run-gates.sh:1081-1084`). `GATE_SPAWN_FLOOR` is
the second such seam, naming the floor file's PATH, and it exists so the two floor states §5
declares can be forced by staging rather than by permission bits: these are Git-Bash trees on
Windows, where mode bits are emulated over ACLs and a `chmod 000` on a file the caller owns is
frequently a no-op, which would run the ordinary path and leave AC4 green over a branch nothing
entered. Pointed at a path staged as a DIRECTORY the read fails on every filesystem; pointed at a
file whose sibling temp path is staged as a DIRECTORY the tmp-then-rename write fails with the old
line still in place.

### The boundary check

The hook owns the id it pins, so a verdict file the runner never wrote cannot be mistaken for one it
did: the directory is removed before the run, and the id carries `$$` and `$RANDOM`.

### Inventory

`measure_neighbours`, `measure_spawn_cost`, `run_leg_retry`, `check_verdict_record` (hook) in
`sh.function`; `measure_legs_retried_after_timeout` in `py.function`. `GATE_SPAWN_CMD` is an arm
seam, and `GATE_HOST_RATIO` is a source constant, not a conf key. `GATE_SPAWN_FLOOR`, which
Calibration above introduces, is a SECOND arm seam and not a conf key either: it names the floor
file's path so AC4 can stage the two floor states §5 declares without permission bits.
Beside `GATE_SPAWN_CMD`, a
verdict-write arm seam that forces the verdict-file write to fail, spelled as the runner's existing
arm seams are (`GATE_` plus a noun), named at build time, and marked an arm seam, not a conf key,
exactly as `GATE_SPAWN_CMD` is.

### Files touched (estimate)

`tools/run-gates/run-gates.sh`, `tools/run-gates/run-gates.test.sh`, `tools/run-gates/README.md`,
`.githooks/pre-push`, `.githooks/pre-push.test.sh`, `tools/drift-audit/drift_report.py`,
`tools/drift-audit/selftest.py`, `memory/guides/SESSION-KICKOFF.md`, and
`memory/map/generated/symbols.json`, regenerated and staged in the commit that adds
`measure_legs_retried_after_timeout`, because the pre-commit codebase-map leg refuses a staged
`.py` whose map is stale or whose regenerated artifacts are unstaged.

### Alternatives rejected

- **A declared timing budget the arm refuses against** (TOOL-dSpentCeiling-8's second candidate).
  It needs a per-arm budget in every suite, and it is not this unit's mechanism: the serial retry
  reaches a ceiling kill and does not reach an arm's own assertion failure, which is what that row
  records, so the row keeps this candidate open for its owner.
- **A wall-clock threshold for HOST.** Rejected by DR: a wall clock on an AV-fronted node is not
  measurable to better than a factor of two (`memory/gotchas/process-creation-is-the-suite-cost.md`),
  so only a ratio against the same clone's own floor can discriminate.
- **Parsing the runner's stdout at the hook.** Rejected: a pipe waits for the last inherited write
  end, and the wall watcher's `sleep` can outlive the runner holding it
  (`memory/gotchas/bounded-through-a-pipe-is-unbounded.md`). The run record is a file the runner
  already writes last.

## 5. Production-readiness checklist

- **security** — the hook's pinned id is removed before use, so a planted record cannot satisfy it;
  AC15 stages that break, and names the half of it no arm can reach. The floor file is under the git
  common dir, which this runner already writes, and AC4 reads what it holds after a bar.
- **perf / scale** — ten spawns per bar, about 0.4 s on node `d` and 2.5 s on node `a`, plus one
  retry per timed-out leg. A bar with no timeout pays only the ten spawns.
- **error / empty / loading states** — an unreadable floor is treated as absent and announced; an
  unwritable one leaves the old floor in force.
- **observability** — the retry tails, the neighbour count, the acquire line, `retried <n>` and the
  drift signal.
- **risks** — a real hang now costs one extra ceiling of wall clock, bounded by the run's wall. A
  host that is slow on every bar grows a high floor and never reads HOST; that is the stated price
  of a per-clone ratio.
- **testing** — arms in `tools/run-gates/run-gates.test.sh` for S1 to S6, in
  `.githooks/pre-push.test.sh` for the hook half of S6, and in `tools/drift-audit/selftest.py` for
  S7, each break staged and seen red.
- **migration** — none; an absent floor file is the first-run state.
- **user docs** — `tools/run-gates/README.md`.

## 6. Acceptance criteria

- **AC1** — When a fixture leg times out only while a sibling spinner leg is alive, the bar prints
  `GATE retry  ` for it, then `GATE ok    ` with `(retried after timeout)`, and exits 0 with
  `retried 1` in the run record; a fixture leg that hangs alone ends `GATE FAIL  ` after its retry,
  with the neighbour count in both tails: `beside 1 neighbours` for the contended leg and
  `beside 0 neighbours` for the lone hang. The arms live in `tools/run-gates/run-gates.test.sh`.
  Red when: the retry is removed, and the contended leg reads FAIL on its first timeout; or
  `measure_neighbours` prints a constant, which both fixtures accept unless the two counts are pinned.
  permission: the canary is held, so it runs at the build's one post-build bar, spelled
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain bar.
- **AC2** — When a chunk holds a deferred leg, its chunk line reads `pending` and the `---- retry:`
  line carries the final verdict. Red when: the chunk closes `green` before its retry has run.
  permission: the canary is held, so it runs at the build's one post-build bar, spelled
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain bar.
- **AC3** — When a fixture bar queues behind a planted live holder and then acquires, stdout carries
  `gate queue: acquired ` after `gate queue: waited ` and the run record header carries the same
  timestamp. Red when: the line is printed before the wait ends, or not at all.
  permission: the canary is held, so it runs at the build's one post-build bar, spelled
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain bar.
- **AC4** — With a planted floor of 1 ms and `GATE_SPAWN_CMD` seamed to cost 50 ms, a leg that times
  out twice ends HOST and `bash tools/run-gates/run-gates.sh` exits 4; with no floor file the same leg
  ends `GATE FAIL  ` naming the missing calibration. The WRITER is read directly, because no other
  criterion of this unit reads `gate-spawn-floor` at all: after a fixture bar runs in a scratch clone
  holding NO floor file, `<git-common-dir>/gate-spawn-floor` exists and holds exactly one
  `<per-spawn-ms><TAB><iso-utc>` line; after a second bar whose seamed spawn is CHEAPER the figure
  falls to that new minimum, and after a third whose seamed spawn is DEARER it does not rise; with
  `GATE_SPAWN_FLOOR` pointed at a path staged as a DIRECTORY the bar announces the floor unreadable
  and treats it as absent; and with `GATE_SPAWN_FLOOR` pointed at a file holding a known line whose
  sibling temp path is staged as a DIRECTORY, so the tmp-then-rename writer cannot open its temp,
  the bar announces and that line survives byte-identical. Both floor states are staged through that
  seam and a directory, never through `chmod`, for the reason §4 states: on these Git-Bash trees a
  `chmod 000` on a file the caller owns is frequently a no-op, and an arm staged that way runs the
  ordinary path and passes.
  Red when: HOST is granted without a recorded
  floor — this bar's own start measurement taken as its calibration, which ends the arm FAIL with a
  ratio and no missing-calibration note, or an absent floor read as zero, which ends it HOST — the
  break DR 21.4 U24 names. Red too when the tmp-then-rename writer is omitted ENTIRELY, which the
  HOST clauses alone cannot see: with `GATE_SPAWN_CMD` seamed to 50 ms the start measurement folds to
  min(1, 50) = 1 against the planted floor, and F4's rule that a retry compares against the floor AS
  READ leaves the no-floor arm ending FAIL whether or not anything was written — so on a real clone
  the file would never appear, HOST would be permanently unavailable, and every double timeout would
  print `GATE FAIL` naming a calibration that never arrives, the whole host-attribution mechanism
  dead behind a full green. §5's two floor states are the last two clauses above. Red too when
  either of those two is staged with `chmod` instead of the seam on a tree where the owner's own
  mode bits do not deny, so the arm takes the readable and writable path and a green row covers a
  branch nothing entered.
  permission: the canary is held, so it runs at the build's one post-build bar, spelled
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain bar.
- **AC5** — When a planted beacon names a dead pid, the bar still prints a verdict line and writes a
  verdict file; and in `.githooks/pre-push.test.sh` a fake runner that exits 0 writing no record gets
  its push blocked. Red when: the hook trusts the exit status alone, the TOOL-aSurfacedLexicon-25
  path.
  permission: the canary and the hook suite are held, so they run at the build's one post-build
  bar, spelled `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain bar.
- **AC6** — When a scoped run with `GATE_REUSE=1` meets a leg whose ledger row reads `retried`, it
  runs the leg. Red when: `retried` is accepted as `ok` by the reuse predicate.
  permission: the canary is held, so it runs at the build's one post-build bar, spelled
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain bar.
- **AC7** — When `python tools/drift-audit/drift_report.py` runs over a fixture git dir holding two
  verdict files with `retried 1`, it reports 2 for `legs_retried_after_timeout`, and it prints DEAD
  PROBE over a git dir holding none. Red when: an unreadable population reports 0.
  permission: the arm lives in `tools/drift-audit/selftest.py`, a held kit leg, so it runs at
  the build's one post-build bar, spelled `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`,
  never a plain bar.
- **AC8** — When `tools/run-gates/README.md` is read after this unit, its exit-code section lists
  exit 4 and the precedence of exits 1, 3 and 4, and it names the `GATE retry` tail and the `pending`
  chunk verdict.
  Red when: the README's exit codes stop at 3, so a caller reading them treats HOST as a red leg.
- **AC9** — When a fixture leg SIGKILLs itself about 2 s into a 600 s ceiling, the bar prints no
  `GATE retry` line for it and ends it `GATE FAIL` with its `killed after` tail and no `timed out`
  text; the `4h` and `stubborn` arms pass pinning the new retry tails; and the `4h-nobound` arm, the
  same self-kill with no ceiling declared, passes unedited.
  Red when: every rc 137 with a positive bound is deferred, so a self-killed or OOM-killed leg is
  retried, printed as timed out, and counted green when its retry passes; or an rc 137 with a bound
  of 0 is deferred because its `.sec` is at or above that zero, so the `4h-nobound` arm reads a
  `GATE retry` line where it pins `(killed after <s>s)`.
  permission: the canary is held, so it runs at the build's one post-build bar, spelled
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain bar.
- **AC10** — With a planted floor of 1 ms and `GATE_SPAWN_CMD` seamed to 50 ms, when a fixture
  bar's only failed leg times out twice while another leg edits a tracked file mid-bar,
  `bash tools/run-gates/run-gates.sh` exits 4 and its `gates HOST` line names the moved tree; with a
  third leg failing an assertion too, it exits 1 and its RED line names the move and the HOST leg.
  Red when: the exits are ranked by whichever check runs last, so one bar exits 1 under one unit's
  rule and 4 under the other's, and the driver blames the subject or holds by accident.
  permission: the canary is held, so it runs at the build's one post-build bar, spelled
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain bar.
- **AC11** — When a fixture leg's timed-out attempt leaves a grandchild that keeps spawning and has
  written its pid to a file, that pid is dead when the leg's serial retry starts, as
  `tools/run-gates/run-gates.test.sh` observes; and a second arm of that suite runs `run_leg_reap`
  against a root pid that has ALREADY exited, leaving the same grandchild ALIVE, which is the
  measurement that rules out placing the reap after the pool drains; and a third arm asserts that
  the WORKER SURVIVES whatever mechanism F5 settles — a fixture leg that times out still writes its
  `.sec` and its `.rc`, and the pool reports that leg's verdict rather than leaving it outstanding.
  Red when: the reap is removed, so the attempt's own descendants run through the retry and the
  spawn measurement, and a bar exits 4 as HOST over its own leftovers — which the gate-wall unit holds
  as host-degraded and auto-resume re-enters; or the reap is rooted at the recorded `<i>.pid` after
  that subshell has exited, which reaches nothing while reading correct at its call site, and which
  the second arm is staged RED to demonstrate before the first arm can mean anything; or the reap is
  rooted at the WALKER's own pid, so `remove_descendants` kills its seed, the worker dies before
  `.rc` is written, and the outstanding-leg reaper and the wall watcher both read that leg as still
  running — which the third arm is staged RED to demonstrate.
  permission: the canary is held, so it runs at the build's one post-build bar, spelled
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain bar.
- **AC12** — When `bash tools/run-gates/run-gates.sh` runs over an empty fixture manifest, it exits 2
  printing `REFUSED` and naming the missing leg lines; when the verdict-file write is forced to fail
  through the unit's arm seam, it exits 2 naming the verdict file. Each is staged RED by removing its
  guard.
  Red when: the runner reaches its green branch with no leg line or no verdict file and exits 0,
  the zero-verdict pass §9 names, which AC5's dead-pid beacon arm never reaches.
  permission: the canary is held, so it runs at the build's one post-build bar, spelled
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain bar.
- **AC13** — When `bash skills/session-kickoff/manifest-check.sh` runs on the unit's commit, check 5
  passes with the re-stamped `last-audit`, and the §B ceiling line names the serial retry and exit 4.
  Red when: the stamp moves and the line still says a leg that outlives its ceiling is killed RED,
  so the front-loaded trap describes the BASE runner under a fresh stamp.
  permission: the command is the `kickoff-manifest ratchet` leg; it runs at the build's one
  post-build bar.
- **AC14** — When `wc -c < memory/guides/SESSION-KICKOFF.md` is read at this unit's commit and at
  its parent, the reading at this unit's commit is NO LARGER than the reading at the parent.
  Red when: S9's replacement runs to a second line, so a carrier other units of this build write too
  grows on a unit that priced itself at nothing. The detail that does not fit that one line has
  AC8 for its landing in `tools/run-gates/README.md`, so the two criteria together are the whole
  route and neither alone is. The cap half is red by the `memory hygiene` leg's index-cap check;
  the NET delta against the parent is the half no leg reads, which is why this criterion reads
  it.
  permission: the reading is `wc -c` over a tracked file in the pass. NO CAP IS RAISED by this
  unit: moving the 61440 is an owner turn.
- **AC15** — When `.githooks/pre-push.test.sh` exports `GATE_RUN_ID` naming a directory it has
  pre-planted under `<git-dir>/gate-run/` carrying `verdict GREEN`, and the stubbed runner writes
  nothing, the push is still BLOCKED, because the hook pins its OWN id and never honours an inherited
  one; and across two consecutive hook runs the stubbed runner records two DIFFERENT ids.
  Red when: the hook pins a fixed or derivable id, or honours the caller's, so a leftover or planted
  `gate-run/<id>/verdict` satisfies the boundary check for a push whose runner wrote nothing — the
  TOOL-aSurfacedLexicon-25 shape this unit exists to close, and the reason §5 states the pin's
  security property outright. AC5 cannot see it, because its scratch repo holds no planted directory
  and the fake runner's push is blocked there whether the pin exists or not, and AC12 grades the
  runner half.
  ungraded half, named rather than implied away: the pre-removal of a directory already carrying the
  hook's freshly computed id. An id carrying `$$` and `$RANDOM` cannot be predicted by an arm, and
  seaming it to make it predictable would install the very lever this criterion denies a caller, so
  the removal stays a belt-and-braces write that S6 specifies and no arm grades.
  permission: the hook suite is held, so it runs at the build's one post-build bar, spelled
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, never a plain bar.

## 7. Gates

`run-gates canary` · `pre-push self-test` · `drift-audit selftest` · `drift-audit records` · `kit version markers` · `kickoff-manifest ratchet` · `codebase-map coverage + freshness` · `memory hygiene`

Existing arms whose pinned tails S1 changes: `4h` (`tools/run-gates/run-gates.test.sh:1149`, pinning
`(timed out after 3s)$`) and `stubborn` (`:1166-1176`) gain the serial-retry tail; `4h-kill`
(`:1179-1210`) stays unedited and is the staged-RED arm for the fired-ceiling predicate, and
`4h-nobound` (`:1216-1244`), which pins the bound-0 kill tail, stays unedited beside it.

New arm: tools/run-gates/run-gates.test.sh · a leg that times out only beside a spinner · the canary's executed-assertion floor
New arm: tools/run-gates/run-gates.test.sh · a seamed spawn cost against a planted floor, and the floor file read after a bar with none, after a cheaper measurement, after a dearer one, unreadable and unwritable · the canary's executed-assertion floor
New arm: tools/run-gates/run-gates.test.sh · a reap rooted at a pid that has already exited, beside the same reap rooted at a live one · the canary's executed-assertion floor
New arm: .githooks/pre-push.test.sh · a fake runner exiting 0 with no record, and an inherited GATE_RUN_ID naming a pre-planted GREEN record · none

## 8. Open questions

- **F1** — The HOST ratio's value, which DR fixes only as "a ratio, never a wall clock". Options: 2,
  4, 10. 2 sits inside the measured 2x single-node spread (0.019-0.039 s per spawn, per the gotcha
  cited in §4) and would call ordinary noise HOST; 10 would miss the 25x-under-contention reading
  recorded at `tools/run-gates/run-gates.sh:852` only if a co-tenant were milder than the bar's own
  load. 4 is twice the measured noise band. PINNED 2026-09-14 from that one figure; the HOST line
  prints the measured ratio every time, which is what re-derives it. RESOLVED (agent, 2026-09-14,
  delegated): 4, the only value derived from a recorded measurement rather than chosen.
- **F2** — Where the silent-pass envelope binds. Options: (a) the runner alone; (b) the hook alone;
  (c) both. (a) cannot catch a path that exits 0 before the runner's own guard runs, and (b) leaves
  every non-hook caller unguarded. RESOLVED (agent, 2026-09-14, delegated): (c), the most
  feature-rich option, since S6 names both halves.
- **F3 — which exit does a bar take when every failed leg is HOST and the tree moved?** Options:
  (a) 4, its HOST line naming the move; (b) 3, TREE MOVED; (c) 1, RED. (c) blames the subject for a
  fault S5 attributes to the host; (b) re-runs at once on a host already measured degraded, and a
  concurrent session that keeps moving the tree then ends the item UNMET with no hold to resume from.
  RESOLVED (agent, 2026-09-14, delegated): (a); the hold waits on `probe host`, the resumed bar
  re-runs on the current tree, and the line names the move.
- **F4 — does a retry's calibration include this bar's own start measurement?** Options: (a) yes,
  the floor is the minimum including it; (b) no, the floor is the one recorded before this bar
  measured. (a) leaves AC4's no-floor arm unable to fail as written and calibrates a bar against a
  host it may have started on loaded. RESOLVED (agent, 2026-09-14, delegated): (b); a clone's first
  bar cannot read HOST.
- **F5 — what reaps a timed-out attempt's residue before the retry and the second spawn
  measurement?** Options: (a) background `timeout` inside `runleg`, record ITS pid and reap from
  there, so the seed `remove_descendants` kills is the leg command rather than the worker; (b) a
  seed-EXCLUDING walk beside `remove_descendants`, called from `runleg` on its own pid, which keeps
  the worker alive but still walks a ppid chain; (c) keep the step after the drain and make it the
  process monitor's SCOPE walk, keyed on the recorded `<i>.pid` and a run id rather than on a live
  ppid chain. None is free. (a) and (b) both assume the residue is still a ppid-descendant of the
  root they walk, which the reparenting recorded at `tools/run-gates/run-gates.sh:419-421` does not
  guarantee on the timeout path, where `timeout`'s own child is already dead. (c) is the only option
  that survives reparenting and the only one needing new surface:
  `tools/process-monitor/reap.py:311` REFUSES a dead msys id today, so it would need a
  by-recorded-root entry point. What is already settled, and is not part of this fork, is what may
  NOT be done: rooting a live-tree reap at the walker's own pid, because `scan_descendants` seeds
  its accumulator with the root and `remove_descendants` kills that seed first, so the worker dies
  before `.sec` and `.rc`. PARKED for the orchestrator. S5 and §4 state the bounds and name no
  mechanism; AC11's third arm holds whichever option is chosen to the worker's survival.

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft from DR 21.4 U24 and D12-i6. DR's "0 legs selected" exit-0
  form is not added: at BASE a guard-skipped leg already prints its own `GATE skip` line, which is a
  leg verdict, so the only zero-verdict case left is an empty manifest, and S6 refuses it.
- rev-2 · 2026-09-14 · folds the round-1 spec audit (G4 H3, H8, M6, M9, M16, M21, M22, L3, L4, L7;
  G1 M11). H3: S1 defers only a fired ceiling, per DR 21.4 U24, and §7 names the `4h`, `stubborn`
  and `4h-kill` arms (AC9). H8: §1 and §4 say the unit answers the timeout class, and
  TOOL-dSpentCeiling-8, whose reds are assertions, stays OPEN; DR's "Closes" line for U24
  over-claims (`…-design.md:2021`). M6: S5 states exit precedence 2, 1, 4, 3, 0 (F3, AC10). M9: S5
  reaps the timed-out tree before the retry and the second measurement (AC11). M21: a bar never
  calibrates against itself (F4, AC4's Red when). M22, L4: the runner refusals and the neighbour
  counts are staged (AC12, AC1). L3 with G1 M11: S8's versions are pointers to units 21 and 1, and
  `tools/drift-audit/kit.toml` leaves Files touched (AC8 reads the README). L7: S9 rewrites the
  kickoff ceiling line and re-stamps it (AC13). M16: consumes-from unit 23 for the CONTENDED seam.
- rev-3 · 2026-09-16 · spec-audit round 2 fold, third pass. S8, from fold verifier problem f3 on
  kit-version ownership, decided by the orchestrator as the unit first in build order to change a
  kit's shipped bytes owning that kit's one version move: S8's version pointer names unit 13, whose
  S11 makes the drift-audit move, in place of unit 21; run-gates stays unit 1's, and S8's version
  clause stays NOT OBSERVED here.
- rev-4 · 2026-09-16 · regrounded on fb07ca25 (origin/main). TOOL-aRatifiedRulings-4 gave
  `report_one` a `(killed after <s>s)` tail for an rc 137 with no bound in play and the canary a
  `4h-nobound` arm pinning it. §2 S1 therefore reads the rc-137 half of the fired-ceiling predicate
  as "under a positive bound", as unit 23 §4 rule 2 now does, and names both of today's kill tails;
  §6 AC9 adds that arm passing unedited and a `Red when:` for a deferred bound-0 kill; §7 names it.
  Line citations re-read at fb07ca25: S5's wall-watcher skip is `:1621`, §4's terminal `wait` is
  `run-gates.sh:1677`, §7's `4h` pinned line moved five lines down while the `stubborn` and
  `4h-kill` arms moved four, and S9's kickoff ceiling line is `:134`. §4 no longer says `read_gate_verdicts` takes a leg's final line:
  it keeps the first per prefix, which is the retry's because a deferred leg prints one. Files
  touched gains `memory/map/generated/symbols.json`, which dUnstagedSymbol's pre-commit leg refuses
  stale or unstaged when a `.py` is staged; §7 gains that pre-commit leg's own name,
  `codebase-map coverage + freshness`, for the same reason. §7's two canary `New arm:` lines
  name the executed-assertion floor they raise instead of `none`, a floor
  TOOL-aRatifiedRulings-4 moved in the window.
  §10's BASE paragraph describes fb07ca25. No S-item landed on main.
  Extended 2026-09-20, same base, by the build-wide consolidation pass. AC2 to AC7 and AC13 gain
  the `permission:` line AC1 and AC9 to AC12 already carried, so every criterion whose
  observation is a held suite or a merge-bar leg command places that run at the build's one
  post-build bar; AC8 reads a README and AC13's command is the `kickoff-manifest ratchet` leg's
  own argv. That folds the CONSERVATIVE reading of BUILD-METHOD M6 and
  `tools/unattended/gate-guard.js`; the ruling conflict behind it is parked for the owner in
  this build's `RUN.md` and is not decided here. §7's three `New arm:` third fields were re-read
  against each named suite and stand: neither the canary nor `.githooks/pre-push.test.sh` is one
  of the two suites that pin an executed-assertion floor under the build-wide arm-line rule. The
  one capped carrier this unit writes is `memory/guides/SESSION-KICKOFF.md`, 20057 bytes against
  the 61440 its class declares.
  Extended again 2026-09-20, same base, by the closing consolidation pass, which applied the
  build's NET-ZERO rule to every capped carrier rather than only to the contested ones. §2 S9 now
  NAMES the passage it rewrites, the command-block ceiling line at
  `memory/guides/SESSION-KICKOFF.md:134`, and the document the detail that will not fit moves to,
  `tools/run-gates/README.md`; new §6 AC14 reads the carrier at this unit's commit against its
  PARENT and reds any growth. Naming the line is what lets the orchestrator see that no sibling
  unit rewrites the same one: inside this closing set the passages taken are the §B `TMPDIR`
  trap, this ceiling line, the §B M6 claim and the `last-audit:` stamp, and specs outside the set
  write the same file, so the join across the whole build is the orchestrator's and no count of it
  is typed here. The header date moves to the
  last-change date; the rev does not, because the unit's scope did not move.
  Closed 2026-09-20, same base, by the last consolidation pass before the spec audits re-run.
  Every `permission:` line naming a HELD leg now spells the VERIFYING run
  `GATE_FULL=1 GATE_SELFTESTS=1 bash tools/run-gates/run-gates.sh`, so the canary, the hook suite and
  `tools/drift-audit/selftest.py` cannot be read as covered by a plain bar. Two rulings reached
  this spec and changed nothing in it. §2 S9 REWRITES a real §B passage, the command-block ceiling
  line, rather than merely re-stamping `last-audit:`, so it is a genuine replacement and not the
  bookkeeping stamp the orchestrator ruled is neither a trim nor a collision. And the scoped
  net-zero rule binds a carrier with less than 2048 bytes free, while
  `memory/guides/SESSION-KICKOFF.md` has 41383 of its 61440 free, so AC14's no-larger reading is
  stricter than the rule requires and is kept because it grades what §2 S9 promises. Rule 1's
  narrow reading moved nothing: AC13 runs `manifest-check.sh` over the real tree and keeps
  deferring, and every other observation is a suite file invocation. The header date stays at the
  last-change date; the rev does not move.
- rev-5 · 2026-09-20 · spec-audit round 3 fold, G4 round 2 · §4 §5 §7 · S5 S6 · AC4 AC11 AC15. H2:
  S5 reaped the timed-out attempt with `run_leg_reap` after the pool drained, at which point the
  attempt's subshell has written `.rc` and exited, and BOTH of that function's arms die on a dead
  root — `remove_descendants` walks from the root over a `ps -ef` snapshot and an exited root yields
  the seed alone, and the monitor arm's `--kill-msys` refuses an msys id that resolves to no census
  row. The monitor's orphan sweep is no substitute either: it grades by age against a 14400-second
  ceiling, so a grandchild orphaned seconds ago reads `OK`. S5 now roots the reap inside `runleg` on
  the timeout path, where the subshell is still alive, and the post-drain step becomes an ASSERTION
  that the recorded `<i>.pid` is dead with any surviving descendant named; §4 Calibration says why
  its precondition cannot be bought after the drain, and AC11 gains the dead-root arm that
  demonstrates it, staged RED. M1: S5's tmp-then-rename writer claimed AC4, AC10 and AC11 and none of
  the three ever READ `gate-spawn-floor` — with the spawn seamed to 50 ms against a planted 1 ms the
  start measurement folds to the planted figure and leaves no trace — so an implementation omitting
  the writer passed all three while HOST stayed permanently unavailable on a real clone. AC4 now
  reads the file itself after a bar with no floor, after a cheaper measurement, after a dearer one,
  unreadable and unwritable, which is also where §5's two floor states are observed. M2: the hook's
  `GATE_RUN_ID` pin and its pre-removal appeared in S6, §4 and §10 and in no criterion, while §5
  stated the security property they buy; new AC15 stages the break an inherited id makes and names
  the one half no arm can reach without installing the lever it denies. §7 gains the dead-root arm
  and extends the spawn-floor and hook rows. No carrier accounting moved.
- rev-6 · 2026-09-20 · §4 · §8 · S5 · AC4 AC11 · the round-3 fold's verifier, repairing the H2 fold
  above and hardening AC4's two new floor clauses. The H2 fold replaced an unreachable reap with one
  that kills the leg worker: `scan_descendants` seeds its accumulator with the ROOT
  (`tools/run-gates/run-gates.sh:429`) and `remove_descendants` iterates that list and `kill -9`s
  the seed first (`:445-452`), so `runleg` calling `run_leg_reap` on its own `$BASHPID` would
  SIGKILL the worker before `.sec` and `.rc`, the completion signal would never appear, and both of
  its readers would take the leg for one still running (`:1033`, `:1621`). A second doubt rides
  behind it and is recorded rather than measured: on the timeout path `timeout`'s own child is
  already dead, so a surviving grandchild has been reparented off the chain either root would walk
  (`:419-421`). S5 and §4 therefore state the BOUNDS and name no mechanism, and the choice becomes
  new fork F5 with three candidates for the orchestrator — a backgrounded `timeout` whose pid is the
  seed, a seed-excluding walk, or the process monitor's scope walk keyed on the recorded pid and a
  run id, the only one that survives reparenting and the only one needing new surface, since
  `tools/process-monitor/reap.py:311` refuses a dead msys id. AC11 gains a THIRD arm holding
  whichever option is chosen to the property this fold broke: the worker survives the reap and still
  writes `.sec` and `.rc`. Separately, AC4's two new floor clauses were staged with `chmod`, which on
  these Git-Bash trees frequently does not deny the owner and would have run the ordinary path and
  passed over an unexercised branch. Both are now forced through a new `GATE_SPAWN_FLOOR` seam
  beside `GATE_SPAWN_CMD` and a staged DIRECTORY — at the floor path for the read failure, at the
  writer's sibling temp path for the write failure — which needs no permission bits at all, and
  AC4's `Red when:` names the `chmod` staging as its own break. No carrier accounting moved, §7 does
  not move, and no criterion's other assertions changed.
  Verified in the same round and corrected in place, at no further rev bump: §4's Inventory named
  `GATE_SPAWN_CMD` and the verdict-write seam and not the third seam this pass added, so
  `GATE_SPAWN_FLOOR` now sits beside them, marked an arm seam and not a conf key.

## 10. Reuse audit

- **Probe result.** `python tools/codebase-map/reuse_lookup.py "retry a timed out gate leg once
  serially and report host degradation"` named `read_gate_verdicts` (`tools/govkit/govkit.py`), the
  consumer whose line-prefix parse the new tails must keep working, and no seam for the runner
  itself: `.sh` is an unscanned layer in its header. Reading source found the seams this unit
  extends: `runleg` and `report_one` for the retry, `input_key` and the `.leg` rows for the records,
  `GATE_RUN_ID` (`tools/run-gates/run-gates.sh:1084`) for the hook's pinned id, and `drift_report.py`'s
  `SIGNALS` list for S7.
- **DR against BASE fb07ca25.** DR places the acquire line as the queue-status replacement for the
  refuted TOOL-aUnblockedFleet-6; BASE agrees that `gate-queue-status` is deleted before a bar can be
  killed (`tools/run-gates/run-gates.sh:925`), which is why the line is on stdout and in the run
  record. Between `abac6d59` and fb07ca25 the runner moved only in its version pair and in
  `report_one`, which gained the bound-0 kill tail and pushed the lines below it down by up to six; the queue,
  `runleg`, `run_leg_reap`, the reuse predicate, `GATE_RUN_ID` and the main-shell `exit 0` sites
  §3 reads did not move. `.githooks/pre-push`, `drift_report.py` and `read_gate_verdicts` did not
  change, and the canary's timeout arms moved down four lines, its `4h` pinned assertion five, and
  the suite gained `4h-nobound`.
- **Rejected candidates** are in §4.
- Recall terms used: `python tools/memory-recall/query.py "how should a leg killed by its ceiling
  under load be retried and distinguished from a real failure" --terms "ceiling timeout retry serial
  contention nondeterministic HOST calibration spawn verdict no-silent-pass pre-push dead-holder"`.
  Top hits: TOOL-dRetiredFork-30 and TOOL-dRetiredFork-40 on ceilings in seconds,
  TOOL-aGradedMandate-12 on idle-node ceilings under fleet load, TOOL-aSurfacedLexicon-22 and -25,
  and TOOL-aReapedSpinner-16.
