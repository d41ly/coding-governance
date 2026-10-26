# TOOL-dPlacedRequest-35 — the bounded age walk ends a tail at its tenure before it reads an age

**Status:** DEFERRED · rev-2 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 23 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-35-deviation-351.md](../build/2026-10-25-build-TOOL-dPlacedRequest-35-deviation-351.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-35-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-35-promoted-fix-return.md) | research | TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 |
| [2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md](../build/2026-10-26-build-TOOL-dPlacedRequest-1-agent-ledger.md) | journal | TOOL-dPlacedRequest-1 TOOL-dPlacedRequest-2 TOOL-dPlacedRequest-3 TOOL-dPlacedRequest-4 TOOL-dPlacedRequest-5 TOOL-dPlacedRequest-6 TOOL-dPlacedRequest-7 TOOL-dPlacedRequest-8 TOOL-dPlacedRequest-9 TOOL-dPlacedRequest-10 TOOL-dPlacedRequest-11 TOOL-dPlacedRequest-12 TOOL-dPlacedRequest-13 TOOL-dPlacedRequest-14 TOOL-dPlacedRequest-15 TOOL-dPlacedRequest-16 TOOL-dPlacedRequest-17 TOOL-dPlacedRequest-18 TOOL-dPlacedRequest-19 TOOL-dPlacedRequest-20 TOOL-dPlacedRequest-21 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-26 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-46 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 TOOL-dPlacedRequest-50 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 TOOL-dPlacedRequest-53 TOOL-dPlacedRequest-54 TOOL-dPlacedRequest-55 TOOL-dPlacedRequest-56 TOOL-dPlacedRequest-57 TOOL-dPlacedRequest-58 TOOL-dPlacedRequest-59 TOOL-dPlacedRequest-60 TOOL-dPlacedRequest-61 TOOL-dPlacedRequest-62 TOOL-dPlacedRequest-63 TOOL-dPlacedRequest-64 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-35-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-35-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-43 |
| [2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-36 TOOL-dPlacedRequest-37 TOOL-dPlacedRequest-38 TOOL-dPlacedRequest-39 TOOL-dPlacedRequest-41 TOOL-dPlacedRequest-42 TOOL-dPlacedRequest-40 TOOL-dPlacedRequest-43 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-1 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md`)
confirmed **finding 1 at HIGH**, its item **H2**, which holds no other finding.
`TOOL-dPlacedRequest-34` S43 and its §4 "The bounded walk (S43)" give the age walk three stops (the
renewing beat, the tenure's start, the first commit sighted more than `leases.expiry-hours` ago)
without ordering them, and §4 says an old commit makes the verdict `stale` "whatever lies further
back". `TOOL-dPlacedRequest-26` S1 ends a tenure at the first commit whose epoch differs from the
tip's. In `TOOL-dPlacedRequest-26` AC1's chain, an epoch-2 take-over sighted a minute ago over an
epoch-1 commit sighted 25 hours ago, a walk that tests the threshold first reads the fresh take-over
`stale`, and a second node may take it at once. This unit repairs `TOOL-dPlacedRequest-34`, built at
order 22, so it sits at order 23: the tenure stop is tested first, and an age is only ever read
inside the tip's tenure.

## 2. Scope (IN)

- **S1** — The stop order. The `awk` of the age pass reads each tail tip first, the tip included,
  and for each commit applies, in this order: (1) a commit whose `epoch` differs from the tip's ends
  the tenure, and the commit is read no further, so no threshold test runs on it; (2) a commit inside
  the tenure whose `renews` reads `yes`, or is absent on a legacy claim, is the renewing beat and
  resolves the tail, aged from its first sighting; (3) a commit inside the tenure sighted before the
  threshold resolves the tail `stale`. Observed by AC1 and AC2.
- **S2** — The fallback. A tail whose tenure ends, or whose chain ends, with no renewing commit is
  aged from the oldest commit read inside the tenure, `TOOL-dPlacedRequest-26` S3's rule kept under
  the bounded walk. Observed by AC3.
## 3. Non-goals (OUT)

- No change to which write renews: `TOOL-dPlacedRequest-25`'s.
- No change to the one streaming `git log` or its refs: `TOOL-dPlacedRequest-34` S43's.
- No new verdict: `live`, `stale` and `unknown` keep `TOOL-dPlacedRequest-17`'s meanings.
- The one-commit tenure of `TOOL-dPlacedRequest-26` §4 (the tip not tested) is finding 38's, an item
  of `TOOL-dPlacedRequest-43`; S1 here reads the tip too, so that item observes it over this order.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-34` — S43's bounded streaming walk and its `awk`, whose stops this unit orders; without it there is no bounded walk to order
- **consumes-from** `TOOL-dPlacedRequest-26` — the tenure rule and AC1's take-over chain, which this unit keeps true under the bounded walk; without it there is no tenure stop to put first
- **hands-off** `TOOL-dPlacedRequest-46` — S1's stop order, which that unit extends with a `renews: -` stop ahead of the threshold test
- **hands-off** `TOOL-dPlacedRequest-47` — S1's threshold test and S2's fallback, which that unit guards so an unsighted commit is never compared

## 4. Design

### The walk, per tail

```
git log --first-parent --format='%x01%H%n%B' <cached lease and legacy refs> | awk
  threshold = now - leases.expiry-hours (an ISO string, the feed's seen-utc compared)
  per tail, tip first, tip included:
    tip                         -> tenure epoch = its epoch (absent reads 0)
    epoch != tenure epoch       -> tenure ended: resolve by S2, read this tail no further
    renews yes or absent        -> renewing beat: resolve, age from its sighting
    seen-utc < threshold        -> resolve stale
    else                        -> oldest-of-tenure = this commit, read on
  chain ended                   -> resolve by S2 (age from oldest-of-tenure)
  every tail resolved           -> exit
```

The stale test sits after the epoch test because a commit of an earlier tenure is another holder's,
and its age says nothing about the tip's holder. Within one tenure a parent is sighted no later than
its child on one node, so a commit inside the tenure sighted before the threshold makes the verdict
`stale` for everything within the tenure behind it.

### Evidence

- The age pass and its verdict `awk` live in `read_claims` (`tools/unattended/unattended.sh:2118`,
  the verdict at `:2177-2186` at the pinned base); no walk exists at the base, and
  `TOOL-dPlacedRequest-26` and `TOOL-dPlacedRequest-34` add it.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: the age pass's `awk`
- `tools/unattended/unattended.test.sh`: the stop-order arms

### Alternatives rejected

- **Test the threshold first and re-check the epoch after.** The early exit would already have
  resolved the tail `stale`; the order is the fix.
- **Drop the threshold stop.** The walk would read every commit of a long tenure again, the cost
  finding 60 of round 1 bounded.

## 5. Production-readiness checklist

- security — none: a narrower reading of commits already fetched.
- perf / scale — unchanged: the same streaming walk, which now stops at an epoch change before any
  age test.
- error / empty / loading states — an unsighted tenure start reads `unknown`, as any unsighted record
  does.
- observability — `--claims`' verdict field, unchanged in shape.
- risks — none beyond `TOOL-dPlacedRequest-26` §5's.
- testing — the probes of §6 and the arm in §7.
- migration — none.
- user docs — none: `memory/guides/UNATTENDED-STOPS.md` section 7 already says a lease is aged
  within its holder's tenure (`TOOL-dPlacedRequest-26` S4).

## 6. Acceptance criteria

The fixture is `TOOL-dPlacedRequest-26`'s: a scratch clone with a bare origin, `RUN_CLAIMS=on`, a
planted feed and `leases.expiry-hours` 24.

- **AC1** — When the chain is `TOOL-dPlacedRequest-26` AC1's, an epoch-1 `renews: yes` commit sighted
  25 hours ago under an epoch-2 take-over planted `renews: no` and sighted a minute ago, `--claims`
  prints the row `live`.
  Red when: the threshold is tested before the tenure stop, the planted case being a scratch copy of
  the driver whose `awk` tests `seen-utc` first.
- **AC2** — When the chain is an epoch-2 tip planted `renews: yes` and sighted a minute ago over
  epoch-1 commits sighted 25 hours ago, `--claims` prints `live`.
  Red when: the tip is skipped and an older tenure's commit decides the verdict.
- **AC3** — When the epoch-2 tenure holds two `renews: no` commits and the older is sighted 25 hours
  ago, `--claims` prints `stale`; with both sighted a minute ago, `live`.
  Red when: a tenure with no renewing commit is aged from outside the tenure or never expires.
## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 · the stop-order arms over planted chains and feed lines, staged by a scratch copy whose `awk` tests the threshold first · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — Which stop does the walk test first?** (a) The tenure stop, then the renewing beat, then the
  threshold, all inside the tenure; (b) the threshold first, as S43's list reads; (c) the threshold
  only on the tip. (b) reads a fresh take-over `stale`, the defect finding 1 names; (c) loses the
  early exit for a long tenure. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the review's
  fix judged sound. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the spec audit of the round-1 promotions, finding
  1 (HIGH, item H2).
- rev-2 · 2026-10-25 · §3 · the round-3 spec audit's disposal: the edge mirror hands-off TOOL-dPlacedRequest-46 and TOOL-dPlacedRequest-47.

## 10. Reuse audit

The seam extended is `TOOL-dPlacedRequest-34` S43's streaming walk inside `read_claims`
(`tools/unattended/unattended.sh:2118`, its verdict `awk` at `:2177-2186` at the pinned base), whose
one `git log` and one `awk` this unit keeps; only the order of three tests inside the `awk` changes.
`python tools/codebase-map/reuse_lookup.py "order the stops of a bounded first-parent walk by tenure
before age"` ranked `before`, `walk`, `boundedParallel` and `read_first_commit_date`, name stems only,
none an age walk. `python tools/memory-recall/query.py "how does the bounded age walk order its
stops"` returned `TOOL-dPlacedRequest-26`, `TOOL-dPlacedRequest-34` §4 and scout A's row on the age
machinery; none disagrees with source.

Recall terms used: bounded walk tenure epoch renewing beat threshold expiry-hours stale first-parent awk
