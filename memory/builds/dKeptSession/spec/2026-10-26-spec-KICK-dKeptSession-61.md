# KICK-dKeptSession-61 — the session chain read over every row on the parent's refs, so a parent with two dependents is placed

**Status:** DEFERRED · rev-5 · 2026-11-21 · node a · Tier-2 · base c2a407b0 · streams kickoff · order 27 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-61-deviation-611.md](../build/2026-10-26-build-KICK-dKeptSession-61-deviation-611.md) | deviation | — |
| [2026-10-26-build-KICK-dKeptSession-61-deviation-612.md](../build/2026-10-26-build-KICK-dKeptSession-61-deviation-612.md) | deviation | — |
| [2026-11-21-build-KICK-dKeptSession-17-reground-orders-27-29-returns.md](../build/2026-11-21-build-KICK-dKeptSession-17-reground-orders-27-29-returns.md) | research | KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-41 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-17-orders-27-29-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-17-orders-27-29-reground-brief.md) | research | KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-41 |
| [2026-10-26-review-KICK-dKeptSession-57-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-57-spec-audit.md) | spec-audit | KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-57 KICK-dKeptSession-62 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build's twelve round-2 promotions
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-45-spec-audit.md`)
confirmed finding **id 31 at HIGH**, report item **H4**, which no other id shares.

`KICK-dKeptSession-53` S1 runs `derive_mail_chain` over one parent's rows of `read_mail_rows`' one
read, and `KICK-dKeptSession-5` S6 filters that read to the rows addressed to the dependent. The
`after` link the chain follows (`KICK-dKeptSession-27` S2) names the sender's newest message to any
recipient. With two dependents, which dKeptSession itself has, a take-over's `seq` 1 `after` usually
names the predecessor's row to the other dependent, absent from the filtered rows, so the
predecessor's `confirmed` is never placed, stays open, and the guard refuses until
`flow.wait-ceiling`: the stall unit 53 exists to remove. This unit gives the chain every row on the
parent's refs, read through the one mail reader, and keeps the rows it acks the filtered ones. It
repairs `KICK-dKeptSession-53` and builds one step after it (order 27).

## 2. Scope (IN)

- **S1** — id 31. The chain read, a selection of the one reader. `read_mailbox <who>
  soft|strict|local [sent]` in `tools/unattended/unattended.sh` (`KICK-dKeptSession-5` S6, with
  `KICK-dKeptSession-21` S2's `local` mode) gains `sent`: the same one `git log --first-parent
  --source` and the same one `awk`, over the cached refs `refs/gov/remote/mail/<who>/*` alone and with
  `check_mail_addressed` not applied, so it prints one row per message the build `<who>` wrote,
  whoever it was addressed to. The row is the reader's own, every column and the collapse rule
  unchanged. The verb is `--mail read <slug> --sent`, beside `--open` and `--ids`; under `--local` it
  reads the cache the dependent's own read has just fetched, with no fetch. No `read_mail_chain` and no
  `--mail chain` is minted (`KICK-dKeptSession-63` S11, §8 F1). Observed by AC1 and AC3.
- **S2** — id 31. The placement. `derive_mail_chain(rows, chain)` in `tools/loop/loop_transition.py`,
  `chain` required and with no default, answers whether R precedes C by `KICK-dKeptSession-53` S1's
  rule applied over `chain`. `write_consumed_acks(root, build, rows)` (`KICK-dKeptSession-42` S1) reads,
  for each parent it judges, that parent's `chain` through `read_mail_rows(root, build, sent=False)`
  (`KICK-dKeptSession-5` S9) called with the parent and `sent=True`, which runs `--mail read <parent>
  --local --sent` under the same launcher, bound and environment as the one read; and it picks the rows
  it acks from `rows`, the dependent's filtered read, as unit 53 S2 states. Every caller of
  `derive_mail_chain` passes `chain`, unit 53's plants included. Observed by AC1 and AC2.
- **S3** — id 31. The sibling text superseded by name. `KICK-dKeptSession-53` S1's "over one parent's
  rows of `read_mail_rows`' one read" reads as S2 here: the order is read over every row the parent
  wrote, the ack set over the rows addressed to the dependent. Answered in unit 53's acceptance
  ledger. Observed by AC1.
- **S4** — id 31. The plant `chain-two-dependents` of `python tools/loop/loop_transition.py --fixture
  --plant <case>`, in `PLANTS` and run by `run_transition_fixture`: unit 53's scratch repository with a
  second dependent, §6's fixture. Observed by AC1 to AC3.

## 3. Non-goals (OUT)

- What a row supersedes and when acks post: unit 53 S2 and `KICK-dKeptSession-55`, unchanged.
- A second fetch. S1 under `local` reads the cache the dependent's read filled, so the chain and the ack
  set come from one fetch.
- A second mode for a cache read: `KICK-dKeptSession-21` S2's `local` is that mode.
- The report's left-shift checklist entry, that a per-recipient reader's fixture has two recipients.
  No clause of this build names that checklist; AC1 is its arm here.

### Edges

- **consumes-from** `KICK-dKeptSession-53` — `derive_mail_chain` and its S1 rule, which this unit runs over every row on the parent's refs (id 31)
- **hands-off** `KICK-dKeptSession-63` — S1's chain read, S2's signature and §7's arm, which the batch's S11, S6, S7 and S22 settle on the one reader (ids 14, 3, 1, 19); S1 and S2 build them in that form
- **hands-off** `KICK-dKeptSession-64` — AC3, §4 Files touched, §5, §7's arm and the plant, which the batch's S4 reads and S5 re-points to the one reader's sent selection (ids 1, 12)
- **hands-off** `KICK-dKeptSession-65` — S2's `write_consumed_acks` and `derive_mail_chain` in the loop kit's transition, which the batch's S11 re-points, and this spec, which the batch's S10 fixture copies (ids 16, 4)

## 4. Design

### Evidence

- spec-5 rev-9 S6: `read_mailbox <who> soft|strict` prints one row per message "whose `to` passes
  `check_mail_addressed <to> <who>`", after one bounded fetch, one `git log --first-parent --source`
  over every cached mail ref and one `awk`; S9's `read_mail_rows(root, build)` runs `--mail read
  <build>`, and F9 makes that one read serve the guard and the disposal.
- spec-21 rev-4 S2: `local`, a third mode that reads the cache with no fetch, selected by `--local` on
  `--mail read`.
- spec-27 rev-5 S2: `after` names "the newest message on any other cached ref under
  `refs/gov/remote/mail/<slug>/`", whoever it was addressed to.
- spec-35 posts one notice per dependent, so a parent with two dependents writes two rows per notice.
- The row's columns, which the chain reads by position: 9 `ref`, 12 `seq`, 13 `after` (spec-5 rev-9,
  spec-27 rev-5), beside 11 `reply` and 14 to 16 `content-key`, `deadline`, `default`.
- The fixture's plants are `PLANTS` members of `tools/loop/loop_transition.py`, run by
  `tools/loop/loop_transition.py#run_transition_fixture`; no mail code is in the tree at `c2a407b0`.

### The two-dependent case

```
ref s1:  seq 1 confirmed K1 to dA (a1) · seq 2 confirmed K1 to dB (b1)
ref s2:  seq 1 changed   K2 to dA (a2) after: b1 · seq 2 changed K2 to dB (b2)
dA's filtered rows: a1, a2          -> b1 absent: a1 unplaced, stays open (unit 53)
chain rows (S1):    a1, b1, a2, b2  -> a1 precedes b1 (s1, seq), b1 is a2's after -> a1 precedes a2
dA acks a2 and a1; dB acks b2 and b1
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `sent` | selection of `read_mailbox`, `tools/unattended/unattended.sh` | none |
| `--sent` | flag of `--mail read`, `tools/unattended/unattended.sh` | none |
| `chain-two-dependents` | `PLANTS` case of `loop_transition.py --fixture` | none |

### Migration

None: no notice exists before `KICK-dKeptSession-7`.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: S1, the `sent` selection and `--sent`
- `tools/loop/loop_transition.py`: S2 in `derive_mail_chain`, `write_consumed_acks` and
  `read_mail_rows`, and S4's plant
- `tools/unattended/VERBS.template.md`: the `--mail` section's `--sent` flag

### Alternatives rejected

- **Dropping the address filter from the dependent's read.** The ack set would then hold rows
  addressed to the other dependent, which this dependent never consumed.
- **Writing `after` per recipient in unit 27.** It changes every message's record for one reader's
  need, and a take-over would still name a row the next recipient never sees when the predecessor
  wrote to it last.
- **A separate `read_mail_chain` and `--mail chain`**, as rev-4 wrote. A second walk of the same refs,
  which `KICK-dKeptSession-63` S11 rules is never minted and `KICK-dKeptSession-64` S5 would remove.

## 5. Production-readiness checklist

- security — none: one more read of refs the node already fetched; nothing is written.
- perf / scale — one `git log` and one `awk` over one build's refs per parent judged, no fetch.
- error / empty / loading states — an empty cache prints no row, so the chain places nothing and the
  guard names the open row, failing closed as unit 53 §5 states.
- observability — `--mail read <parent> --local --sent` prints the rows the placement read.
- risks — a cache older than the dependent's fetch cannot occur, since S2 reads the chain after that
  fetch in the same transition.
- testing — the criteria of §6 and the arm in §7.
- migration — none.
- user docs — the `--mail` section of `tools/unattended/VERBS.template.md` (unit 5's) names `--sent`
  beside `--open`, `--ids` and `--local`.

## 6. Acceptance criteria

The fixture is S4's plant: `KICK-dKeptSession-53`'s scratch repository under `%TEMP%`, with two
dependents `dA` and `dB`; session `s1` posts `confirmed` K1 to `dA` then `dB`, and a take-over session
`s2` posts `changed` K2 to `dA` then `dB`.

- **AC1** — When `python tools/loop/loop_transition.py --fixture --plant chain-two-dependents` has `dA`
  and then `dB` each run one `record`, both transitions succeed, and `--mail read dA` and `--mail read
  dB` show all four rows `acked`.
  Red when: a copy chaining only over the filtered rows leaves `s1`'s `confirmed` to `dA` open and
  the guard refuses.
- **AC2** — When a probe calls `derive_mail_chain` with `dA`'s filtered rows and the parent's sent
  rows, it answers that `s1`'s row to `dA` precedes `s2`'s; with the sent rows replaced by the
  filtered rows it answers that it cannot place it.
  Red when: the two calls answer alike, so the chain read added nothing.
- **AC3** — When `bash unattended.sh --mail read <parent> --local --sent` runs in that repository, it
  prints four rows, each carrying `seq` and `after` in columns 12 and 13.
  Red when: a row addressed to the other dependent is missing.

## 7. Gates

`unattended kit gate` · `scratch-guard self-test` · `tier2-review self-test` · `loop transition record` · `docs` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/loop_transition.py · covers AC1 AC2 AC3 · the two-dependent take-over plant, staged red by a copy of `derive_mail_chain` reading only the dependent's filtered rows · none

## 8. Open questions

- **F1 — Is the chain read a reader of its own or a selection of the one reader?** Options: (a)
  `read_mail_chain <slug>` and `--mail chain`, as rev-4 wrote, running `read_mailbox`'s `git log` and
  `awk` a second time; (b) a `sent` selection of `read_mailbox`, read under `KICK-dKeptSession-21` S2's
  `local` mode by `--mail read <slug> --local --sent`. RESOLVED (agent, 2026-11-21, delegated): (b),
  rung 3; `KICK-dKeptSession-63` S11 settles the chain on the one reader and rules (a)'s names never
  minted, and `local` is the landed spelling of that batch's `cache` mode, so (b) builds one reader
  and no name a later unit removes. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-2 promotions' audit, H4 (id 31).
- rev-2 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-63` mirrored, the other ends of
  the edges the round-3 promotions' audit's disposal declared
- rev-3 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-64` mirrored, the other ends of
  the edges the round-4 minors batch's audit's disposal declared
- rev-4 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-65` mirrored, the other ends of
  the edges the round-5 minors batch's audit's disposal declared
- rev-5 · 2026-11-21 · §1 · S1 to S4 · §3 · §4 · §5 · AC1 to AC3 · §7 · §8 F1 · §10 · re-grounded on
  base `c2a407b0` by `2026-11-21-prompt-KICK-dKeptSession-17-orders-27-29-reground-brief`: narrowed S1
  from a reader of its own to the one reader's `sent` selection under unit 21's `local` mode, so
  `read_mail_chain` and `--mail chain` are never minted (F1); S2 names `chain` required, the launch
  through `read_mail_rows` and the re-pointed callers; S3 re-quotes unit 53 rev-4's S1; S4 and the
  arm move from the absent `tools/loop/selftest.py` to a `loop_transition.py` plant; the columns
  numbered as spec-5 rev-9 and spec-27 rev-5 number them; the leg line names the guarded legs and
  `loop transition record`.

## 10. Reuse audit

The seam extended is the one mail reader, `read_mailbox`'s one `git log` and one `awk`
(`KICK-dKeptSession-5` S6), given a selection rather than a second walk, read under
`KICK-dKeptSession-21` S2's `local` mode rather than a second cache mode; the Python side reuses
`read_mail_rows`' one launch (`KICK-dKeptSession-5` S9) and unit 53's `derive_mail_chain`, given a wider
row set rather than a new rule; the plant joins the landed fixture
`tools/loop/loop_transition.py#run_transition_fixture`. `python tools/codebase-map/reuse_lookup.py
"order mailbox rows across every session ref of one build"` ranked `rows`, `row`, `build` and
`build_records` by name stem only; no mail code is in the tree at `c2a407b0`, so no existing seam in
the tree fits and the sibling specs are the seams.

Recall terms used: `python tools/memory-recall/query.py "how is a promoted unit placed when it
repairs an earlier unit's pass" --terms "promoted order pass commit ledger superseded batch minors
hands-off consumes-from parity mirror"`
