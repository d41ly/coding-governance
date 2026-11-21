# TOOL-dQuietDisk-5 — one `git diff --name-only BASE` decides every plain-guarded leg of a bar

**Status:** SPECCED · rev-2 · 2026-11-22 · node d · Tier-2 · base 609cd40b · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md](../build/2026-11-20-build-TOOL-dQuietDisk-1-agent-ledger.md) | journal | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 TOOL-dQuietDisk-26 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |
| [2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md](../prompts/2026-11-20-prompt-TOOL-dQuietDisk-1-spec-brief.md) | research | TOOL-dQuietDisk-1 TOOL-dQuietDisk-2 TOOL-dQuietDisk-3 TOOL-dQuietDisk-4 TOOL-dQuietDisk-6 TOOL-dQuietDisk-7 TOOL-dQuietDisk-8 TOOL-dQuietDisk-9 TOOL-dQuietDisk-10 TOOL-dQuietDisk-11 TOOL-dQuietDisk-12 TOOL-dQuietDisk-13 TOOL-dQuietDisk-14 TOOL-dQuietDisk-15 TOOL-dQuietDisk-16 TOOL-dQuietDisk-17 TOOL-dQuietDisk-18 TOOL-dQuietDisk-19 |

<!-- /gen:spec-records -->

## 1. Goal

The runner decides each guarded leg with its own `git diff --quiet "$BASE" -- <guards>`, run
serially before dispatch, so a bar pays one git process per guarded leg that reaches the guard pass.
This unit reads the bar's changed paths once, with one `git diff --name-only --no-renames BASE`, and
matches each leg's plain guards against that list in-process by the runner's existing dirt rule. A
guard the rule cannot match keeps today's per-leg diff. Every `GATE skip` and every leg that runs is
the same as today.

## 2. Scope (IN)

- **S1** — Before the held-selection program, when `BASE` is set, `GATE_FULL` is not, and at least
  one leg carries a guard, the runner runs ONE `git -c core.quotePath=false diff --name-only
  --no-renames "$BASE" --` and writes its lines to `$WORK/base.moved`. Observed by AC1 and AC3.
- **S2** — In the guard pass, a leg whose every guard is plain, by the predicate `build_input_keys`
  applies today, is skipped exactly when no line of `$WORK/base.moved` IS one of its guards or sits
  under one. A guard ending in `/` matches only paths under it. Observed by AC1 and AC2.
- **S3** — A leg with any non-plain guard is decided by `changed` as today. So is every guarded leg
  when the one diff exits non-zero, or when a line of its output starts with `"`, a path git still
  quotes. Observed by AC2 and AC4.
- **S4** — The plain-guard predicate becomes one function, `check_plain_guard`, called by
  `build_input_keys` and by the guard pass, so the two can never disagree about which guards are
  plain. Observed by AC5.
- **S5** — The held-selection program, under `GATE_SELFTESTS=changed`, reads `$WORK/base.moved`
  instead of running its own `diff --name-only --no-renames <sha>` for a recorded sha equal to
  `BASE`. A recorded sha that differs from `BASE` keeps its own read. Observed by AC6.
- **S6** — `memory/guides/SESSION-KICKOFF.md` re-stamps `last-audit` in the commit that lands S1,
  because `tools/run-gates/run-gates.sh` is on its `watch:` line. Observed by AC7.

## 3. Non-goals (OUT)

- No change to the docs mode: `check_doc_moved` diffs `DOCS_BASE` and walks a log, a different base
  and a different question.
- No change to the guard-matching rule, to which guards are plain, or to the base derivation.
- No change to `doc_reads` selection under `GATE_SELFTESTS=changed`, the mechanism
  `memory/gotchas/changed-mode-selection-ignores-doc-reads.md` names as a separate unit.
- No cache and no switch. The one diff answers the same question every per-leg diff answered, in
  the same bar, so it is a read, not a stored answer; a switch would choose between two reads of
  one fact.
- No change to `tools/run-gates/verdict_flow.py`. Its `select` reads every input at R from git and
  runs no diff against the working tree, so it has no read this unit could share.

### Edges

- **consumes-from** external — dWitnessedBar's landed tip, which this unit is built on, because that
  branch rewrites the hold and selection block of `tools/run-gates/run-gates.sh`.

## 4. Design

### The guard pass today

All citations are read at `609cd40b1`.

