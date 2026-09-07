# TOOL-aReapedSpinner-7 — the gate runner reaps its own TREE, not just the pid it recorded

**Status:** OPEN · rev-1 · 2026-09-08 · node a · Tier-2 · base e2b82a53 · streams tooling · order 5

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Close the defect the owner's prompt opens with. `tools/run-gates/run-gates.sh` kills the leg pids it
recorded and its own header explains why it cannot do better; the result is that every wall breach
and every interrupted bar leaves a layer of grandchildren running. Have it call the reaper instead,
where the reaper is present.

## 2. Scope (IN)

- **S1** — the runner's kill path delegates to `reap.py --kill <pid>` for each outstanding leg,
  which walks that leg's descendants and verifies. Observed by AC1.
- **S2** — CONDITIONAL delegation: the runner detects the monitor and falls back to its current
  behaviour when it is absent, because an adopter may install `run-gates` and not this kit.
  Observed by AC2.
- **S3** — the fallback ANNOUNCES itself. A bar that reaped only pids prints one line saying the
  tree was not walked, so a survivor is never mistaken for a clean stop. Observed by AC3.
- **S4** — the runner's existing survivor report is kept and now carries the walked count beside
  the killed count, so the two numbers are visible separately. Observed by AC4.
- **S5** — the same delegation on the INTERRUPT path, not only the wall-breach path — a bar stopped
  by a signal leaks exactly the same way. Observed by AC5.

## 3. Non-goals (OUT)

- **No change to WHEN the runner kills.** The wall, the per-leg ceiling and the turnstile decide
  that today and this unit does not touch them. It changes only WHAT dies when they fire.
- **No new dependency from `run-gates` to the monitor.** S2's detection is what keeps the runner
  installable alone; a hard import would couple two kits the deployer ships separately.
- **No process-group kill and no `set -m`.** The runner's header records why it has neither, and
  this build's research record measures that the group is the caller's own.
- **No retry of the existing kill loop's semantics.** One signal, verified, survivors reported —
  unit 4's contract, inherited rather than re-litigated here.

### Edges

- **consumes-from** `TOOL-aReapedSpinner-4` — `run_kill`, and its guarantee that the walk is over
  the killable namespace.
- **consumes-from** `TOOL-aReapedSpinner-2` — transitively: the reaper re-checks the fence, so the
  runner's declared roots must admit its own scratch dirs or the delegation refuses. This is the
  interaction most likely to surprise, and AC6 observes it.
- **hands-off** external — the unattended driver's `GATE_BOUND` path wraps the whole bar rather
  than individual legs, and is NOT changed here. Named as a follow-up rather than silently left.

## 4. Design

### Where it hooks in

`tools/run-gates/run-gates.sh:435-468` holds the existing loop: a pid validation, `kill -9 "$p"`,
then a `kill -0` survivor sweep collecting `left`. The change is inside that loop — replace the
single `kill -9` with the delegated call, keep the survivor sweep exactly as it is, and add the
walked count to what it prints.

Keeping the survivor sweep matters: it is an INDEPENDENT verification of the reaper's own, and unit
4 §4 makes the same argument about not trusting an exit status. Two verifications by two mechanisms
is not duplication here, it is the guard not sharing a variable with the thing it guards.

### Detection

Presence of `tools/process-monitor/reap.py` AND a readable `.process-monitor.conf`. Both, because
the reaper refuses on a blank `PROCMON_ROOTS` and a runner that discovers that mid-kill would be
reporting a monitoring fault as a gate fault. Detection resolves once, before the first leg is
dispatched, so the announcement in S3 is printed with the profile line rather than at kill time.

### The roots interaction

The runner's heavy legs run in `mktemp -d` scratch repos, not in the tree, so their command strings
name a temp path. If `PROCMON_ROOTS` does not include the scratch root, the reaper refuses every
leg pid and the runner falls back — correctly, but silently unless S3 speaks. `.process-monitor.conf`
therefore ships this repo's own scratch root in its declared roots, and the README says why.

### Files touched (estimate)

Edited: `tools/run-gates/run-gates.sh` (the kill loop, the detection line, the trap path). Edited:
`.process-monitor.conf` (the scratch root, if unit 6 did not already declare it). New arm in
`tools/run-gates/run-gates.test.sh`.

## 5. Production-readiness checklist

- security — the runner gains no authority it did not have; it already killed processes. What
  changes is that the kill now reaches the descendants it was always meant to.
- perf / scale — one census per kill, on a path that only runs when a bar is already failing. No
  cost on a green bar.
- error / empty / loading states — monitor absent → announced fallback (S3); monitor present but
  refusing → announced fallback, same line, different reason.
- observability — walked and killed counts printed separately (S4).
- risks — the highest-risk file in this build. A defect here reds or wedges the merge bar for every
  session. Mitigated by the conditional path defaulting to today's exact behaviour and by AC2
  staging the monitor's absence directly.
