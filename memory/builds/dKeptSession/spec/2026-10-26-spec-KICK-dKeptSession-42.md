# KICK-dKeptSession-42 — a dependent's transition acknowledges the notices it has consumed, so a parent's notice never holds the dependent until the wait ceiling

**Status:** INPROGRESS · rev-5 · 2026-11-23 · node a · Tier-2 · base 64e146d9 · streams kickoff · order 25 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-42-deviation-421.md](../build/2026-10-26-build-KICK-dKeptSession-42-deviation-421.md) | deviation | — |
| [2026-11-21-build-KICK-dKeptSession-10-reground-orders-20-26-returns.md](../build/2026-11-21-build-KICK-dKeptSession-10-reground-orders-20-26-returns.md) | research | KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-1 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-35-orders-25-26-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-35-orders-25-26-reground-brief.md) | research | KICK-dKeptSession-35 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 |
| [2026-11-21-prompt-KICK-dKeptSession-42-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-42-build-brief.md) | research | — |
| [2026-11-21-prompt-KICK-dKeptSession-7-precheck-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-7-precheck-brief.md) | research | KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-8 KICK-dKeptSession-55 |
| [2026-11-22-prompt-KICK-dKeptSession-42-reground-brief.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-42-reground-brief.md) | research | — |
| [2026-11-23-prompt-KICK-dKeptSession-42-1-spec-writer.md](../prompts/2026-11-23-prompt-KICK-dKeptSession-42-1-spec-writer.md) | journal | — |
| [2026-10-26-review-KICK-dKeptSession-30-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-30-spec-audit.md) | spec-audit | KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-32 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-35 KICK-dKeptSession-43 KICK-dKeptSession-41 KICK-dKeptSession-44 |

<!-- /gen:spec-records -->

## 1. Goal

The round-1 spec audit of this build's spec set
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md`)
confirmed finding **id 55 at HIGH**, report item **H9**, which no other id shares.

`tools/loop/loop_transition.py#write_transition` refuses a move while any row of its one
`read_mail_rows` read reads `open`, and `tools/unattended/unattended.sh#read_mailbox` keeps a row
`open` until an `answer` or an `ack` names it (`KICK-dKeptSession-5` S7 and S9, landed).
`KICK-dKeptSession-7` S4 and S5 post `confirmed`, `changed` and `landed` to each dependent, and no
unit acknowledges them. So every parent notice holds each dependent's moves until a session runs
`--mail ack` or the row reads `expired` past `flow.wait-ceiling` (`KICK-dKeptSession-24` S5), 72
hours by default and 168 under strict (PINNED 2026-11-23, `tools/policy/catalogue.toml` and
`[preset.strict]` of `tools/policy/presets.toml`). An unattended dependent never acks. This unit
keeps the notice kinds gating, as the clause says, and makes the dependent's transition writer
acknowledge each notice it has consumed. It repairs `KICK-dKeptSession-7` and builds at order 25,
after units 7 and 35.

## 2. Scope (IN)

- **S1** — id 55. Read notices. `write_consumed_acks(root, build, rows)` in
  `tools/loop/loop_transition.py` returns the set of ids it acknowledged with exit 0 and never
  raises. `write_transition` calls it after its one `read_mail_rows(root, build)` read and the
  unarmed line, and before the open-row refusal that raises `MailHeld`, over that read's rows. It
  acknowledges every row whose `state` is `open` and whose `kind` is `landed`, `superseded` or
  `withdrawn`: the transition has read it, and nothing else consumes it. The refusal then holds the
  read's `open` rows less the returned ids, and the read is not repeated. An acknowledged row still
  reads `open` in that read, so this move does not dispose of it; the build's next move reads it
  `acked` and disposes of it, as unit 5 S10 does every acknowledged row
  (`tools/loop/loop_transition.py#MAIL_DISPOSED_STATES`). Observed by AC1.
