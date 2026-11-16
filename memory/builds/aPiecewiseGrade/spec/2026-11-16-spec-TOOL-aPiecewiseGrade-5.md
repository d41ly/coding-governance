# TOOL-aPiecewiseGrade-5 — the spec-token checker's 24 per-spec counter names live in one tuple, and a mismatch is loud or a miss, never a silent 0

**Status:** SPECCED · rev-1 · 2026-11-16 · node a · Tier-2 · base aebbb4a72 · streams tooling · order 5

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-16-prompt-TOOL-aPiecewiseGrade-5-1-spec-writer.md](../prompts/2026-11-16-prompt-TOOL-aPiecewiseGrade-5-1-spec-writer.md) | journal | — |
| [2026-11-16-prompt-TOOL-aPiecewiseGrade-5-review-brief.md](../prompts/2026-11-16-prompt-TOOL-aPiecewiseGrade-5-review-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

`scan_live_spec` returns its 24 counters as a literal dict, and `main` sums them into a
`collections.Counter` and reads them back by names typed a second time. A Counter answers 0 for a
key it does not hold, so a name misspelled on either side prints a 0 in the summary and raises
nothing. With this unit the names live once, in `SPEC_COUNTERS`. A misspelled name raises, a fresh
or cached counter set of another shape fails loudly or is a miss, and four arms expect nonzero values
for the four counters the suite only ever saw at 0. The closing review's item 2 is the source
(`2026-11-16-review-TOOL-aPiecewiseGrade-1-diff-review-round1`, ids 2, 3 and 5).

## 2. Scope (IN)

- **S1** — A module tuple `SPEC_COUNTERS` holds the 24 counter names once, in the order of today's
  return dict. Observed by AC6.
- **S2** — `scan_live_spec` counts into `counts = dict.fromkeys(SPEC_COUNTERS, 0)`. Every counter
  increment writes `counts["<name>"]`, and the function returns `(hits, near, counts)`. Its docstring
  says the counters are the names `SPEC_COUNTERS` holds. Observed by AC1, AC2 and AC3.
- **S3** — `main` sums into `totals = dict.fromkeys(SPEC_COUNTERS, 0)`. Before summing each spec's
  `got[2]`, fresh or cached, it raises `KeyError` naming the spec and the differing names when that
  key set is not `SPEC_COUNTERS`. The read-back keeps its names and now reads a plain dict, so a
  misspelled name raises `KeyError`. The `import collections` line goes, because nothing else in the
  checker uses it. Observed by AC1, AC3 and AC6.
  **Readers:**
  by name: `tools/check-spec-tokens.py` alone spells `collections`, on its import line and on the
  line binding the totals, by a whole-word grep at fccef94ef.
  by value: NO VALUE READERS — a module binding, read only by the one call this item rewrites.
- **S4** — `read_spec_cache` returns None, a miss, when an entry's `counts` key set is not
  `SPEC_COUNTERS`, before it copies the entry into the next generation. Its docstring adds that
  condition. Observed by AC4.
- **S5** — Four arms in the spec-tokens suite each expect one counter nonzero: `skipped`, `so_bare`,
  `ao_graded` and `ao_bad`. `FLOOR_ASSERTIONS` rises from 278 to 282 with its RAISED comment.
  Observed by AC5 for the values the arms expect. The arms themselves are the main loop's, observed
  RED then GREEN at the close under §7's `New arm:` lines.
- **S6** — `memory/gotchas/two-answers-to-one-question.md` gains a read-back form, with its check
  line, because no gate covers the class. Observed by AC7.

## 3. Non-goals (OUT)

- No edit to any CLOSED spec of this build. A correction to a closed unit belongs to this unit.
- No change to a verdict, a refusal line, a report line, the summary line or an exit status of the
  checker or of `--dispatch`. The raise in S3 is reachable only by an edit to the checker (§4).
- No row raised in any shrink-only registry.
- No edit to `tools/unattended/unattended.sh`, which TOOL-aPiecewiseGrade-6 writes concurrently.
- No change to the cache key, the context digest, the entry format or which segments write an entry.
- No predicate or lint over other `collections.Counter` read-backs in the tree. Five sites exist
  under `tools/`, by `grep -rn` at fccef94ef, and none is this unit's. S6 is the left-shift.
- No change to the counters' meaning, their print lines, or the order of any output line.

### Edges

- **consumes-from** external — TOOL-aPiecewiseGrade-1's `scan_live_spec`, its cache entry and its PG1 arm, and TOOL-aPiecewiseGrade-4's named next generation. Both specs are CLOSED and frozen, and predate this unit, so they declare no hands-off here. This unit changes how the counters are named and summed and nothing else they built

## 4. Design

### What the code does today

Read at `fccef94ef`, the tip of this build's branch. The header's base `aebbb4a72` is the build's
base on the default branch, and it predates `scan_live_spec`, which TOOL-aPiecewiseGrade-1 built on
this branch. Every citation below is blob-pinned to the code that exists. The checker's blob is
`93a5d813`, the suite's `ac37f167` and the gotcha record's `e353a387`.

- `scan_live_spec` (`tools/check-spec-tokens.py#scan_live_spec`) binds its 24 counters as locals
  across eight lines (`tools/check-spec-tokens.py@93a5d813:2106` to
  `tools/check-spec-tokens.py@93a5d813:2113`) and returns them in a literal dict
  (`tools/check-spec-tokens.py@93a5d813:2286`). Its 27 increment lines are `+=` on those locals, by
  a grep over the function at fccef94ef.
- `main` binds `totals = collections.Counter()` (`tools/check-spec-tokens.py@93a5d813:2437`), runs
  `totals.update(got[2])` per spec (`tools/check-spec-tokens.py@93a5d813:2451`) and reads the 24
  names back at `tools/check-spec-tokens.py@93a5d813:2452` to
  `tools/check-spec-tokens.py@93a5d813:2459`. The totals feed print lines alone and gate no exit
  status.
- `read_spec_cache` (`tools/check-spec-tokens.py#read_spec_cache`) keeps any `counts` key as
  `{str(k): int(v)}` (`tools/check-spec-tokens.py@93a5d813:2057`) and then copies the entry's two
  files into the next generation (`tools/check-spec-tokens.py@93a5d813:2059`). Its `except` already
  turns `KeyError` and `ValueError` into a miss (`tools/check-spec-tokens.py@93a5d813:2061`).
- `write_spec_cache` dumps `got[2]` as the entry's `counts`
  (`tools/check-spec-tokens.py@93a5d813:2088`).
- The context digest hashes this checker's own bytes (`tools/check-spec-tokens.py#derive_spec_context`),
  so every entry written before the build misses once after it.
- The suite asserts only 0 for the four counters. The skip arm matches `citation(s) skipped` with
  no number (`tools/check-spec-tokens.test.sh@ac37f167:564`), and the ac-order arms expect `0 of 1`
  and `0 out of order` (`tools/check-spec-tokens.test.sh@ac37f167:1067`,
  `tools/check-spec-tokens.test.sh@ac37f167:1070`). The bare-source arm matches the hit line, not
  the count (`tools/check-spec-tokens.test.sh@ac37f167:2118`).
- An uncaught exception exits 1 with a traceback and no summary line, because the module's entry
  point calls `sys.exit(main(...))` with no handler. The house rule reads an exit 1 with no summary
  line as the checker refusing, never as a hit.

### S1 — the tuple

```python
SPEC_COUNTERS = ("skipped", "graded", "ungraded", "noheading", "bar_examined", "bar_specs",
                 "bar_carriers", "g_examined", "g_specs", "g_carriers", "g_nosubhead", "g_nogates",
                 "c_runs", "c_specs", "c_cleared", "cv_lines", "cv_specs", "cv_carriers", "cv_graded",
                 "so_examined", "so_specs", "so_bare", "ao_graded", "ao_bad")
```

It sits beside the other module constants, above `read_spec_cache`, with a comment saying
`scan_live_spec` returns these and `main` reads them back. The order is today's return dict's, so
an entry's `counts` JSON keeps its key order.

### S2 — one seeded dict per spec

The eight binding lines shrink to `hits, near = [], []` and `counts = dict.fromkeys(SPEC_COUNTERS, 0)`.
Each of the 27 increment lines becomes `counts["<name>"] += <value>`. A misspelled name at an increment,
or one the tuple lacks, raises `KeyError` on the first spec that reaches it. The source join's three
increments and the claims join's three run on every spec, so a misspelled name there raises on every
run.

### S3 — the sum, the check and the read-back

```python
hits, near, seen_waived, totals = [], [], set(), dict.fromkeys(SPEC_COUNTERS, 0)
...
    if got[2].keys() != totals.keys():
        raise KeyError(f"{f}: counter names {sorted(got[2].keys() ^ totals.keys())} are not SPEC_COUNTERS")
    for k, v in got[2].items():
        totals[k] += v
```

The check runs after `got` is settled, on the fresh and the cached branch alike, before `hits` and
`near` take it. The read-back lines keep their bytes. On a plain dict a name it misspells raises
`KeyError` before the first print.

The check catches what S2 cannot: an assignment such as `counts["x"] = 0` adds a key with no raise.
On today's code paths it fires only after an edit to the checker, because S2 seeds every fresh set
and S4 turns away every other cached one. That is why it raises rather than printing a refusal
line: it is an invariant of the checker's own code, and §3 keeps every refusal line as it is.

### S4 — a cached set of another shape is a miss

After the `counts` parse, `if counts.keys() != set(SPEC_COUNTERS): return None`, ahead of the copy.
The entry then re-grades and `write_spec_cache` writes a fresh one. The entry's key does not cover
`counts`, so without this an edited `counts` with a valid key would be a hit.

### S5 — the four arms

Each is one `arm` call beside an existing fixture, so no fixture is built anew. The values were
observed over a one-spec scratch fixture built as `scratch` builds it, on 2026-11-16 at fccef94ef.

| counter | placed after | rc | expected substring |
|---|---|---|---|
| `skipped` | the skip arm, `tools/check-spec-tokens.test.sh@ac37f167:564` | 0 | `token(s) graded · 1 citation(s) skipped (untracked path)` |
| `ao_bad` | the ac-order red arm, `tools/check-spec-tokens.test.sh@ac37f167:1064`, same state | 1 | `graded at/after SPEC_AC_ORDER_CUTOFF 2026-09-02 · 1 out of order` |
| `ao_graded` | the reset at the ac-order block's end; the clean spec, `SPEC_AC_ORDER_CUTOFF="2026-09-02"` written and added, then reset again | 0 | `ac-order join · 1 of 1 live spec(s) · graded at/after SPEC_AC_ORDER_CUTOFF 2026-09-02 · 0 out of order` |
| `so_bare` | the bare-source arm, `tools/check-spec-tokens.test.sh@ac37f167:2118`, same fixture | 1 | `1 sourced file(s) examined in 1 live spec(s) · 1 by bare name` |

The `ao_graded` arm uses a spec in order, so it stays green when only `ao_bad` is misspelled, and the
`ao_bad` arm reds alone then. The new comment above `FLOOR_ASSERTIONS` reads `RAISED 278 -> 282 by
TOOL-aPiecewiseGrade-5: its four nonzero-counter arms, each top-level. Counted by reading; OWED:
observed at the close.`

### S6 — the gotcha's read-back form

A section `## The read-back form — counters returned by one function and read back by typed names`
goes after the count form. It names this instance by unit and review record, and ends:

```
**The check:** a dict returned by one function and read back by typed names elsewhere is
single-sourced, and is not read through a defaulting container.
```

No gate covers the class: nothing grades the five other `collections.Counter` sites under
`tools/`. TOOL-dTieredTribunal-5's backlog entry found no obviously safe static predicate for a
neighbouring false-clean family, returned counters a prompt never interpolates, and named a gotcha
record as the cheap left-shift. The record is universal, so
`gotchas.py --for-diff` puts it on every review checklist.

### What the design does not check

- **A counter that is counted wrongly.** The tuple proves the names agree. It does not prove an
  increment adds the right value; the four arms pin one value each, over one fixture each.
- **A counter added to the tuple and never incremented.** It reads 0 everywhere, as a real zero
  does. Only a print line naming it and an arm expecting it nonzero would show it.
- **A forged cache entry.** S4 checks the key set, not the values. The bar's leg runs the plain
  check, as TOOL-aPiecewiseGrade-1 recorded.
- **Other read-backs in the tree.** S6 is a checklist line, not a gate.

### The pass probe, `$SCRATCH/pg5.sh`

`$SCRATCH` is the run's scratch directory. `same` is 1 when stdout, stderr and the exit status equal
the base copy's plain run over the same tree. The base copy is the checker blob the build starts
from, `93a5d813` at this writing, written as a sibling of the checker under test with `.base.py` in
place of `.py`. It resolves its kit from the same directory, and no output line names the checker's
own file (`grep -c check-spec-tokens` over a plain real-tree run at fccef94ef printed 0). Each cached
run names a fresh `mktemp -d` beside its cache, and each promotion moves that directory over the
cache, as the PG1 arm does.

| row | what happens | what it prints |
|---|---|---|
| `real` | over this worktree: the base copy plain, the built checker plain, then cold cached, promote, warm cached | `real plain <0|1> cold <0|1> warm <0|1>` |
| `pg1` | the PG1 arm's fixture and its eleven steps (`tools/check-spec-tokens.test.sh@ac37f167:2370` to `tools/check-spec-tokens.test.sh@ac37f167:2436`); at each step the base copy plain, the built checker plain and cached, then the promotion | `pg1 steps 11 plain <n> cached <n>`, each `<n>` the steps whose run was `same` |
| `mut` | four mutant copies of the built checker in the fixture's tool root, each run plain over the final PG1 tree: `readback`, `so_bare` misspelled `so_bar` in `main`'s read-back alone; `increment`, the same in `scan_live_spec` alone; `tuple`, the same in `SPEC_COUNTERS` alone; `extra`, `counts["extra"] = 0` before `scan_live_spec` returns | `mut <name> rc <n> loud <0|1> summary <0|1>`; `loud` is stderr carrying `KeyError`, `summary` is stdout carrying a `live spec(s) ·` line |
| `cache` | over the warm PG1 cache, the first spec's entry edited three ways, each in a fresh copy of the cache: `renamed`, `graded` spelled `gradde`; `extra`, an `extra` key added; `dropped`, `ao_bad` taken out | `cache <variant> miss <0|1> same <0|1>`; `miss` is the spec named in the run's `graded.list` |
| `nonzero` | the four arms' fixtures of S5, built as the suite builds them, each run once | `nonzero skipped <n> so_bare <n> ao_graded <n> ao_bad <n>`, each `<n>` read from its summary line |

The probe deletes the base and mutant copies before it exits.

### Inventory

| identifier | kind | lexicon |
|---|---|---|
| `SPEC_COUNTERS` | module constant | `--suggest SPEC_COUNTERS --as py.constant` answers that `py.constant` is UNDECLARED: no cell grades it |
| `counts` | local of `scan_live_spec`, named as the cache entry's field already is | no declared cell for a local |
| the four arms' labels | suite assertion labels | no declared cell |

No function, conf key, check number or refusal line is minted. `--suggest tally --as py.function`
answered `measure`, so no local is named `tally`.

### Docs, and what the change owes beyond the code

- The docstrings of `scan_live_spec` and `read_spec_cache`, per S2 and S4. The header docstring's
  cache paragraph says a hit reuses a spec's "counters"
  (`tools/check-spec-tokens.py@93a5d813:292`), which stays true.
- No `help/` page names a counter's print line, by `grep -rln` at fccef94ef.
- The codebase map: the dossier `memory/map/features/spec-tokens.md` claims the checker and its
  suite by path, and neither path moves. The symbols index records functions, classes and JS const
  exports (6805, 103 and 10 at fccef94ef, PINNED), never a Python module constant, and no function
  is added or renamed, so it is not regenerated.
- The gotcha checklist line, per S6.
- No `kit.toml` names `check-spec-tokens`, by a grep at fccef94ef, so no kit version moves.

### Rollout

This unit builds at order 5, after TOOL-aPiecewiseGrade-1 to TOOL-aPiecewiseGrade-4 are CLOSED.
The first cached run after it lands misses on every spec once, because the context digest hashes the
checker's bytes. The suite gains four checker runs over one-spec fixtures, 0.79 s each (PINNED
fccef94ef, this node, one run over a scratch fixture).

