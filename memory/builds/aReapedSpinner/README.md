---
slug: aReapedSpinner
node: a
opened: 2026-09-08
streams: tooling
roster: TOOL
status: OPEN
authorized-by: prompt
ids: TOOL-aReapedSpinner-1
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
- **No count of the live population is written in prose.** The census derives every figure it prints.
## Parked decisions

<!-- roster:units -->

| # | Unit | Status | Mechanism |
|---|---|---|---|
| 1 | `TOOL-aReapedSpinner-1` | PLANNED | the census: one bounded read of the process table, normalized to (pid, ppid, age, cpu, command), with a liveness assertion |
| 2 | `TOOL-aReapedSpinner-2` | PLANNED | the scope fence: a process is attributable to this repo's agent work by a DECLARED root, or it is invisible to every other unit |
| 3 | `TOOL-aReapedSpinner-3` | PLANNED | the classifier: declared ceilings and a two-sample progress probe decide SPIN, IDLE, ORPHAN, OVERAGE or OK |
| 4 | `TOOL-aReapedSpinner-4` | PLANNED | the reaper: a bounded tree kill, children first, death VERIFIED, survivors named |
| 5 | `TOOL-aReapedSpinner-5` | PLANNED | the session seam: a throttled hook puts the verdict in front of an agent mid-turn and at session start |
| 6 | `TOOL-aReapedSpinner-6` | PLANNED | the kit: conf, adopter, govkit entry, gate legs, README — the half that makes an adopter's integration a declaration |

<!-- /roster:units -->

<!-- gen:build-index -->
**Build status:** OPEN · 0 unit(s) · node a · opened 2026-09-08 · streams tooling
ids TOOL-aReapedSpinner-1

<!-- gen:build-units -->
*No spec under this build carries a status header; the status above is declared in the front matter.*
<!-- /gen:build-units -->

Records: 1 bound to this build, across 1 record folder(s).

Ids no record names: none — every unit id is named by a record.

Ids no `spec-audit` record has ever named: none — every unit id has one.
<!-- /gen:build-index -->

<!-- gen:build-order -->

*No spec under this build declares an `order` verb; the build order is whatever its authored plan states.*
<!-- /gen:build-order -->

<!-- gen:build-edges -->

*This build declares no parent and no build declares it as one.*
<!-- /gen:build-edges -->
