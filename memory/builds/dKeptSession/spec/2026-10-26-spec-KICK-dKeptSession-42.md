# KICK-dKeptSession-42 — a dependent's transition acknowledges the notices it has consumed, so a parent's notice never holds the dependent until the wait ceiling

**Status:** DEFERRED · rev-3 · 2026-11-21 · node a · Tier-2 · base c2a407b0 · streams kickoff · order 25 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-42-deviation-421.md](../build/2026-10-26-build-KICK-dKeptSession-42-deviation-421.md) | deviation | — |
| [2026-11-21-build-KICK-dKeptSession-10-reground-orders-20-26-returns.md](../build/2026-11-21-build-KICK-dKeptSession-10-reground-orders-20-26-returns.md) | research | KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-1 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-35-orders-25-26-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-35-orders-25-26-reground-brief.md) | research | KICK-dKeptSession-35 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 |
| [2026-10-26-review-KICK-dKeptSession-30-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md) | spec-audit | KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-32 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-35 KICK-dKeptSession-43 KICK-dKeptSession-41 KICK-dKeptSession-44 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build's spec set
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md`)
confirmed finding **id 55 at HIGH**, report item **H9**, which no other id shares.

`KICK-dKeptSession-5` S7 keeps every message that is not an `answer` or an `ack` open until something
acknowledges it, and S9 refuses a build's transition while an open row is addressed to it.
`KICK-dKeptSession-7` S4 and S5 post `confirmed`, `changed` and `landed` to each dependent, and no unit
acknowledges them, so every parent notice stalls each dependent's transitions until a session runs
`--mail ack` or `flow.wait-ceiling` passes, 72 hours by default and 168 under strict. An unattended
dependent never acks. This unit keeps the notice kinds gating, as the clause says, and makes the
dependent's transition writer acknowledge each notice it has consumed. It repairs
`KICK-dKeptSession-7` and builds one step after it (order 25).

## 2. Scope (IN)

- **S1** — id 55. Read notices. `write_consumed_acks(root, build, rows)` in
  `tools/loop/loop_transition.py` runs in `write_transition` between `KICK-dKeptSession-5` S9's
  `read_mail_rows(root, build)` and its open-row refusal, over that one unfiltered read's rows (spec-5
  F9). It acknowledges every row whose `state`, column 4, is `open` and whose `kind`, column 2, is
  `landed`, `superseded` or `withdrawn`: the transition has read it, and nothing else consumes it.
  The guard then refuses on the read's `open` rows less every id acknowledged with exit 0, and the
  read is not repeated. Observed by AC1.
- **S2** — id 55. Consumed interfaces. For each parent, the `from-build` of column 6, with an `open`
  `confirmed` or `changed` row in those rows, the writer runs `KICK-dKeptSession-27` S5's
  `check_interface_notice <slug> "interfaces <parent>" <listing>` over the listing
  `KICK-dKeptSession-7` S3 derives, written to a scratch file. When it prints `interface — current
  <id>` and that id is an `open` row of the read, the writer acknowledges that row and every earlier
  `open` `confirmed` or `changed` from the same parent, earlier by `first-seen`, column 5. A row it
  does not acknowledge, a `changed` whose key does not recompute, stays open for the re-entry that
  consumes it. The check runs in the driver as §8 F2 rules. Observed by AC2 and AC3.
- **S3** — id 55. The post. Each acknowledgement is `--mail ack <slug> <id>`
  (`KICK-dKeptSession-5` S8), launched as `read_mail_rows` launches its read: the driver
  `resolve_kit_dir("unattended", "unattended.sh", KIT) / "unattended.sh"`
  (`tools/loop/loop_lib.py#resolve_kit_dir`) run under `resolve_bash(<driver>)`
  (`tools/loop/loop_witness.py#resolve_bash`), which returns `None` where no bash sees it, with stdin
  closed, `read_clean_env()` (`tools/loop/loop_witness.py#read_clean_env`) and the bound
  `MAIL_GUARD_SECONDS`. It runs once per id and only while the row reads `open`, so a retried
  transition posts nothing twice. A failed ack prints `mail — ack not posted <id> · rc <n>`, and the
  guard then refuses on the still-open row as unit 5 S9 states. Observed by AC4.
