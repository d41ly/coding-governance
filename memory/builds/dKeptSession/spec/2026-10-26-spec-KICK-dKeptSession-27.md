# KICK-dKeptSession-27 — each message carrying its session's sequence number, a take-over its predecessor, and an interface notice its content key

**Status:** DEFERRED · rev-7 · 2026-11-23 · node a · Tier-2 · base 9900b200 · streams kickoff · order 18 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0164@148f5fda whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md) | research | KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-10 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-28 KICK-dKeptSession-1 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-28 |
| [2026-10-26-build-KICK-dKeptSession-27-deviation-271.md](../build/2026-10-26-build-KICK-dKeptSession-27-deviation-271.md) | deviation | — |
| [2026-10-26-build-KICK-dKeptSession-27-deviation-272.md](../build/2026-10-26-build-KICK-dKeptSession-27-deviation-272.md) | deviation | — |
| [2026-10-26-build-KICK-dKeptSession-27-deviation-273.md](../build/2026-10-26-build-KICK-dKeptSession-27-deviation-273.md) | deviation | — |
| [2026-11-21-build-KICK-dKeptSession-45-reground-orders-14-19-returns.md](../build/2026-11-21-build-KICK-dKeptSession-45-reground-orders-14-19-returns.md) | research | KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-36 KICK-dKeptSession-24 KICK-dKeptSession-1 |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-28 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-28 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-23-precheck-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-23-precheck-brief.md) | research | KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 |
| [2026-11-21-prompt-KICK-dKeptSession-36-orders-17-19-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-36-orders-17-19-reground-brief.md) | research | KICK-dKeptSession-36 KICK-dKeptSession-24 |
| [2026-11-22-prompt-KICK-dKeptSession-27-reground-brief.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-27-reground-brief.md) | research | — |
| [2026-11-23-prompt-KICK-dKeptSession-27-1-spec-writer.md](../prompts/2026-11-23-prompt-KICK-dKeptSession-27-1-spec-writer.md) | journal | — |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |

<!-- /gen:spec-records -->

## 1. Goal

Messages carry no order across one build's session refs, so a take-over's `changed` relayed ahead of
its predecessor's `confirmed` leaves a dependent on the older interface (gap-conc-15). Each message
carries its session's sequence number; a session's first message names its predecessor's last; and
`confirmed` and `changed` carry the content key of the interface they announce, so a dependent acts on
the notice whose key equals the key it recomputes from the interface's text, never on arrival order
(P40: losing a relay costs latency, never correctness).

## 2. Scope (IN)

- **S1** — The sequence number (I22), the key `seq: <n>` that `tools/unattended/unattended.sh#write_mail_post`
  writes into each record through `build_gov_message`, after the landed `answers` key: `1` when the
  tip it reads from this session's cache ref is empty, else `git rev-list --first-parent --count
  <tip>` plus one, the message's first-parent depth on its own ref. `seq` is no field of the id, so a
  retried post keeps the id `check_mail_duplicate` refuses. Observed by AC1.
- **S2** — The predecessor, the key `after: <id>`, written after `seq`. On a message whose `seq` is 1
  it is the id of the tip of the newest other ref cached under `refs/gov/remote/mail/<slug>/`, or
  `none` when that prefix holds no other ref; on every later message it is `none`. One
  `for-each-ref` lists each cached ref with its tip and the tip's subject; a tip whose subject is not
  `gov-mail <slug>/<12 hex>` is skipped, and its id is that subject's tail. Newest is by the first
  sighting of each tip, read by one `read_first_seen` call over one `ref TAB commit` pair per ref on
  stdin (`tools/lib/gov-feed.sh#read_first_seen`, carried in the driver's `gov_feed_sh` block), each
  ref spelled as the feed keys it, `refs/gov/` plus what follows `refs/gov/remote/`. In ascending
  order an unsighted tip reads `-` and sorts after every sighted one, as `read_mailbox` orders its
  rows; ties go to the lesser ref name. The step runs after the post's fetch and its
  `add_feed_sightings`, so every cached tip has been sighted where the feed can be written. A session
  that takes a build over therefore names the last message its predecessor wrote. Observed by AC2.
