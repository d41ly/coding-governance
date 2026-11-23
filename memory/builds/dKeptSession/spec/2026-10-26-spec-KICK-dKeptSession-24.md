# KICK-dKeptSession-24 — a mail deadline judged by the observer clock: `flow.wait-ceiling` declared on each message, the asker's default past it

**Status:** CLOSED · rev-6 · 2026-11-23 · node a · Tier-2 · base 8b8b1374 · streams kickoff · order 19 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0162@6ce67958 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md) | research | KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-10 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-25 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-1 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-11-21-build-KICK-dKeptSession-24-1-acceptance-ledger.md](../build/2026-11-21-build-KICK-dKeptSession-24-1-acceptance-ledger.md) | journal | — |
| [2026-11-21-build-KICK-dKeptSession-45-reground-orders-14-19-returns.md](../build/2026-11-21-build-KICK-dKeptSession-45-reground-orders-14-19-returns.md) | research | KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-36 KICK-dKeptSession-27 KICK-dKeptSession-1 |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-24-1-spec-writer.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-24-1-spec-writer.md) | journal | — |
| [2026-11-21-prompt-KICK-dKeptSession-24-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-24-build-brief.md) | research | — |
| [2026-11-21-prompt-KICK-dKeptSession-24-precheck-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-24-precheck-brief.md) | research | KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-5 |
| [2026-11-21-prompt-KICK-dKeptSession-36-orders-17-19-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-36-orders-17-19-reground-brief.md) | research | KICK-dKeptSession-36 KICK-dKeptSession-27 |
| [2026-11-22-prompt-KICK-dKeptSession-24-reground-brief.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-24-reground-brief.md) | research | — |
| [2026-11-23-prompt-KICK-dKeptSession-24-1-spec-writer.md](../prompts/2026-11-23-prompt-KICK-dKeptSession-24-1-spec-writer.md) | journal | — |
| [2026-11-23-prompt-KICK-dKeptSession-24-2-spec-writer.md](../prompts/2026-11-23-prompt-KICK-dKeptSession-24-2-spec-writer.md) | journal | — |
| [2026-11-23-prompt-KICK-dKeptSession-24-divergence-brief.md](../prompts/2026-11-23-prompt-KICK-dKeptSession-24-divergence-brief.md) | research | — |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-27 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |
| [2026-11-23-review-KICK-dKeptSession-69-closing-diff-review-round1.md](../reviews/2026-11-23-review-KICK-dKeptSession-69-closing-diff-review-round1.md) | diff-review | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 KICK-dKeptSession-67 KICK-dKeptSession-69 |

<!-- /gen:spec-records -->

## 1. Goal

