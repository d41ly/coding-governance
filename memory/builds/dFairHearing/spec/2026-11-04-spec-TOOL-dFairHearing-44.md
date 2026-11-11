# TOOL-dFairHearing-44 — the closing diff review's second batch unit: two docstrings say who calls the ungated reader

**Status:** CLOSED · rev-1 · 2026-11-04 · node d · Tier-1 · base f4120c83 · streams tooling · order 29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-03-build-TOOL-dFairHearing-1-agent-ledger.md](../build/2026-11-03-build-TOOL-dFairHearing-1-agent-ledger.md) | journal | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 TOOL-dFairHearing-20 TOOL-dFairHearing-21 TOOL-dFairHearing-22 TOOL-dFairHearing-23 TOOL-dFairHearing-25 TOOL-dFairHearing-26 TOOL-dFairHearing-27 TOOL-dFairHearing-28 TOOL-dFairHearing-29 TOOL-dFairHearing-30 TOOL-dFairHearing-31 TOOL-dFairHearing-32 TOOL-dFairHearing-33 TOOL-dFairHearing-34 TOOL-dFairHearing-35 TOOL-dFairHearing-36 TOOL-dFairHearing-37 TOOL-dFairHearing-38 TOOL-dFairHearing-39 TOOL-dFairHearing-40 TOOL-dFairHearing-43 TOOL-dFairHearing-45 TOOL-dFairHearing-46 TOOL-dFairHearing-47 TOOL-dFairHearing-48 TOOL-dFairHearing-50 |
| [2026-11-04-build-TOOL-dFairHearing-44-1-acceptance-ledger.md](../build/2026-11-04-build-TOOL-dFairHearing-44-1-acceptance-ledger.md) | journal | — |
| [2026-11-04-build-TOOL-dFairHearing-44-1-builder-return.md](../build/2026-11-04-build-TOOL-dFairHearing-44-1-builder-return.md) | journal | — |
| [2026-11-04-build-TOOL-dFairHearing-44-deviation-441.md](../build/2026-11-04-build-TOOL-dFairHearing-44-deviation-441.md) | deviation | — |
| [2026-11-08-build-TOOL-dFairHearing-1-runlog-70b3ac3f.md](../build/2026-11-08-build-TOOL-dFairHearing-1-runlog-70b3ac3f.md) | journal | TOOL-dFairHearing-1 TOOL-dFairHearing-2 TOOL-dFairHearing-3 TOOL-dFairHearing-4 TOOL-dFairHearing-5 TOOL-dFairHearing-6 TOOL-dFairHearing-7 TOOL-dFairHearing-8 TOOL-dFairHearing-9 TOOL-dFairHearing-10 TOOL-dFairHearing-11 TOOL-dFairHearing-12 TOOL-dFairHearing-13 TOOL-dFairHearing-14 TOOL-dFairHearing-15 TOOL-dFairHearing-16 TOOL-dFairHearing-17 TOOL-dFairHearing-18 TOOL-dFairHearing-20 TOOL-dFairHearing-21 TOOL-dFairHearing-22 TOOL-dFairHearing-23 TOOL-dFairHearing-25 TOOL-dFairHearing-26 TOOL-dFairHearing-27 TOOL-dFairHearing-28 TOOL-dFairHearing-29 TOOL-dFairHearing-30 TOOL-dFairHearing-31 TOOL-dFairHearing-32 TOOL-dFairHearing-33 TOOL-dFairHearing-34 TOOL-dFairHearing-35 TOOL-dFairHearing-36 TOOL-dFairHearing-37 TOOL-dFairHearing-38 TOOL-dFairHearing-39 TOOL-dFairHearing-40 TOOL-dFairHearing-43 TOOL-dFairHearing-45 TOOL-dFairHearing-46 TOOL-dFairHearing-47 TOOL-dFairHearing-48 TOOL-dFairHearing-50 |
| [2026-11-04-prompt-TOOL-dFairHearing-44-1-spec-writer.md](../prompts/2026-11-04-prompt-TOOL-dFairHearing-44-1-spec-writer.md) | journal | — |
| [2026-11-04-prompt-TOOL-dFairHearing-44-build-brief.md](../prompts/2026-11-04-prompt-TOOL-dFairHearing-44-build-brief.md) | research | — |
| [2026-11-04-prompt-TOOL-dFairHearing-44-spec-brief.md](../prompts/2026-11-04-prompt-TOOL-dFairHearing-44-spec-brief.md) | research | — |
| [2026-11-05-review-TOOL-dFairHearing-43-47-diff-review.md](../reviews/2026-11-05-review-TOOL-dFairHearing-43-47-diff-review.md) | diff-review | TOOL-dFairHearing-43 TOOL-dFairHearing-45 TOOL-dFairHearing-46 TOOL-dFairHearing-47 |

