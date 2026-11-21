# KICK-dKeptSession-23 — every mail write appended to the change feed once its ref update lands, inside the feed's census

**Status:** DEFERRED · rev-3 · 2026-11-21 · node a · Tier-2 · base c2a407b0 · streams kickoff · order 17 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0161@10c6cad1 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md) | research | KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-10 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-1 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-build-KICK-dKeptSession-23-deviation-231.md](../build/2026-10-26-build-KICK-dKeptSession-23-deviation-231.md) | deviation | — |
| [2026-11-21-build-KICK-dKeptSession-45-reground-orders-14-19-returns.md](../build/2026-11-21-build-KICK-dKeptSession-45-reground-orders-14-19-returns.md) | research | KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-36 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-1 |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief-2.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief-2.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-1-build-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-33 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-34 KICK-dKeptSession-40 KICK-dKeptSession-4 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-54 KICK-dKeptSession-20 KICK-dKeptSession-32 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-30 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-22 KICK-dKeptSession-31 KICK-dKeptSession-5 KICK-dKeptSession-36 KICK-dKeptSession-39 KICK-dKeptSession-51 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-35 KICK-dKeptSession-42 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-43 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-55 KICK-dKeptSession-17 KICK-dKeptSession-61 KICK-dKeptSession-18 KICK-dKeptSession-41 KICK-dKeptSession-44 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-11-21-prompt-KICK-dKeptSession-5-orders-16-17-reground-brief.md](../prompts/2026-11-21-prompt-KICK-dKeptSession-5-orders-16-17-reground-brief.md) | research | KICK-dKeptSession-5 KICK-dKeptSession-39 KICK-dKeptSession-51 |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |

<!-- /gen:spec-records -->

## 1. Goal

The change feed is how a mirror follows governance state without a change to the core (the owner's
NT-14), and the observer clock reads its first sightings. Every mail write lands in it once its ref
update lands, and in no other case, because the one mail writer reaches the remote only through the
one writer whose success exit appends; and the feed's census, landed with TOOL-dPlacedRequest-13, holds
that true over every tracked shell file, so this unit observes the join on the mail writer it guards.

## 2. Scope (IN)

- **S1** — The join, by construction: KICK-dKeptSession-5's `write_mail_ref`, the only writer of a mail
  ref, pushes only through `write_gov_ref` (`tools/lib/gov-ref.sh#write_gov_ref`), whose one success
  exit calls `write_feed_success`, which sets the cache ref and calls `add_feed_event`
  (`tools/lib/gov-feed.sh#add_feed_event`). A landed post therefore appends one line whose `ref` is the
  remote mail ref, `kind` `mail`, `blob` the empty tree and `commit` the post's commit; a lost,
  uncompleted, refused or duplicate post appends nothing. This unit adds no second call, and its
  fixture cases in `tools/unattended/unattended.test.sh` observe the join. Observed by AC1, AC2.
- **S2** — The census, landed and observed. `scan_feed_writers` (`tools/lib/gov-feed.sh#scan_feed_writers`)
  already reads every tracked `*.sh` and hook less the suites, flags a scope holding a lease-carrying
  push that calls no name on `FEED_WRITER_HELPER_FNS` (limb 1) and any plain push of a `refs/gov/` ref
  (limb 2), and its arm in `tools/lib/resolve-python.test.sh` (section "THE FEED WRITER CENSUS") plants
  a lease writer and a plain push of `refs/gov/mail/fx/a/s1`. So `write_mail_ref`, once it lands, is in
  the population and passes it through `write_gov_ref`, and no census case is added here. Narrowed to
  the two observations. Observed by AC3, AC4.
- **S3** — The sightings: a mail write this node did not make, fetched by `read_mailbox`'s fetch, is
  appended by `add_feed_sightings refs/gov/remote/` (`tools/lib/gov-feed.sh#add_feed_sightings`) as
  KICK-dKeptSession-5 S6 calls it, the whole cache prefix so the walk names the ref `refs/gov/mail/…`
  (`tools/lib/gov-feed.sh#derive_feed_events`), so a message posted on node A is in node B's feed after B's next
  read. Observed by AC5.
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

### The feed line of one post

