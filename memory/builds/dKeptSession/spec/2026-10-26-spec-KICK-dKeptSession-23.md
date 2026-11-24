# KICK-dKeptSession-23 — every mail write appended to the change feed once its ref update lands, inside the feed's census

**Status:** CLOSED · rev-5 · 2026-11-23 · node a · Tier-2 · base c2a407b0 · streams kickoff · order 17 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0161@10c6cad1 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md) | research | KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-10 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-1 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-build-KICK-dKeptSession-23-deviation-231.md](../build/2026-10-26-build-KICK-dKeptSession-23-deviation-231.md) | deviation | — |
| [2026-11-21-build-KICK-dKeptSession-23-1-acceptance-ledger.md](../build/2026-11-21-build-KICK-dKeptSession-23-1-acceptance-ledger.md) | journal | — |
| [2026-11-21-build-KICK-dKeptSession-45-reground-orders-14-19-returns.md](../build/2026-11-21-build-KICK-dKeptSession-45-reground-orders-14-19-returns.md) | research | KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-36 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-1 |
| [2026-11-24-build-KICK-dKeptSession-1-runlog-31fbb903.md](../build/2026-11-24-build-KICK-dKeptSession-1-runlog-31fbb903.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 KICK-dKeptSession-67 KICK-dKeptSession-69 KICK-dKeptSession-79 KICK-dKeptSession-80 KICK-dKeptSession-89 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-23-1-spec-writer.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-23-1-spec-writer.md) | journal | — |
| [2026-11-21-prompt-KICK-dKeptSession-23-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-23-build-brief.md) | research | — |
| [2026-11-21-prompt-KICK-dKeptSession-23-precheck-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-23-precheck-brief.md) | research | KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 |
| [2026-11-21-prompt-KICK-dKeptSession-5-orders-16-17-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-5-orders-16-17-reground-brief.md) | research | KICK-dKeptSession-5 KICK-dKeptSession-39 KICK-dKeptSession-51 |
| [2026-11-22-prompt-KICK-dKeptSession-23-1-spec-writer.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-23-1-spec-writer.md) | journal | — |
| [2026-11-22-prompt-KICK-dKeptSession-23-reground-brief.md](../prompts/2026-11-22-prompt-KICK-dKeptSession-23-reground-brief.md) | research | — |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |
| [2026-11-23-review-KICK-dKeptSession-69-closing-diff-review-round1.md](../reviews/2026-11-23-review-KICK-dKeptSession-69-closing-diff-review-round1.md) | diff-review | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 KICK-dKeptSession-67 KICK-dKeptSession-69 |

<!-- /gen:spec-records -->

## 1. Goal

The change feed is how a mirror follows governance state without a change to the core (the owner's
NT-14), and the observer clock reads its first sightings. Every mail write lands in it once its ref
update lands, and in no other case, because the one mail writer reaches the remote only through the
one writer whose success exit appends; and the feed's census, landed with TOOL-dPlacedRequest-13, holds
that true over every tracked shell file, so this unit observes the join on the mail writer it guards.

## 2. Scope (IN)

- **S1** — The join, by construction: KICK-dKeptSession-5's `write_mail_ref` (its S2), which its S8
  makes the one writer behind `--mail post` and `--mail ack`, pushes only through `write_gov_ref`
  (`tools/lib/gov-ref.sh#write_gov_ref`), whose one success exit calls `write_feed_success`
  (`tools/lib/gov-feed.sh#write_feed_success`), which sets the cache ref and calls `add_feed_event`
  (`tools/lib/gov-feed.sh#add_feed_event`). A landed post therefore appends one line whose `ref` is the
  remote mail ref, `kind` `mail`, `blob` the empty tree and `commit` the post's commit. A lost,
  uncompleted, refused or duplicate post appends no line for a commit of its own; the fetch unit 5's
  S5 runs before the id may append sightings of other writers' commits (S3), and those are events
  that did happen. This unit adds no second call, and its fixture cases in
  `tools/unattended/unattended.test.sh` observe the join. Each case posts kind `question`, never
  `confirmed` or `changed`, which KICK-dKeptSession-27 S3 refuses without `--interface` at order 18,
  so these cases keep passing after that unit. Observed by AC1, AC2.
