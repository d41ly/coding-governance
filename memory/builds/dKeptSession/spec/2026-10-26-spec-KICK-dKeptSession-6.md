# KICK-dKeptSession-6 — live delivery where the harness has it: the post's tail rings the channels `deps.messaging` picks, with only the ref and the id

**Status:** CLOSED · rev-5 · 2026-11-23 · node a · Tier-2 · base b2303b53 · streams kickoff · order 23 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0144@c41201f3 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md) | research | KICK-dKeptSession-5 KICK-dKeptSession-10 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-1 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-11-21-build-KICK-dKeptSession-10-reground-orders-20-26-returns.md](../build/2026-11-21-build-KICK-dKeptSession-10-reground-orders-20-26-returns.md) | research | KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-1 |
| [2026-11-21-build-KICK-dKeptSession-6-1-acceptance-ledger.md](../build/2026-11-21-build-KICK-dKeptSession-6-1-acceptance-ledger.md) | journal | — |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-5 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-24-precheck-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-24-precheck-brief.md) | research | KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-5 |
| [2026-11-21-prompt-KICK-dKeptSession-6-1-spec-writer.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-6-1-spec-writer.md) | journal | — |
| [2026-11-21-prompt-KICK-dKeptSession-6-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-6-build-brief.md) | research | — |
| [2026-11-21-prompt-KICK-dKeptSession-6-orders-23-24-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-6-orders-23-24-reground-brief.md) | research | KICK-dKeptSession-7 |
| [2026-11-22-prompt-KICK-dKeptSession-6-reground-brief.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-6-reground-brief.md) | research | — |
| [2026-11-23-prompt-KICK-dKeptSession-6-1-spec-writer.md](../prompts/2026-11-23-prompt-KICK-dKeptSession-6-1-spec-writer.md) | journal | — |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |
| [2026-11-23-review-KICK-dKeptSession-69-closing-diff-review-round1.md](../reviews/2026-11-23-review-KICK-dKeptSession-69-closing-diff-review-round1.md) | diff-review | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 KICK-dKeptSession-67 KICK-dKeptSession-69 |

<!-- /gen:spec-records -->

## 1. Goal