### Files touched (estimate)

- `tools/check-spec-tokens.py`
- `tools/check-spec-tokens.test.sh`
- `memory/gotchas/two-answers-to-one-question.md`

### Alternatives rejected

- **Keep the locals and build the dict from a `locals()` snapshot.** One line, and a misspelling
  still raises, but it reads the frame by introspection, which a reader must know to trust. A seeded
  dict is the same idiom on both sides.
- **`dict(zip(SPEC_COUNTERS, (skipped, graded, ...)))`.** It trades a misspelling for a silent
  misalignment when the two orders differ.
- **A dataclass of 24 fields.** A class for one product, and the cache needs `asdict` both ways.
- **A `spec-tokens: REFUSING` line in place of the raise.** §3 keeps every refusal line, and the
  state is reachable only by editing the checker, which is a programming error, not an input.
- **Change the existing arms' substrings instead of adding arms.** The brief asks for one new arm
  per counter, and the existing arms' zero assertions keep their own meaning.

## 5. Production-readiness checklist

- security — N/A: no new input, write path or surface. The checker reads the same files and writes
  the same cache entries.
- perf / scale — a dict lookup per increment in place of a local, over 30 live specs; within noise
  of the 19 s real-tree run (PINNED fccef94ef, this node, 19.1 s). The suite gains four runs of
  0.79 s each.
