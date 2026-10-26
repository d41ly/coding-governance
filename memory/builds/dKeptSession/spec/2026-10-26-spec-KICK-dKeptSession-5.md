# KICK-dKeptSession-5 — the mailbox per build: one append-only ref per writing session, closed kinds, read and disposed at every transition

**Status:** OPEN · rev-1 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 16 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0143@cafeb575 whole
**Carries:** node:record-kind.mailbox-message

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-build-KICK-dKeptSession-1-fix-return.md](../build/2026-10-26-build-KICK-dKeptSession-1-fix-return.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-14 KICK-dKeptSession-28 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md) | research | KICK-dKeptSession-6 KICK-dKeptSession-10 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-prompt-KICK-dKeptSession-1-fix-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-fix-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-14 KICK-dKeptSession-28 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |

<!-- /gen:spec-records -->

## 1. Goal

A build can reach the session working on another build, a message survives the session that wrote it,
and a build's transition waits on the messages addressed to it (gap-flow-06). Each writing session
appends to its own ref, `refs/gov/mail/<slug>/<fleet tag>/<session>`, so writers never contend for one
chain (gap-conc-04; the owner's NT-16). A message's kind comes from one closed set checked on write; it
is written only through the coordination verbs; every transition reads the build's messages and is
refused while one addressed to it is neither answered nor acknowledged, until `flow.wait-ceiling`
passes; the transition disposes what was answered, the card shows what is open, and the transition log
keeps what was disposed (coordination item 6; the whole-design audit's C2-F15).

## 2. Scope (IN)

- **S1** — The ref (I16): `derive_mail_ref <slug> <tag> <session>` in `tools/unattended/unattended.sh`
  prints `refs/gov/mail/<slug>/<tag>/<segment>`, the segment `derive_ref_segment <session>`
  (TOOL-dPlacedRequest-12 S1), `<slug>` the SENDER's build (§8 F1) and `<tag>` this node's
  `resolve_fleet_tag` (TOOL-dPlacedRequest-1 S11). It is the one place the namespace is spelled for a
  write. The session is `CLAUDE_CODE_SESSION_ID`; absent, a post prints
  `mail — not written: no session id` and exits 2. Observed by AC1, AC9.
- **S2** — The writer, `write_mail_ref <ref> <tip read> <message>`: `build_gov_commit <tip read>
  <message>` under the fixed `gov-claim` identity, then `write_gov_ref <ref> <tip read> <commit>`
  (TOOL-dPlacedRequest-11 S1, S2), so each post is one commit parented on its ref's previous tip and a
  session's first post is the one parentless commit. rc 0 written, 1 lost, 2 not completed with
  `GOVREF_WHY`. It is the only function that writes a mail ref. Observed by AC1, AC9.
- **S3** — The closed kinds (I18): a `[mail]` table in `tools/loop/loop.toml` holding `kinds`, the
  twelve of coordination item 6 (`confirm-request`, `confirmed`, `changed`, `overlap`, `takeover`,
  `landed`, `question`, `answer`, `ack`, `intake`, `withdrawn`, `superseded`), read by
  `read_mail_kinds(kit_dir)` in `tools/loop/loop_lib.py`, which refuses an empty or repeated list with
  `LoopError`, and printed one per line by `python tools/loop/loop_lib.py --mail-kinds`. A post whose
  kind is not printed there is refused before any commit, exit 2. Observed by AC2.
- **S4** — The record (I17), built by `build_gov_message <header> <body file> <key> <value> …`: the
  header, a blank line, one `key: value` line per pair, a blank line, the body. A body over 4096
  bytes or carrying a NUL or a control byte other than tab and newline, and a value carrying a
  newline, are refused with rc 2 and `GOVMSG_WHY`. It is the second instance of
  TOOL-dPlacedRequest-12 S6's record, so the one builder is extracted here and that unit's
  `write_register` calls it, its record bytes unchanged. A message's header is `gov-mail <slug>/<id>`
  and this unit writes the keys `id`, `build`, `from-tag`, `from-session`, `to`, `kind`, `item`,
  `pass`, `subject` and `answers`, each absent one `none`. Observed by AC3.
- **S5** — The post, `unattended.sh --mail post <slug> --to <recipient> --kind <kind> --subject
  <text> [--item <instance key>] [--pass <pass>] [--answers <id>] <body file>`, in order: the switch
  (S11); the session (S1); the kind (S3); `check_mail_recipient <recipient>` (KICK-dKeptSession-28);
  the body and values (S4); one bounded fetch of `+refs/gov/mail/<slug>/*:refs/gov/remote/mail/<slug>/*`
  through `observe_remote` (`tools/unattended/unattended.sh:480`) to the remote `resolve_claim_remote`
  names (`:2097`), then `add_feed_sightings refs/gov/remote/mail/` (TOOL-dPlacedRequest-13 S4); the id,
  `derive_message_id <slug> <item> <pass> <kind> <subject> <answers>`, and
  `check_mail_duplicate <slug> <id>` (KICK-dKeptSession-22); the tip read from this session's cache
  ref; `write_mail_ref`. It prints `mail — posted <id> · <ref>` and exits 0; a duplicate or a lost
  write exits 1; a refusal or a write not completed exits 2. Observed by AC1, AC2, AC9.
- **S6** — The one reader (I20), `read_mailbox <who> soft|strict`, `<who>` a slug, read as
  `build:<slug>`, or a recipient of KICK-dKeptSession-28's grammar. One bounded fetch of
  `+refs/gov/mail/*:refs/gov/remote/mail/*`, then `add_feed_sightings`; one `git log --source
  --first-parent` over every cached mail ref, parsed by one `awk` as `read_claims` parses claims
  (`:2151-2170`). It prints one tab-separated row per message whose `to` passes
  `check_mail_addressed <to> <who>` (KICK-dKeptSession-28): `id`, `kind`, `to`, `state`, `first-seen`,
  `from-build`, `subject`, `answers`, `ref`, `commit`. `first-seen` is TOOL-dPlacedRequest-17 S1's
  `read_first_seen` for the row's remote ref and commit. Rows with one id collapse to the earliest
  `first-seen`, ties to the lesser ref name, so a cross-ref race shows once. Under `soft` a failed fetch
  prints one `mail — local copy: <why>` line on stderr and reads the cache; under `strict` it exits 2.
  Observed by AC4, AC5.
- **S7** — The states: a row of kind `answer` or `ack` is `reply` and is never open; any other row is
  `answered` when a cached message of kind `answer` names its id in `answers`, `acked` when one of kind
  `ack` does, and `open` otherwise (§8 F5). Observed by AC4.
- **S8** — The verbs (I19), beside `--claims` in the dispatch table (`:14489`): `--mail post` (S5);
  `--mail read <who> [--open] [--ids]`, the reader under `soft`, `--open` printing only `open` rows and
  `--ids` their ids on one space-separated line or `none`; `--mail ack <slug> <id>`, a post of kind
  `ack` from `<slug>` answering `<id>`, addressed to `build:<from-build>` of that row, its subject the
  row's, its body empty, refused with exit 2 when `<id>` is not a row addressed to `<slug>`. These are
  the only writers of a mail ref; KICK-dKeptSession-25 adds `--mail answer`. Observed by AC4, AC5.
- **S9** — The transition guard, a step of TOOL-dDeclaredLoop-3's writer between its §4 steps 1 and 2:
  `write_transition` in `tools/loop/loop_transition.py` runs `bash <prefix>/unattended/unattended.sh
  --mail read <slug> --open` in the repository, bounded by `MAIL_GUARD_SECONDS` (30). Open rows exit 1
  printing `refused — <slug> · mail open <id> …` and write nothing. `mail — off`, an absent driver and
  zero rows each pass, the first two with one NOTE naming why the mailbox is unarmed. A read that
  answers nothing within the bound exits 2, unknown and not none. Only `build:` and `unit:` recipients
  gate (§8 F2). Observed by AC5, AC6.
- **S10** — The disposal: past the guard, the writer lists every row addressed to the build whose
  state is `answered`, `acked` or, once KICK-dKeptSession-24 adds it, `expired`, and whose id no earlier transition of the build names in its
  `disposed` field, read through `read_transitions(build, repo)` (TOOL-dDeclaredLoop-3 S7), and writes
  them as the extension field `disposed=<id>+<id>` (I21), registered in `TRANSITION_FIELDS`. Where
  `log` is selected, it also writes one `mailbox-message` record per disposed id in the same commit.
  Observed by AC6.
- **S11** — The switch and the stand-in. Every mail write runs only while `RUN_CLAIMS` is `on`
  (`:671-676`, TOOL-dPlacedRequest-12 S7's rule), and otherwise prints `mail — off` and writes nothing,
  exit 2 for a post and 0 for a read with no rows. The verbs write the ref directly through
  `write_gov_ref` until dTotalRecall lands the record door, whose hand-over this unit marks at
  `write_mail_ref` (§8 F4). Observed by AC7.
- **S12** — The record kind `record-kind.mailbox-message`, a row of the record factory
  `tools/memory-tree/build_records.py` (PLAY-dOrderedCharter-7 S7):
  `<date>-build-<anchor id>-mailbox-message-<n>.md`, `**Serves:** journal <anchor id>`, fields `Id`,
  `From`, `To`, `Kind`, `Subject`, `Answers`, `State`, `Reply` (the replying message's id) and `Ref`,
  and the body in one fenced block. The anchor is TOOL-dDeclaredLoop-3 §8 F2's rule. Observed by AC6.
- **S13** — The card: the `## pointers` section's `mail —` line (I11, KICK-dKeptSession-13), added to
  that unit's `render_pointers` with the word `mail` appended to its `POINTER_LINES`, and written by
  `manifest-check.sh --card --pointers --build <slug>` from `--mail read <slug> --open --ids`, run
  through `resolve_kit_file unattended unattended.sh` under `CARD_CLAIMS_BOUND`
  (`skills/session-kickoff/manifest-check.sh:228`) as the `claims —` cell runs its read (`:649-655`):
  `mail — <id> <id> …`, `mail — none`, or `mail — skipped: <why>`. Observed by AC8.
- **S14** — The documentation: the verbs guide gains a mailbox section, the three verbs, the ref, the
  kinds, the record, the states and the exit codes; `help/loop.md` (TOOL-dDeclaredLoop-1's page)
  gains the guard and the disposal. Observed by AC10.

## 3. Non-goals (OUT)

- No deadline: `flow.wait-ceiling` is judged by KICK-dKeptSession-24, which adds the `expired` state
  S9 lets pass and S10 disposes. Until it lands, an unanswered message holds the transition.
- No `answer` verb or answering role: KICK-dKeptSession-25.
- No sequence number, predecessor or content key: KICK-dKeptSession-27 adds `seq`, `after` and
  `content-key` to S4's keys and S6's row.
- No notice at items or tool calls, and no fetch stamp: KICK-dKeptSession-21 and -10.
- No live ring: KICK-dKeptSession-6.
- No prune of a closed build's mailbox, and no copy of undisposed messages into its folder: the close
  program's (v2:1927).
- No secret scan of a body. Coordination payloads outside the scan's population are gap-rt-44,
  dWellOiledMachine's; S4 caps and shape-checks the body at the write.
- No record door: dTotalRecall's.

### Edges

- **consumes-from** `KICK-dKeptSession-13` — `## pointers`, the card section whose `mail —` line S13 writes
- **consumes-from** `KICK-dKeptSession-28` — `check_mail_recipient`, which the post refuses an illegal recipient by, and `check_mail_addressed`, which the reader selects rows by
- **consumes-from** `KICK-dKeptSession-22` — `derive_message_id`, each message's id, and `check_mail_duplicate`, which refuses a retried post
- **hands-off** `KICK-dKeptSession-23` — `read_mailbox` and `write_mail_ref`, the one mail writer whose every landed write the change feed records
- **hands-off** `KICK-dKeptSession-27` — `read_mailbox`, whose row and record that unit extends with `seq`, `after` and `content-key`
- **hands-off** `KICK-dKeptSession-24` — `read_mailbox`, whose rows that unit judges against `flow.wait-ceiling` and marks `expired`
- **hands-off** `KICK-dKeptSession-10` — `read_mailbox`, which the item-boundary read arms the position engine's mailbox interrupt with
- **hands-off** `KICK-dKeptSession-25` — `read_mailbox`, whose `question` rows that unit answers through `--mail answer`
- **hands-off** `KICK-dKeptSession-21` — `read_mailbox`, whose unread ids the notice lists
- **hands-off** `KICK-dKeptSession-6` — `read_mailbox` and the post's tail, where the live ring rings after the write
- **hands-off** `KICK-dKeptSession-7` — `read_mailbox`, through which the dependency notices are posted and read
- **consumes-from** external — TOOL-dPlacedRequest-11's `write_gov_ref` and `build_gov_commit`, -12's `derive_ref_segment`, `RUN_CLAIMS` rule and register record, -13's `add_feed_sightings`, -17's `read_first_seen`, and -1's `resolve_fleet_tag`
- **consumes-from** external — TOOL-dDeclaredLoop-1's `loop.toml` and `loop_lib.py`, and -3's `write_transition`, `TRANSITION_FIELDS` and `read_transitions`
- **hands-off** external — dTotalRecall's record door, through which the coordination verbs write once it lands

## 4. Design

### Evidence

- No mail code exists: `git grep -n -i mailbox -- tools skills` finds nothing at this base.
- A gov ref write today is `write_claim`'s `commit-tree` under the `gov-claim` identity and a
  `--force-with-lease` push (`tools/unattended/unattended.sh:2396-2467`, `:2419`, `:2423`), which
  TOOL-dPlacedRequest-11 moves into `build_gov_commit` and `write_gov_ref`.
- `read_claims` makes one bounded fetch of one namespace into its cache and parses every record with
  one `awk` (`:2118-2170`); its refspec and cache are `CLAIM_NS` and `CLAIM_CACHE` (`:2087-2088`).
- The kickoff engine reads a driver verb through `resolve_kit_file unattended unattended.sh` under a
  bound and never re-derives its format (`skills/session-kickoff/manifest-check.sh:630-655`).
- A `[[stand-in]]` row names a transition-table item and its owner, and a row naming no row item is
  red (TOOL-dDeclaredLoop-13 S8, at `origin/main`), so the record door, which is no item, has no row.
- An extension field's value matches `[A-Za-z0-9._:+@-]+` (TOOL-dDeclaredLoop-3 §4 "The trailer"), so
  I21's ids are joined with `+`, never `,`; the owner of I21 refines the brief's spelling.
- The sightings walk stops at the first commit not authored `gov-claim` (TOOL-dPlacedRequest-13 S4);
  S2's commits carry that identity, so the observer clock sees every message.

### Which build's ref a session writes

The slug in the ref is the sender's build. The clause's duplicate check reads "every one of the
build's per-session refs" and catches "a retry from a new session among them" (cl-0160): a retry comes
from the sender, so the build whose session refs hold it is the sender's. A reader therefore reads
every build's mail refs, which the one fetch of `refs/gov/mail/*` already brings, and selects by `to`.

### The record

```
gov-mail fx/3f9c2a71b0de

id: 3f9c2a71b0de
build: fx
from-tag: a
from-session: 6c1f0b8e-…
to: build:fy
kind: question
item: item.design.exit@1#0a1b2c3d
pass: 2
subject: I16
answers: none

Does the mail ref segment stay one component under derive_ref_segment?
```

### The transition, in order

| Step | Owner |
|---|---|
| 1. read the channel set | TOOL-dDeclaredLoop-3 |
| 1a. the guard: `--mail read <slug> --open`; open rows refuse, exit 1 | this unit |
| 2. `derive_move` | TOOL-dDeclaredLoop-3 |
| 3. the witness | TOOL-dDeclaredLoop-3 |
| 3a. the disposal: `disposed=<id>+<id>` and the `mailbox-message` records | this unit |
| 4 to 7. staged check, records, commit, micro-format line | TOOL-dDeclaredLoop-3 |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `--mail` | verb, with `post`, `read` and `ack` | none |
| `derive_mail_ref` | shell function | `derive`, OK |
| `write_mail_ref` | shell function | `write`, OK |
| `build_gov_message` | shell function | `build`, OK |
| `read_mailbox` | shell function | `read`, OK |
| `read_mail_kinds` | Python function | `read`, OK |
| `disposed` | `TRANSITION_FIELDS` member | none |
| `MAIL_GUARD_SECONDS` | constant, 30 | none |
| `mailbox-message` | record kind of `build_records.py` | none |
| `refs/gov/mail/`, `refs/gov/remote/mail/` | ref namespaces | none |

`MAIL_GUARD_SECONDS` is PINNED at 30, twice `CARD_CLAIMS_BOUND`'s 15, since the guard's read fetches
every build's mail refs where the card's claims read fetches one namespace.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: the ref, writer, builder, post, reader, verbs and switch, and
  `KIT_UNATTENDED_VERSION` moved
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`, rendered to `memory/guides/UNATTENDED-VERBS.md`
- `tools/loop/loop.toml`: the `[mail]` table
- `tools/loop/loop_lib.py`: `read_mail_kinds` and `--mail-kinds`
- `tools/loop/loop_transition.py`: the guard, the disposal and `disposed` in `TRANSITION_FIELDS`
- `tools/memory-tree/build_records.py`: the `mailbox-message` kind row
- `skills/session-kickoff/manifest-check.sh`: the `mail —` line
- `skills/session-kickoff/manifest-check.test.sh`
- `help/loop.md`: the guard and the disposal

### Alternatives rejected

- **One ref per build.** Eight writers took 4.5 times the ideal compare-and-swap attempts against 1.0
  with one ref per sender (gap-conc-04).
- **The recipient's build in the ref.** A retry from a new session would land under another build's
  refs than the duplicate check reads, and a `node:` or `project` message would need a build it does
  not have.
- **The guard refusing when the remote is unreachable.** A build carries its work offline (P40), so
  the guard reads the local copy under `soft` and refuses only on rows it sees.
- **The kinds in the driver.** coordination item 6 puts the closed set in the loop definition, "a
  change to the loop kit, never an adopter's extension".

## 5. Production-readiness checklist

- security — a new write surface on the shared remote, written only through `write_gov_ref`, dark
  behind `RUN_CLAIMS`; every field is validated at the write, the recipient by its grammar, the kind
  by the closed set, the body capped and shape-checked; a session writes only its own ref.
- perf / scale — a post makes one bounded fetch of its build's refs and one push; a read makes one
  bounded fetch of every mail ref and one `git log` over them.
- error / empty / loading states — no session, an unknown kind, an illegal recipient and a bad body
  each refuse before a commit; an unreachable remote reads the local copy under `soft`, named.
- observability — every outcome is one `mail —` line naming the id or the ref; a refused transition
  names every open id.
- risks — a message nobody answers holds its recipient's transitions until KICK-dKeptSession-24
  lands its deadline; a mail ref is never pruned before the close program does.
- testing — the fixture cases under AC1 to AC9 and the suite arms in §7.
- migration — none: the namespace and the record kind are new.
- user docs — the verbs guide and `help/loop.md`, TOOL-dDeclaredLoop-1's page, which gains the guard
  and the disposal.

## 6. Acceptance criteria

The fixture is a bare remote and two clones under `%TEMP%` with short names, `RUN_CLAIMS` on, each
clone's sessions a distinct `CLAUDE_CODE_SESSION_ID`, the loop kit and the transition writer installed.

- **AC1** — When clone A's session `s1` posts two messages from `fx` and session `s2` posts one, the
  remote holds `refs/gov/mail/fx/a/s1` with a first-parent chain of two commits, the first parentless,
  and `refs/gov/mail/fx/a/s2` with one, each commit's subject `gov-mail fx/<id>`.
  Red when: two sessions share a ref, or a second post is not parented on the first.
- **AC2** — When a post names `--kind chat`, it exits 2 naming the closed set and the remote gains no
  ref; `python loop_lib.py --mail-kinds` prints the twelve kinds; a planted `loop.toml` repeating one
  is refused with `LoopError`.
  Red when: an unlisted kind reaches the remote.
- **AC3** — When `build_gov_message` is given a 4097-byte body, or one carrying a NUL, or a value with
  a newline, it returns 2; and `--register problem`'s record over a fixed input is byte-equal to
  TOOL-dPlacedRequest-12 S6's layout written by hand.
  Red when: a bad body or value is built, or the register's bytes change.
- **AC4** — When clone B's `fy` posts a `question` to `build:fx` and clone A runs
  `unattended.sh --mail read fx`, one row prints with `state` `open`; after A runs `--mail ack fx
  <id>`, the row reads `acked`, and the `ack` row itself, addressed to `build:fy`, reads `reply` there.
  Red when: an acknowledged message reads `open`, or an `ack` reads `open`.
- **AC5** — When one id is planted on two of `fy`'s session refs, `--mail read fx` prints it once,
  with the earlier `first-seen`; and with the remote unreachable, `--mail read fx` prints
  `mail — local copy` and the cached rows, exit 0.
  Red when: a duplicate shows twice, or a failed fetch reads as an empty mailbox.
- **AC6** — When `python loop_transition.py record --build fx …` runs with the planted `question`
  unanswered, it exits 1 printing `mail open <id>` and writes no commit; after the `ack`, the move
  writes a trailer carrying `disposed=<id>`, a log record carrying it, and one
  `<date>-build-<anchor>-mailbox-message-1.md` with `**State:** acked`; the next move disposes nothing.
  Red when: a transition records over an open message, as a planted guard reading no mail shows, or
  a disposed id is disposed twice.
- **AC7** — When `RUN_CLAIMS` is off in the clone's conf, `--mail post …` prints `mail — off`, exits 2
  and the remote gains no ref, and the transition passes with one NOTE naming the unarmed mailbox.
  Red when: a mail ref is written with the switch off, or the guard refuses on an unarmed mailbox.
- **AC8** — When `manifest-check.sh --card --pointers --build fx` runs with the question open, the
  card's `## pointers` section carries `mail — <id>`, and after the `ack` it carries `mail — none`.
  Red when: the card shows `mail — none` while a message is open.
- **AC9** — When the post runs with `CLAUDE_CODE_SESSION_ID` unset it prints `mail — not written: no
  session id` and exits 2; and `grep -n "refs/gov/mail/" tools/unattended/unattended.sh` finds the
  namespace on `derive_mail_ref`'s line and the two fetch refspecs only.
  Red when: a mail ref is written with no session, or a second constructor spells the namespace.
- **AC10** — When `grep -n -- "--mail" tools/unattended/VERBS.template.md` runs, the guide names the
  three verbs, the twelve kinds, the four states and the exit codes 0, 1 and 2; and `grep -n "mail open"`
  over the loop kit's help page finds the guard.
  Red when: the guide omits a verb, a kind, a state or a code, or the page omits the guard.

## 7. Gates

`unattended kit gate` · `manifest-check self-test` · `scratch-guard self-test` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `memory hygiene`

The loop kit's legs, `loop definition` and `loop transition record`, join the manifest with
TOOL-dDeclaredLoop-1 and -3; the close runs them where they exist.

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC7 AC9 · two sessions' refs, an unlisted kind, a bad body, an ack, a cross-ref duplicate, a failed fetch, the switch off and no session, staged against the base driver, which has no mail verb · none
New arm: tools/loop/loop_transition.py · covers AC6 · a transition over an open question, then over its ack, staged by a planted guard reading no mail · none
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC8 · the `mail —` line open and then none, staged by a planted pointers writer omitting it · none

## 8. Open questions

- **F1 — Whose build names a mail ref?** (a) The sender's, readers selecting by `to`; (b) the
  recipient's. (b) puts a retry from a new session where the clause's duplicate check over "the
  build's per-session refs" cannot be the sender's refs, and leaves a `node:` or `project` message no
  build to sit under. Rung 1, cl-0160's duplicate check, which reads the retrying sender's refs.
  RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none
- **F2 — Which recipients gate a build's transition?** (a) `build:` and `unit:` recipients of the build;
  (b) those and every `node:` and `project` message. (b) lets one broadcast hold every build of the
  project. Rung 1, the clause's "a message addressed to the build". RESOLVED (agent, 2026-10-26,
  delegated): (a). widens: none · relaxes: none
- **F3 — What does the guard read when the fetch fails?** (a) The local copy, named; (b) refuse the
  transition. (b) stops every offline build, against P40's "alone and offline". Rung 3, the most
  capable option. RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none
- **F4 — How is the record door's stand-in registered?** (a) Marked at `write_mail_ref`, the one
  writer, with the hand-over named in §3; (b) a `[[stand-in]]` row, as the brief proposed. (b) is red
  under TOOL-dDeclaredLoop-13 S8, which admits only a transition-table item, and the record door is
  none. Rung 3. RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none
- **F5 — Does a reply need a reply?** (a) `answer` and `ack` read `reply` and never gate; (b) every
  kind gates until answered. (b) makes each `ack` hold the asker until it is acknowledged, so no
  exchange ever ends, against P39's "every loop ends". Rung 3. RESOLVED (agent, 2026-10-26,
  delegated): (a). widens: none · relaxes: none
- **F6 — Is the mailbox dark?** (a) Behind `RUN_CLAIMS`, the coordination switch every gov ref write
  already reads; (b) always on. (b) is a new write path on the shared remote with no switch, against
  the charter's small rule for risky behaviour. Rung 3, TOOL-dPlacedRequest-12 §8 F3's answer.
  RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft. The govkit subject pins are not among the files touched:
  `selfcheck` derives their rows from the gate-legs manifest alone, one per leg
  (`tools/govkit/govkit.py:2968-2975`), and this unit adds no leg, so no row moves.

## 10. Reuse audit

The seams extended are the one compare-and-swap ref writer TOOL-dPlacedRequest-11 extracts from
`write_claim` (`tools/unattended/unattended.sh:2396`), the bounded namespace reader `read_claims`
(`:2118`) whose fetch and `awk` shape `read_mailbox` follows, TOOL-dPlacedRequest-12's record layout,
whose builder this unit extracts at its second instance, the loop definition and transition writer of
TOOL-dDeclaredLoop-1 and -3, and the kickoff engine's bounded driver read
(`skills/session-kickoff/manifest-check.sh:630-655`). The probe
`python tools/codebase-map/reuse_lookup.py "append a message commit to a per-session ref by
compare-and-swap and read every message"` ranked `build_commit` (`tools/unattended/lib-unattended.sh:1186`)
and `read_journal` by name stem: the first builds a records commit over a revision range, not a gov
ref, and neither reads a namespace. Scout B's line cites `:2077`, `:2087-2088`, `:2118`, `:2396`,
`:2419` and `:2423` hold at this base; its `[[stand-in]]` proposal disagrees with TOOL-dDeclaredLoop-13
S8, as F4 records.

Recall terms used: `python tools/memory-recall/query.py "which build's mailbox does a session write and
read" --terms "mailbox per build per-session ref refs/gov/mail append-only transition refused
unanswered acknowledged disposed"`
