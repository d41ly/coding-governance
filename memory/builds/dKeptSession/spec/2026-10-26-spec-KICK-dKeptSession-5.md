# KICK-dKeptSession-5 — the mailbox per build: one append-only ref per writing session, closed kinds, read and disposed at every transition

**Status:** DEFERRED · rev-11 · 2026-11-21 · node a · Tier-2 · base c2a407b0 · streams kickoff · order 16 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0143@cafeb575 whole
**Carries:** node:record-kind.mailbox-message

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-1-fix-return.md](../build/2026-10-26-build-KICK-dKeptSession-1-fix-return.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-14 KICK-dKeptSession-28 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md) | research | KICK-dKeptSession-6 KICK-dKeptSession-10 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-1 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-build-KICK-dKeptSession-5-deviation-51.md](../build/2026-10-26-build-KICK-dKeptSession-5-deviation-51.md) | deviation | — |
| [2026-10-26-build-KICK-dKeptSession-5-deviation-52.md](../build/2026-10-26-build-KICK-dKeptSession-5-deviation-52.md) | deviation | — |
| [2026-10-26-build-KICK-dKeptSession-5-deviation-53.md](../build/2026-10-26-build-KICK-dKeptSession-5-deviation-53.md) | deviation | — |
| [2026-10-26-build-KICK-dKeptSession-5-deviation-54.md](../build/2026-10-26-build-KICK-dKeptSession-5-deviation-54.md) | deviation | — |
| [2026-10-26-build-KICK-dKeptSession-5-deviation-55.md](../build/2026-10-26-build-KICK-dKeptSession-5-deviation-55.md) | deviation | — |
| [2026-10-26-build-KICK-dKeptSession-5-deviation-56.md](../build/2026-10-26-build-KICK-dKeptSession-5-deviation-56.md) | deviation | — |
| [2026-10-26-build-KICK-dKeptSession-5-deviation-57.md](../build/2026-10-26-build-KICK-dKeptSession-5-deviation-57.md) | deviation | — |
| [2026-11-21-build-KICK-dKeptSession-45-reground-orders-14-19-returns.md](../build/2026-11-21-build-KICK-dKeptSession-45-reground-orders-14-19-returns.md) | research | KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-23 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-36 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-1 |
| [2026-10-26-prompt-KICK-dKeptSession-1-fix-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-fix-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-9 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-14 KICK-dKeptSession-28 |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-reground.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-reground.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-25 KICK-dKeptSession-36 KICK-dKeptSession-44 KICK-dKeptSession-56 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-22-precheck-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-22-precheck-brief.md) | research | KICK-dKeptSession-22 KICK-dKeptSession-31 |
| [2026-11-21-prompt-KICK-dKeptSession-24-precheck-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-24-precheck-brief.md) | research | KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 |
| [2026-11-21-prompt-KICK-dKeptSession-5-1-spec-writer.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-5-1-spec-writer.md) | journal | — |
| [2026-11-21-prompt-KICK-dKeptSession-5-orders-16-17-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-5-orders-16-17-reground-brief.md) | research | KICK-dKeptSession-23 KICK-dKeptSession-39 KICK-dKeptSession-51 |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |

<!-- /gen:spec-records -->

## 1. Goal

A build reaches the session working on another, a message outlives its writer, and a build's
transition waits on the messages addressed to it (gap-flow-06). Each writing session appends to its own
ref, `refs/gov/mail/<slug>/<fleet tag>/<session>`, so writers never contend (gap-conc-04; NT-16). A
kind comes from one closed set checked on write; a transition is refused while a message addressed to
the build is neither answered nor acknowledged, until `flow.wait-ceiling` passes, and its log keeps
what it disposed; the card shows what is open (coordination item 6; C2-F15).

## 2. Scope (IN)

- **S1** — The ref (I16): `derive_mail_ref <slug> <tag> <session>` in `tools/unattended/unattended.sh`,
  beside `derive_lease_ref`, prints `refs/gov/mail/<slug>/<tag>/<segment>`, the one place the namespace
  is spelled for a write: the segment `derive_ref_segment <session>`
  (`tools/unattended/unattended.sh#derive_ref_segment`), `<slug>` the SENDER's build (F1) held to the
  silent `check_slug_shape` (§4 Evidence), `<tag>` this node's `resolve_fleet_tag`
  (`tools/unattended/lib-unattended.sh#resolve_fleet_tag`). The session is `CLAUDE_CODE_SESSION_ID`:
  absent, a post prints `mail — not written: no session id`, exit 2; a node with no fleet row prints
  `mail — not written: <the cause resolve_fleet_tag printed>`, exit 2. Observed by AC1, AC9.
- **S2** — The writer, `write_mail_ref <ref> <tip read> <message>`: the three `GOVREF_` names set as
  `write_card_ref` sets them (`tools/unattended/unattended.sh#write_card_ref`), then
  `build_gov_commit <tip read> <message>` (`tools/lib/gov-ref.sh#build_gov_commit`) under the fixed `gov-claim` identity, and `write_gov_ref <ref> <tip
  read> <commit>`. Each post is one commit parented on its ref's previous tip,
  and a session's first post is the one parentless commit. rc 0 written, 1 lost, 2 not completed with
  `GOVREF_WHY`. It is the only function that writes a mail ref. Observed by AC1, AC9.