Every mail message carries the deadline its asker declared, `flow.wait-ceiling` in hours, and a
default answer; a node judges that deadline by the time it first saw the message on its own clock,
the declared clock dPlacedRequest's leases use, never by its clock minus the sender's stamp. Past the
deadline the message reads `expired`, the asker's default answers it, and the recipient build's
transitions go on (P39, the whole-design audit's A2-F6). Without this, a question nobody answers
blocks the recipient for ever, and a reader whose clock runs a day ahead expires every message a day
early, gap-conc-14's class, which TOOL-dPlacedRequest-17 S3 closed for leases in
`tools/unattended/unattended.sh#read_claims` and which the landed mailbox does not meet: its reader
names a deadline as what it does not check (`tools/unattended/unattended.sh#read_mailbox`).

## 2. Scope (IN)

- **S1** — The declared deadline. `tools/unattended/unattended.sh#write_mail_post`, the `--mail post`
  verb `KICK-dKeptSession-5` landed, writes the key `deadline: <hours>` into every record it builds,
  after unit 5's ten keys and the keys `KICK-dKeptSession-27` appends, the hours `flow.wait-ceiling`
  reads at the post. It reads them through `read_lease_policy flow.wait-ceiling`, a new arm of
  `tools/unattended/unattended.sh#read_lease_policy` (§8 F6): the default `72` beside the other keys'
  defaults, one literal `get flow.wait-ceiling` line in the closed `case` the reader's comment says
  the policy kit's reader coverage counts, the number check its three bounds take, and the key
  joining the NOTE's key list, the refusal's key list and the signature comment. The number refusal
  reads "the non-negative number this driver ages a lease or a message by". The call is direct,
  never in a substitution, as that comment requires, and sits in the post's body-and-values step
  after `check_mail_recipient` and before the fetch; a refused read prints
  `mail — not written · <LP_VALUE>`, exit 2, before any fetch or commit. `get` answers at the landed
  revision, for a read naming no build: the file's value, then the preset the file names, then the
  catalogue default (`tools/policy/policy.py#RESOLUTION_ORDER`). A policy kit that does not resolve
  writes `72` under the reader's one NOTE. `--mail ack` posts through `write_mail_post`
  (`tools/unattended/unattended.sh#write_mail_ack`), so an ack carries one too (§8 F2). Neither key
  joins `derive_message_id`'s eight fields (`tools/unattended/unattended.sh#derive_message_id`), so a
  retried post naming another default is refused as a duplicate, as any retry is. The post's comment
  gains the two keys and the policy read in its order list. Observed by AC1 and AC5.
- **S2** — The declared default. The driver's `--mail` arm parses `--default <text>` beside `--to`
  and the other valued flags, and its texts name it: the header usage line of `--mail post`
  (`tools/unattended/unattended.sh@a11693ddbd88:51`) gains `[--default <text>]`, the unknown-flag
  refusal's list and the form refusal gain `--default`, and the `read` form refuses it as it refuses
  `--to`. `write_mail_post` takes it as its last argument, after any `KICK-dKeptSession-27` appends,
  and writes `default: <text>`: the text where given, on any kind; where absent, a `question` or a
  `confirm-request` is refused `mail — not written · a <kind> declares its default with --default`,
  exit 2, and every other kind writes `default: ack`. That refusal sits after the kind check and
  before `check_mail_recipient`, so the switch, slug, session and fleet-tag refusals unit 5 orders
  before the kind print as they landed. The text is a value pair of
  `tools/unattended/unattended.sh#build_gov_message`, which refuses an empty value or one carrying
  any control byte, tab and newline included, printed `mail — not written · <GOVMSG_WHY>`; no length
  limit beyond the subject's is added. No disposed record carries the default, so the `**<Word>:**`
  check the subject takes does not apply. Unit 5's AC1 posts and its AC4 question in
  `tools/unattended/unattended.test.sh` gain `--default`, so each keeps the row it observes; its AC7
  and AC9 posts refuse before the kind and stay as landed; each `question` or `confirm-request` post
  `KICK-dKeptSession-23` or `KICK-dKeptSession-27` lands gains `--default` too. Observed by AC1.
- **S3** — The judgment, `check_mail_deadline <ref> <commit> <hours>` (I23), in
  `tools/unattended/unattended.sh`, the name `tools/unattended/unattended.sh#check_lease_witness`
  already probes with `declare -F`. It spells `<ref>` as the feed keys it, a leading
  `refs/gov/remote/` re-spelled `refs/gov/`; converts `<hours>` to whole seconds through
  `derive_bound_seconds <number> <multiplier>`, which sets DB_VALUE and prints it, returns 1 on a
  number outside `^[0-9]+(\.[0-9]+)?$`, and holds `read_lease_bound`'s arithmetic, extracted: the
  first six fraction digits kept and the rest of the second dropped. `read_lease_bound` then calls it
  directly with its output unchanged. A return of 1 makes `check_mail_deadline` return 2; else it
  returns the code of `check_deadline_passed <ref> <commit> <seconds>`
  (`tools/unattended/unattended.sh#check_deadline_passed`): 0 passed, 1 not yet, 2 not sighted. The
  comment above `check_deadline_passed` names a mail deadline beside its two callers, and
  `read_lease_bound`'s names the extraction. With the name defined beside `read_mailbox`,
  `check_lease_witness`'s probe `declare -F read_mailbox >/dev/null && declare -F
  check_mail_deadline` can no longer fail in the driver, so this unit deletes it: the mailbox is
  read on every call, and its comment's "where `declare -F` finds both …, inert until it lands"
  clause reads "first the mailbox is read". Every `--lease renew --witness` therefore makes the one
  bounded mail fetch TOOL-dPlacedRequest-1 S8 designed. In the suite it deletes the DPR1 AC11
  assertion that the question exits 2 with the two functions absent
  (`tools/unattended/unattended.test.sh@92da5fb2d5cc:19257`), the `$LF/stubs.sh` stub of
  `check_mail_deadline`, both `. "$LF/stubs.sh"` sources in the AC11 and AC12 arms, and the block
  comment's lines naming the stub and the unlanded deadline (§8 F7). **Readers:** by name:
  `tools/unattended/unattended.sh` and `tools/unattended/unattended.test.sh`, the only files that
  spell the probe and the stub; by value: NO VALUE READERS, since the probe gates a read and stores
  nothing. Observed by AC2, AC3, AC4 and AC7.
- **S4** — The sightings, landed. `read_mailbox` and `write_mail_post` each run
  `add_feed_sightings refs/gov/remote/` after their fetch, the one argument under which the walk
  keys a cached mail ref as `refs/gov/mail/…` (`tools/lib/gov-feed.sh#derive_feed_events`), and
  `tools/unattended/unattended.sh#write_mail_ref` builds every message by `build_gov_commit` under
  the fixed `gov-claim` identity the walk requires. This unit adds no call and changes none. NOT
  OBSERVED here: it is landed code this unit relies on, which `KICK-dKeptSession-23`'s AC5, landing
  at order 17, observes as a fetched message sighted.
- **S5** — The `expired` state. `read_mailbox`'s parse reads `deadline` and `default` through
  `read_kv` under a second key set beside the required one, so a record without them keeps its row
  and reads `-` in each. The row appends the two columns after the three `KICK-dKeptSession-27` S4
  appends after unit 5's `reply`, sixteen in all; the first fourteen keep their places, where
  `check_lease_witness` reads 2, 4 and 10 and `tools/loop/loop_transition.py#read_mail_rows` takes
  the first eleven of any row holding at least eleven. After the state pass, each `open` row is
  judged by `check_mail_deadline` over its own ref, commit and deadline: rc 0 sets its state
  `expired`, its `reply` kept `-`; 1 or 2 keeps it `open`, so an unsighted message never expires
  (§8 F4). The reader's comment names the fifth state, the two columns, and what stays unchecked:
  a clock offset between nodes (§3). `print_mailbox` selects `open` alone under `--open`, so an
  expired row leaves `--open --ids`. The guard of `KICK-dKeptSession-5` holds on `open` rows only, so
  an expired message lets the recipient's transitions go on; `MAIL_DISPOSED_STATES` already holds
  `expired` (`tools/loop/loop_transition.py@2f3a26de0fd2:137`), so the disposal takes the row and
  its record's `State` reads `expired`, no edit there. The texts saying what holds a move read the
  expiry: "neither answered nor acknowledged" in `tools/loop/loop_transition.py#MailHeld`'s docstring
  and the module docstring's guard paragraph reads "neither answered, acknowledged nor past its
  deadline", and "answered or acknowledged" reads "answered, acknowledged or past its deadline" in
  `MailHeld`'s message, the `mail —` bullet (`help/orientation-card.md@09510792d640:148`) and the
  guard paragraph of `tools/loop/claim.py@724ab226e58e:46`'s docstring. An expired question reads
  `question-closed` to `check_lease_witness`, which renews nothing on it. A record with no
  `deadline`, as `seed_mail_at` and `tools/loop/loop_transition.py#render_fixture_mail` plant one,
  judges 2 and stays `open`: the DPR1 lease arms' question still renews and `mail-open` still
  refuses. The three planters that put a message straight on a remote, `seed_mail_at`,
  `render_fixture_mail` and `skills/session-kickoff/card-store.fixture.sh#write_card_mail`, each say
  they write it as `--mail post` records it, which this unit's two keys make false; each comment
  reads "as `KICK-dKeptSession-5`'s post recorded it, with no deadline". No landed arm compares a whole row: unit 5's read columns by `cut -f` and `awk` (PINNED,
  2026-11-23 at `9900b200`); an arm unit 23 or 27 lands that does gains the two columns. The plant
  `mail-expired` of `tools/loop/loop_transition.py#write_transition_plant`: `render_fixture_mail`
  takes optional `deadline` and `default` keys; the plant puts `FX_QUESTION` with `deadline: 30` and
  `default: no` on the fixture's remote as `mail-open` does, reads its commit by `ls-remote`, and
  appends one line for that ref and commit, sighted 31 hours ago, to the fixture's
  `<git-common-dir>/gov-feed.log` in the six-field shape `tools/loop/claim.py#check_claim_plant`'s
  `stale-holder` plant writes. Its branch of `tools/loop/loop_transition.py#run_transition_fixture`
  runs B4 and prints the commit count, the trailer and each mail record's `State`, as `mail-disposed`
  does; `PLANTS` gains the key and `tools/loop/loop_transition.py#run_selftest`'s case table one row
  per line AC2 reads. Observed by AC2, AC3, AC4 and AC8.
