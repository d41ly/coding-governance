# TOOL-aAnsweredPark-5 — the closing review's five minors: six fixture variants, the re-ask limit in three documents, the ledger's contradiction

**Status:** CLOSED · rev-1 · 2026-11-25 · node a · Tier-1 · base 3d6c1702 · streams tooling · order 2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-25-build-TOOL-aAnsweredPark-5-1-acceptance-ledger.md](../build/2026-11-25-build-TOOL-aAnsweredPark-5-1-acceptance-ledger.md) | journal | — |
| [2026-11-25-prompt-TOOL-aAnsweredPark-5-brief.md](../prompts/2026-11-25-prompt-TOOL-aAnsweredPark-5-brief.md) | research | — |

<!-- /gen:spec-records -->

## 1. Goal

The arms of TOOL-aAnsweredPark-1 can turn red on each condition of the settle and hold rules that
`2026-11-25-review-TOOL-aAnsweredPark-1-closing-diff-round1` found no arm for. The documents state the
one limit the review found, and the acceptance ledger stops contradicting itself.

## 2. Scope (IN)

- **S1** — The re-ask limit (M1, the document half). The sentence of §4 "The sentence" stands in the
  docstring of `tools/loop/position.py`, in `help/loop.md` and in `tools/loop/README.md`, right after
  the sentence that a newly parked decision stops the run. Observed by AC4.
- **S2** — The two filters (M2). `FX_PARKED` gains the `parked-decisions` variants `other-build` and
  `malformed`. Each owes `awaiting` with the tag, no such record read and no `read —` line, and the
  plant asserts that exactly one of the two filters refuses the record. Observed by AC1.
- **S3** — The newest key (M3). `FX_PARKED` gains the `parked-decisions` variants `tenth` and
  `later-date`, each owing `awaiting` with the tag. Observed by AC2.
- **S4** — The hold's phases (L1). `FX_PARKED` gains the `parked-kinds` variants `hold-specced` and
  `hold-no-phase`, each owing `act` with none. Observed by AC3.
- **S5** — The ledger (L2). The acceptance ledger of TOOL-aAnsweredPark-1 says its two arms were seen
  red afterwards, leaves only the section 7 legs owed, and carries its two seen-red lines inside its
  evidence block, where their reader looks. Observed by AC5.
- **S6** — What names the variants follows them: the two `PLANTS` texts, the comment over `FX_PARKED`,
  the docstring of `run_parked_plant`, the fixture bullet of `help/loop.md`, and the
  `loop position fixtures` row of `tools/run-gates/selftest-budgets.txt`. Observed by AC6.

## 3. Non-goals (OUT)

- The behaviour of `read_open_decisions`, `derive_interrupts` and `read_newest_dispositions`. The review
  judged it correct, and no line of `tools/loop/adapt.py` moves.
- The unattended kit. The driver half of M1 is ask TOOL-aAnsweredPark-6.
- A new plant, and a second scratch repository. The variants join the two plants that stand.
- `actions.free`, `.governance/policy.toml`, any hook, the card's read bound,
  `tools/memory-tree/routed_commits.py`, the disposition grammar and any dBoundRoles file.
- The spec of TOOL-aAnsweredPark-1, which is CLOSED and frozen.

## 4. Design

### What stands today

`tools/loop/position.py#FX_PARKED` holds each record as `(tag, word, reason)`, and
`tools/loop/position.py#run_parked_plant` writes each through
`tools/memory-tree/build_records.py#write_disposition` under `FX_SLUG`. That door validates, numbers the
record itself and takes one date. So no variant can hold a record the two filters of
`tools/loop/adapt.py#read_newest_dispositions` refuse, nor one whose read order disagrees with the key.
`tools/memory-tree/build_records.py#read_records` reads the paths sorted, so `disposition-10` is read
before `disposition-2`.

### The record's change

A record may carry a fourth member, `(old, new)`: one replacement, made once in the path and once in
the text of the record the door wrote. The plant writes the records one at a time. Where a record
carries a change, the plant removes the file the door wrote and writes the changed text at the changed
path with `write_fixture_files`, before the next record is numbered. A change whose `old` is in neither
is a miss. `paths` holds the changed paths, so the staging and the removal reach them.

| Variant | Records of T, in writing order | Owed |
|---|---|---|
| `other-build` | `answered` with a reason, its path under `builds/tOth/` for `builds/tPos/` | `awaiting` · T |
| `malformed` | `answered` with a reason, `- **Channel:** elsewhere` for `- **Channel:** terminal` | `awaiting` · T |
| `tenth` | `answered`, `-disposition-1.md` moved to `-disposition-2.md`; `withdrawn`, `-disposition-3.md` moved to `-disposition-10.md` | `awaiting` · T |
| `later-date` | `answered`, `-disposition-1.md` moved to `-disposition-3.md`; `withdrawn`, `2026-01-01-build-TOOL-tPos-1-disposition-4.md` moved to `2026-01-02-build-TOOL-tPos-1-disposition-2.md` | `awaiting` · T |

