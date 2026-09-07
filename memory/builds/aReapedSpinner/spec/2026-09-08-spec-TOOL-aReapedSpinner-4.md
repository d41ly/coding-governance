# TOOL-aReapedSpinner-4 — the reaper: walk the real edges, kill leaves first, VERIFY

**Status:** OPEN · rev-1 · 2026-09-08 · node a · Tier-2 · base e2b82a53 · streams tooling · order 4

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

Kill a flagged process AND its descendants, and prove each one died. This is the unit the whole
build exists for, and it is the only irreversible thing the kit does.

## 2. Scope (IN)

- **S1** — `tools/process-monitor/reap.py`, exposing `run_kill(pid, census, conf)` which walks the
  census's parent edges to the full descendant set, kills LEAVES FIRST, re-reads, and returns the
  killed set and the survivor set separately. Observed by AC1, AC2.
- **S2** — VERIFICATION: the return is derived from a second census read, never from the kill
  command's exit status. Observed by AC3.
- **S3** — the scope RE-CHECK: every pid in the walked set is re-graded through unit 2's fence
  immediately before the kill, and a set containing any out-of-scope pid REFUSES ENTIRELY rather
  than killing the admissible subset. Observed by AC4.
- **S4** — `PROCMON_REAP_MODE` gates what the automatic path may touch: `report` kills nothing,
  `reap-orphans` kills only `ORPHAN` rows, `reap-all` kills every flagged row. Observed by AC5.
- **S5** — `reap.py --sweep` runs the whole chain (census → fence → classify → kill per mode) and
  prints what it killed and what survived. `--dry-run` prints the same and kills nothing. Observed
  by AC6.
- **S6** — an explicit `reap.py --kill <pid>` for the agent-directed case, subject to the same
  fence and the same verification, and NOT subject to the mode. Observed by AC7.

## 3. Non-goals (OUT)

- **No `taskkill /T` and no process-group kill.** Both are measured wrong in this build's research
  record: `/T` reaped one process of four because it walks the Windows tree, and every descendant of
  the test tree shared the caller's own pgid.
- **No retry loop and no escalation ladder.** One signal, one verification, survivors reported. A
  process that survives `kill -9` is a fact for a human, not something to spin on.
- **No killing of a row this run did not classify.** `--kill <pid>` still requires the pid to be in
  scope; it bypasses the MODE, never the FENCE.
- **No restart, no rescheduling, no cleanup of anything the killed process left behind.**

### Edges

- **consumes-from** `TOOL-aReapedSpinner-1` — the `ppid` edges. The unit is correct only because
  those edges are in the KILLABLE namespace; a census supplying Windows parents would make this
  walk find nothing.
- **consumes-from** `TOOL-aReapedSpinner-2` — the fence, re-run per pid at S3 rather than trusted.
- **consumes-from** `TOOL-aReapedSpinner-3` — the verdict vocabulary, which S4's modes name.
- **consumes-from** `TOOL-aReapedSpinner-6` — `PROCMON_REAP_MODE`.
- **hands-off** `TOOL-aReapedSpinner-7` — the gate runner calls `run_kill` instead of killing a
  recorded pid, which is what makes its grandchildren reachable.

## 4. Design

### The walk

Build a child map from the census's `ppid` edges, collect the transitive descendants of the target,
order them by DEPTH DESCENDING, and signal each in that order before the target itself. Leaves
first, because killing a parent first is exactly what leaves the orphans this kit exists to reap —
measured in the research record, where killing the top left all four descendants alive and one of
them reparented to `ppid=1` in front of the probe.

**A process already orphaned is NOT reachable by this walk**, by construction: nothing points at it
any more. That population is found by the classifier over the whole table and killed as an
individual target. Both mechanisms are needed and the split is stated here so a reader does not
expect the walk to cover it.

### Verification is a re-read, not an exit status

`kill -9` returns success for a signal DELIVERED, and `taskkill` printed `SUCCESS` while killing one
process of four. So the only honest answer to "did it die" is a second census. The survivor set is
`walked ∩ still-present`, and it is REPORTED rather than retried.

### The fence re-check, and why it refuses the whole set

A partial kill on a set containing an out-of-scope pid would be the worst outcome available: some
of the intended tree dead, an unrelated process left flagged, and a report that looks like a
success. So an inadmissible member aborts the whole call, names the offending pid, and kills
nothing. This is the `containment-tested-one-way` class applied to the act rather than to the
predicate.

### Files touched (estimate)

`tools/process-monitor/reap.py` new.

## 5. Production-readiness checklist

- security — the only irreversible action in the kit. Guarded by S3's re-check and by S4's default
  mode, which unit 6 §8 resolved to `reap-orphans` rather than `reap-all`.
- perf / scale — one extra census per kill call, ~1.2 s on Windows. Acceptable: a sweep runs on a
  throttle, not per tool call.
- error / empty / loading states — an empty walked set is a legitimate answer and prints "nothing
  to reap"; a census that cannot be read exits non-zero without killing anything.
