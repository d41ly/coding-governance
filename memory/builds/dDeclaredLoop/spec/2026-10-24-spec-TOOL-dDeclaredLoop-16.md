# TOOL-dDeclaredLoop-16 — one closed disposition set, and the owner's disposition record

**Status:** OPEN · rev-1 · 2026-10-24 · node d · Tier-2 · base ed497191 · streams tooling · order 4 · advances TOOL-dDeclaredLoop-35

**Carries:** cl-dClosedLoop-0101@6e645e0e whole
**Carries:** node:record-kind.disposition

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-reuse-scout-a.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-26 |
| [2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md](../build/2026-10-24-build-TOOL-dDeclaredLoop-1-spec-stage-returns.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |
| [2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md](../prompts/2026-10-24-prompt-TOOL-dDeclaredLoop-1-spec-brief.md) | research | TOOL-dDeclaredLoop-1 TOOL-dDeclaredLoop-2 TOOL-dDeclaredLoop-3 TOOL-dDeclaredLoop-4 TOOL-dDeclaredLoop-5 TOOL-dDeclaredLoop-6 TOOL-dDeclaredLoop-7 TOOL-dDeclaredLoop-8 TOOL-dDeclaredLoop-9 TOOL-dDeclaredLoop-10 TOOL-dDeclaredLoop-11 TOOL-dDeclaredLoop-12 TOOL-dDeclaredLoop-13 TOOL-dDeclaredLoop-14 TOOL-dDeclaredLoop-15 TOOL-dDeclaredLoop-17 TOOL-dDeclaredLoop-18 TOOL-dDeclaredLoop-19 TOOL-dDeclaredLoop-20 TOOL-dDeclaredLoop-21 TOOL-dDeclaredLoop-22 TOOL-dDeclaredLoop-23 TOOL-dDeclaredLoop-24 TOOL-dDeclaredLoop-25 TOOL-dDeclaredLoop-26 TOOL-dDeclaredLoop-27 TOOL-dDeclaredLoop-28 TOOL-dDeclaredLoop-29 TOOL-dDeclaredLoop-30 TOOL-dDeclaredLoop-31 TOOL-dDeclaredLoop-32 TOOL-dDeclaredLoop-33 TOOL-dDeclaredLoop-34 |

<!-- /gen:spec-records -->

## 1. Goal

One closed disposition set, declared once in the loop definition, replaces the two the records give:
placement's set and Plan's draft scope (`gap-flow-13`, "two disposition sets"; the item audit's F12,
research-flow-items-a.md:151-153). Plan's words map into it, the vocabularies that only look alike are
named as different, and the owner's disposition record is a typed record kind carrying one value.

## 2. Scope (IN)

- **S1** — The set, `[dispositions]` in `tools/loop/loop.toml`: `set = ["continue", "amend", "new",
  "patch", "repeat", "unit", "breakpoint", "ask", "none"]`, placement's nine (flow-steps.md:124,
  orientation.md `[placement]`), read through `read_dispositions()` in `tools/loop/loop_lib.py`.
  Observed by AC1.
- **S2** — The mapping, `[[disposition-alias]]` rows with `word` and `means`: Plan's draft words
  `attach` to `amend`, `defer` to `ask`, and `refuse-as-duplicate` to `continue` onto the matched
  build; `resolve_disposition(word)` returns a member for a member or an alias and raises `LoopError`
  for any other word. Observed by AC2.
- **S3** — The vocabularies that are not this set, stated in `tools/loop/README.md` and in the
  definition's comment: the review round's exit `fold|promote` (`REVIEW_DISPOSITIONS`,
  `tools/unattended/unattended.sh:999`), the per-finding report grammar (`class:`, `new:`, `gate:`,
  `none`, dFairHearing-8), and triage's four verdicts (flow-steps.md:182), which move a build in
  planning to one of its terminal states. Observed by AC5.
