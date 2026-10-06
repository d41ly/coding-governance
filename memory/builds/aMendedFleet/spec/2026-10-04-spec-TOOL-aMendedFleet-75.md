# TOOL-aMendedFleet-75 — a `New arm:` line declares the acceptance criteria its arm keeps observed

**Status:** CLOSED · rev-4 · 2026-10-06 · node a · Tier-1 · base 7af5f564 · streams tooling · ratified 2026-10-04 · order 75

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md](../reviews/2026-10-06-review-TOOL-aMendedFleet-1-closing-diff-round1.md) | diff-review | KICK-aMendedFleet-1 KICK-aMendedFleet-2 KICK-aMendedFleet-3 KICK-aMendedFleet-4 PLAY-aMendedFleet-1 PLAY-aMendedFleet-2 PLAY-aMendedFleet-3 PLAY-aMendedFleet-4 TOOL-aMendedFleet-1 TOOL-aMendedFleet-2 TOOL-aMendedFleet-3 TOOL-aMendedFleet-4 TOOL-aMendedFleet-5 TOOL-aMendedFleet-6 TOOL-aMendedFleet-7 TOOL-aMendedFleet-8 TOOL-aMendedFleet-9 TOOL-aMendedFleet-10 TOOL-aMendedFleet-11 TOOL-aMendedFleet-12 TOOL-aMendedFleet-13 TOOL-aMendedFleet-14 TOOL-aMendedFleet-15 TOOL-aMendedFleet-16 TOOL-aMendedFleet-17 TOOL-aMendedFleet-18 TOOL-aMendedFleet-19 TOOL-aMendedFleet-20 TOOL-aMendedFleet-21 TOOL-aMendedFleet-22 TOOL-aMendedFleet-23 TOOL-aMendedFleet-24 TOOL-aMendedFleet-25 TOOL-aMendedFleet-26 TOOL-aMendedFleet-27 TOOL-aMendedFleet-28 TOOL-aMendedFleet-29 TOOL-aMendedFleet-30 TOOL-aMendedFleet-31 TOOL-aMendedFleet-32 TOOL-aMendedFleet-33 TOOL-aMendedFleet-34 TOOL-aMendedFleet-35 TOOL-aMendedFleet-36 TOOL-aMendedFleet-37 TOOL-aMendedFleet-38 TOOL-aMendedFleet-39 TOOL-aMendedFleet-40 TOOL-aMendedFleet-41 TOOL-aMendedFleet-42 TOOL-aMendedFleet-43 TOOL-aMendedFleet-44 TOOL-aMendedFleet-45 TOOL-aMendedFleet-46 TOOL-aMendedFleet-47 TOOL-aMendedFleet-48 TOOL-aMendedFleet-49 TOOL-aMendedFleet-50 TOOL-aMendedFleet-51 TOOL-aMendedFleet-52 TOOL-aMendedFleet-53 TOOL-aMendedFleet-54 TOOL-aMendedFleet-55 TOOL-aMendedFleet-56 TOOL-aMendedFleet-57 TOOL-aMendedFleet-58 TOOL-aMendedFleet-59 TOOL-aMendedFleet-60 TOOL-aMendedFleet-61 TOOL-aMendedFleet-62 TOOL-aMendedFleet-63 TOOL-aMendedFleet-64 TOOL-aMendedFleet-65 TOOL-aMendedFleet-66 TOOL-aMendedFleet-67 TOOL-aMendedFleet-68 TOOL-aMendedFleet-69 TOOL-aMendedFleet-70 TOOL-aMendedFleet-71 TOOL-aMendedFleet-72 TOOL-aMendedFleet-73 TOOL-aMendedFleet-74 TOOL-aMendedFleet-81 TOOL-aMendedFleet-82 TOOL-aMendedFleet-83 TOOL-aMendedFleet-84 TOOL-aMendedFleet-85 TOOL-aMendedFleet-86 TOOL-aMendedFleet-87 TOOL-aMendedFleet-88 TOOL-aMendedFleet-89 TOOL-aMendedFleet-90 TOOL-aMendedFleet-91 TOOL-aMendedFleet-92 TOOL-aMendedFleet-93 TOOL-aMendedFleet-94 TOOL-aMendedFleet-97 TOOL-aMendedFleet-98 TOOL-aMendedFleet-99 TOOL-aMendedFleet-100 TOOL-aMendedFleet-101 TOOL-aMendedFleet-102 TOOL-aMendedFleet-103 TOOL-aMendedFleet-104 TOOL-aMendedFleet-105 |

<!-- /gen:spec-records -->

## 1. Goal