- **S2** — The census, landed and observed. `scan_feed_writers` (`tools/lib/gov-feed.sh#scan_feed_writers`)
  flags, in the files it is handed, a scope holding a lease-carrying push that calls no name on
  `FEED_WRITER_HELPER_FNS` (limb 1) and any push of a `refs/gov/` ref with no lease (limb 2). Its arm
  in `tools/lib/resolve-python.test.sh` (section "THE FEED WRITER CENSUS") hands it every tracked
  `*.sh` and hook less the suites, and plants a lease writer and a plain push of
  `refs/gov/mail/fx/a/s1`. So `write_mail_ref`, once it lands, is in the population and passes it
  through `write_gov_ref`, and no census case is added here. Narrowed to the two observations.
  Observed by AC3, AC4.
- **S3** — The sightings: a mail write this node did not make, fetched by the mailbox fetch, is
  appended by `add_feed_sightings refs/gov/remote/` (`tools/lib/gov-feed.sh#add_feed_sightings`) as
  KICK-dKeptSession-5 S5 and S6 call it after their fetches, the whole cache prefix so the walk names
  the ref `refs/gov/mail/…` (`tools/lib/gov-feed.sh#derive_feed_events`), so a message posted on node
  A is in node B's feed after B's next read. Observed by AC5.
- **S4** — The blind spot, stated: the census's own "WHAT THIS DOES NOT CHECK" names a plain push whose
  ref is spelled through a variable, a lease flag spelled in another file than its push, a writer in
  Python and a helper of a helper; a mail writer of any of those shapes escapes it. NOT OBSERVED: a
  blind spot is a statement of what the census does not check.

## 3. Non-goals (OUT)

- No feed, appender, sighting walk or census of its own: all four are TOOL-dPlacedRequest-13's, landed.
- No census case: the landed arm holds both shapes over the whole population (S2).
- No mail writer: KICK-dKeptSession-5's `write_mail_ref`.
- No mirror: the memory-mirror point is dWellOiledMachine's.
- No feed event for a mailbox prune: the close program's delete writes through `remove_gov_ref`, which
  reaches `write_gov_ref`'s deletion branch and its append.

### Edges

- **consumes-from** `KICK-dKeptSession-5` — `read_mailbox`, whose fetch the sightings follow, and `write_mail_ref`, the one mail writer this unit holds to the feed
- **consumes-from** external — TOOL-dPlacedRequest-13's `add_feed_event`, `add_feed_sightings`, `gov-feed.log` and `scan_feed_writers`, and -11's `write_gov_ref`, all landed
- **hands-off** external — the ask TOOL-dPlacedRequest-66 in dPlacedRequest's `BACKLOG.md`, filed under §8 F1, whose accept line the landed census's plain-push case already meets; closing it is dPlacedRequest's
- **hands-off** `KICK-dKeptSession-63` — S1's one feed line per landed write, which the batch's S16 holds per chained commit (id 26)

## 4. Design

### Evidence