- **S4** — id 55. `KICK-dKeptSession-24` §8 F2's reliance on the deadline for "a `changed` nobody
  acknowledges" now covers only a `changed` the dependent has not consumed; that unit's text is
  superseded by name here, unchanged in behaviour. NOT OBSERVED: no criterion of this unit observes
  unit 24's deadline, which keeps its own AC.
- **S5** — The user page. `help/loop.md`'s guard paragraph, which `KICK-dKeptSession-5` S14 writes
  under "Recording a build's move", gains §4's table "Who acknowledges what". Observed by AC5.

## 3. Non-goals (OUT)

- Acknowledging a `question`, an `intake` or an `overlap`: those wait for an answer or a person, as
  `KICK-dKeptSession-5` S7 says.
- An `expired` row: the guard passes it and unit 5 S10 disposes it (`KICK-dKeptSession-24` S5).
- The re-entry on a `changed`: dIndexedDesign's `design.reentry`.
- Posting from the position engine. §8 F1 records why the writer posts and the engine only reads.
- The report's left-shift checklist entry, that every gating kind names its acker. No clause of this
  build names that checklist; §4's table is the record here.

### Edges

- **consumes-from** `KICK-dKeptSession-7` — the `confirmed`, `changed` and `landed` notices and S3's interface listing, which the writer reads to decide what it has consumed (id 55)
- **consumes-from** `KICK-dKeptSession-5` — `write_transition`'s guard, `read_mail_rows` and the `--mail ack` verb, through which the writer acknowledges between the read and the refusal
- **consumes-from** `KICK-dKeptSession-27` — `check_interface_notice`, whose `current <id>` line names the row the dependent has consumed
- **consumes-from** `KICK-dKeptSession-36` — the landed `resolve_bash(<driver>)` launch the guard's read uses, through which each `--mail ack` runs
- **hands-off** `KICK-dKeptSession-53` — `write_consumed_acks`' S2, whose "earlier by `first-seen`" that unit replaces with the key and chain rule (id 4)
- **hands-off** `KICK-dKeptSession-55` — `write_consumed_acks` and its S1 and S3, which that unit makes conditional on the guard's verdict and visible (id 49)
- **hands-off** `KICK-dKeptSession-56` — `write_consumed_acks`' launcher and failed acks, and the Gates legs, the batch's S3, S32, S27, S44 and S42 (ids 5, 50, 36, 53, 41)

## 4. Design

### Evidence