- **S3** — The content key, the key `content-key: <12 hex>`, written after `after`, on a `confirmed`
  or `changed` post: `derive_gov_id --file <interface file>`
  (`tools/unattended/unattended.sh#derive_gov_id`), the file named by the post's new `--interface
  <file>` option. It also fills the eighth field, `<content-key>`, of the landed
  `derive_message_id` call, where the post passes `none` today; every other kind writes `none` in the
  record and passes `none` to the id. `write_mail_post` takes the file as a ninth argument, the word
  `none` where the option is absent, so `write_mail_ack`'s eight-argument call posts as it does. The
  checks run after the body-line check and before `resolve_claim_remote`, so each refusal reaches no
  remote, and each exits 2 with one line: `mail — not written · a <kind> post names the interface it
  announces: --interface <file>` for a `confirmed` or `changed` post without it; `mail — not written
  · --interface names the interface of a confirmed or changed post, not a <kind>` for any other kind
  naming it; `mail — not written · the interface file cannot be read: <file>` where `derive_gov_id`
  answers rc 1. The `--mail` parser takes `--interface` beside `--to`, `--kind` and `--subject`, its
  two refusals naming the flags and the post's form gain it, and the read's form refusal counts it
  among the flags a read takes none of. Observed by AC3.
- **S4** — The reader: `tools/unattended/unattended.sh#read_mailbox`'s row gains the columns `seq`,
  `after` and `content-key`, columns 12 to 14 after `reply`, read from the record; a record without
  one reads `-`. The record walk reads the three keys through `read_kv` beside the six it requires,
  and never requires them, so a message posted before this unit still prints. Unit 5's eleven
  columns keep their places: `tools/unattended/unattended.sh#check_lease_witness` reads columns 2, 4
  and 10 by position, `write_mail_ack` 1, 6 and 7, `print_mailbox` 1 and 4, and
  `tools/loop/loop_transition.py#read_mail_rows` takes any row of eleven or more fields and zips the
  first eleven with `MAIL_COLUMNS`, so none of them is edited. No landed arm of
  `tools/unattended/unattended.test.sh` compares a whole row: unit 5's read cases take columns 1 to
  5, 9 and 11 by position. Observed by AC1, AC2, AC7.
- **S5** — The dependent's check, `check_interface_notice <slug> <subject> <interface file>` in
  `tools/unattended/unattended.sh`, a shell function no verb prints. While `RUN_CLAIMS` is not `on` it
  prints `interface — off` and exits 2, since the mailbox is then not read. It derives `derive_gov_id
  --file <interface file>` first, then reads `read_mailbox <slug> soft`, and over that read's
  `confirmed` and `changed` rows whose subject is `<subject>` prints `interface — current <id> · <kind>
  · key <k>`, exit 0, for the row whose `content-key` equals the key, and `interface — unconfirmed ·
  key <k>`, exit 1, when none does. Where two rows carry that key, both announcing the same text, it
  names the lesser id, a choice no arrival can move. It never chooses a row by `first-seen`, `seq` or
  fetch order. A read that exits non-zero prints `interface — not read · ` and the read's first line;
  an interface file `derive_gov_id` cannot read prints `interface — not read · the interface file
  cannot be read: <file>`; both exit 2 and print no `unconfirmed` line, so a refusal is not read as a
  stale interface. Observed by AC4, AC5.
