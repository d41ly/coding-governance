# KICK-dKeptSession-61 — the session chain read over every row on the parent's refs, so a parent with two dependents is placed

**Status:** OPEN · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 27 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-62 KICK-dKeptSession-63 |
| [2026-10-26-build-KICK-dKeptSession-61-deviation-611.md](../build/2026-10-26-build-KICK-dKeptSession-61-deviation-611.md) | deviation | — |
| [2026-10-26-review-KICK-dKeptSession-57-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-57-spec-audit.md) | spec-audit | KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-57 KICK-dKeptSession-62 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build's twelve round-2 promotions
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-45-spec-audit.md`)
confirmed finding **id 31 at HIGH**, report item **H4**, which no other id shares.

`KICK-dKeptSession-53` S1 runs `derive_mail_chain` over one dependent's `read_mailbox` rows, which
`KICK-dKeptSession-5` S6 filters to the rows addressed to that dependent. The `after` link it follows
(`KICK-dKeptSession-27` S2) names the sender's newest message to any recipient. With two dependents,
which dKeptSession itself has, a take-over's `seq` 1 `after` usually names the predecessor's row to
the other dependent, absent from the filtered rows, so the predecessor's `confirmed` is never placed,
stays open, and the guard refuses until `flow.wait-ceiling`: the stall unit 53 exists to remove. This
unit gives the chain every row on the parent's refs, and keeps the rows it acks the filtered ones. It
repairs `KICK-dKeptSession-53` and builds one step after it (order 27).

## 2. Scope (IN)

- **S1** — id 31. The chain read. `read_mail_chain <slug>` in `tools/unattended/unattended.sh` runs
  `read_mailbox`'s one `git log --source --first-parent` and its one `awk` over the cached refs
  `refs/gov/remote/mail/<slug>/*` with the address filter off, and prints one tab-separated row per
  message: `id`, `ref`, `seq`, `after`. It fetches nothing: it reads the cache the dependent's `--mail
  read` has just fetched. The verb is `--mail chain <slug>`, beside `--mail read` in the dispatch
  table. Observed by AC1 and AC3.
- **S2** — id 31. The placement. `derive_mail_chain(rows, chain)` in `tools/loop/loop_transition.py`
  answers whether R precedes C by `KICK-dKeptSession-53` S1's rule applied over `chain`, the
  parent's `--mail chain` rows, while `write_consumed_acks` picks the rows it acks from `rows`, the
  dependent's filtered read, as unit 53 S2 states. Observed by AC1 and AC2.
- **S3** — id 31. The sibling text superseded by name. `KICK-dKeptSession-53` S1's "over one parent's
  `read_mailbox` rows" reads as S2 here: the order is read over every row the parent wrote, the ack
  set over the rows addressed to the dependent. Answered in unit 53's acceptance ledger. Observed by
  AC1.

## 3. Non-goals (OUT)

- What a row supersedes and when acks post: unit 53 S2 and `KICK-dKeptSession-55`, unchanged.
- A second fetch. S1 reads the cache the dependent's read filled, so the chain and the ack set come
  from one fetch.
- The report's left-shift checklist entry, that a per-recipient reader's fixture has two recipients.
  No clause of this build names that checklist; AC1 is its arm here.

### Edges

- **consumes-from** `KICK-dKeptSession-53` — `derive_mail_chain` and its S1 rule, which this unit runs over every row on the parent's refs (id 31)
- **hands-off** `KICK-dKeptSession-63` — S1's chain read, S2's signature and §7's arm, which the batch's S11, S6, S7 and S22 settle on the one reader (ids 14, 3, 1, 19)

## 4. Design

### Evidence

- spec-5 S6: `read_mailbox` prints one row per message "whose `to` passes `check_mail_addressed <to>
  <who>`", after one `git log --source --first-parent` over every cached mail ref and one `awk`.
- spec-27 S2: `after` names "the newest message on any other cached ref under
  `refs/gov/remote/mail/<slug>/`", whoever it was addressed to.
- spec-35 posts one notice per dependent, so a parent with two dependents writes two rows per notice.

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
| `read_mail_chain` | shell function, `tools/unattended/unattended.sh` | `read`, asked at the pass |
| `--mail chain` | verb, `tools/unattended/unattended.sh` | none |

### Migration

None: no notice exists before `KICK-dKeptSession-7`.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: S1, `read_mail_chain` and the verb
- `tools/loop/loop_transition.py`: S2 in `derive_mail_chain` and its caller
- `tools/loop/selftest.py`: the case of §6
- `tools/unattended/VERBS.template.md`: the `--mail` section's `--mail chain` line

### Alternatives rejected

- **Dropping the address filter from the dependent's read.** The ack set would then hold rows
  addressed to the other dependent, which this dependent never consumed.
- **Writing `after` per recipient in unit 27.** It changes every message's record for one reader's
  need, and a take-over would still name a row the next recipient never sees when the predecessor
  wrote to it last.

## 5. Production-readiness checklist

- security — none: one more read of refs the node already fetched; nothing is written.
- perf / scale — one `git log` and one `awk` over one build's refs per transition, no fetch.
- error / empty / loading states — an empty cache prints no row, so the chain places nothing and the
  guard names the open row, failing closed as unit 53 §5 states.
- observability — `--mail chain <slug>` prints the rows the placement read.
- risks — a cache older than the dependent's fetch cannot occur, since S1 runs after that fetch in
  the same transition.
- testing — the criteria of §6 and the arm in §7.
- migration — none.
- user docs — the `--mail` section of `tools/unattended/VERBS.template.md` (unit 5's) names `--mail
  chain` beside `--mail read`.

## 6. Acceptance criteria

The fixture is `KICK-dKeptSession-53`'s scratch repository under `%TEMP%`, with two dependents `dA`
and `dB`: session `s1` posts `confirmed` K1 to `dA` then `dB`, and a take-over session `s2` posts
`changed` K2 to `dA` then `dB`.

- **AC1** — When `dA` and then `dB` each run one `python loop_transition.py record`, both transitions
  succeed, and `--mail read dA` and `--mail read dB` show all four rows `acked`.
  Red when: a copy chaining only over the filtered rows leaves `s1`'s `confirmed` to `dA` open and
  the guard refuses.
- **AC2** — When a probe calls `derive_mail_chain` with `dA`'s filtered rows and the parent's chain
  rows, it answers that `s1`'s row to `dA` precedes `s2`'s; with the chain rows replaced by the
  filtered rows it answers that it cannot place it.
  Red when: the two calls answer alike, so the chain read added nothing.
- **AC3** — When `bash unattended.sh --mail chain <parent>` runs in that repository, it prints four
  rows carrying `seq` and `after`.
  Red when: a row addressed to the other dependent is missing.

## 7. Gates

`unattended kit gate` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

The loop kit's `loop selftest` leg runs the case once dDeclaredLoop has landed it; the arm line below
declares it.

New arm: tools/loop/selftest.py · covers AC1 AC2 AC3 · the two-dependent take-over plant, staged red by a copy of `derive_mail_chain` reading only the dependent's filtered rows · none

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-2 promotions' audit, H4 (id 31).
- rev-2 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-63` mirrored, the other ends of
  the edges the round-3 promotions' audit's disposal declared

## 10. Reuse audit

The seam extended is `read_mailbox`'s one `git log` and one `awk` (`KICK-dKeptSession-5` S6), run
with its address filter off rather than a second parser, and unit 53's `derive_mail_chain`, given a
wider row set rather than a new rule. `python tools/codebase-map/reuse_lookup.py "order mailbox rows
across every session ref of one build"` ranked `rows`, `row` and `build_commit` by name stem only;
no mail code exists at this base, so no existing seam in the tree fits and the sibling specs are the
seams.

Recall terms used: `python tools/memory-recall/query.py "how is a promoted unit placed when it
repairs an earlier unit's pass" --terms "promoted order pass commit ledger superseded batch minors
hands-off consumes-from parity mirror"`
