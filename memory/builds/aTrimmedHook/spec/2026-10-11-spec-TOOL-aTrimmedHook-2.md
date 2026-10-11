# TOOL-aTrimmedHook-2 — the staged hygiene leg spends no process on a check its staged set cannot reach

**Status:** SPECCED · rev-2 · 2026-10-11 · node a · Tier-2 · base b726385f · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-11-prompt-TOOL-aTrimmedHook-1-brief.md](../prompts/2026-10-11-prompt-TOOL-aTrimmedHook-1-brief.md) | research | TOOL-aTrimmedHook-1 TOOL-aTrimmedHook-3 KICK-aTrimmedHook-1 |

<!-- /gen:spec-records -->

## 1. Goal

Outside check 9, the staged hygiene leg spends about 220 s on node a (2026-10-11, 64-82 host bash
processes) in 52 source lines of roughly 4 s each. Almost every one is a whole-tree pipeline that
still runs when nothing staged is in its population, and several grade the whole tree's names on
every commit. This unit narrows the leg to the staged files and their build folders, and skips
every pipeline whose narrowed population is empty. Every skip that changes a verdict is announced,
and the full run (`STAGED=0`) grades exactly what it did at BASE.

## 2. Scope (IN)

All in `tools/memory-tree/check-memory-hygiene.sh` unless named.

- **S1 — the narrowed listing.** The staged set is read right after `FILES` with ONE
  `git diff --cached --name-status --diff-filter=ACMR` over the memory root, replacing the BASE
  `--name-only` call and its `sort`. `STAGED_MD` is the tracked listing filtered to that set, so it
  keeps the listing's order; `STAGED_NEW` holds the Added, Copied and Renamed paths. Under
  `STAGED=1`, `FILES` becomes the staged paths plus every tracked file in those paths' own
  `builds/<slug>/` folders, and `FILES_ALL` keeps the whole listing for the checks that resolve
  across it. One line announces the narrowing and that the push-boundary run grades the whole tree.
  Observed by AC1 and AC8.
- **S2 — no unread work.** The `PRE_*` preconditions are computed only under `STAGED=0`, and every
  `pop_guard` call is skipped under `STAGED=1`, so its argument substitutions do not run;
  `pop_guard` already returned first under `--staged` at BASE. Observed by AC8.
- **S3 — names only where a name is new.** Checks 1, 3, 4 and 5 grade path NAMES. Under `STAGED=1`
  they run only when `STAGED_NEW` is non-empty, over the narrowed listing; otherwise one announced
  line says this commit stages no new name. Observed by AC2.
- **S4 — check 2's selection without forks.** Under `STAGED=1`, `scan2` is built from `STAGED_MD`
  by a bash loop applying the same filter (`.md`, outside `DECISIONS.md`, `decisions/`, `archive/`).
  Observed by AC3.
- **S5 — the index set only when an index file is staged.** Under `STAGED=1`, `index_set` and
  `VIEW_SET` run only when a staged path is of an index kind (the kinds `index_set` enumerates, by a
  bash `case`); otherwise both are empty, which is the selection `in_scope` would have produced.
  Observed by AC4.
- **S6 — check 10 held unless its inputs are staged.** Under `STAGED=1`, check 10 runs over
  `FILES_ALL` only when a staged path matches `ROTATED_ARCHIVE_ERE` or is named `DECISIONS.md` or
  `<FAMILY>.md`; otherwise one announced HELD line. Observed by AC5.
- **S7 — check 21's selection only where it is read.** `c21_sel` is computed only under `STAGED=0`,
  its one consumer's condition. Observed by AC8.
- **S8 — check 12's demultiplexer only on output.** The sentinel-routing pipelines after the check-12
  pass (`base12`, `edge12`, `rd25` and their `grep -v` partners, `bad25`, `_rdtok`) are skipped when
  their input is empty, producing the same empty values without a process. Observed by AC8 and AC7.
- **S9 — the stale-line guard held unless its lists are staged.** Under `STAGED=1`, the legacy/debt
  stale-line guard and its whole-repo `TRACKED_SET` run only when
  `memory/project/legacy-files.txt` or `memory/project/curation-debt.txt` is staged; otherwise one
  announced HELD line. Observed by AC6.
- **S10 — two fork-free derivations.** `FAM_ALT` and `DISC_ALT` are joined in bash in both modes,
  byte-identical to the BASE `paste` pipelines' output. Observed by AC7.