<!-- /gen:spec-records -->

## 1. Goal

Two docstrings in `tools/memory-tree/gotchas.py` stop implying that a live path calls `check_ungated`,
and state who does. This closes LOW id 5 of the closing diff review,
`memory/builds/dFairHearing/reviews/2026-11-04-review-TOOL-dFairHearing-1-40-diff-review.md`. It is the
review's second batch unit, because the dispatch verb refused `gotchas.py` beside its generated index
in unit 43's write set. It carries unit 43 rev-2's S8 and AC8.

## 2. Scope (IN)

- **S1** — id 5 (LOW). The `check_ungated` docstring (`tools/memory-tree/gotchas.py:434-440`) names its
  callers: this file's selftest arms (:979-1017) and unit 30's committed instrument,
  `memory/builds/dFairHearing/build/2026-11-04-build-TOOL-dFairHearing-30-ungated.py`, whose line 34
  calls it. It says no `--all-ungated` flag exists and that the unit adding one wires the function in.
  The `check_gate_token` docstring (:401-407) says no live path calls `check_ungated`, and its sentence
  "counts it ungated and announces it as a note" (:405-406) is reworded. The Design section holds the
  text. Nothing else in the file changes. Observed by AC1.

## 3. Non-goals (OUT)

- `check_ungated` stays. The finding's other option, taking it out until the flag's unit, would break
  the instrument, which imports this module (its line 10) and which unit 40's AC17 runs.
- No `--all-ungated` flag and no new caller. The flag's open ask is `TOOL-dLinkedLibrary-35`
  (`memory/builds/dLinkedLibrary/BACKLOG.md:14`).
- Not the class record `helper-whose-only-caller-is-its-selftest` and not `memory/gotchas/INDEX.md`.
  Both stay with unit 43, which keeps the finding's catalogue entry and runs the regeneration.
- No docstring beyond these two. `extract_gated_scope` and the `GATED_*` patterns say nothing about a
  caller, and only `check_ungated` and the selftest reach them (`git grep` over `tools/` and `skills/`).
- No help page: `git grep ungated -- help` finds nothing, and a docstring is not a user surface.

## 4. Design

### The text

The sentence in `check_gate_token`, lines 405-406, becomes:

```text
    `check_invariant` keeps its note on the None state. `check_ungated` reads that state as not gated
    and notes it on stderr (TOOL-dFairHearing-27 S9), so both read a class's gate through this one
    rule, and no live path calls `check_ungated`; its docstring names its callers.
```

`check_ungated` gains a closing paragraph after line 439:

```text
    No live path calls this. Its callers are this file's selftest arms and the replay instrument
    `2026-11-04-build-TOOL-dFairHearing-30-ungated.py`, a committed build record. `gotchas.py` has no
    `--all-ungated` flag, and the unit that adds one wires this in (TOOL-dFairHearing-23 S21).
```

The callers live in one docstring, and `check_gate_token` points there. The review asked for both
docstrings to carry the fact, and the pointer does that without two caller lists.