- **S6** — The user texts. The `--mail` entry of `tools/unattended/VERBS.template.md`, and its
  byte-equal installed copy `memory/guides/UNATTENDED-VERBS.md` under the unattended kit gate's
  check 10: the usage gains `[--default <text>]`; the record's key list gains `deadline` and
  `default`; the row's column list gains them; "The four states" becomes five, `expired` stated as
  an `open` message this node first saw more than its `deadline` hours ago, by its own clock, its
  `default` the answer; and the transition sentence disposes "each answered, acknowledged or expired
  message". `help/loop.md`: the `--mail` paragraph names `--default` and the two columns, its "A
  message is `open` until …" sentence gaining `expired` as the verbs guide states it, its
  `verb:unattended.sh:--mail` anchor re-stamped with the fingerprint
  `python tools/govkit/docs_leg.py --fingerprints` prints at build time, since `--default` joins the
  flags it hashes (`tools/govkit/docs_leg.py#read_verb_usage`); the guard paragraph under "Recording
  a build's move" reads "neither answered, acknowledged nor past its deadline holds the move" and
  "each answered, acknowledged or expired message"; and the fixture-cases sentence names
  `mail-expired`. `tools/loop/README.md`: the mail guard paragraph's
  `open` row reads "neither answered, acknowledged nor past its deadline", and its plant list names
  `mail-expired`. The module docstring of `tools/loop/loop_transition.py` and its comment above
  `TRANSITION_FIELDS` name the plant and the expiry. Observed by AC6 and AC8.

## 3. Non-goals (OUT)

- No mailbox, record, kind list or transition guard: `KICK-dKeptSession-5`'s. This unit fills two of
  I17's fields and adds one state to I20's rows.
- No observer clock of its own: `read_first_seen`, `check_deadline_passed` and the feed's sightings
  walk are landed, TOOL-dPlacedRequest-17's and TOOL-dPlacedRequest-13's. This unit calls them.
- No answering: who answers a `question`, the `mailbox.answer` item and the lease renewal while a
  build waits are `KICK-dKeptSession-25`'s.
- No written answer on expiry. The default is derived from the message, never posted (§8 F5).
- No default in a disposed record: `write_mail_records`' fields are unit 5's, and the message's
  commit at its `Ref` holds the default.
