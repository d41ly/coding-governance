# TOOL-dLinkedLibrary-39 — the anchor arm reds an accepted entry with no anchor line and lists a proposed one without red

**Status:** OPEN · rev-2 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 13 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-62 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-65 TOOL-dLinkedLibrary-66 TOOL-dLinkedLibrary-67 TOOL-dLinkedLibrary-68 TOOL-dLinkedLibrary-69 TOOL-dLinkedLibrary-70 TOOL-dLinkedLibrary-71 TOOL-dLinkedLibrary-72 TOOL-dLinkedLibrary-73 TOOL-dLinkedLibrary-74 |
| [2026-10-26-build-TOOL-dLinkedLibrary-39-deviation-391.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-39-deviation-391.md) | deviation | — |
| [2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md](../reviews/2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md) | spec-audit | TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of the 25 unit specs
(`memory/builds/dLinkedLibrary/reviews/2026-10-26-review-TOOL-dLinkedLibrary-1-spec-audit.md`) confirmed
finding **id 2 at HIGH**, report item **R3**. No other id shares the item.

`TOOL-dLinkedLibrary-4` S8 reds every `accepted` or `proposed` reuse entry whose `anchors` string no
line in the tree carries. `TOOL-dLinkedLibrary-19` (order 10) files 82 proposals, each with the anchor
`gov:feature <feature>`, and no unit writes a `gov:feature` line into code. So `TOOL-dLinkedLibrary-4`
AC11 cannot pass, and once `TOOL-dLinkedLibrary-7` lands the unguarded `annotations` leg every bar is
red until someone weakens the arm or writes 32 unscoped anchors.

A proposal is not yet an instruction (`TOOL-dLinkedLibrary-1` S3: only an accepted part renders into
work orders). This unit grades the entry-to-anchor direction on accepted entries only and lists each
proposed entry whose anchor no line carries, so the owner sees it before accepting. It repairs
`TOOL-dLinkedLibrary-4` and builds one step after it (order 13).

## 2. Scope (IN)

- **S1** — The entry direction. In `check_feature_anchors` (`tools/memory-tree/annotations.py`,
  `TOOL-dLinkedLibrary-4` S8), an `accepted` entry whose `anchors` string no line in the tree carries is
  red, as before. A `proposed` entry in that state prints `annotations: feature: <path>:0 · proposed
  <entry tag> · anchor gov:feature <name> not yet in the tree` and does not red. A `rejected` entry is
  not graded in this direction. Observed by AC1 and AC2.
- **S2** — The anchor direction, unchanged: every `gov:feature <tag>` line is named by an entry in any
  state (LR-6), a second line for one name reds, and an anchor in an unprofiled file reds. Observed by
  AC1.
- **S3** — The summary line counts the listed proposals:
  `annotations: feature: <n> rows · <k> findings · <p> proposed awaiting an anchor`, so a run over 82
  unanchored proposals reads as 82 waiting, never as a green count over them. Observed by AC2 and AC3.
- **S4** — The proposal listing. `reuse_entries.py`'s `proposed` listing (`TOOL-dLinkedLibrary-1` S3), the
  one the owner reads before `accept`, names under each proposal whose anchor no line carries
  `anchor not in the tree — accepting it reds the annotations leg until the line is written`.
  Observed by AC4.
- **S5** — The page. `help/annotations.md` (`TOOL-dLinkedLibrary-4` S12) says the entry-to-anchor
  direction binds an accepted entry and lists a proposed one. Observed by AC5.

## 3. Non-goals (OUT)

- Writing `gov:feature` lines for the 32 features: placing an anchor is the owner's act with the
  acceptance, and choosing a file per feature is a judgement no derivation makes.
- Proposing without `--anchor`: `TOOL-dLinkedLibrary-1` S1 requires the six `reuse` facts, `anchors`
  among them.
- The `notes` and `every-comment-ref` populations of the resolve arm: `TOOL-dLinkedLibrary-44`'s.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-4` — `check_feature_anchors` and its summary line, whose entry-to-anchor direction S1 narrows to accepted entries (id 2)
- **consumes-from** `TOOL-dLinkedLibrary-19` — the 82 proposals `dossier_move.py apply` files, each anchored `gov:feature <feature>`, the population AC3 runs over (id 2)
- **hands-off** `TOOL-dLinkedLibrary-64` — AC4's observation, which unit 64 re-points onto `accept` (ids 6, 20 of the spec audit of units 37 to 53)

## 4. Design

### Evidence

- `TOOL-dLinkedLibrary-4` S8 joins entries in any state for the anchor direction (LR-6) and
  `accepted` or `proposed` ones for the entry direction; its AC11 runs `check --only feature` over the
  tree after its pass.
