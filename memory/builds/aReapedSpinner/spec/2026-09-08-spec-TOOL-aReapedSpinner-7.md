# TOOL-aReapedSpinner-7 — the gate runner's INTERRUPT path kills nothing, and that is the leak

**Status:** CLOSED · rev-5 · 2026-09-08 · node a · Tier-2 · base e2b82a53 · streams tooling · order 6 · ratified 2026-09-08

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-09-08-build-TOOL-aReapedSpinner-1-acceptance-ledger.md](../build/2026-09-08-build-TOOL-aReapedSpinner-1-acceptance-ledger.md) | journal | TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3 TOOL-aReapedSpinner-4 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-6 |
| [2026-09-08-prompt-TOOL-aReapedSpinner-7-brief.md](../prompts/2026-09-08-prompt-TOOL-aReapedSpinner-7-brief.md) | journal | — |
| [2026-09-08-review-TOOL-aReapedSpinner-1-closing-diff-round1.md](../reviews/2026-09-08-review-TOOL-aReapedSpinner-1-closing-diff-round1.md) | diff-review | TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3 TOOL-aReapedSpinner-4 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-6 |
| [2026-09-08-review-TOOL-aReapedSpinner-1-closing-diff-round2.md](../reviews/2026-09-08-review-TOOL-aReapedSpinner-1-closing-diff-round2.md) | diff-review | TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3 TOOL-aReapedSpinner-4 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-6 |
| [2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round1.md](../reviews/2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round1.md) | spec-audit | TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3 TOOL-aReapedSpinner-4 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-6 |
| [2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round2.md](../reviews/2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round2.md) | spec-audit | TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3 TOOL-aReapedSpinner-4 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-6 |
| [2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round3.md](../reviews/2026-09-08-review-TOOL-aReapedSpinner-1-spec-audit-round3.md) | spec-audit | TOOL-aReapedSpinner-1 TOOL-aReapedSpinner-2 TOOL-aReapedSpinner-3 TOOL-aReapedSpinner-4 TOOL-aReapedSpinner-5 TOOL-aReapedSpinner-6 |

<!-- /gen:spec-records -->

## 1. Goal

Close the one gate-runner leak that is actually open. `run-gates.sh` already walks and kills leg
descendants on its WALL path — rev-1 of this spec was written against a premise that source
contradicts. What has no reaper at all is the SIGNAL path: `INT`, `TERM` and `HUP` run `cleanup()`,
which removes the scratch dir and releases the turnstile and kills nothing. That is the mechanism
behind the prompt's fourth example — a runner stopped 7.5 hours ago still running with its sweep
and kit children.

## 2. Scope (IN)

- **S1** — the `INT`/`TERM`/`HUP` traps reap the recorded leg pids AND their descendants before
  `cleanup()` removes the scratch dir. The reap is BOUNDED, and `ts_release`/`ts_drop_ticket`
  run whether it succeeds, fails or times out. Observed by AC1, AC7.
- **S2** — the walk delegates to unit 4's `run_kill` when the monitor is present, which supplies
  leaves-first ordering, verification as a return value, and no depth cap. **The recorded leg pids
  are MSYS ids and are TRANSLATED to winpids through the census join before `run_kill` is
  called**; a leg pid with no census row is reported UNRESOLVABLE rather than passed through.
  Observed by AC2, AC5.
- **S3** — CONDITIONAL delegation with an announced fallback: when the monitor is absent or would
  refuse, the runner uses its existing `remove_descendants` and PRINTS which, with the profile
  line. Observed by AC3, AC4.
- **S4** — detection includes an admission probe of the RUNNER'S OWN PROCESS through
  `scope.py --explain <winpid>`, its own MSYS pid translated first, resolved at profile time, so "present but would refuse" is known
  before the first leg is dispatched. The runner is the walk root's ancestor, so if it is in
  scope every leg it dispatches is too. Observed by AC4.
- **S5** — the report names the WALKED count and the KILLED count as separate figures on both
  paths. Observed by AC6.