- No clock offset correction: the second rule of the `leases.expiry-hours` row of v2
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c9:1160`)
  is dWellOiledMachine's supervisor's.
- No `flow.wait-ceiling` row: the catalogue's, landed with owner dDeclaredLoop.

### Edges

- **consumes-from** `KICK-dKeptSession-5` — `read_mailbox`, its rows and states, the `--mail post` writer and I17's `deadline` and `default` fields; without them there is no message to judge
- **hands-off** `KICK-dKeptSession-25` — `check_mail_deadline` and the `expired` state, through which an unattended build's question is answered by the asker's default
- **consumes-from** external — the landed `check_deadline_passed` and `read_first_seen` of TOOL-dPlacedRequest-17, `add_feed_sightings` and `gov-feed.log` of TOOL-dPlacedRequest-13, `build_gov_commit` of TOOL-dPlacedRequest-11, and the `flow.wait-ceiling` row and its reader `policy.py get`

## 4. Design

### Evidence

Read on the run tree at `9900b200`, 2026-11-23, with units 23, 36, 39, 51 and 27 read as landed.

- The mailbox is landed and judges no deadline: `read_mailbox` prints eleven columns, its four states
  `reply`, `answered`, `acked` and `open`, and its record keys are unit 5's ten, none a deadline
  (`tools/unattended/unattended.sh#read_mailbox`, `tools/unattended/unattended.sh#write_mail_post`).
- The lease ages read the first sighting: `read_claims`' age pass feeds its pairs to
  `read_first_seen`, and an offer's deadline and a tombstone's prune age call
  `check_deadline_passed`, which returns 2 on a bound that is not whole seconds.
- The feed keys a sighting by `ref`, `blob` and `commit` and stamps `seen-utc` on this node's clock
  (`tools/lib/gov-feed.sh#add_feed_event`); `read_first_seen` reads a line of six fields
  (`tools/lib/gov-feed.sh#read_first_seen`), and the walk stops at the first commit not authored
  `gov-claim`, so a fixture's message committed by `fx` is sighted only by a planted line.
- `flow.wait-ceiling` is an `hours` row of default 72 with a minimum of 0 (`tools/policy/catalogue.toml`),
  and the reader admits an integer or a fraction for that type (`tools/policy/policy.py#check_value`);
  `python tools/policy/policy.py get flow.wait-ceiling` printed `72` on this tree, 2026-11-23.
  DERIVED: the catalogue row is the owning source; the printed value re-derives from it. The preset
  `strict` sets it to 168 (`tools/policy/presets.toml@28373c5a97a6:634`, PINNED 2026-11-23).
- `get` reads `.governance/policy.toml` at the landed revision, `refs/remotes/<remote>/<branch>`
  (`tools/policy/policy.py#derive_landed_revision`), so a fixture's value reads once committed,
  pushed and fetched, as the suite's `write_lease_policy` does. A file `validate` refuses reads its
  last valid first-parent revision and refuses only where none precedes it
  (`tools/policy/policy.py#read_last_valid_value`), which DPR1 AC17 stages with an unparsable first
  revision after a fresh `write_lease_fixture`.
- The lander mints kit versions, so a branch owes no bump (`tools/push-main.sh@78f40c3c2475:27`).
- A whitespace-folded search for "answered or acknowledged", "answered nor acknowledged" and "is
  `open` until" outside `memory/builds/` at `0e5b281a` found nine statements beside the verbs guide's
  (PINNED, 2026-11-23): one each in `help/orientation-card.md`, `tools/loop/claim.py` and
  `tools/loop/README.md`, three each in `help/loop.md` and `tools/loop/loop_transition.py`.

### The rule

```
deadline(message) = the asker's flow.wait-ceiling, in hours, written at the post
age(message)      = now(this node) - seen-utc(this node's first sighting of the message commit)
expired           = state would be open  and  age > deadline × 3600
```

The asker's node sights its own question at the write and the recipient's node at its first fetch,
so each side judges the same declared deadline on its own clock, and a constant skew cancels on each.
A message no answer and no acknowledgement disposes stays `open` until then and reads `expired`
after; an answered or acknowledged one keeps the state unit 5's reader gives it.

### The post's two keys

```
deadline: 72
default: no
```

`deadline` is the number the policy read returned; `default` is `--default`'s text, or `ack` for a
kind that only needs acknowledging (`changed`, `landed`, `overlap`, `takeover`, `intake`, `withdrawn`,
`superseded`, `answer`, `ack`, `confirmed`). The two kinds that ask for content, `question` and
`confirm-request`, must declare theirs.

### The read

1. `read_mailbox`'s bounded fetch, then `add_feed_sightings refs/gov/remote/`, both landed.
2. Its parse yields each message's `ref`, `commit`, `state`, `deadline` and `default`.
3. For each `open` row, `check_mail_deadline <ref> <commit> <deadline>`; rc 0 sets `expired`.
   The cost is linear in open messages (§5), which the guard keeps few.

### Shipped texts

| Text | Clause |
|---|---|
| `tools/unattended/unattended.sh`: the usage line, the `--mail` refusals, and the comments of `write_mail_post`, `read_mailbox`, `read_lease_policy`, `read_lease_bound`, `check_deadline_passed` and `check_lease_witness` | S1, S2, S3, S5 |
| `tools/unattended/unattended.test.sh`: the DPR1 AC11 block comment naming the stub | S3 |
| `tools/unattended/VERBS.template.md`, `memory/guides/UNATTENDED-VERBS.md`, `tools/loop/README.md` | S6 |
| `help/loop.md`: the `--mail` paragraph's open-until sentence, the guard paragraph's holds-the-move and disposal sentences, the fixture-cases sentence | S6 |
| `tools/loop/loop_transition.py`: its docstring, its plant comment, `MailHeld`'s docstring and message | S5, S6 |
| `help/orientation-card.md`: the `mail —` bullet's holds-the-moves sentence | S5 |
| `tools/loop/claim.py`: the module docstring's KICK-dKeptSession-5 guard paragraph | S5 |
| the comments of `seed_mail_at`, `render_fixture_mail` and `write_card_mail` | S5 |

