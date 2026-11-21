# KICK-dKeptSession-55 — the transition writer acknowledges notices only when the guard would then pass, and prints each one it consumed

**Status:** DEFERRED · rev-5 · 2026-11-22 · node a · Tier-2 · base c2a407b0 · streams kickoff · order 26 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-55-deviation-551.md](../build/2026-10-26-build-KICK-dKeptSession-55-deviation-551.md) | deviation | — |
| [2026-11-21-build-KICK-dKeptSession-10-reground-orders-20-26-returns.md](../build/2026-11-21-build-KICK-dKeptSession-10-reground-orders-20-26-returns.md) | research | KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-1 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-35-orders-25-26-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-35-orders-25-26-reground-brief.md) | research | KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-52 KICK-dKeptSession-53 |
| [2026-11-21-prompt-KICK-dKeptSession-50-divergence-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-50-divergence-brief.md) | research | KICK-dKeptSession-50 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-51 KICK-dKeptSession-53 KICK-dKeptSession-61 |
| [2026-11-21-prompt-KICK-dKeptSession-7-precheck-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-7-precheck-brief.md) | research | KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 |
| [2026-10-26-review-KICK-dKeptSession-45-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-45-spec-audit.md) | spec-audit | KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-56 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build's fifteen round-1 promotions
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md`)
confirmed finding **id 49 at HIGH**, report item **H9**, which no other id shares. The skeptic judged
the finder's fix UNSOUND, and this unit takes the skeptic's corrected fix.

`KICK-dKeptSession-42` S1 acknowledges every open `landed`, `superseded` and `withdrawn` row ahead of
`KICK-dKeptSession-5` S9's open-row refusal, and prints nothing. Nothing makes the ack wait for the
guard's verdict on the other rows. So a `withdrawn` parent notice is consumed and never shown; under
`mailbox.reads = transitions-only` (`KICK-dKeptSession-10` S3) the transition is the only read, so
it is never surfaced at all. And if an open `question` then refuses the transition, the ack has
already landed, so the next transition passes and the dependent builds on a withdrawn parent: the
outcome unit 42 §4 rejects ("would let a `withdrawn` parent pass unread"). This unit makes the
consuming write conditional on the guard's verdict and visible. It repairs `KICK-dKeptSession-42`
and builds one step after it (order 26).

## 2. Scope (IN)

- **S1** — id 49. List first. `write_consumed_acks` in `tools/loop/loop_transition.py` takes the
  open rows of unit 5's single unfiltered read, `read_mail_rows(root, build)` (`KICK-dKeptSession-5`
  S9 and F9), the rows whose `state`, column 4, is `open`, and computes the ids it would consume:
  unit 42 S1's kinds and S2's interface rows. It makes no read of its own. Observed by AC1 and AC2.
- **S2** — id 49. All or nothing. It posts the acks only when every open row addressed to the build
  is one it consumes, so the guard then judges zero rows. Otherwise it posts none, and the guard
  refuses as `KICK-dKeptSession-5` S9 states, listing every open row, the consumable ones included.
  Observed by AC2.
- **S3** — id 49. Each ack shown. For every ack it posts, the writer prints `mail — acked <kind>
  <id> from build:<parent>` among the lines `write_transition` returns, ahead of the guard's lines,
  so a `withdrawn` notice is read by whoever reads the transition. `help/loop.md`'s guard paragraph
  names the line and S2's rule. Observed by AC1 and AC3.
- **S4** — id 49. The sibling text superseded by name. `KICK-dKeptSession-42` S1's "It acknowledges
  every row whose `state`, column 4, is `open` and whose `kind` … is `landed`, `superseded` or
  `withdrawn`" reads as S1 to S3 here, and unit 42 S3's per-id posts run only under S2's condition.
  Answered in this unit's own acceptance ledger,
  `memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-55-1-acceptance-ledger.md`,
  which quotes unit 42 S1's sentence and S3's "It runs once per id and only while the row reads
  `open`", and states S1 to S3 here supersede them. Unit 42 builds at order 25 and is CLOSED when
  this unit builds, so neither its spec nor its ledger is written (F1). Observed by AC2 and AC4.
- **S5** — The budget row. `acks-withdrawn` and `acks-withdrawn-question` move the `plants=<n>`
  token of the `loop transition record` row in `tools/run-gates/selftest-budgets.txt`, re-priced as
  §4's budget row states. Both are branches of `run_transition_fixture`, as `KICK-dKeptSession-36`
  S4's are, so no plant adds a module-level symbol and `memory/map/generated/symbols.json` does not
  move. Observed by AC5.

## 3. Non-goals (OUT)

- Which interface rows are consumed: unit 42 S2, with id 4's chain rule, `KICK-dKeptSession-53`.
- An ack that fails to post: unit 42 S3, and the batch's item for id 50, `KICK-dKeptSession-56`.
- An `expired` row: the guard passes it and unit 5 S10 disposes it (`KICK-dKeptSession-24` S5),
  so it is neither consumed nor printed here.
- The report's left-shift checklist entry, that a consuming write ahead of a guard is conditional on
  its verdict and prints what it consumed. No clause of this build names that checklist; AC2 is its
  arm here.

### Edges

- **consumes-from** `KICK-dKeptSession-42` — `write_consumed_acks` and its S1 and S3, which this unit makes conditional on the guard's verdict and visible (id 49)
- **hands-off** `KICK-dKeptSession-56` — the listed open rows and the all-or-nothing post, inside which the batch's item for id 50 prices an ack refused for no session id or no remote
- **hands-off** `KICK-dKeptSession-62` — the listed rows, the guard's read and the ack loop, which the batch's S14 and S15 make one read and one ref update, and whose leg S1 records (ids 15, 32, 2)

## 4. Design

### Evidence

- spec-42 S1: the acks run between unit 5's `read_mail_rows` read and its open-row refusal, with no
  output line; spec-42 §4: notice kinds that never gate "would let a `withdrawn` parent pass unread".
- spec-5 S9: open rows raise `TransitionRefused`, which `record` prints as
  `refused — <slug> · mail open <id> …` and exits 1, writing nothing; F9: one read serves the guard
  and the disposal, so an `--open` read beside it is a second snapshot.
- spec-10 S3: under `transitions-only` the item boundary runs no mail read.
- `write_transition` returns its printed lines as `said`, which `record` prints after the move
  (`tools/loop/loop_transition.py#write_transition`).

