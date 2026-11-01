# KICK-dKeptSession-25 — `mailbox.answer`: a `question` to a build answered by its owning role, or by the asker's default until `next` dispatches it, the waiting build's lease renewed

**Status:** DEFERRED · rev-3 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 21 · advances KICK-dKeptSession-29

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
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-reground.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-reground.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-5 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-36 KICK-dKeptSession-44 KICK-dKeptSession-56 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |

<!-- /gen:spec-records -->

## 1. Goal

A `question` addressed to a build is an item, `mailbox.answer`, answered by the role that owns the
asked interface or item and dispatched by `next` when the question arrives. Until dWellOiledMachine
lands `next`, nothing dispatches it, so a question to an unattended build is answered by the asker's
declared default under cl-dClosedLoop-0162, the same stand-in covering its answering role (the closing
pair's answer-dispatch-non-ancestor). Meanwhile the recipient's transition is refused, and that
refusal is a declared wait inside `flow.wait-ceiling`, which `leases.renewal: progress` renews, so a
build waiting on a question does not lose its lease (the whole-design audit's A2-F5, the owner's
FK-5-4). Today the lease's renewal witness is a transition alone (TOOL-dPlacedRequest-1 S8), so a
build waiting 72 hours loses its 24-hour lease on the way.

## 2. Scope (IN)

- **S1** — The item row, `item.mailbox.answer`, one `[[item]]` row in `tools/loop/loop.toml` in
  TOOL-dDeclaredLoop-12's row shape: `step = "none"` (§8 F1), `owner = "dKeptSession"`, `needs = []`,
  actor `command:mailbox.answer` (§8 F2), outcomes `answered`, `awaiting` and `defaulted`, every route
  `stand-in:tools/unattended/unattended.sh` (§8 F3), `deadline = "policy.flow.wait-ceiling"` and
  `on-deadline = "stand-in:tools/unattended/unattended.sh"`, the `defaulted` route's target, the wait
  TOOL-dDeclaredLoop-33 S5's `wait` rule requires of a row whose outcomes hold `awaiting` (its
  `on-deadline`, "the route it takes past it"), `returns` prose while §8 F6 is open, and its witness
  the computed join of S3. Observed by AC1.
