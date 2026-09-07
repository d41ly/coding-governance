# TOOL-aReapedSpinner-4 — the reaper: walk the real edges, signal from the right namespace, VERIFY

**Status:** OPEN · rev-2 · 2026-09-08 · node a · Tier-2 · base e2b82a53 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round1.md](../reviews/2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round1.md) | spec-audit | TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-6 TOOL-aReapedSpinner-7 |

<!-- /gen:spec-records -->

## 1. Goal

Kill a flagged process AND its descendants, and prove each one died. This is the unit the whole
build exists for, and the only irreversible thing the kit does.

## 2. Scope (IN)

- **S1** — `tools/process-monitor/reap.py`, exposing `run_kill(pid, census, conf)` which walks the
  census's parent edges to the full descendant set, signals LEAVES FIRST, re-reads, and returns the
  killed set and the survivor set separately. Observed by AC1, AC2.
- **S2** — VERIFICATION: the return derives from a SECOND census read, never from the signal
  command's exit status. Observed by AC3.
- **S3** — the scope RE-CHECK with DESCENDANT INHERITANCE: a walked member is admissible when it is
  in scope standalone OR when an ancestor of it INSIDE THE SAME WALKED SET is. A set containing a
  member whose whole ancestor chain is out of scope REFUSES ENTIRELY. Observed by AC4, AC8.
- **S4** — the SIGNAL is issued through the MSYS `kill` binary resolved on `PATH`, in the MSYS pid
  namespace. Never `os.kill`, never `taskkill`. Observed by AC9, AC10.
- **S5** — `reap.py --sweep` OWNS the whole chain — census, fence, classify, then kill per mode —
  and prints the population, scoped, flagged, killed and survivor counts. `--dry-run` runs the same
  code path and signals nothing. Observed by AC5, AC6.
- **S6** — `PROCMON_REAP_MODE` gates the automatic path: `report` signals nothing, `reap-orphans`
  only `ORPHAN` rows, `reap-all` every flagged row. Observed by AC5.
- **S7** — `reap.py --kill <pid>` for the agent-directed case, under the same fence and the same
  verification, and NOT under the mode. Observed by AC7.

## 3. Non-goals (OUT)

- **No `taskkill /T` and no process-group kill.** Both measured wrong: `/T` reaped one process of
  four because it walks the WINDOWS tree, and every descendant of the test tree shared the caller's
  own pgid.
- **No `os.kill`, and this is the sharp one.** The resolved interpreter on this node reports
  `sys.platform == 'win32'`, so `os.kill` hands its integer to `TerminateProcess` against a WINDOWS
  pid — while every id in the census's edges is an MSYS pid. That is the mixed-namespace defect
  this build measured in `taskkill`, relocated into the unit the spec itself calls the only
  irreversible thing the kit does (D8).
- **No retry loop and no escalation ladder.** One signal, one verification, survivors reported.
- **No killing of a row this run did not classify.** `--kill <pid>` bypasses the MODE, never the
  FENCE.
- **No restart, no rescheduling, no cleanup of what a killed process left behind.**

### Edges

- **consumes-from** `TOOL-aReapedSpinner-1` — the `ppid` edges, and S7's row guard, without which a
  walked "id" may be a word from somebody's argv.
- **consumes-from** `TOOL-aReapedSpinner-2` — the fence, re-run per member at S3 rather than
  trusted. The inheritance rule is THIS unit's, because inheritance is only meaningful in a walked
  set; unit 2 §3 says so from its side.
- **consumes-from** `TOOL-aReapedSpinner-3` — the verdict vocabulary S6's modes name.
- **consumes-from** `TOOL-aReapedSpinner-6` — `PROCMON_REAP_MODE`.
- **hands-off** `TOOL-aReapedSpinner-5` — the hook reports what a sweep found; it never signals.
- **hands-off** `TOOL-aReapedSpinner-7` — the gate runner calls this unit on its INTERRUPT path,
  which currently kills nothing at all.

## 4. Design

### The walk

