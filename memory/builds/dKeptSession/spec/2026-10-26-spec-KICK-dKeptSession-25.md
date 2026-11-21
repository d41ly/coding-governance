# KICK-dKeptSession-25 — `mailbox.answer`: a `question` to a build answered by its owning role, or by the asker's default until `next` dispatches it, the waiting build's lease renewed

**Status:** DEFERRED · rev-6 · 2026-11-21 · node a · Tier-2 · base c2a407b0 · streams kickoff · order 21 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0504@b051ecfa whole
**Carries:** node:item.mailbox.answer

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md) | research | KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-10 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-1 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-build-KICK-dKeptSession-25-deviation-251.md](../build/2026-10-26-build-KICK-dKeptSession-25-deviation-251.md) | deviation | — |
| [2026-10-26-build-KICK-dKeptSession-25-deviation-252.md](../build/2026-10-26-build-KICK-dKeptSession-25-deviation-252.md) | deviation | — |
| [2026-11-05-build-KICK-dKeptSession-25-deviation-253.md](../build/2026-11-05-build-KICK-dKeptSession-25-deviation-253.md) | deviation | — |
| [2026-11-21-build-KICK-dKeptSession-10-reground-orders-20-26-returns.md](../build/2026-11-21-build-KICK-dKeptSession-10-reground-orders-20-26-returns.md) | research | KICK-dKeptSession-10 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-1 |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-reground.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-reground.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-5 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-36 KICK-dKeptSession-44 KICK-dKeptSession-56 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-11-05-prompt-KICK-dKeptSession-1-owner-forks.md](../prompts/2026-11-05-prompt-KICK-dKeptSession-1-owner-forks.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-7 KICK-dKeptSession-9 KICK-dKeptSession-20 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief-2.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief-2.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-10-orders-20-22-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-10-orders-20-22-reground-brief.md) | research | KICK-dKeptSession-10 KICK-dKeptSession-21 |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |

<!-- /gen:spec-records -->

## 1. Goal

A `question` addressed to a build is an item, `mailbox.answer`, answered by the role that owns the
asked interface or item and dispatched by `next` when the question arrives. Until dWellOiledMachine
lands `next`, nothing dispatches it, so a question to an unattended build is answered by the asker's
declared default under cl-dClosedLoop-0162, the same stand-in covering its answering role (the closing
pair's answer-dispatch-non-ancestor). Meanwhile the recipient's transition is refused, and that
refusal is a declared wait inside `flow.wait-ceiling`, which `leases.renewal: progress` renews, so a
build waiting on a question keeps its lease (the whole-design audit's A2-F5, the owner's FK-5-4). The
landed lease writer already admits that wait: `check_lease_witness` answers `question` for an open
question's commit and `derive_lease_renews` renews on that verdict
(`tools/unattended/unattended.sh#check_lease_witness`). Nothing passes such a commit yet, since the
driver's own witness is a transition alone (`tools/unattended/unattended.sh#read_lease_renewal`).

## 2. Scope (IN)

- **S1** — The item row, one `[[item]]` row of `tools/loop/loop.toml`'s entry program, tagged
  `item.entry.mailbox-answer` (§8 F8), in the landed shape of the row `item.entry.claim`:
  `step = "none"` (§8 F1), `actor = "command:mailbox.answer"` (§8 F2), `needs = []`, prose `inputs`,
  `allowance` and `returns` (§8 F6), outcomes `answered`, `awaiting` and `defaulted` (§8 F3), inline
  `routes` sending `answered` and `defaulted` to `stand-in:{prefix}/unattended/unattended.sh` and
  `awaiting` back to the item itself, `waits = ["awaiting"]`, `deadline = "policy.flow.wait-ceiling"`
  and `on-deadline = "defaulted"`, the outcome outside `waits` the `wait` rule requires
  (`tools/loop/termination.py#check_wait`), its witness S3's computed join under the class `history`,
  and `owner = "dKeptSession"`. Observed by AC1.
- **S2** — The answer verb, `unattended.sh --mail answer <slug> <question id> <body file> [--cite
  <path>@<sha>]…`, a member of `KICK-dKeptSession-5`'s `--mail` family (its S8) with its own
  `#   unattended.sh --mail answer …` usage-header row. `<slug>` is the answering build. It reads
  `read_mailbox <slug> soft` once. Before any commit it refuses with exit 2 an id naming no
  `question` row addressed to `<slug>`, and a cite whose `git cat-file -e <sha>:<path>` fails; it
  refuses with exit 1, printing `answer — <id> · <state>`, a question whose state is not `open`. It
  then posts one message of kind `answer` through unit 5 S5's post path, as its `--mail ack` posts:
  from `<slug>`, addressed to `build:<from-build>` of that row, `answers: <question id>`, the row's
  subject, and the body file with one line `cites <path>@<sha>` per cite appended, held to unit 5
  S4's body checks. It prints the post's `mail — posted <id> · <ref>` line and exits as the post does.
  Observed by AC2.
- **S3** — The outcome, `derive_mail_answer_outcome <slug> <question id>` in
  `tools/unattended/unattended.sh`, from `read_mailbox <slug> soft`'s rows alone (unit 5 S6 and S7,
  `KICK-dKeptSession-24` S5): `answered` when the question's state is `answered`; `defaulted` when it
  is `expired`, `check_mail_deadline` having passed, or `acked` (§8 F9); `awaiting` while it is
  `open`. An id naming no `question` row addressed to `<slug>` exits 2. It prints one word and is the
  item's witness. Observed by AC2, AC3 and AC5.
