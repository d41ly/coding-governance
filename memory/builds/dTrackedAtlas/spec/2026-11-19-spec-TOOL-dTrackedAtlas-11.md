# TOOL-dTrackedAtlas-11 — the closing review's minors: one reader for valued options, the stale ledger line cleared, the owed pane looks recorded

**Status:** CLOSED · rev-1 · 2026-11-19 · node d · Tier-1 · base 9e21ac76 · streams tooling · records-only · order 8

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-19-build-TOOL-dTrackedAtlas-11-ledger.md](../build/2026-11-19-build-TOOL-dTrackedAtlas-11-ledger.md) | journal | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-11-build-brief.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-11-build-brief.md) | research | — |
| [2026-11-19-prompt-TOOL-dTrackedAtlas-8-spec-brief.md](../prompts/2026-11-19-prompt-TOOL-dTrackedAtlas-8-spec-brief.md) | research | TOOL-dTrackedAtlas-8 TOOL-dTrackedAtlas-9 TOOL-dTrackedAtlas-10 |
| [2026-11-19-review-TOOL-dTrackedAtlas-8-9-10-11-diff-review-round2.md](../reviews/2026-11-19-review-TOOL-dTrackedAtlas-8-9-10-11-diff-review-round2.md) | diff-review | TOOL-dTrackedAtlas-1 TOOL-dTrackedAtlas-2 TOOL-dTrackedAtlas-3 TOOL-dTrackedAtlas-4 TOOL-dTrackedAtlas-8 TOOL-dTrackedAtlas-9 TOOL-dTrackedAtlas-10 |

<!-- /gen:spec-records -->

## 1. Goal

The closing review's minors M1, L1 and L2 close together. The Atlas generator's `main` reads every
option that takes a value through one reader, so an option given no value is one `atlas:` refusal
line and never a traceback. Ledger 1 stops owing a lexicon pin raise for a name that no longer
exists. And the two browser-pane observations units 2 and 3 owed to the close are made and recorded
by the main loop at the close, not by this unit's builder.

## 2. Scope (IN)

- **S1** — L1: `read_options(argv)` in the generator reads the value of every option named in a new
  constant `VALUED_OPTIONS`, and is the one place in the generator that indexes `argv`. `main`
  calls it once, before it derives anything, in both its `--page` branch and its derive branch.
  Observed by AC1, AC2, AC3 and AC4.
- **S2** — L1: an option that is the last argument, or whose next argument starts with `-`, is
  refused with the reason `<option> takes a value`. The derive branch exits 1 with the stderr line
  `atlas: <option> takes a value`. The `--page` branch exits 2 with nothing on stdout and the one
  stderr line `atlas: cannot check: <option> takes a value`, as the exit table of
  `TOOL-dTrackedAtlas-3` §4 "The page check" requires of a misuse. Observed by AC2 and AC3.
- **S3** — L2: ledger 1's "Owed to the close" line no longer owes the lexicon's
  `VERB_OFFENDER_PIN` a raise for `predecessors`, and a line beneath it says that spec 1 rev-3's
  rename to `derive_predecessors` cleared the item. Observed by AC5.
- **S4** — M1: the browser-pane observations of `TOOL-dTrackedAtlas-2`'s AC12 and
  `TOOL-dTrackedAtlas-3`'s AC8, each with its red, are made by the main loop at the close and
  recorded in ledgers 2 and 3 by §4 "The pane observations at the close". NOT OBSERVED by this
  unit's criteria: the builder's pass cannot open the browser pane, and a criterion it could not
  observe would close this unit with an acceptance check owed, the defect M1 names. The builder
  writes no pane observation and claims none.

## 3. Non-goals (OUT)

- The functions this unit touches are the generator's `main`, and it adds the constant
  `VALUED_OPTIONS` and the function `read_options` (§4 "Inventory"). `check_page`, `build_stamp`,
  `read_stamp`, `derive`, `derive_actual`, the module docstring and the template stay as
  `TOOL-dTrackedAtlas-9` and `TOOL-dTrackedAtlas-10` leave them. `check_page` keeps its own refusal
  of a `ref` starting with `-`, the boundary of a function `main` is not the only possible caller of.
