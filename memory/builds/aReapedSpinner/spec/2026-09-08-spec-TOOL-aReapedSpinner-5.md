# TOOL-aReapedSpinner-5 — the session seam: the verdict reaches an agent, throttled

**Status:** OPEN · rev-2 · 2026-09-08 · node a · Tier-2 · base e2b82a53 · streams tooling · order 6

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round1.md](../reviews/2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round1.md) | spec-audit | TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3 TOOL-aReapedSpinner-4 TOOL-aReapedSpinner-6 TOOL-aReapedSpinner-7 |

<!-- /gen:spec-records -->

## 1. Goal

Put the monitor's verdict where a session actually reads it — at session start for the standing
population, and mid-turn for what the session itself is creating — at a cost small enough that
nobody turns it off. Without this unit the kit is a command nobody runs, which is the state the
whole fleet is in today.

## 2. Scope (IN)

- **S1** — `tools/process-monitor/procmon-hook.js`, a hook entry point that runs the sweep in
  REPORT-ONLY form and prints at most a few lines. Observed by AC1.
- **S2** — the THROTTLE: the hook stamps a file under the git common dir and exits immediately
  when the stamp is newer than `PROCMON_THROTTLE_S`. The early exit path runs no census. Observed
  by AC2, AC3.
- **S3** — SILENCE ON CLEAN: with nothing flagged the hook prints NOTHING and exits 0, so the
  session's transcript carries a line only when there is something to act on. Observed by AC4.
- **S4** — wiring: a `PostToolUse` hook on matcher `Bash|PowerShell` and a `SessionStart` line, both
  added to `.claude/settings.json` by unit 6's adopter. Observed by AC5.
- **S5** — the SessionStart arm reports the STANDING population unthrottled, because a fresh session
  has no stamp of its own and the two-and-a-half-day orphans are exactly what it must see. Observed
  by AC6.
- **S6** — the hook is BOUNDED and fails OPEN: any error, timeout or missing conf makes it print one
  line naming the failure and exit 0, never blocking a tool call. Observed by AC7, AC8.

## 3. Non-goals (OUT)

- **No killing from the hook.** The build rules make reporting and killing separate authorities;
  the hook runs the report path only, whatever `PROCMON_REAP_MODE` says.
- **No background spawn to hide the census cost.** A hook that detaches a child to save a second is
  a hook that manufactures the orphan class this kit exists to reap. The throttle is the answer.
- **No `PreToolUse` hook.** Nothing here should be able to deny a tool call.
- **No per-tool filtering beyond the matcher.** The throttle already bounds the cost.

### Edges

- **consumes-from** `TOOL-aReapedSpinner-4` — the report path, which is `--sweep` in report mode.
  Unit 4 owns the whole census-fence-classify chain after the round-1 fold; rev-1 of this spec
  consumed unit 3's `--report`, which no longer resolves scope and so cannot answer what the hook
  must print.
- **consumes-from** `TOOL-aReapedSpinner-6` — `PROCMON_THROTTLE_S`, and the adopter that writes the
  settings entries.
- **hands-off** external — the harness reads a hook's stdout; nothing in this repo asserts that it
  does, and AC1 observes the hook's own output rather than the harness's rendering of it.

## 4. Design

### The cost, stated plainly

The census is ~1.2 s on this node, over a 320 ms PowerShell floor. Run per tool call that is
intolerable; run once per `PROCMON_THROTTLE_S` it is invisible. At the default 300 s it is 1.2 s of
every 300, or 0.4%, and only in sessions that make tool calls at all.

**The throttle check itself must be cheap**, so it is a stat of one file and nothing else — no
conf parse, no python start, no census on the early-exit path. That path is what runs on the
overwhelming majority of tool calls, and AC3 asserts it does no work.

### Why the stamp lives in the git common dir

Same reason `.unattended.conf` gives for `LANDER_MARKER`: in a linked worktree `.git` is a file, so
a tree-relative path fails, and `git rev-parse --git-common-dir` is the one location every worktree
of one repo agrees on. It also makes the throttle SHARED across concurrent sessions on one repo,
which is correct — the standing population is shared too, and N sessions should not each pay for
their own census of it.

### Fail open, and say so

A hook that blocks tool calls when the monitor is broken would be worse than no monitor. Every
failure path prints one line naming what failed and exits 0. That line is the liveness assertion:
the difference between "nothing flagged" and "the monitor could not run" is exactly what the build
rules require to stay visible, and silence is reserved for the genuinely clean case.

### Files touched (estimate)

New: `tools/process-monitor/procmon-hook.js`. Edited: `.claude/settings.json` (by unit 6's adopter,
via the existing `tools/settings-merge.py` seam rather than a hand-written JSON edit).

## 5. Production-readiness checklist

- security — the hook reads and prints; it never kills and never writes outside its stamp file.
- perf / scale — the throttled path is one `stat`; the unthrottled path is the census. Both bounded.
- error / empty / loading states — clean is SILENT (S3), broken is one line (S6), flagged is a short
  list. Three distinguishable states.
- observability — the report names the verdict and the age for each flagged row, so the line is
  actionable without a follow-up command.
- risks — hook noise. Mitigated by silence-on-clean and by the throttle; if it still annoys, the
  conf value is the knob and the README says so.