- **S2** — id 55. Consumed interfaces. For each parent, the `from-build` of a row, holding an `open`
  `confirmed` or `changed` row whose `subject` is `interfaces <parent>`, the writer calls
  `KICK-dKeptSession-7` S3's `check_parent_interfaces(root, build, parent)` once, `(rc, line)`: the
  parent lease's `witness`, its listing in a scratch file and `KICK-dKeptSession-27` S5's
  `check_interface_notice`, the one chain the gate reads. When it answers `rc` 0 with
  `interface — current <id> · <kind> · key <k>` and `<id>` is an `open` row of the read, the writer
  acknowledges that row and every `open` `confirmed` or `changed` from the same parent with that
  subject whose `first-seen`, as `read_mailbox` orders it, is strictly earlier. A tie or a `-`
  stamp is not earlier, so it stays open: holding a move is recoverable, and acknowledging an
  unconsumed `changed` loses it. Any other answer acknowledges nothing from that parent. `rc` 1, an
  `interface — unconfirmed` or a witness of `-`, is silent, the guard naming the rows; any other
  `rc`, or a call that raises, writes `mail — interfaces <parent> unread · <line or why>` to stderr,
  as S3's failed ack is written. A `changed` whose key does not recompute stays open for the
  re-entry that consumes it. Observed by AC2 and AC3.
- **S3** — id 55. The post. Each acknowledgement is `--mail ack <build> <id>`
  (`tools/unattended/unattended.sh#write_mail_ack`), launched by
  `tools/loop/breakpoints.py#run_sourced` as §4 "The ack's launch" spells it, `main` inside
  `( … )`, under the landed `tools/loop/loop_witness.py#resolve_bash`. It runs once per id and
  only while the row reads `open`, so a retried transition posts nothing twice. A failed ack, a
  non-zero exit or a launch that raises `LookupError`, `OSError` or `subprocess.TimeoutExpired`,
  writes `mail — ack not posted <id> · rc <n|->` to stderr as it happens, since a move the guard
  then refuses returns no `said`; the guard refuses on the still-open row as unit 5 S9 states.
  Observed by AC4.
- **S4** — id 55. `KICK-dKeptSession-24` §8 F2's reliance on the deadline for "a `changed` nobody
  acknowledges" now covers only a `changed` the dependent has not consumed; that unit's text is
  superseded by name here, unchanged in behaviour. NOT OBSERVED: no criterion of this unit observes
  unit 24's deadline, which keeps its own AC.
- **S5** — The user page, `help/loop.md`. Under "Recording a build's move", the guard paragraph
  (`KICK-dKeptSession-5` S14) gains, before "A mailbox that is not read", one sentence that the
  move first acknowledges each notice it has consumed, §4's table "Who acknowledges what", and the
  `mail — ack not posted` line; the fixture-cases sentence names the four `acks-*` plants. In
  `## Coordinating with a parent build` (`KICK-dKeptSession-7` S8), the sentence that an
  unacknowledged notice is open mail holding the dependent's moves reads instead: "The dependent's
  next move acknowledges each notice it has consumed; a `changed` it has not consumed holds its
  moves until the re-entry or its deadline." Observed by AC5.
- **S6** — The budget row. The four `acks-*` plants move the `plants=<n>` token of the `loop
  transition record` row in `tools/run-gates/selftest-budgets.txt`, re-priced as §4's budget row
  states. They are branches of `run_transition_fixture`, as `KICK-dKeptSession-36` S4's are, so no
  plant adds a module-level symbol. Observed by AC6.
- **S7** — The shipped texts in the loop kit, §4 "The shipped texts": in
  `tools/loop/loop_transition.py` the module docstring's THE MAIL GUARD paragraph and its plant
  sentence, `write_transition`'s docstring and the comment above its guard; in
  `tools/loop/README.md` "The mail guard" paragraph and the fixture sentence naming every plant.
  Each names `write_consumed_acks`, the kinds it acknowledges and, where plants are listed, the four
  `acks-*` plants. Observed by AC7.

