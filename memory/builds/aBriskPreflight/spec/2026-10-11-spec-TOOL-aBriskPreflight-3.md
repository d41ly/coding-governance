# TOOL-aBriskPreflight-3 — preflight's wiring scope, measured: the whole check stays, every candidate recorded

**Status:** CLOSED · rev-1 · 2026-10-11 · node a · Tier-1 · base 271a90045 · streams tooling · order 3 · ratified 2026-10-11

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-build-TOOL-aBriskPreflight-1-baseline.md](../build/2026-10-11-build-TOOL-aBriskPreflight-1-baseline.md) | research | TOOL-aBriskPreflight-1 TOOL-aBriskPreflight-2 TOOL-aBriskPreflight-4 TOOL-aBriskPreflight-5 TOOL-aBriskPreflight-6 TOOL-aBriskPreflight-7 |
| [2026-10-11-build-TOOL-aBriskPreflight-3-wiring-scope.md](../build/2026-10-11-build-TOOL-aBriskPreflight-3-wiring-scope.md) | research | — |
| [2026-10-11-prompt-TOOL-aBriskPreflight-1-brief.md](../prompts/2026-10-11-prompt-TOOL-aBriskPreflight-1-brief.md) | research | TOOL-aBriskPreflight-1 TOOL-aBriskPreflight-2 TOOL-aBriskPreflight-4 TOOL-aBriskPreflight-5 TOOL-aBriskPreflight-6 TOOL-aBriskPreflight-7 |
| [2026-10-11-prompt-TOOL-aBriskPreflight-3-build-brief.md](../prompts/2026-10-11-prompt-TOOL-aBriskPreflight-3-build-brief.md) | research | — |
| [2026-10-11-prompt-TOOL-aBriskPreflight-3-spec-brief.md](../prompts/2026-10-11-prompt-TOOL-aBriskPreflight-3-spec-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

Decide by measurement which arms of `check-wiring.sh --check` the unattended preflight needs, and
record every candidate's cost and what it would stop catching. The decision is the whole check: it
is the one candidate that keeps every verdict preflight reads without a surface the owner has not
granted (§7 F1 and F2), so this unit closes on its record, its instrument and two asks.

## 2. Scope (IN)

- **S1** — A per-arm window instrument, a records-only python file in this build's `build/` folder.
  It splits one `trace-spawns` xtrace of `tools/check-wiring.sh` at the script's top-level run-list
  calls, prints each window's wall, forks and execs, then each candidate's sum. Observed by AC1.
- **S2** — The verdict reading on the tree units 1 and 2 leave: which arms can raise the exit status
  under `--check`, read from the source and confirmed by two staged breaks in a throwaway tree.
  Observed by AC2 and AC3.
- **S3** — One traced `--check` on that tree, and a measurement record carrying each candidate's
  wall, forks and execs from that one trace beside the BASE figures, the arms each leaves out, and
  the `UNWIRED` lines those arms can print. Observed by AC4.
- **S4** — The decision stands as data and nothing else: `WIRING_CHECK` keeps the whole `--check`,
  and no commit of this unit edits a file under `tools/` or `.githooks/`, or `.unattended.conf`.
  Observed by AC5.
- **S5** — Two asks in this build's `BACKLOG.md`: the read-only selector (candidate C2) for the
  owner's turn, carrying its measured price; and a preflight read of the unattended kit's own hook
  wiring, which no wiring arm grades. Observed by AC6.

## 3. Non-goals (OUT)

- Building the selector. A flag on `check-wiring.sh` and an accepted token in the driver's read-only
  allow-list are a new public surface on two shipped kits, which is M3's veto 2 and the owner's turn
  (§7 F2). It goes to the owner as an ask (S5).
- New arms grading the stop-guard, gate-guard and stall-recorder wiring or the resume tick. A new
  refusal is not a cut, and an arm that could red a working adopter is not strictly beneficial. It
  is filed as an ask (S5).
- Cutting the straggler inventory's own cost inside `migrate_backlog.py`, the memory-tree kit's
  engine. It sits outside the brief's four items; the C2 ask names it as the route that keeps the
  check whole and still sheds its wait.
- Any edit to `tools/check-wiring.sh`, `tools/unattended/unattended.sh`, `.unattended.conf` or the
  kit's example conf. No kit is touched, so no kit version moves.
- The wiring check's ceiling, which is TOOL-aBriskPreflight-7's.

### Edges

- **consumes-from** `TOOL-aBriskPreflight-1` — the batched per-item loops. The traced run measures
  the tree they leave; without them the figures are BASE's again.
- **consumes-from** `TOOL-aBriskPreflight-2` — the settings file and fragments read once and python
  resolved once, measured the same way.
- **hands-off** `TOOL-aBriskPreflight-7` — the `WIRING_CHECK` it derives its wiring ceiling from
  stays the whole check, so that ceiling bounds a run that includes the straggler inventory's own
  60 s bound, a report-only arm that took 71.5 s at BASE.

## 4. Design

### The candidates

Preflight reads the wiring check's exit status and nothing else: `check_wiring` in
`tools/unattended/unattended.sh` returns on `run_bounded $WIRING_CHECK && return 0`, and the
check's output reaches the operator only when refusal 4 indents it. The status is the script's last
line, `[ "$unwired" = 0 ] && exit 0 || exit 1`, so a verdict preflight reads is an `unwired`
increment an arm can reach under `--check`.

| Candidate | Arms it runs | What it stops catching |
|---|---|---|
| C1 | the whole run list, twelve arms at BASE | nothing |
| C2 | every arm but `check_eol` and `check_backlog_stragglers` | no verdict preflight reads; on a refusal, the indented output loses those two arms' `ok`, `skip` and `note` lines |
| C3 | the prelude and `check_hooks` (with its blob and mode helpers) | every `UNWIRED` line of nine arms: agent-cap, scratch, recall, card, routed, merge rows, merge ours, ssh and skill |
| C4 | none of this script's arms | every verdict the script prints; the hooks it names are graded elsewhere (below) |

C4 is the prompt's own example, "the stop-guard, gate-guard, stall-recorder and resume-tick wiring".
No arm of `check-wiring.sh` reads any of the four: a count of those names in the script is 0 at
BASE. Their wiring is graded by the fragment loop of `tools/unattended/adopt-unattended.sh --check`,
which reds "the <name> hook is UNWIRED" per kit fragment, and that runs as the merge-bar leg
`unattended skill wiring` only. Preflight reads the resume tick's registration itself and prints a
WARNING, never a refusal. Verified in source at writing.

### The BASE reading (PINNED, measured 2026-10-11)

Run `cw-base-traced` (568.3 s by its timer, rc 0, the host state the baseline record states for
every BASE reading), split into arm windows by the probe this spec's authoring ran over the trace
still held in the run's scratch on node a. Wall here is the trace's, first row to last:

| Window or candidate | Wall (s) | Forks | Execs |
|---|---|---|---|
| `check_eol` | 42.7 | 31 | 33 |
| `check_backlog_stragglers` | 71.5 | 6 | 2 |
| C1, the whole check | 567.6 | 355 | 387 |
| C2 | 453.5 | 318 | 352 |
| C3 | 49.2 | 27 | 27 |

The window sums equal the counter's own totals for that trace, so no row fell outside a window. The
straggler window is wall with almost no traced spawn: its cost is `migrate_backlog.py`'s own git
calls, which the counter cannot see, and it ran into its own `timeout 60` (the `exited 124` note).

### The instrument

`2026-10-11-build-TOOL-aBriskPreflight-3-arm-windows.py`, beside the build's other instruments,
invoked as `python <instrument> <trace> <check-wiring.sh>`.

- It loads `2026-10-11-build-TOOL-aBriskPreflight-1-trace-spawns.py` by path and calls its parser
  and exec rule. It restates neither, so the two instruments cannot count differently.
- The run list is DERIVED from the script argument: every column-0 line that is exactly a function
  name beginning `check_`. A window opens at the first process's row whose `file:line` is one of
  those lines and closes at the next; `(prelude)` precedes the first, and the last closes at the
  trace's final row. A late arm another build adds is measured with no edit here.
- Per window it prints wall, forks (process ids first seen in it, the first process excluded) and
  execs, then a TOTAL row and one row per candidate. The candidate sets are named constants, and
  the record cites the verdict reading as their derivation.
- Two guards, each exiting 1 with a line naming what failed. Every run-list line must match exactly
  one row of the first process, else the trace was not taken from this script. The TOTAL must equal
  the counter's whole-trace figures, else a row fell outside every window.
- Every `open` names its encoding.

### Inventory

Functions, cell `py.function`, each confirmed with `lexicon.py --suggest` at writing:
`load_trace_spawns`, `derive_run_list`, `measure_arm_windows`, `print_arm_windows` and `main`.
The codebase map's python layer reads the tool root only (`_live_py` in `map_extractors.py`), so the
instrument moves no map artifact.

### The measurement on the tree units 1 and 2 leave

- **When.** Once units 1 and 2 are terminal. If either is parked, the trace is taken on the tree as
  it stands and the record says which units it includes.
- **Where.** The BASE trace's own tree, `%TEMP%/bp/A` on node a, moved to the run's tip with a
  detached checkout. It is wired, and it holds 38 local heads, so the straggler inventory walks the
  same refs it walked at BASE. If that tree is gone, a fresh clone under `%TEMP%/<short-name>` is
  wired with `--fix` before any break, and the record prints both head counts and says whether the
  straggler windows compare.
- **How.** A `host-state.sh` line, then `run-traced.sh` with label `cw-u12-traced` on
  `tools/check-wiring.sh --check`, then the counter and the window instrument over the trace. Then
  the verdict probe and the two staged breaks of AC2 and AC3, each restored before the next. The
  CRLF break is written and undone by byte rewrites, because a checkout-based restore can no-op
  under the clean filter, as the eol arm's own comment records.
- Wall depends on the host and the counts do not, so BASE and after compare by forks and execs, and
  each run's wall stands beside its own host line.

### The record

`2026-10-11-build-TOOL-aBriskPreflight-3-wiring-scope.md`, opening `**Serves:** research
TOOL-aBriskPreflight-3`. It carries the verdict probe's output, the full per-window table for BASE
and for `cw-u12-traced` with the candidate rows, each run's host line and head count, what each
candidate stops catching, C4 with its evidence, the decision with its reason, and the result rows.
The filename date is the pass's own date; 2026-10-11 is written here because the build opened then.

### The asks

Two rows in `memory/builds/aBriskPreflight/BACKLOG.md`. Their ids are minted by the run's
orchestrator, because a fan-out child never mints (charter §2).

1. The C2 selector: a read-only flag on `check-wiring.sh` that skips the two report-only arms with a
   `skip` line each, the driver's allow-list accepting it, and the conf value naming it. It carries
   C1 minus C2 from `cw-u12-traced`, says veto 2 is why this run did not build it, and names the
   other route, cutting the straggler inventory's own cost.
2. Preflight reading the unattended kit's own hook wiring before the first unit. Today the
   fragment loop in `adopt-unattended.sh --check` grades it at the merge bar only, so a run can
   start with a dormant stop-guard or gate-guard and learn of it at the close.

### Traps the probes selected

`gotchas.py --for-paths` over these paths selected three that bind this pass.
`staged-break-substitutes-a-synthetic-value`: the matcher break uses `Workflow`, the stale value
the agent-cap arm names, not an invented one. `msys-grep-counts-cr-on-every-line`: the CRLF break
is confirmed with `od -c`, never with a CR grep. `fixture-passes-by-finding-nothing`: every break is
preceded by a clean run of the same tree that exits 0, so a red is the break's and not the tree's.

### Files touched (estimate)

- `memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-3-arm-windows.py`
- `memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-3-wiring-scope.md`
- `memory/builds/aBriskPreflight/BACKLOG.md`
- `memory/backlog/TOOL.md`, the generated view the asks re-render

### Alternatives rejected

- **C3**, by the verdict probe and AC3's matcher break: it leaves out nine arms whose `UNWIRED`
  lines raise the status preflight reads, which fails the build's rule that no check is weakened.
- **C2**, by M3's veto 2 (§7 F2). Its measured price goes to the owner with the ask.
- **C4**, unselectable: no arm of the script reads those hooks, and the grader that does is a
  merge-bar leg, not a wiring arm.
- **A bare `--check` that sheds the two report-only arms while `--session` keeps them.** It changes
  an existing mode's output for every adopter and every hand run, the same veto-2 reading, and the
  brief's own rule that a bare `--check` prints exactly what it prints today.
- **An environment knob selecting arms.** An environment read is a new public surface that leaves
  no diff behind, which unit 7's spec refuses for its ceilings on the same ground.

## 5. Acceptance criteria

- **AC1** — When the window instrument `2026-10-11-build-TOOL-aBriskPreflight-3-arm-windows.py`
  runs over the `cw-base-traced` trace with `tools/check-wiring.sh`, it prints one row per line that
  `grep -c '^check_[a-z_]*$' tools/check-wiring.sh` counts plus a `(prelude)` row, exits 0, and its
  TOTAL row equals the first line the counter prints over the same trace: 567.6 s, 355 forks, 387
  execs. Given a scratch copy of the script with one blank line inserted above its run list, it
  exits 1 naming a run-list line that matched no trace row.
  Red when: the instrument prints a table for a script whose line numbers do not match the trace, or
  a row outside every window leaves the TOTAL short of the counter's figures.
  fixture: the BASE trace sits in this run's scratch on node a and is untracked; if it is gone, AC1
  is observed over the `cw-u12-traced` trace and the record says so.
  figure: the three totals are PINNED from run `cw-base-traced`, measured 2026-10-11.
- **AC2** — When `awk '/^[a-z_]+\(\) *\{/{fn=$1} /unwired=\$\(\(unwired\+1\)\)/{print fn, NR}' tools/check-wiring.sh`
  runs on the tree units 1 and 2 leave, every `check_eol` site it prints sits inside that arm's
  branch that runs only under `--fix`, `check_backlog_stragglers` prints none, and each other arm of
  the run list prints at least one site reachable under `--check`. The record carries the output.
  Red when: a site appears in `check_backlog_stragglers` or outside `check_eol`'s `--fix` branch,
  which puts a verdict preflight reads in C2's left-out set; or the probe prints sites in fewer than
  ten arms, which means a sibling unit respelled the increment and the probe is re-derived first.
- **AC3** — In the after tree, with `.claude/skills/drift-audit/SKILL.md` rewritten to CRLF in the
  working copy, `bash tools/check-wiring.sh --check` prints a `note     eol` line naming that file,
  prints no `UNWIRED` line, and exits 0. Restored, then with the `Workflow|Agent` matcher in
  `.claude/settings.json` narrowed to `Workflow`, it prints an `UNWIRED  agent-cap` line and
  exits 1. Restored again, it exits 0.
  Red when: the CRLF break exits 1, so the eol arm moves the status and C2 would stop catching a
  verdict; or the matcher break exits 0, so the probe cannot see an arm C3 leaves out.
  cost: three runs of the check on node a, minutes each under the load the baseline records.
  fixture: the tree must be wired so a clean run exits 0 first; `%TEMP%/bp/A` is, and a fresh clone
  is not until `--fix` has run.
- **AC4** — When `memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-1-trace-spawns.py`
  runs over the `cw-u12-traced` trace with `tools/check-wiring.sh`, its first line's wall, forks and
  execs equal the C1 row of `2026-10-11-build-TOOL-aBriskPreflight-3-wiring-scope.md`. That record
  also carries the C2 and C3 rows from the same trace, the BASE rows, a host line and a local-head
  count beside each run, and for every candidate the arms it leaves out and their `UNWIRED` lines.
  Red when: a candidate row is missing, a figure differs from what the committed instruments
  re-derive from the trace, or a run's figures stand without its host line.
  figure: DERIVED from the trace at observation time, then PINNED in the record under its run label.
- **AC5** — When `git show --name-only --format= HEAD` runs at each commit whose subject names this
  unit, it lists nothing under `tools/` or `.githooks/` and not `.unattended.conf`; and at the last
  of them `grep '^WIRING_CHECK=' .unattended.conf` prints `WIRING_CHECK="bash tools/check-wiring.sh --check"`.
  Red when: a commit of this unit edits the checker, the driver or the conf, which would build C2
  without the owner's turn.
- **AC6** — When `python tools/memory-tree/gen_build_index.py --asks --build aBriskPreflight --all`
  runs after this unit's commit, it lists two asks that commit filed: one naming the read-only
  selector with C1's and C2's measured wall and execs from the record, and one naming the unattended
  kit's hook wiring and `adopt-unattended.sh`.
  Red when: either ask is absent, or the selector ask carries no measured figure, which leaves the
  owner's turn unpriced.

## 6. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `encoding posture (text IO names its encoding)` · `recall floor` · `recall floor arms` · `pass-order history` · `brief-recorded`

The two recall legs are owed because their guard is `memory/`, which every path this unit writes
sits under. This unit adds no gate arm and edits no kit file, so it owes no kit self-test leg. The
merge bar runs once, at the close.

## 7. Open questions

- **FACT-QUESTION · F1 — Which candidates keep every verdict preflight reads?** A candidate keeps
  them exactly when every arm it leaves out cannot raise `unwired` under `--check` (Design, the
  candidates).
  Probe: the awk of AC2 over `check-wiring.sh`, each site read against the branch it sits under.
  Observation at BASE `271a90045`: the one `check_eol` site, `check-wiring.sh:1066`, sits in the
  branch opened at `check-wiring.sh:1058`, which runs only when `DO_FIX` is 1 and the mode is not
  `session`. `check_backlog_stragglers` has none. The ten other arms each carry at least one site
  reachable under `--check`, `check_agentcap` at `check-wiring.sh:761` among them.
  Liveness: the probe printed sites in ten arms, so a site-free arm is a reading and not a dead
  probe. A staged increment in the eol arm's note loop would move C2 to "stops catching", and AC3's
  matcher break is the positive case for an arm C3 leaves out. Nor does the pick rest on a zero
  alone, M3's counter-rule: the eol arm is observed firing without moving the status (AC3, and the
  check-wiring self-test's eol arm), and that suite's straggler arm pins that a straggler alone does
  not decide the exit.
  RESOLVED (agent, 2026-10-11, delegated): C1 and C2 keep every verdict preflight reads. C3 leaves
  out nine arms that can raise it and is discarded under M3's veto 1, the build's rule that no check
  is weakened. C4 selects no arm of the script at all.
- **F2 — The whole check (C1), or a read-only selector running only the arms preflight reads (C2)?**
  C2 needs three edits: a flag on `check-wiring.sh` that skips the two report-only arms with a
  `skip` line each, the driver's allow-list accepting that flag, and the conf's `WIRING_CHECK` value
  naming it. Keeping C1 costs, at BASE, 114.2 s of 567.6 s with 37 forks and 35 execs, the
  straggler window alone 71.5 s past its own 60 s bound (Design, the BASE reading).
  M3's vetoes, in order. Veto 1 discards neither, because both keep every verdict (F1) and neither
  fails a criterion here. Veto 2 discards C2: a new flag on a shipped kit and a new accepted token
  in the shipped driver are a new public surface, as this corpus has read it before
  (TOOL-aDeferredBar-1 for a flag on the bar, TOOL-aGraftedHelix-32 for a flag or mode on the
  driver). The prompt names the narrowing as a possible answer, and that does not lift the veto:
  the unattended protocol honours a `may:` grant only from an owner-committed `slug` README and
  refuses one in `prompt` mode, and this run's `RUN.md` pins `may: none`. C1 survives every veto.
  Recommendation: C1, with C2 put to the owner priced.
  RESOLVED (agent, 2026-10-11, delegated): C1, the whole `--check`, the only option surviving M3's
  vetoes. No measurement can change this pick. The after-trace is taken so the owner's turn on C2
  carries numbers, and the ask carries them (S5).

## 8. Revision log

- rev-1 · 2026-10-11 · initial draft.

## 9. Reuse audit

- Probe: `python tools/codebase-map/reuse_lookup.py "select a subset of wiring check arms for a read-only caller"`
  named no selector or arm-filter seam. Its nearest were `wired` in `tools/check-wiring.sh`, a
  matcher test and not a mode, and `run_arms` in `tools/lib/lib-selftest.sh`, a self-test runner.
  No existing seam fits a selector, and this unit builds none. The seam it extends is the build's
  own counter,
  `memory/builds/aBriskPreflight/build/2026-10-11-build-TOOL-aBriskPreflight-1-trace-spawns.py`,
  whose parser and exec rule the window instrument loads rather than restates. The grader C4 points
  at is the fragment loop of `tools/unattended/adopt-unattended.sh`, verified in source at writing.
- A second probe, for F2's veto reading: `git grep -n -i "veto 2" -- memory/builds/`, filtered for
  a flag or a public surface, returned TOOL-aDeferredBar-1 and TOOL-aGraftedHelix-32 among others,
  each reading a new flag or mode as a new public surface.
- Context probes: `gotchas.py --for-paths` selected the three classes Design names, and
  `gen_build_index.py --asks --path` over the checker, the driver and the conf returned no open ask
  about narrowing the wiring check.
- Recall: `python tools/memory-recall/query.py "Which wiring check arms does the unattended preflight need, and may a read-only selector narrow the check it delegates to?"`
  returned TOOL-aBranchedMandate-2, which is why the eol arm stopped gating, and
  TOOL-aUnmannedHelm-5, which is why preflight delegates to `--check`. It also returned TOOL-aPromptedMandate-9 and
  TOOL-aBoundedCeiling-6 on the seam's bound. None records a decision to narrow the check.
- Recall terms used: `--terms "WIRING_CHECK preflight check-wiring allow-list read-only note UNWIRED eol straggler exit-status refusal selector"`
