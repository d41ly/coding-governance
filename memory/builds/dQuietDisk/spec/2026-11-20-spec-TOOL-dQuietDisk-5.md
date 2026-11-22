# TOOL-dQuietDisk-5 — one `git diff --name-only BASE` decides every plain-guarded leg of a bar

**Status:** SPECCED · rev-3 · 2026-11-22 · node d · Tier-2 · base 40def53f · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 TOOL-dQuietDisk-28 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-1-pins-task.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-22-prompt-TOOL-dQuietDisk-2-reground-task.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-2-reground-task.md) | research | TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 |
| [2026-11-22-prompt-TOOL-dQuietDisk-5-1-spec-writer.md](../prompts/2026-11-22-prompt-TOOL-dQuietDisk-5-1-spec-writer.md) | journal | — |

<!-- /gen:spec-records -->


## 1. Goal

The runner decides each guarded leg with its own `git diff --quiet "$BASE" -- <guards>`, run
serially before dispatch, so a bar pays one git process per guarded leg that reaches the guard pass.
This unit reads the bar's changed paths once, with one `git diff --name-only --no-renames BASE`, and
matches each leg's plain guards against that list in-process through the runner's existing dirt
rule, extracted from the input keys into one function. A guard the rule cannot match keeps today's
per-leg diff. Every `GATE skip` and every leg that runs is the same as today.

## 2. Scope (IN)

- **S1** — Before the held-selection program, when `BASE` is set, `GATE_FULL` is not, and at least
  one leg carries a guard, the runner runs ONE `git -c core.quotePath=false diff --name-only
  --no-renames "$BASE" --`. Its output becomes `$WORK/base.moved` only when the diff exits 0: it is
  written to a temporary name that is moved into place on exit 0 alone, so any other exit leaves no
  `base.moved` for a reader. Observed by AC1 and AC3.
- **S2** — In the guard pass, a leg reaching today's `changed` call whose every guard is plain is
  collected into `$WORK/moved.guards` as `<index><TAB><guards>` instead. After the loop, one
  `write_guard_slices` call over that file and `$WORK/base.moved` writes `moved.slice.<index>`
  files, and a leg whose slice is empty gets the `skip` its per-leg diff would have given.
  Observed by AC1 and AC2.
- **S3** — A leg with any non-plain guard is decided by `changed` as today. So is every guarded leg
  when `$WORK/base.moved` is absent, and every collected leg when the `write_guard_slices` call
  exits non-zero. Observed by AC4.
- **S4** — The plain-guard predicate becomes one function, `check_plain_guard`, called by
  `build_input_keys` and by the guard pass, so the two can never disagree about which guards are
  plain. Observed by AC5.
- **S5** — The slice `awk` of `build_input_keys` becomes `write_guard_slices <guards file> <path
  list> <slice prefix>`, defined once above the held-selection block. `build_input_keys` calls it
  with its `keys.guards`, `keys.listing` and `keys.slice` names, and the slices it writes are byte
  for byte today's, so no input key and no reuse-cache entry moves. Observed by AC6.
- **S6** — The held-selection program, under `GATE_SELFTESTS=changed`, reads `$WORK/base.moved`
  instead of running its own `diff --name-only --no-renames <sha>` for a recorded sha equal to
  `BASE`. A recorded sha that differs from `BASE`, or an absent `base.moved`, keeps its own read.
  Observed by AC7.
- **S7** — `memory/guides/SESSION-KICKOFF.md` re-stamps `last-audit` in the commit that lands S1,
  because `tools/run-gates/run-gates.sh` is on its `watch:` line. Observed by AC8.
- **S8** — The two shell files' rows in `memory/project/shell-role.txt` are widened through the
  ratchet's widen door, with its widen record, and `memory/map/generated/symbols.json` is
  re-rendered for the two functions S4 and S5 mint. Observed by AC9.

## 3. Non-goals (OUT)

- No change to the docs mode: `check_doc_moved` diffs `DOCS_BASE` and walks a log, a different base
  and a different question.
- No change to the guard-matching rule, to which guards are plain, or to the base derivation.
- No change to the held-selection program's own match, `check_hit`. It also takes a file named like
  a directory guard, `ga` for `ga/`, which the runner's slice rule and `precommit.py`'s
  `check_guard_trips` do not. Aligning it changes which held legs run under changed mode, so it is a
  separate unit, handed off below. S6 shares only the read, never the rule.
