# TOOL-aReapedSpinner-4 — the reaper: walk both graphs, signal per kind, VERIFY

**Status:** OPEN · rev-3 · 2026-09-08 · node a · Tier-2 · base e2b82a53 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-08-build-TOOL-aReapedSpinner-4-signal-namespace-measured.md](../build/2026-09-08-build-TOOL-aReapedSpinner-4-signal-namespace-measured.md) | research | TOOL-aReapedSpinner-1 |
| [2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round1.md](../reviews/2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round1.md) | spec-audit | TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-6 TOOL-aReapedSpinner-7 |
| [2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round2.md](../reviews/2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round2.md) | spec-audit | TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-6 TOOL-aReapedSpinner-7 |

<!-- /gen:spec-records -->

## 1. Goal

Kill a flagged process and its descendants, and prove each one died. This is the unit the build
exists for, and the only irreversible thing the kit does.

## 2. Scope (IN)

- **S1** — `tools/process-monitor/reap.py`, exposing `run_kill(winpid, census, scope_set, conf)`
  which walks the census's UNION parent graph to the descendant set, signals LEAVES FIRST, re-reads,
  and returns the killed and survivor sets separately. Observed by AC1, AC2.
- **S2** — VERIFICATION derives from a SECOND census read, never from a signal command's exit
  status. Observed by AC3.
- **S3** — the MEMBERSHIP test: every walked member must be in `scope_set`, the set unit 2 computed
  once over the whole census. A member outside it is DROPPED from the kill set and REPORTED; the
  call refuses entirely only when the walk ROOT is outside it. Observed by AC4, AC8.
- **S4** — the SIGNAL is chosen per row: MSYS `kill` for a row MSYS can address, else
  `taskkill //PID <winpid> //F` — the SINGLE-PID form, never `/T`. An unresolvable signal binary for
  a row's kind REFUSES for that row and reports it. Observed by AC9, AC10, AC11.
- **S5** — `reap.py --sweep` owns the whole chain — census, scope, classify, kill per mode — and
  prints the census, scoped, flagged, killed and survivor counts, all derived. `--dry-run` runs the
  same code path and signals nothing. Observed by AC5, AC6, AC12.
- **S6** — `PROCMON_REAP_MODE` gates the automatic path: `report` signals nothing, `reap-orphans`
  only `ORPHAN` rows, `reap-all` every flagged row. Observed by AC5.
- **S7** — `reap.py --kill <winpid>` for the agent-directed case, under the same membership test and
  verification, and NOT under the mode. Observed by AC7.

## 3. Non-goals (OUT)

- **No `taskkill /T`.** Measured: it printed `SUCCESS` and killed one process of four, because it
  walks the WINDOWS tree and MSYS parent edges are a different graph. S4 uses the SINGLE-PID form,
  which in both of this build's records killed exactly the process named. The kit does its own walk.
- **No process-group kill.** Every descendant of a staged tree shared the caller's own pgid.
- **No single signal for the whole population.** Measured: a native `PING.EXE` that this shell did
  NOT spawn survived both the bash builtin `kill` and `/usr/bin/kill` with `No such process` and
  died only to `taskkill //PID`; the same binary spawned BY the shell died to `kill`. The predicate
  is not nativeness, it is whether MSYS can address the row (D21).
- **No `os.kill`.** The resolved interpreter reports `sys.platform == 'win32'`, so it would hand its
  integer to `TerminateProcess` against a WINDOWS pid while a caller supplied an MSYS one.
- **No per-member scope re-derivation.** rev-2 re-checked each member with an inheritance clause
  that admitted every member unconditionally (D17). Membership in a precomputed set cannot be
  vacuous that way, and unit 2 §3 says the derivation is its own.
- **No retry loop, no escalation ladder, no restart, no cleanup of what a killed process left.**

### Edges

- **consumes-from** `TOOL-aReapedSpinner-1` — both parent graphs, `kind`, `winpid`, and the row
  guard without which a walked id may be a word from somebody's argv.
- **consumes-from** `TOOL-aReapedSpinner-2` — `derive_scope`'s set. The reaper tests membership and
  derives nothing.
- **consumes-from** `TOOL-aReapedSpinner-3` — the verdict vocabulary S6's modes name.
- **consumes-from** `TOOL-aReapedSpinner-6` — `PROCMON_REAP_MODE`.
- **hands-off** `TOOL-aReapedSpinner-5` — the hook reports what a sweep found; it never signals.
- **hands-off** `TOOL-aReapedSpinner-7` — the gate runner calls this on its INTERRUPT path, which
  kills nothing at all today.

