# TOOL-dDerivedDocket-26 — honest verdicts under contention

**Status:** SPECCED · rev-1 · 2026-09-14 · node d · Tier-2 · base abac6d59 · streams tooling · order 26

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-14-build-TOOL-dDerivedDocket-1-design.md](../build/2026-09-14-build-TOOL-dDerivedDocket-1-design.md) | research | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |
| [2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md](../prompts/2026-09-14-prompt-TOOL-dDerivedDocket-1-spec-brief.md) | journal | TOOL-dDerivedDocket-1 TOOL-dDerivedDocket-2 TOOL-dDerivedDocket-3 TOOL-dDerivedDocket-4 TOOL-dDerivedDocket-5 TOOL-dDerivedDocket-6 TOOL-dDerivedDocket-7 TOOL-dDerivedDocket-8 TOOL-dDerivedDocket-9 TOOL-dDerivedDocket-10 TOOL-dDerivedDocket-11 TOOL-dDerivedDocket-12 TOOL-dDerivedDocket-13 TOOL-dDerivedDocket-14 TOOL-dDerivedDocket-15 TOOL-dDerivedDocket-16 TOOL-dDerivedDocket-17 TOOL-dDerivedDocket-18 TOOL-dDerivedDocket-19 TOOL-dDerivedDocket-20 TOOL-dDerivedDocket-21 TOOL-dDerivedDocket-22 TOOL-dDerivedDocket-23 TOOL-dDerivedDocket-24 TOOL-dDerivedDocket-25 TOOL-dDerivedDocket-27 TOOL-dDerivedDocket-28 TOOL-dDerivedDocket-29 TOOL-dDerivedDocket-30 TOOL-dDerivedDocket-31 TOOL-dDerivedDocket-32 TOOL-dDerivedDocket-33 TOOL-dDerivedDocket-34 TOOL-dDerivedDocket-35 TOOL-dDerivedDocket-36 PLAY-dDerivedDocket-1 DEPL-dDerivedDocket-1 |

<!-- /gen:spec-records -->

## 1. Goal

A leg killed by its ceiling on a loaded host reports FAIL exactly as a real hang does, so a full bar
under its own concurrency is not reproducible (TOOL-dSpentCeiling-8), and one push to the default
branch has proceeded with no bar run while the hook said it was forcing one (TOOL-aSurfacedLexicon-25).
This unit makes the runner retry a timed-out leg once, alone, count a pass on that retry as green
(D12-i6), name the neighbours beside every timeout, print when it acquired the repository, say HOST
when a calibrated measurement shows the host rather than the subject is at fault, and never exit 0
without a verdict the push boundary can read. It removes i70, i91 and i152's timeout half, and i97
together with the gate-wall unit (DR 21.4 U24).

## 2. Scope (IN)

- **S1** — the serial retry. A leg that ends with status 124 or 137 while its recorded ceiling is
  above zero is deferred rather than failed. The reader prints
  `GATE retry  <leg>  (timed out after <n>s beside <k> neighbours; one serial retry after the pool
  drains)` in its manifest position. After the pool drains, and while the run's wall is still armed,
  each deferred leg runs once more alone under its own ceiling. A pass prints
  `GATE ok    <leg>  (retried after timeout)`; a second timeout prints
  `GATE FAIL  <leg>  (timed out after <n>s, again on its serial retry)`; any other failure prints its
  exit status the same way. Observed by AC1.
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
  bar measures once at start and keeps the minimum ever seen in `<git-common-dir>/gate-spawn-floor`,
  written tmp-then-rename. When a deferred leg times out again on its retry, the runner measures
  once more, and the leg is HOST when that figure exceeds `GATE_HOST_RATIO` times the floor. The
  ratio is a source constant of 4 (§8 F1). The bar exits 4, printing `gates HOST — <n> leg(s) timed
  out twice while a spawn cost <x>x this clone's floor; the verdict is about the host, not the
  subject`, only when every failed leg is HOST. A bar with any other failure stays RED and names its
  HOST legs. With no floor recorded, HOST is unavailable and the leg is FAIL with a note saying so.
  The run record's verdict reads `HOST` and no full-green stamp is written. Observed by AC4.
- **S6** — no silent pass. The runner refuses exit 0 unless at least one leg line was reported and
  the run record's verdict file was written; otherwise it exits 2 as REFUSED, naming which half was
  missing. `.githooks/pre-push` pins `GATE_RUN_ID` to a fresh unpredictable id, removes any directory
  of that name first, and after an exit 0 requires `verdict GREEN` in that run's record. A missing or
  different verdict blocks the push as RED. With `GOV_GATE_CMD` set, the hook announces that the
  record check is skipped for an override command. Observed by AC5.