These stay true and are left as they are. `tools/unattended/STOPS.template.md`'s lease-key table
lists the keys that shape a lease, which `flow.wait-ceiling` does not. Its sentence calling an
offer's deadline and a tombstone's prune age "the same judgment" denies no third caller. The
`--lease` entry's "a witness that … is no open question" holds, since an expired question is not
open. `help/reference/policy.md` and the catalogue row are unchanged, and the row carries no summary,
so `.governance/policy.json` does not move. `help/loop.md`'s loop-wait `deadline =
"policy.flow.wait-ceiling"` and the `--entry-claim` ceiling text govern a wait and a claim, never a
message. The key already has readers in `tools/loop/claim.py` and `tools/loop/termination.py`, so
the policy kit's reader coverage moves by nothing a gate reads. `help/loop.md`'s "so answer or acknowledge
each" and "While a message addressed to a build is open, that build's moves are refused" stay true,
as does the card bullet's "names each open message": an expired message is not open.

### The refusal ceiling

`tools/unattended/unattended.sh` sits at its ceiling, 347 sites (PINNED,
`.memory-tree.conf@d4f8d497b8c3:661`, 2026-11-23). The census counts a `fail <n> "` call, an `exit 1`
word and a `status=1` assignment (`tools/memory-tree/check-arms.py@60d9015821da:157`). This unit adds
none: every refusal it adds is `echo …; return 2` inside a function or `_rl_rc=2` in the `--mail`
arm, and the probe it deletes is no site. The ceiling is met unraised.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `check_mail_deadline` | shell function | `check`, OK |
| `derive_bound_seconds` | shell function | `derive`, OK |
| `--default` | flag of `--mail post` | none |
| `deadline`, `default` | record keys and `read_mailbox` columns | none |
| `expired` | a state of I20's rows | none |
| `mail-expired` | plant of `loop_transition.py --fixture` | none |

### Migration

None: a message posted before this unit carries no `deadline` and stays `open`, as S5 reads it.

### Rollout

Behind `RUN_CLAIMS`, as every mail write and read is (I16). A build with no open message sees no
change.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: `check_mail_deadline`, `derive_bound_seconds` and
  `read_lease_bound`'s call of it, `read_lease_policy`'s new arm, the post's two keys and
  `--default`, the `expired` state and its two columns, `check_lease_witness`'s probe deleted, and
  the texts §4's table names
- `tools/unattended/unattended.test.sh`: the arm of §7; `--default` on the earlier question posts;
  DPR1 AC11's absent-functions assertion, the stub and its sources deleted; the effective
  `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8` moved by the arm's counted assertions less one, each with
  a `RAISED` line. At `9900b200` they read 4095 and 1312
  (`tools/unattended/unattended.test.sh@92da5fb2d5cc:24236` and `:24524`, DERIVED, the last
  assignment of each), and units 23 and 27 raise both first
- `tools/loop/loop_transition.py`: the `mail-expired` plant and its cases, `render_fixture_mail`'s
  two keys, `MailHeld`'s docstring and message and the docstring's guard paragraph (S5), the
  docstring's plant list and the plant comment (S6)
- `tools/loop/claim.py`: the docstring's guard clause (S5)
- `help/orientation-card.md`: the `mail —` bullet (S5)
- `tools/run-gates/selftest-budgets.txt`: the `loop transition record` row's `plants=<n>` token, 15
  at `9900b200` (`tools/run-gates/selftest-budgets.txt@9709091da4b8:82`) and 18 once
  `KICK-dKeptSession-36` lands its three, set to 19 (DERIVED: `len(PLANTS)`), its reading re-priced
  by direct CLI over `mail-expired` as unit 5 re-priced its two
- `memory/map/generated/symbols.json`: `check_mail_deadline` and `derive_bound_seconds`, by
  `gen_map.py --write`
- `help/loop.md`, `tools/loop/README.md`, `tools/unattended/VERBS.template.md` and
  `memory/guides/UNATTENDED-VERBS.md`: S6
- `skills/session-kickoff/card-store.fixture.sh`: `write_card_mail`'s comment (S5)

### Alternatives rejected

- **The deadline as the tag `policy.flow.wait-ceiling`, resolved by each reader.** Two nodes with two
  values would judge one message two ways (§8 F1).
- **The sender's commit time as the clock.** It is the holder's stamp, the clause's red case.
- **An `answer` message posted at expiry.** A second record of what the deadline already derives,
  written once per reading node (§8 F5).

## 5. Production-readiness checklist

- security — `--default` passes `build_gov_message`'s value checks before any commit; a refused
  policy read writes nothing; no new outbound call.
- perf / scale — one feed pass and one `date` per open message per read; each witness check one
  bounded mail fetch (S3).
- error / empty / loading states — an unsighted message reads `open`, never `expired`; an unresolved
  policy kit writes the default with a NOTE; a malformed `deadline` judges rc 2 and stays `open`.
- observability — `--mail read` prints each expired row's state and its `default` column.
- risks — a feed deleted and rebuilt restamps every sighting, which delays expiry by up to one
  deadline and never advances it.
