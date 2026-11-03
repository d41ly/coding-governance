# TOOL-dCalibratedLens-12 — the Loop Review pricing cost per item kind from trace rows

**Status:** DEFERRED · rev-2 · 2026-11-02 · node a · Tier-2 · base 8bec4cef · streams tooling · order 5 · advances TOOL-dCalibratedLens-18

**Carries:** cl-dClosedLoop-0469@653feb80 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-11-02-prompt-TOOL-dCalibratedLens-1-spec-brief.md](../prompts/2026-11-02-prompt-TOOL-dCalibratedLens-1-spec-brief.md) | research | TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-14 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 |
| [2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md](../reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md) | spec-audit | TOOL-dCalibratedLens-2 TOOL-dCalibratedLens-3 TOOL-dCalibratedLens-7 TOOL-dCalibratedLens-9 TOOL-dCalibratedLens-15 TOOL-dCalibratedLens-4 TOOL-dCalibratedLens-6 TOOL-dCalibratedLens-16 TOOL-dCalibratedLens-17 TOOL-dCalibratedLens-5 TOOL-dCalibratedLens-10 TOOL-dCalibratedLens-11 TOOL-dCalibratedLens-8 TOOL-dCalibratedLens-13 TOOL-dCalibratedLens-1 TOOL-dCalibratedLens-14 |

<!-- /gen:spec-records -->

## 1. Goal

P35 makes every act carry its own cost and duration (v2:1049-1052), and `trace.cost`
(`tools/policy/catalogue.toml:1602`) selects which of them the act record writes. A build's spend is
summed from those trace rows (TOOL-dWellOiledMachine-51 S2), but nothing sums them per item kind, so
the Loop Review cannot say what a kind of work costs, and the value ledger has no row for it. This unit
gives the ledger its `item` rows: one per item kind, its cost the tokens of the window's act records of
that kind.

## 2. Scope (IN)

Build-run preconditions, each specced and unbuilt at base `8bec4cef`, re-grounded by the build run,
which stops this unit when one is absent: TOOL-dCalibratedLens-2 (the module, `PROVIDERS`, the row
grammar and `price`), TOOL-dCalibratedLens-3 (the window the walk hands `price`),
TOOL-dCalibratedLens-9 (`ledgers.py acts` and `derive_act_tokens`), and the act record with its
`Item`, `Tokens-In` and `Tokens-Out` fields (TOOL-dWellOiledMachine-32 S7, S8) read through
`read_act_records` (TOOL-dWellOiledMachine-53 S4).

- **S1** — (amended, id 51) The provider, `PROVIDERS`' `item` entry. `derive_item_rows(root, window)` in
  `tools/loop/loop_review.py` runs `ledgers.py acts` once through the subprocess
  TOOL-dCalibratedLens-9 S1 states, and hands the parsed list to `derive_item_costs(acts, window)`.
  That pure function groups the act records by `item` and returns `(rows, events)` in
  TOOL-dCalibratedLens-2's provider shape: one row per item kind, as §4 "The rows" states, and no
  event. Observed by AC1 and AC2.
- **S2** — The cost is `derive_act_tokens` (TOOL-dCalibratedLens-9 S2) summed over the item kind's act
  records whose `key` date lies in the window, rendered `<tokens>tok/<acts>`; no second token
  computation is written. Observed by AC1.
- **S3** — Unrecorded cost said, never zeroed: an act record whose `derive_act_tokens` answers `None`,
  under `trace.cost` `none` or a withheld field, is counted per row and printed as one `ledger — item
  · <item tag> · <n> act(s) unrecorded` line on stderr, and a row whose every in-window act is
  unrecorded renders `cost` as `-`. An act record with no `item`, or `item` `none`, is grouped under
  `unattributed`. Observed by AC2 and AC3.
- **S4** — (amended, id 51) A refused act read yields no row and one `ledger — item · acts unread · <why>` line, the
  refusal TOOL-dCalibratedLens-9 S1 states. Observed by AC4.