Where the harness can message another session, a sender writes the mailbox first and then delivers
live, citing the message (coordination item 7,
`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-coordination.md@4a13cbc82a99:122`);
`deps.messaging` picks the channels, and the live message carries only the message's ref and id, so a
lost ring costs only latency (FI-6, the owner's NT-17). This unit gives the one mail writer,
`tools/unattended/unattended.sh#write_mail_post`, that tail: one ring point, called only after the
mailbox write has landed, reading `deps.messaging` and ringing each live channel the harness offers.
The harness this repository runs in offers none between sessions (§8 F1), so today the tail rings
nothing and says so, and a registered doorbell joins at the point dWellOiledMachine declares in
Runtime's `[extend]`
(`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c91952:1167`).

## 2. Scope (IN)

- **S1** — The ring point, `run_mail_ring <ref> <id>` in `tools/unattended/unattended.sh`. Its one
  call sits in the `0)` arm of `write_mail_post`'s closing `case` over `write_mail_ref`'s return,
  after that arm's `echo "mail — posted $id · $ref"` and before its `return 0`, passing the mail
  ref the message was appended to and the message's id, and nothing else: it reads no field of the
  record and passes no fact. The `1)` and `*)` arms, a lost or not-completed write, and every earlier
  refusal call it never. `--mail ack` (`tools/unattended/unattended.sh#write_mail_ack`) and
  `KICK-dKeptSession-25`'s `--mail answer` post through `write_mail_post`, so each rings as a post
  does, with no call of its own. Observed by AC1 and AC2.
- **S2** — `deps.messaging` (`live-and-mailbox`, `live-only`, `mailbox-only`, or a registered doorbell;
  default `live-and-mailbox`; the landed row in `tools/policy/catalogue.toml`, owner dKeptSession), read
  through `read_lease_policy deps.messaging >/dev/null`, called directly as the reader's comment
  requires, a new arm of the driver's one shell policy reader
  (`tools/unattended/unattended.sh#read_lease_policy`), beside the arms `KICK-dKeptSession-24` and
  `KICK-dKeptSession-21` add. The arm is the default `live-and-mailbox` in the first `case`, one
  literal `deps.messaging) out=$("$py" "$d/policy.py" get deps.messaging 2>&1) ;;` line in the `get`
  `case`, the three values as one closed-set line in the value `case`, and the key on the signature
  comment, the no-kit NOTE's key list and the unknown-key refusal's key list. A doorbell name fails
  `check_value` (`tools/policy/policy.py#check_value`) until a registry admits it, so a policy file
  naming one is invalid and reads its last valid revision or refuses
  (`tools/policy/policy.py#read_last_valid_value`). No policy kit found reads the default under the
  reader's one NOTE. Where the reader returns 1, a refused `get` or a value outside the three, the
  point takes `live-and-mailbox` and prints one line on stderr, `unattended: NOTE - deps.messaging did
  not read, so the ring takes live-and-mailbox: <LP_VALUE>`. Observed by AC1 and AC4.
- **S3** — The ring, by value. Under `mailbox-only` the point rings nothing and prints
  `ring — off (deps.messaging: mailbox-only)` on stdout. Under `live-and-mailbox` and `live-only` it
  rings each live channel the harness offers, the empty set today (§8 F1), and prints
  `ring — none · no live channel in this harness (stand-in dWellOiledMachine)`. Under every value the
  mailbox was written first: `live-only` never skips it (§8 F2). Observed by AC1 and AC3.
- **S4** — A ring never fails a post. `run_mail_ring` returns 0 on every path, and the post's exit is
  its write's; the point's own outcome is its one `ring —` line and, on a refused read, S2's NOTE.
  Observed by AC2 and AC4.
- **S5** — The user texts. The `--mail` entry of `tools/unattended/VERBS.template.md` reads "It prints
  ONE line: `mail — posted <id> · <ref>` (exit 0)", which a posted message's second line makes false:
  it becomes one outcome line, a posted one followed by one `ring —` line, with the three values, the
  two lines S3 prints, the stand-in, the mailbox written first under every value and the ring's two
  fields. Its installed copy `memory/guides/UNATTENDED-VERBS.md` is copied byte-equal, as the
  unattended kit gate's check 10 holds it (`tools/unattended/check-unattended.sh`, `VERBSHIP` against
  `VERBDOC`). `help/loop.md` gains one paragraph directly after its `--mail` paragraph under "Claim
  keys", saying the same in user terms and ending in `<!-- usage: policy:deps.messaging <fp8> -->`,
  the fingerprint `python tools/govkit/docs_leg.py --fingerprints` prints for that key at build time.
  The `--mail` paragraph's `verb:unattended.sh:--mail` anchor is not re-stamped, since the unit adds
  no flag to any usage row (`tools/govkit/docs_leg.py#read_verb_usage`). Observed by AC5.
- **S6** — The key's row. The `deps.messaging` row of `tools/policy/catalogue.toml` gains `summary`,
  stating which channels a post rings once the mailbox write has landed under each value and that
  the mailbox is written under every value, and `usage = 'deps.messaging = "mailbox-only"'`, as
  `KICK-dKeptSession-10` and `-21` give the rows they read. `python tools/policy/policy.py lists
  --write` drains it from `tools/policy/unsummarised-keys.txt`; `python tools/policy/policy.py mirror
  --write` re-renders `.governance/policy.json`, whose `catalogue_blob` the edit moves;
  `help/reference/policy.md` is re-rendered by `python tools/playbook/render_playbook.py --reference`.
  The `policy:deps.messaging` row leaves `memory/project/docs-undocumented.txt` by hand, since S5
  anchors it and an anchored member still listed is the docs leg's `DRAINED` finding
  (`tools/govkit/docs_leg.py#read_docs_state`). Observed by AC6.
- **S7** — The driver's own comments. `write_mail_post`'s header comment, whose order list ends at
  `write_mail_ref` and whose "ONE LINE PER OUTCOME" names `mail — posted <id> · <ref>` exit 0, gains
  the ring call after a written post and says a posted outcome is followed by the point's `ring —`
  line. `read_lease_policy`'s header comment names `deps.messaging` among the keys it reads, with the
  point's own default on a refusal. Observed by AC7.

## 3. Non-goals (OUT)