## 4. Design

### The walk

Build a child map from `win_ppid ∪ msys_ppid`, collect the transitive descendants of the target,
order by DEPTH DESCENDING, signal each before the target. Leaves first, because killing a parent
first is what CREATES the orphans this kit reaps — measured, killing the top left all four
descendants alive and one reparented in front of the probe. A visited-set terminates the walk on any
finite table, which is the guarantee `run-gates.sh:429`'s depth-8 cap buys there without discarding
a deep tree here (§8 F3).

**An already-orphaned process is NOT reachable by this walk**, by construction. That population is
found by the classifier over the whole table and killed as an individual target. Both mechanisms are
needed and neither substitutes for the other.

### The signal, per row

| row | signal | why |
|---|---|---|
| MSYS can address it | the resolved MSYS `kill` binary | the namespace the MSYS edges are in; the arm that killed 5 of 5 |
| MSYS cannot | `taskkill //PID <winpid> //F` | the only thing that killed a non-child native process |

The kind test is OPERATIONAL, not a label: `kill -0 <msys_pid>` answering is what makes MSYS the
signal for that row. A row that answers neither probe is reported unsignalable rather than signalled
hopefully — that is AC11, and it is the reason unit 1 AC11 exists on the census side.

### Membership, and why the vacuity is gone

Unit 2 computes the in-scope set once, as the descendant closure of attributable roots with
start-time-corroborated edges. This unit tests `winpid in scope_set`. There is no inheritance clause
here to be vacuous, and there is a reachable refusal: a walked member outside the set is DROPPED and
reported, which happens whenever the two reads disagree — a process that started between them, or
one whose edge failed corroboration.

The whole-call refusal is kept ONLY for a root outside the set, which is a caller error rather than
a race.

### Verification is a re-read

`kill -9` returns success for a signal DELIVERED, and `taskkill /T` printed `SUCCESS` over one death
of four. The survivor set is `walked ∩ still-present` from a second census, REPORTED not retried.

### Files touched (estimate)

`tools/process-monitor/reap.py` new; arms added to `tools/process-monitor/selftest.py`.

## 5. Production-readiness checklist

- security — the only irreversible action in the kit. Guarded by S3's membership test, S4's per-row
  signal rule, and S6's default mode, which unit 6 §8 F1 makes conditional on unit 2's tokenizer.
- perf / scale — one extra census per kill, ~1.2 s, on a path that only runs when something is
  already wrong.
- error / empty / loading states — an empty walked set prints "nothing to reap"; an unreadable
  census exits non-zero having signalled nothing; an unresolvable signal binary refuses per row.
- observability — killed, survivor, dropped and unsignalable sets returned and printed separately,
  never summed.
- risks — killing something wanted. Mitigated by membership, the per-row signal, the mode default,
  `--dry-run`, and never inferring scope from a process name.
- testing — arms stage a REAL mixed-namespace tree with bare-argv leaves, kill it, assert zero
  survivors; plus a native process this shell did not spawn.
- migration — none.
- user docs — the kit README's reap section, unit 6.

## 6. Acceptance criteria

- **AC1** — When a tree is staged as `bash → bash -c → sleep` PLUS a native `python -c` grandchild
  the shell did not directly spawn, and `run_kill` targets its root, the second census contains
  none of them, and the walked-set size equals the fixture's own process count. Observed by
  `selftest.py`, arm `test_mixed_namespace_tree_dies_completely`.
  Red when: only the MSYS members die — rev-2's graph was MSYS-only and structurally could not see
  the native grandchild (D22) — or the walk is silently truncated and reports a small green set.
  `fixture:` the arm creates its own tree under the scratch root; the two-namespace shape is a
  FLOOR, not an option.
- **AC2** — When the walked set is computed for that tree, members are ordered depth-descending and
  the root is last. Observed by `selftest.py`, arm `test_leaves_are_killed_first`.
  Red when: insertion order is used, which kills the parent first and manufactures orphans.
- **AC3** — When a member cannot be signalled, `run_kill` reports it a SURVIVOR even though the
  signal command exited 0. Observed by `selftest.py`, arm
  `test_survivor_is_derived_from_a_re_read`.
  Red when: the return is built from the signal's exit status.
