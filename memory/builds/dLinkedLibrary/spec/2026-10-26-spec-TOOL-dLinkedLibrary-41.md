# TOOL-dLinkedLibrary-41 — the span arm reads `iter_family` on its own conventions: a top-level pair at depth 1, a lead that carries its space

**Status:** OPEN · rev-1 · 2026-10-26 · node d · Tier-2 · base 5fede642 · streams tooling · order 14 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 TOOL-dLinkedLibrary-75 TOOL-dLinkedLibrary-76 TOOL-dLinkedLibrary-77 TOOL-dLinkedLibrary-78 TOOL-dLinkedLibrary-79 TOOL-dLinkedLibrary-80 TOOL-dLinkedLibrary-81 TOOL-dLinkedLibrary-82 TOOL-dLinkedLibrary-83 TOOL-dLinkedLibrary-84 TOOL-dLinkedLibrary-85 TOOL-dLinkedLibrary-86 TOOL-dLinkedLibrary-87 TOOL-dLinkedLibrary-88 TOOL-dLinkedLibrary-89 TOOL-dLinkedLibrary-90 TOOL-dLinkedLibrary-91 TOOL-dLinkedLibrary-92 TOOL-dLinkedLibrary-93 TOOL-dLinkedLibrary-94 TOOL-dLinkedLibrary-95 TOOL-dLinkedLibrary-96 TOOL-dLinkedLibrary-97 TOOL-dLinkedLibrary-98 TOOL-dLinkedLibrary-99 TOOL-dLinkedLibrary-100 TOOL-dLinkedLibrary-101 TOOL-dLinkedLibrary-102 |
| [2026-10-26-build-TOOL-dLinkedLibrary-41-deviation-411.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-41-deviation-411.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 25 unit specs
(`memory/builds/dLinkedLibrary/reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md`) confirmed
finding **id 4 at HIGH**, report item **R5**. No other id shares the item.

`TOOL-dLinkedLibrary-18` numbers a top-level span depth 1: its AC2 returns nested `b` at depth 2.
`TOOL-dLinkedLibrary-17` S5 and §4 "The pairing walk" refuse a span at depth 1 or more as `nested` and
read a well-formed pair as depth 0. And unit 18's family grammar puts the name directly after the lead,
while unit 17 passes the leads `"gov:note"` and `"gov:end"` over lines that carry a space before the
tag. Built as written, the span arm either refuses every well-formed `gov:note`…`gov:end` pair as
`nested`, or recognises no marker and passes every malformed pairing, a check that certifies what it
does not check.

This unit pins the factory's depth origin with a case of its own and makes the span arm read both
conventions as the factory defines them. It repairs `TOOL-dLinkedLibrary-17` and builds one step after
it (order 14).

## 2. Scope (IN)

- **S1** — The origin, pinned. A family case in `tools/memory-tree/marker-contract.test.sh`
  (`TOOL-dLinkedLibrary-18` S8's family cases) asserts that `iter_family` returns a lone top-level pair as
  one span at depth 1, beside the nested case's depth 2. Observed by AC1.
- **S2** — The depth rule. `check_note_spans` (`tools/memory-tree/annotations.py`,
  `TOOL-dLinkedLibrary-17` S5) refuses as `nested` a span `iter_family` returns at depth 2 or more; a span
  at depth 1 is a well-formed pair whose body `read_region` reads. Observed by AC2.
- **S3** — The leads. The span arm calls `iter_family(text, [("gov:note ", "gov:end ", None)])`, each lead
  carrying its trailing space, so the tag follows the lead as the factory's name grammar requires; the
  pairing text keeps each line in the form `gov:note <first tag>` or `gov:end <tag>`. Observed by AC3.
- **S4** — `TOOL-dLinkedLibrary-17`'s acceptance ledger answers its AC5 citing this unit wherever its pass
  met the depth or lead mismatch, and the table of its §4 "The pairing walk" is read with depth 1 for a
  pair and 2 for a pair inside a pair. Observed by AC4.

## 3. Non-goals (OUT)

- Changing `iter_family`'s depth origin or name grammar: the factory is built (order 2) and other
  readers depend on both as `TOOL-dLinkedLibrary-18` lands them.
- The span rule itself, its verdict words and the definition-derived spans: `TOOL-dLinkedLibrary-17`'s.
- The report's left-shift gate, a shared-interface table in the spec brief: a brief is a record of the
  spec stage, not a unit's write.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-17` — `check_note_spans` and its `span-*` plants, whose depth rule S2 and leads S3 correct (id 4)
- **consumes-from** `TOOL-dLinkedLibrary-18` — `iter_family`, its depth origin and name grammar, which S1 pins with a family case (id 4)

## 4. Design

### Evidence

- `TOOL-dLinkedLibrary-18` S2: a family marker is "a lead followed by a name `[A-Za-z0-9_.-]+` and an
  optional space-led tail"; its AC2 returns `b` at depth 2 inside `a`, so `a`, the top-level span, is
  depth 1.
- `TOOL-dLinkedLibrary-17` S5 calls `iter_family(text, [("gov:note", "gov:end", None)])` and refuses "a
  span the walk returns at depth 1 or more"; its §4 table reads a pair "at depth 0".
- `TOOL-dLinkedLibrary-4` §4 "The line" spells `# gov:note feature.roles — …` and `# gov:end
  feature.roles`: one space between the word and the tag, and `feature.roles` fits the name grammar.

### The walk after S2 and S3

| In the pairing text | `iter_family` says | Span verdict |
|---|---|---|
| `gov:note feature.a …` then `gov:end feature.a` | one span, depth 1 | none |
| a pair inside that pair | the inner span, depth 2 | `nested` |
| `gov:note feature.a …` with no close | unclosed open | `unterminated` |

### Files touched (estimate)

- `tools/memory-tree/annotations.py`: S2, S3
- `tools/memory-tree/marker-contract.test.sh`: S1's family case

### Alternatives rejected

- **A depth-0 origin in the factory.** Unit 18 is built at order 2 with depth 1 and other family readers
  read it; moving the origin at order 14 changes their verdicts for one consumer's convenience.
- **The factory's grammar widened to admit one space after the lead.** It changes every family's
  recognition, the gen family's included, where a space after the lead is today a malformed marker.

## 5. Production-readiness checklist

- security — read-only arm.
- perf / scale — unchanged.
- error / empty / loading states — unchanged: an arm with no span prints its `unarmed` line.
- observability — each verdict still names its line.
- risks — none beyond the arm's own.
- testing — the `span-*` plants and S1's family case.
- migration — none.
- user docs — none: `help/annotations.md`'s span section states the verdicts, not the depth numbering.

## 6. Acceptance criteria

- **AC1** — When `python -c` imports `region` from `tools/lib` and calls `iter_family` over one
  `<!-- gen:a -->`/`<!-- /gen:a -->` pair, it returns one span at depth 1, and
  `grep -n "lone top-level" tools/memory-tree/marker-contract.test.sh` prints the family case asserting it.
  Red when: a top-level span reads depth 0, or no case pins the origin.
- **AC2** — When `python annotations.py --fixture --plant span-end` runs `check --only span`, it exits 0;
  `--plant span-nested` exits 1 naming `nested` at the inner `gov:note` line.
  Red when: a well-formed pair is refused as `nested`, or a nested pair passes.
- **AC3** — When `--plant span-unterminated` and `--plant span-orphan` run, each exits 1 naming
  `unterminated` or `orphan`; with the leads staged back to `"gov:note"` and `"gov:end"`, both exit 0.
  Red when: the arm recognises no marker and passes a malformed pairing.
- **AC4** — When `grep -n "AC5" <unit 17's acceptance ledger>` runs, the answer names
  `TOOL-dLinkedLibrary-41` wherever that pass met the mismatch.
  Red when: unit 17's ledger certifies a verdict the depth or lead mismatch produced.
  fixture: unit 17's acceptance ledger under `memory/builds/dLinkedLibrary/build/`.

## 7. Gates

`marker contracts` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/marker-contract.test.sh · covers AC1 · the lone top-level family pair at depth 1, the failing case a factory returning depth 0 · none
New arm: tools/memory-tree/annotations.py · covers AC2 AC3 · the `span-end`, `span-nested`, `span-unterminated` and `span-orphan` plants, the failing case staged by the leads without their space · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 17 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of the 25 unit specs, id 4
  (HIGH, item R5).

## 10. Reuse audit

The seams extended are `TOOL-dLinkedLibrary-18`'s `iter_family` and the marker-contract suite's family
cases, which S1 pins rather than re-deriving, and `TOOL-dLinkedLibrary-17`'s `check_note_spans`, whose
call S3 corrects. `python tools/codebase-map/reuse_lookup.py "census of region parsers outside a
factory"` ranked `parse`, `parse_args`, `census` and `parse_conf`, none a family walk, so no existing
seam fits beyond the factory being consumed.

Recall terms used: `python tools/memory-recall/query.py "how is a promoted spec-audit finding repaired by a unit placed after the unit it repairs" --terms "spec-audit promoted finding repairs order rescope add batch minors disjoint write set"`
