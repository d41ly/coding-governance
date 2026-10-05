# TOOL-aMendedFleet-66 — the unattended close sequence lists the open asks that target files the run touched

**Status:** CLOSED · rev-1 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 66

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The review measured 58 and 37 live asks targeting files that two recent builds edited, and those
builds cited 0 and 1 of them: an open ask about a file reaches no stage that is editing that file.
Unit 10 gives `gen_build_index.py --asks` a `--path` filter that returns the asks whose pointer or
`seen` locator names a given path. This unit calls that filter over the paths an unattended run's
own range touched, from the BASE its run-state file pins to HEAD, and prints the list at the move
into `VERIFYING`, the phase in which a run decides what its one `--close` carries, so each ask can
be disposed while the run can still act on it. The list never refuses and never changes an exit.

## 2. Scope (IN)

- **S1** — A new function in `tools/unattended/unattended.sh`, `print_touched_asks`, takes the
  run-state file. It reads the pinned base with `fact "$1" base`, lists the range's paths with the
  NUL-delimited, rename-free `git diff` read `print_selftests_owed` uses, and, when any path is
  touched, runs `$ASKS_CMD --json --path <every touched path> --limit 0` through `run_bounded`,
  parsing the JSON inline through `resolve_python`. Observed by AC1.
- **S2** — THE LIST. On a live answer it prints one header line,
  `unattended: open asks targeting files this run's range touched (report only, for disposition): <n>`,
  then one indented line per ask, `<id> · <status> · <sev> · <summary>`, in the generator's own
  ranked order. A range touching no path, or matching no ask, prints the header with `0` and no list.
  Observed by AC1, AC2.
- **S3** — EVERY OTHER STATE SAYS WHICH, on one line, and none is silent:
  - not asked, when `ASKS_CMD` is blank, in the register its other skips use;
  - unreadable range, when the record pins no base or the base does not resolve, in the words
    `print_selftests_owed` uses;
  - not asked, when the generator exits 2, quoting the first line of its stderr, which is how a
    generator from before unit 10 refuses `--path`;
  - DEAD PROBE, when the generator exits otherwise, times out, or prints text the inline parse cannot
    read.
  The function returns 0 on every path. Observed by AC3, AC4.
- **S4** — THE CALL SITES are the two that call `print_selftests_owed`: `verb_phase` after a move into
  `VERIFYING`, and `print_resume_orientation` when a session resumes at `VERIFYING`. Each calls
  `print_touched_asks` on the line BEFORE that call, so unit 83's call keeps its place on the line
  after it and the three notices print in a fixed order. Observed by AC5.
- **S5** — Section 8 of `tools/unattended/ASKS.template.md`, which says the driver appends arguments in
  exactly the shapes it lists, gains this call as its fourth shape, read as JSON and never parsed by
  position; `memory/guides/UNATTENDED-ASKS.md` takes the same bytes. `tools/unattended/README.md` says,
  where it describes the move into `VERIFYING`, that the move prints this list. Observed by AC6.
- **S6** — An arm in `tools/unattended/unattended.test.sh` moves a fixture run into `VERIFYING` after a
  commit that touched a path one fixture ask points at, and reads the ask on stdout.
  NOT OBSERVED by a criterion here: the suite runs once at the close, and the arm is declared under
  `New arm:` in §7.

## 3. Non-goals (OUT)

- Disposing of any ask, filing one, or adding a Definition-of-Done item that refuses a close over an
  undisposed one. Report-only is the review's wording, and `asks-disposed` already grades the asks a
  run was mandated or filed.
- Printing the list from `--close` itself; unit 83's §8 F2 gives the reason, and the two notices share
  their phase move.
- Matching asks to paths here. Unit 10's `--path` owns the locator rule and the ranking.
- Bumping the unattended kit version: unit 65's lander mints it, or the close owes it once.

### Edges

- **consumes-from** `TOOL-aMendedFleet-10` — `--asks --json --path` with `--limit 0`, and the
  `pointer`, `summary`, `status` and `sev` fields each row carries; without them there is nothing to
  call.
- **hands-off** external — the unattended kit version, minted at the lander or owed once at the close.

## 4. Design

### Evidence

Read at base `7af5f564`.

- `.unattended.conf` declares `ASKS_CMD="python tools/memory-tree/gen_build_index.py --asks"`, and the
  driver runs it UNQUOTED through `run_bounded`, as it runs `$LANDER` and `$GATE_CMD`.
- `print_selftests_owed` is the driver's report-only range notice: it reads the pinned base with
  `fact`, announces a blank declaration and an unreadable range in words, and is called from exactly
  `verb_phase` on a move into `VERIFYING` and `print_resume_orientation` at that phase.
- Section 8 of the asks companion lists three call shapes and says the driver uses exactly those.
- Unit 83 specifies its call on the line after each `print_selftests_owed` call, and its AC5 counts on
  that adjacency; S4 takes the line before for that reason.

### Inventory

