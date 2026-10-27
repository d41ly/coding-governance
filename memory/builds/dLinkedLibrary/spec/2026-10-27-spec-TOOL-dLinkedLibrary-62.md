# TOOL-dLinkedLibrary-62 — an unresolved reader stays red on a row this repository's own builds own; only rows owned outside read `not installed`

**Status:** OPEN · rev-1 · 2026-10-27 · node d · Tier-2 · base 5fede642 · streams tooling · order 5 · advances TOOL-dLinkedLibrary-26

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dLinkedLibrary-1-agent-ledger.md) | journal | TOOL-dLinkedLibrary-1 TOOL-dLinkedLibrary-2 TOOL-dLinkedLibrary-3 TOOL-dLinkedLibrary-4 TOOL-dLinkedLibrary-5 TOOL-dLinkedLibrary-6 TOOL-dLinkedLibrary-7 TOOL-dLinkedLibrary-8 TOOL-dLinkedLibrary-9 TOOL-dLinkedLibrary-10 TOOL-dLinkedLibrary-11 TOOL-dLinkedLibrary-12 TOOL-dLinkedLibrary-13 TOOL-dLinkedLibrary-14 TOOL-dLinkedLibrary-15 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-17 TOOL-dLinkedLibrary-18 TOOL-dLinkedLibrary-19 TOOL-dLinkedLibrary-20 TOOL-dLinkedLibrary-21 TOOL-dLinkedLibrary-22 TOOL-dLinkedLibrary-23 TOOL-dLinkedLibrary-24 TOOL-dLinkedLibrary-25 TOOL-dLinkedLibrary-37 TOOL-dLinkedLibrary-38 TOOL-dLinkedLibrary-39 TOOL-dLinkedLibrary-40 TOOL-dLinkedLibrary-41 TOOL-dLinkedLibrary-42 TOOL-dLinkedLibrary-43 TOOL-dLinkedLibrary-44 TOOL-dLinkedLibrary-45 TOOL-dLinkedLibrary-46 TOOL-dLinkedLibrary-47 TOOL-dLinkedLibrary-48 TOOL-dLinkedLibrary-49 TOOL-dLinkedLibrary-50 TOOL-dLinkedLibrary-51 TOOL-dLinkedLibrary-52 TOOL-dLinkedLibrary-53 TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-61 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 |
| [2026-10-27-build-TOOL-dLinkedLibrary-54-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-54-promoted-fix-return.md) | research | TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-20 |
| [2026-10-27-build-TOOL-dLinkedLibrary-62-deviation-621.md](../build/2026-10-27-build-TOOL-dLinkedLibrary-62-deviation-621.md) | deviation | — |
| [2026-10-27-prompt-TOOL-dLinkedLibrary-54-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dLinkedLibrary-54-promoted-fix-brief.md) | research | TOOL-dLinkedLibrary-54 TOOL-dLinkedLibrary-55 TOOL-dLinkedLibrary-56 TOOL-dLinkedLibrary-57 TOOL-dLinkedLibrary-58 TOOL-dLinkedLibrary-59 TOOL-dLinkedLibrary-60 TOOL-dLinkedLibrary-63 TOOL-dLinkedLibrary-64 TOOL-dLinkedLibrary-16 TOOL-dLinkedLibrary-20 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of units 37 to 53
(`memory/builds/dLinkedLibrary/reviews/2026-10-27-review-TOOL-dLinkedLibrary-37-spec-audit.md`) confirmed
finding **id 26 at HIGH**, report item **H6**. No other id shares the item.

`TOOL-dLinkedLibrary-48` S1 makes any `reader` that resolves to nothing read `not installed` and exit 0,
in every tree, gov's own included: its verdict table's row `| any | no | any | any | not installed,
announced |` has no owner condition. Its S2 splits rows by owner only for the "appears nowhere"
direction. `TOOL-dLinkedLibrary-12` S1 refuses a `reader` that is not a tracked path and its AC4 expects
exit 1, and spec 48 never amends that criterion. So in gov a reader deleted or renamed, which unit 3
does to files in this very build, prints one announcement line, the unguarded `annotations` leg stays
green, and the registry certifies readers that no longer exist.

This unit applies 48's owned-row rule to the reader too: for a row whose `owner` names a unit of a build
this repository's memory root holds, an unresolved reader is red as unit 12 S1 says; only a row owned
outside the repository reads `not installed`. It repairs `TOOL-dLinkedLibrary-48` and builds one step
after it (order 5).

## 2. Scope (IN)

- **S1** — One ownership test. `annotations.py` derives a row's ownership once, `owned` when its `owner`
  names a unit of a build whose folder `<memory root>/builds/<slug>/` this repository holds, and both
  `TOOL-dLinkedLibrary-48`'s S1 and S2 read that one result. Observed by AC1 and AC2.
- **S2** — The owned row's reader. Where a row is `owned` and its `reader`, neither `none` nor resolved
  through the install by 48's S1, resolves to nothing, `check --only markers` exits 1 naming the row and
  the reader, `TOOL-dLinkedLibrary-12` S1's refusal; no `not installed` line is printed for it. Observed
  by AC1.
- **S3** — The row owned outside. Where a row is not `owned`, an unresolved reader reads `not installed`
  and is announced as 48's S4 states, exit 0. Observed by AC2.
