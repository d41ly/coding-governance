# TOOL-dRankedPlan-28 — the `triage` and `dupes` record kinds join the binding reader, the factory table and the HYGIENE kind list

**Status:** DEFERRED · rev-2 · 2026-10-27 · node a · Tier-2 · base 0689e7fa · streams tooling · order 11 · advances TOOL-dRankedPlan-17

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-TOOL-dRankedPlan-28-deviation-281.md](../build/2026-10-26-build-TOOL-dRankedPlan-28-deviation-281.md) | deviation | — |
| [2026-10-27-build-TOOL-dRankedPlan-19-promoted-fix-return.md](../build/2026-10-27-build-TOOL-dRankedPlan-19-promoted-fix-return.md) | research | TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-29 |
| [2026-10-27-prompt-TOOL-dRankedPlan-19-promoted-fix-brief.md](../prompts/2026-10-27-prompt-TOOL-dRankedPlan-19-promoted-fix-brief.md) | research | TOOL-dRankedPlan-19 TOOL-dRankedPlan-20 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-23 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-29 |
| [2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md](../reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md) | spec-audit | TOOL-dRankedPlan-27 TOOL-dRankedPlan-24 TOOL-dRankedPlan-25 TOOL-dRankedPlan-26 TOOL-dRankedPlan-21 TOOL-dRankedPlan-22 TOOL-dRankedPlan-20 TOOL-dRankedPlan-19 TOOL-dRankedPlan-23 TOOL-dRankedPlan-29 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build
(`memory/builds/dRankedPlan/reviews/2026-10-26-review-TOOL-dRankedPlan-1-spec-audit.md`) confirmed
**finding 28 at HIGH**, item **H6**. `TOOL-dRankedPlan-3` S5 and S7 mint the record kinds `triage` and
`dupes`, served `**Serves:** triage <id>` and `**Serves:** dupes <id>`, and register them only as rows
of `tools/memory-tree/record-kinds.toml` through `record_kinds.py new`. The binding reader reads any
first token outside its closed tuple as malformed (`tools/memory-tree/tree_lib.py:406`, `:544-565`),
the record factory refuses at import when its kind table and `TYPED_RECORD_KINDS` differ
(PLAY-dOrderedCharter-42 S1, S2), and the closed `<kind>` list of the HYGIENE template drifts. So every
triage or dupes record either cannot be written or reads as a malformed binding.
`TOOL-dRankedPlan-16` S2 registers `plan` in all three places, as `TOOL-dDeclaredLoop-16` S4 does
`disposition`; this unit does the same for the two kinds. It repairs `TOOL-dRankedPlan-3`.

## 2. Scope (IN)

- **S1** — The binding reader. `triage` and `dupes` join `TYPED_RECORD_KINDS` in
  `tools/memory-tree/tree_lib.py` (PLAY-dOrderedCharter-42 S1), the tuple the bindings parser takes
  as the closed first-token set, as `TOOL-dRankedPlan-16` S2 adds `plan`. Observed by AC1 and AC2.
- **S2** — The factory. `tools/memory-tree/build_records.py`'s kind table (PLAY-dOrderedCharter-7 S7)
  gains `triage`, its required fields `Value`, `Rules`, `Asks`, `Rows`, `Judged`, `Batch` and
  `Ratified` (`TOOL-dRankedPlan-3` S5), and `dupes`, its required fields `Input`, `Matched`,
  `Finding` and `Overlap` (its S7), so the table equals the tuple at import. Each file is named on the
  strict stem `<date>-build-<unit id>-<kind>-<n>.md`, the typed-kind join `TOOL-dRankedPlan-16` S2
  narrows (PLAY-dOrderedCharter-42 S3). Observed by AC1.
- **S3** — The kind list. The closed `<kind>` list of `tools/memory-tree/HYGIENE.template.md` (its
  "Record bindings" list, :628-631 at base) gains `triage` and `dupes`, each with its one-line meaning,
  and `memory/HYGIENE.md` is re-rendered by `bash tools/memory-tree/adopt-memory-tree.sh --render`.
  Observed by AC3.