`changed` returns true under `GATE_FULL` or an empty `BASE`, and otherwise runs
`! git diff --quiet "$BASE" -- "$@"` (`tools/run-gates/run-gates.sh@609cd40b1:598`). A git error
reads as changed, so the leg runs. The guard pass calls it once per guarded leg that no hold, docs
skip or earlier decision took (`tools/run-gates/run-gates.sh@609cd40b1:3431`), in a serial loop.
Under the default bar of this repository, 8 of the 73 guarded legs reach it; under
`GATE_SELFTESTS=1`, all 73 do. Both counts are DERIVED from `tools/gate-legs.json` at `609cd40b1` and
re-derived by AC3.

The held-selection program runs `diff --name-only --no-renames <sha>` once per distinct recorded sha
(`tools/run-gates/run-gates.sh@609cd40b1:3345`) and matches by `check_hit`, the same dirt rule.

### The dirt rule, already written once

`build_input_keys` classes a guard as plain when it holds only `[A-Za-z0-9._/@+=-]` and is not empty,
`.`, `./`, absolute, magic, or carrying `..` or `//`
(`tools/run-gates/run-gates.sh@609cd40b1:3547`). For plain guards its slice awk matches a path that
IS the guard, unless the guard ends in `/`, or that starts with the guard and a `/`
(`tools/run-gates/run-gates.sh@609cd40b1:3573`). That is what git's pathspec does for a plain guard,
which the comment above the awk states. S2 applies that same rule to the moved list, through one
`awk` over `$WORK/base.moved` and a `name<TAB>guards` file, writing one `skip` file per untouched
leg.

### Why `--no-renames` and `--`

A per-leg `git diff --quiet BASE -- <guard>` limits the diff to the guard before rename detection,
so a file renamed out of the guard reads as deleted inside it. A whole-tree diff with renames on
would print only the new name, and the guard would miss the move. `--no-renames` prints both names.
`--` keeps a path named like a revision from being read as one.

### What stays per leg

A non-plain guard, a quoted output line, and a failed diff each keep today's call for the legs they
touch, so a guard the in-process rule cannot answer is still answered by git.

### Files touched (estimate)

`tools/run-gates/run-gates.sh` · `tools/run-gates/run-gates.test.sh` · `memory/guides/SESSION-KICKOFF.md` (its `last-audit` re-stamp)

### Inventory

| Minted identifier | Kind | Naming cell | Graded by |
|---|---|---|---|
| `check_plain_guard` | shell function in `run-gates.sh` | none in this repo's lexicon for runner helpers | AC5 |
| `base.moved` | a file under the runner's `$WORK` | none; `$WORK` is swept with the run | AC1 |

### Alternatives rejected

| Alternative | Why it loses |
|---|---|
| Run the per-leg diffs in parallel | Same process count, and the skip verdict would depend on scheduling, which the pass's own comment rules out. |
| Match every guard in-process, globs and magic included | It re-implements git's pathspec, and a disagreement would skip a leg that should run. |
| Reuse `verdict_flow.py select` | It reads at R and never diffs the working tree. |

## 5. Production-readiness checklist

- security: N/A — a read of the repository's own diff into the run's swept `$WORK`.
- perf / scale: on this repository's default bar the guard pass goes from 8 git processes to 1,
  and under `GATE_SELFTESTS=1` from 73 to 1 (AC3).
- error / empty / loading states: a failed diff or a quoted path falls back to today's per-leg
  call (S3); an empty `BASE` or `GATE_FULL` runs every leg as today.
- observability: the `GATE skip` lines are unchanged.
- risks: a dirt-rule mismatch would skip a leg that should run. S4 keeps one predicate, and AC1
  compares every guarded leg's answer with git's own.
- testing: the equivalence probe (AC1), the fallbacks (AC2, AC4), the count (AC3).
- migration: none.
- user docs: `help/` holds no page on guard evaluation; the runner's comment above the pass is
  updated in place.

## 6. Acceptance criteria

