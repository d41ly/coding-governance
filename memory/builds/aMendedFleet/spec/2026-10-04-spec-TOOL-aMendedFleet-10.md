# TOOL-aMendedFleet-10 — `--asks` rows carry the pointer and a 160-byte summary, and `--path` ranks and caps them

**Status:** CLOSED · rev-3 · 2026-10-05 · node a · Tier-2 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 10

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-04-build-TOOL-aMendedFleet-10-1-acceptance-ledger.md](../build/2026-10-04-build-TOOL-aMendedFleet-10-1-acceptance-ledger.md) | journal | — |

<!-- /gen:spec-records -->

## 1. Goal

A reviewer or a builder who wants the open asks that touch the files in front of it today reads the
whole `gen_build_index.py --asks --json` projection: 175,183 bytes for the 457 live asks, 312,033
with `--all`, measured 2026-10-04. Its rows carry neither the ask's text nor its pointer, so the
reader still has to open each `BACKLOG.md`. This unit gives every row its pointer and a short
summary, and adds a `--path` filter that ranks the matching asks by severity, then recency, and caps
them, so the feed a stage reads is a few kilobytes about the files that stage touches.

## 2. Scope (IN)

- **S1** — Every row of `--asks --json` gains two fields: `pointer`, the ask's pointer tail exactly as
  `tools/memory-tree/backlog.py` parses it, empty when the ask has none; and `summary`, the ask's text
  at most 160 bytes of UTF-8. The thirteen existing fields keep their names and values. Observed by
  AC1 and AC2.
- **S2** — The summary is the existing `render_summary_cell` reduction measured in encoded BYTES: the
  pointer tail goes, a link becomes its text, backticks go, a pipe becomes a slash, and the cut lands
  on a space, ends with the ellipsis, never splits a multi-byte character, and includes the
  ellipsis's three bytes in the 160. Observed by AC2.
- **S3** — A new option `--path <path>…`, a list option read like `--live-builds`, keeps only the
  asks with a locator matching one of the given paths. An ask's locators are its pointer target and
  the path of every `seen` clause it carries after the merge, read by one helper the READY grader's
  R4 walk also calls. A match is equality or a whole-segment directory prefix in either direction,
  after both sides lose a trailing `:<line>` and fold a backslash to a slash; a locator that is
  relative to the memory root matches as if prefixed by it. Observed by AC3 and AC4.
- **S4** — Under `--path` the kept rows are ordered by severity, `BLOCKER` then `HIGH`, `MED`, `LOW`
  and unlabelled, then by filing date newest first, then by the existing id sort key; and capped at
  `--limit <n>`, default 20, where 0 means no cap. The JSON object gains `paths`, `matched` and
  `cut`; the table form prints one trailing line naming how many were cut and the `--limit 0`
  rerun. Without `--path` every mode keeps today's order and today's bytes apart from S1's two
  fields. Observed by AC4 and AC5.
- **S5** — Refusals, exit 2 with a usage line naming the conflict: a `--path` value that is absolute or
  carries a `..` segment; `--path` together with an id pick, `--tsv`, `--ready`, `--target`,
  `--live-builds` or `--probe`; `--limit` without `--path`, or with a value that is not a
  non-negative integer. Observed by AC6.
- **S6** — The kit README's Print modes paragraph names `--path`, `--limit` and the two new fields.
  Observed by AC7.
- **S7** — `memory/map/generated/symbols.json` is regenerated for the new
  definitions. NOT OBSERVED by a criterion here: `python tools/codebase-map/gen_map.py --check` at
  the close is its check, and §7 names the leg that reads it.

## 3. Non-goals (OUT)

- The TAB projection. `--tsv` is read by the unattended driver by field position, eleven fields, so
  it gains nothing and refuses `--path`.
- Repointing `memory/guides/REVIEW-PROTOCOL.md` and `tools/workflows/tier2-review.js` at the filtered
  call. That is `TOOL-aMendedFleet-11`.
- The close-time list of open asks that target the build's touched files, unit 66, and the kickoff
  step that points at this call, unit 78. Both may read `--path`; neither is built here.
- A path filter on the generated family views under `memory/backlog/`.
- Triage of the 452 unlabelled asks, unit 14. Unlabelled ranks last, which is what it means today.

### Edges

- **hands-off** `TOOL-aMendedFleet-11` — repointing the review protocol and the review harness at the
  `--asks --json --path` call this unit adds.

## 4. Design

### Evidence

Read at base `7af5f564`, re-verified 2026-10-04.

