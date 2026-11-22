# KICK-dKeptSession-25 — `mailbox.answer`: a `question` to a build answered by its owning role, or by the asker's default until `next` dispatches it, the waiting build's lease renewed

**Status:** DEFERRED · rev-8 · 2026-11-23 · node a · Tier-2 · base 8b8b1374 · streams kickoff · order 21 · advances KICK-dKeptSession-29

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
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-10-orders-20-22-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-10-orders-20-22-reground-brief.md) | research | KICK-dKeptSession-10 KICK-dKeptSession-21 |
| [2026-11-21-prompt-KICK-dKeptSession-24-precheck-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-24-precheck-brief.md) | research | KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-5 |
| [2026-11-22-prompt-KICK-dKeptSession-25-reground-brief.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-25-reground-brief.md) | research | — |
| [2026-11-23-prompt-KICK-dKeptSession-25-1-spec-writer.md](../prompts/2026-11-23-prompt-KICK-dKeptSession-25-1-spec-writer.md) | journal | — |
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
  and `owner = "dKeptSession"`. It sits after `item.entry.claim`, and the program's header comment,
  which lists the program as "orient, place by the policy key `placement`, claim", gains the answer.
  Observed by AC1.
- **S2** — The answer verb, `unattended.sh --mail answer <slug> <question id> <body file> [--cite
  <path>@<sha>]…`, a member of `KICK-dKeptSession-5`'s `--mail` family, run by a new function
  `write_mail_answer` beside `tools/unattended/unattended.sh#write_mail_ack`. `<slug>` is the
  answering build. In order:
  1. While `RUN_CLAIMS` is not `on` it prints `mail — off`, exit 2, as `--mail ack` does.
  2. Each `--cite` value splits at its last `@` into a non-empty path and a sha matching
     `^[0-9a-f]{7,40}$`; any other prints `mail — not written · --cite takes <path>@<sha>, not
     <value>`, exit 2, before any read.
  3. It reads `read_mailbox <slug> soft` once; a refused read prints its line, exit 2.
  4. The row whose id is `<question id>` and whose kind is `question` is the question; none prints
     `mail — not written · <question id> is no question addressed to <slug>`, exit 2.
  5. A question reading `answered`, `acked` or unit 24's `expired` prints `answer — <question id> ·
     <state>`, exit 1.
  6. A cite failing `git cat-file -e <sha>:<path>` prints `mail — not written · the cite
     <path>@<sha> names no file this clone holds at that commit`, exit 2.
  7. A scratch body holds the body file and one line `cites <path>@<sha>` per cite, in flag order;
     an unreadable body file prints `mail — not written · the body file cannot be read: <file>`,
     exit 2.
  8. It calls `write_mail_post` as `write_mail_ack` does, with eight arguments: `<slug>`,
     `build:<from-build>` of the row, `answer`, the row's subject, `none`, `none`, the question's id
     and the scratch body. Unit 5's body checks hold the body, unit 27's absent interface reads
     `none`, and unit 24 writes `deadline` and `default: ack`. The post's line and exits are the
     answer's.

  The dispatch's `--mail` arm parses `--cite <value>`, repeatable; with no value it prints `mail —
  not written · --cite takes a value`, exit 2. Its `answer` form takes three positional words and no
  flag but `--cite`, else `mail — not written · the form is --mail answer <slug> <question id> <body
  file> [--cite <path>@<sha>]…`, exit 2; the `post`, `read` and `ack` forms refuse `--cite` in their
  own form refusals. The unknown-flag and unknown-verb refusals name the new words beside those units
  27 and 24 add, and the arm's comment, "a post …, a read …, an ack", names the answer. The usage
  header gains the row `#   unattended.sh --mail answer <slug> <question id> <body file> [--cite
  <path>@<sha>]...`, its comment naming exit 1 for a question no longer open. Observed by AC2.
- **S3** — The outcome, `derive_mail_answer_outcome <slug> <question id>` in
  `tools/unattended/unattended.sh`, from `read_mailbox <slug> soft`'s rows alone (unit 5 S6 and S7,
  `KICK-dKeptSession-24` S5): `answered` when the question's state is `answered`; `defaulted` when it
  is `expired`, `check_mail_deadline` having passed, or `acked` (§8 F9); `awaiting` while it is
  `open`. It prints that one word, exit 0, and is the item's witness. An id naming no `question` row
  addressed to `<slug>` prints `mail — not read · <question id> is no question addressed to <slug>`,
  and a refused read prints the read's line; both exit 2. Observed by AC2, AC3 and AC5.
- **S4** — The declared wait renews the lease. `read_lease_renewal`, the witness the driver derives
  for every claim write it makes of its own run, `--beat`'s included (`write_claim_beat` calls
  `write_claim`, which calls it), gains one step under `progress` and one variable, `LR_WAIT`, empty
  at its top. Its landed step stays first: the newest transition is `new` where it differs from the
  record's `witness` (`tools/unattended/unattended.sh#read_lease_renewal`). Where it finds none, the
  new step reads `read_mailbox <slug> soft 2>/dev/null`, as `check_lease_witness` does, so a write's
  output is unchanged where no question is open; takes the first `question` row reading `open`, the
  oldest by the read's own order; and runs the landed `check_lease_witness <slug> <its commit>`,
  which writes no ref (§8 F7). On the verdict `question` it sets `LR_VERDICT` to `question` and
  `LR_WAIT` to the row's id and keeps `LR_WITNESS` the record's `witness` (§8 F10), so
  `derive_lease_renews` writes `renews: yes`. Any other verdict, `question-closed` included, keeps
  `none`. `--beat`'s `renewed <utc>` line, on a write that returned 0, then ends ` · wait question
  <id>` where `LR_WAIT` is set. The header comment, "every other case … is `none`", names the
  question step and the kept witness. Observed by AC4 and AC5.
- **S5** — The stand-in, stated: until `next` exists, nothing runs `command:mailbox.answer` as a
  dispatch. An attended session answers through S2 when `KICK-dKeptSession-10`'s interrupt shows the
  question; an unattended build, which no one answers, reaches `defaulted` at the deadline, and its
  transitions go on, as unit 5's guard refuses only `open` rows. No code tells the two apart (§8 F5).
  Observed by AC3.
- **S6** — The shipped texts this unit makes false, each rewritten:
  - `tools/unattended/VERBS.template.md` and its byte-equal copy `memory/guides/UNATTENDED-VERBS.md`:
    the `--mail` entry's "three verbs" reads four and gains `--mail answer`, its refusals and
    `--cite`; the `--beat` entry's `renewed` gains the ` · wait question <id>` suffix.
  - `tools/unattended/STOPS.template.md` and its byte-equal copy `memory/guides/UNATTENDED-STOPS.md`:
    the `leases.renewal` row's "only a `--witness` that …" names the driver's own writes too, the
    newest transition differing from the record's `witness`, else the oldest open `question` to the
    build, which renews and keeps that `witness`.
  - `help/loop.md`: the entry section's "five items" reads six, its table gains the row and a
    paragraph its outcomes and routes; the guard paragraph's "answer or acknowledge each (`--mail ack
    <slug> <id>`)" names `--mail answer` for a question; the `--mail` paragraph names `--mail answer`
    and `--cite`, its `verb:unattended.sh:--mail` anchor re-stamped with the fingerprint
    `python tools/govkit/docs_leg.py --fingerprints` prints at build time, since `--cite` joins the
    flags it hashes (`tools/govkit/docs_leg.py#read_verb_usage`).
  - `read_mailbox`'s comment "Columns only append: `check_lease_witness` reads 2, 4 and 10 by
    position" also names the three new readers' columns 1, 2, 4, 6, 7 and 10.

  Observed by AC6.