- **S4** — The declared wait renews the lease. `read_lease_renewal`, the witness the driver derives
  for every claim write it makes of its own run, `--beat`'s included (`write_claim_beat` calls
  `write_claim`, which calls it), gains one step under `progress`. Where no transition newer than the
  record's witness is found, it takes the oldest `question` row addressed to the build whose state is
  `open`, S3's `awaiting`, by `first-seen`, and runs the landed `check_lease_witness <slug> <that
  row's commit>`, which writes nothing (§8 F7). On the verdict `question` it sets `LR_VERDICT` to
  `question`, `LR_WITNESS` to the full sha in `LW_SHA` and `LR_WAIT` to the row's id, so
  `derive_lease_renews` writes `renews: yes` (`tools/unattended/unattended.sh#derive_lease_renews`).
  Any other verdict, `question-closed` for an expired, acked or answered question included, keeps
  `none` and the record's witness. `--beat`'s `renewed` line then ends ` · wait question <id>`. With
  no open question the renewal is TOOL-dPlacedRequest-1 S8's transition rule. Observed by AC4 and AC5.
- **S5** — The stand-in, stated: until `next` exists, nothing runs `command:mailbox.answer` as a
  dispatch. An attended session answers through S2 when `KICK-dKeptSession-10`'s interrupt shows the
  question; an unattended build, which no one answers, reaches `defaulted` at the deadline, and its
  transitions go on, as unit 5's guard refuses only `open` rows. No code tells the two apart (§8 F5).
  Observed by AC3.
- **S6** — The docs: the `--mail` section unit 5 adds to `tools/unattended/VERBS.template.md`
  (rendered to `memory/guides/UNATTENDED-VERBS.md`) gains `--mail answer`, `--cite` and the wait's
  renewal, and `help/loop.md`'s section "The entry items: orienting, placing and claiming a request"
  gains the `item.entry.mailbox-answer` row. Observed by AC6.

## 3. Non-goals (OUT)

- No `next` and no dispatch: dWellOiledMachine's. When it lands, `next` dispatches this item and its
  actor becomes the owning role (the external hand-off below).
- No deadline judgment: `check_mail_deadline` and the `expired` state are `KICK-dKeptSession-24`'s.
- No mailbox, kinds, guard or post path: `KICK-dKeptSession-5`'s.
- No change to the lease witness rule: TOOL-dPlacedRequest-1 S8 already admits an open question's
  commit (its §8 F9), and this unit only passes one.
- No owner question asked live: dFurnishedOrders' (cl-dClosedLoop-0155's join).
- No `[[stand-in]]` row: the landed rows list transition-table items whose owning build has not
  landed (`tools/loop/loop.toml`, its `[[stand-in]]` rows), and this item is dKeptSession's and no
  table row's.
