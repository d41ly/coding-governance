# KICK-dKeptSession-61 — the session chain read over every row on the parent's refs, so a parent with two dependents is placed

**Status:** INPROGRESS · rev-10 · 2026-11-23 · node a · Tier-2 · base c18b223b · streams kickoff · order 27 · advances KICK-dKeptSession-29

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-61-deviation-611.md](../build/2026-10-26-build-KICK-dKeptSession-61-deviation-611.md) | deviation | — |
| [2026-10-26-build-KICK-dKeptSession-61-deviation-612.md](../build/2026-10-26-build-KICK-dKeptSession-61-deviation-612.md) | deviation | — |
| [2026-11-21-build-KICK-dKeptSession-17-reground-orders-27-29-returns.md](../build/2026-11-21-build-KICK-dKeptSession-17-reground-orders-27-29-returns.md) | research | KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-41 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-12-plant-budget-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-12-plant-budget-brief.md) | research | KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-26 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-11 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-17 KICK-dKeptSession-18 |
| [2026-11-21-prompt-KICK-dKeptSession-17-orders-27-29-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-17-orders-27-29-reground-brief.md) | research | KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-41 |
| [2026-11-21-prompt-KICK-dKeptSession-50-divergence-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-50-divergence-brief.md) | research | KICK-dKeptSession-50 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-51 KICK-dKeptSession-53 KICK-dKeptSession-55 |
| [2026-11-21-prompt-KICK-dKeptSession-61-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-61-build-brief.md) | research | — |
| [2026-11-21-prompt-KICK-dKeptSession-61-precheck-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-61-precheck-brief.md) | research | KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 |
| [2026-11-22-prompt-KICK-dKeptSession-61-1-spec-writer.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-61-1-spec-writer.md) | journal | — |
| [2026-11-22-prompt-KICK-dKeptSession-61-reground-brief.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-61-reground-brief.md) | research | — |
| [2026-11-23-prompt-KICK-dKeptSession-61-1-spec-writer.md](../prompts/2026-11-23-prompt-KICK-dKeptSession-61-1-spec-writer.md) | journal | — |
| [2026-11-23-prompt-KICK-dKeptSession-61-2-spec-writer.md](../prompts/2026-11-23-prompt-KICK-dKeptSession-61-2-spec-writer.md) | journal | — |
| [2026-11-23-prompt-KICK-dKeptSession-61-reground-2-brief.md](../prompts/2026-11-23-prompt-KICK-dKeptSession-61-reground-2-brief.md) | research | — |
| [2026-10-26-review-KICK-dKeptSession-57-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-57-spec-audit.md) | spec-audit | KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-57 KICK-dKeptSession-62 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build's twelve round-2 promotions
(`memory/builds/dKeptSession/reviews/2026-10-26-review-KICK-dKeptSession-45-spec-audit.md`)
confirmed finding **id 31 at HIGH**, report item **H4**, which no other id shares.

`KICK-dKeptSession-53` S1 runs `derive_mail_chain` over one parent's rows of `read_mail_rows`' one
read, and that read is the dependent's mailbox: `read_mailbox` keeps only the rows whose `to`
addresses the dependent (`tools/unattended/unattended.sh#read_mailbox`). The `after` link the chain
follows names the newest tip of the sender's other session refs, whoever it was addressed to
(`KICK-dKeptSession-27` S2). With two dependents, which dKeptSession itself has, a take-over's
`seq` 1 `after` usually names the predecessor's row to the other dependent. That row is absent from
the filtered rows, so the predecessor's `confirmed` is never placed and stays open. Under unit 55's
all-or-nothing acks the move then acks nothing and the guard refuses until `flow.wait-ceiling`: the
stall unit 53 exists to remove. This unit gives the chain every row on the parent's refs, read
through the one mail reader, and keeps the rows it acks the dependent's own. It repairs
`KICK-dKeptSession-53` and builds one step after it (order 27).

## 2. Scope (IN)

