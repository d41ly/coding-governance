# KICK-dKeptSession-55 — the transition writer acknowledges notices only when the guard would then pass, and prints each one it consumed

**Status:** OPEN · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 26 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 |
| [2026-10-26-build-KICK-dKeptSession-55-deviation-551.md](../build/2026-10-26-build-KICK-dKeptSession-55-deviation-551.md) | deviation | — |
| [2026-10-26-review-KICK-dKeptSession-45-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-45-spec-audit.md) | spec-audit | KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-56 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build's fifteen round-1 promotions
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md`)
confirmed finding **id 49 at HIGH**, report item **H9**, which no other id shares. The skeptic judged
the finder's fix UNSOUND, and this unit takes the skeptic's corrected fix.

`KICK-dKeptSession-42` S1 acknowledges every open `landed`, `superseded` and `withdrawn` row before
`KICK-dKeptSession-5` S9's guard reads, and prints nothing. Nothing makes the ack wait for the
guard's verdict on the other rows. So a `withdrawn` parent notice is consumed and never shown; under
`mailbox.reads = transitions-only` (`KICK-dKeptSession-10` S3) the transition is the only read, so
it is never surfaced at all. And if an open `question` then refuses the transition, the ack has
already landed, so the next transition passes and the dependent builds on a withdrawn parent: the
outcome unit 42 §4 rejects ("would let a `withdrawn` parent pass unread"). This unit makes the
consuming write conditional on the guard's verdict and visible. It repairs `KICK-dKeptSession-42`
and builds one step after it (order 26).

## 2. Scope (IN)

- **S1** — id 49. List first. `write_consumed_acks` in `tools/loop/loop_transition.py` first reads
  the build's open rows once, `--mail read <slug> --open`, and computes the ids it would consume: unit
  42 S1's kinds and S2's interface rows. Observed by AC1 and AC2.
- **S2** — id 49. All or nothing. It posts the acks only when every open row addressed to the build
  is one it consumes, so the guard then reads zero rows. Otherwise it posts none, and the guard
  refuses as `KICK-dKeptSession-5` S9 states, listing every open row, the consumable ones included.
  Observed by AC2.
- **S3** — id 49. Each ack shown. For every ack it posts, the writer prints `mail — acked <kind>
  <id> from build:<parent>` on the transition's output, before the guard's lines, so a `withdrawn`
  notice is read by whoever reads the transition. `help/loop.md`'s guard paragraph names the line and
  S2's rule. Observed by AC1 and AC3.
- **S4** — id 49. The sibling text superseded by name. `KICK-dKeptSession-42` S1's "Before
  `KICK-dKeptSession-5` S9's guard reads the open rows, `write_transition` acknowledges every open
  row ..." reads as S1 to S3 here, and unit 42 S3's per-id posts run only under S2's condition.
  Answered in unit 42's acceptance ledger. Observed by AC2.

## 3. Non-goals (OUT)

- Which interface rows are consumed: unit 42 S2, with id 4's chain rule, `KICK-dKeptSession-53`.
- An ack that fails to post: unit 42 S3, and the batch's item for id 50, `KICK-dKeptSession-56`.
- The report's left-shift checklist entry, that a consuming write ahead of a guard is conditional on
  its verdict and prints what it consumed. No clause of this build names that checklist; AC2 is its
  arm here.

### Edges

- **consumes-from** `KICK-dKeptSession-42` — `write_consumed_acks` and its S1 and S3, which this unit makes conditional on the guard's verdict and visible (id 49)
- **hands-off** `KICK-dKeptSession-56` — the listed open rows and the all-or-nothing post, inside which the batch's item for id 50 prices an ack refused for no session id or no remote
- **hands-off** `KICK-dKeptSession-62` — the listed rows, the guard's read and the ack loop, which the batch's S14 and S15 make one read and one ref update, and whose leg S1 records (ids 15, 32, 2)

## 4. Design

### Evidence

- spec-42 S1: the acks run "before `KICK-dKeptSession-5` S9's guard reads the open rows", with no
  output line; spec-42 §4: notice kinds that never gate "would let a `withdrawn` parent pass unread".
- spec-5 S9: open rows exit 1 printing `refused — <slug> · mail open <id> …` and write nothing.
- spec-10 S3: under `transitions-only` the item boundary runs no mail read.

### The step

```
open   := --mail read <slug> --open
eat    := { r in open : r.kind in (landed, superseded, withdrawn) } + S2-of-unit-42(open)
if open == eat:  for r in eat: --mail ack <slug> r.id ; print "mail — acked <kind> <id> from build:<parent>"
else:            post nothing        -> the guard refuses, naming every row of open
```

### Inventory

No identifier is minted; `mail — acked` is a line of the existing writer.

### Migration

None: no notice exists before `KICK-dKeptSession-7`.

### Files touched (estimate)

- `tools/loop/loop_transition.py`: S1 to S3 in `write_consumed_acks`
- `tools/loop/selftest.py`: the cases of §6
- `help/loop.md`: S3's sentence in the guard paragraph

### Alternatives rejected

- **Acking first and un-acking on a refusal.** The mail refs are append-only (`KICK-dKeptSession-5`
  S1), so a retracted ack is a second message every reader must reconcile.
- **Acking the consumable rows whatever the guard says.** It is the defect: the consumed notice is
  gone when the refusal is cleared.

## 5. Production-readiness checklist

- security — none beyond unit 42's.
- perf / scale — the one open-row read the guard already makes, run once before it.
- error / empty / loading states — a read that fails leaves `open` unknown, so nothing is posted and
  the guard's own read decides.
- observability — S3's line per consumed notice.
- risks — a dependent with a standing open `question` acks nothing until it is answered, so its
  parent's notices stay listed beside the question; that is the guard's listing, by design.
- testing — the cases of §6 and the arm in §7.
- migration — none.
- user docs — `help/loop.md`'s guard paragraph names the all-or-nothing rule and the `mail — acked`
  line, S3 and AC3.

## 6. Acceptance criteria

The fixture is `KICK-dKeptSession-42`'s two-build scratch repository with a bare origin under
`%TEMP%` and `RUN_CLAIMS=on`.

- **AC1** — When the parent posts `withdrawn` and the dependent runs one `python loop_transition.py
  record` with nothing else open, it succeeds and prints `mail — acked withdrawn <id> from
  build:<parent>`.
  Red when: the `withdrawn` row is acked with no line, so the transition's reader never sees it.
- **AC2** — When the parent posts `withdrawn` and a third build posts an open `question` to the
  dependent, the dependent's transition is refused listing both ids, and `--mail read <dependent>`
  still shows the `withdrawn` row `open`.
  Red when: the `withdrawn` row reads `acked` after the refusal, so the next transition passes it
  unread.
- **AC3** — When `grep -n "mail — acked" loop.md` runs in `help/`, it prints the guard paragraph's
  sentence naming the all-or-nothing rule.
  Red when: the owner's page does not say a consumed notice is printed, or that a refusal acks
  nothing.

## 7. Gates

`lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/selftest.py · covers AC1 AC2 · a lone `withdrawn`, and a `withdrawn` beside an open `question`, staged red by a copy of `write_consumed_acks` that acks before the guard reads · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 promotions' audit, H9 (id 49).
- rev-2 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-62` mirrored, the other ends of
  the edges the round-2 promotions' audit's disposal declared

## 10. Reuse audit

The seams extended are unit 42's `write_consumed_acks`, `KICK-dKeptSession-5`'s `--mail read --open`
reader and `--mail ack` verb; the open-row list is the guard's own read, run first. `python
tools/codebase-map/reuse_lookup.py "acknowledge consumed rows only when the guard would pass"` ranked
`rows`, `row`, `extract_row` and `check_gen_region_only` by name stem only; no mail code exists at
this base, so no existing seam in the tree fits and the sibling specs are the seams.

Recall terms used: `python tools/memory-recall/query.py "when may a transition acknowledge a
withdrawn notice" --terms "withdrawn landed superseded ack open question guard refused transitions-only
write_consumed_acks consumed visible"`
