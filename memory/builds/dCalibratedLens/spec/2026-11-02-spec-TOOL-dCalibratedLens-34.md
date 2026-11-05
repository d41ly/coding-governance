# TOOL-dCalibratedLens-34 — the bug class of a staged break whose red rests on an ancestor clause a newer revision replaced, recorded so a spec review is handed it

**Status:** DEFERRED · rev-2 · 2026-11-03 · node a · Tier-2 · base 8bec4cef · streams tooling · order 4 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dCalibratedLens-34-deviation-341.md](../build/2026-11-02-build-TOOL-dCalibratedLens-34-deviation-341.md) | deviation | — |
| [2026-11-03-build-TOOL-dCalibratedLens-1-agent-ledger.md](../build/2026-11-03-build-TOOL-dCalibratedLens-1-agent-ledger.md) | journal | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-12 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-22 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-29 TOOL-dCalibratedLens-30 TOOL-dCalibratedLens-31 TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-38 TOOL-dCalibratedLens-39 TOOL-dCalibratedLens-40 TOOL-dCalibratedLens-41 TOOL-dCalibratedLens-42 TOOL-dCalibratedLens-43 TOOL-dCalibratedLens-44 TOOL-dCalibratedLens-45 TOOL-dCalibratedLens-46 TOOL-dCalibratedLens-47 TOOL-dCalibratedLens-48 |
| [2026-11-02-prompt-TOOL-dCalibratedLens-31-promoted-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-31-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-31 TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-38 TOOL-dCalibratedLens-39 TOOL-dCalibratedLens-40 TOOL-dCalibratedLens-41 |
| [2026-11-03-prompt-TOOL-dCalibratedLens-1-ancestors-crosscheck.md](../prompts/2026-11-03-prompt-TOOL-dCalibratedLens-1-ancestors-crosscheck.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-42 TOOL-dCalibratedLens-48 |
| [2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md](../reviews/2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit.md) | spec-audit | TOOL-dCalibratedLens-32 TOOL-dCalibratedLens-33 TOOL-dCalibratedLens-35 TOOL-dCalibratedLens-40 TOOL-dCalibratedLens-39 TOOL-dCalibratedLens-38 TOOL-dCalibratedLens-31 TOOL-dCalibratedLens-37 TOOL-dCalibratedLens-36 TOOL-dCalibratedLens-41 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 11, HIGH, of the round-2 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md`). The report merges ids 2, 11 and
26 into its item H1; ids 2 and 26 are `TOOL-dCalibratedLens-33` and `TOOL-dCalibratedLens-32`. Unit
19 §1 rested its staged break on TOOL-dTotalRecall-1 S4, which grades every record under a home by
that home's row, while TOOL-dTotalRecall-42 S5 had already replaced that reading with grading by the
Serves kind; unit 20 at the same order rests on the newer one. The break expected a red the newest
ancestor revision cannot give. The finding's left-shift line asks for a spec-audit checklist entry:
every staged break names the ancestor clause that makes it red, read at its newest revision. This
unit re-grounds unit 19 on that rule and records the variant in the bug-class catalogue every review
checklist is drawn from, in the record whose rule already covers it,
`memory/gotchas/spec-names-code-its-base-lacks.md`, which it also delivers to spec reviews. It
repairs `TOOL-dCalibratedLens-19`.

## 2. Scope (IN)

- **S1** — The design change, made at the audit's disposal in unit 19's text (rev-2, id 11): §1 rests
  on TOOL-dTotalRecall-42 S4 and S5, named at their revision, and every staged break unit 19 keeps
  names the ancestor clause that makes it red. Observed by AC1.
- **S2** — The class record `memory/gotchas/spec-names-code-its-base-lacks.md` gains the
  ancestor-clause variant (round-3 id 18). Its "Where it bit" section gains the
  TOOL-dCalibratedLens-19 instance: a staged break resting on TOOL-dTotalRecall-1 S4 after
  TOOL-dTotalRecall-42 S5 had moved the grading to the Serves kind. Its check gains the variant: a
  staged break, or a criterion's `Red when:`, names the clause of the code or the ancestor spec that
  produces the red, read at the newest revision the build's base holds, and a spec citing an
  ancestor clause checks that no later unit of that ancestor build moved it. Its delivery section
  gains the anchors `/spec/` and `memory/TEMPLATE-SPEC.md`, backticked, so `gotchas.py --for-paths`
  hands the record to every review of a spec, and says this answers the delivery gap the section
  records. Its gate line stays a documented check with no machine gate. Observed by AC1 and AC2.
- **S3** — The catalogue's `memory/gotchas/INDEX.md`, regenerated by
  `python tools/memory-tree/gotchas.py --write` in the same commit; and the codebase map held fresh,
  `python tools/codebase-map/gen_map.py --check` read after the pass and `--write` run in the same
  commit only where it names drift (round-3 id 24). No class key is minted, so no feature card gains
  a claim: `memory/map/features/unattended.md` already claims the record. Observed by AC3 and AC4.

## 3. Non-goals (OUT)

- A machine gate. Deciding that a cited clause was replaced needs a join from a spec citation to
  every later unit of the cited build that amends it; nothing in the tree builds one, and the record
  says so.
- A new class record, the rev-1 design. The existing record's rule ("A record is evidence about a
  moment. When you write from one, date it against the tree you are changing") already covers a
  spec citing an ancestor clause a later revision moved; a second record would hold one rule twice
  (round-3 id 18).
- The restaged red twin and the disjointness case: `TOOL-dCalibratedLens-32` and
  `TOOL-dCalibratedLens-33`.
- A universal record. The class reaches a review through its `/spec/` anchor, so it does not take a
  place in the universal budget.

### Edges

none

## 4. Design

### Evidence

- Unit 19 §1 at rev-1: "TOOL-dTotalRecall-1 S4 grades every tracked record under a row's home against
  that row's fields".
- TOOL-dTotalRecall-42 S5 (`memory/builds/dTotalRecall/spec/2026-10-26-spec-TOOL-dTotalRecall-42.md:53-58`)
  and its line "deciding by the Serves kind needs no disjoint homes".
- `memory/gotchas/spec-names-code-its-base-lacks.md` at base: its rule generalises past code to any
  record written from an older moment, it already holds a non-code variant (files on an unmerged
  branch), and its section "How this one is delivered" says a diff touching specs never selects it,
  because its only backticked path is a shell library.
- `tools/memory-tree/gotchas.py:261-269`: a record declares its resolution by naming a gate or by the
  words "no machine gate" or "documented check" in its body; `:278-282` derive its anchors from its
  backticked paths.
- `memory/gotchas/observed-by-claim-no-arm-discharges.md` anchors on `/spec/` and
  `memory/TEMPLATE-SPEC.md`, and `gotchas.py --for-paths` over a spec of this build selects it by
  directory (probed at base, 2026-11-02).
- `tools/codebase-map/map_extractors.py:220-225`: the `gotcha-classes` inventory is the record file
  names under `memory/gotchas/`, `INDEX.md` excluded, so extending a record mints no key;
  `memory/map/features/unattended.md:24` claims this record (round-3 id 24).

### Inventory

No identifier is minted.

### Files touched (estimate)

- `memory/gotchas/spec-names-code-its-base-lacks.md` — S2
- `memory/gotchas/INDEX.md` — S3, generated
- `memory/map/generated/` — S3, re-rendered only where `gen_map.py --check` names drift

### Alternatives rejected

- **Mint `staged-break-expects-a-red-its-ancestor-superseded`, the rev-1 design.** One rule in two
  records: a reviewer handed one is not handed the other's history, and the older record stays
  undelivered to spec diffs (round-3 id 18).
- **Widen `staged-break-substitutes-a-synthetic-value`.** That class mutates the wrong value; this
  one cites the wrong rule. A reviewer handed one learns nothing about the other.
- **A checklist line in the review harness's lens briefs.** The catalogue is already the one source
  the bug-class checklist is drawn from; a second list would be one fact in two places.

## 5. Production-readiness checklist

- security — N/A: a catalogue record.
- perf / scale — one more class on a spec review's checklist, from its new anchors.
- error / empty / loading states — N/A.
- observability — the class prints on `gotchas.py --for-paths` over any spec.
- risks — checklist length: the class is anchored, not universal, so it is selected only for spec
  paths and the shell library it already names.
- testing — AC1 to AC4 by the pass.
- migration — N/A.
- user docs — N/A: the catalogue is its own documentation.

## 6. Acceptance criteria

- **AC1** — When `python tools/memory-tree/gotchas.py --for-paths` runs over unit 19's spec file
  after this unit's pass, its checklist lists `spec-names-code-its-base-lacks`; at base it does not.
  Red when: the record derives no anchor that reaches a spec path.
- **AC2** — When `python tools/memory-tree/gotchas.py --declares` reads the extended record on
  stdin, it prints `declares: yes`, and `grep -n "TOOL-dCalibratedLens-19"` over the record names the
  new instance.
  Red when: the record neither names a gate nor says it has none, or the instance is absent.
- **AC3** — When `git diff --name-only HEAD~1 HEAD` runs on this unit's commit, it lists both
  `spec-names-code-its-base-lacks.md` and `INDEX.md` under the catalogue.
  Red when: the index was not regenerated with the record.
- **AC4** — When `python tools/codebase-map/gen_map.py --check` runs after the pass, it exits 0.
  Red when: the pass leaves the map stale (round-3 id 24).

## 7. Gates

`gotchas selftest` · `recall floor` · `recall floor arms` · `codebase-map coverage + freshness` · `memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, promoted from id 11 (HIGH, item H1, shared with ids 2 and 26) of
  the round-2 spec audit `2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit`; unit 19 amended at
  the disposal (its rev-2).
- rev-2 · 2026-11-03 · §1 §3 §4 §5 §7 §10 S2 S3 AC1 AC2 AC3 AC4 · amended at the disposal of the
  round-3 spec audit `2026-11-03-review-TOOL-dCalibratedLens-31-spec-audit`, from
  `TOOL-dCalibratedLens-48`: S2 extends `spec-names-code-its-base-lacks.md` rather than minting a
  class (id 18); S3, the Files touched, §7 and AC4 carry the codebase map's freshness (id 24); §10
  records this unit's own probe phrase (id 21).

## 10. Reuse audit

The seam extended is the existing record `memory/gotchas/spec-names-code-its-base-lacks.md` in the
bug-class catalogue under `memory/gotchas/`, rendered by `tools/memory-tree/gotchas.py`, the source
the review checklist is drawn from. `python tools/codebase-map/reuse_lookup.py "a bug class for a
spec citing a superseded rule"` ranked name stems only (`read_spec_revisions` in
`tools/memory-tree/design_lib.py`, `parse_spec_h1`, `build_spec_path_re`); none is a catalogue
record, and the catalogue was read by hand, where the round-3 audit's id 18 named the record whose
rule covers the variant.

Recall terms used: `python tools/memory-recall/query.py "how is a staged break that an ancestor
clause cannot make red repaired, and how is a spec audit finding promoted to a repair unit" --terms
"staged break ancestor clause superseded red twin spec audit promoted repair unit order shape line
renderer"`