Build a child map from the census's `ppid` edges, collect the transitive descendants of the target,
order by DEPTH DESCENDING, signal each before the target itself. Leaves first, because killing a
parent first is what CREATES the orphans this kit exists to reap — measured, where killing the top
left all four descendants alive and one reparented to `ppid 1` in front of the probe.

**An already-orphaned process is NOT reachable by this walk**, by construction. That population is
found by the classifier over the whole table and killed as an individual target. Both mechanisms
are needed and neither substitutes for the other.

### What issues the signal, and why it is a scope item

The census's `pid` is an MSYS id. Measured on this node: `resolve_python` yields an interpreter
whose `sys.platform` is `win32`, reporting `os.getpid()` 7144 while the calling MSYS shell's `$$`
was 2581555 — two disjoint namespaces, with no arithmetic between them. So the signal is issued by
running the MSYS `kill` binary, which is the namespace the walk is in and the arm that killed 5 of
5 in this build's research record.

`kill` is RESOLVED, and an absent one REFUSES rather than falling back to `os.kill` — the fallback
would be silent, plausible, and would terminate whatever unrelated Windows process happens to hold
that integer.

### Descendant inheritance, and why the all-or-nothing check needed it

Unit 2 admits a row on its own command string. Measured: a staged descendant reads
`"…/usr/bin/sleep.exe" 45` and a real leg shell carries a relative script path — **neither names any
repo path.** Every realistic tree therefore contains a bare-argv leaf, so rev-1's rule (refuse the
whole kill if ANY member is out of scope) refused every real tree and the reaper could never kill
anything (D9).

The rule is now: a member inherits admissibility from an in-scope ancestor **within the walked
set**. The refusal S3 keeps is for a member whose whole ancestor chain is also out of scope, which
is the case the refusal was actually written for — a walk that has wandered out of the tree.

Inheritance does not weaken the fence: the ROOT of the walk is still graded standalone, and a root
that is not admissible is refused before any walk happens.

### Verification is a re-read

`kill -9` returns success for a signal DELIVERED, and `taskkill` printed `SUCCESS` while killing one
of four. The survivor set is `walked ∩ still-present` from a second census, REPORTED rather than
retried.

### Files touched (estimate)

`tools/process-monitor/reap.py` new; arms added to `tools/process-monitor/selftest.py`.

## 5. Production-readiness checklist

- security — the only irreversible action in the kit. Guarded by S3's re-check, S4's namespace
  rule, and S6's default mode, which unit 6 §8 resolves to `reap-orphans` conditionally on unit 2's
  program-path matching.
- perf / scale — one extra census per kill, ~1.2 s on Windows, on a path that only runs when
  something is already wrong.
- error / empty / loading states — an empty walked set prints "nothing to reap"; a census that
  cannot be read exits non-zero having signalled nothing; an unresolvable `kill` refuses.
- observability — killed and survivor sets returned and printed separately, never summed.
- risks — killing something wanted. Mitigated by the fence re-check, the namespace rule, the mode
  default, `--dry-run`, and by never inferring scope from a process name.
- testing — arms stage a REAL disposable tree whose leaf argv names no root, kill it, and assert
  zero survivors; plus an arm injecting a member whose whole chain is out of scope and asserting
  nothing was killed.
- migration — none.
- user docs — the kit README's reap section, unit 6.

## 6. Acceptance criteria

- **AC1** — When a disposable three-deep tree is staged — `bash` → `bash -c` → `sleep`, the shape
  from the research record, whose leaf argv names NO declared root — and `run_kill` targets its
  root, the second census contains none of its members. Observed by `selftest.py`, arm
  `test_tree_dies_completely_with_bare_argv_leaves`.
  Red when: the target is signalled and the descendants survive (the measured `kill -9 <top>`
  behaviour), or the bare-argv leaf is refused and the whole kill aborts (D9).
  `fixture:` the arm creates its own tree under the scratch root and declares that root.
- **AC2** — When the walked set is computed for that tree, its members are ordered depth-descending
  and the root is last. Observed by `selftest.py`, arm `test_leaves_are_killed_first`.
  Red when: the order is the map's insertion order, which kills the parent first and manufactures
  the orphans this unit removes.