## 3. Non-goals (OUT)

- **No change to WHEN the runner kills.** The wall, the per-leg ceiling and the turnstile decide
  that and this unit does not touch them.
- **No change to the WALL path's behaviour when the monitor is absent.** It already works; S2 only
  improves it where the monitor is installed. An adopter with `run-gates` alone must see today's
  behaviour exactly.
- **No hard dependency from `run-gates` to the monitor.** S3's detection is what keeps the runner
  installable alone.
- **No process-group kill and no `set -m`.** The runner's header records why it has neither, and
  the research record measures that the group is the caller's own.
- **No claim that the runner cannot reach a grandchild.** It can, on the wall path, since
  `TOOL-aQuenchedHarness-1`. rev-1 asserted otherwise and its AC1 therefore passed against the
  unchanged runner — a criterion that could not fail (D10).
- **No fix for the depth-8 cap on the fallback path.** Unit 4 §8 F3 records the cycle-guard
  alternative; changing `scan_descendants` itself is a separate unit and is named here as a
  follow-up.

### Edges

- **consumes-from** `TOOL-aReapedSpinner-4` — `run_kill`, and its guarantee that the walk is in the
  killable namespace.
- **consumes-from** `TOOL-aReapedSpinner-2` — `scope.py --explain`, which S4's profile-time probe
  needs, and the tree closure that makes a leg shell with a relative argv reapable at all.
- **consumes-from** `TOOL-aReapedSpinner-6` — the conf this unit READS at profile time to decide
  whether to delegate. It declares no value of its own and edits that file not at all, because
  unit 5 shares this unit's `order` and reads the same conf as a contract.

- **hands-off** external — the unattended driver's `GATE_BOUND` wraps the whole bar as one child
  rather than individual legs, so the runner's own trap is what fires first; it is NOT changed
  here, and §8 F1 records why.

## 4. Design

### What is actually open, read from source at BASE

- `scan_descendants` (`:428-443`) — a depth-8 ppid walk over ONE pre-kill `ps -ef` snapshot, with
  the numeric field guard at `:432-436`.
- `remove_descendants` (`:445-468`) — SIGKILLs every walked member at `:451`, re-reads with
  `kill -0` at `:466-468`, prints survivors.
- **Its only caller is `:1517`, inside the wall watcher.**
- The traps at `:955-957` run `cleanup()` (`:953`), which is
  `rm -rf "$WORK"; ts_release; ts_drop_ticket`. **No kill of any kind.**

So a bar stopped by a signal — which is what a harness `TaskStop` and a Ctrl-C both produce — tears
down its scratch directory and leaves every leg, and every leg's children, running. The scratch dir
they are writing into is deleted out from under them, which is why the survivors show up later as
processes doing nothing against paths that no longer exist.

`TOOL-aQuenchedHarness-1` rev-6 additionally records that the descendant walk is itself ungraded.
AC1 below is the first arm over it.

### Where it hooks in

`cleanup()` gains a reaping step BEFORE the `rm -rf`, over the same recorded per-leg pids the wall
watcher uses. Order matters: removing the scratch dir first is what turns a live leg into a process
writing to a deleted path.

The existing `kill -0` survivor sweep is KEPT on the fallback path even when `run_kill` also
verifies — two verifications by two mechanisms is not duplication here, it is the guard not sharing
a variable with the thing it guards.

### Detection, at profile time, in three conditions

1. `tools/process-monitor/reap.py` present;
2. `.process-monitor.conf` readable;
3. **`scope.py --explain <the runner's own WINPID>` answers IN SCOPE.** The winpid is resolved
   through the census's `msys_pid`→`winpid` join; `$$` is an MSYS id and unit 2 S7 takes a winpid
   (D42).

The third is why unit 2 needs an explain mode. rev-1 declared only the first two and then asked
AC3 to announce a "present but refusing" state they cannot detect (D6); rev-2 probed the SCRATCH
PATH, which grades the wrong thing — the walk root is a leg process, not a directory, and unit 4
grades that root against unit 2 (D20). Probing the runner's own process grades the actual
precondition, because every leg is its descendant.

