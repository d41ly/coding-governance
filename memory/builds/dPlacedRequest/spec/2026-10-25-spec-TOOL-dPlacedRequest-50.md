# TOOL-dPlacedRequest-50 — the sighted guard on the threshold compare has a criterion that reaches it

**Status:** DEFERRED · rev-3 · 2026-10-25 · node a · Tier-2 · base c63aabbb · streams tooling · order 25 · advances TOOL-dPlacedRequest-22

**Derived:** PLAY-dClosedLoop-2

<!-- gen:spec-records -->

| Record | Kind | Also serves |
|---|---|---|
| [2026-10-25-build-TOOL-dPlacedRequest-50-deviation-501.md](../build/2026-10-25-build-TOOL-dPlacedRequest-50-deviation-501.md) | deviation | — |
| [2026-10-25-build-TOOL-dPlacedRequest-50-promoted-fix-return.md](../build/2026-10-25-build-TOOL-dPlacedRequest-50-promoted-fix-return.md) | research | TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 |
| [2026-10-25-prompt-TOOL-dPlacedRequest-50-promoted-fix-brief.md](../prompts/2026-10-25-prompt-TOOL-dPlacedRequest-50-promoted-fix-brief.md) | research | TOOL-dPlacedRequest-34 TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 |
| [2026-10-25-review-TOOL-dPlacedRequest-50-spec-audit.md](../reviews/2026-10-25-review-TOOL-dPlacedRequest-50-spec-audit.md) | spec-audit | TOOL-dPlacedRequest-51 TOOL-dPlacedRequest-52 |

<!-- /gen:spec-records -->

## 1. Goal

The spec audit of the round-3 promotions
(`memory/builds/dPlacedRequest/reviews/2026-10-25-review-TOOL-dPlacedRequest-44-spec-audit.md`)
confirmed **finding 1 at HIGH**, its item **H1**, which holds no other finding.
`TOOL-dPlacedRequest-47` S1 guards the threshold compare so an unsighted commit is never compared,
and says AC1 and AC2 observe it. Neither does. AC1 empties the feed and AC2's tip is unsighted, so
both stop at the unsighted-tip stop before any compare. AC3's commit is a renewing beat, which
resolves before the threshold test, so its `Red when:` cannot happen. A build that adds only the
unsighted-tip stop and leaves the compare unguarded passes all three, and a sighted fresh tip over an
unsighted `renews: no` middle commit then reads `stale` (`"" < threshold`) and can be taken over. This
unit repairs `TOOL-dPlacedRequest-47`, at order 24, so it sits at order 25: S1's own case gets a
criterion whose fixture reaches the guard past every earlier stop, and 47's other criteria become
reachable.

## 2. Scope (IN)

- **S1** — The guard's criterion. `TOOL-dPlacedRequest-47` gains AC4, in place: over three commits of
  one epoch, tip first, a `renews: no` tip sighted a minute ago, a `renews: no` middle commit, and a
  `renews: no` tenure start sighted a minute ago, `--claims` prints `live`. AC4 runs twice, once with
  no feed line for the middle commit and once with a line carrying `-` in its `seen-utc` field. Its
  `Red when:` is the scratch copy of the driver whose `awk` holds the unguarded compare, which prints
  `stale`. 47 S1's "Observed by" names AC4. The case joins 47's arm in
  `tools/unattended/unattended.test.sh`. Observed by AC1.
- **S2** — 47's other criteria reach what they name. 47 AC1's cached refs are pinned to tips whose
  `renews` reads `no`, so the `unknown` comes from the unsighted-tip stop and not from the renewing
  mapping at `tools/unattended/unattended.sh:2181`. 47 AC3's `Red when:` is restated as the beat's
  age arithmetic on `-`: the row prints a numeric age or `stale` where `unknown` with age `-` is
  owed. Both edits are one rev bump of 47 with its §9 line. Observed by AC2.

## 3. Non-goals (OUT)

- No change to the walk or its guard: they are `TOOL-dPlacedRequest-47`'s, built at order 24. This
  unit observes them.
- No shape test on a malformed `seen-utc`: finding 34's item of `TOOL-dPlacedRequest-52`.
- No new bug-class record: `memory/gotchas/fixture-passes-by-finding-nothing.md` already names the
  class the review filed this under, and one more instance adds no class.

### Edges

- **consumes-from** `TOOL-dPlacedRequest-47` — the guarded threshold compare, its arm and AC1 to AC3, which this unit reaches with a new criterion and restates in place; without the guard there is nothing for AC4 to observe
- **hands-off** `TOOL-dPlacedRequest-56` — §4 Files touched, Evidence and Edges, which that unit's items for findings 3, 6 and 15 amend
- **hands-off** `TOOL-dPlacedRequest-61` — §4 Files touched, whose sequence sentence that unit's item for finding 10 fixes word for word

## 4. Design

### The fixture rows

```
row         tip (renews, seen)      middle (renews, seen)     start (renews, seen)    expect
AC4 unset   no, a minute ago        no, no feed line          no, a minute ago         live
AC4 dash    no, a minute ago        no, feed line seen-utc -  no, a minute ago         live
red copy    the same rows, the awk's compare unguarded                                 stale
```

