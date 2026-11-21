# KICK-dKeptSession-27 — each message carrying its session's sequence number, a take-over its predecessor, and an interface notice its content key

**Status:** DEFERRED · rev-5 · 2026-11-21 · node a · Tier-2 · base c2a407b0 · streams kickoff · order 18 · advances KICK-dKeptSession-29

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
| [2026-11-21-prompt-KICK-dKeptSession-36-orders-17-19-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-36-orders-17-19-reground-brief.md) | research | KICK-dKeptSession-36 KICK-dKeptSession-24 |
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

- **S1** — The sequence number (I22), the key `seq: <n>` that KICK-dKeptSession-5's post writes into
  each record through `build_gov_message`: `1` when the tip read is empty, else
  `git rev-list --first-parent --count <tip read>` plus one, the message's first-parent depth on its
  own ref. Observed by AC1.
- **S2** — The predecessor, the key `after: <id>`: on a message whose `seq` is 1, the id of the newest
  message on any other cached ref under `refs/gov/remote/mail/<slug>/`, or `none` when the build has
  no other session's ref; `none` on every later message. Newest is by the first sighting of each
  ref's tip, read by one `read_first_seen` call over one `ref TAB commit` pair per ref on stdin
  (`tools/lib/gov-feed.sh#read_first_seen`, carried in the driver's `gov_feed_sh` block), each ref
  spelled as the feed keys it, `refs/gov/` plus what follows `refs/gov/remote/`. An unsighted tip
  reads `-` and sorts after every sighted one; ties go to the lesser ref name. A session that takes a
  build over therefore names the last message its predecessor wrote. Observed by AC2.
- **S3** — The content key, the key `content-key: <12 hex>` on a `confirmed` or `changed` post:
  `derive_gov_id --file <interface file>` (KICK-dKeptSession-22), passed as the post's new
  `--interface <file>` option and computed before the id, so it also fills the `<content-key>` field of
  `derive_message_id` (KICK-dKeptSession-31 S1); `none` on every other kind, in the record and in the
  id. A `confirmed` or `changed` post without `--interface` is refused with exit 2 before any commit.
  Observed by AC3.
- **S4** — The reader: `read_mailbox`'s row (KICK-dKeptSession-5 S6) gains the columns `seq`, `after`
  and `content-key`, after `reply`, the last of unit 5's columns, read from the record; a record
  without one reads `-`. Unit 5's columns keep their places, whose first ten the landed witness check
  reads by position (`tools/unattended/unattended.sh#check_lease_witness`). Observed by AC1, AC2.
- **S5** — The dependent's check, `check_interface_notice <slug> <subject> <interface file>` in
  `tools/unattended/unattended.sh`: over the `confirmed` and `changed` rows `read_mailbox <slug> soft`
  prints with that subject, it recomputes `derive_gov_id --file <interface file>` and prints
  `interface — current <id> · <kind> · key <k>`, exit 0, for the row whose `content-key` equals it, and
  `interface — unconfirmed · key <k>`, exit 1, when none does. It never chooses a row by `first-seen`,
  `seq` or fetch order. Observed by AC4, AC5.
- **S6** — The documentation: the verbs guide's mailbox section names the three keys, the
  `--interface` option and the rule a dependent acts by. Observed by AC6.

## 3. Non-goals (OUT)

- No dependency action: what a dependent's unit does on a current `changed`, the interface-change
  re-entry, and where it reads the interface's text from are KICK-dKeptSession-7's.
- No lease take-over: TOOL-dPlacedRequest-1 S5's `take-over` verb; this unit names the predecessor from
  the mail refs alone, so it holds when the lease record is unreadable.
- No total order across builds: `seq` orders one session's messages and `after` links one build's
  sessions; nothing orders two builds' messages, and nothing needs to.
- No rewrite of a delivered message: a later notice supersedes by key, never by editing.

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

- Each session writes its own ref, one commit per message, parented on its previous tip
  (KICK-dKeptSession-5 S1, S2), so a message's depth on its ref is its order within its session and is
  recomputable from the ref.
- Two sessions' refs share no history: a session's first post is a parentless commit, so nothing in
  git links a take-over to its predecessor unless the message says so.
- P40 states that losing a relay costs latency and never correctness
  (`memory/builds/dClosedLoop/build/2026-10-14-build-PLAY-dClosedLoop-1-architecture-v2.md@9bf3b4c9:1076`),
  which arrival order cannot give: a relay may deliver a newer notice first.
- The feed keys every sighting by the remote's spelling of a ref: `derive_feed_events` maps a cached
  `refs/gov/remote/<tail>` to `refs/gov/<tail>` (`tools/lib/gov-feed.sh#derive_feed_events`), and
  `read_first_seen` matches that spelling, so a pair spelled with the cache prefix reads `-`.
- `tools/memory-tree/row_grammar.py#derive_content_key` is a text fold for backlog rows, and
  `tools/loop/request.py#derive_request_content_key` a SHA-256 over that fold for requests; both are
  a different key, and the id convention here is KICK-dKeptSession-22's `derive_gov_id`.

### The red case

| Order of arrival at the dependent | Interface text now | Arrival-order reader | `check_interface_notice` |
|---|---|---|---|
| `changed` (key K2, from the take-over) first, then `confirmed` (key K1) | K2's | `confirmed`, stale | `changed`, current |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `seq`, `after`, `content-key` | record keys and `read_mailbox` columns | none |
| `--interface` | `--mail post` option | none |
| `check_interface_notice` | shell function | `check`, OK |

### Files touched (estimate)

- `tools/unattended/unattended.sh`: the three keys, `--interface`, the row's columns,
  `check_interface_notice`, and `KIT_UNATTENDED_VERSION` moved
- `tools/unattended/unattended.test.sh`
- `tools/unattended/VERBS.template.md`, rendered to `memory/guides/UNATTENDED-VERBS.md`

### Alternatives rejected

- **A timestamp per message.** Two nodes' clocks disagree, and a relay reorders arrival regardless.
- **A build-wide counter.** It needs one ref every session contends for, the serialisation
  gap-conc-04 removed.
- **The predecessor read from the lease's history.** `read_claims` parses only each lease's tip
  (TOOL-dPlacedRequest-1 S2), so the previous holder would need a second parser of the lease record.

## 5. Production-readiness checklist

- security — three more validated keys on an existing write; the interface file is read only to hash
  it and never reaches the remote.
- perf / scale — one `rev-list --count` per post, and on a session's first post one
  `read_first_seen` over its build's refs.
- error / empty / loading states — a `confirmed` or `changed` without an interface file is refused; an
  unsighted ref sorts as never seen, after every sighted one.
- observability — the check prints the chosen id, its kind and the key, or `unconfirmed` with the key.
- risks — two sessions posting first messages at one instant may each name the other's earlier
  message; `after` is a link, and the content key, not `after`, decides what a dependent acts on.
- testing — the fixture cases under AC1 to AC5 and the suite arm in §7.
- migration — none: no message exists yet.
- user docs — the verbs guide; no `help/` page covers the unattended kit.

## 6. Acceptance criteria

The fixture is KICK-dKeptSession-5's: a bare remote and two clones under `%TEMP%`, `RUN_CLAIMS` on.

- **AC1** — When session `s1` of `fx` posts two messages to `build:fy`, `unattended.sh --mail read fy`
  shows them with `seq` 1 and 2.
  Red when: a second post reads `seq` 1, as a planted writer counting from zero shows.
- **AC2** — When session `s2` of `fx` then posts its first message, its `after` is `s1`'s second id; its
  second message's `after` is `none`; and a build's very first message has `after` `none`.
  Red when: a take-over's first message names no predecessor, or names one that is not the last, as a
  planted pair spelled with the cache prefix shows.
- **AC3** — When a `confirmed` post names `--interface i.txt`, its record's `content-key` equals
  `derive_gov_id --file i.txt`; a `changed` post with no `--interface` exits 2 and the remote is
  unchanged.
  Red when: an interface notice lands without its key.
- **AC4** — When clone B holds `s1`'s `confirmed` (key of `i1.txt`) and `s2`'s `changed` (key of
  `i2.txt`), the `changed` planted as sighted first, and `check_interface_notice fy I16 i2.txt` runs,
  it prints `interface — current <the changed's id> · changed`.
  Red when: the dependent acts on the `confirmed`, as a planted check choosing the newest `first-seen`
  shows.
- **AC5** — When the same check runs with an interface file matching neither key, it prints
  `interface — unconfirmed` and exits 1.
  Red when: an unmatched interface reads as confirmed.
- **AC6** — When `grep -n "content-key" tools/unattended/VERBS.template.md` runs, the guide names
  `seq`, `after`, `content-key` and `--interface`.
  Red when: the guide omits a key or the option.

## 7. Gates

`unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `scratch-guard self-test` · `tier2-review self-test` · `lexicon naming predicates` · `recall floor` · `recall floor arms` · `memory hygiene`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC5 · two posts on one session, a take-over's first post, an interface notice without a file, and a `changed` sighted before the `confirmed` it supersedes, staged by a planted check choosing by arrival · none

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

## 10. Reuse audit

The seams are KICK-dKeptSession-5's writer and `read_mailbox`, which this unit's three keys extend, and
KICK-dKeptSession-22's `derive_gov_id`, which the content key reuses; the predecessor's order is the
landed `tools/lib/gov-feed.sh#read_first_seen`, the observer clock every lease read takes. The probe
`python tools/codebase-map/reuse_lookup.py "order messages by sequence number and content key not
arrival"`, re-run 2026-11-21, ranked `key`, `keys`, `parse_key`, `read_conf_key` and
`derive_request_content_key` (`tools/loop/request.py`), none a sequence or a supersession; the last
is a normalised fold, F2's option (b). No existing seam fits the ordering rule itself. Scout B's row
9 named `tools/memory-tree/row_grammar.py#derive_content_key` and ruled it out, which holds.

Recall terms used: `python tools/memory-recall/query.py "how does a dependent order a changed relayed
before confirmed" --terms "sequence number take-over predecessor content key confirmed changed arrival
order relay P40"`