- No transport, doorbell or adapter: the doorbell point and its registered names are
  dWellOiledMachine's, in Runtime's `[extend]`
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c91952:1777`);
  TOOL-dWellOiledMachine-35 S5 gives this point its first live channel. Building one here would build a
  later build's surface.
- No receiver: what a node does on a ring, the notice fetch through `--mail notice --ring`, and I25's
  payload rule are `KICK-dKeptSession-21`'s.
- No mailbox, record or post path: `KICK-dKeptSession-5`'s, with the keys `KICK-dKeptSession-27` and
  `-24` add to the record.
- No new catalogue row and no preset change: the `deps.messaging` row stands, with
  `registry = "a registered doorbell"`, and every preset in `tools/policy/presets.toml` keeps
  `live-and-mailbox`; `KICK-dKeptSession-21` carries the key's node.
- No `[[stand-in]]` row (§8 F3).

### Edges

- **consumes-from** `KICK-dKeptSession-5` — `write_mail_post`, whose success arm this point follows, `write_mail_ref`, and `write_mail_ack`, which posts through it; the id a ring carries is the one `read_mailbox` reports, so a receiver finds the message by it
- **consumes-from** `KICK-dKeptSession-21` — `deps.messaging`, the channel key, and I25's payload `<mail ref> <message id>` whose receiver is `--mail notice --ring`
- **hands-off** external — dWellOiledMachine's doorbell point in Runtime's `[extend]` arms the registered doorbell names and the live channels the ring point rings

## 4. Design

### Evidence

- Coordination item 7
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-coordination.md@4a13cbc82a99:122`):
  the sender writes the mailbox first, then delivers live citing the message id; any other harness,
  and the owner by hand, use the same verbs; the live message carries only ref and id.
- FI-6 (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-flow-interactions.md@6f6b55dd620d:113`):
  "Live where possible, mailbox always".
- No code rings anything: `git grep -n 'SendMessage\|doorbell' -- tools skills` prints only the
  `deps.messaging` row's `registry` cell in `tools/policy/catalogue.toml`, re-probed at base b2303b53.
- The runtime research row on `SendMessage` records it resuming an agent of the session that spawned
  it, and names no reach into another session
  (`memory/builds/dClosedLoop/build/2026-10-15-build-PLAY-dClosedLoop-1-research-runtime-spawn.md@8224d5e17818:103`).
- The post is landed. `write_mail_post` ends in one `case` over `write_mail_ref`'s return: `0)` prints
  `mail — posted <id> · <ref>` and returns 0, `1)` prints `mail — lost`, any other `mail — not
  written` (`tools/unattended/unattended.sh#write_mail_post`). Its `ref` is `derive_mail_ref`'s
  `refs/gov/mail/<slug>/<tag>/<session>` and its `id` `derive_message_id`'s twelve hex digits, both
  held at the post before any write (`tools/unattended/unattended.sh#derive_mail_ref`,
  `tools/unattended/unattended.sh#derive_message_id`). `write_mail_ack` calls it with an empty body.
- `read_lease_policy` sets `LP_VALUE` and prints it, returns 1 with the refusal in `LP_VALUE` on a
  refused `get` or a value outside its closed `case`, caches a read key in `LP_SEEN`, and prints its
  no-kit NOTE once per process under `LP_NOTED`, on stderr
  (`tools/unattended/unattended.sh#read_lease_policy`). Its no-kit branch returns 0 with the default.
- `policy.py get` reads the policy file at the landed revision, the remote-tracking tip of the
  default branch (`tools/policy/policy.py#derive_landed_revision`), so a fixture's planted value
  reads only once pushed and fetched, as the suite's `write_lease_policy` helper does
  (`tools/unattended/unattended.test.sh#write_lease_policy`). The file falls back or refuses whole,
  never one key (`tools/policy/policy.py#read_last_valid_value`), and `KICK-dKeptSession-24` S1 makes
  the post read `flow.wait-ceiling` before its fetch, a refused read refusing the post, so a whole-file
  refusal never reaches the ring. The tracked driver resolves the policy kit beside its own
  directory (`tools/lib/resolve_kit_dir.py#resolve_kit_dir`), never a stub in the clone it runs in.
  AC4 therefore stages its refusal at the reader.
- The policy kit's reader coverage counts a literal `policy.py get <key>` call
  (`tools/policy/check_policy.py#check_reader_coverage`), and grades only keys whose owner build has
  landed, dKeptSession not yet among them, so the arm's literal line is the key's first reader.

### The tail, in order