## 3. Non-goals (OUT)

- Acknowledging a `question`, an `intake` or an `overlap`: those wait for an answer or a person, as
  `KICK-dKeptSession-5` S7 says.
- An `expired` row: the guard passes it and unit 5 S10 disposes of it (`KICK-dKeptSession-24` S5).
- The re-entry on a `changed`: dIndexedDesign's `design.reentry`.
- Posting from the position engine. §8 F1 records why the writer posts and the engine only reads.
- A line among `said` naming each ack, and acks made conditional on the guard's verdict:
  `KICK-dKeptSession-55`.
- Any edit of `tools/unattended/unattended.sh`: the verb, its usage row and `write_mail_ack`'s
  comment stay as landed (§4 "The refusal ceiling").
- The report's left-shift checklist entry, that every gating kind names its acker. No clause of this
  build names that checklist; §4's table is the record here.

### Edges

- **consumes-from** `KICK-dKeptSession-7` — the `confirmed`, `changed` and `landed` notices, S3's `check_parent_interfaces` and §4's extended `run_sourced`, by which the writer decides what it has consumed and posts its acks (id 55)
- **consumes-from** `KICK-dKeptSession-5` — `write_transition`'s guard, `read_mail_rows` and the `--mail ack` verb, through which the writer acknowledges between the read and the refusal
- **consumes-from** `KICK-dKeptSession-27` — `check_interface_notice`, whose `current <id>` line names the row the dependent has consumed
- **consumes-from** `KICK-dKeptSession-36` — the landed `resolve_bash(<driver>)` the guard's read uses, under which `run_sourced` runs each `--mail ack`
- **hands-off** `KICK-dKeptSession-53` — `write_consumed_acks`' S2, whose "earlier by `first-seen`" that unit replaces with the key and chain rule (id 4)
- **hands-off** `KICK-dKeptSession-55` — `write_consumed_acks` and its S1 and S3, which that unit makes conditional on the guard's verdict and visible (id 49)
- **hands-off** `KICK-dKeptSession-56` — `write_consumed_acks`' launcher and failed acks, and the Gates legs, the batch's S3, S32, S27, S44 and S42 (ids 5, 50, 36, 53, 41)

## 4. Design

### Evidence

Read at `64e146d9` (2026-11-23), past units 22, 5, 31, 23, 36, 39 and 51's landings, with the specs
of units 27, 24, 10, 25, 21, 6, 7 and 35 read as landed before this unit.

- `tools/loop/loop_transition.py#write_transition` binds `mail, unarmed = read_mail_rows(root,
  build)`, appends the unarmed line, collects the ids whose `state` is `open` and raises `MailHeld`
  on any, before `derive_move`. `MAIL_COLUMNS` names eleven columns and `read_mail_rows` zips the
  first eleven, so unit 27's and unit 24's appended columns never reach a row dict; the writer reads
  `id`, `kind`, `state`, `first-seen`, `from-build` and `subject` only. Unit 10's `local=False`
  keyword leaves this call as it is.
- `tools/unattended/unattended.sh#write_mail_ack` refuses an id not addressed to the slug as
  `mail — not written · <id> is no message addressed to <slug>`, exit 2, and otherwise posts an
  `ack` from the slug answering the id to `build:<from-build>`, its exits the post's:
  `tools/unattended/unattended.sh#write_mail_post` answers 0 posted, 1 duplicate or lost, 2 not
  written, and needs `CLAUDE_CODE_SESSION_ID` and a fleet tag. `read_mailbox` reads the row `acked`
  once that `ack` is cached.
- A sourced driver's `main` called in the sourcing shell prints `unattended: REFUSING - main was
  called in the shell that sourced the driver …` and returns 2 (`tools/unattended/unattended.sh#main`),
  so `tools/loop/placement.py#read_build_lease` wraps it in `( … )`, as unit 7 rev-9 does.
