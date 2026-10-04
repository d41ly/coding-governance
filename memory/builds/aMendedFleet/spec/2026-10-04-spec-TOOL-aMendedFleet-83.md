# TOOL-aMendedFleet-83 — the unattended close sequence lists the dossiers its range touched and did not refresh

**Status:** SPECCED · rev-2 · 2026-10-04 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 83

<!-- gen:spec-records -->

*No record names this unit.*

<!-- /gen:spec-records -->

## 1. Goal

The charter's Definition of Done owes a dossier refresh on touch, and the review measured 23 of 84
feature touches doing it. Unit 37 derives dossier freshness from git and gives `map_diff.py` a range
mode that lists the dossiers a `<base>..<head>` range touched and did not refresh. This unit, split
from unit 37 at its F1, calls that mode over an unattended run's own range, from the BASE its
run-state file pins to HEAD, and prints the list where the driver already prints its other
report-only range notice: at the move into `VERIFYING`, the phase in which the main loop decides what
its one `--close` carries, and again on a resume at that phase. A run then sees every dossier it left
older than its code while it can still refresh one. The list never refuses and never changes an exit.

## 2. Scope (IN)

- **S1** — A new function in `tools/unattended/unattended.sh`, `print_stale_dossiers`, takes the
  run-state file. It reads the pinned base with `fact "$1" base`, locates the map's range reader as
  `map_diff.py` in the directory of the declared `MAP_CLI`, resolves python with `resolve_python`,
  and runs `map_diff.py <base>..HEAD --stale-dossiers --json` through `run_bounded`. Observed by
  AC1.
- **S2** — THE LIST. On a live answer it prints one header line,
  `unattended: dossiers this run's range touched and did not refresh (report only): <n> of <of>`,
  then one indented line per stale dossier, `<feature> · <dossier> · <behind> behind · newest <sha8>`,
  in the JSON's most-behind-first order; on zero stale it prints the header with `0` and no list.
  Observed by AC1, AC2.
- **S3** — EVERY OTHER STATE SAYS WHICH, on one line, and none is silent:
  - not asked, when `MAP_CLI` is blank or names no file, or when no `map_diff.py` sits beside it;
  - unreadable range, when the record pins no base, in the words `print_selftests_owed` uses;
  - not asked, when `map_diff.py` exits 2, quoting the first line of its stderr, which is how an
    unadopted map refuses;
  - DEAD PROBE, when the JSON's `live` is false, quoting its `note`, or when it exits otherwise,
    times out, or prints text the inline parse cannot read.
  The function returns 0 on every path. Observed by AC3, AC4.
- **S4** — THE CALL SITES are the two that already call `print_selftests_owed`: `verb_phase` after a
  move into `VERIFYING`, and `print_resume_orientation` when a session resumes at `VERIFYING`. Each
  calls `print_stale_dossiers` on the line after that call, so the two notices print together and in
  that order. Observed by AC1, AC5.
- **S5** — `tools/unattended/README.md` says, where it describes the move into `VERIFYING`, that the
  move prints the stale-dossier list from `MAP_CLI`'s kit and that the list is report-only.
  Observed by AC6.
- **S6** — An arm in `tools/unattended/unattended.test.sh` moves a fixture run into `VERIFYING` after
  a commit that touched a claimed path without its dossier, and reads the list on stdout.
  NOT OBSERVED by a criterion here: the suite runs once at the close, and the arm is declared under
  `New arm:` in §7.

## 3. Non-goals (OUT)

- Printing the list from `--close` itself. §8 F2 says why the move into `VERIFYING` is the close
  sequence's point for it.
- Refusing any verb over a stale dossier, or adding a Definition-of-Done item for it. Report-only is
  the review's and unit 37's wording, and a new item is a protocol change.
- A new `.unattended.conf` key naming `map_diff.py`. §8 F1 says why the reader is derived instead.
- Refreshing any dossier, or computing staleness here. Unit 37 owns the rule; this prints it.
- Bumping the unattended kit version, owed once at the close.

### Edges

- **consumes-from** `TOOL-aMendedFleet-37` — `map_diff.py --stale-dossiers` in range mode with
  `--json`, and the `live` and `note` fields it defines; without them there is nothing to call.