- No change to the loop kit's programs: the row joins the entry program
  (`tools/loop/loop_lib.py#PROGRAM_SEGMENTS`).
- No kit version: the lander mints it (`tools/push-main.sh@78f40c3c2475:27`).

### Edges

- **consumes-from** `KICK-dKeptSession-5` — `read_mailbox`, its rows and states, and the post path `--mail answer` writes through
- **consumes-from** `KICK-dKeptSession-24` — `check_mail_deadline` and the `expired` state, through which an unanswered question is answered by the asker's default
- **consumes-from** external — the landed entry program and row shape (TOOL-dPlacedRequest-3, TOOL-dDeclaredLoop-12), `termination.py`'s `wait` rule (TOOL-dDeclaredLoop-33), TOOL-dDeclaredLoop-9's actor grammar, and the landed lease writer's `read_lease_renewal`, `check_lease_witness` and `derive_lease_renews` (TOOL-dPlacedRequest-1, TOOL-dPlacedRequest-25)
- **hands-off** external — dWellOiledMachine's `next` dispatches `mailbox.answer` when a question arrives and re-points its actor to the owning role, with the per-question actor form TOOL-dDeclaredLoop-9's grammar does not spell
- **hands-off** `KICK-dKeptSession-44` — §7's covers list, the batch's S2 (id 5), whose premise, an ask dPlacedRequest had not accepted, the landed TOOL-dPlacedRequest-1 retired

## 4. Design

### Evidence

- flow-steps' `[entry]` row gives the actor as "the role that owns the asked interface or item, one
  per question", proven by a computed join of the `answer` message to the question's id
  (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md@d73cb002d028:128`).
- Its `[rules]` paragraph makes the transition refused while a message awaits its answer a declared
  wait inside `flow.wait-ceiling`, which `leases.renewal: progress` renews
  (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md@d73cb002d028:78`).
- The landed lease writer: under `progress` a write renews on a `new` transition verdict or a
  `question` verdict (`tools/unattended/unattended.sh#derive_lease_renews`). `check_lease_witness`
  answers `question` for the commit of an `open` question row and `question-closed`, exit 1, for one
  in any other state, `expired` included; it reads the mailbox only where `declare -F` finds
  `read_mailbox` and `check_mail_deadline` (`tools/unattended/unattended.sh#check_lease_witness`).
  TOOL-dPlacedRequest-1, CLOSED, carries `closes TOOL-dPlacedRequest-67`, the ask this spec's F4 filed.
- The driver's own claim writes take their witness from `read_lease_renewal`, which looks for a
  transition alone (`tools/unattended/unattended.sh#read_lease_renewal`); `--beat` renews through
  `write_claim` and prints one `beat —` line (`tools/unattended/unattended.sh#write_claim_beat`).
- `check_program` admits a `step = "none"` row only under a segment of `PROGRAM_SEGMENTS`, `review`,
  `probe` or `entry` (`tools/loop/loop_lib.py#check_program`). The landed wait row `item.entry.claim`
  writes `waits`, `deadline`, an `on-deadline` naming an outcome, and inline `routes` with a
  `{prefix}` stand-in (`tools/loop/loop.toml`, row `item.entry.claim`).