- **S4** — The record kind `disposition` in the typed build-folder record factory
  (PLAY-dOrderedCharter-7 S7, `tools/memory-tree/build_records.py`): name
  `<date>-build-<unit id>-disposition-<n>.md`, required fields `Item` (the disposed owner item's tag),
  `Disposition` (one `seg`-shaped word) and `Channel` (`mailbox`, `terminal` or `prompt`, the three
  channels `[breakpoint]` names), optional `Reason`; and its door, `build_records.py new disposition
  --build <slug> --unit <id> --item <tag> --disposition <word> --channel <channel>`. Observed by AC3.
- **S5** — The value join, `check_disposition_record(record)` in `tools/loop/loop_lib.py`: the
  record's `Disposition` is a member of the disposed item's closed outcome set, read by
  `read_outcome_set(item)`, which returns the set of S1 for an item declaring
  `outcomes = "dispositions"`, the item's own list otherwise, and nothing for an item the definition
  does not declare, printed `unarmed`, never green. Observed by AC4.

## 3. Non-goals (OUT)

- The placing items `entry.place`, `entry.place-check` and `entry.place-owner`, and `placement.check`:
  dPlacedRequest's. This unit declares the set they return from.
- Triage's rules and its verdict set: dRankedPlan's (`plan.triage-rule`, `plan.triage-judge`).
- `REVIEW_DISPOSITIONS`, check 37 (`tools/unattended/unattended.sh:12715-12726`) and the leg's
  `core_of` read (`tools/unattended/check-unattended.sh:624-628`): unchanged, a different vocabulary.
- Item outcome sets: TOOL-dDeclaredLoop-12 declares each item's `outcomes`; this unit reads them.
- The owner items themselves and their holds: TOOL-dDeclaredLoop-19's breakpoints and owner gates.
- A writer of the record by mailbox or prompt: dWellOiledMachine's and dKeptSession's channels; the
  door of S4 is the stand-in every channel calls.

### Edges

- **consumes-from** `TOOL-dDeclaredLoop-1` — `loop_lib.py` and `loop.toml`, where the set is declared and read
- **hands-off** `TOOL-dDeclaredLoop-12` — `read_outcome_set` and the `dispositions` reference an item's `outcomes` may name, so a placing item's closed outcome set is this set and never a copy
- **hands-off** `TOOL-dDeclaredLoop-13` — `record-kind.disposition`, the owner's disposition record a transition row reads as its witness
- **hands-off** `TOOL-dDeclaredLoop-15` — `record-kind.disposition`, the owner's disposition record a transition row reads as its witness
- **hands-off** `TOOL-dDeclaredLoop-19` — `record-kind.disposition`, the owner's disposition record a transition row reads as its witness
- **hands-off** `TOOL-dDeclaredLoop-28` — `record-kind.disposition`, the owner's record that releases or refuses a held change
- **hands-off** `TOOL-dDeclaredLoop-31` — `record-kind.disposition`, the owner's disposition record a transition row reads as its witness

## 4. Design

### Data model

```toml
# tools/loop/loop.toml
[dispositions]
# The one closed disposition set (cl-dClosedLoop-0101). Not REVIEW_DISPOSITIONS (fold|promote), not
# the per-finding report grammar (class:, new:, gate:, none), not triage's verdicts.
set = ["continue", "amend", "new", "patch", "repeat", "unit", "breakpoint", "ask", "none"]

[[disposition-alias]]
word = "defer"
means = "ask"
```

| Word | Source | Means | Why |
|---|---|---|---|
| `attach` | flow `[plan]` draft scope | `amend` | attaching a request to a live build is its re-entry at Design |
| `defer` | flow `[plan]` draft scope | `ask` | a deferred request is filed as an ask (flow-steps.md:182) |
| `refuse-as-duplicate` | the item audit's F12 | `continue` | a duplicate is re-placed onto the matched build, which carries on; the re-placement after `plan.dedupe` ends the duplicate `merged` (flow-steps.md:738) |

### The record

```markdown
**Serves:** disposition TOOL-tFix-1
**Item:** item.plan.exit
**Disposition:** continue
**Channel:** terminal
**Reason:** the plan record is ratified as written
```

The record carries one word. Which words are legal is the disposed item's: a placing item declares
`outcomes = "dispositions"` and takes S1's set; an owner gate such as `item.build.ratify` declares its
own outcomes (`ratified`, `rejected`, flow-steps.md:296), and its record carries one of those. So the
record's value is graded against one closed set per item, and the placement set is declared once.

A build-level owner item that no unit owns names the build's first unit id in the record's file name,
the convention this build's own build-level records follow (`memory/builds/dDeclaredLoop/build/`,
every record named under `TOOL-dDeclaredLoop-1`), until a build-level grammar lands.