Three limits bind the wording. It spells the instrument by its file name, because `gotchas.py` ships to
adopters at other prefixes. It cites no id but closed units 23, 27 and 30, because the drift audit's
oracle reports a non-terminal spec whose id product source cites
(`tools/drift-audit/drift_report.py:729-743`), so this unit's own id stays out. And the flag's name sits
only in the docstring: unit 38's S3 slice reads `main`'s `--for-diff` branch and states that a docstring
sits outside it. Unit 25 AC6's `grep -c` count would now print 1, but unit 32 S13 and unit 37 S4 record
that a docstring stating this contract reds that count, and both moved the observation to behaviour.

### Re-grounding AC8

Unit 43 rev-2's AC8 cannot be carried as written. Its third grep,
`grep -c "counts it ungated and announces it as a note"`, prints 0 on today's tree because the phrase
wraps across lines 405 and 406, so that clause could never go red. Its other two greps count the whole
file, so one docstring alone would pass both. The probe below reads each docstring with its whitespace
folded. The `--selftest` clause moves to the leg line in the Gates section, and the probe's byte
comparison of everything outside the two docstrings replaces it with a stronger observation.

### The probe

Save this block to `$TEMP/fh44probe` and run it from the repository root.

```python
import ast, subprocess, sys

PATH = "tools/memory-tree/gotchas.py"
STEM = "2026-11-04-build-TOOL-dFairHearing-30-ungated.py"
NAMES = ("check_gate_token", "check_ungated")


def funcs(src):
    return {f.name: f for f in ast.parse(src).body if isinstance(f, ast.FunctionDef) and f.name in NAMES}


def rest(src):  # the file with the two docstrings cut out, line for line
    lines = src.split("\n")
    for f in sorted(funcs(src).values(), key=lambda f: -f.lineno):
        del lines[f.body[0].lineno - 1:f.body[0].end_lineno]
    return lines


new = open(sys.argv[1] if len(sys.argv) > 1 else PATH, encoding="utf-8").read()
old = subprocess.run(["git", "show", "f4120c83:" + PATH], capture_output=True, encoding="utf-8", check=True).stdout
gate, ungated = (" ".join(ast.get_docstring(funcs(new)[n]).split()) for n in NAMES)
instrument = open("memory/builds/dFairHearing/build/" + STEM, encoding="utf-8").read()
bad = [name for name, ok in (
    ("phrase", "counts it ungated" not in gate),
    ("gate-token", "no live path calls `check_ungated`" in gate),
    ("no-live-path", "No live path calls this" in ungated),
    ("selftest", "selftest arms" in ungated),
    ("stem", STEM in ungated),
    ("flag", "`--all-ungated`" in ungated),
    ("instrument", "g.check_ungated(" in instrument),
    ("rest", rest(new) == rest(old)),
) if not ok]
print("fh44: " + (" ".join(bad) if bad else "ok"))
sys.exit(1 if bad else 0)
```

Measured at `f4120c83` over scratch copies. Today's file prints the six names AC1 quotes. A copy
carrying the text above prints `fh44: ok`. That copy with a changed pattern, or with one changed
comment, prints `fh44: rest`.

### Why the map does not move

`memory/map/generated/symbols.json` holds one `id`, `kind` and `file` per public module-level symbol
(`tools/codebase-map/map_lib.py:325-328`), and its renderer refuses any other key (:1610). It stores no
line number and no docstring. This unit adds, renames and moves no definition, so no row changes, and
the two functions' rows already stand. Commit `6d768c563` added nine lines to this file and moved no
file under `memory/map/`. The codebase-map leg in `.githooks/pre-commit` still runs, because a `.py` is
staged, and it has nothing to regenerate.

### Why the index is not declared

`memory/gotchas/INDEX.md` renders from the class records, and `gotchas.py` reads no `__doc__`, so a
docstring edit leaves the render unchanged. The dispatch verb refuses a declaration that pairs that
index with its generator (`tools/unattended/unattended.sh:14606-14617`, generator row at
`tools/memory-tree/kit.toml:504-507`), and this one names only the generator.