- **S4** — The plants `triage-kind` and `dupes-kind` join `python tools/memory-tree/record_kinds.py
  --selftest` (`TOOL-dRankedPlan-16`'s arm): each writes one record through `gov_record.py new <kind>`
  with every field and lists it bound through `gen_build_index.py --print-bindings`. Observed by AC1
  and AC2.

## 3. Non-goals (OUT)

- The kinds' fields, writers and meaning: `TOOL-dRankedPlan-3` S5 and S7, unchanged.
- A single registration path through `record_kinds.py new`, the audit's left-shift: the registry's
  verb is dTotalRecall's; the main loop may file it as an ask on that build.
- The kit version: `TOOL-dRankedPlan-16` moves the memory-tree kit's version in this build, and the
  `kit epoch` leg grades from the merge-base, so this unit moves it no further.

### Edges

- **consumes-from** `TOOL-dRankedPlan-3` — the `triage` and `dupes` rows of `record-kinds.toml` and their fields, which S1 to S3 register in the reader, the factory and the kind list; without them there is no kind to register
- **hands-off** `TOOL-dRankedPlan-37` — §3's reason for leaving the memory-tree version alone, which that unit restates by its `version_from` carrier (spec audit of units 19 to 29, id 24)

## 4. Design

### Evidence

- `tools/memory-tree/tree_lib.py:406`: `RECORD_KIND_TOKENS = ("spec-audit", "diff-review", "journal",
  "research", "deviation")`; `:544-565` binds a record whose first token is in it and otherwise marks
  it malformed, "first token … is not one of …". `TYPED_RECORD_KINDS` is PLAY-dOrderedCharter-42's,
  unbuilt at base 0689e7fa, and the factory `build_records.py` is PLAY-dOrderedCharter-7's, absent
  there.
- `tools/memory-tree/HYGIENE.template.md:628-631` holds the closed `<kind>` list.
- `TOOL-dRankedPlan-16` S2 and `TOOL-dDeclaredLoop-16` S4 each name `tree_lib.py`, the factory table
  and the HYGIENE list for their kind; `TOOL-dRankedPlan-3`'s Files touched names none of them.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `triage`, `dupes` | `TYPED_RECORD_KINDS` members and factory kinds | none |
| `triage-kind`, `dupes-kind` | `record_kinds.py --selftest` plants | none |

### Rollout

Lands one order after `TOOL-dRankedPlan-3`. Between the two, a triage or dupes record unit 3's pass
writes reads malformed or is refused; the close's bar reads both.

### Files touched (estimate)

- `tools/memory-tree/tree_lib.py`: S1
- `tools/memory-tree/build_records.py`: S2
- `tools/memory-tree/HYGIENE.template.md`: S3
- `memory/HYGIENE.md`: S3's render
- `tools/memory-tree/record_kinds.py`: S4's plants

### Alternatives rejected

- **A parity leg reding a registry row missing from `TYPED_RECORD_KINDS`.** It finds this defect and
  fixes nothing; the registration is owed either way, and the leg is a mechanism for dTotalRecall's
  registry.
- **Serve the records as `research`.** Unit 3 names them as typed kinds whose fields the factory
  checks; an untyped kind skips that check.

## 5. Production-readiness checklist

- security — N/A — registration of two kinds; the door's write path is unchanged.
- perf / scale — N/A — two tuple members.
- error / empty / loading states — a record missing a field is refused by the factory, as AC1 stages.
- observability — `--print-bindings` lists each record bound.
- risks — none: no record of either kind exists before unit 3 lands.
- testing — the two plants, red and green.
- migration — none.
- user docs — the HYGIENE kind list, S3.

## 6. Acceptance criteria

- **AC1** — When `python record_kinds.py --selftest` runs its `triage-kind` plant,
  `gov_record.py new triage` with all seven fields writes `<date>-build-TOOL-tFix-1-triage-1.md`, and
  `python tools/memory-tree/gen_build_index.py --print-bindings` lists it bound with kind `triage`;
  the same call without `--field Rows=…` exits 2 naming `Rows`.
  Red when: a triage record reads malformed or is written without a required field.
- **AC2** — When the `dupes-kind` plant runs over a scratch copy of `tree_lib.py` whose tuple lacks
  `dupes`, the record it writes reads malformed, `first token dupes is not one of`; with the tuple as
  landed it reads bound.
  Red when: the binding reader admits a kind it does not list, or refuses one it does.
- **AC3** — When `grep -n "triage" memory/HYGIENE.md` runs, the closed kind list names `triage` and
  `dupes`, and the rendered file equals the template's render.
  Red when: the kind list omits either kind.

## 7. Gates

`memory hygiene` · `memory-hygiene self-test` · `build-index selftest` · `kit/dogfood doc parity` · `recall floor` · `recall floor arms` · `policy fixtures` · `kit epoch (shipped bytes move, the version moves)` · `spec tokens (a spec's own names resolve)`

New arm: tools/memory-tree/record_kinds.py · covers AC1 AC2 · the `triage-kind` and `dupes-kind` plants in `--selftest`, staged by a tuple lacking the kind · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's finding 28 (HIGH, item
  H6), repairing `TOOL-dRankedPlan-3`.
- rev-2 · 2026-10-27 · §3 · gains the hands-off edge to `TOOL-dRankedPlan-37`, each the reciprocal of that promoted unit's own edge (spec audit of units 19 to 29, `reviews/2026-10-27-review-TOOL-dRankedPlan-19-spec-audit.md`); no other section moves.

## 10. Reuse audit

The seams extended are the three registration points `TOOL-dRankedPlan-16` S2 extends for `plan`:
`TYPED_RECORD_KINDS` in `tools/memory-tree/tree_lib.py`, the factory's kind table in
`build_records.py`, and the HYGIENE template's closed list; nothing is minted. `python
tools/codebase-map/reuse_lookup.py "register a typed record kind so its binding reads bound"` was run
for the set; the binding reader's tuple at `tools/memory-tree/tree_lib.py:406` is the one first-token
set, verified at base, so no second seam exists. The recall query returned the audit's H6 item,
`TOOL-dDeclaredLoop-16` S4 and `TOOL-dRankedPlan-16` S2, which agree.

Recall terms used: `python tools/memory-recall/query.py "what must a new typed record kind register so its records bind" --terms "TYPED_RECORD_KINDS RECORD_KIND_TOKENS build_records kind table HYGIENE kind list triage dupes Serves malformed"`