- `TOOL-dLinkedLibrary-19` S3 proposes with `--anchor "gov:feature <feature>"`, and its §3 writes no
  anchor line.
- At base `git grep -n -E "gov:feature\b" -- tools skills .githooks` returns no line
  (`TOOL-dLinkedLibrary-4` §4 Evidence).

### The two directions after S1

| Entry state | Anchor line carrying its `anchors` | Verdict |
|---|---|---|
| `accepted` | none | red |
| `proposed` | none | listed, counted, not red |
| `rejected` | any | not graded |
| any | a `gov:feature` line no entry names | red (S2) |

### Files touched (estimate)

- `tools/memory-tree/annotations.py`: S1 to S3, and the plants of §6
- `tools/memory-tree/reuse_entries.py`: S4
- `help/annotations.md`: S5

### Alternatives rejected

- **Each dossier's anchor written by this unit or by unit 19.** A feature spans many files, and which
  one carries its single anchor is a judgement with no rule to derive it; 32 such lines would be
  anchors nobody chose.
- **Proposed entries graded and the arm left off the leg.** It turns the both-ways join off for every
  accepted entry too.

## 5. Production-readiness checklist

- security — read-only, as `TOOL-dLinkedLibrary-4` §5.
- perf / scale — the same join; one more state test per entry.
- error / empty / loading states — with no anchor and no entry the arm still prints `unarmed`.
- observability — every waiting proposal prints a line, and the summary counts them.
- risks — a proposal accepted with no anchor reds the leg; S4 says so before `accept`.
- testing — the plants of §6 under `annotations.py --selftest`.
- migration — none.
- user docs — `help/annotations.md`, S5.

## 6. Acceptance criteria

- **AC1** — When `python annotations.py --fixture --plant proposed-unanchored` runs
  `check --only feature` over a tree holding one proposed entry and no anchor line, it exits 0 printing
  the `proposed … not yet in the tree` line; `--plant accepted-unanchored`, the same entry accepted,
  exits 1 naming it.
  Red when: a proposal reds the arm, or an accepted entry with no anchor passes.
- **AC2** — When the plant `proposed-unanchored` runs, its summary line reads
  `0 findings · 1 proposed awaiting an anchor`.
  Red when: the waiting proposal is not counted.
- **AC3** — When `python annotations.py check --only feature` runs at this pass's tip, after
  `TOOL-dLinkedLibrary-19`'s proposals, it exits 0 and its summary counts every live proposal with no
  anchor line.
  Red when: an unanchored proposal reds the tree, or the count reads 0 over proposals that exist.
  figure: DERIVED at the pass from `read_reuse_entries`; 82 seam lines at `5fede642`.
- **AC4** — When `python reuse_entries.py proposed` runs over the plant `proposed-unanchored`, the
  proposal's block names `anchor not in the tree`.
  Red when: the owner's listing hides the missing anchor.
- **AC5** — When `grep -n "proposed" annotations.md` runs over the help page, it finds the sentence on the
  entry-to-anchor direction.
  Red when: the page says a proposed entry needs its anchor line.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/annotations.py · covers AC1 AC2 AC4 · the `proposed-unanchored` and `accepted-unanchored` plants, the failing case staged by grading `proposed` entries in the entry direction · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 4 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none
- **F2 — How does the arm meet 82 unanchored proposals?** Options: (a) grade accepted entries only,
  listing proposed ones; (b) propose without an anchor; (c) write each feature's anchor. (b) fails
  `TOOL-dLinkedLibrary-1` S1's six required facts (veto 1); (c) writes 32 lines no rule places (veto 3, an
  unpriced write over product code). RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the one
  survivor. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit of the 25 unit specs, id 2
  (HIGH, item R3).
- rev-2 · 2026-10-27 · §3 · the Edges block gains the bullets mirroring TOOL-dLinkedLibrary-64, promoted from the spec audit of units 37 to 53; nothing else moved.

## 10. Reuse audit

The seam extended is `TOOL-dLinkedLibrary-4`'s `check_feature_anchors` over `compute_coverage`
(`coverage_join.py`, PLAY-dOrderedCharter-19 S9), which already reads each entry's state through
`read_reuse_entries`; S1 adds a state test, not a second join. `python
tools/codebase-map/reuse_lookup.py "count the parts of a feature's reuse entries"` ranked `counts` and
`measure_typed_counts`, neither a join over entry states, so no existing seam fits beyond the arm being
repaired.

Recall terms used: `python tools/memory-recall/query.py "how is a promoted spec-audit finding repaired by a unit placed after the unit it repairs" --terms "spec-audit promoted finding repairs order rescope add batch minors disjoint write set"`