- `tools/loop/breakpoints.py#run_sourced` is `run_sourced(repo, script, driver=None)` at this HEAD,
  raising `LookupError` where no bash resolves, with a fixed 900 s bound (DERIVED: its source);
  unit 7 §4 "The driver launch" adds `args=()` and `timeout=900`. It passes this process's
  `read_clean_env()`. `tools/loop/breakpoints.py@bc677275e24b:90` imports this module at its top.
- `check_parent_interfaces` answers `(rc, line)`, `rc` 0 on `check_interface_notice`'s exit 0, 1
  for `awaiting confirmed` and 2 for an unread confirmation (`KICK-dKeptSession-7` S3). The check
  prints `interface — current <id> · <kind> · key <k>`, exit 0, naming the lesser id where two rows
  share the key; `interface — unconfirmed · key <k>`, exit 1; `interface — not read` or
  `interface — off`, exit 2 (`KICK-dKeptSession-27` S5).
- Every landed case refusing on open mail plants a `question`, `FX_QUESTION` of
  `tools/loop/loop_transition.py#run_transition_fixture` and `mail-held` of
  `tools/loop/claim.py`, a kind this unit never acknowledges, so no landed case moves.

### Who acknowledges what

| Kind addressed to the dependent | Acknowledged by | When |
|---|---|---|
| `landed`, `superseded`, `withdrawn` | the dependent's `write_transition` | at its next transition |
| `confirmed`, `changed`, current | the dependent's `write_transition` | at its next transition, S2 |
| `confirmed`, `changed`, strictly earlier than the current one | the same | with the current one |
| `changed`, not current | nobody here | dIndexedDesign's re-entry, or the deadline |

### The ack's launch

The ack is this unit's one driver call, unit 7 §4's `run_sourced` form, never a launcher of its
own; the check's launch is inside `check_parent_interfaces`, as unit 7 §4 spells it. `run_sourced`
is imported inside `write_consumed_acks`, since `breakpoints.py` imports this module at its top.

```
run_sourced(root, '( load_driver_conf && main --mail ack "$2" "$3" )', args=(build, id), timeout=MAIL_GUARD_SECONDS)
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `write_consumed_acks` | function, `tools/loop/loop_transition.py` | `py.function`, `write`, OK |
| `acks-landed`, `acks-confirmed`, `acks-superseded`, `acks-failed` | `--plant` cases of `loop_transition.py --fixture`, `PLANTS` and `run_selftest` | none |
| `mail — ack not posted`, `mail — interfaces <parent> unread` | stderr lines of `write_consumed_acks` | none |

### The plants

Each extends `write_transition_plant`'s mail branch: the driver's conf with `RUN_CLAIMS` on and a
bare remote inside the git dir, each message put on it by `write_fixture_gov_ref` over
`render_fixture_mail`, from `fy` or `fz` to `build:tFix`, one ref per message
(`tools/loop/loop_transition.py#write_transition_plant`). The acks post as `USERNAME` from
`tools/loop/placement.py#read_fleet_user` with a `CLAUDE_CODE_SESSION_ID`, both set in this
process's environment for the plant and restored. A state is read by `read_mail_rows(top, "tFix")`
and printed `loop: fixture · state <id> · <state>`; stderr, captured, as `loop: fixture · stderr ·
<line>`.

| Plant | Stages |
|---|---|
| `acks-landed` | one `landed`; B4 |
| `acks-confirmed` | `fy`'s spec committed, its lease by `write_foreign_lease` with `fields` naming that commit as `witness`, a `confirmed` by `render_fixture_mail` with `content_key`, the key derived as unit 7's plants derive it (unit 7 §4 Inventory); B4 over the real chain |
| `acks-superseded` | `check_parent_interfaces` stood in and `run_sourced` wrapped, each recording its calls; `fy`'s `confirmed` sighted by one read, then `fy`'s `changed`, the stand-in naming it current; B4. Then `fz`'s pair, the stand-in answering `rc` 1; B5 |
| `acks-failed` | `run_sourced` wrapped, each ack recorded; one `landed`, B4, then B5. Then two `landed`, the wrapper answering `(1, "mail — lost …")` for one ack and raising `LookupError` for the other; B7 |

