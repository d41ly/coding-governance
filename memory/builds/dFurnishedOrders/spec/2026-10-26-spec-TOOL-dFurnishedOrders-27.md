# TOOL-dFurnishedOrders-27 — every owner question the driver raises carries the run's window: `--dispatch` and `--phase` ask the door through one helper that hands it the run's session and lease start

**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 5ff43572 · streams tooling · order 21 · advances TOOL-dFurnishedOrders-21

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 20 unit specs
(`memory/builds/dFurnishedOrders/reviews/2026-10-26-review-TOOL-dFurnishedOrders-1-spec-audit-round1.md`)
confirmed finding **id 19 at HIGH**, report item **H1**, of the class
`invariant-held-on-one-admission-path`. Ids 3 and 52 share that item and take
`TOOL-dFurnishedOrders-26` and `TOOL-dFurnishedOrders-28`.

The skeptic reproduced the defect on this run's own session: `scan_owner_turns` returned `owner typed`
first and only `keepalive` after it, so a FORKED `--dispatch` raised before the first fire takes
`TOOL-dFurnishedOrders-16` S4's `write_owner_hold` path and is refused for an owner who is not there;
with cron disabled, every raise of the run is. Unit 16 asks the door from two places in the driver,
`--dispatch`'s FORKED case (its S4) and `--phase`'s gated exit (its S5). A window held on one of them
and not the other leaves the second admitting the launch turn as presence.

This unit makes both paths ask the door through one helper that hands it the run's session and its
lease start, the window `TOOL-dFurnishedOrders-26` reads. It repairs `TOOL-dFurnishedOrders-16` and
builds one step after it (order 21), after unit 26 by the dispatch's id sort.

## 2. Scope (IN)

- **S1** — One helper. `read_owner_door <run-state file> <kind> [<item>]` in
  `tools/unattended/unattended.sh` runs `handoff.py owner-question --kind <kind> --session <sid>
  --since <lease-utc>`, the two values read by `fact` (`tools/unattended/unattended.sh:1359`) from the
  run-state file's `session` and `lease-utc` lines, as `:2406` reads them, and prints the door's one
  line. Where unit 16 built its door call inline at each site, both sites are re-pointed to the helper;
  where it built one function, that function becomes the helper. Observed by AC1 and AC2.
- **S2** — Both admission paths. `verb_dispatch`'s FORKED case (`:13624`, `TOOL-dFurnishedOrders-16`
  S4) and `--phase`'s gated-exit refusal (`TOOL-dFurnishedOrders-16` S5) ask the door only through S1,
  so no driver path raises an owner question without the window. Observed by AC1 and AC2.
- **S3** — A run-state file without the window. A `lease-utc` or `session` line that is absent or
  `absent` leaves the matching flag off, and the helper prints one line, `owner question — no run
  window: <key> absent`, before the door's answer, so the caller sees why unit 16's table answered.
  Observed by AC3.
- **S4** — The docs: `tools/unattended/VERBS.template.md`'s hold lines of `--dispatch` and `--phase`
  say the door is asked with the run's lease start, rendered to `memory/guides/UNATTENDED-VERBS.md`.
  Observed by AC4.

## 3. Non-goals (OUT)

- The window itself and the door's `--since` flag: `TOOL-dFurnishedOrders-26`.
- What an unreadable turn answers inside the window: `TOOL-dFurnishedOrders-28`.
- `write_owner_hold`, the hold row and its release: unit 16 S4 and TOOL-dDeclaredLoop-31 S6, unchanged.
- The unattended kit's self-test suites at landing: WAIVED by the build README's rule, their clean
  reading owed with PLAY-dClosedLoop-18; the arm of §7 is declared and observed at the close.

### Edges

- **consumes-from** `TOOL-dFurnishedOrders-16` — the two driver paths that ask the `owner-question` door, `--dispatch`'s FORKED case and `--phase`'s gated exit, which S1 and S2 route through one helper (id 19)
- **consumes-from** `TOOL-dFurnishedOrders-26` — `--since`, the door flag the helper fills with the run's lease start (ids 3 and 19)

## 4. Design

### The helper

```
read_owner_door <rel> <kind> [<item>]
  fact "$rel" session   -> sid      (absent: no --session, one "no run window" line)
  fact "$rel" lease-utc -> since    (absent: no --since,   one "no run window" line)
  python <roles kit>/handoff.py owner-question --kind <kind> [--session <sid>] [--since <since>]
  print the door's "<answer> · <source>" line
```

The roles kit is found as unit 16 S4 finds the door; the helper adds no second resolution. The
`<item>` argument is carried for the hold line the caller writes and is not passed to the door.

### Why one helper

The invariant is that no owner question of a run reads the launch turn as presence. It is held where
the question is asked, and the driver asks in two places today, with more to come as gates are added
(TOOL-dDeclaredLoop-19). One helper is the one place the window is attached, so a third caller that
uses it inherits the window, and AC2 fails on a path that bypasses it.

### Inventory

