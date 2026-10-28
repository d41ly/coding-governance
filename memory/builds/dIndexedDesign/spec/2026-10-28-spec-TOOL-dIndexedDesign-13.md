# TOOL-dIndexedDesign-13 — the reuse scout's return under M1c's contract: the `seams` record, its caps and MUST definition, read once and its seams handed on as rows

**Status:** OPEN · rev-2 · 2026-10-28 · node d · Tier-2 · base 57bc3b91 · streams tooling · order 9 · advances TOOL-dIndexedDesign-17

**Carries:** cl-dClosedLoop-0395@07a81090 whole
**Carries:** node:item.design.seams
**Carries:** node:record-kind.seams

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-agent-ledger.md) | journal | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-31 TOOL-dIndexedDesign-32 TOOL-dIndexedDesign-33 TOOL-dIndexedDesign-34 TOOL-dIndexedDesign-35 TOOL-dIndexedDesign-36 TOOL-dIndexedDesign-37 TOOL-dIndexedDesign-38 TOOL-dIndexedDesign-39 TOOL-dIndexedDesign-40 TOOL-dIndexedDesign-41 TOOL-dIndexedDesign-42 TOOL-dIndexedDesign-43 TOOL-dIndexedDesign-44 TOOL-dIndexedDesign-45 TOOL-dIndexedDesign-46 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-fix-return.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-fix-return.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-b.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-b.md) | research | TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-1 |
| [2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md](../build/2026-10-28-build-TOOL-dIndexedDesign-1-spec-stage-returns.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-1-fix-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-1-fix-brief.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-20 |
| [2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md](../prompts/2026-10-28-prompt-TOOL-dIndexedDesign-1-spec-brief.md) | research | TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-3 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-16 |
| [2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md](../reviews/2026-10-28-review-TOOL-dIndexedDesign-9-spec-audit-round1.md) | spec-audit | TOOL-dIndexedDesign-9 TOOL-dIndexedDesign-12 TOOL-dIndexedDesign-16 TOOL-dIndexedDesign-1 TOOL-dIndexedDesign-7 TOOL-dIndexedDesign-2 TOOL-dIndexedDesign-6 TOOL-dIndexedDesign-8 TOOL-dIndexedDesign-20 TOOL-dIndexedDesign-5 TOOL-dIndexedDesign-4 TOOL-dIndexedDesign-14 TOOL-dIndexedDesign-10 TOOL-dIndexedDesign-11 TOOL-dIndexedDesign-15 TOOL-dIndexedDesign-3 |

<!-- /gen:spec-records -->

## 1. Goal

gap-design-11 (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-gap-register.md:359`):
the reuse scout's return is unspecified; it returns one seam, with no cap, no MUST definition, no census
and no unmet needs (`tools/roles/agents/gov-reuse-scout.agent.md:10`, `returns: the seam to extend`).
TOOL-dLinkedLibrary-2 S5 and S6 give the scout a house index and a record with a `## Matches` section.
This unit widens that record to the contract aScoutedSeam measured and the owner adopted as NT-10
(`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md:162-163`,
:194-196): needs and a concrete sketch before the search, the anchors resolved, a convention census, at
most twelve seams and five MUSTs, a MUST defined as an existing implementation that new code would
duplicate, the unmet needs, and the MUST and SHOULD seams handed on as rows.

## 2. Scope (IN)

Build-run preconditions this unit calls and does not build: `tools/codebase-map/house_index.py`, its
`## Steps` and the scout's record with its one reader `read_reuse_scouts(root, slug)` and `python
gen_build_index.py --reuse-scouts <slug>` (TOOL-dLinkedLibrary-2 S2, S3, S5, S6); the record-kind factory
(TOOL-dTotalRecall-1 S9); the `[[item]]` and `[[stand-in]]` rows of `tools/loop/loop.toml`
(TOOL-dDeclaredLoop-12 S2, -13 S8) and the `upstream` field with its `## Establishes` rows
(TOOL-dDeclaredLoop-29 S1, S3, S4); the tag bundle as TOOL-dIndexedDesign-12 routes it (`bundle`).

Shared file the build run sequences: `tools/loop/loop.toml`, where TOOL-dIndexedDesign-8 S11 (order 8)
arms `item.design.decompose`'s row before S6 below adds its `upstream` entry to that same row, and
TOOL-dIndexedDesign-20 S10, at this unit's order 9, arms the `input`, `reentry` and `inventory` rows.

- **S1** — The record kind `seams`, tag `record.seams`, registered by `python record_kinds.py new seams
  --tag record.seams --writer hand --check "memory hygiene" --field Index` (I15). Its home stays
  TOOL-dLinkedLibrary-2 S6's `<date>-build-<unit id>-reuse-scout[-<x>].md`, now bound `**Serves:**
  seams <ids>` with its `**Index:** <sha8>` line. A `-reuse-scout` record bound `research`, every one in
  the tree at base, is read as TOOL-dLinkedLibrary-2 reads it and graded by nothing here. Observed by AC6.
- **S2** — The return grammar, sections in M1c's order (I10, refined in §4 "The return"): `## Needs`,
  `## Sketch`, `## Anchors`, `## Census`, `## Matches`, `## Unmet`, `## Bug classes`, `## Establishes`.
  `## Matches` keeps TOOL-dLinkedLibrary-2's heading and takes TOOL-aScoutedSeam-1 §4's line spelling,
  with one field added, the sketched component a MUST would duplicate. `## Bug classes` is a slot this
  unit places and does not grade: its lines, cap and arming are TOOL-dIndexedDesign-14's. Observed by AC1.
- **S3** — The one reader. `read_reuse_scouts(root, slug)` in `tools/memory-tree/tree_lib.py`, widened:
  each record bound `seams` also returns its sections parsed, `{"needs", "sketch", "anchors", "census",
  "matches", "unmet", "bug_classes", "establishes"}`, a match as `{binding, path, symbol, how,
  duplicates, not}`. Its CLI's printed lines are unchanged. Units 4 and 14 read the sections here and
  nowhere else. Observed by AC1.
- **S4** — The caps. `MATCH_CAP = 12` and `MUST_CAP = 5` beside the reader in `tree_lib.py`, PINNED from
  M1c's return cap
  (`memory/builds/aScoutedSeam/build/2026-10-11-build-TOOL-aScoutedSeam-1-6-m1c-sketch-scout.js:58`) and
  TOOL-aScoutedSeam-1 §4's `MUST_CAP` (`memory/builds/aScoutedSeam/spec/2026-10-11-spec-TOOL-aScoutedSeam-1.md:314-316`).
  Observed by AC2.
- **S5** — The grader, `check_reuse_scout(rec, root)` in `tree_lib.py`, each finding naming the record
  and the line: a section missing or out of order; `## Needs` outside 3 to 10 lines or `## Sketch`
  outside 6 to 15, M1c's step-2 ranges; an `## Anchors` path absent at the record's `**Index:**` sha;
  a `## Census`, `## Unmet` or `## Matches` line outside its grammar, or an empty section with no `none`;
  more than `MATCH_CAP` matches, more than `MUST_CAP` MUSTs, or a SHOULD before a MUST; a MUST that
  duplicates nothing, by either test of §4 "A MUST"; and a MUST or SHOULD with no `## Establishes` row,
  or a row with no match. CLI `python gen_build_index.py --reuse-scouts <slug> --check`, exit 1 on a
  finding, 0 on none, 2 on a record it could not read, its last line counting graded and `research`
  records. Observed by AC2, AC3, AC4 and AC5.
- **S6** — The rows. Each MUST and SHOULD match has one row under `## Establishes`, `- seam-<n> · seam ·
  <path> :: <symbol>`, `<n>` its match's position, in TOOL-dDeclaredLoop-29 S3's grammar and closed
  kind set. `item.design.decompose`'s row in `tools/loop/loop.toml` gains `upstream = [{ item =
  "item.design.seams" }]`, gate `record`, so `derive_upstream_rows` hands each row to the decompose
  item; no entry is `measured` (TOOL-dDeclaredLoop-29 S2). Observed by AC4 and AC7.
- **S7** — The item goes live. `item.design.seams`'s `[[stand-in]]` row leaves `tools/loop/loop.toml`,
  its row's `witness` names `--reuse-scouts --check` and its `returns` `record-kind.seams`; its other
  fields stay as TOOL-dDeclaredLoop-12 transcribed them. Observed by AC7.
- **S8** — The bar grades it. A new hygiene check 31, "a seams record conforms to the scout's return",
  delegated to `gen_build_index.py --reuse-scouts --check` over every build, printed and verdicted as
  check 29 is (`tools/memory-tree/check-memory-hygiene.sh:1780-1819`), and written into the check
  catalogue of `tools/memory-tree/HYGIENE.template.md` (:192), rendered to `memory/HYGIENE.md`; under
  `--staged` it grades the staged `seams` records alone, since each is graded by its own text and the
  tree at its sha. Observed by AC5.
- **S9** — The scout is told. `house_index.py`'s `## Steps` (TOOL-dLinkedLibrary-2 S3) gains a final
  Return step: the eight sections in order, the two caps as numbers, the MUST and SHOULD definitions of
  §4, one `## Establishes` row per MUST and SHOULD, and, for each anchor the request names as a tag,
  the anchors step reading its bundle as `bundle` arrives from TOOL-dIndexedDesign-12, by
  `derive_tag_bundles(tags, root)` in `design_lib.py`.
  `gov-reuse-scout.agent.md`'s `returns:` line names the `seams` record's eight sections, and its body
  stays under its 1536-byte ceiling (`tools/roles/check_roles.py:88`); `.claude/agents/gov-reuse-scout.md`
  and `tools/roles/README.md` re-render. The `reuse` entry's `enforced-by` in `tools/roles/workflows.toml`
  (:28) names check 31. `help/reuse.md`, TOOL-dLinkedLibrary-2's page, gains a section on the
  return's eight sections and its caps. Observed by AC8.