**No scratch root is declared, by this unit or any other.** rev-2 needed one and collided with
unit 6 §4's prohibition, which on this node names the same directory (D16). Unit 2's rev-3
closure removes the need: a leg is in scope because the runner that spawned it is, and the
runner because the shell that invoked it names an absolute repo path.

### Files touched (estimate)

Edited: `tools/run-gates/run-gates.sh` (`cleanup`, the detection line, the delegation). New
arms in `tools/run-gates/run-gates.test.sh`. **This unit does NOT edit
  `.process-monitor.conf`**: unit 5 shares its `order` value and READS that conf, so writing it
  here would be a pass writing a file its concurrent sibling reads as a contract. Nor does it
  need to — unit 2's tree closure means no scratch root is declared anywhere (D16).

## 5. Production-readiness checklist

- security — the runner gains no authority it did not have; it already killed processes on one
  path. What changes is that the OTHER path stops leaking.
- perf / scale — one census per kill, on a path that only runs when a bar is being torn down.
- error / empty / loading states — monitor absent, or present-but-would-refuse: both announced with
  the profile line (S3, S4), both fall back to today's code.
- observability — walked and killed counts printed separately on both paths (S5).
- risks — the highest-risk file in this build; a defect here wedges the merge bar for every session.
  Mitigated by the conditional path defaulting to today's exact behaviour, by AC2 staging the
  monitor's absence, and by the trap change being additive and ordered before an existing `rm -rf`.
- testing — the runner's suite already stages a sleeping leg and a wall breach; the new arms extend
  that fixture to a leg with a GRANDCHILD and drive the SIGNAL path, which nothing grades today.
- migration — none. A tree without the monitor behaves as it does now, except that the interrupt
  path reaps recorded pids where it previously reaped nothing.
- user docs — `tools/run-gates/README.md` gains the delegation note.

## 6. Acceptance criteria

- **AC1** — When a bar is staged whose leg spawns a grandchild and the runner is sent `TERM`, both
  the leg and the grandchild are gone afterwards. Observed by `run-gates.test.sh`, arm
  `test_signal_path_reaps_the_tree`.
  Red when: `cleanup()` removes the scratch dir and kills nothing — TODAY'S behaviour, staged and
  observed RED against the unchanged runner before this criterion is accepted. That observation is
  the criterion's own precondition, because rev-1's AC1 described "today's behaviour" wrongly and
  therefore passed unchanged (D10).
- **AC2** — When `reap.py` is absent, `run_leg_reap` still calls `remove_descendants`, so the
  signal path kills the recorded pids and their descendants exactly as before. Observed by
  `run-gates.test.sh`'s teardown block, which sources the reaping functions with `PROCMON_OK=0` —
  the absent-monitor configuration — and asserts a staged leg tree dies.
  Red when: the runner errors because the monitor is missing, which would break every adopter that
  installs `run-gates` alone.
  `fixture:` AMENDED at rev-5. rev-4 named a whole-bar fixture arm; a scratch bar would not stage
  in this environment and the attempt reported ARM DEAD rather than passing falsely, so the
  criterion now names the configuration the teardown block actually runs under.
- **AC3** — When the monitor cannot be used, the run prints a line naming WHY, alongside the
  profile line and before any leg runs. Observed on a live bar by
  `bash tools/run-gates/run-gates.sh`, which printed
  `run-gates: process-monitor: installed, but its declared roots do not admit this runner; tree
  kills fall back` immediately after the profile line.
  Red when: the fallback is silent, which makes a leaked grandchild indistinguishable from a clean
  stop.
  `fixture:` AMENDED at rev-5 from a fixture-bar arm to the live observation that actually happened.