- error / empty / loading states — a misspelled name raises `KeyError` and exits 1 with no summary
  line. A cached `counts` of another shape is a miss and re-grades.
- observability — the traceback names the spec and the differing names.
- risks — an unreachable raise looks like dead code to a later editor; the comment above it says
  which edit reaches it.
- testing — the pass probe above, and the four arms observed RED then GREEN at the close.
- migration — none. Old entries miss once on the context digest.
- user docs — N/A: no `help/` page names these lines.

## 6. Acceptance criteria

Each probe line comes from one run of `bash "$SCRATCH/pg5.sh"`, described in §4, removed after the
pass.

- **AC1** — When `bash "$SCRATCH/pg5.sh"` runs, it prints `real plain 1 cold 1 warm 1`.
  Red when: the built checker's plain or cached run over the real tree prints a byte, a line or an
  exit status the base checker's plain run does not.
  cost: four runs over the real tree, about 19 s each (PINNED fccef94ef, this node).
- **AC2** — When `bash "$SCRATCH/pg5.sh"` runs, it prints `pg1 steps 11 plain 11 cached 11`.
  Red when: a step's plain or cached run over the PG1 fixture differs from the base checker's plain
  run, as a counter summed from a misaligned or zeroed set would.
- **AC3** — When `bash "$SCRATCH/pg5.sh"` runs, it prints `mut readback rc 1 loud 1 summary 0`,
  `mut increment rc 1 loud 1 summary 0`, `mut tuple rc 1 loud 1 summary 0` and
  `mut extra rc 1 loud 1 summary 0`.
  Red when: `main` still reads through a `collections.Counter`, `scan_live_spec` still counts into
  locals, or `main` sums a `got[2]` whose key set it never compares.