### Migration

None: no notice exists before `KICK-dKeptSession-7`.

### The shipped texts

Found by `git grep -n -i -E "mail ack|acknowledg|mail open|MailHeld"` over `tools`, `skills`,
`help` and `memory/guides` at `64e146d9`, with unit 7's and unit 35's specs for the texts they land.

| Text | Verdict |
|---|---|
| `help/loop.md`, the guard paragraph and the fixture-cases sentence | false by omission: S5 |
| `help/loop.md`, unit 7's `## Coordinating with a parent build` sentence on unacknowledged notices | false: S5 |
| `tools/loop/loop_transition.py`, the module docstring, `write_transition`'s docstring and guard comment | false: S7 |
| `tools/loop/README.md`, "The mail guard" and the fixture sentence | false: S7 |
| `help/loop.md`, the `--mail` paragraph and its `verb:unattended.sh:--mail` anchor | stays |
| `tools/unattended/VERBS.template.md`, `memory/guides/UNATTENDED-VERBS.md`, the `--mail` entry | stays |
| `help/orientation-card.md`, the `mail —` line; `tools/loop/claim.py`, its docstring | stays |
| `tools/loop/loop_transition.py#MailHeld`, its docstring and message | stays |
| `tools/unattended/unattended.sh`, the usage row and `write_mail_ack`'s comment | stays |
| `tools/policy/catalogue.toml`, the `deps.` and `mailbox.` rows | stays |

The `--mail` paragraph and the guide pair say a build's moves are refused while a message reads
`open`, and an acknowledged row no longer reads open. The card line and `claim.py` say a message
holds a move until it is acknowledged, which the writer's ack is. `MailHeld` names only rows still
open. The verb is unchanged. No catalogue row carries a summary, so `.governance/policy.json` does
not move. No usage row moves, so no `<!-- usage: -->` fingerprint is re-stamped
(`tools/govkit/docs_leg.py#derive_usage_fingerprint`, over `tools/govkit/usage.toml`).

### The refusal ceiling

The driver's refusal sites read `347/347` (DERIVED: `python tools/memory-tree/check-arms.py
--report`'s `ceiling tools/unattended/unattended.sh` row at `64e146d9`). This unit does not edit
the driver, so it adds no `fail`, `exit 1` or `status=1` site and owes no ceiling decision.

### The budget row

`check_plant_tokens` holds the `plants=<n>` token of each loop-kit row equal to `len(PLANTS)` of the
module its argv runs, once imported, and refuses a note carrying two tokens
(`tools/run-gates/run-selftests.sh#check_plant_tokens`). The `loop transition record` row runs
`loop_transition.py check --selftest` and carries `plants=18` and a budget of 67 (DERIVED:
`len(PLANTS)` and the row, read at `64e146d9`). Units 24, 7 and 35 add one, one and two before this
unit, so S6 moves the token from 22 to 26 (DERIVED: 18 plus those plants plus four). The builder
re-reads the count at the unit's base and moves the one token in place, four above it.

| Figure | `loop transition record` |
|---|---|
| proxy `r`, the row's note (PINNED 2026-11-23, node d) | 44.3 s over 18 plants |
| units 24, 7 and 35, as spec-7 and spec-35 price them (PINNED 2026-11-23) | 6 s, 33 s and 18 s |
| this unit's four plants, estimates (PINNED 2026-11-23) | 7 s, 13 s, 11 s and 9 s |
| `r` after this unit (PINNED 2026-11-23, the sum) | 141.3 s |
| budget, max of the row's value at the base and 1.5 `r` (PINNED 2026-11-23) | 212 |
| the leg's ceiling in `tools/gate-legs.json` (PINNED 2026-11-23) | 120, under 141.3 s |