## 3. Non-goals (OUT)

- No `next` and no dispatch: dWellOiledMachine's. When it lands, `next` dispatches this item and its
  actor becomes the owning role (the external hand-off below).
- No deadline judgment: `check_mail_deadline` and the `expired` state are `KICK-dKeptSession-24`'s.
- No mailbox, kinds, guard or post path: `KICK-dKeptSession-5`'s.
- No change to the lease witness rule: TOOL-dPlacedRequest-1 S8 already admits an open question's
  commit (its §8 F9), and this unit only passes one.
- No change to `--lease renew --witness`: a verb's caller names its witness each time, and the verb
  stores it as landed.
- No owner question asked live: dFurnishedOrders' (cl-dClosedLoop-0155's join).
- No `[[stand-in]]` row: the landed rows list items whose owning build has not landed
  (`tools/loop/loop.toml`, its `[[stand-in]]` rows), and this item's owner lands it here.
- No change to the loop kit's programs: the row joins the entry program
  (`tools/loop/loop_lib.py#PROGRAM_SEGMENTS`).
- No kit version: the lander mints it (`tools/push-main.sh@3a5bf825e879:27`).

### Edges

- **consumes-from** `KICK-dKeptSession-5` — `read_mailbox`, its rows and states, and the post path `--mail answer` writes through
- **consumes-from** `KICK-dKeptSession-24` — `check_mail_deadline` and the `expired` state, through which an unanswered question is answered by the asker's default
- **consumes-from** external — the landed entry program and row shape (TOOL-dPlacedRequest-3, TOOL-dDeclaredLoop-12), `termination.py`'s `wait` rule (TOOL-dDeclaredLoop-33), TOOL-dDeclaredLoop-9's actor grammar, and the landed lease writer's `read_lease_renewal`, `check_lease_witness` and `derive_lease_renews` (TOOL-dPlacedRequest-1, TOOL-dPlacedRequest-25)
- **hands-off** external — dWellOiledMachine's `next` dispatches `mailbox.answer` when a question arrives and re-points its actor to the owning role, with the per-question actor form TOOL-dDeclaredLoop-9's grammar does not spell
- **hands-off** `KICK-dKeptSession-44` — §7's covers list, the batch's S2 (id 5), whose premise, an ask dPlacedRequest had not accepted, the landed TOOL-dPlacedRequest-1 retired

