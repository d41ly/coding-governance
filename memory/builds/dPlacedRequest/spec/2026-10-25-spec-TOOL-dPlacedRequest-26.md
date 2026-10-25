# TOOL-dPlacedRequest-26 — the renewing-beat walk stops at the current holder's tenure

**Status:** OPEN · rev-2 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 5 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-23-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-23-promoted-fix-return.md) | research | TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |
| [2026-10-25-build-TOOL-dPlacedRequest-26-deviation-261.md](../build/2026-10-25-build-TOOL-dPlacedRequest-26-deviation-261.md) | deviation | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-23-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |
| [2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-23-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-27 TOOL-dPlacedRequest-23 TOOL-dPlacedRequest-24 TOOL-dPlacedRequest-25 TOOL-dPlacedRequest-28 TOOL-dPlacedRequest-29 TOOL-dPlacedRequest-30 TOOL-dPlacedRequest-31 TOOL-dPlacedRequest-32 TOOL-dPlacedRequest-33 TOOL-dPlacedRequest-34 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of this build, round 1
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-1-spec-audit.md`),
confirmed **finding 1 at HIGH**. It shares item **H1**, "a new holder inherits the previous holder's
renewing beat", with finding 20, which `TOOL-dPlacedRequest-25` closes. `TOOL-dPlacedRequest-17` S2 and
§4 "The age pass" step 2 age a lease from the newest commit whose `renews` is `yes` on its whole
first-parent chain, crossing tenures, and reset nothing at an epoch change; S3 gives no verdict for a
chain with no renewing commit. A take-over over a chain whose last renewing beat is older than
`leases.expiry-hours` therefore reads `stale` the moment it is written, so a second node or the
driver's preflight can take it at once, and two draws can hold one closed root. This unit repairs
`TOOL-dPlacedRequest-17`: the walk reads only the tip's tenure, and a tenure with no renewing commit is
aged from its first commit.

## 2. Scope (IN)

- **S1** — The tenure. A lease row's tenure is the run of commits on its first-parent chain, from the
  tip back, whose `epoch` equals the tip's; the walk of `TOOL-dPlacedRequest-17` §4 step 2 stops at the
  first commit whose `epoch` differs, which belongs to an earlier holder and is never the row's
  renewing beat. A legacy `refs/gov/runs/*` claim carries no `epoch` and reads 0
  (`TOOL-dPlacedRequest-1` S3), so a legacy chain is one tenure and a lease's first commit, at epoch 1
  over a legacy tip, starts a new one. Observed by AC1 and AC4.
- **S2** — The renewing beat within it: the newest commit of the tenure whose `renews` reads `yes`, or
  is absent on a legacy claim; a `renews: -` there keeps `TOOL-dPlacedRequest-17` S3's never-stale rule.
  Observed by AC2.
- **S3** — A tenure with no renewing commit is aged from its first commit, the oldest commit of the
  tenure: its first sighting is the row's renewing age, so the verdict is `live` until
  `leases.expiry-hours` after the new holder's first write and `stale` after, never `unknown` unless the
  feed has not sighted that commit. Observed by AC3.
- **S4** — The stops guide's verdict table (`tools/unattended/STOPS.template.md` section 7, rendered to
  `memory/guides/UNATTENDED-STOPS.md`) states that a lease is aged within its holder's tenure, and the
  S3 rule. Observed by AC5.

## 3. Non-goals (OUT)

- No change to which write renews: the writer's tenure rule is `TOOL-dPlacedRequest-25`'s, and this
  unit is correct with or without it, since S3 ages an unmarked tenure from its start.
- No bound on the walk's cost: the walk still lists every commit of every cached lease, and finding
  60's bound is an item of `TOOL-dPlacedRequest-34`.
- No change to the observer clock, `read_first_seen`, or `check_deadline_passed`:
  `TOOL-dPlacedRequest-17`'s.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-17` — the age pass's walk and verdict `awk` in `read_claims`, which this unit bounds to the tenure; without it there is no renewing-beat walk to bound
- **consumes-from** `TOOL-dPlacedRequest-1` — the `epoch` and `renews` keys of the lease record, which mark the tenure and its renewals; without them a tenure cannot be told from the chain
- **hands-off** `TOOL-dPlacedRequest-34` — the tenure-bounded walk, which that unit's item for finding 60 bounds in cost
- **hands-off** `TOOL-dPlacedRequest-35` — the tenure stop, which that unit tests before any age once the walk is bounded
- **hands-off** `TOOL-dPlacedRequest-43` — the walk's tip, which that unit's item for finding 38 observes as a one-commit tenure

## 4. Design

### The walk, per `gov-claim` tail

```
git log --topo-order --first-parent --format='%x01%H%n%B' <every cached lease and legacy ref>
awk, per tail:
  first commit seen          -> tip; tenure epoch = its epoch (absent reads 0)
  each later commit:
    epoch != tenure epoch    -> tenure ended: stop reading this tail
    renews yes (or absent)   -> renewing beat, if none found yet
    always                   -> oldest-of-tenure = this commit
  end of tail:
    renewing beat found      -> age from it
    none found               -> age from oldest-of-tenure
```

The one `git log` and the one `awk` of `TOOL-dPlacedRequest-17` §4 stay; the change is the stop rule
and the fallback, both inside the `awk`.

### Why the epoch marks the tenure

`TOOL-dPlacedRequest-1` S3 raises the epoch at every take, and `TOOL-dPlacedRequest-16` at the take of
a `released` lease and at a draw; every other write keeps it. A change of holder is therefore always a
change of epoch, and a run of equal epochs is one holder's.

### Files touched (estimate)

- `tools/unattended/unattended.sh`: the age pass's `awk`
- `tools/unattended/unattended.test.sh`: the tenure arms
- `tools/unattended/STOPS.template.md`: section 7's verdict table
- `memory/guides/UNATTENDED-STOPS.md`: its render

### Alternatives rejected

- **Read `unknown` for a tenure with no renewing commit.** `unknown` refuses every taker, so an
  abandoned no-witness lease would be held for ever.
- **Age an unmarked tenure from the tip.** Every beat would then restart the clock, so a holder that
  only beats would never expire, which `TOOL-dPlacedRequest-17` S6 forbids.

## 5. Production-readiness checklist

- security — none: a narrower reading of commits already fetched.
- perf / scale — the same one `git log` and one `awk`; the `awk` stops reading a tail at its tenure.
- error / empty / loading states — an unsighted tenure start reads `unknown`, as any unsighted record
  does.
- observability — `--claims`' fourth and fifth fields, unchanged in shape.
- risks — a holder that re-takes its own lease at a higher epoch starts a new tenure and an age from
  that write.
- testing — the probes of §6 and the arm in §7.
- migration — none.
- user docs — `memory/guides/UNATTENDED-STOPS.md` section 7; no `help/` page covers the kit.

## 6. Acceptance criteria

The fixture is `TOOL-dPlacedRequest-17` AC1's: a scratch clone with a bare origin, `RUN_CLAIMS=on`
and a feed the probe plants.

- **AC1** — When the chain is an epoch-1 `renews: yes` commit sighted 25 hours ago followed by an
  epoch-2 take-over commit planted `renews: no` and sighted a minute ago, `--claims` prints the row
  `live`, and a third session's `--lease take-over build tFix` exits 1 printing `live-holder`.
  Red when: the take-over inherits the earlier tenure's beat and reads `stale`; the planted case is a
  scratch copy of the driver whose walk crosses the epoch change.
- **AC2** — When the chain's epoch-2 tenure holds a `renews: yes` commit sighted 25 hours ago and a
  `renews: no` beat sighted a minute ago, `--claims` prints it `stale`; with that tenure's renewing
  commit sighted a minute ago, `live`.
  Red when: the tenure rule stops a holder's own lease from expiring.
- **AC3** — When the chain's epoch-2 tenure holds two `renews: no` commits and its first is sighted 25
  hours ago, `--claims` prints it `stale`; sighted a minute ago, `live`; with that first commit's feed
  line deleted, `unknown`.
  Red when: a tenure with no renewing commit reads `unknown` while sighted, or never expires.
- **AC4** — When the chain is a legacy `refs/gov/runs/tFix` claim with no `epoch` key, its tip sighted
  a minute ago, `--claims` prints it `live` as `TOOL-dPlacedRequest-17` AC1 does.
  Red when: a legacy chain is split into tenures.
- **AC5** — When `grep -n 'tenure' tools/unattended/STOPS.template.md` runs, a section 7 line says a
  lease is aged within its holder's tenure.
  Red when: the guide omits the rule.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 AC4 · the tenure arms over planted chains and feed lines, staged by a scratch copy whose walk crosses the epoch change · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — What verdict does a tenure with no renewing commit read?** (a) Aged from its first commit;
  (b) `unknown`; (c) `stale` at once. (b) holds an abandoned lease for ever, the consequence finding 1
  names; (c) frees a lease the moment it is taken. RESOLVED (agent, 2026-10-25, delegated): (a), rung
  3, the review's fix judged sound. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the round-1 spec audit's finding 1 (HIGH, item H1,
  shared with finding 20).
- rev-2 · 2026-10-25 · §3 · the spec audit of the round-1 promotions' disposal: the edge mirrors
  hands-off TOOL-dPlacedRequest-35, hands-off TOOL-dPlacedRequest-43.

## 10. Reuse audit

The seam extended is `TOOL-dPlacedRequest-17`'s age pass inside `read_claims`
(`tools/unattended/unattended.sh:2118`, its verdict `awk` at `:2177-2186` at the pinned base), whose one
`git log` and one `awk` this unit keeps; no code for the walk exists at the base. `python
tools/codebase-map/reuse_lookup.py "age a lease from the newest renewing commit of the current
holder"` ranked `build_commit`, `holder`, `resolveLease` and `check_lease_only_diff`, name stems only;
none reads a renewing beat, so the unit this repairs is the seam. `python
tools/memory-recall/query.py "how is a lease aged from its renewing beat"` returned scout A's row 7,
unit 17's §2 and the spec brief's row; none disagrees with the spec.

Recall terms used: renewing beat age pass first-parent walk tenure epoch observer clock expiry-hours stale
