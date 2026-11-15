# TOOL-aMeasuredDrag-2 — the stop-guard decides a terminal lease and a pending background task before it spawns `--liveness`

**Status:** SPECCED · rev-1 · 2026-11-15 · node a · Tier-1 · base aebbb4a7 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief.md](../prompts/2026-11-15-prompt-TOOL-aMeasuredDrag-1-brief.md) | research | TOOL-aMeasuredDrag-1 TOOL-aMeasuredDrag-3 TOOL-aMeasuredDrag-4 TOOL-aMeasuredDrag-5 TOOL-aMeasuredDrag-6 TOOL-aMeasuredDrag-7 TOOL-aMeasuredDrag-8 TOOL-aMeasuredDrag-9 TOOL-aMeasuredDrag-10 TOOL-aMeasuredDrag-11 |

<!-- /gen:spec-records -->

## 1. Goal

Brief item 2, findings sessionhooks-1 and pipeline-5 of the 2026-11-15 performance review. On every
Stop of a bound session, `tools/unattended/stop-guard.js#checkSession` spawns the driver's
`--liveness` (`runLiveness`, `tools/unattended/stop-guard.js@44860d3237:107-115`, called at `:223`)
before it reads `background_tasks`, which allows the stop whatever the driver says (`:151`). The
review's skeptic counted 5,492 of 5,653 bound Stops PINNED (verdicts record, 2026-11-15) with
background tasks, each paying the spawn first. This unit decides the two allows that need no driver
before the spawn, with the block or allow decision unchanged for every payload over a record the
driver wrote.

## 2. Scope (IN)

- **S1** — A pure function `checkStopWithoutDriver(phase, backgroundTasks, terminal)` in
  `tools/unattended/stop-guard.js`, exported, returns `{decision: 'allow', reason: 'terminal'}` when
  `terminal` includes the lease's phase, `{decision: 'allow', reason: 'background-tasks'}` when
  `backgroundTasks > 0` and the phase is neither `LANDING` nor `HELD`, and `null` otherwise.
  Observed by AC1 and AC2.
- **S2** — The lease loop of `checkSession` (`:221-244`) asks S1 first, with the lease's `phase`
  from `tools/unattended/run-lease.js#scanLeases` (`tools/unattended/run-lease.js@8a5aa9d79e:161`).
  On a non-null answer it calls no `runLiveness` and takes that answer as the stop's decision. On
  `null` it runs the driver and `checkStop` exactly as today. Observed by AC1 and AC2.
- **S3** — The sidecar line of a stop S1 decided carries the lease's phase in `phase` and the
  literal `unknown` in `verdict`. Every other key is written as today, `blocks` still counted from
  the file. Observed by AC1.
- **S4** — The terminal set is the one `tools/unattended/gate-guard.js` exports, `PHASES_TERMINAL`
  (`tools/unattended/gate-guard.js@e58690cf70:168`, `:969`), read with a `require` inside a `try`
  once per bound stop. When that load throws, S1 is not asked at all, and every stop runs the
  driver as today. Observed by AC3.
- **S5** — The header's decision table (`:25-38`) gains the two driverless rows above the
  `--liveness` sentence. NOT OBSERVED: comment text, read by the focused self-review.
- **S6** — The unit's acceptance ledger records the before and after of AC4 beside its spawn
  baseline. Observed by AC4.

## 3. Non-goals (OUT)

- `checkStop`, `REASONS`, `renderBlock`, the knob and the block count are not edited.
- `tools/unattended/run-lease.js` and `tools/unattended/gate-guard.js` are not edited. The
  terminal set stays where its parity arm pins it.
- No verdict cache keyed on the run-state file: that is the review's section 5 work.
- A stop at `LANDING` is never decided early. The newest sidecar line's `phase` is what
  `--landed` grades (`tools/unattended/unattended.sh@eb567029d1:6500`), so every landing stop keeps
  the driver's reading byte for byte.
- A stop at `HELD` is never decided early. TOOL-dDerivedDocket-61 S5 orders `held` ahead of
  `background-tasks`, and the arm `U61 line reason is held, ahead of background-tasks` of the
  stop-guard suite pins that reason.
- What moves, stated rather than hidden. On a record the driver wrote, the decision, stdout,
  stderr and exit status never move.
  On a stop S1 decides, the sidecar's `verdict` reads `unknown`. Its `reason` differs from today's
  in two cases only, and F1 asks whether that is admitted: a payload cwd in a worktree off the
  run's branch with tasks pending, today `elsewhere`; and a driver that would have failed, today
  `liveness-unreadable`, where `phase` also reads the lease's phase instead of `unknown`.
- The terminal test reads the lease's phase as `scanLeases` trims it, as the question arm of
  `gate-guard.js` already does (`:884`). A phase line hand-edited with a tab or trailing blank
  after `LANDED` reads terminal here and not in the driver. The driver never writes one, and the
  hook already binds its session through the same reader.