- **S10** — The ask, so no third grammar lands: an ask in aScoutedSeam's `BACKLOG.md`, filed by the main
  loop, text in §8 F3. NOT OBSERVED by a criterion: the main loop files it after the writers return,
  and this unit's build observes its row, not its disposition.

## 3. Non-goals (OUT)

- The house index, its sections, its slot and the scout's record name: TOOL-dLinkedLibrary-2.
- The bug classes: what `## Bug classes` lists, `BUG_CLASS_CAP`, the replay that arms it and its
  retirement are TOOL-dIndexedDesign-14's; this unit only places the section.
- The §10 check that a spec's reuse audit cites a recorded probe: TOOL-dIndexedDesign-4, which reads S3.
- The diff-time reuse check and its rows (`build.reuse-check`): dScopedBuild.
- The tag bundle's reader and its stand-in: TOOL-dIndexedDesign-12; S9 only tells the scout to read it.
- Demoting a sixth MUST to SHOULD as TOOL-aScoutedSeam-1's harness does: no harness runs this scout's
  return, so a return past a cap is refused and the scout re-returns.
- Re-shaping the existing `research`-bound scout records: they stay as written.

### Edges

- **consumes-from** `TOOL-dIndexedDesign-12` — `bundle`, `derive_tag_bundles`, the tag bundle the anchors step reads for a tag the request names; without it the step reads paths only and says so
- **hands-off** `TOOL-dIndexedDesign-4` — `read_reuse_scouts`, the widened reader whose parsed `seams` record the §10 arm checks a spec's outcome against
- **hands-off** `TOOL-dIndexedDesign-14` — `read_reuse_scouts`, the widened reader, and the `## Bug classes` slot S2 places, whose lines, cap and arming are that unit's
- **hands-off** `TOOL-dIndexedDesign-33` — the `seams` kind of S1, which that unit adds to the untyped head of `RECORD_KIND_TOKENS` (report id 20, HIGH)
- **hands-off** `TOOL-dIndexedDesign-38` — the round-1 spec audit's minors that land on this spec, report ids 10 and 45, each a scope item of that batch unit