- **S3** — The closed kinds (I18): a `[mail]` table in `tools/loop/loop.toml` holding `kinds`, the
  twelve of coordination item 6 (`confirm-request`, `confirmed`, `changed`, `overlap`, `takeover`,
  `landed`, `question`, `answer`, `ack`, `intake`, `withdrawn`, `superseded`). `read_mail_kinds(kit_dir)`
  in `tools/loop/loop_lib.py` reads it as `read_dispositions` reads `[dispositions]`, and `check_loop` grades the table where present as it
  grades that one (`tools/loop/loop_lib.py#check_loop`): an absent table, an empty list, a repeated
  member or one outside `SEG` is `LoopError`. `python tools/loop/loop_lib.py --mail-kinds` prints the
  kinds one per line, exit 0, or `loop: <why>`, exit 1, its usage line naming it. The
  driver reaches it through `resolve_python` and its `resolve_kit_dir` for the `loop` home; a post whose
  kind is not printed there, or made where no loop kit resolves, is refused before any commit, exit 2,
  naming the set or the missing kit. Observed by AC2.
- **S4** — The record (I17), built by `build_gov_message <header> <body file> <key> <value> …`: the
  header, a blank line, one `key: value` line per pair, a blank line, the body with its trailing
  newlines cut. `write_register` writes that layout inline today, so the builder is extracted at its
  second instance and `write_register` calls it for both forms, its bytes, its `register —` lines and
  its field checks unchanged. The builder
  refuses, rc 2 with `GOVMSG_WHY` carrying the words `write_register` prints today, a body over 4096
  bytes (PINNED, the cap `write_register` holds), a body carrying a NUL or a control byte other than
  tab and newline, and an empty value or one carrying a control byte. A message's header is
  `gov-mail <slug>/<id>`, and this unit writes the keys `id`, `build`, `from-tag`, `from-session`, `to`,
  `kind`, `item`, `pass`, `subject` and `answers`, each absent one `none`. Observed by AC3.
- **S5** — The post, `unattended.sh --mail post <slug> --to <recipient> --kind <kind> --subject
  <text> [--item <instance key>] [--pass <pass>] [--answers <id>] <body file>`, in order: the switch
  (S11); `check_slug_shape <slug>`; the session and the tag (S1); the kind (S3); `check_mail_recipient
  <recipient>` (KICK-dKeptSession-28); the body and the values (S4), and any body line or value the
  record factory would refuse at disposal (F7); `resolve_claim_remote`, check 24; one bounded, pruned fetch of
  `+refs/gov/mail/<slug>/*:refs/gov/remote/mail/<slug>/*` with `write_card_ref`'s options, then
  `add_feed_sightings refs/gov/remote/`; the id, `derive_message_id <slug> <item> <pass> <kind>
  <subject> <answers> <to> none`, KICK-dKeptSession-31 S1's eight fields, and `check_mail_duplicate <slug> <id>` (KICK-dKeptSession-22); the tip read from this session's cache ref `refs/gov/remote/mail/<slug>/<tag>/<segment>`; `write_mail_ref`. It
  prints `mail — posted <id> · <ref>` and exits 0; a duplicate or a lost write exits 1; a refusal or
  a write not completed exits 2. Observed by AC1, AC2, AC9.
- **S6** — The one reader (I20), `read_mailbox <who> soft|strict`, `<who>` a slug passing
  `check_slug_shape`, read as `build:<slug>`, or a recipient passing `check_mail_recipient`, since
  `check_mail_addressed` checks neither argument's form (KICK-dKeptSession-28 S4); any other `<who>`
  exits 2 before any fetch. `resolve_claim_remote`; one bounded fetch of
  `+refs/gov/mail/*:refs/gov/remote/mail/*` with `--prune`, then `add_feed_sightings refs/gov/remote/`,
  every landed caller's prefix (`tools/lib/gov-feed.sh#derive_feed_events`); one `git log --first-parent --source` over every cached
  mail ref, none run where none is cached, since `git log` given no revision walks HEAD
  (KICK-dKeptSession-22 S3), its `key: value` lines split in one `awk` by `CLAIM_KV_AWK`'s `read_kv`
  in its strict form (`tools/unattended/unattended.sh#CLAIM_KV_AWK`). It prints one
  TAB-separated row per message whose `to` passes `check_mail_addressed <to> <who>`
  (KICK-dKeptSession-28): `id`, `kind`, `to`, `state`, `first-seen`, `from-build`, `subject`, `answers`,
  `ref`, `commit`, `reply`. `ref` is the remote ref name; `first-seen` is `read_first_seen`
  (`tools/lib/gov-feed.sh#read_first_seen`) over `ref` and `commit`, `-` where the feed has not sighted
  it; `reply` is S7's (F8). Rows with one id collapse to the earliest `first-seen`, ties to the lesser
  ref name, so a cross-ref race shows once. The first ten columns are the order the landed
  `tools/unattended/unattended.sh#check_lease_witness` reads by position, so a column only appends.
  The suite's DPR1 AC11 and AC12 arms `export -f` a stub `read_mailbox`, which the driver's own now
  replaces; they keep their observations exporting `check_mail_deadline` alone, the question a mail
  commit to `build:tFix` on the fixture's origin, closed by an `ack` in place of the stub's `expired`. Under `soft` a failed fetch prints one `mail — local copy: <why>`
  line on stderr and reads the cache; under `strict` it exits 2. Observed by AC4, AC5.
- **S7** — The states: a row of kind `answer` or `ack` is `reply` and is never open; any other row is
  `answered` when a cached message of kind `answer` names its id in `answers`, `acked` when one of kind
  `ack` does and none of kind `answer`, and `open` otherwise (F5). Its `reply` column is the id of the
  earliest-sighted message deciding that state, `-` for `open` and `reply` rows. Observed by AC4.