- `print_touched_asks` — cell `sh.function`; answered OK by
  `python tools/lexicon/lexicon.py --suggest print_touched_asks --as sh.function`.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/README.md`
- `tools/unattended/unattended.test.sh`
- `tools/unattended/ASKS.template.md`
- `memory/guides/UNATTENDED-ASKS.md`

### Rollout

Unit 10 ships `--path` and is ordered first. Units 49 and 83 add sibling notices to the same driver;
83 is ordered after this unit and rebases onto it.

## 5. Production-readiness checklist

- security — the paths are git's own names from the recorded base, passed as separate words; the
  generator never opens them, and unit 10 refuses an absolute or `..` value.
- perf / scale — one `git diff` and one generator run, about three seconds, once per run. A range of a
  few hundred paths stays far inside the Windows command-line limit.
- error / empty / loading states — S3's states, one line each; none changes the exit.
- observability — the list is the run's disposition worklist, each line naming the ask id to close,
  advance or decline.
- risks — a run whose range touches a hot file prints a long list once; it is the honest worklist.
- testing — AC1 to AC6 here; the arm in S6.
- migration — none.
- user docs — S5.

## 6. Acceptance criteria

- **AC1** — When, in a scratch clone of the unit's tip under a short `%TEMP%` path whose
  `memory/builds/aMendedFleet/RUN.md` has its `base:` fact rewritten to that tip, one commit appends
  a comment line to `tools/unattended/unattended.sh` and
  `bash tools/unattended/unattended.sh --phase aMendedFleet VERIFYING <that commit's sha>` runs, its
  stdout carries the header with a count of at least 1, and every indented line's id is among the ids
  `python tools/memory-tree/gen_build_index.py --asks --json --path tools/unattended/unattended.sh --limit 0`
  returns in that clone.
  Red when: the move prints no list, or lists an id the filter does not return.
  figure: the count is DERIVED at observation time.
  fixture: the rewritten base makes the range that one commit; at the unpinned base the range is the
  whole build so far, and the count would mean nothing.
- **AC2** — When the same rebased clone instead commits only a new file at its root that no ask names,
  and the move is made, stdout carries the header with `0` and no indented line.
  Red when: an untouched file's asks are listed.
- **AC3** — When `ASKS_CMD` is blanked in the clone's `.unattended.conf` and the move is made, stdout
  carries one `not asked` line naming `ASKS_CMD`, and the verb exits 0 as it did with the key set.
  Red when: the notice is silent, or the blank key changes the exit.
- **AC4** — When `ASKS_CMD` is set to `false` in the clone's `.unattended.conf` and the move is made,
  stdout carries one `DEAD PROBE` line. This is the staged break for S3's dead arm.
  Red when: a failed generator prints a count of 0.
- **AC5** — When `grep -n "print_touched_asks" tools/unattended/unattended.sh` runs, it prints the
  definition and exactly two calls, each on the line before a `print_selftests_owed` call.
  Red when: the resume path at `VERIFYING` does not print the list, or a third caller exists.
- **AC6** — When `cmp tools/unattended/ASKS.template.md memory/guides/UNATTENDED-ASKS.md` runs it exits
  0, and `grep -n -- "--path" tools/unattended/ASKS.template.md tools/unattended/README.md` hits the
  fourth call shape and the description of the move into `VERIFYING`.
  Red when: the companion still says the driver uses three shapes, or its two copies differ.

## 7. Gates

`unattended kit gate` · `unattended skill wiring` · `recall floor` · `recall floor arms` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `line length` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: `tools/unattended/unattended.test.sh` · a fixture run moved into `VERIFYING` after a commit touching a path one fixture ask points at, staged red by deleting the `verb_phase` call · none

## 8. Open questions

- **F1 — Which verb prints the list?**
  Options: `--close`; the move into `VERIFYING` and the resume at it. `--close` runs the whole bar
  before anything after its Definition-of-Done loop, so no criterion could observe it short of the
  bar, and a disposition needs a phase in which the run can still edit a backlog.
  RESOLVED (agent, 2026-10-04, delegated): the move into `VERIFYING` and the resume at it, per S4,
  which is where unit 83 puts its sibling notice.
- **F2 — Where does the call sit beside unit 83's?**
  Options: the line before `print_selftests_owed`; the line after. Unit 83's AC5 requires its own call
  on the line after, so the line after would make the two specs disagree.
  RESOLVED (agent, 2026-10-04, delegated): the line before, per S4.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from a read of `verb_phase`, `print_selftests_owed`, the
  `ASKS_CMD` call sites and section 8 of the asks companion at base, and of units 10 and 83's specs.

## 10. Reuse audit

The seams extended are `print_selftests_owed` in `tools/unattended/unattended.sh`, both its shape as a
report-only notice that reads the pinned base with `fact` and announces every skip, and its two call
sites; the driver's existing `run_bounded $ASKS_CMD` calls; and unit 10's `--path` filter, which owns
matching and ranking so nothing here re-implements either. `python
tools/codebase-map/reuse_lookup.py "list open asks whose pointer targets files a range touched"`
returned `render_ask_row` and `build_ask_sort_key` in `tools/memory-tree/backlog.py`, which unit 10
already reuses behind `--path`, and no range-to-asks join; the scan names `.sh` as unscanned, so
`git grep -n ASKS_CMD tools/unattended/unattended.sh` was the probe for the shell layer and found the
three call shapes and no path-keyed one. Recall returned units 49 and 83, the two sibling notices, and
`TOOL-aSealedCaravan-7`, on the close reading the RECORDED base, which S1 follows. Where the report
and the tree disagree: the 58 and 37 figures were not re-measured; unit 10 measured 31 live asks
targeting `tools/unattended/unattended.sh` alone.

Recall terms used: `python tools/memory-recall/query.py "does the unattended close surface open asks
that target the files the build touched, for disposition" --terms "open asks pointer touched files
close disposition ASKS_CMD asks-disposed report-only BASE..HEAD --path gen_build_index"`