## 4. Design

### Evidence

- The role returns "the seam, cited by path" and defers to `reuse-lookup.agent.md`
  (`tools/roles/agents/gov-reuse-scout.agent.md:10`, :18-20); TOOL-dLinkedLibrary-3 S1 deletes that file.
- The `reuse` workflow runs no harness and is enforced by nothing (`tools/roles/workflows.toml:22-29`).
- M1c's schema asks for `needs`, `sketch`, `census`, `seams` and `unmet`, each seam with `binding` MUST
  or SHOULD and `not` (`…-1-6-m1c-sketch-scout.js:21-34`), and caps seams at 12 (:58).
- TOOL-aScoutedSeam-1 §4 spells `- MUST <repo>:<path> :: <symbol> — <how>[; not <stale copy>]` and
  defines a MUST as an implementation the build would duplicate or bypass, its `how` naming the
  duplicate (`2026-10-11-spec-TOOL-aScoutedSeam-1.md:298-305`, :324-326).
- TOOL-dDeclaredLoop-29 S3 closes the row kinds at `seam`, `criterion`, `interface`, `fork`, `finding`,
  `repair`, a row id one tag segment.

### The return

```markdown
**Serves:** seams TOOL-tFix-1
**Index:** 1a2b3c4d

## Needs
- <need>
## Sketch
- c1 — <component a builder would write>
## Anchors
- <named thing> — <path>[ :: <symbol>]
## Census
- <choice>: <majority> (<n> of <m>)
## Matches
- MUST <path> :: <symbol> — <how> · duplicates c<n>[; not <stale copy>]
- SHOULD <path> :: <symbol> — <how>[; not <stale copy>]
## Unmet
- <need> — searched <what>
## Bug classes
## Establishes
- seam-1 · seam · <path> :: <symbol>
```

