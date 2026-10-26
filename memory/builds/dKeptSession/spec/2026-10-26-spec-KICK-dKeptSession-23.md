# KICK-dKeptSession-23 — every mail write appended to the change feed once its ref update lands, inside the feed's census

**Status:** DEFERRED · rev-2 · 2026-10-26 · node a · Tier-2 · base 462d20f3 · streams kickoff · order 17 · advances KICK-dKeptSession-29

**Carries:** cl-dClosedLoop-0161@10c6cad1 whole

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md](../build/2026-10-26-build-KICK-dKeptSession-1-agent-ledger.md) | journal | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-30 KICK-dKeptSession-31 KICK-dKeptSession-32 KICK-dKeptSession-33 KICK-dKeptSession-34 KICK-dKeptSession-35 KICK-dKeptSession-36 KICK-dKeptSession-37 KICK-dKeptSession-38 KICK-dKeptSession-39 KICK-dKeptSession-40 KICK-dKeptSession-41 KICK-dKeptSession-42 KICK-dKeptSession-43 KICK-dKeptSession-44 KICK-dKeptSession-45 KICK-dKeptSession-46 KICK-dKeptSession-47 KICK-dKeptSession-48 KICK-dKeptSession-49 KICK-dKeptSession-50 KICK-dKeptSession-51 KICK-dKeptSession-52 KICK-dKeptSession-53 KICK-dKeptSession-54 KICK-dKeptSession-55 KICK-dKeptSession-56 KICK-dKeptSession-57 KICK-dKeptSession-58 KICK-dKeptSession-59 KICK-dKeptSession-60 KICK-dKeptSession-61 KICK-dKeptSession-62 KICK-dKeptSession-63 KICK-dKeptSession-64 KICK-dKeptSession-65 |
| [2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md](../build/2026-10-26-build-KICK-dKeptSession-1-reuse-scout-b.md) | research | KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-10 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-27 KICK-dKeptSession-28 KICK-dKeptSession-1 |
| [2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md](../build/2026-10-26-build-KICK-dKeptSession-1-spec-stage-returns.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-build-KICK-dKeptSession-23-deviation-231.md](../build/2026-10-26-build-KICK-dKeptSession-23-deviation-231.md) | deviation | — |
| [2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md](../prompts/2026-10-26-prompt-KICK-dKeptSession-1-spec-brief.md) | research | KICK-dKeptSession-1 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-5 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-9 KICK-dKeptSession-10 KICK-dKeptSession-11 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-14 KICK-dKeptSession-15 KICK-dKeptSession-16 KICK-dKeptSession-17 KICK-dKeptSession-18 KICK-dKeptSession-19 KICK-dKeptSession-20 KICK-dKeptSession-21 KICK-dKeptSession-22 KICK-dKeptSession-24 KICK-dKeptSession-25 KICK-dKeptSession-26 KICK-dKeptSession-27 KICK-dKeptSession-28 |
| [2026-10-26-review-KICK-dKeptSession-1-spec-audit.md](../reviews/2026-10-26-review-KICK-dKeptSession-1-spec-audit.md) | spec-audit | KICK-dKeptSession-1 KICK-dKeptSession-19 KICK-dKeptSession-2 KICK-dKeptSession-3 KICK-dKeptSession-4 KICK-dKeptSession-20 KICK-dKeptSession-16 KICK-dKeptSession-12 KICK-dKeptSession-13 KICK-dKeptSession-26 KICK-dKeptSession-15 KICK-dKeptSession-14 KICK-dKeptSession-9 KICK-dKeptSession-28 KICK-dKeptSession-22 KICK-dKeptSession-5 KICK-dKeptSession-27 KICK-dKeptSession-24 KICK-dKeptSession-10 KICK-dKeptSession-25 KICK-dKeptSession-21 KICK-dKeptSession-6 KICK-dKeptSession-7 KICK-dKeptSession-8 KICK-dKeptSession-11 KICK-dKeptSession-17 KICK-dKeptSession-18 |

<!-- /gen:spec-records -->