1. `write_mail_post` builds and writes the message; on any return of `write_mail_ref` but 0 it prints
   and exits as unit 5 landed it.
2. On 0 it prints its `mail — posted` line and calls `run_mail_ring "$ref" "$id"`.
3. The point calls `read_lease_policy deps.messaging >/dev/null`, takes `live-and-mailbox` with S2's
   NOTE on a return of 1, prints its one `ring —` line and returns 0.
4. `write_mail_post` returns 0.

### Shipped texts

The clauses make these false, and each is rewritten:

| Text | Clause |
|---|---|
| `tools/unattended/VERBS.template.md`'s `--mail` entry, "It prints ONE line", and its copy `memory/guides/UNATTENDED-VERBS.md` | S5 |
| `help/loop.md`'s `--mail` paragraph, which names `mail — posted <id> · <ref>` as the post's output; the paragraph after it | S5 |
| `tools/policy/catalogue.toml`'s `deps.messaging` row, with no summary; `tools/policy/unsummarised-keys.txt`, `.governance/policy.json`, `help/reference/policy.md` and `memory/project/docs-undocumented.txt`, which follow it | S6 |
| the header comments of `write_mail_post` and `read_lease_policy` in `tools/unattended/unattended.sh` | S7 |

A text `KICK-dKeptSession-25` lands saying `--mail answer` prints the post's one line is rewritten to
its lines under S5 or S7, found by `grep -n "post's line\|ONE line" tools/unattended/VERBS.template.md
tools/unattended/unattended.sh help/loop.md` at build time.

These stay true and are left as they are. The `--mail post` usage row in the driver's header names
the exits, which the ring does not move. `write_mail_ack`'s "the post's exits are the ack's" and the
`--mail ack` entry's "else the post's exits" name exits only. `tools/loop/README.md`, which says
`--mail post` refuses any other kind before it writes, and the comments in `tools/loop/loop_lib.py`,
`tools/loop/loop.toml`, `tools/loop/loop_transition.py`, `skills/session-kickoff/card-store.fixture.sh`
and the suite's fixture helpers, which name the post's record or kinds, say nothing of its output.
The suite's landed mail arms read the post's `mail — posted` line with `sed -n 's/^mail — posted …/p'`
or `grep -c`, never as the output's only line, so a second line moves none of them. Every preset
keeps `live-and-mailbox`.

### The refusal ceiling

`tools/unattended/unattended.sh` sits at its ceiling, 347 sites (PINNED,
`.memory-tree.conf@d4f8d497b8c3:661`, 2026-11-23). The census counts a `fail <n> "` call, an `exit 1`
word and a `status=1` assignment (`tools/memory-tree/check-arms.py@60d9015821da:157`). This unit adds
none: `run_mail_ring` returns 0 on every path and prints with `echo`, and the reader's arm adds `case`
lines and list words only. The ceiling is met unraised.

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `run_mail_ring` | shell function | `sh.function`, OK by `lexicon.py --suggest run_mail_ring --as sh.function` |
| `ring —` | the post's output line | none |

### Migration

None. The catalogue row gains two optional fields (`tools/policy/policy.py#OPTIONAL`), and its
`allowed` and `default` do not move.

### Rollout

Behind `RUN_CLAIMS` with every mail write. The point rings nothing until a live channel exists, so
landing it changes no delivery. The kit version is the lander's to mint at the push, never this
branch's (`tools/push-main.sh@3a5bf825e879:27`).

### Files touched (estimate)

- `tools/unattended/unattended.sh`: `run_mail_ring`, its call in `write_mail_post`'s `0)` arm,
  `read_lease_policy`'s `deps.messaging` arm, and the two comments of S7
- `tools/unattended/unattended.test.sh`: the arms of §7 in a block of their own in region eight,
  opened by `if in_shard 8; then` past a seam as the mail blocks there are; the effective
  `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8` raised by the arms' counted assertions, each with a `RAISED`
  line. At b2303b53 they read 4100 and 1317 (DERIVED, the last assignment of each in the suite), and
  the units ordered before this one raise both first. No row of `tools/run-gates/selftest-budgets.txt`
  is re-priced: the `unattended driver selftest shard 8/8` row is an ESTIMATE sized by region share
  and carries no `plants=` token, as `KICK-dKeptSession-23` left it.