A spec names each suite arm it adds on a `New arm:` line in §7, and nothing on that line says which
acceptance criterion the arm keeps observed after the build. So a reader cannot tell a criterion
observed once by a direct check from one a suite re-observes on every bar, and an adopter gets no
test-adequacy signal at all. The report's answer is one grammar token on the line that already
exists, not a second traceability line. This unit adds an optional `covers` field to the `New arm:`
grammar and grades it: every id the field names must be a criterion the same spec's §6 defines.

## 2. Scope (IN)

- **S1** — The grammar. In `tools/memory-tree/SPEC-TEMPLATE.template.md` and its dogfood copy
  `memory/TEMPLATE-SPEC.md`, identically, the arm-home line in the section "Where a new arm lives"
  and the one in the skeleton's §7 body both read
  `New arm: <suite path> · covers <AC ids|none> · <what stages its failing case> · <floor to move, or none>`.
  The paragraph below the first one says the `covers` field is the one part of the line a checker
  reads, that it lists the criteria of THIS spec the arm re-observes, space-separated, or `none`
  for an arm that observes only scope items no criterion names, that a line without the field is
  legal and ungraded, and that the rest of the line is prose which never satisfies the leg line.
  Observed by AC4.
- **S2** — The join. `tools/check-spec-tokens.py` gains `scan_arm_covers`, which reads the Gates
  section of every live spec through `extract_gates`. An arm line is a line opening `New arm:` at
  column 0 plus every following line that is indented and non-blank. Its fields split on ` · `.
  A field whose text opens with `covers ` yields its whitespace-separated tokens. A token passes
  when it is `none` standing alone in the field, or a label the spec's Acceptance section defines
  through `extract_acceptance`, in any of the three label forms the template admits. Every other
  token is a hit of kind `covers`: an id the section does not define, a malformed id, or `none`
  beside an id. Hits print and waive exactly as every other kind does; the hit token is the
  composite `covers <- <spec path> <token>`, as the size and claims joins compose theirs, so a
  waiver row reaches one spec's id and never every spec's. Observed by AC1 and AC2.
- **S7** — The one live spec whose field the join refuses on the day it lands, unit 4 of the
  kickoff family in this build, spelled a range, `covers AC1 to AC4`; its line is written out as
  the four ids, as its own rev bump. Observed by AC3, which requires the run add no `[covers]` hit.
- **S3** — Liveness. Every run prints one line,
  `spec-tokens: covers join · <n> New arm line(s) in <m> live spec(s) · <c> carry a covers field · <k> token(s) graded`,
  so a join that matched nothing is distinguishable from a clean one. Observed by AC3.
- **S4** — The codebase-map dossier `memory/map/features/spec-tokens.md` gains one sentence naming
  the covers join beside its existing `New arm:` sentence. Observed by AC5.
- **S5** — An arm in `tools/check-spec-tokens.test.sh` over a fixture spec carrying a dangling id,
  `none`, a defined id, and an arm line with no field. NOT OBSERVED by a criterion here: the suite
  runs once at the close, and the arm is declared under `New arm:` in §7.
- **S6** — `memory/map/generated/symbols.json` is regenerated for `scan_arm_covers`, in the same
  commit. NOT OBSERVED by a criterion here: `python tools/codebase-map/gen_map.py --check` at the
  close is its check, and §7 already names the leg that reads it.

## 3. Non-goals (OUT)

- Requiring the field. Making every new `New arm:` line carry `covers` needs a dated cutoff key,
  and unit 21 of this build makes a new cutoff key retire an old one; the S3 count is the adoption
  reading, and a requirement is a follow-up once it shows the field is written.
- Reading criterion ids anywhere else on the line. §8 F2 measured that it reds an innocent spec.
- A report of criteria no arm covers, or of arms covering every criterion. That is an adequacy
  report over the field, worth building once lines carry it.
- Mutation testing, which the report defers.
- A second §7 traceability line, which the report rejected because it duplicates `New arm:`.
- Rewriting the 88 `New arm:` lines live specs carry today. They stay legal and ungraded.
- Bumping the spec-tokens or memory-tree kit versions, owed once at the build's close.

### Edges

none

## 4. Design

### Evidence

Read at the worktree HEAD `efc4b0c9`, whose bytes under `tools/` and in `memory/TEMPLATE-SPEC.md`
equal base `7af5f564`'s.

- The template's section "Where a new arm lives" defines the line as three fields and says it is
  prose, never machine-graded, and never satisfies the leg join; the skeleton's §7 body repeats the
  three-field shape. `tools/memory-tree/SPEC-TEMPLATE.template.md` is the kit source and
  `memory/TEMPLATE-SPEC.md` its rendered copy, held equal by the `kit/dogfood doc parity` leg.