## 1. Goal

The change feed is how a mirror follows governance state without a change to the core (the owner's
NT-14), and the observer clock reads its first sightings. Every mail write lands in it once its ref
update lands, and in no other case, because the one mail writer reaches the remote only through the
one writer whose success exit appends; and the feed's census holds that true, red on a planted mail
write that skips the append (the answers' review).

## 2. Scope (IN)

- **S1** — The join, by construction: KICK-dKeptSession-5's `write_mail_ref`, the only writer of a mail
  ref, pushes only through `write_gov_ref`, whose one success exit sets the cache ref and calls
  `add_feed_event` (TOOL-dPlacedRequest-13 S3). A landed post therefore appends one line whose `ref` is
  the remote mail ref, `kind` `mail`, `blob` the empty tree and `commit` the post's commit; a lost,
  uncompleted, refused or duplicate post appends nothing. This unit adds no second call. Observed by
  AC1, AC2.
- **S2** — The census arm: a case of TOOL-dPlacedRequest-13 S9's `scan_feed_writers` over a scratch copy
  of `tools/unattended/unattended.sh` holding a planted mail writer, a function that pushes
  `refs/gov/mail/…` with `--force-with-lease` and calls neither `add_feed_event` nor `write_gov_ref`;
  the census prints that copy's line. Over the shipped driver it prints nothing, so `write_mail_ref`
  is inside the census's population and passes it. Observed by AC3, AC4.
- **S3** — The sightings: a mail write this node did not make, fetched by `read_mailbox`'s fetch, is
  appended by `add_feed_sightings refs/gov/remote/mail/` (TOOL-dPlacedRequest-13 S4) as KICK-dKeptSession-5
  S6 calls it, so a message posted on node A is in node B's feed after B's next read. Observed by AC5.
- **S4** — The blind spot, stated: the census reads a line carrying both `push` and
  `--force-with-lease` (TOOL-dPlacedRequest-13 §4 "The census"), so a mail write by a plain `git push`
  or from a Python file escapes it. This unit plants the shape the census reads and files the wider
  census as an ask (§8 F1). NOT OBSERVED: a blind spot is a statement of what the arm does not check.

## 3. Non-goals (OUT)

- No feed, appender, sighting walk or census of its own: all four are TOOL-dPlacedRequest-13's.
- No mail writer: KICK-dKeptSession-5's `write_mail_ref`.
- No mirror: the memory-mirror point is dWellOiledMachine's.
- No feed event for a mailbox prune: the close program's delete writes through `write_gov_ref`, whose
  deletion branch TOOL-dPlacedRequest-13 S3 already appends.

### Edges

- **consumes-from** `KICK-dKeptSession-5` — `read_mailbox`, whose fetch the sightings follow, and `write_mail_ref`, the one mail writer this unit holds to the feed
- **consumes-from** external — TOOL-dPlacedRequest-13's `add_feed_event`, `add_feed_sightings`, `gov-feed.log` and `scan_feed_writers`, and -11's `write_gov_ref`
- **hands-off** external — the ask for dPlacedRequest that the census also read a `refs/gov/` push with no lease, §8 F1
- **hands-off** `KICK-dKeptSession-63` — S1's one feed line per landed write, which the batch's S16 holds per chained commit (id 26)

## 4. Design

### Evidence

- `write_gov_ref`'s success exit appends the event and a lost or uncompleted write appends nothing
  (TOOL-dPlacedRequest-13 S3); `kind` is the segment after `refs/gov/`, derived from `ref`, and `blob`
  the commit's tree, the empty tree for a gov commit (its §4 "The file").
- The census flags a line carrying both `push` and `--force-with-lease` in a function whose body calls
  neither `add_feed_event` nor `write_gov_ref`, and an empty population reds it (its §4 "The census").
- `git grep -n -- --force-with-lease -- tools/unattended/unattended.sh` finds the push at `:2423` in
  `write_claim` at this base; TOOL-dPlacedRequest-11 moves it into `write_gov_ref`.
- The sightings walk stops at the first commit not authored `gov-claim` (TOOL-dPlacedRequest-13 S4),
  and KICK-dKeptSession-5's `write_mail_ref` builds every commit through `build_gov_commit` under that
  identity (scout B's disagreement 5).

### The feed line of one post

```
41	refs/gov/mail/fx/a/6c1f0b8e…	mail	4b825dc642cb6eb9a060e54bf8d69288fbee4904	9d0e…	2026-10-26T10:02:11Z
```

### Inventory

Nothing is minted: the unit adds a census case and fixture cases, and no function, flag or field.

### Files touched (estimate)

- `tools/lib/resolve-python.test.sh`: the planted mail writer case of the census arm
- `tools/unattended/unattended.test.sh`: the post, refusal and sighting cases

### Alternatives rejected

- **An `add_feed_event` call in `write_mail_ref`.** It would append a second line per post, which
  `add_feed_event`'s key refuses only by accident, and it is the copy the census exists to make
  unnecessary.
- **Planting a plain `git push`.** The census does not read that shape, so the planted case would
  pass green and prove nothing (scout B's disagreement 4).

## 5. Production-readiness checklist

- security — no new write surface; the unit only proves the feed records an existing one.
- perf / scale — none added: the append is TOOL-dPlacedRequest-13's, once per landed write.
- error / empty / loading states — a lost, refused or duplicate post appends nothing; an empty census
  population reds the arm, never passes it.
- observability — every landed mail write is one feed line, replayable by `--feed print`.
- risks — S4's blind spot: a mail writer added later by a plain push or in Python escapes the census
  until the ask lands.
- testing — the fixture cases under AC1 to AC5 and the suite arms in §7.
- migration — none.
- user docs — none: the feed's verbs guide section, TOOL-dPlacedRequest-13's, already names every
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
- **AC3** — When `scan_feed_writers` runs over a scratch copy of `unattended.sh` with a planted
  function pushing `refs/gov/mail/fx/a/s1` with `--force-with-lease` and no append, it prints that
  copy's line.
  Red when: the planted mail writer passes the census.
- **AC4** — When `scan_feed_writers` runs over the shipped `unattended.sh`, it prints nothing, and its
  population holds the push inside `write_gov_ref` that `write_mail_ref` calls.
  Red when: the census population is empty, or the shipped mail writer is flagged.
- **AC5** — When clone B posts a message and clone A then runs `unattended.sh --mail read fy`, A's feed
  gains one line for B's commit, `kind` `mail`.
  Red when: a fetched mail write is not sighted.

## 7. Gates

`unattended kit gate` · `python resolver (behaviour + inline parity + idiom ban)` · `memory hygiene`

New arm: tools/lib/resolve-python.test.sh · covers AC3 AC4 · the census over a planted mail writer that skips the append, staged in a scratch copy of the driver · none
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

## 9. Revision log

- rev-1 · 2026-10-26 · initial draft.
- rev-2 · 2026-10-26 · §3 · the Edges bullet to `KICK-dKeptSession-63` mirrored, the other ends of
  the edges the round-3 promotions' audit's disposal declared

## 10. Reuse audit

The seams are TOOL-dPlacedRequest-13's: the join at `write_gov_ref`'s success exit (S3), the sightings
walk (S4) and the census `scan_feed_writers` (S9), run by `tools/lib/resolve-python.test.sh`, which
already holds the `PARITY_ROWS` loop (`:168-233`). The probe `python tools/codebase-map/reuse_lookup.py
"every ref write appended to the node change feed and a census of writers"` ranked `write`, `census`
(`tools/memory-tree/merge-rows.py`) and `write_record` by name stem; none is the feed, which is unbuilt,
so the seam is the parent spec's, and no existing code seam fits beyond it. Scout B's row 6 and its
disagreement 4 agree with TOOL-dPlacedRequest-13 §4 "The census" as written.

Recall terms used: `python tools/memory-recall/query.py "is every mail write recorded in the change
feed" --terms "change feed gov-feed.log census scan_feed_writers write_gov_ref add_feed_event mail
append"`