- **S7** — the drift signal. `tools/drift-audit/drift_report.py` gains `legs_retried_after_timeout`,
  the sum of `retried` over the run records it can read, report-only. Zero readable verdict files is
  a DEAD PROBE, never a reassuring 0. Observed by AC7.
- **S8** — carriers and versions. `tools/run-gates/README.md` states exit 4, the retry verb and the
  pending chunk verdict. The drift-audit kit version moves because its signal set changed, and the
  run-gates version stays at the 1.7 the scratch-hygiene unit set, since both land in one build.
  Observed by AC8.

## 3. Non-goals (OUT)

- **Attributing a timeout.** The red-attribution unit classifies a timed-out leg CONTENDED on its
  own terms; this unit does not read that verdict and adds no edge to it.
- **The root cause of TOOL-aSurfacedLexicon-25.** Reading the source at BASE finds no main-shell
  `exit 0` other than the green line and `--print-profile`, so the failing path is UNVERIFIED. S6 is
  the envelope that turns any such path into RED at the boundary, whatever it turns out to be.
- **The beacon reap race** of TOOL-aReapedTicket-4.
- **The driver's reaction to HOST and to a kill before `acquired`.** Both are the gate-wall unit's.
- **Retrying a leg more than once, or retrying a non-timeout failure.** One retry, timeouts only.

### Edges

- **consumes-from** `TOOL-dDerivedDocket-25` — the TREE MOVED verdict, which S6 must accept as a written verdict rather than a missing one
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
unknown `GATE retry` prefix and takes the leg's final `ok` or `FAIL` line.

### The retry pass

The reader's walk is unchanged except for the deferral. After the terminal `wait`
(`tools/run-gates/run-gates.sh:1671`) and before `remove_wall_watcher`, a loop runs each deferred
leg through the existing `runleg` into fresh `.retry` files, one at a time. Keeping the wall armed
is the bound on the retry: a retry cannot extend the run past its declared wall.

### Calibration

The floor is per CLONE, because node `a` pays roughly 251 ms per process against node `d`'s 19-39 ms
(DR 21.7), so an absolute figure would call one node permanently degraded. The measurement at the
second timeout happens after the pool drained, so the bar's own concurrency is gone and a high figure
means another tenant. `GATE_SPAWN_CMD` is a seam for the arm, naming the binary timed, exactly as
`GATE_RUN_ID` is seamed for an arm (`tools/run-gates/run-gates.sh:1081-1084`).

### The boundary check

The hook owns the id it pins, so a verdict file the runner never wrote cannot be mistaken for one it
did: the directory is removed before the run, and the id carries `$$` and `$RANDOM`.

### Inventory

`measure_neighbours`, `measure_spawn_cost`, `run_leg_retry`, `check_verdict_record` (hook) in
`sh.function`; `measure_legs_retried_after_timeout` in `py.function`. `GATE_SPAWN_CMD` is an arm
seam, and `GATE_HOST_RATIO` is a source constant, not a conf key.

### Files touched (estimate)

`tools/run-gates/run-gates.sh`, `tools/run-gates/run-gates.test.sh`, `tools/run-gates/README.md`,
`.githooks/pre-push`, `.githooks/pre-push.test.sh`, `tools/drift-audit/drift_report.py`,
`tools/drift-audit/selftest.py`, `tools/drift-audit/kit.toml`.

### Alternatives rejected