- No change to `doc_reads` selection under `GATE_SELFTESTS=changed`, the mechanism
  `memory/gotchas/changed-mode-selection-ignores-doc-reads.md` names as a separate unit.
- No cache and no switch. The one diff answers the same question every per-leg diff answered, in
  the same bar, so it is a read, not a stored answer; a switch would choose between two reads of
  one fact.
- No change to `tools/run-gates/verdict_flow.py`. Its `select` reads every input at R from git and
  runs no diff against the working tree, so it has no read this unit could share.
- No kit version bump. Kit versions are minted by the lander, never on a branch
  (`tools/push-main.sh@3a5bf825e879:27`), and the runner's move from 1.55 to 1.56 came that way.

### Edges

- **consumes-from** external — dWitnessedBar's landing, main at `8b8b1374c`, merged into this branch
  at `40def53f7`. It rewrote the hold and selection block this unit edits; the block is now the
  landed one, so this precondition holds at the base.
- **hands-off** external — the held-selection program's `check_hit` admitting a file named like a
  directory guard, a BACKLOG ask the main loop files in this build's `BACKLOG.md`.

## 4. Design

### The guard pass today

All citations are read at `HEAD` `8688cdbba`, where the runner's blob is `2e851a92d9ce`, unchanged
since the merge `40def53f7`.

`changed` returns true under `GATE_FULL` or an empty `BASE`, and otherwise runs
`! git diff --quiet "$BASE" -- "$@"` (`tools/run-gates/run-gates.sh@2e851a92d9ce:599`). A git error
reads as changed, so the leg runs. The guard pass begins at
`tools/run-gates/run-gates.sh@2e851a92d9ce:3427`. A leg reaches the `changed` call
(`tools/run-gates/run-gates.sh@2e851a92d9ce:3477`) only after four earlier exits:
- a `run` row, which executes past every rule (TOOL-dWitnessedBar-30);
- a `kit`, `quarantine` or `level` hold, which writes `ondemand`;
- the docs mode, for a leg declaring `doc_reads`;
- an empty guard.

Under the default bar of this repository, 8 of the 74 guarded legs reach that call; under
`GATE_SELFTESTS=1`, all 74 do, less any leg a selection file holds. Both counts are DERIVED from
`tools/gate-legs.json` at `HEAD`: a leg is counted when it carries a `guard`, and for the default
bar when it is neither `subject` `kit` nor `chunk` `selftests`. AC3 re-derives them.

Every guard in the manifest is plain once `{prefix}` resolves to `tools`. A root install resolves
`{prefix}/` to the empty string and a bare `{prefix}` to `.`
(`tools/run-gates/run-gates.sh@2e851a92d9ce:2981`), both non-plain, so an adopter installed at its
root keeps today's per-leg diff for those legs under S3.

The held-selection program runs `diff --name-only --no-renames <sha>` once per distinct recorded sha
(`tools/run-gates/run-gates.sh@2e851a92d9ce:3387`) and matches by `check_hit`
(`tools/run-gates/run-gates.sh@2e851a92d9ce:3313`).

### The dirt rule, already written once

`build_input_keys` classes a guard as plain when it holds only `[A-Za-z0-9._/@+=-]` and is not
empty, `.`, `./`, absolute, magic, or carrying `..` or `//`
(`tools/run-gates/run-gates.sh@2e851a92d9ce:3593`). For plain guards its slice `awk`
(`tools/run-gates/run-gates.sh@2e851a92d9ce:3611`) matches a path that IS the guard, unless the
guard ends in `/`, or that starts with the guard and a `/`. That is what git's pathspec does for a
plain guard, which the comment above the `awk` states.

The `awk` takes the path after the first TAB of each line. A line with no TAB yields the whole line,
so a bare `--name-only` list feeds it unchanged. It also strips the quotes from a C-quoted line
(`tools/run-gates/run-gates.sh@2e851a92d9ce:3616`), and the comment at
`tools/run-gates/run-gates.sh@2e851a92d9ce:3574` gives the reason that holds here too: git escapes
only characters a plain guard never holds, so the escaped text agrees with the raw path on every
plain prefix. A quoted line in `base.moved` therefore needs no fallback of its own.

S5 lifts that `awk` into `write_guard_slices`, with one change of spelling: the output prefix
becomes an argument where it is `dir "/keys.slice."` today. S2 calls the same function over
`base.moved`, so the guard pass and the input keys share one matcher as well as one predicate.

### Why `--no-renames` and `--`

