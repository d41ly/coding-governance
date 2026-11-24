# KICK-dKeptSession-55 — the transition writer acknowledges notices only when the guard would then pass, and prints each one it consumed

**Status:** CLOSED · rev-6 · 2026-11-23 · node a · Tier-2 · base 689698a5 · streams kickoff · order 26 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-55-deviation-551.md](../build/2026-10-26-build-KICK-dKeptSession-55-deviation-551.md) | deviation | — |
| [2026-11-21-build-KICK-dKeptSession-10-reground-orders-20-26-returns.md](../build/2026-11-21-build-KICK-dKeptSession-10-reground-orders-20-26-returns.md) | research | KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-1 |
| [2026-11-21-build-KICK-dKeptSession-55-1-acceptance-ledger.md](../build/2026-11-21-build-KICK-dKeptSession-55-1-acceptance-ledger.md) | journal | — |
| [2026-11-24-build-KICK-dKeptSession-1-runlog-31fbb903.md](../build/2026-11-24-build-KICK-dKeptSession-1-runlog-31fbb903.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 KICK-dKeptSession-67 KICK-dKeptSession-69 KICK-dKeptSession-79 KICK-dKeptSession-80 KICK-dKeptSession-89 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-35-orders-25-26-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-35-orders-25-26-reground-brief.md) | research | KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-52 KICK-dKeptSession-53 |
| [2026-11-21-prompt-KICK-dKeptSession-50-divergence-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-50-divergence-brief.md) | research | KICK-dKeptSession-50 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-51 KICK-dKeptSession-53 KICK-dKeptSession-61 |
| [2026-11-21-prompt-KICK-dKeptSession-55-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-55-build-brief.md) | research | — |
| [2026-11-21-prompt-KICK-dKeptSession-7-precheck-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-7-precheck-brief.md) | research | KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 |
| [2026-11-22-prompt-KICK-dKeptSession-55-reground-brief.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-55-reground-brief.md) | research | — |
| [2026-11-23-prompt-KICK-dKeptSession-55-1-spec-writer.md](../prompts/2026-11-23-prompt-KICK-dKeptSession-55-1-spec-writer.md) | journal | — |
| [2026-10-26-review-KICK-dKeptSession-45-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-45-spec-audit.md) | spec-audit | KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-56 |
| [2026-11-23-review-KICK-dKeptSession-69-closing-diff-review-round1.md](../reviews/2026-11-23-review-KICK-dKeptSession-69-closing-diff-review-round1.md) | diff-review | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 KICK-dKeptSession-67 KICK-dKeptSession-69 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build's fifteen round-1 promotions
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md`)
confirmed finding **id 49 at HIGH**, report item **H9**, which no other id shares. The skeptic judged
the finder's fix UNSOUND, and this unit takes the skeptic's corrected fix.

`KICK-dKeptSession-42` S1 has `write_transition` call `write_consumed_acks` between unit 5's one
`read_mail_rows` read and the open-row refusal that raises `MailHeld`, acknowledging every open
`landed`, `superseded` and `withdrawn` row, and no line names an ack it posted. Nothing makes the ack
wait for the guard's verdict on the other rows. So a `withdrawn` parent notice is consumed and never
shown; under `mailbox.reads = transitions-only` (`KICK-dKeptSession-10` S3) the transition is the
only read, so it is never surfaced at all. And if an open `question` then refuses the transition,
the ack has already landed, so the next transition passes and the dependent builds on a withdrawn
parent: the outcome unit 42 §4 rejects ("would let a `withdrawn` parent pass unread"). This unit
makes the consuming write conditional on the guard's verdict and visible. It repairs
`KICK-dKeptSession-42` and builds after it, the last of order 26.

## 2. Scope (IN)

- **S1** — id 49. List first. `write_consumed_acks(root, build, rows)` (unit 42 S1) first takes the
  rows of unit 5's one `read_mail_rows(root, build)` read whose `state`, column 4, is `open`
  (`KICK-dKeptSession-5` S9 and F9), and computes, posting nothing, the ids it would consume: unit 42
  S1's kinds, and the interface rows unit 42 S2 acknowledges as `KICK-dKeptSession-53` S3 rewrites
  it. It makes no read of its own. Its signature and its return, the set of ids acknowledged with
  exit 0, are unit 42's, so `write_transition`'s call does not move. Observed by AC1 and AC2.
- **S2** — id 49. All or nothing. It posts only when every `open` row of the read is one it would
  consume, so the guard, which holds the read's `open` rows less the returned ids (unit 42 S1), then
  holds none but a row whose ack failed. Otherwise it posts none and returns the empty set, and the
  guard refuses as `KICK-dKeptSession-5` S9 states, `MailHeld` naming every open row, the consumable
  ones included. Observed by AC2.
- **S3** — id 49. Each ack shown. For every ack that posts with exit 0, the writer writes
  `mail — acked <kind> <id> from build:<parent>` to stderr as it happens, `<parent>` the row's
  `from-build`, column 6. Stderr is the channel unit 42 S3 gives `mail — ack not posted`, for the
  reason §4's evidence states: a move refused after the acks returns no `said`. So a consumed
  `withdrawn` notice is printed whether the move then records or is refused. Observed by AC1.
- **S4** — id 49. The sibling text superseded by name. `KICK-dKeptSession-42` S1's "It acknowledges
  every row whose `state` is `open` and whose `kind` is `landed`, `superseded` or `withdrawn`" reads
  as S1 to S3 here, and unit 42 S3's per-id posts run only under S2's condition. Answered in this
  unit's own acceptance ledger,
  `memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-55-1-acceptance-ledger.md`,
  which quotes unit 42 S1's sentence and S3's "It runs once per id and only while the row reads
  `open`", and states S1 to S3 here supersede them. Unit 42 builds at order 25 and is CLOSED when
  this unit builds, so neither its spec nor its ledger is written (F1). Observed by AC4.
- **S5** — The budget row. `acks-withdrawn` and `acks-withdrawn-question` move the `plants=<n>`
  token of the `loop transition record` row in `tools/run-gates/selftest-budgets.txt`, re-priced as
  §4's budget row states. Both are branches of `run_transition_fixture`, as `KICK-dKeptSession-42`
  S6's are, so no plant adds a module-level symbol and `memory/map/generated/symbols.json` does not
  move. Observed by AC5.
- **S6** — The user page, `help/loop.md`, under "Recording a build's move". The guard paragraph
  gains, after unit 42 S5's sentence that the move first acknowledges each notice it has consumed,
  one sentence: "The acknowledgements are all or nothing: the move acknowledges the notices it has
  consumed only when no other message is open, and prints `mail — acked <kind> <id> from
  build:<parent>` for each; otherwise it acknowledges none, and the refusal names every open
  message." Each `When` cell of unit 42's table "Who acknowledges what" that reads "at its next
  transition" reads "at its next transition with no other message open". The fixture-cases sentence
  names both plants. In `## Coordinating with a parent build`, unit 42 S5's sentence reads "The
  dependent's next move with no other message open acknowledges each notice it has consumed; a
  `changed` it has not consumed holds its moves until the re-entry or its deadline." Observed by AC3.