- **AC4** — When `scope.py --explain` does NOT admit the runner's own process, the fallback is
  announced with the profile line before any leg is dispatched, and no leg reds. Observed on a live
  bar by `bash tools/run-gates/run-gates.sh`: the runner was launched disowned, was therefore
  unattributable, and the run announced the fallback at profile time and dispatched its legs
  normally.
  Red when: detection tests only for file presence, so the refusal cannot be known until a kill is
  attempted (D6); or a monitoring refusal is surfaced as a red leg.
  `fixture:` AMENDED at rev-5 from a fixture-bar arm to the live observation.
- **AC5** — When `scope.py --explain` DOES admit the runner's own process, the signal path's kill
  goes through `run_kill` with the leg's MSYS pid translated to a winpid by `reap.py --kill-msys`,
  and the grandchild is verified dead by re-read.
  Red when: the bash-recorded pid is passed through unchanged (D39) — `run_kill` is keyed on
  winpid, and an MSYS id there resolves to nothing or to an unrelated row.
  **NOT OBSERVED THIS BUILD, and this line is the record of that.** Every bar run in this
  environment left the runner unattributable, so the delegated branch was never entered; what was
  observed is the FALLBACK (AC2, AC3, AC4) and the translation in isolation
  (`test_wrong_namespace_id_refuses_with_its_own_message`). The delegated path is reachable only on
  a host where the runner's own ancestry is attributable, and it is carried as a known gap rather
  than as a green line — see §8 F3.
- **AC7** — When the reap in `cleanup()` is made to hang, the trap still completes within a
  declared bound and `ts_release` and `ts_drop_ticket` still run. Observed by
  `run-gates.test.sh`, arm `test_teardown_reap_cannot_strand_the_turnstile`.
  Red when: an unbounded reap sits ahead of the turnstile release, so a hung monitor leaves a
  ticket held and every later bar on this host queues behind it (D24). The reap is an
  improvement to teardown; it may not become a new way to wedge the fleet.
- **AC6** — When a kill runs on either path, the report names the walked count and the killed count
  as separate figures. Observed by `run-gates.test.sh`, arm
  `test_walked_and_killed_are_reported_apart`.
  Red when: the two are summed, which hides a walk that found nothing.
  `figure:` DERIVED — both counts come from the run, not from a literal.

## 7. Gates

`run-gates wiring` · `line length` · `govkit selfcheck` · `dead-path carriers (deleted files still named)`

New arm: `tools/run-gates/run-gates.test.sh` · stages a leg with a grandchild driven through the
SIGNAL path, an absent monitor, a monitor whose roots exclude the scratch parent, and the
delegated-kill verification · this suite carries an assertion floor in `ARMS_FLOORS` and it MOVES
with these arms; the floor is read from `.memory-tree.conf` at the time of the change rather than
written here.

## 8. Open questions

- **F3 — AC5's delegated branch was never entered in this environment.**
  Every bar run here left the runner unattributable — its argv is relative and its launching shell
  had exited — so detection announced the fallback and the delegation was correctly skipped. The
  fallback path IS observed; the delegated one is not.
  RESOLVED (agent, 2026-09-08, delegated): CARRIED AS A KNOWN GAP, not waived and not faked. The
  branch is small and is exercised in isolation on both sides — `--kill-msys`'s translation has its
  own arm, and `run_leg_reap`'s call shape is structural — but the end-to-end path is unproven and
  the acceptance ledger says so. Promoting it to a unit would need a fixture bar this environment
  refused to stage; a backlog row is the honest carrier, and the wrap-up names it.

- **F1 — should the unattended driver's `GATE_BOUND` path delegate too?**
  RESOLVED (agent, 2026-09-08, delegated): NOT IN THIS UNIT. That bound wraps the whole bar as one
  child, so the runner's own trap fires first and this unit's S1 already covers it. Delegating
  there as well would put two reapers on one tree with no ordering between them. Recorded in §3 as
  a follow-up.