## 4. Design

### Evidence

Read on the run tree at `d06e2a65`, 2026-11-23, with units 36, 39, 51, 27 and 24 read as landed.

- flow-steps' `[entry]` row gives the actor as "the role that owns the asked interface or item, one
  per question", proven by a computed join of the `answer` message to the question's id that cites
  records existing at their SHAs
  (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md@d73cb002d028:128`).
- Its bullet "A question to a build is answered" makes the transition refused while a message awaits
  its answer a declared wait inside `flow.wait-ceiling`, which `leases.renewal: progress` renews
  (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-flow-steps.md@d73cb002d028:78`).
- Under `progress` a write renews on a `new` or a `question` verdict
  (`tools/unattended/unattended.sh#derive_lease_renews`). `check_lease_witness` answers `question`
  for an `open` question row's commit and `question-closed`, exit 1, for any other state
  (`tools/unattended/unattended.sh#check_lease_witness`); unit 24 S3 deletes its `declare -F` probe,
  so it reads the mailbox on every call.
- The driver's own claim writes take their witness from `read_lease_renewal`, which sets `new` where
  `read_transition_witness`'s newest transition differs from `CW_WIT`, the record's `witness`, and
  never compares ages (`tools/unattended/unattended.sh#read_lease_renewal`). `--beat` renews through
  `write_claim` and prints one `beat —` line (`tools/unattended/unattended.sh#write_claim_beat`),
  which the resume tick quotes whole; every suite matches its `renewed ` prefix.
- `read_mailbox` prints one TAB row per message, oldest sighting first: unit 5's eleven columns, id,
  kind, to, state, first-seen, from-build, subject, answers, ref, commit and reply, then unit 27's
  three and unit 24's two (`tools/unattended/unattended.sh#read_mailbox`). `write_mail_ack` reads
  columns 1, 6 and 7 and posts with eight arguments (`tools/unattended/unattended.sh#write_mail_ack`).
- `check_program` admits a `step = "none"` row only under a segment of `PROGRAM_SEGMENTS`, `review`,
  `probe` or `entry` (`tools/loop/loop_lib.py#check_program`). The landed wait row `item.entry.claim`
  writes `waits`, `deadline`, an `on-deadline` naming an outcome, and inline `routes` with a
  `{prefix}` stand-in (`tools/loop/loop.toml`, row `item.entry.claim`).
- TOOL-dDeclaredLoop-9's actor is one `<kind>:<name>` (`tools/loop/loop_lib.py#ACTOR_FORM`).
- A prose `returns` names no record kind (`tools/loop/loop_items.py#derive_record_ref`), so the record
  join reads nothing from it (`tools/loop/loop_items.py#check_item_composition`).

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
2. Each own claim write, every `--beat` among them, takes a transition differing from the record's
   `witness` first, else the oldest open question to the build, which `check_lease_witness` admits:
   it renews, the `witness` stays the last transition, and the beat's line names the question.
3. An answer makes the question `answered`, the deadline `expired`, an `ack` `acked`. The guard then
   passes, `check_lease_witness` answers `question-closed`, and a beat renews once a move is recorded.

### Texts that stay true