- **S7** — The kit's texts, §4 "The shipped texts". In `tools/loop/loop_transition.py`, the module
  docstring's THE MAIL GUARD paragraph, its plant sentence, `write_transition`'s docstring, the
  comment above its guard and `write_consumed_acks`' docstring; in `tools/loop/README.md`, "The mail
  guard" paragraph and the fixture sentence naming every plant. Each text that states what the
  writer acknowledges says the acks are all or nothing and name the `mail — acked` line; each that
  lists plants names both. Observed by AC6.

## 3. Non-goals (OUT)

- Which interface rows are consumed: unit 42 S2, with id 4's key and chain rule,
  `KICK-dKeptSession-53` S3.
- An ack that fails to post: unit 42 S3, and the batch's item for id 50, `KICK-dKeptSession-56`.
- An `expired` row: the guard passes it and unit 5 S10 disposes of it (`KICK-dKeptSession-24` S5),
  so it is neither consumed nor printed here.
- A `mail — acked` line among `said`: §4's evidence shows it is lost on every refusal after the acks.
- Any edit of `tools/unattended/unattended.sh`: the `--mail ack` verb is unit 5's, unchanged (§4
  "The refusal ceiling").
- The report's left-shift checklist entry, that a consuming write ahead of a guard is conditional on
  its verdict and prints what it consumed. No clause of this build names that checklist; AC2 is its
  arm here.

