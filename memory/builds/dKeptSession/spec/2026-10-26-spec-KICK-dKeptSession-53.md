# KICK-dKeptSession-53 — a consumed interface notice supersedes the parent's earlier rows by content key and by the session chain, never by arrival

**Status:** OPEN · rev-3 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 26 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 |
| [2026-10-26-build-KICK-dKeptSession-53-deviation-531.md](../build/2026-10-26-build-KICK-dKeptSession-53-deviation-531.md) | deviation | — |
| [2026-10-26-review-KICK-dKeptSession-45-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-45-spec-audit.md) | spec-audit | KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-55 KICK-dKeptSession-56 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build's fifteen round-1 promotions
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md`)
confirmed finding **id 4 at HIGH**, report item **H6**, which no other id shares. The skeptic judged
the finder's fix UNSOUND, and this unit takes the skeptic's corrected fix.

`KICK-dKeptSession-42` S2 acknowledges the row `check_interface_notice` names current and "every
earlier open `confirmed` or `changed` from the same parent, earlier by `first-seen`".
`KICK-dKeptSession-27` S5 says the check never chooses a row by `first-seen`, `seq` or fetch order,
and its red case (AC4) has a take-over's `changed` K2 sighted first and the predecessor's `confirmed`
K1 sighted later. There the check names K2 current, S2 acks K2 and the rows sighted before it, and
K1, sighted later, stays open, so `KICK-dKeptSession-5` S9's guard refuses the dependent's
transition until `flow.wait-ceiling`, 72 hours or 168 under strict: the stall unit 42 exists to
remove. This unit orders the parent's rows by what they say and by the chain unit 27 records. It
repairs `KICK-dKeptSession-42` and builds one step after it (order 26).

## 2. Scope (IN)

- **S1** — id 4. The chain. `derive_mail_chain(rows)` in `tools/loop/loop_transition.py`, over one
  parent's `read_mailbox` rows (`KICK-dKeptSession-5` S6, with `KICK-dKeptSession-27` S4's `seq`,
  `after` and `ref` columns), answers whether row R precedes row C: R and C share a `ref` and R's
  `seq` is lower, or C's ref's `seq` 1 row names in `after` a row that R precedes or is, applied
  transitively. `first-seen` and fetch order are never read. Observed by AC1 and AC2.
- **S2** — id 4. What the current row supersedes. Where `check_interface_notice` prints `interface —
  current <id>`, `write_consumed_acks` acknowledges that row, every open `confirmed` or `changed` row
  from the same parent whose `content-key` equals the current key, and every one the chain places
  before the current row. A row the chain places after it, or cannot place at all, stays open and the
  guard names it. `help/loop.md`'s guard table says a row is superseded "by content key or by the
  session chain". Observed by AC1, AC2, AC3 and AC4.
- **S3** — id 4. The sibling text superseded by name. `KICK-dKeptSession-42` S2's "earlier by
  `first-seen`" reads as S1 and S2 here, and unit 42 §4's table row "superseded by a current one"
  means superseded by key or by the chain. Answered in unit 42's acceptance ledger. Observed by AC1.

## 3. Non-goals (OUT)

- Which row is current: `KICK-dKeptSession-27` S5's `check_interface_notice`, unchanged.
- When the acks are posted relative to the guard: id 49, `KICK-dKeptSession-55`.
- An order across two builds' messages: unit 27 §3 records that none exists or is needed.
- The report's left-shift checklist entry, that a spec ordering rows cites its source unit's rule.
  No clause of this build names that checklist; AC1 is its arm here.

### Edges

- **consumes-from** `KICK-dKeptSession-42` — `write_consumed_acks`' S2, whose "earlier by `first-seen`" this unit replaces with the key and chain rule (id 4)
- **consumes-from** `KICK-dKeptSession-27` — the `seq`, `after` and `content-key` columns of `read_mailbox`'s row, from which S1 derives the chain
- **hands-off** `KICK-dKeptSession-61` — `derive_mail_chain` and its S1 rule, which that unit runs over every row on the parent's refs (id 31)
- **hands-off** `KICK-dKeptSession-62` — the chain's arm and the order it reads, whose leg the batch's S1 records and on which S9's re-posts are placed (ids 2, 7)
- **hands-off** `KICK-dKeptSession-63` — `derive_mail_chain`'s AC2, its selftest arm and S1's ledger answer, which the batch's S6, S20 and S22 move to the two-argument form and read (ids 3, 8, 19)

## 4. Design

### Evidence

- spec-42 S2: "the writer acknowledges that row and every earlier open `confirmed` or `changed` from
  the same parent, earlier by `first-seen`".
- spec-27 S1 and S2: `seq` is a message's first-parent depth on its own ref; `after` names, on a
  session's `seq` 1 message, the newest message on the build's other cached refs, else `none`. S5:
  the check "never chooses a row by `first-seen`, `seq` or fetch order"; AC4 plants the `changed`
  sighted first.

### The take-over case

```
ref s1:  seq 1 confirmed K1 (id a)                      first-seen 10:05
ref s2:  seq 1 changed   K2 (id b) after: a             first-seen 10:01
check_interface_notice -> current b
chain: a precedes b (s2's seq 1 names a in after)      -> ack b, ack a
first-seen rule (unit 42 S2):  a is later than b        -> a stays open, the guard refuses
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_mail_chain` | function, `tools/loop/loop_transition.py` | `py.function`, `derive`, asked at the pass |

### Migration

None: no notice exists before `KICK-dKeptSession-7`.

### Files touched (estimate)

- `tools/loop/loop_transition.py`: S1, and S2 in `write_consumed_acks`
- `tools/loop/selftest.py`: the cases of §6
- `help/loop.md`: the guard table's superseded row, S2

### Alternatives rejected

- **Acking every row except a `changed` whose key is not current**, the finder's second option. It
  leaves an older superseded `changed` with a stale key open, which recreates the stall.
- **Ordering by `seq` alone.** `seq` orders one session's messages; a take-over starts at `seq` 1
  again, so only `after` links the two sessions.

## 5. Production-readiness checklist

- security — none beyond unit 42's: the acks pass through `--mail ack`.
- perf / scale — one pass over one parent's rows per transition.
- error / empty / loading states — a row with no `seq` reads `-` (unit 27 S4) and is placed by
  nothing, so it stays open and is named.
- observability — the guard's refusal names every row left open.
- risks — two sessions writing one parent's notices at once, with no take-over, leave each other
  unplaced; the guard names the row, which fails closed.
- testing — the cases of §6 and the arm in §7.
- migration — none.
- user docs — `help/loop.md`'s guard table (unit 42 §5) names the key and chain rule, S2 and AC4.

## 6. Acceptance criteria

The fixture is `KICK-dKeptSession-42`'s two-build scratch repository with a bare origin under
`%TEMP%` and `RUN_CLAIMS=on`, with `KICK-dKeptSession-27` AC4's plant: session `s1`'s `confirmed`
of key K1, then a take-over session `s2`'s `changed` of key K2, the `changed` sighted first.

- **AC1** — When the dependent, whose listing recomputes K2, runs one `python loop_transition.py
  record` with no manual ack, the transition succeeds and `--mail read <dependent>` shows both rows
  `acked`.
  Red when: the predecessor's `confirmed`, sighted later, stays `open` and the guard refuses, as the
  `first-seen` rule leaves it.
- **AC2** — When a probe calls `derive_mail_chain` over that plant's rows, it answers that `s1`'s row
  precedes `s2`'s, and over the same rows with `first-seen` swapped it answers the same.
  Red when: the answer moves with arrival order.
- **AC3** — When `s2` posts a second `changed` of key K3 after K2 and the dependent recomputes K2,
  the transition is refused naming the K3 row, which stays `open`.
  Red when: a row the chain places after the current one is acked unconsumed.
- **AC4** — When `grep -n "content key or by the session chain" loop.md` runs in `help/`, it prints
  the guard table's row for a superseded `confirmed` or `changed`.
  Red when: the owner's page still describes supersession by arrival.

## 7. Gates

`lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/selftest.py · covers AC1 AC2 AC3 · unit 27's take-over plant with the `changed` sighted first, and a later key, staged red by a copy of `write_consumed_acks` ordering by `first-seen` · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 promotions' audit, H6 (id 4).
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-61`, `KICK-dKeptSession-62`
  mirrored, the other ends of the edges the round-2 promotions' audit's disposal declared
- rev-3 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-63` mirrored, the other ends of
  the edges the round-3 promotions' audit's disposal declared

## 10. Reuse audit

The seams extended are `KICK-dKeptSession-27`'s `seq` and `after` keys, read from
`KICK-dKeptSession-5`'s `read_mailbox` row, and unit 42's `write_consumed_acks`; the chain is the
order unit 27 already writes, read rather than re-derived from arrival. `python
tools/codebase-map/reuse_lookup.py "order mailbox rows by session sequence and predecessor link"`
ranked `rows`, `row`, `extract_row` and `extract_session` by name stem only; no mail code exists at
this base, so no existing seam in the tree fits and the sibling specs are the seams.

Recall terms used: `python tools/memory-recall/query.py "which earlier notices does a consumed
interface notice supersede" --terms "seq after content-key take-over first-seen arrival order
check_interface_notice acked superseded chain"`