- `memory/map/generated/symbols.json`: `run_mail_ring`, re-rendered by `python
  tools/codebase-map/gen_map.py --write`, never hand-edited
- `tools/unattended/VERBS.template.md` and its copy `memory/guides/UNATTENDED-VERBS.md`: S5
- `help/loop.md`: S5's paragraph and anchor
- `tools/policy/catalogue.toml`: the row's `summary` and `usage`
- `tools/policy/unsummarised-keys.txt`: drained by `lists --write`
- `.governance/policy.json`: re-rendered by `mirror --write`
- `help/reference/policy.md`: re-rendered by `render_playbook.py --reference`
- `memory/project/docs-undocumented.txt`: the `policy:deps.messaging` row deleted

### Alternatives rejected

- **A same-node ring through a file the other session's hook watches.** The tool-call hook of
  `KICK-dKeptSession-21` already reads the node's local copy, which the post's own write updates, so
  a ring file would be a second copy of what the cache already holds.
- **A ring before the write.** A receiver could fetch before the message exists and find nothing,
  and a lost write would leave a ring for no message.
- **A ring call in each verb that posts.** `--mail ack` and `--mail answer` would each carry a copy;
  the one writer's success arm is the one place every post passes.

## 5. Production-readiness checklist

- security — the ring passes two strings the post validated before any write, a ref of I16's grammar
  and a twelve-hex id; no body, sender or subject leaves the mailbox.
- perf / scale — one `policy.py get` per post process, cached in `LP_SEEN` after.
- error / empty / loading states — no channel prints `ring — none`; a refused read prints a NOTE and
  rings as the default.
- observability — every posted message prints its `ring —` line.
- risks — none at landing: nothing is rung.
- testing — the probes of §6 and the arms of §7.
- migration — none.
- user docs — `memory/guides/UNATTENDED-VERBS.md`, `help/loop.md` and `help/reference/policy.md`.

## 6. Acceptance criteria

- **AC1** — When `bash tools/unattended/unattended.sh --mail post` posts a `landed` message, which
  needs no `--default` (`KICK-dKeptSession-24` S2), with no `deps.messaging` set, its stdout's last
  two lines are `mail — posted <id> · <ref>` and `ring — none · no live channel in this harness
  (stand-in dWellOiledMachine)`, exit 0; with `deps.messaging = "mailbox-only"` set, its last line is
  `ring — off (deps.messaging: mailbox-only)`, exit 0.
  Red when: the post rings under `mailbox-only`, or prints no ring line.
  fixture: a scratch clone with a bare origin under `%TEMP%`, `RUN_CLAIMS=on`, a fleet tag and
  `CLAUDE_CODE_SESSION_ID` set; the value written as `[deps]` with `messaging = "mailbox-only"` in
  `.governance/policy.toml`, committed, pushed to the origin's `main` and fetched, since `policy.py
  get` reads the landed revision (§4 Evidence).
- **AC2** — When a shell that has sourced `tools/unattended/unattended.sh` replaces `run_mail_ring`
  with a recorder and posts in AC1's clone, the recorder holds one call of exactly two arguments, the
  mail ref and the id, and at that call `git ls-remote` already shows the ref at the message commit;
  with `write_gov_ref` replaced by one returning 1, the recorder holds no call and the post prints
  `mail — lost` and returns 1.
  Red when: the ring runs before the mailbox write, after a lost one, or with more than the ref and id.
- **AC3** — When `deps.messaging = "live-only"` is set as AC1 sets it, the post still moves the mail
  ref on the origin and prints `ring — none · no live channel in this harness (stand-in
  dWellOiledMachine)`, exit 0.
  Red when: `live-only` skips the mailbox.
- **AC4** — When a shell that has sourced `tools/unattended/unattended.sh` wraps `read_lease_policy`
  so `deps.messaging` returns 1 with a planted refusal in `LP_VALUE` and every other key reads through
  the driver's own, then runs `run_mail_ring refs/gov/mail/fx/a/s1 0123456789ab 2>&1`, it prints one
  `unattended: NOTE -` line naming `deps.messaging` and the planted refusal, then `ring — none · no
  live channel in this harness (stand-in dWellOiledMachine)`, the `live-and-mailbox` line, and returns
  0.
  Red when: a refused read rings nothing silently or returns non-zero.
- **AC5** — When `grep -n 'ring —'` and `grep -n 'deps.messaging'` run over
  `tools/unattended/VERBS.template.md` and `help/loop.md`, each finds a line in each file, the VERBS
  ones inside the `--mail` entry and the help ones in the paragraph after the `--mail` one; `cmp
  tools/unattended/VERBS.template.md memory/guides/UNATTENDED-VERBS.md` prints nothing; `grep -c
  'usage: policy:deps.messaging' help/loop.md` prints `1`; and `grep -c 'It prints ONE line:
  .mail — posted' tools/unattended/VERBS.template.md` prints `0`.
  Red when: the ring line is undocumented, or the guide still says a post prints one line.