A per-leg `git diff --quiet BASE -- <guard>` limits the diff to the guard before rename detection,
so a file renamed out of the guard reads as deleted inside it. A whole-tree diff with renames on
would print only the new name, and the guard would miss the move. `--no-renames` prints both names.
`--` keeps a path named like a revision from being read as one. `precommit.py`'s `read_staged` makes
the same choice for the same reason (`tools/run-gates/precommit.py@245c835e8a51:183`).

### What stays per leg

A non-plain guard, an absent `base.moved` and a failed slice call each keep today's `changed` call
for the legs they touch, so a guard the in-process rule cannot answer is still answered by git.
Under `GATE_FULL` or an empty `BASE` no `base.moved` is written, and `changed` returns before it
spawns anything, as today.

### The held-selection program's read

The program gains two arguments, `BASE` and the path of `base.moved`, empty when absent. For a
recorded sha equal to `BASE` it reads that file in place of its own diff. The argv S1 runs is the
program's own plus a trailing `--`, which names no path, so the bytes it reads are the bytes its own
call would have printed, and `check_hit` sees the same list.

### Shared paths with the other order-2 units

TOOL-dQuietDisk-7 shares three paths with this unit, as its rev-5 Files touched reads:
`memory/guides/SESSION-KICKOFF.md` for its `last-audit` re-stamp, `memory/project/shell-role.txt`
for its widen, and `memory/map/generated/symbols.json` for its new functions. Units 5 and 7
therefore build in sequence. Units 2, 3, 4 and 8 name no path this unit writes, so they may build
beside it. Unit 13, at order 3, moves `tools/run-gates/run-gates.test.sh` onto
the template cache and carries the arm this unit adds.

### The shrink-only rows and the map

Both shell files sit exactly at their shrink-only rows: `run-gates.sh` at 3737 code lines and
`run-gates.test.sh` at 3179. Both are PINNED, measured at `HEAD` on 2026-11-22 by
`measure_code_lines` in the gate-lint kit's `sh_hygiene.py`, against the rows at
`memory/project/shell-role.txt@995611c472b5:114` and the line after it. Any code line this unit adds
reds the `portability (shell lines only shrink)` leg, so the pass widens
both through `python tools/memory-tree/ratchet.py widen shell-role --key <path> --reason <text>
--unit TOOL-dQuietDisk-5` (`tools/memory-tree/ratchet.py#run_widen`). That door writes the widen
record and its `widened:<stem>` row, and picks `<n>` as one past the highest widen record in the
build folder at the time it runs. The map is re-rendered by `python tools/codebase-map/gen_map.py
--write`, which indexes the runner's column-0 functions (`build_input_keys` has a row today).

### Files touched (estimate)

`tools/run-gates/run-gates.sh` · `tools/run-gates/run-gates.test.sh` ·
`memory/guides/SESSION-KICKOFF.md` (its `last-audit` re-stamp) · `memory/project/shell-role.txt` ·
`memory/builds/dQuietDisk/build/<date>-build-TOOL-dQuietDisk-5-widen-<n>.md` ·
`memory/map/generated/symbols.json`

### Inventory

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| `check_plain_guard` | shell function in `run-gates.sh` | `sh.function`, lexicon `--suggest` OK | AC5 |
| `write_guard_slices` | shell function in `run-gates.sh` | `sh.function`, lexicon `--suggest` OK | AC6 |
| `base.moved`, `moved.guards`, `moved.slice.<index>` | files under the runner's `$WORK` | none; `$WORK` is swept with the run | AC1 |

### Alternatives rejected

| Alternative | Why it loses |
|---|---|
| Run the per-leg diffs in parallel | Same process count, and the skip verdict would depend on scheduling, which the pass's own comment rules out. |
| Match every guard in-process, globs and magic included | It re-implements git's pathspec, and a disagreement would skip a leg that should run. |
| A second `awk` written for the guard pass | It is the slice `awk`'s second instance, so the charter's reuse rule extracts the first. |
| Call `precommit.py`'s `check_guard_trips` | One more python launch per bar, and that docstring defers to the runner's own rule, which already lives in this file. |
| Keep rev-2's fallback on a quoted line | The shared `awk` already answers a quoted line correctly for every plain guard, by the reason its comment states. |
| Reuse `verdict_flow.py select` | It reads at R and never diffs the working tree. |

## 5. Production-readiness checklist

- security: N/A — a read of the repository's own diff into the run's swept `$WORK`.
- perf / scale: on this repository's default bar the guard pass goes from 8 git processes to 1,
  and under `GATE_SELFTESTS=1` from 74 to 1 (AC3). The one diff compares the whole tree once, in
  place of one pathspec-limited compare per leg.