- testing — the probes of §6 and the arms of §7.
- migration — none.
- user docs — the verbs guide, `help/loop.md` and `tools/loop/README.md` (S6);
  `help/orientation-card.md` (S5).

## 6. Acceptance criteria

The fixture is `KICK-dKeptSession-5`'s two-clone mailbox, or the lease fixture's clone, under
`%TEMP%`, `RUN_CLAIMS` on, a fleet tag and `CLAUDE_CODE_SESSION_ID` set.

- **AC1** — When `bash tools/unattended/unattended.sh --mail post` posts a `question` with
  `--default no` after `write_lease_policy` lands `wait-ceiling = 30` under `[flow]`, the new mail
  commit's message carries `deadline: 30` and `default: no`; the same post without `--default` exits
  2 printing `mail — not written · a question declares its default with --default` and the remote
  gains no ref; a `landed` post and a `--mail ack` each carry `default: ack`; and with the file
  landed as `preset = "strict"` alone, a post carries `deadline: 168`.
  Red when: a message is written with no deadline, a question with no declared default, or the
  post reads a value other than the one `get` answers at the landed revision.
  figure: 30 is the fixture's PINNED literal; 168 is DERIVED by `policy.py get flow.wait-ceiling` in
  that clone.
- **AC2** — When a question addressed to `build:<slug>` with `deadline: 30` has its feed line, keyed
  `refs/gov/mail/…`, planted by `add_claim_sighting` 31 hours ago, `--mail read <slug>` prints its row
  with the state `expired` and the `default` column `no`, and `--mail read <slug> --open --ids` prints
  `none`; with the line planted one hour ago the row reads `open` and `--ids` prints its id. When
  `python tools/loop/loop_transition.py --fixture --plant mail-expired` runs, the move records, exit
  0, one commit, its trailer carrying `disposed=a1b2c3d4e5f6` and its `mailbox-message` record
  `State expired`, where `--plant mail-open` over the same question with no deadline exits 1. This
  is the clause's planted question nobody answers.
  Red when: an unanswered question blocks the transition past its deadline, as a guard reading
  `expired` as `open` shows.
  figure: 30, 31 and the id are PINNED literals of the fixtures.
- **AC3** — When the question's commit carries a committer date 25 hours before now, as a holder a
  day behind the reader stamps it, its `deadline` is 24 and this node's feed sights it a minute ago,
  `--mail read` prints it `open`; a scratch copy of the driver whose `check_mail_deadline` ages
  `now - %ct` prints it `expired`. This is the clause's reader whose clock runs a day ahead.
  Red when: the sender's stamp decides the deadline.
  figure: PINNED, the fixture's own literals.
- **AC4** — When `check_mail_deadline <ref> <sha> 1` runs in a shell that has sourced
  `tools/unattended/unattended.sh`, it returns 0 over a commit whose feed line is planted
  `7200` seconds before now, 1 over one planted `60` seconds before now, 2 over an unsighted sha, and 2
  with `<hours>` planted `x`; `<hours>` planted `1.5` returns 0 over the first and 1 over one planted
  `5000` seconds before now; a `<ref>` passed in its `refs/gov/remote/` spelling answers as its
  `refs/gov/` spelling does; the unsighted message's row reads `open`.
  Red when: an unsighted or malformed deadline reads `expired`, or a fraction of an hour is dropped.
  figure: PINNED, the planted ages are the fixture's own literals.
- **AC5** — When `--mail post` runs from a scratch copy of the driver with no policy kit beside it,
  it writes `deadline: 72` and prints one NOTE whose key list names `flow.wait-ceiling`; when a fresh
  `write_lease_fixture` lands an unparsable first policy revision, as DPR1 AC17 stages one, so
  `policy.py get` exits 2, the post exits 2 printing `mail — not written · ` and the refusal, and the
  remote gains no ref.
  Red when: a refused read writes a deadline, or an unresolved policy kit writes a value other than
  the catalogue default.
  figure: 72 is DERIVED by `policy.py get flow.wait-ceiling` over the catalogue.
- **AC6** — When `grep -n -- '--default\|deadline\|expired\|first saw'` runs over
  `tools/unattended/VERBS.template.md`, each is found in its `--mail` entry, and `cmp` finds
  `memory/guides/UNATTENDED-VERBS.md` byte-equal to it; `grep -n -- '--default' help/loop.md` finds
  the `--mail` paragraph and `grep -n 'deadline' help/loop.md` the guard paragraph;
  `grep -n 'mail-expired' help/loop.md tools/loop/README.md` finds each plant list; and
  `python tools/govkit/docs_leg.py --fingerprints` prints `verb:unattended.sh:--mail` with the
  fingerprint that paragraph's anchor carries.
  Red when: a text states no deadline rule, or the anchor keeps the fingerprint from before
  `--default`.
- **AC7** — When `grep -c 'declare -F check_mail_deadline' tools/unattended/unattended.sh` runs it
  prints 0, and `grep -c "functions absent" tools/unattended/unattended.test.sh` prints 0.
  Red when: a probe that can no longer fail stays in the driver, or the suite still asserts its
  absent case.
