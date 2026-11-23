# KICK-dKeptSession-22 — each message's id derived from what it says, never from its sender's session, and a retried post refused across the build's session refs

**Status:** CLOSED · rev-7 · 2026-11-22 · node a · Tier-2 · base c2a407b0 · streams kickoff · order 15 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0160@3e3e0128 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md) | research | KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-10 KICK-dKeptSession-21 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-1 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-build-KICK-dKeptSession-22-deviation-221.md](../build/2026-10-26-build-KICK-dKeptSession-22-deviation-221.md) | deviation | — |
| [2026-10-26-build-KICK-dKeptSession-22-deviation-222.md](../build/2026-10-26-build-KICK-dKeptSession-22-deviation-222.md) | deviation | — |
| [2026-10-26-build-KICK-dKeptSession-22-deviation-223.md](../build/2026-10-26-build-KICK-dKeptSession-22-deviation-223.md) | deviation | — |
| [2026-10-26-build-KICK-dKeptSession-22-deviation-224.md](../build/2026-10-26-build-KICK-dKeptSession-22-deviation-224.md) | deviation | — |
| [2026-11-21-build-KICK-dKeptSession-22-1-acceptance-ledger.md](../build/2026-11-21-build-KICK-dKeptSession-22-1-acceptance-ledger.md) | journal | — |
| [2026-11-21-build-KICK-dKeptSession-45-reground-orders-14-19-returns.md](../build/2026-11-21-build-KICK-dKeptSession-45-reground-orders-14-19-returns.md) | research | KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-28 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-36 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-1 |
| [2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-parents-crosscheck.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-20 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-22-1-spec-writer.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-22-1-spec-writer.md) | journal | — |
| [2026-11-21-prompt-KICK-dKeptSession-22-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-22-build-brief.md) | research | — |
| [2026-11-21-prompt-KICK-dKeptSession-22-precheck-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-22-precheck-brief.md) | research | KICK-dKeptSession-31 KICK-dKeptSession-5 |
| [2026-11-21-prompt-KICK-dKeptSession-28-orders-14-16-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-28-orders-14-16-reground-brief.md) | research | KICK-dKeptSession-28 KICK-dKeptSession-31 |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-5 KICK-dKeptSession-23 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |
| [2026-11-23-review-KICK-dKeptSession-69-closing-diff-review-round1.md](../reviews/2026-11-23-review-KICK-dKeptSession-69-closing-diff-review-round1.md) | diff-review | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-23 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 KICK-dKeptSession-67 KICK-dKeptSession-69 |

<!-- /gen:spec-records -->

## 1. Goal