The estimates price 2 s a driver call and 1 s a scratch repository (PINNED 2026-11-23), from the
row's note: `mail-open`, one move and one read over a bare remote, reads 2.0 s (PINNED 2026-11-23).
The calls are three, six, five and four, by §4 "The plants". The builder reads each new plant
alone by direct CLI and appends `Then re-read by KICK-dKeptSession-42 as PINNED proxy r <s>` to the
row's note, the budget the row's value or 1.5 `r` rounded up, whichever is higher. The leg has no
row in `tools/run-gates/ceiling-evidence.txt`, so no evidenced maximum moves. By these estimates
`r` passes the leg's ceiling. A declared ceiling is the owner's to move
(`memory/guides/BUILD-METHOD.md`, M3), and neither `tools/gate-legs.json` nor the build README
grants a raise: where the builder's reading takes `r` to the ceiling the leg carries at the unit's
base, the unit stops before it lands, names the raise for the owner, and never edits
`tools/gate-legs.json`.

### Files touched (estimate)

- `tools/loop/loop_transition.py`: `write_consumed_acks` and its call, the four plants and their
  `run_selftest` cases, and S7's docstrings and comment
- `tools/loop/README.md`: S7
- `tools/run-gates/selftest-budgets.txt`: S6, the `loop transition record` row's `plants=` token
  four above its count at the unit's base and its note's re-read (DERIVED: `len(PLANTS)`)
- `memory/map/generated/symbols.json`: `write_consumed_acks`, by `python
  tools/codebase-map/gen_map.py --write`, as the commit hook demands
- `help/loop.md`: S5

### Alternatives rejected

- **The position engine posting the ack when its gate accepts.** The engine is called by the card,
  the boundary hook and every `next`, so a read would post mail at every one of them.
- **Notice kinds that never gate.** The clause's guard reads every message addressed to the build;
  exempting kinds would let a `withdrawn` parent pass unread.
- **A second `--mail read` after the acks.** Unit 5's F9 keeps one snapshot for the guard and the
  disposal; the acked ids are known from the posts' exits.
- **`tools/loop/position.py#run_driver` as the launcher.** It runs the executed driver under a fixed
  900 s bound (DERIVED: its source), and `tools/loop/position.py@7ecce560a0ee:143` imports this
  module, so a second launcher would sit beside unit 7's.
- **Every plant over the real chain.** `acks-superseded` stands in for `check_parent_interfaces`,
  whose verdict unit 7's AC4 observes, so the leg pays the lease and the check once, in
  `acks-confirmed`.

## 5. Production-readiness checklist

- security — acks pass through `KICK-dKeptSession-5` S8's verb, which refuses an id not addressed
  to the slug; the launch's script is fixed and its values are positional arguments, never shell
  text.
- perf / scale — one `check_parent_interfaces` per parent with an open notice, and one post per
  consumed id, at a transition, each under `MAIL_GUARD_SECONDS`.
- error / empty / loading states — a failed ack, or a check that does not answer within the bound,
  leaves the row open and the guard refuses, its line on stderr, so the failure is never silent. A
  writer with no session id or fleet tag posts nothing, exit 2, the same way.
- observability — each ack is a mail message in the parent's view of the dependent's replies.
- risks — a dependent that never transitions never acks; its parent is not held by that, since only
  rows addressed to a build gate that build. A move the table refuses after the guard has still
  acked what the transition read, which `KICK-dKeptSession-55` makes conditional and visible. Two
  notices of one parent sighted by one fetch tie, so the older stays open until the deadline,
  `KICK-dKeptSession-53`'s rule. By §4's estimates the leg passes its ceiling, the owner's raise.
- testing — the plants of §6 and the arm in §7.
- migration — none.
- user docs — `help/loop.md`, S5; the loop kit's README, S7.