### The step

```
open   := { r in read_mail_rows(root, build) : r.state == open }
eat    := { r in open : r.kind in (landed, superseded, withdrawn) } + S2-of-unit-42(open)
if open == eat:  for r in eat: --mail ack <slug> r.id ; say "mail — acked <kind> <id> from build:<parent>"
else:            post nothing        -> the guard refuses, naming every row of open
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `acks-withdrawn`, `acks-withdrawn-question` | `--plant` cases of `loop_transition.py --fixture` | none |

`mail — acked` is a line of the existing writer.

### Migration

None: no notice exists before `KICK-dKeptSession-7`.

### The budget row

`check_plant_tokens` holds the `plants=<n>` token of each loop-kit row equal to `len(PLANTS)` of the
module its argv runs, once imported, and refuses a note carrying two tokens
(`tools/run-gates/run-selftests.sh#check_plant_tokens`). The `loop transition record` row runs
`loop_transition.py check --selftest`. Units ordered before this one add thirteen plants,
KICK-dKeptSession-5's two, -36's three, -24's one, -7's one, -35's two and -42's four, and the units
of this unit's step add up to eight more, KICK-dKeptSession-11's five, -52's one and -53's two. So S5
moves the token from 26 to 28, or from as high as 34 to 36 where those land first (DERIVED:
`len(PLANTS)` read at 7df6a1dac, 13, plus those units' plants). The builder re-reads the count at the
unit's base and moves the one token in place, two above it.

| Figure | `loop transition record` |
|---|---|
| proxy `r` at this tree, the row's note (PINNED 2026-11-21) | 33.4 s over 13 plants |
| the earlier units' plants, estimates (PINNED 2026-11-22) | 13 times 9 s, and up to 3 times 9 s and 5 times 3 s more |
| this unit's plants, estimates (PINNED 2026-11-22) | 2 times 9 s |
| `r` after this unit (PINNED 2026-11-22, the sum) | 168.4 s, up to 210.4 s |
| budget, max of the row's value and 1.5 `r` | 253, up to 316 |
| the leg's ceiling in `tools/gate-legs.json` | 120, under the 150.4 s base |

The 9 s estimates (PINNED 2026-11-22) are the `backward-rows` plant's 8.2 s, the module's slowest,
rounded up, read alone by direct CLI on the run's node at 7df6a1dac, since each plant builds a
scratch repository with a second build or a bare origin; the 3 s ones (PINNED 2026-11-22) are
unit 11's five `notify-*` plants, as unit 11's spec states. The builder reads each new plant alone
by direct CLI and appends `Then re-read by KICK-dKeptSession-55 as PINNED proxy r <s>` to the row's
note, with the budget the row's value or 1.5 `r` rounded up, whichever is higher. The leg has no row
in `tools/run-gates/ceiling-evidence.txt`, so no evidenced maximum moves. By these estimates the
row's `r` passes the leg's 120 s ceiling (PINNED 2026-11-22) at step 25, before this unit. A declared ceiling is the owner's to move
(`memory/guides/BUILD-METHOD.md`, M3): where the builder's reading takes `r` to the ceiling the leg
carries at the unit's base, the unit stops before it lands and names the raise for the owner, and it
never edits `tools/gate-legs.json`.

### Files touched (estimate)

- `tools/loop/loop_transition.py`: S1 to S3 in `write_consumed_acks`, and the two plants
- `tools/run-gates/selftest-budgets.txt`: S5, the `loop transition record` row's `plants=` token
  two above its count at the unit's base and its note's re-read (DERIVED: `len(PLANTS)`)
- `help/loop.md`: S3's sentence in the guard paragraph
- `memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-55-1-acceptance-ledger.md`:
  S4's answer beside the criteria observed

### Alternatives rejected

- **Acking first and un-acking on a refusal.** The mail refs are append-only (`KICK-dKeptSession-5`
  S1), so a retracted ack is a second message every reader must reconcile.
- **Acking the consumable rows whatever the guard says.** It is the defect: the consumed notice is
  gone when the refusal is cleared.
- **A second `--mail read --open` before the guard.** Unit 5's F9 rules one snapshot for the guard
  and the disposal; a reply landing between two reads splits the judgments.

## 5. Production-readiness checklist

- security — none beyond unit 42's.
- perf / scale — no read beyond the guard's one, which the writer filters in memory.
- error / empty / loading states — a read that fails refuses the transition through unit 5's
  guard before this step runs, so nothing is posted.
- observability — S3's line per consumed notice.
- risks — a dependent with a standing open `question` acks nothing until it is answered, so its
  parent's notices stay listed beside the question; that is the guard's listing, by design. A move
  the table refuses after the guard passed has still acked, and printed, what it consumed.
- testing — the cases of §6 and the arm in §7.
- migration — none.
- user docs — `help/loop.md`'s guard paragraph names the all-or-nothing rule and the `mail — acked`
  line, S3 and AC3.

## 6. Acceptance criteria

The fixture is `KICK-dKeptSession-42`'s two-build scratch repository with a bare origin under
`%TEMP%` and `RUN_CLAIMS=on`.

- **AC1** — When `python tools/loop/loop_transition.py --fixture --plant acks-withdrawn` has the
  parent post `withdrawn` and the dependent run one `record` with nothing else open, it succeeds and
  prints `mail — acked withdrawn <id> from build:<parent>`.
  Red when: the `withdrawn` row is acked with no line, so the transition's reader never sees it.
- **AC2** — When `--plant acks-withdrawn-question` has the parent post `withdrawn` and a third build
  post an open `question` to the dependent, the dependent's transition is refused listing both ids,
  and `--mail read <dependent>` still shows the `withdrawn` row `open`.
  Red when: the `withdrawn` row reads `acked` after the refusal, so the next transition passes it
  unread.
- **AC3** — When `grep -n "mail — acked" loop.md` runs in `help/`, it prints the guard paragraph's
  sentence naming the all-or-nothing rule.
  Red when: the owner's page does not say a consumed notice is printed, or that a refusal acks
  nothing.
- **AC4** — `tr -s ' \r\n' ' '` over this unit's acceptance ledger piped into `grep -c "It
  acknowledges every row whose"` prints `1`, and into `grep -c "It runs once per id and only while
  the row reads"` prints `1`; and `git diff --name-only <pass base> HEAD --` over unit 42's spec and
  its acceptance ledger prints nothing.
  Red when: S4's answer lands in a record of unit 42, or this unit's ledger quotes neither passage.
- **AC5** — When, at the unit's commit,
  `python -I -c "import sys; sys.path.insert(0, 'tools/loop'); import loop_transition as m; print(len(m.PLANTS))"`
  runs, it prints the number that
  `grep -oP '^loop transition record\t.*\Kplants=\d+' tools/run-gates/selftest-budgets.txt`
  prints after `plants=`, and `acks-withdrawn` and `acks-withdrawn-question` are among the keys of
  `PLANTS`.
  Red when: the row still carries the count from before this unit's plants.
  figure: PINNED 2026-11-22 at `7df6a1dac`, the probe prints `13` and the grep `plants=13`, before
  the units ordered ahead of this one land.

## 7. Gates

`loop transition record` · `every held leg is budgeted, every budget row resolves` · `policy fixtures` · `docs` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/loop_transition.py · covers AC1 AC2 · a lone `withdrawn`, and a `withdrawn` beside an open `question`, staged red by a scratch copy of `write_consumed_acks` that acks whatever the guard then reads · the `loop transition record` row's `plants=<n>` token rises by two

## 8. Open questions

- **F1 — Where is S4's answer to unit 42's superseded wording recorded?** Unit 42 builds at order
  25, one step before this unit, so it is CLOSED when this unit builds, and its ledger is in neither
  this unit's Files touched nor its write set. (a) Unit 42's acceptance ledger, a record of a closed
  unit written by a later one; (b) this unit's own acceptance ledger, quoting the unit 42 spec text
  it supersedes. Recommendation (b). RESOLVED (agent, 2026-11-21, delegated): (b), rung 3; a CLOSED
  unit's records are never written by a later unit, as KICK-dKeptSession-49 rev-6 ruled. Rejected:
  (a), writing the earlier unit's ledger. The main loop's ruling, in
  `2026-11-21-prompt-KICK-dKeptSession-50-divergence-brief`.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 promotions' audit, H9 (id 49).
- rev-2 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-62` mirrored, the other ends of
  the edges the round-2 promotions' audit's disposal declared
- rev-3 · 2026-11-21 · §1 · S1 · S3 · S4 · §3 · §4 · §5 · AC1 · AC2 · §7 · §10 · re-grounded on base
  c2a407b0 by `2026-11-21-prompt-KICK-dKeptSession-35-orders-25-26-reground-brief`: S1's
  `--open` row set reads as the open rows of unit 5's single unfiltered `read_mail_rows` read
  (spec-5 F9); S3 prints among the lines `write_transition` returns; S4 quotes unit 42 rev-3's S1;
  the `expired` state of spec-24 named in §3; the arm moves from the absent `tools/loop/selftest.py`
  to `loop_transition.py`'s plants; the leg line gains `loop transition record` and `docs`.
  Narrowed: no read of this unit's own, since the guard's one read serves it.
- rev-4 · 2026-11-21 · S4 · §4 · AC4 · §7 · §8 · S4's answer to unit 42 moves to this unit's own
  acceptance ledger, which joins Files touched and trips the two `recall floor` legs now on §7's leg
  line; F1 resolved (b) and AC4 observing the quoted passages, under the brief
  `2026-11-21-prompt-KICK-dKeptSession-50-divergence-brief`; the class of `KICK-dKeptSession-50`'s
  divergence, which unit 49's rev-6 first resolved. S4 names unit 42 S3's sentence it supersedes.
  `policy fixtures`, whose guard holds `tools/loop/`, joins the leg line too.
- rev-5 · 2026-11-22 · S5 · §4 · §4 Files touched · AC5 · §7 · by
  `2026-11-22-prompt-KICK-dKeptSession-7-1-spec-writer`: the two plants move the `plants=<n>` token
  `check_plant_tokens` grades, which siblings 11, 52, 53 and 61 already count, so S5 and AC5 observe
  it, `tools/run-gates/selftest-budgets.txt` joins Files touched, §4 states the row's re-price and the
  stop at the leg's ceiling, and §7 names the budget leg and the token's rise.

## 10. Reuse audit

The seams extended are unit 42's `write_consumed_acks`, `KICK-dKeptSession-5`'s one `read_mail_rows`
read and its `--mail ack` verb, and the `said` lines `tools/loop/loop_transition.py#write_transition`
returns; the open-row list is the guard's own read, filtered in memory. `python
tools/codebase-map/reuse_lookup.py "acknowledge consumed rows only when the guard would pass"`
ranked `rows`, `row`, `parse_unit_rows` and `read_catalogue_row` by the name stem `row` only; no mail
code is in the tree at c2a407b0, so no other seam fits and the sibling specs are the seams.

Recall terms used: `python tools/memory-recall/query.py "when may a transition acknowledge a
withdrawn notice" --terms "withdrawn landed superseded ack open question guard refused transitions-only
write_consumed_acks consumed visible"`