- **S8** — The verbs (I19), dispatched beside `--register` and `--card-ref` in the driver's verb
  `case` through `refuse_waive_unless_preflight --mail`, each with its usage-header row, the
  `#   unattended.sh --mail …` lines the docs leg reads: `--mail post` (S5); `--mail read <who>
  [--open] [--ids]`, the reader under `soft`, `--open` printing only `open` rows and `--ids` their ids
  on one space-separated line or `none`; `--mail ack <slug> <id>`, a post of kind `ack` from `<slug>`
  answering `<id>`, addressed to `build:<from-build>` of that row, its subject the row's and its body
  empty, refused with exit 2 when `<id>` is not a row addressed to `<slug>`. These are the only
  writers of a mail ref; KICK-dKeptSession-25 adds `--mail answer`. Observed by AC4, AC5, AC10.
- **S9** — The transition guard, in `tools/loop/loop_transition.py#write_transition` after the channel
  set is read and before `derive_move`, TOOL-dDeclaredLoop-3's writer steps 1 and 2. `read_mail_rows(root, build)` in the same file runs `[bash, driver, "--mail", "read",
  build]` in `root` with stdin closed, `read_clean_env()` and the bound `MAIL_GUARD_SECONDS`, the
  driver `resolve_kit_dir("unattended", "unattended.sh", KIT) / "unattended.sh"` and the bash
  `resolve_bash(driver)` (`tools/loop/loop_witness.py#resolve_bash`, `None` where none sees it), as `write_card_follow` runs the
  kickoff engine (`tools/loop/loop_transition.py#write_card_follow`); that one read serves the guard
  and the disposal (F9). Open rows raise `MailHeld`, a `TransitionRefused` subclass in the same file,
  which `record` prints as `refused — <slug> · mail open <id> …` and exits 1, writing nothing
  (`tools/loop/loop_transition.py#main`); `claim.py`'s first move catches it as it catches
  `PatchHeld`, printing `claim held — <slug> · mail open <id> …`, exit 1 (F10). Passing, each but the last with
  one `loop: mail · unarmed · <why>` line: `mail — off`; the locator's `LookupError`; a `root` with no
  `.unattended.conf`, whose `RUN_CLAIMS` cannot be on (S11), where nothing is launched; zero rows.
  Raised as `ValueError`, which `record` prints after `loop: unanswered · ` and exits 2 on, as unknown
  and never none: a located driver no bash can see, `mail unknown: no bash that can see <driver>`
  (KICK-dKeptSession-36 S3), a read answering nothing within the bound, and any other read exiting
  non-zero with no row, naming its exit and first line. Only `build:` and `unit:` recipients gate
  (F2), which the `build:<slug>` read selects by construction. Observed by AC5, AC6, AC12.
- **S10** — The disposal: past the guard, the rows of that read whose state is `answered`, `acked`
  or, once KICK-dKeptSession-24 adds it, `expired`, whose id no move of `before`, the writer's
  `read_transitions(build, root)` (`tools/loop/loop_transition.py#read_transitions`), names in its
  `disposed` field, written as the extension field `disposed=<id>+<id>` (I21): `disposed` joins
  `TRANSITION_FIELDS`, is derived, and a `--field disposed` is refused as `composition` is. It is set
  before the `VALUE` check, so the trailer and the log record carry it. Where `log` is selected and the
  build has an anchor, `write_mail_records(root, build, anchor, rows)` writes one `mailbox-message`
  record per disposed id after this move's record and before step 6 commits, its paths joining
  `wrote`, so step 4's staged-index refusal never sees them and the one commit stages them beside the
  transition record; a failed commit leaves none behind. Observed by AC6.
- **S11** — The switch and the stand-in. Every mail write runs only while `RUN_CLAIMS` is `on`, and otherwise prints `mail — off` and writes nothing: exit 2 for a post
  and an ack, exit 0 for a read, which prints no row. The verbs write through `write_gov_ref`
  until dTotalRecall's record door lands, its `[[door]]` row in `tools/playbook/doors.toml` reading
  `pending = "dTotalRecall"`, the hand-over marked at `write_mail_ref` (F4). Observed by AC7.
- **S12** — The record kind `record-kind.mailbox-message`: a `KINDS` row
  (`tools/memory-tree/build_records.py#KINDS`) requiring `Id`,
  `From`, `To`, `Kind`, `Subject`, `Answers`, `State`, `Reply` and `Ref`, with no closed field, and its
  member in `TYPED_RECORD_KINDS` (`tools/memory-tree/tree_lib.py#TYPED_RECORD_KINDS`) in the same
  commit, since the factory refuses its own import when the two differ (KICK-dKeptSession-39 §8 F1).
  `write_record` writes `<date>-build-<anchor id>-mailbox-message-<n>.md`, its own `**Serves:**
  mailbox-message <anchor id>` line, the body one `~~~~` fenced block in `lines`, as `card`'s text is. `read_mailbox_message(path, text)`, beside `read_card`, is the
  reader `build_records.py read` dispatches to: a missing field, or no single fenced block, is
  malformed. The anchor is
  `resolve_build_anchor` (TOOL-dDeclaredLoop-3 §8 F2). Observed by AC6, AC11.