- error / empty / loading states: a failed diff or a failed slice call falls back to today's
  per-leg call (S3); an empty `BASE` or `GATE_FULL` runs every leg as today; an empty moved list
  skips every plain-guarded leg, as every per-leg diff would.
- observability: the `GATE skip` lines are unchanged.
- risks: a dirt-rule mismatch would skip a leg that should run. S4 and S5 keep one predicate and
  one matcher, and AC1 compares every guarded leg's answer with git's own.
- testing: the equivalence probe (AC1), the matcher fixture (AC2), the fallbacks (AC4), the
  unchanged keys (AC6), the count (AC3).
- migration: none. The reuse cache keeps every entry, because AC6 holds the input keys still.
- user docs: `help/` holds no page on guard evaluation; the runner's comment above the pass is
  updated in place, and `tools/run-gates/README.md` states nothing the change moves.

## 6. Acceptance criteria

- **AC1** — When a probe runs, in a scratch `git clone --shared` at `HEAD`, both today's
  `git diff --quiet "$BASE" -- <guards>` and `write_guard_slices` over one `git diff --name-only
  --no-renames "$BASE" --` for every guarded leg of `tools/gate-legs.json`, against five bases
  (`HEAD`, `HEAD~1`, `HEAD~20`, the merge-base with the clone's `origin/main`, and the run's pinned
  base `c95ef6216`), with one tracked file edited uncommitted and one renamed out of its guard, the
  two answers agree for every leg and base.
  Red when: any leg's skip decision differs from git's.
  fixture: a clone in the session scratch directory with its own `TEMP`; the function is extracted
  from the edited runner between its definition line and its closing brace.
- **AC2** — When `write_guard_slices` is fed a moved list holding only `xga/f` and a leg guarded by
  `ga/`, that leg's slice is empty; fed `ga/f`, it holds the line; fed `ga`, a leg guarded by `ga/`
  stays empty while one guarded by `ga` holds it; and fed the quoted line `"ga/a\tb"`, the `ga/` leg
  holds it.
  Red when: a substring match takes `xga/f` for `ga/`, a directory guard matches a file of its name,
  or a quoted line under a plain guard is missed.
- **AC3** — When AC1's probe runs under `GIT_TRACE2_EVENT=<dir>`, one directory per side, the old
  side holds one `diff` command event per guarded leg it decides and the new side holds one `diff`
  event in all, the two counts printed side by side. When the main loop runs a bar's guard pass over
  the AC1 clone under the same variable at the close, the directory holds one `diff` event for the
  guard pass, against today's one per guarded leg reaching it.
  Red when: a per-leg `diff --quiet` survives for a plain-guarded leg.
  figure: the per-leg counts, 8 and 74 at `HEAD`, are DERIVED from the manifest at observation.
  permission: a role agent runs no runner, a fixture copy included
  (`tools/hooks/scratch-guard.js@0251d34d5941:1614`, row G2), so the bar's own count is owed to
  the main loop; the pass makes the probe's count.
- **AC4** — When the guard pass's fallback, extracted from the edited runner into a probe script
  as AC1 extracts the function, is given no `base.moved`, then a `write_guard_slices` that exits 2,
  then a leg guarded by `fx/*.sh`, it decides each such leg by `changed`. The main loop observes the
  runner's own `GATE` lines equal the old runner's in each case, through the `New arm:` line of
  section 7.
  Red when: a failed read or a non-plain guard skips a leg.
  permission: the runner's `GATE` lines are owed to the main loop (scratch-guard row G2).
- **AC5** — When `grep -c 'check_plain_guard' tools/run-gates/run-gates.sh` runs, it prints 3 or
  more, the definition and its two callers, and the inline `case` at `build_input_keys` is gone.
  Red when: the guard pass and the input keys each keep their own predicate.
- **AC6** — When a probe builds `keys.guards` and `keys.listing` from the real tree at `HEAD`, as
  `build_input_keys` does, and runs the slice `awk` extracted from the runner at `HEAD` and
  `write_guard_slices` extracted from the edited runner into two directories, `diff -r` over the two
  prints nothing.
  Red when: any slice file differs, which would move an input key and orphan every reuse entry.