- **A declared timing budget the arm refuses against** (TOOL-dSpentCeiling-8's second candidate).
  It needs a per-arm budget in every suite and still cannot tell load from a hang. The serial retry
  tells them apart for every leg at once.
- **A wall-clock threshold for HOST.** Rejected by DR: a wall clock on an AV-fronted node is not
  measurable to better than a factor of two (`memory/gotchas/process-creation-is-the-suite-cost.md`),
  so only a ratio against the same clone's own floor can discriminate.
- **Parsing the runner's stdout at the hook.** Rejected: a pipe waits for the last inherited write
  end, and the wall watcher's `sleep` can outlive the runner holding it
  (`memory/gotchas/bounded-through-a-pipe-is-unbounded.md`). The run record is a file the runner
  already writes last.

## 5. Production-readiness checklist

- **security** — the hook's pinned id is removed before use, so a planted record cannot satisfy it.
  The floor file is under the git common dir, which this runner already writes.
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
  with the neighbour count in both tails. The arms live in `tools/run-gates/run-gates.test.sh`.
  Red when: the retry is removed, and the contended leg reads FAIL on its first timeout.
  permission: the canary is held; it runs at the build's one post-build bar with `GATE_SELFTESTS=1`.
- **AC2** — When a chunk holds a deferred leg, its chunk line reads `pending` and the `---- retry:`
  line carries the final verdict. Red when: the chunk closes `green` before its retry has run.
- **AC3** — When a fixture bar queues behind a planted live holder and then acquires, stdout carries
  `gate queue: acquired ` after `gate queue: waited ` and the run record header carries the same
  timestamp. Red when: the line is printed before the wait ends, or not at all.
- **AC4** — With a planted floor of 1 ms and `GATE_SPAWN_CMD` seamed to cost 50 ms, a leg that times
  out twice ends HOST and `bash tools/run-gates/run-gates.sh` exits 4; with no floor file the same leg
  ends `GATE FAIL  ` naming the missing calibration. Red when: HOST is granted without a floor, the
  break DR 21.4 U24 names.
- **AC5** — When a planted beacon names a dead pid, the bar still prints a verdict line and writes a
  verdict file; and in `.githooks/pre-push.test.sh` a fake runner that exits 0 writing no record gets
  its push blocked. Red when: the hook trusts the exit status alone, the TOOL-aSurfacedLexicon-25
  path.
- **AC6** — When a scoped run with `GATE_REUSE=1` meets a leg whose ledger row reads `retried`, it
  runs the leg. Red when: `retried` is accepted as `ok` by the reuse predicate.
- **AC7** — When `python tools/drift-audit/drift_report.py` runs over a fixture git dir holding two
  verdict files with `retried 1`, it reports 2 for `legs_retried_after_timeout`, and it prints DEAD
  PROBE over a git dir holding none. Red when: an unreadable population reports 0.
- **AC8** — When `bash tools/check-kit-versions.sh` runs, every kit whose shipped bytes moved carries
  a matching version and marker. Red when: the drift-audit marker is left behind its constant.

## 7. Gates

`run-gates canary` · `pre-push self-test` · `drift-audit selftest` · `drift-audit records` · `kit version markers` · `memory hygiene`

New arm: tools/run-gates/run-gates.test.sh · a leg that times out only beside a spinner · none
New arm: tools/run-gates/run-gates.test.sh · a seamed spawn cost against a planted floor · none
New arm: .githooks/pre-push.test.sh · a fake runner exiting 0 with no record · none

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

## 9. Revision log

- rev-1 · 2026-09-14 · initial draft from DR 21.4 U24 and D12-i6. DR's "0 legs selected" exit-0
  form is not added: at BASE a guard-skipped leg already prints its own `GATE skip` line, which is a
  leg verdict, so the only zero-verdict case left is an empty manifest, and S6 refuses it.

## 10. Reuse audit

- **Probe result.** `python tools/codebase-map/reuse_lookup.py "retry a timed out gate leg once
  serially and report host degradation"` named `read_gate_verdicts` (`tools/govkit/govkit.py`), the
  consumer whose line-prefix parse the new tails must keep working, and no seam for the runner
  itself: `.sh` is an unscanned layer in its header. Reading source found the seams this unit
  extends: `runleg` and `report_one` for the retry, `input_key` and the `.leg` rows for the records,
  `GATE_RUN_ID` (`tools/run-gates/run-gates.sh:1084`) for the hook's pinned id, and `drift_report.py`'s
  `SIGNALS` list for S7.
- **DR against BASE.** DR places the acquire line as the queue-status replacement for the refuted
  TOOL-aUnblockedFleet-6; BASE agrees that `gate-queue-status` is deleted before a bar can be killed
  (`tools/run-gates/run-gates.sh:925`), which is why the line is on stdout and in the run record.
- **Rejected candidates** are in §4.
- Recall terms used: `python tools/memory-recall/query.py "how should a leg killed by its ceiling
  under load be retried and distinguished from a real failure" --terms "ceiling timeout retry serial
  contention nondeterministic HOST calibration spawn verdict no-silent-pass pre-push dead-holder"`.
  Top hits: TOOL-dRetiredFork-30 and TOOL-dRetiredFork-40 on ceilings in seconds,
  TOOL-aGradedMandate-12 on idle-node ceilings under fleet load, TOOL-aSurfacedLexicon-22 and -25,
  and TOOL-aReapedSpinner-16.