```
41	refs/gov/mail/fx/a/6c1f0b8e…	mail	4b825dc642cb6eb9a060e54bf8d69288fbee4904	9d0e…	2026-10-26T10:02:11Z
```

### Inventory

Nothing is minted: the unit adds fixture cases, and no function, flag, field or census case.

### Files touched (estimate)

- `tools/unattended/unattended.test.sh`: the post, refusal and sighting cases

### Alternatives rejected

- **An `add_feed_event` call in `write_mail_ref`.** It would append a second line per post, which
  `add_feed_event`'s key refuses only by accident, and it is the copy the census exists to make
  unnecessary.
- **A mail-specific census case.** Limb 1 judges any lease push whatever its ref, and the arm already
  plants a plain mail push for limb 2, so a third plant would gate an instance of a class the arm holds.

## 5. Production-readiness checklist

- security — no new write surface; the unit only proves the feed records an existing one.
- perf / scale — none added: the append is TOOL-dPlacedRequest-13's, once per landed write.
- error / empty / loading states — a lost, refused or duplicate post appends nothing; an empty census
  population prints a line and fails, never passes.
- observability — every landed mail write is one feed line, replayable by `--feed print`.
- risks — S4's blind spot: a mail writer added later in one of the census's unread shapes escapes it.
- testing — the fixture cases under AC1, AC2 and AC5, the direct probes AC3 and AC4, and the arm in §7.
- migration — none.
- user docs — none: the feed's verbs guide entry, TOOL-dPlacedRequest-13's, already names every
  `refs/gov/*` write.

## 6. Acceptance criteria

The fixture is KICK-dKeptSession-5's: a bare remote and two clones under `%TEMP%`, `RUN_CLAIMS` on.

- **AC1** — When clone A posts one message, its `gov-feed.log` gains exactly one line whose `ref` is the
  post's remote mail ref, `kind` `mail` and `commit` the remote ref's tip.
  Red when: a landed post leaves the feed unchanged, as a planted `write_mail_ref` pushing around
  `write_gov_ref` shows.
- **AC2** — When the same post is retried and refused as a duplicate, and when a post loses its
  compare-and-swap against a planted remote tip, A's `gov-feed.log` gains no line in either case.
  Red when: a write that did not land is appended.
- **AC3** — When `bash -c '. tools/lib/gov-feed.sh && scan_feed_writers "$1"' _ <copy>` runs over a
  scratch copy of `tools/unattended/unattended.sh` holding a planted function that pushes
  `refs/gov/mail/fx/a/s1` with `--force-with-lease` and calls no helper, it prints that copy's line.
  Red when: the planted mail writer passes the census.
- **AC4** — When the same probe runs over the shipped `tools/unattended/unattended.sh` after
  KICK-dKeptSession-5 lands, it prints nothing, and `write_mail_ref` carries no push of its own.
  Red when: the shipped mail writer is flagged, or pushes around `write_gov_ref`.
- **AC5** — When clone B posts a message and clone A then runs `unattended.sh --mail read fy`, A's feed
  gains one line for B's commit, `kind` `mail`.
  Red when: a fetched mail write is not sighted.

## 7. Gates

`unattended kit gate` · `python resolver (behaviour + inline parity + idiom ban)` · `memory hygiene` · `spec tokens (a spec's own names resolve)`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC5 · a landed post, a duplicate and a lost post, and a sighted foreign post, staged against a planted writer pushing around `write_gov_ref` · none

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

## 10. Reuse audit

The seams are TOOL-dPlacedRequest-13's, landed: the join at `write_gov_ref`'s success exit, the
sightings walk `add_feed_sightings` and the census `scan_feed_writers`
(`tools/lib/gov-feed.sh#scan_feed_writers`), whose arm in `tools/lib/resolve-python.test.sh` already
holds both writer shapes. The probe `python tools/codebase-map/reuse_lookup.py "every ref write
appended to the node change feed and a census of writers"` ranked `write`, `write_text`, `census`
(`tools/memory-tree/merge-rows.py`), `write_record` and `write_change` by name stem; none is the feed,
which the map does not rank, so the seam is the landed feed library read directly, and no other
existing seam fits.

Recall terms used: `python tools/memory-recall/query.py "is every mail write recorded in the change
feed" --terms "change feed gov-feed.log census scan_feed_writers write_gov_ref add_feed_event mail
append limb plain push"`
