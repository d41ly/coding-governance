---
slug: aReapedSpinner
node: a
opened: 2026-09-08
streams: tooling
roster: TOOL
authorized-by: prompt
ids: TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3 TOOL-aReapedSpinner-4 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-6 TOOL-aReapedSpinner-7
---

# aReapedSpinner — a process this fleet launched has no deadline, no witness and no reaper, so nothing observes it burning

## The problem this build exists to solve
Every deadline this repo owns bounds a command a CHECKER launched — `run-gates.sh` its legs,
`unattended.sh` its `GATE_BOUND` commands, `run-selftests.sh` its suites. Nothing bounds a process an
AGENT launched, and that is where every observed failure came from.

One sweep on node `a` found, live at once: two `until grep -q …; do :; done` spin loops 11.4 h old
holding 46221 CPU-seconds between them, waiting on a file no writer was left to make; nine
`check-unattended.test.sh` where one was started; five `Monitor` greps 52–61 h old with dead parents
still holding pipes; and a runner plus children alive 7.5 h after `TaskStop` returned success. Three
independent defects — `TaskStop` stops a handle and not a tree, an agent-launched job has no ceiling,
and nothing ENUMERATES the population, which is why all three ran unseen for two and a half days.
## Expected improvements
- A forgotten process is NAMED — age, CPU, and why it is judged dead weight — to a session that can
  act, instead of surfacing in a manual sweep days later.
- The provably-dead class dies on a schedule, so a spin loop costs minutes of a core, not half a day.
- Cost verdicts stop competing with orphans from runs that ended.
- An adopter declares its roots and gets the same observer, writing no process-table reader.
## Detriments if this is not built
- The fleet keeps paying an unbounded, unmeasured CPU tax, and every timing this repo records stays
  contaminated by whatever else was burning beside it.
- `TaskStop` keeps reading as a stop when it is not one.
- Adopters inherit all three defects, since none of them is repo-specific.
## Build-level rules
- **SCOPE IS THE SAFETY PROPERTY**, gated harder than anything else here. Attribution is POSITIVE and
  declared: a process is in scope because something says so, never because nothing excluded it. A
  reaper that can name a process outside the declared roots is worse than every failure it fixes.
- **The observer may never become the thing it observes.** Every probe here is bounded, single-shot
  and non-recursive. A monitor with a spin loop in it is the joke that writes itself.
- **Reporting and killing are different authorities** — separate units, separate gates, and no report
  path kills as a side effect.
- **`nothing to report` must be distinguishable from `the probe could not run`.** A process monitor
  that reports zero when the table read failed is the purest instance of the class this repo gates
  against in a dozen places.
- **No count of the live population is written in prose.** The census derives every figure it
  prints.
- **THE ARCHITECTURE, settled by two audit rounds and stated once.** The census keys on
  `winpid`, the only id every process has, and carries BOTH parent graphs. Scope is a TREE
  CLOSURE from attributable roots, not a per-row predicate. The signal is chosen per row:
  MSYS `kill` where MSYS can address it, `taskkill //PID` otherwise. Each of the three replaced
  an MSYS-only assumption that measured out at 10 of 313 rows.
## Parked decisions

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aReapedSpinner-1` | SPECCED | the census: a platform-selected read of the process table, normalized to (id, parent, age, cpu, command); on Windows a JOIN of `ps -W` and CIM, and an unrecognised platform REFUSES rather than reporting an empty table |
| 2 | `TOOL-aReapedSpinner-2` | SPECCED | the scope fence: a row is attributable to this repo's agent work by a DECLARED root, or it is invisible to every other unit |
| 3 | `TOOL-aReapedSpinner-3` | SPECCED | the classifier: a declared age ceiling DECIDES and the CPU rate LABELS, giving OK, OVERAGE, SPIN, IDLE or ORPHAN |
| 4 | `TOOL-aReapedSpinner-4` | SPECCED | the reaper: walk the parent edges leaves-first, kill, VERIFY each death, name survivors. Not `taskkill /T`, which measured 25% effective, and not a process group, which reaps the caller |
| 5 | `TOOL-aReapedSpinner-5` | SPECCED | the session seam: a throttled hook puts the verdict in front of an agent mid-turn and at session start |
| 6 | `TOOL-aReapedSpinner-6` | SPECCED | the kit: conf, adopter, govkit entry, gate legs, README — the half that makes an adopter's integration a declaration rather than a port |
| 7 | `TOOL-aReapedSpinner-7` | SPECCED | the gate runner reaps its own TREE at every exit path, delegating to unit 4 instead of killing a recorded pid and leaving the grandchildren |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 7 unit(s) · node a · opened 2026-09-08 · streams tooling
ids TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3 TOOL-aReapedSpinner-4 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-6 TOOL-aReapedSpinner-7

<!-- gen:build-units -->
| Unit | Order | Tier | Status | Rev | Last change |
|---|---|---|---|---|---|
| [TOOL-aReapedSpinner-6 — the kit skeleton: a declared population an adopter joins by declaration](spec/2026-09-08-spec-TOOL-aReapedSpinner-6.md) | 1 | 2 | OPEN | rev-4 | 2026-09-08 |
| [TOOL-aReapedSpinner-1 — the census: one bounded read, keyed on the id every process has](spec/2026-09-08-spec-TOOL-aReapedSpinner-1.md) | 2 | 2 | OPEN | rev-4 | 2026-09-08 |
| [TOOL-aReapedSpinner-2 — the scope fence: attribution is a TREE property, computed once](spec/2026-09-08-spec-TOOL-aReapedSpinner-2.md) | 3 | 2 | OPEN | rev-4 | 2026-09-08 |
| [TOOL-aReapedSpinner-3 — the classifier: age DECIDES, the CPU rate LABELS](spec/2026-09-08-spec-TOOL-aReapedSpinner-3.md) | 4 | 2 | OPEN | rev-4 | 2026-09-08 |
| [TOOL-aReapedSpinner-4 — the reaper: walk both graphs, signal per kind, VERIFY](spec/2026-09-08-spec-TOOL-aReapedSpinner-4.md) | 5 | 2 | OPEN | rev-4 | 2026-09-08 |
| [TOOL-aReapedSpinner-5 — the session seam: the verdict reaches an agent, throttled](spec/2026-09-08-spec-TOOL-aReapedSpinner-5.md) | 6 | 2 | OPEN | rev-4 | 2026-09-08 |
| [TOOL-aReapedSpinner-7 — the gate runner's INTERRUPT path kills nothing, and that is the leak](spec/2026-09-08-spec-TOOL-aReapedSpinner-7.md) | 6 | 2 | OPEN | rev-4 | 2026-09-08 |
<!-- /gen:build-units -->

Records: 9 bound to this build, across 4 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

| Step | Units | Parallel |
|---|---|---|
| 1 | `TOOL-aReapedSpinner-6` | no |
| 2 | `TOOL-aReapedSpinner-1` | no |
| 3 | `TOOL-aReapedSpinner-2` | no |
| 4 | `TOOL-aReapedSpinner-3` | no |
| 5 | `TOOL-aReapedSpinner-4` | no |
| 6 | `TOOL-aReapedSpinner-5`, `TOOL-aReapedSpinner-7` | yes |
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