## 6. Acceptance criteria

Each plant is a scratch repository of §4 "The plants", built by `loop_transition.py --fixture`.

- **AC1** — When `python tools/loop/loop_transition.py --fixture --plant acks-landed` runs, with one
  `landed` from `fy` to `build:tFix` on the remote and no manual ack, B4 records, exit 0, and the
  read after it prints that row's state `acked`.
  Red when: the move is refused `mail open <id>`, as unit 5's guard alone refuses it.
- **AC2** — When `--plant acks-confirmed` runs, its `confirmed` key recomputing over the listing at
  the lease's `witness`, B4 records with no manual ack and the read after it prints the row `acked`.
  Red when: the consumed notice holds the move until the wait ceiling.
- **AC3** — When `--plant acks-superseded` runs, B4 records and the wrapper's recorded acks are
  `fy`'s `confirmed` and `changed`, each exit 0; B5 is refused `refused — tFix · mail open` naming `fz`'s
  `changed` id, and the stand-in was called once for `fy` and once for `fz`.
  Red when: a superseded `confirmed` stays open, an unconsumed `changed` is acked, or the check
  runs for a parent with no open row.
- **AC4** — When `--plant acks-failed` runs, the wrapper records one ack of the first `landed` across
  B4 and B5; B7 exits 1 refused `mail open` naming both later ids, and the captured stderr holds
  `mail — ack not posted <id> · rc 1` and `mail — ack not posted <id> · rc -`.
  Red when: an ack is posted twice, or a failed or raising ack passes the guard.
- **AC5** — When `grep -n "Acknowledged by\|next move acknowledges\|acks-landed" help/loop.md`
  runs, it prints the table's header row under "Recording a build's move", the sentence inside
  `## Coordinating with a parent build`, and the fixture-cases sentence.
  Red when: the owner's page does not say who acknowledges a notice, or still says every notice
  holds the dependent until a manual ack.
- **AC6** — When, at the unit's commit,
  `python -I -c "import sys; sys.path.insert(0, 'tools/loop'); import loop_transition as m; print(len(m.PLANTS))"`
  runs, it prints the number that
  `grep -oP '^loop transition record\t.*\Kplants=\d+' tools/run-gates/selftest-budgets.txt`
  prints after `plants=`, and the four `acks-*` plants are among the keys of `PLANTS`.
  Red when: the row still carries the count from before this unit's plants.
  figure: PINNED 2026-11-23 at `64e146d9`, the probe prints `18` and the grep `plants=18`, before
  units 24, 7 and 35 take both to 22 (DERIVED: their plants).
- **AC7** — When `grep -n "write_consumed_acks\|acks-landed" tools/loop/README.md tools/loop/loop_transition.py`
  runs, it prints the README's mail-guard paragraph and fixture sentence, and the module
  docstring's mail-guard paragraph and `write_transition`'s docstring.
  Red when: a shipped text still says every open row refuses the move.

## 7. Gates

`loop transition record` · `policy fixtures` · `every held leg is budgeted, every budget row resolves` · `recall floor` · `recall floor arms` · `docs` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/loop_transition.py · covers AC1 AC2 AC3 AC4 · the `acks-landed`, `acks-confirmed`, `acks-superseded` and `acks-failed` plants, staged red with the `write_consumed_acks` call left out of `write_transition` · the `loop transition record` row's `plants=<n>` token rises by four

The arm does not check the chain under a refused lease or check, unit 7's AC4; a tie by
`first-seen`, unit 53's; or an ack posted by a node whose fleet registry holds no row.

## 8. Open questions

- **F1 — Which step posts the acknowledgement of a consumed interface notice?** Options: (a) the
  dependent's transition writer, ahead of the guard; (b) the position engine, when its gate accepts
  a row; (c) a new verb a session runs. (b) makes a read path write, at every card render and
  boundary; (c) is the manual step the defect is. RESOLVED (agent, 2026-10-26, delegated): (a),
  rung 3, the same acceptance as the corrected fix, posted from a writer. widens: none · relaxes:
  none