- TOOL-dDeclaredLoop-9's actor is one `<kind>:<name>` (`tools/loop/loop_lib.py#ACTOR_FORM`), and
  layer-roles' `[matrix]` notes the instrument cannot read which role owns a question
  (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md@276f0fc62a94:434`).
- A prose `returns` names no record kind (`tools/loop/loop_items.py#derive_record_ref`), so the record
  join reads nothing from it, and an input naming a kind no needed item returns is refused
  (`tools/loop/loop_items.py#check_item_composition`).

### The row

```toml
# tools/loop/loop.toml — the entry program; mailbox.answer, before any step (flow-steps' [entry])
[[item]]
tag = "item.entry.mailbox-answer"
step = "none"
actor = "command:mailbox.answer"   # the stand-in covering the owning role until `next` (cl-dClosedLoop-0504)
needs = []
inputs = ["layer.flow:the question message", "layer.memory:the asked interface's declaration or the asked item's witnesses"]
allowance = "one answer commit on the answering session's mail ref"
returns = "the answer's mail commit"
outcomes = ["answered", "awaiting", "defaulted"]
witness = { class = "history", by = "derive_mail_answer_outcome over the question's mail rows" }
owner = "dKeptSession"
routes = { answered = "stand-in:{prefix}/unattended/unattended.sh", awaiting = "item.entry.mailbox-answer", defaulted = "stand-in:{prefix}/unattended/unattended.sh" }
waits = ["awaiting"]
deadline = "policy.flow.wait-ceiling"
on-deadline = "defaulted"
```

### The wait, in order

1. A `question` addressed to `build:<slug>` lands; unit 5's guard refuses the build's next
   transition while it reads `open`.
2. Each claim write the driver makes of the run, every `--beat` among them, derives its witness in
   `read_lease_renewal`: a newer transition first; else the oldest open question addressed to the
   build, which `check_lease_witness` admits, renews, and the beat's line names it.
3. An answer through S2 makes the question `answered`, the deadline passing `expired`, an `ack`
   `acked`. Each lets the guard pass the transition, `check_lease_witness` then answers
   `question-closed`, and the beat renews by the transition rule again.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `item.entry.mailbox-answer` | loop item tag | `tag.item`, OK by `lexicon.py --tags` |
| `command:mailbox.answer` | item actor | none |
| `--mail answer`, `--cite` | verb and flag of `tools/unattended/unattended.sh` | none |
| `derive_mail_answer_outcome` | shell function | `sh.function`, OK by `lexicon.py --suggest` |
| `LR_WAIT` | variable `read_lease_renewal` sets | none declared |

### Migration

None: no question exists before unit 5 lands.

### Rollout

Behind `RUN_CLAIMS` with every mail verb. The question witness arms where `declare -F` finds unit 5's
`read_mailbox` and unit 24's `check_mail_deadline`, both earlier in build order, so S4 renews from the
first beat after this unit lands.

### Files touched (estimate)

- `tools/loop/loop.toml`: the `item.entry.mailbox-answer` row in the entry program
- `tools/unattended/unattended.sh`: `--mail answer` and its usage row, `derive_mail_answer_outcome`,
  `read_lease_renewal`'s question step, and the beat's ` · wait question` suffix
- `tools/unattended/unattended.test.sh`: the arms of §7
- `tools/unattended/VERBS.template.md`: `--mail answer`, `--cite`, the wait's renewal
- `memory/guides/UNATTENDED-VERBS.md`: its render
- `help/loop.md`: the `item.entry.mailbox-answer` row in the entry items section

### Alternatives rejected

- **A transition commit written to renew the lease while waiting.** A transition recorded, by trailer
  or log record, for a move that did not happen is a false witness, and the position engine would read
  it as one.
- **A version gate on the beat's witness.** The lease verbs and the beat are one driver, so a version
  compared there compares the file with itself; the witness check is the landed rule itself (§8 F7).
- **An answer posted by the waiting build at once, from the asker's default.** The clause answers by
  default only past the deadline, under cl-dClosedLoop-0162.
- **A `[[stand-in]]` row naming dWellOiledMachine.** The landed stand-in rows hold transition-table
  items whose owner is the stand-in's, and this item's owner is dKeptSession.
- **A fourth program for one item**, `mailbox` added to `PROGRAM_SEGMENTS` (§8 F8).
- **The question step only on the beat**, a flag beside `read_lease_renewal`. Every own claim write
  during the wait is a write inside it, so a flag would make one witness rule two.

## 5. Production-readiness checklist

- security — `--mail answer`'s body passes unit 5 S4's body check; each cite is resolved by
  `git cat-file -e` before the post, so an answer cannot cite a record that does not exist.
- perf / scale — under `progress` with no newer transition, each own claim write reads the mailbox
  once, and once more inside `check_lease_witness` where an open question stands: one bounded fetch
  per beat, two during a wait. Questions are few per build.
- error / empty / loading states — an unknown id or a bad cite exits 2 with nothing written; an
  answered, acked or expired question exits 1 naming its state; a failed fetch reads the cache under
  `soft`, as unit 5 S6 reads it.
- observability — the `beat —` line names the question a renewal waits on.
- risks — a beat outside a wait now pays one mailbox read; a question the feed never sighted sorts
  last and still renews while `open`, since `check_lease_witness` reads its state, not its age.
- testing — the probes of §6 and the arms of §7.
- migration — none.
- user docs — `memory/guides/UNATTENDED-VERBS.md` and `help/loop.md`.

## 6. Acceptance criteria

- **AC1** — When `python tools/loop/loop_lib.py --check`, `python tools/loop/loop_items.py check` and
  `python tools/loop/termination.py check` run over the tree holding the row, each exits 0; in a
  scratch clone whose committed row has its `deadline` line deleted, `termination.py check` exits 1
  naming `item.entry.mailbox-answer` under its `wait` rule.
  Red when: the row is refused as no program's, or its wait declares no deadline and nothing says so.
- **AC2** — When `bash tools/unattended/unattended.sh --mail answer <slug> <qid> <file> --cite
  <path>@<sha>` runs over an open question addressed to `build:<slug>`, an `answer` message with
  `answers: <qid>` and the body line `cites <path>@<sha>` is posted to `build:<from-build>`, and a
  probe sourcing the driver prints `answered` from `derive_mail_answer_outcome <slug> <qid>`; a
  second answer exits 1 printing `answer — <qid> · answered`, and a cite whose sha does not hold the
  path exits 2 with no commit.
  Red when: a question is answered twice, or an answer cites a record that does not exist.
  fixture: a scratch clone with a bare origin under `%TEMP%`, `RUN_CLAIMS=on`, two builds and a
  fleet tag.
- **AC3** — When a question with `deadline: 30` is planted to an unattended build and nobody answers,
  with its feed line sighted one hour ago `derive_mail_answer_outcome` prints `awaiting` and
  `python tools/loop/loop_transition.py record` is refused naming the id; with the line planted 31
  hours ago it prints `defaulted`, the record is written, and `--mail read` shows the question
  `expired` with its `default`.
  Red when: an unattended build answers before the deadline, or blocks past it.
  figure: the deadline and both sightings are PINNED fixture literals.
- **AC4** — When a question addressed to the build was sighted 30 hours ago with `deadline: 72`, no
  transition of the build is newer than its lease record's `witness`, and `--beat` runs under the
  default `progress`, the lease commit it writes carries `witness: <the question's commit>` and
  `renews: yes` and its line ends ` · wait question <qid>`; a second beat writes `renews: yes` again;
  a scratch copy of the driver whose `read_lease_renewal` skips the question step writes `renews: no`.
  This is the clause's planted question to an unattended build, whose lease would otherwise lapse at
  `leases.expiry-hours` while it waits.
  Red when: a beat during a wait inside its deadline renews nothing.
  fixture: a scratch clone with a bare origin, `RUN_CLAIMS=on`, a run record `--liveness` reads LIVE
  on this host, and the question's mail ref and feed line planted.
  figure: the sighting and the deadline are PINNED fixture literals.
- **AC5** — When the same question's sighting is planted 73 hours ago, `derive_mail_answer_outcome`
  prints `defaulted` and `--beat` writes `renews: no` with the record's `witness` unchanged and no
  `wait question` in its line; the same holds with the question answered; and with a transition
  commit newer than the record's `witness` planted beside the open question, the beat's `witness` is
  that transition.
  Red when: an expired or answered wait keeps renewing, or a wait outranks a newer transition.
  figure: the sighting is a PINNED fixture literal.
- **AC6** — When `grep -n -- '--mail answer\|--cite\|wait question' tools/unattended/VERBS.template.md`
  runs, and `grep -n 'item.entry.mailbox-answer' help/loop.md`, each is found.
  Red when: the verb or the item is undocumented.

## 7. Gates

`unattended kit gate` · `scratch-guard self-test` · `tier2-review self-test` · `loop definition` · `loop item kind` · `loop termination` · `docs` · `recall floor` · `recall floor arms` · `python resolver (behaviour + inline parity + idiom ban)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · covers AC2 AC3 AC4 AC5 · the answer, the default and the wait arms over planted mail commits, feed lines and lease chains, AC4 staged by a scratch copy whose `read_lease_renewal` skips the question step · `FLOOR_ASSERTIONS` and its shard floor rise by the arms' count, counted off the diff

AC1 adds no arm: the `loop termination` leg runs the check over gov's composition, which then holds
the row, and its landed `wait-no-deadline` plant already observes the rule's red.

## 8. Open questions

- **F1 — What `step` does the row carry?** Options: (a) `step = "none"`, the value
  TOOL-dPlacedRequest-3 §8 F2 gives the entry items, since flow-steps places `mailbox.answer` in
  `[entry]`, before any step; (b) a step of its own, which changes TOOL-dDeclaredLoop-1's five-step
  definition, a parent's mechanism. RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, the
  flow-steps row (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md@d73cb002d028:128`).
  widens: none · relaxes: none