## 4. Design

```js
// in checkSession, once leases.length > 0
let terminal = null
try {
  terminal = require(path.join(__dirname, 'gate-guard.js')).PHASES_TERMINAL
} catch { terminal = null }
for (const l of leases) {
  const sidecar = lease.deriveSidecarPath(repo.gitDir, 'stop', l.slug)
  const early = terminal ? checkStopWithoutDriver(l.phase, tasks, terminal) : null
  const run = early ? null : runLiveness(__dirname, repo.root, l.slug)
  const liveness = run && run.ok ? parseLiveness(run.stdout) : null
  const before = measureBlocks(sidecar, sessionId)
  const verdict = early || checkStop(liveness, tasks, knob, before)
  // line: phase  early ? l.phase : (liveness ? liveness.phase : 'unknown')
  //       verdict early ? 'unknown' : (liveness ? liveness.verdict : 'unreadable')
}
```

Why the decision cannot move. Every row of `checkStop` above `background-tasks` is an allow
(`:140-150`), so a payload with tasks pending is allowed whatever the driver answers. A recorded
phase in `PHASES_TERMINAL` makes `derive_liveness` read `state=terminal`
(`tools/unattended/unattended.sh@eb567029d1:9064`), and TERMINAL is the first verdict
(`:9116`), so the driver's answer is the `terminal` allow or, when it fails, the
`liveness-unreadable` allow. The terminal test runs first, so a terminal record with tasks pending
keeps the reason `terminal` it has today.

Why `phase` takes the lease's phase and not `unknown`. `--liveness` prints the recorded phase
through `read_recorded_phase`, the same `## Run facts` fact `scanLeases` reads. `--landed`'s
check 54 prints the newest line's phase in its refusal text (`:6501`), so `unknown` would move that
text on every early stop, and the lease's phase moves it on none where the driver would have
succeeded.

The `require` of `gate-guard.js` cost 4.2 ms PINNED (node a, 2026-11-15, at aebbb4a7), once per
bound stop, against a driver spawn. `gate-guard.js` loads `stop-guard.js` only inside `checkAsk`
(`:888`), so the two files never load each other at load time.

### Files touched (estimate)

- `tools/unattended/stop-guard.js`

### Alternatives rejected

- The terminal pair restated in `stop-guard.js`: a third copy of the driver's `PHASES_TERMINAL`,
  against the charter's `[reuse]` rule, with no parity arm of its own.
- The pair moved into `run-lease.js` with `gate-guard.js` reading it there: `gate-guard.js` states
  that an unloadable `run-lease.js` must leave its bar arm standing (`:141-149`), and a top-level
  `require` would break that.
- Testing ELSEWHERE in JavaScript, from HEAD and the record's `run-branch` fact: a second
  derivation of `resolve_holder_worktree`, and it still cannot see a driver failure. F1 option B.

## 5. Acceptance criteria

- **AC1** — When `node <kit>/stop-guard.js` reads each payload below on stdin, once from a scratch
  kit holding `stop-guard.js`, `run-lease.js` and `gate-guard.js` from `git show aebbb4a7:<path>`
  and once from a scratch kit holding the built files, each with a stub `unattended.sh` that prints
  the case's phase and verdict as `phase:` and `verdict:` lines, stdout, stderr and exit status are
  byte-identical (`cmp`). The sidecar line is
  identical once `utc` is dropped, and `verdict` too for the stops S1 decides. The cases, as
  record phase, stub verdict and task count: BUILDING LIVE 0 · BUILDING LIVE 2 · BUILDING
  ELSEWHERE 0 · HELD HELD 1 · LANDING FINISHED-UNSTAMPED 0 · LANDING FINISHED-UNSTAMPED 1 · LANDED
  TERMINAL 0 · ABORTED TERMINAL 1.
  Red when: S1 answers for a case the driver would block, such as LANDING FINISHED-UNSTAMPED 0, and
  the built kit prints no block where the base kit does.
  fixture: built in a scratch tree under `%TEMP%`, a fake `.git/HEAD`, a `.unattended.conf` and one
  `RUN.md` per case, the shape `build_fixture` of the stop-guard suite writes. The tree holds none
  today, and the pass builds it.
- **AC2** — When the stub `unattended.sh` of AC1 appends one line to a count file per call, the
  built kit's count grows by 0 for BUILDING LIVE 2, LANDED TERMINAL 0 and ABORTED TERMINAL 1, and
  by 1 for BUILDING LIVE 0, HELD HELD 1 and LANDING FINISHED-UNSTAMPED 1. The base kit's count
  grows by 1 for every case.
  Red when: the loop calls `runLiveness` before it asks S1, and every case counts 1.
