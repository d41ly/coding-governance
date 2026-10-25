# TOOL-dPlacedRequest-27 — the change feed skips only an immediate retry: the append-once test reads the ref's newest event

**Status:** OPEN · rev-1 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 3 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-23-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-23-promoted-fix-return.md) | research | TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |
| [2026-10-25-build-TOOL-dPlacedRequest-27-deviation-271.md](../build/2026-10-25-build-TOOL-dPlacedRequest-27-deviation-271.md) | deviation | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build, round 1
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md`),
confirmed **finding 52 at HIGH**, its item **H6**. `TOOL-dPlacedRequest-13` S1-S2 keys an event by
(`ref`, `blob`, `commit`) and appends only when no line of the whole file carries that key. Every
deletion is (`-`, 40 zeros), and a ref set back to a commit it once held repeats its old key, so every
clear of `refs/gov/bar-red` after the first, which `remove_red_ref` makes on every green
(`tools/run-gates/post-merge.sh:301`, called at `:392`), and a second red on one main sha are silently
missing; a replay from `--from <seq>` shows the bar red when it is green. The finder's fix was judged
unsound, since any whole-file key drops a genuine repeat; this unit builds the skeptic's corrected fix.
It repairs `TOOL-dPlacedRequest-13`: an event is skipped only when the ref's newest event already
carries the same `blob` and `commit`, so only an immediate retry of one write appends nothing.

## 2. Scope (IN)

- **S1** — The append test. `add_feed_event <ref> <commit or empty>`, under its lock, reads the newest
  line of the feed whose `ref` field equals `<ref>` and appends unless that line's `blob` and `commit`
  equal the new event's. A write, a deletion, the same write and a deletion of one ref on one sha
  append four lines; an identical event repeated with nothing between appends one. Observed by AC1.
- **S2** — The sightings agree. `add_feed_sightings`' "a cached ref whose tip the feed does not hold"
  reads as a cached ref whose tip is not the commit of the feed's newest line for that ref, and the
  walk stops at that newest line's commit; so a ref another node set back to a commit this feed holds
  in an older line is sighted again. Observed by AC3.
- **S3** — The check agrees. `check_feed`'s duplicate rule becomes two consecutive events of one ref,
  in file order, with one `blob` and `commit`; a repeat with another event of that ref between is
  legal. `missing` and `extra` are unchanged. Observed by AC2.
- **S4** — The key's statement. `TOOL-dPlacedRequest-13` S1's sentence "The key is (`ref`, `blob`,
  `commit`)" stands for what identifies an event; the append-once rule is S1 here. The stops guide's
  section 7 sentence naming the feed (`tools/unattended/STOPS.template.md`, rendered to
  `memory/guides/UNATTENDED-STOPS.md`) says a retry appends nothing and a repeat later appends again.
  Observed by AC4.

## 3. Non-goals (OUT)

- No `seq` in the key: `seq` is node-local and assigned at the append, so a retry would never share
  one.
- No change to the deletion's encoding: `blob` `-` and 40 zeros stay `TOOL-dPlacedRequest-13` S1's.
- The criterion "two deletions of one ref with a re-create between them leave two deletion lines" is
  finding 2's, the medium twin of this defect, an item of `TOOL-dPlacedRequest-34` observed over this
  rule.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-13` — `add_feed_event`, `add_feed_sightings`, `check_feed` and `gov-feed.log`, whose append-once rule this unit narrows; without them there is no feed to key
- **hands-off** `TOOL-dPlacedRequest-34` — the per-ref append rule, which that unit's item for finding 2 observes over repeated deletions

## 4. Design

### The test

```
under gov-feed.lock:
  last = the newest line whose field 2 == ref      (one awk over the file, keeping the last match)
  last's fields 4 and 5 == (blob, commit)  -> release, return 0
  otherwise                                -> seq + 1, append, write the counter, release
```

The `awk` reads the whole file, as the `grep -qF` it replaces did, so the cost is unchanged: one pass
per write.

### What a retry is now

A caller retries when a write landed but its caller did not learn so, and the retry appends the same
event; nothing of that ref can land between, because the retrying writer's own compare-and-swap
expects the tip it wrote. A later write of the same value comes after some other event of the ref, so
it appends.

### Files touched (estimate)