- `write_gov_ref` calls `write_feed_success` on its one success exit, and a lost or uncompleted write
  appends nothing (`tools/lib/gov-ref.sh#write_gov_ref`, carried inline in the driver's `gov_ref_sh`
  block). The feed's line is six TAB fields, `seq`, `ref`, `kind` (the segment after `refs/gov/`),
  `blob` (the commit's tree), `commit` and `seen-utc` (`tools/lib/gov-feed.sh`, its "I4, THE CHANGE
  FEED" comment), and a gov commit's tree is the empty tree `build_gov_commit` builds.
- The census's limb 2, a plain push of a governance ref, shipped with TOOL-dPlacedRequest-13 itself
  (commit 2178069e1), and its arm's `plain.sh` case is the planted plain push of
  `refs/gov/mail/fx/a/s1` the ask TOOL-dPlacedRequest-66 names in its accept line.
- The sightings walk stops at the first commit not authored `gov-claim`, and KICK-dKeptSession-5's
  `write_mail_ref` builds every commit through `build_gov_commit` under that identity.
- Probed 2026-11-22 at c9e89a057: the census over the shipped `tools/unattended/unattended.sh`
  printed nothing, rc 0, since the driver carries the `gov_ref_sh` and `gov_feed_sh` blocks inline
  and so defines every `FEED_WRITER_HELPER_FNS` entry; over a scratch copy with a planted function
  pushing `refs/gov/mail/fx/a/s1` under `--force-with-lease` and calling no helper, it printed the
  copy's path and the push's line, 19679 (PINNED, that probe), rc 1.
- The lost race is staged as the suite's run-claim block stages one: a `git` shim on PATH that, on a
  push naming the ref, writes a racer commit into the bare origin by `update-ref` and then runs the
  real git (`tools/unattended/unattended.test.sh`, its "THE RUN CLAIM ON THE REMOTE" block, AC6).
  The racer is on the remote, and a fetch after the loss may sight it; the lost post's own commit
  never reaches the remote, so AC2 reads the feed for a commit the remote does not hold.
- A retried post derives the id of the post it retries under KICK-dKeptSession-31's eight fields as
  under unit 22's six, since neither reads the session or the clock, so AC2's duplicate holds across
  unit 31.
- Refusal sites: none. The unit edits neither `tools/unattended/unattended.sh` nor
  `tools/unattended/check-unattended.sh`, the two `REFUSAL_CEILINGS` rows of `.memory-tree.conf`
  (347 and 266, PINNED, 2026-11-22), and adds no `fail`, `exit 1` or `status=1` site anywhere.

### Shipped texts

No text states that a mail write is outside the feed, so none is rewritten. Each text read stays true:

| Text | Why it stays true |
|---|---|
| `help/loop.md`'s change-feed paragraph, anchored `verb:unattended.sh:--feed` | "every governance ref write it made or saw" covers a mail write |
| `memory/guides/UNATTENDED-STOPS.md`'s change-feed paragraph | it names claim reads as appending sightings without saying only they do; a card read sights today unnamed |
| `tools/unattended/VERBS.template.md`'s `--feed` entry, rendered to `memory/guides/UNATTENDED-VERBS.md` | the same sentence, and no closed list of the feed's kinds |
| `tools/lib/gov-ref.sh`'s I1 comment, carried in every `gov_ref_sh` copy | its head, "ONE WRITER FOR EVERY GOVERNANCE REF", covers a mail ref, and the refs it lists after are no closed set |
| `tools/lib/gov-feed.sh`'s I4 and census comments; the census arm's comment | they speak of every `refs/gov/` ref, mail included |

No `tools/policy/catalogue.toml` summary names the feed, so `.governance/policy.json` stays.

### The feed line of one post

```
41	refs/gov/mail/fx/a/6c1f0b8e…	mail	4b825dc642cb6eb9a060e54bf8d69288fbee4904	9d0e…	2026-10-26T10:02:11Z
```

### Inventory

Nothing is minted: the unit adds fixture cases, and no function, flag, field or census case.

### Files touched (estimate)

- `tools/unattended/unattended.test.sh`: the post, refusal and sighting cases, beside
  KICK-dKeptSession-5's arm, whose two-clone fixture they reuse, as inline arms that define no shell
  function, so the codebase map's symbol index, which lists the suite's functions, does not move;
  and the effective `FLOOR_ASSERTIONS` and that region's `FLOOR_SHARD_<k>` raised by the cases'
  counted assertions, with a `RAISED` line as the suite's floor paragraph has each unit write. At
  c9e89a057 they read 4077 and, for region eight where units 28's and 22's mail blocks sit, 1294
  (DERIVED, the last assignment of each in the suite); unit 5's arm raises both first. No row of
  `tools/run-gates/selftest-budgets.txt` is re-priced: the driver suite's shard rows are ESTIMATE
  rows sized by region share, carry no `plants=` token, and units 28 and 22 left them as they were.

### Alternatives rejected

- **An `add_feed_event` call in `write_mail_ref`.** It would append a second line per post, which
  `add_feed_event`'s key refuses only by accident, and it is the copy the census exists to make
  unnecessary.
- **A mail-specific census case.** Limb 1 judges any lease push whatever its ref, and the arm already
  plants a plain mail push for limb 2, so a third plant would gate an instance of a class the arm holds.

## 5. Production-readiness checklist

- security — no new write surface; the unit only proves the feed records an existing one.
- perf / scale — none added: the append is TOOL-dPlacedRequest-13's, once per landed write.
- error / empty / loading states — a lost, refused or duplicate post appends no line of its own; an
  empty census population prints a line and fails, never passes.
- observability — every landed mail write is one feed line, replayable by `--feed print`.
- risks — S4's blind spot: a mail writer added later in one of the census's unread shapes escapes it.
- testing — the fixture cases under AC1, AC2 and AC5, the direct probes AC3 and AC4, and the arm in §7.
- migration — none.
- user docs — none: the feed's verbs guide entry, TOOL-dPlacedRequest-13's, already names every
  `refs/gov/*` write.

## 6. Acceptance criteria

The fixture is KICK-dKeptSession-5's: a bare remote and two clones under `%TEMP%`, `RUN_CLAIMS` on.

- **AC1** — When clone A posts one `question` to a bare remote holding no mail ref, its
  `gov-feed.log` gains exactly one line whose `ref` is the post's remote mail ref, `kind` `mail`,
  `blob` the empty tree and `commit` the remote ref's tip.
  Red when: a landed post leaves the feed unchanged, as a planted `write_mail_ref` pushing around
  `write_gov_ref` shows.
  figure: one line, PINNED, the fixture's single post.
- **AC2** — When the same post is retried and refused as a duplicate, exit 1, A's `gov-feed.log`
  gains no line; and when a post loses its compare-and-swap, exit 1, every line the feed gains names
  a commit the bare remote holds, `git --git-dir=<bare> cat-file -e <commit>` exiting 0 for each.
  The lost race is staged by the shim §4's Evidence names, on a push naming
  `refs/gov/mail/`, so the post's fetch never reads the racer.
  Red when: a write that did not land is appended.
- **AC3** — When `bash -c '. tools/lib/gov-feed.sh && scan_feed_writers "$1"' _ <copy>` runs over a
  scratch copy of `tools/unattended/unattended.sh` holding a planted function that pushes
  `refs/gov/mail/fx/a/s1` with `--force-with-lease` and calls no helper, it prints that copy's
  `<file>:<line>`, the planted push's line, and exits 1.
  Red when: the planted mail writer passes the census.
- **AC4** — When the same probe runs over the shipped `tools/unattended/unattended.sh` after
  KICK-dKeptSession-5 lands, it prints nothing, rc 0; and `awk '/^write_mail_ref\(\)/,/^}/'
  tools/unattended/unattended.sh | grep -v '^[[:space:]]*#' | grep -cw push` prints 0 while the
  same body calls `write_gov_ref`.
  Red when: the shipped mail writer is flagged, or pushes around `write_gov_ref`.
- **AC5** — When clone B's `fy` posts a `question` to `build:fx` and clone A then runs
  `unattended.sh --mail read fx`, A's feed gains one line for B's commit, its `ref` under
  `refs/gov/mail/fy/` and `kind` `mail`.
  Red when: a fetched mail write is not sighted.

## 7. Gates

`unattended kit gate` · `python resolver (behaviour + inline parity + idiom ban)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC5 · a landed post, a duplicate and a lost post, and a sighted foreign post, staged against a planted writer pushing around `write_gov_ref` · the effective `FLOOR_ASSERTIONS` (4077 at c9e89a057, DERIVED) and its region's `FLOOR_SHARD_<k>` rise by its counted assertions, over unit 5's raise

## 8. Open questions

- **F1 — Which planted shape does the red case use, given the census reads only lease pushes?**
  (a) Plant the `--force-with-lease` shape the census reads, state the blind spot, and file an ask for
  dPlacedRequest: "accept `scan_feed_writers` also flags a line pushing a `refs/gov/` ref without
  `--force-with-lease`, seen red on a planted plain push of `refs/gov/mail/fx/a/s1`"; (b) widen the
  census in this unit; (c) plant the lease shape and file nothing. (b) edits TOOL-dPlacedRequest-13's
  mechanism, which this build's brief forbids; (c) leaves the gap unrecorded. Rung 3, the most capable
  option that edits no parent spec: (a), the ask filed by the main loop.
  RESOLVED (agent, 2026-10-26, delegated): (a). widens: none · relaxes: none
  At base c2a407b0 the ask stands as TOOL-dPlacedRequest-66 and the landed census meets it, so no
  plant is added here (S2).

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.
- rev-2 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-63` mirrored, the other ends of
  the edges the round-3 promotions' audit's disposal declared
- rev-3 · 2026-11-21 · §1 · S1 S2 S4 · §3 · §4 · §5 · AC3 AC4 · §7 · §8 F1 · §10 · re-grounded on base
  c2a407b0 by brief 2026-11-21-prompt-KICK-dKeptSession-5-orders-16-17-reground-brief: the feed, the
  appender and the census are landed in `tools/lib/gov-feed.sh`, and the census's limb 2 and its
  planted plain mail push already meet the F1 ask, TOOL-dPlacedRequest-66; S3's sightings prefix
  corrected to `refs/gov/remote/`, under which the walk names the mail ref. Narrowed: S2's census case
  and the `tools/lib/resolve-python.test.sh` arm are dropped, AC3 and AC4 reduced to direct probes of
  `scan_feed_writers`, and S4's blind spot restated from the census's own list.
- rev-4 · 2026-11-21 · S1 · §4 · AC2 · AC3 · AC5 · §7 · checked for behaviour under
  `2026-11-21-prompt-KICK-dKeptSession-23-precheck-brief`: AC2's lost post is staged by a git shim
  between the fetch and the push, since a planted tip the post's fetch reads is sighted and appends a
  line; AC3 names the census's `<file>:<line>` and exit 1, as a scratch copy shows; AC5 posts from `fy`
  to `build:fx` and reads `fx`, unit 5 AC4's shape; S1's cases post `question`, which unit 27's
  `--interface` refusal never reaches; Files touched names the floor the cases raise and states
  `symbols.json` does not move. Nothing narrowed: no landed unit since rev-3 touches the feed or the
  driver.
- rev-5 · 2026-11-22 · S1 · S2 · S3 · §4 · AC1 · AC2 · AC3 · AC4 · §7 · §10 · re-grounded at
  c9e89a057 by 2026-11-22-prompt-KICK-dKeptSession-23-reground-brief, units 5 and 31 read as landed:
  S1 names `--mail ack` as a writer and says a post's fetch may sight others' commits, so AC1 starts
  on an empty remote and AC2's lost case reads for a commit the remote lacks; S2 says the arm, not the
  census, picks the population; S3 adds the post's sighting; AC4 gains its command; §4 gains the census
  probe, the shim's source, the id across unit 31, the refusal-site and floor figures and Shipped
  texts, none rewritten. Nothing narrowed.

## 10. Reuse audit

The seams are TOOL-dPlacedRequest-13's, landed: the join at `write_gov_ref`'s success exit, the
sightings walk `add_feed_sightings` and the census `scan_feed_writers`
(`tools/lib/gov-feed.sh#scan_feed_writers`), whose arm in `tools/lib/resolve-python.test.sh` already
holds both writer shapes. The probe `python tools/codebase-map/reuse_lookup.py "every ref write
appended to the node change feed and a census of writers"`, re-run 2026-11-22 at c9e89a057, ranked `write`, `write_text`, `census`
(`tools/memory-tree/merge-rows.py`), `write_record` and `write_change` by name stem; none is the feed,
which the map does not rank, so the seam is the landed feed library read directly, and no other
existing seam fits.

Recall terms used: `python tools/memory-recall/query.py "is every mail write recorded in the change
feed" --terms "change feed gov-feed.log census scan_feed_writers write_gov_ref add_feed_event mail
append limb plain push"`