Every record of `tenth` and `later-date` carries a reason. T, the one decision row and the phase
`BUILDING` are those of the variants that stand. In both, the owed winner is the record written last, so
the plant's check that the last record of a tag is the one read stands unchanged.

`later-date` is beyond the two breaks the review named for M3. It is here because the goal asks for each
condition, the key is the date and then `n`, and its one row needs no code of its own.

### What the plant asserts of a record

The variant's `staged` flag becomes a word: `read`, `untracked` or `refused`. Records are staged unless
the word is `untracked`. A record is owed under its tag in the map, and as a `read —` line, only where
the word is `read`; the two present comparisons take that test in place of `staged`.

A `refused` variant could pass by staging nothing. So the plant also reads every disposition record of
the scratch repository through `read_records` with `read_disposition`, and for each record of a variant
that is not `untracked` counts two facts: its build is not `FX_SLUG`, and it is malformed. The record
must be there with its planted `Item`, with a count of 1 under `refused` and 0 under `read`. So
`other-build` is refused by the build filter alone and `malformed` by the malformed filter alone.

### The holds

An empty phase member drops the fact: the replacement for the `phase: BUILDING` line is then the empty
string, and the plant asserts that a `phase:` line stands exactly where the member is not empty.

| Variant | Planted | Owed |
|---|---|---|
| `hold-specced` | `phase: SPECCING`, `hold-code: host-owner-action`, `hold-until: owner` | `act` · none |
| `hold-no-phase` | no `phase` fact, the same two facts | `act` · none |

### What was probed

Both plants were run with these six variants from a scratch script over the engine at `66ffa667`, the
repository untouched, and both ended `held`. With the build filter dropped, `other-build` alone answered
`act`. With the malformed filter dropped, `malformed` alone did. With the key replaced by last-read, and
then by a lexical compare of `id`, `tenth` alone did. With the date dropped from the key, `later-date`
alone did. With the phase test replaced by `!= "BUILDING"`, `hold-specced` and `hold-no-phase` alone
moved, to `awaiting`. The two plants took 16.1 s and 9.3 s on node a, PINNED 2026-11-25 from one direct
run, and 52.9 s and 30.0 s in a second, the box under load, PINNED the same day. The budgets row reads
them at 11.5 s and 6.5 s, the leg's ceiling is 300 s and that row's reading 219.6 s, all PINNED
2026-11-25. The first run's growth of 7.4 s leaves the leg inside its ceiling.

### The sentence

In all three documents, word for word, wrapped as the document wraps:

> The driver's `--park` writes no row for an item and reason already parked, so a question asked again
> in the same words after its answer raises no interrupt and must be parked with a different reason; a
> second `flow.on-exhausted` ending keeps the first row (ask TOOL-aAnsweredPark-6).

Read at `tools/unattended/unattended.sh@9b83204c:17645`, where the compare strips the timestamp and
returns 0, and at `tools/unattended/unattended.sh@9b83204c:9592`, where a standing row is printed.
The probe AC4 runs:

```bash
python - <<'PY'
import pathlib
want = ("The driver's `--park` writes no row for an item and reason already parked, so a question asked again in the "
        "same words after its answer raises no interrupt and must be parked with a different reason; a second "
        "`flow.on-exhausted` ending keeps the first row (ask TOOL-aAnsweredPark-6).")
for p in ("tools/loop/position.py", "help/loop.md", "tools/loop/README.md"):
    t = " ".join(pathlib.Path(p).read_text(encoding="utf-8").split())
    print(p, t.count(want), t.count("until it is answered. " + want))
PY
```

### The ledger

Its "Owed to the close" section ends "Neither was observed in this pass", and the two seen-red lines
stand under it. HYGIENE's "Acceptance ledger" closes an evidence block at the next heading, and
`tools/memory-tree/seen_red.py` reads seen-red lines inside a block alone, so it reads neither:
`seen_red.py --build aAnsweredPark --base 3d6c1702` prints `NO RECORD` at `66ffa667`. The two lines
move, byte for byte, to directly under the AC10 line. The section keeps its heading and this paragraph
alone:

> Every leg section 7 of the spec names. The two arms `parked-decisions` and `parked-kinds` were not
> observed in this pass; the main loop saw each red and then green afterwards, at `ace7f1eec`, and the
> two seen-red lines above record it.

That join is per leg, so from this unit on those two lines also answer the leg for this unit's own
arms. The main loop still records this unit's seen-red lines in its own ledger.

### Inventory

| Name | Kind |
|---|---|
| `other-build`, `malformed`, `tenth`, `later-date` | variants of `parked-decisions` |
| `hold-specced`, `hold-no-phase` | variants of `parked-kinds` |

No function, constant or plant key is minted.

### Files touched (estimate)