- **AC4** — When `bash "$SCRATCH/pg5.sh"` runs, it prints `cache renamed miss 1 same 1`,
  `cache extra miss 1 same 1` and `cache dropped miss 1 same 1`.
  Red when: `read_spec_cache` keeps an entry whose `counts` key set is not `SPEC_COUNTERS`, so the
  run either sums it short or raises in `main`.
- **AC5** — When `bash "$SCRATCH/pg5.sh"` runs, it prints
  `nonzero skipped 1 so_bare 1 ao_graded 1 ao_bad 1`.
  Red when: a fixture of S5 no longer produces its counter, so the arm placed beside it would assert
  a value the run does not print.
  figure: PINNED, observed 2026-11-16 at fccef94ef over a one-spec scratch fixture.
- **AC6** — When `grep -cw collections tools/check-spec-tokens.py` runs it prints 0, and
  `grep -c '^SPEC_COUNTERS = (' tools/check-spec-tokens.py` prints 1.
  Red when: the `collections.Counter` read-back survives, or the names are not one module tuple.
- **AC7** — When `grep -c 'read back by typed names elsewhere is' memory/gotchas/two-answers-to-one-question.md`
  runs, it prints 1.
  Red when: the gotcha record carries no check line for the read-back form.

## 7. Gates

`spec-tokens self-test` · `spec tokens (a spec's own names resolve)` · `spec tokens (the pass's own spec)` · `policy fixtures` · `memory-hygiene self-test` · `build-index selftest` · `harness arms (fail branches armed or pinned)` · `lexicon naming predicates` · `gotchas selftest` · `recall floor` · `recall floor arms` · `memory hygiene`