- The `--option=value` spelling, a refusal of an unknown option, and a refusal of a repeated
  option. Today an unknown argument is ignored and a repeated option reads its first value, and both
  stay so.
- The meaning of any value: `--claims` keeps its `cache` or `none` refusal in `main`, and
  `--plant` its case check in `derive`.
- Any browser-pane observation, any edit to ledger 2 or ledger 3, and any claim that S4 is done:
  those are the main loop's at the close.
- The left-shift gates the review names: a self-test arm for valued options, a hygiene check for a
  CLOSED spec with an owed line, and a token check over ledger "Owed" lines. This repository's
  `review.left-shift` is `second-occurrence`, so a first occurrence owes no gotcha file and no gate.
- Any file under `tools/`, any new file under `memory/builds/dClosedLoop/build/`, and the specs of
  units 1 to 3, which are CLOSED and stay frozen.

### Edges

- **consumes-from** `TOOL-dTrackedAtlas-9` — any option taking a value that it adds to the
  generator's `main`, such as the default-branch ref; this unit's reader then reads it, and
  `VALUED_OPTIONS` names it.
- **consumes-from** `TOOL-dTrackedAtlas-10` — the generator as it leaves `build_stamp` and
  `check_page`; this unit builds after it and edits neither.
- **consumes-from** `TOOL-dTrackedAtlas-3` — the page check's exit table, which fixes the frame of
  a refusal in the `--page` branch.

## 4. Design

### Where it lands

The generator is `memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py`.
At `2b57a776e`, `main` indexes `argv` for a value at six sites
(`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py@2b57a776e68945c686ea9538150f6eaa198b8649:931`,
and lines 938, 939, 940, 945 and 954 of the same blob). Only the `--page` branch bounds the index,
for `--page` and `--ref`
(`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py@2b57a776e68945c686ea9538150f6eaa198b8649:932`).
The derive branch reads `--ref`, `--claims`, `--plant` and `--out` with no bound, so
`--check --ref` raises `IndexError` (observed on 2026-11-19 at `2b57a776e`), and `--out` as the last
argument raises it only after a whole derivation. These are two answers to one question, the class
`two-answers-to-one-question` the review names.

### The reader

```python
VALUED_OPTIONS = ("--page", "--ref", "--claims", "--plant", "--out")

def read_options(argv):
    """({option: value} for each option of VALUED_OPTIONS present in argv, None), or
    (None, "<option> takes a value") for the first option of VALUED_OPTIONS, in that tuple's order,
    that is the last argument or whose next argument starts with "-"."""
```

`VALUED_OPTIONS` names every option `main` reads a value for when this unit builds. That is the five
above, plus any `TOOL-dTrackedAtlas-9` or `TOOL-dTrackedAtlas-10` add before it, appended at the
tuple's end. An option present more than once reads its first occurrence, as
`argv.index` does today. The pair return follows `read_stamp`'s `(stamp, None)` or `(None, reason)`
shape (`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py#read_stamp`),
so neither branch catches an exception.

### `main` after the change

1. `values, reason = read_options(argv)`, as `main`'s first statement.
2. When `--page` is in `argv`: a `reason` prints `atlas: cannot check: <reason>` on stderr and
   returns 2. Otherwise the existing refusal of a missing `--check` or a mixed option, with its
   existing text, returns 2. Otherwise it returns
   `check_page(values["--page"], values.get("--ref", "HEAD"))`.
3. Otherwise a `reason` exits with `atlas: <reason>`, exit 1, the derive branch's existing refusal
   convention. `ref`, `claims`, `plant` and the `--out` path come from `values` with today's
   defaults: `HEAD`, `cache`, none and none.
4. The derive branch's `ref.startswith("-")` refusal is deleted, since the reader refuses every such
   value first; so are the `--page` branch's `has_ref`, empty-page and dash-page tests.

The rest of `main` keeps its order and its text: the `--claims` value check, `derive_actual`, the
`--check` summary, the usage exit when `--out` is absent, the stamp and the splice.

### Ledger 1's owed line

