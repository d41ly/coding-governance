# TOOL-dCalibratedLens-22 — one route from every item to `file`: the walk collects each item's proposals, and every producer spells the five fields

**Status:** DEFERRED · rev-2 · 2026-11-02 · node a · Tier-2 · base 8bec4cef · streams tooling · order 3 · advances TOOL-dCalibratedLens-18

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-build-TOOL-dCalibratedLens-22-deviation-221.md](../build/2026-11-02-build-TOOL-dCalibratedLens-22-deviation-221.md) | deviation | — |
| [2026-11-02-prompt-TOOL-dCalibratedLens-19-promoted-fix-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-19-promoted-fix-brief.md) | research | TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-29 TOOL-dCalibratedLens-30 |
| [2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md](../reviews/2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit.md) | spec-audit | TOOL-dCalibratedLens-26 TOOL-dCalibratedLens-19 TOOL-dCalibratedLens-20 TOOL-dCalibratedLens-27 TOOL-dCalibratedLens-28 TOOL-dCalibratedLens-21 TOOL-dCalibratedLens-29 TOOL-dCalibratedLens-25 TOOL-dCalibratedLens-23 TOOL-dCalibratedLens-24 TOOL-dCalibratedLens-30 |

<!-- /gen:spec-records -->

## 1. Goal

Close finding id 3, HIGH, item H4 of the round-1 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md`). Units 4, 6 and 16
produce proposals during `gather` and say only that `loop_review.py file` files them, but unit 3 S7
hands `run_loop_file` only the proposals of the item routed to it (unit 5's `propose`) or
`--proposals` under `--dry-run`, and refuses a proposal with an empty `accept`, which none of the
three spells. Unit 5 F5 says earlier proposers join `PROPOSERS` "in this unit's pass" while its S6
moves none. The cap, item-budget and bound proposals therefore never reach the owner. This unit fixes
one route, the walk collecting every item's proposals into `run_loop_file`, and proves it on planted
proposers. It repairs `TOOL-dCalibratedLens-3`, whose walk is the route.

## 2. Scope (IN)

- **S1** — The design change, made at the audit's disposal in the sibling specs' text (each at rev-2,
  its §4 "Amendments (round-1 spec audit)", id 3): unit 3 S7 — every item's step answers
  `(outcome, proposals)`, the walk appends each item's proposals in item order, and `item.loop.file`
  files the whole list, so a gather-time proposal and a `propose`-time one take the same route, unit
  15 F5's extension being one instance of it; units 4 S8, 6 S5 and 16 S8 each spell their proposal's
  `kind`, `id`, `action`, `accept` and `row` (kinds `cap-value`, `item-budget` and `bound`); unit 5's §3
  and F5 read that `PROPOSERS` holds `propose`-time proposers only and that no earlier unit's
  proposer is re-homed into it. Observed by AC1.
- **S2** — The proof, a `--fixture` plant `every-proposer` in `tools/loop/loop_review.py`: two planted
  `gather` steps, each answering one proposal with all five fields, and a third answering one whose
  `accept` is empty; `run --dry-run --key 2026-W45` prints both filed texts at `item.loop.file`, each
  `filed`, and the refusal line `loop — refused: <kind> <id> carries no accept line` for the third.
  The same plant then runs `run` twice without `--dry-run`, the key in `GOV_CADENCE_KEY=2026-W45` and a
  counting stub standing in for the intake filer: each run exits 0, the first files the two valid
  proposals as `filed`, and the second files no new intake, each a `seen` receipt (round-2 id 33).
  Observed by AC2.
- **S3** — The staged break: a walk that hands `file` only the outcomes routed to it files zero of the
  planted proposals, so the plant reds. Observed by AC3.

## 3. Non-goals (OUT)

- The proposers themselves: each producer lands its own under its amended spec. This unit proves the
  route on planted ones, since units 4, 6 and 16 build after it.
- Routing by `review.loop.retire`: unit 5 S7 governs `retire`, `prune` and `tighten` only, unchanged.
- Unit 14's scenario proposal shape: id 7 (`TOOL-dCalibratedLens-30`).
- AC1 observes only the disposal's text in sibling specs and is green at writing; it is a
  precondition, not an observation of this unit's build (the round-2 audit's ids 4, 18 and 29).

### Edges

- **consumes-from** `TOOL-dCalibratedLens-3` — `run_loop_walk`, `run_loop_file` and the `--fixture` frame; without the walk there is no route to observe

## 4. Design

### Evidence

- spec-3 S7: a proposal reaches `run_loop_file` only "handed by the walk from the item routed to it
  (unit 5's `propose`), or by `--proposals <path>` with `--dry-run`", and an empty `accept` is
  refused.
- spec-4 S8, spec-6 S5 and spec-16 S8 produce proposals at `gather`; none spells an `accept`.
- spec-15 F5 already extends `run_loop_walk` with `derive_cap_raises`' proposals (option (a), the walk
  being "the one place every item's output meets").

### The five fields, per producer

| Producer | `kind` | `id` | `action` | `accept` |
|---|---|---|---|---|
| unit 4 caps | `cap-value` | the cap name | `raise` or `lower` | the owner applies the printed `policy_edit.py set` command, or keeps the current value |
| unit 6 budgets | `item-budget` | the role | `raise` or `lower` | the owner pins the role's value through `policy_edit.py set`, or keeps it |
| unit 16 bounds | `bound` | the policy key | `raise` or `lower` | the owner applies the printed command, or keeps the bound |

`cap-value` is not unit 15's `cap`: a breach raise and a re-derived value for one subject are two owner
items, and the key hash of `<kind>\t<id>` keeps them apart.

### Inventory

| Minted | Kind | Naming cell |
|---|---|---|
| `every-proposer` | `--fixture` plant name | none |
| `cap-value`, `item-budget`, `bound` | proposal kinds | none |

### Files touched (estimate)

- `tools/loop/loop_review.py` — S2 and S3, the plant

### Alternatives rejected

- **Each producer files its own proposals.** A second filing path beside `run_loop_file`, which unit 5
  F5's option (c) already rejected.
- **Every proposer re-homed into `PROPOSERS` at unit 5's pass.** It leaves the cap, budget and bound
  proposals unfiled from their landing (orders 7 to 9) until order 11, and rewrites three landed steps.

## 5. Production-readiness checklist

- security — no new write path; `run_loop_file` keeps its refusal of an empty `accept` and its stdin
  filing.
- perf / scale — the list is the period's proposals, a few dozen.
- error / empty / loading states — no proposal: the zero line unit 3 S7 prints.
- observability — one line per filed text and per refusal.
- risks — a producer that omits `accept` is refused loudly, never filed blank.
- testing — the plant of S2 and its staged break.
- migration — N/A: no proposal is filed at base.
- user docs — N/A: `help/loop-review.md` (unit 3 S11) describes filing.

## 6. Acceptance criteria

- **AC1** — When `grep -n 'cap-value\|"item-budget"\|"bound"'` runs over the specs of units 4, 6 and 16
  and `grep -n '^- \*\*id 3 · '` runs over the specs of units 3 and 5, each prints its amendment, unit
  5's naming `propose-time` proposers only.
  Red when: a producer's spec still names no `accept`, or unit 5 still re-homes earlier proposers.
  A precondition read at writing: it greps the disposal's text.
- **AC2** — When `python loop_review.py --fixture --plant every-proposer` runs `run --dry-run --key
  2026-W45`, it prints two filed texts and one refusal line at `item.loop.file`; run twice as `run`
  under `GOV_CADENCE_KEY=2026-W45` with the counting stub, each run exits 0 and the second files no
  `filed` intake.
  Red when: a gather-time proposal is not filed, an empty `accept` is filed, the refusal exits the
  walk, or a second run files a new intake.
- **AC3** — When the plant `every-proposer` runs under the staged break of S3, it reds naming the two unfiled
  proposals.
  Red when: a walk that drops gather-time proposals passes.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates`