New arm: tools/check-spec-tokens.test.sh · covers AC5 · the four nonzero-counter arms of S5, beside the skip, ac-order and bare-source arms; staged RED by misspelling each counter's name in main's read-back and then in scan_live_spec's increment, which reds its arm, and by restoring the Counter with one name misspelled, which reds that counter's arm alone · FLOOR_ASSERTIONS 278 to 282, which the close confirms

The close runs the bar once, after the last unit is terminal. This spec's author ran no gate but
the spec-token checker's `--spec` over this file.

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-16 · initial draft from brief `2026-11-16-prompt-TOOL-aPiecewiseGrade-5-1-spec-writer`,
  the owner's "Promote, build now" for item 2 of
  `2026-11-16-review-TOOL-aPiecewiseGrade-1-diff-review-round1`, grounded at `fccef94ef`.

## 10. Reuse audit

The seams this unit extends are TOOL-aPiecewiseGrade-1's own: `scan_live_spec`, `main`'s per-spec
loop and `read_spec_cache`, each changed in place, and the suite's `arm` helper and existing fixtures
for the four arms. `tools/codebase-map/reuse_lookup.py` for "a fixed set of counter names declared
once and summed across per-item results with a loud failure on a mismatched key set" ranked generic
`key`, `keys` and `counts` stems, `measure_typed_counts` in `tools/codebase-map/map_lib.py`, which
counts typed numbers in prose, and `check_count_sources` in `tools/runlog/record.py`, which grades a
record schema's count slots. Neither declares a counter set a caller sums, so no existing seam fits
beyond the checker's own. Recall's top hits were this unit's own review item and TOOL-dTieredTribunal-5,
whose backlog entry found no safe static predicate for a neighbouring counter family and named a
gotcha record as the left-shift, which is the shape S6 takes.

Recall terms used: `python tools/memory-recall/query.py "a counter returned by one function and read back by typed names through a defaulting Counter reads a misspelled name as zero" --terms "Counter read-back counters spelled twice silent zero scan_live_spec totals SPEC_COUNTERS defaulting container key set"`