Two refinements of I10's proposed spelling, both this unit's as its owner: sketch lines carry an id
`c<n>`, and a MUST carries `· duplicates c<n>`. `<repo>:` is dropped from TOOL-aScoutedSeam-1's
spelling because the scout searches one tree. A section with nothing to say holds the single line
`none`, so an empty section and a forgotten one differ.

### A MUST

A MUST duplicates nothing, and is a finding, when either test holds: its `duplicates c<n>` names no
`## Sketch` line, so no component a builder would write is shown to duplicate it; or its `<path>` is
absent at the record's `**Index:**` sha, or present without `<symbol>` in it, so no existing
implementation stands behind it. The first is the clause's definition made checkable; the second is
"existing". What neither test sees: whether the sketched component really is what the implementation
does, which the closing review and dScopedBuild's reuse check read.

### What it does not check

A seam the scout missed; whether a SHOULD fits its need; whether the census counted real siblings; and
a `research`-bound scout record.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `check_reuse_scout`, `MATCH_CAP`, `MUST_CAP` | function, constants in `tree_lib.py` | `py.function`, `py.constant`, asked at the pass |
| `--check` on `--reuse-scouts` | flag of `gen_build_index.py` | `cli.flag`, asked at the pass |
| `seams` | record kind, a row of `record-kinds.toml` | none |
| `## Needs`, `## Sketch`, `## Anchors`, `## Census`, `## Unmet`, `## Bug classes`, `## Establishes` | return sections | none |
| `c<n>`, `seam-<n>`, `duplicates` | sketch ids, row ids, the MUST field | none |
| check 31 | hygiene check | none |

### Migration

None: the four `research`-bound scout records of this build and dLinkedLibrary's stay ungraded, and the
first `seams` record is the first graded one.

### Rollout

Live at landing. The decompose item's `upstream` entry sits at `record`, so rows are handed on and
answered and gate nothing until a measurement moves the edge.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`, `tools/memory-tree/gen_build_index.py`: S3, S4, S5
- `tools/memory-tree/record-kinds.toml`: S1, written by the factory
- `tools/memory-tree/check-memory-hygiene.sh`, `tools/memory-tree/check-memory-hygiene.test.sh`: S8
- `tools/memory-tree/HYGIENE.template.md`, render `memory/HYGIENE.md`: S8
- `tools/codebase-map/house_index.py`, `tools/codebase-map/selftest.py`: S9
- `tools/roles/agents/gov-reuse-scout.agent.md`, renders `.claude/agents/gov-reuse-scout.md` and `tools/roles/README.md`: S9
- `tools/roles/workflows.toml`, `help/reuse.md`: S9
- `tools/loop/loop.toml`: S6, S7

### Alternatives rejected

- **TOOL-aScoutedSeam-1's `## reuse` section as the grammar** — lost to the parent rule: a parent's
  `## Matches` and its reader exist in TOOL-dLinkedLibrary-2, and a second heading is a second grammar
  for one return · `memory/builds/dIndexedDesign/build/2026-10-28-build-TOOL-dIndexedDesign-1-reuse-scout-b.md:20`
- **The caps in `house_index.py`, as I10 proposed** — lost to the kit boundary: the grader sits beside
  the one reader in the memory-tree kit, which may not import the codebase-map kit; the index's Return
  step spells the numbers and the hygiene suite holds them equal to the constants · `tools/memory-tree/kit.toml:7`
- **Grading by the presence of `## Needs`** — lost to the vacuous selector: a return omitting the
  section escapes the grader; the kind token selects the population instead · BUILD-METHOD M3's
  counter-rule