Minted: `read_owner_door`, a shell function, and the printed line `owner question — no run window:`.
`python tools/lexicon/lexicon.py --suggest read_owner_door --as sh.function` answered OK;
`ask_owner_door` was refused, `ask` being no declared verb.

### Migration

None: no row changes shape; the door gains a flag it already validates.

### Rollout

Live at landing. The unattended kit's version moves where the kit epoch leg asks.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`, rendered to `memory/guides/UNATTENDED-VERBS.md`

### Alternatives rejected

- **Pass `--since` at each call site.** Two copies of one rule, the instance this finding's class
  names: the next site written without it reads the launch turn again.
- **Export the window in the environment for the door to read.** A variable set once leaks into every
  child of the driver, and the door would read a value nobody passed it on its command line.

## 5. Production-readiness checklist

- security — no new write path; the helper reads two lines of the run-state file and passes them as
  argv, never through a shell string.
- perf / scale — one `fact` read per value, at raise only.
- error / empty / loading states — an absent value prints S3's line and the door answers by unit 16's
  table.
- observability — the door's source line names the window it read.
- risks — a run-state file whose `lease-utc` is later than the owner's real return would read that
  return as before the window; `lease-utc` moves only when a run takes or re-takes the lease, which is a
  turn of its own.
- testing — AC1 to AC4 by fixtures a pass builds; the arm of §7 at the close.
- migration — none.
- user docs — `memory/guides/UNATTENDED-VERBS.md` by S4; no `help/` page names the driver's hold.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/unattended.sh --dispatch <slug> <unit>` runs in a scratch build
  whose unit has an open F-item and whose run-state file holds `session: S` and `lease-utc: T`, with
  the roles kit's `handoff.py` replaced by a stub that records its argv and answers `owner · stub`, the
  recorded argv holds `--kind fork`, `--session S` and `--since T`.
  Red when: a FORKED dispatch asks the door without the run's window.
  fixture: a scratch clone under `%TEMP%`, built by the pass, as unit 16's fixtures are.
- **AC2** — When `--phase` refuses a move past a gated exit in the AC1 fixture, the stub's recorded argv
  holds `--kind owner-gate`, `--session S` and `--since T`; and every line that
  `grep -n "owner-question --kind"` prints over `unattended.sh` in `tools/unattended/` lies inside
  `read_owner_door`'s body.
  Red when: a second path raises an owner question without the window.
- **AC3** — When the AC1 run-state file carries no `lease-utc` line, the dispatch prints
  `owner question — no run window: lease-utc absent` and the recorded argv holds no `--since`.
  Red when: a missing window passes an empty flag the door refuses, or is silent.
- **AC4** — When `grep -n "lease start"` runs over `tools/unattended/VERBS.template.md` and its render
  `memory/guides/UNATTENDED-VERBS.md`, each prints the hold line.
  Red when: the verbs guide still says the door reads the newest turn alone.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `recall floor` · `recall floor arms` · `kit epoch (shipped bytes move, the version moves)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 · a stub door recording argv behind a FORKED dispatch and a gated phase, staged by calling the door inline at the phase site without the window · none

## 8. Open questions

- **F1 — Where is the window attached?** Options: (a) one helper both driver paths call; (b) each call
  site; (c) an environment variable. (b) is the one-admission-path class; (c) leaks to every child.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the most feature-rich survivor, which also
  covers a later caller. widens: none · relaxes: none
- **F2 — Which binding line does a unit the spec audit promoted carry?** RESOLVED (agent, 2026-10-26,
  delegated): `**Derived:**` naming `PLAY-dClosedLoop-2`, rung 3, the precedent `TOOL-dBoundRoles-39`
  §8 F1 records. widens: none · relaxes: none
- **F3 — The units this one extends are unbuilt.** `TOOL-dFurnishedOrders-16` and `-26`, and
  TOOL-dBoundRoles-11 S6's FORKED case, are specced and unbuilt at `5ff43572`. RESOLVED (agent,
  2026-10-26, delegated): the build run re-grounds on each at the pass and stops this unit if a named
  section is still absent then, rung 1, the brief's rule for unbuilt parents. widens: none ·
  relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of the 20 unit specs, id 19
  (HIGH, item H1, shared with ids 3 and 52).

## 10. Reuse audit

The seams extended: the driver's run-state reader `fact` (`tools/unattended/unattended.sh:1359`),
already used for `session` and `lease-utc` at `:2406`, and unit 16's door call. `python
tools/codebase-map/reuse_lookup.py "pass the unattended run's lease start to a helper the driver
calls"` ranked `run`, `run_git`, `run_arms`, `extract_run_facts` (`tools/unattended/lib-unattended.sh`)
and `resolveLease` (`tools/unattended/run-lease.js`); `extract_run_facts` parses a whole record for the
status verbs and `resolveLease` serves the JS hooks, so `fact`, the driver's own one-key reader, is the
seam. The recall probe returned the audit's H1 text and TOOL-dBoundRoles-72, neither disagreeing with
source.

Recall terms used: `python tools/memory-recall/query.py "does the launch prompt of an unattended run
count as owner presence" --terms "attended owner turn typed keepalive launch prompt lease unattended
presence derive_attended hold"`