- testing — arms drive the hook directly with a fresh stamp, a stale stamp, a clean census, a
  flagged census, and a raising census.
- migration — none, but the settings edit must be idempotent: `tools/settings-merge.py` already is,
  and is reused rather than re-implemented.
- user docs — the kit README's wiring section, unit 6.

## 6. Acceptance criteria

- **AC1** — When the hook runs with a stale stamp against a census holding a flagged row, its
  stdout names that row's pid, verdict and age. Observed by `selftest.py`, arm
  `test_hook_reports_a_flagged_row`.
  Red when: the hook prints a bare count, which tells a session something is wrong and not what.
- **AC2** — When the hook runs twice in succession, the second run exits 0 having printed nothing
  and having run no census. Observed by `selftest.py`, arm `test_throttle_suppresses_the_second_run`.
  Red when: the stamp is written before the work rather than after, so a crashing hook throttles
  itself out of ever running again.
- **AC3** — When the throttled early-exit path runs, no census backend process is spawned. Observed
  by `selftest.py`, arm `test_throttled_path_spawns_nothing`, which shims the backend to write a
  marker file and asserts the marker is absent.
  Red when: the conf is parsed or the census imported before the stamp is checked, which puts the
  expensive work on the common path.
- **AC4** — When the census holds no flagged row, the hook prints NOTHING and exits 0. Observed by
  `selftest.py`, arm `test_clean_is_silent`.
  Red when: a "0 flagged" line is printed on every throttle window, which is the noise that gets a
  hook removed.
- **AC5** — When `adopt-process-monitor.sh` runs against a scratch tree,
  `.claude/settings.json` gains both hook entries and a second run adds no duplicate. Observed by
  `adopt-process-monitor.test.sh`, arm `test_wiring_is_idempotent`.
  Red when: the adopter appends rather than merging, which grows the hook list on every adoption.
- **AC6** — When the hook is invoked in its SessionStart form, it runs the census regardless of the
  stamp. Observed by `selftest.py`, arm `test_session_start_ignores_the_throttle`.
  Red when: a fresh session inherits another session's fresh stamp and reports nothing, which is
  precisely the 52-hour-orphan case going unseen.
- **AC7** — When the census raises, the hook prints one line naming the failure and exits 0.
  Observed by `selftest.py`, arm `test_broken_monitor_fails_open`.
  Red when: the hook exits non-zero, which blocks the session's tool call over a monitoring fault.
- **AC8** — When the census is made to hang, the hook returns within its declared bound and prints
  the timeout line. Observed by `selftest.py`, arm `test_hung_census_does_not_block_the_hook`.
  Red when: the bound is applied through a pipe, which bounds the verdict and not the clock — the
  `bounded-through-a-pipe-is-unbounded` class, selected for these paths.

## 7. Gates

`line length` · `hook destinations (every declared hook path ships)` · `check-wiring self-test` · `govkit selfcheck` · `dead-path carriers (deleted files still named)`

New arm: `tools/process-monitor/selftest.py` · stages a fresh and a stale stamp, a clean and a
flagged and a raising census, a hanging backend, and both hook forms · floor moves with unit 1's
arms, one suite.

## 8. Open questions

- **F1 — `PostToolUse` on `Bash|PowerShell`, or on every tool?**
  RESOLVED (agent, 2026-09-08, delegated): `Bash|PowerShell`. Those are the only tools that create
  processes, so a wider matcher pays the hook's start cost on reads and edits that cannot possibly
  have changed the population. The existing `scratch-guard.js` uses exactly this matcher, so the
  pair is consistent. Vetoes clean.
- **F2 — what is the default `PROCMON_THROTTLE_S`?**
  RESOLVED (agent, 2026-09-08, delegated): 300. At 1.2 s per census that is 0.4% of a session's
  tool-call time, and it is short enough that a spin loop started mid-session is named within five
  minutes rather than at the next session start. Declared, so an adopter can move it.

## 9. Revision log

- rev-1 · 2026-09-08 · initial draft.
- rev-2 · 2026-09-08 · header order · §3 Edges · no findings against this unit in spec-audit round 1.
  `order` moves 5 → 6 behind unit 3's and unit 4's shifts, and the report edge moves from unit 3 to
  unit 4, which took ownership of the full chain under D5.

## 10. Reuse audit

The seams this unit EXTENDS, both cited by path and verified against source at BASE:
`tools/settings-merge.py` for the idempotent `.claude/settings.json` edit — reused rather than
re-implemented, because a hand-written JSON edit in an adopter is how a settings file gets
duplicated hook rows; and `tools/check-wiring.sh --session`, which is this repo's existing proof
that a SessionStart hook's stdout reaches the agent and is the pattern S5 copies. The hook file
shape follows `tools/hooks/scratch-guard.js`, which already runs on the `Bash|PowerShell` matcher.
The probe `python tools/codebase-map/reuse_lookup.py "kill a hung or idle background process and
report it to the session"` returned the `unattended` and `govkit` dossiers for the report stem, and
`SESSION-KICKOFF.md` — none of which is a reporting seam for this.

Recall terms used: `gate runner wall clock bound timeout kill children orphan process leg pool
watchdog GATE_WALL background subprocess reaper`
