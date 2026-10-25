# TOOL-dPlacedRequest-47 — the bounded age walk never compares an unsighted commit with the threshold

**Status:** DEFERRED · rev-4 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 24 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-44-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-44-promoted-fix-return.md) | research | TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 |
| [2026-10-25-build-TOOL-dPlacedRequest-47-deviation-471.md](../build/2026-10-25-build-TOOL-dPlacedRequest-47-deviation-471.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-47-deviation-472.md](../build/2026-10-25-build-TOOL-dPlacedRequest-47-deviation-472.md) | deviation | — |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-35 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-44-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-44-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 |
| [2026-10-25-review-TOOL-dPlacedRequest-44-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-44-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-2 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md`)
confirmed **finding 33 at HIGH**, its item **H3**, which holds no other finding.
`TOOL-dPlacedRequest-35` §4 tests `seen-utc < threshold -> resolve stale` as an `awk` string compare,
and nothing in S1 or §4 guards a commit the feed has not sighted. In `awk` an unset `seen-utc` is the
empty string and the feed's `-` placeholder (`TOOL-dPlacedRequest-17` S1) is `-`, and both sort before
every ISO stamp; probed 2026-10-25 on node a, `awk` printed both as below `2026-10-24T14:00:00Z`.
`TOOL-dPlacedRequest-35` §5 covers only an unsighted tenure start. So over an empty or missing feed
(a fresh upgrade before `--feed rebuild`, a deleted feed) or a tip not yet sighted, every affected
row reads `stale` and may be taken over, where `TOOL-dPlacedRequest-17` S3 and AC6 require `unknown`
and never `stale`. This unit repairs `TOOL-dPlacedRequest-35`, at order 23, so it sits at order 24.

## 2. Scope (IN)

- **S1** — The sighted guard. The threshold test reads `seen-utc` set and not `-`, and `seen-utc`
  below the threshold; an unsighted commit is never compared. A non-renewing unsighted commit inside
  the tenure is read on, and it still becomes the oldest commit of the tenure. Observed by AC1 and AC2.
- **S2** — The unsighted outcomes. An unsighted tip resolves the tail `unknown` with age `-` at once;
  an unsighted renewing beat resolves it `unknown` with age `-`; a fallback aged from an unsighted
  oldest commit resolves `unknown` with age `-`, as `TOOL-dPlacedRequest-26` S3 states. No path from
  an unsighted commit reaches `stale`. Observed by AC1, AC2 and AC3.

## 3. Non-goals (OUT)

- No change to the observer clock or to what the feed records: `TOOL-dPlacedRequest-17` S1 and
  `TOOL-dPlacedRequest-13`.
- No `-` class of `renews`: finding 32's, `TOOL-dPlacedRequest-46`.
- No rebuild of a missing feed: `--feed rebuild` is `TOOL-dPlacedRequest-13`'s.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-35` — S1's threshold test and S2's fallback inside the age pass's `awk`, which this unit guards against an unsighted commit; without them there is no compare to guard
- **hands-off** `TOOL-dPlacedRequest-50` — S1's guard, AC1 and AC3, which that unit observes with a new AC4 and restates in place so each criterion reaches the stop it names
- **hands-off** `TOOL-dPlacedRequest-52` — the sighted test and the walk, which that unit's items for findings 34 and 36 make a shape test and merge with `TOOL-dPlacedRequest-46`'s walk
- **hands-off** `TOOL-dPlacedRequest-56` — AC4's rows and arm, which that unit's item for finding 15 extends with the torn-stamp row

## 4. Design

### The walk, per tail

```
per tail, tip first, tip included:
  tip unsighted                               -> resolve unknown, age -                (S2)
  tip                                         -> tenure epoch = its epoch (absent reads 0)
  epoch != tenure epoch                       -> tenure ended: resolve by 35 S2
  renews yes or absent                        -> renewing beat: unsighted ? unknown : age from its sighting
  seen-utc set, not -, and seen-utc < threshold -> resolve stale                     (S1)
  else                                        -> oldest-of-tenure = this commit, read on
chain or tenure ended                         -> 35 S2's fallback; an unsighted oldest reads unknown
```

The guard sits on the compare, not on the commit, because an unsighted commit inside a tenure says
nothing about age either way: it neither proves the tenure fresh nor stale.

### Evidence

- `TOOL-dPlacedRequest-35` §4 line `seen-utc < threshold -> resolve stale` and its §5 "an unsighted
  tenure start reads `unknown`".
- `TOOL-dPlacedRequest-17` S3: "a row whose tip or renewing beat the feed has not sighted reads
  `unknown` with age `-`, never `stale`"; its AC6 deletes the feed and expects every row `unknown`.
- Today's verdict `awk` already maps an unaged row to `unknown` (`tools/unattended/unattended.sh:2181`,
  `if ($10 != 1 || a == "-") { vd = "unknown"; a = "-" }`), the outcome this unit keeps.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: the age pass's `awk`