### Edges

- **consumes-from** `KICK-dKeptSession-42` — `write_consumed_acks` and its S1 and S3, which this unit makes conditional on the guard's verdict and visible (id 49)
- **hands-off** `KICK-dKeptSession-56` — the listed open rows and the all-or-nothing post, inside which the batch's item for id 50 prices an ack refused for no session id or no remote
- **hands-off** `KICK-dKeptSession-62` — the listed rows, the guard's read and the ack loop, which the batch's S14 and S15 make one read and one ref update, and whose leg S1 records (ids 15, 32, 2)

## 4. Design

### Evidence

Read at `689698a5` (2026-11-23), past units 22, 5, 31, 23, 36, 39, 51, 27 and 24's landings, with the
specs of units 10, 25, 21, 6, 7, 35, 42, 8, 11, 43, 52 and 53 read as landed before this unit.

- `tools/loop/loop_transition.py#write_transition` binds `mail, unarmed = read_mail_rows(root,
  build)`, appends the unarmed line to `said`, collects the ids whose `state` is `open` and raises
  `MailHeld` on any, before `derive_move`. `read_mail_rows` zips each row with `MAIL_COLUMNS`, eleven
  names (DERIVED: the tuple), and unit 53 S2 adds `MAIL_ORDER_COLUMNS` after them. This unit reads
  `id`, `kind`, `state` and `from-build` alone. Unit 10's `local=False` keyword leaves the call as it is.
- spec-42 rev-5 S1: `write_consumed_acks(root, build, rows)` returns the ids it acknowledged with exit
  0 and never raises; the refusal holds the read's `open` rows less those ids, and an acknowledged row
  still reads `open` in that read, so the next move disposes of it. S2 calls
  `check_parent_interfaces` once per parent with an open interface notice, any answer but a current
  row acknowledging nothing from that parent. S3 posts each id once, through
  `tools/loop/breakpoints.py#run_sourced`, and writes a failed ack's line to stderr "as it happens,
  since a move the guard then refuses returns no `said`".
- `tools/loop/loop_transition.py#main` prints `said` only after `write_transition` returns, and its
  `TransitionRefused` handler prints `refused — <e>` alone; `tools/loop/claim.py#write_first_transition`
  joins the lines only from a move that records. So a line put in `said` is lost on every refusal
  after the acks: a failed ack's still-open row, the table's `derive_move`, the witness, a value or a
  staged index. Rev-5's S3 put the line there, and its §5 claim that a refused move had printed it
  did not hold.
- spec-5 S9: open rows raise `MailHeld`, a `TransitionRefused`, which `record` prints as
  `refused — <slug> · mail open <id> …` and exits 1, writing nothing; F9: one read serves the guard
  and the disposal. spec-10 S3: under `transitions-only` the item boundary runs no mail read.
- `tools/loop/loop_transition.py#run_selftest` captures stdout alone. Unit 42's plants print each
  captured stderr line as `loop: fixture · stderr · <line>` and each state of a read after a move as
  `loop: fixture · state <id> · <state>`; this unit's plants print both the same way.