- **F2 — What actor does the row declare while `next` is unbuilt?** Options: (a)
  `command:mailbox.answer`, the stand-in the clause says covers the answering role, the owning role
  joining when `next` dispatches the item; (b) a per-question role, which TOOL-dDeclaredLoop-9 S1's
  grammar cannot spell, since `role:<slot>` names one slot and the owning role is chosen per question.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, the clause's "the same stand-in covering its
  answering role". widens: none · relaxes: none
- **F3 — What are the item's outcomes and routes?** Options: (a) `answered`, `awaiting` and
  `defaulted`, with a declared wait as TOOL-dDeclaredLoop-33 S5 requires; (b) `answered` and
  `defaulted` only, so the recipient's wait is declared nowhere and the `wait` rule cannot see it. The
  asking item belongs to another build, so no route can name it. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3. widens: none · relaxes: none. Re-grounded 2026-11-21: the landed `wait`
  rule reads `on-deadline` as an outcome outside `waits` (`tools/loop/termination.py#check_wait`), and
  the landed wait rows route the waiting outcome back to the item, so the row writes
  `waits = ["awaiting"]`, `on-deadline = "defaulted"` and `awaiting` to itself; the pick stands.
- **F4 — How does a waiting build's lease renew, when TOOL-dPlacedRequest-1 S8 renewed only on a
  transition?** Options: (a) this unit's beat passes the open question's commit as its witness, and an
  ask asks dPlacedRequest to accept it while the question is inside its deadline; (b) a transition
  commit written to renew, a false witness; (c) edit TOOL-dPlacedRequest-1, which the brief bars.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, the `leases.renewal` row's "renews … on
  declared waits inside their deadline"
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c9:1159`).
  Ask: target dPlacedRequest · accept under `leases.renewal: progress` a renew whose `--witness` is
  the commit of a mail message of kind `question` addressed to the lease's build, `open` on this node
  and inside its declared deadline by `check_mail_deadline`, writes `renews: yes` even when it
  equals the record's `witness`, red on that witness once the question reads `expired`. widens: none ·
  relaxes: none. Re-grounded 2026-11-21: accepted and landed as TOOL-dPlacedRequest-67, which
  TOOL-dPlacedRequest-1 closes, its S8 and §8 F9 the question witness; this unit passes the commit
  from `read_lease_renewal`, the driver's own witness, rather than a `--witness` flag.
- **F5 — Does the code tell an unattended build from an attended one?** Options: (a) no: every build's
  unanswered question takes the default past the deadline, and an attended session answers sooner
  through `--mail answer`; (b) detect a mandate in the run-state file and default only there, which
  leaves an attended build's unanswered question blocking for ever, against cl-dClosedLoop-0162.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, cl-dClosedLoop-0162. widens: none · relaxes: none
- **F6 — What does the row's `returns` name, when an answer writes a mail commit and no record kind?**
  TOOL-dDeclaredLoop-24 §4 "Records at a version" writes `returns` as `record-kind.<name>@<n>` and
  calls only an input naming no record kind prose; TOOL-dDeclaredLoop-12's row names a record kind.
  The answer is one commit on the answerer's mail ref (KICK-dKeptSession-5 S2, S8); the
  `mailbox-message` record (its S12) is written later by the transition writer at disposal, for the
  question, never by this item. Options: (a) an ask to dDeclaredLoop that a `returns` naming no record
  kind is prose and joins nothing, as a prose input is, the row keeping a prose `returns`;
  TOOL-dPlacedRequest-3 already reads it so for `item.entry.claim` (its §4, the claim row "returns
  the claim ref"), so one answer re-grounds both; (b) `returns = "record-kind.mailbox-message@1"`, a
  record this item never writes, so an input could join to an item that does not produce it; (c) a
  new record kind per answer, a second copy of the mail commit. (b) states a false producer and (c)
  writes one fact twice. Recommendation (a). RESOLVED (owner, 2026-11-05): (a) the prose-`returns`
  ask, the row keeping a prose `returns`. The ask this build's run files in dDeclaredLoop's
  `BACKLOG.md` is "TOOL-dDeclaredLoop-24: on a non-role row, a `returns` naming no record kind is prose and joins
  nothing, as a prose input does, seen on `item.mailbox.answer` passing `check_item_composition` and
  red on an input naming `record-kind.<name>@<n>` from an item whose `returns` is prose".
  Re-grounded 2026-11-21: the ask's acceptance holds at HEAD, so it is not filed. The landed
  `derive_record_ref` reads no kind from a prose `returns`, and `check_item_composition` refuses an
  input whose kind no needed item returns; `item.entry.claim` already passes with a prose `returns`.
  The owner's pick, a prose `returns` on the row, stands.
- **F7 — How does S4 know the landed lease writer admits a question commit as its witness?** Options:
  (a) a version gate, the beat passing the question commit only at or past the driver version that
  lands F4's acceptance; (b) a capability probe, the beat running the witness check `--lease renew`
  applies over the question commit with no write; (c) a renew tried with the question commit and,
  on `lease not written` with exit 2, tried again with the transition witness. (a) compares one
  driver with itself, its version unknown until dPlacedRequest's acceptance lands; (c) spends a
  second bounded fetch per beat and reads every exit 2, a failed fetch included, as the refusal.
  RESOLVED (agent, 2026-10-26, delegated): (b), rung 3, the survivor that follows the landed rule with
  no version and no extra write; where the landed renew inlines the check, the build pass names it
  as one function both call, its verdict unchanged. widens: none · relaxes: none. Re-grounded
  2026-11-21: the landed check is that one function, `check_lease_witness`, which `--lease renew`
  calls and whose header names this unit's no-write call.
- **F8 — Where does the row sit, since the landed `check_program` admits a `step = "none"` row only
  under the `review`, `probe` or `entry` segment?** Options: (a) the entry program, tagged
  `item.entry.mailbox-answer`, the placement flow-steps' `[entry]` row gives it, with no loop kit
  change; (b) a fourth program, `mailbox` added to `PROGRAM_SEGMENTS`, keeping the tag
  `item.mailbox.answer`, an edit to the parent kit's program set, its README and `--check`'s program
  lines for one item; (c) a gov step's program, which F1 rejected. RESOLVED (agent, 2026-11-21,
  delegated): (a), rung 3; it is the record's own placement and changes no parent mechanism, where (b)
  adds a program of one item, and the clause's name stays in the actor and the carried node.
  widens: none · relaxes: none
- **F9 — What outcome does an `acked` question take?** Unit 5 S7 reads a question `acked` when an
  `ack` names it and no `answer` does, and its guard then lets the transition through, while unit 24
  expires only `open` rows. Options: (a) `defaulted`: the recipient acknowledged without answering,
  so the asker takes its declared default, as past the deadline; (b) `answered`, which reads an
  acknowledgement as an answer no message carries; (c) `awaiting`, a wait the guard has already
  released and no deadline ever ends. RESOLVED (agent, 2026-11-21, delegated): (a), rung 3; (c)
  leaves a wait no deadline ends, against cl-dClosedLoop-0162, and (b) claims an answer nobody gave.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 25, scout B row 8 and its
  disagreement 2, Shared interfaces I19, I20 and I23, the flow-steps `[rules]` paragraph and
  `[entry]` row, and v2's `leases.renewal` row.
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-44` mirrored, the other ends of
  the edges the round-1 spec audit's promoted units declare; no other section moved.