- **AC4** — When a walked member is absent from `scope_set`, it is DROPPED, reported, and the rest
  of the tree still dies. Observed by `selftest.py`, arm `test_member_outside_the_scope_set_is_dropped`.
  Red when: the member is killed anyway, or the whole call aborts — rev-2 aborted, which refused
  every real tree (D9), and its repair then admitted every member (D17).
- **AC5** — Under `report` a `--sweep` signals nothing and still prints the flagged rows; under
  `reap-orphans` it kills only `ORPHAN` rows; under `reap-all` every flagged row. Observed by
  `selftest.py`, arm `test_mode_bounds_the_act`.
  Red when: any mode kills a row the classifier did not flag.
- **AC6** — When `--sweep --dry-run` runs against a staged flagged tree, the tree is ALIVE
  afterwards, the dry run's walked set equals the real run's over the same staging, and the dry
  run's survivor set equals its own walked set. Observed by `selftest.py`, arm
  `test_dry_run_walks_the_same_set_and_kills_nothing`.
  Red when: the dry path diverges from the real one. rev-1 demanded byte-identity, which is
  unsatisfiable and would have landed as a quietly weakened comparison (D7).
- **AC7** — When `reap.py --kill <winpid>` names a winpid outside `scope_set`, it refuses and exits
  non-zero regardless of `PROCMON_REAP_MODE`. Observed by `selftest.py`, arm
  `test_explicit_kill_still_obeys_membership`.
  Red when: the explicit path bypasses the fence along with the mode.
- **AC8** — When the walk ROOT is outside `scope_set`, `run_kill` refuses before walking. Observed
  by `selftest.py`, arm `test_out_of_scope_root_refuses_before_the_walk`.
  Red when: the root is admitted by closure from a member, which would let any in-scope descendant
  drag an arbitrary parent into the kill set.
- **AC9** — When a staged MSYS process is killed, an arm asserts the signal went through the
  resolved MSYS `kill` binary, by shimming it and observing the shim ran. Observed by
  `selftest.py`, arm `test_msys_row_is_signalled_by_the_kill_binary`.
  Red when: the signal is issued via `os.kill`, which targets a different namespace on this node's
  `win32` interpreter.
- **AC10** — When a native process THIS SHELL DID NOT SPAWN is staged (via `Start-Process`) and
  targeted, it is dead by re-read, and an arm asserts `taskkill //PID` was the signal used.
  Observed by `selftest.py`, arm `test_non_msys_row_is_signalled_by_taskkill`.
  Red when: the MSYS `kill` binary is used for it. Measured: it answers `No such process` and the
  process survives, so a single-signal reaper reports that row a survivor forever (D21).
  `fixture:` the arm spawns its own detached process; a process spawned by the test shell would be
  MSYS-addressable and would pass under the WRONG signal, which is the confound that nearly
  refuted this finding.
- **AC11** — When a row answers neither liveness probe, `run_kill` reports it UNSIGNALABLE and does
  not count it killed. Observed by `selftest.py`, arm `test_unaddressable_row_is_reported_not_claimed`.
  Red when: it is signalled hopefully and reported killed, which is the reassuring-zero class on the
  one path where it costs a live process.
- **AC12** — When `--sweep` runs, its output names the census, scoped, flagged, killed and survivor
  counts, each derived from the run. Observed by `selftest.py`, arm
  `test_sweep_counts_are_derived_and_complete`.
  Red when: any count is a literal or missing. rev-2 moved the chain here from unit 3 and left the
  five counts graded by nothing (D25).
  `figure:` DERIVED — the arm compares each against the fixture's own sizes.

## 7. Gates

`line length` · `lexicon naming predicates` · `govkit selfcheck` · `dead-path carriers (deleted files still named)`

New arm: `tools/process-monitor/selftest.py` · stages a mixed-namespace tree with bare-argv leaves,
a detached native process, an unsignalable row, a member outside the scope set, an out-of-scope
root, a shimmed and an absent signal binary, and each reap mode · floor moves with unit 1's arms.

New arm: a `namespace ban` leg over `tools/process-monitor/` · refuses `os.kill(` and any
`taskkill` invocation carrying `/T`, with the reason in the leg header · a CLASS ban, not an
instance fix.

## 8. Open questions