- **S13** — The card's `mail —` line (I11): `render_mail_line <slug>` in
  `skills/session-kickoff/manifest-check.sh`, called by `render_pointers` (KICK-dKeptSession-13 S2)
  after the `budget —` line (KICK-dKeptSession-26 S1), `mail` appended to `POINTER_LINES`. It runs
  `run_driver_bounded "$CARD_CLAIMS_BOUND" <out> <err> --mail read <slug> --open --ids`
  (`skills/session-kickoff/manifest-check.sh#run_driver_bounded`), printing `mail — <id> <id> …`, `mail — none`, `mail — skipped: RUN_CLAIMS is off` on the
  read's `mail — off`, or `mail — skipped: <why>` for an unresolved driver, a non-zero exit or the
  bound passed. The plants `mail-open`, `mail-none` and `mail-off` join
  `skills/session-kickoff/card-store.fixture.sh`'s `PLANTS`, each pushing its message commit, and
  `mail-none` its `ack`, straight to the fixture's bare remote, never posted, since its stub
  playbook kit holds no `render_playbook.py` for `resolve_fleet_tag`. Observed by AC8.
- **S14** — The documentation. The verbs guide `tools/unattended/VERBS.template.md` gains the `--mail`
  entry: the three verbs, the ref, the kinds, the four recipient
  forms (KICK-dKeptSession-28 S1), the id's eight fields in order
  (KICK-dKeptSession-22 S2, -31 S1), the record, the states, the row's columns and
  the exit codes, rendered to `memory/guides/UNATTENDED-VERBS.md`. `help/loop.md` gains the guard and
  the disposal under "Recording a build's move", and beside `--register`'s paragraph under "Claim keys"
  the `--mail` one, naming the four recipient forms and carrying the `verb:unattended.sh:--mail`
  usage anchor with the fingerprint `python tools/govkit/docs_leg.py --fingerprints` prints.
  `help/orientation-card.md`'s pointers section (KICK-dKeptSession-13 S10) gains the `mail —` line.
  Observed by AC10.

## 3. Non-goals (OUT)

- No deadline: KICK-dKeptSession-24's `check_mail_deadline` and the `expired` state S10 disposes.
- No `answer` verb or answering role: KICK-dKeptSession-25.
- No `seq`, `after` or `content-key`: KICK-dKeptSession-27's.
- No notice at items or tool calls, and no fetch stamp: KICK-dKeptSession-21 and -10.
- No live ring: KICK-dKeptSession-6.
- No bash resolver of its own: KICK-dKeptSession-36's. No refusal of a non-zero read with rows:
  KICK-dKeptSession-44's.
- No `[[record-version]]` row: no loop item returns or reads the kind, so
  `tools/loop/loop_items.py#check_record_versions` owes none.
- No prune of a closed build's mailbox, nor a copy of its open messages: the close program's.
- No secret scan of a body: dWellOiledMachine's (gap-rt-44).
- No record door: dTotalRecall's.

### Edges

- **consumes-from** `KICK-dKeptSession-13` — `## pointers`, the card section whose `mail —` line S13 writes
- **consumes-from** `KICK-dKeptSession-28` — `check_mail_recipient`, the post's recipient check, and `check_mail_addressed`, the reader's row filter
- **consumes-from** `KICK-dKeptSession-22` — `derive_message_id` and `check_mail_duplicate`, the id and the retry refusal
- **hands-off** `KICK-dKeptSession-23` — `read_mailbox` and `write_mail_ref`, whose landed writes the feed records
- **hands-off** `KICK-dKeptSession-27` — `read_mailbox`, whose row and record that unit extends
- **hands-off** `KICK-dKeptSession-24` — `read_mailbox`, whose rows that unit judges against `flow.wait-ceiling` and marks `expired`
- **hands-off** `KICK-dKeptSession-10` — `read_mailbox`, which arms the engine's mailbox interrupt
- **hands-off** `KICK-dKeptSession-25` — `read_mailbox`, whose `question` rows that unit answers through `--mail answer`
- **hands-off** `KICK-dKeptSession-21` — `read_mailbox`, whose unread ids the notice lists
- **hands-off** `KICK-dKeptSession-6` — `read_mailbox` and the post's tail, where the live ring rings after the write
- **hands-off** `KICK-dKeptSession-7` — `read_mailbox`, which carries the dependency notices
- **consumes-from** external — dPlacedRequest, landed: the gov ref writer pair, `derive_ref_segment`, the `RUN_CLAIMS` rule, the register, the feed, `resolve_fleet_tag` and `check_lease_witness`
- **consumes-from** external — dDeclaredLoop, landed: TOOL-dDeclaredLoop-1's `loop.toml` and `loop_lib.py`, and -3's `write_transition`, `TRANSITION_FIELDS` and `read_transitions`
- **hands-off** external — dTotalRecall's record door, the verbs' writer once it lands
- **hands-off** `KICK-dKeptSession-31` — `--mail post`'s eight-argument id call (id 54)
- **hands-off** `KICK-dKeptSession-36` — S9's launch through `resolve_bash` and its missing-shell refusal (id 22)
- **hands-off** `KICK-dKeptSession-39` — S12's factory row, whose hygiene-guide entry that unit writes (id 32)
- **hands-off** `KICK-dKeptSession-42` — `write_transition`'s guard and `--mail ack`, which acknowledge a dependent's notices (id 55)
- **hands-off** `KICK-dKeptSession-44` — `--mail post`'s kinds and fetch and the guard's non-zero read, the batch's S28 to S30 (ids 56, 59, 60)
- **hands-off** `KICK-dKeptSession-56` — S12's factory row, landed in this unit's pass, naming `build-index selftest` (id 11)
- **hands-off** `KICK-dKeptSession-62` — `--mail ack`, `write_mail_ref` and S9's guard read, the batch's S14 and S15 (ids 15, 32)
- **hands-off** `KICK-dKeptSession-63` — `read_mailbox`'s modes, `write_mail_ref`'s signature and `--mail ack`, the batch's S11, S12 and S15 (ids 14, 15, 25)
- **hands-off** `KICK-dKeptSession-64` — S5's exits, S7's `acked` state and S8's `--mail ack`, the batch's S1 to S3 (ids 4, 15, 19)
- **hands-off** `KICK-dKeptSession-65` — S6's strict fetch and rows, S7's precedence and S8's addressed-to check, read by the batch's S1, S2 and S12 (ids 1, 11, 21, 20)