- **S6** — The texts this unit makes false, each rewritten as §4 "The shipped texts" lists: the
  driver's `--mail post` usage line names `[--interface <file>]` after `[--answers <id>]`;
  `write_mail_post`'s and `read_mailbox`'s header comments name the three keys, the content key's
  source and the three columns; the `--mail` entry of `tools/unattended/VERBS.template.md` and its
  installed copy name the three keys, `--interface`, the columns and the rule a dependent acts by,
  keeping `KICK-dKeptSession-51` S2's act sentence where it landed; `help/loop.md`'s `--mail`
  paragraph names `--interface` and the three columns, and its `verb:unattended.sh:--mail` anchor
  takes the fingerprint `python tools/govkit/docs_leg.py --fingerprints` prints once the usage line
  carries the option, since `tools/govkit/docs_leg.py#read_verb_usage` derives the row from the usage
  line's flags; and the comment above `MAIL_COLUMNS` in `tools/loop/loop_transition.py` says it names
  the row's first eleven columns. Observed by AC6.

## 3. Non-goals (OUT)

- No dependency action: what a dependent's unit does on a current `changed`, the interface-change
  re-entry, and where it reads the interface's text from are KICK-dKeptSession-7's.
- No lease take-over: TOOL-dPlacedRequest-1 S5's `take-over` verb; this unit names the predecessor from
  the mail refs alone, so it holds when the lease record is unreadable.
- No total order across builds: `seq` orders one session's messages and `after` links one build's
  sessions; nothing orders two builds' messages, and nothing needs to.
- No rewrite of a delivered message: a later notice supersedes by key, never by editing.
- No deadline columns: `KICK-dKeptSession-24` appends `deadline` and `default` after this unit's
  three, at order 19.
- No change to `MAIL_COLUMNS`' eleven names: a loop kit reading fourteen would drop every row an
  older driver prints, and the guard would pass open mail.
- No kit version: the lander mints the unattended and loop kits' (`tools/push-main.sh@78f40c3c2475:27`).

### Edges

- **consumes-from** `KICK-dKeptSession-22` — `derive_message_id` and `derive_gov_id`, whose 12-hex convention the content key reuses over the interface's text
- **consumes-from** `KICK-dKeptSession-5` — `read_mailbox`, whose row this unit extends, and the post, whose record carries the three keys
- **hands-off** `KICK-dKeptSession-7` — `content-key` and `check_interface_notice`, by which a dependent acts on the recomputed key and never on arrival order
- **consumes-from** external — TOOL-dPlacedRequest-17 S1's `read_first_seen`, landed in `tools/lib/gov-feed.sh`, which orders the predecessor's refs
- **consumes-from** `KICK-dKeptSession-31` — the eight-field `derive_message_id`, whose `<content-key>` field this unit's `--interface` key fills in place of `none`
- **hands-off** `KICK-dKeptSession-42` — `check_interface_notice`, whose `current <id>` line names the row that unit's transition writer acknowledges (id 55)
- **hands-off** `KICK-dKeptSession-53` — the `seq`, `after` and `content-key` columns of `read_mailbox`'s row, from which that unit derives the chain (id 4)
- **hands-off** `KICK-dKeptSession-63` — S1's `seq` from the tip read, which the batch's S12 derives per chained message (id 15)

## 4. Design

### Evidence

Read at HEAD `9900b2007` (2026-11-23), past unit 22's, unit 5's and unit 31's landings (merge
`cc68aefa0`), with `KICK-dKeptSession-23` rev-5, `-36` rev-7, `-39` rev-5 and `-51` rev-5 read as
landed before this unit.

- Each session writes its own ref, one commit per message, parented on its previous tip
  (`tools/unattended/unattended.sh#write_mail_ref`), so a message's depth on its ref is its order
  within its session and is recomputable from the ref. A session's first post is parentless, so
  nothing in git links a take-over to its predecessor unless the message says so.