### Inventory

Minted: `[dispositions]` with key `set`; `[[disposition-alias]]` with keys `word` and `means`;
`read_dispositions`, `resolve_disposition`, `read_outcome_set` and `check_disposition_record` in
`tools/loop/loop_lib.py`; the outcome reference `dispositions`; the record kind `disposition` with its
fields `Item`, `Disposition`, `Channel` and `Reason`; the plants `disposition-unknown`,
`disposition-alias`, `disposition-outcome` and `disposition-undeclared`. Naming cells: each function is
asked of `python tools/lexicon/lexicon.py --suggest <name> --as py.function` at the pass.

### Migration

Additive: no record of this kind exists, and no reader of placement words exists in code at base.

### Rollout

Live at landing; the join is `unarmed` for every item until TOOL-dDeclaredLoop-12's rows land.

### Files touched (estimate)

- `tools/loop/loop.toml`
- `tools/loop/loop_lib.py`
- `tools/loop/README.md`
- `tools/memory-tree/build_records.py`

### Alternatives rejected

- **The record closed over the nine words alone** (shared interface I9's literal reading): an owner
  gate's ruling, ratified or rejected, a park's resume, has no member, so TOOL-dDeclaredLoop-15, -19 and
  -31 could not write their records (§8 F2).
- **Triage's verdicts folded into the set**: `retire` and `refuse` decide terminal states of a build
  already in planning, a different question from where a request goes.

## 5. Production-readiness checklist

- security — the door writes one record in the session's own build folder, its fields checked by the
  factory before the write; no network.
- perf / scale — one TOML read per call.
- error / empty / loading states — an unknown word is a `LoopError` naming it and the set; an item with
  no outcome set reads `unarmed`.
- observability — `loop_lib.py --check` prints the set and the aliases.
- risks — an alias hides a legacy word behind a member; the README names each so a reader can find it.
- testing — the plants of §4, observed by a pass through the fixture; the suite arm in §7 is observed
  RED then GREEN by the main loop at the close.
- migration — none.
- user docs — `help/loop.md` gains the set and the record (S1, S4).

## 6. Acceptance criteria

- **AC1** — When `python loop_lib.py --check` runs in the loop kit, it prints the nine members in the
  order of S1; under `--fixture --plant disposition-unknown`, a definition whose set repeats `ask`, it
  exits 1 naming the repeat.
  Red when: the set is read without a duplicate check, so `ask` twice reads green.
- **AC2** — When `python -c` imports `loop_lib` from the loop kit and calls `resolve_disposition` on
  `defer`, `attach`, `refuse-as-duplicate`, `new` and `fold`, it returns `ask`, `amend`, `continue` and
  `new`, and raises `LoopError` on `fold`.
  Red when: an unknown word falls through as itself, so `fold` returns `fold`.
- **AC3** — When `python build_records.py new disposition --build tFix --unit TOOL-tFix-1 --item
  item.plan.exit --disposition continue --channel terminal` runs on a scratch tree, it writes
  `<date>-build-TOOL-tFix-1-disposition-1.md` carrying the four fields; without `--item` it exits 1
  naming the field, and with `--channel email` it exits 1 naming the closed set.
  Red when: the factory accepts the record with no `Item`, so a disposition names no item.
- **AC4** — When `python loop_lib.py --fixture --plant disposition-outcome` runs, an item declaring
  `outcomes = ["ratified", "rejected"]` with a record `ratified` passes and one `continue` exits 1
  naming the item and its set; an item declaring `outcomes = "dispositions"` passes `continue`; and
  under `--plant disposition-undeclared` a record on an undeclared item prints `unarmed` and exits 0.
  Red when: the join reads S1's set for every item, so `ratified` is refused, or an undeclared item
  reads green.
- **AC5** — When `grep -nE 'REVIEW_DISPOSITIONS|class:|select' README.md` runs in the loop kit, it
  finds each other vocabulary named as not this set.
  Red when: the README names the set and none of the vocabularies it is not, which is the confusion
  the clause closes.

## 7. Gates

The pass adds no leg: `loop_lib.py --check` runs under TOOL-dDeclaredLoop-1's `loop definition` leg.

`check-arms selftest` · `memory-hygiene self-test` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/loop_lib.py · covers AC1 AC2 AC4 · the `loop definition` leg's fixture plants, the failing case staged by the `disposition-unknown` plant · none

## 8. Open questions

- **FACT-QUESTION · F1 — The brief gives this spec's status header the token `DRAFT`; is that a legal
  status?** Probe: `STATUS_TOKENS` at `tools/memory-tree/tree_lib.py:27`. Observation, 2026-10-24:
  `DRAFT` is not in the tuple. Liveness: the tuple would carry it if the vocabulary admitted it.
  RESOLVED (agent, 2026-10-24, delegated): `OPEN`, rung 2. widens: none · relaxes: none
- **F2 — Shared interface I9 says the owner's disposition record "carries one value of the set"; which
  set?** Options: (a) always the nine placement words; (b) the disposed item's closed outcome set, the
  nine for a placing item. Flow-steps' owner items route on their own outcomes, `ratified` and
  `rejected` at `build.ratify` (flow-steps.md:296), the parked state's disposition back to its state
  (flow-steps.md:759), so (a) leaves those records nothing to carry. RESOLVED (agent, 2026-10-24,
  delegated): (b), rung 1, flow-steps' owner items as written; the placement set is still declared
  once. widens: none · relaxes: none
- **F3 — Plan's set today is triage's `select`, `defer`, `retire`, `refuse` (flow-steps.md:182, the
  fold's `disposition-set-gaps` row at :950); does the one set absorb it?** Options: (a) map the draft
  scope's words, as F12 asks, and name triage's verdicts as a different vocabulary; (b) add `retire`
  and `refuse` to the set. (b) widens what `entry.place` may return to two verdicts about a build already
  in planning. RESOLVED (agent, 2026-10-24, delegated): (a), rung 1, F12's "maps defer and
  refuse-as-duplicate". widens: none · relaxes: none
- **F4 — What unit id names a build-level owner item's record?** Options: (a) the build's first unit
  id, the convention of this build's build-level records; (b) a new name form without a unit id. (b) is a
  change to PLAY-dOrderedCharter-7's grammar this unit's clause does not name. RESOLVED (agent,
  2026-10-24, delegated): (a), rung 3, reuse of the grammar as landed. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-24 · initial draft, from the packet's Items 16, the brief's shared interface I9,
  scout A's row for cl-0101, and flow-steps' placement, triage and owner items read at base `ed497191`.

## 10. Reuse audit

The seam extended for the set is the closed-set constant with membership by whole member, the shape
of `REVIEW_DISPOSITIONS` (`tools/unattended/unattended.sh:999`) and check 37 (:12715-12726), carried
here as a TOML array so no member can hold a separator; the record is PLAY-dOrderedCharter-7 S7's
factory, extended by one kind. `python tools/codebase-map/reuse_lookup.py "one closed set of
disposition values checked by membership"` ranked generic stems (`check`, `checks`, `check_line`,
`resolve_pattern_sets`) and named no disposition seam. The recall probe returned scout A's row and
the item audit's F12, which agree with source; scout A quoted Plan's set as the draft
`{attach, new, defer, refuse}`, where flow-steps after the fold reads triage's four verdicts, recorded
as F3.

Recall terms used: `python tools/memory-recall/query.py "which disposition sets disagree between placement and plan" --terms "disposition set placement continue amend new patch ask none defer refuse REVIEW_DISPOSITIONS"`