- `git grep "New arm"` outside build records finds the two templates, two conf comments, the
  spec-tokens dossier, the bar join's refusal text `BAR_WHY` and its suite. Nothing parses the line;
  the leg join skips it because a prose prefix is not a leg line.
- `tools/check-spec-tokens.py` already holds `extract_gates` and `extract_acceptance`, both found by
  heading text, its own hit and waiver plumbing with a `kind` per hit, and one summary line per join.
- A probe over the tree at the date, a scratch reading of each live spec's arm lines with their
  continuations: 98 live specs, 88 `New arm:` lines, 8 naming a criterion id in their prose and 0
  carrying a `covers` field. Seven of the eight name ids their own §6 defines. The eighth, unit 5
  of this build, names `AC11`, which is a criterion of the transition-audit suite's own record and
  not of unit 5. PINNED, measured 2026-10-04.

### Data model

```
New arm: <suite path> · covers <AC ids|none> · <what stages its failing case> · <floor to move, or none>
New arm: `tools/check-spec-tokens.test.sh` · covers AC1 AC2 · a dangling id staged in a fixture spec · none
```

### Inventory

| Identifier | Kind | Cell |
|---|---|---|
| `scan_arm_covers` | Python function | `py.function`; `python tools/lexicon/lexicon.py --suggest scan_arm_covers --as py.function` answered OK |
| `covers` | hit kind and grammar field keyword | none |

### Files touched (estimate)

- `tools/check-spec-tokens.py`
- `tools/check-spec-tokens.test.sh`
- `tools/memory-tree/SPEC-TEMPLATE.template.md`
- `memory/TEMPLATE-SPEC.md`
- `memory/map/features/spec-tokens.md`
- `memory/map/generated/symbols.json`
- `memory/builds/aMendedFleet/spec/2026-10-04-spec-KICK-aMendedFleet-4.md`

### Alternatives rejected

- **Grade every criterion id on the line.** It needs no keyword, and it reds unit 5 for citing
  another record's `AC11`, measured in §8 F2.
- **A fourth field at the end of the line.** Today's third field is free prose that often carries
  ` · ` inside it, so a trailing field cannot be told from prose by position; a keyworded field can
  sit anywhere, and the second place keeps the suite and its criteria together.
- **A new `### Arms` table in §7.** It is the second traceability surface the report rejected.

## 5. Production-readiness checklist

- security — N/A: a read-only lint over tracked markdown.
- perf / scale — one regex pass over the Gates section of each live spec, already in memory; no
  spawn.
- error / empty / loading states — a spec with no Gates heading or no arm line contributes nothing
  and is counted on the S3 line; a spec with no Acceptance heading defines no label, so any id its
  field names is a hit.
- observability — the S3 line on every run.
- risks — an author writes `covers` with a criterion of another document; that is the hit S2 exists
  to print, waivable when deliberate.
- testing — AC1 to AC5 here; the arm in S5.
- migration — N/A: the field is optional and no live line carries it.
- user docs — S1 is the user documentation; the template is what an author reads.

## 6. Acceptance criteria

- **AC1** — When a scratch clone made by `git clone --local` under a short `%TEMP%` directory gains
  one tracked fixture spec under a fixture build's `spec/` folder, `SPECCED`, whose §6 defines only
  `AC1` and whose §7 carries `New arm:` with the field `covers AC1 AC9`, and
  `python tools/check-spec-tokens.py` runs in that clone without `--list`, stdout carries one line
  carrying `[covers]` and the composite token `covers <- <fixture spec> AC9`, and none whose token
  names `AC1`; the `HIT` prefix is `--list`'s and a plain run never prints it.
  Red when: the `scan_arm_covers` call is staged out of `main` and the `AC9` line is absent.
  cost: seconds, plus the clone.
- **AC2** — When the fixture's field is changed in turn to `covers AC1`, to `covers none`, and to
  `covers none AC1`, and the checker re-runs after each, the first two print no `[covers]` line and
  the third prints one naming `none`; and when the field is deleted and the line names `AC9` only
  in its prose, no `[covers]` line prints.
  Red when: `none` is refused alone or accepted beside an id, or an id in prose is graded.
- **AC3** — When `python tools/check-spec-tokens.py` runs in this tree, stdout carries one line
  opening `spec-tokens: covers join ·` whose arm-line count equals the number of column-0
  `New arm:` lines in the Gates sections of the live specs, and the run adds no `[covers]` hit.
  Red when: the count is 0 while live specs carry arm lines, which is a join reading nothing.
  figure: DERIVED; the count is whatever the live population holds on the day, 88 at writing.