- `tools/unattended/unattended.sh#write_mail_post` takes eight arguments, slug to body file; after
  its fetch it calls `add_feed_sightings refs/gov/remote/`, then `derive_message_id "$slug" "$it"
  "$ps" "$kind" "$sub" "$an" "$to" none`, then `check_mail_duplicate`, then reads the tip from
  `refs/gov/remote/${ref#refs/gov/}`, then builds the record with the keys `id`, `build`, `from-tag`,
  `from-session`, `to`, `kind`, `item`, `pass`, `subject` and `answers`. Its refusals print `mail —
  not written · <why>` and `return 2`.
- `tools/unattended/unattended.sh#derive_gov_id` returns rc 1 where `--file` names a file that is not
  a readable regular file, and prints 12 hex digits otherwise.
- `tools/unattended/unattended.sh#read_mailbox`'s record walk calls `read_kv($0, want, v, 0)` with
  `want` the six keys `id build to kind subject answers`, and drops a record missing any of them; its
  second `awk` prints eleven fields, `reply` last. `CLAIM_KV_AWK`'s `read_kv` keeps only a key of the
  set it is given, so the three keys need a read set wider than `want`.
- The `--mail` branch of the driver's dispatch takes `--to`, `--kind`, `--subject`, `--item`,
  `--pass` and `--answers` as value flags; its refusals `mail — not written · --mail takes …` and
  `mail — not written · the form is --mail post …` spell that set, and the read refuses any value
  flag through `[ -n "$MV_TO$MV_KIND$MV_SUB$MV_ITEM$MV_PASS$MV_ANS" ]`.
- `tools/loop/loop_transition.py#read_mail_rows` keeps a line where `ln.count("\t") >=
  len(MAIL_COLUMNS) - 1` and zips it with the eleven `MAIL_COLUMNS`, so a fourteen-field row reads its
  first eleven unchanged; `write_mail_records` reads only those.
- No tracked text posts a `confirmed` or `changed` today (`git grep` for `--kind confirmed` and
  `--kind changed` over `tools`, `skills` and `help` prints nothing, PINNED `9900b2007`), and
  `KICK-dKeptSession-23`'s cases post `question` only, so S3's refusal breaks no landed caller.
- The feed keys every sighting by the remote's spelling of a ref: `derive_feed_events` maps a cached
  `refs/gov/remote/<tail>` to `refs/gov/<tail>` (`tools/lib/gov-feed.sh#derive_feed_events`), and
  `read_first_seen` matches that spelling, so a pair spelled with the cache prefix reads `-`; it
  answers the oldest feed line of each ref and commit in file order.
- P40 states that losing a relay costs latency and never correctness
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c9:1076`).
- `tools/memory-tree/row_grammar.py#derive_content_key` is a text fold for backlog rows, and
  `tools/loop/request.py#derive_request_content_key` a SHA-256 over that fold for requests; both are
  a different key, and the id convention here is KICK-dKeptSession-22's `derive_gov_id`.

### The ceiling

`.memory-tree.conf#REFUSAL_CEILINGS` holds the driver at 347 (PINNED, read 2026-11-23,
TOOL-dWitnessedBar-1), its census at that ceiling by this re-ground's brief. A site is a line whose
code carries `exit 1`, assigns `status=1` or calls `fail <n> "` (`tools/memory-tree/check-arms.py`,
its module docstring, signature 2). Every refusal this unit adds prints a line and `return`s 2 or 1
from a function, as the landed mail refusals do, and the dispatch exits through `exit "$_rl_rc"`, so
it adds no site, the census stays at 347 and no ceiling decision is owed. A builder who finds a
refusal needs an `exit 1` writes it as a `return` instead.

### The red case

| Order of arrival at the dependent | Interface text now | Arrival-order reader | `check_interface_notice` |
|---|---|---|---|
| `changed` (key K2, from the take-over) first, then `confirmed` (key K1) | K2's | `confirmed`, stale | `changed`, current |

### The shipped texts

Every shipped text stating the mail record's keys, the row's columns, the content key or the post's
form, by `git grep -n -i -E "mail read|read_mailbox|MAIL_COLUMNS|content key|--mail post|gov-mail"`
over `tools`, `skills`, `help`, `memory/guides`, `memory/gotchas` and the root documents at
`9900b2007`.