At `memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-ledger.md@2b57a776e68945c686ea9538150f6eaa198b8649:54`
the "Owed to the close" line opens, and on line 56 it ends with the item that the lexicon's
`VERB_OFFENDER_PIN` gains `predecessors`. Spec 1 rev-3 renamed that function, and
`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py#derive_predecessors`
is the name today, which leads with the declared verb `derive`. The edit removes that item from the
owed line, keeping the plain bar and the `chain-packet self-test` item as they are. It adds one line
directly beneath, opening `Cleared since:`, which says that spec 1 rev-3's rename to
`derive_predecessors` at `f24d90e25` cleared the `VERB_OFFENDER_PIN` item and that the lexicon owes
nothing for this unit.

### The pane observations at the close

The main loop makes these after the last unit is terminal and before the bar, with the generator
at the close's tip. It serves each page with `python -m http.server` from a temporary launch
configuration that it deletes afterwards, and opens it in the browser pane.

| Ledger | Criterion | Green, as the criterion states it | Red |
|---|---|---|---|
| `2026-11-19-build-TOOL-dTrackedAtlas-2-ledger.md` | `TOOL-dTrackedAtlas-2` AC12, on that spec's AC1 page | the Chain view's rows, landed merges and `can start` builds, and the Build area's "Since the baseline" panel naming dTrueNorth and `2511c1181` | the page of the generator at `9e21ac760` |
| `2026-11-19-build-TOOL-dTrackedAtlas-3-ledger.md` | `TOOL-dTrackedAtlas-3` AC8, on that spec's `p0.html` | `generated from` and the first 12 hex of the page's commit in the header line | the page of the generator at `f1b02b3eb` |

Each ledger gains one line directly beneath its "Owed to the close" line, in the precedent's form
`Owed to the close, and since observed by the main loop in the browser pane: ...`
(`memory/builds/aClearedLedger/build/2026-11-13-build-TOOL-aClearedLedger-3-1-acceptance-ledger.md@2b57a776e68945c686ea9538150f6eaa198b8649:7`),
naming what the pane showed for green and for red. The line is added under a `Pass: none` commit.
If the pane disagrees with a criterion, the main loop records that instead and the unit's
disposition follows the unattended protocol, never a line claiming the observation.

### Inventory

| Name | Kind | Value or signature |
|---|---|---|
| `VALUED_OPTIONS` | constant | the tuple of every option `main` reads a value for |
| `read_options(argv)` | function | `(values, None)` or `(None, reason)`, by §4 "The reader" |

### Files touched (estimate)

`memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py`
`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-ledger.md`
`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-11-ledger.md`

### Alternatives rejected

- `argparse`, which `TOOL-dTrackedAtlas-1`'s module uses
  (`memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py#main`).
  Tested on 2026-11-19 with a parser given `--ref` and no value: it printed a `usage:` line and an
  `error:` line and exited 2. That fails `TOOL-dTrackedAtlas-3` AC7's one stderr line in the
  `--page` branch and the derive branch's exit 1, so the reader is hand-written instead.
- The finder's instance fix, copying the `--page` branch's bound check to `--ref`, `--claims` and
  `--plant`: it leaves two rules and misses `--out`, which the skeptic judged INSTANCE-ONLY.
- Deleting ledger 1's owed item with no line saying why: a reader of the ledger would then see an
  item vanish with no record of what cleared it.

## 5. Acceptance criteria

The commands run from a worktree root with these names set. Nothing here writes a file, a ref or
the working tree.

```bash
. tools/lib/resolve-python.sh && PY=$(resolve_python)
ATLAS=memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.py
TPL=memory/builds/dClosedLoop/build/2026-10-16-build-PLAY-dClosedLoop-1-atlas.html
L1=memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-ledger.md
VALUED=$("$PY" -c 'import importlib.util as u, sys; s = u.spec_from_file_location("a", sys.argv[1]); m = u.module_from_spec(s); s.loader.exec_module(m); print(*m.VALUED_OPTIONS)' "$ATLAS")
```

The probe `argv_readers.py`, kept in the run's scratch directory, prints the functions that index
`argv`:

```python
import ast, sys
tree = ast.parse(open(sys.argv[1], encoding="utf-8").read())
print(" ".join(sorted({f.name for f in ast.walk(tree) if isinstance(f, ast.FunctionDef)
    for n in ast.walk(f) if isinstance(n, ast.Subscript)
    and isinstance(n.value, ast.Name) and n.value.id == "argv"})))
```

- **AC1** — When `"$PY" argv_readers.py "$ATLAS"` runs, it prints exactly `read_options`, and
  `$VALUED` holds `--page`, `--ref`, `--claims`, `--plant` and `--out`.
  Red when: the generator before this unit, where the probe prints `main`.
- **AC2** — When `"$PY" "$ATLAS" --check "$o"` and `"$PY" "$ATLAS" "$o" --check` run for each `$o`
  of `$VALUED` other than `--page`, each exits 1 within seconds, prints nothing on stdout, and its
  stderr is the one line `atlas: $o takes a value`, with no `Traceback`.
  Red when: the generator before this unit, where `--check --ref` prints a `Traceback` ending in
  `IndexError: list index out of range`.
  figure: the option count is DERIVED from `VALUED_OPTIONS`; five at `2b57a776e`.
- **AC3** — When `"$PY" "$ATLAS" --check --page "$TPL" "$o"` runs for each `$o` of `$VALUED` other
  than `--page`, and `"$PY" "$ATLAS" --check --page` runs, each exits 2 with nothing on stdout and
  the one stderr line `atlas: cannot check: $o takes a value`, `--page` for the last.
  Red when: the `--page` branch keeps its own rule, whose line for a bare `--ref` reads
  `--page takes a page path and runs with --check and an optional --ref alone`.
- **AC4** — When `"$PY" "$ATLAS" --check --page "$TPL" --ref HEAD` runs, it exits 1 with
  `atlas: unstamped`, and `--check --page "$TPL" --plant view-unread` exits 2 with the existing
  mixed-option line ending `not --plant`; `--check --claims maybe` exits 1 with
  `atlas: --claims takes cache or none, not maybe`; and `--check --claims none` prints its one
  `atlas: derived —` line with exit 0.
  Red when: the reader returns the option's own position, so `--claims none` reads `--claims` and
  every valued option is refused.
  cost: the last command derives the whole page, minutes rather than seconds.
- **AC5** — When `grep -n "gains .predecessors." "$L1"` runs it prints nothing, and
  `grep -n "derive_predecessors" "$L1"` prints the one line clearing the item, while
  `grep -n "^def derive_predecessors" memory/builds/dTrackedAtlas/build/2026-11-19-build-TOOL-dTrackedAtlas-1-build-state.py`
  prints one line.
  Red when: the ledger at `2b57a776e`, where the first `grep` prints line 56.

## 6. Gates

The close runs the plain bar once. The legs below are those the files touched keep green, the last
two owed because `tools/gate-legs.json` guards `memory/builds/dClosedLoop/build/` with them. No
suite arm is added or moved, so no arm line is declared.

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `recall floor` · `recall floor arms` · `chain-packet self-test` · `policy fixtures`

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-19 · initial draft, from the closing review's M1, L1 and L2 and the spec brief
  2026-11-19-prompt-TOOL-dTrackedAtlas-8-spec-brief.

## 9. Reuse audit

The seam extended is the generator's own `main`: its `--page` branch already bounds the index of
`--page` and `--ref`, and this unit makes that rule the one reader of every valued option. It
takes `read_stamp`'s pair-return shape. `python tools/codebase-map/reuse_lookup.py "read the value of a command line option and refuse when it is missing"`
ranked name-stem helpers only, `read_text`, `read_git`, `read_policy_value` and the like, none an
argument reader. `argparse`, the reader of `TOOL-dTrackedAtlas-1`'s module, was tested and rejected
in §4 "Alternatives rejected". The recall probe returned the review's own L1, and
`TOOL-aFlaggedScaffold-2`'s note on `bench.py`'s `--json <value>` footgun, which it left uncovered.

Recall terms used: `python tools/memory-recall/query.py "how does a build-folder instrument read the value of a command line option and refuse a missing one" --terms "argv option value refusal IndexError traceback generator main atlas flag missing last argument"`