- **AC4** — When `grep -c "covers <AC ids|none>"` runs over
  `tools/memory-tree/SPEC-TEMPLATE.template.md` and over `memory/TEMPLATE-SPEC.md`, each reports 2,
  and `grep -n "covers"` over each hits the paragraph under "Where a new arm lives".
  Red when: one copy carries the field and the other does not.
- **AC5** — When `grep -n "covers" memory/map/features/spec-tokens.md` runs, it hits the sentence
  naming the join.
  Red when: the checker gains a join its dossier never names.

## 7. Gates

`spec tokens (a spec's own names resolve)` · `spec-tokens self-test` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `lexicon naming predicates` · `line length` · `kit epoch (shipped bytes move, the version moves)`

New arm: `tools/check-spec-tokens.test.sh` · covers AC1 AC2 · a fixture spec whose `covers` field names a dangling id, `none` alone, `none` beside an id and a defined id, staged red by deleting the `scan_arm_covers` call · none

## 8. Open questions

- **F1** — Prose grammar only, or a graded field?
  Options: document the field and grade nothing, as the line is today; or document it and grade
  that each id resolves in the same spec. An ungraded field is the remembered-not-gated shape the
  charter's §7 rules against, and the grade costs one join in a checker that already extracts both
  sections. The grammar and its grader are one mechanism, as every graded spec rule in the template
  is. No veto applies: the join adds no dependency, no surface and no write.
  RESOLVED (agent, 2026-10-04, delegated): graded, per S2, and opt-in by the field's presence, so
  no cutoff key is minted.
- **FACT-QUESTION · F2** — Can the join grade every criterion id the line carries, with no keyword?
  Probe: a scratch reading of each live spec's `New arm:` lines and continuations, every token
  shaped like a criterion id joined against that spec's §6 labels. The observation that decides it
  is whether any live line names an id its own §6 does not define. Liveness: the same probe printed
  the 8 lines naming an id and resolved seven of them, so it can answer both ways.
  RESOLVED (agent, 2026-10-04, delegated): no. Unit 5's line names `AC11` of another record and
  would red; only a declared `covers` field is graded.
- **F3** — Must every new arm line carry the field?
  Options: required from a dated cutoff; optional and counted. A cutoff key is a new conf key that
  unit 21 makes retire an old one, and no line carries the field today to show it is wanted.
  RESOLVED (agent, 2026-10-04, delegated): optional and counted, per S3.

## 9. Revision log

- rev-1 · 2026-10-04 · initial draft, from the spec brief's unit 75, report items [B#27] and
  [B#45], a read of `tools/check-spec-tokens.py` and both template copies, and a probe of every
  live spec's arm lines at base.
- rev-2 · 2026-10-04 · S6 · §4 · M2 cross-read: `scan_arm_covers` moves
  `memory/map/generated/symbols.json`, which units 18, 70 and 82 regenerate and declare for their
  own definitions; this spec named the freshness leg but omitted the write and its Files touched row.
- rev-3 · 2026-10-06 · S2 · S7 · §4 · built: the join, run over the tree, refused one live line,
  `covers AC1 to AC4` in a sibling spec written after this one, so AC3 could not hold without S7;
  and S2 now names the composite hit token, which a bare `AC9` waiver row would otherwise share
  across every spec.
- rev-4 · 2026-10-06 · AC1 · the closing review's finding 20: AC1 asked a plain run for a `HIT`
  line, which only `--list` prints; it now asks for the plain form, `[covers]` and the composite
  token, the form the covers arm of `tools/check-spec-tokens.test.sh` asserts. Built by
  TOOL-aMendedFleet-112; no code moved.

## 10. Reuse audit

The seams extended are `extract_gates` and `extract_acceptance` in `tools/check-spec-tokens.py`,
which already find both sections by heading text, and that checker's hit, waiver and summary-line
plumbing, which every join shares. `python tools/codebase-map/reuse_lookup.py "declare which
acceptance criteria a suite arm keeps observed and grade the ids against the spec"` returned
name-stem neighbours, among them `inventory_ids` in the map extractors, `armed` in
`tools/memory-tree/corpus_ids.py` and `parse_spec_h1` in the memory-tree library, none of which
reads a `New arm:` line; `git grep "New arm"` confirmed no parser exists. Recall returned the
template's own arm-home paragraph, the bar join's `New arm:` substitute, and `TOOL-aHonedRuleset-12`,
an ask naming a §7 leg no §6 criterion runs, which this field gives a place to answer. Where the
report and the tree disagree: none; the line is still three fields and ungraded.

Recall terms used: `python tools/memory-recall/query.py "should a New arm line name the acceptance
criteria the suite arm covers, and is the New arm line graded" --terms "New arm grammar acceptance
criterion AC ids suite arm traceability spec-tokens §7 leg line test adequacy mutation"`