- `build_ask_row` in `tools/memory-tree/gen_build_index.py` returns thirteen pinned fields, none of
  them the text or the pointer. Its docstring calls the names a contract, and the self-test arm that
  pins them asserts the thirteen are PRESENT, so an added field breaks neither it nor its readers:
  `drift_report.py` reads the length of `--asks --json`, nothing inside a row.
- `backlog.py` parses the pointer at the ` → ` arrow into `Ask.pointer`, and `read_pointer_target`
  normalises the three authored shapes. The R4 walk in `derive_ready` reads the same two locator
  sources this unit filters on: `parse_seen` over the merged `seen` clauses, and the pointer.
- `render_summary_cell` cuts at `BACKLOG_EXCERPT_CHARS`, default 72, measured in CHARACTERS.
- Of the 457 live asks, 267 carry a pointer. A rough count over pointer and `seen` paths found 31
  live asks targeting `tools/unattended/unattended.sh`, 18 `tools/govkit/govkit.py` and 18
  `tools/memory-tree/gen_build_index.py`; PINNED, measured 2026-10-04 with a regex read of the raw
  rows, which the helper in S3 supersedes. The report's figure was 26 of 58 hits on the first two.

### Data model

One `--asks --json` row, with the two additions marked:

```
{"id", "home", "file", "line", "filed", "unit", "status", "decided_by", "sev",
 "closing", "declining", "holds", "live_specs",
 "pointer": "<the parsed pointer, or an empty string>",          # S1, every row
 "summary": "<the reduced text, at most 160 bytes of UTF-8>"}     # S1, every row
```

The envelope under `--path`, beside today's `mode`, `examined` and `asks`:

```
"paths": ["<each normalised --path value>"], "matched": <rows before the cap>, "cut": <rows the cap removed>
```

### Inventory

- `ASK_SUMMARY_BYTES = 160` and `ASK_PATH_LIMIT = 20`, module constants of `gen_build_index.py`.
- `--path` joins `ASK_LIST_OPTIONS`, `--limit` joins `ASK_VALUE_OPTIONS`, and `ASK_USAGE` names both.
- `derive_ask_locators` in `backlog.py`: an ask and its merged clauses in; its located paths and
  whether any locator is external out. R4 calls it instead of its inline walk, so the filter and the
  grade read one locator set.
- A `by_bytes` keyword on `render_summary_cell`, default false, so the view's cell is unchanged.
- `resolve_ask_path` and `check_ask_path` in `gen_build_index.py`: the one normaliser both sides
  of S3's comparison pass through, and the match itself; and `ASK_PATH_CONFLICTS`, the options S5
  refuses beside `--path`.

Every name above is graded by the lexicon leg like any other definition; a name it refuses is
replaced with its `--suggest` answer at build time, and this list is amended with a rev bump.

### Files touched (estimate)

- `tools/memory-tree/gen_build_index.py`
- `tools/memory-tree/backlog.py`
- `tools/memory-tree/README.md`
- `memory/map/generated/symbols.json`

### Rollout

Additive. Every existing consumer reads fields by name or reads the TAB projection, which does not
change. The kit version bump is owed once, at this build's close, after the last move.

### Alternatives rejected

- **Ranking and capping every mode.** The view and the print modes share `build_ask_sort_key` so a
  table and the view it explains agree on order; reordering the unfiltered modes breaks that.
- **Matching on the pointer alone.** 190 of the 457 live asks carry no pointer, and most of those
  name their file in a `seen` locator; R4 already treats the two as one locator set.
- **A byte budget instead of a row cap.** Rows differ by their list fields, so a byte budget cuts
  mid-severity unpredictably. A row count with a printed cut is the shape a reader can rerun.
- **Recall's `query.py --for-paths`.** BM25 over prose answers "what is about this file" by
  vocabulary; the locators answer it by declaration. The report ranks the structured join higher.

## 5. Production-readiness checklist

- security — read-only over tracked records. `--path` values are compared as strings and never
  opened, and the `..` and absolute refusals keep them repo-relative.
- perf / scale — one extra pass over the asks already in memory; the run stays at today's 2.6 s.
- error / empty / loading states — no match prints an empty `asks` list with `matched` 0, and the
  table prints its header with no rows, as today.
- observability — `matched` and `cut` say what the cap removed, and the table's trailing line says
  how to see it.
- risks — a pointer in prose that normalises to nothing matches nothing, which is R4's answer too.
- testing — new arms in the generator's own `--selftest`, plus direct calls on the live tree.
- migration — none.
- user docs — the kit README's Print modes paragraph, S6.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gen_build_index.py --asks --json` runs on the live tree,
  every row carries `pointer` and `summary` beside the thirteen existing fields, and a row whose raw
  line in its `BACKLOG.md` has a ` → ` tail carries that tail as `pointer`.
  Red when: a row lacks either field, or a pointered ask reports an empty `pointer`.