- `KICK-dKeptSession-5` S7 and S9; `KICK-dKeptSession-7` S4 and S5 post to `build:<dependent>`; a
  grep for `--mail ack` and `acknowledg` over the spec set finds only unit 5's own verb and
  criterion, unit 21's non-goal and unit 24's deadline text (the audit's reading).
- Unit 5 S6's row, as later units append to it: 1 `id`, 2 `kind`, 3 `to`, 4 `state`, 5
  `first-seen`, 6 `from-build`, 7 `subject`, 8 `answers`, 9 `ref`, 10 `commit`, 11 `reply`
  (spec-5 rev-9), 12 to 14 `seq`, `after`, `content-key` (spec-27 rev-5), 15 to 16 `deadline`,
  `default` (spec-24 rev-3).
- Unit 5 S9 and F9: one `read_mail_rows` read serves the guard and the disposal, launched as
  `tools/loop/loop_transition.py#write_card_follow` runs the kickoff engine.
- `KICK-dKeptSession-27` S5 prints `interface — current <id> · <kind> · key <k>` for the row whose
  key recomputes, exit 0, and `interface — unconfirmed`, exit 1, otherwise. It is a shell function
  of the driver and no verb prints it.
- The driver defines every function and returns when sourced, and loads its conf through
  `load_driver_conf` (`tools/unattended/unattended.sh#load_driver_conf`); its own refusal names the
  sourced form `( load_driver_conf && main <argv> )` (`tools/unattended/unattended.sh#main`).

### Who acknowledges what

| Kind addressed to the dependent | Acknowledged by | When |
|---|---|---|
| `landed`, `superseded`, `withdrawn` | the dependent's `write_transition` | at its next transition |
| `confirmed`, `changed`, current | the dependent's `write_transition` | at its next transition, S2 |
| `confirmed`, `changed`, superseded by a current one | the same | with the current one |
| `changed`, not current | nobody here | dIndexedDesign's re-entry, or the deadline |

### The check's launch (§8 F2)

```
[<bash>, "-c", '. "$1" && load_driver_conf && check_interface_notice "$2" "$3" "$4"',
 "check_interface_notice", <driver>, <slug>, "interfaces <parent>", <listing file>]
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `write_consumed_acks` | function, `tools/loop/loop_transition.py` | `py.function`, `write`, OK |
| `acks-landed`, `acks-confirmed`, `acks-superseded`, `acks-failed` | `--plant` cases of `loop_transition.py --fixture` | none |

### Migration

None: no notice exists before `KICK-dKeptSession-7`.

### Files touched (estimate)

- `tools/loop/loop_transition.py`: `write_consumed_acks`, called between the read and the refusal,
  and the four plants
- `help/loop.md`: S5's table

### Alternatives rejected

- **The position engine posting the ack when its gate accepts.** The engine is called by the card,
  the boundary hook and every `next`, so a read would post mail at every one of them.
- **Notice kinds that never gate.** The clause's guard reads every message addressed to the build;
  exempting kinds would let a `withdrawn` parent pass unread.
- **A second `--mail read` after the acks.** Unit 5's F9 keeps one snapshot for the guard and the
  disposal; the acked ids are known from the posts' exits.

## 5. Production-readiness checklist

- security — acks pass through `KICK-dKeptSession-5` S8's verb, which refuses an id not addressed
  to the slug; the check's argv is fixed and its values are arguments, never shell text.
- perf / scale — one `check_interface_notice` per parent with an open notice, and one post per
  consumed id, at a transition.
- error / empty / loading states — a failed ack, or a check that does not answer within the bound,
  leaves the row open and the guard refuses, so the failure is visible and never silent.
- observability — each ack is a mail message in the parent's view of the dependent's replies.
- risks — a dependent that never transitions never acks; its parent is not held by that, since only
  rows addressed to a build gate that build. A move the table refuses after the guard has still
  acked what the transition read, which `KICK-dKeptSession-55` makes conditional and visible.
- testing — the cases of §6 and the arm in §7.
- migration — none.
- user docs — `help/loop.md`'s guard paragraph gains the table of §4, S5.

## 6. Acceptance criteria

The fixture is `KICK-dKeptSession-7` AC7's two-build scratch repository with a bare origin under
`%TEMP%` and `RUN_CLAIMS=on`, planted by `loop_transition.py --fixture`.

- **AC1** — When `python tools/loop/loop_transition.py --fixture --plant acks-landed` lands the
  parent and the dependent then runs one `record` with no manual ack, the transition succeeds and
  `--mail read <dependent>` shows the `landed` row `acked`.
  Red when: the transition is refused with `mail open`, as unit 5's guard alone refuses it.
- **AC2** — When `--plant acks-confirmed` has the parent leave Design and the dependent, whose
  listing recomputes the key, run one transition with no manual ack, it succeeds and the
  `confirmed` row reads `acked`.
  Red when: the consumed notice holds the transition until the wait ceiling.
- **AC3** — When `--plant acks-superseded` has the parent post `confirmed` then `changed` and the
  dependent's listing recompute only the `changed` key, one transition acks both; when it recomputes
  neither, the transition is refused naming the `changed` id.
  Red when: a superseded `confirmed` stays open, or an unconsumed `changed` is acked.
- **AC4** — When `--plant acks-failed` retries the transition after AC2's, it posts no second ack,
  and with `--mail ack` planted to exit 1 the transition is refused printing `ack not posted`.
  Red when: an ack is posted twice, or a failed ack passes the guard.
- **AC5** — When `grep -n "Acknowledged by" loop.md` runs in `help/`, it prints the table's header
  row under "Recording a build's move".
  Red when: the owner's page does not say who acknowledges a notice.

## 7. Gates

`loop transition record` · `docs` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/loop_transition.py · covers AC1 AC2 AC3 AC4 · the `acks-landed`, `acks-confirmed`, `acks-superseded` and `acks-failed` plants, staged red against unit 5's guard with no ack step · none

## 8. Open questions

- **F1 — Which step posts the acknowledgement of a consumed interface notice?** Options: (a) the
  dependent's transition writer, through the gate's own `check_interface_notice`, ahead of the guard;
  (b) the position engine, when its gate accepts a row, the skeptic's wording; (c) a new verb a
  session runs. (b) makes a read path write, at every card render and boundary; (c) is the manual
  step the defect is. (a) meets AC1 to AC4 at the one write path that the open row blocks.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 3, the same acceptance as the corrected fix,
  posted from a writer. widens: none · relaxes: none
- **F2 — How does the Python writer run `check_interface_notice`, a driver shell function no verb
  prints?** Options: (a) the sourced driver under the same `resolve_bash(<driver>)`, the argv of §4
  "The check's launch", the conf loaded by `load_driver_conf` as the driver's own refusal names;
  (b) a new `--mail` verb printing the check, asked of `KICK-dKeptSession-27`, which moves a sibling's
  verb set; (c) the key recomputed in Python over the read's `content-key` column, a second
  implementation of `derive_gov_id`'s hash beside the driver's. (a) keeps unit 27's check the one
  implementation and adds no verb; its cost is one sourced driver per parent. Recommendation (a).
  RESOLVED (agent, 2026-11-21, delegated): (a), rung 3; the most capable option no veto removes,
  one implementation of the check and no new surface. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's H9 (id 55).
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-53`, `KICK-dKeptSession-55`,
  `KICK-dKeptSession-56` mirrored, the other ends of the edges the round-1 promotions' audit's
  disposal declared
- rev-3 · 2026-11-21 · S1 · S2 · S3 · S5 · §3 · §4 · §5 · AC1 to AC5 · §7 · §8 F2 · §10 ·
  re-grounded on base c2a407b0 by `2026-11-21-prompt-KICK-dKeptSession-35-orders-25-26-reground-brief`:
  S1 runs over unit 5's one unfiltered `read_mail_rows` read (spec-5 F9), the guard judging its open
  rows less the acked ids; the row's columns spelled from spec-5 rev-9, spec-27 rev-5 and spec-24
  rev-3; S3 launches through the landed `tools/loop/loop_witness.py#resolve_bash(<script>)`, which
  returns `None`, as the guard's read does; F2 ruled for the check's launch; the arm moves from the
  absent `tools/loop/selftest.py` to `loop_transition.py`'s plants; S5 and AC5 carry §5's page into
  the files touched; the leg line gains `loop transition record` and `docs`; line citations re-cited
  by section. Narrowed: no second read before the guard, since the one read is unit 5's.

## 10. Reuse audit

The seams extended are `KICK-dKeptSession-5`'s `read_mail_rows` read, `--mail ack` verb and
`write_transition` guard, `KICK-dKeptSession-27`'s `check_interface_notice` and `KICK-dKeptSession-7`'s
listing, launched as `tools/loop/loop_transition.py#write_card_follow` launches the kickoff engine,
through `tools/loop/loop_lib.py#resolve_kit_dir` and `tools/loop/loop_witness.py#resolve_bash`;
nothing is re-derived. `python tools/codebase-map/reuse_lookup.py "acknowledge a mailbox message
once its consumer reads it"` ranked `read_text`, `read`, `read_bytes` and `read_git` by the name
stem `read` only; no mail code is in the tree at c2a407b0, so no other seam fits and the sibling
units' specs are the seams.

Recall terms used: `python tools/memory-recall/query.py "who acknowledges a parent's notice to a
dependent build" --terms "mail ack acked open notice confirmed changed landed transition guard
wait-ceiling check_interface_notice dependent"`