`tools/loop/position.py`
`tools/loop/README.md`
`help/loop.md`
`tools/run-gates/selftest-budgets.txt`
`memory/builds/aAnsweredPark/build/2026-11-25-build-TOOL-aAnsweredPark-1-1-acceptance-ledger.md`
`memory/builds/aAnsweredPark/build/2026-11-25-build-TOOL-aAnsweredPark-5-1-acceptance-ledger.md`
`memory/builds/aAnsweredPark/spec/2026-11-25-spec-TOOL-aAnsweredPark-5.md`
`memory/LIVE.md`
`memory/builds/aAnsweredPark/README.md`

The second ledger is this unit's own journal record, one line per criterion, every line sharing a
backticked token with its criterion. This spec's header moves to its terminal status with the build.
The pre-commit hook renders `memory/LIVE.md`, `memory/builds/aAnsweredPark/README.md` and this spec's
records block; none is hand-edited. The budgets row gains one re-read naming this unit once: the two
plants read alone by direct CLI over the unit's base, their growth added to the earlier reading. Its
seconds column stands while x1.5 of the new reading is under it, and its `plants=` token does not move.

### Alternatives rejected

- Padding records of other tags to reach n=10: eight more files staged and read, for one moved path.
- A second build folder passed to the door: it needs the folder made first, where a moved path does
  the same through the one mechanism the other variants use.
- Changing `hold-resumed` to `SPECCING`: the review rejected it, since it moves the blind spot.

## 5. Acceptance criteria

- **AC1** — When `python tools/loop/position.py --fixture --plant parked-decisions` runs, its
  `other-build` and `malformed` lines read `awaiting` with `item.parked.2026-01-01t00-00-00z`, the seven
  variants that stood answer as before, and the case ends `held`.
  Red when: `r["build"] != build or` is dropped from `read_newest_dispositions`, which reds
  `other-build`, or `r["malformed"] or` is, which reds `malformed`.
- **AC2** — When the same `parked-decisions` plant runs, its `tenth` and `later-date` lines read
  `awaiting` with that tag.
  Red when: the newest key is replaced by last-read or by a lexical compare of `id`, each of which reds
  `tenth`, or its date half is dropped, which reds `later-date`.
- **AC3** — When `python tools/loop/position.py --fixture --plant parked-kinds` runs, its
  `hold-specced` and `hold-no-phase` lines read `act` with none, and the case ends `held`.
  Red when: the phase test of `derive_interrupts` is replaced by `!= "BUILDING"`.
- **AC4** — When the probe of §4 "The sentence" runs, it prints `1 1` after each of
  `tools/loop/position.py`, `help/loop.md` and `tools/loop/README.md`.
  Red when: a document lacks the sentence, which is the base, or words it otherwise or puts it elsewhere.
- **AC5** — When `python tools/memory-tree/seen_red.py --build aAnsweredPark --base 3d6c1702` runs, it
  names `loop position fixtures` with `ace7f1ee` and the first ledger, and
  `grep -c "Neither was observed" memory/builds/aAnsweredPark/build/2026-11-25-build-TOOL-aAnsweredPark-1-1-acceptance-ledger.md`
  prints 0.
  Red when: the two lines stay under the heading, where the reader prints `NO RECORD`, or the old
  paragraph stays.
- **AC6** — When `grep -n "seven variants" tools/loop/position.py` runs, it prints nothing, and
  `grep -c "TOOL-aAnsweredPark-5" tools/run-gates/selftest-budgets.txt` prints 1. The fixture bullet of
  `help/loop.md` describes the six new variants beside the ones it lists.
  Red when: a text still counts or lists only the variants that stood.

## 6. Gates

`loop position fixtures` · `docs` · `every held leg is budgeted, every budget row resolves` · `codebase-map coverage + freshness` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `line length` · `kit version markers` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/position.py · covers AC1 AC2 · the plant `parked-decisions`: `other-build` is red with the build filter dropped, `malformed` with the malformed filter dropped, `tenth` with the newest key replaced by last-read and again by a lexical compare, `later-date` with the date dropped from the key · none
New arm: tools/loop/position.py · covers AC3 · the plant `parked-kinds`: `hold-specced` and `hold-no-phase` are red with the phase test replaced by `!= "BUILDING"` · none

## 7. Open questions

none

## 8. Revision log

- rev-1 · 2026-11-25 · initial draft.

## 9. Reuse audit

`tools/codebase-map/reuse_lookup.py` with "fixture variant of a parked decision record" ranked
`write_fixture_files`, `write_record` and `read_records`, all three already under the plant, and named
no other writer of a record a reader must refuse. The seam is `tools/loop/position.py#run_parked_plant`
with `FX_PARKED`, extended in place over `tools/memory-tree/build_records.py#write_disposition`.
`tools/memory-recall/query.py` answered TOOL-aAnsweredPark-1, TOOL-aAnsweredPark-6 and
TOOL-dUnstuckLanding-3, and no record of such an arm. The recall and the code disagreed nowhere.

Recall terms used: parked decision owed owner-decision settle answer resume hold disposition
PARK_KINDS_OWED position awaiting interrupt.