- **S4** — The verdict table. The row of 48's §4 table `| any | no | any | any | not installed, announced
  |` is read, from this unit on, as two rows: owned and unresolved, red; owned outside and unresolved,
  `not installed`. The table in `tools/memory-tree/README.md`'s registry paragraph, which 48's §5 adds,
  states the two. Observed by AC3.

## 3. Non-goals (OUT)

- The resolution itself through `resolve_kit_dir`: `TOOL-dLinkedLibrary-48` S1, unchanged.
- The "appears nowhere" and "unregistered" directions: 48's S2 and S3, unchanged.
- The registry's rows and their owners: `TOOL-dLinkedLibrary-12`'s and the units that add rows.

### Edges

- **consumes-from** `TOOL-dLinkedLibrary-48` — S1's `not installed` reading and S2's owned-row split, which this unit's S1 joins and S2 narrows (id 26)
- **consumes-from** `TOOL-dLinkedLibrary-12` — S1's refusal of a reader that is not a tracked path and its AC4, which S2 keeps live for owned rows (id 26)

## 4. Design

### Evidence

- `TOOL-dLinkedLibrary-48` §4 "The verdicts after S1 and S2": the `not installed` row carries `any` in the
  owner column.
- `TOOL-dLinkedLibrary-12` S1 (its spec :36-41) and AC4 (:197-199): an untracked reader exits 1 naming the
  row.
- `TOOL-dLinkedLibrary-48` S2: "owned" is a row whose `owner` names a unit of a build whose folder this
  repository's memory root holds.

### The verdicts after S2 and S3

| Row owned here | Reader resolves | Verdict |
|---|---|---|
| yes | yes | graded as 48 states |
| yes | no | red: the reader names nothing, unit 12 S1 |
| no | yes | graded as 48 states |
| no | no | `not installed`, announced |

### Files touched (estimate)

- `tools/memory-tree/annotations.py`: S1 to S3, and the `owned-reader-gone` and `owned-outside-reader-gone`
  selftest cases
- `tools/memory-tree/README.md`: S4's two rows

### Alternatives rejected

- **A standing arm in gov that greps every reader path.** It duplicates the check S2 makes live, and a
  second reader of one registry can disagree with the first.
- **`not installed` kept everywhere, with 48's AC1 run at every pass.** AC1 is a one-time observation;
  a criterion is not a gate.

## 5. Production-readiness checklist

- security — read-only.
- perf / scale — one ownership test per row, already computed for 48's S2.
- error / empty / loading states — an owned row's missing reader exits 1 naming both; an adopter's rows
  owned outside keep their announcement.
- observability — the refusal names the row's word, its reader and its owner.
- risks — a gov unit that deletes a reader must edit its row in the same pass; the leg tells it so.
- testing — AC1 and AC2 by the module's `--selftest` scratch tree, unit 12's harness, since the
  `--fixture --plant` flags are minted by `TOOL-dLinkedLibrary-4` at order 12.
- migration — none.
- user docs — none under `help/`: `tools/memory-tree/README.md`, S4.

## 6. Acceptance criteria

- **AC1** — When `python annotations.py --selftest` runs, its `owned-reader-gone` case,
  `check --only markers` over the selftest's scratch tree with a registry row owned by a unit of a build
  that tree's memory root holds and its `reader` file deleted, sees exit 1 naming the row and the reader
  and no `not installed` line for it, and the selftest prints the case `ok`.
  Red when: an owned row's missing reader reads `not installed`.
- **AC2** — When the same `--selftest` run reaches the `owned-outside-reader-gone` case, the same row
  owned by `TOOL-dElsewhere-1`, the check exits 0 printing `not installed` for it; and
  `TOOL-dLinkedLibrary-48`'s `adopter-memory-tree-only` case, wherever that unit's pass hosts it, stays
  green.
  Red when: the adopter envelope reds on a reader its install never received.
- **AC3** — When `grep -n "not installed" tools/memory-tree/README.md` runs, it prints the two rows of S4.
  Red when: the README states `not installed` with no owner condition.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/annotations.py · covers AC1 AC2 · the `owned-reader-gone` and `owned-outside-reader-gone` selftest cases, the failing case staged by 48's rev-1 `not installed` for every row · none

## 8. Open questions

- **F1 — Which binding line does a unit the spec audit promoted carry?** Options: (a) `**Derived:**`
  naming `PLAY-dClosedLoop-2`; (b) a `part k/n` carry of the repaired unit's clause. (b) splits a clause
  unit 12 carries whole; veto 1 discards it. RESOLVED (agent, 2026-10-27, delegated): (a), rung 3, the
  precedent `TOOL-dTotalRecall-40` set for this chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-27 · initial draft, promoted from the spec audit of units 37 to 53, id 26 (HIGH, item
  H6).

## 10. Reuse audit

The seam extended is `TOOL-dLinkedLibrary-48`'s owned-row test in `tools/memory-tree/annotations.py`,
derived once and read by both directions, and its reader resolution through `resolve_kit_dir`
(`tools/memory-tree/backlog.py:1758`). `python tools/codebase-map/reuse_lookup.py "resolve a marker word
reader through the install receipt"` ranked `read`, `read_text`, `resolve` and `resolve_kit_dir`; the
last is the resolution 48 already calls, and none tests a row's owner, so no existing seam fits beyond
the check being narrowed.

Recall terms used: `python tools/memory-recall/query.py "how does a promoted high finding repair a spec-audited unit at the next order step" --terms "spec-audit promoted high finding repairs order inline parity block tree-kill witness before-image"`