- The landed cases S2 moves. Every case of units 5, 24, 36 and `tools/loop/claim.py` that refuses on
  open mail plants a `question` alone, so S2 posts nothing there as before. Unit 42's four `acks-*`
  plants hold only consumable rows at each move that acks, so they post as before. Unit 53's
  `acks-later-key` holds `c`, which the chain places after the current row: under S2 its move posts
  no ack. Its AC3 still holds, `c` named in the refusal and not on its `loop: fixture · acks` line.
  Where its `run_selftest` case owes that line naming `a` and `b`, the case owes `none` here.

### The step

```
open   := { r in read_mail_rows(root, build) : r.state == open }
eat    := { r in open : r.kind in (landed, superseded, withdrawn) } + S3-of-unit-53(open)
if open == eat:  for r in eat: --mail ack <slug> r.id ; on exit 0: stderr "mail — acked <kind> <id> from build:<parent>"
else:            post nothing, return {}  -> the guard refuses, naming every row of open
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `acks-withdrawn`, `acks-withdrawn-question` | `--plant` cases of `loop_transition.py --fixture`, `PLANTS` and `run_selftest` | none |
| `mail — acked` | stderr line of `write_consumed_acks` | none |

### The plants

Each extends unit 42's `acks-*` branch of `write_transition_plant`: the driver's conf with
`RUN_CLAIMS` on, a bare remote inside the git dir, each message put on it by `write_fixture_gov_ref`
over `render_fixture_mail`, one ref per message, and the fleet user and session id set as unit 42's
plants set them (`tools/loop/loop_transition.py#write_transition_plant`). The acks post for real.

| Plant | Stages |
|---|---|
| `acks-withdrawn` | `fy`'s `withdrawn` to `build:tFix`, nothing else; B4; its captured stderr printed |
| `acks-withdrawn-question` | `fy`'s `withdrawn` and `fz`'s `question` to `build:tFix`; B4; its captured stderr printed; then one `read_mail_rows(top, "tFix")`, each row's state printed |

### Migration

None: no notice exists before `KICK-dKeptSession-7`.

### The shipped texts

Found by `git grep -n -i -E "mail ack|acknowledg|mail open|MailHeld|consumed"` over `tools/loop`,
`help`, `memory/guides`, `tools/unattended/VERBS.template.md` and `tools/policy/catalogue.toml` at
`689698a5`, with unit 42's, 53's, 7's and 10's specs for the texts they land.

| Text | Verdict |
|---|---|
| `help/loop.md`, the guard paragraph, with unit 42 S5's sentence | false by omission: S6 |
| `help/loop.md`, unit 42's table "Who acknowledges what", its `When` cells | false: S6 |
| `help/loop.md`, unit 42 S5's sentence in `## Coordinating with a parent build` | false: S6 |
| `help/loop.md`, the fixture-cases sentence naming every plant | false by omission: S6 |
| `tools/loop/loop_transition.py`, the module docstring, `write_transition`'s docstring and guard comment, `write_consumed_acks`' docstring | false: S7 |
| `tools/loop/README.md`, "The mail guard" and the fixture sentence | false: S7 |
| `help/loop.md`, the `--mail` paragraph and its `verb:unattended.sh:--mail` anchor | stays |
| `help/loop.md`, `## When a parent build is withdrawn` | stays |
| `tools/unattended/VERBS.template.md`, `memory/guides/UNATTENDED-VERBS.md`, the `--mail` entry | stays |
| `help/orientation-card.md`, the `mail —` line; `tools/loop/claim.py`, its docstring | stays |
| `tools/loop/loop_transition.py#MailHeld`, its docstring and message | stays |
| `tools/policy/catalogue.toml`, the `mailbox.` and `deps.` rows | stays |

