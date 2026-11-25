# TOOL-aAnsweredPark-1 — an owner decision settles by its own answer record, and only an open decision or a live hold interrupts

**Status:** INPROGRESS · rev-1 · 2026-11-25 · node a · Tier-2 · base 3d6c1702 · streams tooling · order 1

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-25-prompt-TOOL-aAnsweredPark-1-brief.md](../prompts/2026-11-25-prompt-TOOL-aAnsweredPark-1-brief.md) | research | — |
| [2026-11-25-prompt-TOOL-aAnsweredPark-1-divergence.md](../prompts/2026-11-25-prompt-TOOL-aAnsweredPark-1-divergence.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The position engine counts as an open owner decision only a parked `decision` row with no answer
record of its own, and a hold of a run whose phase is `HELD`. Today every owed parked row and every
hold fact interrupts for the run's whole life, so a run that parked once never answers `act` again.

## 2. Scope (IN)

- **S1** — The answer record. A parked `decision` row settles when the newest tracked, well-formed
  disposition record of the same build whose `Item` is the row's tag has `Disposition` exactly
  `answered` and a `Reason` that is not blank. The tag is `item.parked.` followed by the row's
  timestamp, lowercased, each `:` written `-`. Any other record, word or absence leaves the row open,
  so a later record of another word re-opens it. Observed by AC1, AC2, AC3.
- **S2** — The same second. The second `decision` row of one timestamp, in file order, takes the tag
  ending `.2`, the third `.3`, and so on, so no record settles two rows. Observed by AC4.
- **S3** — The kinds. Only a `decision` row is read. A `rescope`, `handoff`, `abort`, `override` or
  `waiver` row raises no interrupt. One open decision still answers `awaiting` for the whole build.
  Observed by AC1, AC5.
- **S4** — The hold. A hold interrupts only while the run-state `phase` fact reads `HELD`. Its
  `hold-code` and `hold-until` are read as today. Observed by AC6.
- **S5** — The interrupt names its answer. The subject of an open row is
  `decision · item <first word> · answer <tag>`, so the tag to record is printed and not composed by
  hand. Each record that decides a row, settled or not, is listed as a `read —` line. Observed by AC1,
  AC2, AC4.
- **S6** — The seam. `tools/loop/adapt.py` gains `read_newest_dispositions`, one read answering every
  tag, and `read_disposition_release` answers from it, its signature and its return unchanged.
  Observed by AC7.
- **S7** — The engine stops reading the `owed` line of the hand-over: `read_handover` drops its parse,
  its `owed` member and its default, and `FX_OWED` goes from the fixtures. The driver goes on printing
  the line. Observed by AC8.
  - **Readers:**
    by name: `tools/loop/position.py`, whose `read_handover` fills the member, whose `derive_interrupts`
    reads it and whose `render_handover` spells `FX_OWED`.
    by value: NO VALUE READERS — the member is a pair of tuples compared only in the
    engine's own interrupt read, which this unit rewrites.
- **S8** — The rule is stated in the docstring of `tools/loop/position.py` and in `help/loop.md`, with
  four sentences in each: that it replaces the interrupt wording of TOOL-dDeclaredLoop-7, which
  counted every owed kind; that a newly parked decision stops the run until it is answered; that an
  agent types the record, so the quoted words in its `Reason` are the evidence; and how the record is
  written. `tools/loop/README.md` gains the same rule in one paragraph. Observed by AC9.

## 3. Non-goals (OUT)

- `actions.free`, `.governance/policy.toml`, any hook, the card's read bound and
  `tools/memory-tree/routed_commits.py`.
- The unattended kit, the line it prints into the hand-over included, and its owed sets. The driver's
  surfaced count, runlog and the drift report keep counting every owed kind.
- The disposition grammar, the record door, and the join `check_disposition_record` makes. An
  `item.parked.` tag is declared by no definition, so that join answers None, unarmed.
- A door verb that derives the tag from a row. The interrupt prints it (S5).
- Settling a `flow.on-exhausted` or an owner-gate row by its item's own disposition. Each is a
  `decision` row as any other and needs its own record.
- Proving that a `Reason` quotes the owner. No machine can.
- Any file of the dBoundRoles run. Its records are its owner's to have written.
- The cost of one position read: `TOOL-aAnsweredPark-2`.

### Edges

- **consumes-from** external — the disposition door and reader of `tools/memory-tree/build_records.py`,
  without which a row has no record to settle by
- **hands-off** external — the read's cost, ask TOOL-aAnsweredPark-2; who commits a park's row and its
  answer under the `actions.free` guard, ask TOOL-aAnsweredPark-3; the hand-over line no reader uses,
  ask TOOL-aAnsweredPark-4

## 4. Design

### What stands today

`tools/loop/position.py#derive_interrupts` matches `PARKED_ROW` over the run-state text and raises an
`owner-decision` for each row whose kind is in the hand-over's owed set, and for each `rescope` row
whose act is in its owed acts. It reads no record, and its docstring says so: every owed entry stands.
It reads a hold from `hold-code` and `hold-until` alone. `tools/unattended/unattended.sh` resumes a run
without clearing either fact: dBoundRoles at `18ba9d38` reads `phase: SPECCING` beside
`hold-code: host-owner-action` and `hold-until: owner`.

### The seam

`tools/loop/adapt.py#read_disposition_release` reads every disposition record through
`tools/memory-tree/build_records.py#read_records`, keeps the build's well-formed ones of one tag and
answers the newest as `(stem, word)`. It drops the `Reason`. The change lifts its body:

```python
def read_newest_dispositions(root, build, named=()):
    """{tag: record} of `build`: per `Item`, the newest well-formed tracked disposition record whose
    stem is not in `named`."""

def read_disposition_release(root, build, tag, named):
    newest = read_newest_dispositions(root, build, named).get(tag)
    return (newest["id"], newest.get("Disposition", "").strip("`")) if newest else None
```

Newest keeps its one key, the stem's date and then `n`. A value is the whole record, its `Reason` and
its `path` included. The callers of `read_disposition_release`, in `adapt.py`, `breakpoints.py`,
`budget.py`, `claim.py` and `placement.py`, are untouched.

### The read in position.py

`PARKED_ROW` is replaced by `DECISION_ROW`, the same grammar with the timestamp captured and the kind
fixed:

```python
DECISION_ROW = re.compile(r"^([0-9][0-9-]*T[0-9:]*Z) decision · item (\S+)")

def read_open_decisions(root, build, text):
    """`(open, records)`: `open` the `(item, tag)` of each decision row of `text` no record settles, in
    file order; `records` the path of each record that decided a row."""
```

It walks the lines with the trailing CR cut, as today. It counts each timestamp seen, so the n-th row
of one timestamp takes the bare tag at 1 and `.<n>` above it. Where no row matches it returns two empty
lists and reads no record. Otherwise it calls `read_newest_dispositions(root, build)` once for all
rows. A row is settled where `newest.get(tag)` has `Disposition` equal to `answered` and a `Reason`
that is not blank, backticks stripped from the first as the seam strips them. `adapt` is imported
inside the function, for the reason the import in `tools/loop/position.py#read_build_items` states.

Every timestamp the grammar admits gives a tag the door takes: the first segment character is a digit,
and the rest is digits, `t`, `z` and `-`. No escape is needed.

`derive_position_into` calls it after the run-state text is read and appends one `read` entry per
returned path, `<path>@<blob>`, as the acceptance records get theirs. `derive_interrupts` takes the
list as a required positional, so a caller cannot omit it silently:

```python
def derive_interrupts(text, handover, owed, decisions, parents_open, claims, now, remote_absent=False):
    out = [{"kind": "owner-decision", "subject": "decision · item %s · answer %s" % d} for d in decisions]
    code = owed(text, "hold-code") if owed and (owed(text, "phase") or "").strip() == "HELD" else None
```

The rest of the hold branch is unchanged. `derive_answer` is unchanged. An open decision still
precedes the dependency rung and the next item.

A record that is staged and not committed settles a row, since
`tools/memory-tree/design_lib.py#read_tracked_builds` reads the index. An unstaged one does not.

### The fixtures

`tools/loop/position.py --fixture --plant owner-decision` took 8.7 s and `steps` 15.3 s on node a,
PINNED 2026-11-25, and the leg's ceiling is 300 s against a recorded reading of 201.6 s. So the unit
adds two plants, each one scratch repository read once per variant, as `url-forms` prints several rows
over one repository. A variant rewrites the working copy of `RUN.md`, writes its records through
`tools/memory-tree/build_records.py#write_disposition` with `today="2026-01-01"`, stages them unless it
says otherwise, derives one position, and removes its records from the index and the tree. Each prints
`position: fixture · <plant> · <variant> · <answer> · <open tags or none>`.

`T` is `item.parked.2026-01-01t00-00-00z`, spelled as a literal and not derived, so the plant is an
oracle of its own.

| Plant | Variant | Planted | Owed |
|---|---|---|---|
| `parked-decisions` | `unanswered` | one row, no record | `awaiting` · T |
| | `answered` | T `answered`, a reason | `act` · none |
| | `untracked` | the same record, never staged | `awaiting` · T |
| | `other-row` | the tag of second `00:00:01`, `answered`, a reason | `awaiting` · T |
| | `other-word` | T `answered` with a reason, then T `withdrawn` with one | `awaiting` · T |
| | `no-reason` | T `answered`, no `Reason` line | `awaiting` · T |
| | `one-second` | three rows of one second, T and T`.3` answered | `awaiting` · T`.2` alone |
| `parked-kinds` | `no-question` | one row each of `rescope` with act `defer`, `handoff`, `abort`, `override`, `waiver` | `act` · none |
| | `hold-resumed` | `phase: BUILDING`, a hold code, `hold-until: owner` | `act` · none |
| | `hold-live` | `phase: HELD`, the same two facts | `awaiting` on the hold |
| | `hold-passed` | `phase: HELD`, `hold-until: after 2026-01-01T00:00:00Z` | `act` · none |

A negative variant could pass by finding nothing. So each variant with a tracked record also asserts
that `read_newest_dispositions` over the scratch repository holds that record under its tag with the
planted word, and `untracked` asserts that the file exists and the map does not hold its tag.

The `owner-decision` plant's predicate gains the printed tag.

### Inventory

| Name | Cell or kind |
|---|---|
| `read_newest_dispositions` | a python function, verb `read` |
| `read_open_decisions` | a python function, verb `read` |
| `run_parked_plant` | a python function, verb `run` |
| `DECISION_ROW`, `FX_PARKED` | python constants |
| `parked-decisions`, `parked-kinds` | plant keys of `PLANTS` |
| `item.parked.<timestamp>` | a record's `Item` tag, declared by no definition |

### Migration

No stored data moves. A run that parked before this unit keeps its open decisions until each has its
record. Its `rescope` and `handoff` rows and its released hold stop interrupting at the next read.

### Files touched (estimate)

`tools/loop/position.py`
`tools/loop/adapt.py`
`tools/loop/README.md`
`help/loop.md`
`tools/run-gates/selftest-budgets.txt`
`memory/map/generated/symbols.json`

The budgets row of `loop position fixtures` moves its `plants=` token from 45, PINNED 2026-11-25, to
the derived `len(PLANTS)`, with the two new plants' direct readings added. The map file is regenerated
and never hand-edited.

### Alternatives rejected

- A `resume` settling every earlier row: the owner ruled each row needs its own record.
- A new row kind in the run-state file: it edits the unattended kit and its grammar.
- One record read per row: each spawns one `git ls-files` and reads every disposition record, on a read
  that is already too slow for its caller (TOOL-aAnsweredPark-2).
- A `.1` suffix on every first row: the common row would carry a suffix that says nothing.

## 5. Production-readiness checklist

- security — a record lifts an owner interrupt, so the test is exact: the row's own tag, the one word,
  a present `Reason`, tracked, newest. Anything else leaves the row open. The evidence is the quoted
  words, which no check verifies, and both documents say so.
- perf / scale — one record read per position, and none where the run holds no decision row.
- error / empty / loading states — a failed record read raises as the acceptance read beside it does,
  and answers `invalid-input`. No run-state file gives no row and no hold. A malformed record is
  skipped, as the seam skips it, so an older well-formed `answered` record still stands.
- observability — an open row prints its answer tag, and each deciding record is a `read —` line.
- risks — an agent can write a record the owner never gave; the review reads its `Reason`. A run sees
  the fix only once it carries this unit's commit.
- testing — the two plants of §4, red and then green, and the staged breaks of §7.
- migration — none; §4 Migration.
- user docs — `help/loop.md`, the position section and the disposition record section.

## 6. Acceptance criteria

- **AC1** — When `python tools/loop/position.py --fixture --plant parked-decisions` runs, its
  `unanswered` line reads `awaiting` with T, its `answered` line reads `act` with none and that read
  lists the record as a `read —` line, its `untracked` line reads `awaiting`, and the case ends `held`.
  `python tools/loop/position.py --fixture --plant owner-decision` prints
  `interrupt — owner-decision · decision · item which-way · answer item.parked.2026-01-01t00-00-00z`.
  Red when: no record settles a row, which is the base engine, or a row settles with no tracked record.
- **AC2** — When the same `parked-decisions` plant runs, its `other-row` and `no-reason` lines read
  `awaiting` with T.
  Red when: the tag is not compared, or the `Reason` test is dropped.
- **AC3** — When the same `parked-decisions` plant runs, its `other-word` line reads `awaiting` with T.
  Red when: any record of the tag settles, or an older `answered` record outranks the newer one.
- **AC4** — When the same `parked-decisions` plant runs, its `one-second` line names T`.2` alone.
  Red when: one record settles every row of its second, or the ordinal counts from another base.
- **AC5** — When `python tools/loop/position.py --fixture --plant parked-kinds` runs, its `no-question`
  line reads `act` with none.
  Red when: any of the five kinds interrupts, which is the base engine.
- **AC6** — When the same `parked-kinds` plant runs, `hold-resumed` and `hold-passed` read `act`,
  `hold-live` reads `awaiting` naming the hold, and the case ends `held`.
  Red when: the `phase` fact is not read, which is the base engine on `hold-resumed`; or a live hold
  stops interrupting.
- **AC7** — When `python tools/loop/adapt.py --fixture --plant owner-approves` runs, it ends `held`,
  the held change released by its `continue` record, and
  `grep -c "def read_disposition_release(root, build, tag, named)" tools/loop/adapt.py` prints 1.
  Red when: the lifted body answers another record or another shape than the base reader.
- **AC8** — When `grep -nE "FX_OWED|handover\[.owed.\]|PARKED_ROW" tools/loop/position.py` runs, it
  prints nothing, and the `steps` plant still ends `held`.
  Red when: the engine still reads the owed sets.
- **AC9** — When `grep -c "replaces the interrupt wording of" tools/loop/position.py help/loop.md` runs,
  each file counts at least 1, the other sentences of S8 beside it, and
  `grep -n "every owed entry stands" tools/loop/position.py` prints nothing.
  Red when: a document still states the old rule, or leaves out one of the four sentences.
- **AC10** — When `read_open_decisions` of `tools/loop/position.py` runs over a throwaway clone checked
  out at `18ba9d38`, for the build dBoundRoles and the text of its run-state file, it returns six open
  rows and no record path. The six tags are `item.parked.2026-11-22t08-48-53z`, `item.parked.2026-11-23t08-04-03z`,
  `item.parked.2026-11-23t09-30-23z`, `item.parked.2026-11-24t23-07-16z`,
  `item.parked.2026-11-24t23-07-22z` and `item.parked.2026-11-24t23-07-28z`. So the build answers
  `awaiting` until each has its record, by the unchanged rung of `derive_answer`.
  Red when: a row of another kind is returned, or a decision with no record is missing.
  cost: seconds for the function; the whole engine took 51 s there on node a.
  fixture: a shared clone under `%TEMP%`, removed after. The whole engine of this tree answers
  `invalid-input` over that commit, since its overlay rows are older than this tree's item schema, so
  the function is the observation.
  figure: PINNED at `18ba9d38`, 2026-11-25. That tree's own engine printed 28 owner-decision
  interrupts: 6 `decision`, 20 `rescope`, 1 `handoff` and 1 hold.

## 7. Gates

`loop position fixtures` · `loop adapt fixtures` · `loop budget fixtures` · `loop breakpoint fixtures` · `loop claim fixtures` · `loop placement fixtures` · `loop termination` · `docs` · `every held leg is budgeted, every budget row resolves` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `line length` · `kit version markers` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/position.py · covers AC1 AC2 AC3 AC4 · the plant `parked-decisions`: `answered` and `one-second` are red on the base engine; `unanswered` and `untracked` are red with settled fixed true, `other-row` with the tag compare dropped, `other-word` with the word test dropped, `no-reason` with the `Reason` test dropped · plants 45 to the derived count
New arm: tools/loop/position.py · covers AC5 AC6 · the plant `parked-kinds`: `no-question` and `hold-resumed` are red on the base engine; `hold-live` is red with the hold branch removed, `hold-passed` with the passed test fixed false · plants 45 to the derived count

## 8. Open questions

none

The owner ruled the three forks on 2026-11-25, and the brief quotes the answer: a row settles only by
its own record, only decision rows and a live hold interrupt, and one open decision stops the run.

## 9. Revision log

- rev-1 · 2026-11-25 · initial draft.

## 10. Reuse audit

`tools/codebase-map/reuse_lookup.py` with "read the newest owner disposition record of a tag" ranked
`read_records` and `read_memory_tree`, both already under the seam, and named no reader of the newest
disposition by tag. The seam is `tools/loop/adapt.py#read_disposition_release`, found from its five
calling modules; it is extended in place. `tools/memory-recall/query.py` answered the asks of this
build, TOOL-dUnstuckLanding-3 and TOOL-dDeclaredLoop-19, whose design has the owner write the answer to
a gate through `build_records.py new disposition`. No record names an answer form for a parked row.
The interrupt wording this unit replaces is S4 of
`memory/builds/dDeclaredLoop/spec/2026-10-24-spec-TOOL-dDeclaredLoop-7.md`, which is closed and frozen.
Where the recall and the code disagreed: nowhere. The brief's prototype of the door was re-read in
`tools/memory-tree/build_records.py#check_disposition_fields`, whose `TAG` admits no uppercase and no
colon, which is why the tag is lowercased and dashed.

Recall terms used: parked decision owed owner-decision settle answer resume hold disposition
PARK_KINDS_OWED position awaiting interrupt.