### Rollout

Unit 43 and this unit share order 29, but the two passes cannot be open together. The same refusal
reads every open sibling's paths as well as this declaration's (`tools/unattended/unattended.sh:14568`,
:14606), and unit 43 declares the index, so whichever pass declares second is refused. The build
method's parallel rule does not apply, because it excludes a generated index with its generator.
Dispatch one, commit it, then dispatch the other. Unit 46 shares the order and declares neither path.

### The header's ask clause

The header carries neither `closes` nor `advances`, for the reason unit 43's Design section gives under
this same heading. Ask `TOOL-dFairHearing-19` derives CLOSED from unit 40's CLOSED header
(`tools/memory-tree/backlog.py:836-842` and :933-940), and this is the build run, so neither verb
moves that derivation.

### Files touched (estimate)

- `tools/memory-tree/gotchas.py`
- `memory/builds/dFairHearing/build/2026-11-04-build-TOOL-dFairHearing-44-1-acceptance-ledger.md`
- `memory/builds/dFairHearing/spec/2026-11-04-spec-TOOL-dFairHearing-44.md`
- `memory/builds/dFairHearing/README.md`
- `memory/LIVE.md`
- `memory/backlog/TOOL.md`

The last three are the renders the status flip forces at the hygiene hook, as units 38 and 40 declared
them in their `RUN.md` dispatch rows. No `memory/map/` path and no kit version moves: commit
`6d768c563` edited this kit file with neither.

### Alternatives rejected

- **Take `check_ungated` out until the flag's unit.** It breaks unit 30's instrument and unit 40's AC17.
- **Give `check_gate_token` its own caller list.** That is the same fact twice, and the copy drifts.
- **Spell the instrument's full path.** Its directory exists only in this repository, and the file name
  is enough to find it.

## 5. Acceptance criteria

- **AC1** — When `python $TEMP/fh44probe` runs from the repository root over the built
  `tools/memory-tree/gotchas.py`, it prints `fh44: ok` and exits 0. When
  `python $TEMP/fh44probe $TEMP/fh44copy` runs over a copy of the built file whose `GATED_LINE_RE` line
  drops `|at`, it prints `fh44: rest` and exits 1.
  Red when: a docstring reads as if a live path calls `check_ungated`, or omits its callers, as today's
  file does in printing `fh44: phrase gate-token no-live-path selftest stem flag`; or the build changes
  anything outside the two docstrings.
  fixture: the probe is the Design section's fenced block, saved to `$TEMP/fh44probe`, and `$TEMP/fh44copy`
  is made by the pass; both are removed after it. The comparison reads the blob at `f4120c83`, and no
  unit ordered before this one writes the file.

## 6. Gates

`gotchas selftest` · `policy fixtures` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `drift-audit records` · `install-prefix (shipped surface)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

No new arm: the docstrings change no behaviour, and the probe shows the code is byte-identical.
`drift-audit records` and `install-prefix (shipped surface)` carry reds today that the `RUN.md` rescope
rows for units 45 and 46 own. This unit adds no offender to either.

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-04 · S1 · AC1 · initial draft, carrying unit 43 rev-2's S8 and AC8 as the review's
  second batch unit.

## 9. Reuse audit

The seam is the two docstrings themselves, `tools/memory-tree/gotchas.py:400` and :433, so no code seam
is extended. `python tools/codebase-map/reuse_lookup.py "state in a docstring who calls a helper with no
live caller"` ranked generic name stems only, so no existing seam fits and none is needed. The recall
query returned the finding, unit 43's S8, unit 23's S21 and ask `TOOL-dLinkedLibrary-35`, which is the
flag's open ask. `gen_build_index.py --asks --path tools/memory-tree/gotchas.py` named no ask on these
docstrings.

Recall terms used: `python tools/memory-recall/query.py "a helper whose only live caller is a committed build instrument and its selftest" --terms "check_ungated all-ungated check_gate_token docstring selftest caller instrument ungated gotchas replay"`