| Text | Verdict |
|---|---|
| `tools/unattended/unattended.sh`, the `--mail post` usage line | false by omission: S6 |
| `tools/unattended/unattended.sh#write_mail_post`, its header comment's keys and "the content key `none`" | false: S6 |
| `tools/unattended/unattended.sh#read_mailbox`, its header comment's column list | false by omission: S6 |
| the `--mail` dispatch's flag and post-form refusals | false by omission: S3 |
| `tools/unattended/VERBS.template.md` and `memory/guides/UNATTENDED-VERBS.md`, the `--mail` entry | false: S6 |
| `help/loop.md`, the `--mail` paragraph and its usage anchor | false by omission: S6 |
| `tools/loop/loop_transition.py`, the comment above `MAIL_COLUMNS` | false: S6 |
| `tools/unattended/unattended.sh#check_lease_witness`, its comment's ten columns | stays |
| `tools/unattended/unattended.sh#derive_message_id`, its comment | stays |
| `help/loop.md`'s guard paragraph, `tools/loop/README.md`'s mail guard and `[mail]` text | stays |
| `help/orientation-card.md`, `skills/session-kickoff/manifest-check.sh` and both unattended Skill copies | stays |
| `skills/session-kickoff/card-store.fixture.sh` and the suite's `seed_mail_at`, planted records | stays |
| `tools/policy/catalogue.toml`, the three `mailbox.` keys | stays |

The witness check's comment names the columns it reads by position, which keep their places. The id's
comment names a content-key field without a value, true once the key fills it, and
`KICK-dKeptSession-51` S1's ninth-field sentence lands there first. The guard paragraphs and the
loop README name the read and the open state, never a column count, and the `[mail]` text names the
kinds, which do not change. The card, the kickoff engine and the Skills read `--open --ids`, whose
output does not change. A planted record without the three keys reads `-` in each (S4), so neither
fixture is edited. The catalogue keys name how often a mailbox is read and fetched, so no summary
moves and the policy mirror does not move.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `seq`, `after`, `content-key` | record keys and `read_mailbox` columns | none |
| `--interface` | `--mail post` option | none |
| `check_interface_notice` | shell function | `check`, OK |

### Files touched (estimate)

- `tools/unattended/unattended.sh`: S1 to S3 in `write_mail_post` and the `--mail` dispatch, S4 in
  `read_mailbox`, S5's `check_interface_notice`, and S6's usage line and comments
- `memory/map/generated/symbols.json`: `check_interface_notice`, re-rendered by `python
  tools/codebase-map/gen_map.py --write`, never hand-edited
- `tools/unattended/unattended.test.sh`: the arm in §7, inline and defining no shell function, and
  the effective `FLOOR_ASSERTIONS` and region eight's `FLOOR_SHARD_8` raised by its counted
  assertions, each with a `RAISED` line. They read 4095 and 1312 at `9900b2007` (DERIVED, the last
  assignment of each in the suite), and unit 23's cases raise both first. No row of
  `tools/run-gates/selftest-budgets.txt` is re-priced: the driver suite's shard rows are ESTIMATE
  rows sized by region share and carry no `plants=` token, and no loop plant is added.
- `tools/loop/loop_transition.py`: the comment above `MAIL_COLUMNS` alone (S6); no code line moves
- `tools/unattended/VERBS.template.md`, and its installed copy `memory/guides/UNATTENDED-VERBS.md`,
  byte-equal under the unattended kit gate's check 10
- `help/loop.md`: S6's paragraph and the re-stamped `verb:unattended.sh:--mail` anchor, which reads
  `f25c9c53` before this unit (PINNED, `docs_leg.py --fingerprints` at `9900b2007`)

No kickoff manifest's `watch:` line names any of these paths.

### Alternatives rejected