- **AC8** — When `python tools/loop/loop_transition.py --fixture --plant mail-open` runs, its
  `refused —` line ends "until it is answered, acknowledged or past its deadline"; with text folded
  to one line by `tr -s ' \n' '  '`, `grep -c 'answered, acknowledged or past its deadline'` prints 1
  over each of `help/orientation-card.md` and `tools/loop/claim.py`, and
  `grep -c -E 'answered (or|nor) acknowledged'` prints 0 over those two, `help/loop.md`, `tools/loop/loop_transition.py`,
  `tools/loop/README.md` and `tools/unattended/VERBS.template.md` folded together.
  Red when: a shipped text says an answer or an ack alone releases a move.
  figure: 1 and 0 are PINNED, the folded counts once every rewrite lands.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `scratch-guard self-test` · `tier2-review self-test` · `policy check` · `policy fixtures` · `loop transition record` · `loop claim fixtures` · `docs` · `manifest-check self-test`

By `python tools/check-spec-tokens.py --legs-for tools/loop/claim.py help/orientation-card.md`,
2026-11-23: `tools/loop/claim.py` trips only the broad `tools/` guard, as
`tools/loop/loop_transition.py` does; `kit epoch` reads it as loop-kit bytes and `loop claim
fixtures` runs it, so joins the line. The card page trips no guarded leg; `docs` reads its
anchors, commands and links, never prose, and the edit keeps its link and moves no anchor's shape.

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC5 · the deadline arms over planted feed lines and mail commits, staged by a scratch copy whose judgment reads the commit's own date · the effective `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8` move by the arms' counted assertions less DPR1 AC11's retired one, counted off the diff
New arm: tools/loop/loop_transition.py · covers AC2 · the `mail-expired` plant, staged by a guard reading `expired` as `open` · the `loop transition record` row's `plants=<n>` token rises by one, to 19 over unit 36's 18

## 8. Open questions

- **F1 — What does a message's `deadline` hold: the asker's hours, or the key each reader resolves?**
  Options: (a) the hours `flow.wait-ceiling` read at the post, so every reader judges the one
  deadline the asker declared; (b) the tag `policy.flow.wait-ceiling`, TOOL-dDeclaredLoop-33 S5's
  grammar for a row, resolved by each reader, so two nodes with two values judge one message two
  ways. The clause says the message declares the deadline, and P40 forbids two nodes deciding one
  verdict differently. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3. widens: none · relaxes: none
- **F2 — Which messages carry a deadline?** Options: (a) every message, since cl-dClosedLoop-0143 refuses
  a transition while any message addressed to the build is neither answered nor acknowledged until
  `flow.wait-ceiling` passes; (b) only `question` and `confirm-request`, which leaves a `changed` nobody
  acknowledges blocking for ever. RESOLVED (agent, 2026-10-26, delegated): (a), rung 1, cl-dClosedLoop-0143.
  widens: none · relaxes: none
- **F3 — What does a `question` posted with no declared default do?** Options: (a) refused at the
  post, exit 2; (b) written with `default: none`, so it expires into an answer nobody chose. The
  clause names "the asker's declared default". RESOLVED (agent, 2026-10-26, delegated): (a), rung 1,
  the clause's text. widens: none · relaxes: none
- **F4 — What does a reader do with a message its feed has not sighted?** Options: (a) `open`, never
  `expired`, the rule TOOL-dPlacedRequest-17 §8 F3 settled for leases; (b) sighted now, which restarts
  the clock whenever a feed line is lost. RESOLVED (agent, 2026-10-26, delegated): (a), rung 3.
  widens: none · relaxes: none
- **F5 — Is the default answer written when the deadline passes?** Options: (a) derived, read as
  `expired` with its `default`; (b) an `answer` message posted by the first reader past the deadline,
  a second record of a derived fact that each reading node would post. RESOLVED (agent, 2026-10-26,
  delegated): (a), rung 3, the charter's `[derive]` rule. widens: none · relaxes: none
- **F6 — Through which reader does the post read `flow.wait-ceiling`, and what does a refused read
  write?** The driver landed one shell reader of policy keys, `read_lease_policy`, whose rule is the
  catalogue default with one NOTE where no policy kit resolves, and a refusal returned to a caller
  that then writes nothing. Options: (a) a new arm of that reader under its rule, a refused `get`
  refusing the post; (b) the rev-2 read of the post's own, writing the default on any refusal.
  RESOLVED (agent, 2026-11-21, delegated): (a), rung 3; the charter's `[reuse]` and `[security]`
  rules, since (b) is a second reader and writes a deadline the adopter's invalid file never
  declared. widens: none · relaxes: none
- **F7 — What becomes of `check_lease_witness`'s `declare -F` probe once both names it probes ship in
  the driver?** Options: (a) delete it, with the suite's assertion of its absent case and the stub
  the lease arms export; (b) keep it and stage the absent case over a scratch copy deleting
  `check_mail_deadline`; (c) keep it and drop only the assertion, a branch nothing observes.
  RESOLVED (agent, 2026-11-21, delegated): (a), rung 3; the charter's `[yagni]` rule deletes rather
  than disables, and (b) and (c) keep a probe no shipped driver can fail. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 24, scout B row 7 and its disagreement
  5, Shared interfaces I17, I20 and I23, v2's rows at
  `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c9:1263` and
  `memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c9:1582`,
  and TOOL-dPlacedRequest-17 S1, S4.
- rev-2 · 2026-11-21 · §7 · the leg line names `scratch-guard self-test`, `tier2-review self-test`
  and `policy fixtures`, the legs whose manifest guards §4's `tools/unattended/unattended.sh` and
  `tools/govkit/govkit.py` trip, as the spec-tokens guards join named at the build run's spec stage
  under the brief `2026-11-21-prompt-KICK-dKeptSession-1-build-brief`; no other section moved.