- **F1 — one signal or a TERM-then-KILL ladder?**
  RESOLVED (agent, 2026-09-08, delegated): ONE signal. A ladder needs a wait between rungs, and a
  timed wait inside the observer is what this build's rules forbid. The population is processes
  hours past a deadline with, in the reaped class, no live parent to flush anything for.
- **F2 — should a survivor red the sweep's exit status?**
  RESOLVED (agent, 2026-09-08, delegated): YES. A survivor is the state a human must see and the
  state this build was opened over.
- **F3 — inherit `scan_descendants`'s depth cap of 8?**
  RESOLVED (agent, 2026-09-08, delegated): NO CAP, a CYCLE GUARD instead. The cap exists there so a
  `ps` table disagreeing with itself mid-write costs a truncated tree rather than a spin; a
  visited-set gives the same termination guarantee without discarding a deep tree.
- **F4 — is `taskkill` admissible at all, given this build rejected it?**
  RESOLVED (agent, 2026-09-08, delegated): YES, in its SINGLE-PID form only, and the distinction is
  measured rather than asserted. `taskkill /T` walks the Windows tree and killed one of four
  because MSYS edges are a different graph; `taskkill //PID <one> //F` killed exactly the process
  named in both records, including one nothing else could kill. The kit supplies its own walk, so
  it uses the form that was measured correct and bans the one measured broken — §7's `namespace
  ban` leg enforces the second half. Vetoes clean: no new dependency (`taskkill` ships with
  Windows), and the surface narrows because rows that previously could not be killed at all no
  longer masquerade as survivors.

## 9. Revision log

- rev-1 · 2026-09-08 · initial draft.
- rev-2 · 2026-09-08 · S3 · S4 · S5 · AC1 · AC4 · AC6 · AC8-AC10 · §10 · folded round 1
  (D7, D8, D9, D12).
- rev-3 · 2026-09-08 · S1 · S3 · S4 · §3 · §4 · every AC · §7 · §8 F4 · folded round 2. D17: the
  per-member inheritance clause is deleted — it admitted every member unconditionally — and
  replaced by a membership test against the set unit 2 computes once, with a reachable drop case
  (AC4). D20 and D16 dissolve with it: the walk root is admitted by unit 2's closure, so a
  relative-argv leg shell no longer refuses every delegated call. D21: the signal is chosen per row,
  with `taskkill //PID` for rows MSYS cannot address, and AC10 stages a process the test shell did
  not spawn — the confound that nearly refuted the finding. D22: the walk runs over the union of
  both parent graphs and AC1's fixture carries a native grandchild as a FLOOR. D25: AC12 grades the
  five sweep counts this unit inherited at rev-2.

## 10. Reuse audit

**The corpus already holds a walk-kill-verify mechanism, and rev-1's rejection of it was false.**
`tools/run-gates/run-gates.sh:445-468` is `remove_descendants`: it snapshots `ps -ef` at `:447`,
walks ppid edges via `scan_descendants` at `:428-443`, SIGKILLs every member at `:451`, re-reads
with `kill -0` at `:466-468` and reports survivors. rev-1 rejected it as unable to reach a
grandchild, "verified against source at BASE", while the file's header at `:416-417` says the
opposite (D12).

**Its four recorded corrections are inherited by id rather than rediscovered:** the snapshot taken
before any kill because killing a parent reparents its children (`:419-421`); the numeric field
guard (`:432-436`, now unit 1 S8); the depth-8 bound (`:429`, answered in §8 F3); and the survivor
report carrying the walk's only liveness assertion (`:453-470`, corrected in
`TOOL-aQuenchedHarness-7` after an `rm` in the wrong place made it decorative — the same class as
AC3).

**What this unit ADDS**, and why extending that function was rejected: leaves-first ordering, a
returned verdict rather than a printed message, the scope membership test, the per-row signal
choice, walking over BOTH parent graphs, and no depth cap. That reader works purely in MSYS ids,
which unit 1 measures at 10 of 313 rows, so extending it would mean rebuilding it. Those changes
would alter the cost and semantics of every existing caller — the gate runner's hot failure path —
so unit 7 inverts the dependency instead.

`python tools/codebase-map/reuse_lookup.py "kill a hung or idle background process and report it to
the session"` returned nothing here, and its coverage line reads `unscanned layers: .sh`, so the
shell function above is invisible to it. The grep that found it is recorded in unit 7 §10.

Recall terms used: `gate runner wall clock bound timeout kill children orphan process leg pool
watchdog GATE_WALL background subprocess reaper`