- **S2** — The answer verb, `unattended.sh --mail answer <slug> <question id> <body file> [--cite
  <path>@<sha>]…`, I19's member this unit owns. It posts one message of kind `answer`, `answers:
  <question id>`, addressed to the asking build, through `KICK-dKeptSession-5`'s post path. Before any
  commit it refuses with exit 2 an id naming no `question` addressed to `<slug>`, and a cite whose
  `git cat-file -e <sha>:<path>` fails; it refuses with exit 1, printing `answer — <id> · <state>`, a
  question whose state is not `open`. Each cite is written as a body line `cites <path>@<sha>`.
  Observed by AC2.
- **S3** — The outcome, `derive_mail_answer_outcome <slug> <question id>`, from I20's rows alone:
  `answered` when the question's state is `answered`, `defaulted` when it is `expired`
  (`KICK-dKeptSession-24`'s `check_mail_deadline` passed), `awaiting` while it is `open`. It is the
  item's witness and the beat's test (S4), and prints one word. Observed by AC2, AC3 and AC5.
- **S4** — The declared wait renews the lease. While `derive_mail_answer_outcome` answers `awaiting`
  for a `question` addressed to the build, the driver's `--beat`, which renews the build lease under
  TOOL-dPlacedRequest-1 S4 and S5, first asks the witness check the landed `--lease renew` applies to
  its `--witness` whether it admits the oldest such question's mail commit, with no write (§8 F7).
  Only when it admits it does the beat pass that commit as `--witness` and append ` · wait question
  <id>` to its `beat —` line. Otherwise the beat passes the transition witness TOOL-dPlacedRequest-1
  §4 "The witness under `progress`" names, the newest commit on the run's branch recording a
  transition of the build, as it does with no wait: that check exits 2 on a question commit until
  §8 F4's ask is accepted. Once no question awaits, the beat asks nothing and the renewal is S8's
  transition rule again. Observed by AC4 and AC5.
- **S5** — The stand-in, stated: until `next` exists, nothing runs `command:mailbox.answer` as a
  dispatch. An attended session answers through S2 when unit 10's interrupt shows the question; an
  unattended build, which no one answers, reaches `defaulted` at the deadline, and its transitions go
  on as `KICK-dKeptSession-5`'s guard refuses only `open` messages. No code tells the two apart
  (§8 F5). Observed by AC3.
- **S6** — The docs: the `--mail` section of `tools/unattended/VERBS.template.md` (rendered to
  `memory/guides/UNATTENDED-VERBS.md`) gains `--mail answer`, `--cite` and the wait's renewal, and
  `help/loop.md` gains the `mailbox.answer` row beside the entry items. Observed by AC6.

## 3. Non-goals (OUT)

- No `next` and no dispatch: dWellOiledMachine's. When it lands, `next` dispatches this item and its
  actor becomes the owning role (§3 Edges, the external hand-off).
- No deadline judgment: `check_mail_deadline` and the `expired` state are `KICK-dKeptSession-24`'s.
- No mailbox, kinds, guard or post path: `KICK-dKeptSession-5`'s.
- No change to the lease witness rule: TOOL-dPlacedRequest-1 S8's, changed only through §8 F4's ask.
- No owner question asked live: dFurnishedOrders' (cl-dClosedLoop-0155's join).
- No `[[stand-in]]` row: TOOL-dDeclaredLoop-13 S8's list holds transition-table items whose owning
  build has not landed, and this item is dKeptSession's and no table row's.

### Edges

- **consumes-from** `KICK-dKeptSession-5` — `read_mailbox`, its rows and states, and the `--mail post` path the answer is written through
- **consumes-from** `KICK-dKeptSession-24` — `check_mail_deadline` and the `expired` state, through which an unanswered question is answered by the asker's default
- **consumes-from** external — TOOL-dDeclaredLoop-12's `[[item]]` row shape and `check_program`, TOOL-dDeclaredLoop-9's actor grammar, TOOL-dDeclaredLoop-33's `wait` rule, and TOOL-dPlacedRequest-1's build lease, its `--beat` renew, `--witness` and the witness check its renew applies
- **hands-off** external — dWellOiledMachine's `next` dispatches `mailbox.answer` when a question arrives and re-points its actor to the owning role, with the per-question actor form TOOL-dDeclaredLoop-9's grammar does not spell
- **hands-off** external — dPlacedRequest admits a declared wait on an open question as a renewing witness under `leases.renewal: progress` (§8 F4, an ask)
- **hands-off** external — dDeclaredLoop admits a prose `returns` naming no record kind on a non-role row (§8 F6, an ask open for the owner)
- **hands-off** `KICK-dKeptSession-44` — §7's covers list, AC4 taken out of it by the batch's S2 (id 5)

## 4. Design

### Evidence

- flow-steps' `[entry]` row (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md:128`):
  actor "the role that owns the asked interface or item, one per question"; proven by "a computed
  join: the `answer` message names the question's id and cites records that exist at their SHAs";
  then "answered → done … no answer within `flow.wait-ceiling`, or no `next` to dispatch the question
  before dWellOiledMachine lands it → back to the asking item, which takes its declared default".
- The `[rules]` paragraph (:78-83): the transition refused while a message awaits its answer is a
  declared wait inside `flow.wait-ceiling`, so `leases.renewal: progress` renews the lease.
- v2:1159: `progress` renews "on declared waits inside their deadline"; TOOL-dPlacedRequest-1 S8
  renews only on a commit that records a transition of the build on the channel `transitions.record`
  makes, its `Gov-Transition` trailer or its `-transition-<n>.md` log record, and that differs from
  the record's `witness` (scout B's disagreement 2); any other `--witness` exits 2, and under
  `micro-format` alone no commit witnesses (its §4 "The witness under `progress`").