- **S5** — The docs. `tools/loop/README.md` and `help/loop-review.md` (TOOL-dCalibratedLens-2 S12)
  each state the `item` row and its source. NOT OBSERVED by a criterion: prose, read by the closing
  review.

## 3. Non-goals (OUT)

- The view, its grammar, `price`, `derive_ledger_rows`, and the `window` and `state` columns:
  TOOL-dCalibratedLens-2's.
- The act read and the token sum: TOOL-dCalibratedLens-9's `ledgers.py acts` and
  `derive_act_tokens`, called, never copied.
- Wall time per item kind, and the reservation estimate per item kind: TOOL-dWellOiledMachine-53's
  `derive_estimate_hours`, trended by TOOL-dCalibratedLens-17. The `cost` unit is `tok`.
- A build's spend: TOOL-dWellOiledMachine-51's `derive_build_spend`, a sibling over the same rows
  grouped by build. Neither calls the other: they are two kits' readings of one source.
- Proposing an item kind's retirement or a merge: TOOL-dCalibratedLens-5's `propose`. An item kind has
  no catch of its own (§8 F1), so this row informs the owner and never reads as a row that caught
  nothing.
- Reading `trace.cost` itself. The act records already reflect its value: a field it withholds reads
  `withheld`, which S3 reports.

### Edges

- **consumes-from** `TOOL-dCalibratedLens-9` — `ledgers.py acts` and `derive_act_tokens`; without them this unit has no act read and would write a second cost computation
- **consumes-from** `TOOL-dCalibratedLens-2` — `PROVIDERS`, which gains the `item` entry, the provider shape and the `-` catches rule
- **consumes-from** `TOOL-dCalibratedLens-3` — the window the walk hands `price`
- **consumes-from** external — TOOL-dWellOiledMachine-32 (the act record and its token fields) and -53 (`read_act_records`), DEFERRED at base and of an ancestor build
- **hands-off** `TOOL-dCalibratedLens-30` — the `[[usage]]` row of any flag it adds, which the minors batch's `docs_leg.py --list` observation reads (id 39)

## 4. Design

### The rows

| Column | Value for one item kind |
|---|---|
| `kind` | `item` |
| `id` | the act record's `item`, an item tag such as `item.build.unit`, or `unattributed` |
| `since` | the earliest `<date>` of that kind's act record keys, over every act record and not only the window's |
| `cost` | `<tokens>tok/<acts>`: the sum of `derive_act_tokens` over the kind's in-window act records with a cost, and their count; `-` per S3 |
| `catches` | `-`, so `derive_ledger_rows` keeps `-` in all three catch columns |

An act record's date is the `<date>` its file name opens with, the door's minted date
(TOOL-dWellOiledMachine-32 S7), compared as a UTC day against the window's start and end. An item kind
with no act record in the window writes no row, since the review prices what the window spent. Rows
sort by kind and then id, the grammar's order (TOOL-dCalibratedLens-2 §4 "The row").

```
| item | item.build.unit | 2026-08-02 | 1840221tok/38 | - | - | - | 60d | idle |
| item | item.review.synth | 2026-08-05 | 402118tok/12 | - | - | - | 60d | idle |
| item | unattributed | 2026-10-11 | - | - | - | - | 60d | new |
```

The `window` and `state` cells are TOOL-dCalibratedLens-2's to render; the figures are illustrative
and DERIVED at each review.

### Inventory

Minted: the functions `derive_item_rows` and `derive_item_costs` in `tools/loop/loop_review.py`, each
answered OK by `python tools/lexicon/lexicon.py --suggest <name> --as py.function` at this base; the
`PROVIDERS` key `item`; the output lines `ledger — item · …`.

### Migration

None: no act record exists at base, and a review over none writes no `item` row.

### Amendments (round-1 spec audit)