- `tools/unattended/unattended.test.sh`: the unsighted arms

`TOOL-dPlacedRequest-46` writes the same two files at the same order, so the two passes run in
sequence.

### Alternatives rejected

- **Treat an unsighted commit as sighted now.** It would read a never-seen take-over as fresh and
  hide a missing feed behind `live`.
- **Refuse the whole `--claims` read on an empty feed.** `TOOL-dPlacedRequest-17` AC6 asks for rows
  printed `unknown`, not a refusal.

## 5. Production-readiness checklist

- security — closes a take-over that an empty or missing feed would permit.
- perf / scale — none: one more test per compare.
- error / empty / loading states — an empty feed prints every lease row `unknown`, age `-`.
- observability — `--claims`' verdict field, unchanged in shape.
- risks — none beyond `TOOL-dPlacedRequest-26` §5's.
- testing — the probes of §6 and the arm in §7.
- migration — none: the walk is new in this build.
- user docs — none: `memory/guides/UNATTENDED-STOPS.md` section 7 states the unsighted rule
  (`TOOL-dPlacedRequest-17` S3).

## 6. Acceptance criteria

The fixture is `TOOL-dPlacedRequest-26`'s: a scratch clone with a bare origin, `RUN_CLAIMS=on`, a
planted feed and `leases.expiry-hours` 24.

- **AC1** — When the feed is emptied under a non-empty cache of lease refs and `--claims` runs, every
  lease row prints `unknown` with age `-`, and none prints `stale`.
  Red when: an unset `seen-utc` is compared with the threshold, the planted case being a scratch copy
  of the driver whose `awk` holds `TOOL-dPlacedRequest-35` §4's test.
- **AC2** — When a two-commit tenure's tip is unsighted and its older `renews: no` commit was sighted
  25 hours ago, `--claims` prints `unknown`.
  Red when: an unsighted tip falls through to an older commit's age.
- **AC3** — When a feed line for the renewing beat carries `-` in its `seen-utc` field and the tip is
  sighted a minute ago with `renews: no`, `--claims` prints `unknown`.
  Red when: the `-` placeholder compares below the threshold and reads `stale`.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 · an emptied feed, an unsighted tip and a `-` sighting over planted chains, staged by a scratch copy whose `awk` compares unguarded · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — What does the walk do with an unsighted commit?** (a) Never compare it; an unsighted tip,
  beat or oldest resolves `unknown`; (b) treat it as sighted now; (c) compare it, as
  `TOOL-dPlacedRequest-35` reads. (c) is the defect; (b) reads a never-seen write as fresh.
  RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the review's fix judged sound.
  widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the spec audit of the round-2 promotions, finding
  33 (HIGH, item H3).
- rev-2 · 2026-10-25 · header above §1 · the round-3 promotions' fix brief: the `**Derived:** PLAY-dClosedLoop-2` line, binding this audit-promoted unit, which carries no clause, to the decision that derives it.
- rev-3 · 2026-10-25 · §3 · the disposal of the spec audit of the round-3 promotions: the hands-off edges to `TOOL-dPlacedRequest-50` and `TOOL-dPlacedRequest-52`, mirroring their consumes-from.
- rev-4 · 2026-10-25 · §3 · the disposal of the spec audit of the round-4 promotions: the hands-off edge to `TOOL-dPlacedRequest-56`, mirroring its consumes-from.

## 10. Reuse audit

The seam extended is `TOOL-dPlacedRequest-35`'s threshold test inside `read_claims`' age `awk`
(`tools/unattended/unattended.sh:2118`), whose existing `unknown` mapping for an unaged row
(`:2181`) is the outcome reused. `python tools/codebase-map/reuse_lookup.py "an unsighted commit in
the age walk reads unknown not stale"` ranked `read`, `read_text`, `note` and `walk`, name stems only.
`python tools/memory-recall/query.py "what does the age walk do with a commit the feed has not
sighted"` returned `TOOL-dPlacedRequest-42`, scout A's row on `TOOL-dPlacedRequest-17`, this audit's
H3 and `TOOL-dPlacedRequest-35`; none disagrees with source.

Recall terms used: unsighted seen-utc feed first sighting unknown stale threshold age walk read_first_seen empty feed