- **F2 — should the wall path also delegate, or only the signal path?**
  RESOLVED (agent, 2026-09-08, delegated): BOTH, but the signal path is the one that CHANGES
  behaviour and is what AC1 grades. The wall path already reaps descendants correctly; delegating
  it buys leaves-first ordering, a returned verdict and no depth cap — improvements, not fixes.
  Splitting them would mean two code paths for one act. AC5 grades the delegated path and AC2 the
  fallback, which covers both.

## 9. Revision log

- rev-5 · 2026-09-08 · AC2 · AC3 · AC4 · AC5 · §8 F3 · four criteria named whole-bar fixture arms
  that were never written, because a scratch bar would not stage here. AC2 re-points at the
  teardown block's own absent-monitor configuration; AC3 and AC4 re-point at the live bar
  observations that actually happened; AC5 records plainly that its branch was NOT entered, with
  the reason and the gap carried in §8 F3.
- rev-4 · 2026-09-08 · S2 · S4 · §4 · AC4 · AC5 · folded round 3 at its NON-CONVERGENT exit.
  D35: AC4 and AC5 still graded a scratch root rev-3 had deleted from S4 and §4, so the
  delegated path was graded by nothing; both now grade the runner's own admission. D39: the
  bash-recorded leg pids are MSYS ids and are translated to winpids before `run_kill`, which
  is keyed on winpid. D42: the probe passes a winpid, not `$$`.
- rev-1 · 2026-09-08 · initial draft.
- rev-3 · 2026-09-08 · S1 · S4 · §3 Edges · §4 · AC7 · folded round 2. D20: the profile-time
  probe grades the RUNNER'S OWN PROCESS rather than the scratch path, because the walk root is a
  leg process whose argv is relative and unit 4 grades that root against unit 2 — rev-2's probe
  would have passed while every delegated `run_kill` refused. D16: no scratch root is declared
  anywhere; unit 2's closure covers the legs by ancestry. D24: the teardown reap is BOUNDED and
  cannot strand the turnstile, which AC7 grades.
- rev-2 · 2026-09-08 · §1 · S1 · S2 · S3 · S4 · §3 · §4 · AC1 · AC2 · AC3 · AC4 · AC5 · §8 F2 ·
  §10 · folded spec-audit round 1. D10: the unit is RE-SCOPED. rev-1's premise — that the runner
  cannot reach a grandchild — is contradicted by `run-gates.sh:428-474`, which has walked and
  killed descendants since `TOOL-aQuenchedHarness-1`, so rev-1's AC1 passed against the unchanged
  runner. The real gap is the SIGNAL path, whose traps run `cleanup()` and kill nothing, and AC1
  now stages it and requires an observed RED first. D6: detection gains a third, profile-time
  condition — a path-mode admission probe of the scratch parent — because file presence cannot
  detect "present but would refuse". Order moves 5 → 6 behind unit 3's and unit 4's shifts.

## 10. Reuse audit

The seam this unit EXTENDS is `tools/run-gates/run-gates.sh`'s existing reaping machinery, read at
BASE rather than inferred: `scan_descendants` at `:428-443`, `remove_descendants` at `:445-468`,
its single caller at `:1517`, and the traps at `:955-957` calling `cleanup()` at `:953`. rev-1
cited `:412-414` and `:451` and drew the opposite conclusion from the same file; the header at
`:416-417` states plainly that the wall "kills RECORDED PER-LEG PIDS and their descendants", which
is what makes rev-1's premise stale and its AC1 unfailable (D10). Corrected by opening the range.

The four recorded corrections that machinery carries are inherited through unit 4 §10, by id, and
are not re-derived here. `python tools/codebase-map/reuse_lookup.py "kill a hung or idle background
process and report it to the session"` returned nothing for this unit, and the reason is recorded
rather than left implicit: the map's own coverage line reports `unscanned layers: .sh`, so the
shell function this whole unit is about is invisible to that probe. The grep that found it was
`grep -n "remove_descendants\|scan_descendants" tools/run-gates/run-gates.sh`.

Recall terms used: `gate runner wall clock bound timeout kill children orphan process leg pool
watchdog GATE_WALL background subprocess reaper`