## 4. Design

### Evidence

- No mail code exists: `git grep -n "refs/gov/mail" -- tools skills` finds only the census's planted
  push and the lease arms' `read_mailbox` stubs, which a process run of the driver loses to its own.
- An extension field's value matches `tools/loop/loop_transition.py#VALUE`, so I21 joins ids by `+`.
- `write_record` refuses a field value holding a CR or an LF or opening `**<Word>:**`, and any line
  after the fields that reads as a field (`tools/memory-tree/build_records.py#write_record`), so a
  body the post admitted could otherwise make its own disposal refuse every later transition.
- The sightings walk stops at the first commit not authored `gov-claim`
  (`tools/lib/gov-feed.sh#add_feed_sightings`); S2's commits carry that identity, so the observer clock
  sees every message.
- Probed 2026-11-21: `check_slug` prints a `check 1 FAILED` line on stdout and sets `status`
  (`tools/unattended/unattended.sh#fail`); the driver exits 2 in a root with no `.unattended.conf`
  (`#load_driver_conf`), as every transition plant's root does; `--fleet-tag` answered `d` here and `a` under `GOV_NODE=a`. The
  lander mints kit versions, so a branch owes no bump (`tools/push-main.sh`).

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

Does the ref segment stay one component?
```

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `--mail` | verb, with `post`, `read` and `ack` | none |
| `derive_mail_ref`, `write_mail_ref`, `build_gov_message`, `read_mailbox`; `render_mail_line` | shell functions, the driver; `manifest-check.sh` | `sh.function`, OK |
| `read_mail_kinds` (and `--mail-kinds`); `read_mail_rows`, `write_mail_records`; `read_mailbox_message` | Python, `loop_lib.py`; `loop_transition.py`; `build_records.py` | `py.function`, OK |
| `disposed`; `MAIL_GUARD_SECONDS`, `MailHeld`; `mailbox-message`; `reply` | `TRANSITION_FIELDS` member; constant and class, `loop_transition.py`; `KINDS` row and tuple member; S6's eleventh column | `MailHeld` `py.type`, OK; else none |
| `mail-kinds-repeated`; `mail-open`, `mail-disposed`; `mail-held`; `mail-open`, `mail-none`, `mail-off` | plants: `loop_lib.py`; `loop_transition.py`; `claim.py`; the card store | none |
| `refs/gov/mail/`, `refs/gov/remote/mail/` | ref namespaces | none |

`MAIL_GUARD_SECONDS` is 30 (PINNED), twice `CARD_CLAIMS_BOUND`'s 15
(`skills/session-kickoff/manifest-check.sh#CARD_CLAIMS_BOUND`): the guard fetches every build's mail
refs, the card's claims read two namespaces.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: the ref, writer, builder, post, reader, verbs, usage rows and
  switch, and `write_register`'s call