- **AC3** — When the built kit of AC1 is copied without `gate-guard.js` and the cases of AC1 run
  again, every case counts 1 call, and every sidecar line equals the base kit's once `utc` is
  dropped.
  Red when: the missing file throws out of `checkSession`, or S1 is asked with no terminal set and
  LANDED TERMINAL 1 records `background-tasks`.
- **AC4** — When `time bash tools/unattended/unattended.sh --liveness aMeasuredDrag` runs in this
  worktree, and `time` wraps the built and base kits' BUILDING LIVE 2 stop of AC1, each beside
  `time (for i in 1 2 3 4 5 6 7 8 9 10; do /usr/bin/true; done)` taken in the same shell, the
  built stop is under the base stop, and the ledger records the four wall times.
  Red when: the built stop is not under the base stop, which means the spawn still runs.
  figure: every time is DERIVED at observation time and recorded with its commit sha.

## 6. Gates

`unattended kit gate` · `lexicon naming predicates`

What the close runs, and no pass does: the merge bar once, which runs the stop-guard suite and the
gate-guard suite (`tools/unattended/stop-guard.test.sh`, `tools/unattended/gate-guard.test.sh`)
through its selftest runner. What no suite sees: the stop-guard suite's kit copy holds
`stop-guard.js` and `run-lease.js` only (`tools/unattended/stop-guard.test.sh@003d91bd43:272`), so
every terminal case there takes the S4 fallback and runs the stub driver. The early terminal row is
observed by AC1 to AC3 and by no arm. No arm is added or moved.

## 7. Open questions

- **F1 — On a stop S1 decides, may the sidecar's `reason` read `background-tasks` where the driver
  would have answered `elsewhere`, or `liveness-unreadable`?**
  The brief admits only the line's `phase` and `verdict` reading `unknown` for these stops. The
  `reason` cannot match today's in the two cases §3 names, because only the driver can tell them.
  Nothing in the tree reads `reason` but the stop-guard suite:
  `grep -rn "background-tasks\|liveness-unreadable"` over `tools/` and `skills/`, outside
  `stop-guard.js` and its suite, finds no line at aebbb4a7, and
  `read_stop_listing` (`unattended.sh@eb567029d1:6442`) reads `utc`, `phase` and `session_crons`.
  One printed text can move, and only on the driver-failure case: when such a stop is the newest
  line at `--landed`, check 54's refusal (`unattended.sh@eb567029d1:6501`) names the lease's
  phase where it named `unknown`. Its decision does not move, because an early stop is never at
  `LANDING`. Every option that skips the spawn has this case, the terminal row included, because
  a failure of a probe that is not run cannot be recorded.
  - Option A — admit it. S1 to S6 as written. Every pending-task stop outside `LANDING` and
    `HELD`, and every terminal stop, pays no spawn.
  - Option B — also leave out a stop whose payload cwd is off the run's branch, tested in
    JavaScript from the worktree's HEAD and the record's `run-branch` fact. That adds a field to
    `scanLeases` and a second copy of the holder test. The driver-failure case still moves.
  - Option C — park the whole unit, both rows. Nothing moves, and none of the measured saving is
    recovered.
  - Recommendation: A. The decision, stdout, stderr and exit status hold on every record the
    driver wrote. `reason` is a written field with no reader outside the suite, and the one
    printed text that moves reports a driver failure on a stop the brief itself lets read
    `unknown`. A satisfies the most of brief item 2, and B adds a surface for one case and still
    leaves the other. If the resolver reads check 54's text as a printed line under this build's
    non-goal, M3's first veto discards A and B, and C is the survivor.

## 8. Revision log

- rev-1 · 2026-11-15 · initial draft from brief item 2 of the aMeasuredDrag brief.

## 9. Reuse audit

The seam is `checkSession` in `tools/unattended/stop-guard.js`, edited in place, with the lease's
phase `scanLeases` already parses and `gate-guard.js`'s pinned `PHASES_TERMINAL`, which its question
arm already uses for the same skip (`tools/unattended/gate-guard.js@e58690cf70:884`).
`python tools/codebase-map/reuse_lookup.py "stop hook allows without spawning the liveness driver
when background tasks are pending"` named `runLiveness` and `parseLiveness`, the functions this unit
orders, and no seam that decides a stop without the driver. Recall returned TOOL-dDerivedDocket-61,
whose S5 orders `held` ahead of `background-tasks`, and TOOL-aWokenSentinel-8, the
`landing-unstamped` row that keeps `LANDING` on the driver.

Recall terms used: `python tools/memory-recall/query.py "why is a held run's stop allowed ahead of
background tasks in the stop-guard" --terms "stop-guard background_tasks liveness runLiveness held
terminal phase lease sidecar reason landed keepalive-reaped"`