- **Demoting past the cap, as aScoutedSeam's harness does** — lost to the clause: "at most five MUSTs"
  is a property of the return, and no harness stands between this scout and its record ·
  `2026-10-11-spec-TOOL-aScoutedSeam-1.md:143`

## 5. Production-readiness checklist

- security — reads tracked records and runs `git cat-file` and `git show` with argv lists at a sha the
  grader validates as hex; the record's text is data, never a command.
- perf / scale — one pass per `seams` record, one batched `cat-file` per record for its paths.
- error / empty / loading states — exit 2 naming an unreadable record or an unresolvable `**Index:**`
  sha; `none` lines; the population line counts `research` records passed over.
- observability — each finding names its record, section and line.
- risks — a scout re-returns when it overruns a cap; the Return step states the caps it is graded on.
- testing — each grader case planted red and its twin green; the parse; the caps' parity with the
  index's Return step.
- migration — none.
- user docs — `help/reuse.md`, TOOL-dLinkedLibrary-2's page, gains the return's sections (S9); check
  31's catalogue entry (S8).

## 6. Acceptance criteria

- **AC1** — When `python -c` calls `tree_lib.read_reuse_scouts` on a scratch build holding one
  conforming `seams` record, it returns each of the eight sections, a MUST match as `binding`, `path`,
  `symbol`, `how`, `duplicates` and `not`, and the record's `**Index:**` sha.
  Red when: a section or a match field is dropped.
- **AC2** — When `python gen_build_index.py --reuse-scouts tFix --check` runs over a record with 13
  matches, it exits 1 naming `MATCH_CAP`; over one with 6 MUSTs, it exits 1 naming `MUST_CAP`; over one
  with 12 matches of which 5 are MUST, it exits 0.
  Red when: either cap is passed, or the record at both caps is a finding.
- **AC3** — When the same command runs over a record whose MUST reads `· duplicates c9` with no `c9`
  sketch line, it exits 1 naming the MUST; over one whose MUST's `<symbol>` is absent from its path at
  the record's `**Index:**` sha, it exits 1 naming the path and symbol; over the conforming record, 0.
  fixture: the scratch build commits the MUST's file and passes that commit as the sha.
  Red when: a MUST that duplicates nothing passes either test.
- **AC4** — When the same command runs over a record whose second MUST has no `## Establishes` row, it
  exits 1 naming `seam-2`; over one with a row of kind `finding`, it exits 1 naming the kind.
  Red when: a match leaves no row, or a row outside the `seam` kind passes.
- **AC5** — When `bash check-memory-hygiene.sh --only 31` runs over a scratch tree holding a `seams`
  record with sections out of order, it fails check 31 naming the record; over this tree at landing it
  passes and prints the count of `research` scout records it passed over.
  Red when: the misordered record passes, or a `research` record is graded.
- **AC6** — When `python -c` loads `record-kinds.toml` with `tomllib`, a `seams` row has tag
  `record.seams` and field `Index`, and `python gen_build_index.py --reuse-scouts dIndexedDesign`
  still prints the four scout records of this build.
  Red when: the row is missing, or a `research` record leaves the reader's list.
- **AC7** — When `python -c` loads `loop.toml` with `tomllib`, no `[[stand-in]]` row names
  `item.design.seams`, that item's `witness` names `--reuse-scouts`, and `item.design.decompose`'s
  `upstream` holds `item.design.seams` at gate `record`.
  Red when: the stand-in survives the witness, or the upstream entry is absent or `measured`.
- **AC8** — When `python house_index.py --out <scratch>/hi.md` runs, its `## Steps` holds a Return step
  naming the eight sections, `12` and `5`, which equal `tree_lib.MATCH_CAP` and `tree_lib.MUST_CAP` read
  by `python -c`; `grep -n "## Needs" gov-reuse-scout.agent.md` finds the `returns:` line, and the body
  after the front matter, CR stripped, is at most 1536 bytes; `grep -n "MUST_CAP" reuse.md` finds the
  help page's section.
  Red when: a number disagrees with its constant, the body overruns its ceiling, or the page is silent.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `build-index selftest` · `kit/dogfood doc parity` · `policy fixtures` · `tier2-review self-test` · `codebase-map kit selftest` · `codebase-map gate coverage` · `codebase-map adopter e2e` · `check-wiring self-test` · `roles catalogue` · `roles render wiring` · `roles render selftest` · `recall floor` · `recall floor arms` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