- `tools/unattended/unattended.test.sh`: the arm §7 declares, and S6's two lease arms re-planted
- `tools/unattended/VERBS.template.md`: the `--mail` entry
- `memory/guides/UNATTENDED-VERBS.md`: its render
- `tools/loop/loop.toml`: the `[mail]` table
- `tools/loop/loop_lib.py`: `read_mail_kinds`, the grade, `--mail-kinds` and its plant
- `tools/loop/loop_transition.py`: the guard, `MailHeld`, the disposal, `disposed`, the bound and plants
- `tools/loop/claim.py`: the `MailHeld` arm and the `mail-held` plant
- `tools/run-gates/selftest-budgets.txt`: the `plants=<n>` token
  `tools/run-gates/run-selftests.sh#check_plant_tokens` grades, each row re-priced by direct CLI:
  `loop transition record` 13 to 15, `loop definition fixtures` 55 to 56, `loop claim fixtures` 14
  to 15 (DERIVED: each module's `len(PLANTS)`, read 2026-11-21)
- `tools/memory-tree/build_records.py`: the `mailbox-message` row and `read_mailbox_message`
- `tools/memory-tree/tree_lib.py`: the `TYPED_RECORD_KINDS` member
- `skills/session-kickoff/manifest-check.sh`: `render_mail_line` and the `POINTER_LINES` word
- `memory/guides/SESSION-KICKOFF.md`: `last-audit` re-stamped, `watch:` naming `manifest-check.sh`
- `skills/session-kickoff/manifest-check.test.sh`: the arm §7 declares
- `skills/session-kickoff/card-store.fixture.sh`: S13's plants
- `help/loop.md`: the guard, the disposal and the `--mail` paragraph
- `help/orientation-card.md`: the `mail —` line
- `memory/map/generated/symbols.json`: the functions minted, by `gen_map.py --write`

### Alternatives rejected

- **One ref per build.** Eight writers took 4.5 times the ideal compare-and-swap attempts, against 1.0
  with one ref per sender (gap-conc-04).
- **The kinds in the driver.** coordination item 6 puts the closed set in the loop definition.

## 5. Production-readiness checklist

- security — a new write surface on the shared remote, only through `write_gov_ref`, dark behind
  `RUN_CLAIMS`; every field validated once at the write (S4, S5, F7); a session writes its own ref.
- perf / scale — a post: one fetch and one push; a read: one fetch and one `git log`; a move: one read.
- error / empty / loading states — S1 to S5 refuse before a commit; `soft` reads a named local copy;
  S9 names an unarmed or unrunnable guard.
- observability — every outcome is one `mail —` line; a refused transition names every open id.
- risks — an unanswered message holds its recipient's transitions until KICK-dKeptSession-24's
  deadline; no mail ref is pruned before the close program.
- testing — §6 and the arms in §7.
- migration — none: all three are new.
- user docs — the verbs guide, `help/loop.md` and `help/orientation-card.md`, S14.

## 6. Acceptance criteria

The fixture: a bare remote and two clones under `%TEMP%`, `RUN_CLAIMS` on, each session its own
`CLAUDE_CODE_SESSION_ID`, clone A under `GOV_NODE=a` and B under `b`, the loop kit installed.

- **AC1** — When clone A's session `s1` posts two messages from `fx` and session `s2` posts one, the
  remote holds `refs/gov/mail/fx/a/s1` with a first-parent chain of two commits (PINNED, the
  fixture's), the first parentless, and `refs/gov/mail/fx/a/s2` with one, each commit's subject
  `gov-mail fx/<id>`.
  Red when: two sessions share a ref, or a second post is not parented on the first.
- **AC2** — When a post names `--kind chat`, it exits 2 naming the closed set, the remote gaining no
  ref; `python tools/loop/loop_lib.py --mail-kinds` prints the twelve kinds; and
  `python tools/loop/loop_lib.py --fixture --plant mail-kinds-repeated` exits 1 naming the repeated kind.
  Red when: an unlisted kind reaches the remote, or a repeated kind reads.
- **AC3** — When `build_gov_message` is given a body of 4097 bytes (PINNED, one over the cap), one
  carrying a NUL, or a value with a newline, it returns 2; and `--register problem`'s record over a
  fixed input is byte-equal to the base driver's.
  Red when: a bad body or value is built, or the register's bytes change.
- **AC4** — When clone B's `fy` posts a `question` to `build:fx` and clone A runs
  `unattended.sh --mail read fx`, one row prints with `state` `open` and `reply` `-`; after A runs
  `--mail ack fx <id>`, the row reads `acked` with `reply` the ack's id, and the `ack` row itself,
  addressed to `build:fy`, reads `reply` there.
  Red when: an acknowledged message reads `open`, or an `ack` reads `open`.
- **AC5** — When one id is planted on two of `fy`'s session refs, `--mail read fx` prints it once,
  with the earlier `first-seen`; and with the remote unreachable, `--mail read fx` prints
  `mail — local copy` and the cached rows, exit 0.
  Red when: a duplicate shows twice, or a failed fetch reads as an empty mailbox.
- **AC6** — The `mail-` plants write the driver's conf, `RUN_CLAIMS` on, and a bare remote, as
  `tools/loop/placement.py`'s `write_placement_fixture` does, pushing the `question` and `ack`. When
  `python tools/loop/loop_transition.py --fixture --plant mail-open` runs, the move over the unanswered
  `question` exits 1 printing `refused — ` and `mail open <id>`, no commit; `--plant mail-disposed`, after the
  `ack`, writes in one transition commit a trailer and a log record carrying `disposed=<id>` and one
  `<date>-build-<anchor>-mailbox-message-1.md` with `**Serves:** mailbox-message <anchor>` and
  `**State:** acked`, which `python tools/memory-tree/build_records.py read <path>` reads with exit 0;
  the next move disposes nothing.
  Red when: a transition records over an open message, as a planted guard reading no mail shows, or
  a disposed id is disposed twice.
- **AC7** — When `RUN_CLAIMS` is off in the clone's conf, `--mail post …` prints `mail — off`, exits 2
  and the remote gains no ref, and the transition passes with one `loop: mail · unarmed` line.
  Red when: a mail ref is written with the switch off, or the guard refuses on an unarmed mailbox.
- **AC8** — When `bash skills/session-kickoff/card-store.fixture.sh --plant mail-open` runs, the card's
  `## pointers` section carries `mail — <id>`; `--plant mail-none` carries `mail — none` after the
  `ack`; and `--plant mail-off` carries `mail — skipped: RUN_CLAIMS is off`, each printing `held`.
  Red when: the card shows `mail — none` while a message is open.
- **AC9** — When the post runs with `CLAUDE_CODE_SESSION_ID` unset it prints `mail — not written: no
  session id`, exit 2; and `grep -n "refs/gov/mail/" tools/unattended/unattended.sh` finds the
  namespace, outside comment lines, on `derive_mail_ref`'s line and the two fetch refspecs only.
  Red when: a mail ref is written with no session, or a second site spells the namespace.
- **AC10** — When `grep -n -- "--mail" tools/unattended/VERBS.template.md` runs, the guide names the
  three verbs, the twelve kinds, the four recipient forms, the id's eight fields, the four states and
  the exit codes 0, 1 and 2; `grep -n "mail open" help/loop.md` finds the guard; and
  `python tools/govkit/docs_leg.py --list` shows `verb:unattended.sh:--mail` anchored by `help/loop.md`.
  Red when: the guide omits any of them, or no page anchors the verb.
- **AC11** — When `python tools/memory-tree/build_records.py --fixture --plant typed-kinds` runs, it
  prints `build-records: PASS typed-kinds` with `mailbox-message` among the kinds it wrote and bound.
  Red when: the `KINDS` row lands without its tuple member, and the factory's import refuses.
- **AC12** — When a `python -c` probe rebinds `loop_witness.resolve_bash` to answer `None` and calls
  `read_mail_rows` over a root whose `.unattended.conf` sets `RUN_CLAIMS` on, it raises `ValueError`
  reading `mail unknown: no bash that can see <driver>`; and `python tools/loop/claim.py --fixture
  --plant mail-held`, a `question` to `build:<slug>` pushed to its bare remote before the claim,
  prints `claim held — <slug> · mail open <id>` and `claim: mail-held · … · held`.
  Red when: a driver no bash sees reads as absent, or a held claim names a missing row.

## 7. Gates

`unattended kit gate` · `manifest-check self-test` · `scratch-guard self-test` · `tier2-review self-test` · `policy fixtures` · `loop definition` · `loop definition fixtures` · `loop transition record` · `loop claim fixtures` · `loop item kind` · `memory-hygiene self-test` · `build-index selftest` · `docs` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC5 AC7 AC9 · each criterion's case, staged against the base driver, which has no mail verb · the effective `FLOOR_ASSERTIONS` and its region's `FLOOR_SHARD_<k>` rise by its counted assertions
New arm: tools/loop/loop_transition.py · covers AC6 · the `mail-open` and `mail-disposed` plants, staged by a planted guard reading no mail · the `loop transition record` row's `plants=<n>` token rises by two
New arm: tools/loop/loop_lib.py · covers AC2 · the `mail-kinds-repeated` plant, staged against a `check_loop` that grades no `[mail]` table · the `loop definition fixtures` row's `plants=<n>` token rises by one
New arm: tools/loop/claim.py · covers AC12 · the `mail-held` plant, staged by a claim whose `TransitionRefused` arm names a row miss · the `loop claim fixtures` row's `plants=<n>` token rises by one
New arm: skills/session-kickoff/manifest-check.test.sh · covers AC8 · the three card-store plants, staged by a pointers writer omitting the `mail —` line · `FLOOR_ASSERTIONS` rises by the three plants' rows

## 8. Open questions

- **F1 — Whose build names a mail ref?** (a) The sender's, readers selecting by `to`; (b) the
  recipient's. (b) puts a new session's retry outside the duplicate check, and leaves a
  `node:` or `project` message no build. Rung 1, cl-0160's check.
  RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none
- **F2 — Which recipients gate a build's transition?** (a) `build:` and `unit:` recipients of the build;
  (b) those and every `node:` and `project` message. (b) lets one broadcast hold every build. Rung 1,
  the clause's "a message addressed to the build". RESOLVED (agent, 2026-10-26,
  delegated): (a). widens: none · relaxes: none
- **F3 — What does the guard read when the fetch fails?** (a) The local copy, named; (b) refuse the
  transition. (b) stops every offline build, against P40's "alone and offline". Rung 3. RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none
- **F4 — How is the record door's stand-in registered?** (a) Marked at `write_mail_ref`, the one
  writer, with the hand-over named in §3; (b) a `[[stand-in]]` row, red under TOOL-dDeclaredLoop-13 S8,
  which admits only a transition-table item. Rung 3. RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none
- **F5 — Does a reply need a reply?** (a) `answer` and `ack` read `reply` and never gate; (b) every
  kind gates until answered. (b) makes each `ack` hold the asker until acknowledged, so no exchange
  ends, against P39's "every loop ends". Rung 3. RESOLVED (agent, 2026-10-26,
  delegated): (a). widens: none · relaxes: none