- **AC6** — When `grep -c '^deps.messaging$' tools/policy/unsummarised-keys.txt` and `grep -c
  '^policy:deps.messaging' memory/project/docs-undocumented.txt` run, each prints `0`; `python
  tools/policy/policy.py lists --check`, `python tools/policy/policy.py mirror --check` and `python
  tools/playbook/render_playbook.py --reference --check` each report nothing for the key.
  Red when: the row is still unsummarised or listed undocumented, or a generated copy holds the old
  catalogue.
- **AC7** — When `grep -c 'deps.messaging' tools/unattended/unattended.sh` and `grep -n 'run_mail_ring'
  tools/unattended/unattended.sh` run, the second finds the definition, the call in `write_mail_post`'s
  `0)` arm and a line of `write_mail_post`'s header comment; the first counts the default, the `get`
  line, the closed-set line, the three key lists and `read_lease_policy`'s header comment.
  Red when: a comment still says a posted outcome is one line, or the reader's lists omit the key.
  figure: the count is DERIVED by the grep at observation time.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `govkit selftest` · `govkit refusal join` · `govkit acceptance matrix` · `scratch-guard self-test` · `tier2-review self-test` · `policy check` · `policy fixtures` · `routed-commits selftest` · `help reference pages` · `docs`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 · the ring arms over a post in region eight, AC2 staged by a recorder in place of `run_mail_ring` and a planted lost write, AC4 by a wrapped `read_lease_policy` · the effective `FLOOR_ASSERTIONS` and `FLOOR_SHARD_8` rise by its counted assertions

## 8. Open questions

- **FACT-QUESTION · F1 — Does this harness offer a channel by which one session messages another?**
  Probe: `git grep -n 'SendMessage\|doorbell' -- tools skills`, and the installed CLI's tool text read
  with `grep -a -o '.\{0,100\}SendMessage.\{0,240\}' <CLI binary>` (Claude Code 2.1.308). Observation,
  2026-10-26: no file under `tools` or `skills` rings anything; the CLI's `SendMessage` addresses an
  agent this session spawned or a teammate of "a single implicit team", never another session, as the
  runtime research row records. Re-probed 2026-11-23 at base b2303b53: the grep prints only the
  catalogue's `registry` cell. Liveness: a tool addressing another session would print in the CLI's
  tool text the grep reads. RESOLVED (agent, 2026-10-26, delegated): no live channel; the set the ring
  point rings is empty until Runtime's doorbell point, rung 2. widens: none · relaxes: none
- **F2 — Does `live-only` skip the mailbox?** Options: (a) no: the mailbox is written under every
  value, since a ring carries only a ref and an id (cl-dClosedLoop-0159) and the sender writes the
  mailbox first (coordination item 7); (b) yes, which rings an id no mailbox holds. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 1. widens: none · relaxes: none
- **F3 — Is the stand-in a `[[stand-in]]` row?** The brief asks a stand-in be registered so.
  Options: (a) no row: the `[[stand-in]]` rows of `tools/loop/loop.toml` name row items whose owning
  build has not landed, and `check_transition_tables` refuses a row naming no row item
  (`tools/loop/loop_table.py#check_transition_tables`), and a ring is no item, so the stand-in is named
  on the `ring —` line and in §3's hand-off; (b) a row, which that check refuses. RESOLVED (agent,
  2026-10-26, delegated): (a), rung 1, TOOL-dDeclaredLoop-13 S8. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft, from the packet's Items 6, scout B row 2, Shared interfaces
  I8, I19 and I25, coordination item 7, FI-6 and v2's `deps.messaging` row.