The loop kit's leg `loop-review selftest` (TOOL-dCalibratedLens-2 S11) is not in the manifest at base
and is named here in prose; it runs the plant once that unit lands.

New arm: tools/loop/loop_review.py · covers AC2 AC3 · the `every-proposer` plant, staged red by a walk that hands `file` only its routed outcomes · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, promoted from id 3 (HIGH, item H4) of the round-1 spec audit;
  units 3, 4, 5, 6 and 16 amended at the disposal (their rev-2).
- rev-2 · 2026-11-02 · §3 S2 AC1 AC2 · amended at the disposal of the round-2 spec audit
  `2026-11-02-review-TOOL-dCalibratedLens-19-spec-audit`, each `TOOL-dCalibratedLens-41`'s: AC2 states
  exit 0 and a second run filing no new intake (id 33); AC1 stated a precondition (ids 4, 18, 29).

## 10. Reuse audit

The seam extended is unit 15 F5's option (a), the walk extending what it hands `run_loop_file`,
generalised from one provider to every item. `python tools/codebase-map/reuse_lookup.py "isolate each
reader so one failure becomes an unread line, never the walk's exit"`, run once for the set, ranked
name stems only; the loop kit is absent at base, so the seam is the sibling specs'. The recall probe
returned TOOL-cMendedVintage-19, the placement ruling this unit's order follows.

Recall terms used: `python tools/memory-recall/query.py "how is a spec audit finding promoted to a
repair unit placed after the unit it repairs" --terms "spec audit promoted repair unit order hands-off
consumes-from minors batch loop review record kind"`