- `tools/lib/gov-feed.sh`: the append test, the sightings' stop and the check's duplicate rule
- `tools/unattended/unattended.sh`: the inline block, carried
- `tools/run-gates/post-merge.sh`: the inline block, carried
- `tools/unattended/unattended.test.sh`: the repeat arms
- `tools/unattended/STOPS.template.md`: section 7's feed sentence
- `memory/guides/UNATTENDED-STOPS.md`: its render

### Alternatives rejected

- **Key a deletion by the tip it deleted.** A write of X, a deletion and a write of X repeats the first
  write's key, so the re-set is still dropped (the skeptic's reading of finding 52).
- **Key by (`ref`, old tip, new tip).** absent-to-X repeats in the same sequence.
- **Skip the test for deletions.** A retried deletion then appends twice, the defect the key exists to
  stop.

## 5. Production-readiness checklist

- security — none: the same file, the same fields.
- perf / scale — one `awk` over the file per append, replacing one `grep`.
- error / empty / loading states — a ref with no line appends; an unreadable file is the existing
  `feed: NOTE -` line and rc 0.
- observability — a replay shows every clear of `bar-red`.
- risks — a caller that retries after another write of the same ref landed appends its event again;
  that event happened, so the feed is still true.
- testing — the probes of §6 and the arm in §7.
- migration — none: no feed exists before this build lands.
- user docs — `memory/guides/UNATTENDED-STOPS.md` section 7; no `help/` page covers the kit.

## 6. Acceptance criteria

The fixture is `TOOL-dPlacedRequest-13` AC1's scratch clone and bare origin.

- **AC1** — When a probe writes `refs/gov/bar-red` to main commit X, deletes it, writes X again and
  deletes it again, each through `write_gov_ref`, `gov-feed.log` holds four lines for that ref in that
  order, and a fifth call of `add_feed_event refs/gov/bar-red` with an empty commit appends nothing.
  Red when: the third or fourth event is dropped, the planted case being a scratch copy of the block
  whose test greps the whole file.
- **AC2** — When `check_feed` reads the AC1 feed it exits 0; with the fourth line duplicated in place
  it exits 1 printing `duplicate`.
  Red when: a legal repeat reads as a duplicate, or an adjacent one does not.
- **AC3** — When a second clone sets a lone-commit ref back to a commit this feed holds in an older
  line and the first clone fetches into `refs/gov/remote/` and calls `add_feed_sightings
  refs/gov/remote/`, the feed gains one line for it.
  Red when: a re-set another node made is never sighted.
- **AC4** — When `grep -n 'retry' tools/unattended/STOPS.template.md` runs, a section 7 line about the
  feed says a retry appends nothing and a later repeat appends.
  Red when: the guide still states a whole-file key.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `python resolver (behaviour + inline parity + idiom ban)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `spawn budget (forks per hot entrypoint)` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 · the repeat arms over a write, delete, write, delete sequence and a re-set sighting, staged by a scratch copy whose test greps the whole file · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — What does the append-once test compare?** (a) The ref's newest event; (b) the whole file, by
  a richer key; (c) nothing, appending every call. (b) drops a genuine repeat under any key without a
  sequence, as the skeptic showed; (c) appends a retried write twice. RESOLVED (agent, 2026-10-25,
  delegated): (a), rung 3, the skeptic's corrected fix. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit's finding 52 (HIGH, item H6).

## 10. Reuse audit

The seam extended is `TOOL-dPlacedRequest-13`'s `add_feed_event` in the `gov_feed_sh` block; its lock,
counter and line stay, and only the test before the append changes. The deletion's writer is
post-merge's `remove_red_ref` (`tools/run-gates/post-merge.sh:301`, called at `:392`), read at source.
`python tools/codebase-map/reuse_lookup.py "append an event only when the ref's newest event differs"`
ranked `add_health_event`, `check_gen_region_only` and `check_lease_only_diff`, name stems only; the
health log's appender keeps no per-key rule, so no existing seam fits beyond the unit this repairs.
`python tools/memory-recall/query.py "how does the feed avoid appending a retried write twice"`
returned the spec brief's unit 13 row, the audit's H6 and unit 13's §4; none disagrees with source.

Recall terms used: gov-feed.log key append-once retry deletion bar-red seq ref blob commit