- rev-3 · 2026-11-21 · §1 · S1 · S2 · S3 · S4 · §3 · §4 · AC2 · AC4 · AC5 · AC6 · §7 · §8 F1 · F6 ·
  §10 · re-grounded on the landed tree at `c2a407b0` by
  `2026-11-21-prompt-KICK-dKeptSession-36-orders-17-19-reground-brief`: the parents' clock is landed,
  so S3 calls `check_deadline_passed` with the ref in the feed's spelling and converts a fractional
  `hours` value through `derive_bound_seconds`, extracted from `read_lease_bound`; S4 names
  `add_feed_sightings refs/gov/remote/` as the one argument that keys mail sightings; S1 reads
  through a new arm of `read_lease_policy`, a refused read refusing the post (F6, AC5); narrowed
  §4's files by the `subject-pins.tsv` regeneration no leg change needs, and §7 by the five govkit
  and policy-fixtures legs it pulled in, `policy check` named for the new reader; every line-number
  citation replaced by a `path#symbol` or blob pin.
- rev-4 · 2026-11-21 · S1 · S2 · S3 · S5 · S6 · §4 · §5 · AC1 · AC2 · AC5 · AC7 · AC8 · §7 · §8 F7 ·
  checked for behaviour under `2026-11-21-prompt-KICK-dKeptSession-24-precheck-brief`: `get` answers at
  the landed revision through the landed preset step, so AC1 lands its file by `write_lease_policy`
  and reads a preset, and AC5 stages a refusal as DPR1 AC17 does, an invalid file over a valid one
  reading that one; AC2's transition is the loop kit's `mail-expired` plant, the unattended suite
  running no writer; S2 adds `--default` to the earlier units' question posts; S3 deletes the
  `declare -F` probe and its absent-case assertion (F7, AC8); S5 disposes `expired` and keeps
  no-deadline records `open`; S6 and AC7 re-stamp `help/loop.md`'s `--mail` anchor; the version move
  left Files touched, which gained `symbols.json`, the plant and its budget row; `policy fixtures`,
  `loop transition record` and `docs` joined §7.
- rev-5 · 2026-11-23 · §1 · S1 · S2 · S3 · S4 · S5 · S6 · §3 · §4 · §5 · AC1 · AC2 · AC5 · AC6 · AC7 ·
  §7 · §10 · re-grounded on the run tree at `9900b200` under
  `2026-11-22-prompt-KICK-dKeptSession-24-reground-brief`: unit 5 landed the post, the reader's
  eleven columns, `add_feed_sightings refs/gov/remote/` and `expired` in the disposal set, so S4
  observes landed code and rev-4's AC6, a restatement of unit 23's AC5, is retired, AC7 and AC8
  renumbered AC6 and AC7; S2 names the `--mail` arm's texts, orders its refusal after the kind and
  drops the length limit no other value carries; S5 reads the two keys under a second key set after
  unit 27's three columns, rewrites `MailHeld`'s message and the three planters' comments, and
  plants the expired plant's feed line;
  §4 gains the shipped-texts table and the refusal ceiling, met unraised, and §7 the
  `manifest-check self-test` leg the card-store fixture's comment trips; the floors, the plant
  count and the strict preset are pinned; base moved to `8b8b1374`, the default-branch sha the run
  branch reconciled.
- rev-6 · 2026-11-23 · S5 · S6 · §4 · §5 · AC8 · §7 · under
  `2026-11-23-prompt-KICK-dKeptSession-24-divergence-brief`: S5 rewrites the card's `mail —` bullet
  and `tools/loop/claim.py`'s guard clause, both in Files touched; S6 names the `help/loop.md`
  sentences, §4 those that stay true; AC8 observes them; §7 adds `loop claim fixtures`.

## 10. Reuse audit

The seam extended is the landed `tools/unattended/unattended.sh#check_deadline_passed`, the one
judgment of a deadline by first sighting, which this unit calls with a mail ref, a message commit
and the declared hours in seconds; its sighting is `tools/lib/gov-feed.sh#read_first_seen` over the
feed `tools/lib/gov-feed.sh#add_feed_sightings` fills, both carried in the driver's `gov_feed_sh`
block. The policy read extends `tools/unattended/unattended.sh#read_lease_policy` by one arm, the
conversion is `read_lease_bound`'s arithmetic, extracted at this second instance, the value check is
`build_gov_message`'s, and the state extends `read_mailbox`'s one state pass. `python
tools/codebase-map/reuse_lookup.py "a deadline judged by the time this node first saw a record"`,
re-run 2026-11-23, ranked `records`, `build_records`, `write_record` and `read_records`, name stems
only, and `python tools/codebase-map/reuse_lookup.py "convert a policy duration in hours to whole
seconds"` ranked `read_policy_value`, `read_policy_kit`, `PolicyRefused` and `load_policy`, Python
readers that do not convert; neither probe names a shell judgment or conversion, so no seam fits
beyond the driver's own. `python tools/memory-recall/query.py "how does a mailbox message expire by
the observer clock"` returned scout B's row 7 and this spec.

Recall terms used: mailbox deadline flow.wait-ceiling observer clock first sighting check_deadline_passed expired default read_first_seen add_feed_sightings