- **S11 — the arms.** `tools/memory-tree/check-memory-hygiene.test.sh` gains staged arms for AC2 to
  AC6, after the existing `--staged` block. Observed by AC2 to AC6.

## 3. Non-goals (OUT)

- **N1** — no change to any check's verdict under `STAGED=0`; AC7 compares the whole-tree output.
- **N2** — no change to the corpus joins already held under `--staged` (13-16, 17-19, 20, 23, 24, 27,
  28, check 12's edge joins, check 21's bindings).
- **N3** — a staged DELETION is not graded under `--staged`, as at BASE (`--diff-filter=ACMR`).
- **N4** — check 9 is TOOL-aTrimmedHook-1's.
- **N5** — no change to `.githooks/pre-commit`, which still invokes the leg only when `memory/**` is
  staged.

### Edges

none

## 4. Design

### The cost is processes, not bytes

Profiled at BASE with `bash -x` and an `EPOCHREALTIME` PS4, each interval attributed to the line that
ends it, staging one `RUN.md` line. The run took ~293 s; 53 lines cost ≥2 s and ~15600 cost about
nothing. Every costly line is one pipeline or one `$(…)`, each process costing 1-2 s on a contended
node. Narrowing `FILES` shortens every grep, but a grep over ten lines costs the same process as one
over four thousand, so each unit of saving is a pipeline that does not START. That is why S2 to S9
are guards and S1 alone would save only the per-element loops (check 10's, the index set's,
check 5's).

### Which checks may narrow, and how

| check | BASE under `--staged` | after | announced |
|---|---|---|---|
| 1, 3, 4, 5 | whole tree's names | new names only (S3) | yes, when skipped |
| 2 | staged `.md` files | same set, no fork (S4) | no, same set |
| 6, 7 | `INDEX_SET` ∩ staged | same, skipped when empty (S5) | no, same set |
| 10 | every archive | held unless an archive or live index is staged (S6) | yes |
| 12, 25 | staged specs | same; demultiplexer skipped on empty (S8) | no, same set |
| 21 | selection computed, never read | not computed (S7) | no |
| 22 | every review record | narrowed listing (S1) | yes, by the S1 line |
| stale-line guard | whole repo | held unless a list is staged (S9) | yes |

### Absence-type predicates — none narrow wrongly

A narrowed listing false-reds only a check that asserts PRESENCE across the tree. Read at BASE:
check 3 refuses unexpected entries and never requires one (~563-645); check 4's `flush` reports bad
entries per folder and demands no README (~684-728, its own comment says so); check 5 grades each
name alone. Check 10 resolves a live index by basename across the tree (~1330-1351), which a narrowed
listing would mis-resolve, so S6 runs it over `FILES_ALL`. `TRACKED_SET` has one other reader
(~2652), inside a `STAGED = 0` block.

### Fork-free equivalents (S10)

`FAM_ALT` at BASE is `for p in $FAMILIES; do echo "${p#*:}"; done | paste -sd'|' -`; the bash form
joins the same tokens with `|` in a loop, with its own loop variable so no global moves. `DISC_ALT`
likewise over `$DISCIPLINES`. `LEGACY` and `DEBT` keep their `grep`: MSYS grep drops a trailing CR
that a bash `read` keeps, so a shell reader would answer differently from the BASE pipeline on one
platform, which is two answers to one question for two processes' saving.

### Files touched (estimate)

- `tools/memory-tree/check-memory-hygiene.sh`
- `tools/memory-tree/check-memory-hygiene.test.sh`
- `tools/memory-tree/README.md`

### Rollout

Order 2, after TOOL-aTrimmedHook-1. Line numbers above are BASE's and move with that unit. The arms
are developed against a slice of the self-test (prologue plus the new block, inside the kit dir,
deleted before commit and before any `gen_map.py --write`). The memory-tree version bump is the
build's, after the last unit. `tools/memory-tree/README.md`'s `--staged` sentence (~504) states the
narrowed scope.

### Alternatives rejected

- **Narrow `FILES` and nothing else** (the prompt's wording). Saves only the loops, about 30-40 s of
  ~220 s, because the cost is processes. The owner chose narrowing plus skipping empties.
- **Hold checks 1, 3, 4 and 5 entirely under `--staged`.** A badly named new file would then pass the
  commit and red only at the push; grading new names keeps that signal at the commit for free.

## 5. Production-readiness checklist

- security — N/A — a gate's selection logic over the local index; no new input surface.
- perf / scale — the point: a one-file `RUN.md` stage starts no process in checks 1, 3, 4, 5, 6, 7,
  10, 21 or the stale-line guard, and none for the preconditions.
- error / empty / loading states — an empty staged set selects nothing everywhere, as at BASE.
- observability — four announced lines: the narrowing (S1), the name checks (S3), check 10 (S6) and
  the stale-line guard (S9).
- risks — a pre-existing violation outside the staged neighborhood no longer reds an unrelated
  commit; it reds at the push boundary, which is the owner's ask. An absence-type predicate missed
  by the audit would false-red a commit; AC2 to AC6 exercise each guarded check both ways.
- testing — AC2 to AC6 are self-test arms; AC7 compares whole-tree output; AC8 is a profile.
- migration — none; the full run is unchanged.
- user docs — the kit README's `--staged` sentence.

## 6. Acceptance criteria

- **AC1** — When `bash tools/memory-tree/check-memory-hygiene.sh --staged` runs with one tracked
  `RUN.md` line staged, its output carries the narrowing line.
  Red when: the line is absent.
- **AC2** — When `check-memory-hygiene.sh --staged` runs in the self-test's fixture tree and the arm stages a NEW recording file with a malformed
  name, the staged leg reports check 5 for it; staging only a one-line edit to an existing file
  prints the S3 line and no check 1, 3, 4 or 5 finding, while an unstaged badly named file exists.
  Red when: the new name is not reported, or the edit-only stage reports one.
  cost: seconds per arm, run through a slice of the self-test.
- **AC3** — When `check-memory-hygiene.sh --staged` runs in that fixture tree and the arm stages a `.md` file carrying a broken relative link, the staged leg
  reports check 2 for it.
  Red when: it does not.
- **AC4** — When `check-memory-hygiene.sh --staged` runs in that fixture tree and the arm stages an over-cap index file, the staged leg reports check 6 or 7
  for it; with only a non-index file staged, neither check reports.
  Red when: either expectation fails.
- **AC5** — When `check-memory-hygiene.sh --staged` runs in that fixture tree and the arm stages a rotated archive its live index does not reference, check 10
  reports it; with no archive or live index staged, the HELD line prints and check 10 reports
  nothing.
  Red when: either expectation fails.
- **AC6** — When `check-memory-hygiene.sh --staged` runs in that fixture tree and the arm stages `memory/project/legacy-files.txt` listing an untracked path,
  the stale-line guard reports it; with the list unstaged, the HELD line prints.
  Red when: either expectation fails.
- **AC7** — When `bash tools/memory-tree/check-memory-hygiene.sh` runs with no argument on the real
  tree at BASE and after this unit, the two outputs agree line for line except for lines naming this
  build's own files.
  Red when: any other line differs.
  cost: two full runs, each up to the leg's ceiling on a contended host.
- **AC8** — When the BASE profile instrument (`bash -x`, `EPOCHREALTIME` PS4, one staged `RUN.md`
  line) runs after this unit, none of the S2, S3, S5, S6, S7, S8 or S9 lines costs a process.
  Red when: any of them appears among the lines costing ≥1 s.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `harness arms (fail branches armed or pinned)` · `check-arms selftest` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `kit version markers`

New arm: tools/memory-tree/check-memory-hygiene.test.sh staged narrowing · covers AC2 AC3 AC4 AC5 AC6 · each guard inverted so the staged case skips, and `STAGED_NEW` forced empty · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-11 · initial draft, from the brief and the BASE profile.
- rev-2 · 2026-10-11 · AC2 to AC6 name the checker run on a fixture, not the suite that hosts the fixture, after `--dispatch`'s spec-token check refused the suite form

## 10. Reuse audit

No new mechanism: the unit reuses the leg's own `in_scope` and `STAGED_SET` (~500-505 at BASE), the
`case`-based membership idiom the file already prefers over forks (the `LEGACY_SET` comment, ~341),
and its HELD-line convention (check 23, the curation-debt guard). `python
tools/codebase-map/reuse_lookup.py "narrow the hygiene file list to the staged set"` returned only
name-stem matches (`corpus_files`, `read_id_list`, `resolve_pattern_sets`). Recall surfaced
`TOOL-aThawedCorpus-5`, which held check 23 under `--staged` for the same process-cost reason, and
the 2026-08-30 lens review listing which checks the staged leg holds.

Recall terms used: staged pre-commit hygiene check 9 gen_build_index fork spawn cost manifest-check C6 commit-msg check-commit