- **A timestamp per message.** Two nodes' clocks disagree, and a relay reorders arrival regardless.
- **A build-wide counter.** It needs one ref every session contends for, the serialisation
  gap-conc-04 removed.
- **The predecessor read from the lease's history.** `read_claims` parses only each lease's tip
  (TOOL-dPlacedRequest-1 S2), so the previous holder would need a second parser of the lease record.
- **`MAIL_COLUMNS` widened to fourteen.** Its row filter would then drop an older driver's rows.

## 5. Production-readiness checklist

- security — three more validated keys on an existing write, each through `build_gov_message`'s
  control-byte check; the interface file is read only to hash it and never reaches the remote.
- perf / scale — one `rev-list --count` per post, and on a session's first post one `for-each-ref`
  and one `read_first_seen` over its build's refs.
- error / empty / loading states — a `confirmed` or `changed` without an interface file is refused; an
  unsighted ref sorts as newest; a record without the keys reads `-`; the check exits 2, never
  `unconfirmed`, on a mailbox it did not read.
- observability — the check prints the chosen id, its kind and the key, or `unconfirmed` with the key.
- risks — two sessions posting first messages at one instant may each name the other's earlier
  message; `after` is a link, and the content key, not `after`, decides what a dependent acts on.
- testing — the fixture cases under AC1 to AC5, the suite arm in §7, and the landed `mail-open` plant
  under AC7.
- migration — none: no `confirmed` or `changed` message exists yet, and an older record reads `-`.
- user docs — the verbs guide, and `help/loop.md`'s `--mail` paragraph and its usage anchor (S6).

## 6. Acceptance criteria

The fixture has the shape of KICK-dKeptSession-5's arm in `tools/unattended/unattended.test.sh`,
built fresh in its own directory so no landed case's post shares its refs: a bare remote and two
clones A and B under `%TEMP%`, `RUN_CLAIMS` on, each post made as that arm's `run_mail_arm` makes it
under its own `CLAUDE_CODE_SESSION_ID`, and each check in a subshell that sources the driver and runs
`load_driver_conf`, as that arm's AC3 does. B reads nothing before AC4.

- **AC1** — When session `s1` of `fx` on clone A posts two `question`s to `build:fy`, `unattended.sh
  --mail read fy` on A prints them with `seq` 1 and 2 in column 12.
  Red when: a second post reads `seq` 1, as a planted writer counting from zero shows.
- **AC2** — When session `s0` of `fx` on clone A posts one message before AC1's posts, the
  `seen-utc` of A's feed line for `s0`'s tip is rewritten to `2026-01-01T00:00:00Z` so the order holds
  without a sleep, and session `s2` on A then posts twice, column 13 of `s2`'s first message reads
  `s1`'s second id, of `s2`'s second `none`, and of `s0`'s message, the build's very first, `none`.
  Red when: a take-over's first message names no predecessor, or names one that is not the last, as a
  planted pair spelled with the cache prefix shows: every tip then reads `-`, and the tie goes to
  `s0`, the lesser ref name `refs/gov/mail/fx/a/s0`.
  figure: the stamp is PINNED; the ids are DERIVED from the posts' `mail — posted <id>` lines.
- **AC3** — When a `confirmed` post names `--interface i.txt`, its record's `content-key` equals
  `derive_gov_id --file i.txt` and its id equals `derive_message_id` over its fields with that key
  eighth; a `changed` post with no `--interface`, a `question` post naming `--interface i.txt`, and a
  `confirmed` post naming an absent file each exit 2 with S3's line and the remote's refs are unchanged.
  Red when: an interface notice lands without its key, or an option no kind reads is ignored.