- rev-3 · 2026-10-26 · §2 S1, S4 · §3 Edges · §4 Evidence, The row, The wait in order, Rollout,
  Alternatives rejected · §6 AC4, AC5 · §8 F3, F4, F6, F7 · re-grounded on dDeclaredLoop at
  `783f1ad3a` and dPlacedRequest at `2740f0a3d` by the cross-check record
  `build/2026-10-26-build-KICK-dKeptSession-1-parents-crosscheck.md`, rows 82, 83, 87 and 90: the
  lease witness is the channel source, trailer or log record; the beat passes a question commit only
  once the landed witness check admits it (F7), else the transition witness; `returns` stays prose
  under F6's open ask; `on-deadline` names the `defaulted` route's target and F3's deferral goes.
- rev-4 · 2026-11-05 · §2 S1 · §3 Edges · §8 F6 · F6 resolved by the owner to (a), the prose-`returns`
  ask filed in dDeclaredLoop's `BACKLOG.md`, under the brief
  `2026-11-05-prompt-KICK-dKeptSession-1-owner-forks`; no other section moved.
- rev-5 · 2026-11-21 · §7 · the leg line names `scratch-guard self-test`, `tier2-review self-test`
  and `policy fixtures`, the legs whose manifest guards §4's `tools/unattended/unattended.sh` and
  `tools/govkit/govkit.py` trip, as the spec-tokens guards join named at the build run's spec stage
  under the brief `2026-11-21-prompt-KICK-dKeptSession-1-build-brief`; no other section moved.