- **AC3** — When a kill is staged against a member that cannot be signalled, `run_kill` reports it
  as a SURVIVOR even though the signal command exited 0. Observed by `selftest.py`, arm
  `test_survivor_is_derived_from_a_re_read`.
  Red when: the return is built from the signal command's exit status, which reported `SUCCESS`
  over a 25%-effective kill in this build's research record.
- **AC4** — When a member whose WHOLE ancestor chain is out of scope is injected into the walked
  set, `run_kill` refuses, names that member, and the staged tree is still ALIVE afterwards.
  Observed by `selftest.py`, arm `test_wholly_out_of_scope_member_aborts_the_kill`.
  Red when: the admissible subset is killed anyway, leaving a partial kill reported as success.
- **AC5** — When `PROCMON_REAP_MODE=report`, a `--sweep` over a staged flagged tree signals nothing
  and still prints the flagged rows; under `reap-orphans` it kills the `ORPHAN` rows only; under
  `reap-all` every flagged row. Observed by `selftest.py`, arm `test_mode_bounds_the_act`.
  Red when: any mode kills a row the classifier did not flag.
- **AC6** — When `--sweep --dry-run` runs against a staged flagged tree: the tree is ALIVE
  afterwards, the dry run's WALKED set equals the real run's walked set over the same staging, and
  the dry run's survivor set equals its own walked set. Observed by `selftest.py`, arm
  `test_dry_run_walks_the_same_set_and_kills_nothing`.
  Red when: the dry path takes a different code path from the real sweep. rev-1 demanded the two
  stdouts be "byte-identical", which is unsatisfiable — after a real sweep the survivor set is
  empty and after a dry one it is everything — so it would have landed as a quietly weakened
  comparison that still read as verified (D7).
- **AC7** — When `reap.py --kill <pid>` names a pid whose chain is out of scope, it refuses and
  exits non-zero regardless of `PROCMON_REAP_MODE`. Observed by `selftest.py`, arm
  `test_explicit_kill_still_obeys_the_fence`.
  Red when: the explicit path bypasses the fence along with the mode, making every safety property
  in unit 2 optional.
- **AC8** — When the ROOT of a walk is itself out of scope, `run_kill` refuses before walking
  anything. Observed by `selftest.py`, arm `test_out_of_scope_root_is_refused_before_the_walk`.
  Red when: inheritance is applied to the root, which would let any in-scope descendant drag an
  arbitrary parent into the kill set.
- **AC9** — When a staged MSYS process is killed, it is dead by re-read; and an arm asserts the
  signal was issued by the resolved MSYS `kill` binary, by shimming that binary and observing the
  shim ran. Observed by `selftest.py`, arm `test_signal_goes_through_the_msys_kill_binary`.
  Red when: the signal is issued via `os.kill`, which on this node's `win32` interpreter targets a
  DIFFERENT pid namespace and would terminate an unrelated Windows process (D8).
- **AC10** — When no `kill` binary resolves on `PATH`, `run_kill` REFUSES and signals nothing.
  Observed by `selftest.py`, arm `test_absent_kill_binary_refuses`.
  Red when: it falls back to `os.kill`, which is the silent, plausible, wrong-namespace path.

## 7. Gates

`line length` · `lexicon naming predicates` · `govkit selfcheck` · `dead-path carriers (deleted files still named)`

New arm: `tools/process-monitor/selftest.py` · stages a live disposable tree with bare-argv leaves
under the scratch root, an unsignalable member, a wholly-out-of-scope member, an out-of-scope root,
a shimmed `kill` binary, an absent `kill` binary, and each reap mode · floor moves with unit 1's
arms, one suite.

New arm: a `namespace ban` leg over `tools/process-monitor/` · refuses any occurrence of `os.kill(`
or a `taskkill` invocation, with the reason in the leg header · it is a CLASS ban, not an instance
fix, and it survives the next author who reaches for the obvious stdlib call.

## 8. Open questions

- **F1 — one signal or a TERM-then-KILL ladder?**
  RESOLVED (agent, 2026-09-08, delegated): ONE signal, the forceful one. A ladder needs a wait
  between rungs, and a timed wait inside the observer is what this build's own rules forbid. The
  population is processes hours past a deadline with, in the reaped class, no live parent to flush
  anything for. Vetoes clean.
