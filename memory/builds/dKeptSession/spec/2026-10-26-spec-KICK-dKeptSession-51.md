# KICK-dKeptSession-51 — the act's place in the message id is the ninth field, after the recipient and the content key, in every text that states it

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 17 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 |
| [2026-10-26-build-KICK-dKeptSession-51-deviation-511.md](../build/2026-10-26-build-KICK-dKeptSession-51-deviation-511.md) | deviation | — |
| [2026-10-26-review-KICK-dKeptSession-45-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-45-spec-audit.md) | spec-audit | KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-56 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build's fifteen round-1 promotions
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md`)
confirmed finding **id 39 at HIGH**, report item **H4**, which no other HIGH id shares. Id 8 is the
same defect at MEDIUM, item M7, batched into `KICK-dKeptSession-56`, whose item observes this fix.

`KICK-dKeptSession-31` S1 orders the id's eight fields with `<to>` and `<content-key>` at positions 7
and 8, and says `KICK-dKeptSession-22` S4's act "joins as the ninth field". Its S4 supersedes only
unit 22 S2's "six fields", AC2 and unit 5 S5. It leaves standing unit 22 S4, "the act is a seventh
field of S2, appended after `answers`", and unit 22's `hands-off external` edge to dWellOiledMachine,
"whose act joins S2 as a seventh field" (spec-22 lines 45-46 and 65). That edge is the contract the
child build reads. A builder there who puts the act seventh, between `answers` and `to`, derives a
different id for the same message than this build does, and the duplicate refusal across the two
builds fails open. This unit makes every text that states the act's place say ninth, and hands the
child build that answer as an ask. It repairs `KICK-dKeptSession-31` and builds one step after it
(order 17).

## 2. Scope (IN)

- **S1** — id 39. The order in code. `derive_message_id`'s comment in
  `tools/unattended/unattended.sh` lists the eight fields in order and states that a later act is
  appended as the ninth, after `<content-key>`, so a reader of the function reads the position where
  the derivation lives. Observed by AC1.
- **S2** — id 39. The order in the guide. The verbs guide's mailbox id paragraph,
  `tools/unattended/VERBS.template.md` and its render `memory/guides/UNATTENDED-VERBS.md`, names the
  act as the ninth field after the recipient and the content key. Observed by AC2.
- **S3** — id 39. The child build's contract. One ask row in
  `memory/builds/dWellOiledMachine/BACKLOG.md`, as this build's README write rule allows: "the act
  joins `derive_message_id` as its ninth field, after `<to>` and `<content-key>`
  (`KICK-dKeptSession-31` S1); `KICK-dKeptSession-22` S4's seventh is superseded". Its accept line:
  the child's Runtime spec states the ninth position. Observed by AC3.
- **S4** — id 39. The sibling text superseded by name. `KICK-dKeptSession-22` S4 and its `hands-off
  external` edge to dWellOiledMachine join `KICK-dKeptSession-31` S4's superseded list, with the act
  at position 9. Each is answered in unit 22's acceptance ledger, citing S3's ask. Observed by AC3.

## 3. Non-goals (OUT)

- Minting the act: dWellOiledMachine's Runtime.
- The eight fields themselves: `KICK-dKeptSession-31`.
- The report's left-shift checklist entry, that a spec changing a field order lists every sibling
  clause and edge stating the old order. No clause of this build names that checklist.

### Edges

- **consumes-from** `KICK-dKeptSession-31` — the eight-field `derive_message_id` and its S4 superseded list, which this unit completes with the act's ninth position (id 39)
- **consumes-from** `KICK-dKeptSession-22` — S4 and its `hands-off external` edge to dWellOiledMachine, whose seventh position this unit supersedes
- **hands-off** `KICK-dKeptSession-56` — the act's ninth position in code, guide and ask, which the batch's item for id 8, the same defect at MEDIUM, observes
- **hands-off** external — dWellOiledMachine's Runtime, whose act joins `derive_message_id` as its ninth field, by S3's ask

## 4. Design

### Evidence

- spec-22:45-46, S4: "the act is a seventh field of S2, appended after `answers`"; spec-22:65, the
  `hands-off external` edge: "whose act joins S2 as a seventh field".
- spec-31:35-39, S1: eight fields ending `<to> <content-key>`, and "`KICK-dKeptSession-22` S4's act
  joins as the ninth field"; spec-31 S4 supersedes unit 22 S2, AC2 and unit 5 S5 only.
- dWellOiledMachine's `BACKLOG.md` holds one ask today, `TOOL-dWellOiledMachine-62`, so S3's row is
  the second.

### The fields

```
1 build · 2 item · 3 pass · 4 kind · 5 subject · 6 answers · 7 to · 8 content-key · 9 act (once minted)
```

### Inventory

No identifier is minted; S3's ask takes the next id in dWellOiledMachine's family when the main loop
files it.

### Migration

None: no act exists, and no message exists before this build.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: S1, the comment on `derive_message_id`
- `tools/unattended/VERBS.template.md`: S2
- `memory/guides/UNATTENDED-VERBS.md`: S2's render
- `memory/builds/dWellOiledMachine/BACKLOG.md`: S3's ask row

### Alternatives rejected

- **The act seventh, the recipient and key moved after it.** It reorders fields this build's ids
  already derive from, so a message retried across the change would mint a second id.
- **Leaving the position to the child build.** The child reads it from this build's edge, which is
  what disagreed.

## 5. Production-readiness checklist

- security — none: text and an ask row.
- perf / scale — none.
- error / empty / loading states — none.
- observability — the guide and the comment state one position.
- risks — the child may decline the ask; its own spec then owns the disagreement, recorded.
- testing — the criteria of §6; no suite arm, since nothing executes differently.
- migration — none.
- user docs — the verbs guide, S2.

## 6. Acceptance criteria

- **AC1** — When `grep -n "ninth" unattended.sh` runs in the unattended kit, it prints the comment on
  `derive_message_id` naming the act after `content-key`.
  Red when: the function states no position, or the seventh.
- **AC2** — When `grep -n "ninth" UNATTENDED-VERBS.md` runs in `memory/guides/`, the mailbox id
  paragraph names the act after the recipient and the content key, and `grep -c "seventh field"`
  over that file prints `0`.
  Red when: the guide states the act's place as seventh.
- **AC3** — When `python tools/memory-tree/gen_build_index.py --asks --build dWellOiledMachine` runs,
  it lists the ask naming `derive_message_id` and the ninth field.
  Red when: the child build's only statement of the position is unit 22's superseded edge.

## 7. Gates

`unattended kit gate` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

## 8. Open questions

none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 promotions' audit, H4 (id 39).

## 10. Reuse audit

The seam extended is `KICK-dKeptSession-31`'s superseded list over `derive_message_id`, the one id
derivation every post calls, and the verbs guide's mailbox section unit 31 S5 already edits; the
ask uses the README's write rule for another build's `BACKLOG.md`. `python
tools/codebase-map/reuse_lookup.py "derive a stable id from fields by hashing so a retry is refused
as a duplicate"`, unit 22's probe, ranked `derive_clause_hash` and `derive_baseline_additions` by
name stem; no mail code exists at this base, so no existing seam in the tree fits and unit 31's spec
is the seam.

Recall terms used: `python tools/memory-recall/query.py "where does the act join the message id"
--terms "derive_message_id act ninth field seventh content-key recipient dWellOiledMachine Runtime
hands-off superseded"`