- The entry items take `step = "none"` (TOOL-dPlacedRequest-3 §8 F2); TOOL-dDeclaredLoop-9 S1's actor
  is one `<kind>:<name>`, and layer-roles' `[matrix]` notes the instrument cannot read which role owns
  a question (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-layer-roles.md:434-438`).

### The row

```toml
# tools/loop/loop.toml — mailbox.answer, before any step (flow-steps.md:128)
[[item]]
tag = "item.mailbox.answer"
step = "none"
actor = "command:mailbox.answer"   # the stand-in covering the owning role until `next` (cl-dClosedLoop-0504)
needs = []
inputs = ["layer.flow:the question message", "layer.memory:the asked interface's declaration or the asked item's witnesses"]
allowance = "records"
returns = "the answer's mail commit"   # prose, no record kind: §8 F6's ask
outcomes = ["answered", "awaiting", "defaulted"]
deadline = "policy.flow.wait-ceiling"
on-deadline = "stand-in:tools/unattended/unattended.sh"   # the `defaulted` route's target
witness = { class = "history", by = "derive_mail_answer_outcome over the question's mail rows" }
owner = "dKeptSession"
[item.routes]
answered = "stand-in:tools/unattended/unattended.sh"
awaiting = "stand-in:tools/unattended/unattended.sh"
defaulted = "stand-in:tools/unattended/unattended.sh"
```

### The wait, in order

1. A `question` addressed to `build:<slug>` lands; unit 5's guard refuses the build's next
   transition while it reads `open`.
2. Each `--beat` asks `derive_mail_answer_outcome` for the build's open questions, oldest first by
   first sighting; on `awaiting` it renews the lease with that question's commit as `--witness` when
   the landed witness check admits it, and with the transition witness otherwise (S4).
3. An answer through S2 makes the question `answered`; the deadline passing makes it `expired` and
   the outcome `defaulted`. Either way the guard lets the transition through and the beat stops
   passing the witness.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `item.mailbox.answer` | loop item tag | none |
| `command:mailbox.answer` | item actor | none |
| `--mail answer`, `--cite` | verb and flag of `tools/unattended/unattended.sh` | none |
| `derive_mail_answer_outcome` | shell function | `derive`, OK |

### Migration

None: no question exists before unit 5 lands.

### Rollout

Behind `RUN_CLAIMS` with every mail verb. S4 renews only once dPlacedRequest accepts §8 F4's ask.
Before it, the witness check refuses a question commit, so the beat passes the transition witness and
its lease commit and `beat-utc` move as they do with no wait: nothing renews early, and no beat is
refused `lease not written` because a question awaits. The beat passes the question commit from the
first beat after the accepting landing, with no change here.

### Files touched (estimate)

- `tools/loop/loop.toml`: the `item.mailbox.answer` row
- `tools/unattended/unattended.sh`: `--mail answer`, `derive_mail_answer_outcome`, the beat's
  witness, `KIT_UNATTENDED_VERSION` moved
- `tools/unattended/unattended.test.sh`: the arms of §7
- `tools/unattended/VERBS.template.md`: `--mail answer`, `--cite`, the wait
- `memory/guides/UNATTENDED-VERBS.md`: its render
- `help/loop.md`: the `mailbox.answer` row
- `tools/govkit/subject-pins.tsv`, regenerated by `python tools/govkit/govkit.py selfcheck --write`

### Alternatives rejected

- **A transition commit written to renew the lease while waiting.** A transition recorded, by trailer
  or log record, for a move that did not happen is a false witness, and the position engine would read
  it as one.
- **A version gate on the beat's witness.** The lease verbs and the beat are one driver, so a version
  compared there compares the file with itself; the witness check is the landed rule itself (§8 F7).
- **An answer posted by the waiting build at once, from the asker's default.** The clause answers by
  default only past the deadline, under cl-dClosedLoop-0162.
- **A `[[stand-in]]` row naming dWellOiledMachine.** TOOL-dDeclaredLoop-13 S8 reds a stand-in row whose
  owner differs from the item's.

## 5. Production-readiness checklist

- security — `--mail answer`'s body passes I17's body check; each cite is resolved by `git cat-file -e`
  before the post, so an answer cannot cite a record that does not exist.
- perf / scale — the beat reads the build's mail rows once; questions are few per build.
- error / empty / loading states — an unknown id or a bad cite exits 2 with nothing written; an
  answered or expired question exits 1 naming its state.
- observability — the `beat —` line names the question a renewal waits on.
- risks — until dPlacedRequest accepts §8 F4, a 72-hour wait still loses a 24-hour lease; AC4 is the
  observation that it does not.
- testing — the probes of §6 and the arms of §7.
- migration — none.
- user docs — `memory/guides/UNATTENDED-VERBS.md` and `help/loop.md`.

## 6. Acceptance criteria

- **AC1** — When `python loop_lib.py --check` and `python termination.py check` run over a loop
  definition holding the `item.mailbox.answer` row, both pass; with the row's `deadline` removed,
  `termination.py check` exits 1 naming `item.mailbox.answer` under its `wait` rule.
  Red when: the item's wait declares no deadline and nothing says so.
- **AC2** — When `bash tools/unattended/unattended.sh --mail answer <slug> <qid> <file> --cite
  <path>@<sha>` runs over an open question addressed to `build:<slug>`, an `answer` message with
  `answers: <qid>` and the line `cites <path>@<sha>` is posted to the asking build, and
  `derive_mail_answer_outcome <slug> <qid>` prints `answered`; a second answer exits 1 printing
  `answer — <qid> · answered`, and a cite whose sha does not hold the path exits 2 with no commit.
  Red when: a question is answered twice, or an answer cites a record that does not exist.
  fixture: a scratch clone with a bare origin under `%TEMP%`, `RUN_CLAIMS=on`, two builds and a
  fleet tag.
- **AC3** — When a question with `deadline: 30` is planted to an unattended build and nobody answers,
  with its feed line sighted one hour ago `derive_mail_answer_outcome` prints `awaiting` and
  `python loop_transition.py record` is refused naming the id; with the line planted 31 hours ago it
  prints `defaulted`, the record is written, and `--mail read` shows the question's `default`.
  Red when: an unattended build answers before the deadline, or blocks past it.
- **AC4** — When a question addressed to the build was sighted 30 hours ago with `deadline: 72`, and
  the build lease's last renewing commit 25 hours ago under `leases.expiry-hours = 24`, `--beat` writes
  a lease commit carrying `witness: <the question's commit>` and `renews: yes`, its line ends
  ` · wait question <qid>`, and `--claims` reads the lease `live`; a scratch copy of the driver whose
  beat passes no wait witness leaves the lease `stale`. This is the clause's planted question to an
  unattended build whose lease lapses while it waits.
  Red when: the lease lapses while the build waits inside the deadline.
  fixture: observable once dPlacedRequest accepts §8 F4's ask; before it, the witness check refuses
  the question's commit, the beat passes the transition witness and writes `renews: no`, so the
  planted case reads `stale` both ways and the arm stays red.
- **AC5** — When the same question's sighting is planted 73 hours ago, `derive_mail_answer_outcome`
  prints `defaulted` and `--beat` passes no wait witness, so the lease's renewal follows the
  transition rule alone. With the sighting planted 30 hours ago under a witness check that refuses a
  question commit, as before §8 F4's ask lands, `--beat` exits 0, writes a lease commit whose
  `witness` is the planted transition commit, moves `beat-utc`, and its line names no `wait question`.
  Red when: an expired wait keeps a lease alive for ever, or a beat during a wait is refused or writes
  no lease commit while the check refuses the question's commit.
- **AC6** — When `grep -n -- '--mail answer\|--cite\|wait question'` runs over
  `tools/unattended/VERBS.template.md`, and `grep -n 'item.mailbox.answer'` over `loop.md`, the loop kit's help page, each
  is found.
  Red when: the verb or the item is undocumented.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix`

New arm: tools/unattended/unattended.test.sh · covers AC2 AC3 AC4 AC5 · the answer, the default and the wait arms over planted mail commits, feed lines and lease chains, AC4 staged by a scratch copy whose beat passes no witness · `FLOOR_ASSERTIONS` and its shard floor rise by the arms' count, counted off the diff
New arm: tools/loop/selftest.py · covers AC1 · the row with its `deadline` removed, red under the `wait` rule · none

## 8. Open questions

- **F1 — What `step` does `item.mailbox.answer` carry?** Options: (a) `step = "none"`, the value
  TOOL-dPlacedRequest-3 §8 F2 gives the entry items, since flow-steps places `mailbox.answer` in
  `[entry]`, before any step; (b) a step of its own, which changes TOOL-dDeclaredLoop-1's five-step
  definition, a parent's mechanism. RESOLVED (agent, 2026-10-26, delegated): (a), rung 1,
  flow-steps.md:128. widens: none · relaxes: none
- **F2 — What actor does the row declare while `next` is unbuilt?** Options: (a)
  `command:mailbox.answer`, the stand-in the clause says covers the answering role, the owning role
  joining when `next` dispatches the item; (b) a per-question role, which TOOL-dDeclaredLoop-9 S1's
  grammar cannot spell, since `role:<slot>` names one slot and the owning role is chosen per question.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, the clause's "the same stand-in covering its
  answering role". widens: none · relaxes: none
- **F3 — What are the item's outcomes and routes?** Options: (a) `answered`, `awaiting` and
  `defaulted`, every route `stand-in:tools/unattended/unattended.sh`, the tool that answers and judges
  today, with `deadline` and `on-deadline` as TOOL-dDeclaredLoop-33 S5 requires; (b) `answered` and
  `defaulted` only, so the recipient's wait is declared nowhere and the `wait` rule cannot see it. The
  asking item belongs to another build, so no route can name it. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3; `on-deadline` names the `defaulted` route's target, as
  TOOL-dDeclaredLoop-33 S5 reads the key. widens: none · relaxes: none
- **F4 — How does a waiting build's lease renew, when TOOL-dPlacedRequest-1 S8 renews only on a
  transition?** Options: (a) this unit's beat passes the open question's commit as `--witness`, and an
  ask asks dPlacedRequest to accept it while the question is inside its deadline; (b) a transition
  commit written to renew, a false witness; (c) edit TOOL-dPlacedRequest-1, which the brief bars.
  RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, v2:1159 ("renews … on declared waits inside
  their deadline"). Ask: target dPlacedRequest · accept under `leases.renewal: progress` a renew whose
  `--witness` is the commit of a mail message of kind `question` addressed to the lease's build, `open`
  on this node and inside its declared deadline by `check_mail_deadline`, writes `renews: yes` even when
  it records no transition of the build on the channel `transitions.record` makes, and even when it
  equals the record's `witness`, seen on a lease kept live past a 24-hour `leases.expiry-hours` by a
  30-hour wait, and red on that witness once the question reads `expired`. widens: none · relaxes: none
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
  writes one fact twice. Recommendation (a). Open for the owner: the ask the build run files is
  "TOOL-dDeclaredLoop-24: on a non-role row, a `returns` naming no record kind is prose and joins
  nothing, as a prose input does, seen on `item.mailbox.answer` passing `check_item_composition` and
  red on an input naming `record-kind.<name>@<n>` from an item whose `returns` is prose".
- **F7 — How does S4 know the landed lease verb admits a question commit as `--witness`?** Options:
  (a) a version gate, the beat passing the question commit only at or past the driver version that
  lands F4's acceptance; (b) a capability probe, the beat running the witness check `--lease renew`
  applies over the question commit with no write; (c) a renew tried with the question commit and,
  on `lease not written` with exit 2, tried again with the transition witness. (a) compares one
  driver with itself, its version unknown until dPlacedRequest's acceptance lands; (c) spends a
  second bounded fetch per beat and reads every exit 2, a failed fetch included, as the refusal.
  RESOLVED (agent, 2026-10-26, delegated): (b), rung 3, the survivor that follows the landed rule with
  no version and no extra write; where the landed renew inlines the check, the build pass names it
  as one function both call, its verdict unchanged. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 25, scout B row 8 and its
  disagreement 2, Shared interfaces I19, I20 and I23, flow-steps.md:78-83 and :128, and v2:1159.
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-44` mirrored, the other ends of
  the edges the round-1 spec audit's promoted units declare; no other section moved.
- rev-3 · 2026-10-26 · §2 S1, S4 · §3 Edges · §4 Evidence, The row, The wait in order, Rollout,
  Alternatives rejected · §6 AC4, AC5 · §8 F3, F4, F6, F7 · re-grounded on dDeclaredLoop at
  `783f1ad3a` and dPlacedRequest at `2740f0a3d` by the cross-check record
  `build/2026-10-26-build-KICK-dKeptSession-1-parents-crosscheck.md`, rows 82, 83, 87 and 90: the
  lease witness is the channel source, trailer or log record; the beat passes a question commit only
  once the landed witness check admits it (F7), else the transition witness; `returns` stays prose
  under F6's open ask; `on-deadline` names the `defaulted` route's target and F3's deferral goes.

## 10. Reuse audit

The seams extended are TOOL-dDeclaredLoop-12's `[[item]]` row shape in `tools/loop/loop.toml`, written
as TOOL-dPlacedRequest-3 writes the entry items, and TOOL-dPlacedRequest-1's build lease renew, whose
`--witness` this unit fills while a question awaits. None exists at base: `tools/loop/` is absent, and
the driver's beat is today's claim beat (`write_claim_beat`, dispatched at
`tools/unattended/unattended.sh:14538`), which TOOL-dPlacedRequest-1 S4 moves onto the build lease.
`python tools/codebase-map/reuse_lookup.py "answer a question by a declared default when no one
answers"` ranked `declares`, `declared_list`, `declared_scalar` and `default_kits`, name stems only;
no existing function answers a message or renews on a wait, so no code seam fits beyond the parents'.
`python tools/memory-recall/query.py "who answers a question addressed to a build before next exists"`
returned this build's brief, the packet's Items and scout B's row 8; scout B's disagreement 2 holds
against TOOL-dPlacedRequest-1 S8's text and is §8 F4.

Recall terms used: mailbox.answer question answer default stand-in next unattended lease renewal progress declared wait witness