- **F6 — Is the mailbox dark?** (a) Behind `RUN_CLAIMS`, the coordination switch every gov ref write
  already reads; (b) always on. (b) is an unswitched write path on the shared remote, against the
  charter's small rule. Rung 3, TOOL-dPlacedRequest-12 §8 F3's answer.
  RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none
- **F7 — Where is a body that the record factory would refuse stopped?** Options: (a) at the post,
  exit 2, each body line and value held to `write_record`'s field shapes, the `~~~~` line refused;
  (b) escaped into the record at disposal, the folder's copy differing from the ref's; (c) nowhere,
  one message refusing every later transition of its recipient. RESOLVED (agent, 2026-11-21, delegated): (a), rung 3; the
  write boundary validates once and the record stays the message's bytes. widens: none · relaxes: none
- **F8 — Where does the record's `Reply` come from?** Options: (a) an eleventh `reply` column of S6's
  row, after `commit`; (b) drop the `Reply` field. The reader selects by `to`, so a reply is never a
  row of the recipient's read; (a) keeps `check_lease_witness`'s ten columns. RESOLVED (agent, 2026-11-21, delegated): (a), rung 3; the state's own derivation
  already finds that message, and (b) loses which answer closed the question. widens: none · relaxes:
  none
- **F9 — How many reads does a transition make?** Options: (a) one `--mail read <slug>`, its `open`
  rows refusing and its `answered` and `acked` rows disposed; (b) an `--open` read, then a second fetch for
  the disposal, a reply landing between them splitting the two judgments. RESOLVED (agent, 2026-11-21, delegated): (a), rung 3;
  one snapshot decides both. widens: none · relaxes: none