- **F2 — How does the Python writer reach `check_interface_notice`, a driver shell function no verb
  prints?** Options: (a) the sourced driver under the same `resolve_bash(<driver>)`, now inside unit
  7's `check_parent_interfaces`; (b) a new `--mail` verb asked of `KICK-dKeptSession-27`; (c) the key
  recomputed in Python, a second implementation of `derive_gov_id`'s hash. RESOLVED (agent,
  2026-11-21, delegated): (a), rung 3; one implementation of the check and no new surface, re-read
  at rev-5 as unit 7's chain. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, promoted from the round-1 spec audit's H9 (id 55).
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-53`, `KICK-dKeptSession-55`,
  `KICK-dKeptSession-56` mirrored from the round-1 promotions' audit's disposal.
- rev-3 · 2026-11-21 · S1 · S2 · S3 · S5 · §3 · §4 · §5 · AC1 to AC5 · §7 · §8 F2 · §10 ·
  re-grounded on base c2a407b0 by `2026-11-21-prompt-KICK-dKeptSession-35-orders-25-26-reground-brief`:
  S1 over unit 5's one read; the row's columns; S3 under the landed `resolve_bash`; F2 ruled; the
  arm moved to `loop_transition.py`'s plants; the page joined the files touched.
- rev-4 · 2026-11-22 · S2 · S3 · S6 · §3 Edges · §4 · AC6 · §7 · §10 · by
  `2026-11-22-prompt-KICK-dKeptSession-7-1-spec-writer`: S2 calls unit 7's
  `check_parent_interfaces` and S3 posts through `run_sourced`; failed lines on stderr; S6 and AC6
  move the `plants=<n>` token, priced with the stop at the leg's ceiling.
- rev-5 · 2026-11-23 · §1 · S1 to S7 · §3 · §4 · §5 · AC1 to AC7 · §7 · §8 F2 · §10 · re-grounded
  at `64e146d9` under `2026-11-22-prompt-KICK-dKeptSession-42-reground-brief`, handed off by
  `2026-11-23-prompt-KICK-dKeptSession-42-1-spec-writer`: the ack's launch wraps `main` in
  `( … )`, as its sourced-call guard asks, and imports `run_sourced` inside the function; S1 leaves
  the disposal to the next move; S2 filters by subject and counts a `first-seen` tie as not
  earlier; S5 and S7 name the texts made false (AC5, AC7); §4 plans the plants, one stood in for
  the chain, and re-prices from 22 to 26 plants; the refusal ceiling stated untouched. Narrowed:
  `acks-superseded` no longer runs the real chain.

## 10. Reuse audit

The seams extended are `KICK-dKeptSession-5`'s `read_mail_rows` read, `--mail ack` verb and
`write_transition` guard, landed, `KICK-dKeptSession-27`'s `check_interface_notice`, and
`KICK-dKeptSession-7`'s `check_parent_interfaces` and its extension of the landed
`tools/loop/breakpoints.py#run_sourced`, under `tools/loop/loop_witness.py#resolve_bash`; nothing is
re-derived and no second launcher is minted. Re-run at `64e146d9`: `python
tools/codebase-map/reuse_lookup.py "acknowledge a mailbox message once its consumer reads it"`
ranked `read_text`, `read`, `read_bytes` and `read_rows` by the name stem `read` only, none a mail
writer; `"post an ack through the sourced driver"` ranked `drive`, `run_driver` and
`load_driver_conf`, the second rejected in §4. The recall query below returned this spec, unit 35's
and the round-1 audit's H9 fix, none disagreeing with source.

Recall terms used: `python tools/memory-recall/query.py "who acknowledges a parent's notice to a
dependent build" --terms "mail ack acked open notice confirmed changed landed transition guard
wait-ceiling check_interface_notice dependent"`