A mailbox post retried after a crash lands twice today in design, because a commit's id changes
with its time (gap-conc-09). Each message's id is instead derived from its build, its item's instance
key, its pass, its kind, its subject and the id it answers, and never from its sender's session, so a
retry carries the id of the post it retries, from the same session or a new one. A duplicate check
reading every one of the build's per-session refs refuses it, while two answers to two messages carry
two ids and both land (the night pass two, point 4; the owner's NT-18 and FK-1-7). The driver's one
shell derivation of an id over fields today is the landed `derive_problem_id`; this unit extracts
its hashing at the second instance.

## 2. Scope (IN)

- **S1** — The shared id, `derive_gov_id [--file <path>] [<field>…]` in
  `tools/unattended/unattended.sh`: the first 12 hex digits of `GIT hash-object --stdin` over each
  field followed by one NUL, then, when `--file` is given, that file's bytes followed by one NUL.
  The cut is the repository's id convention (PINNED, §4 Evidence).
  Zero fields with `--file` hash the file's bytes and their NUL alone, the form KICK-dKeptSession-27
  S3's content key takes. rc 1 when the file cannot be read or git cannot hash: the file is tested
  before the pipe, since the landed pipe answers rc 0 over a missing file, hashing the fields alone
  (§4 Evidence). It is the second
  instance of `derive_problem_id` (`tools/unattended/unattended.sh#derive_problem_id`,
  TOOL-dPlacedRequest-12 S3), so the one derivation is extracted here: that function calls
  `derive_gov_id --file <body file> <session> <item> <subject>`, its output on every readable body
  file byte-identical to its landed derivation, and its one caller, `write_register`
  (`#write_register`), is unchanged. Observed by AC1, AC2.
- **S2** — The message id (I15), `derive_message_id <build> <item> <pass> <kind> <subject> <answers>`:
  `derive_gov_id` over those six fields in that order, each absent one written `none`. It takes no
  session and no time. Observed by AC2, AC3.
- **S3** — The duplicate check, `check_mail_duplicate <build> <id>`: one `GIT for-each-ref` listing
  every ref this node's cache holds under `refs/gov/remote/mail/<build>/`, one per writing session of
  the build (I16, KICK-dKeptSession-5 S1), then one `GIT log --source --first-parent` across all of
  them, its format the source ref, a tab and the subject, matching a subject equal to
  `gov-mail <build>/<id>`, I17's header (KICK-dKeptSession-5 S4). rc 0 when no ref holds it, an empty
  cache included: with no ref listed the log is never run, since `git log` given no revision reads
  HEAD and exits 128 in a repository with no commit. rc 1 printing `mail — duplicate <id> · <ref>` naming the first ref the log prints
  it under; rc 2 when the cache cannot be read. It reads the cache only; its caller fetches first.
  Observed by AC3, AC4, AC5.
- **S4** — The act joins later: once dWellOiledMachine's Runtime mints acts, the act is a seventh
  field of S2, appended after `answers`. Until then the id has six fields. KICK-dKeptSession-31 adds
  two fields at order 16 and KICK-dKeptSession-51 restates the act's place after them. NOT OBSERVED:
  no act exists to derive from in this build, and S2's fixture holds the six.

## 3. Non-goals (OUT)

- No post, fetch or ref write: KICK-dKeptSession-5's `--mail post` fetches the build's mail refs, calls
  `derive_message_id` and `check_mail_duplicate`, and writes only on rc 0.
- No reader collapse of a cross-ref race. Two sessions posting one id to two refs at one instant both
  pass this check, since a compare-and-swap guards one ref only; KICK-dKeptSession-5's `read_mailbox`
  collapses duplicate ids to the earliest sighting.
- No change to what a problem id derives from: TOOL-dPlacedRequest-12 S3 keeps its fields; this unit
  moves only where the hashing lives.
- No act minting: dWellOiledMachine's.
- No guide or help text: KICK-dKeptSession-5's `--mail` entry states the id's fields.

### Edges

- **hands-off** `KICK-dKeptSession-5` — `derive_message_id`, the id every post carries in its header, and `check_mail_duplicate`, which refuses a retried post before any commit is built
- **hands-off** `KICK-dKeptSession-27` — `derive_message_id` and `derive_gov_id`, whose 12-hex convention the content key reuses over an interface's text
- **consumes-from** external — TOOL-dPlacedRequest-12 S3's `derive_problem_id`, the first instance this unit extracts the derivation from
- **hands-off** external — dWellOiledMachine's Runtime, whose act joins S2 as a seventh field
- **hands-off** `KICK-dKeptSession-31` — `derive_message_id`, to which that unit adds the recipient and the content key (id 54)
- **hands-off** `KICK-dKeptSession-51` — S4 and the `hands-off external` edge to dWellOiledMachine, whose seventh position that unit supersedes with the ninth (id 39)
- **hands-off** `KICK-dKeptSession-64` — the retry row of the red-case table and `check_mail_duplicate`'s rc 1, which the batch's S2 supersedes for `--mail ack` (id 15)
- **hands-off** `KICK-dKeptSession-65` — S3's cache-only `check_mail_duplicate`, whose caller the batch's S12 makes fetch first (id 20)

## 4. Design

### Evidence

- `derive_problem_id` pipes session, item and subject, each followed by one NUL, then the body file's
  bytes and one NUL, into `GIT hash-object --stdin`, and prints the first 12 hex of the result
  (PINNED, read 2026-11-21 in `tools/unattended/unattended.sh#derive_problem_id`). That cut is the
  repository's id convention, as `derive_section_sha` (`tools/roles/handoff.py#derive_section_sha`)
  and the request content key (`tools/loop/request.py#derive_request_content_key`) cut theirs. Both
  of those are Python over one text, not shell over fields, so the problem id is the one first
  instance.
- `write_register` refuses an unreadable body file before it derives a problem id
  (`tools/unattended/unattended.sh#write_register`), so the rc 1 S1 adds on an unreadable file
  changes no landed outcome.
- A gov commit's id moves with its time: `build_gov_commit` builds each commit with `commit-tree`
  under the fixed `gov-claim` identity (`tools/lib/gov-ref.sh#build_gov_commit`, inlined in the
  driver), so its date is the only varying input, and a retry is a new commit.
- `read_claims` reads its namespaces' caches in one `for-each-ref`
  (`tools/unattended/unattended.sh#read_claims`). A governance write that lands sets this node's
  cache ref `refs/gov/remote/<tail>` through `write_feed_success`
  (`tools/lib/gov-feed.sh#write_feed_success`, TOOL-dPlacedRequest-34 S5), so a session's own
  earlier post is in the cache without a fetch.
- The night pass two's "Messages" paragraph derives the id from "its sender's act or session"
  (`memory/builds/dClosedLoop/build/2026-10-19-build-PLAY-dClosedLoop-1-night-pass-two.md@e3bafb8b44c7:336`);
  cl-0160 drops the session by the owner's FK-1-7.
- No message id exists: `git grep -n -E "derive_message_id|check_mail_duplicate|derive_gov_id" --
  tools skills` finds nothing at this tree.
- A probe sourcing the driver at this tree (2026-11-21) printed one id from `derive_problem_id s1
  entry.claim push-main.sh body.txt` and from AC1's hand pipe; over a missing body file it printed
  the fields-only hash with rc 0, so S1's rc 1 is new. `git log --source --first-parent` over no
  revision exited 128 in a repository with no commit; `for-each-ref refs/gov/remote/mail/fx/` listed
  `fx`'s session refs and none of `fxy`'s.
- `derive_problem_id`'s one caller is `write_register`; the suite's register arms run the tracked
  driver (`run_register_arm` in `tools/unattended/unattended.test.sh`), so no fixture copy of the
  driver needs the new functions. `memory/map/generated/symbols.json` lists each of the driver's shell
  functions, so the three minted here move it.

### The three red cases

| Case | Fields | Outcome |
|---|---|---|
| a post retried after a crash, same session | equal | `check_mail_duplicate` rc 1, refused |
| a retry from a new session | equal; the session is not a field | rc 1 on the other session's ref, refused |
| two `ack`s from one item, to two messages | `answers` differs | two ids, both rc 0 |

### Inventory

| Minted | Kind | Lexicon cell |
|---|---|---|
| `derive_gov_id` | shell function | `derive`, OK |
| `derive_message_id` | shell function | `derive`, OK |
| `check_mail_duplicate` | shell function | `check`, OK |

### Files touched (estimate)

- `tools/unattended/unattended.sh`
- `tools/unattended/unattended.test.sh`
- `memory/map/generated/symbols.json`: the three functions, regenerated by `gen_map.py --write`

### Alternatives rejected

- **The commit's own sha as the id.** It moves with the commit time, so a retry is a new id: the
  gap itself.
- **Reading only the poster's own ref.** A retry from a new session writes a new ref, so the
  duplicate sits beside it unseen; the clause names this case.
- **Parsing each record's `id:` line.** The header already carries the id, so the subject alone
  answers, and the record keeps one parser, KICK-dKeptSession-5's reader.

## 5. Production-readiness checklist

- security — the id is a hash of fields the post already validated; only the build, a slug the post
  checked, reaches a ref prefix, and only as a read.
- perf / scale — one `for-each-ref` and one `git log` over the build's cached mail refs per post; a
  build's refs number its sessions.
- error / empty / loading states — an empty cache is no duplicate, rc 0; an unreadable one is rc 2,
  and the post refuses rather than writing blind.
- observability — a refusal names the id and the ref holding it.
- risks — two messages with equal fields are one message by design: a sender meaning two must
  differ in subject or pass.
- testing — the fixture cases under AC1 to AC5 and the suite arm in §7.
- migration — none: no message exists yet; problem ids keep their bytes.
- user docs — the verbs guide's mailbox entry, KICK-dKeptSession-5's, states the id's fields.

## 6. Acceptance criteria

The fixture for AC3 to AC5 is a scratch repository under `%TEMP%` whose cache refs
`refs/gov/remote/mail/fx/a/<session>` hold planted commits whose subjects are `gov-mail fx/<id>`.

- **AC1** — When a probe sources `unattended.sh` and runs `derive_problem_id s1 entry.claim push-main.sh
  body.txt` and the landed derivation by hand, `printf 's1\0entry.claim\0push-main.sh\0' | cat -
  body.txt` with a trailing NUL piped to `git hash-object --stdin`, the two print the same 12 hex.
  `derive_gov_id --file` over a missing file returns 1.
  Red when: the extraction changes a problem id, as a planted `derive_gov_id` that drops the file's
  trailing NUL shows, or a missing file hashes the fields alone with rc 0, as the landed pipe does.
- **AC2** — When `derive_message_id fx 'item.design.exit@1#0a1b2c3d' 1 question I16 none` runs twice,
  once under `CLAUDE_CODE_SESSION_ID=s1` and once under `s2`, both print one 12-hex id; changing any
  one of the six fields changes it.
  Red when: the session changes the id, or a field leaves it unchanged.
- **AC3** — When `check_mail_duplicate fx <id>` runs with `<id>` planted on session `s1`'s cache ref, it
  returns 1 naming that ref: the post retried after a crash by `s1` is refused.
  Red when: the planted id returns 0.
- **AC4** — When the planted id sits only on session `s1`'s ref and the check runs for a retry from
  session `s2`, whose own ref is empty, it returns 1 naming `s1`'s ref.
  Red when: a check reading only the poster's own ref returns 0, as a planted copy shows.
- **AC5** — When two `ack`s from one item and pass answer two planted messages, their two
  `derive_message_id` outputs differ, and `check_mail_duplicate` returns 0 for each before either is
  planted, in a fresh scratch repository holding no commit and no mail ref, and 0 for the second
  after the first is.
  Red when: the second acknowledgement is refused as a duplicate of the first, or the empty cache
  returns 2, as a check running the log over no ref shows.

## 7. Gates

`unattended kit gate` · `scratch-guard self-test` · `tier2-review self-test` · `recall floor` · `recall floor arms` · `lexicon naming predicates` · `memory hygiene`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 AC5 · the problem id's bytes, the session excluded, a retry on the same and on another session's ref, and two acknowledgements, staged against the base driver, which has no message id · the effective `FLOOR_ASSERTIONS` pin and its region's `FLOOR_SHARD_<k>` rise by the arm's counted assertions

## 8. Open questions

- **F1 — How does the check find a duplicate?** (a) By each cached ref's commit subjects, the header
  carrying `gov-mail <build>/<id>`; (b) by each record's `id:` line; (c) by a node-local index of ids.
  (b) makes a second parser of the record; (c) is a copy that can disagree with the refs. Rung 3, the
  most capable option: (a) meets AC3 to AC5 from the refs alone. RESOLVED (agent, 2026-10-26,
  delegated): (a). widens: none · relaxes: none
- **F2 — Where does the shared hashing live?** (a) `derive_gov_id`, extracted at this second instance
  with `derive_problem_id` its caller; (b) a copy in `derive_message_id`. (b) is the copy the charter's
  reuse rule forbids at a kind's second instance. Rung 1, the brief's I15. RESOLVED (agent, 2026-10-26,
  delegated): (a). widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.
- rev-2 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-31` mirrored, the other ends of
  the edges the round-1 spec audit's promoted units declare; no other section moved.
- rev-3 · 2026-10-26 · §3 · the Edges bullets to `KICK-dKeptSession-51` mirrored, the other ends of
  the edges the round-1 promotions' audit's disposal declared
- rev-4 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-64` mirrored, the other ends of
  the edges the round-4 minors batch's audit's disposal declared
- rev-5 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-65` mirrored, the other ends of
  the edges the round-5 minors batch's audit's disposal declared
- rev-6 · 2026-11-21 · §1 · S1 · S3 · S4 · §3 · §4 · §5 · AC1 · §7 · §10 · re-grounded on the landed
  dPlacedRequest and dDeclaredLoop at base c2a407b0 by
  2026-11-21-prompt-KICK-dKeptSession-28-orders-14-16-reground-brief: every line citation re-cited by
  symbol or blob pin; the first instance confirmed as the landed `derive_problem_id`, its one caller
  `write_register` kept; S1 admits zero fields with `--file`, the content key's form, and names its
  rc 1; S3 names the log's source-ref format and the cache list, and its cache rule is re-cited to
  `write_feed_success`; S4 names the units that move the act; the guide text left to unit 5; the two
  guarded driver legs named; the arm's floor effect stated. Nothing narrowed: no landed unit builds
  a message id.
- rev-7 · 2026-11-21 · S1 · S3 · §4 · AC1 · AC5 · §7 · checked for behaviour under
  `2026-11-21-prompt-KICK-dKeptSession-22-precheck-brief`: AC1's two derivations probed equal on the
  sourced driver; S1's rc 1 shown new, the landed pipe answering 0 over a missing file, and AC1
  observes it; S3's empty cache shown to need no log run, a log over no ref exiting 128, and AC5
  observes it; `symbols.json`, which the three functions move, added with the `recall floor` legs
  its path trips. No landed unit since base touched a cited symbol.

## 10. Reuse audit

The seam extended is the landed `derive_problem_id` (`tools/unattended/unattended.sh#derive_problem_id`,
TOOL-dPlacedRequest-12 S3), the repository's first derived gov id over fields, whose hashing this
unit extracts as `derive_gov_id`. The cache it reads is the landed `refs/gov/remote/<tail>` mirror
(`tools/lib/gov-feed.sh#write_feed_success`), read the way `read_claims` reads its namespaces
(`tools/unattended/unattended.sh#read_claims`). Re-run at this tree, `python
tools/codebase-map/reuse_lookup.py "derive a stable id from fields by hashing so a retry is refused as
a duplicate"` ranked `field`, `PolicyRefused`, `derive_kit_prefix`, `derive_clause_hash` and
`derive_pin_hash` by name stem: the last two are Python hashes of clause text in
`tools/memory-tree/design_lib.py`, a different input and language, and none reads a ref. Scout B
cited the id convention by line; source holds it at `tools/roles/handoff.py#derive_section_sha` and
in `derive_problem_id`'s own cut. The recall query returned scout B's row 5 and this build's specs 5
and 22.

Recall terms used: `python tools/memory-recall/query.py "how is a retried mailbox post refused as a
duplicate" --terms "message id derive_problem_id hash-object retry duplicate per-session ref mailbox
recipient content-key"`