New arm: tools/memory-tree/check-memory-hygiene.test.sh · covers AC2 AC3 AC4 AC5 · check 31 over scratch builds holding each grader plant and its conforming twin, staged by dropping the MUST's sketch line · none
New arm: tools/codebase-map/selftest.py · covers AC8 · the Return step's caps against the grader's constants, staged by changing one number · none

## 8. Open questions

- **F1 — Where does the return contract live, and which grammar?** Options: (a) widen
  TOOL-dLinkedLibrary-2's record and `## Matches` with TOOL-aScoutedSeam-1's line spelling, the grader
  beside the one reader; (b) adopt TOOL-aScoutedSeam-1's `## reuse` section whole; (c) a new record
  beside the scout's. (b) is not a parent's and puts a second grammar beside a parent's; (c) is a third.
  RESOLVED (agent, 2026-10-28, delegated): (a), rung 3, the most feature-rich survivor and the reuse of
  the parent's reader.
  grants: PLAY-dClosedLoop-3 the scout's return contract and its role body. widens: none · relaxes: none
- **F2 — Does the bar grade the return?** Options: (a) a hygiene check, delegated to the generator as
  check 29 is; (b) the CLI only, as the item's witness; (c) inside TOOL-dIndexedDesign-4's §10 arm. (b)
  leaves the record kind's `check` column naming a leg that grades nothing; (c) grades only a record a
  spec cites. RESOLVED (agent, 2026-10-28, delegated): (a), rung 3, check 31, the number minted here;
  grants: PLAY-dClosedLoop-3 the hygiene gate gains check 31. widens: none · relaxes: none
- **F3 — The third grammar.** TOOL-aScoutedSeam-1 (SPECCED, not an ancestor) would land `## reuse`
  beside this record. Options: (a) an ask in aScoutedSeam's `BACKLOG.md`; (b) an edit of its spec,
  which the brief forbids; (c) nothing. RESOLVED (agent, 2026-10-28, delegated): (a), rung 3. Ask for
  the main loop to file, target build aScoutedSeam: "TOOL-aScoutedSeam-1 S5's `## reuse` section would
  be a third grammar for the scout's return, which TOOL-dIndexedDesign-13 lands as the `seams` record's
  `## Matches` in TOOL-aScoutedSeam-1 §4's line spelling" · accept TOOL-aScoutedSeam-1 S5 re-pointed to
  render from the `seams` record through `read_reuse_scouts`, or retired, before aScoutedSeam builds.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-28 · initial draft, from the packet's Items 13, gap-design-11, night pass two point
  2, M1c's scout schema and checklist, TOOL-aScoutedSeam-1 §4, TOOL-dLinkedLibrary-2 S3, S5 and S6,
  TOOL-dDeclaredLoop-29 S1 to S4, and scout B's row for this unit.
- rev-2 · 2026-10-28 · §3 · the Edges block gains the hands-off bullets mirroring the consumes-from edges of TOOL-dIndexedDesign-33, TOOL-dIndexedDesign-38,
  promoted by the round-1 spec audit of this build; nothing else moved.

## 10. Reuse audit

The seams extended are TOOL-dLinkedLibrary-2's record and its reader `read_reuse_scouts` over
`tree_lib.read_bindings` (`tools/memory-tree/tree_lib.py:471`), its `## Steps` in `house_index.py`, the
record-kind factory (TOOL-dTotalRecall-1 S9), and TOOL-dDeclaredLoop-29's `## Establishes` rows and
`upstream` field; each parent read at its spec, and `read_bindings` verified at `4bf0f400d`. Scout B's
row holds at that commit, with one correction: it cites the role's `returns:` at
`gov-reuse-scout.agent.md:10`, which is right, and `workflows.toml:28` for `enforced-by`, also right.
`python tools/codebase-map/reuse_lookup.py "grade a reuse scout's return sections against caps and parse
them for later readers"` ranked name stems (`read`, `read_text`, `parse`, `parse_conf`,
`resolve_caps`); `resolve_caps` caps size budgets, not a return, so no existing seam fits the grader and
S5 adds it beside the parent's reader.

Recall terms used: `python tools/memory-recall/query.py "what must the reuse scout return under the M1c contract and how are its seams handed on" --terms "reuse scout return M1c needs sketch anchors census MUST SHOULD unmet establishes rows"`