- **S1** — id 31. The chain read, a selection of the one reader. `read_mailbox <who>
  soft|strict|local [sent]` (`KICK-dKeptSession-5` S6, with `KICK-dKeptSession-21` S2's landed
  `local` mode) gains the selection `sent`. It runs the same one `git log --first-parent --source`
  over every cached mail ref and the same `awk`, so each row's every column, its state, its
  `expired` judgement and the collapse rule are the reader's own. Only the last loop's filter
  changes: under `sent` it keeps the rows whose `ref`, column 9, lies under
  `refs/gov/mail/<who>/`, where `check_mail_addressed` keeps the rows addressed to `<who>`
  otherwise. So it prints one row per message the build `<who>` wrote, whoever it was addressed to.
  Under `sent` the `<who>` must pass `check_slug_shape`: a recipient form prints `mail — not read ·
  --sent reads one build's own mail refs, and '<who>' is no build's slug` and returns 2, before the
  remote is read. The verb is `--mail read <slug> --sent`, beside `--open`, `--ids` and unit 21's
  `--local`, with which it composes. The arm sets `MV_SENT` and records `--sent` in `MV_FLAGS` as it
  records `--open`; `print_mailbox` takes the selection as a fifth argument after unit 21's mode and
  passes it on, `soft` where `--local` is absent. The arm's unknown-flag refusal names `--sent`, and
  the `read` form refusal and the usage-header row gain `[--sent]`. `ack` and unit 25's `answer`
  refuse the flag by their landed form tests over `MV_FLAGS`; the form tests of `post` and unit
  21's `notice` gain `MV_SENT` beside the flags they refuse. No `read_mail_chain` and no `--mail
  chain` is minted (`KICK-dKeptSession-63` S11, §8 F1). Observed by AC3, AC7 and AC8.
- **S2** — id 31. The placement. `derive_mail_chain(rows, chain)` in `tools/loop/loop_transition.py`,
  `chain` required and with no default, returns the `(earlier id, later id)` pairs among the ids of
  `rows` that `KICK-dKeptSession-53` S1's rule, applied over the rows of `chain`, places. It stays
  pure. `read_mail_rows(root, build)` gains the keyword `sent=False`, appending `--sent` to its argv
  after unit 10's landed `--local` where true; its launch, bound, environment and refusals are unit
  5 S9's. `write_consumed_acks(root, build, rows)` (`KICK-dKeptSession-42` S1, as unit 55 S1
  rewrites it) reads a parent's chain only where `check_parent_interfaces` answers `rc` 0 naming an
  `open` row of `rows`: `read_mail_rows(root, <parent>, local=True, sent=True)`, `--mail read
  <parent> --local --sent`, the cache the guard's read has just fetched. It then runs
  `derive_mail_chain` over that parent's rows of `rows` with that `chain`, so the rows it acks stay
  the dependent's own, as unit 53 S3 states. A chain read that raises its `ValueError`, or answers
  unarmed, takes unit 42 S2's path for a call that raises: `mail — interfaces <parent> unread ·
  <why>` on stderr and nothing acknowledged from that parent. So `write_consumed_acks` still never
  raises (unit 42 S1), and the guard then refuses naming the open rows, the cause on stderr. Every
  caller of `derive_mail_chain` passes `chain`: unit 53's `acks-takeover` plant passes its read's
  rows as both arguments in each of its two calls, since one dependent's read there holds every row
  the parent wrote. Unit 5's guard, unit 7's notices and unit 10's interrupts call `read_mail_rows`
  with no `sent` and read as before. Observed by AC1 and AC2.
- **S3** — id 31. The sibling texts superseded by name. `KICK-dKeptSession-53` S1's "over one
  parent's rows of `read_mail_rows`' one read" reads as S2 here: the order is read over every row
  the parent wrote, the ack set over the rows addressed to the dependent. `KICK-dKeptSession-55` S1's
  "It makes no read of its own" reads as S2 too: the one read of the dependent's mailbox is kept,
  and S2 adds one cache read per parent judged. Answered in this unit's own acceptance ledger,
  `memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-61-1-acceptance-ledger.md`,
  which quotes both passages and states S2 supersedes them. Units 53 and 55 build at order 26 and
  are CLOSED when this unit builds, so neither spec nor ledger of theirs is written (F2).
  `KICK-dKeptSession-63` AC20 reads this answer in this unit's ledger. Observed by AC4.
- **S4** — id 31. The plant `chain-two-dependents` of `python tools/loop/loop_transition.py --fixture
  --plant <case>`, in `PLANTS` and run by `run_transition_fixture`, §4 "The plant". It prints `loop:
  fixture · record · exit <rc>` for `tFix`'s and then `tTwo`'s B4 through `run_verb`; one `loop:
  fixture · chain tFix · <a1> precedes <a2> · sent <yes|no> · filtered <yes|no>` line; one `loop:
  fixture · sent fy · <n> row(s) · seq and after on <k>` line, `<k>` the rows carrying neither as
  `-`, and one `loop: fixture · state <id> · <state>` line per row of that read; one `loop: fixture
  · sent build:fy · refused · <why>` line; and last its verdict, `loop: fixture ·
  chain-two-dependents · held`, exit 0, or `MISSED <why>`, exit 1, as `descope-spent` prints its
  own. `run_selftest`'s case table gains one row per line AC1 to AC3 read. It lands each ref's
  second message through `tools/loop/placement.py#write_fixture_gov_ref` with the `parent` keyword
  and the sha return `KICK-dKeptSession-53` S7 lands at order 26, and edits that helper in no way.
  The plant is a branch of `run_transition_fixture` and S1 and S2 add no function, so
  `memory/map/generated/symbols.json` does not move. It moves the `plants=<n>` token of the `loop
  transition record` row in `tools/run-gates/selftest-budgets.txt`, re-priced as §4 "The budget
  rows" states. Observed by AC1 to AC3 and AC5.
- **S5** — The texts this unit makes false, each rewritten as §4 "The shipped texts" states. The
  `--mail` entry of `tools/unattended/VERBS.template.md` gains, after its `--local` sentence: "`--sent`
  takes a build's slug alone and prints instead one row per message on that build's own mail refs,
  `refs/gov/mail/<slug>/`, whoever it was addressed to, each state read as in the build's own
  mailbox; a recipient form prints `mail — not read · --sent reads one build's own mail refs, and
  '<who>' is no build's slug` (exit 2), and `post`, `ack`, `answer` and `notice` refuse the flag."
  Its `--mail read <who> [--open] [--ids]` reads `[--local] [--sent]` after them.
  `memory/guides/UNATTENDED-VERBS.md`, the kit's placeholder-free `rendered` row, is its byte-equal
  copy, copied whole. `help/loop.md`'s `--mail` paragraph gains, after "`--local` reads that copy
  without trying the remote at all.": "`--sent`, given your build's slug, prints every message your
  build wrote, whoever it was addressed to, each in the state its recipient's mailbox shows." Its
  `verb:unattended.sh:--mail` anchor is re-stamped with the fingerprint `python
  tools/govkit/docs_leg.py --fingerprints` prints at build time, since `read_verb_usage` hashes the
  flags of the usage-header row (`tools/govkit/docs_leg.py#read_verb_usage`). Its guard paragraph
  gains one sentence, after unit 55's: "To order a parent's notices the move also reads every
  message that parent wrote, with `--mail read <parent> --local --sent`, from the copy its first
  read fetched." Its fixture-cases sentence names the plant. The loop kit's `README.md` and the
  module docstring of `tools/loop/loop_transition.py` gain the same guard sentence in their
  mail-guard paragraphs and name the plant where they list plants. Observed by AC6.