- testing — the runner's suite already stages a sleeping leg and a wall breach; the new arm extends
  that fixture to a leg with a GRANDCHILD and asserts the grandchild dies.
- migration — none. A tree without the monitor behaves exactly as it does today.
- user docs — `tools/run-gates/README.md` gains the delegation note; the charter's bar section is
  unchanged, because the leg list and the bar's behaviour are unaffected.

## 6. Acceptance criteria

- **AC1** — When a bar is staged whose leg spawns a grandchild and the wall fires, the grandchild is
  gone afterwards. Observed by `run-gates.test.sh`, arm `test_wall_breach_reaps_the_grandchild`.
  Red when: only the recorded leg pid dies — today's behaviour, and the defect the prompt opens
  with.
  `fixture:` a scratch bar with a `sleeper` leg that itself backgrounds a `sleep`, built the way
  the existing turnstile fixture builds its own.
- **AC2** — When the same fixture runs with `reap.py` absent, the bar still
  kills its recorded pids, still reports survivors, and exits with the same status as before this
  change. Observed by `run-gates.test.sh`, arm `test_absent_monitor_falls_back_unchanged`.
  Red when: the runner errors or hangs because the monitor is missing, which would break every
  adopter that installs `run-gates` alone.
- **AC3** — When the monitor is absent OR refusing, the run prints a line naming which, and the line
  appears with the profile line rather than at kill time. Observed by `run-gates.test.sh`, arm
  `test_fallback_announces_itself`.
  Red when: the fallback is silent, which makes a leaked grandchild indistinguishable from a clean
  stop — the announced-skip rule the charter states in §7.
- **AC4** — When a kill runs with the monitor present, the runner's report names the walked count
  and the killed count as separate figures. Observed by `run-gates.test.sh`, arm
  `test_walked_and_killed_are_reported_apart`.
  Red when: the two are summed, which hides a walk that found nothing.
  `figure:` DERIVED — both counts come from the reaper's return, not from a literal.
- **AC5** — When the staged bar is interrupted rather than wall-breached, the grandchild is gone
  afterwards. Observed by `run-gates.test.sh`, arm `test_interrupt_path_reaps_the_tree_too`.
  Red when: the delegation is wired into the wall branch only, leaving the signal path leaking —
  which is how the `TaskStop`-stopped runner in the prompt kept its sweep and kit children.
- **AC6** — When `PROCMON_ROOTS` does not admit the runner's scratch root, the bar falls back and
  announces it, and does NOT report a gate failure. Observed by `run-gates.test.sh`, arm
  `test_unadmitted_scratch_root_is_a_fallback_not_a_gate_failure`.
  Red when: a monitoring refusal is surfaced as a red leg, which would make a misconfigured conf
  block every push.

## 7. Gates

`run-gates wiring` · `line length` · `govkit selfcheck` · `dead-path carriers (deleted files still named)`

New arm: `tools/run-gates/run-gates.test.sh` · stages a leg with a grandchild, an absent monitor, a
refusing monitor, and the interrupt path · this suite carries an assertion floor in `ARMS_FLOORS`
and it MOVES with these arms; the floor is read from `.memory-tree.conf` at the time of the change
rather than written here, since a literal would be stale on the next arm anyone adds.

## 8. Open questions

- **F1 — should the unattended driver's `GATE_BOUND` path delegate too?**
  RESOLVED (agent, 2026-09-08, delegated): NOT IN THIS UNIT. That bound wraps the whole bar as one
  child, so the runner's own trap is what fires first and this unit already fixes that. Delegating
  there as well would put two reapers on one tree with no ordering between them. Recorded in §3 as
  a follow-up rather than built, which is the tie-break on fewer open questions.

## 9. Revision log

- rev-1 · 2026-09-08 · initial draft.

## 10. Reuse audit

`python tools/codebase-map/reuse_lookup.py "kill a hung or idle background process and report it
to the session"` returned no seam for the kill itself, but the seam this unit EXTENDS was already
known and is cited directly: `tools/run-gates/run-gates.sh`'s existing kill loop at `:435-468`,
cited by path and verified against source at BASE — the pid validation, the `kill -9`, and the
`kill -0` survivor sweep are all kept, and only the signal itself is replaced by the delegated
walk. The recall probe returned this exact region as its second and eighth hits, both from
`aPacedTurnstile` and `aPooledSweep` review records, and both confirm the same finding from the
other side: no process group exists to signal, so descendants survive. Those records are the
evidence that the seam is the right one and that the fix is not "add `set -m`", which was
considered and rejected there.

Recall terms used: `gate runner wall clock bound timeout kill children orphan process leg pool
watchdog GATE_WALL background subprocess reaper`