- **F10 — How does a claim report the guard?** `tools/loop/claim.py#write_first_transition` reads a
  `TransitionRefused` as a row miss. Options: (a) a `MailHeld` subclass it catches first; (b) one
  arm reworded for both; (c) none. RESOLVED (agent, 2026-11-21, delegated): (a), rung 3; `PatchHeld`'s
  shape, where (c) names a missing row. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft. The govkit subject pins are not among the files touched:
  `selfcheck` derives their rows from the gate-legs manifest alone, one per leg, and this unit adds
  no leg, so no row moves.
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-31`, `KICK-dKeptSession-36`,
  `KICK-dKeptSession-39`, `KICK-dKeptSession-42`, `KICK-dKeptSession-44` mirrored from the round-1
  spec audit's promoted units; no other section moved.
- rev-3 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-56` mirrored
  from the round-1 promotions' audit's disposal
- rev-4 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-62` mirrored
  from the round-2 promotions' audit's disposal
- rev-5 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-63` mirrored
  from the round-3 promotions' audit's disposal
- rev-6 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-64` mirrored
  from the round-4 minors batch's audit's disposal
- rev-7 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-65` mirrored
  from the round-5 minors batch's audit's disposal
- rev-8 · 2026-10-26 · §2 S10, S12 · §4 The transition, in order · §6 AC6 · re-grounded on
  dDeclaredLoop at `783f1ad3a` by the cross-check record
  `build/2026-10-26-build-KICK-dKeptSession-1-parents-crosscheck.md`, rows 13 and 16: the
  `mailbox-message` records are written at step 5a, after TOOL-dDeclaredLoop-3's staged-index
  refusal, and serve as `mailbox-message`, never `journal`, by reference to `KICK-dKeptSession-39`.
- rev-9 · 2026-11-21 · §2 S1 to S14 · §3 · §4 · §5 · §6 AC1 to AC11 · §7 · §8 F7 F8 F9 · §10 ·
  re-grounded on base c2a407b0 by brief 2026-11-21-prompt-KICK-dKeptSession-5-orders-16-17-reground-brief:
  line citations re-cited by symbol to the landed gov-ref, feed, driver, loop and factory code; S2
  and S5 follow `write_card_ref`, S9 launches through the inline `resolve_bash`, S12 carries the
  tuple member the factory's import demands and `read_mailbox_message`, S13 reads through
  `run_driver_bounded`, S14 adds the docs anchor and the card page. Folded from the re-grounded KICK-dKeptSession-22, -28 and -31: S5 writes the
  eight-argument id call itself, S6 checks its `<who>`, S14 and AC10 state the four recipient forms
  and the eight id fields; from -36 and -24, S9's no-bash line and S5 and S6's sightings prefix
  `refs/gov/remote/`. Narrowed: the factory's Serves line and file-name join are landed and dropped from
  this unit's work. Forks F7 to F9 ruled; `tier2-review self-test`, `policy fixtures`, the loop
  legs, `docs`, `memory-hygiene self-test` and `build-index selftest` joined the leg line.
- rev-10 · 2026-11-21 · S1 · S5 · S6 · S9 · S10 · S12 · S13 · §3 · §4 · §6 · §7 · §8 · §10 · checked
  for behaviour under `2026-11-21-prompt-KICK-dKeptSession-22-precheck-brief`: slugs held to the
  silent `check_slug_shape`; S6 runs no log over no ref and re-plants the lease arms' stubs; S9 passes a conf-less root and refuses any
  other non-zero read with no row; plants push straight to their remotes; the fixture pins
  `GOV_NODE`; the lander's version bump and the `v2` cite dropped; `symbols.json` added; two floors
  named; the transition table S9 and S10 restate dropped, and prose tightened, under the size cap.
- rev-11 · 2026-11-21 · S9 · §4 · AC6 · AC12 · §7 · §8 F10 · checked for behaviour under
  `2026-11-21-prompt-KICK-dKeptSession-24-precheck-brief`: S9's unknown cases print `loop: unanswered`,
  exit 2, and only `MailHeld` prints `refused —`, exit 1, `claim.py` reporting it held (F10); three
  `plants=<n>` rows, AC12 and `loop claim fixtures` added; prose cut under the size cap.

## 10. Reuse audit

The seams extended are the gov ref writer pair `build_gov_commit` and `write_gov_ref`
(`tools/lib/gov-ref.sh#write_gov_ref`), called as `write_card_ref` calls them
(`tools/unattended/unattended.sh#write_card_ref`); `write_register`'s record, whose builder this unit
extracts at its second instance (`tools/unattended/unattended.sh#write_register`); `CLAIM_KV_AWK`,
`add_feed_sightings` and `read_first_seen`; `read_dispositions` (`tools/loop/loop_lib.py#read_dispositions`),
which `read_mail_kinds` mirrors; `write_card_follow`'s sibling-kit launch; the factory's `KINDS` and
`TYPED_RECORD_KINDS`; and `run_driver_bounded`. `python tools/codebase-map/reuse_lookup.py "append a
message commit to a per-session ref by compare-and-swap and read every message"` ranked name stems,
`read_clean_env`, S9's launch environment, among them; it ranks none of the driver's shell seams,
found by reading the driver.

Recall terms used: mailbox per-session ref refs/gov/mail append-only transition refused unanswered
acknowledged disposed write_gov_ref write_card_ref read_dispositions