## 3. Non-goals (OUT)

- What a row supersedes and when acks post: unit 53 S3 and `KICK-dKeptSession-55`, unchanged.
- A second fetch. S2 reads the cache the guard's read filled, so the chain and the ack set come from
  one fetch.
- A second mode for a cache read: `KICK-dKeptSession-21` S2's landed `local` is that mode.
- Any edit of `tools/loop/placement.py`: `KICK-dKeptSession-53` S7 lands `write_fixture_gov_ref`'s
  `parent` keyword, its sha return and its docstring, and S4's plant calls them.
- The report's left-shift checklist entry, that a per-recipient reader's fixture has two recipients.
  No clause of this build names that checklist; AC1 and AC7 are its arms here.

### Edges

- **consumes-from** `KICK-dKeptSession-53` — `derive_mail_chain` and its S1 rule, which this unit runs over every row on the parent's refs (id 31), and S7's `parent` keyword of `write_fixture_gov_ref`, which S4's plant calls
- **hands-off** `KICK-dKeptSession-63` — S1's chain read, S2's signature and §7's arm, which the batch's S11, S6, S7 and S22 settle on the one reader (ids 14, 3, 1, 19); S1 and S2 build them in that form
- **hands-off** `KICK-dKeptSession-64` — AC3, §4 Files touched, §5, §7's arm and the plant, which the batch's S4 reads and S5 re-points to the one reader's sent selection (ids 1, 12)
- **hands-off** `KICK-dKeptSession-65` — S2's `write_consumed_acks` and `derive_mail_chain` in the loop kit's transition, which the batch's S11 re-points, and this spec, which the batch's S10 fixture copies (ids 16, 4)

## 4. Design

### Evidence

Read at `c18b223b` (2026-11-23), past the landings of units 5, 27, 24, 10, 25 and 21, with the
specs of units 6, 7, 35, 42, 8, 11, 43, 52, 53, 55 and 17 read as landed first.

- `tools/unattended/unattended.sh#read_mailbox` takes `<who> soft|strict|local`, unit 21's `local`
  attempting no fetch. It runs one `git log` over every cached mail ref and one `awk`, and prints
  sixteen TAB columns, `ref` 9, `seq` 12, `after` 13, `deadline` 15 and `default` 16 (DERIVED: its
  last `printf`). Its last loop keeps a row where `check_mail_addressed` passes column 3, then reads
  an `open` row `expired` where `check_mail_deadline` passes over columns 9, 10 and 15.