- **hands-off** external — the unattended kit version bump, owed once at the close.

## 4. Design

### Evidence

Read at the worktree HEAD `fee9f62b`, whose bytes under `tools/` and in `.unattended.conf` equal
base `7af5f564`'s.

- `.unattended.conf` declares `MAP_CLI="tools/codebase-map/reuse_lookup.py"`, and `unattended.sh`
  initialises `MAP_CLI=""` beside `RECALL_CLI` and `SPEC_TOKENS_CLI`. The driver reads `MAP_CLI`
  only for the `reuse-probed` item's log today.
- `print_selftests_owed` is the driver's report-only range notice. It reads the pinned base with
  `fact`, announces a blank declaration and an unreadable range in words, never refuses, and is
  called from exactly two places: `verb_phase` on a move into `VERIFYING`, and
  `print_resume_orientation` at that phase. Its comment records why it left `--close`
  (`TOOL-dAlignedCarrier-6`): an instruction printed inside the close arrives after the phase it is
  about, which `TOOL-dDerivedDocket-70` measured.
- `--dispatch` runs the declared `SPEC_TOKENS_CLI` through `resolve_python` and `run_bounded`, the
  shape S1 reuses for a declared python CLI.
- `verb_phase` writes nothing but the phase, its witness and the staged record, so a move into
  `VERIFYING` in a scratch clone is a seconds-long, side-effect-contained observation, where a
  `--close` runs the whole bar first.
- Node d's live branch adds no dossier or `map_diff` call to `tools/unattended/unattended.sh`, so
  there are no bytes to reuse.

### Inventory

- `print_stale_dossiers` — cell `sh.function`; answered OK from
  `python tools/lexicon/lexicon.py --suggest print_stale_dossiers --as sh.function`.

### Rollout

Unit 37 ships the range mode and is ordered first. Units 49 and 66 add close-sequence blocks to the
same driver and are ordered first too; this unit rebases onto them.

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/README.md`
- `tools/unattended/unattended.test.sh`
- `memory/map/generated/symbols.json`

### Alternatives rejected

- **A literal path to the map kit.** The kit-file literal ban refuses it, and it would point at
  nothing in an adopter that installed at another prefix.
- **Parse `map_diff.py`'s human output.** Unit 37 specifies only the JSON's fields; the human render
  can change without breaking its own criteria, so the driver reads the contract.
- **Read the base from `trusted_base`.** It observes the remote and prints refusals of its own; a
  report-only notice wants the pinned value, which is what `print_selftests_owed` reads.

## 5. Production-readiness checklist

- security — a fixed argv through `run_bounded`; the base is a recorded sha, quoted, and the reader
  path is the declared `MAP_CLI`'s directory, never a string a run's output supplies.
- perf / scale — one python spawn and the one `git log` unit 37 makes, about a second on node a, on
  a phase move that happens once per run.
- error / empty / loading states — S3's states, each one line; none changes the exit.
- observability — the list is the run's own refresh worklist, each line naming the newest commit a
  re-reader starts from.
- risks — a run whose range moves many kits prints a long list once; it is the honest worklist.
- testing — AC1 to AC6 here; the arm in S6.
- migration — N/A: nothing stored changes, and no conf key is added.
- user docs — S5.

## 6. Acceptance criteria

- **AC1** — When, in a scratch clone of the unit's tip under a short `%TEMP%` path, one commit
  appends a comment line to `tools/codebase-map/rank_harness.py` and
  `bash tools/unattended/unattended.sh --phase aMendedFleet VERIFYING <that commit's sha>` runs, its
  stdout carries the header line with a count of at least 1 and an indented line naming
  `codebase-map`, after the `phase VERIFYING` line.
  Red when: the move prints no list, or the list omits the dossier the commit left behind.
  cost: seconds; the clone is the only thing written.
- **AC2** — When the same clone then commits a one-line edit to
  `memory/map/features/codebase-map.md` and the move is made again, no indented line names
  `codebase-map`.
  Red when: a dossier the range refreshed is still listed.
- **AC3** — When `MAP_CLI` is blanked in the clone's `.unattended.conf` and the move is made, stdout
  carries one `not asked` line naming `MAP_CLI`, and the verb exits 0 as it did with the key set.
  Red when: the notice is silent, or the blank key changes the exit.