The `--mail` paragraph and the guide pair say a build's moves are refused while a message addressed
to it is `open`, which S2 keeps. The withdrawn-parent section reads a parent's run-state and its
route, never the mailbox. The card line and `claim.py` say a message holds a move until it is
acknowledged, which the all-or-nothing ack still is. `MailHeld` names every row still open, which
under S2 is every open row of the read. No `mailbox.` or `deps.` catalogue row carries a `summary`,
so `.governance/policy.json` does not move. The fixture sentence's `script:tools/loop/loop_transition.py`
anchor fingerprints the `--fixture` and `--plant=` flags of `tools/govkit/usage.toml` alone
(`tools/govkit/docs_leg.py#derive_usage_fingerprint`), so naming two plants re-stamps no anchor.

### The refusal ceiling

The driver's refusal sites read `347/347` (DERIVED: `python tools/memory-tree/check-arms.py
--report`'s `ceiling tools/unattended/unattended.sh` row at `689698a5`). This unit does not edit
the driver, so it adds no `fail`, `exit 1` or `status=1` site and owes no ceiling decision. It adds
no arm to `tools/unattended/unattended.test.sh`, so that suite's floors do not move.

### The budget row

`check_plant_tokens` holds the `plants=<n>` token of each loop-kit row equal to `len(PLANTS)` of the
module its argv runs, once imported, and refuses a note carrying two tokens
(`tools/run-gates/run-selftests.sh#check_plant_tokens`). The `loop transition record` row runs
`loop_transition.py check --selftest` and carries `plants=19` and a budget of 71 (DERIVED:
`len(PLANTS)` and the row, read at `689698a5`). Units 7, 35, 42, 11, 52 and 53 add one, two, four,
five, one and two before this unit, so S5 moves the token from 34 to 36 (DERIVED: 19 plus those
plants). The builder re-reads the count at the unit's base and moves the one token in place, two
above it.

| Figure | `loop transition record` |
|---|---|
| proxy `r`, the row's note (PINNED 2026-11-23, node d) | 47.1 s over 19 plants |
| units 7, 35, 42, 11, 52 and 53, as their specs price them (PINNED 2026-11-23) | 33 s, 18 s, 40 s, 15 s, 28 s and 18 s |
| `r` before this unit (PINNED 2026-11-23, the sum) | 199.1 s |
| this unit's two plants, estimates (PINNED 2026-11-23) | 5 s and 5 s |
| `r` after this unit (PINNED 2026-11-23, the sum) | 209.1 s |
| budget, max of the row's value at the base and 1.5 `r` (PINNED 2026-11-23) | 314 |
| the leg's ceiling in `tools/gate-legs.json` (PINNED 2026-11-23) | 120, passed at step 25 |