The round-1 spec audit
(`reviews/2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit.md`) confirmed the
findings below on this spec, and its disposal amended this text. Each bullet supersedes the text it
names; the unit it names owns the finding and its proof.

- **id 23 · §4 "The rows" (L8, `TOOL-dCalibratedLens-30`)** — Corrected in place: the two `idle`
  sample rows carry `since` dates before the window's start, as unit 2's `derive_row_state` makes a
  row inside it `new`.
- **id 51 · S1, S4 (M26, `TOOL-dCalibratedLens-30`)** — The acts are read with
  `ledgers.py acts --since <window start>` (TOOL-dCalibratedLens-9 S1 as amended).
- **id 39 · Files touched (M19, `TOOL-dCalibratedLens-30`)** — Every `loop_review.py` verb or flag
  this unit adds to `help/loop-review.md` gets its `[[usage]]` row in `tools/govkit/usage.toml`, and
  the page's `<!-- usage: … -->` anchor is re-fingerprinted, so
  `python tools/govkit/docs_leg.py --list` names it and the `docs` leg reads no `UNROWED` line.

### Files touched (estimate)

- `tools/loop/loop_review.py` (S1 to S4, and the `--fixture` cases of §7)
- `tools/loop/README.md` (S5)
- `help/loop-review.md` (S5, TOOL-dCalibratedLens-2's page)
- `tools/govkit/usage.toml` — the `[[usage]]` row of each verb or flag added (id 39)

### Alternatives rejected

- **Calling `derive_build_spend` per build and splitting by item.** It returns a build's totals, not
  its acts, and lives in the runtime kit the loop kit may not import.
- **A per-kind sum written by the act record's writer.** A running total beside the records it sums
  is a fact twice, and goes stale on a pruned or late record.

## 5. Production-readiness checklist

- security — no write path: the provider reads the act records through the runtime kit's CLI, and its
  rows land through `price`, TOOL-dCalibratedLens-2's.
- perf / scale — one `ledgers.py acts` per review; its cost is `read_act_records`'s, one `show` per act
  record, that spec's ceiling.
- error / empty / loading states — a refused read yields no row and names why; unrecorded acts are
  counted per row; an empty population writes no row.
- observability — every `ledger — item` line names the kind and the count it could not price.
- risks — a review whose window spans a `trace.cost` change prices some acts and reports the rest
  unrecorded, which S3 makes visible rather than averaged.
- testing — each criterion is a probe of this unit's functions over planted act rows; the arm in §7 is
  observed RED then GREEN by the main loop at the close.
- migration — none.
- user docs — S5.

## 6. Acceptance criteria

- **AC1** — When a probe calls `derive_item_costs` from `loop_review.py` over planted act rows, two
  `item.build.unit` acts of 100 and 50 tokens and one `item.review.synth` act of 70 tokens inside the
  window and one `item.build.unit` act of 900 tokens dated before it, it returns `item.build.unit` with
  `cost` `150tok/2` and `since` the earlier act's date, and `item.review.synth` with `cost` `70tok/1`,
  each with `catches` `-`, and no event.
  Red when: an out-of-window act is summed, `since` is read from the window alone, or a catch column
  carries a number.
- **AC2** — When the same probe adds an `item.review.synth` act whose `tokens-in` is `withheld`, that
  row's `cost` stays `70tok/1` and stderr carries one `ledger — item · item.review.synth · 1 act(s)
  unrecorded` line.
  Red when: the withheld act is summed as zero, or counted in `<acts>`, with no line.
- **AC3** — When the probe plants one in-window act with no `item` and `tokens-out` `withheld`, the
  rows include `unattributed` with `cost` `-`.
  Red when: an item-less act is dropped, or a row of unrecorded acts reads `0tok`.
- **AC4** — When `derive_item_rows` runs in a scratch repository with no runtime kit on the resolve
  path, it returns no row and prints one `ledger — item · acts unread ·` line.
  Red when: a refused read yields rows priced at zero.
  fixture: a scratch repository under `%TEMP%`.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `lexicon naming predicates` · `docs` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix`

The leg `loop-review selftest` (TOOL-dCalibratedLens-2 S11, argv `loop_review.py --fixture`) is not in
the manifest at base, so it is named here in prose; it grades the arm below once that unit lands.

New arm: tools/loop/loop_review.py · covers AC1 AC2 AC3 AC4 · `--fixture` cases planting act rows in and out of the window, a withheld field, an item-less act and a missing runtime kit; the failing case staged by dropping the window filter from `derive_item_costs` · none

## 8. Open questions

- **F1 — What fills `catches`, `false-reds` and `last-catch` for an `item` row?** Options: (a) `-`,
  an item kind having no catch of its own; (b) the catch source `review.loop.catch-source` names, whose
  records attribute reds to legs and never to an item kind, so every item row reads `0` catches and is
  proposed every review; (c) a catch per item derived from its outcomes, which no record marks as a
  catch. RESOLVED (agent, 2026-11-02, delegated): (a), rung 1 of the records: TOOL-dCalibratedLens-2
  §4 "The row" keeps `-` in the three catch columns of a row its provider returns with `catches` `-`,
  "so a kind no source attributes a catch to never reads as one that caught nothing". widens: none ·
  relaxes: none
- **F2 — Which date places an act record in the window?** Options: (a) the `<date>` its file name
  opens with; (b) its commit time, one `git log` per record; (c) its `Epoch` field, the lease epoch,
  which is no time. RESOLVED (agent, 2026-11-02, delegated): (a), rung 3: the door mints it at the
  act's exit (TOOL-dWellOiledMachine-32 S7), so it is the day the cost was spent and costs no spawn.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-11-02 · initial draft, from the packet's Items 12 (`cl-dClosedLoop-0469@653feb80`), P35
  (v2:1049-1052), the brief's row for this unit and S1, the sibling specs TOOL-dCalibratedLens-2, -3
  and -9 as written this run, and TOOL-dWellOiledMachine-32, -51 and -53 at base `8bec4cef`. The status
  token is `OPEN`, the drafting token of TEMPLATE-SPEC; the brief's `DRAFT` is no member of
  `STATUS_TOKENS` (`tools/memory-tree/tree_lib.py:28`).
- rev-2 · 2026-11-02 · §3 §4 §7 S1 S4 · amended at the disposal of the round-1 spec audit
  `2026-11-02-review-TOOL-dCalibratedLens-1-spec-audit`, §4 "Amendments (round-1 spec
  audit)": ids 23, 51 and 39 (`TOOL-dCalibratedLens-30`); §3 gains the hands-off to unit 30.

## 10. Reuse audit

The seams extended are TOOL-dCalibratedLens-2's `PROVIDERS` and TOOL-dCalibratedLens-9's `ledgers.py
acts` and `derive_act_tokens`, called as they are, over TOOL-dWellOiledMachine-53's
`read_act_records`; the shape is the sibling of TOOL-dWellOiledMachine-51 S2's `derive_build_spend`,
which groups the same rows by build. `python tools/codebase-map/reuse_lookup.py "sum token cost of act
records grouped by item kind"` ranked name stems (`sum`, `records`, `resolve_prefix_token`) and
runlog's record helpers, none a reader of act records, which are absent at base with the runtime kit;
no landed seam fits beyond the units named. Where record and source disagree:
TOOL-dWellOiledMachine-32 S8 cites `trace.cost` at `catalogue.toml:1572`, and at base its row's `name`
line is `tools/policy/catalogue.toml:1602`, as the brief says.

Recall terms used: `python tools/memory-recall/query.py "where is the cost per item kind derived from act records and trace cost" --terms "act record Tokens-In Tokens-Out Item trace.cost read_act_records derive_build_spend spend per item kind value ledger"`