- `tools/unattended/unattended.sh#print_mailbox` takes `who · open · ids · [soft|local]` and calls
  `read_mailbox` with that mode. The `--mail` arm parses `--open`, `--ids` and `--local` into
  `MV_FLAGS`, and its unknown-flag refusal names the thirteen flags it takes (DERIVED: the
  refusal's list). Its `read` form refusal and the usage-header row read `--mail read <who> [--open]
  [--ids] [--local]`. The `post` form test refuses `--open`, `--ids` and `--local` by their
  variables, `notice`'s refuses `--open` and `--ids`, `ack`'s any flag in `MV_FLAGS`, and `answer`'s
  any but `--cite`.
- `tools/loop/loop_transition.py#read_mail_rows` takes `local=False` (unit 10) and launches `--mail
  read <build>`, `--local` appended where true. It zips each row with `MAIL_COLUMNS`, eleven names
  (DERIVED: the tuple); a `mail — off` or absent conf answers `([], why)`, and any other non-zero
  read with no row raises `ValueError`, `mail unknown: --mail read <build> exited <rc>: <first
  line>`. Unit 53 S2 zips `MAIL_ORDER_COLUMNS` after them.
- spec-53 rev-9: S1's `derive_mail_chain(rows)` returns the `(earlier id, later id)` pairs; S3 acks
  the current row and every open interface row of the parent with its key or placed before it; S6
  gives `render_fixture_mail` `seq` and `after`; S7 gives `write_fixture_gov_ref` `parent=None`,
  the commit's one parent where given, and its sha as the return; its `acks-takeover` plant prints a
  chain line over its read's rows and over a `first-seen`-swapped copy.
- spec-42 rev-5 S1: `write_consumed_acks` never raises; S2 calls `check_parent_interfaces(root,
  build, parent)` once per parent and, on a call that raises, writes `mail — interfaces <parent>
  unread · <line or why>` to stderr and acks nothing from that parent.
- spec-55 rev-6 S1, S2: the writer computes every id it would consume before posting and posts only
  when that is every open row, else none; S3 prints `mail — acked <kind> <id> from build:<parent>`.
- `tools/loop/placement.py#write_fixture_gov_ref` pushes one parentless commit and returns nothing at
  `c18b223b`; git refuses a parentless commit pushed onto a ref that already holds one, so the
  second message per ref waits on unit 53 S7.
- Check 26 of the kit gate reds a flag the driver parses that no header line documents
  (`tools/unattended/check-unattended.sh@f00a66b44555:5126`) or that no non-comment line of
  `tools/unattended/unattended.test.sh` carries (`tools/unattended/check-unattended.sh@f00a66b44555:5135`).
  `--sent` is on no line of the suite at `c18b223b` (DERIVED: `grep -c -- --sent` prints 0).

### The two-dependent case

```
ref fy/z/s1:  seq 1 confirmed K1 to tFix (a1) · seq 2 confirmed K1 to tTwo (b1)
ref fy/z/s2:  seq 1 changed   K2 to tFix (a2) after: b1 · seq 2 changed K2 to tTwo (b2)
tFix's rows: a1, a2          -> b1 absent: a1 unplaced, stays open, nothing acked (units 53, 55)
sent rows (S1): a1, b1, a2, b2 -> a1 precedes b1 (s1, seq), b1 is a2's after -> a1 precedes a2
tFix acks a2 and a1; tTwo acks b2 and b1
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `sent` | selection of `read_mailbox`, `tools/unattended/unattended.sh` | none |
| `--sent` | flag of `--mail read`, `tools/unattended/unattended.sh` | none |
| `MV_SENT` | variable of the `--mail` arm, `tools/unattended/unattended.sh` | none |
| `sent` | keyword of `read_mail_rows`, `tools/loop/loop_transition.py` | none |
| `chain` | argument of `derive_mail_chain`, `tools/loop/loop_transition.py` | none |
| `chain-two-dependents` | `PLANTS` case of `loop_transition.py --fixture` | none |

### The plant

It extends unit 53's `acks-takeover` branch of `write_transition_plant`: the driver's conf with
`RUN_CLAIMS` on, a bare remote inside the git dir, `fy`'s spec and lease, K2 the key over the
listing at the lease's `witness` and K1 a key no listing derives, and the fleet user and session id
set as unit 42's plants set them. A second build `tTwo` is staged as `FX_BUILD` is, its README and
an INPROGRESS spec. The four messages of §4's case go from `fy` with the subject `interfaces fy`,
each by `render_fixture_mail` with unit 7's `content_key` and unit 53's `seq` and `after`, `none`
for every `after` but `a2`'s. `a1` and `a2` are each their ref's first commit; `b1` and `b2` are
pushed by `write_fixture_gov_ref` with `parent` the sha it returned for `a1` and `a2`. Then
`tFix`'s B4, and the same argv with `--build tTwo`, the plant's witness an ancestor of HEAD; the
chain line, over `tFix`'s rows of one `read_mail_rows(top, "tFix")` and the rows of
`read_mail_rows(top, "fy", sent=True)`, then over those `tFix` rows as both arguments; that sent
read's lines, fetched so it holds every ack; and `read_mail_rows(top, "build:fy", sent=True)`, whose
`ValueError` it prints.

### Migration

None: no notice exists before `KICK-dKeptSession-7`.

### The shipped texts

Found by `git grep -n -E "mail read|read_mailbox|check_mail_addressed|derive_mail_chain|write_fixture_gov_ref|read_mail_rows"`
over `tools`, `skills`, `help` and `memory/guides` at `c18b223b`, with the specs of units 42, 53 and
55 for the texts they land.

| Text | Verdict |
|---|---|
| `tools/unattended/unattended.sh`, the `--mail read` usage-header row | false by omission: S1 |
| `tools/unattended/unattended.sh`, THE ONE MAILBOX READER comment and `read_mailbox`'s signature comment, one row per message whose `to` passes | false: S1 |
| `tools/unattended/unattended.sh`, `print_mailbox`'s comment and signature comment, the `--mail` arm's comment, its unknown-flag refusal and its `read` form refusal | false by omission: S1 |
| `tools/unattended/unattended.sh`, the comments of `check_lease_witness`, THE ONE CLAIM-LINE READER, `write_mail_ack`, `write_mail_answer` and `print_mail_notice` | stays |
| `tools/unattended/VERBS.template.md`, `memory/guides/UNATTENDED-VERBS.md`, the `--mail` entry | false by omission: S5 |
| `help/loop.md`, the `--mail` paragraph and its `verb:unattended.sh:--mail` anchor | false by omission: S5 |
| `help/loop.md`, the guard paragraph, with units 42 and 55's sentences | false by omission: S5 |
| `help/loop.md`, unit 42's table "Who acknowledges what", as unit 53 S4 writes it | stays |
| `help/loop.md`, the bullets "Read the build's mail at an item boundary" and "See the build's unread mail as it arrives" | stays |
| `help/loop.md`, the loop kit's `README.md`, the module docstring: each sentence listing the plants | false by omission: S5 |
| `tools/loop/README.md`'s and `tools/loop/position.py`'s texts on the interrupts' `local` read | stays |
| `tools/loop/loop_transition.py`, the docstrings of `read_mail_rows`, `derive_mail_chain` and `write_consumed_acks` | false: S2, each naming `sent`, `chain` and the chain read |
| `tools/loop/loop_transition.py`, the comment above `MAIL_COLUMNS` (unit 53) | stays |
| `tools/loop/placement.py#write_fixture_gov_ref`, its docstring as unit 53 S7 writes it | stays |
| `help/orientation-card.md`, `skills/session-kickoff/manifest-check.sh` and `tools/unattended/SKILL.template.md`, the `--open --ids` reads | stays |
| `tools/template-size-limits.txt`, the SKILL row's note on its `--mail read <slug> --open` line | stays |
| `tools/policy/catalogue.toml`, the `mailbox.` and `deps.` rows | stays |

The driver comments that stay describe callers of `read_mailbox <slug> soft` or `local` and the
shared `read_kv` split, none of which passes `sent`. Unit 42's table says a row is superseded by
content key or by the session chain, which this unit widens in rows and keeps in rule. The two
mailbox bullets of `help/loop.md` and the position engine's texts describe unit 10's and unit 21's
reads, which pass no `--sent`. The comment above `MAIL_COLUMNS` names the zip, which S2 does not
move. Unit 53 S7's docstring names `parent` and the sha, which S4 only calls. The card, the kickoff
engine, the skill and the size note read `--open --ids` or `--open`, never `--sent`. No catalogue
row moves, so `.governance/policy.json` does not. The fixture sentence's
`script:tools/loop/loop_transition.py` anchor fingerprints the `--fixture` and `--plant=` flags of
`tools/govkit/usage.toml` alone (`tools/govkit/docs_leg.py#derive_usage_fingerprint`), so naming a
plant re-stamps none. The loop and unattended kit versions are the lander's to mint.

### The refusal ceiling

The driver's refusal sites read `347/347` (DERIVED: `python tools/memory-tree/check-arms.py
--report`'s `ceiling tools/unattended/unattended.sh` row at `c18b223b`). S1 adds no `fail`, `exit 1`
or `status=1` site: its refusal is an `echo` and `return 2` in `read_mailbox`, and the arm's refusals
set `_rl_rc=2`, none of which `tools/memory-tree/check-arms.py` counts, so the ceiling is met
unmoved. The suite arm sits in region eight of `tools/unattended/unattended.test.sh`, opened by `if
in_shard 8; then` past a seam as the mail blocks there are. The effective `FLOOR_ASSERTIONS`, 4156,
and `FLOOR_SHARD_8`, 1373, at `c18b223b` (DERIVED: the last assignment of each) are raised first by
the units ordered before this one, then each over its value at build time by the block's four
`same` assertions (DERIVED: AC7 and AC8), each with its `RAISED` line.

### The budget rows

`check_plant_tokens` holds the `plants=<n>` token of each loop-kit row equal to `len(PLANTS)` of the
module its argv runs, once imported, and refuses a note carrying two tokens
(`tools/run-gates/run-selftests.sh#check_plant_tokens`). The `loop transition record` row runs
`loop_transition.py check --selftest` and carries `plants=19` and a budget of 71 (DERIVED:
`len(PLANTS)` and the row, read at `c18b223b`). Units 7, 35, 42, 11, 52, 53 and 55 add one, two,
four, five, one, two and two before this unit, so S4 moves the token from 36 to 37 (DERIVED: 19
plus those plants). The builder re-reads the count at the unit's base and moves the one token in
place, one above it.

| Figure | `loop transition record` |
|---|---|
| `r` before this unit, as spec-55 rev-6 sums it (PINNED 2026-11-23) | 209.1 s |
| S2's chain read in four landed plants, an estimate (PINNED 2026-11-23) | 4 times 2 s |
| this unit's plant, an estimate (PINNED 2026-11-23) | 31 s |
| `r` after this unit (PINNED 2026-11-23, the sum) | 248.1 s |
| budget, max of the row's value at the base and 1.5 `r` (PINNED 2026-11-23) | 373 |
| the leg's ceiling in `tools/gate-legs.json` (PINNED 2026-11-23) | 120, passed at step 25 |

This unit adds 39 s to the leg (PINNED 2026-11-23, the estimates' sum). The estimates price 2 s a
driver call and 1 s a scratch repository (PINNED 2026-11-23), unit 42's basis, from the row's note,
where `mail-open`, one move and one read over a bare remote, reads 2.0 s (PINNED 2026-11-23). The
four landed plants whose move reaches a current interface row, unit 42's `acks-confirmed` and
`acks-superseded` and unit 53's two, each gain one chain read. The plant makes fifteen calls: per
dependent the guard's read, the lease read and the check inside `check_parent_interfaces`, the
chain read and two acks; then `tFix`'s read, the sent read and the refused read (DERIVED: §4 "The
plant"). The builder reads each plant alone by direct CLI and appends `Then re-read by
KICK-dKeptSession-61 as PINNED proxy r <s>` to the row's note, the budget the row's value or 1.5
`r` rounded up, whichever is higher. The leg has no row in `tools/run-gates/ceiling-evidence.txt`,
so no evidenced maximum moves. The ceiling is parked for the owner, since unit 42's pricing passes
it, and is the owner's to move (`memory/guides/BUILD-METHOD.md`, M3): where the builder's reading
takes `r` past the ceiling the leg carries at the unit's base, the unit stops before it lands, names
the raise, and never edits `tools/gate-legs.json`.

The `unattended driver selftest shard 8/8` row reads 6587 at `c18b223b` (DERIVED: the row), last
raised by `KICK-dKeptSession-21` by 1.5 times its block's direct reading, as unit 35 raises it too.
This unit raises it the same way, over its value at the unit's base, with a `RAISED <old> -> <new>
by KICK-dKeptSession-61` note naming the reading. The block makes eight driver calls (DERIVED: AC7
and AC8) over a bare origin and one clone, read at about 18 s (PINNED 2026-11-23, an estimate):
eight calls at 2 s each and 2 s for the repositories (PINNED 2026-11-23, unit 42's basis), so the
raise is near 27, 1.5 times the estimate (PINNED 2026-11-23).

### Files touched (estimate)

- `tools/unattended/unattended.sh`: S1, the `sent` selection, its refusal, `print_mailbox`'s pass,
  the arm's flag, form tests and refusals, the usage-header row and the comments of §4 "The shipped
  texts"
- `tools/unattended/unattended.test.sh`: the block of AC7 and AC8 in region eight, and the two
  floors' `RAISED` lines
- `tools/loop/loop_transition.py`: S2 in `derive_mail_chain`, `read_mail_rows` and
  `write_consumed_acks`, unit 53's plant calls, S4's plant and its `run_selftest` cases, and S5's
  docstring sentences
- `tools/loop/README.md`: S5, the guard sentence and the plant
- `tools/run-gates/selftest-budgets.txt`: S4, the `loop transition record` row's `plants=` token 36
  to 37 and its note's re-read (DERIVED: `len(PLANTS)` at the unit's base), the token moved in
  place; and the `unattended driver selftest shard 8/8` row's raise of §4 "The budget rows"
- `tools/unattended/VERBS.template.md`, `memory/guides/UNATTENDED-VERBS.md`: S5, the entry and its copy
- `help/loop.md`: S5, the `--mail` paragraph and its re-stamped anchor, the guard sentence and the
  fixture-cases sentence
- `memory/builds/dKeptSession/build/2026-11-21-build-KICK-dKeptSession-61-1-acceptance-ledger.md`:
  S3's answer beside the criteria observed

### Alternatives rejected

- **Dropping the address filter from the dependent's read.** The ack set would then hold rows
  addressed to the other dependent, which this dependent never consumed.
- **Writing `after` per recipient in unit 27.** It changes every message's record for one reader's
  need, and a take-over would still name a row the next recipient never sees when the predecessor
  wrote to it last.
- **A separate `read_mail_chain` and `--mail chain`**, as rev-4 wrote. A second walk of the same refs,
  which `KICK-dKeptSession-63` S11 rules is never minted and `KICK-dKeptSession-64` S5 would remove.
- **`sent` walking only `refs/gov/remote/mail/<who>/`.** The acks sit on the dependents' refs, so
  every row would read `open` and the row would no longer be the reader's own.
- **The chain read's `ValueError` raised out of `write_consumed_acks`**, as rev-8 wrote. Unit 42 S1
  makes the writer never raise and S2 names the path a raising call takes, which keeps the refusal
  and names its cause.
- **A second `parent` keyword landed here**, as rev-9 wrote. Unit 53 S7 lands the same keyword one
  order earlier, so a second edit of `write_fixture_gov_ref` would find it present.

## 5. Production-readiness checklist

- security — none: one more read of refs the node already fetched; nothing new is written.
- perf / scale — one `git log` and one `awk` per parent judged, no fetch.
- error / empty / loading states — an empty cache prints no row, so the chain places nothing and the
  guard names the open row, failing closed as unit 53 §5 states; a refused chain read is named on
  stderr.
- observability — `--mail read <parent> --local --sent` prints the rows the placement read.
- risks — a cache older than the dependent's fetch cannot occur, since S2 reads the chain after that
  fetch in the same transition.
- testing — the criteria of §6 and the arms in §7.
- migration — none.
- user docs — the `--mail` entry of `tools/unattended/VERBS.template.md` and its copy, and the
  `--mail` and guard paragraphs of `help/loop.md`, name `--sent` (S5).

## 6. Acceptance criteria

The loop fixture is S4's plant, §4 "The plant": dependents `tFix` and `tTwo`, session `s1` posting
`confirmed` K1 to each and the take-over `s2` posting `changed` K2 to each.

- **AC1** — When `python tools/loop/loop_transition.py --fixture --plant chain-two-dependents` runs,
  it prints `loop: fixture · record · exit 0` twice, `loop: fixture · state <id> · acked` for each
  of the four rows of its sent read, and `loop: fixture · chain-two-dependents · held`, and exits 0.
  Red when: a copy of `derive_mail_chain` reading `rows` in place of `chain` leaves `a1` unplaced, so
  `tFix`'s record acks nothing, prints `refused — tFix · mail open` naming `a1` and `a2` and exits
  1, and the plant prints `MISSED`.
- **AC2** — When the same plant prints its chain line, it reads `<a1> precedes <a2> · sent yes ·
  filtered no`.
  Red when: the two calls answer alike, as that copy prints `sent no`, so the chain read added
  nothing.
- **AC3** — When the same plant reads `fy`'s sent rows, it prints `loop: fixture · sent fy · 4
  row(s) · seq and after on 4`, and `loop: fixture · sent build:fy · refused · ` naming `exited 2`
  and `is no build's slug`.
  Red when: the sent read keeps the address filter, as a scratch `unattended.sh` doing so prints
  `0 row(s)`, no message being addressed to `build:fy`.
- **AC4** — `tr -s ' \r\n' ' '` over this unit's acceptance ledger piped into `grep -c "over one
  parent's rows of"` prints `1`, and into `grep -c "It makes no read of its own"` prints `1`; and
  `git diff --name-only <pass base> HEAD --` over the specs of units 53 and 55 and their acceptance
  ledgers prints nothing.
  Red when: S3's answer lands in a record of unit 53 or 55, or this unit's ledger does not quote a
  passage it supersedes.
- **AC5** — When, at the unit's commit,
  `python -I -c "import sys; sys.path.insert(0, 'tools/loop'); import loop_transition as m; print(len(m.PLANTS))"`
  runs, it prints the number that
  `grep -oP '^loop transition record\t.*\Kplants=\d+' tools/run-gates/selftest-budgets.txt`
  prints after `plants=`, and `chain-two-dependents` is among the keys of `PLANTS`.
  Red when: the row still carries the count from before this unit's plant.
  figure: PINNED 2026-11-23 at `c18b223b`, the probe prints `19` and the grep `plants=19`, before
  units 7, 35, 42, 11, 52, 53 and 55 take both to 36 (DERIVED: their plants).
- **AC6** — When `python tools/govkit/docs_leg.py --fingerprints` runs at the unit's commit, the
  fingerprint its `verb:unattended.sh:--mail` row prints is the one `grep -o 'usage:
  verb:unattended.sh:--mail [0-9a-f]*' help/loop.md` prints; `grep -c -- '--sent' help/loop.md
  tools/unattended/VERBS.template.md tools/loop/README.md` prints at least 1 for each;
  `chain-two-dependents` is in `help/loop.md`; and `cmp tools/unattended/VERBS.template.md
  memory/guides/UNATTENDED-VERBS.md` prints nothing.
  Red when: the usage row gains `--sent` and the page's anchor keeps the fingerprint from before it,
  which the `docs` leg reads as stale.
  figure: PINNED 2026-11-23 at `c18b223b`, the row and the anchor print `e05e3012`, which unit 6
  leaves as it is; the builder re-reads both at the unit's base.
- **AC7** — When the suite's block has build `fx`'s session `s1` post to `build:fy` then to
  `build:fz`, and `s2` do the same, `--mail read fy` on that clone prints two rows, and `--mail read
  fx --local --sent` then prints the four posts' ids, column 13 of `s2`'s first naming `s1`'s post to
  `build:fz`, a row `--mail read fy` does not print.
  Red when: a scratch `unattended.sh` whose `read_mailbox` keeps the address filter under `sent`
  prints no row, no post being addressed to `build:fx`.
- **AC8** — When the block runs `--mail read build:fx --sent`, it exits 2 printing `mail — not read
  · --sent reads one build's own mail refs, and 'build:fx' is no build's slug`; and `--mail ack fx
  <id> --sent` exits 2 printing the ack's form refusal.
  Red when: a recipient form reads a mailbox under `--sent`, or `ack` passes the flag.

## 7. Gates

`unattended kit gate` · `scratch-guard self-test` · `tier2-review self-test` · `loop transition record` · `loop claim fixtures` · `loop position fixtures` · `kit epoch (shipped bytes move, the version moves)` · `every held leg is budgeted, every budget row resolves` · `policy fixtures` · `docs` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/loop/loop_transition.py · covers AC1 AC2 AC3 · the two-dependent take-over plant, staged red by a copy of `derive_mail_chain` reading `rows` in place of `chain` and one of `read_mailbox` keeping the address filter under `sent` · the `loop transition record` row's `plants=<n>` token rises by one
New arm: tools/unattended/unattended.test.sh · covers AC7 AC8 · one build's two sessions posting to two dependents, read sent and cached, and two refused forms, staged red by a scratch `unattended.sh` whose `read_mailbox` keeps the address filter under `sent` · `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8` rise by four

`loop claim fixtures` and `loop position fixtures` run plants whose driver calls reach
`read_mailbox`, which S1 edits, with no `sent`: the claim kit's `mail-held` and the position
engine's mail plants. Check 26 of `unattended kit gate` reads `--sent` on the usage-header row and on
the suite's block. The arms do not check two parents writing to one dependent, a chain read whose
cache lags a fetch, or a `--sent` read of a build with no mail ref, which prints no row.

## 8. Open questions

- **F1 — Is the chain read a reader of its own or a selection of the one reader?** Options: (a)
  `read_mail_chain <slug>` and `--mail chain`, as rev-4 wrote, running `read_mailbox`'s `git log` and
  `awk` a second time; (b) a `sent` selection of `read_mailbox`, read under `KICK-dKeptSession-21` S2's
  `local` mode by `--mail read <slug> --local --sent`. RESOLVED (agent, 2026-11-21, delegated): (b),
  rung 3; `KICK-dKeptSession-63` S11 settles the chain on the one reader and rules (a)'s names never
  minted, and `local` is the landed spelling of that batch's `cache` mode, so (b) builds one reader
  and no name a later unit removes. widens: none · relaxes: none
- **F2 — Where is S3's answer to unit 53's superseded wording recorded?** Unit 53 builds at order
  26, one step before this unit, so it is CLOSED when this unit builds, and its ledger is in neither
  this unit's Files touched nor its write set. (a) Unit 53's acceptance ledger, a record of a closed
  unit written by a later one; (b) this unit's own acceptance ledger, quoting the unit 53 spec text
  it supersedes. Recommendation (b). RESOLVED (agent, 2026-11-21, delegated): (b), rung 3; a CLOSED
  unit's records are never written by a later unit, as KICK-dKeptSession-49 rev-6 ruled. Rejected:
  (a), writing the earlier unit's ledger. The main loop's ruling, in
  `2026-11-21-prompt-KICK-dKeptSession-50-divergence-brief`.
  widens: none · relaxes: none

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
- rev-6 · 2026-11-21 · S3 · §4 · AC4 · §7 · §8 · S3's answer to unit 53 moves to this unit's own
  acceptance ledger, which joins Files touched and trips the two `recall floor` legs now on §7's leg
  line; F2 resolved (b) and AC4 observing the quoted passage, under the brief
  `2026-11-21-prompt-KICK-dKeptSession-50-divergence-brief`; the class of `KICK-dKeptSession-50`'s
  divergence, which unit 49's rev-6 first resolved. S3 names unit 63's AC20, which still reads the
  answer in unit 53's ledger. `policy fixtures`, whose guard holds `tools/loop/`, joins the leg line
  too.
- rev-7 · 2026-11-22 · S4 · §4 · §4 Files touched · AC5 · §7 · by
  `2026-11-21-prompt-KICK-dKeptSession-12-plant-budget-brief`: the plants move the `plants=<n>` token
  `check_plant_tokens` grades, so S4 and AC5 observe it, `tools/run-gates/selftest-budgets.txt` joins
  Files touched, §4 states the row's re-price over the earlier units' plants and the stop at the
  leg's ceiling, and §7 names the budget leg.
- rev-8 · 2026-11-22 · S1 · S2 · S4 · §4 Files touched · §5 · AC1 · AC3 · AC6 · checked for
  behaviour by `2026-11-21-prompt-KICK-dKeptSession-61-precheck-brief`: `--sent` moves the
  `--mail` verb's fingerprint, so `help/loop.md`'s anchor and the verbs guide's render join Files
  touched and AC6 observes the anchor; S2 names the keyword `read_mail_rows` gains and keeps unit 5
  S9's refusals for the chain read; the plant's lines, verdict and exit spelled as the fixture prints
  them, so AC1 and AC3 read what the plant prints in its scratch repository; `symbols.json` stated
  unmoved; the `plants=` token moved in place.
- rev-9 · 2026-11-23 · §1 · S1 to S5 · §3 · §4 · §5 · AC1 to AC8 · §7 · §10 · re-grounded at
  `bfc0a4e4` under `2026-11-22-prompt-KICK-dKeptSession-61-reground-brief`, with units 10 to 55 and
  17 read as landed: S1's `sent` keeps the one `git log` over every cached ref and selects by the
  `ref` column, so each row's state is the reader's own; S2 states `derive_mail_chain(rows, chain)`'s
  pairs, the chain read only for a parent with a current row, and its refusal on unit 42 S2's
  stderr path in place of rev-8's raise, which unit 42 S1 rules out; S3 also supersedes unit 55
  S1's "no read of its own"; S4's plant names `tTwo`, prints the sent read's states, and lands two
  messages per ref through `write_fixture_gov_ref`'s new `parent`; S5 lists the texts made false,
  §4 their verdicts; the suite arm AC7 and AC8, which check 26 of the kit gate owes `--sent`, with
  its two floors; the refusal ceiling met unmoved; the budget re-priced over 19 landed plants,
  adding 39 s (PINNED 2026-11-23, an estimate); §7 gains the two fixture legs and `kit epoch`.
- rev-10 · 2026-11-23 · S1 · S3 · S4 · S5 · §3 · §4 · AC5 · AC6 · §7 · §10 · re-grounded at
  `c18b223b` under `2026-11-23-prompt-KICK-dKeptSession-61-reground-2-brief`, past units 24, 10, 25
  and 21's landings and with unit 53 rev-9 read as landing first: S4 calls the `parent` keyword and
  sha return unit 53 S7 lands, so `tools/loop/placement.py` leaves Files touched and §3 says so; S1
  names `MV_SENT`, the fifth argument of `print_mailbox` and the form tests of `post`, `ack`,
  `answer` and `notice`; S5 spells the sentences the verbs entry and the `--mail` paragraph gain;
  §4's evidence, texts table and figures re-read at this tree, the floors 4156 and 1373 (DERIVED:
  the suite's last assignments), the anchor `e05e3012`; the shard 8/8 row raised by the block's
  reading, as unit 21 raised it; §7 trades `loop placement fixtures` for `loop position fixtures`,
  whose mail plants reach the reader.

## 10. Reuse audit

The seam extended is the one mail reader, `read_mailbox`'s one `git log` and one `awk`
(`KICK-dKeptSession-5` S6), given a selection rather than a second walk, read under
`KICK-dKeptSession-21` S2's landed `local` mode rather than a second cache mode; the Python side
reuses `read_mail_rows`' one launch (`KICK-dKeptSession-5` S9) and unit 53's `derive_mail_chain`,
given a wider row set rather than a new rule; the plant joins the landed fixture
`tools/loop/loop_transition.py#run_transition_fixture`, extends unit 53's branch, and lands its
second message per ref through the `parent` keyword unit 53 S7 gives
`tools/loop/placement.py#write_fixture_gov_ref`. `python tools/codebase-map/reuse_lookup.py "read
every message one build sent across its mail refs"`, re-run at `c18b223b`, ranked `read_text`,
`read`, `read_bytes` and `build` by name stem only; no existing seam in the tree selects a mailbox
by sender, so the one reader and the sibling specs are the seams.

Recall terms used: `python tools/memory-recall/query.py "how is a promoted unit placed when it
repairs an earlier unit's pass" --terms "promoted order pass commit ledger superseded batch minors
hands-off consumes-from parity mirror"`
