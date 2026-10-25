# TOOL-dPlacedRequest-46 — the bounded age walk stops on a `renews: -` commit before any threshold test

**Status:** OPEN · rev-3 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 24 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-44-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-44-promoted-fix-return.md) | research | TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 |
| [2026-10-25-build-TOOL-dPlacedRequest-46-deviation-461.md](../build/2026-10-25-build-TOOL-dPlacedRequest-46-deviation-461.md) | deviation | — |
| [2026-10-25-prompt-TOOL-dPlacedRequest-44-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-44-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 |
| [2026-10-25-review-TOOL-dPlacedRequest-44-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-44-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-47 TOOL-dPlacedRequest-44 TOOL-dPlacedRequest-45 TOOL-dPlacedRequest-48 TOOL-dPlacedRequest-49 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-2 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-35-spec-audit.md`)
confirmed **finding 32 at HIGH**, its item **H2**, which holds no other finding.
`TOOL-dPlacedRequest-35` S1 and its §4 "The walk, per tail" order three stops: the epoch change, the
renewing beat on `renews` reading `yes` or absent, then `seen-utc < threshold -> stale`. A commit
carrying `renews: -` matches neither of the first two, so it reaches the threshold test. Under
`leases.renewal none` every commit is `renews: -` (`TOOL-dPlacedRequest-25`), so every held lease
reads `stale` after `leases.expiry-hours` and another node may take it over. That contradicts
`TOOL-dPlacedRequest-17` S3 and AC4 (a `renews: -` beat sighted 1,000 hours ago prints `live`) and
`TOOL-dPlacedRequest-26` S2, which keeps that rule inside the tenure. This unit repairs
`TOOL-dPlacedRequest-35`, at order 23, so it sits at order 24: the walk names every class of `renews`
and the `-` class has its own stop ahead of the threshold.

## 2. Scope (IN)

- **S1** — The `-` stop. Inside the tenure, a commit whose `renews` reads `-` resolves the tail by
  `TOOL-dPlacedRequest-17` S3's never-stale rule: `live`, aged from that commit's first sighting, or
  `unknown` with age `-` when the feed has not sighted it. It is tested after the epoch stop and
  before the threshold test, so no `-` commit is ever compared with the threshold. Observed by AC1
  and AC2.
- **S2** — Every class named. The walk's stops cover each value `renews` takes: `yes`, absent on a
  legacy claim, `-`, and `no`, which alone reads on; a value outside the four reads on as `no` does.
  A fixture row runs the walk once per class. Observed by AC3.

## 3. Non-goals (OUT)

- No change to which write sets `renews: -`: `TOOL-dPlacedRequest-25`'s.
- No change to the epoch stop, the renewing beat or the fallback: `TOOL-dPlacedRequest-35` S1 and S2.
- No guard for an unsighted commit at the threshold test: finding 33's, `TOOL-dPlacedRequest-47`.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-35` — S1's stop order inside the age pass's `awk`, which this unit extends with the `-` stop; without it there is no ordered walk to extend
- **hands-off** `TOOL-dPlacedRequest-52` — the walk, S2 and AC3, which that unit's items for findings 9, 35 and 36 merge with `TOOL-dPlacedRequest-47`'s walk and extend with out-of-set rows

## 4. Design

### The walk, per tail

```
per tail, tip first, tip included:
  tip                         -> tenure epoch = its epoch (absent reads 0)
  epoch != tenure epoch       -> tenure ended: resolve by 35 S2
  renews -                    -> resolve never-stale: live from its sighting, unknown if unsighted   (S1)
  renews yes or absent        -> renewing beat: resolve, age from its sighting
  seen-utc < threshold        -> resolve stale
  else                        -> oldest-of-tenure = this commit, read on
```

The `-` stop sits beside the renewing beat because both resolve the tail on the commit's own class;
it sits above the threshold test because a never-expiring lease has no threshold.

### Evidence

- The age pass and its verdict `awk` live in `read_claims` (`tools/unattended/unattended.sh:2118`,
  verdict at `:2177-2186` at the pinned base); the walk is built by `TOOL-dPlacedRequest-26`,
  `TOOL-dPlacedRequest-34` S43 and `TOOL-dPlacedRequest-35`, none present at the base.
- `TOOL-dPlacedRequest-17` S3: "A row whose renewing beat carries `renews: -` (`leases.renewal: none`)
  never reads `stale`".

### Files touched (estimate)

- `tools/unattended/unattended.sh`: the age pass's `awk`
- `tools/unattended/unattended.test.sh`: the class arms

`TOOL-dPlacedRequest-47` writes the same two files at the same order, so the two passes run in
sequence.

### Alternatives rejected

- **Read `-` as a renewing beat and skip the age.** The row would print an age the guide says is a
  first sighting; aging it from its sighting keeps the field's meaning.
- **Skip the threshold test for the whole chain under `none`.** The walk reads the record, not the
  conf, and a chain written partly under another policy carries both classes.

## 5. Production-readiness checklist

- security — closes a take-over of a held lease under `leases.renewal none`.
- perf / scale — none: one more string compare per commit, and the walk now stops at the tip under
  `none`.
- error / empty / loading states — an unsighted `-` commit reads `unknown`.
- observability — `--claims`' verdict field, unchanged in shape.
- risks — none beyond `TOOL-dPlacedRequest-26` §5's.
- testing — the probes of §6 and the arm in §7.
- migration — none: the walk is new in this build.
- user docs — none: `memory/guides/UNATTENDED-STOPS.md` section 7 already states the never-stale
  rule (`TOOL-dPlacedRequest-17` AC7).

## 6. Acceptance criteria

The fixture is `TOOL-dPlacedRequest-26`'s: a scratch clone with a bare origin, `RUN_CLAIMS=on`, a
planted feed and `leases.expiry-hours` 24.

- **AC1** — When a one-tenure chain's tip carries `renews: -` and was sighted 1,000 hours ago,
  `--claims` prints the row `live`.
  Red when: the threshold test runs on a `-` commit, the planted case being a scratch copy of the
  driver whose `awk` holds `TOOL-dPlacedRequest-35` §4's order.
- **AC2** — When the tip carries `renews: no`, sighted a minute ago, over a `renews: -` commit of the
  same epoch sighted 1,000 hours ago, `--claims` prints `live`.
  Red when: a `-` commit below the tip is tested against the threshold.
- **AC3** — When four one-commit tenures whose tips read `renews: yes`, no `renews` key, `renews: -`
  and `renews: no` are each sighted 1,000 hours ago, `--claims` prints them `stale`, `stale`, `live`
  and `stale`.
  Red when: a class of `renews` reaches a stop the walk does not name.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC1 AC2 AC3 · one walk per `renews` class over planted chains and feed lines, staged by a scratch copy whose `awk` holds unit 35's order · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — Where does a `renews: -` commit stop the walk?** (a) Its own stop after the epoch stop and
  before the threshold, resolving never-stale; (b) folded into the renewing beat; (c) no stop, as
  `TOOL-dPlacedRequest-35` reads. (c) is the defect; (b) loses the never-stale verdict at the
  threshold the beat's age is compared with. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3,
  the review's fix judged sound. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the spec audit of the round-2 promotions, finding
  32 (HIGH, item H2).
- rev-2 · 2026-10-25 · header above §1 · the round-3 promotions' fix brief: the `**Derived:** PLAY-dClosedLoop-2` line, binding this audit-promoted unit, which carries no clause, to the decision that derives it.
- rev-3 · 2026-10-25 · §3 · the disposal of the spec audit of the round-3 promotions: the hands-off edge to `TOOL-dPlacedRequest-52`, mirroring its consumes-from.

## 10. Reuse audit

The seam extended is `TOOL-dPlacedRequest-35`'s stop order inside `read_claims`' age `awk`
(`tools/unattended/unattended.sh:2118`, verdict at `:2177-2186` at the pinned base); one stop is added
and the one `awk` kept. `python tools/codebase-map/reuse_lookup.py "a lease walk stop for a renewal
policy that never expires"` ranked `walk`, `load_policy`, `resolveLease` and `build_walk`, name stems
only; `resolveLease` resolves the run lease of the stop hook, not an age. `python
tools/memory-recall/query.py "how does the age walk treat a renews dash commit under renewal none"`
returned scout A's row on `TOOL-dPlacedRequest-17`, this audit's H2, `TOOL-dPlacedRequest-35` §4 and
`TOOL-dPlacedRequest-26`; none disagrees with source.

Recall terms used: renews dash leases.renewal none never stale age walk tenure renewing beat threshold expiry-hours