- **AC4** — When clone A's `s1` posts a `confirmed` (`--interface i1.txt`) and `s2` a `changed`
  (`--interface i2.txt`), both to `build:fy` with the subject `I16`, B's feed holds planted sightings
  of the `changed`'s tip at `2026-01-01T00:00:00Z` and the `confirmed`'s at `2026-01-01T00:01:00Z`
  before B's first read, and `check_interface_notice fy I16 i2.txt` runs on B, it prints `interface —
  current <the changed's id> · changed · key <i2.txt's key>` and exits 0.
  Red when: the dependent acts on the `confirmed`, as a planted check choosing the newest `first-seen`
  shows.
  figure: both stamps are PINNED.
- **AC5** — When the same check runs with an interface file matching neither key, it prints
  `interface — unconfirmed · key <k>` and exits 1; with an interface file that does not exist it
  prints `interface — not read · the interface file cannot be read: <file>`, exits 2 and prints no
  `unconfirmed` line; and with `RUN_CLAIMS` off it prints `interface — off` and exits 2.
  Red when: an unmatched interface reads as confirmed, or an unreadable file or an unread mailbox
  reads as unconfirmed.
- **AC6** — When `grep -n "content-key" tools/unattended/VERBS.template.md` runs, the `--mail` entry
  names `seq`, `after`, `content-key` and `--interface`, and `cmp` finds
  `memory/guides/UNATTENDED-VERBS.md` equal to it; `grep -n -- "--interface" help/loop.md` finds the
  `--mail` paragraph; `grep -n "interface <file>" tools/unattended/unattended.sh` finds the usage line;
  and `python tools/govkit/docs_leg.py --fingerprints` prints `verb:unattended.sh:--mail` with the
  fingerprint that paragraph's anchor carries.
  Red when: the guide omits a key or the option, or the anchor keeps `f25c9c53`, the fingerprint from
  before `--interface`.
- **AC7** — When `python tools/loop/loop_transition.py --fixture --plant mail-open` runs, the driver
  printing fourteen-column rows, it exits 1 printing `refused — <build> · mail open <id>`, as
  `KICK-dKeptSession-5` AC6 states.
  Red when: the guard's row split refuses or misreads a fourteen-column row.

## 7. Gates

`unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `scratch-guard self-test` · `tier2-review self-test` · `docs` · `loop transition record` · `policy fixtures` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `memory hygiene`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC5 · two posts on one session, a take-over's first post, an interface notice without a file, and a `changed` sighted before the `confirmed` it supersedes, staged by a planted writer counting from zero, a planted pair spelled with the cache prefix and a planted check choosing by arrival · the effective `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8` rise by its counted assertions

## 8. Open questions

- **F1 — How does a take-over find its predecessor?** (a) From the build's other session refs in the
  mail cache, newest tip by first sighting; (b) from the build lease's previous holder. (b) needs the
  lease's history, which `read_claims` does not parse, and a mail message would then depend on the
  lease kit's record. Rung 3, the most capable option: (a) meets AC2 from the mail refs alone.
  RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none
- **F2 — What does the content key hash?** (a) The interface file's bytes through `derive_gov_id
  --file`; (b) a normalised text fold, as `derive_content_key` folds backlog rows. (b) calls two
  different interfaces equal when they differ in whitespace a consumer may read. Rung 3: (a).
  RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-31`, `KICK-dKeptSession-42`
  mirrored, the other ends of the edges the round-1 spec audit's promoted units declare; no other
  section moved.
- rev-3 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-53` mirrored, the other ends of
  the edges the round-1 promotions' audit's disposal declared
- rev-4 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-63` mirrored, the other ends of
  the edges the round-3 promotions' audit's disposal declared
- rev-5 · 2026-11-21 · S2 · S3 · S4 · §3 · §4 · AC1 · AC2 · §7 · §10 · re-grounded on the landed
  tree at `c2a407b0` by `2026-11-21-prompt-KICK-dKeptSession-36-orders-17-19-reground-brief`: S2
  reads the landed `read_first_seen` by its stdin pairs, each ref spelled as the feed keys it; S3
  names the id's `<content-key>` field it fills; S4 appends after `reply`, the eleventh column
  `KICK-dKeptSession-5` rev-9 added, and keeps the ten the landed witness check reads by position; the version move and the guarded legs `kit epoch`, `scratch-guard self-test`
  and `tier2-review self-test` added; line-number citations replaced by `path#symbol` and blob pins.
  Nothing narrowed: no landed unit carries a key, the option or the check.