- rev-6 · 2026-11-21 · §1 · S1 to S6 · §3 · §4 · §5 · AC1 to AC6 · §7 · §8 F1 F3 F4 F6 F7 F8 F9 ·
  §10 · re-grounded on the landed tree at `c2a407b0` by
  `2026-11-21-prompt-KICK-dKeptSession-10-orders-20-22-reground-brief`: the landed `check_program`
  refuses a `step = "none"` row outside the review, probe and entry segments, so the row is
  `item.entry.mailbox-answer` in the entry program (F8), in the landed shape, `on-deadline` an outcome
  and `awaiting` routed to itself (F3); dPlacedRequest accepted F4's ask, so S4 extends
  `read_lease_renewal` to pass the open question's commit to the landed `check_lease_witness`, which
  reads an expired question as closed, and AC4 is observable; `acked` reads `defaulted` (F9). Narrowed:
  the dPlacedRequest and dDeclaredLoop asks are dropped, both met at HEAD (F4, F6); AC5's
  before-the-ask half and rev-5's AC1 arm, in a loop self-test file the kit does not hold, are dropped; the kit version and the
  `subject-pins.tsv` regeneration left §4, and `policy fixtures`, `kit epoch` and the four govkit
  legs left §7, which gained the three loop legs and `docs`. Every line-number citation became a
  `path#symbol` or blob pin.

## 10. Reuse audit

The seams extended are the landed entry program of `tools/loop/loop.toml`, written as the row
`item.entry.claim` writes its wait, and the landed lease writer's witness derivation,
`tools/unattended/unattended.sh#read_lease_renewal`, whose one new step calls the landed one witness
check, `tools/unattended/unattended.sh#check_lease_witness`, and lets
`tools/unattended/unattended.sh#derive_lease_renews` renew on its `question` verdict. The answer verb
posts through unit 5's post path, as `--mail ack` does, and reads its rows through `read_mailbox`.
`python tools/codebase-map/reuse_lookup.py "answer a question by a declared default when no one
answers"`, re-run at this writing, ranked `declares`, `read_role_defaults`, `DerivedDefault`,
`check_item_declarations`, `declared_list` and `declared_scalar` by name stem; none answers a message
or renews on a wait, so no code seam fits beyond the landed lease writer's. Scout B's disagreement 2,
TOOL-dPlacedRequest-1 S8 renewing only on a transition, was §8 F4 and is closed by that unit's landed
question witness.

Recall terms used: mailbox.answer question answer default stand-in next unattended lease renewal progress declared wait witness check_lease_witness read_lease_renewal