The entry section's heading names the request path, which holds, and the closed
TOOL-dPlacedRequest-3 ledger records it. `check_lease_witness`'s header already names this unit's
probe, and `write_claim`'s names `read_lease_renewal`. `help/orientation-card.md` and
`tools/loop/README.md` name mail states, never verbs, and the entry program by its segment. No help
page states the beat's line: `verb:unattended.sh:--beat` names none (PINNED, `docs_leg.py
--fingerprints`, 2026-11-23). The catalogue's `leases.renewal` row has no summary, so
`.governance/policy.json` does not move.

### The refusal ceiling

`tools/unattended/unattended.sh` sits at its ceiling, 347 sites (PINNED,
`.memory-tree.conf@d4f8d497b8c3:661`, 2026-11-23). The census counts a `fail <n> "` call, an `exit 1`
word and a `status=1` assignment (`tools/memory-tree/check-arms.py#FAIL_RE`, `#EXIT_RE`,
`#STATUS_RE`). This unit adds none: `write_mail_answer`'s refusals are `echo …; return 2` and
`return 1`, `derive_mail_answer_outcome`'s `return 2`, and the `--mail` arm's `_rl_rc=2`. The
ceiling is met unraised.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `item.entry.mailbox-answer` | loop item tag | `tag.item`, OK by `lexicon.py --tags` |
| `command:mailbox.answer` | item actor | none |
| `--mail answer`, `--cite` | verb and flag of `tools/unattended/unattended.sh` | none |
| `write_mail_answer` | shell function | `sh.function`, OK by `lexicon.py --suggest` |
| `derive_mail_answer_outcome` | shell function | `sh.function`, OK by `lexicon.py --suggest` |
| `LR_WAIT` | variable `read_lease_renewal` sets | none declared |

### Migration

None: no question exists before unit 5 lands, and a lease record keeps its shape.

### Rollout

Behind `RUN_CLAIMS` with every mail verb. The question step reads unit 5's `read_mailbox`, whose
deadline judgment unit 24 adds, both earlier in build order, so S4 renews from the first beat after
this unit lands.

### Files touched (estimate)

- `tools/loop/loop.toml`: the `item.entry.mailbox-answer` row in the entry program and its header
  comment
- `tools/unattended/unattended.sh`: `write_mail_answer`, `--mail answer`'s parse and usage row,
  `derive_mail_answer_outcome`, `read_lease_renewal`'s question step, the beat's ` · wait question`
  suffix, and the comments §4's table names
- `tools/unattended/unattended.test.sh`: the arms of §7, inline, defining no shell function, and the
  effective `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8` raised by their counted assertions, each with a
  `RAISED` line. They read 4100 and 1317 at `d06e2a65`
  (`tools/unattended/unattended.test.sh@3d75bb5502e5:24312` and `:24601`, DERIVED, the last
  assignment of each); units 27 and 24 raise both first. No budget row is re-priced: the shard rows
  are ESTIMATE rows carrying no `plants=` token
  (`tools/run-gates/selftest-budgets.txt@9709091da4b8:161`), and no loop plant is added
- `tools/unattended/VERBS.template.md` and `memory/guides/UNATTENDED-VERBS.md`: S6
- `tools/unattended/STOPS.template.md` and `memory/guides/UNATTENDED-STOPS.md`: S6
- `help/loop.md`: S6, the `verb:unattended.sh:--mail` anchor reading `f25c9c53` before units 27 and 24
  re-stamp it (PINNED, `docs_leg.py --fingerprints` at `d06e2a65`)
- `memory/map/generated/symbols.json`: `write_mail_answer` and `derive_mail_answer_outcome`,
  re-rendered by the codebase map's generator, never hand-edited

### Alternatives rejected

- **A transition commit written to renew the lease while waiting.** A transition recorded, by trailer
  or log record, for a move that did not happen is a false witness, and the position engine would read
  it as one.
- **The question's commit stored as the record's `witness`.** The next write's transition step reads
  the older transition as differing from it, so the lease renews once more after the question closes
  with no move made (§8 F10).
- **An answer posted by the waiting build at once, from the asker's default.** The clause answers by
  default only past the deadline, under cl-dClosedLoop-0162.
- **A `[[stand-in]]` row naming dWellOiledMachine.** The landed stand-in rows hold items whose owner
  has not landed, and this item's owner is dKeptSession.
- **The question step only on the beat**, a flag beside `read_lease_renewal`. Every own claim write
  during the wait is a write inside it, so a flag would make one witness rule two.