- rev-2 · 2026-11-21 · §7 · the leg line names `scratch-guard self-test`, `tier2-review self-test`
  and `policy fixtures`, the legs whose manifest guards §4's `tools/unattended/unattended.sh` and
  `tools/govkit/govkit.py` trip, as the spec-tokens guards join named at the build run's spec stage
  under the brief `2026-11-21-prompt-KICK-dKeptSession-1-build-brief`; no other section moved.
- rev-3 · 2026-11-21 · §1 · §2 S1, S2, S5 · §3 · §4 · §5 · §6 AC1, AC4, AC5 · §7 · §8 F1, F3 · §10 ·
  re-grounded on the run's base c2a407b0 under the brief
  `2026-11-21-prompt-KICK-dKeptSession-6-orders-23-24-reground-brief`: every line citation re-cited to a
  symbol or a blob pin; the policy read re-cited to the landed `read_lease_policy` and the doorbell
  refusal to `check_value`; the `deps.messaging` row marked landed; the stand-in check re-cited to
  `check_transition_tables`; narrowed by dropping the kit version move, which the lander mints, and
  the `subject-pins.tsv` regeneration, which no leg change of this unit owes, with `policy fixtures`
  off the leg line; the arm's floor reads none, as the suite declares no assertion floor; widened by
  the `help/loop.md` sentence the charter's docs rule owes, with `docs` on the leg line.
- rev-4 · 2026-11-21 · S2 · §4 · AC1 · AC4 · §7 · checked for behaviour under
  `2026-11-21-prompt-KICK-dKeptSession-24-precheck-brief`: S2 reads through a new arm of
  `read_lease_policy` and names the point's NOTE on the reader's return 1; a stub policy kit in a
  scratch clone is never the one the tracked driver resolves, and a whole-file refusal also refuses
  unit 24's `flow.wait-ceiling` read before any ring, so AC4 wraps the reader in a sourced shell and
  calls `run_mail_ring` itself; AC1 posts a `landed` message, which needs no `--default`; the suite
  does declare an assertion floor, so §7's arm and Files touched name it; `symbols.json` joined.
- rev-5 · 2026-11-23 · §1 · S1 to S7 · §3 · §4 · §5 · AC1 to AC7 · §7 · §8 F1 · §10 · re-grounded
  on the run tree at `b2303b53` under `2026-11-22-prompt-KICK-dKeptSession-6-reground-brief`, units
  39, 51, 27, 24, 10, 25 and 21 read as landed: unit 5 landed `write_mail_post`, so S1 places the call
  in its `0)` arm, where `--mail ack` and unit 25's `--mail answer` ring through it too; S2 spells
  the arm beside units 24's and 21's and puts the point's NOTE on stderr; widened by S5's rewrite of the guide's "It prints ONE line", which a ring
  line makes false, S5's `policy:deps.messaging` anchor in its own paragraph, S6's summary, usage and
  the four files they move, as units 10 and 21 give the keys they read, and S7's two comments, with
  AC6 and AC7 observing them; §4 gains the evidence of the landed post and reader, the shipped-texts
  table and the refusal ceiling, met unraised; Files touched names region eight's `FLOOR_SHARD_8`
  and the unre-priced budget row; §7 gains `policy check`, `policy fixtures`, `routed-commits selftest`
  and `help reference pages`; the push-main pin re-cited to its blob at the base.

## 10. Reuse audit

No existing seam fits the ring itself: `git grep -n 'SendMessage\|doorbell' -- tools skills` finds no
ring, and scout B's row 2 found the same. The seam extended is `write_mail_post`'s success arm
(`tools/unattended/unattended.sh#write_mail_post`), the one place every post, ack and answer passes
after a landed write; the policy read is the driver's one shell form, `read_lease_policy`
(`tools/unattended/unattended.sh#read_lease_policy`), one arm more. `python
tools/codebase-map/reuse_lookup.py "ring another session live after writing a message"`, re-run at
b2303b53, ranked `write`, `write_text`, `live` and `write_fixture_files`, name stems only, none a
delivery. `python tools/memory-recall/query.py "how does a live ring reach another session"` with the
terms below returned scout B's row 2, this spec, the spec brief's unit row, the night-pass
instrument's `deps.messaging` cell, the packet's `deps.messaging` row and TOOL-dWellOiledMachine-55's
transport points; none disagrees with source.

Recall terms used: deps.messaging live-and-mailbox doorbell live ring SendMessage registered doorbell mailbox-only Runtime extend run_mail_ring