- **AC2** — When the generator's `--selftest` runs, an arm over a fixture ask whose text is 400 bytes
  with a multi-byte character straddling byte 160 reads a `summary` of at most 160 encoded bytes,
  ending in the ellipsis on a whole character.
  Red when: the cut is measured in characters, or splits the character.
- **AC3** — When `gen_build_index.py --asks --json --limit 0` runs with `--path` naming
  `tools/unattended/unattended.sh`, every returned row's raw line, read at its `file` and `line`,
  names that path or a directory containing it, in its pointer or a `seen` locator.
  Red when: a returned row names neither.
  figure: the row count is DERIVED at observation time.
- **AC4** — When the generator's `--selftest` runs, a fixture of five asks with known pointers, `seen`
  locators and severities returns, for `--path` on a file one directory pointer and two `seen` clauses
  reach, exactly those three asks ordered HIGH before MED before unlabelled, and a fourth ask whose
  pointer is relative to the memory root is matched by its rooted path.
  Red when: an ask outside the three is returned, one is missed, or the order differs.
- **AC5** — When the AC3 call runs without `--limit`, it returns at most 20 rows with `cut` equal to
  `matched` less 20, and its byte count is below a tenth of the unfiltered `--asks --json` measured
  in the same session; and when `--asks --json` runs without `--path`, its rows keep today's order.
  Red when: the cap is not applied, `cut` disagrees, or the unfiltered order changes.
  figure: both byte counts DERIVED at observation time.
- **AC6** — When `gen_build_index.py --asks` is called five times, with `--path` set to ../x, with
  `--path` set to an absolute path, with `--tsv` beside a `--path`, with `--limit 5` alone, and with
  `--limit -1` beside a `--path`, each exits 2 and names the conflict. These five calls are the staged breaks for S5's refusals.
  Red when: any exits 0 or prints a row.
- **AC7** — When `grep -n -- "--path" tools/memory-tree/README.md` runs, the Print modes paragraph
  names `--path`, `--limit`, `pointer` and `summary`.
  Red when: the paragraph names none of them.

## 7. Gates

`build README slot contract` · `memory hygiene` · `drift-audit records` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/gen_build_index.py --selftest · a five-ask fixture for `--path`, and a 400-byte summary, against today's generator · none

## 8. Open questions

- **F1 — Which modes does the ranking and the cap reach?**
  Options: every mode; only under `--path`. Every mode reorders the view's print twin.
  RESOLVED (agent, 2026-10-04, delegated): only under `--path`; the unfiltered modes keep their order.
- **F2 — Which locators does `--path` match?**
  Options: the pointer alone, as the report words it; the pointer and the `seen` paths, as R4 reads
  them. The second reaches the 190 pointerless asks and shares one helper with R4.
  RESOLVED (agent, 2026-10-04, delegated): the pointer and every merged `seen` path.
- **F3 — Does `--tsv` take the filter?**
  Options: filter the READY population too; refuse the pair. The driver parses `--tsv` by position
  and drives it with `--ready` lists, so a cap there would silently shrink a mandate's grade.
  RESOLVED (agent, 2026-10-04, delegated): refuse the pair with exit 2.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from `cmd_asks`, `build_ask_row` and the R4 walk at base.
- rev-2 · 2026-10-04 · §2 S7 · §4 · §7 · M2 cross-read: the definitions this unit adds
  move `memory/map/generated/symbols.json`, which `TOOL-aMendedFleet-82` and the build's other
  code units regenerate and declare; this spec omitted the write, its Files touched row and the leg.
- rev-3 · 2026-10-05 · §4 Inventory · the build added two helpers and one constant the inventory
  did not list, so S3's normalisation and match are written once rather than inline twice.

## 10. Reuse audit

The seams extended are `cmd_asks` and `build_ask_row` in `tools/memory-tree/gen_build_index.py`,
`read_asks_args` for the two options, `render_summary_cell` for the reduction, and the R4 locator walk
of `derive_ready` in `tools/memory-tree/backlog.py`, which S3 lifts into one helper both readers call.
`python tools/codebase-map/reuse_lookup.py "filter open asks by the file path they point at"` named
`render_ask_row` and `build_ask_sort_key` in `backlog.py` and no path filter, so no existing filter
fits; the R4 walk was found by reading the grader. Recall named the report row this unit implements
and `TOOL-dDerivedDocket-7`'s view spec, which is where the excerpt cell and the pinned projection
were decided. The report said 164 KB for `--asks --json`; the tree now says 175,183 bytes.

Recall terms used: asks pointer arrow path filter gen_build_index --asks --json summary excerpt severity rank cap backlog view