## 5. Production-readiness checklist

- security — the body passes unit 5's body check; each cite's sha is held to hex before any git call
  and resolved by `git cat-file -e` before the post, so no answer cites a missing record.
- perf / scale — with no differing transition each own claim write reads the mailbox once, and once
  more inside `check_lease_witness` during a wait. Questions are few per build.
- error / empty / loading states — S2's exit 2 writes nothing; a closed question exits 1; a failed
  fetch reads the cache under `soft`.
- observability — the `beat —` line names the question a renewal waits on.
- risks — an unsighted question sorts last and still renews while `open`; a `witness` a `--lease
  renew --witness <question>` stored reads the next transition as `new` once, as the verb landed.
- testing — §6 and §7. migration — none.
- user docs — the two guides of S6 and `help/loop.md`.

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
  second answer exits 1 printing `answer — <qid> · answered`; a cite whose sha does not hold the
  path, and one whose sha is `-x`, each exit 2 with no commit; an id naming no question exits 2
  printing `is no question addressed to`; and `--mail read <slug> --cite a@b` exits 2.
  Red when: a question is answered twice, or an answer cites a record that does not exist.
  fixture: a scratch clone with a bare origin under `%TEMP%`, `RUN_CLAIMS=on`, two builds and a
  fleet tag, the question posted with `--default no`, which `KICK-dKeptSession-24` S2 requires.
- **AC3** — When a question with `deadline: 30` is planted to an unattended build and nobody answers,
  with its feed line sighted one hour ago `derive_mail_answer_outcome` prints `awaiting` and
  `--mail read <slug> --open --ids` prints its id, the row unit 5's guard refuses on; with the line
  planted 31 hours ago it prints `defaulted`, `--open --ids` prints `none`, and `--mail read` shows
  the question `expired` with its `default`.
  Red when: an unattended build answers before the deadline, or blocks past it.
  figure: the deadline and both sightings are PINNED fixture literals.
- **AC4** — When a question addressed to the build was sighted 30 hours ago with `deadline: 72`, the
  lease record's `witness` is the newest transition the branch records, and a due `--beat` runs under
  the default `progress`, the lease commit it writes carries `renews: yes` and that same `witness`,
  and its line ends ` · wait question <qid>`; a second due beat writes the same; a scratch copy of the
  driver whose `read_lease_renewal` skips the question step writes `renews: no`.
  This is the clause's planted question to an unattended build, whose lease would otherwise lapse.
  Red when: a beat during a wait inside its deadline renews nothing.
  fixture: a scratch clone with a bare origin, `RUN_CLAIMS=on`, a run `--liveness` reads LIVE here,
  each beat made due as the landed `--beat` arm makes one, and the question's ref and feed line.
  figure: the sighting and the deadline are PINNED fixture literals.
- **AC5** — When the same question's sighting is planted 73 hours ago, `derive_mail_answer_outcome`
  prints `defaulted` and `--beat` writes `renews: no` with the record's `witness` unchanged and no
  `wait question` in its line. The same holds with the question answered after a beat that renewed on
  it, where a scratch copy storing the question's commit as the `witness` writes `renews: yes`. With
  a transition commit differing from the record's `witness` planted beside the open question, the
  beat's `witness` is that transition and its line names no wait.
  Red when: an expired or answered wait keeps renewing, or a wait outranks a newer transition.
  figure: the sighting is a PINNED fixture literal.
- **AC6** — When `grep -n -- '--mail answer\|--cite\|wait question' tools/unattended/VERBS.template.md`
  runs, `grep -n 'oldest open' tools/unattended/STOPS.template.md`, and `grep -n
  'item.entry.mailbox-answer\|six items\|--mail answer' help/loop.md`, each is found; `cmp` finds each
  installed guide byte-equal to its template; `grep -c 'five items' help/loop.md` prints 0; and
  `python tools/govkit/docs_leg.py --fingerprints` prints `verb:unattended.sh:--mail` with the
  fingerprint the `--mail` paragraph's anchor carries.
  Red when: the verb, the item or the wait's renewal is undocumented, or the anchor keeps the
  fingerprint from before `--cite`.

## 7. Gates