- **AC4** — When `git clone --depth 1` from a `file://` URL makes a shallow clone of the unit's tip
  under a short `%TEMP%` path and the move is made there, stdout carries one `DEAD PROBE` line
  quoting the shallow-history note.
  Red when: a shallow clone prints a count.
- **AC5** — When `grep -n "print_stale_dossiers" tools/unattended/unattended.sh` runs, it prints the
  definition and exactly two calls, each on the line after a `print_selftests_owed` call.
  Red when: the resume path at `VERIFYING` does not print the list, or a third caller exists.
- **AC6** — When `grep -n "stale-dossier" tools/unattended/README.md` runs, it hits the description
  of the move into `VERIFYING`.
  Red when: the driver prints a notice its README does not describe.

## 7. Gates

`unattended kit gate` · `codebase-map coverage + freshness` · `unattended skill wiring` · `install-prefix (shipped surface)` · `lexicon naming predicates` · `line length` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms`

New arm: `tools/unattended/unattended.test.sh` · a fixture run moved into `VERIFYING` after a commit that touched a claimed path without its dossier, staged red by deleting the `verb_phase` call · none

## 8. Open questions

- **F1** — How does the driver find `map_diff.py`?
  Options: a new `.unattended.conf` key; the directory of the declared `MAP_CLI`. A new key needs a
  row in the protocol's key table, a governance carrier the mandate's third answer opens for stale
  facts and the context diet but not for new surface, plus the example conf and the driver's
  initialiser. `MAP_CLI` already declares the codebase-map kit, and `map_diff.py` sits beside
  `reuse_lookup.py` in every install of it.
  RESOLVED (agent, 2026-10-04, delegated): derive it from `MAP_CLI`'s directory, and announce a
  missing file as not asked, per S1 and S3.
- **F2** — The brief says the close prints the list. Which verb carries it?
  Options: `--close`; the move into `VERIFYING` and the resume at it; both. `--close` runs the whole
  bar before any line after its Definition-of-Done loop, so no criterion could observe it short of
  the bar, and `TOOL-dAlignedCarrier-6` moved this driver's other range notice out of the close for
  arriving after the phase it is about. The move into `VERIFYING` is the close sequence's first act,
  where a run can still refresh; printing in both is the same list twice.
  RESOLVED (agent, 2026-10-04, delegated): the move into `VERIFYING` and the resume at it, per S4.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, split from unit 37 at its F1, from a read of `verb_phase`,
  `print_selftests_owed`, `verb_close` and the conf's CLI keys at base.
- rev-2 · 2026-10-04 · §4 Files touched and §7 add symbols.json and its coverage leg: the new public shell function is indexed after TOOL-aMendedFleet-35 S1.

## 10. Reuse audit

The seams extended are `print_selftests_owed` in `tools/unattended/unattended.sh`, both its shape as
a report-only notice that reads the pinned base with `fact` and announces every skip, and its two
call sites, and the `SPEC_TOKENS_CLI` call in `--dispatch`, the shape of a declared python CLI run
through `resolve_python` and `run_bounded`. `python tools/codebase-map/reuse_lookup.py "print at the
unattended close the dossiers a range touched and did not refresh"` returned map-kit neighbours such
as `load_dossier_texts` and `parse_dossier` and `print_report` in the transition audit, none of which
runs in the driver; the scan names `.sh` as unscanned, so `git grep` over `tools/unattended/` was the
probe for the shell layer, and it found `print_selftests_owed` and no existing dossier or `map_diff`
call. Recall returned unit 37's spec, which names this split, `TOOL-dDerivedDocket-70`, on a notice
inside `--close` arriving too late, which §8 F2 follows, and `TOOL-aSealedCaravan-7`, on the close
reading the RECORDED base. Where the report and the tree disagree: the report's 23 of 84 touches was
not re-measured; unit 37 re-measured 26 of 27 dossiers older than their paths.

Recall terms used: `python tools/memory-recall/query.py "does the unattended close report dossiers
the run touched without refreshing them" --terms "unattended close dossier refresh on touch
stale-dossiers map_diff codebase-map freshness BASE..HEAD report-only MAP_CLI"`