This unit adds 10 s to the leg (PINNED 2026-11-23, the estimates' sum). The estimates price 2 s a
driver call and 1 s a scratch repository (PINNED 2026-11-23), unit 42's basis, from the row's note,
where `mail-open`, one move and one read over a bare remote, reads 2.0 s (PINNED 2026-11-23).
`acks-withdrawn` makes two calls, the guard's read and the ack; `acks-withdrawn-question` makes two,
the guard's read and the read after (DERIVED: §4 "The plants"). The builder reads each new plant
alone by direct CLI and appends `Then re-read by KICK-dKeptSession-55 as PINNED proxy r <s>` to the
row's note, the budget the row's value or 1.5 `r` rounded up, whichever is higher. The leg has no
row in `tools/run-gates/ceiling-evidence.txt`, so no evidenced maximum moves. The ceiling is parked
for the owner, since unit 42's pricing passes it, and is the owner's to move
(`memory/guides/BUILD-METHOD.md`, M3): where the builder's reading takes `r` past the ceiling the
leg carries at the unit's base, the unit stops before it lands, names the raise, and never edits
`tools/gate-legs.json`.

### Files touched (estimate)

- `tools/loop/loop_transition.py`: S1 to S3 in `write_consumed_acks`, the two plants and their
  `run_selftest` cases, S7's docstrings and comment, and unit 53's `acks-later-key` case where §4's
  evidence moves it
- `tools/loop/README.md`: S7
- `help/loop.md`: S6
- `tools/run-gates/selftest-budgets.txt`: S5, the `loop transition record` row's `plants=` token
  two above its count at the unit's base and its note's re-read (DERIVED: `len(PLANTS)`)
- `memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-55-1-acceptance-ledger.md`:
  S4's answer beside the criteria observed

### Alternatives rejected

- **Acking first and un-acking on a refusal.** The mail refs are append-only (`KICK-dKeptSession-5`
  S1), so a retracted ack is a second message every reader must reconcile.
- **Acking the consumable rows whatever the guard says.** It is the defect: the consumed notice is
  gone when the refusal is cleared.
- **A second `--mail read --open` before the guard.** Unit 5's F9 rules one snapshot for the guard
  and the disposal; a reply landing between two reads splits the judgments.
- **The `mail — acked` line among `said`.** Every refusal after the acks drops it, §4's evidence.

## 5. Production-readiness checklist

- security — none beyond unit 42's.
- perf / scale — no read beyond the guard's one, which the writer filters in memory; S2 can only
  remove posts.
- error / empty / loading states — a read that fails refuses the transition through unit 5's
  guard before this step runs, so nothing is posted. A check that does not answer leaves its rows
  unconsumed, so S2 posts nothing.
- observability — S3's stderr line per posted ack.
- risks — a dependent with a standing open `question`, or an unconsumed `changed`, acks nothing until
  it is answered or consumed, so its parent's notices stay listed beside it; that is the guard's
  listing, by design. A move refused after the guard passed has still acked, and printed on stderr,
  what it consumed. By §4's estimates the leg passes its ceiling, the owner's raise.
- testing — the plants of §6 and the arm in §7.
- migration — none.
- user docs — `help/loop.md`, S6; the loop kit's README and docstrings, S7.

## 6. Acceptance criteria

Each plant is a scratch repository of §4 "The plants", built by `loop_transition.py --fixture`.

- **AC1** — When `python tools/loop/loop_transition.py --fixture --plant acks-withdrawn` runs, with
  `fy`'s `withdrawn` the one open row, B4 prints `loop: fixture · record · exit 0` and
  `loop: fixture · stderr · mail — acked withdrawn <id> from build:fy`.
  Red when: the `withdrawn` row is acked with no line, as a scratch copy of `write_consumed_acks`
  writing none shows, so the transition's reader never sees it.
- **AC2** — When `--plant acks-withdrawn-question` runs, B4 prints `loop: fixture · record · exit 1`
  and a `refused — tFix · mail open` line naming both ids, no `mail — acked` line, and the read after
  it prints `loop: fixture · state <id> · open` for the `withdrawn` row.
  Red when: the `withdrawn` row reads `acked` after the refusal, as a scratch copy of
  `write_consumed_acks` acking whatever the guard then reads leaves it, so the next transition
  passes it unread.
- **AC3** — When `grep -n "mail — acked\|with no other message open\|acks-withdrawn" help/loop.md`
  runs, it prints S6's sentence in the guard paragraph, the table's rows whose `When` cell it
  rewrites, the sentence in `## Coordinating with a parent build`, and the fixture-cases sentence.
  Red when: the owner's page does not say a consumed notice is printed, or that a refusal acks
  nothing.
- **AC4** — `tr -s ' \r\n' ' '` over this unit's acceptance ledger piped into `grep -c "It
  acknowledges every row whose"` prints `1`, and into `grep -c "It runs once per id and only while
  the row reads"` prints `1`; and `git diff --name-only <pass base> HEAD --
  memory/builds/dKeptSession/spec/2026-10-26-spec-KICK-dKeptSession-42.md
  'memory/builds/dKeptSession/build/*KICK-dKeptSession-42-*'` prints nothing.
  Red when: S4's answer lands in a record of unit 42, or this unit's ledger quotes neither passage.
- **AC5** — When, at the unit's commit,
  `python -I -c "import sys; sys.path.insert(0, 'tools/loop'); import loop_transition as m; print(len(m.PLANTS))"`
  runs, it prints the number that
  `grep -oP '^loop transition record\t.*\Kplants=\d+' tools/run-gates/selftest-budgets.txt`
  prints after `plants=`, and `acks-withdrawn` and `acks-withdrawn-question` are among the keys of
  `PLANTS`.
  Red when: the row still carries the count from before this unit's plants.
  figure: PINNED 2026-11-23 at `689698a5`, the probe prints `19` and the grep `plants=19`, before
  units 7, 35, 42, 11, 52 and 53 take both to 34 (DERIVED: their plants).
- **AC6** — When `grep -n "all or nothing\|acks-withdrawn" tools/loop/README.md tools/loop/loop_transition.py`
  runs, it prints the README's mail-guard paragraph and fixture sentence, the module docstring's
  mail-guard paragraph and plant sentence, `write_transition`'s docstring, the comment above its
  guard, `write_consumed_acks`' docstring and the two `PLANTS` keys.
  Red when: a shipped text still says the writer acknowledges every consumed notice whatever else is
  open.

## 7. Gates

`loop transition record` · `every held leg is budgeted, every budget row resolves` · `policy fixtures` · `docs` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/loop_transition.py · covers AC1 AC2 · a lone `withdrawn`, and a `withdrawn` beside an open `question`, staged red by scratch copies of `write_consumed_acks` that write no line and that ack whatever the guard then reads · the `loop transition record` row's `plants=<n>` token rises by two

The arm does not check an ack that fails beside others that post, unit 42's AC4; an interface row
beside a non-consumable one, which unit 53's `acks-later-key` case holds; or the line's reader.

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
- rev-6 · 2026-11-23 · §1 · S1 to S7 · §3 · §4 · §5 · AC1 to AC6 · §7 · §10 · re-grounded at
  `689698a5` under `2026-11-22-prompt-KICK-dKeptSession-55-reground-brief`, handed off by
  `2026-11-23-prompt-KICK-dKeptSession-55-1-spec-writer`: S1 over unit 42 rev-5's signature and unit
  53's rule; S3's line moves from `said` to stderr, since `main` drops `said` on every refusal after
  the acks; S4 quotes unit 42 rev-5's S1; S6 and S7 name the texts made false (AC3, AC6); §4 plans
  the plants, names the landed case S2 moves, and re-prices from 34 to 36 plants (DERIVED),
  adding 10 s (PINNED 2026-11-23, an estimate); the refusal ceiling stated untouched. Narrowed: no
  line among `said`.

## 10. Reuse audit

The seams extended are unit 42's `write_consumed_acks`, its signature and its return kept,
`KICK-dKeptSession-5`'s one `read_mail_rows` read and its `--mail ack` verb, and the stderr channel
unit 42 S3 gives a failed ack; the open-row list is the guard's own read, filtered in memory, and no
function or launcher is minted. Re-run at `689698a5`: `python tools/codebase-map/reuse_lookup.py
"acknowledge consumed notices only when the guard would then pass"` ranked `check_gen_region_only`,
`pass_commit`, `check_guard_trips` and `check_lease_only_diff` by the name stems `only`, `pas` and
`guard` alone, none a mail writer; `write_consumed_acks` is not in the tree until unit 42 lands, so
the sibling specs are the seams. The recall query below returned this spec and unit 42's, neither
disagreeing with source.

Recall terms used: `python tools/memory-recall/query.py "when may a transition acknowledge a
withdrawn notice" --terms "withdrawn landed superseded ack open question guard refused transitions-only
write_consumed_acks consumed visible stderr"`