`unattended kit gate` · `scratch-guard self-test` · `tier2-review self-test` · `loop definition` · `loop item kind` · `loop termination` · `policy fixtures` · `docs` · `recall floor` · `recall floor arms` · `python resolver (behaviour + inline parity + idiom ban)` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · covers AC2 AC3 AC4 AC5 · the answer, the default and the wait arms over planted mail commits, feed lines and lease chains, AC4 staged by a scratch copy whose `read_lease_renewal` skips the question step and AC5 by one storing the question's commit as the witness · the effective `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8` rise by the arms' count, counted off the diff

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
  The ask to dPlacedRequest: a renew whose witness is an open question to the lease's build renews
  under `progress`, and not once it reads `expired`. widens: none · relaxes: none. Re-grounded
  2026-11-21: accepted and landed as TOOL-dPlacedRequest-67, which
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
  false producer; (c) a new record kind per answer, one fact written twice. Recommendation (a).
  RESOLVED (owner, 2026-11-05): (a) the prose-`returns` ask, the row keeping a prose `returns`.
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
  no version and no extra write. widens: none · relaxes: none. Re-grounded
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
- **F10 — What `witness` does a write that renews on an open question store?** The landed transition
  step reads the newest transition as `new` wherever it differs from the record's `witness`, and
  compares no ages (`tools/unattended/unattended.sh#read_lease_renewal`). Options: (a) the record's
  `witness`, kept, the renewal resting on the `question` verdict and the beat's line naming the
  question, as `activity` already renews on a kept witness; (b) the question's commit, as `--lease
  renew --witness` stores a caller's, so the next write reads the older transition as `new` and
  renews after the question closes with no move made; (c) the question's commit, the transition step
  compared to the last transition the lease chain holds, a chain walk per write. RESOLVED (agent,
  2026-11-23, delegated): (a), rung 3; (b) is a false renewal and (c) walks to recover what (a) never
  drops. widens: none · relaxes: none

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
- rev-7 · 2026-11-21 · S2 · S4 · S6 · §4 · AC2 · AC3 · AC6 · §7 · checked for behaviour under
  `2026-11-21-prompt-KICK-dKeptSession-24-precheck-brief`: the unattended suite runs no transition
  writer, so AC3 observes the guard's input, `--mail read --open --ids`, in place of a `record` run;
  S4 reads the mailbox with its stderr discarded, as `check_lease_witness` does; unit 24 deletes the
  `declare -F` probe §4 and Rollout cited; AC2's question carries unit 24's `--default`; `--cite`
  moves the `--mail` fingerprint, so S6 and AC6 re-stamp the anchor; `symbols.json` and the suite's
  floors joined Files touched; `policy fixtures`, whose guard holds `tools/loop/`, joined §7.
- rev-8 · 2026-11-23 · §1 · S1 · S2 · S3 · S4 · S6 · §3 · §4 · §5 · AC2 · AC4 · AC5 · AC6 · §7 · §8 F10 ·
  §10 · re-grounded on the run tree at `d06e2a65` under
  `2026-11-22-prompt-KICK-dKeptSession-25-reground-brief`, units 36, 39, 51, 27 and 24 read as
  landed: the transition step compares by difference, so a stored question commit would renew once
  after the question closed, and the renewal keeps the record's `witness` (F10, AC4, AC5); S2 names
  `write_mail_answer`, its order, texts and hex cite check; S3 its exit-2 lines; S6 the texts made
  false, "five items", the guard paragraph, `--beat` and the STOPS row among them, §4 the rest; no
  refusal site is added, the floors read 4100 and 1317, and no budget row is re-priced.

## 10. Reuse audit

The seams extended are the landed entry program of `tools/loop/loop.toml`, written as
`item.entry.claim` writes its wait, and `tools/unattended/unattended.sh#read_lease_renewal`, whose
new step calls the one witness check, `tools/unattended/unattended.sh#check_lease_witness`, and lets
`derive_lease_renews` renew on its verdict. The answer verb is
`tools/unattended/unattended.sh#write_mail_ack`'s shape with a body and cites.
`python tools/codebase-map/reuse_lookup.py "answer a question message and renew a lease while
waiting"`, re-run at this writing, ranked `resolveLease`, `check_lease_only_diff`, `read_cap_answer`,
`check_lease_witness`, `derive_answer` and `derive_lease_renews` by name stem; `resolveLease` finds a
JS hook's run lease and `derive_answer` is the position engine's, so no seam fits beyond the lease
writer's and the ack's. Scout B's disagreement 2 was §8 F4, closed by TOOL-dPlacedRequest-1.

Recall terms used: mailbox.answer question answer default stand-in next unattended lease renewal progress declared wait witness check_lease_witness read_lease_renewal write_mail_ack