- **AC1** — When a probe runs, in a scratch `git clone --shared` at `609cd40b1`, both today's
  `git diff --quiet "$BASE" -- <guards>` and the new in-process rule for every guarded leg of
  `tools/gate-legs.json`, against five bases (HEAD, HEAD~1, HEAD~20, the merge-base with `main`, and
  the build's base), with one tracked file edited uncommitted and one renamed, the two answers agree
  for every leg and base.
  Red when: any leg's skip decision differs from git's.
  fixture: a clone under `%TEMP%` with its own `TEMP`.
- **AC2** — When the guard-pass `awk` is fed a moved list holding only `xga/f` and a leg guarded by
  `ga/`, the leg is skipped; fed `ga/f`, it runs; and a leg guarded by the file name `ga` is not
  matched by a path `ga/` names as a directory unless the path sits under it.
  Red when: a substring match takes `xga/f` for `ga/`, or a directory guard matches a file of its name.
- **AC3** — When AC1's probe runs under `GIT_TRACE2_EVENT=<dir>`, one directory per side, the old
  side holds one `diff` event per guarded leg it decides and the new side holds one `diff` event in
  all, the two counts printed side by side. When the main loop runs a bar's guard pass over the AC1
  clone under the same variable at the close, the directory holds one `diff` event for the guard
  pass, against today's one per guarded leg reaching it.
  Red when: a per-leg `diff --quiet` survives for a plain-guarded leg.
  figure: the per-leg count is DERIVED from the manifest at observation.
  permission: a role agent runs no runner, a fixture copy included (scratch-guard row G2), so the
  bar's own count is owed to the main loop; the pass makes the probe's count.
- **AC4** — When the guard pass's fallback test, extracted from the edited runner into a probe
  script as AC2 extracts its `awk`, is given a diff status of 128, and separately a moved list
  holding a line that starts with `"`, it decides every guarded leg by `changed`. The main loop
  observes the runner's own `GATE` lines equal the old runner's in both cases, through the `New
  arm:` line of section 7.
  Red when: a failed or quoted read skips a leg.
  permission: the runner's `GATE` lines are owed to the main loop (scratch-guard row G2).
- **AC5** — When `grep -c 'check_plain_guard' tools/run-gates/run-gates.sh` runs, it prints 3 or more,
  the definition and its two callers, and the inline `case` at `build_input_keys` is gone.
  Red when: the guard pass and the input keys each keep their own predicate.
- **AC6** — When `grep -n 'base.moved' tools/run-gates/run-gates.sh` runs, it prints the one write
  of S1, the guard pass's read and the held-selection program's read under the sha-equals-`BASE`
  test. When the main loop runs the held-selection program in changed mode at the close, with a
  last-run record whose sha equals `BASE`, the trace holds no second `diff --name-only` for that
  sha, and the `selftests changed` lines equal the old runner's.
  Red when: the program still diffs a sha equal to `BASE`.
  permission: changed mode is a bar run, owed to the main loop (scratch-guard row G2); the pass
  makes the `grep`.
- **AC7** — When `bash skills/session-kickoff/manifest-check.sh --staged` runs over the commit that
  lands S1, it exits 0.
  Red when: the watched runner moves without the `last-audit` re-stamp.

## 7. Gates

`run-gates canary` · `kickoff-manifest ratchet` · `recall floor` · `recall floor arms` · `line length` · `shell hygiene (a loop fed by a command substitution)` · `spec tokens (a spec's own names resolve)`

New arm: tools/run-gates/run-gates.test.sh · covers AC2 AC4 AC6 · a fixture manifest with a plain directory guard, a near-miss path, a glob guard, a planted failing diff and a last-run record whose sha equals the base; its failing case is staged by matching the guard as a substring, by reading a failed diff as clean, and by diffing the recorded sha again · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-20 · initial draft.
- rev-2 · 2026-11-22 · under `2026-11-22-prompt-TOOL-dQuietDisk-1-divergence-task`. AC3, AC4 and
  AC6 had the pass run the runner, which a role agent may not run in any form. AC3's figure now
  comes from AC1's probe, AC4's from the extracted fallback test, and AC6's from a `grep`; the bar's
  own count, `GATE` lines and changed-mode trace are owed to the main loop, and the `New arm:` line
  covers AC6 too. `check_plain_guard`, the one name this spec mints, passes `--suggest`.

## 10. Reuse audit

The seam extended is the runner's own dirt rule: the plain-guard `case` and the slice `awk` of
`build_input_keys` (`tools/run-gates/run-gates.sh#build_input_keys`), extracted at its second caller
into `check_plain_guard` per the charter's reuse rule. The held-selection program's per-sha diff is
the second read S5 shares. The chain build owning the area is dWitnessedBar (Test: gate health),
whose branch moves both blocks; this unit is built on its landed tip and contradicts none of
TOOL-dWitnessedBar-5's hold rules, since only guard-skips are decided here.

`python tools/codebase-map/reuse_lookup.py "one git diff name-only read once for every guarded leg"`
returned name-token neighbours only (`read_text`, `read`, `git`, `read_bytes`). Recall over the
terms below returned nothing, twice, which is recorded as an answer. No existing seam fits beyond the
runner's own rule.

Recall terms used: changed guard pathspec git diff quiet BASE guarded leg skip plain guard slice dirt rule