- **F2 — should a survivor red the sweep's exit status?**
  RESOLVED (agent, 2026-09-08, delegated): YES, non-zero. A survivor is precisely the state a human
  must see and the state this build was opened over; reporting survivors and exiting 0 is the
  reassuring-zero class one level up.
- **F3 — should the walk inherit `scan_descendants`'s depth cap of 8?**
  RESOLVED (agent, 2026-09-08, delegated): NO CAP, but a CYCLE GUARD. The cap exists there because
  a `ps` table that disagrees with itself mid-write must cost a truncated tree rather than a spin;
  this unit gets the same guarantee from a visited-set, which terminates on any finite table
  without discarding a deep tree. Recorded because unit 7's fix removes that cap's protection for
  the runner too, and the two must not disagree.

## 9. Revision log

- rev-1 · 2026-09-08 · initial draft.
- rev-2 · 2026-09-08 · S3 · S4 · S5 · §3 · §4 · AC1 · AC4 · AC6 · AC8 · AC9 · AC10 · §7 · §8 F3 ·
  §10 · folded spec-audit round 1. D8: S4 names the MSYS `kill` binary as the signal, §3 bans
  `os.kill` with the measured namespace evidence, AC9/AC10 stage it, and a class-ban leg joins §7.
  D9: S3 gains descendant inheritance within the walked set — rev-1's all-or-nothing rule refused
  every real tree because a leaf's argv names no root — with AC1 staging bare-argv leaves and AC8
  keeping the root graded standalone. D7: AC6 replaces an unsatisfiable byte-identity comparison
  with walked-set equality plus a live-tree assertion. D5: S5 takes ownership of the full chain,
  which rev-1 split between this unit and unit 3.

## 10. Reuse audit

**No existing seam fits for the reaper as a whole, but the corpus already holds a walk-kill-verify
mechanism and rev-1's rejection of THAT was false.** `python tools/codebase-map/reuse_lookup.py "kill a hung or idle background process and report
it to the session"` returned no such mechanism, and the reason is recorded rather than trusted:
that probe's own coverage line reads `unscanned layers: .sh`, so a shell function is invisible
to it. The grep that found it was
`grep -n "remove_descendants\|scan_descendants" tools/run-gates/run-gates.sh`.
`tools/run-gates/run-gates.sh:445-468` is `remove_descendants`: it snapshots `ps -ef` at `:447`,
walks ppid edges via `scan_descendants` at `:428-443`, SIGKILLs every member at `:451`, re-reads
with `kill -0` at `:466-468` and reports survivors. rev-1's §10 rejected it because it "kills only
pids it recorded, so it cannot reach a grandchild", explicitly "verified against source at BASE" —
and the file's own header at `:416-417` says the opposite: "The wall kills RECORDED PER-LEG PIDS
and their descendants." The secondary ground, that extending it would mean giving the runner a
process-table reader, is false too: it has one at `:447` (D12).

**The four corrections that mechanism carries are inherited here by id rather than rediscovered:**
the snapshot taken before any kill because killing a parent reparents its children (`:419-421`,
which is why S1 walks one census rather than re-reading per level); the numeric field guard
(`:432-436`, which unit 1 S7 now owns); the depth-8 bound (`:429`, addressed in §8 F3); and the
survivor report carrying the walk's only liveness assertion (`:453-470`, corrected in
`TOOL-aQuenchedHarness-7` after an `rm` in the wrong place made it decorative — the same class as
this unit's AC3).

**What this unit genuinely ADDS**, and why it is not an extension of that function: leaves-first
ordering; verification returned as a value rather than printed as a message; the scope fence; the
MSYS-namespace signal rule; and no depth cap. Those change the semantics and cost of every existing
caller of `remove_descendants`, which is the gate runner's hot failure path, so the dependency is
inverted instead — unit 7 has the runner call THIS, which is also what gets its interrupt path
covered.

Recall terms used: `gate runner wall clock bound timeout kill children orphan process leg pool
watchdog GATE_WALL background subprocess reaper`
