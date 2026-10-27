# TOOL-dLinkedLibrary-97 — the census's decode walk counts every standard-library decode spelling, each planted red

**Status:** DEFERRED · rev-1 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 38 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |
| [2026-10-27-build-TOOL-dLinkedLibrary-97-deviation-971.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-97-deviation-971.md) | deviation | — |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 92 to 96
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-92-spec-audit.md`) confirmed
finding **id 9 at HIGH**, report item **H1**. Id 28 binds the same gap at MEDIUM, item M10, and is batched
in `TOOL-dLinkedLibrary-102`.

`TOOL-dLinkedLibrary-96` S6 promises a walk that finds "a decode in any spelling" outside `ci_lines`,
then lists seven spellings and stops. `universal_newlines=True`, an `errors=` keyword given alone to a
subprocess call and `os.popen` each decode, and each folds a lone CR and a CR LF to LF before `ci_lines`
sees the text. A reader spelled that way passes the walk, and unit 93's `unreadable line break U+000D`
refusal never fires on its lines. The walk certifies a decode path it never checked.

This unit defines the walk's decode class by behaviour, as a table of every standard-library entry
point that turns bytes into text, and gives the walk one planted reader per spelling in that table, so
a spelling the walk misses is red in the fixture itself. It repairs `TOOL-dLinkedLibrary-96` and builds
one step after it (order 38).

## 2. Scope (IN)

- **S1** — The class. In `tools/memory-tree/adopt_program.py`, 96 S6's walk counts as a decode every
  call whose target is a spelling in §4 "The decode table", and "any spelling" in 96 S6 reads as "every
  spelling in that table". The walk resolves a call's target through `adopt_program.py`'s own import
  statements, so `from subprocess import run as r` then `r(..., errors="strict")` is the subprocess row.
  Observed by AC1 and AC2.
- **S2** — The keyword rows. A subprocess call holding any of the keywords `text`, `universal_newlines`,
  `encoding` or `errors` with a value other than the constants `False` or `None` is a decode, the keyword
  alone deciding it; an open call holding `encoding`, `errors` or `newline` is a decode, since Python
  refuses those keywords in binary mode. Observed by AC1 and AC2.
- **S3** — The mode rows. An open call whose mode argument, positional or `mode=`, is a constant without
  `b`, or is not a constant, is a decode; with no mode argument it is a decode for `open`, `io.open`,
  `os.fdopen` and any `.open` attribute call, and not for the `tempfile` factories, whose default mode is
  binary. A mode the walk cannot read is counted: deny by default. Observed by AC1.
- **S4** — One plant per spelling. The structural check 96 AC6 runs holds, for each spelling of the
  table, a planted reader: a source text defining a function named as 96 S5's Azure reader whose body takes
  its text by that spelling and nothing else. The check walks each planted reader beside the real
  `ci_lines` and prints `structural: decode named <row> <spelling> <reader>` for each, and exits non-zero
  naming any planted reader it did not name. The planted readers are string constants, never `def`s of
  the module, so the walk over the real module never meets them. Observed by AC1 and AC3.
- **S5** — The record. 96's acceptance ledger carries an amendment line citing this unit, restating 96
  S6's class as the table and naming the count of planted spellings. Observed by AC4.

## 3. Non-goals (OUT)

- A decode inside another module the walked readers call, `tree_lib.read_blobs_at` without `raw` among
  them: report id 27, `TOOL-dLinkedLibrary-100`.
- The end-to-end subprocess twins through a scratch copy of the real module, an `errors=` reader among
  them: id 28, `TOOL-dLinkedLibrary-102`.
- A bug-class checklist entry that a walk claiming "any spelling" plants one red per spelling: the
  report's left-shift, a separate record this unit does not write.
- Reusing `scan_text_io` in `tools/gate-lint/encoding_posture.py`: §10 says why.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-96` — S6's walk over S5's readers and AC6's structural check, which S1 to S4 give a closed decode table and one planted red per spelling (id 9)
- **hands-off** `TOOL-dLinkedLibrary-102` — S2's subprocess keyword row, which unit 102 observes end to end through a scratch copy of the real module whose Azure reader decodes by an `errors=` keyword alone and by `universal_newlines=True` (id 28)

## 4. Design

### The decode table

Each row is a class of call; each spelling is one planted reader of S4. The count of spellings is
DERIVED from this table at the build pass and is the count AC1 compares.

| Row | Spellings |
|---|---|
| `decode-method` | `<x>.decode(...)`, any receiver |
| `str-encoding` | `str(<b>, <enc>)`, `str(<b>, encoding=...)`, `str(<b>, errors=...)` |
| `codecs` | `codecs.decode`, `codecs.open`, `codecs.iterdecode`, `codecs.getreader`, `codecs.getdecoder`, `codecs.getincrementaldecoder` |
| `open-text` | `open(<p>)`, `open(<p>, "r")`, `open(<p>, mode=<m>)` with `<m>` a name, `open(<p>, encoding="utf-8")`, `io.open(<p>)`, `os.fdopen(<fd>)`, `<path>.open()` |
| `read-text` | `<x>.read_text(...)`, any receiver |
| `subprocess-text` | each of `run`, `Popen`, `call`, `check_call`, `check_output` with `text=True`; `check_output` with `universal_newlines=True`, with `encoding="utf-8"` and with `errors="strict"` alone |
| `subprocess-always` | `subprocess.getoutput`, `subprocess.getstatusoutput` |
| `os-popen` | `os.popen` |
| `text-wrapper` | `io.TextIOWrapper` |
| `tempfile-text` | `tempfile.TemporaryFile(mode="w+")`, `tempfile.NamedTemporaryFile(mode="r")`, `tempfile.SpooledTemporaryFile(mode="w+")` |
| `parser-bytes` | `json.loads(<b>)`, `json.load(<fh>)`, `tomllib.load(<fh>)` |