- rev-6 · 2026-11-21 · S3 · S4 · S5 · S6 · §3 · §4 · §5 · AC2 to AC7 · §7 · checked for behaviour
  under `2026-11-21-prompt-KICK-dKeptSession-23-precheck-brief`: AC2's red is staged over two other
  refs, since one alone is chosen whatever its spelling; the sightings AC2 and AC4 order are planted
  a minute apart, since `seen-utc` counts whole seconds; S3 refuses `--interface` on another kind and
  an unreadable file; S5 names the lesser id where two rows share the key, and exits 2, never
  `unconfirmed`, on a read or file it cannot use; S4 holds unit 5's `read_mail_rows` and whole-row
  arms to the widened row, AC7 observing the guard; S6 re-stamps `help/loop.md`'s
  `verb:unattended.sh:--mail` anchor, whose fingerprint the option moves, and the `docs`,
  `loop transition record` and `policy fixtures` legs join; `symbols.json` joins Files touched for
  `check_interface_notice`; the version move is dropped, the lander minting it.
- rev-7 · 2026-11-23 · S1 to S6 · §3 · §4 · §5 · AC1 to AC7 · §7 · §10 · re-grounded at `9900b2007`
  under `2026-11-22-prompt-KICK-dKeptSession-27-reground-brief`, units 22, 5 and 31 landed and 23,
  36, 39 and 51 read as landed: S3 names the post's ninth argument, where its checks sit and its
  three refusal lines, and the dispatch's flag set; S2 reads each tip's id from its subject and says
  an unsighted tip sorts as newest; S4 is narrowed, since the landed `read_mail_rows` already takes
  any row of eleven or more fields and no landed arm compares a whole row, so neither is edited, and
  it widens the record walk's read set past the six keys it requires; S5 names its refusal lines and
  `interface — off`; S6 lists every shipped text the keys make false, the usage line, two header
  comments, the guide, the help paragraph and the `MAIL_COLUMNS` comment, with §4's table of the
  texts that stay; AC2 rewrites `s0`'s stamp on clone A, since `s0` on B would make the lesser ref
  `s1`'s and hide the red, and AC4 plants B's two sightings before its first read; §4 states the
  refusal ceiling met with no new site and the floors at 4095 and 1312 (DERIVED, `9900b2007`); §3
  keeps `MAIL_COLUMNS` at eleven.

## 10. Reuse audit

The seams are KICK-dKeptSession-5's `write_mail_post` and `read_mailbox`, which this unit's three
keys extend, the post's record through the landed `build_gov_message` and the reader's walk through
`CLAIM_KV_AWK`'s `read_kv`; KICK-dKeptSession-22's `derive_gov_id`, which the content key reuses;
and the landed `tools/lib/gov-feed.sh#read_first_seen`, the observer clock every lease read takes,
which orders the predecessor. The probe `python tools/codebase-map/reuse_lookup.py "order messages
by sequence number and content key not arrival"`, re-run 2026-11-23 at `9900b2007`, ranked `key`,
`keys`, `note`, `parse_key`, `read_conf_key` and `derive_request_content_key`
(`tools/loop/request.py`), none a sequence or a supersession; the last is a normalised fold, F2's
option (b). No existing seam fits the ordering rule itself. Scout B's row 9 named
`tools/memory-tree/row_grammar.py#derive_content_key` and ruled it out, which holds.

Recall terms used: `python tools/memory-recall/query.py "how does a dependent order a changed relayed
before confirmed" --terms "sequence number take-over predecessor content key confirmed changed arrival
order relay P40"`