The walk of `TOOL-dPlacedRequest-47` §4 reads the tip: sighted, not a renewing beat, not below the
threshold, so it reads on. The middle commit is unsighted and is never compared, so it reads on. The
start is sighted a minute ago and is the oldest of the tenure, and the chain ends there, so 35 S2's
fallback ages it `live`. The unguarded copy compares the middle's empty or `-` stamp, which sorts below
every ISO stamp, and resolves `stale`. That difference is the guard, observed alone.

### Evidence

- `TOOL-dPlacedRequest-47` S1 (`:33-35`) names AC1 and AC2; its AC1 (`:111-114`), AC2 (`:115-117`)
  and AC3 (`:118-120`) are as the review reads them.
- The verdict `awk` maps an unaged row to `unknown` at `tools/unattended/unattended.sh:2181`,
  `if ($10 != 1 || a == "-") { vd = "unknown"; a = "-" }`, read 2026-10-25.

### Files touched (estimate)

- `tools/unattended/unattended.test.sh`: the AC4 rows in 47's arm
- `memory/builds/dPlacedRequest/spec/2026-10-25-spec-TOOL-dPlacedRequest-47.md`: S1, AC1, AC3, AC4
  and its §9 line

### Alternatives rejected

- **Make AC1's tips sighted.** AC1 is the empty-feed criterion that `TOOL-dPlacedRequest-17` AC6
  asks for, and sighting its tips removes that case.
- **A criterion in this unit only.** The guard is 47's, so its criterion belongs in 47's §6, which
  is where a reader of 47 looks for what observes S1.

## 5. Production-readiness checklist

- security — the criterion that observes a take-over guard.
- perf / scale — two more planted rows in one arm.
- error / empty / loading states — N/A — no runtime path changes.
- observability — the arm prints each row's verdict.
- risks — none: a test row and spec text.
- testing — the probes of §6 and the arm in §7.
- migration — none.
- user docs — none: a criterion.

## 6. Acceptance criteria

The fixture is `TOOL-dPlacedRequest-26`'s: a scratch clone with a bare origin, `RUN_CLAIMS=on`, a
planted feed and `leases.expiry-hours` 24.

- **AC1** — When 47's AC4 rows are planted and `--claims` runs over the built walk, both rows print
  `live`; over the scratch copy whose `awk` reads `seen-utc < threshold` with no sighted test, both
  print `stale`.
  Red when: the two runs print the same verdict, so the rows do not reach the guard.
- **AC2** — When `grep -n -A3 'AC1\*\*' 2026-10-25-spec-TOOL-dPlacedRequest-47.md` and the same for
  `AC3` run, AC1's text names `renews: no` tips and AC3's `Red when:` names the beat's age on `-`,
  and 47 S1 names AC4.
  Red when: a criterion of 47 still names a break its fixture cannot stage.

## 7. Gates

`memory hygiene` · `spec tokens (a spec's own names resolve)` · `unattended kit gate` · `kit epoch (shipped bytes move, the version moves)` · `govkit selfcheck` · `lexicon naming predicates` · `recall floor` · `recall floor arms`

New arm: tools/unattended/unattended.test.sh · covers AC1 · a sighted tip over an unsighted middle commit, with no line and with a `-` line, staged by a scratch copy whose `awk` compares unguarded · waived for this build's landing by README rule 8, so its clean reading is owed with PLAY-dClosedLoop-14

## 8. Open questions

- **F1 — How is 47's guard observed?** (a) A new 47 criterion over a sighted tip and start around an
  unsighted middle, with AC1's tips pinned and AC3's `Red when:` restated; (b) AC1 changed to sighted
  tips; (c) a criterion held in this unit only. (b) loses the empty-feed case; (c) puts 47's
  observation outside 47. RESOLVED (agent, 2026-10-25, delegated): (a), rung 3, the review's fix
  judged sound. widens: none · relaxes: none

## 9. Revision log

- rev-1 · 2026-10-25 · initial draft, promoted from the spec audit of the round-3 promotions, finding
  1 (HIGH, item H1).
- rev-2 · 2026-10-25 · §3 · the disposal of the spec audit of the round-4 promotions: the hands-off edge to `TOOL-dPlacedRequest-56`, mirroring its consumes-from.
- rev-3 · 2026-10-25 · §3 · the disposal of the spec audit of the round-6 promotions: the hands-off edge to `TOOL-dPlacedRequest-61`, mirroring its consumes-from.

## 10. Reuse audit

The seam extended is `TOOL-dPlacedRequest-47`'s arm in `tools/unattended/unattended.test.sh` and its
planted-chain fixture from `TOOL-dPlacedRequest-26`; no product seam is added.
`python tools/codebase-map/reuse_lookup.py "a fixture that reaches a guard past every earlier stop in
the age walk"` ranked `walk`, `fixture` (`tools/unattended/unattended.test.sh` among its files) and
`build_fixture`, name stems only; `fixture` is the suite this unit's rows join. `python
tools/memory-recall/query.py "which criterion observes the sighted guard on the age walk threshold
compare"` returned this audit's H1, `TOOL-dPlacedRequest-47` and `TOOL-dPlacedRequest-46`; none
disagrees with source.

Recall terms used: unsighted seen-utc threshold guard criterion fixture reaches stop renews no tenure start live stale