### Evidence

- 96 S6 (`2026-10-27-spec-TOOL-dLinkedLibrary-96.md`, S6) lists `.decode(`, `encoding=`, `text=True`,
  `read_text`, text-mode `open`, `str` with an encoding and `codecs.decode`; 96 AC6 stages only the
  `text=True` spelling.
- Python's `subprocess` documentation opens its file objects in text mode when `encoding` or `errors` is
  given or `text` (alias `universal_newlines`) is true, decoding with universal newlines.
- `tools/gate-lint/encoding_posture.py:59-61` declares `SUBPROCESS_FNS` and
  `TEXT_MODE_FLAGS = ("text", "universal_newlines")`: the house already names both flags as one mode.
- `tools/memory-tree/adopt_program.py` is absent at base; the walk is built at 90's pass by 96 S6.

### Inventory

S4 mints one module constant in `adopt_program.py`, `DECODE_SPELLINGS`, a tuple of `(row, spelling,
planted source)` triples. A function the pass adds is named after `python3 tools/lexicon/lexicon.py
--suggest <name>`, the lexicon's cell for a function name.

### Rollout

Order 38, one step after `TOOL-dLinkedLibrary-96`, beside `TOOL-dLinkedLibrary-98`, `-100` and `-101`.
This unit and 100 both write the walk in `adopt_program.py`, so BUILD-METHOD M6's clause 1 sequences
those two passes. If the pass adds a function, it re-renders the generated map with `python
tools/codebase-map/gen_map.py --write` where its `--check` exits 1, then runs `python
tools/lexicon/lexicon.py`, in the pass commit.

### Files touched (estimate)

- `tools/memory-tree/adopt_program.py`: S1 to S4
- `memory/builds/dLinkedLibrary/build/`: S5's amendment line
- `memory/map/generated/inventories.json`, `memory/map/generated/MAP.md`,
  `memory/map/generated/CARDS.md`, `memory/map/generated/symbols.json`: the Rollout re-render

### Alternatives rejected

- **Adding the three missing spellings to 96 S6's list.** It repeats the defect: a closed list claiming
  "any", with one staged red for seven spellings.
- **Scratch copies of the module, one per spelling, typed into a criterion.** Each runs once by hand;
  S4's planted readers run on every fixture run.
- **Counting every call in a walked reader that the walk cannot type.** Every string method would
  count, and a correct build would read red.

## 5. Production-readiness checklist

- security — closes a reader decoding outside `ci_lines` by a spelling the walk did not list, which
  hides a lone CR from unit 93's refusal; deny by default on an unreadable mode.
- perf / scale — one `ast` parse per planted reader, a few dozen small sources per fixture run.
- error / empty / loading states — a planted reader the walk misses exits non-zero naming it.
- observability — one `structural: decode named` line per spelling.
- risks — a standard-library decode outside the table is not seen; the table is the class's closed
  list, every row planted, and a new spelling is a row added with its plant.
- testing — AC1 to AC4 by the fixture, a scratch copy and a ledger grep.
- migration — none: the walk runs at fixture time.
- user docs — none under `help/`: the fixture is a developer surface.

## 6. Acceptance criteria

- **AC1** — When `python adopt_program.py --fixture --plant ci-census` runs its structural check, it
  prints one `structural: decode named` line per spelling of §4's table, their count equal to the
  length of `DECODE_SPELLINGS`, and prints no decode outside `ci_lines` over the real module.
  Red when: a spelling's planted reader passes the walk, or the real module's readers decode elsewhere.
  figure: DERIVED from the table at the build pass.
- **AC2** — When a scratch copy of `adopt_program.py` whose Azure reader takes its text from
  `subprocess.run` over `git show` with `universal_newlines=True` runs the same check by `python -I`, it
  names that reader.
  Red when: the walk passes a reader decoding by `universal_newlines`.
- **AC3** — When a scratch copy whose walk omits `universal_newlines` from the subprocess row runs the
  check by `python -I`, it exits non-zero naming the `subprocess-text` plant spelled with
  `universal_newlines=True`.
  Red when: the check exits 0, so the plants do not guard the table.
- **AC4** — When `grep 'TOOL-dLinkedLibrary-97'` runs over 96's acceptance ledger, it prints the line
  restating 96 S6's class as the decode table.
  Red when: 96's ledger still certifies the seven-spelling walk.

## 7. Gates

`codebase-map coverage + freshness` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/adopt_program.py · covers AC1 · the structural check's one planted reader per decode-table spelling, the failing case staged by a walk missing the `universal_newlines` keyword · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 8 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 92 to 96, id 9 (HIGH, item
  H1).

## 10. Reuse audit

The seam extended is 96 S6's walk in `tools/memory-tree/adopt_program.py`, which 90 AC4's `ast` probe
began. `tools/gate-lint/encoding_posture.py`'s `scan_text_io` (`:94-127`) walks the same call shapes but
reports only text IO with no `encoding=`, the opposite predicate, and the memory-tree kit declares no
requirement on gate-lint (`tools/memory-tree/kit.toml`, `requires = []`), so importing it would add a
kit edge; its two flag names are copied into the table instead. `python
tools/codebase-map/reuse_lookup.py "find every call that decodes bytes into text in a python module"`
ranked `read_text`, `write_text`, `resolve_python` and `load_text`, none a call classifier, so no
existing seam fits beyond the walk being extended.

Recall terms used: `python tools/memory-recall/query.py "how does the census walk prove no decode outside ci_lines" --terms "census ci_lines decode walk ast spelling universal_newlines subprocess text-mode codecs structural check"`