- **AC7** — When `grep -n 'base.moved' tools/run-gates/run-gates.sh` runs, it prints the one write
  of S1, the guard pass's read and the held-selection program's read under the sha-equals-`BASE`
  test. When the main loop runs the held-selection program in changed mode at the close, with a
  last-run record whose sha equals `BASE`, the trace holds no second `diff --name-only` for that
  sha, and the `selftests changed` lines equal the old runner's.
  Red when: the program still diffs a sha equal to `BASE`.
  permission: changed mode is a bar run, owed to the main loop (scratch-guard row G2); the pass
  makes the `grep`.
- **AC8** — When `bash skills/session-kickoff/manifest-check.sh --staged` runs over the commit that
  lands S1, it exits 0.
  Red when: the watched runner moves without the `last-audit` re-stamp.
- **AC9** — When `python tools/gate-lint/sh_hygiene.py --shell-role memory/project/shell-role.txt`
  runs after the widen, it names neither runner file, and `python tools/codebase-map/gen_map.py
  --check` exits 0 with `check_plain_guard` and `write_guard_slices` in
  `memory/map/generated/symbols.json`.
  Red when: a runner file's code lines exceed its row, or the map is stale for the two functions.

## 7. Gates

`run-gates canary` · `run-gates gov canary` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms` · `line length` · `shell hygiene (a loop fed by a command substitution)` · `portability (shell lines only shrink)` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)`

New arm: tools/run-gates/run-gates.test.sh · covers AC2 AC4 AC7 · section 3h's guarded fixture gains a plain directory guard, a near-miss path, a glob guard, a planted failing diff and a last-run record whose sha equals the base; its failing case is staged by matching the guard as a substring, by reading a failed diff as clean, and by diffing the recorded sha again · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft.
- rev-2 · 2026-11-22 · under `2026-11-22-prompt-TOOL-dQuietDisk-1-divergence-task`. AC3, AC4 and
  AC6 had the pass run the runner, which a role agent may not run in any form. AC3's figure now
  comes from AC1's probe, AC4's from the extracted fallback test, and AC6's from a `grep`; the bar's
  own count, `GATE` lines and changed-mode trace are owed to the main loop, and the `New arm:` line
  covers AC6 too. `check_plain_guard`, the one name this spec mints, passes `--suggest`.
- rev-3 · 2026-11-22 · §2 S2 S3 S5 S8 · §3 · §4 · AC2 AC4 AC6 AC9 ·
  re-grounded at 40def53f7 (order 1 built, dWitnessedBar landed), under
  `2026-11-22-prompt-TOOL-dQuietDisk-2-reground-task`. Every citation moved to the runner's blob
  `2e851a92d9ce`; the guard pass gained the `run` row exit and the `quarantine` and `level` holds,
  and the guarded count is 74, not 73. The slice `awk` is now extracted into `write_guard_slices`
  and shared, by the charter's reuse rule, which drops rev-2's quoted-line fallback, since that
  `awk` already answers a quoted line; AC4 loses that case, AC2 gains it, and AC6 is new, holding
  the input keys byte-identical. Both shell files sit at their shrink-only rows, so S8 and AC9 add
  the widen and the map render. The held program's looser `check_hit` is named and handed off. The
  old AC6 to AC7 become AC7 to AC8.

## 10. Reuse audit

The seam extended is the runner's own dirt rule: the plain-guard `case` and the slice `awk` of
`build_input_keys` (`tools/run-gates/run-gates.sh#build_input_keys`), extracted at their second
caller into `check_plain_guard` and `write_guard_slices` per the charter's reuse rule. The
held-selection program's per-sha diff is the second read S6 shares. The chain build owning the area
is dWitnessedBar (Test: gate health). Its TOOL-dWitnessedBar-10 and TOOL-dWitnessedBar-108 already
did this unit's work at the commit boundary: `precommit.py` lists the staged set once with
`--no-renames` and matches every row's guard in-process by `check_guard_trips`, "the runner's
semantics". This unit brings the same shape to the bar, against the runner's own copy of the rule
that `precommit.py` names as its source. It contradicts none of TOOL-dWitnessedBar-5's or -30's
hold rules, since only guard skips are decided here and every hold exits before the guard is read.

`python tools/codebase-map/reuse_lookup.py "one git diff name-only read once for every guarded leg"`
returned name-token neighbours only (`read_text`, `read`, `git`, `read_bytes`) at rev-1. The rev-3
re-ground found the precommit seam by reading the landed `tools/run-gates/README.md` and
`git log 59e882afd..fb6f1a74c -- tools/run-gates/`, not by recall.

Recall terms used: changed guard pathspec git diff quiet BASE guarded leg skip plain guard slice dirt rule staged name-only check_guard_trips