- observability — killed and survivor sets are returned and printed separately, never summed into
  one count.
- risks — killing something wanted. Mitigated by the fence re-check, the mode default, `--dry-run`,
  and by never inferring scope from a process name.
- testing — arms stage a real disposable tree, kill it, and assert zero survivors; plus an arm
  staging an out-of-scope pid inside the walked set and asserting NOTHING was killed.
- migration — none.
- user docs — the kit README's reap section, unit 6.

## 6. Acceptance criteria

- **AC1** — When a disposable three-deep tree is staged and `run_kill` targets its root, the second
  census contains none of its members. Observed by `selftest.py`, arm `test_tree_dies_completely`.
  Red when: the target is signalled and the descendants survive — the measured `kill -9 <top>`
  behaviour this unit exists to replace.
  `fixture:` the arm creates its own `sleep` tree under the scratch root and declares that root, so
  it never depends on the ambient process table.
- **AC2** — When the walked set is computed for that tree, its members are ordered depth-descending
  and the root is last. Observed by `selftest.py`, arm `test_leaves_are_killed_first`.
  Red when: the order is the map's insertion order, which kills the parent first and manufactures
  the orphans this unit is meant to remove.
- **AC3** — When a kill is staged against a pid that cannot be signalled, `run_kill` reports it as
  a SURVIVOR even though the kill command exited 0. Observed by `selftest.py`, arm
  `test_survivor_is_derived_from_a_re_read`.
  Red when: the return is built from the kill command's exit status, which reported `SUCCESS` over
  a 25%-effective kill in this build's research record.
- **AC4** — When one out-of-scope pid is injected into the walked set, `run_kill` refuses, names
  that pid, and the staged tree is still ALIVE afterwards. Observed by `selftest.py`, arm
  `test_out_of_scope_member_aborts_the_whole_kill`.
  Red when: the admissible subset is killed anyway, leaving a partial kill reported as success.
- **AC5** — When `PROCMON_REAP_MODE=report`, a `--sweep` over a staged flagged tree kills nothing
  and still prints the flagged rows; under `reap-orphans` it kills the `ORPHAN` rows only; under
  `reap-all` it kills every flagged row. Observed by `selftest.py`, arm `test_mode_bounds_the_act`.
  Red when: any mode kills a row the classifier did not flag.
- **AC6** — When `reap.py --sweep --dry-run` runs against a staged flagged tree, the tree is alive
  afterwards and the stdout is byte-identical to the non-dry run's except for its mode banner.
  Observed by `selftest.py`, arm `test_dry_run_kills_nothing`.
  Red when: `--dry-run` takes a different code path from the real sweep, which makes it a rehearsal
  of something other than what runs.
- **AC7** — When `reap.py --kill <pid>` names an out-of-scope pid, it refuses and exits non-zero
  regardless of `PROCMON_REAP_MODE`. Observed by `selftest.py`, arm
  `test_explicit_kill_still_obeys_the_fence`.
  Red when: the explicit path is written to bypass the fence along with the mode, which would make
  every safety property in unit 2 optional.

## 7. Gates

`line length` · `lexicon naming predicates` · `govkit selfcheck` · `dead-path carriers (deleted files still named)`

New arm: `tools/process-monitor/selftest.py` · stages a live disposable tree under the scratch
root, an unsignalable pid, an injected out-of-scope pid, and each reap mode · floor moves with unit
1's arms, one suite.

## 8. Open questions

- **F1 — one signal or a TERM-then-KILL ladder?**
  RESOLVED (agent, 2026-09-08, delegated): ONE signal, the forceful one. A ladder needs a wait
  between rungs, and a timed wait inside the observer is what this build's own rules forbid. The
  population is processes already hours past a deadline with, in the reaped class, no live parent
  to flush anything for — there is nothing a graceful stop preserves. Vetoes clean; the tie-break
  is fewer open questions.
- **F2 — should a survivor red the sweep's exit status?**
  RESOLVED (agent, 2026-09-08, delegated): YES, non-zero, because a survivor is precisely the state
  a human must see and the state this whole build was opened over. A sweep that reports survivors
  and exits 0 is the reassuring-zero class one level up.

## 9. Revision log

- rev-1 · 2026-09-08 · initial draft.

## 10. Reuse audit

No existing seam fits, and the nearest candidate was examined and REJECTED with evidence.
`tools/run-gates/run-gates.sh:435-468` holds a kill loop with a survivor list — structurally the
closest thing in the corpus — but its own header at `:412-414` records that it has no process group
to signal and it kills only pids it recorded, so it cannot reach a grandchild. Extending it would
mean giving the gate runner a process-table reader, which is this kit's job; unit 7 inverts the
dependency instead and has the runner call `run_kill`. Verified against source at BASE rather than
taken from the recall hit.

Recall terms used: `gate runner wall clock bound timeout kill children orphan process leg pool
watchdog GATE_WALL background subprocess reaper`
